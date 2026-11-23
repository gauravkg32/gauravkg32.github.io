"""The bluer mint candidate for the NOZ logo (23 Nov 2026, under review, not adopted).

Runs _tools/make_logos.py with the kit's green and blue swapped for a bluer mint (#08EAC4, mint #3EEBA0 turned 16 degrees toward blue in OKLCH, same lightness) and electric blue, and writes the
logo files into this folder. The live kit in assets/brand is unchanged. Run from the repo root:
    python docs/brand-candidates/bluer/make_bluer.py
"""
import contextlib, io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SWAP = {
    "#4ADE80": "#08EAC4",  # terminal green -> bluer mint, on dark
    "#38BDF8": "#3D7BFF",  # blue flame -> electric blue, on dark
    "#E0F2FE": "#DCE6FF",  # flame core, on dark
    "#15803D": "#077E69",  # deep green -> deep bluer mint, on white (5.0:1)
    "#0284C7": "#3469D9",  # deep blue -> deep electric blue, on white
    "#BAE6FD": "#C9D7FF",  # flame core, on white
    "#BBF7D0": "#C2F8EE",  # pale green in the "don't" example
}

src = open(os.path.join(HERE, "..", "..", "..", "_tools", "make_logos.py"), encoding="utf-8").read()
for old, new in SWAP.items():
    assert old in src, f"{old} is no longer in make_logos.py"
    src = src.replace(old, new)

sys.argv = ["make_logos.py", HERE]
with contextlib.redirect_stdout(io.StringIO()):  # the script prints a manifest for the kit page; not needed here
    exec(compile(src, "make_logos.py (bluer)", "exec"), {"__name__": "__main__"})
print("Wrote the bluer logos to", HERE)
