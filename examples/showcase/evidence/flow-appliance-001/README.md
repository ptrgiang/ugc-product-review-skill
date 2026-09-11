# FLOW-APPLIANCE-001 — Evidence

Real-generation evidence for the first appliance multi-state Google Flow / Veo showcase.

## Media bundle status

**V02 media temporarily removed for manual high-quality re-upload.**

The evidence bundle currently contains:

- [reference-product.jpg](reference-product.jpg) — product reference used by the case.
- [v01-contact-sheet.jpg](v01-contact-sheet.jpg) — sampled frames across the original V01 outputs.
- [v01-clip-1-preview.mp4](v01-clip-1-preview.mp4) — V01 setup / processing generation.
- [v01-clip-2-preview.mp4](v01-clip-2-preview.mp4) — V01 reveal / verdict generation.
- [v02-qa.md](v02-qa.md) — QA of the V02 outputs, including the state-continuity failure and root-cause diagnosis.
- [v03-clip-2-prompt.md](v03-clip-2-prompt.md) — targeted V03 repair prompt for clip 2 only.

The previously generated lightweight V02 media files were removed because their repository copies were too heavily compressed. V02 images and video will be uploaded manually at the intended quality rather than regenerated or recompressed by the assistant.

## Quick visual review

### Product reference

![Product reference](reference-product.jpg)

### V01 contact sheet

![V01 contact sheet](v01-contact-sheet.jpg)

### V01 generated video previews

- [Watch V01 clip 1 — setup / processing](v01-clip-1-preview.mp4)
- [Watch V01 clip 2 — reveal / verdict](v01-clip-2-preview.mp4)

## V02 review

The V02 split-clip generation validates the decision to give each generation one main physical objective. Clip 1 is materially cleaner and keeps the product, ingredients, lid interaction, and controls readable.

Clip 2 exposes a more specific reusable failure: it regresses to the coarse/raw ingredient state at the beginning, then presents processed salsa only after the lid is removed. This breaks causal state continuity even though product identity remains reasonably stable.

See [V02 generation QA](v02-qa.md) for the diagnosis.

### V02 media status

The V02 contact sheet and both V02 video files are intentionally absent until the original-quality media is uploaded manually.

## V03 next experiment

V03 deliberately keeps V02 clip 1 unchanged and modifies one major variable only: the opening state of the continuation clip is made immutable.

Use [V03 clip-2 targeted repair prompt](v03-clip-2-prompt.md) to regenerate **clip 2 only**. V03 passes only if the salsa is already processed before the lid starts opening and remains in that same finished state through the reveal.

## Provenance

- Generation date: 2026-09-10
- Workflow: Google Flow / Veo
- Tested practical generation duration: 8 seconds per output
- Prompt lineage: `V01 → V02 → V03 targeted clip-2 repair`
- Evaluation result: V01 reviewed; V02 generated and reviewed; V03 prepared to test immutable continuation-state locking
- Media handling: preserve original-quality user uploads for showcase evidence; do not silently replace them with heavily compressed previews

## Storage policy

Preserve showcase evidence at a quality that remains useful for visual inspection. Avoid aggressive recompression merely to make repository uploads smaller.

If media size becomes unsuitable for normal Git history, prefer Git LFS or release assets while keeping stable links and lightweight derivatives only when explicitly desired.

## Integrity rule

Do not replace a failed generation with a prettier recreation while keeping the same evidence label. A new generation must receive a new prompt/output revision so the chain remains auditable.
