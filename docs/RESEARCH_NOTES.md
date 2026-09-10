# Research Notes: Patterns from Popular Agent Skills Repositories

This file records maintainership patterns that informed the repository structure. It is not part of the runtime skill.

## Patterns worth adopting

### 1. One-command installation
Popular skill repositories make the fastest path obvious. This repository uses the open `skills` CLI in the README and keeps manual installation as a fallback.

### 2. Progressive disclosure
The open Agent Skills specification recommends a small `SKILL.md` with supporting references loaded only when needed. The canonical skill follows that model.

### 3. Cross-agent portability
The repository keeps the canonical skill client-neutral and isolates optional vendor metadata under `skills/ugc-product-review/agents/`.

### 4. Contributor paths
Healthy repositories make contributions easy to scope. This project separates category, campaign, QA, model-adapter, and performance modules so contributors can change one behavior without rewriting the system.

### 5. Validation and QA
Production-grade skill repositories increasingly test skill structure and behavior. This project currently has structural CI validation; behavior/evaluation fixtures are on the roadmap.

### 6. Security posture
Skills influence agent behavior and may include executable resources. The project documents security reporting and intentionally keeps the runtime skill Markdown-first with no required executable dependency.

### 7. Examples over exhaustive prose
Examples and reproducible failure cases are more useful than an ever-growing monolithic handbook. New examples should live under `examples/`.

### 8. Discoverability
A strong README should immediately answer: what the project does, why it is useful, how to install it, how to try it, which agents it supports, and how to contribute.

## Patterns intentionally not copied blindly

- duplicating generated skill copies for every vendor
- adding a custom CLI before the installation problem requires one
- making undocumented model-specific behavior part of the core contract
- loading all category knowledge by default
- adding badges or claims that imply benchmarks not actually run

The repository should earn stronger claims through reproducible evaluations rather than README marketing.
