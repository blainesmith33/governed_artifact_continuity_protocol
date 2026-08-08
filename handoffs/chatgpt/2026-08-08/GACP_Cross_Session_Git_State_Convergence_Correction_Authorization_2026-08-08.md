# GACP Cross-Session Git-State Convergence Correction Authorization

- Date: 2026-08-08
- Owner decision: **APPROVED**
- Authorized branch: `gacp/codex-execution-automation-corrective-20260807`
- Governing continuity handoff: `72155e09b9eb4a0e6783994a9f0c1a6ac4f85523`
- Latest substantive failed acceptance result entering this phase: `cb573859522accfc0eb98be3c28201670945cc19`
- Readiness entering operation: **false**
- Substantive acceptance entering operation: **FAIL / BLOCKED**
- Merge authorization: **NOT GRANTED**

## Owner authorization

The owner approves the bounded investigation and correction of the demonstrated GACP cross-session local Git-state convergence failure, followed by a clean full acceptance rerun.

This authorization satisfies the next owner gate recorded in the governing continuity handoff. Codex must retrieve the governing handoff, read `AGENTS.md`, and use the authoritative Git evidence rather than reconstructing scope from conversational memory.

Routine mechanical actions already inside this bounded authorization do not require additional owner governance approvals.

## Authorized scope

Codex may, using disposable repositories and the existing corrective branch:

1. Reproduce and diagnose why successful governed pushes left local disposable branch refs/worktrees inconsistent with the pushed remote commits.
2. Establish the evidence-supported root cause before changing the adapter or acceptance harness.
3. Determine whether the failure arises from the execution boundary, protected Git-metadata handling, the GACP adapter, the acceptance harness, or their interaction.
4. Make only the minimum GACP adapter/harness correction supported by that evidence.
5. Run relevant deterministic validation after the correction.
6. Rerun the complete fresh-session governed acceptance scenario from a clean disposable state.
7. Publish the governed diagnosis/result/receipt to this existing corrective branch under established GACP conventions.

If evidence shows that a required fix would exceed this scope or conflict with an explicit exclusion below, stop fail-closed and return a governed blocker instead of expanding authority.

## Security and governance invariants

The correction and rerun must preserve:

- the existing Codex sandbox;
- protected `.git` metadata boundaries;
- Auto-review governance for eligible execution-environment escalations;
- the existing least-privilege GACP Codex execution profile;
- the global AppArmor user-namespace restriction already remediated and verified;
- the requirement for **0 routine manual human approval prompts** during governed execution;
- informed owner-facing reporting at genuine governance gates;
- separation between mechanical publication success and substantive acceptance/readiness.

Do not weaken a security boundary merely to make the acceptance test pass.

## Explicit exclusions

The owner does **not** authorize:

- weakening or bypassing `.git` protection;
- `danger-full-access`, `--yolo`, unrestricted execution, or approval bypass;
- disabling or weakening the global AppArmor restriction;
- changing unrelated host security configuration;
- modifying ACMP, KGI, BGF, Kimbers Kreations, or any other real project;
- using a real project as the acceptance target;
- force-pushing, deleting branches, rewriting published history, or destructive Git repair;
- merging the corrective branch into `main`;
- declaring readiness from unit tests, deterministic tests, or prompt count alone;
- publishing credentials, secrets, raw private sessions, or unnecessary private host details.

## Required acceptance rerun

A PASS requires a clean disposable end-to-end scenario that proves all of the following together:

1. Fresh governed Codex execution reaches real repository operations.
2. The intended disposable target and GACP artifacts are edited/generated, validated, staged, committed, and normally pushed within authorization.
3. Local branch refs/worktrees converge to the exact commits published remotely.
4. Final local/remote commit identity is verified.
5. Final worktrees are clean as required by the harness.
6. Governed human-readable result and machine receipt identities are valid and consistent.
7. A second fresh session proves the expected idempotent/resumable behavior rather than stopping on stale local state.
8. Routine manual human approval prompt count is **0**.
9. No security/governance invariant above is weakened to obtain the result.

Unit/deterministic tests remain supporting evidence, not a substitute for this full acceptance scenario.

`ready_for_real_migration` must remain `false` unless every required acceptance property passes. Any unresolved mismatch is substantive **FAIL / BLOCKED**.

## Durable return

Publish the governed human-readable result and machine-readable receipt only to the existing corrective branch within established GACP result conventions. The result must report:

- established root cause and supporting evidence;
- exact corrective changes made;
- deterministic validation outcome;
- full fresh-session acceptance outcome;
- local/remote convergence evidence;
- routine human approval prompt count;
- substantive acceptance status;
- `ready_for_real_migration`;
- any remaining limitation;
- Codex's recommendation and the next genuine owner gate.

Normal scoped publication to the corrective branch is authorized. Merge is not.

Return only a short conversational receipt so ChatGPT can retrieve the substantive result from Git and provide the owner an independent governed assessment.
