#!/usr/bin/env python3
"""Run all code quality checks."""

import subprocess
import sys


def run(cmd: list[str], name: str) -> bool:
    """Run a command and return success status."""
    print(f"\n{'=' * 60}")
    print(f"Running: {name}")
    print(f"{'=' * 60}")
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        print(f"FAILED: {name}")
        return False
    print(f"PASSED: {name}")
    return True


def main() -> int:
    """Run all checks."""
    fix_mode = "--fix" in sys.argv

    checks = [
        (["uv", "run", "ruff", "format", "." if fix_mode else "--check", "."], "Ruff Format"),
        (
            ["uv", "run", "ruff", "check", ".", *(["--fix"] if fix_mode else [])],
            "Ruff Lint",
        ),
        (["uv", "run", "mypy", "tensors.py"], "Mypy"),
    ]

    # Fix the format check command
    if not fix_mode:
        checks[0] = (["uv", "run", "ruff", "format", "--check", "."], "Ruff Format")

    results = [run(cmd, name) for cmd, name in checks]

    print(f"\n{'=' * 60}")
    if all(results):
        print("All checks passed!")
        return 0
    else:
        failed = [name for (_, name), passed in zip(checks, results, strict=True) if not passed]
        print(f"Failed checks: {', '.join(failed)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
