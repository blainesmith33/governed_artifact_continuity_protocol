# GACP minimum operational kit — corrective handoff

## Document control

- Project: Governed Artifact Continuity Protocol (GACP)
- Date: 2026-08-07
- Repository: `blainesmith33/governed_artifact_continuity_protocol`
- Working branch: `gacp/new-chat-handoff-automation-framework-20260803`
- Prior implementation/result commit: `31377f7f0790e2a6109f2744525d705a274c238f`
- Prior result: `handoffs/codex/2026-08-07/GACP_Minimum_Operational_Kit_Implementation_Result_2026-08-07.json`
- Governing bootstrap: `AGENTS.md`
- Governing operating baseline: `GACP_File_First_Governed_Handoff_Workflow.md`
- Approved baseline SHA-256: `6c59fbc2f49786a9a3bd3499256332950fd1639269f40770ae12fd0b04c33458`
- Status: authorized corrective pass
- Scope: GACP only; no merge

## Owner authorization

At the substantive-acceptance gate, ChatGPT identified one gap in the minimum operational kit and did not recommend final acceptance.

The owner then explicitly authorized the requested corrective phase with:

> I approve the corrective pass.

This authorization covers the bounded corrective work in this handoff and routine mechanical actions required to implement, validate, commit, and push that correction on the named GACP working branch. It does not authorize scope expansion, exceptions, sensitive publication beyond the already-public-safe GACP corrective artifacts, destructive operations, force-push, branch deletion, final substantive acceptance, or merge to `main`.

Do not ask the owner to approve routine reads, local tests, scoped edits, staging, commits, or the scoped push covered here. Stop only for a genuine governed exception, a technical permission boundary that cannot be satisfied normally, or an authority gate that this handoff does not grant.

## Why this corrective pass exists

The prior implementation correctly added manifest validation, repository preflight, artifact/hash/protection checks, changed-path scope enforcement, public-safety checks, receipt generation, templates, tests, and the agent bootstrap.

However, the implementation does not satisfy the assessment's requirement for the compact operational path to **perform the mechanical steps authorized by an operation manifest**.

The repository evidence is explicit:

- The operationalization assessment requires: "Add a compact runner or stable Codex command family that performs the mechanical steps authorized by an operation manifest and refuses out-of-scope actions."
- The same assessment identifies routine actions that may be automatic inside an approved manifest, including scoped staging, scoped commit creation, and scoped branch push.
- The current `bin/gacp` accepts `stage`, `commit`, and `push` in `scope.allowed_actions`.
- Yet the current `command_run` only validates, preflights, verifies scope/public safety, and optionally writes a receipt.
- Its own result says `"implementation_push": "not-performed-by-run"`.

Therefore the prior `PASS` establishes that validation works, but it does not establish that the minimum operational kit is fully operational. This is the defect to correct. Do not redesign GACP or repeat the ChatGPT/Git/Codex communication proof.

## Corrective objective

Make the compact governed invocation actually execute the bounded, manifest-authorized mechanical Git operations needed for routine handoff work, while preserving fail-closed scope, safety, provenance, and owner gates.

A conforming fresh agent should be able to start from `AGENTS.md`, obtain an approved operation manifest, invoke the compact path, and have the runner carry out the authorized mechanical Git steps without reconstructing those steps from chat or requiring the owner to approve them one-by-one.

## Required work

1. Bootstrap from repository state.
   - Read `AGENTS.md` completely.
   - Read the approved operating baseline completely.
   - Read the operationalization assessment and the prior implementation result.
   - Inspect the current `bin/gacp`, manifest template, receipt template, operation record, and tests.
   - Verify repository identity, working branch, remote/upstream, and current remote synchronization before editing.
   - Treat the actual remote branch tip you verify as the corrective operation's starting point. Record it explicitly.

2. Correct the compact runner rather than adding a parallel workflow.
   - Keep `./bin/gacp run <operation-manifest.json>` as the compact entry point unless repository evidence requires a narrowly compatible extension.
   - Make `run` execute only the mechanical operations that the manifest both authorizes and sufficiently specifies.
   - At minimum, close the verified gap for `stage`, `commit`, and `push`.
   - If a manifest authorizes only inspection/validation, the runner must remain non-mutating.
   - Do not interpret the presence of an action in a global allowlist as authority to execute it; execution must be authorized by the specific operation manifest.
   - Do not add arbitrary shell-command execution to the manifest as a shortcut.

3. Make mutation parameters explicit and deterministic.
   - If the present manifest lacks data required for safe execution (for example, a commit message or other deterministic execution metadata), make the smallest compatible schema/template addition necessary.
   - The named destination remote and branch must be used; do not infer a different publication target.
   - Stage only paths allowed by the operation scope and never excluded/protected unrelated paths.
   - Before committing, verify the staged set is entirely authorized and public-safety checks pass where applicable.
   - A commit must contain only manifest-authorized paths.
   - A push must be a normal non-force push of the named authorized branch to the named remote.
   - Never force-push, delete a branch, merge, or modify `main`.

4. Resolve the preflight/execution mismatch safely.
   - The current `require_clean_tracked` behavior is useful for a read-only preflight but can conflict with a runner that is supposed to stage and commit already-authorized work.
   - Define and implement a fail-closed distinction between unexpected pre-existing work and the exact authorized candidate changes the operation is meant to publish.
   - Do not weaken protection of unrelated user work merely to make mutation tests pass.
   - Preserve detection of unexpected tracked, staged, and untracked paths.

5. Make receipt behavior accurately describe what happened.
   - The result/receipt must distinguish requested, skipped, performed, and stopped actions.
   - When a commit is created, record verifiable commit/parent/scope evidence.
   - When a push is authorized and succeeds, record the named remote/branch and evidence that the remote ref reached the expected commit.
   - Do not claim a push or synchronization happened when `run` did not perform or verify it.
   - Preserve a workable provenance convention for a receipt that is itself included in a containing commit; do not invent a false self-hash or impossible self-referential commit value.
   - A governed stop/failure must not be mislabeled `PASS`.

6. Update only the minimum operational artifacts required by the correction.
   Expected candidates are:
   - `bin/gacp`
   - `templates/gacp_operation_manifest.template.json`
   - `templates/gacp_codex_result_receipt.template.json` if needed for truthful execution evidence
   - `tests/test_gacp.py`
   - `AGENTS.md` only if its invocation/behavior description needs correction
   - a new corrective operation manifest under `operations/2026-08-07/`
   - a new Codex corrective result/receipt under `handoffs/codex/2026-08-07/`

   Do not modify the exact approved bytes of `GACP_File_First_Governed_Handoff_Workflow.md`. Do not rewrite the prior assessment, prior handoff, or prior result to make history appear different.

7. Prove the correction with executable tests.
   Use isolated temporary Git repositories and local bare remotes or equivalent disposable fixtures so tests do not mutate `main` or depend on pushing test commits to the authoritative remote.

   Required test coverage includes:
   - inspect/validate-only manifest performs no mutation;
   - unauthorized `stage`, `commit`, or `push` is not performed;
   - authorized candidate paths can be staged while out-of-scope or excluded changes stop the run;
   - commit occurs only when explicitly authorized and contains only authorized paths;
   - push occurs only when explicitly authorized, publication authorization is true, and the named branch/remote are correct;
   - push is non-force and fails closed on divergence/non-fast-forward instead of rewriting remote history;
   - public/sensitivity and protected-file checks stop mutation when violated;
   - unexpected pre-existing work is preserved and causes the required governed stop;
   - the receipt truthfully records actions actually performed;
   - repeat/duplicate invocation has defined, safe behavior and does not generate accidental duplicate commits or destructive state changes.

8. Exercise the corrected compact path.
   - Demonstrate in a disposable end-to-end fixture that one authorized `run` invocation can perform the intended stage -> commit -> push sequence and verify the remote result.
   - Validation that merely mocks or reports these actions without causing the disposable Git state transitions is insufficient.
   - Also run the repository's full relevant test suite and format/static checks.

9. Record the corrective operation durably.
   - Create a machine-readable operation manifest for this corrective pass with the verified starting commit as its base.
   - Keep its allowed paths limited to the corrective artifacts.
   - Record this handoff as the approval reference.
   - Record publication as authorized only for these public-safe corrective artifacts on the existing working branch.
   - Write a durable Codex corrective result/receipt containing the verified starting state, files changed, tests, execution evidence, commit lineage, remote push state, any exceptions, and the next genuine owner gate.

10. Commit and push the correction to:
    `gacp/new-chat-handoff-automation-framework-20260803`

    Use scoped normal Git operations. Do not merge.

## Acceptance criteria

Do not report the corrective pass as ready for ChatGPT acceptance unless all of the following are true:

- the approved workflow baseline remains byte-identical at SHA-256 `6c59fbc2f49786a9a3bd3499256332950fd1639269f40770ae12fd0b04c33458`;
- the runner demonstrably performs authorized mechanical Git operations rather than only validating them;
- unauthorized actions remain non-executable;
- scope/exclusion/protected-work/publication gates remain fail-closed;
- stage/commit/push behavior is deterministic enough to be driven from a governed operation manifest without reconstructing command sequences from conversation memory;
- tests prove an actual disposable stage/commit/push lifecycle and the principal stop conditions;
- the authoritative remote working branch contains the corrective result/receipt and is synchronized to the reported correction;
- `main` is unchanged;
- no other repository is modified;
- no force-push, merge, branch deletion, or destructive operation occurred.

If any criterion fails, record a governed STOP/exception in Git when safely possible and do not ask the owner to manually relay the substantive failure report.

## Durable return

The substantive result must be committed and pushed into this GACP working branch. The Codex conversational response is only a compact completion receipt.

At completion, report only:

- corrective commit hash;
- pushed branch;
- corrective result/receipt path;
- validation status;
- whether ChatGPT can retrieve the substantive result directly from Git;
- whether an immediate owner gate exists and its category.

The next expected gate after a successful correction is ChatGPT substantive review followed, if warranted, by owner final acceptance. Merge authorization remains separate.
