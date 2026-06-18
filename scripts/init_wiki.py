#!/usr/bin/env python3
"""
Initialize a private LLM Wiki skeleton.

Examples:
  python scripts/init_wiki.py
  python scripts/init_wiki.py --demo
  python scripts/init_wiki.py --wiki-dir my-private-wiki --demo --force
"""

from __future__ import annotations

import argparse
import shutil
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


SCHEMA = """# LLM Wiki Schema

This private wiki is optimized for AI agents. Read `index.md` first, then open
only the pages needed for the current task.

## Core Directories

- `raw/`: private source exports and processed summaries.
- `entities/`: durable people, tools, platforms, projects, services, and profiles.
- `concepts/`: reusable ideas, workflows, learning topics, and methods.
- `queries/`: saved agent questions and reusable prompts.
- `_archive/`: old pages kept for reference.

## Page Requirements

Each useful page should include frontmatter with `title`, `created`, `updated`,
`type`, `tags`, `sources`, and `confidence`.

Prefer direct facts over guesses. Mark inferences clearly and add open questions
when the agent should ask the user for confirmation.
"""


def write_if_missing(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.write_text(content, encoding="utf-8")


def copy_demo(wiki_dir: Path, force: bool) -> None:
    demo_dir = ROOT / "examples" / "demo-wiki"
    if not demo_dir.exists():
        raise SystemExit(f"Demo wiki not found: {demo_dir}")

    for source in demo_dir.rglob("*"):
        if source.is_dir():
            continue
        target = wiki_dir / source.relative_to(demo_dir)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not force:
            continue
        shutil.copy2(source, target)


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize an AI-readable LLM Wiki.")
    parser.add_argument("--wiki-dir", default=".wiki", help="Target wiki directory.")
    parser.add_argument("--demo", action="store_true", help="Copy synthetic demo pages.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    today = date.today().isoformat()
    wiki_dir = Path(args.wiki_dir)
    for relative in [
        "raw/ai-memory",
        "raw/health",
        "raw/notes",
        "raw/platform-exports",
        "entities",
        "concepts",
        "queries",
        "_archive",
    ]:
        (wiki_dir / relative).mkdir(parents=True, exist_ok=True)

    if args.demo:
        copy_demo(wiki_dir, args.force)

    write_if_missing(wiki_dir / "SCHEMA.md", SCHEMA, args.force)
    write_if_missing(
        wiki_dir / "index.md",
        f"""# Wiki Index

> Query this page first. It lists high-value pages and one-line summaries.

## High-Value Pages

- Add imported entity and concept pages here.

## Sources

- No real sources imported yet.
""",
        args.force,
    )
    write_if_missing(
        wiki_dir / "log.md",
        f"""# Wiki Log

## [{today}] init | LLM Wiki skeleton
- Source: local initializer
- Created:
  - SCHEMA.md - local schema
  - index.md - starting index
  - log.md - append-only import log
- Privacy: no raw private data imported yet
- Notes: use `--demo` for synthetic example pages.
""",
        args.force,
    )

    print(f"Initialized {wiki_dir}")
    if args.demo:
        print("Copied synthetic demo pages.")


if __name__ == "__main__":
    main()
