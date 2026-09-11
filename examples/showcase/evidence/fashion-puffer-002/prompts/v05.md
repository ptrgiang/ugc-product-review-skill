# FASHION-PUFFER-002 — V05 test prompt

Status: **ready for generation**

## Experiment goal

V05 tests a stricter conditioning mode than V04.

V04 showed that a visually supplied reference state may still be treated as appearance guidance rather than an immutable first frame. V05 is valid only when the partial-worn still is used as the **literal first frame / image-to-video initial image**.

```text
V04
reference-conditioned image
→ model may reconstruct an earlier dressing state

V05
literal first-frame image-to-video input
→ frame 1 is fixed
→ animate only forward from the supplied partial state
```

## Required first-frame image

The input still must already show all of the following clearly:

```text
RIGHT arm fully inside right sleeve
RIGHT hand outside right cuff
RIGHT shoulder correctly seated
LEFT arm fully outside jacket
LEFT sleeve visibly empty
LEFT sleeve opening clearly readable
jacket open at front
center zipper aligned
product geometry matching the original reference
same creator / room / daylight character
```

The image must be supplied through the workflow's actual **Start Frame / First Frame / Image-to-Video Initial Image** control. Do not use it only as a generic reference image.

## V05 Clip 1 — Literal First-Frame Sleeve Insertion

```text
TITLE
Navy Puffer Fit Review — V05 Clip 1 — Literal First-Frame Sleeve Insertion

GENERATION MODE
Image-to-video using the supplied partial-worn still as the literal first frame of the video.

The first generated frame must be the supplied image itself. Do not reinterpret, reconstruct, replace, or precede that opening frame.

OBJECTIVE
Animate only one forward action from the supplied first frame: the creator inserts the LEFT arm into the already-visible empty LEFT sleeve, the left hand emerges from the cuff, and the jacket settles naturally on both shoulders.

Do not show or reconstruct any earlier dressing state.
Do not begin before the supplied image.
Do not explain how the creator reached this pose.

PRODUCT / CREATOR LOCK
Preserve all visible identity and product information already present in frame 1. Keep the exact creator, room, lighting, jacket color, quilt geometry, collar, centered zipper, sleeves, cuffs, pockets, hem, length, puffiness, scale, and silhouette.

0:00–0:00.8 — HOLD THE EXACT FIRST-FRAME STATE
Begin exactly from the supplied image.

Keep movement minimal so the viewer can clearly read:
- right arm already inserted;
- right hand outside the cuff;
- left arm outside the jacket;
- left sleeve visibly empty.

No cut. No camera move. No dialogue.

0:00.8–0:05.8 — ANIMATE ONLY THE LEFT-ARM INSERTION
The creator slowly moves her LEFT fingertips into the visible LEFT sleeve opening.

Maintain one continuous physical path:
left fingertips enter sleeve opening
→ left hand travels through sleeve
→ forearm follows
→ elbow bends naturally
→ sleeve fabric gathers around the forearm
→ left hand emerges from the correct left cuff.

The same left sleeve remains continuously attached to the left shoulder seam.
The right side of the jacket remains already worn.
The right hand may lightly stabilize the jacket front but performs no separate complex action.

Use realistic textile resistance, gravity, mild compression, shoulder loading, and soft folds.

No full-body occlusion.
No fast motion.
No camera trick that hides the sleeve path.

0:05.8–0:07.0 — NATURAL SETTLE
After the left hand exits the cuff, the creator makes one small left-shoulder roll and lets the jacket settle across both shoulders.

One small downward tug on the front panel is acceptable.
Keep the jacket open.
Do not zip it.

0:07.0–0:08.0 — END-STATE HOLD
Hold the completed worn state for one second.

Both arms are inside the correct sleeves.
Both hands are outside the cuffs.
The jacket remains open and visually identical to the product reference.

CAMERA / AUDIO
Static or nearly static vertical smartphone UGC framing.
Natural daylight.
Quiet room ambience and subtle fabric rustle only.

DO NOT
- reconstruct an earlier unworn state
- change or replace frame 1
- remove the jacket from the body
- begin with both arms outside
- begin fully worn
- hide the left sleeve opening
- cut away during insertion
- teleport the left hand to the cuff
- pass the arm through fabric
- duplicate limbs, sleeves, hands, or cuffs
- change jacket geometry, scale, quilting, zipper, collar, sleeve length, or color
- add mirror shots, dialogue, zipper use, or unrelated actions

PASS CONDITION
V05 passes only if:
1. frame 1 is the supplied partial-worn image itself;
2. the left sleeve is visibly empty at the beginning;
3. the left hand enters that exact visible sleeve opening;
4. the arm path remains physically continuous;
5. the left hand exits the correct cuff;
6. jacket geometry remains stable;
7. no earlier dressing state is reconstructed.
```

## Validity rule

If the platform does not have a mode that guarantees the supplied image is the literal first frame, **do not count that run as V05**. It would only repeat V04 with a different prompt.

If V05 uses a true literal-first-frame mode and still fails, classify this one-arm sleeve-insertion interaction as **unreliable / unsupported for production in the tested model-workflow combination** and stop repairing this specific interaction.
