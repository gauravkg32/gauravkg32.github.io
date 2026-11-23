"""The flame-glow candidate for the NOZ logo (23 Nov 2026, under review, not adopted).

Hyprland's default border colours: the arrow and nozzle in green #00FF99, lit from the flame by a smooth cyan
#33CCFF glow that fades to green toward the tip, and the flame in electric blue #3D7BFF. The NOZ lettering stays
solid green. Runs _tools/make_logos.py with these changes and writes the files into this folder; assets/brand is
unchanged. Run from the repo root:
    python docs/brand-candidates/glow/make_glow.py
"""
import contextlib, io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "..", "..", "_tools", "make_logos.py"), encoding="utf-8").read()

def swap(old, new):
    global src
    assert src.count(old) == 1, f"make_logos.py changed: {old[:60]}"
    src = src.replace(old, new)

# Colours. `glow` is the flame's light on the nozzle; the one-colour logos have none.
swap('"dark":  dict(c="#4ADE80", flame="#38BDF8", core="#E0F2FE"),',
     '"dark":  dict(c="#00FF99", glow="#33CCFF", flame="#3D7BFF", core="#DCE6FF"),')
swap('"light": dict(c="#15803D", flame="#0284C7", core="#BAE6FD"),',
     '"light": dict(c="#007F4C", glow="#1E7896", flame="#3469D9", core="#C9D7FF"),')  # both 5:1 on white

# The glow: a radial gradient centred behind the nozzle, where the flame is, in the mark's own coordinates.
swap('def mark(p, angle=TILT, hooks=False):',
     'def _glow(p):\n'
     '    if "glow" not in p:\n'
     '        return p["c"], ""\n'
     '    g = (f\'<defs><radialGradient id="nzglow" gradientUnits="userSpaceOnUse" cx="{42 - G - 16:.2f}" cy="50" r="66">\'\n'
     '         f\'<stop offset="0" stop-color="{p["glow"]}"/><stop offset=".22" stop-color="{p["glow"]}"/>\'\n'
     '         f\'<stop offset=".72" stop-color="{p["c"]}"/></radialGradient></defs>\')\n'
     '    return "url(#nzglow)", g\n\n\n'
     'def mark(p, angle=TILT, hooks=False):')
swap('''    solid = lambda poly, extra="": (f'<path{extra} d="{_d(poly)}" fill="{p["c"]}" stroke="{p["c"]}" \'''',
     '''    paint, glow_defs = _glow(p)
    solid = lambda poly, extra="": (f'<path{extra} d="{_d(poly)}" fill="{paint}" stroke="{paint}" \'''')
swap('''    return f'<g transform="rotate({-angle} 50 50)">{flame}{ribs}{solid(ARROW)}</g>\'''',
     '''    return f'<g transform="rotate({-angle} 50 50)">{glow_defs}{flame}{ribs}{solid(ARROW)}</g>\'''')

sys.argv = ["make_logos.py", HERE]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, "make_logos.py (glow)", "exec"), {"__name__": "__main__"})
print("Wrote the glow logos to", HERE)
