# FLOW-APPLIANCE-001 — Evidence

Real-generation evidence for the first appliance multi-state Google Flow / Veo showcase.

## Media bundle status

**Prepared; binary publish pending.**

The case already records the real-generation observations and V01 → V02 repair. The browsing media bundle has been prepared with the following canonical names and should be published into this directory without changing those names:

- `reference-product.jpg` — resized showcase copy of the supplied product reference.
- `v01-contact-sheet.jpg` — sampled frames across the two generated outputs for fast visual review.
- `v01-clip-1-preview.mp4` — lightweight preview of the setup / processing generation.
- `v01-clip-2-preview.mp4` — lightweight preview of the reveal / verdict generation.

The preview media is intentionally compressed for repository browsing. It is evidence of the tested generation, not a training asset or canonical product reference.

## Provenance

- Generation date: 2026-09-10
- Workflow: Google Flow / Veo
- Tested practical generation duration: 8 seconds per output
- Prompt lineage: `V01` in `../../appliance-multistate-google-flow.md`
- Evaluation result: V01 reviewed; V02 split-clip repair prepared
- Post-processing for repository previews: resize/compression only; no creative content edits

## Storage policy

Keep still-image previews directly in Git when small. Generated `.mp4` / `.mov` evidence paths are covered by the repository `.gitattributes` Git LFS rules so adding more showcase video does not silently inflate normal Git object history.

For a small representative case, publish lightweight video previews through Git LFS. If the evidence collection grows substantially, full-resolution masters may move to release assets while this directory retains stable links, contact sheets, and browsing previews.

## Integrity rule

Do not replace a failed generation with a prettier recreation while keeping the same evidence label. A new generation must receive a new prompt/output revision so the chain remains auditable.
