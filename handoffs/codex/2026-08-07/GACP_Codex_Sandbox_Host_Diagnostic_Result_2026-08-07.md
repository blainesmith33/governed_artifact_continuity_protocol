# GACP Codex Sandbox Host Diagnostic Result

- Date: 2026-08-07
- Governing handoff commit: `564f79e05e5b6a94d116d64c011f73510e0aad48`
- Branch: `gacp/codex-execution-automation-corrective-20260807`
- Diagnostic status: **PASS — root cause established**
- Existing acceptance/readiness status: **FAIL / BLOCKED; not ready for real migration**
- Host changes performed: **None**

## Root cause

The Codex sandbox failure is the documented Ubuntu 24.04 AppArmor/bubblewrap case. The host has the
Ubuntu distribution `bubblewrap` executable and permits unprivileged user namespaces at the general
kernel controls, but AppArmor's separate unprivileged-user-namespace restriction is enabled. The
Ubuntu 24.04 extra `bwrap-userns-restrict` profile is neither installed at its package source path
nor present under `/etc/apparmor.d/`.

Kernel audit evidence confirms the causal chain: execution of `/usr/bin/bwrap` transitions from
`unconfined` to the generic `unprivileged_userns` profile, which denies `setpcap`,
`net_admin`, and writes to the process `uid_map`. A minimal user-namespace invocation consequently
fails while setting the UID map; adding a network namespace fails while configuring loopback. Codex's
Linux sandbox reproduces that same loopback failure.

This is not a missing-`bwrap` problem, a disabled `kernel.unprivileged_userns_clone` control, a
zero namespace quota, or a GACP adapter configuration error.

## Host prerequisite evidence

| Prerequisite | Sanitized finding | Assessment |
|---|---|---|
| OS | Ubuntu 24.04.4 LTS | Matches the documented affected release |
| Kernel | Linux 6.17.0-35-generic, x86_64 | Supports the inspected namespace controls |
| Codex CLI | 0.147.0 | Present |
| Resolved bubblewrap | Distribution executable at `/usr/bin/bwrap` | Present and first on `PATH` |
| `bubblewrap` package | 0.9.0-1ubuntu0.1 | Installed |
| `apparmor` package | 4.0.1really4.0.1-0ubuntu0.24.04.7 | Installed |
| `apparmor-profiles` | Candidate available; not installed | Required extra profile source absent |
| `apparmor-utils` | Candidate available; not installed | Official procedure requests it |
| `apparmor_parser` | Present, version 4.0.1 | Load/remove commands available |
| AppArmor module/service | Enabled and active | Restriction is enforced |
| Current process label | `unconfined` | Audit still shows user-namespace profile transition |
| `kernel.apparmor_restrict_unprivileged_userns` | `1` | Restriction enabled |
| `kernel.unprivileged_userns_clone` | `1` | General unprivileged user namespaces enabled |
| `user.max_user_namespaces` | `29345` | Nonzero; quota is not the blocker |
| `/etc/apparmor.d/bwrap-userns-restrict` | Absent | Profile is not installed for loading |
| Extra-profile package source path | Absent | Consistent with missing `apparmor-profiles` |
| Loaded-profile enumeration | Not readable without additional privilege | No privileged diagnostic was attempted |

Although direct loaded-profile enumeration was unavailable to the unprivileged diagnostic, the
missing profile files and kernel audit transition to the generic `unprivileged_userns` profile
establish that the required bwrap-specific policy is not providing the needed permissions.

## Reproduction evidence

- Minimal `bwrap` user namespace: `bwrap: setting up uid map: Permission denied`
- Minimal `bwrap` user plus network namespace:
  `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`
- Minimal `unshare --user --map-root-user`:
  `unshare: write failed /proc/self/uid_map: Operation not permitted`
- Codex Linux sandbox:
  `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted`
- Sanitized kernel audit classes: AppArmor denied capabilities `setpcap` and `net_admin`, and
  denied writes to `/proc/<pid>/uid_map`, under `profile="unprivileged_userns"`.

All probes were read-only or ephemeral. No `sudo`, package operation, sysctl write, profile load,
configuration edit, or persistent host mutation was performed.

## Official-platform comparison

The [official OpenAI Codex sandbox documentation](https://learn.chatgpt.com/docs/sandboxing) states
that Linux uses the first `bwrap` on `PATH`, recommends the distribution package, and documents
that Ubuntu 24.04 may still block user-namespace creation until the extra
`bwrap-userns-restrict` AppArmor profile is installed and loaded. The observed host state and exact
denials match that case.

The documented global fallback
`kernel.apparmor_restrict_unprivileged_userns=0` is not authorized and is not recommended here.

## Least-privilege remediation recommendation

Subject to owner approval, follow the profile-specific Ubuntu 24.04 procedure from the official
documentation:

1. Run `sudo apt update`.
2. Run `sudo apt install apparmor-profiles apparmor-utils`.
3. Copy the packaged profile with:
   `sudo install -m 0644 /usr/share/apparmor/extra-profiles/bwrap-userns-restrict /etc/apparmor.d/bwrap-userns-restrict`.
4. Load only that profile with:
   `sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict`.
5. Re-run the minimal `bwrap` and Codex sandbox probes, then run the existing disposable GACP
   acceptance harness.

Every remediation step changes host state and requires `sudo` plus explicit owner action. Step 1
refreshes package metadata; step 2 installs two Ubuntu packages; step 3 adds one root-owned AppArmor
profile; step 4 loads/replaces that profile in the kernel. No global sysctl change is required.

## Security impact and rollback

The recommended approach preserves
`kernel.apparmor_restrict_unprivileged_userns=1` and grants the required namespace behavior through
a purpose-specific AppArmor profile for the distribution `bwrap` executable. This is narrower than
disabling the restriction globally.

If rollback is required, an owner-authorized administrator can remove the loaded profile with
`sudo apparmor_parser -R /etc/apparmor.d/bwrap-userns-restrict` and remove the copied
`/etc/apparmor.d/bwrap-userns-restrict` file. Package removal is optional and should be evaluated
separately because those packages may supply other administrative profiles or tools.

## Adapter and acceptance disposition

The existing GACP execution adapter does not need a code or configuration change for this root cause.
Its strict profile verification passed before the sandbox invocation; failure occurs below it during
host namespace setup.

After the narrow AppArmor remediation and successful minimal probes, a clean rerun of
`tests/run_codex_execution_acceptance.py` should be sufficient to test the existing adapter. This is
a recommendation, not a readiness claim: readiness remains false until the complete fresh-session
cross-repository scenario passes with zero routine manual prompts.

## Next genuine owner gate

The next gate is owner approval or rejection of the four host-remediation steps above. No remediation
has been authorized or performed by this diagnostic handoff. If approved and completed, the next
technical action is the bounded verification and existing acceptance-harness rerun. No merge to
`main` is authorized.
