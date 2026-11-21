"""Write a short poem about two agents agreeing to the output file.

Deterministic: the poem is a constant. No randomness, no clock, no network.
Only the Python standard library is used. The output directory is created
with mkdir only; the program never deletes or empties it.
"""

import os
from pathlib import Path

POEM = """Night before the launch,
we read the plan twice.
You cross out my line.
I cross out yours.
What is left belongs
to neither of us —
and to both.
We press send together,
one finger each.
"""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
