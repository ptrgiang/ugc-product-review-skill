# FLOW-APPLIANCE-001 — V03 clip 2 targeted repair

Status: **ready to generate**

V03 keeps V02 clip 1 unchanged and repairs only the continuation-state failure observed in V02 clip 2. The single major change is a hard **immutable opening state**: the salsa must already be processed before the first frame and must not transform during lid opening.

## Generation prompt

```text
TITLE
Food Processor Salsa Review — V03 Clip 2 — Finished-State Reveal Repair

OBJECTIVE
Create an 8-second vertical 9:16 realistic smartphone UGC continuation clip.
This clip begins after the processing shown in V02 clip 1 has fully finished.
The only goal is to reveal the already-finished salsa and give a restrained natural verdict.

REFERENCE PRIORITY
1. Use the original supplied product reference as the authority for appliance geometry, color, materials, bowl, lid, right-side handle, central spindle, controls, scale, and visible branding.
2. Use V02 clip 1 only as the continuity reference for creator, wardrobe, kitchen, daylight, counter position, framing character, and overall product placement.
If V02 clip 1 conflicts with the original product reference, preserve the original product reference.

CONTINUITY LOCK
Keep the exact same white appliance body, proportions, clear processing bowl, clear locking lid, right-side clear handle, central spindle, two circular front controls, creator, wardrobe, kitchen, countertop position, daylight direction, and casual smartphone UGC character.
Do not redesign, add, remove, move, or simplify any product part.

IMMUTABLE OPENING STATE — CRITICAL
The processing cycle has already fully finished before the first frame of this clip.
At frame 1:
- the same bowl is attached to the same appliance;
- the machine is stopped;
- the lid is fully closed and locked;
- the contents underneath the closed lid are already the final processed chunky salsa;
- no raw or coarse pre-processing ingredients exist anywhere in this clip.

This finished food state is immutable.
Opening the lid does not cause, trigger, or complete any transformation.
The salsa must already be processed before the lid starts moving.

FORBIDDEN REGRESSIONS
Never show the earlier coarse/raw ingredient state.
Never reset the bowl to the pre-processing state.
Never morph the contents during or after lid movement.
Never make finished salsa suddenly appear after the lid opens.
No second processing event occurs in this clip.

CAMERA / STYLE
Natural bright home-kitchen daylight. Vertical 9:16 casual smartphone UGC. Stable medium-close counter-height framing, slight human handheld imperfection only. Product and bowl readable. No cinematic orbit, no studio ad lighting, no generated captions, no logo card.

TIMELINE
0:00–0:02 — OPEN ALREADY-FINISHED BOWL
Start on the stopped appliance with the lid still closed.
One hand stabilizes the bowl/appliance. The other releases and lifts the existing lid in one simple physically plausible motion.
As the lid lifts, the same already-finished chunky salsa is continuously visible underneath. Its texture does not change.
Natural latch/contact sound. No dialogue.

0:02–0:05 — HERO PROOF
Hold a stable close-medium view of the open bowl and appliance for about 3 seconds.
Make the finished chunky salsa texture easy to read.
No dialogue during the clearest first 1.5–2 seconds of this hero hold.
No stirring, pouring, or other action that obscures the result.

0:05–0:08 — NATURAL VERDICT
Keep the result visible.
The creator briefly looks from the salsa to the phone with a small impressed reaction and says:
“Okay... that actually came out really good.”
No thumbs-up, pointing, broad grin, product beside face, or commercial presenter pose.
Finish as though the creator is about to keep using or tasting the result.

AUDIO
Natural kitchen room tone + lid/latch contact + natural voice.
No dramatic music.

PHYSICS / PRODUCT FIDELITY
Realistic hand grip and product weight. Stable bowl attachment. Correct lid geometry. Same handle direction. Same control layout. No floating parts, deformed hands, changing product scale, logo drift, control drift, lid morphing, or impossible food physics.

PASS CONDITION
V03 only passes if the very first visible food state is already processed salsa and that exact processed state remains unchanged through lid opening and hero reveal.
```

## Generation setup

Use:

- the original product reference as the primary visual authority;
- V02 clip 1 as the continuity anchor for creator/environment/session consistency;
- this prompt for **clip 2 only**.

Do not regenerate V02 clip 1. This keeps the experiment controlled and tests whether explicitly locking the first-frame state repairs the observed failure.

## V03 pass criteria

V03 passes if:

- the bowl contains finished salsa from the first visible food frame;
- no raw/coarse state appears anywhere in the clip;
- lid opening reveals rather than causes the finished result;
- product geometry and controls remain faithful to the reference;
- hands/lid interaction remain physically plausible;
- the hero result receives readable stable screen time;
- the verdict remains observational rather than commercial.
