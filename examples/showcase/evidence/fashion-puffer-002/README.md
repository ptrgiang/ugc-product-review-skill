# FASHION-PUFFER-002 — evidence manifest

Status: **repair testing; V04 failed, V05 pending**

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
│   └── v05.md
└── qa/
    ├── v01.md
    ├── v02.md
    ├── v03.md
    └── v04.md
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
true start-frame / image-to-video test
→ pending
```

## Prompts

- [V01 original prompt](prompts/v01.md)
- [V02 safe partial-state repair](prompts/v02.md)
- [V03 dedicated sleeve-insertion repair](prompts/v03.md)
- [V04 reference-conditioned test](prompts/v04.md)
- [V05 true start-frame test](prompts/v05.md)

## QA

- [V01 QA](qa/v01.md)
- [V02 QA](qa/v02.md)
- [V03 QA](qa/v03.md)
- [V04 QA](qa/v04.md)

## Canonical case

The narrative case file remains:

`examples/showcase/fashion-puffer-fit-proof.md`

## Current hypothesis

The failure has progressed from interaction overload to a more specific intermediate-state representation problem. V05 tests whether a literal first-frame image-to-video start state can force the model to preserve the asymmetric one-arm-in / one-sleeve-empty configuration before animating the left-arm insertion.
