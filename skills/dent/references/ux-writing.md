# UX Writing — Voice, Tone and Microcopy Library

Words are interface. Good copy is clear first, concise second, and has personality third.

---

## 1. Principles
1. **Clear:** say exactly what happens. Use the user's words, not internal terms.
2. **Concise:** cut filler ("please note that", "in order to", "simply"). Front-load the key words.
3. **Useful:** every piece of text helps the user decide or act.
4. **Consistent:** same term for the same thing everywhere (keep a glossary).
5. **Human:** conversational, active voice, "you" for the user.
6. **Accessible:** plain language; avoid idioms for global audiences; don't rely on visual position ("click the button on the right").

## 2. Voice vs tone
- **Voice** = the product's constant personality (e.g. "friendly, confident, plain-spoken"). Define 3 adjectives + "this, not that" pairs: *Friendly, not silly · Confident, not arrogant · Simple, not dumbed-down*.
- **Tone** = how the voice adapts to the moment:

| Situation | User's state | Tone |
|---|---|---|
| Onboarding / welcome | Curious | Warm, encouraging |
| Routine task | Focused | Neutral, brief |
| Success | Pleased | Positive, brief (celebrate big wins only) |
| Error (user) | Frustrated | Calm, helpful, no blame |
| Error (system) | Annoyed/worried | Apologetic, honest, give a way forward |
| Destructive action | Cautious | Serious, explicit about consequences |
| Money / security / health | Anxious | Precise, reassuring, no jokes |
| Empty state | Unsure | Guiding, motivating |

Never use humor in errors, payments, security or sensitive moments.

## 3. Style rules [Convention]
- **Sentence case** for headings, buttons, labels ("Create new project"), not Title Case or ALL CAPS (easier to read; caps only as a style choice for short labels).
- **Buttons:** verb + object ("Save changes", "Send invoice"). Match the button to the question in dialogs ("Delete project?" → "Delete" / "Cancel", not "Yes"/"No").
- **Links:** describe the destination ("View pricing"), never "click here".
- **Numbers:** numerals ("3 files"), not words; consistent formats.
- **Dates/times:** relative for recent ("2 min ago"), absolute for older/precise ("12 Mar 2026, 14:30").
- **Avoid:** jargon, double negatives, "please" everywhere, exclamation marks in excess, "oops"/"uh-oh" in serious errors, ellipses for drama.
- **Length targets:** button 1–3 words; tooltip ≤ 1 sentence; toast ≤ 1 line; error ≤ 2 short sentences; empty state headline ≤ 6 words + 1–2 sentence body.

## 4. Microcopy library (patterns to adapt)

**Buttons**
- Primary: "Create account", "Start free trial", "Save changes", "Send", "Continue", "Place order", "Publish"
- Secondary: "Cancel", "Back", "Skip for now", "Preview"
- Destructive: "Delete project", "Remove member", "Cancel subscription"

**Errors** — what happened + why (if useful) + how to fix:
- Field: "Enter an email address like name@example.com" · "Password needs at least 8 characters" · "This date is in the past — choose a future date"
- Form: "There are 2 problems with this form" (with links to fields)
- Network: "You're offline. We'll save your changes and sync when you're back."
- Server: "Something went wrong on our side. Your data is safe — try again in a moment." + Retry
- Permission: "You don't have access to this project. Ask the owner, Priya, to invite you."
- Not found (404): "We can't find that page. It may have moved or been deleted." + Search / Home
- Payment: "Your card was declined. Check the details or try another card." (never reveal bank-side specifics that confuse)

**Confirmations (destructive)**
- Title: "Delete 'Q3 Report'?" Body: "This permanently deletes the file and its 12 comments. You can't undo this." Buttons: "Delete file" / "Cancel"

**Success**
- Toast: "Changes saved" · "Invoice sent to arjun@acme.com" · "Project archived. Undo"
- Big milestone: "You've published your first site 🎉 Share it with the world." (emoji only if voice allows)

**Empty states**
- First use: "No projects yet" / "Create your first project to start tracking work." [Create project]
- No results: "No results for 'invioce'" / "Check the spelling or try fewer filters." [Clear filters]
- Cleared: "You're all caught up" / "New notifications will appear here."

**Loading / progress**
- "Loading your dashboard…" · "Uploading 3 of 8 files" · "This can take up to a minute"

**Onboarding**
- "Welcome, Aisha. Let's set up your workspace — it takes about 2 minutes."
- Checklist items as actions: "Invite your team", "Connect your calendar"

**Permissions (pre-prompt)**
- "Allow notifications so we can tell you when your order ships. You can change this anytime in Settings." [Allow] [Not now]

**Forms**
- Labels: nouns ("Email", "Company name"); helper text for format/why ("We'll only use this for receipts").
- Optional marking: "Phone (optional)".
- Password rules shown before typing.

**Notifications**
- Lead with what matters: "Payment received: ₹4,500 from Rohan" not "You have a new notification".

**AI features**
- Be honest about uncertainty: "AI-generated — check important details." Explain what data is used.

## 5. Inclusive language
- Gender-neutral ("they", "team members", "everyone").
- Avoid ableist idioms ("crazy fast", "blind spot", "sanity check" → "very fast", "gap", "quick check").
- Avoid violent/exclusionary tech terms where alternatives exist ("primary/replica", "allowlist/blocklist").
- People-first or identity-first language as the community prefers; ask/research.

## 6. Content design process
1. Write the message for the user's goal in this moment.
2. Draft long, then cut by 30–50%.
3. Read aloud — does it sound like a helpful person?
4. Check consistency with glossary and voice.
5. Test with real users (comprehension, not preference).
