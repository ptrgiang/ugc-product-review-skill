# QA and Repair Module

Load only when evaluating generated output or repairing a prompt.

## 1. QA dimensions

Score 1–5:
- Product Fidelity
- Creator Identity
- Hands
- Physics
- Product State Continuity
- Camera Realism
- Environment Consistency
- Dialogue / Lip Sync
- Audio Realism
- Hook Strength
- Hero Moment
- UGC Authenticity
- Commercial Feel
- Pacing
- Verdict Clarity

Critical:
- Product Fidelity
- Creator Identity
- Physics
- Hero Moment

Any critical score ≤2 requires repair.

## 2. Severity

- P0 Blocking
- P1 Major
- P2 Moderate
- P3 Minor

Fix P0/P1 first.

## 3. Error tags

Product:
- PRODUCT_MORPH
- WRONG_VARIANT
- COLOR_DRIFT
- LOGO_DRIFT
- CONTROL_LAYOUT_ERROR
- SCALE_DRIFT
- STATE_DISCONTINUITY
- NO_CAUSAL_TRANSITION

Creator:
- IDENTITY_DRIFT
- HAIR_DRIFT
- WARDROBE_DRIFT
- BODY_PROPORTION_DRIFT
- EXPRESSION_OVERACTING

Hands/body:
- HAND_DEFORMATION
- EXTRA_FINGERS
- GRIP_ERROR
- BODY_MECHANICS_ERROR
- HIGH_INTERACTION_RISK

Physics:
- LIQUID_PHYSICS
- FABRIC_PHYSICS
- OBJECT_FLOATING
- CONTACT_ERROR
- WEIGHT_ERROR
- HINGE_OR_LATCH_ERROR

Camera/story:
- TOO_CINEMATIC
- UNNATURAL_CAMERA_MOVE
- WEAK_HOOK
- HERO_MOMENT_TOO_FAST
- NO_PAYOFF
- PACING_ERROR
- DIALOGUE_TOO_LONG

Authenticity:
- TOO_COMMERCIAL
- ROBOTIC_PERFORMANCE
- CONSTANT_SMILING
- SCRIPTED_DIALOGUE
- OVER_STAGED_ENVIRONMENT

## 4. Root-cause first

Do not repair only the symptom.

Example:
PRODUCT_MORPH may come from:
- weak reference lock
- too many rotations
- clip too long
- too much hand interaction
- model overload

Repair the cause.

For continuation clips, distinguish:

```text
visual similarity problem
```

from:

```text
causal state problem
```

A clip can match the same product, creator, and environment while still starting from the wrong product state.

Also distinguish a reference-lock failure from an interaction-complexity failure. If the product looks correct before and after an action but breaks during a multi-limb or flexible-material transition, stronger product-lock wording alone may not solve the root cause.

## 5. Targeted repair rules

### Product fidelity
- strengthen product lock
- reduce rotations
- reduce extreme close-ups
- repeat geometry/color/control constraints
- split clip if needed

### Creator identity
- repeat face/hair/wardrobe lock
- reduce dramatic angle changes
- keep lighting/environment stable
- reduce occlusion

### Hands
- one hand stabilizes, one manipulates
- simplify grip
- avoid crossing hands
- reduce finger-level choreography
- shorten close-up

### Physics
- state material property
- state support/contact points
- slow action
- separate setup/action/result

### High-interaction-risk transitions

Use `HIGH_INTERACTION_RISK` when one shot requires several tightly coupled body/object constraints simultaneously, especially:
- multiple limbs plus multiple openings;
- flexible fabric or deformable material;
- substantial occlusion;
- changing body pose;
- precise contact or insertion;
- moving camera during the interaction.

Typical examples include putting on jackets/coats, complex footwear entry, crossing both hands around a product, or manipulating flexible material while changing pose.

Likely root cause:
- the model is being asked to solve too many dependent physical relationships inside one short continuous action.

Repair:
- reduce the shot to one major body-object interaction;
- prefer a stable partial starting state instead of showing the entire transition;
- use a hard cut between believable stable states;
- keep one hand stabilizing while the other performs the key action when possible;
- explicitly preserve contact points, openings, attachment points, and continuous movement through them;
- reduce camera movement during the fragile interaction;
- remove the interaction entirely when it is not the hero proof.

Outerwear example:

```text
held
→ hard cut
→ one arm already fully inserted
→ second arm slides through the remaining sleeve
→ both arms inserted
→ garment settles
```

Avoid forcing this into one short shot:

```text
held
→ first arm enters
→ second arm enters
→ shoulders rotate
→ fabric wraps torso
→ garment settles
```

### State discontinuity / no causal transition

Use when a continuation clip starts in the wrong state, regresses to an earlier state, or makes a result appear during an unrelated action.

Typical symptoms:
- raw ingredients reappear in a post-processing reveal clip;
- a clean surface becomes dirty again before the result shot;
- a product returns to a sealed/pre-use state after an earlier clip already advanced the sequence;
- the result appears only when a lid, door, package, or hand moves, even though the transformation should already have happened off-screen.

Likely root causes:
- opening state is implied rather than explicit;
- continuity anchor describes appearance but not state;
- prompt says “continue after X” without defining frame 1;
- earlier states are not explicitly forbidden;
- too many state changes remain inside the continuation clip.

Repair:
- preserve the previous continuity anchor;
- define an **immutable opening state** before the timeline;
- state what happened before frame 1;
- forbid regression to previous states;
- explicitly state that reveal actions do not cause the already-completed transformation;
- regenerate only the failed continuation clip when the previous clip is already good.

Example:

```text
This clip begins immediately after processing has fully finished.
At frame 1, the finished result already exists under the closed lid.
Do not show raw or partially processed ingredients anywhere in this clip.
Opening the lid only reveals the result; it does not cause the transformation.
```

### Too commercial
Reduce:
- presenter posing
- perfect composition
- feature dumping
- exaggerated reaction
- product beside face

Increase:
- observational dialogue
- product-focused glances
- ordinary environment
- natural continuation after verdict

### Weak hook
Try:
- result-first
- problem-first
- skepticism
- curiosity
- stronger first-frame product visibility

### Hero moment too fast
- allocate more screen time
- remove dialogue over reveal
- reduce camera movement
- simplify surrounding action

## 6. Repair scope

Prefer the smallest repair that targets the diagnosed root cause.

If clip 1 passes and clip 2 fails, do not regenerate both by default. The inverse also applies: if a later clip passes and an earlier interaction fails, preserve the successful clip and regenerate only the failed interaction when the edit structure allows it.

Preserve:
- already-correct product identity
- already-correct creator identity
- already-correct environment
- successful earlier or later clips
- successful hook/proof structure

Change only the variable responsible for the failure when practical.

## 7. Repair output

Return:

### Diagnosis
Top issues.

### Error tags
Tags only.

### Root cause
Brief.

### Repair strategy
Targeted changes.

### Revised prompt
Only affected section unless full rewrite is necessary.

### Preserve
State what should remain unchanged.

## 8. Evidence-backed repair notes

### Multi-state appliance continuation

In a real multi-clip appliance test, a continuation clip matched the product reasonably well but regressed from a finished state back to raw ingredients before the reveal. Rewriting the full sequence was unnecessary.

The successful repair kept the first clip unchanged and modified the continuation prompt with one major addition: an immutable opening-state contract plus forbidden regressions. The next generation began with the result already complete and revealed that same state correctly.

Generalized lesson: **when identity continuity passes but causal state continuity fails, repair the state contract rather than broadening the whole prompt.**

### Fashion outerwear try-on

In a real navy quilted puffer test, product inspection and the already-worn fit clip were substantially usable, but the dressing action in Clip 1 broke during the transition from held garment to worn garment. The jacket appeared to morph/snap onto the creator while arm/sleeve contact and fabric state became ambiguous.

The failure was classified as `P1` with `HIGH_INTERACTION_RISK`, `FABRIC_PHYSICS`, `BODY_MECHANICS_ERROR`, `STATE_DISCONTINUITY`, `CONTACT_ERROR`, and localized `PRODUCT_MORPH`.

The targeted repair preserves the successful fit clip and changes only the failed dressing sequence: hard cut to a partial starting state with one arm already inserted, then show one controlled insertion of the remaining arm.

Generalized lesson: **when a multi-limb flexible-material interaction fails, reduce simultaneous physical constraints before adding more prompt detail.**
