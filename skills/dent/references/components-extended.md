# Components — Extended Library

`foundations-and-components.md` §4 defines the foundation components. This file specs the next tier, using the same shared control tokens (§4.1) and the spec template (§4.21). Everything here inherits: control height/radius/font, focus ring, state color formula, hit areas, and the "define once, reuse everywhere" rule. Keyboard/ARIA details: `accessibility.md` §4. On the web, implement each component the way its Modern Web Guidance guide says (`modern-web-guidance.md` §4) and apply these specs on top.

---

## 1. Accordion / disclosure
- Header row height ≥ 48px; whole row is the button; chevron 16–20px on the trailing side, rotates 180° (or 90°) in 150–250ms.
- Content padding = card padding. Web: `<details>`/`<summary>`, height animated on `::details-content` with `interpolate-size: allow-keywords`, not `max-height` hacks; no headings inside `summary` and no arrow-key handling (`mwg:accordion`).
- Default: multiple sections may be open. Avoid exclusive (single-open) accordions; use `<details name>` only when sections are mutually exclusive steps (`mwg:accordion`).
- Don't hide content users need to compare or scan (prices, specs) in accordions on desktop.

## 2. Breadcrumbs
- Caption/label text, secondary color; separator `/` or `›` in the disabled text color, 8px each side.
- Current page last, not a link, primary text color, `aria-current="page"`.
- Collapse middle levels into "…" menu when more than ~4 levels or on mobile; on mobile prefer a single "← Parent" back link.

## 3. Pagination
- Prev / page numbers / Next; buttons = control height (ghost style), current page = tinted fill + `aria-current`.
- Show first, last, current ±1, ellipsis between: `1 … 4 5 6 … 20`.
- Show the range ("Showing 41–60 of 1,284") and optionally a page-size select.
- Keep the URL in sync (`?page=3`) so position survives back/refresh.

## 4. Stepper / wizard progress
- Use for 3–7 sequential steps (Goal-gradient). Fewer than 3 → no stepper. More than 7 → group into phases.
- Each step: number or check icon (completed), label, state = upcoming / current / complete / error.
- Completed steps are clickable to go back; future steps aren't (unless steps are independent).
- Mobile: compact "Step 2 of 5 · Shipping" + thin progress bar instead of the full row.
- Save progress between steps; never lose input on Back.

## 5. Date and time pickers
- **Always allow typing** the date in a text field (with format hint "DD/MM/YYYY" from locale) **plus** a calendar popover. Typing is faster for known dates (birthdays); the calendar is better for near dates.
- Birthdays / far dates: three fields or typed input, never a calendar starting at today.
- Calendar: 7-column grid, cells ≥ 40px (44 touch), today outlined, selected filled with accent, disabled dates struck/dimmed with reason on hover/focus.
- Ranges: two months side by side on desktop, one on mobile; in-range days tinted; presets ("Last 7 days", "This month") on the side for analytics.
- Week starts per locale (Mon in most of the world, Sun in US). Time: 12/24h per locale; type-in with stepped minutes (5/15) where sensible.
- Show time zone when users in different zones interact (meetings, deadlines).
- Native `<input type="date">` is acceptable for Essential effort and on mobile.

## 6. File upload / dropzone
- Dropzone: dashed 1.5–2px border (≥ 3:1), container radius, icon + "Drag files here or **browse**" (browse is a real button) + accepted types and max size.
- Drag-over state: accent border + tinted background.
- Each file row: icon/thumbnail, name (truncate middle: `annual-rep…2025.pdf`), size, progress bar while uploading, success check / error message + retry, remove (×).
- Validate type/size **before** upload with a specific message ("Max 10 MB — this file is 14.2 MB").
- Allow paste (Ctrl/Cmd+V) for images; keyboard-accessible button path always exists.
- Avatars/images: show crop step with fixed aspect ratio.

## 7. Search field
- Same tokens as text input; leading search icon; clear (×) appears when non-empty; `type="search"`, Enter submits.
- Instant results: debounce 150–300ms, show loading in the field, keep results stable while typing (no flicker).
- Suggestions dropdown: recent searches, top matches grouped by type, highlight matched text (bold), keyboard navigation.
- No results: say what was searched, suggest spelling fixes/filters to remove, offer a path forward.
- Shortcut hint `/` or `⌘K` shown in the field on desktop.

## 8. Command palette (⌘K / Ctrl+K)
- Centered modal (a native `<dialog>`, `mwg:dialog`), width ~560–640px, top offset ~15–20dvh, input at top (no border), results list below, max ~8–10 visible rows.
- Groups (Navigation, Actions, Recent), each row: icon, label, optional description, trailing shortcut hint.
- Fuzzy match; empty query shows recent and suggested commands.
- Enter runs; Esc closes; arrows move; nested commands push a breadcrumb chip in the input; Backspace on empty input goes up a level.
- Every command must also be reachable without the palette.

## 9. Number input / quantity stepper
- Text field + − / + buttons (icon buttons, control height). Buttons disabled at min/max with reason.
- Allow typing; validate on blur; accept locale formats (Postel's Law).
- Hold-to-repeat on +/− for large ranges; arrow keys ±1, Shift+arrow ±10.
- Units as suffix ("kg", "%"); right-align or center digits with tabular figures.

## 10. One-time code (OTP) input
- **One `<input>`**, visually split into 6 cells if the design wants boxes (monospace, `letter-spacing`, a cell background), ≥ 44px tall, tabular, large (20–24px). Never six separate inputs: they break `one-time-code` autofill, paste and screen readers (`mwg:sms-otp-form`).
- `type="text"`, `autocomplete="one-time-code"`, `inputmode="numeric"`, `pattern`, `maxlength`; paste and SMS autofill (WebOTP where supported) fill the whole code; submit with `requestSubmit()`.
- Auto-submit when complete; show resend with countdown ("Resend in 0:24"); say where the code was sent ("Sent to ••• 4821").

## 11. Tag / multi-select input
- Selected values as removable chips inside the field (chip spec `foundations-and-components.md` §4.12); field grows to wrap.
- Typing filters options; Enter adds; Backspace on empty removes last chip (with undo-able behavior); comma/paste splits values for free-form tags.
- Show "+3 more" when collapsed; list all on focus.
- Max selections stated up front if limited.

## 12. Rating input
- 5 stars (or thumbs for binary). Each star target ≥ 44px on touch.
- Implement as a radio group; hover previews; labels for each value ("4 — Good").
- Display ratings with the number and count: ★ 4.6 (1,284 reviews). Never stars alone.

## 13. Carousel
- Use only when items are truly parallel and browsing is the goal (product images, testimonials). Never to hide important content (most users don't advance carousels).
- Peek the next item (10–20% visible) so it's obviously swipeable. Visible prev/next buttons on desktop; position indicator ("3 / 8" or dots ≥ 24px hit area).
- **No auto-advance** by default; if required, ≥ 5s per slide with a pause control (WCAG 2.2.2), pause on hover/focus.
- Use `scroll-snap` for native momentum; keyboard arrows when focused.

## 14. Tree view
- Row height = list row (compact 32–36px allowed in dense pro tools); indent 16–24px per level; chevron toggle + optional icon.
- Guide lines optional (low contrast). Keyboard: arrows to move, Right expands / Left collapses, type-ahead.
- Lazy load deep levels with an inline spinner row.

## 15. Data table — advanced
Builds on `foundations-and-components.md` §4.15.
- **Sorting:** click header; arrow icon shows direction; only one active sort unless multi-sort is needed (Shift+click). `aria-sort`.
- **Selection:** checkbox column (40–48px), header checkbox with indeterminate state; selecting shows a **bulk action bar** (replaces the table toolbar or sticks at the bottom) with count ("12 selected") and actions; "Select all 1,284" link after selecting a page.
- **Filtering:** filter chips above the table showing active filters, each removable, "Clear all".
- **Column controls:** resize handles, show/hide columns menu, pin first column on horizontal scroll, density toggle (compact / default / relaxed).
- **Inline edit:** click-to-edit cells with clear editable affordance on hover; Enter saves, Esc cancels; errors inline.
- **Row actions:** most common 1–2 visible on hover/focus (and always visible on touch), the rest in a "⋯" menu.
- **Empty/loading:** skeleton rows matching column widths; filtered-empty state ("No invoices match 'Overdue' + 'EUR'") with "Clear filters".
- **Mobile:** turn rows into cards with the 3–4 most important fields, or allow horizontal scroll with pinned first column.
- Numbers right-aligned, tabular; dates in one consistent format; truncate long text with tooltip/full value on focus.

## 16. Kanban board
- Columns 272–320px wide, column header with name + count + add button; horizontal scroll with visible scrollbar/peek.
- Cards: compact card spec (padding 12px), title first, max 3–4 metadata items (assignee avatar, due date, label).
- Drag: lift (shadow + 1–2° tilt optional), placeholder shows drop spot, auto-scroll near edges; **keyboard alternative** (move via menu "Move to → Done", or Space to grab + arrows).
- WIP limits shown in header when used; empty column has a drop hint.

## 17. Calendar / scheduler
- Views: day / week / month / agenda (list — the accessible default on mobile).
- Events: colored by calendar/category **plus** a label; time and title visible; overlapping events side by side.
- Current time line (accent, 2px) in day/week views. Drag to create/resize with 15-min snap; click empty slot to create.
- Show time zone; handle all-day events in a separate top row.

## 18. Timeline / activity feed
- Vertical line (1–2px, low contrast) with dot/avatar per item; timestamp relative ("2h ago") with absolute on hover/focus.
- Group by day ("Today", "Yesterday", "Mar 4"). Actor + action + object: "**Priya** moved **Invoice #204** to **Paid**".
- Filters by type/actor for audit-heavy products.

## 19. Rich text editor toolbar
- Group tools: text style | bold/italic/underline | lists | link/media | more. Icon buttons sm/md with tooltips + shortcuts.
- Active formatting = tinted pressed state (`aria-pressed`).
- Prefer floating (selection) toolbar + slash commands ("/") for document editors; fixed toolbar for forms/email.
- Markdown shortcuts (`#`, `-`, `**`) for power users.

## 20. Inline confirmation and popconfirm
- For low-to-medium risk destructive actions in lists, prefer **undo toast** (`modern-layer.md` §7.8), as long as the deleted item can also be restored somewhere permanent (trash, history), since a toast must not be the only place an action lives (`mwg:persistent-toast-notifications`). If confirmation is needed, a small popover anchored to the button ("Delete 'Q3 plan'? [Cancel] [Delete]") beats a full modal.
- High-risk/irreversible (delete workspace, cancel subscription): modal with consequence summary; for the most severe, type-to-confirm the resource name.

## 21. Empty state (component)
- Anatomy: small illustration or icon (optional) → title (what this is) → one line (why it's empty / value) → primary action → optional secondary (import, learn more).
- Types: **first use** (teach + start), **no results** (adjust filters), **cleared** (celebrate inbox zero), **error** (what happened + retry), **no permission** (who to ask).
- Max width ~400px, centered in its container, vertical padding 48–64px.

## 22. Banner / announcement bar
- Full-width bar above the header (site-wide) or inline at top of content (page-level); 40–48px tall; semantic tint + icon + one sentence + optional link/action + dismiss (×) if non-critical.
- Only one global banner at a time; remember dismissal.

## 23. Avatar group, copy field, code block, stat
- **Avatar group:** overlap −8px with a 2px ring in the background color; max 3–5, then "+N" avatar; tooltip/list of names.
- **Copy field:** read-only input + copy button; button morphs to check for ~1.5s and announces "Copied".
- **Code block:** monospace 13–14px, line-height 1.5–1.6, padding 16px, container radius, syntax theme matched to light/dark, copy button top-right, horizontal scroll (no wrap) by default, optional filename tab and line numbers.
- **Stat / KPI:** see `data-visualization.md` §6.

## 24. Color picker
- Swatch grid of preset brand-safe colors first (most users want presets); "Custom" opens a saturation/brightness area + hue slider + hex/RGB input.
- Show contrast warning when the chosen color will be used behind text.

## 25. Range slider (two thumbs)
- Same as slider spec (`foundations-and-components.md` §4.10) with two thumbs; thumbs can't cross; paired number inputs for min/max; show histogram above for price filters if data allows.
