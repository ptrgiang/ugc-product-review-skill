# Model Adapters

Load only when the target video model is known or the user explicitly asks for model optimization.

These are prompt-structure strategies, not claims about undocumented capabilities.

## Generic
Use:
- timestamps
- clear shot boundaries
- moderate detail
- natural-language directions
- explicit continuity

If the actual generation workflow exposes a shorter duration than the creative plan, recompile the story for the available duration rather than shrinking every beat proportionally.

## Veo-style
Prefer:
- rich temporal prose
- explicit dialogue timing
- environmental audio
- causal action flow
- realistic scene detail
- simple physical objectives per generation when interaction is fragile

Avoid keyword stuffing.

### Short-duration workflow adaptation

When the tested Flow/Veo workflow provides only a short per-generation duration, treat that duration as a production constraint for the current run rather than as a reason to compress a longer story into rushed timestamps.

For multi-state product reviews:

- split around causal state boundaries;
- give each generation one primary physical objective;
- repeat the exact product/reference lock in every clip;
- define the end state of one clip and the compatible start state of the next;
- protect dedicated hero-result time;
- assemble with simple hard cuts or a natural sound bridge.

Example:

```text
8s clip A: ingredient proof → secure lid → start processing
8s clip B: open finished state → stable result proof → natural verdict
```

This rule is based on observed workflow behavior from a real showcase test. Do not generalize a specific duration limit to every Veo product, account, interface, or future version unless the current environment confirms it.

## Kling-style
Prefer:
- shorter action blocks
- one major action per clip
- strong repeated reference locks
- minimal camera choreography
- multi-clip segmentation for difficult interaction

## Seedance-style
Prefer:
- concise shot grammar
- motion-first phrasing
- one visual objective per shot
- clear subject-object interaction

## Sora-style
Prefer:
- coherent scene descriptions
- natural environmental detail
- causal physical progression
- shot separation when exact timing matters

## Fallback
If exact model/version behavior is uncertain:
- do not invent syntax
- use universal natural language
- simplify temporal complexity
- split difficult sequences
