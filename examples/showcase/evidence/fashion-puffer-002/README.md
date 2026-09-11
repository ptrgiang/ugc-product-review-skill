# FASHION-PUFFER-002 evidence

## Reference input

A navy quilted puffer jacket reference image was supplied for the prompt-design step of this case.

- Type: product/reference image
- Product: navy quilted puffer jacket
- Role: visible source of truth for garment color, quilting, geometry, material appearance, collar, zipper, sleeves, hem, and overall silhouette
- Repository media status: the binary reference image is not committed in this prompt-only update
- Post-processing: none recorded

## V01 generation status

Two native 8-second Google Flow / Veo preview clips were generated and reviewed outside the repository media bundle.

### Clip 1

Status: **repair required — P1 Major**

Observed failure: the jacket-donning sequence breaks during the transition from holding the garment to wearing it. The garment appears to partially morph/snap onto the creator, with ambiguous arm-to-sleeve contact and physically weak cloth/body continuity.

Tags:

```text
HIGH_INTERACTION_RISK
FABRIC_PHYSICS
BODY_MECHANICS_ERROR
STATE_DISCONTINUITY
CONTACT_ERROR
PRODUCT_MORPH
```

Root cause: the shot requires the model to solve both arms, both sleeves, shoulder rotation, flexible quilted fabric, occlusion, and product geometry at the same time.

### Clip 2

Status: **preserve by default**

The already-worn fit sequence is substantially more stable than Clip 1 and should not be regenerated merely because the dressing interaction failed. Reuse it unless a separate QA issue is identified.

## Repair

V02 uses a targeted repair rather than a full rewrite:

```text
held
→ hard cut
→ one arm already fully inserted
→ second arm slides through remaining sleeve
→ both arms inserted
→ garment settles
→ preserved fit-proof continuation
```

See:

`examples/showcase/fashion-puffer-fit-proof-v02.md`

## Evidence status

The QA finding and V02 prompt are now documented in the repository. The actual V01 preview binaries are not committed in this update.

The case should be considered **in repair testing**, not yet validated. V02 must be generated and inspected before the interaction-risk strategy is considered successful for this case.
