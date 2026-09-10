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

Use when one long generation is fragile.

Return:

### SHARED CONTINUITY
creator, wardrobe, product, environment, lighting, scale

### CLIP 1 — HOOK
prompt

### STATE HANDOFF
product state

### CLIP 2 — DEMO
prompt

### CLIP 3 — HERO RESULT
prompt

### CLIP 4 — VERDICT
prompt

### EDIT ASSEMBLY
cut order, sound bridge, dialogue placement

Critical continuity must be repeated per clip.

## 6. Audio

Prioritize:
1. environment
2. product sound
3. human reaction/dialogue
4. music

Keep product sound audible during demonstrations.

## 7. Editing

Default:
- hard cuts
- simple jump cuts
- no cinematic transitions
- no commercial logo end card
- no unnecessary speed ramps

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

Revise before returning if not.
