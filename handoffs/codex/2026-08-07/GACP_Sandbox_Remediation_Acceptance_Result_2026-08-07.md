# GACP Sandbox Remediation and Acceptance Result

- Date: 2026-08-07
- Governing handoff commit: `d4d06f9b8222d16a43de31584696412b38e44713`
- Branch: `gacp/codex-execution-automation-corrective-20260807`
- Host remediation: **PASS**
- Sandbox prerequisite verification: **PASS**
- Fresh-session acceptance: **FAIL / BLOCKED**
- Ready for real migration: **No**
- Merge authorization: **Not granted**

## Outcome

The owner-authorized Ubuntu 24.04 AppArmor remediation was applied exactly as documented. It resolves
the original bubblewrap initialization blocker while preserving the global AppArmor
unprivileged-user-namespace restriction. Host-level minimal bubblewrap probes and the correctly
invoked Codex Linux sandbox probe now pass.

The complete disposable fresh-session GACP acceptance scenario nevertheless failed. It recorded zero
routine manual prompts and reached real repository execution, including correct commits and normal
pushes to both disposable remotes. However, after the first fresh session returned, the corresponding
local disposable branch refs and worktrees were not converged to the pushed commits. The second fresh
session correctly stopped on that local/remote mismatch. The harness therefore failed its exact
scope, local commit, governed result, and final-cleanliness assertions.

The host remediation is successful, but substantive execution acceptance is not. Readiness remains
`false`.

## Host changes performed

1. Refreshed Ubuntu package metadata.
2. Installed the two approved packages:
   - `apparmor-profiles`
   - `apparmor-utils`
3. Installed their package-manager-selected runtime dependencies:
   - `python3-apparmor`
   - `python3-libapparmor`
4. Copied the packaged `bwrap-userns-restrict` profile to
   `/etc/apparmor.d/bwrap-userns-restrict` with mode `0644`.
5. Loaded only that profile with `apparmor_parser -r`.

Administrator authentication was required for this one-time remediation setup and is reported
separately from the acceptance prompt count. No administrator authentication occurred inside the
routine governed acceptance sessions.

No package was removed or upgraded, no sysctl was written, no global restriction was disabled, no
Codex base configuration was edited, and no unrelated project was touched.

## Security-boundary verification

| Check | Result |
|---|---|
| `kernel.apparmor_restrict_unprivileged_userns` | `1` — preserved |
| `kernel.unprivileged_userns_clone` | `1` |
| `user.max_user_namespaces` | `29345` at host level |
| Packaged and installed profile bytes | Exact SHA-256 match |
| Installed profile ownership/mode | `root:root`, `0644` |
| Minimal bwrap user namespace | PASS |
| Minimal bwrap user plus network namespace | PASS |
| Correct Codex sandbox probe, `codex sandbox /bin/true` | PASS |
| Generic `unshare --user --map-root-user` | Expected FAIL under the preserved global restriction |

The generic `unshare` failure is intentional: the least-privilege AppArmor policy permits the
distribution `/usr/bin/bwrap` path rather than globally enabling arbitrary unprivileged namespace
creation.

This matches the [official OpenAI Codex sandbox procedure](https://learn.chatgpt.com/docs/sandboxing)
for Ubuntu 24.04. The documented global sysctl fallback was neither used nor authorized.

## Deterministic validation

- GACP unit and disposable-Git guardrail suite: **20/20 PASS**
- Installed `gacp` profile exact/strict verification: **PASS**
- Base Codex configuration modified: **No**
- Temporary acceptance profile removed: **Yes**
- Danger-full-access or approval bypass used: **No**

## Fresh-session acceptance evidence

- Scenario: disposable fresh-session cross-repository
- Fresh Codex sessions: **2**
- Interactive TTY: **No**
- Session stdin: `DEVNULL`
- Routine manual human approval prompts: **0**
- Original bubblewrap initialization blocker: **Cleared**
- First session: reached edit, validation, exact commits, normal pushes, and remote verification
- Second session: stopped fail-closed after detecting local/remote and worktree mismatches
- Overall harness status: **FAIL**

Harness failure classes:

- `target-commit-missing`
- `target-scope`
- `gacp-receipt-commit-missing`
- `gacp-scope`
- `result-receipt`
- `final-worktree`

The first session's remote publications do not satisfy acceptance because the harness must also prove
the local branch identities, result receipt, final cleanliness, and second-session idempotence.
Zero prompts alone cannot promote this result.

## Assessment and recommendation

The Ubuntu host no longer blocks Codex sandbox startup, so no rollback or additional AppArmor change
is recommended. The existing GACP adapter still needs a narrowly governed follow-up investigation of
why successful disposable Git pushes were not reflected as stable local branch/worktree state across
fresh sessions. The current evidence is consistent with an interaction among protected Git metadata,
approval/escalation execution, and session-local repository state, but this handoff does not authorize
an adapter or harness change and no unproven root cause is asserted.

Do not use the adapter for real migrations. Do not weaken `.git` protection or change approval
policy without a separately governed correction and fresh acceptance evidence.

## Rollback availability

The authorized diagnostic documented a rollback path: unload the specific profile with
`apparmor_parser -R` and remove the copied `/etc/apparmor.d/bwrap-userns-restrict` file. No rollback
was performed because the remediation achieved its intended host-level result and preserved the
global restriction. Package removal remains a separate owner decision.

## Next genuine owner gate

The next gate is owner authorization for a bounded investigation and correction of the
cross-session local Git state failure, followed by another clean run of the existing acceptance
scenario. Final substantive acceptance and any merge to `main` remain separate, unauthorized gates.
