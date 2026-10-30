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
- **Colors (final, 30 Oct 2026):** primary terminal green `#4ADE80`, secondary near-black `#0A0D0C` (not pure black on screen), tertiary blue flame `#38BDF8`, text `#E6EEE9`. On white: deep green `#15803D`, deep blue `#0284C7`. Never use green vs blue alone to mean different things, and keep blue rare. Teal, mint, violet, orange, yellow and pink variants were tried and rejected: green reads as growth and blue as trust to business-owner clients.
- **NOZ logo (final, 30 Oct 2026):** an open nozzle tilted up 25°, blue flame out of the open end, green fill up to a slanted line, and NOZ in JetBrains Mono ExtraBold Italic (thickened, converted to outlines) that turns into cut-outs over the fill. The "NOZ Studio" lockup adds small spaced STUDIO (JetBrains Mono Bold) under the nozzle. All versions are in `assets/brand/` (dark, light, one-colour black/white, icon without lettering, favicon, plus PNG icons, a 400 px social avatar, print PDFs and the site's `og-image.png` link preview). Regenerate them with `python _tools/make_logos.py assets/brand` then `python _tools/export_brand.py assets/brand` (needs Chrome); never edit them by hand or retype NOZ in a font. Under 120 px wide use the icon. `index.html` also carries an inline copy of the lockup (for its charge-up animation): update it too if the logo ever changes.
- **Brand guidelines:** `docs/brand-guidelines.md` is the source of truth (colours, type, logo rules, voice traits, tone by context, prohibited terms, messaging and elevator pitches, imagery, AI image prompts). The `brand` and `design` skills read it; keep its table formats, since their scripts parse them. Brand green is the brand, not "success": status colours are `#22C55E` / `#FBBF24` / `#F87171`, always with an icon and a word.
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
- `index.html`: personal hero with a "Now" card (#home: the name slides up from a mask, a blinking terminal caret, and faint "boost" streaks drifting up at the logo's 25°), a scrolling capabilities strip, then the NOZ Studio feature (#noz: inline NOZ Studio lockup that charges up, lights its flame, flickers, and boosts on hover; live animated dashboard and phone mock, promise strip), then services, work (CSS-drawn thumbnails), process and pricing (all NOZ), then About me (#about), Projects (#projects: NOZ card plus a coming-soon card) and Contact.
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
