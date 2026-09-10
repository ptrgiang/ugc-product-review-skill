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

## 6. Repair output

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
