# FLOW-APPLIANCE-001 — V03 clip-2 QA

Status: **PASS — targeted continuation-state repair validated**

## Evidence reviewed

V03 regenerated **clip 2 only** while keeping V02 clip 1 unchanged.

The purpose of V03 was intentionally narrow: test whether an explicit immutable opening state and forbidden regressions could remove the continuation-state failure observed in V02.

## V02 failure being repaired

V02 clip 2 began too close to the pre-processing ingredient state, then revealed processed salsa only after the lid was removed.

That created the invalid sequence:

```text
raw / coarse ingredients
→ lid opens
→ processed salsa appears
```

The intended sequence was:

```text
processing already finished before clip starts
→ finished salsa exists under the closed lid
→ lid opens
→ the same finished salsa is revealed
```

## V03 result

V03 fixes the primary V02 failure.

At the opening of the regenerated clip, the contents are already in the processed salsa state before the lid is lifted. The lid-opening action reveals the existing result instead of causing or coinciding with a hidden transformation.

The product remains recognizable and the result is given enough stable screen time to function as the hero proof. The creator reaction also remains restrained and review-like rather than ending in a generic presenter gesture.

## QA score

| Dimension | Score | Observation |
| --- | ---: | --- |
| Product fidelity | 2 / 2 | Appliance body, clear bowl, handle orientation, and control layout remain recognizable. |
| State continuity | 2 / 2 | Finished salsa exists before lid opening; no regression to the raw ingredient state. |
| Physical plausibility | 2 / 2 | The reveal is causally valid and the product stays supported. |
| Hand / lid interaction | 1.5 / 2 | Usable and plausible, though the interaction still has slight generated smoothness. |
| Hero clarity | 2 / 2 | Processed result is readable and receives dedicated screen time. |
| UGC authenticity | 2 / 2 | Reaction is restrained and product-focused rather than overtly commercial. |
| Prompt adherence | 2 / 2 | The critical immutable opening-state instruction is followed. |
| Pacing | 1.5 / 2 | Strong overall; the hero hold could be marginally more static before the reaction. |
| **Total** | **15 / 16** | Targeted repair succeeds; no V04 required for this root cause. |

## Error status

Resolved:

- `STATE_DISCONTINUITY`
- `NO_CAUSAL_TRANSITION`

Remaining minor quality note:

- slight lid / hand interaction smoothness, below the threshold for another repair cycle

## What V03 validated

The evidence supports a reusable continuation-clip rule:

1. name the exact previous continuity anchor;
2. define an **immutable opening state** before the timeline;
3. state what already happened before frame 1;
4. explicitly forbid regression to earlier states;
5. separate the hero reveal from any transformation that should have happened off-screen.

The useful distinction is:

```text
continuity description ≠ opening-state lock
```

A prompt can describe continuity correctly and still allow the model to reconstruct an earlier state. For fragile multi-clip workflows, the first frame needs its own explicit state contract.

## Decision

**PASS.**

Do not create V04 for this case unless a future generation exposes a different material failure.

FLOW-APPLIANCE-001 can now be treated as a completed repair lifecycle:

```text
V01 — temporal overload / weak hero
↓
V02 — split-clip strategy improves execution but exposes state regression
↓
V03 — immutable opening-state repair resolves the regression
↓
PASS
```
