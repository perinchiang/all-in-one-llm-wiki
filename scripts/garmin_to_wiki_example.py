#!/usr/bin/env python3
"""
Generic Garmin Connect to LLM Wiki starter.

Install dependency in your own environment:
  pip install garminconnect

Use environment variables instead of hardcoding credentials:
  GARMIN_EMAIL
  GARMIN_PASSWORD

This script intentionally exports only a compact private JSON summary and a
Markdown entity page. Adapt fields to the user's consent and region.
"""

from __future__ import annotations

import json
import os
from datetime import date, timedelta
from pathlib import Path


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"Missing environment variable: {name}")
    return value


def main() -> None:
    try:
        from garminconnect import Garmin
    except ImportError as exc:
        raise SystemExit("Install dependency first: pip install garminconnect") from exc

    email = require_env("GARMIN_EMAIL")
    password = require_env("GARMIN_PASSWORD")

    wiki_dir = Path(os.environ.get("LLM_WIKI_DIR", "wiki"))
    raw_dir = wiki_dir / "raw" / "health" / "garmin"
    entity_dir = wiki_dir / "entities"
    raw_dir.mkdir(parents=True, exist_ok=True)
    entity_dir.mkdir(parents=True, exist_ok=True)

    client = Garmin(email, password)
    client.login()

    today = date.today()
    start = today - timedelta(days=14)

    summaries = []
    activities = []
    for offset in range(15):
        day = start + timedelta(days=offset)
        day_str = day.isoformat()
        try:
            summaries.append({"date": day_str, "summary": client.get_stats(day_str)})
        except Exception as error:
            summaries.append({"date": day_str, "error": str(error)})

    try:
        activities = client.get_activities(0, 10)
    except Exception as error:
        activities = [{"error": str(error)}]

    summary = {
        "source": "Garmin Connect",
        "generated": today.isoformat(),
        "date_range": {"start": start.isoformat(), "end": today.isoformat()},
        "daily_summaries": summaries,
        "recent_activities": activities,
        "privacy": "Private raw summary. Do not publish exact routes or account identifiers.",
    }

    json_path = raw_dir / f"garmin-summary-{today.isoformat()}.json"
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    md = f"""---
title: Garmin Health Summary
created: {today.isoformat()}
updated: {today.isoformat()}
type: entity
tags: [health, garmin, fitness, sleep]
sources: [{json_path.as_posix()}]
confidence: high
---

# Garmin Health Summary

> Recent Garmin Connect summary for agent context. Keep raw health data private.

## Overview

| Dimension | Value |
| --- | --- |
| Date range | {start.isoformat()} to {today.isoformat()} |
| Daily summaries | {len(summaries)} |
| Recent activities | {len(activities)} |

## Agent affordances

- Suggest recovery, light activity, or training based on recent sleep and activity.
- Notice anomalies and ask for confirmation before drawing conclusions.
- Avoid publishing exact routes, locations, or raw heart-rate streams.
"""

    page_path = entity_dir / "garmin-health-summary.md"
    page_path.write_text(md, encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {page_path}")


if __name__ == "__main__":
    main()
