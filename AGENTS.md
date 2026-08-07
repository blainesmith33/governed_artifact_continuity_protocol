# GACP agent bootstrap governance

## Authority and purpose

This file is the repository-level bootstrap for any AI agent, automation, or human-assisted tool operating on the Governed Artifact Continuity Protocol (GACP) repository.

The repository is the durable source of governed project state. Conversation memory is not authoritative project state and must not be required to reconstruct completed work.

The proven communication model is:

`Owner -> ChatGPT -> Git/GACP -> Codex -> Git/GACP -> ChatGPT -> Owner`

Git/GitHub is the durable backend communication channel between cooperating agents. The owner is an approval authority, not an artifact courier.

## Mandatory bootstrap

Before substantive GACP work, every agent must:

1. Verify the repository identity, current branch/ref, and relevant remote state available to it.
2. Read this `AGENTS.md` completely.
3. Read the current governing workflow baseline when tracked in the repository.
4. Read the current operation manifest or governed handoff identified for the task.
5. Read any prior result/receipt explicitly referenced by that manifest or handoff.
6. Use repository evidence to determine completed work. Do not ask the owner to reconstruct or paste information that is already retrievable from Git.
7. Stop if required governed inputs are missing, inconsistent, outside authorized scope, or cannot be verified.

Until the approved file-first workflow has been integrated as a tracked baseline, the current operationalization assessment is the controlling implementation-phase reference:

`handoffs/codex/2026-08-07/GACP_Operationalization_Assessment_2026-08-07.md`

The assessment records that the communication proof is complete and must not be redesigned or repeated merely to prove that ChatGPT and Codex can exchange artifacts through Git.

## Inter-agent communication rule

Substantive information crossing between ChatGPT and Codex must be represented by a governed Git artifact.

This includes, as applicable:

- implementation handoffs;
- operation manifests;
- specifications and approved source artifacts;
- Codex findings and implementation results;
- validation reports and receipts;
- exceptions requiring review;
- continuation/new-chat handoffs.

Chat conversation should be limited to:

- owner decisions and approvals;
- short completion receipts;
- minimal retrieval/invocation instructions that point the next agent to Git;
- technical permission prompts imposed by the execution environment.

Do not use the owner to manually transfer substantive documents, prompts, findings, reports, or state between agents when the receiving agent can retrieve them from Git.

## Authorization model

A single owner authorization may cover a bounded phase. Within its documented scope, routine mechanical actions do not require separate owner approvals.

After start authorization, actions documented as routine by the governing operation may include read-only inspection, hashing, validation, governed artifact generation, repository-approved tests, scoped staging, scoped commits, and scoped branch pushes when publication is already authorized.

Stop for owner authority when required by the governing operation, including:

- scope expansion;
- verification failure or material repository-state mismatch;
- detected sensitive/publication concern not already authorized;
- exception acceptance;
- final substantive acceptance;
- merge into the authoritative/protected branch;
- destructive or otherwise separately governed actions.

Execution-environment permission prompts are capability boundaries, not GACP governance approvals. Never bypass them or misrepresent them as owner decisions.

## Mandatory owner-facing reporting

Meaningful human oversight requires concise interpretation, not manual artifact relay.

For any governed job delegated to Codex or another cooperating agent:

1. Before execution, the owner-facing coordinating agent must give the owner a concise plain-English summary of what the delegated agent is being asked to accomplish. Keep the substantive technical/governed handoff in Git.
2. After the delegated agent returns, retrieve the authoritative result and relevant evidence from Git rather than relying only on its conversational completion receipt.
3. Provide the owner an evidence-based summary covering, as applicable:
   - what the delegated agent found;
   - what it actually did;
   - what it recommends;
   - the coordinating agent's independent assessment;
   - what the coordinating agent agrees with and why;
   - what the coordinating agent disagrees with or believes needs correction;
   - validation results and current project state;
   - what happens next;
   - any genuine owner decision required, with enough context for an informed decision.
4. Treat an agent-reported `PASS` as evidence to review, not as a substitute for independent assessment when substantive acceptance or an owner decision is involved.
5. Do not turn the owner-facing summary into the durable inter-agent transport. Git remains authoritative for substantive state and evidence.
6. Do not require the owner to paste or relay the full result between agents when it is retrievable from Git.

The provenance and rationale for this requirement are recorded in:

`handoffs/chatgpt/2026-08-07/GACP_Owner_Facing_Reporting_Governance_Amendment_2026-08-07.md`

## Preserve established work

Do not:

- redesign GACP when the requested task is implementation or operation of the proven workflow;
- repeat the completed ChatGPT/Git/Codex communication proof without a new requirement or failure;
- silently transform exact-content artifacts;
- overwrite unrelated or protected work;
- expand work into ACMP, KGI, BGF, Kimbers Kreations, or another repository without explicit authorization;
- merge, delete branches, publish sensitive/raw private material, or take destructive action without the applicable authorization.

## Durable return requirement

An agent's substantive result is not complete merely because it was printed in chat.

If the task produces information another agent needs, write the governed result/receipt to the authorized Git branch, validate it, and publish it within the authorized scope. The conversational response should then be only a compact receipt or retrieval pointer.

If publication is not authorized or is technically blocked, stop and report that exact gate or blocker; do not substitute manual owner relay as the normal workflow.

## AI-independence requirement

The workflow must not depend on a particular model remembering earlier conversation state. Operational instructions, scope, evidence, and state transitions must be recoverable from repository artifacts and deterministic tooling.

Agent reasoning may vary, but governed inputs, allowed actions, validation requirements, stop conditions, and durable outputs must remain explicit enough that a different conforming agent can resume the operation from Git.

No repository file can control an agent that has not been given access to or instructed to use this repository. Once an agent is operating on GACP, this file is the mandatory bootstrap entrypoint.

## Minimum operational kit

Once the minimum operational kit is present, use these repository artifacts instead of reconstructing routine checks from conversation history:

- `GACP_File_First_Governed_Handoff_Workflow.md` — owner-approved operating baseline;
- `templates/gacp_operation_manifest.template.json` — parameterized operation definition;
- `templates/gacp_codex_result_receipt.template.json` — durable Codex result/receipt format;
- `bin/gacp` — dependency-free manifest, preflight, scope, safety, exact staging, commit, normal-push, and receipt runner;
- `tests/` — executable read-only and disposable-Git guardrail tests.

The compact entry point is:

`./bin/gacp run <operation-manifest.json>`

Use `./bin/gacp --help` for the narrower validation commands. A manifest grants no authority by itself: its authorization reference and repository evidence must be valid, and the runner stops on mismatched identity, state, hashes, scope, safety findings, or missing approval.
