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

## Veo-style
Prefer:
- rich temporal prose
- explicit dialogue timing
- environmental audio
- causal action flow
- realistic scene detail

Avoid keyword stuffing.

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
