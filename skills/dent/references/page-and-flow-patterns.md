# Page and Flow Patterns

Proven structures for common screens and flows. Each pattern lists **structure** (what goes where, in order), **rules**, and **common mistakes**. Combine with SKILL.md foundations and any chosen aesthetic style — patterns decide structure, styles decide look.

Labels: **[Law]** research-backed · **[Rule]** standard/accessibility · **[Convention]** proven industry practice.

---

## 1. Landing page (marketing)

### Structure (top to bottom)
1. **Navigation** — logo, 3–6 links, one CTA button (same as hero CTA).
2. **Hero** — headline (what it is / outcome for the user, ≤ ~10 words), subheadline (how/for whom, 1–2 lines), **one primary CTA** + optional secondary (e.g. "See how it works"), hero visual (product screenshot/video/real photo — shows the actual thing).
3. **Social proof strip** — customer logos, rating, user count, press.
4. **Problem → solution** — the pain, then how the product solves it.
5. **Features / benefits** — 3–6 items, each benefit-led ("Ship in minutes", not "CI/CD pipeline"). Alternate image/text rows or a bento grid.
6. **How it works** — 3 steps.
7. **Testimonials / case studies** — real names, photos, roles, specific results.
8. **Pricing** (or link to it).
9. **FAQ** — answer objections (price, security, cancellation, setup time).
10. **Final CTA** — repeat the main action with a short reassurance ("Free for 14 days · No credit card").
11. **Footer** — links, legal, contact, social.

### Rules
- **[Law: 5-second test]** A visitor should know what it is, who it's for, and what to do next within ~5 seconds of seeing the hero.
- **[Law: Von Restorff / Hick]** One primary CTA style across the page, same label every time.
- **[Law: social proof]** Specific proof beats generic claims ("Cut onboarding time 42% — Head of Ops, Acme" > "Loved by teams").
- Show the real product early (screenshots, demo video, interactive demo).
- Every section answers one question; heading states the answer.
- Copy: concrete outcomes, user's words, no buzzword soup.

### Common mistakes
- Clever headline that doesn't say what the product does.
- Three generic icon cards ("Fast", "Secure", "Easy") — says nothing.
- Multiple competing CTAs with different labels.
- Stock photos of people pointing at laptops.

---

## 2. Pricing page

### Structure
1. Headline + billing toggle (monthly/annual, show savings "Save 20%").
2. **2–4 plan cards** side by side (stack on mobile with the recommended plan first or clearly marked).
3. Each card: plan name → who it's for (1 line) → price (big, with period and currency) → primary CTA → key features list (most important first, "Everything in X, plus:").
4. Full **feature comparison table** below (sticky header with plan names + CTAs).
5. FAQ (billing, cancellation, refunds, limits), trust (security, guarantees), contact sales for enterprise.

### Rules
- **[Law: center-stage / decoy effects]** People favor the highlighted, middle option; mark one plan "Recommended/Most popular" with a visual emphasis (border, badge, filled CTA). Only one.
- Show the **total cost clearly**; no hidden fees (unexpected costs are a leading cause of checkout abandonment — Baymard Institute).
- Use the same feature order in every card so they can be compared (Law of similarity).
- Use checkmarks + text, and "—" for not included; never color alone.
- Free plan or trial clearly explained (what happens at the end).

---

## 3. Dashboard

### Structure
1. **Header:** page title, global filters (date range, workspace/segment), primary action.
2. **KPI row:** 3–5 key metrics, each with value, label, change vs comparison period (▲ 12% vs last month, colored + arrow + text), optional sparkline.
3. **Primary chart(s):** the main trend the user cares about.
4. **Secondary breakdowns:** smaller charts/tables by segment.
5. **Detail table / activity list** with links to drill down.

### Rules
- **[Law: Shneiderman's mantra]** "Overview first, zoom and filter, then details on demand."
- Put the **most important information top-left** (scanning starts there in LTR languages).
- Every number has context: comparison, target or trend. A number without context is decoration.
- Limit to what drives a decision; a dashboard answers specific questions ("Are sales on track this month?").
- Consistent time range across all widgets; show it clearly.
- Group related widgets (proximity); align widget heights in rows.
- Design empty, loading (skeletons), partial-data and error states for every widget.
- Make charts clickable to drill into detail.
- See `data-visualization.md` for chart rules.

### Common mistakes
- 12 equal-sized cards with no hierarchy.
- Vanity metrics with no comparison.
- Rainbow colors with no meaning.
- Each widget with a different date range.

---

## 4. Onboarding (first-run experience)

### Rules
- **Time to value:** get users to their first success ("aha moment") as fast as possible. Defer everything that isn't needed for it.
- **Progressive onboarding:** teach features in context when they're first needed, not in a long upfront tour (users skip/forget tours).
- If you use intro screens, max ~3, skippable, with a clear benefit each.
- **Ask only what personalizes the experience** (role, goal) — and use the answer visibly.
- **[Law: goal-gradient, Zeigarnik]** Setup checklists with progress ("3 of 5 done") increase completion; pre-check a first easy item.
- **Permission priming:** explain why before the OS permission dialog; ask at the moment of need.
- **Empty states as onboarding:** every empty screen explains what goes here and offers the first action (template, sample data, import).
- Let users explore before forcing sign-up when possible.

---

## 5. Authentication (sign up, log in, reset)

### Sign up
- Minimum fields (often just email + password, or email-only magic link/passkey). Collect profile details later.
- Offer **social/SSO** and **passkeys** where appropriate; email option always available.
- Password: show requirements **before** typing, validate live, **show/hide toggle**, allow paste and password managers (`autocomplete="new-password"`).
- Don't ask to confirm password twice when there's a show toggle.
- Clear legal consent (link to terms), no pre-checked marketing opt-ins.

### Log in
- Email + password on one screen (or identifier-first for SSO detection).
- `autocomplete="username"` / `"current-password"`; "Forgot password?" next to the password field.
- **[Rule: security UX]** Error message shouldn't reveal whether the account exists: "Email or password is incorrect."
- "Stay signed in" option where appropriate.
- One-time codes: `autocomplete="one-time-code"`, numeric keyboard, auto-advance, paste whole code, resend with countdown.

### Reset / recovery
- One field (email), same confirmation message regardless of account existence, link expiry explained, new password screen with same rules as sign up.

---

## 6. Forms (general)

### Proven rules
- **[Law]** **Single-column** forms are completed faster and with fewer errors than multi-column (CXL/Baymard research); exceptions: short related pairs (City + ZIP, First + Last name).
- **[Law]** **Top-aligned labels** give the fastest completion (eye-tracking studies, Penzo); left-aligned labels for long forms where scanning labels matters on desktop.
- **[Law]** **Inline validation** (after the user leaves a field, not while typing the first characters) increased success rates and reduced errors and completion time in Wroblewski's study.
- **[Law: Hick, Tesler]** Remove every field you don't truly need; mark optional fields; use smart defaults and autofill.
- Group related fields with headings (Gestalt proximity/common region).
- Field width suggests expected input length (ZIP short, address long).
- Use the right control: ≤ 5 options → radio buttons; many → select/combobox; yes/no → checkbox/toggle; dates → date picker + typing allowed.
- **[Law: Postel]** Accept flexible input (spaces in card numbers, various phone formats) and format it for the user.
- Errors: summary at top for long forms (with links to fields) + message at each field, focus moves to first error.
- Primary button labeled with the outcome ("Create account"), left-aligned with fields (on web), disabled state only if you also explain why — prefer enabled + validation on submit.
- Multi-step forms: show steps and progress, save progress, allow going back without losing data.
- Never clear the form on error.

---

## 7. E-commerce: product page, cart, checkout

### Product page
- Gallery (multiple images, zoom, video), title, price (with any discount shown clearly), key variants (size/color as visible options, not dropdown, when few), stock/delivery estimate, **Add to cart** as primary (sticky on mobile), reviews summary near title, details/specs, shipping & returns info, reviews.

### Cart
- Item list with image, name, variant, quantity stepper, remove, price; **order summary** with subtotal, shipping estimate, taxes, total; primary "Checkout"; continue shopping link.

### Checkout (Baymard Institute large-scale research)
- **Guest checkout** prominently offered — forced account creation is a major abandonment reason.
- **Show total cost early** — unexpected extra costs (shipping, taxes, fees) is among the top reasons for abandonment.
- Fewer fields: combine name into one field where possible, hide "Address line 2" behind a link, auto-detect city/state from ZIP, use address autocomplete.
- Linear steps (shipping → payment → review) with a progress indicator; order summary visible throughout.
- Trust signals near payment (security badges, accepted cards, return policy).
- Payment: wallet options (Apple Pay/Google Pay/UPI etc. per market), card fields with correct keyboards and autofill.
- Clear confirmation page: order number, what happens next, delivery estimate, email sent.

---

## 8. Settings

- Group into categories (Account, Notifications, Privacy, Appearance, Billing…). Use search when there are many settings.
- Each setting: label, short description of effect, control.
- **Toggles apply immediately** (show confirmation toast if needed); text/form settings use explicit Save (sticky save bar showing "Unsaved changes").
- Put destructive actions (delete account, leave workspace) at the bottom in a separated **danger zone**, with confirmation that requires deliberate action (type the name) for irreversible ones.
- Show current values in list rows on mobile ("Language — English ›").

---

## 9. Search and filtering

- Search box visible and wide where search is a key task; placeholder shows what can be searched.
- **Autocomplete/suggestions** after 1–2 characters; show recent searches; keyboard navigable.
- Tolerate typos and synonyms.
- Results: show count, highlight matched terms, sort options, clear relevance.
- **Faceted filters** (left sidebar on desktop, bottom sheet on mobile) with counts per option; applied filters shown as removable chips + "Clear all".
- Filter results update instantly on desktop; on mobile, "Show 24 results" button applies.
- **No-results state:** say so clearly, show the query, suggest fixes (spelling, fewer filters), offer popular items.
- Keep the query and filters in the URL.

---

## 10. Lists, feeds and long content

- **Pagination** for goal-oriented finding (search results, catalogs) — users can return to a position.
- **"Load more" button** as a middle ground (keeps footer reachable).
- **Infinite scroll** only for exploratory feeds (social, inspiration); never when there's an important footer, and preserve scroll position on back navigation.
- Sorting controls visible; default sort stated.
- Bulk actions appear when items are selected (contextual toolbar with count: "3 selected").

---

## 11. Detail pages (item, profile, record)

- Header: title, key status/metadata, primary action(s).
- Main content in order of importance; secondary info in a side panel on desktop, below on mobile.
- Related items / activity history at the bottom.
- Edit in place (inline) or via a clear Edit mode — not both inconsistently.
- Breadcrumb or back link to the list, preserving the list's filters and scroll position.

---

## 12. Empty, error and system states

**Empty states** (three kinds):
1. **First use:** explain what will appear here + primary action + optional illustration or sample/template.
2. **User cleared** (inbox zero): positive confirmation.
3. **No results:** explain why + how to fix (clear filters).

**Error states:**
- Inline field errors (see forms).
- Page/section errors: what happened in plain language + what to do (Retry button) + keep the rest of the page working.
- **404 page:** say it plainly, offer search, link home and to popular pages; keep navigation.
- **Offline:** show cached content, indicate offline status, queue actions and sync later.

**Loading states** (by duration, Nielsen response-time limits):
- < 1s: no indicator needed (avoid flicker; delay spinners ~300ms).
- 1–10s: skeleton screens (content shape) or spinner for small regions.
- > 10s: progress bar with percentage/time estimate, allow background work and cancel.

---

## 13. Navigation patterns

| Pattern | Use when | Notes |
|---|---|---|
| Bottom tab bar (mobile) | 3–5 top-level sections | Always visible, icon + label |
| Top nav bar (web) | 4–7 top-level sections | Collapse on mobile |
| Sidebar | Apps with many sections, workspaces | Collapsible; groups with headings |
| Navigation rail | Tablets/medium widths | Icons + labels, vertical |
| Hamburger/drawer | Secondary navigation, or > 5 sections on mobile | Discoverability drops when hidden [Law] |
| Tabs | Switch between views of the same object | Not for navigation between unrelated pages |
| Breadcrumbs | Deep hierarchies (3+ levels) | Supplement, never replace main nav |
| Mega menu | Large sites with many categories | Grouped, with headings, hover delay + click support |
| Command palette | Power users, many actions | Supplement to visible navigation |

Rule: navigation structure follows the **user's mental model** (validate with card sorting / tree testing when possible), not the company's org chart.

---

## 14. Modals vs pages vs inline

- **Inline** (expand in place): small edits, quick details — keeps context.
- **Popover/menu:** a few options tied to one element.
- **Modal dialog:** short focused task or decision that blocks progress (confirm delete, quick create). Not for long forms or content that needs to be shared/bookmarked.
- **Drawer/side panel:** view/edit details while keeping the list visible.
- **Full page:** complex tasks, long forms, anything that deserves a URL.
- Never stack modals on modals.

---

## 15. Notifications and messaging

- **Toast/snackbar:** confirmation of a completed action, with Undo when reversible.
- **Inline banner:** persistent info about the current page (trial ending, maintenance).
- **Badge:** count of new items; clear it when seen.
- **Notification center:** history of events, grouped by time/type, mark as read.
- **Push/email:** only for things users asked for or truly need; let them control frequency per type.

---

## 16. AI, chat and agent interfaces

### Chat
- Input at the bottom, auto-growing, with clear send button and keyboard shortcut (Enter to send, Shift+Enter newline on desktop).
- **Show state:** thinking/working indicator, streaming text, which tools/sources are being used.
- **Stop** button while generating; **regenerate/edit** after.
- **Sources/citations** inline and expandable; clear uncertainty language.
- Suggested prompts on the empty state.
- Make outputs actionable: copy, insert, export, retry with changes.
- Keep conversation history findable (sidebar with search, rename, delete).

### Beyond chat — principles and patterns
#### Principles (drawing on Google PAIR, Microsoft HAX guidelines for human-AI interaction)
1. **Set expectations:** make clear what the AI can and can't do; show examples of good requests.
2. **Show uncertainty and sources:** citations, confidence cues, "check important details".
3. **Keep humans in control:** easy to stop, undo, edit, approve, or override; confirm before consequential actions (sending, buying, deleting, posting).
4. **Make state visible:** thinking, searching, using tools, waiting for approval, done, failed.
5. **Efficient correction:** edit the prompt, regenerate, refine with follow-ups, give feedback (👍/👎 with reason).
6. **Explain when useful:** why a recommendation was made; what data was used.
7. **Remember and forget transparently:** show what the system remembers; let users view/edit/delete it.
8. **Fail gracefully:** helpful error messages, fallbacks, hand-off to a human.
9. **Respect privacy:** clear data use; opt-in for training/sharing.

#### Patterns
- **Inline AI (copilot):** suggestions appear in context (ghost text, side panel, slash commands), accept with Tab/Enter, dismiss easily; diff view for changes ("Accept / Reject" per change).
- **Agents (multi-step tasks):** show a **plan** before acting (editable), a **progress list** of steps with status, **approval checkpoints** for risky actions, logs/trace of what was done, ability to pause/resume/cancel, and a final **summary of results** with links.
- **Generative output:** multiple variations to choose from; refine controls (tone, length, style); version history.
- **Prompt input:** suggestions/templates, attachments, mode selectors, character/context indicators.
- **Labels:** mark AI-generated content where relevant.
- **Latency:** stream partial results; skeletons; time estimates for long tasks; let users leave and get notified.

---

## 17. Mobile-specific patterns

- **Bottom sheets** for actions and filters (thumb-reachable), with drag handle and clear close.
- **Sticky bottom action bar** for the primary action on long screens (Fitts's Law).
- **Pull to refresh** on feeds/lists.
- **Swipe actions** on rows (with visible alternatives).
- **Floating action button** for one primary creation action (Android).
- Keyboard-aware layouts: the focused field and submit button stay visible above the keyboard; correct keyboard types.
