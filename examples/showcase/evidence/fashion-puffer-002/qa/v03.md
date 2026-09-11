# FASHION-PUFFER-002 — V03 generation QA

Status: **generated and reviewed; dedicated single-action repair still failed — P1 Major**

## Evidence reviewed

One 8-second V03 Clip 1 generated from the dedicated single-action sleeve-insertion prompt.

Intended opening state:

```text
right arm fully inside right sleeve
left sleeve visibly empty
left arm outside jacket
```

Intended action:

```text
hold partial state
→ left arm enters left sleeve continuously
→ left hand emerges from cuff
→ garment settles
```

## What improved

The output is visually cleaner than V01 and V02 in several dimensions:

```text
Product fidelity:            9.0/10
Creator consistency:         9.0/10
Garment geometry:            9.0/10
Fabric physics:              8.5/10
Hands/body mechanics:        8.5/10
Camera / UGC realism:        9.0/10
State continuity:            8.0/10
Required opening state:      1.0/10
Required sleeve insertion:   0.0/10
Repair objective:            FAIL
```

The navy color, horizontal quilting, collar, centered zipper, hem, sleeves, scale, and overall silhouette remain stable. Creator identity also remains coherent, and the visible hand/fabric interactions are generally plausible.

## Primary failure

The clip does not begin in the requested partial-worn state.

From frame 1, the creator already appears to have:

```text
right arm inside right sleeve
left arm inside left sleeve
both hands already outside the cuffs
jacket settled on both shoulders
```

The model then substitutes the requested insertion action with a simpler already-worn adjustment action, such as sleeve/cuff or front-panel adjustment.

## Error tags

```text
OPENING_STATE_VIOLATION
TRY_ON_ACTION_OMITTED
PARTIAL_STATE_COLLAPSE
INTERACTION_SUBSTITUTION
STATE_GOAL_NOT_EXECUTED
```

The major V01 physics failures are no longer dominant. In particular, no severe product morph, body intersection, or sleeve teleport is required to explain the failure. The remaining issue is task/state compliance.

## Root cause update

V03 removed unrelated actions and dedicated the full generation to one sleeve insertion, yet the model still collapsed the requested partial-worn starting state into the more semantically common **fully worn** state.

This suggests the limiting factor is no longer just interaction complexity. The requested intermediate garment state is itself unstable under text-only prompting for this workflow.

The model appears to prefer familiar semantic states:

```text
holding jacket
or
fully wearing jacket
```

over the less common intermediate state:

```text
one arm fully inserted
other sleeve empty
other arm still outside
```

## V04 test direction

Do not continue escalating text-only negative constraints.

V04 should test **visual start-state conditioning**. Supply a start/reference frame that visibly establishes the exact partial-worn state before generation begins.

The experimental question is:

```text
Can the model preserve and continue a visually supplied partial-worn state
when it repeatedly collapses the same state under text-only instructions?
```

The start frame should clearly show:

- right arm already inside the correct right sleeve;
- right hand outside the right cuff;
- right shoulder correctly loaded;
- left sleeve visibly empty;
- left arm clearly outside the jacket;
- jacket front open;
- correct navy color, quilting, collar, zipper, length, and scale;
- no ambiguous occlusion hiding the left sleeve opening.

The V04 motion prompt should then remain minimal: preserve the supplied frame state, slowly insert the left arm through the visible left sleeve, let the hand emerge through the cuff, allow the jacket to settle, and hold the final state.

## Reusable lesson for the skill

After two or more targeted prompt repairs, if a model consistently collapses the same unusual intermediate state into a common semantic state, classify the failure as **intermediate-state representation failure**.

Escalation should move from:

```text
text repair
→ action simplification
→ dedicated single-action clip
→ visual state conditioning
```

rather than indefinitely increasing text constraints.
