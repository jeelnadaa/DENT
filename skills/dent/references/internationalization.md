# Internationalization (i18n) and Localization (l10n)

Design so the product works in any language, script, region and format — even if it launches in one language first. Retrofitting is expensive.

---

## 1. Text expansion and contraction
- Translations from English are often longer: roughly **+30–40%** on average for languages like German, French, Finnish, Russian; **short strings can grow 100–300%** ("OK" → "Rendben").
- CJK languages (Chinese, Japanese, Korean) are often **shorter in width** but need more line height and larger minimum sizes.
- Design rules:
  - No fixed-width buttons/tabs for text; let them grow; allow wrapping to 2 lines where acceptable.
  - Avoid text in tight pills/badges without room.
  - Test with **pseudo-localization** (e.g. "[Ŝéţţîñĝš ļļļļļ]" — accented + 40% longer) to find truncation.
  - Truncate only with tooltip/full text available, never for critical info.
- Never build sentences by concatenating fragments ("You have " + n + " items") — grammar differs. Use full translatable strings with placeholders and **plural rules** (ICU MessageFormat: one/few/many/other).
- Avoid text in images; if unavoidable, keep source files localizable.

## 2. Right-to-left (RTL) languages
Arabic, Hebrew, Persian (Farsi), Urdu are written right-to-left.
- Set `dir="rtl"` and `lang` on `<html>` (or per element for mixed content).
- **Mirror the layout:** navigation, alignment, progress direction, back/forward arrows, sidebar side, text alignment, icons with direction (arrows, send, reply).
- **Don't mirror:** logos, media playback controls (play ▶ stays), clocks, charts' time axes (often stay LTR in many locales — check), numbers (digits are LTR even in RTL text), checkmarks, phone numbers, code.
- Use **CSS logical properties**: `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`, `border-start-start-radius`. Then RTL works almost automatically.
- Flexbox/grid follow `dir` automatically; avoid `left/right` hardcoding.
- Bidirectional text (Arabic text with English names/numbers) needs `<bdi>` or `unicode-bidi` handling in user-generated content.
- Fonts: Arabic needs fonts with proper shaping (Noto Naskh/Sans Arabic, IBM Plex Sans Arabic, Cairo, Tajawal); typically larger size/line height than Latin.

## 3. Scripts and fonts
- Choose fonts that support all needed scripts, or define per-script fallbacks in the font stack.
- **Google Noto** family covers almost every script; pair carefully with the brand font (match x-height/weight).
- **Indic scripts** (Devanagari for Hindi/Marathi, Bengali, Tamil, Telugu, Kannada, Malayalam, Gujarati, Gurmukhi…):
  - Need complex text shaping (conjuncts, vowel signs above/below). Use proper fonts (Noto Sans Devanagari/Tamil/…, Mukta, Hind, Poppins (Devanagari), Baloo 2, Tiro, Anek family).
  - Need **more line height** (≈ 1.6–1.8) because of marks above and below the line; don't clip with tight `line-height` or fixed heights.
  - Often set slightly larger than Latin for equal readability.
  - Don't apply letter-spacing (breaks conjuncts) or uppercase transforms (not applicable).
  - Users often mix English and Indian languages (Hinglish/code-switching) — support both scripts in inputs and search, and transliteration where useful.
- **CJK:** large character sets (font files are big — subset or use system fonts); line height ~1.7; no italics (use weight/color for emphasis); line breaking rules differ (`word-break`/`line-break` CSS); vertical text possible in Japanese.
- **Thai, Lao, Khmer, Myanmar:** no spaces between words — line breaking needs dictionaries (browsers handle it; avoid manual hyphenation); tall diacritics need line height.
- Avoid `text-transform: uppercase` for non-Latin; avoid fake bold/italic.

## 4. Formats (locale-aware)
Always use locale APIs (`Intl.NumberFormat`, `Intl.DateTimeFormat`, ICU) — never hand-format.
- **Numbers:** 1,234,567.89 (US/UK) · 1.234.567,89 (DE) · 1 234 567,89 (FR) · **12,34,567.89 (India — lakh/crore grouping)**.
- **Currency:** symbol position and spacing vary (₹1,00,000 · $100,000 · 100.000 € · ¥100,000). Show currency codes when ambiguous ($ = USD/CAD/AUD…).
- **Dates:** 03/04/2025 is ambiguous (March 4 US vs 3 April most countries). Prefer "3 Apr 2025" or locale formats; ISO (2025-04-03) for technical contexts.
- **Times:** 12h vs 24h by locale; time zones displayed explicitly for scheduling.
- **Week start:** Sunday (US, India commonly), Monday (Europe, ISO), Saturday (parts of Middle East).
- **Calendars:** Gregorian plus others in some locales (Hijri, Persian, Buddhist, Indian national calendar) — support where needed.
- **Names:** don't force first/last name split; support single names, long names, non-Latin characters; family name first in some cultures.
- **Addresses:** formats vary greatly; use country-specific forms or a flexible single field + autocomplete; don't require ZIP/state for countries without them (Indian PIN code is 6 digits).
- **Phone numbers:** country code selector, store in E.164; accept spaces and dashes.
- **Units:** metric vs imperial; paper sizes (A4 vs Letter).
- **Sorting/collation:** alphabetical order differs by language; use locale-aware sorting.

## 5. Culture and content
- Colors, symbols, gestures and imagery carry different meanings (see color.md Part 1 §3). Hand gestures (thumbs up, OK sign) can be offensive in some regions.
- Use diverse, locally relevant imagery; avoid region-specific metaphors (mailboxes, baseball idioms).
- Formality levels differ (tu/vous, du/Sie, aap/tum in Hindi): decide per language in the voice guide.
- Legal/regional requirements: cookie consent (EU), data residency, accessibility laws, payment methods (UPI in India, iDEAL in NL, Pix in Brazil, cards vs wallets).

## 6. Language selection UX
- Detect from browser/OS but **let users choose**; remember the choice.
- Show language names in their own language ("Deutsch", "हिन्दी", "日本語"), not flags (flags = countries, not languages).
- Keep the switcher in a consistent place (header or footer); separate language from region/currency when needed.
- URLs per locale (`/de/`, `de.example.com`) with `hreflang` for SEO.

## 7. Engineering checklist
- [ ] All strings externalized; no hardcoded UI text.
- [ ] ICU MessageFormat for plurals/gender; placeholders, not concatenation.
- [ ] UTF-8 everywhere; fonts cover scripts.
- [ ] Logical CSS properties; tested in RTL.
- [ ] Locale-aware number/date/currency formatting and sorting.
- [ ] Layouts tested with pseudo-localization and the longest real language.
- [ ] Line heights generous enough for Indic/Thai/Arabic scripts.
- [ ] Inputs accept non-Latin characters (names, addresses, search).
