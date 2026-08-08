# GACP Codex Sandbox Host Diagnostic Handoff

- Date: 2026-08-07
- Repository: `blainesmith33/governed_artifact_continuity_protocol`
- Branch: `gacp/codex-execution-automation-corrective-20260807`
- Predecessor result commit: `85973f1e01373e3438e801d9eadde59231b3700e`
- Corrective implementation commit: `16671dac00bf52209379633d16d1080ffd832655`
- Authority: continuation of the owner-authorized GACP execution-automation correction, limited here to non-destructive host diagnosis
- Publication: result/evidence may be committed and normally pushed only to this corrective branch
- Merge authorization: **not granted**

## Purpose

Determine why the required fresh-session Codex acceptance test is blocked by bubblewrap initialization on the owner's Ubuntu host, without weakening security or changing host configuration.

The predecessor corrective implementation remains **FAIL / BLOCKED** for end-to-end acceptance and `ready_for_real_migration: false`. Do not promote readiness on the basis of zero observed prompts because repository execution did not begin.

## Mandatory bootstrap

1. Retrieve this commit and verify the repository/branch identity.
2. Read root `AGENTS.md` completely.
3. Read:
   - `handoffs/codex/2026-08-07/GACP_Codex_Execution_Automation_Corrective_Result_2026-08-07.md`
   - `handoffs/codex/2026-08-07/GACP_Codex_Execution_Automation_Corrective_Result_2026-08-07.json`
   - `evidence/2026-08-07/codex-execution-acceptance.json`
   - `docs/GACP_Codex_Execution_Adapter.md`
4. Preserve the existing corrective implementation and evidence. Do not rewrite the prior result to make it pass.

## Diagnostic scope

Perform only read-only or ephemeral diagnostics necessary to identify the sandbox initialization failure. Capture sanitized evidence sufficient for ChatGPT and the owner to understand the actual host condition.

At minimum determine:

- OS/distribution/release and kernel identity relevant to Linux sandboxing.
- Codex CLI version and the `bwrap` executable Codex resolves.
- Whether the Ubuntu/Debian `bubblewrap`, `apparmor`, `apparmor-profiles`, and `apparmor-utils` packages are installed, including versions when present.
- Whether AppArmor is enabled/loaded.
- Values or availability of relevant namespace controls, including `kernel.apparmor_restrict_unprivileged_userns`, `kernel.unprivileged_userns_clone`, and `user.max_user_namespaces`.
- Whether `/etc/apparmor.d/bwrap-userns-restrict` exists.
- Whether `/usr/share/apparmor/extra-profiles/bwrap-userns-restrict` exists.
- Whether the `bwrap-userns-restrict` AppArmor profile appears loaded, using available read-only tooling.
- A minimal, non-destructive bubblewrap namespace invocation sufficient to reproduce or clear the initialization failure. Do not use sudo, setuid changes, sysctl writes, profile loads, or other host mutation.
- The exact sanitized bubblewrap/Codex startup error text needed to distinguish missing package, missing/unloaded AppArmor profile, user-namespace restriction, UID/GID-map failure, loopback/network-namespace failure, or another cause.

If a diagnostic command itself would require privilege or change persistent host state, do not run it. Record that limitation instead.

## Official-platform baseline to compare against

Use current official OpenAI Codex sandbox documentation as the product baseline. It states that Linux uses bubblewrap, that installing the distribution `bubblewrap` package is preferred, and that Ubuntu 24.04 may require the extra `bwrap-userns-restrict` AppArmor profile from `apparmor-profiles` to be copied to `/etc/apparmor.d/` and loaded.

Reference:
`https://learn.chatgpt.com/docs/sandboxing`

Do not interpret the documented global fallback
`kernel.apparmor_restrict_unprivileged_userns=0`
as authorized. It is **not authorized** by this handoff.

## Prohibited actions

Do **not**:

- run `sudo`;
- install, remove, upgrade, or reconfigure packages;
- write under `/etc`, `/usr`, `/proc/sys`, or `/sys`;
- load, unload, replace, or edit AppArmor profiles;
- change sysctls or namespace/security policy;
- use `danger-full-access`, `--yolo`, approval bypass, blanket network access, or otherwise weaken the sandbox;
- edit the user's base Codex configuration;
- touch ACMP, KGI, BGF, Kimbers Kreations, or another real project;
- merge to `main`, delete branches, force-push, or perform destructive Git operations;
- publish credentials, environment secrets, raw Codex session contents, usernames/home paths, or other machine-specific private data not required for diagnosis.

## Durable result

Write a concise human-readable diagnostic result to:

`handoffs/codex/2026-08-07/GACP_Codex_Sandbox_Host_Diagnostic_Result_2026-08-07.md`

and a machine-readable sanitized receipt/evidence record to:

`handoffs/codex/2026-08-07/GACP_Codex_Sandbox_Host_Diagnostic_Result_2026-08-07.json`

The result must state:

1. exact root cause if established, otherwise the narrowest remaining hypotheses;
2. evidence for each relevant host prerequisite;
3. whether the failure matches OpenAI's documented Ubuntu 24.04 AppArmor/bubblewrap case;
4. the least-privilege remediation recommended;
5. every host/system change that remediation would require;
6. whether any step requires `sudo` or owner action;
7. security impact and rollback path;
8. whether the existing GACP execution adapter itself needs code/config changes;
9. whether a clean rerun of the existing acceptance harness should be sufficient after remediation;
10. what genuine owner gate comes next.

## Publication scope

You are authorized to create, stage, commit, and normally push only the two diagnostic result paths named above, plus a narrowly necessary sanitized diagnostic evidence file under `evidence/2026-08-07/` if the two results cannot faithfully carry the evidence.

Before publication, verify no secrets, raw sessions, usernames, home-directory paths, tokens, credentials, or unrelated machine data are included. Preserve all existing tracked changes and commits.

The conversational return should be a compact receipt only. ChatGPT will retrieve and independently assess the substantive result from Git before any host remediation is authorized.
