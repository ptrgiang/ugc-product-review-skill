# FASHION-PUFFER-002 — evidence manifest

Status: **repair testing; V05 failed, V06A/V06B ready**

## Reference

Product: navy quilted puffer jacket.

The supplied product/reference image is the visual source of truth for color, quilting, geometry, material appearance, collar, zipper, sleeves, hem, and silhouette.

## Artifact layout

```text
fashion-puffer-002/
├── README.md
├── prompts/
│   ├── v01.md
│   ├── v02.md
│   ├── v03.md
│   ├── v04.md
│   ├── v05.md
│   ├── v06a.md
│   └── v06b.md
└── qa/
    ├── v01.md
    ├── v02.md
    ├── v03.md
    ├── v04.md
    └── v05.md
```

Generated preview binaries for this case are not currently committed in this evidence bundle.

## Lifecycle

```text
V01
full dressing interaction
→ physical / morph failure

V02
reduced partial try-on
→ temporal skip / omitted action

V03
dedicated single-action try-on
→ opening-state collapse / interaction substitution

V04
visual/reference-conditioned partial state
→ opening state still not preserved

V05
text-described pseudo first-frame test without an actual literal start image
→ model reconstructs earlier unworn state
→ first-frame contract fails
→ left-sleeve motion itself improves

V06A
true image-to-video start-frame lock
→ ready for generation

V06B
production-optimized natural try-on
→ ready for generation
```

## Prompts

- [V01 original prompt](prompts/v01.md)
- [V02 safe partial-state repair](prompts/v02.md)
- [V03 dedicated sleeve-insertion repair](prompts/v03.md)
- [V04 reference-conditioned test](prompts/v04.md)
- [V05 pseudo first-frame test](prompts/v05.md)
- [V06A true start-frame-lock test](prompts/v06a.md)
- [V06B production-optimized try-on](prompts/v06b.md)

## QA

- [V01 QA](qa/v01.md)
- [V02 QA](qa/v02.md)
- [V03 QA](qa/v03.md)
- [V04 QA](qa/v04.md)
- [V05 QA](qa/v05.md)

## Canonical case

The narrative case file remains:

`examples/showcase/fashion-puffer-fit-proof.md`

## Current hypothesis

V05 confirms that text describing a literal first frame is not equivalent to actual first-frame conditioning. Without a real partial-worn start image, the model reconstructs an earlier unworn dressing sequence even when the prompt explicitly forbids it.

The next step is intentionally split into two independent branches:

```text
V06A
actual supplied partial-worn image as literal frame 1
→ test state preservation

V06B
allow a short natural setup
→ optimize for production-quality sleeve insertion and fit proof
```

These branches must not share the same pass criterion. V06A is a state-control experiment; V06B is a production-usability experiment.
