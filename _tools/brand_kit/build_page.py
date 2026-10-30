"""Build the NOZ Studio brand kit page (published as a private claude.ai artifact).

Usage (from the repo root):
  python _tools/make_logos.py assets/brand > manifest.json
  python _tools/brand_kit/build_page.py manifest.json _tools/brand_kit/template.html noz-brand-kit.html assets/brand
Then publish noz-brand-kit.html to https://claude.ai/artifact/BxKAQVQGMbdBdSFzMVchqw (downloads capability).
"""
import base64, html, json, sys

man = json.load(open(sys.argv[1], encoding="utf-8"))
tpl = open(sys.argv[2], encoding="utf-8").read()
files, extras = man["files"], man["extras"]


def uri(svg):
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


tiles = []
for name, f in files.items():
    sq = " square" if name == "noz-favicon.svg" else ""
    tiles.append(
        f'<div class="tile{sq}"><div class="stage st-{f["bg"]}"><img src="{uri(f["svg"])}" alt="{html.escape(f["label"])}"></div>'
        f'<div class="info"><div class="name">{html.escape(f["label"])}</div><div class="use">{html.escape(f["use"])}</div>'
        f'<div class="file">{name}</div>'
        f'<div class="dl" data-file="{name}" hidden><button data-kind="svg">SVG</button><button data-kind="png">PNG</button></div></div></div>')

donts = [
    ("st-dark", "", extras["dont-flat"], "Don't straighten it", "The 25° tilt is part of the mark."),
    ("st-dark", "", extras["dont-allgreen"], "Don't recolour the flame", "The flame is always blue."),
    ("st-light", "", files["noz-logo.svg"]["svg"], "Don't use the green logo on white", "Use the light-background version."),
    ("st-dark", " stretch", files["noz-logo.svg"]["svg"], "Don't stretch or squash it", "Scale it evenly, or not at all."),
]
dont_html = "".join(
    f'<div class="dont"><div class="stage {st}{cls}"><img src="{uri(s)}" alt="Wrong: {html.escape(h)}"></div>'
    f'<p><b>{html.escape(h)}</b><span>{html.escape(d)}</span></p></div>' for st, cls, s, h, d in donts)


def swatch(name, hexv, role, ratio, ink):
    return (f'<div class="swatch"><div class="chip" style="background:{hexv};color:{ink}">Aa</div>'
            f'<div class="info"><div class="name">{name}</div><div class="role">{role}</div>'
            f'<div class="row"><span class="hex">{hexv}</span><button data-copy="{hexv}" aria-label="Copy {hexv}">Copy</button></div>'
            f'<div class="ratio">{ratio}</div></div></div>')


sw = "".join(swatch(*a) for a in [
    ("Terminal green", "#4ADE80", "Primary. The logo, buttons, links and highlights.", "11.2:1 on near-black", "#0A0D0C"),
    ("Near-black", "#0A0D0C", "Secondary. Backgrounds. Never pure black on screen.", "Base for every ratio here", "#E6EEE9"),
    ("Blue flame", "#38BDF8", "Tertiary, used rarely. The flame and small highlights.", "9.1:1 on near-black", "#0A0D0C"),
    ("Mist", "#E6EEE9", "Text on near-black.", "16.5:1 on near-black", "#0A0D0C"),
    ("Panel", "#101614", "Cards and panels on near-black.", "Surface, not for text", "#E6EEE9"),
    ("Flame core", "#E0F2FE", "The bright centre of the flame only.", "Inside the logo only", "#0A0D0C"),
])
sw_light = "".join(swatch(*a) for a in [
    ("Deep green", "#15803D", "Logo, links and buttons on white.", "5.0:1 on white", "#FFFFFF"),
    ("Deep blue", "#0284C7", "The flame on white. Graphics only, not small text.", "4.1:1 on white", "#FFFFFF"),
    ("White", "#FFFFFF", "Light backgrounds and documents.", "Base for light ratios", "#0A0D0C"),
])

assets = {k: {"svg": v["svg"], "square": k == "noz-favicon.svg" or "icon" in k} for k, v in files.items()}

# Exported PNG/PDF files (made by the site's _tools/export_brand.py), offered as downloads
import os
BRAND = sys.argv[4]
extra_files = [
    ("noz-avatar-400.png", "Social profile picture", "400 × 400 PNG, safe for a circle crop"),
    ("noz-apple-touch-icon.png", "iPhone home-screen icon", "180 × 180 PNG"),
    ("noz-favicon-32.png", "Favicon", "32 × 32 PNG"),
    ("noz-logo-light.pdf", "Logo for print", "Vector PDF, for white paper"),
    ("noz-studio-lockup-light.pdf", "NOZ Studio lockup for print", "Vector PDF, for white paper"),
    ("noz-logo-black.pdf", "One-colour logo for print", "Vector PDF, black"),
]
bin_json, extra_html = {}, []
for name, label, note in extra_files:
    raw = open(os.path.join(BRAND, name), "rb").read()
    bin_json[name] = base64.b64encode(raw).decode()
    thumb = (f'data:image/png;base64,{bin_json[name]}' if name.endswith(".png")
             else uri(files["noz-logo-light.svg"]["svg"] if "black" not in name else files["noz-logo-black.svg"]["svg"]))
    bg = ' style="background:#fff"' if name.endswith(".pdf") else ""
    extra_html.append(f'<div class="file"><img src="{thumb}" alt=""{bg}><div class="ft"><b>{label}</b><span>{name} · {note}</span></div>'
                      f'<button data-bin="{name}" hidden>Download</button></div>')
out = (tpl.replace("{{HERO}}", uri(files["noz-logo.svg"]["svg"]))
          .replace("{{ICON}}", uri(files["noz-icon.svg"]["svg"]))
          .replace("{{TILES}}", "".join(tiles))
          .replace("{{DONTS}}", dont_html)
          .replace("{{SWATCHES}}", sw)
          .replace("{{SWATCHES_LIGHT}}", sw_light)
          .replace("{{EXTRAS}}", "".join(extra_html))
          .replace("{{BIN_JSON}}", json.dumps(bin_json))
          .replace("{{ASSETS_JSON}}", json.dumps(assets).replace("</", "<\\/")))
assert "{{" not in out
open(sys.argv[3], "w", encoding="utf-8").write(out)
print(len(out))
