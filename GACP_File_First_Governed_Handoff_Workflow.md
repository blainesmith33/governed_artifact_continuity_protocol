# GACP File-First Governed Handoff Workflow

## Document control

- Project: Governed Artifact Continuity Protocol (GACP)
- Status: Proposed for owner review
- Draft version: 0.1
- Date: 2026-08-03
- Scope: ChatGPT-approved artifacts transferred to a local Codex environment for governed repository integration
- First validated use case: ACMP–KGI responsibility-boundary integration

## 1. Decision

GACP defines a file-first handoff workflow in which the human owner approves explicit artifact files, those exact files are transferred with cryptographic integrity evidence, and a local integration agent verifies and incorporates them under the destination repository's own rules.

The chat transcript is not the authoritative handoff artifact. The approved file is authoritative for its content, and its recorded SHA-256 digest is authoritative for transfer verification.

Repository changes that require interpretation are not treated as byte-identical copies. They are governed separately as authorized integration changes and require review of the resulting diff before publication.

## 2. Purpose

The workflow exists to preserve continuity between collaborative work in ChatGPT and durable implementation in a local Git repository without relying on copy-and-paste reconstruction.

It provides:

- an exact, downloadable representation of approved content;
- evidence that the local input matches what the owner approved;
- explicit authority boundaries for the authoring and integration environments;
- repository-aware validation before changes are published;
- an audit trail connecting approval, transfer, integration, review, commit, and push;
- clear stop conditions when identity, scope, or repository state cannot be proven.

## 3. Scope boundary

GACP owns the continuity controls for moving an approved artifact between environments. It does not own the subject matter of the artifact or the destination project's architecture.

The destination project retains authority over:

- repository structure;
- generator or template requirements;
- branch and pull-request policy;
- validation commands;
- versioning rules;
- commit and publication policy;
- acceptance of the proposed content into the project.

For ACMP, this means GACP governs the handoff of approved ACMP documents, while ACMP governs their substance and repository integration requirements.

## 4. Roles and authority

### 4.1 Human owner

The human owner:

- approves or rejects artifact content;
- authorizes the intended destination and integration scope;
- reviews any integration that required interpretation;
- authorizes commit and publication;
- resolves conflicts that cannot be decided deterministically.

### 4.2 ChatGPT authoring environment

The authoring environment:

- collaborates with the owner to produce the artifact;
- emits the approved result as an actual file;
- records the filename, byte count, line count when applicable, media type, and SHA-256 digest;
- identifies whether the artifact is an exact destination file or an integration instruction;
- does not claim repository integration has occurred;
- does not silently revise an artifact after approval.

### 4.3 Transfer operator

The transfer operator may be the owner or an approved automated mechanism. The operator moves the files between environments without changing their bytes and preserves their exact filenames where required.

### 4.4 Local integration agent

The local integration agent:

- verifies the transferred input before editing the repository;
- follows destination-repository instructions;
- checks repository identity, cleanliness, branch, remote, and synchronization state;
- performs only the authorized integration;
- validates the resulting repository state;
- stops at every required owner-approval gate;
- reports exact evidence rather than merely stating success.

### 4.5 Destination repository

The destination repository is the durable implementation and version-history system after an authorized commit is created. It does not retroactively replace the approved source file or its handoff evidence.

## 5. Handoff artifact classes

### 5.1 Exact-content artifact

An exact-content artifact is intended to appear at a declared repository path byte for byte.

Requirements:

- its SHA-256 digest must match before integration and after generation or placement;
- no normalization, reformatting, newline conversion, renaming, or content correction is permitted unless the owner approves a new version;
- if a repository generator manages the destination file, the generator must reproduce the approved bytes exactly;
- any mismatch is a stop condition.

### 5.2 Governed integration instruction

A governed integration instruction authorizes bounded changes to existing project files. It is not expected to become a repository file unless explicitly stated.

Requirements:

- it must identify the allowed targets, required changes, exclusions, and validation gates;
- the local integration agent may interpret it only as necessary to apply the authorized change;
- every resulting change must be traceable to a specific authorization in the instruction or an already-applicable repository rule;
- the complete human-readable diff must receive owner review before commit;
- ambiguity that could materially change the result is a stop condition.

### 5.3 Handoff manifest

The manifest identifies every approved input and the properties needed to verify it. The manifest accompanies the source artifacts but is not automatically added to the destination repository.

### 5.4 Owner-review report

When integration changes existing content or generator sources, a read-only review report presents the original and proposed wording, the authority for each change, all interpretations made, and the repository state. It is evidence for owner review, not automatically a repository artifact.

## 6. Artifact lifecycle

The governed lifecycle is:

1. Drafted.
2. Reviewed by the owner.
3. Approved as a specific file version.
4. Packaged with a manifest.
5. Transferred.
6. Hash-verified locally.
7. Integrated into an uncommitted repository state.
8. Validated.
9. Reviewed by the owner when interpretation or multi-file changes occurred.
10. Authorized for publication.
11. Committed and pushed under repository policy.
12. Recorded with final commit and synchronization evidence.

Approval applies only to the exact reviewed version. Any post-approval byte change creates a new candidate version that must be identified, hashed, and approved again.

## 7. Required workflow

### 7.1 Author and approve

1. Produce the proposed artifact as a file, not only as rendered chat text.
2. Mark it as proposed until the owner explicitly approves its wording.
3. After approval, freeze that version for the handoff.
4. Calculate its SHA-256 digest from the actual file bytes.
5. Record its filename, size, and intended integration role.

### 7.2 Package

1. Create a manifest for all approved inputs in the handoff.
2. Distinguish exact-content artifacts from governed integration instructions.
3. Declare the intended repository for every exact-content artifact and either its destination path or that repository inspection is still required before integration.
4. Declare whether each supporting file is repository-bound or handoff-only.
5. Record dependencies between artifacts.

### 7.3 Transfer

1. Transfer the artifact files and manifest through an owner-authorized mechanism.
2. Preserve the bytes and required filenames.
3. Do not treat browser display, chat rendering, or copied text as proof of file identity.
4. If a download system changes a filename, resolve the exact file deliberately; do not guess among duplicates.

### 7.4 Pre-integration gate

Before modifying the destination repository, the local integration agent must:

1. Read applicable repository guidance.
2. Verify every input digest against the approved manifest.
3. Confirm the intended repository path and configured remote.
4. Fetch the intended upstream without silently merging or rebasing.
5. Confirm the current branch and upstream relationship.
6. Confirm the allowed cleanliness state of the worktree and index.
7. Record baseline hashes for explicitly protected files.
8. stop without editing if any required fact cannot be verified.

### 7.5 Integration

The integration agent must:

- add exact-content artifacts only at their authorized paths;
- preserve byte identity where exactness is required;
- apply integration instructions only within their approved scope;
- preserve repository generators, templates, indexes, and other sources of truth;
- avoid unrelated cleanup or opportunistic changes;
- avoid committing or pushing until the applicable review gate is satisfied.

### 7.6 Validation

Validation must include, when applicable:

- a second generator pass proving idempotence;
- generator check mode;
- expected managed-document counts and listings;
- link, heading, table, fence, or schema checks;
- UTF-8 validation;
- line-ending and final-newline validation;
- exact SHA-256 verification for exact-content artifacts;
- protected-file hash comparison;
- repository-specific tests;
- `git diff --check`;
- confirmation that the final diff contains only authorized changes.

### 7.7 Owner review

Owner review is mandatory before commit when:

- an integration instruction was interpreted;
- existing substantive wording changed;
- generator or template sources changed;
- more repository files changed than the exact approved artifact files;
- the owner or repository policy requires review.

The review must use the actual uncommitted repository state. A summary alone is not sufficient when human-readable content changed.

### 7.8 Commit and publication

After approval, the integration agent must:

1. Recheck upstream synchronization and the complete change set.
2. Stage only the authorized files.
3. Inspect the staged file list and staged diff.
4. Commit with an approved or clearly scoped message.
5. Publish through the repository's required branch, pull-request, or direct-push process.
6. Confirm local and remote commit identity.
7. Confirm the final worktree and index state.
8. Return the commit SHA, subject, file list, push result, synchronization evidence, and final status.

## 8. Minimum manifest fields

Every handoff manifest must identify:

- protocol name and manifest version;
- handoff identifier;
- creation date;
- source environment;
- intended destination project and repository;
- artifact filename;
- artifact role;
- integration mode: `exact-content` or `governed-instruction`;
- intended destination path, `handoff-only`, or `pending-repository-inspection` before integration;
- media type;
- byte count;
- SHA-256 digest;
- approval status;
- approval reference or statement;
- dependencies;
- explicitly excluded destinations or actions when needed.

The manifest must not claim approval that has not occurred. A pre-approval delivery package must say that owner review is pending.

## 9. Integrity and version rules

- SHA-256 is the minimum required digest for file identity.
- File identity is determined from bytes, not appearance or filename alone.
- The approved digest must be calculated after the final approved file is written.
- A changed digest means a different artifact version, even if the rendered text looks equivalent.
- Normalizing line endings changes the artifact and is prohibited after approval unless a new version is approved.
- The manifest may be versioned independently, but it must never silently point to different artifact bytes.
- Previous approved artifacts and their evidence may be retained according to the governing retention policy.

## 10. Mandatory stop conditions

The integration agent must stop before modification, staging, commit, or push as appropriate when:

- an approved file is missing;
- a digest does not match;
- the destination repository or remote is not the intended one;
- repository instructions conflict with the handoff;
- the worktree or index contains unexpected changes;
- upstream advanced in a way that invalidates the reviewed baseline;
- an exact artifact cannot remain byte-identical;
- the requested change requires a new architectural or governance decision;
- an instruction is materially ambiguous;
- an unexpected file would need to change;
- validation fails;
- the staged diff differs from the owner-reviewed state;
- publication authority is absent.

A correct stop is a successful governance outcome, not a workflow failure.

## 11. Generator-managed repositories

When the destination repository uses a documentation generator, the generator remains the repository source of truth unless the repository explicitly states otherwise.

For an exact-content artifact:

- the artifact must be added to the generator's managed mapping;
- the generated repository file must match the approved digest;
- the generator listing and index must be updated as required;
- generation must be idempotent;
- preserved unmanaged drafts must remain outside generator control.

For instruction-driven corrections:

- generator templates or managed sources must be updated first;
- generated files must not be hand-edited as a substitute;
- the owner reviews the human-readable result, not a compressed or embedded generator archive.

## 12. Audit evidence

A completed handoff record should preserve:

- approved input filenames and digests;
- manifest version;
- destination repository and branch;
- pre-integration HEAD and upstream state;
- protected-file baseline hashes;
- exact changed-file list;
- validation results;
- owner-review decision when required;
- committed file list;
- commit SHA and subject;
- push result;
- post-publication local and remote synchronization;
- final worktree and index status;
- confirmed exclusions.

The evidence may remain outside the destination repository when repository inclusion would create unnecessary project content. Its storage location and retention are governed separately.

## 13. Non-goals

This workflow does not:

- automatically grant ChatGPT authority to write to GitHub;
- require direct publication to `main`;
- replace repository-specific governance;
- guarantee that approved subject matter is technically correct;
- allow an integration agent to expand scope because a related improvement seems useful;
- treat a hash as proof of semantic quality or owner approval;
- make handoff-only audits, manifests, or instruction packages repository content by default;
- define ACMP, KGI, BGF, or another project's internal architecture.

## 14. First validated application

The workflow was first exercised for the ACMP–KGI responsibility boundary:

- ChatGPT produced an exact ADR file and a governed correction instruction.
- The owner approved both inputs.
- Local Codex stopped safely when the approved files were initially absent.
- After transfer, Codex verified the approved hashes.
- The ADR was integrated byte for byte through ACMP's documentation generator.
- The correction instruction produced a bounded multi-file documentation change.
- A read-only owner-review report exposed the complete human-readable changes.
- The owner approved the uncommitted integration.
- Local Codex committed and pushed exactly the approved 14-file change set.
- ACMP `main` and `origin/main` synchronized at commit `884fa19c0ee5dec0ee9cb876d2e1fb3ec3d6f032`.
- KGI, BGF, and Kimbers Kreations were not inspected or changed.

This precedent validates the workflow pattern. It does not make ACMP-specific paths, generator commands, file counts, or direct-push policy universal GACP requirements.

## 15. Acceptance criteria for this GACP workflow

This proposed workflow is ready for repository integration when the owner confirms that it:

- accurately separates exact-content adoption from instruction-driven integration;
- assigns approval and publication authority to the human owner;
- preserves destination-project governance;
- requires cryptographic verification and explicit repository-state gates;
- treats safe stopping as required behavior;
- requires review of interpreted or multi-file changes;
- records sufficient evidence to reconstruct the artifact's path from approval to publication;
- remains reusable beyond ACMP.

## 16. Next action after approval

After owner approval of this exact document version:

1. Freeze and hash the approved bytes.
2. Update the accompanying manifest from `pending-owner-review` to `approved` without changing this document.
3. Give both files to local Codex as immutable handoff inputs.
4. Have local Codex inspect the GACP repository and determine the correct governed location and any generator or index requirements.
5. Stop before commit for owner review if integration requires any interpretation or additional repository changes.
