#!/usr/bin/env python3
"""Tests for the reversible Codex execution-profile adapter."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ADAPTER = PROJECT_ROOT / "bin" / "gacp-codex-profile"


def command(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class CodexProfileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.home = self.root / "codex-home"
        self.home.mkdir()
        self.repo = self.root / "gacp"
        (self.repo / "bin").mkdir(parents=True)
        (self.repo / "AGENTS.md").write_text("# GACP\n", encoding="utf-8")
        (self.repo / "bin" / "gacp").write_text("# test\n", encoding="utf-8")
        command("git", "init", "-q", self.repo.as_posix())
        self.codex = self.root / "codex"
        self.codex.write_text(
            "#!/usr/bin/env python3\n"
            "import json, sys\n"
            "if '--version' in sys.argv:\n"
            "    print('codex-cli 0.147.0')\n"
            "else:\n"
            "    print(json.dumps({'checks': {'config.load': {'status': 'PASS'}}}))\n",
            encoding="utf-8",
        )
        self.codex.chmod(0o755)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def adapter(self, command_name: str) -> subprocess.CompletedProcess[str]:
        return command(
            sys.executable,
            str(ADAPTER),
            "--codex-home",
            str(self.home),
            "--gacp-repo",
            str(self.repo),
            "--codex-bin",
            str(self.codex),
            command_name,
        )

    def test_install_verify_disable_enable_are_idempotent_and_reversible(self) -> None:
        first = self.adapter("install")
        self.assertEqual(first.returncode, 0, first.stderr)
        profile = self.home / "gacp.config.toml"
        self.assertTrue(profile.is_file())
        self.assertEqual(profile.stat().st_mode & 0o777, 0o600)
        body = profile.read_text(encoding="utf-8")
        self.assertIn('approvals_reviewer = "auto_review"', body)
        self.assertIn('extends = ":workspace"', body)
        self.assertNotIn("danger-full-access", body)
        second = self.adapter("install")
        self.assertEqual(json.loads(second.stdout)["action"], "already-current")
        verified = self.adapter("verify")
        self.assertEqual(verified.returncode, 0, verified.stderr)
        self.assertEqual(json.loads(verified.stdout)["strict_config"], "PASS")
        self.assertEqual(json.loads(self.adapter("disable").stdout)["action"], "disabled")
        self.assertEqual(json.loads(self.adapter("disable").stdout)["action"], "already-disabled")
        self.assertEqual(json.loads(self.adapter("enable").stdout)["action"], "enabled")
        self.assertEqual(json.loads(self.adapter("enable").stdout)["action"], "already-enabled")

    def test_base_config_is_preserved_and_legacy_conflict_stops(self) -> None:
        original = 'model = "example"\nsandbox_mode = "workspace-write"\n'
        base = self.home / "config.toml"
        base.write_text(original, encoding="utf-8")
        result = self.adapter("install")
        self.assertEqual(result.returncode, 2)
        self.assertIn("legacy sandbox settings", result.stderr)
        self.assertEqual(base.read_text(encoding="utf-8"), original)
        self.assertFalse((self.home / "gacp.config.toml").exists())

    def test_non_managed_profile_is_never_overwritten(self) -> None:
        profile = self.home / "gacp.config.toml"
        profile.write_text("# owner file\n", encoding="utf-8")
        result = self.adapter("install")
        self.assertEqual(result.returncode, 2)
        self.assertIn("non-GACP profile", result.stderr)
        self.assertEqual(profile.read_text(encoding="utf-8"), "# owner file\n")

    def test_inspection_is_sanitized(self) -> None:
        result = self.adapter("inspect")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["profile_state"], "absent")
        self.assertFalse(report["characteristics"]["danger_full_access"])
        self.assertNotIn(str(self.root), result.stdout)


if __name__ == "__main__":
    unittest.main()
