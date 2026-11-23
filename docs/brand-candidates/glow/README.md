# The flame glow, a candidate (23 Nov 2026)

Not adopted. Kumar's favourite so far, chosen over the solid mints and over flat (cel-shaded) bands.

Hyprland's default window-border colours: the arrow and nozzle in green, lit by the flame. A smooth cyan glow spreads
from behind the nozzle, so the ribs catch the most of it and the arrow's tip stays green. The flame is electric blue.
The lettering carries the same colours (Kumar, 23 Nov 2026): NOZ's green half runs from cyan into green, and STUDIO, drawn on its own scale, comes out mostly cyan.

| | Dark backgrounds | White backgrounds (5:1) |
|---|---|---|
| Green (arrow, NOZ, STUDIO) | `#00FF99` | `#007F4C` |
| Glow from the flame | `#33CCFF` | `#1E7896` |
| Flame | `#3D7BFF` | `#3469D9` |
| Flame core | `#DCE6FF` | `#C9D7FF` |

The glow is a radial gradient, so flat-colour uses (stamps, embroidery, vinyl) take the one-colour black or white logo,
which do not change. The site and the apps still need one solid brand colour for buttons and links: `#00FF99` is the
natural one, still to be decided: Bluer (`#08EAC4`, `../bluer/`) is being tried for buttons and links beside this logo.

Made by `_tools/make_logos.py` with these colours and the glow patched in: run
`python docs/brand-candidates/glow/make_glow.py` from the repo root. If adopted, move the glow into `make_logos.py`
itself (and its `--inline` output for `index.html`), update the guidelines, regenerate `assets/brand`, and delete the
candidate folders.
