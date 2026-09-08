# FAQ

## What is CareerOS?

CareerOS is a Skill for AI assistants that turns career growth into action. It identifies your target role, analyzes skill gaps, recommends industrial-complexity projects, and — uniquely — turns any project into a step-by-step **learning-by-doing** course made of Markdown lessons.

## How do I install it?

See the **Installation** section of the README. In short: copy `SKILL.md` (or `SKILL.zh-CN.md`) into your assistant's skills directory under a `career-os/` folder, restart the session, then run `/CareerOS init`.

## Which assistants does it support?

Any assistant that loads Skills from a directory of `SKILL.md` files (e.g. Claude Code, Doubao Agent, and similar agent frameworks). The path differs per assistant — check your assistant's documentation for its skills directory.

## English or Chinese?

Both. `SKILL.md` is English, `SKILL.zh-CN.md` is Simplified Chinese. Install whichever you prefer; the commands are identical.

## What's the difference between "generate project" and "generate course"?

- `/CareerOS generate project` proposes 2–3 project ideas targeting your skill gaps.
- `/CareerOS generate course` takes a chosen project and breaks it into a `course/` folder of Markdown lessons — each lesson has learning goals, minimal knowledge, a hands-on task (a real piece of the project), and acceptance criteria.

## I'm a complete beginner. Will this work for me?

Yes — that's a core use case. When building a course, CareerOS asks for your base level first. Zero-base users get smaller, more scaffolded lessons that start from environment setup.

## I'm stuck on a lesson. What do I do?

Tell CareerOS the exact error message and the step where you got stuck. It will give you a minimal hint first — not the full solution — and only escalate to a concrete fix if you're still blocked. The struggle is where the learning happens.

## Does CareerOS remember my progress between sessions?

Yes. CareerOS persists a `career-profile.md` (target role, skill matrix, projects, difficulty preferences) and tracks course progress through the acceptance-criteria checkboxes in each lesson file.

## How do I uninstall?

Remove the `career-os/` folder from your skills directory. Your `career-profile.md` and any `course/` folders are plain Markdown files — keep them, they're your own work.

## How do I report a bug or request a feature?

Open a GitHub issue using the provided templates (Bug report / Feature request).

## Can I contribute?

Yes — see `CONTRIBUTING.md`. Templates for new domains, example courses, and translations are especially welcome.

## I have another question.

Open an issue, or ask your assistant while running CareerOS — it will route you appropriately.
