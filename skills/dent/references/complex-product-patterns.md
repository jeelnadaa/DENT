# Complex Product Patterns and Content Pages

`page-and-flow-patterns.md` covers the common pages and flows. This file covers what real, grown-up products need once they have teams, money, permissions and history — plus the content and marketing pages that are often forgotten.

---

# Part 1 — Product patterns

## 1. Workspaces, teams and accounts (multi-tenancy)
- **Workspace switcher** at the top of the sidebar (avatar/logo + name + chevron). Shows current workspace always; list with search when > ~7; "Create workspace" at the bottom.
- Make the current workspace **visually unmistakable** when actions affect a whole org (e.g. workspace color/logo in the header). Users destroy data in the wrong tenant otherwise.
- Personal vs team spaces are labeled differently; moving items between them is explicit.
- Switching keeps the user on the equivalent page if it exists, otherwise the workspace home.

## 2. Roles and permissions
- Prefer **a few named roles** (Owner, Admin, Member, Viewer/Guest) with a plain-language description each, over a giant checkbox matrix. Offer custom roles only for enterprise tiers.
- Show a **role comparison table** when inviting/changing roles.
- **Hidden vs disabled:** hide features the user can never access; **disable with a reason** ("Only admins can delete projects — ask Priya") for things they might get access to. Never a silent dead button.
- "Request access" flows for blocked pages: who owns it, one-click request, status.
- Invites: email list (paste many), role select, optional message, pending invites list with resend/revoke, expiry.
- Guarded actions (transfer ownership, delete workspace): re-authentication + type-to-confirm.

## 3. Billing, plans and subscriptions
- **Billing page:** current plan, price, renewal date, seats/usage with progress bars, payment method (brand + last 4), invoices table with download, billing email, tax IDs.
- **Usage limits:** warn at ~80% and 100% in-product before blocking; explain what happens at the limit (hard stop vs overage).
- **Upgrade:** contextual (at the limit or on a locked feature) with the exact benefit; show prorated cost before confirming.
- **Downgrade/cancel:** as easy as signing up [Rule in many jurisdictions; see persuasion-and-ethics.md]. One optional "why" question and one optional retention offer, never a maze. Show what will be lost and when access ends. Offer pause and export.
- **Failed payments:** non-blocking banner + email, grace period, clear "Update payment method" action.
- Trials: days remaining visible but calm; no surprise charges — remind before the trial converts.

## 4. Notification center (in-app)
- Bell icon with unread badge (count up to 99+). Panel/popover ~360–420px wide or a full page.
- Tabs or filters: All / Mentions / Unread. Each item: actor avatar, sentence, object, time, unread dot; click goes to the exact object.
- Mark as read on open, "Mark all as read"; per-item "⋯" (mute thread, turn off this type).
- **Notification settings** matrix: event types × channels (in-app, email, push, Slack), with sensible defaults; digest options (instant / daily / weekly).
- Respect quiet hours and batching; never use notifications as marketing without consent.

## 5. Activity log and audit trail
- Readable sentences ("Ana changed **Status** from *Draft* to *Published*"), actor, timestamp (absolute on hover), IP/device for security-relevant events.
- Filters: actor, action type, object, date range; export (CSV) for admins/compliance.
- Diff view for content changes; link to restore a version where possible.

## 6. Version history, undo and drafts
- **Autosave** with visible status ("Saved · 2s ago", "Saving…", "Offline — changes will sync"). Never require a Save button for documents unless the domain expects it (forms, settings with dependencies).
- Undo/redo (⌘Z / ⌘⇧Z) for every editing action; multi-step undo in editors.
- Version history panel: named versions + automatic snapshots, preview, compare, restore (restoring creates a new version — never destroys history).
- Unsaved changes on navigation: warn only when changes would actually be lost.

## 7. Collaboration and multiplayer
- **Presence:** avatars of people currently viewing (top-right), colored cursors/selections with name labels, "Ana is typing…".
- **Comments:** anchored to an object or text range; threads with replies, mentions (@name with autocomplete), reactions, resolve/reopen, filter open/resolved.
- **Mentions** notify; show who will be notified before sending when access differs ("Raj doesn't have access — share?").
- **Sharing dialog:** people with access + roles, invite field, general access (Restricted / Anyone in org / Anyone with link) with plain consequences, copy link.
- **Conflicts:** prefer real-time merge (CRDT/OT) so conflicts don't happen; otherwise show both versions and let the user choose.

## 8. Offline, sync and real-time
- Show connectivity status only when it matters (offline banner; subtle sync indicator).
- Queue actions offline with a pending marker; sync when back; report failures per item with retry.
- Real-time updates: animate new items in gently; **don't move content under the user's cursor** — show "3 new items" pill instead of reflowing a list they're reading.
- Stale data: show "Updated 5 min ago" + refresh on dashboards.

## 9. Bulk actions and long-running jobs
- Select → bulk bar with count and actions (components-extended.md §15).
- Destructive bulk actions summarize scope: "Delete 128 contacts? This also removes their 312 notes."
- Long jobs (imports, exports, bulk edits): run in the background with a progress indicator (toast or jobs panel), allow leaving the page, notify on completion, show a result summary ("1,204 imported · 12 skipped — view errors").

## 10. Import and export
- **Import wizard:** upload → **column mapping** (auto-matched with confidence, editable) → preview with validation errors highlighted per row → import → summary with downloadable error report.
- Provide a template file. Accept common formats (CSV, XLSX, JSON) and varied date/number formats (Postel's Law).
- **Export:** format choice, scope (current filter vs all), columns; deliver via download or email for large exports.

## 11. Admin, back-office and CRUD
- List → detail → edit is the backbone. Make lists fast to scan (tables), detail pages read-first, edit in place or side panel.
- **Side panel (drawer) editing** keeps list context; full page for complex records.
- Dangerous admin actions grouped in a "Danger zone" section at the bottom of settings, red outlined, each with explanation.
- Internal tools may use Essential effort, but never skip states, confirmation of destructive actions, or accessibility.

## 12. Power users and keyboard-first
- Shortcuts for the top 10 actions; single-key shortcuts only when focus isn't in a text field; show them in tooltips and menus.
- `?` opens a shortcut sheet. Command palette (components-extended.md §8).
- Multi-select with Shift/⌘-click; j/k navigation in lists; Esc always backs out one level.
- Saved views (filters + sort + columns) shareable by URL.

## 13. Security, privacy and account UX
- **Sign-in methods:** passkeys first where supported, then email magic link / password + 2FA, SSO for business. Allow password managers and paste (WCAG 3.3.8).
- **2FA setup:** QR + manual key, verify a code, **show recovery codes once** with copy/download, and require acknowledgment.
- **Sessions & devices:** list active sessions (device, location, last active), "Sign out of other sessions".
- **Sensitive actions:** re-authenticate (step-up) for email/password changes, payouts, deleting accounts.
- **Account deletion:** self-serve, explain what is deleted and when, offer data export first, grace period if offered, confirmation email. (Required by app stores for apps with account creation, and by privacy laws in many markets.)
- **Data export** ("Download your data") in a clear place.
- **Privacy settings:** plain language, granular toggles, defaults that favor privacy; explain trade-offs at the moment of choice.
- **OS permission requests (camera, location, notifications, contacts):** ask **in context**, when the feature needs it, with a pre-prompt screen explaining the benefit ("Allow location to show stores near you"). If denied, keep the feature usable in a reduced form and show how to enable later. Never request all permissions at launch.

## 14. Trust and safety (UGC, social, marketplaces)
- Report and block reachable from every user-generated item and profile (⋯ menu); reporting flow: reason → optional details → confirmation of what happens next.
- Blocking is silent to the blocked person; muting is softer.
- Content warnings/blur for sensitive media with tap-to-reveal; safety center link.
- Verified badges explain what was verified.

## 15. In-product help and education
- Contextual help: "?" tooltips next to complex fields, inline examples, empty-state guidance — before product tours.
- **Tours/coachmarks:** max 3–5 steps, skippable, triggered by the relevant feature (not all on first login), never blocking real work.
- **Checklists** for setup (Zeigarnik, Goal-gradient): 3–6 items, each completable, dismissible.
- Help center/search and "Contact support" reachable from a stable place (help menu or account menu).
- "What's new": changelog popover or badge; short, visual, dismissible.

## 16. Feature states: beta, locked, coming soon
- Badges: "Beta" (works, may change), "New" (time-limited, ~2–4 weeks), "Pro" / lock icon (plan-gated with upgrade path).
- Don't show "coming soon" items in primary navigation; use a roadmap/changelog instead.

---

# Part 2 — Content and marketing pages

## 17. Blog / article page
- Reading column 60–75 characters (~680–720px), body 17–20px, line-height 1.6–1.7, generous paragraph spacing.
- Header: category, title (balanced wrap), dek/subtitle, author + date + reading time, hero image (optional).
- Table of contents (sticky on desktop) for long posts; anchored headings with copy-link.
- Pull quotes, figures with captions, code blocks, callouts — all from tokens.
- End: author bio, related posts (3), newsletter signup (one, not three).

## 18. Documentation site
- Three columns on desktop: nav tree (left, ~240–280px) · content (~720px) · on-this-page TOC (right).
- Search (⌘K) with keyboard navigation is the main navigation for experienced users.
- Version and language selectors in the header; "Edit this page" and "Last updated".
- Code blocks with copy, language tabs (npm / pnpm / yarn), and runnable examples where possible.
- Callouts: Note, Tip, Warning, Danger — semantic colors + icon + label.
- Previous/next links at the bottom; feedback ("Was this helpful?").

## 19. Changelog / release notes
- Reverse chronological, dated entries; each with a short title, category tags (New, Improved, Fixed), a visual for big features, and links to docs.
- RSS/email subscribe. Group minor fixes in a compact list.

## 20. About, team and careers
- About: mission in one sentence, story, real team photos, values shown through specifics (not a list of adjectives).
- Careers: why work here (concrete benefits), open roles list with filters (team, location, remote), salary ranges where required or possible, hiring process steps.

## 21. Contact and support
- Choose the channel for them: sales vs support vs press. Short form (name, email, topic, message), expected response time, alternative channels.
- Show business address/legal info where required.

## 22. Error pages (404 / 500 / maintenance)
- 404: say it plainly, keep the full header/nav, offer search and 3–5 popular links; a touch of brand personality is fine.
- 500: apologize, no technical blame on the user, "Try again", status page link.
- Maintenance: what, until when (with time zone), status page.

## 23. Legal pages (privacy, terms, cookies)
- Readable typography (same as articles), table of contents, last-updated date, plain-language summary at the top of each section where possible.
- Never hide these behind accordions only; they must be linkable by section.

## 24. Comparison ("X vs Y") and alternatives pages
- Honest comparison table: features with check/cross **and** text, pricing, who each is better for. Be fair — users verify.
- Migration path and testimonials from switchers.

## 25. Waitlist / coming soon / launch
- One promise sentence, one visual, email field + button, privacy note, what happens next ("We'll email you once when it's live").
- Optional referral position — but no fake scarcity counters.

## 26. Case study / portfolio project
- Structure: context (client, problem, constraints) → role → process highlights (2–4 key decisions with visuals) → outcome with numbers → reflection.
- Big visuals, short text blocks, scannable metrics.
