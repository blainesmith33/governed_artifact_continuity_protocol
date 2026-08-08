# blAIne AV Studio — first visible wordmark particle proof authorization

## Control

- Protocol: Governed Artifact Continuity Protocol (GACP)
- Date: 2026-08-08
- Target project: blAIne AV Studio
- Target repository: `blainesmith33/blAIne_av_studio`
- Canonical base branch: `main`
- Required base commit: `790798904db67391961644504cb98468d060782f`
- Governing particle-core merge result commit: `0949a43c48c7ac67fc176aa31f687aeeef729af8`
- Operation class: bounded implementation proof on a separate governed branch
- Owner decision: approved direction
- Target outcome: deterministic particles visibly assemble into the `blAIne` wordmark

## Owner authorization and selected first creation

After the accepted particle core was merged and independently reviewed, the owner instructed that work continue step by step until the studio is usable. The owner then selected the supplied `blAIne` wordmark image as the first particle generation.

This authorizes the next bounded implementation slice described here. It does not authorize a merge into `main`; substantive acceptance and merge remain later owner gates.

## Visual intent

Create a reproducible demonstration in which particles begin dispersed over a dark background, travel inward, and assemble into the complete `blAIne` wordmark.

The visible target is:

- the full word `blAIne`, preserving that exact capitalization;
- pale white/light-gray particles for `bl` and `ne`;
- cyan/blue particles for the central `AI`;
- a restrained blue glow around `AI`;
- the completed wordmark held clearly on screen;
- a deterministic restart/replay that produces the same particle placement and motion from the same seed.

The implementation must describe the checked-in target representation honestly. If the original uploaded raster is not available as a repository/workspace asset, create a clearly documented provisional repository-native mask that follows the composition above; do not claim pixel-exact reproduction of an unavailable source. Record that asset-fidelity limitation in the result without blocking the visible proof.

## Objective

Starting from authoritative `main` at the required base commit, create a separate governed implementation branch and deliver the smallest Steam Deck-compatible visible rendering proof that consumes the existing deterministic particle core and forms the selected wordmark.

The result must be directly launchable as a demonstration, not merely a renderer library or an offline data conversion.

## Mandatory bootstrap and preconditions

Before substantive work:

1. Verify target and GACP repository identities, remotes, branches, upstream state, and worktree/index state.
2. Read target `AGENTS.md`, GACP `AGENTS.md`, and the current GACP workflow completely.
3. Read the governing merge result at commit `0949a43c48c7ac67fc176aa31f687aeeef729af8`.
4. Fetch relevant remotes without silently merging or rebasing.
5. Confirm local and remote authoritative `main` resolve to `790798904db67391961644504cb98468d060782f`.
6. Confirm the existing particle-core behavior and tests pass before implementation.
7. Inspect the actual Steam Deck build environment and existing repository structure before selecting the minimal rendering integration.
8. Create and publish a separate governed working branch; do not implement directly on `main`.
9. Stop on a material state mismatch, sensitive-publication concern, requirement for force/history rewriting, or inability to obtain a viable window/render surface without broad dependency or system mutation.

## Authorized implementation scope

The slice may add only what is needed for the first visible proof:

- a window and basic 2D render surface;
- a minimal Steam Deck-compatible rendering integration;
- conversion from deterministic particle state/targets to screen-space draw data;
- a checked-in, deterministic wordmark target mask or equivalent repository-native representation;
- deterministic target assignment and target-directed motion sufficient to assemble the wordmark;
- particle color, size, opacity, lifetime/hold behavior, and simple fading;
- restrained cyan/blue glow for the `AI`, using basic blending or a similarly small technique;
- a fixed demo scene with a stable seed and a documented launch command;
- a replay/restart control;
- focused tests for mask interpretation, deterministic target generation/assignment, and CPU-to-draw-data conversion;
- minimal CMake and documentation changes required by the slice.

Prefer an already available system rendering library suitable for a basic 2D proof. If a new dependency is necessary, keep it narrowly scoped, document its source and license, and do not vendor large frameworks or mutate the operating system. Stop for a new owner gate if the viable choice would materially expand architecture, licensing, or installation scope.

## Required behavior

A successful run must:

1. open a visible window on the Steam Deck desktop;
2. show particles initially dispersed against a dark background;
3. animate them into a recognizable `blAIne` wordmark;
4. distinguish the blue `AI` from the pale surrounding letters;
5. hold the assembled result long enough to inspect;
6. restart deterministically through a simple input;
7. exit cleanly;
8. preserve the existing particle-core tests and semantics unless a strictly compatible extension is required and tested.

## Required validation

Before publication:

- perform a clean out-of-tree configure and build;
- run all CTest tests;
- repeat deterministic tests enough to demonstrate stable results;
- run the existing studio smoke check;
- launch the visible demo in the actual Steam Deck graphical environment and verify window creation, animation, final hold, restart, and clean exit;
- capture durable non-sensitive evidence of runtime success, preferably a screenshot of the assembled state plus concise reproduction details, when the environment permits;
- verify the target representation, color classification, and target assignment tests;
- inspect and document any new runtime/build dependency and license;
- verify no excluded subsystem was introduced;
- run diff and repository-safety checks;
- verify the working branch and its remote resolve to the same commit and the worktree/index are clean apart from predeclared ignored state.

If automated execution cannot visually assess recognizability, report that exact limitation and provide the strongest available screenshot/runtime evidence for owner review. Do not self-accept the visual result.

## Explicit exclusions

This operation does not authorize:

- merge into `main`;
- a general-purpose renderer architecture or rendering API abstraction layer;
- GPU particle simulation, compute shaders, elaborate shader systems, 3D rendering, camera systems, or post-processing pipelines;
- an editor UI or general emitter-control panel;
- audio loading, playback, analysis, reactivity, or master timeline work;
- project save/load, asset browser/import pipelines, AI features, export/video rendering, deployment, or networking;
- broad refactoring unrelated to the visible proof;
- operating-system package mutation, large vendored frameworks, or unrelated third-party dependencies;
- destructive Git actions, branch deletion, amend, squash, rebase, force-push, or history rewriting.

## Durable result requirement

Publish a substantive result through GACP under `handoffs/codex/2026-08-08/` (or the current date-equivalent directory if execution crosses a date boundary). Record:

- target base, working branch, and implementation commit;
- exact changed-file scope;
- rendering integration and dependency/license decision;
- target-mask provenance and whether it is exact or provisional;
- implemented behavior;
- build, CTest, deterministic, smoke, runtime, screenshot/evidence, exclusion, cleanliness, and remote-synchronization results;
- any visual-review limitations, blockers, or exceptions;
- the next owner gate.

Publication of the implementation branch and GACP result branch by ordinary non-force push is authorized when validation passes.

## Stop conditions and next gate

Stop without merging to `main` after publishing the implementation and durable result.

The next gate is owner substantive review of the actual visible wordmark proof. The owner may accept it, request visual revision, provide/replace the exact source asset, or reject the rendering/dependency choice. Only a later explicit authorization may merge the implementation into `main` or begin authoring controls, audio, timeline, or export work.

## Completion response

Keep the conversational receipt compact. Include only:

- implementation branch and commit;
- visible runtime and validation status;
- target-mask provenance (`exact` or `provisional`);
- durable GACP result path and commit;
- blocker if any;
- next genuine owner gate.

Do not require the owner to relay the substantive result when it is retrievable from Git.
