# Cross-agent smoke test — 2026-09-10

This document records the first reproducible compatibility run for the `ugc-product-review` skill.

## Test matrix

| Agent | Model / mode | Activation | Lazy references | Notes |
| --- | --- | --- | --- | --- |
| Claude Code | Sonnet 5, caveman mode | Pass | Pass | Correct routing on single prompt and campaign tests; repair test loaded one extra compiler reference before router tightening |
| Codex | GPT-5.6 Terra, medium | Pass | Pass for Tests 1–2 | After router tightening and reinstall, single-product and concept-only campaign routes loaded the expected minimal references |
| Codex | GPT-5.6 Terra, high | Pass | Pending re-test | Initial run activated the skill but did not load sibling references; high-mode re-test is still pending |

## Expected routes

### Test 1 — single appliance prompt

Expected:

```text
core.md
creative-strategy.md
categories/appliances.md
prompt-compiler.md
```

Claude Code matched exactly.

Codex medium initially activated the skill without loading sibling references. After adding an explicit reference-loading contract, refreshing the installed skill, and verifying sibling-file access, Codex medium re-ran Test 1 and matched the expected route exactly.

The re-test also improved output quality: the response stopped inventing unsupported controls or claims and preserved a more conservative product-consistency workflow.

## Test 2 — campaign concepts only

Expected:

```text
core.md
creative-strategy.md
categories/appliances.md
campaign-engine.md
```

Claude Code matched exactly and correctly avoided `prompt-compiler.md`.

Codex medium first loaded `prompt-compiler.md` unnecessarily. The campaign route was then split into explicit concept-only and full-prompt variants, with `prompt-compiler.md` made a hard exclusion for concept-only requests.

After refreshing the skill, Codex medium re-ran Test 2 and matched the expected minimal route exactly:

```text
core.md
creative-strategy.md
categories/appliances.md
campaign-engine.md
```

This confirms progressive disclosure works on Codex medium when the routing contract is explicit enough.

## Test 3 — generated-video diagnosis only

Expected minimum:

```text
core.md
qa-and-repair.md
```

A category reference may be added only when product-specific construction or physics materially changes the diagnosis.

Claude Code loaded `core.md`, `qa-and-repair.md`, and `prompt-compiler.md` in the original run. The extra compiler reference was not necessary for a diagnosis-only task, so the root router was tightened after this test.

Codex medium re-test is pending.

## Findings

### Claude Code

The progressive-disclosure architecture works as intended. The agent respected category routing and campaign-specific loading. Output quality was strongest when it loaded the category and QA modules explicitly.

A diagnosis-only re-test is still useful to confirm the tightened router now excludes `prompt-compiler.md` unless a revised generation prompt is requested.

### Codex

Codex can access sibling reference files from the installed skill directory. The initial failure was therefore a routing/adherence issue, not a filesystem or host limitation.

After strengthening the routing contract and separating concept-only campaign behavior, Codex Terra medium passed both the single-product and campaign-concepts routes with the expected minimal reference sets.

This is important because it validates the modular architecture on Codex without flattening the skill or duplicating vendor-specific copies.

## Changes made during this run

`SKILL.md` now contains an explicit reference-loading contract:

- routed references must be opened before final output,
- paths are relative to `SKILL.md`,
- file/shell tools should be used when available,
- agents must not claim a reference was used unless it was actually opened,
- diagnosis-only routes should not load the prompt compiler unless a revised generation prompt is requested,
- concept-only campaign routes explicitly exclude `prompt-compiler.md`.

OpenAI-specific metadata also reinforces the same routing behavior without changing the canonical skill design.

## Next verification

1. Run Test 3 on Codex Terra medium.
2. Re-run diagnosis-only routing on Claude Code after refreshing the latest skill.
3. Run one lightweight Codex Terra high smoke test after medium passes all three routes.

If these pass, mark Claude Code and Codex Terra medium as verified for the current baseline and move to real Google Flow video-generation demos.
