#!/usr/bin/env python3
import os
from pathlib import Path

if __name__ == "__main__":
    _ = Path(__file__).with_name("data.txt").write_text(
        f"{(100, 200, 300, 200)[int(os.environ['GITHUB_RUN_NUMBER']) % 4]}\n",
    )
