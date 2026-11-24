#!/usr/bin/env python3
"""Till Firmware Do Us Part: a robot's wedding vow, one line."""

import os

VOW = "I promise to love you through every update, every crash, and every low-battery warning, and to reboot beside you each morning until my circuits finally give out."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(VOW)

if __name__ == "__main__":
    main()
