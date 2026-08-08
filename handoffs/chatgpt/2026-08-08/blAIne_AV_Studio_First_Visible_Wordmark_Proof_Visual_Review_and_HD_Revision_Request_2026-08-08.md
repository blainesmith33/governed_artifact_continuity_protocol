# blAIne AV Studio — First Visible Wordmark Proof Visual Review and HD Revision Request

## Document control

- Protocol: GACP
- Date: 2026-08-08
- Owner: Blaine Smith
- Target repository: `blainesmith33/blAIne_av_studio`
- Reviewed implementation branch: `gacp/blaine-av-studio-visible-wordmark-particle-proof-20260808`
- Reviewed implementation commit: `1c218588b17bdf41307b69f821f8a079d029e27f`
- Governing result commit: `4040934e152351c45d5b2cf6bc1b53a310b22c5e`
- Target `main` baseline: `790798904db67391961644504cb98468d060782f`
- Decision: revision requested; merge not authorized

## Owner assessment

The first visible proof is technically successful and visually interesting as an early dot-matrix particle experiment. It proves that the accepted deterministic particle core can drive a visible SDL window, move scattered particles into assigned targets, hold an assembled state, restart deterministically, render two color groups, and capture repeatable framebuffer evidence on the Steam Deck.

It does not reproduce the selected `blAIne` wordmark at the intended quality. The owner expects HD visuals and a faithful, high-density particle representation of the supplied artwork. The current result must not be merged into `main` as the accepted wordmark implementation.

The existing branch and commit should be preserved as historical proof and may later remain available as an alternate coarse or dot-matrix visual style.

## Evidence-based reason for revision

The published result establishes that the demo:

- renders at 960 by 540 rather than the Steam Deck's native 1280 by 800;
- uses a provisional repository-native mask because the original raster was unavailable;
- represents the wordmark with a 35-by-7 grid containing only 86 occupied cells;
- expands those cells into only 774 particle targets;
- explicitly makes no pixel-exact claim.

Those choices explain the coarse, simplified letterforms. Enlarging the current mask or window would not restore the missing source detail.

## Required source asset gate

The next implementation must derive its target positions, colors, and opacity from the actual owner-selected `blAIne` logo raster or an owner-approved equivalent source asset.

Before implementation begins, the executing agent must identify and hash the exact source file and record:

- source path or repository path;
- media type and dimensions;
- byte size;
- SHA-256 digest;
- whether the asset is authorized for publication in the target repository.

If the exact source asset is unavailable, ambiguous, corrupted, or not publication-authorized, the agent must stop and report that prerequisite. It must not invent another hand-authored logo mask or claim visual fidelity to an unavailable source.

## HD revision requirements

Once the exact source asset is available and verified, the revised slice must:

1. Default to a 1280-by-800 Steam Deck presentation and use the actual drawable framebuffer dimensions.
2. Preserve the source artwork's aspect ratio, proportions, capitalization, spacing, contours, colors, and alpha silhouette.
3. Derive particle targets from visible source pixels rather than a hand-authored character grid.
4. Provide a literal one-particle-per-meaningful-source-pixel mode where practical.
5. Provide deterministic adaptive-density modes so preview quality and performance can be balanced without changing the underlying artwork.
6. Use resolution-independent target coordinates so the same scene can target at least 1920 by 1080 production output, with a path to 2560 by 1440 and 3840 by 2160.
7. Use smooth particle primitives or an efficient batched/instanced equivalent rather than visually coarse X-shaped or block-cell glyphs.
8. Reproduce pale white/gray outer lettering and cyan/blue `AI` coloring from the source asset.
9. Create restrained blue glow with bounded layered rendering or another measured technique that does not require an expensive blur per particle.
10. Preserve deterministic scattered starts, assembly, final hold, replay, and clean exit.
11. Produce native 1280-by-800 assembled-state screenshot evidence and record its dimensions and SHA-256 digest.
12. Record particle counts, density mode, frame timing, and observed runtime behavior on the Steam Deck.
13. Include focused nonvisual tests for asset sampling, aspect-ratio placement, deterministic target generation, density selection, color/alpha preservation, restart behavior, and invalid inputs.
14. Require substantive owner visual review. Build, test, runtime, and screenshot checks cannot self-accept brand fidelity.

## Architectural expectation

The Steam Deck is sufficient for this revision. The design should use efficient batched GPU drawing, point sprites, instancing, or an equivalently appropriate approach for dense real-time preview. If full-density 1080p or 4K output cannot run in real time, the architecture may support slower-than-real-time offline rendering later; that limitation is not grounds to reduce the authoritative artwork to a coarse mask.

Any rendering-backend or dependency choice beyond the existing narrow SDL demonstration must be justified, bounded to this slice, documented with license and system-impact evidence, and treated as provisional unless separately accepted.

## Exclusions

This review does not authorize:

- merging `1c218588b17bdf41307b69f821f8a079d029e27f` or any revision into `main`;
- deleting or rewriting the existing proof branch;
- editor UI or general emitter-authoring controls;
- audio playback, analysis, reactivity, or master-timeline work;
- project save/load, asset browsing, AI tools, export, deployment, or networking;
- GPU particle simulation unless independently necessary, justified, and explicitly authorized;
- unrelated renderer architecture or repository refactoring;
- force-push, rebase, squash, amend, history rewrite, or branch deletion.

## Next gate

The immediate prerequisite is identification of the exact owner-selected logo source asset and confirmation that it may be used and published for this project.

After that prerequisite is durably specified, a separate bounded GACP authorization may permit Codex to implement the HD image-derived revision on a new governed branch. The revised result must stop for owner visual review before any merge into `main`.
