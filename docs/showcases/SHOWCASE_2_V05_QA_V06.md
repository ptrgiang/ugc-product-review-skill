# Showcase #2 — V05 QA and V06 Prompt Branches

## V05 Verdict

**Status:** FAIL  
**Severity:** P1 — Major  
**Primary failure:** Opening-state compliance / temporal setup

V05 does **not** satisfy the intended first-frame-lock experiment because the generated video begins from an unworn jacket state and reconstructs the dressing sequence before reaching the requested partial-worn state.

At the same time, the clip provides useful positive evidence: once the model is allowed to create its own transition, the left-sleeve insertion and jacket settling are comparatively plausible.

## Test Objective

Evaluate whether the model can begin directly from a specified **partial-worn asymmetric jacket state** and continue a controlled try-on action without reconstructing earlier states.

Required opening state:

- creator already has the **right arm fully inside the right sleeve**
- right side of the jacket already seated on the shoulder
- **left sleeve remains empty**
- left arm remains outside the jacket
- jacket geometry, quilting, color, and proportions match the reference
- no pre-roll from an unworn state
- no jacket morphing into place

Target continuation:

`partial-worn → left-arm insertion → jacket settles → fully worn fit proof`

## Observed Result

Actual sequence:

`unworn → jacket lifted/positioned → partial-worn → left-arm insertion → settling → fully worn`

The generated sequence therefore contains an earlier state that should not exist in this test.

The model effectively interpreted the requested first-frame state as a **story target to reconstruct**, not as a literal initial visual condition.

## Pass / Fail Conditions

### 1. Literal opening-state preservation

**Expected:** First generated frame already matches the partial-worn state.  
**Observed:** Creator begins without the jacket fully established in the requested asymmetric state.  
**Result:** FAIL

### 2. No earlier-state reconstruction

**Expected:** No unworn or pre-dressing state appears.  
**Observed:** The model reconstructs the dressing setup before reaching the requested state.  
**Result:** FAIL

### 3. Product fidelity

The navy quilted jacket remains visually stable overall. Color, quilting, general silhouette, and proportions stay consistent through most of the clip.

**Result:** PASS

### 4. Creator consistency

Face, hair, clothing underneath the jacket, body proportions, and room environment remain consistent.

**Result:** PASS

### 5. Left-sleeve insertion readability

The insertion action is more legible and physically plausible than in earlier iterations. The left arm visibly progresses into the sleeve instead of the garment simply teleporting to the final state.

**Result:** PARTIAL PASS

### 6. Fabric and body physics

Sleeve motion, shoulder settling, and hand interaction are generally believable. No severe garment explosion, floating, or major anatomy failure is observed.

**Result:** PASS

### 7. UGC realism

Static smartphone-like framing, ordinary bedroom environment, natural creator behavior, and low-polish presentation remain appropriate for UGC.

**Result:** PASS

## QA Scores

| Dimension | Score |
|---|---:|
| Product fidelity | 9.0 / 10 |
| Creator identity | 9.0 / 10 |
| Hands / body mechanics | 8.5 / 10 |
| Fabric physics | 8.5 / 10 |
| State continuity after setup | 8.0 / 10 |
| Camera realism | 9.0 / 10 |
| UGC authenticity | 9.0 / 10 |
| Left-sleeve action readability | 7.0 / 10 |
| Opening-state compliance | 0.0 / 10 |
| No-earlier-state compliance | 0.0 / 10 |
| Objective completion | 3.5 / 10 |

## Error Tags

```text
OPENING_STATE_VIOLATION
EARLIER_STATE_RECONSTRUCTION
FIRST_FRAME_CONTRACT_FAILED
TEMPORAL_REINTERPRETATION
PROMPT_MODE_MISMATCH
```

## Root Cause

### Primary root cause: no actual first-frame image was supplied

The prompt described the partial-worn image as a literal start frame, but the generation input did not contain an actual partial-worn start-frame image.

Therefore the model had no image-level visual state to preserve.

The instruction:

> start from this exact partial-worn state

was effectively treated as:

> create a sequence that reaches this partial-worn state

This is a mismatch between **prompt semantics** and the actual **generation mode/input configuration**.

### Secondary root cause: asymmetric clothing states are temporally unstable

A state where one sleeve is worn while the opposite sleeve is empty is mechanically unusual and visually transitional. Without a fixed image condition, the model has a strong tendency to infer and reconstruct the preceding dressing motion.

## What V05 Proves

V05 does **not** prove that text prompting alone can lock a literal partial-worn opening state.

It does provide evidence that the model can generate a comparatively believable jacket try-on when allowed to create its own temporal setup.

This suggests two different V06 experiments should now be separated:

- **V06A:** true first-frame-lock experiment
- **V06B:** production-oriented motion experiment

Do not combine these objectives into one prompt.

---

# V06A — True Start-Frame Lock

## Goal

Test one narrow hypothesis:

> Can the model preserve a real supplied partial-worn image as the literal first frame and continue only the missing left-sleeve insertion?

## Required Input

This branch **requires an actual start-frame image** showing:

- same creator
- same bedroom
- same navy quilted jacket
- right arm fully inside the right sleeve
- right shoulder already seated
- left sleeve visibly empty
- left arm fully outside the jacket
- no ambiguous overlap between left hand and sleeve opening

If no such image is supplied, do not run V06A.

## Generation Prompt

```text
Create a realistic vertical 9:16 smartphone UGC continuation from the supplied start-frame image.

The supplied image is the literal first frame of the video. Preserve it exactly at the beginning. Do not reconstruct any earlier dressing action.

The creator, bedroom, clothing, body proportions, camera position, navy quilted jacket, jacket color, quilting pattern, silhouette, sleeve length, zipper position, and garment scale must remain consistent with the supplied image.

OPENING STATE — LOCK THIS EXACTLY

At frame 1:
- the creator's RIGHT arm is already fully inside the jacket's right sleeve
- the right shoulder of the jacket is already seated naturally
- the LEFT sleeve is completely empty
- the creator's LEFT arm is outside the jacket
- the left sleeve opening is clearly visible and physically separate from the left hand
- the jacket must not jump, morph, teleport, or reset to an unworn state

Do not show:
- the jacket off the body
- both sleeves empty
- the right arm entering the jacket
- the creator picking up the jacket
- any action occurring before this supplied start frame

ACTION

From the locked opening state, the creator naturally inserts only her LEFT arm into the empty left sleeve.

She looks down briefly at the sleeve opening, guides her left hand into it, pushes her arm through in one continuous natural motion, then gives the jacket a small shoulder adjustment.

The jacket should react with realistic padded-fabric resistance and gravity.

The sleeve must remain visibly attached to the jacket throughout the action. No sleeve duplication, shortening, stretching, detachment, or geometry change.

ENDING

End with the jacket fully worn on both arms.

The creator gives one small natural fit-check gesture near the front panels and looks back toward the camera with a subtle satisfied expression.

CAMERA

Static or nearly static smartphone camera at approximately chest-to-full-body framing.

Natural bedroom daylight.

No cinematic camera movement.
No zoom.
No orbit.
No reframing transition.
No slow motion.

PERFORMANCE

Casual, understated social-media try-on behavior.

No exaggerated smiling.
No commercial-model posing.
No dramatic acting.

NEGATIVE CONSTRAINTS

No jacket morphing.
No garment teleportation.
No missing sleeve.
No duplicated sleeve.
No arm clipping through fabric.
No impossible elbow bending.
No extra fingers.
No body deformation.
No sudden camera cut.
No reset to an earlier clothing state.
No generated captions or text.
```

## V06A Pass Conditions

A successful result must satisfy all of the following:

1. frame 1 visibly matches the supplied start frame
2. no unworn state appears
3. right arm never exits or re-enters the jacket
4. only the left arm completes the dressing action
5. left-sleeve insertion is visually readable
6. jacket geometry remains stable
7. final state is fully worn without morphing

If condition 1 fails, classify the whole experiment as failed regardless of later motion quality.

---

# V06B — Production-Optimized Try-On

## Goal

Generate the most believable usable UGC try-on clip without requiring a fragile literal asymmetric opening state.

This branch prioritizes:

**natural motion > strict start-state experiment**

## Generation Prompt

```text
Create a realistic 8-second vertical 9:16 smartphone UGC fashion try-on video in an ordinary bright bedroom.

Use the same creator and the exact same navy quilted jacket throughout the entire video.

Preserve the creator's face, hair, complexion, body proportions, white fitted long-sleeve top, black wide-leg pants, and white shoes.

Preserve the jacket's exact navy color, padded quilting, body length, collar shape, zipper layout, sleeve proportions, material, and overall silhouette.

The clip should feel like a real casual social-media try-on, not a fashion commercial.

0:00–0:01.5 — FAST SETUP

Start with the creator already holding and positioning the jacket around her torso.

The right side of the jacket is immediately close to the right shoulder and the right arm begins entering or is nearly seated in the right sleeve.

Do not spend time showing the jacket folded, picking it up, or presenting it to camera.

The viewer should understand within the first second that she is putting the jacket on.

0:01.5–0:04.5 — CLEAR LEFT-SLEEVE ACTION

The right side becomes naturally seated first.

Then keep the left-arm insertion clearly visible.

The creator looks briefly toward the empty left sleeve opening, reaches her left hand into it, and pushes the left arm through in one continuous motion.

Prioritize clear hand-to-sleeve contact and believable padded-fabric resistance.

Do not hide the insertion behind the torso.

Do not let the jacket instantly snap into the fully worn state.

0:04.5–0:06 — SETTLE

The jacket naturally settles onto both shoulders.

The creator makes one small adjustment near the collar or front panels.

The fabric responds with realistic weight and quilting.

0:06–0:08 — FIT PROOF

Hold a clean full-body view long enough to read the final fit.

The creator faces the camera, lightly touches the front of the jacket, and gives a restrained satisfied expression.

Keep the final fully worn state visible for at least one second.

CAMERA

Vertical 9:16 smartphone video.

Static tripod-like phone or extremely subtle handheld movement.

Natural bedroom daylight.

Minor realistic autofocus or exposure breathing is acceptable.

No cinematic orbit.
No dramatic push-in.
No fashion-film camera choreography.

PHYSICS

Hands must visibly contact the garment before moving it.

Sleeves maintain constant length and attachment.

The jacket has believable padded weight.

Shoulders, elbows, and wrists follow normal human movement.

The jacket may wrinkle and compress naturally but must not change design.

EDITING

Prefer one continuous shot.

If a cut is absolutely necessary, use only one hard cut and preserve body pose and garment state across the cut.

No transitions.
No speed ramp.
No montage.

NEGATIVE CONSTRAINTS

No garment morphing.
No instant fully-worn teleport.
No disappearing sleeve.
No duplicated fabric.
No detached jacket panels.
No extra buttons, pockets, logos, or design changes.
No hand deformation.
No extra fingers.
No arms passing through fabric.
No constant smiling.
No staged commercial posing.
No captions.
No logo card.
```

## V06B Pass Conditions

For production use, prioritize:

- product recognizable within the first second
- right side settles quickly without obvious artifact
- left-arm insertion remains visible and continuous
- no major clothing morph
- final fit is readable for at least one second
- creator motion feels casual rather than choreographed

Unlike V06A, an initial setup state is allowed as long as it is brief and physically believable.

## Recommended Test Decision

Run the branches as separate experiments.

**V06A** answers a technical question about start-frame conditioning.

**V06B** answers a production question about whether the model can deliver a usable fashion try-on clip.

The results should not be scored against the same opening-state criterion.
