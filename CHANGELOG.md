# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

No unreleased changes yet.

## [0.3.0] - 2026-09-08

### Added

- Zero-base course example ([`examples/course-zero/`](examples/course-zero/00-course-overview.md)): overview + first two lessons, showing how the course adapts to a complete beginner
- Study schedule generation: weekly time budget → week-by-week lesson plan in the course overview

### Changed

- SKILL.md / SKILL.zh-CN.md: standard six-axis capability radar dimensions (Language & Frameworks, Data & Storage, Engineering Practice, Architecture & Design, Domain Knowledge, Soft Skills)
- SKILL.md / SKILL.zh-CN.md: proficiency anchors for beginner / intermediate / advanced assessment
- SKILL.md / SKILL.zh-CN.md: growth path planning — a 3-project serial path (Foundation → Capability → Showcase) per target role
- SKILL.md / SKILL.zh-CN.md: Phase 4 course schedule step (version 0.3.0)
- CI: version consistency check (SKILL ↔ README badge ↔ CHANGELOG)

## [0.2.0] - 2026-09-08

### Added

- YAML front matter (name, description, version)
- Phase 4 Course Builder — learning-by-doing Markdown courses
- Command Reference, Debug Protocol, Domain Templates sections
- Difficulty calibration bands and milestone feedback loop
- State persistence via `career-profile.md` and course progress
- Domain template library ([`templates/`](templates/README.md))
- Course example ([`examples/course/`](examples/course/00-course-overview.md))
- FAQ ([`FAQ.md`](FAQ.md))
- CI workflow verifying front matter, links, and changelog
- Code of Conduct, issue templates, repository banner, social preview assets
- Contribution guide ([`CONTRIBUTING.md`](CONTRIBUTING.md))
- Bilingual README with banner, badges, installation guide, and new commands

## [0.1.0] - 2026-09-08

### Added

- Initial project scaffold: repository, README description, MIT LICENSE
