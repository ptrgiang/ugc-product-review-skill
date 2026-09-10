# Real-generation showcase

This directory contains proof cases where the skill is evaluated against an actual video-generation workflow.

The showcase is intentionally separate from `skills/`. The installable skill should stay focused on instructions and reusable references; testing history, output evidence, and iteration logs belong here.

## Featured case

### FLOW-APPLIANCE-001 — Google Flow / Veo appliance multi-state UGC

**Result:** V01 produced usable product-consistent footage, but the original ~12-second story did not fit the tested 8-second-per-generation Flow workflow cleanly. The repair recompiles the same concept as two native 8-second clips with one physical objective per clip.

**V01 QA:** `13 / 16`

**Main observed weaknesses:** hero result too compressed, generic thumbs-up ending, cross-clip continuity now needs explicit production handling.

**Repair:** `setup → start` in clip A, then `open → hero result → natural verdict` in clip B.

[Open the full case →](appliance-multistate-google-flow.md)

[Open the evidence bundle →](evidence/flow-appliance-001/README.md)

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
PROMPT V02
        ↓
REGENERATION / COMPARISON
```

Do not present a case as a success simply because the output looks polished. Failures and limitations are first-class evidence.

## Recommended case layout

Keep the top of each case useful even for someone who does not read the full prompt:

1. short result summary
2. visual/reference evidence
3. generated preview/contact sheet
4. compact QA score
5. what changed in the repair
6. exact prompts and detailed diagnosis below

Use [CASE_TEMPLATE.md](CASE_TEMPLATE.md) for new showcase cases.

## Evidence policy

For representative cases, prefer a small evidence bundle near the case:

```text
evidence/<case-id>/
├── README.md
├── reference-product.jpg
├── v01-contact-sheet.jpg
├── v01-clip-1-preview.mp4
└── v01-clip-2-preview.mp4
```

The repository copy should be optimized for browsing, not archival quality. Keep lightweight previews in Git when practical. If showcase media begins making repository history unnecessarily large, move full-resolution videos to Git LFS or release assets and keep stable links plus small previews here.

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
