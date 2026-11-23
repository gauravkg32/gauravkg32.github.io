# Kumar Gaurav's personal site (gauravkg32.github.io)

Personal page of Kumar Gaurav, with his managed web and app studio **NOZ Studio** as the main featured section. Jekyll on GitHub Pages: every push to `main` deploys in about a minute. CLAUDE.md is excluded from the built site in `_config.yml`.

**This repo is public, and so is this file.** Never put private emails, passwords, keys, phone numbers, the founder's city, or client names in here or anywhere else in the repo.

## Brand decisions

- **Brand: NOZ** (from nitrous, the racing-game boost; never write "NO2"). The company name is shown as **NOZ Studio**. "Studio" is a descriptor, not part of product names.
- **Owned:** domain `nozstudio.com` (GoDaddy), GitHub account `nozstudio`, and a dedicated NOZ Studio Gmail account used as that GitHub login (address deliberately not written here; ask Kumar if it's needed). Keep that Gmail off the site. A domain email (e.g. hello@nozstudio.com, forwarded) is planned as the public contact address.
- **Two sites (tentative):** NOZ Studio will later get its own site under the `nozstudio` account at nozstudio.com. When that happens, the #noz section moves there almost unchanged and this page keeps a short NOZ Studio card. This repo stays Kumar Gaurav's personal page and shifts toward his own projects over time.
- **Dropped names:** Edgecraft Studio, the old placeholder (edgecraftstudio.com is a live same-name US software studio). Techweaver, Technoz, Pitstop and Swiftcraft are crowded or clash.
- **Trademark:** an IP India search for NOZ in classes 9 and 42 found only one abandoned NOZ (class 9). NOS (a sound-alike) still needs searching. Filing NOZ is under consideration.
- **Product naming:** apps are "X by NOZ Studio" (short form "NOZ" only in tight spaces). Modules use plain descriptive names: Orders, Sales, Stock. The suite name is undecided.
- **Colors (final, 30 Oct 2026):** primary terminal green `#4ADE80`, secondary near-black `#0A0D0C` (not pure black on screen), tertiary blue flame `#38BDF8`, text `#E6EEE9`. On white: deep green `#15803D`, deep blue `#0284C7`. Never use green vs blue alone to mean different things, and keep blue rare. Teal, mint, violet, orange, yellow and pink variants were tried and rejected: green reads as growth and blue as trust to business-owner clients. **Mint is being reconsidered (23 Nov 2026):** a candidate set of logos is in `docs/brand-candidates/mint/` (not adopted; `assets/brand` is unchanged).
- **NOZ logo (final, 1 Nov 2026):** a green boost arrow, a jet nozzle of three ribs coming out of its back (its back corners are 120°, so it narrows toward the flame like a real exhaust), and the first logo's curved blue flame with a pale core coming out of the nozzle, all tilted up 25°. The mark is the logo and is the same drawing at every size, down to a 16 px tab (Kumar's brother's rule: a cut-down version looks like a counterfeit of the real one). The "NOZ Studio" lockup sets NOZ (JetBrains Mono ExtraBold Italic, outlines) and spaced STUDIO beside the mark; NOZ keeps the first logo's colour change, white (near-black on light) up to a slanted line through the O and green after it. Use the lockup from 130 px wide. (Tried and rejected for the lettering: ribbed letters, gradients, the first logo's full green block with cut-outs, which crowds small sizes and fights green buttons, and two-tone O variants.) All files are in `assets/brand/` (dark, light, one-colour black/white, lockups, favicon/app icon, PNG icons, a 400 px social avatar, print PDFs and the site's `og-image.png`). Regenerate with `python _tools/make_logos.py assets/brand` then `python _tools/export_brand.py assets/brand` (needs Chrome); never edit them by hand or retype NOZ in a font. `index.html` carries an inline copy of the lockup with animation hooks (`nz-rib`, `nz-flame`, `nz-block`, `nz-sweep`): replace it with the output of `python _tools/make_logos.py --inline` whenever the logo changes. Rejected on 31 Oct-1 Nov 2026: the lettered nozzle (too busy, unreadable small), a NOZ tile favicon (a second logo), a plain upright flame (reads as LPG gas in India), a wordmark only, and many arrow variants: straight triangle flames looked like an ice cream cone, two even tails like a tooth, square-backed nozzles like a house.
- **Brand guidelines:** `docs/brand-guidelines.md` is the source of truth (colours, type, logo rules, voice traits, tone by context, prohibited terms, messaging and elevator pitches, imagery, AI image prompts). The `brand` and `design` skills read it; keep its table formats, since their scripts parse them. Brand green is the brand, not "success": status colours are `#22C55E` / `#FBBF24` / `#F87171`, always with an icon and a word. Success green is close to brand green, so in app screens brand green is only for the main action button (one per screen) and the logo, and success shows as a toast with ✓ and words in a fixed place.
- **Brand kit page:** a private claude.ai artifact (Kumar has the link). Its source is `_tools/brand_kit/` (template plus build script, usage in the script's docstring); when the brand changes, update `docs/brand-guidelines.md`, the template, and republish to the same artifact URL.
- **Personal logo:** `assets/logo.svg` is the KG monogram and stays the favicon of this personal page. The NOZ favicon is for nozstudio.com.
- For any new name ideas, use the `brand-name-check` skill.

## Business positioning (drives the copy)

- **Managed service:** setup fee plus a monthly plan (hosting, daily backups, updates, support). Clients don't own the code; they own their data and can export it anytime. No prices on the site.
- **Services:** Websites, Mobile apps, Business software (orders, sales, inventory, field teams). Client work only; no games.
- **Location is shown only as "India".**
- **Work section:** describe client projects generically and never name clients.
- **Promises on the site the products must actually keep:** offline, daily backups, data export.
- **Copy rule:** never describe the method as "websites turned into apps" or "Web → App". Say what clients get (websites, mobile apps, business software). The benefit line "built alongside your website so you get both for less" is fine.

## Site structure

- `_config.yml`: name, tagline, studio name/tagline/pitch, email/LinkedIn (empty = buttons hidden), nav.
- `index.html`: personal hero with a "Now" card (#home: the name slides up from a mask, a blinking terminal caret, and faint "boost" streaks drifting up at the logo's 25°), a scrolling capabilities strip, then the NOZ Studio feature (#noz: inline NOZ Studio lockup whose nozzle ribs slide in one by one, the flame lights and flickers, then the first logo's green block sweeps in behind the name with the letters cut out and fades away; the flame boosts on hover; live animated dashboard and phone mock, promise strip), then services, work (CSS-drawn thumbnails), process and pricing (all NOZ), then About me (#about), Projects (#projects: NOZ card plus a coming-soon card) and Contact.
- `assets/css/style.css`: design tokens at the top, then sections. Motion styles and the newer sections are near the end.
- `assets/js/main.js`: hero entrance, heading reveals (skipped for `.noz-title`, whose gradient text breaks when split), live dashboard ticker, cursor effects (desktop only), nav and tab-bar scroll-spy, phone carousels, Ctrl+K quick menu (its items list lives in this file).
- `_layouts/default.html`: header, footer, quick menu markup, phone tab bar (Home, NOZ, Work, About, Contact).
- **Blog:** `/blog/` exists but isn't linked. Link it from the nav and quick menu once 2-3 real posts exist.
- **Everything must respect `prefers-reduced-motion`**, and content must stay visible if JS never runs. `.js` is set in `<head>`, with a timer fallback for `.ready`.

## Working on it

- Jekyll and Ruby aren't installed locally. To preview, render `index.html` through `_layouts/default.html` with a small Python script (substitute the `site.*` values, strip Liquid), serve it with `python -m http.server`, and check at 1100px and 375px widths. The browser pane pauses animations while hidden, so a screenshot can catch a mid-animation frame; confirm with JS (computed opacity or class names) before calling something broken.
- Commit as Kumar Gaurav <gauravkg32@users.noreply.github.com>.

## Open items

- A contact email (hello@nozstudio.com once forwarding is set up), plus LinkedIn if wanted. The contact section, footer and quick menu currently offer only GitHub.
- The About me bio is a Claude draft; Kumar may rewrite it.
- Later: the separate NOZ Studio site on nozstudio.com (CNAME file plus GoDaddy DNS records).
- A public demo of the order-booking app, for a "Try the demo" button.
