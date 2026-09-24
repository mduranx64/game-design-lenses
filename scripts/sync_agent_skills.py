#!/usr/bin/env python3
"""Keep the portable .agents bundle identical to the canonical plugin skills."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "plugins" / "game-design-lenses"
PORTABLE = ROOT / ".agents"
PAIRS = (
    (SOURCE / "skills", PORTABLE / "skills"),
    (SOURCE / "references", PORTABLE / "references"),
)


def files_under(path: Path) -> dict[Path, bytes]:
    return {
        child.relative_to(path): child.read_bytes()
        for child in path.rglob("*")
        if child.is_file()
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="copy source files into .agents")
    args = parser.parse_args()

    for source, target in PAIRS:
        if args.write:
            target.mkdir(parents=True, exist_ok=True)
            for rel, contents in files_under(source).items():
                output = target / rel
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(contents)

        original = files_under(source)
        portable = files_under(target) if target.exists() else {}
        if original != portable:
            missing = sorted(original.keys() - portable.keys())
            extra = sorted(portable.keys() - original.keys())
            changed = sorted(rel for rel in original.keys() & portable.keys() if original[rel] != portable[rel])
            print(f"Out of sync: {target.relative_to(ROOT)}", file=sys.stderr)
            for label, paths in (("missing", missing), ("extra", extra), ("changed", changed)):
                for rel in paths:
                    print(f"  {label}: {rel}", file=sys.stderr)
            return 1

    print("Portable skills and references match the plugin source")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
