# Governed Artifact Continuity Protocol (GACP)

The **Governed Artifact Continuity Protocol (GACP)** is a reusable governance and operational framework for preserving approved work as it moves between ChatGPT, GitHub, and local Codex environments.

GACP defines how documents, specifications, decisions, policies, plans, templates, code, and other AI-assisted project artifacts become durable, authoritative project records without losing their approval, ownership, provenance, meaning, integrity, or history.

> **Core question:** How can we prove that the work we approved became the correct durable artifact, in the correct repository, with its meaning, history, and integrity intact?

## Project Status

GACP is currently in the **conceptual and foundational stage**.

Its purpose, boundaries, initial use case, lifecycle, major responsibilities, and relationship to adjacent systems have been defined. Its formal specifications, schemas, procedures, controls, validation tools, and automation have not yet been fully designed or implemented.

This repository therefore represents the foundation of the protocol, not a completed production system.

## Why GACP Exists

Substantial project work can be produced during AI-assisted conversations without ever becoming part of the durable project record.

An important architectural decision may exist in ChatGPT but not in GitHub. A GitHub artifact may not be present in the authorized local clone. A local file may contain uncommitted work. Several similar documents may exist without proof of which is authoritative. An AI assistant may then reason from incomplete repository contents because essential decisions remain trapped in previous conversations.

AI-assisted projects commonly distribute their working knowledge across:

- Active and archived ChatGPT conversations
- Generated or downloaded files
- GitHub repositories, branches, and pull requests
- Local repository clones
- Uncommitted working-tree changes
- Multiple GitHub accounts and repository owners
- Multiple machines and Codex environments
- Decisions remembered by participants but never formally recorded

These environments do not automatically remain synchronized. Without a governed preservation process, approved work can be lost, copied incorrectly, silently rewritten, stored in the wrong repository, duplicated into competing sources of truth, or separated from the evidence needed to understand its origin and authority.

GACP closes this gap by treating artifact preservation as a governed lifecycle rather than an informal act of copying and pasting.

## Mission

GACP provides a repeatable and auditable method for converting approved work into durable, version-controlled project artifacts while preserving the relationship between:

- The artifact
- Its source
- Its owning project
- Its approval
- Its canonical repository location
- Its Git history
- Its remote publication state
- Its local availability
- Its later revisions or supersession

The intended outcome is a project environment in which the repository—not conversational memory—is the durable record of approved artifacts.

ChatGPT may remain the environment in which ideas are explored, language is drafted, systems are designed, and decisions are discussed. Material does not become authoritative merely because it appeared in a conversation. It becomes an official project artifact only through the applicable approval, preservation, validation, and publication process.

## What GACP Governs

GACP is expected to govern the complete path from approved conversational work to a verified project artifact.

### ChatGPT-to-Repository Preservation

The protocol determines the correct project, repository, directory, filename, format, and artifact status before approved content is written into the project record.

Exploratory reasoning, brainstorming, abandoned alternatives, and unapproved drafts remain distinct from authoritative documentation.

### Approval and Authority

GACP requires an identifiable approval point before conversational content becomes an official artifact. A project's governance model determines who can approve an artifact and what form that approval must take.

The protocol must distinguish between approval of:

- Exact wording
- The underlying decision or intent
- A specific adaptation
- A reconstruction from historical material
- A derivative document or summary

AI systems and automation may assist with the process, but they do not silently grant authority to content.

### Content Integrity

When exact preservation is required, GACP must prevent silent rewriting, summarization, normalization, or formatting changes. Integrity may be verified through SHA-256 or another appropriate cryptographic mechanism.

When transformation is intentional, the resulting artifact must disclose what changed and how it relates to the source.

GACP distinguishes among:

- **Exact-content artifacts** — intended to preserve approved source bytes or content exactly
- **Approved adaptations** — intentionally modified versions approved for preservation
- **Reconstructed artifacts** — assembled from incomplete or distributed historical evidence
- **Derivative documents** — new works based on one or more governed sources
- **Summaries** — condensed representations that do not claim exact reproduction

### Repository Placement and Ownership

Every governed artifact belongs to an identified project and must remain in the repository that owns it.

The GACP repository contains the reusable continuity system: protocol rules, lifecycle definitions, schemas, registries, procedures, audit formats, validation requirements, templates, and supporting automation. It does not become a duplicate warehouse for the canonical documentation of every governed project.

### Git and GitHub Controls

GACP governs how artifacts enter version control and how evidence of that transition is preserved. Applicable controls may include:

- Verifying repository identity and working-tree state
- Selecting the correct branch and remote
- Reviewing the intended file and diff
- Separating unrelated changes
- Running required validation
- Creating meaningful commits
- Using pull requests where required
- Recording commit and pull-request identifiers
- Confirming publication to the authorized remote
- Verifying local and remote synchronization

The protocol is adaptable. A small personal repository may permit direct commits to its canonical branch, while a higher-risk project may require feature branches, review, and pull requests.

### Local Codex Synchronization

Publication to GitHub does not prove that the local environment used by Codex contains the artifact.

GACP therefore verifies the authorized local repository path, configured remote, checked-out branch, current commit, working-tree state, divergence from the remote, and availability of required artifacts.

This is essential because local reasoning is only as complete as the project information accessible in the working environment.

### Historical Conversation Recovery

GACP supports the recovery of approved work that exists only in earlier ChatGPT conversations.

Historical recovery must not manufacture certainty. A recovered artifact must disclose whether it is:

- An exact reproduction of identifiable approved content
- A reconstruction assembled from multiple sources
- A later restatement of an earlier decision
- A partial recovery
- An unresolved candidate awaiting human review

If provenance, completeness, or exactness cannot be demonstrated, that limitation remains visible.

### Completeness Audits

GACP compares the artifacts expected to exist with those actually present in their owning repositories.

A completeness audit may identify:

- Artifacts present and verified
- Artifacts present but outdated
- Artifacts stored in the wrong location
- Duplicate or conflicting artifacts
- Artifacts mentioned in conversations but absent from repositories
- Repository files with unclear conversational origins
- Approved decisions that were never documented
- Unresolved drafts
- Artifacts that cannot yet be recovered

The result is an evidence-based account of repository completeness and known gaps—not an unsupported declaration that documentation is complete.

### Project and Repository Registry

GACP is expected to maintain a registry describing governed projects and their repository relationships. Registry data may include:

- Project name, identifier, and purpose
- Responsible owner
- GitHub account or organization
- Canonical repository and branch
- Authorized local repository path
- Documentation locations
- Applicable governance model
- Expected artifact inventory
- Onboarding and audit status
- Known continuity exceptions

This makes multi-project, multi-account, and multi-owner work explicit and reduces the risk of publishing an artifact under the wrong identity or authority.

### Account and Environment Transitions

GACP governs transitions between GitHub accounts, repository owners, machines, local clones, and Codex environments.

Before a transition, the existing state must be understood. Afterward, the new identity, permissions, repository owner, remote, branch, local destination, and ownership boundary must be verified before changes are made.

## Artifact Lifecycle

A mature GACP implementation is expected to define the following lifecycle:

1. **Identified** — Content with potential project value has been located.
2. **Classified** — Project ownership, artifact type, and relationship to existing records have been determined.
3. **Reviewed** — The content has been examined for correctness, relevance, duplication, and sensitivity.
4. **Approved** — An authorized person has approved preservation or a specific adaptation.
5. **Prepared** — The repository file, metadata, and intended location have been established.
6. **Validated** — Applicable structural, content, formatting, and integrity checks have passed.
7. **Committed** — The artifact has entered Git history in the correct repository.
8. **Published** — The authorized commit or pull request has reached the correct GitHub remote.
9. **Synchronized** — Required local repositories contain the published artifact.
10. **Verified** — Evidence confirms that the expected artifact is present and correct.
11. **Maintained** — Later changes follow the applicable versioning and approval rules.
12. **Superseded or Retired** — Obsolete material remains traceable or is removed under an authorized retention policy.

These states must be defined precisely enough that a person or automation can report an artifact's actual condition without implying that unfinished work is complete.

## Core Principles

### Human Authority

AI and automation may assist with drafting, classification, validation, comparison, and repository operations, but authority remains with the authorized human or governance role.

### Repository Ownership

Each project owns its authoritative artifacts. GACP governs continuity without taking ownership away from the project.

### Provenance Without False Certainty

Source and lineage information should be preserved whenever available. Uncertainty must be disclosed rather than concealed.

### No Silent Transformation

Content must not be rewritten, summarized, reformatted, or "improved" during preservation without disclosure and any required renewed approval.

### Verifiable Integrity

Claims about exact content, publication, synchronization, and completeness should be supported by reproducible checks.

### Separation of Draft and Authority

Exploratory conversation remains distinct from approved project documentation.

### Visible Exceptions

Missing sources, failed validation, ambiguous ownership, unresolved conflicts, and incomplete recovery remain visible until resolved or formally accepted.

### Minimal Duplication

Canonical artifacts should have one clearly identified authoritative location. Registries and indexes may reference them without creating uncontrolled competing copies.

### Repeatability

The process should apply consistently across projects, repositories, accounts, owners, machines, and authorized environments.

### Recoverability

Governed state and artifact history should remain recoverable after a tool failure, account transition, machine loss, or interrupted workflow.

## Evidence and Auditability

A governed operation must produce enough evidence for an authorized person or system to understand what occurred. Depending on the operation, that evidence may include:

- Source and approval references
- Target repository paths
- File hashes
- Validation results
- Git diffs
- Commit identifiers
- Branch and remote information
- Pull-request links
- Synchronization results
- Timestamps
- Exceptions and unresolved discrepancies

GACP requires sufficient and honest evidence. It does not demand impossible proof or allow limitations to be hidden.

## Relationship to Other Systems

GACP has a specific responsibility within the broader governed system landscape.

### AI Chat Migration Protocol (ACMP)

ACMP governs the ingestion, extraction, verification, organization, and packaging of knowledge from AI conversations for migration or reuse.

ACMP may produce artifacts that GACP then preserves. GACP does not replace ACMP's knowledge-migration responsibilities.

### Business Governance Framework (BGF)

BGF defines how a business is governed, including roles, authority, policy, operations, compliance responsibilities, knowledge, and AI use.

BGF may determine who has authority to approve a business artifact. GACP then applies the continuity controls needed to preserve it correctly.

### Knowledge Governance Infrastructure (KGI)

KGI governs broader knowledge infrastructure, stewardship, validation, and responsible knowledge handling.

GACP supports KGI by keeping approved knowledge artifacts traceable and available across the environments in which they are created and maintained.

### Governed Project Repositories

Each governed project retains its own documentation. GACP records how repositories are onboarded, verified, audited, and synchronized; it does not replace them.

## Initial Real-World Validation

GACP's first implementation will be the governed recovery and documentation of existing project repositories.

The initial effort is intended to:

1. Establish the GACP repository and foundational governance.
2. Identify and register currently governed projects.
3. Record repository owners, canonical branches, remotes, and authorized local paths.
4. Inspect documentation already present in each repository.
5. Identify artifacts known or expected to exist from prior ChatGPT work.
6. Determine which approved artifacts remain available only in conversations.
7. Recover approved material into the correct owning repositories.
8. Classify reconstruction and provenance limitations honestly.
9. Verify file contents, Git history, remote publication, and local synchronization.
10. Produce evidence of repository completeness and unresolved gaps.
11. Document the onboarding and audit procedure used.
12. Repeat the governed process across Blaine's and Kimberly's GitHub environments under explicit account and ownership controls.
13. Refine the protocol based on problems discovered during real use.

This turns repository recovery from a one-time cleanup into the first practical validation of a reusable continuity system.

## Expected Repository Components

As the project matures, this repository may contain:

- A governing protocol specification
- Artifact lifecycle and classification models
- Approval and authority requirements
- Repository onboarding procedures
- Account and environment transition procedures
- Project and repository registry schemas
- Expected-artifact inventory templates
- Historical conversation recovery procedures
- Completeness-audit templates
- Provenance and lineage record formats
- Integrity-verification procedures
- Branch, commit, review, and pull-request rules
- Local synchronization checks
- Exception and discrepancy ledgers
- Recovery and rollback procedures
- Configuration examples
- Validation scripts
- Audit-report generators
- Constrained automation for repeatable checks

Automation supports the governed process; it does not become the source of governance. Automated actions remain constrained by project ownership, authorization, validation, and audit requirements.

## Codex execution adapter

GACP includes a reversible user-scope Codex profile adapter for governed work that begins in another
repository. It preserves the user's base configuration, supplies the GACP bootstrap path privately,
uses a workspace-based permission profile with a narrow GitHub allowlist, and keeps technical
permissions separate from owner authorization. Setup, verification, disablement, and fresh-session
acceptance are documented in [docs/GACP_Codex_Execution_Adapter.md](docs/GACP_Codex_Execution_Adapter.md).

Public operation manifests use `runtime-repository-root` instead of publishing machine-specific
checkout paths. The runner resolves that token to the repository in which it is invoked and continues
to verify repository, remote, branch, upstream, baseline, scope, and publication authority.

## What GACP Is Not

GACP is not:

- A general AI-chat migration platform
- A business-governance framework
- A replacement for Git or GitHub
- A universal document-management system
- A repository containing copies of every governed project's artifacts
- An automatic declaration that every ChatGPT response is authoritative
- A guarantee of perfect provenance where evidence is unavailable
- Permission for AI systems to publish unapproved content
- A requirement that every project use an identical Git workflow

GACP establishes shared continuity requirements while allowing project-specific controls to reflect ownership, risk, maturity, and operational needs.

## Success Criteria

GACP succeeds when it can answer, with evidence:

- What artifacts should a project contain?
- Which expected artifacts are present?
- Which approved artifacts remain trapped in conversations?
- Which repository owns each artifact?
- Which file is canonical?
- Who approved it?
- Does the repository file match the approved content?
- Has it been committed and published?
- Does the authorized local repository contain it?
- Are conflicting or superseded versions present?
- What remains missing, uncertain, or unresolved?
- Can the process be repeated for another owner or repository without inventing a new workflow?

At the broader level, success means that important work is no longer dependent on the continued accessibility of a particular conversation, account, machine, or AI context. Approved artifacts become durable project assets with traceable history and demonstrable continuity.

## Development Direction

The immediate development priorities are:

1. Define the formal protocol and governance boundary.
2. Define artifact classifications and lifecycle state requirements.
3. Establish project, repository, and expected-artifact registries.
4. Create repository onboarding and environment-verification procedures.
5. Define historical recovery and completeness-audit workflows.
6. Establish provenance, integrity, exception, and evidence formats.
7. Validate the protocol through existing repository recovery.
8. Introduce automation only after the governed manual process is understood and repeatable.

## Summary

GACP ensures that approved AI-assisted work survives beyond the conversation in which it was produced.

It establishes a controlled path from ChatGPT to the correct project repository, through GitHub, and into synchronized local Codex environments. Throughout that path, it preserves approval, ownership, provenance, integrity, version history, and audit evidence.

GACP is ultimately a continuity protocol for turning approved conversational work into durable, verifiable project assets.
