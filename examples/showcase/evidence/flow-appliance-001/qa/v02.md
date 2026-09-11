# FLOW-APPLIANCE-001 — V02 generation QA

Status: **generated and reviewed; clip 2 needs targeted state-continuity repair**

## Evidence reviewed

Two 8-second V02 outputs generated from the split-clip repair plan:

- `v02-clip-1` — ingredient proof → lid close → control press / processing start
- `v02-clip-2` — intended continuation: processing complete → lid open → hero result → verdict

## What improved

V02 confirms that splitting the sequence into short outputs is the right production strategy for the tested Google Flow / Veo workflow.

Clip 1 is materially cleaner than trying to compress the full review into one generation. The product remains readable, the coarse ingredient state is clear, the lid interaction is simple, and the front controls stay recognizable.

Across both clips, the appliance body, clear bowl, right-side handle, central spindle, and two-control front layout remain substantially consistent. The ordinary bright kitchen and close smartphone-style framing also stay coherent enough to support a hard-cut assembly.

## Primary failure

Clip 2 does **not** begin in the required immutable post-processing state.

The opening frames show the bowl with visibly coarse/raw ingredients. The lid is then removed, and the processed salsa appears afterward. This produces an impossible causal jump:

```text
raw / coarse ingredients
→ lid removal
→ processed salsa suddenly appears
```

The intended sequence was:

```text
processing already completed before clip starts
→ lid still closed
→ lid removed
→ already-finished salsa revealed
```

The problem is therefore not mainly product identity. It is **state regression at the first frame of a continuation clip**.

## Error tags

- `STATE_DISCONTINUITY`
- `NO_CAUSAL_TRANSITION`
- `LID_GEOMETRY_DRIFT` — minor

## Root cause

The V02 prompt says that clip 2 should continue after processing has completed, but the opening state is not constrained strongly enough to prevent the model from reconstructing the visually familiar raw-ingredient setup before performing the reveal.

A continuation prompt needs more than a continuity description. It needs an explicit **immutable opening state** plus **forbidden regressions**.

## Targeted repair

Add this block before the clip-2 timeline:

```text
IMMUTABLE OPENING STATE
This clip begins immediately after the processing cycle from clip 1 has fully finished.
At the very first frame, the exact same clear bowl is still attached to the exact same appliance and the contents inside are already fully processed into the finished chunky salsa result.
The machine is no longer actively running.
The lid is still closed at the first frame.

Do not show raw or partially processed ingredients at any point in this clip.
Do not transform the ingredients after the lid begins opening.
The processing happened entirely before this clip begins.
```

Then keep the remaining clip simple:

```text
0:00–0:02 — unlock and lift the lid
0:02–0:05 — stable hero view of the already-finished salsa
0:05–0:08 — restrained natural verdict
```

Do not regenerate clip 1. Repair and regenerate **only clip 2**.

## Reusable lesson for the skill

For every continuation clip, explicitly define four things:

1. **continuity anchor** — which prior reference/output must be matched
2. **immutable opening state** — what is already true on the first frame
3. **forbidden regressions** — which earlier states must never reappear
4. **hero isolation** — enough quiet/stable screen time for the visual proof

This case should be used to strengthen `prompt-compiler` and `qa-and-repair` guidance for multi-clip state handoffs.
