# ACMP Knowledge Model and Data Schema readiness assessment

## 1. Executive conclusion

**Assessment status: PASS for bounded specification work; NOT READY for normative serialized schemas or schema-dependent implementation.**

At authoritative ACMP commit `884fa19c0ee5dec0ee9cb876d2e1fb3ec3d6f032`, ACMP has a coherent, accepted conceptual contract baseline. It normatively establishes the runtime capability boundaries, seven shared record concepts, source immutability, evidence-bounded provenance, human authority, Reference ownership, history-preserving lifecycle behavior, explicit compatibility, independent Consumer Packages, and the ACMP/KGI separation.

That baseline deliberately does not choose field names, identifier syntax, status vocabularies, event and edge representations, Knowledge Object update semantics, schema format or dialect, schema identifiers, extension behavior, validation errors, or compatibility algorithms. Those are material design decisions, not mechanical transcription tasks. `docs/schemas/` must therefore remain unpopulated until a bounded shared-contract decision package and the affected subsystem semantic contracts have been reviewed and approved.

No genuine contradiction was found in the authoritative set. The material risks are unresolved ownership seams and representation choices: shared envelope versus subsystem payload, Reference identity versus originating provenance, Protocol lifecycle semantics versus subsystem transitions, human decisions versus Verification Records, and retention-policy deletion versus durable history. These are resolvable ambiguities, not evidence that the accepted architecture must be reopened.

The smallest correct next step is one proposed shared data-contract foundation decision artifact, followed by a prose Data Schema Specification and a dependency-ordered set of subsystem contract decisions. Draft machine schemas should follow those decisions, beginning with a coherent core migration-lineage slice and conformance fixtures. This assessment makes no architecture decision authoritative.

## 2. Verified repository and authority state

- GACP handoff branch: `gacp/acmp-schema-readiness-assessment-20260807`.
- Governed handoff commit: `d29630651dc4772072f665dbd57ba613b5962269`, whose direct parent is the authorized GACP base `8d2006271092b7edc82fe5e1b7049eb5ff1279d4`.
- ACMP repository identity: `blainesmith33/ai_chat_migration_protocol`.
- Freshly fetched ACMP `origin/main`: `884fa19c0ee5dec0ee9cb876d2e1fb3ec3d6f032`, exactly matching the handoff's expected authoritative commit.
- Inspection method: read-only inspection of tracked content at that exact commit. The existing checkout was already at the same commit. Pre-existing owner work was left untouched.
- Authority set read: all 21 managed documentation paths reported by `python3 scripts/bootstrap_acmp_docs.py --list`, including the two architecture documents, ADR-0001 through ADR-0008, and all nine specifications required by the handoff.
- Authority status: the ADRs are accepted; architecture and subsystem documents are authoritative conceptual baselines; `docs/specifications/01_protocol.md` says its semantic contracts are approved. The same documents expressly state that serialized schemas, final fields, detailed state transitions, and conformance tests are not approved.
- The preserved misspelled draft `docs/architecture/decisions/ACMP_System_Archetecture.md` is explicitly unmanaged and non-authoritative and was not used as decision authority.

## 3. Normative-vs-unresolved matrix

| Area | Already authoritative | Unresolved before normative schemas | Primary evidence |
| --- | --- | --- | --- |
| Authority level | Accepted ADRs and authoritative conceptual specifications govern semantics; conceptual, draft, and approved normative schema artifacts must remain distinct. | Approval state, document location, schema release procedure, and promotion rules for future schema artifacts. | `README.md` / **Current Development Status**; `docs/specifications/01_protocol.md` / **Status**; ADR-0007 / **Decision** |
| Shared object taxonomy | Protocol recognizes Source Artifact, Knowledge Candidate, Verification Record, Knowledge Object, Reference Record, workflow execution record, and Consumer Package. No persistent “Verified Knowledge” object exists. | Canonical kind tokens, whether all seven are serialized shared object types, required/conditional occurrence, subtype/profile rules, and the status of manifests/audit context. | Protocol / **Shared Object Contracts**, **Inputs and Outputs**; ADR-0004 / **Decision** |
| Identity | Shared objects identify durable identity and object kind when applicable and available. Reference owns durable identifiers. Derived objects retain their own identity. | Identifier syntax, namespace/issuer, uniqueness scope, stability, logical-object versus version identity, external-ID mapping, collision rules, and minting responsibility. | Protocol / **Minimum Shared Metadata**, **Identity and Lifecycle Rules**; Reference / **Ownership Boundary** |
| Source preservation | Retained Source Artifact content is immutable. Corrections and replacements create linked artifacts or versions. Exclusions do not alter source. | Content/metadata boundary, correction and replacement edge forms, integrity representation, source-region addressing, and minimum retained acquisition fields. | ADR-0002 / **Decision**; Ingestion / **Retained Source Artifacts**, **Integrity Evidence** |
| Deletion and retention | Deletion requires externally authorized retention policy; ACMP retains only policy-permitted deletion-event metadata and records available authority/limitations. | Policy-reference shape, deletion-event/tombstone representation, redaction and unavailable-value behavior, referential behavior after deletion, and retention evidence minimum. | Protocol / **Identity and Lifecycle Rules**; Ingestion / **Retention-Policy Deletion**; Reference / **Lineage Transparency** |
| Human and source authority | Source authority is external to ACMP. Only an authorized human may record a human approval; the subject, action, scope, authority basis, evidence, and limitations are required. Automation cannot infer approval. | Actor/authority identifiers, evidence references, delegation/expiry representation, signature or attestation needs, decision vocabulary, and how a decision is embedded or referenced. | ADR-0006 / **Decision**; Verification / **Human Decision Boundary**; Protocol / **Human Authority and Limitations** |
| Provenance | Originating subsystems own provenance created by their operations. All known inputs, transformations, versions, verification activity, human decisions, and package-selection context remain traceable. Missing/uncertain lineage stays visible. | Common provenance event model, operation identity, input/output cardinality, transformation parameters, granularity, ordering, partial/unknown evidence encoding, and normalization rules. | ADR-0002 / **Decision**; Technical Architecture / **Provenance Architecture** |
| Shared metadata | Shared contracts identify, when applicable and available, identity/kind, contract version, lifecycle/history, inputs/operation context, human authority/decision scope, limitations, and trace references. Invented values are prohibited. | Exact fields; required, conditional, nullable, or unavailable semantics; common envelope boundary; timestamp and actor representation; subsystem extension points. | Protocol / **Minimum Shared Metadata** |
| Lifecycle and history | Correction, versioning, rejection, exclusion, reprocessing, supersession, and authorized deletion preserve ACMP history. Protocol owns shared lifecycle semantics; subsystem specifications own detailed states/transitions. | Common versus object-specific states; event/state model; allowed transitions; terminality; reasons/actors; correction/supersession direction; reactivation; cross-version references. | Protocol / **Identity and Lifecycle Rules**, **Protocol and Subsystem Specification Boundary**; ADR-0003 / **Decision** |
| Versioning and compatibility | Known contract, classification, transformation, verification, selection, and rule versions are identified. Differently versioned contracts cannot be assumed interchangeable. | Version syntax and requiredness, schema/protocol version relationship, compatibility matrix/algorithm, migrations, negotiation, extension policy, and unknown-field handling. | Protocol / **Versioning and Compatibility** |
| References and citations | Reference owns durable identifiers, resolvable citations, cross-object lineage links, and historical relationships; a resolvable reference proves neither truth nor authority. | Reference syntax, resolver behavior, source-region selectors, edge taxonomy/direction/cardinality, broken/deleted targets, integrity binding, and external reference policy. | Reference / **Purpose**, **Ownership Boundary**, **Lineage Transparency** |
| Candidate, verification, knowledge | Candidates are proposed and distinct; Verification Records preserve evaluation/human decisions; eligible candidates may create or update portable Knowledge Objects while all earlier history remains. | Candidate granularity/taxonomy, Verification Record cardinality and decision structure, eligibility calculation/scope, Knowledge Object content model, aggregation, update/version semantics, and conflict representation. | Extraction / **Knowledge Candidates**; Verification / **Verification Records**, **Knowledge Semantics**; Knowledge Model / **Purpose**, **Verification Relationship** |
| Consumer Packages | Packages are independently requested and identify type, intended consumer, selection scope, lineage, disclosures, manifest context, and handoff evidence. Package generation does not create truth or downstream acceptance. | Manifest schema, embed-versus-reference policy, selected-object snapshot/version binding, package profile/version identifiers, validation, serialized formats, and acknowledgment evidence shape. | ADR-0005 / **Decision**; Packaging / **Lineage and Manifest Obligations**, **Handoff Responsibility** |
| Automation | Automation coordinates approved capabilities and records workflow context/gates; it cannot own package semantics or human decisions. | Workflow execution fields, state machine, retry/idempotency semantics, gate-result references, failure model, and correlation with subsystem operations. | Automation / **Coordination Scope**, **Gate Enforcement**, **Boundary** |
| Runtime/subsystem boundaries | Runtime capabilities are Ingestion, Extraction, Verification, Knowledge, Reference, Automation, and Packaging. Protocol and Roadmap are specification domains. Physical co-location may not collapse responsibility boundaries. | Concrete APIs, persistence boundaries, transaction/order behavior, subsystem payload schemas, and processing validation. | System Architecture / **Runtime Capability Boundaries**; Technical Architecture / **Domain Separation** |
| ACMP/KGI boundary | ACMP and KGI have separate repositories, objects, schemas, identifiers, authorities, and lifecycles. Handoff does not imply KGI acceptance or identity equivalence. | No cross-system mapping is in scope. Any adapter, profile, identity mapping, acknowledgment, feedback, or compatibility contract requires a separate approved decision. | ADR-0008 / **Decision**, **Non-decisions** |

## 4. Object and contract responsibility matrix

| Concept | Semantic owner | Normative responsibility now | Required schema work; not yet authoritative |
| --- | --- | --- | --- |
| Source Artifact | Ingestion payload; Protocol invariants; Reference identity/history | Retained authorized source content, acquisition context, limitations, immutable content, linked correction/replacement, policy-bounded deletion. | Content representation, acquisition/authorization fields, integrity evidence, source regions, correction/version links, deletion evidence. |
| Knowledge Candidate | Extraction payload; Protocol invariants; Reference links | Proposed knowledge from identified source regions; distinct identity; extensible/versioned classification; traceable rejection, exclusion, re-extraction, and supersession. | Candidate unit/payload, region citations, taxonomy identifiers, classification instances, exclusion records, status/transition rules. |
| Verification Record | Verification payload; Protocol authority rules; Reference history | Evaluation and human decisions about one or more candidates, including evidence, uncertainty, conflict, limitations, authority, scope, and history. | Record cardinality, evaluation/activity model, decision object or reference, reviewer authority, eligibility outcome, status/transition and supersession model. |
| Knowledge Object | Knowledge payload; Protocol invariants; Reference identity/history | Portable evidence-linked ACMP knowledge created or updated from eligible candidates; retains decision/source lineage; is not organizational truth. | Content/granularity, aggregation, logical/version identity, create/update rules, effective state, uncertainty/conflict projection, correction and supersession behavior. |
| Reference Record | Reference | Durable identity, resolvable citations, cross-object lineage, and correction/version/exclusion/supersession/reprocessing/selection/handoff history. | Identifier and citation syntax, edge registry, edge direction/cardinality, resolver contract, deleted/inaccessible target behavior, normalization provenance. |
| Workflow execution record | Automation | Coordination history, known inputs/transformations/versions, gates, human-decision references, failures, retries, and handoffs without semantic authority. | Execution ID, state machine, attempt/retry model, gate result, operation correlation, error semantics, idempotency. |
| Consumer Package | Packaging; Reference for identity/lineage | Independently requested selection with type, intended consumer, scope, manifest, lineage, disclosures, decisions, reproducibility, and handoff evidence. | Manifest and package profile, snapshot/version binding, embed/reference rules, selection and exclusion entries, serialized format, acknowledgment evidence. |
| Human decision | Verification originates; other records reference within scope; Protocol supplies invariant | Authorized human decision remains distinct from automated activity and carries subject, action, scope, authority basis, evidence, and limitations. | Decide whether it is a nested structure, independently identified record, or both; define actor/authority references, vocabulary, dates, rationale, supersession. |
| Provenance/operation event | Each originating capability; Reference indexes/links | Each capability records what it creates; Reference may normalize/index but may not silently replace or strengthen it. | Common event envelope, input/output references, transformation identity/version, ordering/time, unknown/partial information, normalization linkage. |
| Package manifest | Packaging, with Reference links | Identifies package, selected inputs, transformations/versions, verification, decisions, selection context, links, generation context, limitations, and handoff. | Decide whether it is part of Consumer Package or a separately identified supporting object; define required fields and resolution/integrity rules. |

This matrix does not add object types. Human decisions, provenance events, and manifests are listed as contract concerns because authoritative prose requires their information, while current authority does not decide whether each becomes a standalone serialized object.

## 5. Unresolved decision register with dependencies

| ID | Decision required and why | Constraints and affected contracts | Dependencies / ownership | Risk if premature or wrong |
| --- | --- | --- | --- | --- |
| D01 | Approve the serialized object registry: kind names, required/conditional concepts, profiles/subtypes, and whether supporting structures are standalone. A schema cannot validate object kind or dispatch without it. | Protocol **Shared Object Contracts**, **Inputs and Outputs**; all seven runtime capabilities. Must not add persistent “Verified Knowledge.” | Shared Protocol; first decision. | Accidental new architecture, type proliferation, or missing contract coverage. |
| D02 | Define a common envelope and the envelope/payload ownership line, including required, conditional, unavailable, and prohibited data. | Protocol **Minimum Shared Metadata** and **Protocol and Subsystem Specification Boundary**; every shared object. | Shared Protocol; depends on D01. | Duplicated/conflicting metadata or Protocol taking subsystem-owned fields. |
| D03 | Define durable ID, namespace, issuer, uniqueness, stability, logical/version ID, external-ID mapping, and minting rules. | Reference **Ownership Boundary**; Protocol **Identity and Lifecycle Rules**; all objects and citations. | Shared Protocol/Reference; depends on D01-D02. | Broken lineage, collisions, unstable references, or implicit ACMP/KGI identity equivalence. |
| D04 | Define resolvable citation and reference syntax, source-region selectors, resolution outcomes, and integrity/version binding. | Reference **Purpose**, **Lineage Transparency**; Ingestion source representation; Extraction evidence regions; Packaging manifests. | Shared Reference contract; depends on D03 and Source Artifact content model. | Ambiguous evidence, references that drift between versions, or false resolution guarantees. |
| D05 | Define timestamps, actor references, authority basis, source-authorization evidence, decision scope, and unavailable/expired authority context. | Protocol **Minimum Shared Metadata**, **Human Authority and Limitations**; Ingestion **Authorization Boundary**; Verification **Human Decision Boundary**. | Shared primitives plus Ingestion/Verification payloads; depends on D02-D03. | Automation mistaken for human authority, overclaimed source rights, or unauditable decisions. |
| D06 | Define common lifecycle/event semantics and the division between shared events and subsystem status machines. | Protocol **Identity and Lifecycle Rules**; ADR-0003 **Decision**; all objects. | Shared Protocol first; object transition vocabularies remain subsystem-owned. Depends on D01-D03. | Circular ownership, inconsistent states, history loss, or a shared enum that cannot fit objects. |
| D07 | Define correction, replacement, version, supersession, rejection, exclusion, reprocessing, and deletion relationships, including directionality and effective/current semantics. | ADR-0002 **Decision**; Protocol **Identity and Lifecycle Rules**; Reference **Source and Historical Relationships**. | Shared historical-edge model plus subsystem rules; depends on D03, D06, D08. | Silent overwrite, conflated deletion/exclusion/rejection, or ambiguous current versions. |
| D08 | Define provenance and transformation-event representation, including operation identity/version, inputs/outputs, ordering, granularity, partial results, and explicit unknowns. | Technical Architecture **Provenance Architecture**; all originating specifications; Reference indexing boundary. | Shared event primitives with subsystem payload ownership; depends on D02-D04. | Overstated lineage, duplication that diverges, or provenance stripped of originating meaning. |
| D09 | Define lineage/reference edge registry, direction, cardinality, edge provenance, and behavior for unavailable/deleted targets. | Reference **Ownership Boundary**, **Lineage Transparency**; all derived objects and packages. | Shared Reference; depends on D03-D04, D07-D08. | Non-traversable history, cycles with unclear semantics, or policy leakage after deletion. |
| D10 | Define Verification Record scope/cardinality, evaluation activities, evidence, human-decision representation, eligibility outcome, and later supersession. | Verification **Verification Records**, **Human Decision Boundary**, **Conflict and Uncertainty**; ADR-0004 **Decision**. | Verification contract using D03-D09. Human-decision semantics require explicit owner review. | Confidence becoming approval, decisions detached from scope, or eligibility treated as downstream authority. |
| D11 | Define structured uncertainty, conflict, omission, exclusion, access constraint, and limitation representation and projection rules. | Protocol **Minimum Shared Metadata**; Verification **Conflict and Uncertainty**; Packaging **Conflict, Uncertainty, and Limitation Disclosure**. | Shared minimum plus subsystem detail; depends on D02, D05, D08-D10. | Lossy disclosures, false completeness, or incompatible free-text-only representations. |
| D12 | Define Knowledge Object unit/content model, candidate aggregation, create/update eligibility, logical/version identity, correction, and supersession semantics. | Knowledge Model **Purpose**, **Verification Relationship**, **Authority and Limitations**; ADR-0004. | Knowledge contract; depends on D03, D06-D11. | A mutable “truth” object, erased evidence, duplicate identities, or unclear updates. |
| D13 | Choose serialized format/dialect, media types, canonical schema identifiers, schema resolution, and representation-level integrity needs. | Technical Architecture **Technology and Deployment Deferral**, **Readiness Gate**; ADR-0007. | Shared Protocol decision after semantic D01-D12 requirements are known. | Technology selection becoming accidental architecture or schemas unable to express required constraints. |
| D14 | Define protocol/schema/classification/profile versions, compatibility and negotiation rules, deprecation/migration, extensions, and unknown-field behavior. | Protocol **Versioning and Compatibility**; Extraction **Classification**; Roadmap **Subsystem Contracts**. | Shared Protocol; depends on D01-D03 and D13. | Silent incompatibility, rejected safe extensions, or consumers misreading newer content. |
| D15 | Define validation and error semantics: structural versus semantic versus referential checks, error codes/paths, warning handling, profile validation, and conformance evidence. | ADR-0007 **Consequences**; Roadmap **Conformance, Security, and Retention**; each subsystem's deferred validation responsibility. | Shared conformance baseline plus subsystem checks; depends on D04-D14. | Validators disagree, errors are unactionable, or schema validity is mistaken for semantic approval. |
| D16 | Define Consumer Package manifest and reference behavior without moving selection, approval, reproducibility, or handoff semantics into Protocol. | Packaging **Lineage and Manifest Obligations**, **Handoff Responsibility**; ADR-0005; Automation **Packaging Boundary**. | Packaging-specific contract using shared IDs/references/versions; depends on D03-D15. | Package semantics collapse into generic objects, selected versions drift, or receiver acceptance is inferred. |
| D17 | Define retention-policy references and deletion evidence without encoding a retention schedule or granting ACMP external governance authority. | Ingestion **Retention-Policy Deletion**; Protocol **Identity and Lifecycle Rules**; ADR-0008 boundary. | Shared reference/event minimum plus Ingestion/Reference contract; depends on D03, D05, D07, D09. | Over-retention, forbidden residual metadata, unresolvable history, or false policy authority. |
| D18 | Define Workflow execution records, gates, retry/failure/idempotency semantics, and links to human decisions without moving subsystem meaning into Automation. | Automation **Coordination Scope**, **Gate Enforcement**, **Boundary**. | Automation-specific and may follow the core migration-object schemas; depends on D03, D06, D08, D10, D15. | Orchestration bypasses gates, duplicates operations, or appears to own package/decision semantics. |

## 6. Contradictions, ambiguities, and dependency hazards

### Contradictions that must be resolved

None found in the authoritative authority set.

Source immutability and authorized policy deletion are compatible: immutability prohibits silent rewriting while the accepted policy boundary permits an authorized deletion event with only allowed residual metadata. Similarly, Knowledge Object creation/update and preserved candidate/decision history are compatible, provided future schemas define version identity rather than overwrite history.

### Ambiguities requiring explicit decisions

| Ambiguity | Why it matters | Classification |
| --- | --- | --- |
| Protocol recognizes seven shared concepts, while **Inputs and Outputs** also mentions manifests and audit context. | It is not decided whether those are standalone shared object kinds, nested structures, or outputs outside the shared registry. | D01 object-registry ambiguity. |
| “When applicable and available” governs minimum metadata, while unavailable information must be explicit. | Schemas need a precise distinction among omitted, null, unavailable, inapplicable, redacted, and unknown. | D02/D11 requiredness ambiguity. |
| Reference owns durable identifiers and links, while originating subsystems own their provenance. | Minting, storage, and normalization boundaries are not concrete; careless schemas could make Reference overwrite source meaning. | D03/D08/D09 ownership seam. |
| Protocol owns shared lifecycle semantics; each subsystem owns its states and transitions. | A universal status enum would overreach, but no common event/state minimum would produce incompatible histories. | D06/D07 dependency seam. |
| Verification Records contain human decisions, while shared-object metadata carries human actor/authority/decision scope “where a decision exists.” | It is unclear whether decisions are embedded, referenced, independently identified, or represented by a reusable structure. | D05/D10 representation ambiguity. |
| Versions are recorded “when known,” but compatibility must be explicit. | A normative serialized object needs rules for when schema/contract version is mandatory and what an absent domain-specific version means. | D14 compatibility ambiguity. |
| Knowledge Objects may be created or updated from eligible candidates. | Logical identity, version identity, aggregation, update mechanics, and effective/current state are not defined. | D12 blocking ambiguity. |
| Reference supports history after policy deletion, but only policy-permitted deletion metadata may remain. | Resolution and lineage must tolerate redacted or unavailable targets without violating policy. | D09/D17 policy seam. |
| “Eligible,” “approved,” and conceptual “verified” describe related but scoped ideas. | Their relationship must be explicit so a schema does not convert migration eligibility into truth or downstream authority. | D10/D12 terminology ambiguity. |

### Intentionally deferred subsystem detail

- Source adapters, exact acquisition fields, persistence, and processing rules remain Ingestion work.
- Candidate taxonomies, scoring calibration, fields, and transitions remain Extraction work.
- Reviewer permissions, Verification states/transitions, and validation remain Verification work.
- Knowledge Object fields, persistence, and transitions remain Knowledge work.
- Workflow states, retries, and technology remain Automation work.
- Package formats, provider profiles, and implementation technology remain Packaging work.
- Security, threat/data-handling controls, and external retention-policy interfaces remain required future specification work.

### Harmless terminology or abstraction differences

- “Record concept,” “shared concept,” “conceptual output,” and “object contract” are used at different abstraction levels; current text consistently denies that these labels establish persistence or fields.
- “Correction or replacement creates linked artifacts or versions” intentionally allows the later schema to choose a precise representation; it is not a contradiction.
- The repository structure ADR reserves `docs/schemas/`, while current documentation says no schema document or directory content is established. This is planned structure, not an existing schema claim.
- Similar ACMP/KGI terms do not create a conflict. ADR-0008 expressly scopes each system's objects, authorities, and lifecycles.

### Dependency hazards

1. Defining subsystem payloads before D01-D09 would cause each subsystem to invent incompatible identities, versions, references, history, and provenance.
2. Defining Knowledge Objects before D10 would make eligibility and human decisions implicit and could erase Verification scope.
3. Defining a package schema before stable ID/version/reference rules would make selections non-reproducible or vulnerable to target drift.
4. Defining a global lifecycle enum before object-specific transitions would collapse semantically different rejection, exclusion, supersession, deletion, and handoff states.
5. Selecting a schema technology before semantic constraints are understood could make technology limitations accidental protocol policy.
6. Treating JSON-schema validity or a completed workflow as approval would violate the human-authority invariant.
7. Embedding a KGI mapping, downstream acknowledgment, or external retention schedule in the shared ACMP schema would exceed current authority.

## 7. Recommended bounded specification sequence

### Step 1 — proposed shared data-contract foundation decision

Author one reviewable, non-normative decision proposal first. It should present explicit options and a recommended choice for D01-D09 and D13-D15: object registry; envelope/payload boundary; unavailable-value semantics; IDs and citations; time/actor/authority primitives; lifecycle/history and provenance primitives; serialized schema format and identifiers; evolution/extensions; and conformance/error levels.

These decisions can be grouped because every subsystem depends on them. The proposal must preserve the already-approved ownership line: Protocol defines common invariants, Reference owns durable identity/links/history, and each subsystem owns its fields, states, transitions, validation, and processing.

Owner decision required: approve, amend, or reject the foundation. Drafting and repository evidence collection are mechanical; choosing among representation and compatibility options is not.

### Step 2 — prose shared Data Schema Specification

After Step 1 approval, draft one prose specification that converts the approved choices into testable requirements without yet claiming machine schemas are normative. It should contain:

- the canonical object registry and contract ownership table;
- common envelope and explicit absence/redaction semantics;
- ID, citation, reference, version, compatibility, and extension rules;
- common actor/authority, provenance/event, history-edge, uncertainty/limitation, and validation primitives;
- rules that prevent schema validity, automation, eligibility, or packaging from implying human or downstream approval;
- a schema-module map and conformance plan.

The owner must approve this semantic contract before it is labeled normative. Generator integration and index changes can then be produced mechanically under a later implementation handoff.

### Step 3 — dependency-ordered subsystem contract decisions

Author only the contracts needed for the first coherent migration-lineage slice, in this order:

1. **Reference plus Ingestion:** D03-D09 and D17 applied to identifiers, source citations/regions, Source Artifacts, acquisition/integrity evidence, historical edges, and policy-bounded deletion.
2. **Extraction:** Candidate content/granularity, classifications, exclusions, and source-region links.
3. **Verification:** D10-D11, including evaluation, evidence, conflict/uncertainty, authorized human decisions, eligibility scope, and supersession.
4. **Knowledge:** D12, separately reviewed after Verification because Knowledge Object creation/update depends on eligibility and preserved decision lineage.
5. **Packaging:** D16 after object/version/reference rules are stable; keep package selection, manifest, reproducibility, and handoff semantics Packaging-owned.
6. **Automation:** D18 may follow the core object contracts because coordination records depend on gates and operation references but do not block defining the knowledge objects.

Verification and Knowledge decisions must remain separately reviewable even if drafted in one bounded phase; combining them risks turning evaluation into object authority. Packaging and Automation must also remain separate. External retention-policy rules, security/threat controls, and any named adapter or KGI profile require separate artifacts because they involve authority or integration boundaries beyond generic object shape.

Owner decisions required: approve the human-decision/eligibility model, Knowledge Object identity/update semantics, retention evidence boundary, and Packaging selection/reference contract. Routine examples, tables, schema skeletons, and traceability matrices may be drafted mechanically after their governing choices are approved.

### Step 4 — first population of `docs/schemas/`

Do not populate `docs/schemas/` during Steps 1 or 2. First populate it only after the shared prose contract and the Step 3 core contracts through Knowledge have been approved, and after the owner has approved the schema artifact location and format.

The smallest coherent initial draft schema set is:

- shared definitions/envelope, identity, actor/authority, version, reference, event/provenance, history edge, and limitation structures;
- Source Artifact and Reference Record;
- Knowledge Candidate;
- Verification Record and its human-decision/eligibility structures;
- Knowledge Object.

This is a core end-to-end vertical slice, not a generalized schema platform. Consumer Package/manifest and workflow execution schemas may follow as separately reviewable modules before implementation that depends on them. All initial machine schemas must be labeled draft until owner approval; their existence is not approval.

### Step 5 — conformance evidence and normative approval

Accompany the first draft schemas with:

- positive and negative fixtures for every object kind and shared primitive;
- cross-object referential and lineage tests, including version-bound citations;
- history tests for correction, replacement, rejection, exclusion, reprocessing, supersession, and authorized deletion/redaction;
- tests proving missing/uncertain data stays explicit and invented provenance is rejected;
- human-authority tests proving automated activity cannot satisfy a human-decision requirement;
- compatibility and unknown-field/extension tests across supported versions;
- validation error code/path fixtures and structural-versus-semantic failure distinctions;
- package-selection fixtures later, proving independently requested packages bind selected object versions and preserve disclosures;
- generator manifest/index checks, UTF-8/LF/final-newline checks, schema parser/meta-schema validation, link checks, and idempotence checks.

Only the reviewed prose contracts, machine schemas, conformance fixtures, and approval record together should be promoted to an approved normative schema release. Runtime implementation remains gated only on the particular approved contracts it consumes.

## 8. Explicit owner decisions needed next

The next owner review should decide, in bounded packages:

1. **Foundation scope:** approve the serialized object registry and common-envelope versus subsystem-payload boundary, including how unavailable/inapplicable/redacted information is represented.
2. **Identity and history:** approve identifier/namespace/stability, logical-versus-version identity, citation/reference rules, shared lifecycle/history edges, and provenance-event minimums.
3. **Authority:** approve actor and external-authority references, human-decision representation, eligibility scope, uncertainty/conflict/limitation structures, and the policy-bounded deletion evidence model.
4. **Knowledge semantics:** approve candidate aggregation and Knowledge Object create/update/version/supersession behavior without creating a persistent “Verified Knowledge” object or organizational truth claim.
5. **Serialization and evolution:** choose the schema format/dialect, schema identifiers, protocol/schema version relationship, compatibility rules, extension/unknown-field behavior, and validation/error model.
6. **Subsystem profiles:** approve the Packaging manifest/reference contract and, later, Automation execution contract while preserving their accepted separation.
7. **Artifact governance:** approve where the prose Data Schema Specification and machine schemas live, how the generator manages them, and the criteria for draft-to-normative promotion.

These may be presented in one coordinated review packet, but approval should record each decision independently so a disputed choice does not silently authorize the rest.

## 9. Explicit non-decisions and deferred matters

This assessment does not:

- select JSON, JSON Schema, YAML, Protocol Buffers, a database, a language, or any other representation or implementation technology;
- define field names, enums, identifier syntax, namespace values, timestamps, requiredness, status values, or error codes;
- approve any schema, create an ACMP schema directory, or authorize schema-dependent implementation;
- create a persistent “Verified Knowledge” object;
- decide Knowledge Object granularity, aggregation, mutability, or update semantics;
- approve a named source/consumer adapter, provider-specific package, Migration/RAG pairing, or package serialization;
- define an external retention schedule, override policy-permitted deletion metadata, or grant ACMP governance authority;
- define an ACMP/KGI interface, identity mapping, acknowledgment, compatibility mapping, or lifecycle propagation;
- reopen ADR-0008 or transfer any ACMP responsibility to KGI;
- modify ACMP, merge any GACP branch, or grant final substantive acceptance.

Security/threat modeling, data-handling policy, external retention interfaces, deployment, persistence, migrations, performance, and operational APIs remain future bounded work. They should be specified before implementation that depends on them but should not be pulled into the first shared schema foundation unless needed to constrain the data contract.

## 10. Evidence and citation index

All citations refer to ACMP commit `884fa19c0ee5dec0ee9cb876d2e1fb3ec3d6f032`.

| Path | Authoritative headings used |
| --- | --- |
| `README.md` | **Authority and Scope**; **Design Principles**; **Repository Domains and Runtime Capabilities**; **Current Development Status** |
| `docs/README.md` | **Required Future Work / Data Schema Specification**; **Unmanaged Preserved Draft** |
| `docs/architecture/ACMP_System_Architecture.md` | **Status**; **Specification and Repository Domains**; **Runtime Capability Boundaries**; **Conceptual Processing Relationships**; **Source Preservation and Authorization**; **Provenance and Reference Responsibilities**; **Packaging and Automation**; **Architectural Boundaries**; **Architectural Invariants** |
| `docs/architecture/ACMP_Technical_Architecture.md` | **Domain Separation**; **Contract Responsibilities**; **Conceptual Records**; **Provenance Architecture**; **Preservation and Retention Boundary**; **Packaging and Coordination**; **Adapter Independence**; **Technology and Deployment Deferral**; **Readiness Gate** |
| `docs/architecture/decisions/ADR-0001-repository-structure.md` | **Decision**; **Non-Decisions** |
| `docs/architecture/decisions/ADR-0002-source-preservation-and-lineage.md` | **Decision**; **Consequences** |
| `docs/architecture/decisions/ADR-0003-system-domains-and-runtime-boundaries.md` | **Decision**; **Consequences** |
| `docs/architecture/decisions/ADR-0004-verification-and-knowledge-semantics.md` | **Decision**; **Consequences** |
| `docs/architecture/decisions/ADR-0005-consumer-package-semantics.md` | **Decision**; **Consequences** |
| `docs/architecture/decisions/ADR-0006-source-and-integration-independence.md` | **Decision**; **Consequences** |
| `docs/architecture/decisions/ADR-0007-schema-readiness-gate.md` | **Decision**; **Consequences** |
| `docs/architecture/decisions/ADR-0008-acmp-kgi-responsibility-boundary.md` | **Decision** and all subsections; **Non-decisions**; **Decision authority and future review** |
| `docs/specifications/01_protocol.md` | **Status**; **Protocol Role**; **Shared Object Contracts**; **Minimum Shared Metadata**; **Identity and Lifecycle Rules**; **Versioning and Compatibility**; **Cross-Subsystem Invariants**; **Protocol and Subsystem Specification Boundary**; **Human Authority and Limitations** |
| `docs/specifications/02_ingestion.md` | **Authorization Boundary**; **Adapter Boundary**; **Retained Source Artifacts**; **Retention-Policy Deletion**; **Provenance Responsibility**; **Integrity Evidence**; **Handoff Boundary** |
| `docs/specifications/03_extraction.md` | **Knowledge Candidates**; **Classification**; **Derived-Output Exclusion**; **Extraction Provenance**; **Automated and AI-Assisted Extraction**; **Handoff Boundary** |
| `docs/specifications/04_verification.md` | **Mission**; **Verification Records**; **Knowledge Semantics**; **Human Decision Boundary**; **Conflict and Uncertainty**; **Provenance and Reference**; **Handoff Boundary** |
| `docs/specifications/05_knowledge_model.md` | **Purpose**; **Verification Relationship**; **Authority and Limitations**; **Provenance and Reference**; **Boundary** |
| `docs/specifications/06_automation.md` | **Coordination Scope**; **Packaging Boundary**; **Gate Enforcement**; **Provenance and Reference**; **Boundary** |
| `docs/specifications/07_reference.md` | **Purpose**; **Ownership Boundary**; **Lineage Transparency**; **Source and Historical Relationships**; **Package Relationships**; **Boundary** |
| `docs/specifications/08_roadmap.md` | **Required Specification Work**; **Implementation Sequence**; **Integration Candidates**; **Package Evolution**; **Roadmap Controls** |
| `docs/specifications/packaging.md` | **Conceptual Inputs**; **Independently Requested Consumer-Package Outputs**; **Selection Scope**; **Lineage and Manifest Obligations**; **Conflict, Uncertainty, and Limitation Disclosure**; **Verification and Human-Approval Boundaries**; **Reproducibility Expectations**; **Automation Coordination Boundary**; **Handoff Responsibility** |
| `scripts/bootstrap_acmp_docs.py` | Authoritative managed-document manifest as emitted by `--list` (21 paths). |

## 11. Validation performed

- Fetched ACMP `origin/main` without merge or rebase and verified it exactly equals `884fa19c0ee5dec0ee9cb876d2e1fb3ec3d6f032`.
- Verified the local tracked checkout `HEAD` equals the same commit and did not switch, reset, clean, stage, commit, or push ACMP.
- Read every required authority file at the pinned commit.
- Ran `python3 scripts/bootstrap_acmp_docs.py --list`; it reported the expected 21 managed documents and the assessment covered all 21.
- Distinguished accepted/authoritative conceptual content from explicitly deferred schemas, fields, states, transitions, validation, persistence, and technology.
- Cross-checked each unresolved decision against the Protocol/subsystem ownership boundary and ADR-0008 so recommendations do not transfer authority to Automation, Packaging, KGI, or ACMP itself.
- Reviewed the proposed return for public-safe content: no credentials, secrets, raw transcripts, hidden instructions, private filesystem paths, or unrelated local details are included.
- Markdown structure, whitespace, JSON receipt syntax, exact changed paths, commit lineage, and remote publication are validated as part of the governed return process; final publication evidence is recorded by the containing commit and remote branch.

## 12. Scope, exclusions, and exceptions

- Scope was read-only ACMP architecture and schema readiness plus the two authorized GACP return artifacts.
- ACMP files, index, staging area, branch, history, and remote were not modified.
- KGI, BGF, Kimbers Kreations, and all unrelated repositories were not inspected or modified.
- ADR-0008 was treated as sufficient authority for the ACMP/KGI boundary; no new contradiction was found and the completed audit was not reopened.
- No schemas, implementation, generator changes, pull requests, merges, branch deletions, or destructive operations were performed.
- No exception to the governed handoff was required.
