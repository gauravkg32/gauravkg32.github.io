"""Generate NOZ Studio logo SVGs into <out> (python _tools/make_logos.py assets/brand) and print a JSON manifest.
`python _tools/make_logos.py --inline` instead prints the lockup with animation hooks, for the copy inlined in index.html.

The mark (chosen 1 Nov 2026): a green boost arrow, a jet nozzle of three ribs coming out of its back,
and the blue flame from the first logo coming out of the nozzle, all tilted up 25 degrees.
Drawn pointing right along y=50 in a 0-100 box, then rotated. Every gap between parts is G wide.
"""
import json, math, os, sys

OUT = sys.argv[1]

# JetBrains Mono ExtraBold Italic "NOZ" (118px, centred on x=364, baseline 184), converted to outlines
NOZ = "M272.26 184L256.69 184L270.38 97.86L290.79 97.86L302.71 164.53Q303.06 160.16 303.53 154.44Q304.01 148.72 304.60 143.00Q305.19 137.27 305.78 133.26L305.78 133.26L311.44 97.86L327.02 97.86L313.33 184L292.91 184L281.11 117.33Q280.88 121.11 280.46 126.30Q280.05 131.49 279.52 136.80Q278.99 142.11 278.28 146.24L278.28 146.24L272.26 184ZM357.57 185.18L357.57 185.18Q348.96 185.18 343.12 181.940Q337.28 178.69 334.74 172.85Q332.20 167.01 333.38 159.22L333.38 159.22L339.16 122.64Q340.46 114.85 344.83 109.01Q349.19 103.17 356.10 99.92Q363 96.68 371.61 96.68L371.61 96.68Q380.35 96.68 386.19 99.92Q392.03 103.17 394.57 109.01Q397.10 114.85 395.80 122.64L395.80 122.64L390.02 159.22Q388.84 167.01 384.42 172.85Q379.99 178.69 373.15 181.94Q366.30 185.18 357.57 185.18ZM360.05 169.84L360.05 169.84Q365.36 169.84 368.43 167.07Q371.50 164.29 372.32 159.22L372.32 159.22L378.10 122.64Q379.05 117.45 376.87 114.73Q374.68 112.02 369.25 112.02L369.25 112.02Q363.83 112.02 360.82 114.73Q357.81 117.45 356.86 122.64L356.86 122.64L351.08 159.22Q350.26 164.29 352.50 167.07Q354.74 169.84 360.05 169.84ZM457.16 184L404.18 184L406.77 167.48L446.18 114.38L415.98 114.38L418.69 97.86L469.55 97.86L466.83 114.38L427.30 167.48L459.75 167.48L457.16 184Z"
# JetBrains Mono Bold "STUDIO" (100px, letter-spacing 40, centred on x=0, baseline 0)
STUDIO = "M-269.80 1L-269.80 1Q-277.30 1-282.80-1.50Q-288.30-4-291.25-8.65Q-294.20-13.30-294.30-19.60L-294.30-19.60L-281.80-19.60Q-281.80-15.10-278.55-12.55Q-275.30-10-269.70-10L-269.70-10Q-264.30-10-261.25-12.50Q-258.20-15-258.20-19.40L-258.20-19.40Q-258.20-23.10-260.35-25.85Q-262.50-28.60-266.50-29.60L-266.50-29.60L-274.90-31.90Q-283.50-34.10-288.15-39.80Q-292.80-45.50-292.80-53.60L-292.80-53.60Q-292.80-59.80-290-64.40Q-287.20-69-282.05-71.50Q-276.90-74-269.90-74L-269.90-74Q-259.30-74-253.10-68.55Q-246.90-63.10-246.80-53.90L-246.80-53.90L-259.30-53.90Q-259.30-58.20-262.10-60.65Q-264.90-63.10-270-63.10L-270-63.10Q-274.90-63.10-277.60-60.80Q-280.30-58.50-280.30-54.30L-280.30-54.30Q-280.30-50.50-278.25-47.85Q-276.20-45.20-272.30-44.10L-272.30-44.10L-263.60-41.70Q-254.90-39.50-250.30-33.85Q-245.70-28.20-245.70-19.90L-245.70-19.90Q-245.70-13.70-248.70-8.95Q-251.70-4.20-257.10-1.60Q-262.50 1-269.80 1ZM-163.70 0L-176.30 0L-176.30-61.40L-195.40-61.40L-195.40-73L-144.60-73L-144.60-61.40L-163.70-61.40L-163.70 0ZM-70 1L-70 1Q-80.70 1-86.75-4.85Q-92.80-10.70-92.80-20.80L-92.80-20.80L-92.80-73L-80.20-73L-80.20-20.90Q-80.20-15.70-77.60-12.80Q-75-9.90-70-9.90L-70-9.90Q-65.10-9.90-62.45-12.80Q-59.80-15.70-59.80-20.90L-59.80-20.90L-59.80-73L-47.20-73L-47.20-20.80Q-47.20-10.70-53.20-4.85Q-59.20 1-70 1ZM29.20 0L7.50 0L7.50-73L29.20-73Q36.60-73 42.050-70.20Q47.50-67.40 50.50-62.30Q53.50-57.20 53.50-50.20L53.50-50.20L53.50-22.90Q53.50-16 50.50-10.85Q47.50-5.70 42.05-2.85Q36.60 0 29.20 0L29.20 0ZM20-61.50L20-11.50L29.20-11.50Q34.60-11.50 37.80-14.55Q41-17.60 41-22.90L41-22.90L41-50.20Q41-55.40 37.80-58.45Q34.60-61.50 29.20-61.50L29.20-61.50L20-61.50ZM151 0L109 0L109-11L123.70-11L123.70-62L109-62L109-73L151-73L151-62L136.30-62L136.30-11L151-11L151 0ZM230 1L230 1Q223 1 217.85-1.65Q212.70-4.30 209.95-9.15Q207.20-14 207.20-20.60L207.20-20.60L207.20-52.40Q207.20-59 209.95-63.85Q212.70-68.70 217.85-71.35Q223-74 230-74L230-74Q237.10-74 242.20-71.35Q247.30-68.70 250.05-63.85Q252.80-59 252.80-52.50L252.80-52.50L252.80-20.60Q252.80-14 250.05-9.15Q247.30-4.300 242.20-1.65Q237.10 1 230 1ZM230-10L230-10Q235.10-10 237.70-12.75Q240.30-15.50 240.30-20.60L240.30-20.60L240.30-52.40Q240.30-57.60 237.70-60.30Q235.10-63 230-63L230-63Q224.90-63 222.30-60.30Q219.70-57.60 219.70-52.40L219.70-52.40L219.70-20.60Q219.70-15.50 222.35-12.75Q225-10 230-10Z"

G, ROUND, TILT = 5.0, 1.6, 25           # gap between parts, corner-rounding stroke, upward tilt in degrees

# Arrow: tip at (96,50), arms 18 wide, notch vertex at (74,50)
ARROW = [(96, 50), (66, 18), (48, 18), (74, 50), (48, 82), (66, 82)]

# Nozzle: back end at x=42, 28 tall; its corners there are 120 degrees, so it narrows toward the flame
# like a jet exhaust. Its sides run until they are G away from the arrow's inner edge.
_L, _T30 = math.hypot(26, 32), math.tan(math.radians(30))
_xf = (2368 - 26 * 14 + 26 * _T30 * 42 - _L * G) / (32 + 26 * _T30)
_hf = 14 + (_xf - 42) * _T30
NOZZLE = [(42, 36), (_xf, 50 - _hf), (74 - G * _L / 32, 50), (_xf, 50 + _hf), (42, 64)]


def _clip(poly, y0, y1):
    """The part of a polygon between two horizontal lines."""
    def cut(p, keep, yc):
        out = []
        for i in range(len(p)):
            a, b = p[i - 1], p[i]
            cross = lambda: (a[0] + (b[0] - a[0]) * (yc - a[1]) / (b[1] - a[1]), yc)
            if keep(b[1]):
                if not keep(a[1]):
                    out.append(cross())
                out.append(b)
            elif keep(a[1]):
                out.append(cross())
        return out
    return cut(cut(poly, lambda y: y >= y0, y0), lambda y: y <= y1, y1)


_top, _bot = 50 - _hf, 50 + _hf
_h = (_bot - _top - 2 * G) / 3
RIBS = [_clip(NOZZLE, _top + i * (_h + G), _top + i * (_h + G) + _h) for i in range(3)]

# Flame: the first logo's flame (drawn base at x=166, tip at x=40, centred on y=140), scaled to the nozzle's back end
FLAME = "M166 86C120 80 90 110 40 140C90 170 120 200 166 194Z"
CORE = "M166 106C135 104 110 122 80 140C110 158 135 176 166 174Z"
FLAME_AT = f"translate({42 - G} 50) scale(0.48 {28 / 108:.4f}) translate(-166 -140)"
_flame_pts = [(42 - G + (x - 166) * .48, 50 + (y - 140) * 28 / 108) for x, y in ((166, 86), (166, 194), (40, 140), (100, 95), (100, 185))]

PALETTES = {
    "dark":  dict(c="#4ADE80", flame="#38BDF8", core="#E0F2FE"),
    "light": dict(c="#15803D", flame="#0284C7", core="#BAE6FD"),
    "black": dict(c="#0A0D0C", flame="#0A0D0C", core=None),
    "white": dict(c="#FFFFFF", flame="#FFFFFF", core=None),
}


def _d(poly):
    return "M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in poly) + "Z"


def mark(p, angle=TILT, hooks=False):
    """The mark, rotated up by `angle` degrees around (50,50). `hooks` adds the classes the site animates."""
    solid = lambda poly, extra="": (f'<path{extra} d="{_d(poly)}" fill="{p["c"]}" stroke="{p["c"]}" '
                                    f'stroke-width="{ROUND}" stroke-linejoin="round"/>')
    flame = f'<path d="{FLAME}" fill="{p["flame"]}"/>' + (f'<path d="{CORE}" fill="{p["core"]}"/>' if p["core"] else "")
    flame = f'<g transform="{FLAME_AT}">{flame}</g>'
    if hooks:
        flame = f'<g class="nz-flame">{flame}</g>'
    ribs = "".join(solid(r, f' class="nz-rib" style="--d:{.3 + .15 * i:.2f}s"' if hooks else "") for i, r in enumerate(RIBS))
    return f'<g transform="rotate({-angle} 50 50)">{flame}{ribs}{solid(ARROW)}</g>'


def box(angle=TILT, pad=ROUND / 2 + .5):
    r = math.radians(-angle)
    pts = [(50 + (x - 50) * math.cos(r) - (y - 50) * math.sin(r), 50 + (x - 50) * math.sin(r) + (y - 50) * math.cos(r))
           for x, y in ARROW + NOZZLE + _flame_pts]
    x0, y0 = min(p[0] for p in pts) - pad, min(p[1] for p in pts) - pad
    return x0, y0, max(p[0] for p in pts) + pad - x0, max(p[1] for p in pts) + pad - y0


def svg(vb, body, title="NOZ Studio", px=5):
    x, y, w, h = vb
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:.2f} {y:.2f} {w:.2f} {h:.2f}" '
            f'width="{w * px:.0f}" height="{h * px:.0f}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>')


def logo(p, angle=TILT):
    return svg(box(angle), mark(p, angle))


def favicon(fill=.80):
    x, y, w, h = box()
    s = max(w, h) / fill
    x, y = x + w / 2 - s / 2, y + h / 2 - s / 2
    return svg((x, y, s, s), f'<rect x="{x:.2f}" y="{y:.2f}" width="{s:.2f}" height="{s:.2f}" rx="{s * .22:.2f}" fill="#0A0D0C"/>'
               + mark(PALETTES["dark"]), px=550 / s)


# Lettering colour change, from the first logo: left of a slanted line through the O the name is
# `word` (white or near-black), right of it brand green. FILL is the first logo's green block; the site
# sweeps it in behind the green part with the letters cut out, then fades it (hooks only).
LEFT_OF_SLANT = "M150 40H406.67L323.33 240H150Z"
RIGHT_OF_SLANT = "M406.67 40H600V240H323.33Z"
FILL = "M390 80H532A28 28 0 0 1 560 108V172A28 28 0 0 1 532 200H340Z"


def lockup(p, word, hooks=False):
    """The mark, with NOZ and STUDIO beside it, in the NOZ lettering's coordinates."""
    x0, y0, w, h = box()
    k = 150 / h
    mx = 250 - w * k - 30
    letters = lambda c, clip: (f'<path d="{NOZ}" fill="{c}" stroke="{c}" stroke-width="6" '
                               f'stroke-linejoin="round" clip-path="url(#{clip})"/>')
    defs = (f'<clipPath id="nzl"><path d="{LEFT_OF_SLANT}"/></clipPath>'
            f'<clipPath id="nzr"><path d="{RIGHT_OF_SLANT}"/></clipPath>')
    block = ""
    if hooks:
        defs += (f'<clipPath id="nzw"><rect class="nz-sweep" x="330" y="70" width="240" height="140"/></clipPath>'
                 f'<clipPath id="nzf"><path d="{FILL}"/></clipPath>')
        block = (f'<g class="nz-block" clip-path="url(#nzw)"><path d="{FILL}" fill="{p["c"]}"/>'
                 f'<path d="{NOZ}" fill="#0A0D0C" stroke="#0A0D0C" stroke-width="6" stroke-linejoin="round" clip-path="url(#nzf)"/></g>')
    right = 568 if hooks else 486               # room for the block when it sweeps in
    return svg((mx - 8, 72, right - mx + 8, 178),
               f'<defs>{defs}</defs>'
               f'<g transform="translate({mx:.2f} 84) scale({k:.4f}) translate({-x0:.2f} {-y0:.2f})">{mark(p, hooks=hooks)}</g>'
               + letters(word, "nzl") + letters(p["c"], "nzr") + block
               + f'<path d="{STUDIO}" fill="{p["c"]}" transform="translate(363.5 238) scale(0.36)"/>', px=1)


if OUT == "--inline":
    print(lockup(PALETTES["dark"], "#E6EEE9", hooks=True).replace("<svg ", '<svg class="noz-logo" ', 1))
    sys.exit()
os.makedirs(OUT, exist_ok=True)

files = {
    "noz-logo.svg":                ("Logo", "Main logo, for dark backgrounds", "dark", logo(PALETTES["dark"])),
    "noz-logo-light.svg":          ("Logo, light backgrounds", "White or pale backgrounds", "light", logo(PALETTES["light"])),
    "noz-studio-lockup.svg":       ("NOZ Studio lockup", "The logo with the company name, where there is room", "dark", lockup(PALETTES["dark"], "#E6EEE9")),
    "noz-studio-lockup-light.svg": ("NOZ Studio lockup, light", "Invoices, letters, documents", "light", lockup(PALETTES["light"], "#0A0D0C")),
    "noz-logo-black.svg":          ("One colour, black", "Print, stamps, faxes, engraving", "light", logo(PALETTES["black"])),
    "noz-logo-white.svg":          ("One colour, white", "On photos and coloured backgrounds", "photo", logo(PALETTES["white"])),
    "noz-favicon.svg":             ("App icon", "Favicon, app icon, profile picture", "none", favicon()),
}
# Shown only as "don't" examples on the page; not saved as files.
extras = {
    "dont-flat": logo(PALETTES["dark"], angle=0),
    "dont-allgreen": logo(dict(c="#4ADE80", flame="#4ADE80", core="#BBF7D0")),
}

for name, (_, _, _, s) in files.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(s)

json.dump({"files": {k: {"label": v[0], "use": v[1], "bg": v[2], "svg": v[3]} for k, v in files.items()},
           "extras": extras}, sys.stdout)
