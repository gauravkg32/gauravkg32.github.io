"""Export PNG and PDF versions of the SVG logos with headless Chrome.

Usage: python _tools/export_brand.py assets/brand
Needs Google Chrome installed. Writes next to the SVGs:
  noz-favicon-32.png, noz-apple-touch-icon.png (180), noz-avatar-400.png  (icons, square)
  noz-logo-light.pdf, noz-studio-lockup-light.pdf, noz-logo-black.pdf      (print, vector)
  og-image.png (1200x630 link preview for this site)
"""
import os, subprocess, sys, tempfile

CHROME = next((p for p in [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
] if os.path.exists(p)), None)

OUT = os.path.abspath(sys.argv[1])
TMP = tempfile.mkdtemp()


def chrome(*args):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--default-background-color=00000000", *args],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)


FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=JetBrains+Mono:wght@500&display=block">'


def page(name, body, css=""):
    path = os.path.join(TMP, name + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"<!doctype html><meta charset=utf-8>{FONTS}<style>html,body{{margin:0;background:transparent}}{css}</style>{body}")
    return "file:///" + path.replace("\\", "/")


def svg(name):
    return open(os.path.join(OUT, name), encoding="utf-8").read()


def png(name, src_svg, w, h, scale=1.0, bg="transparent"):
    """scale < 1 adds padding (for avatars that get cropped to a circle); bg fills the square."""
    url = page(name, svg(src_svg), f"html,body{{background:{bg};width:{w}px;height:{h}px;display:grid;place-items:center}}"
                                   f"svg{{display:block;width:{w * scale}px;height:{h * scale}px}}")
    chrome(f"--screenshot={os.path.join(OUT, name)}", f"--window-size={w},{h}", url)


def pdf(name, src_svg):
    url = page(name, svg(src_svg), "@page{size:530px 310px;margin:0}svg{display:block;width:530px;height:310px}")
    chrome(f"--print-to-pdf={os.path.join(OUT, name)}", "--no-pdf-header-footer", url)


png("noz-favicon-32.png", "noz-favicon.svg", 32, 32)
png("noz-apple-touch-icon.png", "noz-logo.svg", 180, 180, scale=.9, bg="#0A0D0C")  # iOS rounds the corners itself
png("noz-avatar-400.png", "noz-logo.svg", 400, 400, scale=.8, bg="#0A0D0C")  # safe inside a circle crop; shown at 40-170 px, so NOZ but no STUDIO
for n in ["noz-logo-light", "noz-studio-lockup-light", "noz-logo-black"]:
    pdf(n + ".pdf", n + ".svg")

og = f"""<div class=og><div class=t><p class=e>Hi, I'm</p><h1>Kumar Gaurav</h1>
<p class=l>I build software that runs businesses: websites, apps and the tools behind them.</p>
<p class=u>gauravkg32.github.io</p></div><div class=lg>{svg("noz-studio-lockup.svg")}</div></div>"""
css = """.og{width:1200px;height:630px;box-sizing:border-box;padding:80px;display:flex;align-items:center;gap:40px;font-family:Inter,sans-serif;color:#E6EEE9;
background:radial-gradient(700px 420px at 85% 15%,rgba(74,222,128,.18),transparent 70%),radial-gradient(500px 400px at 5% 100%,rgba(56,189,248,.10),transparent 70%),
linear-gradient(#1c2925 1px,transparent 1px) 0 0/56px 56px,linear-gradient(90deg,#1c2925 1px,transparent 1px) 0 0/56px 56px,#080b0a}
.t{flex:1}.e{font:500 22px 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:#4ADE80;margin:0 0 18px}
h1{font-size:88px;line-height:1;letter-spacing:-.03em;margin:0 0 26px}.l{font-size:30px;line-height:1.4;color:#8ea39a;margin:0 0 34px;max-width:620px}
.u{font:500 22px 'JetBrains Mono',monospace;color:#8ea39a;margin:0}.lg svg{width:360px;height:auto;display:block}"""
url = page("og", og, css)
chrome(f"--screenshot={os.path.join(OUT, 'og-image.png')}", "--window-size=1200,630", "--virtual-time-budget=10000", url)
print("exported to", OUT)
