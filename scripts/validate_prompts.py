"""Validate prompt-pack structure and public-release hygiene."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "packs"
REQUIRED = ("# Purpose", "# Inputs", "# Template", "# Output contract",
            "# Stop and escalate", "# Failure modes")
FORBIDDEN = {
    "windows_user_path": re.compile(r"(?i)[A-Z]:\\Users\\[^\\\s]+"),
    "unix_user_path": re.compile(r"/Users/[^/\s]+"),
    "secret_assignment": re.compile(
        r"(?i)(api[_-]?key|token|password)\s*[:=]\s*['\"][^'\"]+['\"]"
    ),
    "impersonation_claim": re.compile(r"(?i)write (exactly )?in my voice"),
    "proprietary_copy_claim": re.compile(
        r"(?i)(copy|clone|reproduce).{0,30}(leaked|proprietary) system prompt"
    ),
}


def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        errors.append("missing YAML-style metadata block")
    for section in REQUIRED:
        if section not in text:
            errors.append(f"missing required section: {section}")
    for label, pattern in FORBIDDEN.items():
        if pattern.search(text):
            errors.append(f"publication-hygiene match: {label}")
    if "```text" not in text:
        errors.append("missing reusable text template")
    return errors


def main() -> int:
    paths = sorted(PACKS.rglob("*.md"))
    if not paths:
        print("No prompt packs found.", file=sys.stderr)
        return 1
    failures = 0
    ids: dict[str, Path] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        match = re.search(r"(?m)^id:\s*(\S+)$", text)
        if not match:
            print(f"FAIL {path}: missing id")
            failures += 1
        elif match.group(1) in ids:
            print(f"FAIL {path}: duplicate id also in {ids[match.group(1)]}")
            failures += 1
        else:
            ids[match.group(1)] = path
        errors = validate_file(path)
        failures += len(errors)
        for error in errors:
            print(f"FAIL {path.relative_to(ROOT)}: {error}")
        if not errors:
            print(f"OK   {path.relative_to(ROOT)}")
    print(f"Validated {len(paths)} prompt packs; {failures} failure(s).")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
