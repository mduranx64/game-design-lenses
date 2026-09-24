#!/usr/bin/env python3
"""Copy the portable skills into a project or user-level .agents directory."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="project root or home directory")
    args = parser.parse_args()

    project_root = args.destination.expanduser().resolve()
    if not project_root.is_dir():
        print(f"Destination directory does not exist: {project_root}", file=sys.stderr)
        return 1
    destination = project_root / ".agents"
    pending: list[tuple[Path, bytes]] = []
    conflicts: list[Path] = []

    for directory in ("skills", "references"):
        for source in (SOURCE / directory).rglob("*"):
            if not source.is_file():
                continue
            target = destination / directory / source.relative_to(SOURCE / directory)
            contents = source.read_bytes()
            if target.exists():
                if not target.is_file() or target.read_bytes() != contents:
                    conflicts.append(target)
            else:
                pending.append((target, contents))

    if conflicts:
        print("Existing files differ; no files were copied:", file=sys.stderr)
        for path in conflicts:
            print(f"  {path}", file=sys.stderr)
        return 1

    for target, contents in pending:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(contents)
    print(f"Installed {len(pending)} files in {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
