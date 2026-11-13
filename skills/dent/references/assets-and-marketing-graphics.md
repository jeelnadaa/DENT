# Assets and Marketing Graphics

Part 1: exact specs for product assets (favicons, share images, app icons, splash screens, store screenshots, export rules). Part 2: graphic design for marketing material (social, print, slides, ads, email, infographics, video).

# Part 1 — Asset specs

Exact sizes change occasionally; these are current common specs. Verify with the platform's official docs before a production release.

---

## 1. Favicons (web)
Minimal modern set:
| File | Size | Notes |
|---|---|---|
| `favicon.ico` | 32×32 (can include 16, 32, 48) | Legacy/browser tabs, placed at site root |
| `icon.svg` | vector | Modern browsers; can include dark-mode CSS media query inside the SVG |
| `apple-touch-icon.png` | **180×180** | iOS home screen; no transparency (iOS fills black), add own background and ~10% padding |
| `icon-192.png`, `icon-512.png` | 192×192, 512×512 | Web app manifest (Android/PWA) |
| maskable icon | 512×512 with safe zone (important content within central ~80% circle) | `"purpose": "maskable"` in manifest |

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0A0A0B" media="(prefers-color-scheme: dark)">
```
Design: simplify the logo to the symbol/lettermark; strong silhouette; test at 16px.

## 2. Social share / Open Graph images
| Platform | Recommended | Notes |
|---|---|---|
| Open Graph (Facebook, LinkedIn, WhatsApp, Slack, Discord…) | **1200×630** (1.91:1) | `og:image`, keep text in center safe area; < ~5MB |
| X (Twitter) summary_large_image | 1200×628 (≈1.91:1) | Falls back to OG tags |
| Square fallback | 1200×1200 | Some apps crop to square |

```html
<meta property="og:title" content="…"><meta property="og:description" content="…">
<meta property="og:image" content="https://…/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
```
Design: title (large, ≤ 8 words), logo, brand background; key content inside central ~1000×500 area (cropping varies); legible on mobile previews; per-page OG images for blogs/products.

## 3. iOS app icon
- Provide a **1024×1024** PNG master (no transparency, no rounded corners — the system masks it). Current Xcode can generate all sizes from one image; iOS 18+ also supports dark and tinted appearance variants.
- Design: simple, one focal element, no text (unless the logo is text), avoid photos, fill the square, test at 60px and smaller.

## 4. Android app icon
- **Adaptive icon:** foreground + background layers, each **108×108dp**; safe zone central **66×66dp** (masks vary: circle, squircle, rounded square).
- **Monochrome layer** for themed icons (Android 13+).
- Play Store listing icon **512×512** PNG (32-bit).
- Feature graphic (Play Store) **1024×500**.

## 5. Windows / macOS app icons
- macOS: 1024×1024 master; follow macOS icon grid (rounded-rect shape with shadow, as per HIG templates).
- Windows: multiple sizes (16–256) in .ico; tiles/manifest assets for Store apps.

## 6. Splash / launch screens
- **iOS:** launch screen should look like the first screen of the app (background color + maybe logo), not an ad; no text that needs localization.
- **Android 12+:** SplashScreen API: centered icon (animated optional) on a background color; icon area 240×240dp with ~160dp visible circle.
- **PWA:** generated from manifest `name`, `background_color`, icons.
- Keep launch fast; avoid artificial delays.

## 7. App store screenshots (summary)
- Use current required sizes from App Store Connect / Google Play Console (they change with devices). Typically: iPhone 6.9" and 6.5" displays, iPad 13"; Google Play phone 16:9 or 9:16, min 320px, max 3840px.
- Design: first 2–3 screenshots carry the message (caption + real UI), consistent background, readable captions, localized versions.

## 8. Export rules
- Logos/icons: SVG master + PNG fallbacks at 1×/2×/3×.
- Photos: AVIF/WebP + JPEG fallback.
- Name files clearly: `logo-horizontal-dark.svg`, `og-pricing.png`.
- Keep a source folder with editable files.

---

# Part 2 — Graphic design and marketing material

For designs outside product UI: social posts, posters, flyers, banners, slides, email campaigns, ads, print. Same foundations apply (hierarchy, contrast, alignment, consistency) with medium-specific rules.

---

## 1. Universal graphic design principles
- **One message per piece.** Decide the single takeaway before designing.
- **Visual hierarchy in 3 levels:** (1) hook — headline/image noticed first, (2) supporting info, (3) details/CTA/logo.
- **Contrast** of size, weight, color and space creates the hierarchy.
- **Alignment & grid** even in posters — edges line up.
- **Balance:** symmetric (formal, calm) or asymmetric (dynamic) — never accidental.
- **White space** makes it premium and readable.
- **Typography:** max 2 typefaces; headline short and big; body readable at viewing distance.
- **Color:** brand palette; one accent for the most important element.
- **Repetition:** consistent template elements across a campaign/series.
- **Readability test:** view at actual size (phone feed size for social, distance for posters).

## 2. Social media (common sizes — verify current platform specs)
| Format | Size | Notes |
|---|---|---|
| Instagram feed portrait | **1080×1350** (4:5) | Best feed real estate |
| Instagram/Facebook square | 1080×1080 | |
| Stories / Reels / TikTok / Shorts | **1080×1920** (9:16) | Keep text out of top ~250px and bottom ~340px (UI overlays) |
| LinkedIn feed image | 1200×627 or 1080×1080/1350 | |
| X (Twitter) image | 1600×900 (16:9) | |
| YouTube thumbnail | 1280×720 | Big face/text, high contrast; readable at small size |
| LinkedIn banner | 1584×396 | Account for profile photo overlap |
| X header | 1500×500 | |
| YouTube channel art | 2560×1440 | Safe area 1546×423 center |
| Facebook cover | ~851×315 (desktop) | Mobile crops sides |

Rules: text large (readable on a phone in a feed), ≤ ~20 words on an image, strong contrast, brand-consistent template, carousel slides with consistent layout and a progress cue, captions for video (most watch muted).

## 3. Posters & flyers (print)
- Sizes: A4 (210×297mm), A3, A2, US Letter (8.5×11in), Tabloid (11×17in).
- **300 DPI** at final size; **CMYK** color for professional print (RGB colors may shift); **3mm bleed** (0.125in) on all sides; keep text **5mm** inside the trim (safe zone).
- Hierarchy for distance: headline readable from ~3m; essential info (what, when, where, CTA/QR) clear.
- QR codes: min ~2×2cm, high contrast, quiet zone, test scanning; include short URL too.
- Export: PDF/X with crop marks and bleed.

## 4. Presentations / slides
- **One idea per slide;** headline states the takeaway ("Revenue grew 40% after launch"), not the topic ("Revenue").
- 16:9 (1920×1080) default.
- Large type: titles 36–54pt, body ≥ 20–24pt; ≤ ~6 lines of text; prefer visuals.
- Consistent template: title, content, section divider, image, quote, chart, closing.
- Charts simplified (data-visualization.md), one highlight color.
- Contrast for projectors (rooms wash out light colors — use strong contrast).
- Speaker notes hold the detail; slides support the speaker.

## 5. Ads & banners (display)
- Common IAB sizes: 300×250 (medium rectangle), 728×90 (leaderboard), 160×600 / 300×600 (skyscraper/half page), 320×50 / 320×100 (mobile), 970×250 (billboard).
- Elements: logo, short headline (≤ 5–7 words), image, clear CTA button; brand consistent.
- File size limits (often ~150KB); animation limited (often ≤ 15–30s, few loops).
- Honest claims; clearly identifiable as ads.

## 6. Email campaigns
- Single column ~600px (max ~640); images at 2× (1200px) scaled down; logo ~150–200px wide; HTML < ~100KB (some clients clip larger emails); mobile-first; key message + CTA in the first screen.
- Bulletproof (HTML/CSS) buttons, ≥ 44px tall; live text over images (many clients block images by default); alt text.
- Web-safe font fallbacks; dark-mode friendly (transparent logos with outline or dark-mode variant; avoid pure white backgrounds in images).
- Clear sender, subject (≤ ~40–50 chars) + preview text; unsubscribe link visible (legal requirement under CAN-SPAM/GDPR etc.).
- Inspiration: Really Good Emails.

## 7. Print stationery
- Business card 85×55mm (EU) / 3.5×2in (US) / 90×54mm (India common); letterhead A4; envelope DL.
- Min type size ~7–8pt; 300 DPI; CMYK; bleed.

## 8. Infographics
- Clear narrative top-to-bottom; one data story; consistent icon style; source cited; data-visualization.md rules apply.

## 9. Video & motion graphics (brief)
- Safe areas for titles; captions burned-in or provided; brand intro/outro ≤ 2–3s; consistent lower-thirds; music licensed.
