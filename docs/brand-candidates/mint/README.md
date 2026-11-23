# Mint, a candidate (23 Nov 2026)

Not adopted. Kumar is reconsidering the colours: mint was tried and rejected on 30 Oct 2026, and is back on the table
because the kit's `#4ADE80` and `#38BDF8` are stock Tailwind colours, and mint keeps the terminal look while making the
green the brand's own.

| | Dark backgrounds | White backgrounds |
|---|---|---|
| Green | Mint `#3EEBA0` (was `#4ADE80`) | `#217D55`, 5.1:1 on white (was `#15803D`) |
| Flame | Electric blue `#3D7BFF` (was `#38BDF8`) | `#3469D9` (was `#0284C7`) |
| Flame core | `#DCE6FF` (was `#E0F2FE`) | `#C9D7FF` (was `#BAE6FD`) |

The SVGs here come from `_tools/make_logos.py` with those colours swapped: run
`python docs/brand-candidates/mint/make_mint.py` from the repo root. The one-colour black and white logos do not change.
If mint is adopted, change `PALETTES` in `make_logos.py` and the guidelines, regenerate `assets/brand` and the inline
logo as usual, and delete this folder.
