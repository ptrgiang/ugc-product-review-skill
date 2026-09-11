# Real-generation showcase

This directory contains proof cases where the skill is evaluated against an actual video-generation workflow.

The showcase is intentionally separate from `skills/`. The installable skill should stay focused on instructions and reusable references; testing history, output evidence, and iteration logs belong here.

## Featured case

### FLOW-APPLIANCE-001 — Google Flow / Veo appliance multi-state UGC

**Current status:** completed repair lifecycle; **V03 PASS**.

**V01 QA:** `13 / 16`

**V01 lesson:** the original ~12-second story did not fit the tested 8-second-per-generation workflow cleanly. Recompiling as two native 8-second clips improved temporal and physical reliability.

**V02 result:** clip 1 is materially cleaner, but clip 2 regresses to coarse/raw ingredients before the lid opens, then shows processed salsa afterward.

**V02 failure tags:** `STATE_DISCONTINUITY`, `NO_CAUSAL_TRANSITION`, minor `LID_GEOMETRY_DRIFT`.

**V03 repair:** keep V02 clip 1 unchanged and enforce an immutable post-processing opening state in clip 2. The finished salsa must exist before frame 1 and remain unchanged through lid opening.

**V03 QA:** `15 / 16` — PASS. The continuation-state regression is resolved; no V04 is required for this root cause.

### Evidence preview

#### V01

**Clip 1 — setup / processing**

https://github.com/user-attachments/assets/71937adb-04bc-4c5a-8eb2-d10db02e70ea

**Clip 2 — reveal / verdict**

https://github.com/user-attachments/assets/90213915-376f-4d0a-9afb-f6f9f1cb88e8

![FLOW-APPLIANCE-001 V01 contact sheet](evidence/flow-appliance-001/v01-contact-sheet.jpg)

#### V02

**Clip 1 — ingredient proof / start**

https://github.com/user-attachments/assets/aa72da59-b23f-47be-956e-db1ed5cb4193

**Clip 2 — failed continuation reveal**

https://github.com/user-attachments/assets/1c47f50f-60c2-4bc7-acf0-50fa75b018b6

![FLOW-APPLIANCE-001 V02 contact sheet](evidence/flow-appliance-001/v02-contact-sheet.jpg)

[Read V02 QA](evidence/flow-appliance-001/v02-qa.md)

#### V03

**Clip 2 — targeted repair**

https://github.com/user-attachments/assets/b286e7c8-c2ea-4385-b421-6044d13a2cc9

![FLOW-APPLIANCE-001 V03 contact sheet](evidence/flow-appliance-001/v03-contact-sheet.jpg)

- [Read V03 repair prompt](evidence/flow-appliance-001/v03-clip-2-prompt.md)
- [Read V03 QA](evidence/flow-appliance-001/v03-qa.md)
- [View product reference](evidence/flow-appliance-001/reference-product.jpg)
- [Open the full case →](appliance-multistate-google-flow.md)
- [Open the evidence bundle →](evidence/flow-appliance-001/README.md)

## In-progress case

### FASHION-PUFFER-002 — Navy quilted puffer jacket / fit-proof UGC

**Current status:** prompt set prepared; **awaiting real generation**.

This case extends showcase coverage into fashion/wearables. It tests product geometry lock during handling and try-on, textile compression and drape, mirror continuity, fit readability, and concept diversity.

The prompt set includes four distinct concepts:

- buyer-doubt-led “does it look like the photos?” fit proof — recommended primary concept;
- material + try-on proof;
- skeptical → impressed review;
- everyday routine / lifestyle review.

No success claim or QA score is recorded yet because generated-video evidence does not exist for this case.

- [Open Showcase #2 prompt set →](fashion-puffer-fit-proof.md)
- [Open the evidence manifest →](evidence/fashion-puffer-002/README.md)

## Showcase standard

Every case should make the evidence chain easy to scan:

```text
REFERENCE / INPUT
        ↓
EXACT ASK
        ↓
AGENT ROUTE
        ↓
PROMPT V01
        ↓
REAL GENERATION
        ↓
QA + FAILURE TAGS
        ↓
ROOT CAUSE
        ↓
MINIMAL REPAIR
        ↓
PROMPT V02+
        ↓
REGENERATION / COMPARISON
        ↓
PASS OR NEW TARGETED REPAIR
```

Do not present a case as a success simply because the output looks polished. Failures and limitations are first-class evidence.

## Recommended case layout

Keep the top of each case useful even for someone who does not read the full prompt:

1. short result summary
2. inline generated-video preview plus contact sheet
3. compact QA score
4. what changed in the repair
5. exact prompts and detailed diagnosis below

Use [CASE_TEMPLATE.md](CASE_TEMPLATE.md) for new showcase cases.

## Evidence policy

For representative cases, keep an evidence bundle near the case. Media should be uploaded at a quality that remains useful for visual inspection.

A typical iterative case may contain:

```text
evidence/<case-id>/
├── README.md
├── reference-product.jpg
├── v01-contact-sheet.jpg
├── v01-clip-1-preview.mp4
├── v01-clip-2-preview.mp4
├── v02-contact-sheet.jpg
├── v02-clip-1-preview.mp4
├── v02-clip-2-preview.mp4
├── v02-qa.md
├── v03-contact-sheet.jpg
├── v03-clip-2-preview.mp4
├── v03-clip-2-prompt.md
└── v03-qa.md
```

For README presentation, prefer GitHub user-attachment URLs so generated videos render inline. Keep repository media files as the auditable evidence copy unless the storage policy changes.

Do not aggressively recompress showcase evidence merely to minimize file size. If video or image size becomes unsuitable for normal Git history, prefer Git LFS or release assets while keeping stable links and, when useful, deliberately generated lightweight derivatives.

Every media item should state:

- whether it is a product reference, generated frame, or generated video;
- model/workflow used when known;
- generation date;
- prompt revision;
- whether the asset is original-resolution or a compressed preview;
- whether the output is unedited or post-processed.

## What a showcase should prove

The showcase exists to answer two questions:

1. Does the skill make the generation workflow more reliable?
2. When generation fails, does the skill produce a smaller and better-targeted repair rather than rewriting everything?

As cases accumulate, prioritize coverage over volume. Add different product categories, interaction patterns, model/workflow constraints, and failure classes instead of collecting near-duplicate attractive outputs.

## Promotion criteria

A case is ready to be highlighted from the repository root when it includes:

- an actual product/reference input;
- at least one real generated output;
- reproducible prompt revision(s);
- explicit QA evidence;
- honest failure notes;
- a targeted repair or a documented pass;
- media provenance.

A polished mockup without real generation evidence is an example, not a showcase.
