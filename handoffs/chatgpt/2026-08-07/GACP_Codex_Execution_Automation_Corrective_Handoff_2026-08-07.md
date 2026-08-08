# GACP Codex Execution Automation Corrective Handoff — 2026-08-07

## Status

Authorized corrective implementation handoff.

This handoff exists because the GACP minimum operational kit passed its repository-level tests but failed the owner's real operational requirement during cross-repository use: routine Codex work still produced a large number of execution-environment approval prompts.

The prior claim that GACP was ready for real migration is therefore not sufficient evidence of end-to-end automation readiness. GACP must not claim this corrective requirement is satisfied until the acceptance test in this handoff passes.

## Owner intent and authorization

The owner has authorized publication of this sanitized corrective handoff and authorized Codex to implement and validate the bounded GACP correction described here on this corrective branch.

This authorization does **not** authorize:

- merge to `main`;
- destructive operations;
- unrelated repository changes;
- changes to ACMP, KGI, BGF, Kimbers Kreations, or any other project repository;
- publication of credentials, secrets, tokens, raw session transcripts, or user-local filesystem paths;
- unrestricted Codex execution such as danger-full-access / yolo-style bypasses;
- weakening genuine owner governance gates.

If implementation reaches a genuine owner decision, stop and return a governed result with the evidence needed for an informed decision.

## Problem statement

Authoritative GACP currently contains a mismatch between governance intent and actual Codex execution behavior.

1. GACP's authorization model says one bounded owner authorization may cover routine mechanical work such as inspection, validation, governed artifact generation, exact staging, commit, and already-authorized branch publication.
2. Codex execution-environment permission prompts can still interrupt those routine actions repeatedly.
3. GACP does not yet provide a complete reusable Codex execution adapter/profile that makes those two layers operate together across repositories.
4. Existing workflow language must be reviewed for conflicts between older per-step owner gates and the newer bounded-authorization model.
5. Prior tests validated runner behavior, but did not measure the owner's actual burden in a fresh cross-repository Codex session.

This is an end-to-end acceptance-test gap, not a request to redesign GACP.

## Required corrective outcome

Implement the minimum safe GACP-to-Codex execution layer needed so that, after one-time setup and a single bounded operation authorization, routine governed Codex work can proceed without repeated human execution approvals.

The correction must preserve human authority for genuine governance decisions.

### 1. Reconcile governance

Review `AGENTS.md`, `GACP_File_First_Governed_Handoff_Workflow.md`, the operational kit, manifests, runner behavior, and relevant tests.

Resolve conflicting or ambiguous language so the authoritative rule is explicit:

- a bounded owner authorization covers routine actions documented within that operation's scope;
- routine tool/sandbox steps must not be reinterpreted as separate governance approvals;
- genuine owner gates remain explicit;
- execution-environment capability boundaries remain real and must not be bypassed.

Also ensure mandatory owner-facing reporting applies **before** any genuine owner approval is requested, as well as after delegated work. The owner must receive enough plain-English evidence, risk, recommendation, scope, and consequence information to make an informed decision rather than being asked to approve blindly.

### 2. Add a reusable Codex execution adapter/profile

Design and implement a GACP-owned, reusable Codex execution configuration/bootstrap mechanism using only currently supported Codex capabilities.

Before relying on configuration keys or behavior, verify them against the current authoritative OpenAI/Codex documentation available to the execution environment.

The adapter must:

- work for GACP-governed operations launched from another project repository;
- provide a deterministic way for a fresh Codex session to discover the GACP bootstrap/governance without each project reinventing it;
- configure normal permissions broadly enough for routine in-scope work to avoid human prompt storms;
- route eligible exceptional execution approvals through supported automatic review where appropriate;
- use narrow, least-privilege command/network/filesystem allowances for recurring boundary crossings;
- preserve execution isolation and deny unrestricted-machine modes;
- keep genuine owner governance gates separate from technical permission review;
- be idempotent;
- preserve and safely coexist with the owner's existing Codex configuration;
- provide inspect/dry-run or equivalent behavior before applying user-scope configuration changes;
- never embed credentials, tokens, secrets, machine-specific absolute paths, or raw session data in public repository artifacts.

Do not assume that a repository `AGENTS.md` alone changes Codex sandbox policy. Explicitly connect governance/bootstrap to execution configuration.

### 3. Provide setup and verification tooling

Provide the smallest deterministic tooling/documentation needed to install or activate the GACP execution adapter and verify the effective state.

A fresh conforming agent must be able to determine from repository artifacts:

- what has to be configured once;
- what is operation-specific;
- how to activate the governed profile;
- how to verify that the intended configuration is active;
- how to restore or disable the GACP-specific integration without damaging unrelated user configuration.

Avoid manual multi-step instructions where they can be safely automated and validated.

### 4. Add a real end-to-end acceptance test

The corrective change is **not accepted** merely because unit tests pass.

Build and execute a representative fresh-session/cross-repository acceptance test in a disposable test repository or equally isolated fixture. Do not modify ACMP or another real project merely to prove the fix.

The representative governed operation must cover the normal lifecycle:

`inspect -> edit -> validate -> governed artifact -> exact stage -> commit -> normal push -> result receipt`

The acceptance evidence must explicitly record:

- number of manual human execution approval prompts after the one-time setup;
- number and identity of genuine owner governance gates encountered;
- effective Codex profile/policy characteristics relevant to the test, excluding sensitive or machine-specific values;
- Git scope/parentage/ref verification;
- validation results;
- rerun/idempotence behavior;
- any limitation that prevents the test from representing a real fresh cross-repository session.

### Required pass criterion

For routine in-scope actions after one-time setup:

**Manual owner approval prompts caused by routine execution: 0**

A genuine governance decision may still stop execution; it must be reported distinctly and must not be counted as a routine technical prompt.

If the system cannot demonstrate the zero-routine-prompt criterion safely with supported Codex mechanisms, report **FAIL** or **BLOCKED** with the exact limitation. Do not weaken the criterion and do not claim operational readiness.

## Safety requirements

- No force push.
- No branch deletion.
- No merge to `main`.
- No destructive cleanup of user configuration.
- No unrestricted Codex/sandbox bypass.
- No publication of secrets, credentials, raw sessions, or local absolute paths.
- Do not alter unrelated tracked files.
- Keep generated test repositories disposable and isolated.
- Preserve prior provenance/history; correct the readiness claim with new evidence rather than rewriting historical receipts.

## Required durable result

Return all substantive work through Git on the corrective branch.

The final governed result/receipt must include, at minimum:

1. what Codex found;
2. root cause(s);
3. files changed and why;
4. configuration/bootstrap approach implemented;
5. how existing user configuration is preserved;
6. tests executed;
7. end-to-end prompt-count evidence;
8. whether the required pass criterion was met;
9. known limitations or remaining risks;
10. Codex recommendation;
11. exact commit/ref state and remote synchronization evidence;
12. next genuine owner gate, if any.

Do not use the owner as the artifact courier. The conversational response should be a compact retrieval receipt only.

## Stop conditions

Stop and publish a governed blocked/failure result if:

- required Codex behavior cannot be verified against supported mechanisms;
- safe automation would require unrestricted execution;
- existing configuration cannot be preserved safely;
- the cross-repository acceptance test cannot measure human prompt behavior credibly;
- repository state diverges materially from the authorized base/scope;
- implementation requires touching another real project;
- a genuine owner decision is required.

## Definition of done

This corrective implementation is ready for ChatGPT/owner review only when the durable Git evidence allows an independent reviewer to answer all of these:

- Does a fresh GACP-governed Codex operation discover the right governance cross-repository?
- Does one bounded authorization cover the routine governed phase?
- Do routine Codex execution actions complete with zero manual human approval prompts after setup?
- Are real owner gates still preserved?
- Can the owner understand any requested decision from a plain-English evidence-based summary?
- Can the configuration be safely inspected, applied idempotently, and disabled/restored?
- Can another conforming AI reconstruct what happened from Git without conversation history?

Until those answers are supported by evidence, treat GACP automation readiness as unproven.
