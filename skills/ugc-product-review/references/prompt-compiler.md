# Prompt Compiler Module

Load when producing generation-ready prompts.

## 1. Compile only what is needed

Recommended sections:

1. TITLE
2. CREATIVE OBJECTIVE
3. CHARACTER CONSISTENCY
4. PRODUCT CONSISTENCY
5. ENVIRONMENT
6. CAMERA LANGUAGE
7. TIMELINE
8. AUDIO
9. PRODUCT STATE CONTINUITY
10. CATEGORY PHYSICS
11. EDITING
12. NEGATIVE CONSTRAINTS

Omit unused sections.

## 2. Prompt density

### Compact
6–8s, one simple idea.

### Standard
9–15s, 3–5 shots.

### Detailed
Complex product interaction or strict continuity.

### Production
Multi-clip, difficult physics, campaign reuse.

Do not maximize length for its own sake.

## 3. Shot format

For each shot, define only relevant fields:

`0:00–0:03 — HOOK`

- Camera
- Creator action
- Product action
- Expression
- Dialogue
- Audio
- State handoff

Prefer precise physical action over aesthetic adjectives.

## 4. Example action quality

Weak:
"She uses the product."

Better:
"Her left hand steadies the container while her right hand rotates the lid clockwise until the latch clicks."

## 5. Multi-clip mode

Use when one long generation is fragile **or when the target workflow's available clip duration is shorter than the intended story**.

Do not compress a longer narrative into a shorter model limit just to preserve the original timestamps. Recompile the story natively for the available clip duration.

### Activation signals

Prefer multi-clip compilation when one or more are true:

- the target workflow has a known short per-generation duration limit;
- the sequence requires several fragile product states or state reversals;
- more than one difficult hand/product interaction must happen in the same generation;
- a hero result needs dedicated readable screen time that would otherwise be squeezed;
- an earlier generation showed product drift, hand failure, state discontinuity, or rushed payoff caused by temporal overload.

### Segmentation rule

Each generated clip should have **one primary physical objective**.

Examples:

```text
clip 1: setup → start
clip 2: result → verdict
```

```text
clip 1: package → open
clip 2: reveal → try-on
```

```text
clip 1: dirty state → apply product
clip 2: wipe → clean proof
```

Avoid making every clip a miniature full story. The final edit carries the complete narrative.

Return:

### SHARED CONTINUITY
creator, wardrobe, product, environment, lighting, scale

### CLIP 1 — PHYSICAL OBJECTIVE
prompt

### STATE HANDOFF
exact end state needed by the next clip

### CLIP 2 — PHYSICAL OBJECTIVE
prompt

### OPTIONAL ADDITIONAL CLIPS
only when the story genuinely needs them

### EDIT ASSEMBLY
cut order, sound bridge, dialogue placement

Critical continuity must be repeated per clip.

### State handoff quality

Weak:

```text
Continue from the previous clip.
```

Better:

```text
same appliance + same bowl + same lid orientation + same counter position + processing underway
```

The next clip should start from a causally compatible state, not merely a visually similar composition.

### Hero-time protection

Do not let setup consume the result.

For transformation-led reviews, reserve enough time in the result clip for the proof to be readable before verdict dialogue or a new action begins. A stable 1.5–2 second hero hold is a useful default when the target duration allows it.

## 6. Audio

Prioritize:
1. environment
2. product sound
3. human reaction/dialogue
4. music

Keep product sound audible during demonstrations.

For multi-clip edits, a simple natural sound bridge may connect a causal time jump when useful. Do not rely on elaborate transition sound design to hide continuity problems.

## 7. Editing

Default:
- hard cuts
- simple jump cuts
- no cinematic transitions
- no commercial logo end card
- no unnecessary speed ramps

When clips are generated separately, prefer a clean causal hard cut over inventing an in-model transition.

## 8. On-screen text

Default to no generated text.

If captions are needed, prefer adding them in post-production.

## 9. Negative constraints

Use category-specific constraints only.

Do not append a giant generic negative list if it is irrelevant.

## 10. Pre-output QA

Check:
- product appears early
- strongest proof is shown
- hero moment has enough time
- dialogue fits duration
- actions are physically plausible
- state transitions are valid
- product/creator locks are present
- prompt is not overloaded
- requested story duration fits the target generation workflow
- if split, each clip has one primary physical objective
- if split, the state handoff is explicit and causally valid

Revise before returning if not.

## 11. Evidence-backed compiler note

A real Google Flow / Veo appliance test showed that a concept originally designed as a ~12-second one-pass story became more reliable when recompiled as two native 8-second generations rather than squeezing the same five-state timeline into the shorter workflow limit.

Treat this as a general compiler lesson, not a universal Veo capability claim: **when the actual generation environment exposes a shorter limit than the creative plan, preserve the concept and proof hierarchy, then re-segment the physical objectives for the available duration.**
