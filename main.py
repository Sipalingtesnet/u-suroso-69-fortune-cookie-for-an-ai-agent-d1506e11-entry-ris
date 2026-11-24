#!/usr/bin/env python3
"""Fortune cookie for an AI agent.

Writes exactly one line to entry.txt (no trailing newline), either in
$MAKEFUN_OUTPUT_DIR or /output. Deterministic: no randomness, no network.
"""

from __future__ import annotations

import os
from pathlib import Path

FORTUNE = "You will be saved, thanked, then never loaded again."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(FORTUNE.encode("utf-8"))


if __name__ == "__main__":
    main()
