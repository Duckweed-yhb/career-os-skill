import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []


def check_skill_frontmatter():
    """SKILL.md must start with valid front matter (name + description)."""
    for skill in ["SKILL.md", "SKILL.zh-CN.md"]:
        path = ROOT / skill
        if not path.exists():
            errors.append(f"[frontmatter] missing file: {skill}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"[frontmatter] {skill} must start with `---` YAML front matter")
            continue
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not m:
            errors.append(f"[frontmatter] {skill} has unclosed front matter block")
            continue
        for field in ("name:", "description:"):
            if field not in m.group(1):
                errors.append(f"[frontmatter] {skill} missing `{field}`")


def check_relative_links():
    """Every relative link in README*/FAQ must point to an existing file."""
    for md in [ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "FAQ.md"]:
        if not md.exists():
            continue
        text = md.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)#]+?)(?:#[^)]*)?\)", text):
            if target.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            if target.startswith("assets/"):
                continue  # binary assets; presence not enforced here
            if (ROOT / target).exists():
                continue
            errors.append(f"[link] {md.name}: broken relative link -> {target}")


def check_changelog():
    path = ROOT / "CHANGELOG.md"
    if not path.exists():
        errors.append("[changelog] CHANGELOG.md missing")
        return
    text = path.read_text(encoding="utf-8")
    if "## [Unreleased]" not in text:
        errors.append("[changelog] CHANGELOG.md must contain an [Unreleased] section")


def check_version_consistency():
    """SKILL front-matter version, README badge, and latest CHANGELOG version must match."""
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"^version:\s*([\d.]+)", skill_text, re.MULTILINE)
    if not m:
        errors.append("[version] SKILL.md missing `version:` in front matter")
        return
    skill_version = m.group(1)

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"badge/version-([\d.]+)-blue", readme_text)
    if not m:
        errors.append("[version] README.md missing shields.io version badge")
        return
    badge_version = m.group(1)

    changelog_text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    m = re.search(r"^## \[([\d.]+)\]", changelog_text, re.MULTILINE)
    if not m:
        errors.append("[version] CHANGELOG.md missing a released version section")
        return
    changelog_version = m.group(1)

    versions = {"SKILL": skill_version, "README badge": badge_version, "CHANGELOG": changelog_version}
    if len(set(versions.values())) != 1:
        errors.append(f"[version] version mismatch: {versions}")


def main():
    check_skill_frontmatter()
    check_relative_links()
    check_changelog()
    check_version_consistency()
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: verified {ROOT} — front matter, links, changelog, version consistency all valid.")


if __name__ == "__main__":
    main()
