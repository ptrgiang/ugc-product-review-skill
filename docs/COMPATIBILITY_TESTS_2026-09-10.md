# Cross-agent smoke test — 2026-09-10

This document records the first reproducible compatibility run for the `ugc-product-review` skill.

## Test matrix

| Agent | Model / mode | Activation | Lazy references | Notes |
| --- | --- | --- | --- | --- |
| Claude Code | Sonnet 5, caveman mode | Pass | Pass | Single-product, campaign-concepts, and diagnosis-only routing verified against the tightened router |
| Codex | GPT-5.6 Terra, medium | Pass | Pass | All three baseline routes loaded the expected minimal references after router tightening and reinstall |
| Codex | GPT-5.6 Terra, high | Pass | Pass | Current single-product smoke test loaded the expected minimal references |

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

Codex Terra high later ran the same current-router smoke test and also matched the expected four-file route exactly.

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

After refreshing the latest skill, Claude Code re-ran Test 3 and matched the expected minimal route exactly:

```text
core.md
qa-and-repair.md
```

Codex Terra medium also re-ran Test 3 after the routing changes and matched the same expected minimal route exactly.

Both agents correctly avoided `prompt-compiler.md` because the request asked for diagnosis and targeted repair instructions only, not a rewritten generation prompt.

The resulting diagnoses followed the QA taxonomy and targeted-repair approach: product morphing, control-layout drift, hand/grip complexity, and hero-moment pacing were separated into actionable repair instructions without rewriting unaffected creative sections.

## Findings

### Claude Code

The progressive-disclosure architecture works as intended on the tested Claude Code setup. The agent respected category routing, campaign-specific loading, and diagnosis-only exclusions after the router tightening.

### Codex

Codex can access sibling reference files from the installed skill directory. The initial failure was therefore a routing/adherence issue, not a filesystem or host limitation.

After strengthening the routing contract and separating concept-only campaign behavior, Codex Terra medium passed all three baseline routes with the expected minimal reference sets:

- single-product prompt
- concept-only campaign
- generated-video diagnosis-only

Codex Terra high also passed the current single-product smoke test with the expected minimal reference set.

This validates the modular progressive-disclosure architecture on the tested Codex setups without flattening the skill or duplicating vendor-specific copies.

## Changes made during this run

`SKILL.md` now contains an explicit reference-loading contract:

- routed references must be opened before final output,
- paths are relative to `SKILL.md`,
- file/shell tools should be used when available,
- agents must not claim a reference was used unless it was actually opened,
- diagnosis-only routes should not load the prompt compiler unless a revised generation prompt is requested,
- concept-only campaign routes explicitly exclude `prompt-compiler.md`.

OpenAI-specific metadata also reinforces the same routing behavior without changing the canonical skill design.

## Baseline status

Current verified baseline:

```text
Claude Code — Sonnet 5, caveman mode      PASS
Codex — GPT-5.6 Terra medium              PASS
Codex — GPT-5.6 Terra high                PASS (single-product smoke test)
```

The next phase is real AI-video generation evaluation in Google Flow, using reproducible product inputs, generation prompts, QA scoring, and targeted repair rounds.