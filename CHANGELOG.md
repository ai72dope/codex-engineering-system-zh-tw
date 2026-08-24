# Changelog

## v1.3.3 — Decision Boundary Hardening

- Added an explicit business-rule boundary: Codex must not invent consequential product policy such as loyalty tiers, percentages, eligibility, or stacking rules.
- Added a high-risk context gate for authentication, authorization, destructive operations, and security-boundary work.
- Missing actor identity, auth context, roles/permissions, protected API, or denial semantics now require clarification instead of implicit architecture invention.
- Clarified that plausible defaults are still invented requirements.
- Preserved existing adaptive routing, TDD, verification, and Simple-task behavior.

## [1.3.2] - 2026-08-23
### Fixed
- Routing Trace is mandatory immediately after classifying any non-Simple task.
- Clarification-only responses must show the Route block first.
- Missing-context and “already fixed” responses must show the Route block first.
- Spec/TDD routing fields may use `Pending` when not yet decided.
- TDD Trace requirements now explicitly require real execution evidence.

## [1.3.1] - 2026-08-23
### Added
- Compact Routing Trace for Standard, Complex, and High-Risk tasks.
- One-line route trace for Simple tasks.
- TDD Trace with actual RED / GREEN / REFACTOR / Full Suite evidence.
- `docs/OBSERVABILITY.md` explaining route and validation visibility.

### Changed
- Completion reports now include the selected route.
- TDD may no longer be claimed without observable execution evidence.
- Feature and Bug workflows now reference routing/TDD traces.

## [1.3.0] - 2026-08-23
### Added
- Simple / Standard / Complex task routing.
- Independent high-risk routing for security- and data-sensitive work.
- Spec-driven development workflow with acceptance criteria and out-of-scope boundaries.
- Optional TDD workflow using Red → Green → Refactor.
- Explicit verification contract: Passed / Failed / Not run / Manual-Static check.

### Changed
- Feature workflow now adapts to task complexity and risk.
- Bug workflow emphasizes reproduction, root cause, regression testing, and minimal fixes.
- `AGENTS.md` now acts as a lightweight adaptive router rather than forcing one workflow depth.
- Workflow guidance now uses progressive disclosure: load only the files relevant to the task.

## [1.2.0] - 2026-08-22
### Changed
- Renamed the hidden workflow directory to `codex-system/` to avoid hidden-folder upload and visibility issues.
- Updated routing paths, installation docs, and demo structure.
- Installation is now `AGENTS.md` + `codex-system/`.

## [1.2.0] - 2026-08-22
### Changed
- Introduced the install-once structure.
- Users install only `AGENTS.md` and `codex-system/` into the repository root.
- Added workflow routing in `AGENTS.md`.
- Workflows, prompts, docs, and templates live under `codex-system/`.
- Manual prompt copy-pasting is no longer the default usage model.

## [1.0.0] - 2026-08-22
- Initial release.
