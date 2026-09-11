# FLOW-APPLIANCE-001 — Evidence

Real-generation evidence for the first appliance multi-state Google Flow / Veo showcase.

## Media bundle status

**V01, V02, and V03 evidence are published. V03 targeted repair passed.**

The repository keeps the uploaded media files as evidence artifacts. GitHub user-attachment URLs are used below for inline video playback so readers can preview the generations directly in the README.

## Quick visual review

### Product reference

![Product reference](reference-product.jpg)

## V01 — Original generation

### Clip 1 — setup / processing

https://github.com/user-attachments/assets/71937adb-04bc-4c5a-8eb2-d10db02e70ea

### Clip 2 — reveal / verdict

https://github.com/user-attachments/assets/90213915-376f-4d0a-9afb-f6f9f1cb88e8

### V01 contact sheet

![V01 contact sheet](v01-contact-sheet.jpg)

V01 established usable product consistency, but the original story was too dense for the tested 8-second-per-generation workflow.

## V02 — Split-clip repair generation

### Clip 1 — ingredient proof / start

https://github.com/user-attachments/assets/aa72da59-b23f-47be-956e-db1ed5cb4193

### Clip 2 — attempted result / verdict

https://github.com/user-attachments/assets/1c47f50f-60c2-4bc7-acf0-50fa75b018b6

### V02 contact sheet

![V02 contact sheet](v02-contact-sheet.jpg)

[Read V02 QA](v02-qa.md)

V02 validates the split-clip strategy but exposes a continuation-state regression in clip 2: the clip reintroduces coarse/raw ingredients before the reveal, then shows the processed result afterward.

## V03 — Targeted continuation-state repair

### Clip 2 — repaired post-processing reveal

https://github.com/user-attachments/assets/b286e7c8-c2ea-4385-b421-6044d13a2cc9

### V03 contact sheet

![V03 contact sheet](v03-contact-sheet.jpg)

- [Read the V03 prompt](v03-clip-2-prompt.md)
- [Read V03 QA](v03-qa.md)

V03 keeps V02 clip 1 unchanged and modifies one major variable only: the continuation clip receives an explicit immutable opening-state contract plus forbidden regressions.

The regenerated clip begins with the salsa already processed under the closed lid, then reveals that same finished state. The V02 causal failure is resolved.

## Repair lifecycle

```text
V01 — temporal overload / weak hero
↓
V02 — native split clips improve execution
↓
V02 clip 2 — continuation-state regression discovered
↓
V03 — immutable opening-state repair
↓
PASS
```

## Provenance

- Generation date: 2026-09-10 to 2026-09-11
- Workflow: Google Flow / Veo
- Tested practical generation duration: 8 seconds per output
- Prompt lineage: `V01 → V02 → V03 targeted clip-2 repair`
- Evaluation result: V03 passed at `15 / 16`; no V04 required for the observed root cause
- Media handling: preserve original-quality or intentionally chosen user uploads for showcase evidence; use user-attachment URLs for README playback

## Storage policy

Preserve showcase evidence at a quality that remains useful for visual inspection. Avoid aggressive recompression merely to make repository uploads smaller.

For README playback, prefer GitHub user-attachment URLs when available. Keep repository media files as the auditable evidence copy unless storage policy changes.

If media size becomes unsuitable for normal Git history, prefer Git LFS or release assets while keeping stable links and lightweight derivatives only when explicitly desired.

## Integrity rule

Do not replace a failed generation with a prettier recreation while keeping the same evidence label. A new generation must receive a new prompt/output revision so the chain remains auditable.
