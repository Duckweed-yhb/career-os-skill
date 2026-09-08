# CareerOS

![CareerOS banner](assets/careeros-banner.jpg)

> An operating system for your career growth.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.3.0-blue.svg)](CHANGELOG.md)
[![Last Commit](https://img.shields.io/github/last-commit/Duckweed-yhb/career-os-skill)](https://github.com/Duckweed-yhb/career-os-skill)

**[English](README.md) | [简体中文](README.zh-CN.md)**

---

## Overview

**CareerOS** is not just a learning guide — it's a dynamic career growth engine. It helps you identify your target role, map out the required skill stack, assess where you currently stand, and bridge the gap through **real-world project recommendations**.

It doesn't just tell you what to learn. It gives you something to build. Tailored to your domain, experience level, and learning pace, you walk away with not just new skills, but a **portfolio** you can actually show.

## Installation

1. **Clone the repository** (or download and extract it):

   ```bash
   git clone https://github.com/Duckweed-yhb/career-os-skill.git
   ```

2. **Locate your AI assistant's skills directory:**

   | Assistant | Skills directory |
   |---|---|
   | Claude Code | `~/.claude/skills/` |
   | Doubao Agent | `<workspace>/.skills/` |
   | Other assistants | See your assistant's documentation for the skills directory |

3. **Copy the Skill into a `career-os/` folder** inside that directory:

   ```bash
   # example (Claude Code)
   mkdir -p ~/.claude/skills/career-os
   cp SKILL.md ~/.claude/skills/career-os/
   ```

   Use `SKILL.zh-CN.md` instead if you prefer the Chinese version.

4. **Restart your assistant session** and verify:

   ```text
   /CareerOS init
   ```

   If you see the init welcome message, you are all set.

## Core Modules

Just like an operating system manages hardware resources, CareerOS manages your career resources:

### 1. Target Identification
- Parse your interests and background to lock in a high-potential target role.
- Generate a capability radar for that role.

### 2. Skill Gap Analysis
- Compare your current resume/skills against the target role requirements.
- Identify the critical missing links.

### 3. Project Generator
- **No toy projects.** Generate real-world project ideas with industrial-level complexity.
- Includes tech stack recommendations, difficulty predictions, and acceptance criteria.

### 4. Course Builder
- Turn any chosen project into a step-by-step **learning-by-doing** course.
- Generates the tech-stack learning route and the project development route, then splits the project into Markdown lessons — each with hands-on tasks and acceptance criteria.

### 5. Portfolio Builder
- Turn your projects into interview highlights.
- Resume bullet optimization and GitHub README writing guidance included.

## How to Use

Load the `CareerOS` Skill in your AI assistant, then try:

```text
/CareerOS init
/CareerOS analyze [your resume or current skill list]
/CareerOS generate project --focus=[specific tech, e.g. Redis/microservices]
/CareerOS generate course [project]  # turn a chosen project into learning-by-doing lessons
```

For a complete walkthrough, see [examples/frontend-to-fullstack.md](examples/frontend-to-fullstack.md). Have questions? See the [FAQ](FAQ.md).

## Why CareerOS?

- **Action-Oriented** — Switch from input mode to output mode.
- **Context-Aware** — Understands your level; never recommends something too easy or too hard.
- **Result-Driven** — Everything leads to one thing: a project you can put on your resume.

## License

[MIT License](LICENSE)

---

Made with ❤️ by Duckweed-yhb
