#!/usr/bin/env python3
"""Create a skeleton experiment directory for sampler research."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import re


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "experiment"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root. Default: current directory.")
    parser.add_argument("--slug", required=True, help="Short experiment slug.")
    parser.add_argument("--objective", required=True, help="Experiment objective.")
    parser.add_argument("--target", default="unspecified", help="Declared target distribution.")
    parser.add_argument("--dry-run", action="store_true", help="Print the path without creating files.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    now = datetime.now(timezone.utc)
    dirname = f"{now:%Y%m%d-%H%M%S}-{slugify(args.slug)}"
    exp_dir = root / "experiments" / dirname

    if args.dry_run:
        print(exp_dir)
        return 0

    exp_dir.mkdir(parents=True, exist_ok=False)
    plan = exp_dir / "plan.md"
    plan.write_text(
        "\n".join(
            [
                f"# {args.slug}",
                "",
                f"- Created UTC: {now.isoformat()}",
                f"- Objective: {args.objective}",
                f"- Target distribution: {args.target}",
                "- Parameters: TBD",
                "- Commands: TBD",
                "- Raw data: TBD",
                "- Interpretation: TBD",
                "- Next changes: TBD",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (exp_dir / "results.jsonl").write_text("", encoding="utf-8")
    print(exp_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
