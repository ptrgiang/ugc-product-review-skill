# Cross-agent smoke test — 2026-09-10

This document records the first reproducible compatibility run for the `ugc-product-review` skill.

## Test matrix

| Agent | Model / mode | Activation | Lazy references | Notes |
| --- | --- | --- | --- | --- |
| Claude Code | Sonnet 5, caveman mode | Pass | Pass | Correct routing on single prompt and campaign tests; repair test loaded one extra compiler reference |
| Codex | GPT-5.6 Terra, medium | Pass | Partial | Skill activated but only `SKILL.md` was reported as read |
| Codex | GPT-5.6 Terra, high | Pass | Partial | Same reference-loading issue as medium |

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

Codex activated the skill but reported only `SKILL.md`.

## Test 2 — campaign concepts only

Expected:

```text
core.md
creative-strategy.md
categories/appliances.md
campaign-engine.md
```

Claude Code matched exactly and correctly avoided `prompt-compiler.md`.

Codex again reported only `SKILL.md` and produced a generic concept list.

## Test 3 — generated-video diagnosis only

Expected minimum:

```text
core.md
qa-and-repair.md
```

A category reference may be added only when product-specific construction or physics materially changes the diagnosis.

Claude Code loaded `core.md`, `qa-and-repair.md`, and `prompt-compiler.md`. The extra compiler reference was not necessary for a diagnosis-only task, so the root router was tightened after this test.

Codex reported only `SKILL.md`.

## Findings

### Claude Code

The progressive-disclosure architecture works as intended. The agent respected category routing and campaign-specific loading. Output quality was strongest when it loaded the category and QA modules explicitly.

### Codex

The skill activates correctly but the tested installation did not follow the reference-loading routes. Because the root router contains summaries of the expected behavior, Codex still produced plausible output, but it missed several safeguards and made more product assumptions than desired.

## Change made after this run

`SKILL.md` now contains an explicit reference-loading contract:

- routed references must be opened before final output,
- paths are relative to `SKILL.md`,
- file/shell tools should be used when available,
- agents must not claim a reference was used unless it was actually opened,
- diagnosis-only routes should not load the prompt compiler unless a revised generation prompt is requested.

## Next verification

Re-test Codex medium/high after refreshing the installed skill. If Codex still refuses to open sibling references, document it as a host-specific limitation and consider an optional Codex adapter rather than making the canonical skill monolithic.
