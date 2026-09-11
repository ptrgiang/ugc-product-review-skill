# Real-generation showcase

This directory contains auditable real-generation cases used to test prompt reliability, QA, targeted repair, and model-specific failure modes.

## Standard structure

Every showcase case keeps the narrative case file at the showcase root and stores implementation artifacts in one case-specific evidence bundle:

```text
examples/showcase/
├── README.md
├── CASE_TEMPLATE.md
├── <case-file>.md
└── evidence/
    └── <case-id>/
        ├── README.md        # evidence manifest / lifecycle index
        ├── prompts/         # generation or repair prompts only
        ├── qa/              # QA reports only
        └── <media files>    # reference images, previews, contact sheets
```

Rules:
- Case narrative and lifecycle stay in the top-level case file.
- `prompts/` contains only runnable generation/repair prompts.
- `qa/` contains only generation QA and diagnosis.
- Binary evidence stays directly in the case evidence directory so existing media links remain stable.
- `README.md` inside each evidence bundle is the index connecting prompts, QA, and media.
- Do not place prompt files inside `qa/`, QA reports inside `prompts/`, or either type loose beside media.

## Cases

### FLOW-APPLIANCE-001 — Appliance multi-state / Google Flow

Status: **V03 PASS**.

- [Canonical case](appliance-multistate-google-flow.md)
- [Evidence bundle](evidence/flow-appliance-001/README.md)
- [V02 QA](evidence/flow-appliance-001/qa/v02.md)
- [V03 prompt](evidence/flow-appliance-001/prompts/v03-clip-2.md)
- [V03 QA](evidence/flow-appliance-001/qa/v03.md)

### FASHION-PUFFER-002 — Navy puffer fit-proof

Status: **repair testing; V04 failed, V05 pending**.

- [Canonical case](fashion-puffer-fit-proof.md)
- [Evidence bundle](evidence/fashion-puffer-002/README.md)
- [V02 QA](evidence/fashion-puffer-002/qa/v02.md)
- [V03 QA](evidence/fashion-puffer-002/qa/v03.md)
- [V04 QA](evidence/fashion-puffer-002/qa/v04.md)
- [V05 prompt](evidence/fashion-puffer-002/prompts/v05.md)

## Lifecycle convention

```text
REFERENCE / INPUT
        ↓
PROMPT V01
        ↓
REAL GENERATION
        ↓
QA + FAILURE TAGS
        ↓
ROOT CAUSE
        ↓
TARGETED REPAIR PROMPT V02+
        ↓
REGENERATION
        ↓
PASS OR NEXT TARGETED REPAIR
```

Versioned artifacts should use predictable names:

```text
prompts/v02.md
prompts/v03-clip-2.md
qa/v02.md
qa/v03.md
v03-contact-sheet.jpg
v03-clip-2-preview.mp4
```

The evidence manifest should record which artifact is current, which outputs are preserved, and whether the case is validated or still in repair testing.

Use [CASE_TEMPLATE.md](CASE_TEMPLATE.md) for all new showcase cases.
