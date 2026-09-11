# FLOW-APPLIANCE-001 — Evidence

Real-generation evidence for the first appliance multi-state Google Flow / Veo showcase.

## Media bundle status

**Published and browsable through V02; V03 clip-2 repair ready to generate.**

The evidence bundle is committed under canonical names:

- [reference-product.jpg](reference-product.jpg) — resized showcase copy of the supplied product reference.
- [v01-contact-sheet.jpg](v01-contact-sheet.jpg) — sampled frames across the two original generated outputs for fast visual review.
- [v01-clip-1-preview.mp4](v01-clip-1-preview.mp4) — lightweight preview of the V01 setup / processing generation.
- [v01-clip-2-preview.mp4](v01-clip-2-preview.mp4) — lightweight preview of the V01 reveal / verdict generation.
- [v02-contact-sheet.jpg](v02-contact-sheet.jpg) — sampled V02 frames showing the improved split-clip execution and the remaining clip-2 state regression.
- [v02-clip-1-preview.mp4](v02-clip-1-preview.mp4) — lightweight V02 preview: ingredient proof → lid close → processing start.
- [v02-clip-2-preview.mp4](v02-clip-2-preview.mp4) — lightweight V02 preview: attempted post-processing reveal / verdict.
- [v02-qa.md](v02-qa.md) — QA of the V02 outputs, including root-cause diagnosis.
- [v03-clip-2-prompt.md](v03-clip-2-prompt.md) — generation-ready targeted repair for clip 2 only.

The preview media is intentionally compressed for repository browsing. It is evidence of the tested generation, not a training asset or canonical product reference. Full-resolution generation masters are kept outside the lightweight browsing bundle.

## Quick visual review

### Product reference

![Product reference](reference-product.jpg)

### V01 contact sheet

![V01 contact sheet](v01-contact-sheet.jpg)

### V01 generated video previews

- [Watch V01 clip 1 — setup / processing](v01-clip-1-preview.mp4)
- [Watch V01 clip 2 — reveal / verdict](v01-clip-2-preview.mp4)

### V02 contact sheet

![V02 contact sheet](v02-contact-sheet.jpg)

### V02 generated video previews

- [Watch V02 clip 1 — ingredient proof / start](v02-clip-1-preview.mp4)
- [Watch V02 clip 2 — attempted result / verdict](v02-clip-2-preview.mp4)

## V02 review

The V02 split-clip generation validates the decision to give each generation one main physical objective. Clip 1 is materially cleaner and keeps the product, ingredients, lid interaction, and controls readable.

Clip 2 exposes a more specific reusable failure: it regresses to the coarse/raw ingredient state at the beginning, then presents processed salsa only after the lid is removed. This breaks causal state continuity even though product identity remains reasonably stable.

See [V02 generation QA](v02-qa.md) for the diagnosis.

## V03 next experiment

V03 deliberately keeps V02 clip 1 unchanged and modifies one major variable only: the opening state of the continuation clip is made immutable.

Use [V03 clip-2 targeted repair prompt](v03-clip-2-prompt.md) to regenerate **clip 2 only**. V03 passes only if the salsa is already processed before the lid starts opening and remains in that same finished state through the reveal.

## Provenance

- Generation date: 2026-09-10
- Workflow: Google Flow / Veo
- Tested practical generation duration: 8 seconds per output
- Prompt lineage: `V01 → V02 → V03 targeted clip-2 repair`
- Evaluation result: V01 reviewed; V02 generated and reviewed; V03 prepared to test immutable continuation-state locking
- Post-processing for repository previews: resize/compression only; no creative content edits

## Storage policy

Keep still-image previews directly in Git when small. Generated `.mp4` / `.mov` evidence paths are covered by the repository `.gitattributes` Git LFS rules so future showcase video can avoid silently inflating normal Git object history.

For a small representative case, lightweight previews may stay next to the case. If the evidence collection grows substantially, full-resolution masters can move to release assets while this directory retains stable links, contact sheets, and browsing previews.

## Integrity rule

Do not replace a failed generation with a prettier recreation while keeping the same evidence label. A new generation must receive a new prompt/output revision so the chain remains auditable.
