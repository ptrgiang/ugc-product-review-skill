# FASHION-PUFFER-002 — V02 generation QA

Status: **generated and reviewed; targeted repair failed — P1 Major**

## Evidence reviewed

One 8-second V02 Clip 1 generated from the partial-state repair plan.

Intended progression:

```text
material proof
→ hard cut
→ right arm already inserted
→ left sleeve visibly empty
→ left arm travels through sleeve
→ left hand emerges from cuff
→ garment settles
```

## What improved

V02 materially improved several dimensions compared with V01:

- product fidelity remained strong;
- creator identity stayed consistent;
- hand quality was substantially better;
- quilted-fabric behavior was more believable;
- the opening material-inspection segment was usable;
- the post-transition already-worn state was also usable as an independent fit shot.

Approximate QA scores:

```text
Product fidelity:        8.5/10
Creator consistency:     9.0/10
Fabric/material realism: 8.0/10
Hands/body:              8.5/10
UGC authenticity:        8.0/10
Camera realism:          8.5/10
State continuity:        4.0/10
Try-on physics:          2.0/10
Repair objective:        FAIL
```

## Primary failure

The model still did not execute the requested sleeve-insertion interaction.

Observed sequence:

```text
creator holding unworn jacket
→ hard cut
→ creator temporarily absent / empty room
→ hard cut
→ creator reappears with jacket already fully worn
```

This replaces the requested physical action with a temporal shortcut.

## Error tags

```text
STATE_DISCONTINUITY
TRY_ON_ACTION_OMITTED
TEMPORAL_SKIP
SUBJECT_DISAPPEARANCE
INTERACTION_GOAL_NOT_EXECUTED
```

## Root cause

V02 reduced the original full-dressing complexity, but one 8-second generation still had to solve several phases:

```text
material inspection
→ state change
→ partial try-on setup
→ sleeve insertion
→ garment settling
→ reaction
```

The model chose a cheaper temporal solution: omit the highest-risk interaction and jump directly to the completed state.

This is therefore not primarily a product-fidelity problem. It is a **temporal interaction-planning failure**.

## Targeted repair direction

Do not add more negative constraints around the same overloaded structure.

V03 should dedicate the full clip to one interaction only:

```text
partial-worn state from frame 1
→ hold state visibly
→ one continuous left-arm sleeve insertion
→ garment settles
→ hold completed state
```

Remove material inspection, dialogue, zipper use, internal cuts, mirror reveal, and unrelated product actions from the repair clip.

## Reusable lesson for the skill

When a model repeatedly skips the fragile middle of an interaction, repair **shot architecture** before increasing prompt length.

Recommended escalation:

1. remove unrelated actions;
2. begin at the nearest stable pre-action state;
3. allow one major interaction only;
4. remove internal cuts;
5. dedicate most of the clip duration to that interaction;
6. preserve successful surrounding shots instead of regenerating them.
