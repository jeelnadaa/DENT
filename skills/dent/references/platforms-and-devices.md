# Platforms and Devices

Read the section for the platform you are designing for. Platform rules sit **between** the core SKILL.md and an aesthetic style: a style can change how things look, but on native platforms it should not break the platform's navigation, gestures or control behavior (Jakob's Law — users bring habits from every other app on that device).

Labels: **[Rule]** platform requirement or accessibility standard · **[Convention]** platform guideline/default · **[Law]** research-backed.

---

## 0. Decisions for every platform

1. **Input method:** touch, mouse + keyboard, pen, remote, voice? This decides target sizes, hover, density.
2. **Screen sizes:** list the smallest and largest you support; design the smallest first.
3. **Context of use:** one hand on the move (mobile), focused desk work (desktop), lean-back (TV).
4. **Platform conventions vs brand:** brand goes into color, type (where allowed), imagery, illustration, motion details. Navigation structure, gestures, system controls (pickers, share sheets, permissions dialogs) stay native.

### Mobile ergonomics [Law]
- Most phone use is one-handed or cradled, and the thumb reaches the **bottom-center** of the screen most easily; the top corners are hardest (Hoober's field studies on how people hold phones).
- Put frequent actions and main navigation at the **bottom**; put rare or destructive actions at the top or behind menus.
- Large phones: avoid important single-tap targets in the top-left/top-right only; offer gestures (swipe back, pull down) or bottom duplicates.

---

## 1. iOS / iPadOS (Apple Human Interface Guidelines)

### Layout and sizing
- **[Rule]** Minimum touch target **44×44pt**.
- **[Rule]** Respect **safe areas** (notch/Dynamic Island, home indicator, rounded corners). Content can extend edge-to-edge behind bars; controls stay inside safe areas.
- **[Convention]** Standard margins: 16pt (compact width), 20pt on larger widths; iPad uses readable content width for text.
- **[Convention]** Support all iPhone sizes and both orientations where sensible; iPad must support Split View / Slide Over / Stage Manager widths (use size classes: compact vs regular).

### Typography — Dynamic Type
- System font **SF Pro** (SF Pro Rounded / New York serif / SF Mono available). Custom fonts are allowed but must scale with Dynamic Type.
- **[Rule]** Support **Dynamic Type** (user-chosen text size, including accessibility sizes). Layouts must reflow, not truncate critical text.
- Default text styles (at default size): Large Title 34 · Title 1 28 · Title 2 22 · Title 3 20 · Headline 17 semibold · **Body 17** · Callout 16 · Subheadline 15 · Footnote 13 · Caption 1 12 · Caption 2 11 (pt).

### Navigation
- **Tab bar** (bottom): 2–5 top-level sections, icon + short label, always visible on top-level screens. Don't use it for actions.
- **Navigation bar** (top): back button (previous screen's title or "Back"), title (Large Title that collapses on scroll for top-level screens), up to ~2 trailing actions.
- **Hierarchical push** for drilling into detail; **[Convention]** swipe from the left edge goes back — never block it.
- **Sheets** for focused, self-contained tasks (compose, edit, filters). Use detents (medium/large). Provide Cancel/Done in the sheet's top bar. Swipe-down dismisses (confirm if there's unsaved input).
- **Full-screen modals** only for immersive tasks (camera, media editing).
- **Sidebar** on iPad for apps with many sections.

### Controls (use native ones)
- Switches (immediate effect), segmented controls (2–5 options), steppers, pickers/date pickers (wheel or inline calendar), context menus (long press with preview), **action sheets** for choices related to an action, **alerts** only for critical info or confirming destructive actions (max 2–3 buttons; destructive button in red, Cancel in its standard position).
- **Swipe actions** on list rows (trailing: delete/archive; leading: mark/flag). Always also available elsewhere (edit mode, context menu).
- Pull-to-refresh on content lists.
- **[Convention]** Grouped "inset" lists for settings.

### Visual and feedback
- System colors adapt to light/dark and increased contrast; if you use custom colors, provide **light, dark and high-contrast** variants.
- **SF Symbols** for icons (match weight to text weight; they scale with Dynamic Type).
- Materials (blur) for bars and overlays; let content show through.
- **Haptics** for confirmations (success, selection change, impact on snapping) — subtle and meaningful, never on every tap.
- Motion: springs, interruptible; respect Reduce Motion (cross-fade instead of zoom/slide) and Reduce Transparency.

### Platform rules that are easy to miss
- **[Rule]** VoiceOver labels on every control; logical order.
- Ask for permissions **in context**, after explaining why (a "pre-permission" screen); never on first launch without context.
- Don't put a hamburger menu as the main navigation — use tab bar.
- Don't add a custom "Back" that behaves differently from the system back.

---

## 2. Android (Material Design 3)

### Layout and sizing
- **[Rule]** Minimum touch target **48×48dp** (visual can be smaller, touch area not).
- **Window size classes:** compact < 600dp (phones), medium 600–839dp (foldables, small tablets), expanded ≥ 840dp (tablets, desktop). Layout changes by class, not by device name.
- **[Convention]** 4dp grid; 16dp margins on compact, 24dp on medium/expanded.
- **Edge-to-edge** by default: draw behind status and navigation bars; pad content with window insets.

### Typography
- Roboto / Roboto Flex by default; custom fonts allowed via the type scale. Use **sp** units so text scales with user font size **[Rule]**.
- Type scale (sp): Display L 57 · M 45 · S 36 · Headline L 32 · M 28 · S 24 · Title L 22 · M 16 · S 14 · Body L 16 · **M 14** · S 12 · Label L 14 · M 12 · S 11.

### Navigation
- **Navigation bar** (bottom) for 3–5 destinations on compact; **navigation rail** on medium; **navigation drawer** (or permanent rail/drawer) on expanded.
- **Top app bar:** small / center-aligned / medium / large (collapses on scroll). Title + up to ~3 actions + overflow menu.
- **[Rule]** System **back** (gesture or button) must always work predictably; support **predictive back** animations. Back closes the topmost thing (sheet, dialog, search) before navigating.
- **FAB** for the single most important constructive action on a screen (create, compose). Not for destructive or minor actions. One per screen.

### Controls
- Buttons: filled (highest emphasis), tonal, elevated, outlined, text.
- Chips: assist, filter, input, suggestion.
- **Snackbars** for brief feedback with optional one action (Undo); **dialogs** for decisions; **bottom sheets** for supplementary content/actions.
- Text fields: filled or outlined (pick one product-wide), with supporting text and error text.
- Switches, checkboxes, radio buttons, sliders, date/time pickers — use Material components.

### Visual and feedback
- **Dynamic color** (Material You): optionally derive the scheme from the user's wallpaper; keep brand color for key moments if needed.
- Tonal elevation (surfaces tinted by primary) rather than heavy shadows.
- Ripple/state layers for touch feedback.
- Material Symbols icons (24dp, consistent fill/weight/grade).
- Motion: container transforms, shared axis, fade through; durations ~200–500ms with emphasized easing.

### Easy to miss
- **[Rule]** TalkBack content descriptions; focus order.
- Support large font scales (up to 200%) without clipping.
- Respect "Remove animations" setting.
- Don't copy iOS patterns (iOS-style back chevron + text, iOS switches, action sheets) into Android apps.

---

## 3. Web (responsive websites and web apps)

### Responsive strategy
- **Mobile-first CSS**: base styles for small screens, add complexity with `min-width` media queries.
- **Breakpoints from content** (where the layout breaks), typical starting set: 480 · 768 · 1024 · 1280 · 1536px.
- Use **fluid** values: `clamp()` for type and spacing, `minmax()`/`auto-fit` grids, **container queries** for components that live in different-width containers.
- **[Rule]** Content reflows at 320 CSS px wide without horizontal scrolling for text (WCAG 1.4.10 Reflow), except data tables/maps.
- **[Rule]** Works at 200% browser zoom.
- Max content width for reading ~65–75ch; for app layouts ~1200–1440px, or full-width for data-heavy tools.

### Reading and scanning [Law]
- Eye-tracking research (Nielsen Norman Group) shows people **scan**, often in an **F-pattern** on text-heavy pages (headings and first words of lines get attention), and in a **layer-cake** pattern when headings are clear. Design for it: meaningful headings, front-loaded words, short paragraphs, bulleted lists.
- Simple visual pages (landing heroes) are often read in a **Z-pattern**: logo top-left → nav top-right → diagonal to content → CTA bottom-right.
- People do scroll — but content at the top still gets the most attention. Put the key message and primary action in the first screen; don't try to cram everything there.

### Navigation
- Top navigation with 4–7 items on desktop; collapse into a menu on mobile.
- **[Law]** Hidden navigation (hamburger) reduces discoverability and use compared with visible navigation (NN/g research). On desktop keep nav visible; on mobile show the 3–5 most important items visibly if possible (bottom bar for web apps, visible tabs).
- Logo links to home. Current page marked. Breadcrumbs for deep hierarchies. Footer with secondary links (contact, legal, sitemap).
- Search visible as a field (not just an icon) when search is a primary task.

### Web-specific rules
- **[Rule]** Semantic HTML: `<button>` for actions, `<a href>` for navigation, `<nav>`, `<main>`, headings in order, `<label for>` on inputs. Skip-to-content link.
- **[Rule]** Visible focus (`:focus-visible`), full keyboard support, no keyboard traps.
- **URLs are UI:** every meaningful state (tab, filter, page, modal with content) should have a shareable URL; Back button works as expected.
- Links open in the same tab by default; new tab only for external tools/docs while in a task (and indicate it).
- Use the right input types (`email`, `tel`, `url`, `number` only for real numbers) and `autocomplete` attributes so browsers/password managers autofill.
- Hover enhancements only under `@media (hover: hover)`.
- Respect `prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast`.

### Performance is design [Law: Doherty threshold, response-time limits]
- Core Web Vitals "good" thresholds: **LCP ≤ 2.5s** (main content visible), **INP ≤ 200ms** (responsiveness), **CLS ≤ 0.1** (layout stability).
- Reserve space for images/ads/embeds (width/height or aspect-ratio). Use modern image formats (AVIF/WebP), responsive `srcset`, lazy-load below the fold.
- Fonts: 1–2 families, subset, `font-display: swap`, preload critical.

### Cookie/consent banners, popups
- Don't cover the main content on first load with modals (newsletter popups hurt experience); if legally required, keep banners compact with equally visible accept/reject choices.

---

## 4. Desktop apps (macOS, Windows, cross-platform like Electron/Tauri)

### General desktop rules
- **Density is higher** than mobile: controls 24–32px tall, list rows 28–36px; pointer targets ≥ 24px **[Rule: WCAG 2.2]**.
- **Keyboard-first:** every frequent command has a shortcut; standard shortcuts must work (Copy/Paste/Undo/Redo/Find/Select all/Save/New/Close/Preferences/Quit).
- **Right-click context menus** on objects with relevant actions.
- **Drag and drop** where it makes sense (files, reordering).
- **Multi-select** (Shift-click range, Ctrl/Cmd-click toggle) in lists and grids.
- **Resizable windows** with a sensible minimum size; layout adapts (collapse sidebar, wrap toolbars). Remember window size/position.
- **Menu bar / app menu** contains all commands (discoverability, recognition over recall).
- Tooltips on all icon-only buttons, including the shortcut ("Bold — ⌘B").
- Undo for almost everything; confirmations only for destructive irreversible actions.
- Don't use mobile patterns blindly (bottom tab bars, huge touch targets, hamburger menus) on desktop.

### macOS
- System font SF Pro; body text 13pt. Window controls (traffic lights) top-left.
- Common layout: **sidebar** (source list) + content + optional inspector; unified **toolbar** with title.
- Vibrancy/materials on sidebars; respect accent color and light/dark.
- Shortcuts use ⌘ (Command). Settings via ⌘, . Sheets attach to windows.
- Native controls: popup buttons, segmented controls, steppers, disclosure triangles.

### Windows (Fluent Design)
- Font Segoe UI Variable; body 14px. Window controls (minimize/maximize/close) top-right.
- Materials: **Mica** (window background tinted by desktop), **Acrylic** (transient surfaces like menus/flyouts).
- Rounded corners: ~4px controls, ~8px windows/flyouts.
- Navigation: NavigationView (left pane or top), command bars.
- Shortcuts use Ctrl; Alt for menu access keys.
- Support Snap Layouts (window snapping) — layouts must work at half/third screen widths.

### Cross-platform desktop (Electron, Tauri, Flutter desktop)
- Keep the brand UI, but **adapt the chrome**: window controls position, shortcut modifier (⌘ vs Ctrl), menu location, font fallback (system-ui stack).
- Use OS-native dialogs for file open/save, notifications and permissions.

---

## 5. Other surfaces and emerging interfaces

- **Tablets:** use the extra space for multi-column (list + detail), not just bigger phone layouts. Support pointer/keyboard on iPad and Android tablets.
- **Email templates:** table-based layout, inline CSS, web-safe fallback fonts (full email design rules: assets-and-marketing-graphics.md Part 2 §6).

### Voice interfaces (VUI)
- Conversation design: short prompts, one question at a time, confirm critical info implicitly ("Booking a table for 4 at 8pm — anything else?") or explicitly for money/irreversible actions.
- Offer **examples** of what to say; handle no-input, no-match and errors gracefully (reprompt differently, then offer help/fallback).
- Keep lists short (≤ 3 options spoken); allow barge-in (interrupting).
- Visual + voice (multimodal): show transcript, options, and results on screen; allow touch fallback.
- Persona: consistent voice and tone; don't pretend to be human.
- Privacy: clear listening indicator; mute option.

### AR / VR / spatial
- Comfort: avoid camera motion the user didn't cause (motion sickness); stable horizon; teleport or smooth-with-vignette locomotion options; maintain ≥ 72–90fps.
- Placement: UI within comfortable field of view (roughly central ~60° horizontal, slightly below eye level), at comfortable distances (~1–3m for panels); avoid placing content too close.
- Targets: larger than 2D (angular size matters); clear hover/gaze feedback; support hands, controllers, gaze+pinch.
- Text: larger, high contrast, sans-serif, on solid/glass panels with backing.
- Spatial audio cues for off-screen events.
- Safety: boundaries, passthrough awareness, session breaks.
- See styles/spatial.md for the visual style.

### Wearables (watch)
- Glanceable: one key piece of information per screen; interactions < ~5 seconds.
- Large text and targets; dark backgrounds (OLED, battery); complications/widgets for at-a-glance data.
- Notifications concise and actionable; haptics as primary feedback.

### Automotive / in-car
- Minimize distraction: limit glance time (~2s per glance, ~12s per task per common guidelines), large targets, high contrast, voice-first for complex tasks, lock out typing while driving, night/day modes.

### Smart TV / 10-foot UI
- Focus-based navigation with remote (clear focus state, predictable D-pad movement), large type, overscan-safe margins (~5%), minimal text input (use phone pairing/QR), rows of content (lean-back browsing).

### Conversational UI in messaging apps (WhatsApp/Slack bots)
- Quick-reply buttons over free text where possible; clear menu/help command; handoff to human; respect platform message templates and limits.

---

## 6. Sound and haptics

Sound and touch feedback can make interactions feel physical and confirm actions — or become annoying fast. Default: **little or none**, used only for meaningful moments.

---

### 6.1 When to use
- **Confirmation** of important actions (payment sent, message sent, task complete).
- **Alerts** that need attention when the user isn't looking (incoming call, timer done, error in background task).
- **Physical feel** of controls (snapping a slider, toggling, pull-to-refresh threshold, picker detents).
- **Brand moments** (app open sound in media apps, a signature success sound) — sparingly.
- **Accessibility** support (audio cues for blind users, haptic cues for deaf users).

### 6.2 When not to use
- Every tap, scroll, or hover.
- Web pages by default (users don't expect sound; autoplay audio is disruptive and restricted by browsers).
- Errors with harsh sounds in routine tasks.
- Situations where users are likely in public/quiet places without opt-in.

### 6.3 Haptics guidelines
- **iOS:** use system feedback generators — selection (light ticks when changing a value), impact (light/medium/heavy/soft/rigid for collisions/snaps), notification (success, warning, error). Match intensity to the visual event.
- **Android:** `HapticFeedbackConstants` (CLOCK_TICK, CONFIRM, REJECT, CONTEXT_CLICK, LONG_PRESS, etc.) via `performHapticFeedback`; prefer predefined effects over custom vibration patterns.
- **Web:** Vibration API (Android browsers only, not iOS Safari) — rarely appropriate.
- Rules: short and crisp, synchronized with the visual change (within a few ms), consistent mapping (same event = same haptic), never long buzzes for UI, respect system haptics settings, provide a setting to turn off in apps where they're frequent.

### 6.4 Sound design guidelines
- **Short:** UI sounds ~50–300ms; notifications ≤ ~1–2s.
- **Soft and pleasant:** avoid harsh high frequencies; mix quieter than media audio.
- **Consistent family:** all sounds from one sonic palette (same instrument/timbre), like an icon set.
- **Meaningful mapping:** rising tones for success/positive, falling for negative/close; distinct sounds for distinct events (don't reuse the success sound for errors).
- **Respect system settings:** silent mode, volume, "reduce sounds"; in-app toggle for sound effects.
- **Never** the only signal — always pair with visual (and ideally haptic) feedback.
- **Formats:** small compressed files (AAC/OGG/MP3), preload short UI sounds to avoid latency.
- **Licensing:** use licensed or original sounds.

### 6.5 Multisensory consistency
Define in DESIGN.md: event → visual feedback → haptic → sound. Example:
| Event | Visual | Haptic | Sound |
|---|---|---|---|
| Payment success | Checkmark animation | notification.success | Short rising chime |
| Toggle | Thumb slides | selection | none |
| Error on submit | Field highlight + message | notification.error | none |
| Pull to refresh threshold | Spinner appears | impact.light | none |


> AI, chat and agent interface patterns live in `page-and-flow-patterns.md` §16.
