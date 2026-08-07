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
        raise AssertionError(f"command failed: {' '.join(args)}\nstdout={result.stdout}\nstderr={result.stderr}")
    return result


class GACPTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="gacp-test-")
        self.repo = Path(self.temp.name) / "repo"
        self.repo.mkdir()
        command("git", "init", "-b", "test", cwd=self.repo)
        command("git", "config", "user.name", "GACP Test", cwd=self.repo)
        command("git", "config", "user.email", "gacp-test@example.invalid", cwd=self.repo)
        (self.repo / "approved.md").write_text("approved\n", encoding="utf-8", newline="\n")
        command("git", "add", "approved.md", cwd=self.repo)
        command("git", "commit", "-m", "baseline", cwd=self.repo)
        self.base = command("git", "rev-parse", "HEAD", cwd=self.repo).stdout.strip()
        command("git", "remote", "add", "origin", "https://github.com/example/project.git", cwd=self.repo)
        command("git", "update-ref", "refs/remotes/origin/test", self.base, cwd=self.repo)
        command("git", "branch", "--set-upstream-to", "origin/test", cwd=self.repo)
        self.manifest_path = self.repo / "operation.json"
        self.write_manifest()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_manifest(self, **updates: object) -> dict[str, object]:
        artifact = self.repo / "approved.md"
        manifest: dict[str, object] = {
            "protocol": "GACP",
            "manifest_version": "1.0",
            "operation_id": "test-operation",
            "created_at": "2026-08-07T00:00:00Z",
            "source_environment": "unit-test",
            "destination": {
                "project": "Test",
                "repository": "example/project",
                "local_path": str(self.repo),
                "remote": "origin",
                "branch": "test",
                "upstream": "origin/test",
            },
            "scope": {
                "allowed_actions": ["inspect", "validate"],
                "allowed_paths": ["approved.md", "operation.json", "receipts"],
                "excluded_paths": ["excluded"],
                "base_commit": self.base,
            },
            "artifacts": [
                {
                    "path": "approved.md",
                    "role": "test artifact",
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
                "publication_authorized": False,
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
        manifest.update(updates)
        self.manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8", newline="\n")
        return manifest

    def gacp(self, *args: str) -> subprocess.CompletedProcess[str]:
        return command("python3", str(GACP), *args, cwd=self.repo, check=False)

    def test_valid_manifest_and_preflight_pass(self) -> None:
        self.assertEqual(self.gacp("validate-manifest", str(self.manifest_path)).returncode, 0)
        result = self.gacp("preflight", str(self.manifest_path))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"status": "PASS"', result.stdout)

    def test_missing_start_authorization_stops(self) -> None:
        manifest = self.write_manifest()
        manifest["authorization"]["start_authorized"] = False  # type: ignore[index]
        self.manifest_path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")
        result = self.gacp("validate-manifest", str(self.manifest_path))
        self.assertEqual(result.returncode, 2)
        self.assertIn("start authorization is not granted", result.stderr)

    def test_protected_hash_mismatch_stops(self) -> None:
        manifest = self.write_manifest()
        manifest["validation"]["protected_files"][0]["sha256"] = "0" * 64  # type: ignore[index]
        self.manifest_path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")
        result = self.gacp("preflight", str(self.manifest_path))
        self.assertEqual(result.returncode, 2)
        self.assertIn("protected file SHA-256 mismatch", result.stderr)

    def test_out_of_scope_and_sensitive_files_stop(self) -> None:
        (self.repo / "unexpected.txt").write_text("unexpected\n", encoding="utf-8")
        result = self.gacp("verify", str(self.manifest_path))
        self.assertEqual(result.returncode, 2)
        self.assertIn("out-of-scope paths changed", result.stderr)
        (self.repo / "unexpected.txt").unlink()
        receipts = self.repo / "receipts"
        receipts.mkdir()
        (receipts / "sensitive.txt").write_text("ghp_" + "A" * 24 + "\n", encoding="utf-8")
        result = self.gacp("verify", str(self.manifest_path))
        self.assertEqual(result.returncode, 2)
        self.assertIn("public-safety scan failed", result.stderr)

    def test_compact_validate_only_run_does_not_write(self) -> None:
        before = command("git", "rev-parse", "HEAD", cwd=self.repo).stdout.strip()
        result = self.gacp("run", str(self.manifest_path))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(command("git", "rev-parse", "HEAD", cwd=self.repo).stdout.strip(), before)
        self.assertFalse((self.repo / "receipts" / "result.json").exists())
        attempted_write = self.gacp("run", str(self.manifest_path), "--receipt", "receipts/result.json")
        self.assertEqual(attempted_write.returncode, 2)
        self.assertIn("validation-only run is non-mutating", attempted_write.stderr)


if __name__ == "__main__":
    unittest.main()
