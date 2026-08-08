from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GACP = PROJECT_ROOT / "bin" / "gacp"


def command(*args: str, cwd: Path, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [*args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        raise AssertionError(
            f"command failed: {' '.join(args)}\nstdout={result.stdout}\nstderr={result.stderr}"
        )
    return result


class GovernedGitActionsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="gacp-git-actions-")
        self.root = Path(self.temp.name)
        self.remote = self.root / "example" / "project.git"
        self.remote.parent.mkdir()
        command("git", "init", "--bare", str(self.remote), cwd=self.root)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        command("git", "init", "-b", "test", cwd=self.repo)
        command("git", "config", "user.name", "GACP Test", cwd=self.repo)
        command("git", "config", "user.email", "gacp-test@example.invalid", cwd=self.repo)
        (self.repo / "approved.md").write_text("approved\n", encoding="utf-8", newline="\n")
        command("git", "add", "approved.md", cwd=self.repo)
        command("git", "commit", "-m", "baseline", cwd=self.repo)
        self.base = command("git", "rev-parse", "HEAD", cwd=self.repo).stdout.strip()
        command("git", "remote", "add", "origin", self.remote.as_uri(), cwd=self.repo)
        command("git", "push", "-u", "origin", "test", cwd=self.repo)
        self.manifest_path = self.repo / "operation.json"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_manifest(
        self,
        *,
        actions: list[str],
        candidate_paths: list[str] | None = None,
        publication_authorized: bool = False,
    ) -> dict[str, object]:
        artifact = self.repo / "approved.md"
        manifest: dict[str, object] = {
            "protocol": "GACP",
            "manifest_version": "1.0",
            "operation_id": "governed-git-action-test",
            "created_at": "2026-08-07T00:00:00Z",
            "source_environment": "disposable-unit-test",
            "destination": {
                "project": "Test",
                "repository": "example/project",
                "local_path": str(self.repo),
                "remote": "origin",
                "branch": "test",
                "upstream": "origin/test",
            },
            "scope": {
                "allowed_actions": actions,
                "allowed_paths": [
                    "approved.md",
                    "candidate.txt",
                    "operation.json",
                    "receipts",
                ],
                "candidate_paths": candidate_paths or [],
                "excluded_paths": ["excluded"],
                "base_commit": self.base,
            },
            "execution": {
                "commit_message": "Apply authorized candidate",
                "receipt_commit_message": "Add governed result receipt",
                "require_candidate_changes": True,
            },
            "artifacts": [
                {
                    "path": "approved.md",
                    "role": "protected test artifact",
                    "integration_mode": "exact-content",
                    "destination_path": "approved.md",
                    "media_type": "text/markdown",
                    "bytes": artifact.stat().st_size,
                    "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
                    "approval_status": "approved",
                    "approval_reference": "test authorization",
                    "dependencies": [],
                }
            ],
            "sensitivity": {
                "classification": "public",
                "public_repository": True,
                "publication_authorized": publication_authorized,
            },
            "validation": {
                "require_clean_tracked": True,
                "allow_untracked_paths": ["operation.json"],
                "protected_files": [
                    {
                        "path": "approved.md",
                        "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
                    }
                ],
            },
            "authorization": {
                "start_authorized": True,
                "authorized_by": "test-owner",
                "approval_reference": "test authorization",
                "current_gate": "acceptance",
            },
            "result": {"receipt_path": "receipts/result.json"},
        }
        self.manifest_path.write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
        return manifest

    def gacp(self, *args: str) -> subprocess.CompletedProcess[str]:
        return command("python3", str(GACP), *args, cwd=self.repo, check=False)

    def head(self) -> str:
        return command("git", "rev-parse", "HEAD", cwd=self.repo).stdout.strip()

    def remote_head(self) -> str:
        result = command(
            "git", "ls-remote", "--heads", "origin", "refs/heads/test", cwd=self.repo
        ).stdout
        return result.split()[0]

    def test_validate_only_run_is_non_mutating(self) -> None:
        self.write_manifest(actions=["inspect", "validate"])
        before_status = command("git", "status", "--porcelain=v1", cwd=self.repo).stdout
        result = self.gacp("run", "operation.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.head(), self.base)
        self.assertEqual(self.remote_head(), self.base)
        self.assertEqual(command("git", "status", "--porcelain=v1", cwd=self.repo).stdout, before_status)
        self.assertFalse((self.repo / "receipts" / "result.json").exists())
        output = json.loads(result.stdout)
        self.assertEqual(output["actions"]["commit"], "not-authorized")

    def test_incoherent_or_unauthorized_git_actions_stop(self) -> None:
        (self.repo / "candidate.txt").write_text("candidate\n", encoding="utf-8")
        self.write_manifest(actions=["inspect", "validate", "commit"], candidate_paths=["candidate.txt"])
        result = self.gacp("validate-manifest", "operation.json")
        self.assertEqual(result.returncode, 2)
        self.assertIn("commit authorization requires stage authorization", result.stderr)
        self.assertEqual(self.head(), self.base)

    def test_stage_is_exact_and_unexpected_work_stops(self) -> None:
        (self.repo / "candidate.txt").write_text("candidate\n", encoding="utf-8")
        (self.repo / "unexpected.txt").write_text("unexpected\n", encoding="utf-8")
        self.write_manifest(actions=["inspect", "validate", "stage"], candidate_paths=["candidate.txt"])
        stopped = self.gacp("run", "operation.json")
        self.assertEqual(stopped.returncode, 2)
        self.assertIn("unexpected pre-existing work", stopped.stderr)
        self.assertEqual(command("git", "diff", "--cached", "--name-only", cwd=self.repo).stdout, "")
        (self.repo / "unexpected.txt").unlink()
        passed = self.gacp("run", "operation.json")
        self.assertEqual(passed.returncode, 0, passed.stderr)
        self.assertEqual(
            command("git", "diff", "--cached", "--name-only", cwd=self.repo).stdout.strip(),
            "candidate.txt",
        )
        self.assertEqual(self.head(), self.base)

    def test_commit_has_explicit_message_parent_and_scope(self) -> None:
        (self.repo / "candidate.txt").write_text("candidate\n", encoding="utf-8")
        self.write_manifest(
            actions=["inspect", "validate", "stage", "commit"],
            candidate_paths=["candidate.txt"],
        )
        result = self.gacp("run", "operation.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        implementation = self.head()
        self.assertEqual(command("git", "rev-parse", "HEAD^", cwd=self.repo).stdout.strip(), self.base)
        self.assertEqual(
            command("git", "show", "-s", "--format=%s", "HEAD", cwd=self.repo).stdout.strip(),
            "Apply authorized candidate",
        )
        self.assertEqual(
            command(
                "git", "diff-tree", "--no-commit-id", "--name-only", "-r", implementation, cwd=self.repo
            ).stdout.strip(),
            "candidate.txt",
        )
        receipt = json.loads(result.stdout)
        self.assertEqual(receipt["repository"]["implementation_commit"], implementation)
        self.assertEqual(receipt["publication"]["implementation_push"], "not-authorized")
        self.assertFalse(receipt["ready_for_real_migration"])
        self.assertEqual(self.remote_head(), self.base)

    def test_push_and_receipt_are_verified_end_to_end(self) -> None:
        (self.repo / "candidate.txt").write_text("candidate\n", encoding="utf-8")
        self.write_manifest(
            actions=["inspect", "validate", "generate", "write", "stage", "commit", "push"],
            candidate_paths=["candidate.txt"],
            publication_authorized=True,
        )
        result = self.gacp("run", "operation.json")
        self.assertEqual(result.returncode, 0, result.stderr)
        output = json.loads(result.stdout)
        receipt_path = self.repo / "receipts" / "result.json"
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        implementation = receipt["repository"]["implementation_commit"]
        receipt_commit = self.head()
        self.assertEqual(output["implementation_commit"], implementation)
        self.assertEqual(output["receipt_commit"], receipt_commit)
        self.assertEqual(output["push"], "performed-and-verified")
        self.assertEqual(receipt["repository"]["implementation_parent"], self.base)
        self.assertEqual(receipt["action_outcomes"]["push"], "performed-and-verified")
        self.assertEqual(receipt["publication"]["implementation_push"], f"verified:{implementation}")
        self.assertFalse(receipt["ready_for_real_migration"])
        self.assertEqual(self.remote_head(), receipt_commit)
        self.assertEqual(command("git", "rev-parse", f"{implementation}^", cwd=self.repo).stdout.strip(), self.base)
        self.assertEqual(command("git", "rev-parse", "HEAD^", cwd=self.repo).stdout.strip(), implementation)
        self.assertEqual(
            command(
                "git", "diff-tree", "--no-commit-id", "--name-only", "-r", implementation, cwd=self.repo
            ).stdout.strip(),
            "candidate.txt",
        )
        self.assertEqual(
            command(
                "git", "diff-tree", "--no-commit-id", "--name-only", "-r", receipt_commit, cwd=self.repo
            ).stdout.strip(),
            "receipts/result.json",
        )
        validated = self.gacp("validate-receipt", "receipts/result.json")
        self.assertEqual(validated.returncode, 0, validated.stderr)

    def test_non_fast_forward_remote_divergence_stops_before_mutation(self) -> None:
        self.write_manifest(
            actions=["inspect", "validate", "stage", "commit", "push"],
            candidate_paths=["candidate.txt"],
            publication_authorized=True,
        )
        other = self.root / "other"
        command("git", "clone", "--branch", "test", self.remote.as_uri(), str(other), cwd=self.root)
        command("git", "config", "user.name", "Other Test", cwd=other)
        command("git", "config", "user.email", "other@example.invalid", cwd=other)
        (other / "advance.txt").write_text("advance\n", encoding="utf-8")
        command("git", "add", "advance.txt", cwd=other)
        command("git", "commit", "-m", "advance remote", cwd=other)
        command("git", "push", "origin", "test", cwd=other)
        (self.repo / "candidate.txt").write_text("candidate\n", encoding="utf-8")
        result = self.gacp("run", "operation.json")
        self.assertEqual(result.returncode, 2)
        self.assertIn("publication base mismatch", result.stderr)
        self.assertEqual(self.head(), self.base)
        self.assertEqual(command("git", "diff", "--cached", "--name-only", cwd=self.repo).stdout, "")

    def test_protected_and_sensitive_content_stop_before_staging(self) -> None:
        self.write_manifest(actions=["inspect", "validate", "stage"], candidate_paths=["approved.md"])
        (self.repo / "approved.md").write_text("changed\n", encoding="utf-8")
        protected = self.gacp("run", "operation.json")
        self.assertEqual(protected.returncode, 2)
        self.assertIn("protected file SHA-256 mismatch", protected.stderr)
        command("git", "restore", "approved.md", cwd=self.repo)
        (self.repo / "candidate.txt").write_text("ghp_" + "A" * 24 + "\n", encoding="utf-8")
        self.write_manifest(actions=["inspect", "validate", "stage"], candidate_paths=["candidate.txt"])
        sensitive = self.gacp("run", "operation.json")
        self.assertEqual(sensitive.returncode, 2)
        self.assertIn("public-safety scan failed", sensitive.stderr)
        self.assertEqual(command("git", "diff", "--cached", "--name-only", cwd=self.repo).stdout, "")

    def test_branch_mismatch_stops(self) -> None:
        (self.repo / "candidate.txt").write_text("candidate\n", encoding="utf-8")
        manifest = self.write_manifest(actions=["inspect", "validate", "stage"], candidate_paths=["candidate.txt"])
        manifest["destination"]["branch"] = "wrong"  # type: ignore[index]
        self.manifest_path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")
        result = self.gacp("run", "operation.json")
        self.assertEqual(result.returncode, 2)
        self.assertIn("branch mismatch", result.stderr)
        self.assertEqual(self.head(), self.base)

    def test_duplicate_invocation_stops_without_duplicate_commit(self) -> None:
        (self.repo / "candidate.txt").write_text("candidate\n", encoding="utf-8")
        self.write_manifest(
            actions=["inspect", "validate", "generate", "write", "stage", "commit", "push"],
            candidate_paths=["candidate.txt"],
            publication_authorized=True,
        )
        first = self.gacp("run", "operation.json")
        self.assertEqual(first.returncode, 0, first.stderr)
        completed_head = self.head()
        second = self.gacp("run", "operation.json")
        self.assertEqual(second.returncode, 2)
        self.assertIn("mutation base mismatch", second.stderr)
        self.assertEqual(self.head(), completed_head)
        self.assertEqual(self.remote_head(), completed_head)


if __name__ == "__main__":
    unittest.main()
