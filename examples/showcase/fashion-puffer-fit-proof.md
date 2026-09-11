# Showcase #2: Navy quilted puffer jacket — fit-proof UGC

Status: **V02 QA completed — V03 dedicated try-on repair proposed**

## At a glance

**Case ID:** `FASHION-PUFFER-002`

**Product/category:** Navy quilted puffer jacket / fashion

**Workflow/model:** Google Flow / Veo, using the practical constraint of **8 seconds per generated clip**

**Creative angle:** Buyer-doubt-led fit proof with product inspection, controlled try-on, mirror proof, and a natural verdict

**Primary visual proof:** The jacket's real-world silhouette, puffiness, shoulder fit, length, and material behavior while handled and worn

**Current result:** V02 Clip 1 was generated and QA'd. Product fidelity and creator continuity improved, but the repair still fails because the model skips the sleeve-insertion interaction via a temporal discontinuity. V01 Clip 2 remains substantially usable. A **V03 dedicated single-action try-on prompt** is proposed below.

**QA:** V01 completed; V02 completed with `P1 — Major`; V03 repair prompt ready

## Why this case uses native 8-second clips

Showcase #1 established a practical production lesson for the tested Google Flow / Veo workflow: asking one generation to carry a long multi-state story creates unnecessary temporal pressure when the workflow practically returns 8-second clips.

Showcase #2 therefore uses native 8-second blocks and preserves successful surrounding shots instead of regenerating the whole sequence.

## Evidence

Product/reference input: a navy quilted puffer jacket reference image was supplied for this case.

Generated-video evidence status:
- V01 Clip 1: generated, QA failed during dressing interaction
- V01 Clip 2: generated, substantially usable
- V02 Clip 1: generated, QA failed due to omitted try-on interaction / temporal skip
- V03 Clip 1: proposed dedicated single-action repair

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

# V01 summary

## V01 outcome

- **Clip 1:** failed during the full dressing motion.
- **Clip 2:** substantially usable and should be preserved by default.

## V01 QA

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

### V01 repair strategy

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

# V02 production repair

V02 Clip 1 kept the successful material inspection and attempted one controlled sleeve insertion after a hard cut.

The critical requested progression was:

```text
right arm already inserted
→ left sleeve still empty
→ left arm visibly travels through sleeve
→ left hand emerges from cuff
→ garment settles
```

The intended constraints included:
- exact product geometry and color lock;
- same creator and room continuity;
- one major dressing action only;
- nearly static camera during insertion;
- no zipper interaction;
- no sleeve swapping, garment resizing, morphing, teleporting, or body-fabric intersection.

Clip 2 remained an already-worn fit-proof shot and was preserved by default.

---

# V02 QA — Clip 1

## Verdict

`P1 — Major / REGENERATE CLIP 1`

V02 materially improved product fidelity, creator consistency, hand quality, and fabric realism compared with V01, but it **did not pass the actual repair objective**. The model avoided the fragile sleeve-insertion action by skipping directly from an unworn state to a fully worn state.

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

## Observed transition failure

Around the transition, the generated sequence behaves approximately like this:

```text
creator holding unworn jacket
→ hard cut
→ creator temporarily absent / empty room
→ hard cut
→ creator reappears with jacket already fully worn
```

The requested state progression was:

```text
right arm already inserted
→ left sleeve visibly empty
→ left arm travels through sleeve
→ left hand emerges from cuff
→ garment settles
```

The difficult interaction is therefore still omitted rather than solved.

## Error tags

```text
STATE_DISCONTINUITY
TRY_ON_ACTION_OMITTED
TEMPORAL_SKIP
SUBJECT_DISAPPEARANCE
INTERACTION_GOAL_NOT_EXECUTED
```

## What worked

The opening material-inspection portion is substantially usable. The jacket remains visually consistent, hand contact is plausible, and the quilted fabric behaves naturally enough for UGC review footage.

The post-transition already-worn state is also substantially usable as an independent fit-proof shot. The failure is localized primarily to the handoff between the unworn and worn states.

## Root cause update

V02 reduced the original multi-limb complexity, but still asked one 8-second generation to perform several phases:

```text
material inspection
→ hard cut
→ partial try-on setup
→ constrained sleeve insertion
→ garment settling
→ reaction
```

The model still found a lower-cost temporal solution: omit the highest-complexity interaction and jump directly to the completed state. Additional negative constraints alone are unlikely to solve this reliably.

The next repair should therefore change **shot architecture**, not merely add stronger wording.

---

# Proposed canonical repair — V03

V03 removes material inspection from the repair clip entirely. The full 8-second generation is dedicated to **one continuous sleeve-insertion action**.

The clip must begin directly in the partial-worn state so the model is never asked to invent the transition from holding the jacket to partially wearing it.

## V03 CLIP 1 — DEDICATED SINGLE-ACTION SLEEVE INSERTION

```text
TITLE
Navy Puffer Fit Review — V03 Clip 1 — Dedicated Sleeve Insertion

OBJECTIVE
Create one 8-second vertical 9:16 realistic smartphone UGC clip using the exact navy quilted puffer jacket from the supplied product reference.

This clip has ONE purpose only: show one physically continuous left-arm sleeve insertion from a stable partial-worn starting state to a fully worn open-jacket state.

Do not include material inspection, unboxing, dialogue, zipper use, mirror reveal, or any other product action.

PRODUCT LOCK
Preserve exactly the reference jacket's deep navy color, horizontal quilt geometry and panel spacing, material finish, believable puffiness, stand collar, centered front zipper, sleeves, cuffs, hem, visible pockets, jacket length, proportions, scale, and silhouette.

The jacket must remain the same physical object throughout all 8 seconds. No redesign, resizing, color drift, quilt-pattern change, zipper relocation, collar change, sleeve-length change, added features, or sudden puffiness change.

CREATOR / ENVIRONMENT
Use the same creator identity, face, hair, complexion, body proportions, base outfit, ordinary bright bedroom or dressing area, daylight direction, and casual smartphone UGC character established by the previous clips when continuity references are supplied.

Camera is nearly static at chest-to-three-quarter height. Slight natural phone imperfection is acceptable, but no orbit, zoom, whip, reframing, or cinematic movement.

IMMUTABLE OPENING STATE — FRAME 1
At the very first frame, the creator is ALREADY partially wearing the jacket.

The starting state must already satisfy all of the following:
- RIGHT arm fully inside the correct right sleeve;
- right hand naturally outside the right cuff;
- right shoulder seam correctly resting on the right shoulder;
- right side of the jacket hanging naturally from the torso;
- LEFT sleeve completely empty and visibly attached to the correct left shoulder seam;
- left arm outside the jacket and positioned naturally beside the left sleeve opening;
- jacket open at the front;
- centered zipper aligned correctly;
- collar, quilting, cuffs, hem, pockets, jacket length, scale, and silhouette already match the supplied reference.

Do not show any earlier state. Do not show the jacket being held as an unworn object. Do not cut away from this partial-worn starting state.

0:00–0:01.5 — HOLD THE PARTIAL STATE
Hold the starting state long enough for the viewer to clearly understand that the right arm is already inserted and the left sleeve is still empty.

The creator makes only a small natural body adjustment. No dialogue. No camera movement beyond subtle handheld breathing.

0:01.5–0:05.5 — ONE CONTINUOUS LEFT-ARM INSERTION — CRITICAL
The creator slowly inserts her LEFT arm into the existing left sleeve.

This is the only major action in the clip.

The left hand and forearm must move continuously through the physical sleeve path. The sleeve remains visibly connected to the left shoulder seam at all times. The left hand naturally emerges from the left cuff near the end of the motion.

Preserve realistic fabric resistance, textile compression, gravity, shoulder loading, elbow bending, and soft folds. The garment may shift slightly on the torso because of the real arm motion, but its geometry and scale must remain unchanged.

The right hand may lightly stabilize the left front opening or shoulder area, but it must not perform a second complex action.

No cuts during this insertion. No hidden transition. No temporary empty frame. No occlusion trick that conceals the entire arm path.

0:05.5–0:07.0 — GARMENT SETTLES
Once the left hand is naturally outside the left cuff, the creator gently rolls the left shoulder once and makes one small downward tug at the front panel so the jacket settles naturally across both shoulders.

Keep the jacket open. Do not touch the zipper.

0:07.0–0:08.0 — END STATE HOLD
Hold the completed worn state for one full second. Both arms are fully inserted, both hands are outside the cuffs, the jacket is open, and the garment sits naturally on both shoulders.

The creator looks down briefly at the fit with a restrained, natural expression. No dialogue is required.

AUDIO
Quiet room ambience and realistic clothing rustle only. No dialogue during the sleeve insertion. No music required.

STRICTLY FORBIDDEN
- no hard cut inside this clip
- no creator disappearance
- no empty-room bridge frame
- no jacket teleporting onto the torso
- no instant wardrobe transformation
- no sleeve swapping sides
- no sleeve detaching from the shoulder
- no sleeve changing length
- no arm passing through fabric
- no hidden full-state jump behind a cut or camera move
- no duplicated arms, hands, or cuffs
- no hand emerging from outside the physical sleeve path
- no quilt-pattern change
- no zipper relocation
- no garment resizing
- no mirror shot
- no camera orbit or dramatic reframing

END-STATE CONTRACT
At the end of the clip:
- both arms are fully inside the correct sleeves;
- both hands are naturally outside the cuffs;
- the jacket is correctly settled on both shoulders;
- the jacket remains open;
- product geometry still matches the original reference exactly;
- creator identity, base outfit, room, and lighting remain compatible with the preserved fit-proof Clip 2.

PASS CONDITION
The clip passes only if the left-arm insertion is visibly continuous from the partial-worn first frame through hand emergence from the cuff, with no cut, no disappearance, no temporal skip, no garment morph, and no body-fabric intersection.
```

## V03 edit strategy

Do not regenerate material inspection unless necessary. The strongest usable material-proof portion from V02 can be retained in editing.

Recommended assembly:

```text
usable V02 material-inspection segment
→ hard cut
→ V03 dedicated sleeve-insertion clip
→ hard cut
→ preserved V01/V02 Clip 2 already-worn fit hero
→ detail proof
→ verdict
```

The generation model is therefore responsible for only one fragile interaction at a time.

## New generalized lesson

When a model repeatedly skips a difficult interaction even after the prompt specifies the intermediate state, treat that as a **temporal-planning failure**, not merely a constraint-following failure.

The repair hierarchy should be:

```text
1. remove unrelated actions
2. begin directly from the nearest stable pre-action state
3. allow only one major interaction
4. remove internal cuts
5. give the action most of the clip duration
6. preserve successful surrounding shots instead of regenerating them
```

This is more reliable than indefinitely increasing negative constraints around an overloaded shot.

## Next step

- Generate **V03 Clip 1** using the dedicated single-action prompt above.
- Preserve the usable V02 material-proof segment for edit assembly.
- Preserve **Clip 2** unless an independent defect appears.
- QA V03 specifically on continuous sleeve path, creator persistence, garment geometry, and final state.
