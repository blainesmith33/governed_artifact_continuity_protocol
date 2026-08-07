# GACP minimum operational kit implementation handoff — 2026-08-07

## Document control

- Project: Governed Artifact Continuity Protocol (GACP)
- Repository: `blainesmith33/governed_artifact_continuity_protocol`
- Working branch: `gacp/new-chat-handoff-automation-framework-20260803`
- Prior operationalization assessment commit: `c6acce4c6fb1334eec8924cf8c6db9a00ef1fed5`
- Assessment: `handoffs/codex/2026-08-07/GACP_Operationalization_Assessment_2026-08-07.md`
- Repository bootstrap governance added at commit: `b2b88f8ffc8e9043e2108dc13539aed80d02465b`
- Bootstrap: `AGENTS.md`
- Approved protected workflow SHA-256: `6c59fbc2f49786a9a3bd3499256332950fd1639269f40770ae12fd0b04c33458`
- Scope: GACP only

## Owner authorization

The owner has explicitly approved the bundled decision requested by the operationalization assessment.

The approved authorization is:

> I approve the protected workflow draft at SHA-256 `6c59fbc2f49786a9a3bd3499256332950fd1639269f40770ae12fd0b04c33458` as the source operating baseline, authorize its provenance-preserving integration into GACP, and authorize the bounded implementation of the minimum operational kit. Routine actions within that scope are pre-authorized; exceptions, sensitive publication, final acceptance, and merge still require owner approval.

Treat this authorization as granted for this implementation phase.

Do not request separate owner approval for routine operations inside this scope.

## Purpose

Implement the minimum operational kit already recommended by the committed GACP Operationalization Assessment.

The ChatGPT/Git/Codex communication workflow has already been proven and owner-accepted. This task operationalizes it for routine repeated use. It is not authorization to redesign GACP or rerun the communication proof.

Git remains the durable backend communication channel between ChatGPT and Codex. The owner must not be used as a courier for substantive prompts, files, findings, validation reports, or return artifacts.

## Mandatory startup

1. Confirm the authoritative local repository is:
   `/media/kimberly/320GB/governed_artifact_continuity_protocol`
2. Verify repository identity, current branch, remote, upstream relationship, worktree/index status, and relevant remote refs.
3. Read root `AGENTS.md` completely and follow it.
4. Read the complete Operationalization Assessment named above.
5. Inspect and verify the protected local workflow draft:
   `GACP_File_First_Governed_Handoff_Workflow.md`
6. Verify that draft's SHA-256 is exactly:
   `6c59fbc2f49786a9a3bd3499256332950fd1639269f40770ae12fd0b04c33458`
7. Preserve unrelated/protected work. Stop on an invariant mismatch instead of guessing.

## Implementation objective

Move GACP from “the proven workflow works” to “the workflow is operational and reusable for the next real migration/project handoff with minimal owner intervention.”

Use the assessment as the authoritative definition of the minimum operational kit.

At minimum, implement the assessment's recommended components:

1. Integrate the owner-approved protected file-first workflow as the tracked operating baseline with provenance preserved and without silently changing its approved meaning or exact approved bytes.
2. Add one parameterized operation-manifest template for repository, branch, scope, allowed actions, exclusions, artifact hashes, sensitivity/publication status, validation requirements, authorization state, and current gate.
3. Add one parameterized Codex result/receipt template for repository verification, exact changes, tests/checks, commit lineage, push state, exceptions, and next gate.
4. Add deterministic helpers for read-only repository preflight and result verification covering repository identity, branch/upstream state, protected work, hashes, formatting, scope, lineage, and public-safety checks.
5. Add a compact runner or stable Codex command family that consumes the governed operation definition, performs only authorized routine mechanical steps, records evidence, and refuses out-of-scope operations.
6. Add the smallest validation/test coverage needed to demonstrate that the operational kit enforces its declared scope and stop conditions.

Prefer the smallest concrete implementation that makes the next real migration usable. Do not build a generalized platform or duplicate mechanisms already present.

## Required behavioral invariant

The implementation must make this repeatable across fresh conversations and across conforming AI agents without depending on conversational memory.

A receiving agent must be able to start from repository state and determine:

- which governance to load;
- which operation is current;
- what has already been completed;
- what actions are authorized;
- which actions require an owner gate;
- what validation must pass;
- where to write its durable result;
- how the next agent retrieves that result.

Repository artifacts and deterministic tooling—not model-specific memory—must carry those invariants.

## Automation and approval boundary

Within the approved scope, routine operations are pre-authorized as described by the assessment and root `AGENTS.md`.

Do not stop for separate owner approval for routine:

- repository inspection;
- hashing and integrity checks;
- validation;
- parameterized governed-artifact creation;
- repository-approved tests/checks;
- staging of only authorized paths;
- scoped commit creation on the authorized isolated branch;
- scoped push when already covered by this authorization.

Stop and record an exception for:

- scope expansion;
- failed invariants or unexpected repository state;
- sensitive/publication concerns outside the authorization;
- destructive operations;
- final substantive acceptance;
- merge into `main` or another protected/authoritative branch.

Environment-level permission prompts remain technical capability boundaries. They must not be bypassed, but they are not new GACP governance approvals.

## Scope exclusions

Do not modify:

- ACMP;
- KGI;
- BGF;
- Kimbers Kreations;
- any other repository.

Do not merge this implementation to `main`.
Do not delete branches.
Do not publish raw private session archives, credentials, hidden instructions, authentication material, or unrelated conversation content.

## Durable return requirement

The substantive deliverable must be committed and pushed to this GACP working branch.

Create or update the governed Codex result/receipt in the repository so ChatGPT can retrieve and review it directly from Git.

The result must state, with evidence:

- what was implemented;
- what was validated;
- exact files changed/added;
- relevant hashes and commit lineage;
- whether the compact operational path is ready for a real migration;
- remaining exceptions or gaps;
- whether an owner decision is now required and the category of that decision.

Do not require the owner to paste that result back into ChatGPT.

## Completion response

After the durable result has been committed and pushed, the Codex conversational response must contain only a compact receipt:

- commit hash;
- pushed branch;
- result/receipt path;
- validation status;
- whether ChatGPT can retrieve the result;
- whether an immediate owner gate exists.

Proceed without requesting per-command approval for routine actions already authorized above.
