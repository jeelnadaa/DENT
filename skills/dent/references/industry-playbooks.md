# Industry Playbooks

Each industry has its own trust signals, regulations, patterns and user expectations. Read the matching section after choosing the product type. Combine with page-and-flow-patterns.md and a style.

Format: **Users & context · Priorities · Must-have patterns · Visual direction · Watch-outs**.

---

## 1. Fintech, banking, payments, investing
- **Users & context:** anxious about money; need speed for routine tasks and certainty for big ones.
- **Priorities:** trust, clarity, security, accuracy.
- **Must-haves:** balance and recent transactions on home; clear transaction states (pending/completed/failed); confirmation screens before money moves (amount, recipient, fees, arrival time); receipts; biometric login; transaction search/filters; spending insights; strong error handling; 2FA; session timeout warnings; masked account numbers (show last 4).
- **Visual:** Corporate, Minimal, Dark Tech (crypto/trading); blue/green/neutral palettes; tabular numerals; restrained motion; clear charts.
- **Watch-outs:** never ambiguous numbers (sign, currency, decimals); color-blind-safe gains/losses (▲▼ + sign); no dark patterns on fees; regulatory disclosures readable; India: UPI flows (VPA, QR, PIN entry handled by the UPI app), RBI-required disclosures; avoid playful tone in errors.

## 2. Healthcare, medical, wellness
- **Users:** patients (possibly stressed, older, low vision, low health literacy), clinicians (time-pressed, data-dense).
- **Priorities:** safety, clarity, privacy, accessibility.
- **Must-haves:** appointment booking with clear availability; medication schedules; plain-language results with reference ranges; secure messaging; consent flows; emergency info visible; clinician tools with dense but scannable data, critical values highlighted.
- **Visual:** calm palettes (blues, greens, soft neutrals), Organic/Japandi for wellness, Corporate for clinical; large type; high contrast.
- **Watch-outs:** privacy regulations (HIPAA in US, GDPR health data, India's DPDP Act 2023); never alarming colors without explanation; avoid jargon; double-check units/doses; AAA contrast where possible; don't use red/green only for results.

## 3. E-commerce, retail, marketplaces
- **Users:** browsing for inspiration or searching with intent; price- and trust-sensitive.
- **Priorities:** findability, product clarity, trust, fast checkout.
- **Must-haves:** search with autocomplete & filters; product pages (gallery, price, variants, delivery date, returns, reviews); cart & guest checkout (see page-and-flow-patterns.md §7); wishlists; order tracking; ratings with real reviews; size guides; local payment methods (UPI, cards, wallets, COD in India).
- **Visual:** product photography leads; Minimal/Premium Product for premium brands, Playful/Flat for value brands, Luxury for high-end; clear price typography.
- **Watch-outs:** no fake scarcity/urgency (illegal in India/EU); total cost early; mobile-first (most traffic is mobile); fast image loading.

## 4. SaaS / B2B tools / productivity
- **Users:** daily, repetitive use; power users and new users; buyers ≠ users.
- **Priorities:** efficiency, learnability, consistency, data density.
- **Must-haves:** onboarding with sample data/templates; empty states; command palette & shortcuts; tables with sort/filter/bulk actions; settings & permissions/roles; team invites; billing; notifications; activity logs; integrations; search.
- **Visual:** Minimal, Dark Tech, Corporate; compact density option; neutral UI with one accent; strong typography for hierarchy.
- **Watch-outs:** don't sacrifice density for "airy" marketing looks inside the app; keyboard support; performance with large datasets.

## 5. Education / e-learning
- **Users:** students (varying ages), teachers, parents.
- **Priorities:** motivation, clarity, progress, accessibility.
- **Must-haves:** course structure (modules → lessons), progress tracking, streaks/goals (gentle), quizzes with immediate feedback, video with captions/transcripts and speed control, offline download, teacher dashboards, parental controls.
- **Visual:** Playful for kids/language apps, Minimal/Editorial for adults/academic; readable type; illustrations.
- **Watch-outs:** child privacy (COPPA in US, GDPR-K, India DPDP verifiable parental consent for under-18s); no manipulative engagement for kids; low-bandwidth support.

## 6. Government & public services
- **Users:** everyone, including low digital literacy, disabilities, low bandwidth, old devices.
- **Priorities:** accessibility, clarity, trust, inclusivity.
- **Must-haves:** plain language, step-by-step forms ("one thing per page" — GOV.UK pattern), save and resume, clear eligibility checks, multilingual support, offline/assisted alternatives, status tracking.
- **Visual:** Corporate/Minimal, high contrast, simple; follow official design systems (GOV.UK Design System, USWDS, India's GIGW guidelines + UX4G design system).
- **Watch-outs:** legal accessibility requirements; no reliance on JavaScript-heavy UI for core tasks; works on slow networks.

## 7. Travel & hospitality
- **Must-haves:** search (destination, dates, guests) above the fold; date pickers with prices; map + list views; photo-rich listings; transparent total price; flexible cancellation info; booking management; offline tickets/boarding passes; reviews.
- **Visual:** imagery-led; Premium Product, Luxury (hotels), Organic, Minimal.
- **Watch-outs:** drip pricing (fees) is regulated; time zones in itineraries; mobile use while traveling.

## 8. Food & delivery, restaurants
- **Must-haves:** menu with photos, dietary/allergen tags, customization, cart, live order tracking, ETA, reorder, ratings; restaurant sites: menu, hours, location, reservation, call button.
- **Visual:** appetizing photography, warm colors, Playful/Organic/Vintage.
- **Watch-outs:** allergen info prominent and accurate; veg/non-veg marks in India (green/brown symbols) on food items.

## 9. Media, streaming, news, podcasts
- **Must-haves:** content-first layouts, continue watching, recommendations, search, player with captions/speed/quality, downloads, profiles; news: clear headlines, timestamps, author, corrections, readable article layout.
- **Visual:** Dark Tech/cinematic dark for video; Editorial for news; Kinetic Typography for campaigns.
- **Watch-outs:** autoplay controls, ad labeling, reading comfort, avoid infinite engagement traps.

## 10. Social & community
- **Must-haves:** feeds, profiles, posting composer, comments, reactions, notifications, privacy controls, blocking/reporting, moderation tools, onboarding to follow/interest.
- **Watch-outs:** safety and moderation UX, harassment controls, privacy defaults, minors' safety, wellbeing features (time reminders).

## 11. Gaming & gamified apps
- **Must-haves:** clear HUD, readable at a glance, menus navigable by controller/keyboard, settings (accessibility: subtitles, color-blind modes, remapping, difficulty), progression/rewards, store transparency.
- **Visual:** Cyberpunk, Pixel, Synthwave, Playful, custom.
- **Watch-outs:** loot box/odds disclosure, no manipulative monetization for kids, motion sickness options.

## 12. Real estate
- **Must-haves:** search by location/price/type, map, large photo galleries, virtual tours, floor plans, mortgage/EMI calculator, agent contact, saved searches.
- **Visual:** Premium/Luxury or Minimal; photography-led.

## 13. Automotive / mobility / ride-hailing
- **Must-haves:** map-first, clear pickup/drop, price estimate, driver/vehicle info, safety features (share trip, SOS), ratings; in-car UI: huge targets, glanceable, minimal distraction.
- **Watch-outs:** driving-distraction guidelines (glance time ~2s per task), night mode.

## 14. HR / recruiting / job boards
- **Must-haves:** job search with filters, clear salary ranges (where required by law), simple apply (resume parsing), application status, candidate pipelines (kanban), interview scheduling.
- **Watch-outs:** bias-aware forms (don't ask unnecessary personal data), accessibility.

## 15. AI products & developer tools
- **Must-haves:** prompt/chat interfaces (page-and-flow-patterns.md §16), clear model/state indicators, cost/usage visibility, API keys management, docs with code samples & copy buttons, playgrounds, logs.
- **Visual:** Dark Tech, Minimal, Terminal accents; monospace for code.
- **Watch-outs:** transparency about AI limitations, data usage, human override.

## 16. Nonprofit / charity
- **Must-haves:** clear mission, impact stories with real numbers, simple donation flow (preset amounts, recurring option, tax receipt info), volunteer sign-up, transparency (where money goes).
- **Visual:** human photography, Organic/Editorial/Minimal.
- **Watch-outs:** no guilt-trip dark patterns; accessibility.

## 17. Portfolio / personal / agency
- **Must-haves:** work showcase first (case studies: problem → process → result), about, contact; fast loading.
- **Visual:** anything distinctive — Swiss, Brutalism, Kinetic Typography, Editorial, Minimal, Anti-design.
- **Watch-outs:** creativity must not block navigation or readability; show real results.
