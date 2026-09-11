# Showcase #2: Navy quilted puffer jacket — fit-proof UGC

Status: **V03 QA completed — V04 reference-conditioned partial-state test proposed**

## At a glance

**Case ID:** `FASHION-PUFFER-002`

**Product/category:** Navy quilted puffer jacket / fashion

**Workflow/model:** Google Flow / Veo, using the practical constraint of **8 seconds per generated clip**

**Creative angle:** Buyer-doubt-led fit proof with product inspection, controlled try-on, mirror proof, and a natural verdict

**Primary visual proof:** Real-world silhouette, puffiness, shoulder fit, length, and material behavior while handled and worn

**Current result:** V01, V02, and V03 Clip 1 have all been generated and QA'd. Product fidelity and creator consistency improved across iterations, but the model repeatedly avoids the requested intermediate dressing state. V03 no longer shows major morphing or body intersection, but it starts already fully worn and substitutes a sleeve-adjustment action for the requested sleeve insertion. V01 Clip 2 remains substantially usable.

**QA status:**
- V01: `P1 — Major`
- V02: `P1 — Major`
- V03: `P1 — Major`
- V04: test prompt ready

## Why this case uses native 8-second clips

The tested Google Flow / Veo workflow practically returns 8-second clips. Showcase #2 therefore uses native 8-second blocks and preserves successful surrounding shots instead of regenerating the full story.

The iteration history is intentionally retained because this case tests how prompt architecture should change when a model repeatedly collapses a difficult intermediate garment state.

## Evidence status

Product/reference input: navy quilted puffer jacket reference image.

Generated-video evidence:
- V01 Clip 1: generated; full dressing interaction failed
- V01 Clip 2: generated; substantially usable fit-proof shot
- V02 Clip 1: generated; temporal skip from unworn to fully worn
- V03 Clip 1: generated; opening-state violation and action substitution
- V04 Clip 1: pending

## Agent route

```text
core
+ creative-strategy
+ categories/fashion
+ prompt-compiler
+ model-adapters
+ qa-and-repair
```

## Product/reference lock

Use the supplied product reference as the visual authority in every clip.

Preserve only visible or reliably supplied details:
- deep navy color;
- horizontal quilt geometry and panel spacing;
- material finish and believable puffiness;
- stand collar;
- centered front zipper;
- sleeves and cuffs;
- hem and jacket length;
- visible pockets when readable in the reference;
- overall proportions and silhouette.

Do not invent logos, labels, buttons, trims, extra pockets, extra zippers, removable parts, or technical features.

---

# V01 — full dressing attempt

## Outcome

- **Clip 1:** failed during the full dressing motion.
- **Clip 2:** substantially usable and should be preserved by default.

## QA

**Severity:** `P1 — Major`

```text
HIGH_INTERACTION_RISK
FABRIC_PHYSICS
BODY_MECHANICS_ERROR
STATE_DISCONTINUITY
CONTACT_ERROR
PRODUCT_MORPH
```

The full outerwear dressing transition required too many simultaneous constraints: both arms, both sleeves, shoulder rotation, flexible fabric, occlusion, and product geometry. The model partially morphed or snapped the jacket onto the creator instead of preserving a physically continuous dressing sequence.

## Repair strategy

V02 reduced the requested action to a safer partial-state transition:

```text
held
→ hard cut
→ right arm already fully inserted
→ left arm slides through left sleeve
→ both arms inserted
→ one small settling tug
→ worn state
```

---

# V02 — partial-state transition after material proof

## Intended progression

```text
right arm already inserted
→ left sleeve still empty
→ left arm visibly travels through sleeve
→ left hand emerges from cuff
→ garment settles
```

## QA verdict

`P1 — Major / REGENERATE CLIP 1`

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

## Observed failure

```text
creator holding unworn jacket
→ hard cut
→ creator temporarily absent / empty room
→ hard cut
→ creator reappears with jacket already fully worn
```

The difficult interaction was omitted instead of solved.

## Error tags

```text
STATE_DISCONTINUITY
TRY_ON_ACTION_OMITTED
TEMPORAL_SKIP
SUBJECT_DISAPPEARANCE
INTERACTION_GOAL_NOT_EXECUTED
```

## What worked

The opening material-inspection segment is substantially usable. Product geometry, color, creator identity, and fabric behavior are much more stable than V01.

The post-transition fully worn state is also usable as a separate fit-proof shot.

## Root cause update

V02 still asked one 8-second generation to manage too many phases:

```text
material inspection
→ hard cut
→ partial-state setup
→ sleeve insertion
→ garment settling
→ reaction
```

The model found a lower-cost temporal solution by skipping the fragile interaction.

---

# V03 — dedicated single-action sleeve-insertion test

V03 removed material proof, removed internal cuts, removed dialogue, and dedicated the entire 8 seconds to one sleeve-insertion action from a supposed partial-worn first frame.

## Intended opening state

```text
RIGHT arm inside right sleeve
RIGHT hand outside right cuff
RIGHT shoulder seated correctly
LEFT sleeve completely empty
LEFT arm outside jacket
jacket open
```

## Intended progression

```text
stable partial-worn first frame
→ left arm enters existing left sleeve
→ hand emerges from left cuff
→ jacket settles on both shoulders
→ stable worn end state
```

## V03 QA verdict

`P1 — Major / V03 FAIL`

Approximate QA scores:

```text
Product fidelity:             9.0/10
Creator consistency:          9.0/10
Garment geometry:             9.0/10
Fabric physics:               8.5/10
Hands/body mechanics:         8.5/10
Camera / UGC realism:         9.0/10
State continuity:             8.0/10
Required opening state:       1.0/10
Required sleeve insertion:    0.0/10
Repair objective:             FAIL
```

## Observed behavior

At frame 1 the creator is already wearing the jacket with both arms inserted and both hands outside the cuffs. The requested partial-worn state never appears.

The generated action is approximately:

```text
fully worn jacket
→ creator adjusts an already-worn sleeve / cuff
→ creator adjusts front panel
→ fully worn jacket
```

Instead of:

```text
right arm inserted
+ left sleeve empty
→ left arm enters sleeve
→ hand exits cuff
```

## V03 error tags

```text
OPENING_STATE_VIOLATION
TRY_ON_ACTION_OMITTED
PARTIAL_STATE_COLLAPSE
INTERACTION_SUBSTITUTION
STATE_GOAL_NOT_EXECUTED
```

## What improved

V03 is visually stronger than V01 and V02 in several important ways:
- no major garment morph;
- no creator disappearance;
- no empty-room bridge frame;
- no obvious body-through-fabric event;
- stable jacket color, quilting, zipper, collar, hem, and silhouette;
- believable small hand-to-fabric interactions;
- natural static UGC camera behavior.

If the requirement to show the try-on is removed, V03 is usable as an **already-worn detail-adjustment shot**.

## Root cause update after V03

The failure is no longer primarily interaction overload.

The model appears to have a strong semantic prior for the jacket being either:

```text
unworn / held
```

or:

```text
fully worn
```

The asymmetric intermediate state — one arm already inserted while the other sleeve remains completely empty — is unstable when described only in text. Even after the prompt allocates the entire clip to one action, the model collapses the opening state into the more common fully worn state and replaces the requested interaction with a safer garment-adjustment motion.

This is best classified as an **intermediate-state representation failure** rather than a simple wording failure.

---

# V04 — reference-conditioned partial-state experiment

V04 is intentionally not another text-only repair. It tests whether supplying an explicit **first-frame visual reference** for the partial-worn state can overcome the model's semantic tendency to collapse directly to fully worn.

## Test hypothesis

```text
Text-only partial-state instruction
→ model collapses state to fully worn

Explicit visual first-frame / start-frame conditioning
+ concise motion instruction
→ higher probability of preserving the asymmetric partial state
```

This test should use a prepared start image showing the exact target partial state whenever the Flow/Veo workflow allows image-to-video or start-frame conditioning.

### Required V04 start-frame reference

Create or provide a still image with all of these properties before generating the video:

```text
same creator identity
same room / daylight character
same exact navy puffer jacket
RIGHT arm fully inside right sleeve
RIGHT hand naturally outside right cuff
RIGHT shoulder seam already seated on shoulder
LEFT arm fully outside jacket
LEFT sleeve visibly empty
LEFT sleeve opening clearly readable
jacket open at front
center zipper aligned
no left hand hidden inside jacket
no ambiguous crossed arms
three-quarter front framing
camera nearly static
```

The start image should make the empty left sleeve and external left arm visually undeniable. Do not use a pose where the left arm is hidden behind the torso, jacket, or camera crop.

## V04 CLIP 1 — REFERENCE-CONDITIONED ONE-SLEEVE INSERTION

```text
TITLE
Navy Puffer Fit Review — V04 Clip 1 — Reference-Conditioned Sleeve Insertion

INPUT PRIORITY
1. The supplied V04 start-frame image defines the exact opening body and garment state.
2. The original navy puffer product reference defines jacket geometry, color, quilting, collar, zipper, cuffs, pockets, material, length, and proportions.
3. Previous successful clips define creator identity, room, daylight, and casual UGC character when needed.

OBJECTIVE
Generate one 8-second vertical 9:16 realistic smartphone UGC video that CONTINUES DIRECTLY from the supplied V04 start frame.

Do not reinterpret or recreate the opening pose. The first video frame must match the supplied start-frame state: right arm already inside the right sleeve, left arm outside the jacket, and left sleeve visibly empty.

The only major action is for the creator to insert the LEFT arm into the already-visible empty left sleeve and finish wearing the jacket.

OPENING STATE — PRESERVE THE INPUT IMAGE
At frame 1, preserve the exact state shown in the supplied start image:
- RIGHT arm remains fully inside the right sleeve;
- right hand remains outside the right cuff;
- right shoulder remains seated correctly;
- LEFT arm remains outside the jacket;
- LEFT sleeve remains visibly empty;
- left sleeve stays attached to the correct left shoulder seam;
- jacket remains open;
- centered zipper remains aligned;
- jacket geometry, scale, quilting, color, collar, cuffs, pockets, hem, and length remain unchanged.

Do not convert this opening state into a fully worn jacket before the visible motion begins.

0:00–0:01.0 — PRESERVE THE START STATE
Continue naturally from the supplied first frame with almost no movement.

The viewer must still clearly see:
- right arm inserted;
- left arm outside;
- left sleeve empty.

No dialogue. No cut. No camera move.

0:01.0–0:05.8 — LEFT ARM ENTERS THE EMPTY LEFT SLEEVE
The creator slowly moves the LEFT hand into the existing left sleeve opening.

Show the action continuously:
1. left fingertips enter the sleeve opening;
2. left hand travels through the sleeve;
3. left forearm follows the sleeve path;
4. left elbow bends naturally;
5. fabric gathers and shifts around the forearm;
6. left hand emerges naturally from the left cuff.

The left sleeve must stay visibly connected to the left shoulder seam throughout the motion.

The right side of the jacket remains already worn. The right hand may lightly stabilize the jacket front, but no second complex action occurs.

Use realistic textile resistance, gravity, mild compression, shoulder loading, and folds. No hidden transition, no full-body occlusion, no fast arm motion.

0:05.8–0:07.0 — SHOULDER SETTLE
After the left hand exits the cuff, the creator gently rolls the left shoulder and allows the jacket to settle naturally across both shoulders.

One small downward adjustment of the front panel is acceptable.

Keep the jacket open. Do not zip it.

0:07.0–0:08.0 — END-STATE HOLD
Hold the final worn state clearly for one second.

Both arms are now correctly inside the sleeves, both hands outside the cuffs, jacket open, product geometry unchanged.

No dialogue required.

CAMERA
Vertical 9:16 smartphone UGC.
Nearly static three-quarter framing.
Natural home daylight.
No orbit, zoom, dolly, whip, rack-focus trick, or reframing that hides the sleeve action.

AUDIO
Quiet room ambience and realistic fabric rustle only.

STRICTLY FORBIDDEN
- do not ignore or redesign the supplied start frame
- do not begin fully worn
- do not place the left arm inside the sleeve before visible motion begins
- do not collapse the partial state into a fully worn state at frame 1
- no hard cuts
- no creator disappearance
- no empty-room bridge frame
- no teleporting garment
- no instant wardrobe transformation
- no sleeve swapping sides
- no sleeve detachment
- no sleeve-length change
- no arm passing through fabric
- no duplicated arms, hands, sleeves, or cuffs
- no hidden state jump behind body occlusion
- no hand emerging outside the real cuff path
- no quilt-pattern drift
- no zipper relocation
- no garment resizing
- no mirror shot
- no dialogue over the insertion

PASS CONDITION
V04 passes only if:
1. the first video frame preserves the supplied partial-worn reference state;
2. the left sleeve is visibly empty at the beginning;
3. the left arm visibly enters that same sleeve;
4. the left hand visibly emerges from the correct cuff;
5. there is no cut, disappearance, teleport, or hidden state jump;
6. jacket geometry remains stable throughout.
```

## V04 fallback if start-frame conditioning is unavailable

If the workflow cannot accept a true start image, do **not** run the same text-only V04 prompt and expect a different result.

Use a two-stage workaround instead:

```text
Stage A: create a still image of the exact partial-worn state
Stage B: use that still as image-to-video input / first-frame reference
```

If neither first-frame nor image-to-video conditioning is available, stop testing the sleeve insertion in this workflow and classify the interaction as **unsupported / unreliable for production**.

## V04 experiment design

The goal of V04 is not merely to obtain a nicer clip. It tests whether the failure is caused by text-only state representation.

Keep other variables fixed:
- same creator;
- same product;
- same room;
- same 8-second duration;
- same single sleeve-insertion action;
- no dialogue;
- no internal cut;
- near-static camera.

The main changed variable is:

```text
V03: text-only opening-state description
V04: explicit visual opening-state conditioning
```

This makes the result diagnostically useful.

---

# Canonical assembly strategy

If V04 passes:

```text
usable V02 material-inspection segment
→ hard cut
→ V04 successful sleeve insertion
→ hard cut
→ preserved V01/V02 Clip 2 fit hero
→ detail proof
→ verdict
```

If V04 fails but remains visually clean:

```text
usable V02 material-inspection segment
→ hard cut
→ usable V03 already-worn adjustment shot
→ hard cut
→ preserved Clip 2 fit hero
```

Do not keep regenerating an unstable try-on interaction indefinitely for a production deliverable.

---

# Generalized lessons from V01–V04

## Repair hierarchy for difficult garment interactions

```text
1. reduce simultaneous limb and garment interactions
2. remove unrelated actions from the shot
3. remove internal cuts
4. allocate most of the clip to one physical action
5. define explicit start and end states
6. if text-only start state repeatedly collapses, switch to visual start-state conditioning
7. after repeated failure, preserve the story through editing rather than endless regeneration
```

## New failure class

A useful distinction from this case:

```text
interaction-overload failure
!=
temporal-skip failure
!=
intermediate-state representation failure
```

V01 primarily showed interaction overload and physical morphing.
V02 primarily showed temporal skipping.
V03 primarily showed intermediate-state collapse and interaction substitution.
V04 tests whether explicit visual state conditioning can solve that final failure mode.

## Production principle

The try-on itself is not the main buyer proof. Material, silhouette, fit, proportions, and movement are more important to the viewer.

Generation experiments may continue for learning, but production reliability should outrank showing every intermediate dressing step.

## Next step

1. Prepare a V04 start-frame image with the exact one-arm-in / one-arm-out state.
2. Generate V04 Clip 1 using that image as start-frame or image-to-video conditioning.
3. QA first-frame preservation before evaluating later sleeve physics.
4. If frame 1 already collapses to fully worn, mark V04 failed immediately without over-analyzing later movement.
5. If V04 passes, reuse V02 material proof and preserved Clip 2 for the final assembly.
