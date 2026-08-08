# blAIne AV Studio — accepted definition merge and particle-first implementation authorization

## Control

- Protocol: Governed Artifact Continuity Protocol (GACP)
- Date: 2026-08-08
- Target project: blAIne AV Studio
- Target repository: `blainesmith33/blAIne_av_studio`
- Canonical branch: `main`
- Accepted continuity baseline: `6c6398ae69b0675cd322efda79a5f05619f29553`
- Accepted candidate definition commit: `96e55257d3d308d2928f09f27c678f1a72bfab7e`
- Accepted candidate branch: `gacp/blaine-av-studio-design-history-project-definition-20260808`
- Owner acceptance record: `handoffs/chatgpt/2026-08-08/blAIne_AV_Studio_Candidate_Definition_Acceptance_and_Particle_First_Direction_2026-08-08.md`
- Owner acceptance record commit: `7210e10cac6c78bd5457baf0c907b6d95d62fd73`
- Operation class: governed merge of accepted documentation followed by bounded particle-engine-first implementation preparation
- Owner decision: approved

## Owner authorization

The owner has explicitly accepted the candidate project definition and architecture and explicitly established the particle engine as the first implementation priority. The owner then instructed: `do it`.

This authorizes the bounded actions in this handoff without requiring separate owner approval for each routine mechanical step, provided all preconditions and validation gates pass and scope is not expanded.

## Objective

1. Integrate the already accepted project-definition documentation from candidate commit `96e55257d3d308d2928f09f27c678f1a72bfab7e` into authoritative `main` using a non-destructive repository-approved mechanism.
2. Verify authoritative publication and synchronization.
3. Establish the next bounded implementation operation so development begins with the particle-engine foundation first.

This handoff does not authorize broad AV Studio implementation. It authorizes only the accepted documentation merge and preparation/execution of the first minimal particle-engine slice defined below.

## Mandatory bootstrap

Before acting:

1. Verify repository identity, remote, branch/ref state, upstream state, and worktree/index state.
2. Read target `AGENTS.md` completely.
3. Read GACP `AGENTS.md` completely.
4. Read the accepted candidate documentation at commit `96e55257d3d308d2928f09f27c678f1a72bfab7e`.
5. Read the owner acceptance record at commit `7210e10cac6c78bd5457baf0c907b6d95d62fd73`.
6. Fetch `origin` without silently merging or rebasing.
7. Confirm `main`/`origin/main` are synchronized and descend from accepted baseline `6c6398ae69b0675cd322efda79a5f05619f29553`.
8. Confirm the candidate branch still resolves to `96e55257d3d308d2928f09f27c678f1a72bfab7e` and contains only the accepted documentation changes.
9. Stop on any material mismatch.

## Phase A — accepted documentation integration

If all gates pass:

- Integrate candidate commit `96e55257d3d308d2928f09f27c678f1a72bfab7e` into `main` through an ordinary non-force mechanism compatible with repository policy.
- Do not rewrite accepted history.
- Do not force-push.
- Do not delete the candidate branch.
- Do not opportunistically edit the accepted documentation during merge.
- Verify local HEAD, upstream, and authoritative remote SHA after publication.
- Re-run documentation integrity and scope validation after integration.

## Phase B — first implementation slice: particle-engine foundation

Only after Phase A is successfully integrated and verified, begin the first implementation slice on a dedicated governed working branch.

### Authorized implementation goal

Create the smallest coherent particle-engine foundation that proves the project can represent, update, and execute a particle simulation through deterministic engine abstractions without yet selecting or implementing a graphics API.

### Authorized scope

The implementation may add or modify only what is necessary to establish a non-rendering particle core, including:

- particle data/state representation;
- emitter configuration/state;
- deterministic spawn/update/lifetime behavior;
- position/velocity/acceleration integration;
- particle-system container/update lifecycle;
- stable engine-facing interfaces for creating and updating a particle system;
- unit or lightweight executable tests validating deterministic particle behavior;
- CMake updates required to build and run those tests;
- minimal documentation describing the implemented particle-core boundary and current non-rendering limitation.

### Explicit exclusions

This phase does NOT authorize:

- Vulkan, OpenGL, DirectX, Metal, WebGPU, or any rendering-backend selection or implementation;
- shader implementation;
- GPU compute;
- particle rendering;
- editor UI;
- audio implementation;
- master timeline implementation beyond any minimal time-step abstraction strictly required by the particle tests;
- AI features;
- asset system implementation;
- export/deployment implementation;
- networking;
- third-party dependency introduction unless already present and specifically required by repository policy;
- broad refactoring of unrelated existing scaffold code;
- license selection/change;
- merge of the particle implementation branch to `main` without a later owner acceptance/merge authorization gate.

## Particle-core acceptance evidence

The first particle slice should demonstrate at minimum:

1. a particle can be spawned with deterministic initial state;
2. update with a fixed timestep changes position/velocity according to the defined integration rule;
3. lifetime/expiry works deterministically;
4. emitter behavior can produce a reproducible particle count/state under fixed configuration and timestep;
5. tests/build pass in the available Steam Deck development environment;
6. implementation remains independent of any graphics backend;
7. changed files remain within the authorized particle/core/test/build/documentation scope.

If a technical choice is required that would materially constrain future architecture and is not already determined by the accepted documentation, stop and record it as an open decision rather than silently deciding it.

## Publication model

- Phase A may publish authoritative `main` as explicitly authorized above.
- Phase B must use a dedicated governed working branch and may normally push that branch if validation passes.
- Phase B must not merge to `main` without a separate owner substantive acceptance and merge authorization.

## Durable result requirement

Publish substantive result/receipt artifacts through GACP under `handoffs/codex/2026-08-08/` or the current date-equivalent path if execution crosses a date boundary.

The durable result must separately record:

- Phase A merge/publication outcome and resulting `main` SHA;
- Phase B branch, commit SHA, changed files, tests/validation, and exact implemented particle-core behavior;
- confirmation that rendering/audio/editor/AI/export work remained out of scope;
- any blocker or unresolved architectural decision;
- the next genuine owner gate.

## Completion response

Keep the conversational receipt compact. Include only:

- authoritative `main` SHA after accepted documentation integration;
- particle implementation branch and commit SHA if Phase B completed;
- durable GACP result path/commit;
- validation status;
- blocker if any;
- next genuine owner gate.

Do not ask the owner to relay substantive results between Codex and ChatGPT.
