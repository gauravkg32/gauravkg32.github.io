# NOZ Studio Brand Guidelines v1.2

> Last updated: 31 Oct 2026
> Status: Final (logo and colours decided 30 Oct 2026)

The source of truth for the NOZ Studio brand. The `brand` and `design` skills read this file; the brand kit page and `assets/brand/` follow it. NOZ comes from nitrous, the boost in racing games: **a boost for your business**.

## Quick Reference

| Element | Value |
|---------|-------|
| Primary Color | #4ADE80 (Terminal Green) |
| Secondary Color | #0A0D0C (Near-black) |
| Accent Color | #38BDF8 (Blue Flame) |
| Primary Font | Inter |
| Voice | Plain-spoken, Dependable, Practical |

---

## 1. Color Palette

Green reads as growth and money to business owners; blue as trust and technology. Mostly near-black and green; blue only in the flame and small highlights.

### Primary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Terminal Green** | #4ADE80 | rgb(74,222,128) | Logo, buttons, links, highlights on dark |
| **Terminal Green Dark** | #15803D | rgb(21,128,61) | Logo, links and buttons on white (5.0:1) |

### Secondary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Near-black** | #0A0D0C | rgb(10,13,12) | Backgrounds. Never pure black on screen |
| **Panel** | #101614 | rgb(16,22,20) | Cards and panels on near-black |

### Accent Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Blue Flame** | #38BDF8 | rgb(56,189,248) | The flame and rare highlights (9.1:1 on near-black) |
| **Blue Flame Dark** | #0284C7 | rgb(2,132,199) | The flame on white. Graphics only, not small text (4.1:1) |
| **Flame Core** | #E0F2FE | rgb(224,242,254) | Centre of the flame, inside the logo only |

### Neutral Palette

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Mist | #E6EEE9 | rgb(230,238,233) | Text on near-black (16.5:1) |
| Muted | #8EA39A | rgb(142,163,154) | Secondary text on near-black |
| Border | #1C2925 | rgb(28,41,37) | Dividers and borders on dark |
| White | #FFFFFF | rgb(255,255,255) | Light backgrounds, documents |

### Semantic Colors

Brand green is the brand, not "success". Status colours always come with an icon and a word, never colour alone.

| State | Hex | Usage |
|-------|-----|-------|
| Success | #22C55E | Done, delivered, saved. Always with ✓ and a label |
| Warning | #FBBF24 | Pending, packed, low stock |
| Error | #F87171 | Failed, out of stock, destructive actions |
| Info | #38BDF8 | Neutral notices (rare) |

### Accessibility

- Mist on near-black: 16.5:1 (AAA)
- Terminal Green on near-black: 11.2:1 (AAA)
- Terminal Green Dark on white: 5.0:1 (AA)
- Terminal Green #4ADE80 on white is 1.7:1: never use it for text or the logo on white
- Never tell two things apart by green vs blue alone

---

## 2. Typography

### Font Stack

```css
--font-heading: 'Inter', system-ui, sans-serif;
--font-body: 'Inter', system-ui, sans-serif;
--font-mono: 'JetBrains Mono', ui-monospace, monospace;
```

JetBrains Mono is for labels, numbers and code-like details. The NOZ lettering in the logo is JetBrains Mono ExtraBold Italic converted to shapes: use the logo files, never retype it.

### Type Scale

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Display (h1) | clamp(2.6rem, 8vw, 5rem) | 700 | 1.08 |
| H2 | clamp(1.7rem, 3.5vw, 2.4rem) | 700 | 1.15 |
| H3 | 1.15rem | 600 | 1.3 |
| Body | 16px | 400 | 1.65 |
| Label (mono, uppercase, +0.12em) | 0.78rem | 500 | 1.4 |

Running text stays under about 65 characters wide.

### Font Loading

Google Fonts: Inter 400/500/600/700 and JetBrains Mono 500/700 with `display=swap`.

---

## 3. Logo Usage

An open nozzle tilted up 25°, a blue flame out of the open end, green fill up to a slanted line, and NOZ in heavy italic letters that become cut-outs over the fill.

### Variants

| File (assets/brand/) | Use |
|------|-----|
| noz-logo.svg | Main logo, dark backgrounds |
| noz-logo-light.svg / .pdf | White and pale backgrounds, print |
| noz-studio-lockup.svg / -light.svg / -light.pdf | Where the full name "NOZ Studio" matters |
| noz-logo-black.svg / .pdf, noz-logo-white.svg | One colour: stamps, engraving, photos |
| noz-icon.svg / noz-icon-light.svg | No lettering: below 40 px only (browser tabs, tiny UI) |
| noz-favicon.svg / noz-favicon-32.png | Browser tabs |
| noz-apple-touch-icon.png | iPhone home screen (180 px) |
| noz-avatar-400.png | Social profile pictures: logo with NOZ, safe for a circle crop |

Regenerate everything with `python _tools/make_logos.py assets/brand` then `python _tools/export_brand.py assets/brand`. Never edit the files by hand.

### Clear Space

Keep empty space around the logo at least as tall as the nozzle's body. No text, edges or other logos inside it.

### Minimum Size

Pick the version by how big the logo will appear. The lettering needs room; STUDIO is much smaller than NOZ.

| Version | Use from | Print |
|---------|----------|-------|
| NOZ Studio lockup (with STUDIO) | 130 px wide; 160 px in a round avatar | 35 mm wide |
| Logo with NOZ | 40 px wide or tall | 10 mm |
| No lettering | Below 40 px only (browser tabs) | Not for print |

### Don'ts

- Don't change the 25° angle or straighten it (the tilt is part of the mark)
- Don't recolour any part; the flame is always blue
- Don't use the dark-background logo on white; use the light version
- Don't stretch, squash, crop, or add shadows, glows or outlines
- Don't retype NOZ in a font or rearrange the parts

---

## 4. Voice & Tone

Talk like a capable friend who builds software: plain words, short sentences, and only promises the product keeps.

### Brand Personality

| Trait | Description | Do | Don't |
|-------|-------------|-----|-------|
| **Plain-spoken** | Everyday words a shop owner uses | "Your orders, sales and stock in one app" | "An integrated omnichannel ERP solution" |
| **Dependable** | Promise only what we deliver, then deliver it | "Daily backups. Works offline." | "Never lose anything, ever!" |
| **Practical** | Lead with what the client gets | "See which reps visited which shops today" | "Powered by a modern tech stack" |
| **Friendly** | Warm and direct, never stiff | "Got a project? I read every message." | "Kindly revert at the earliest." |
| **Quietly confident** | Calm, no hype | "We build it, run it and keep it improving" | "Revolutionary, game-changing software" |

### Tone by Context

| Context | Tone | Example |
|---------|------|---------|
| Website | Clear and benefit-first | "A boost for your business." |
| WhatsApp / first reply | Warm, short, a question back | "Happy to help. How do you take orders today?" |
| Proposal / quote | Precise, scoped, no fluff | "Setup covers data import and training for 5 users." |
| Something went wrong | Own it, say what's next | "Sync failed at 2 pm. Fixed, and nothing was lost." |
| Social posts | Show real work, one idea per post | "Reps book orders with no signal. Here's how." |

### Prohibited Terms

| Avoid |
|-------|
| websites turned into apps |
| Web → App |
| NO2 |
| Client names |
| enterprise-grade |
| cutting-edge |
| seamless |
| leverage |
| You own the code |

### Say Instead

| Instead of | Say |
|------------|-----|
| websites turned into apps, Web → App | websites, mobile apps, business software |
| NO2, Noz | NOZ (always in capitals) |
| a client's name | a generic description ("a consumer brand's field team") |
| enterprise-grade, cutting-edge, seamless | what it actually does |
| how it's built (tools, methods) | what the client gets |
| you own the code | your data, always exportable |

---

## 5. Messaging

### Positioning Statement

NOZ Studio is the managed software studio for growing Indian businesses that run on spreadsheets, paper and WhatsApp, who want their orders, sales and stock in one place without hiring an IT team, because we build the software, host it, back it up and keep improving it for one monthly fee.

### Value Proposition

For business owners who lose time and money to scattered orders and stock, NOZ Studio builds and runs business software tailored to how they work. Unlike one-time freelance projects, we stay: hosting, backups, updates and support are included, and their data stays theirs.

### Key Messages

| Message | Audience Need | Proof Point |
|---------|---------------|-------------|
| Your orders, sales and stock in one app | Stop chasing paper and WhatsApp | Order, sales and inventory products already built |
| Works where your team works | Reps out of signal range | Offline-first field-sales app with GPS- and photo-verified visits |
| We run it, you run your business | No IT team | Hosting, daily backups, updates and support in the monthly plan |
| Your data is yours | Fear of lock-in | Export anytime |

### Elevator Pitches

**10-second:** NOZ Studio builds and runs business software, like order booking, sales tracking and stock, so growing businesses can get off spreadsheets and WhatsApp.

**30-second:** Most growing businesses run on paper, Excel and WhatsApp groups, and things slip. NOZ Studio sets up software for your orders, sales and stock, tailored to how you work, and then we run it: hosting, daily backups, updates and support for one monthly fee. Your team gets an app that works even with no signal, and your data is always yours to export.

**60-second:** Add to the 30-second pitch one real example: a field-sales team whose reps book orders and verify shop visits with GPS and photos, offline, while the owner sees everything on a dashboard. Close with: "What's the most annoying part of how you take orders today?"

---

## 6. Imagery Guidelines

### Photography Style

- Real screens of real products, on near-black, are the main imagery
- No stock photos of handshakes or people at laptops; no AI-generated people
- Founder photos are fine on the personal site, natural light, uncluttered

### Illustrations

- Simple geometric, CSS- or SVG-drawn product mock-ups (dashboards, phones, maps)
- Angled "boost" lines at the logo's 25° are the one decorative motif

### Icons

- Line icons on a 24 px grid, 1.8 px stroke, round caps and joins
- Green (#4ADE80) on a 12% green tint tile, or current text colour

---

## 7. Design Components

### Buttons

| Type | Style |
|------|-------|
| Primary | Terminal Green fill, #04140A text, 10 px radius, 600 weight |
| Ghost | Transparent, Border outline, Mist text |

### Spacing Scale

4, 8, 12, 16, 24, 32, 48, 64, 96 px. Sections breathe: 64–104 px vertical padding.

### Border Radius

| Element | Radius |
|---------|--------|
| Buttons | 10 px |
| Cards | 14 px |
| Big panels | 16–20 px |
| Tags and pills | 999 px |

---

## AI Image Generation

### Base Prompt Template

```
Flat vector style on a near-black #0A0D0C background, terminal green #4ADE80
as the main colour, one small sky-blue #38BDF8 highlight, clean geometric
shapes, generous empty space, no people, no text unless specified, no
gradients except a soft glow.
```

### Style Keywords

| Category | Keywords |
|----------|----------|
| **Look** | terminal, dashboard, clean, geometric, flat vector |
| **Motion** | speed lines at 25°, boost, lift |
| **Setting** | Indian small business, shop, warehouse, field sales |

### Visual Mood Descriptors

- Focused
- Fast
- Dependable
- Calm, like dark-mode software (not neon gaming)

### Visual Don'ts

| Avoid | Why |
|-------|-----|
| Neon cyberpunk and purple | Reads as gaming, not business software |
| Stock-photo people and handshakes | Generic; clients want to see the product |
| Rockets and fire as the subject | The flame belongs to the logo only |
| Redrawn or "improved" NOZ logos | Always place the real logo file |

### Example Prompts

**Social post**:
```
Phone showing an order-booking app on a near-black desk, terminal green accents, flat vector, no people
```

**Website illustration**:
```
Owner dashboard with order bars and a low-stock alert, terminal green on near-black, one sky-blue highlight, flat vector
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.2 | 31 Oct 2026 | Size tiers: lockup from 130 px, NOZ from 40 px, no lettering only below 40 px; avatar and iPhone icon now show NOZ |
| 1.1 | 31 Oct 2026 | Messaging, voice traits, tone by context, semantic colours, imagery, larger clear space, PNG/PDF exports |
| 1.0 | 30 Oct 2026 | Final logo (25° open nozzle) and colours (green + sky) |
