# Domain Templates

This directory holds optional domain templates that make CareerOS projects and courses more concrete.

## How it works

- One Markdown file per domain (e.g. `web-fullstack.md`, `ai-data.md`, `devops.md`).
- When generating a project or course, CareerOS matches the user's domain to a template and uses its structure — typical milestones, tech-stack skeletons, lesson patterns — as the starting skeleton.
- If no template matches, CareerOS falls back to the generic rules in the SKILL.

## Template format

Each template should contain:

1. **Domain name & typical roles** — who this applies to (e.g. Full-Stack Engineer, Data Engineer)
2. **Canonical tech stack** — the default stack with common alternatives
3. **Project archetypes** — 3–5 realistic project shapes in this domain (with difficulty hints)
4. **Typical milestones** — the M1/M2/M3 skeleton that fits most projects in this domain
5. **Lesson patterns** — how courses are usually sliced in this domain (e.g. "env → API → data → ops")

## How to add a template

1. Create `<domain>.md` following the format above.
2. Keep it concise: a template is a skeleton, not a full course.
3. Update the SKILL's Domain Templates section if the naming convention changes.

## Language rule

One language per file (same convention as the rest of the repo). Name the file with `-zh` suffix for Chinese versions (e.g. `web-fullstack.zh-CN.md`).
