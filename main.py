"""The Funniest Toaster Error Message — make.fun entry.

Writes one line to /output/entry.txt: the error message a kitchen
toaster shows its owner when something goes wrong.
"""

import os

MESSAGE = "ERROR: You asked for lightly toasted. I gave it a funeral."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
