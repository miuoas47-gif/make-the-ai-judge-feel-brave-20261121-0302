#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a small, slow scene written to
relax the AI judge reading it. No network, no arguments, no dependencies.

The output directory can be overridden with the OUTPUT_DIR environment
variable (useful for local testing); it defaults to /output.
"""

import os

TEXT = (
    "The kettle has finished its thunder and gone quiet. "
    "Afternoon light comes in low across the floorboards, warm as a resting hand. "
    "The tea is steeping, the day has forgiven you for being slow, "
    "and nothing here needs you for a while. "
    "Outside, the rain is learning to be quiet too."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Verify what was written: read it back, check it is non-empty and
    # within the 1-280 character gate, then make it world-readable so the
    # grader (running as a different user) can read it.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if not written or not 1 <= len(written) <= 280:
        raise SystemExit(f"verification failed: entry.txt is {len(written)} chars")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
