# Showcase: <case title>

Status: **awaiting generation | reviewed | repaired | validated**

## At a glance

**Case ID:** `<CASE-ID>`

**Product/category:** `<product / category>`

**Workflow/model:** `<generation workflow>`

**Creative angle:** `<angle>`

**Primary visual proof:** `<what must visibly convince the viewer>`

**Current result:** `<one-sentence outcome>`

**QA:** `<score / scale>`

## Evidence

Place lightweight browsing assets under:

```text
evidence/<case-id>/
```

Recommended:

- product/reference preview
- contact sheet or representative generated still
- lightweight generated-video preview(s)
- evidence README with provenance

Do not claim a real-generation result without actual output evidence.

## Exact ask

```text
<user request or normalized test brief>
```

## Agent route

```text
core
+ <strategy/category/compiler/adapter/qa modules actually used>
```

Explain only routing choices that materially affect reproducibility.

## Product/reference lock

Record only visible or reliably supplied facts. Do not invent features to make the showcase look more complete.

## Prompt V01

```text
<exact generation-ready prompt>
```

## Real-generation result — V01

**Generation date:** `<YYYY-MM-DD>`

**Workflow/model shown:** `<value>`

**Generation duration/settings:** `<value>`

**Post-processing:** `<none / exact edits>`

### QA

| Dimension | Score | Observation |
| --- | ---: | --- |
| Product fidelity |  |  |
| Creator continuity |  |  |
| Physical plausibility |  |  |
| Hand quality |  |  |
| State continuity |  |  |
| Hero clarity |  |  |
| UGC realism |  |  |
| Prompt adherence |  |  |
| **Total** |  |  |

### What worked

- ...

### What failed

- ...

### Failure tags

- `...`

## Root cause

Identify the production/prompt cause, not just the visible symptom.

## Minimal repair

State what changes and what must remain untouched.

### Preserve

- ...

### Change

- ...

## Prompt V02

```text
<only the revised production prompt needed for regeneration>
```

## V01 → V02 comparison

Fill only after real V02 generation.

| Dimension | V01 | V02 | Change |
| --- | ---: | ---: | --- |
| Product fidelity |  |  |  |
| Hero clarity |  |  |  |
| UGC realism |  |  |  |
| State continuity |  |  |  |

## Production lesson

Record only a lesson supported by this case. If the lesson is general enough to change the reusable skill, link the commit that updates the relevant reference module.
