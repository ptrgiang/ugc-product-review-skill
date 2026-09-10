# Security Policy

## Supported versions

The `main` branch and the latest tagged release are supported.

## Reporting a vulnerability

Please do **not** publish sensitive security findings in a public issue.

Use GitHub's private vulnerability reporting for this repository when available. If private reporting is not available, contact the maintainer privately through the contact method listed on the maintainer's GitHub profile.

Include:

- affected file or workflow
- impact
- minimal reproduction
- suggested mitigation, if known

## Scope

Security reports may include:

- unsafe executable scripts
- prompt instructions that cause unintended tool use
- path traversal or arbitrary file access in helper scripts
- dependency or workflow supply-chain issues
- misleading installation instructions that could execute untrusted code

General prompt-quality bugs should use the normal bug-report template instead.

## Dependency policy

The canonical skill is Markdown-first and intentionally has no runtime dependency. Helper validation scripts should prefer the Python standard library unless an external dependency provides clear value.
