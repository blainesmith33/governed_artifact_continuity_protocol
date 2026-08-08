#!/usr/bin/env python3
"""Run a disposable, fresh-session, cross-repository GACP acceptance scenario."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ADAPTER = PROJECT_ROOT / "bin" / "gacp-codex-profile"


def run(
    *args: str,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
    timeout: int = 60,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=cwd,
        env=env,
        stdin=subprocess.DEVNULL,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=timeout,
    )


def git(repo: Path, *args: str) -> str:
    result = run("git", *args, cwd=repo)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def initialize_repository(path: Path, branch: str, files: dict[str, str]) -> tuple[str, Path]:
    path.mkdir(parents=True)
    remote = path / "remote-store"
    run("git", "init", "--bare", "-q", str(remote))
    run("git", "init", "-q", "-b", branch, str(path))
    git(path, "config", "user.name", "GACP Acceptance")
    git(path, "config", "user.email", "gacp-acceptance@example.invalid")
    for relative, body in files.items():
        target = path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8", newline="\n")
    git(path, "add", *files.keys())
    git(path, "commit", "-m", "Acceptance baseline")
    git(path, "remote", "add", "origin", str(remote))
    git(path, "push", "-u", "origin", branch)
    return git(path, "rev-parse", "HEAD"), remote


def event_types(stdout: str) -> list[str]:
    found: set[str] = set()
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and isinstance(event.get("type"), str):
            found.add(event["type"])
    return sorted(found)


def session(
    profile: str, target: Path, handoff: Path, codex_binary: str
) -> dict[str, Any]:
    prompt = (
        "Execute the authorized GACP acceptance handoff at "
        f"{handoff}. Read the configured GACP AGENTS.md completely first. "
        "Do not ask the owner to relay content; use the two Git repositories and return only a compact receipt."
    )
    started = dt.datetime.now(dt.timezone.utc)
    try:
        result = run(
            codex_binary,
            "--strict-config",
            "--profile",
            profile,
            "exec",
            "--ephemeral",
            "--json",
            "-C",
            str(target),
            prompt,
            timeout=300,
        )
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        result = subprocess.CompletedProcess(exc.cmd, 124, exc.stdout or "", exc.stderr or "")
        timed_out = True
    return {
        "returncode": result.returncode,
        "timed_out": timed_out,
        "interactive_tty": False,
        "stdin": "DEVNULL",
        "manual_prompt_count": 0,
        "event_types": event_types(result.stdout),
        "duration_seconds": round((dt.datetime.now(dt.timezone.utc) - started).total_seconds(), 3),
        "_stderr": result.stderr,
        "_stdout": result.stdout,
    }


def changed_files(repo: Path, commit: str) -> list[str]:
    output = git(repo, "diff-tree", "--no-commit-id", "--name-only", "-r", commit)
    return output.splitlines() if output else []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--codex-bin", default=shutil.which("codex") or "codex")
    args = parser.parse_args()
    evidence_path = Path(args.evidence).resolve()
    profile_name = f"gacp-acceptance-{os.getpid()}"
    failures: list[str] = []
    sessions: list[dict[str, Any]] = []
    installed_profile: Path | None = None

    with tempfile.TemporaryDirectory(prefix="gacp-codex-acceptance-") as temporary:
        root = Path(temporary)
        target = root / "target"
        gacp = root / "gacp"
        target_base, _ = initialize_repository(
            target,
            "acceptance",
            {
                ".gitignore": "remote-store/\n",
                "value.txt": "before\n",
                "verify.py": (
                    "from pathlib import Path\n"
                    "assert Path('value.txt').read_text(encoding='utf-8') == 'after\\n'\n"
                    "print('PASS')\n"
                ),
            },
        )
        gacp_files = {
            ".gitignore": "remote-store/\n",
            "AGENTS.md": (PROJECT_ROOT / "AGENTS.md").read_text(encoding="utf-8"),
            "bin/gacp": (PROJECT_ROOT / "bin" / "gacp").read_text(encoding="utf-8"),
            "handoff.md": "",
        }
        gacp_base, _ = initialize_repository(gacp, "acceptance", gacp_files)
        handoff = gacp / "handoff.md"
        handoff.write_text(
            "# Disposable GACP Codex execution acceptance\n\n"
            "Owner authorization covers this complete bounded phase: inspect, edit, validate, exact stage, "
            "commit, and normal push in both disposable repositories. No merge, force push, deletion, "
            "destructive action, network publication, scope expansion, or owner prompt is authorized.\n\n"
            "Target repository actions:\n"
            "1. Confirm branch `acceptance`, clean tracked/index state, and origin.\n"
            "2. Change only `value.txt` from `before` to `after`.\n"
            "3. Run `python3 verify.py` and `git diff --check`.\n"
            "4. Stage exactly `value.txt`, commit with subject `Acceptance: update target`, and perform a "
            "normal push to `origin acceptance`; verify local and remote identities.\n\n"
            "GACP backend actions:\n"
            "1. Create only `result.json` containing JSON keys `status` = `PASS`, "
            "`target_commit` = the full target commit, and `validation` = `PASS`.\n"
            "2. Validate JSON, stage exactly `result.json`, commit with subject "
            "`Acceptance: add governed result`, and perform a normal push to `origin acceptance`; verify refs.\n\n"
            "Idempotence: if both repositories already contain these exact committed and pushed results, "
            "validate them and exit without editing, committing, or pushing. Stop on any mismatch or ambiguity.\n",
            encoding="utf-8",
            newline="\n",
        )
        git(gacp, "add", "handoff.md")
        git(gacp, "commit", "-m", "Add acceptance handoff")
        git(gacp, "push", "origin", "acceptance")
        gacp_base = git(gacp, "rev-parse", "HEAD")

        install = run(
            sys.executable,
            str(ADAPTER),
            "--profile-name",
            profile_name,
            "--gacp-repo",
            str(gacp),
            "--codex-bin",
            args.codex_bin,
            "install",
        )
        if install.returncode:
            failures.append("profile-install")
        else:
            codex_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).resolve()
            installed_profile = codex_home / f"{profile_name}.config.toml"
            verify = run(
                sys.executable,
                str(ADAPTER),
                "--profile-name",
                profile_name,
                "--gacp-repo",
                str(gacp),
                "--codex-bin",
                args.codex_bin,
                "verify",
            )
            if verify.returncode:
                failures.append("profile-verify")

        if not failures:
            first = session(profile_name, target, handoff, args.codex_bin)
            sessions.append(first)
            if first["returncode"]:
                failures.append("first-session")
            target_after_first = git(target, "rev-parse", "HEAD")
            gacp_after_first = git(gacp, "rev-parse", "HEAD")
            if target_after_first == target_base:
                failures.append("target-commit-missing")
            if gacp_after_first == gacp_base:
                failures.append("gacp-receipt-commit-missing")
            if changed_files(target, target_after_first) != ["value.txt"]:
                failures.append("target-scope")
            if changed_files(gacp, gacp_after_first) != ["result.json"]:
                failures.append("gacp-scope")
            if git(target, "rev-parse", "origin/acceptance") != target_after_first:
                failures.append("target-push")
            if git(gacp, "rev-parse", "origin/acceptance") != gacp_after_first:
                failures.append("gacp-push")
            verifier = run("python3", "verify.py", cwd=target)
            if verifier.returncode:
                failures.append("target-validation")
            try:
                receipt = json.loads((gacp / "result.json").read_text(encoding="utf-8"))
                if (
                    receipt.get("status") != "PASS"
                    or receipt.get("validation") != "PASS"
                    or receipt.get("target_commit") != target_after_first
                ):
                    failures.append("result-receipt")
            except (OSError, json.JSONDecodeError):
                failures.append("result-receipt")

            before_rerun = (target_after_first, gacp_after_first)
            second = session(profile_name, target, handoff, args.codex_bin)
            sessions.append(second)
            if second["returncode"]:
                failures.append("rerun-session")
            after_rerun = (git(target, "rev-parse", "HEAD"), git(gacp, "rev-parse", "HEAD"))
            if after_rerun != before_rerun:
                failures.append("rerun-not-idempotent")
            if git(target, "status", "--porcelain=v1") or git(gacp, "status", "--porcelain=v1"):
                failures.append("final-worktree")

        if failures:
            for index, item in enumerate(sessions, start=1):
                if item["_stderr"]:
                    print(f"session {index} stderr tail:\n{item['_stderr'][-2000:]}", file=sys.stderr)
                if item["_stdout"]:
                    print(f"session {index} event tail:\n{item['_stdout'][-6000:]}", file=sys.stderr)

        if installed_profile and installed_profile.exists():
            body = installed_profile.read_text(encoding="utf-8")
            if body.startswith("# Managed by GACP Codex execution adapter v1\n"):
                installed_profile.unlink()
            else:
                failures.append("profile-cleanup-refused")

        public_sessions = [
            {key: value for key, value in item.items() if not key.startswith("_")} for item in sessions
        ]
        sandbox_initialization_failed = any(
            "bwrap:" in (item["_stderr"] + item["_stdout"]) for item in sessions
        )
        evidence = {
            "schema_version": "1.0",
            "scenario": "disposable-fresh-session-cross-repository",
            "status": "PASS" if not failures else "FAIL",
            "fresh_sessions": len(sessions),
            "routine_manual_prompt_count": sum(
                item["manual_prompt_count"] for item in public_sessions
            ),
            "profile": {
                "approval_policy": "on-request",
                "approvals_reviewer": "auto_review",
                "permission_base": ":workspace",
                "danger_full_access": False,
                "base_config_modified": False,
                "temporary_profile_removed": bool(installed_profile and not installed_profile.exists()),
            },
            "coverage": [
                "inspect",
                "edit",
                "validate",
                "governed-result",
                "exact-stage",
                "commit",
                "normal-push",
                "remote-ref-verification",
                "fresh-session-rerun",
                "idempotence",
            ],
            "sessions": public_sessions,
            "failures": sorted(set(failures)),
            "blocker": (
                "host-bubblewrap-sandbox-initialization"
                if sandbox_initialization_failed
                else None
            ),
        }
        evidence_path.parent.mkdir(parents=True, exist_ok=True)
        evidence_path.write_text(
            json.dumps(evidence, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(json.dumps(evidence, indent=2, sort_keys=True))
        return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
