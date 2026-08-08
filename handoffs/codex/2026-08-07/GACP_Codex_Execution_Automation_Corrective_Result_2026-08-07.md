# GACP Codex Execution Automation Corrective Result

- Date: 2026-08-07
- Governing handoff commit: `c541149f8b9e0a342e7ff85faf82b1c3f3d18848`
- Branch: `gacp/codex-execution-automation-corrective-20260807`
- Acceptance status: **FAIL / BLOCKED**
- Ready for real migration: **No**

## Executive finding

The corrective implementation resolves the identified configuration and governance-design gaps, and
its deterministic regression suite passes. The required disposable fresh-session acceptance did not
complete because this host's bubblewrap sandbox fails during namespace initialization before any
nested Codex command can run. Two fresh non-interactive sessions surfaced zero manual owner prompts,
but neither could inspect, edit, validate, commit, or push. The handoff's hard pass gate therefore is
not satisfied and no real-migration readiness claim is made.

## Root causes

The previous operational kit automated Git mechanics after an agent had begun work, but did not:

1. provide a current-platform Codex profile for cross-repository bootstrap and routine permissions;
2. make GACP `AGENTS.md` discoverable to a fresh session starting in another repository;
3. separate reusable technical capability from operation-specific owner authority;
4. reconcile bounded phase authorization with older mechanically repeated pre-commit review wording;
5. prevent public manifests from requiring machine-specific absolute checkout paths;
6. require explicit evidence before a runner receipt claimed readiness; or
7. launch fresh Codex sessions and count routine manual prompts.

The remaining execution blocker is host-level: bubblewrap reports namespace/loopback or UID-map
initialization failures. This occurs before repository permissions are evaluated. Auto-review cannot
approve around a sandbox that does not initialize, and danger-full-access is prohibited.

## Implemented correction

- Added `bin/gacp-codex-profile` with read-only inspection, exact rendering, atomic installation,
  strict verification, reversible disablement/enablement, drift refusal, version checks, and
  sanitized public characteristics.
- Added a dedicated user-scope profile overlay using `on-request` plus `auto_review`, a custom
  `:workspace`-derived permission set, the active target plus one GACP backend, protected metadata
  paths, secret-file denies, and a narrow GitHub network allowlist.
- Preserved the user's base `config.toml`; the installed profile is a separate mode-`0600` file.
- Added private cross-repository bootstrap instructions without publishing the machine-local path.
- Reconciled bounded phase authorization with owner gates: explicit scope may cover routine
  interpretation, staging, commit, and branch push, while scope expansion, exceptions, acceptance,
  protected-branch merge, and destructive actions remain genuine owner gates.
- Added `runtime-repository-root` for portable public manifests while retaining runtime repository,
  remote, branch, upstream, baseline, scope, and publication checks.
- Changed readiness from an unconditional runner success value to an explicit validated manifest
  field that defaults to false.
- Added a disposable two-session acceptance harness covering inspect, edit, validation, governed
  result generation, exact staging, commits, normal pushes, remote verification, rerun, and
  idempotence.

## Files changed

- `AGENTS.md`
- `GACP_File_First_Governed_Handoff_Workflow.md`
- `README.md`
- `bin/gacp`
- `bin/gacp-codex-profile`
- `docs/GACP_Codex_Execution_Adapter.md`
- `templates/gacp_operation_manifest.template.json`
- `tests/test_gacp.py`
- `tests/test_gacp_git_actions.py`
- `tests/test_gacp_codex_profile.py`
- `tests/run_codex_execution_acceptance.py`
- `evidence/2026-08-07/codex-execution-acceptance.json`
- this result and its operation manifest

## Configuration preservation and reversibility

Read-only inspection found Codex CLI `0.147.0`, a compatible base configuration, no legacy sandbox
collision, and no permission-name collision. Installation created only the dedicated `gacp` profile;
base configuration was not modified. Exact reinstall is idempotent. Disable and enable are
reversible and refuse unmanaged or drifted files. No danger-full-access setting, approval bypass,
credential, secret, private transcript, or machine-local absolute path is present in published files.

## Validation evidence

- Full deterministic suite: **20/20 PASS**
- Runner/runtime-token regression: **PASS**
- Explicit readiness-default regression: **PASS**
- Profile install/verify/idempotence/disable/enable tests: **PASS**
- Base-config preservation and unmanaged-file refusal tests: **PASS**
- Strict selected-profile load using a supported runtime command: **PASS**
- `git diff --check`: **PASS**
- Disposable fresh-session cross-repository acceptance: **FAIL / BLOCKED**
- Fresh sessions attempted: **2**
- Routine manual prompts observed: **0**
- Disposable target commits/pushes completed: **0**
- Disposable GACP result commits/pushes completed: **0**
- Acceptance evidence: `evidence/2026-08-07/codex-execution-acceptance.json`

The zero prompt count is not promoted to a pass because the sessions could not execute repository
work. The hard requirement is a complete end-to-end run with zero routine manual prompts.

## Risks and limitations

- The installed profile is verified but not accepted for real migration on this host.
- Permission profiles and Auto-review are current Codex capabilities and require retesting after
  material CLI permission-model changes.
- A working Linux sandbox/user-namespace environment is required for the least-privilege profile.
- Relaxing to danger-full-access would hide the blocker by weakening the required safety boundary and
  is not an acceptable remedy.
- Complete Codex session-archive enforcement remains outside this corrective handoff and retains its
  separately documented governance status.

## Recommendation

Do not use the adapter for real migrations yet. Repair or move to a host where Codex's bubblewrap
sandbox can initialize, then rerun:

`python3 tests/run_codex_execution_acceptance.py --evidence evidence/2026-08-07/codex-execution-acceptance.json`

Readiness may change to true only after that fresh-session scenario completes all scoped Git actions,
both remote-ref verifications, the second-session no-op check, and records zero routine manual prompts.

## Commit state and next gate

The corrective branch remained at the authorized baseline while this result was prepared. The
authorized GACP runner publishes the implementation commit followed by its machine-readable receipt
commit; their exact identities and remote verification are recorded in
`handoffs/codex/2026-08-07/GACP_Codex_Execution_Automation_Corrective_Result_2026-08-07.json`.

Next gate: technical sandbox remediation followed by corrective acceptance rerun. After a PASS,
return to the owner for final substantive acceptance. No merge to `main` is authorized.
