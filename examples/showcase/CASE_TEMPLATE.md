# Showcase case template

Use this template for every new real-generation showcase case.

## Canonical case file

Create one top-level narrative file:

```text
examples/showcase/<case-slug>.md
```

It should contain:
- case ID
- product/category
- model/workflow
- creative objective
- reference/product lock
- lifecycle summary
- the important prompt evolution
- concise QA conclusions
- generalized lesson
- current next step

Do not use the canonical case file as a dumping ground for every QA report or every prompt revision.

## Evidence bundle

Create:

```text
examples/showcase/evidence/<case-id>/
├── README.md
├── prompts/
├── qa/
└── <media evidence>
```

### `README.md`
Use as the evidence/lifecycle index. Record:
- reference input status
- generated versions
- current pass/fail state
- links to prompts and QA
- preserved outputs
- current experiment direction

### `prompts/`
Store only generation-ready or repair prompts.

Naming:

```text
v01.md
v02.md
v03-clip-2.md
v05-start-frame.md
```

### `qa/`
Store only QA reports and diagnosis.

Naming:

```text
v01.md
v02.md
v03.md
```

Each QA file should contain:
- verdict / severity
- evidence reviewed
- scores when useful
- observed failure
- error tags
- root cause
- what improved
- repair direction

### Media evidence
Keep reference images, generated previews, and contact sheets directly in the case evidence directory:

```text
reference-product.jpg
v02-clip-1-preview.mp4
v02-clip-2-preview.mp4
v02-contact-sheet.jpg
```

This keeps media URLs short and stable while separating prose artifacts into `prompts/` and `qa/`.

## Lifecycle rule

```text
prompt
→ generation
→ qa
→ targeted repair prompt
→ regeneration
```

Never create an isolated `vXX-prompt.md` beside QA/media files. Never store QA inside a prompt file. If a version has both, it gets one file under `prompts/` and one under `qa/`.

## Promotion rule

A showcase can be presented as validated only when real generation evidence exists and the relevant QA has passed. Otherwise mark it explicitly as `in repair testing`, `pending generation`, or `failed`.
