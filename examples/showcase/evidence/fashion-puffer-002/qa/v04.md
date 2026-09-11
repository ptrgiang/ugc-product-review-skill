# FASHION-PUFFER-002 — V04 generation QA

Status: **generated and reviewed; visual-conditioning experiment failed — P1 Major**

## Evidence reviewed

One 8-second V04 Clip 1 generated for the reference-conditioned partial-state experiment.

The intended test was not another text-only repair. V04 was meant to preserve a supplied partial-worn visual state and animate only one action: the creator's left arm entering the already-visible empty left sleeve.

## Verdict

`P1 — Major / V04 FAIL`

Approximate QA scores:

```text
Product fidelity:              9.0/10
Creator consistency:           9.0/10
Fabric physics:                8.5/10
Hands/body mechanics:          8.5/10
Camera / UGC realism:          9.0/10
Opening-state compliance:      0.0/10
Required one-arm insertion:    2.0/10
State continuity:              6.0/10
Experiment objective:          FAIL
```

## Expected opening state

```text
RIGHT arm already inside right sleeve
RIGHT hand outside right cuff
RIGHT shoulder seated correctly
LEFT sleeve visibly empty
LEFT arm clearly outside jacket
jacket open
```

## Observed behavior

The generated clip does not preserve the required partial-worn opening state.

The sequence behaves approximately like this:

```text
0.00s
creator not yet wearing the jacket

~0.5–1.0s
jacket appears behind / beside the body

~1.25–2.0s
one side of the jacket is partially on the creator

~2.0–4.0s
creator mainly pulls / adjusts sleeve and front panel

~5.5s+
jacket fully worn
```

Instead of continuing directly from the required partial-worn state, the model reconstructs its own earlier dressing sequence.

## Error tags

```text
OPENING_STATE_VIOLATION
REFERENCE_STATE_NOT_PRESERVED
PARTIAL_STATE_RECONSTRUCTION
INTERACTION_SUBSTITUTION
TEMPORAL_REINTERPRETATION
```

## What improved

V04 remains visually cleaner than V01:

- product geometry is stable;
- navy color and quilting remain consistent;
- creator identity is stable;
- fabric motion is plausible;
- hands and body mechanics are mostly believable;
- no major product morph or severe body-through-fabric event is obvious;
- the camera remains simple and UGC-like.

The failure is therefore primarily **state-control / task-compliance**, not general visual quality.

## Root-cause update

V03 showed that a text-described asymmetric garment state can collapse into a fully worn state.

V04 shows a stronger limitation: **visual conditioning is not necessarily treated as an immutable first-frame state**. In the tested workflow, the supplied visual appears to influence appearance and composition but the model may still reconstruct an earlier semantic dressing sequence before reaching the requested state.

This means the following are not equivalent:

```text
reference image conditioning
!=
true first-frame / start-frame conditioning
```

If the generation workflow interprets the image only as a general reference, more text constraints are unlikely to solve the problem reliably.

## Recommended next experiment — V05

V05 should test a stricter generation mode:

```text
true image-to-video / first-frame input
→ exact supplied frame is the actual first video frame
→ animate only the left arm through the visible empty sleeve
```

The prompt should be shorter than V04 and should not describe any earlier dressing history. The model should not be asked to construct the partial state; that state must already exist in the first frame.

If the platform cannot guarantee that the supplied image is the literal first frame, classify this interaction as unreliable for production in that workflow rather than continuing to add negative constraints.

## Reusable lesson for the skill

For difficult intermediate physical states, distinguish three conditioning modes:

```text
appearance/reference conditioning
start-state conditioning
literal first-frame image-to-video conditioning
```

Do not assume that a reference image is an immutable opening state. When the exact intermediate state is essential, use a workflow that guarantees the supplied image is frame 1, then animate only the minimum required motion.
