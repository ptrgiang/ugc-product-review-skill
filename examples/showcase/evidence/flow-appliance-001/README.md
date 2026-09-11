# FLOW-APPLIANCE-001 — Evidence

Real-generation evidence for the first appliance multi-state Google Flow / Veo showcase.

## Media bundle status

**Published and browsable.**

The evidence bundle is committed under canonical names:

- [reference-product.jpg](reference-product.jpg) — resized showcase copy of the supplied product reference.
- [v01-contact-sheet.jpg](v01-contact-sheet.jpg) — sampled frames across the two original generated outputs for fast visual review.
- [v01-clip-1-preview.mp4](v01-clip-1-preview.mp4) — lightweight preview of the V01 setup / processing generation.
- [v01-clip-2-preview.mp4](v01-clip-2-preview.mp4) — lightweight preview of the V01 reveal / verdict generation.
- [v02-qa.md](v02-qa.md) — QA of the regenerated split-clip V02 outputs, including the state-continuity failure and targeted clip-2 repair.

The preview media is intentionally compressed for repository browsing. It is evidence of the tested generation, not a training asset or canonical product reference.

## Quick visual review

### Product reference

![Product reference](reference-product.jpg)

### V01 contact sheet

![V01 contact sheet](v01-contact-sheet.jpg)

### Generated video previews

- [Watch V01 clip 1 — setup / processing](v01-clip-1-preview.mp4)
- [Watch V01 clip 2 — reveal / verdict](v01-clip-2-preview.mp4)

### V02 review

The V02 split-clip generation has now been reviewed. Clip 1 substantially validates the split-clip strategy, while clip 2 exposes a reusable continuation-state failure: it regresses to coarse/raw ingredients before revealing the processed salsa.

See [V02 generation QA](v02-qa.md) for the root-cause diagnosis and repaired opening-state rule.

## Provenance

- Generation date: 2026-09-10
- Workflow: Google Flow / Veo
- Tested practical generation duration: 8 seconds per output
- Prompt lineage: `V01` and `V02` in `../../appliance-multistate-google-flow.md`
- Evaluation result: V01 reviewed; V02 generated and reviewed; clip 2 targeted repair required
- Post-processing for repository previews: resize/compression only; no creative content edits

## Storage policy

Keep still-image previews directly in Git when small. Generated `.mp4` / `.mov` evidence paths are covered by the repository `.gitattributes` Git LFS rules so future showcase video can avoid silently inflating normal Git object history.

For a small representative case, lightweight previews may stay next to the case. If the evidence collection grows substantially, full-resolution masters can move to release assets while this directory retains stable links, contact sheets, and browsing previews.

## Integrity rule

Do not replace a failed generation with a prettier recreation while keeping the same evidence label. A new generation must receive a new prompt/output revision so the chain remains auditable.
