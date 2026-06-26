# Support Guide
## Buyer FAQ · 10 Questions · Airbnb Host Starter Kit

---

## Q1: Where do I start? The number of files is overwhelming.

**Start with `00-QUICK-START-GUIDE.md`.** Read it completely before opening anything else. It gives you 5 specific actions in order of priority. The entire product is navigable from that guide.

If you have a booking arriving this week: go directly to `02-sops-and-checklists/SOP-03-PRE-ARRIVAL-PREP.md`.

If you have no listing yet: go to `02-sops-and-checklists/SOP-01-LISTING-CREATION.md`.

---

## Q2: The financial projections use €98 ADR in Lisbon. My market is different. Do the numbers still apply?

The projections in `01-HOST-BUSINESS-PLAN.md` are illustrative — they show the structure, not the absolute figures.

**How to adapt:**
1. Replace the ADR in Section 2 with your target or current rate
2. The occupancy percentages are calibrated for mid-tier European markets — adjust if your market has significantly higher or lower seasonal variation
3. Fixed costs (insurance, WiFi, noise monitor) are similar across most European markets — adjust if your actual costs differ
4. Variable costs (cleaning at €55/turnover) reflect a professional cleaner in a mid-tier city — adjust for your local rate

The formulas and structure remain valid regardless of your numbers.

---

## Q3: I'm not in Europe. Can I still use this kit?

Yes, with adjustments.

**What works globally without changes:**
- All 10 SOPs
- All 14 message templates
- All tracking dashboards (TAB-01 through TAB-07)
- The Notion workspace
- The Superhost 90-Day Sprint
- The guest portal documents

**What needs adaptation:**
- `06-FINANCIAL-MODEL-GUIDE.md` tax section: replace with your country's specific rules
- `01-HOST-BUSINESS-PLAN.md` financial projections: replace with your market's rates
- `02-PRICING-STRATEGY-PLAYBOOK.md` event calendar: replace with your local events
- `GUEST-04-EMERGENCY-CONTACTS.md`: replace EU emergency numbers with local equivalents

The system structure is universal. The market-specific content is in the financial and tax documents.

---

## Q4: The message templates have [PERSONALISATION VARIABLES] in them. Do I replace these before saving in Airbnb?

Yes. Every [VARIABLE IN SQUARE BRACKETS AND ALL CAPS] must be replaced with your actual data before saving the template in Airbnb Saved Messages.

The most important variables to replace in the message templates:

- [PROPERTY NAME] — your property's name
- [HOST NAME] — your first name
- [HOST PHONE] — your direct phone number
- [ACCESS CODE] — this changes per booking (do not save a static code — leave as [ACCESS CODE] in the template and update when sending)
- [WIFI NETWORK NAME] and [WIFI PASSWORD] — your property's WiFi details
- [CHECK-IN TIME] and [CHECKOUT TIME] — your standard times

For [ACCESS CODE] specifically: this is per-booking, so you update it manually each time you send MSG-03. The template saves with [ACCESS CODE] and you fill it in for each guest.

---

## Q5: The Notion workspace looks complicated. Do I need it?

No. The Notion workspace is optional. The core product works without it:

- Guest and booking management: use the Google Sheets tracking dashboards (TAB-01 through TAB-07) — these cover the same data
- Task management: your existing task system (Trello, paper, phone reminders) handles the recurring SOPs

The Notion workspace adds value if:
- You want a single place where bookings, guests, tasks, and maintenance are linked
- You access your operations from your phone regularly
- You plan to delegate to a co-host (Notion sharing is cleaner than sharing Google Sheets with edit access)

If you already use Notion and like it: build the workspace. If you don't: skip it. The kit works without it.

---

## Q6: SOP-04 says to give the cleaning team a printed copy. What if my cleaner doesn't read English?

Two options:

1. **Translate the relevant sections.** SOP-04 is structured in simple numbered steps — it translates well into Google Translate for the major European languages. Print the translated version.

2. **Adapt the walkthrough approach.** Go through SOP-04 with your cleaner once in person, demonstrating each step. The written SOP becomes a reminder checklist rather than primary instruction.

The photo confirmation protocol (send 3 photos after each clean) does not require language — it is visual.

---

## Q7: Airbnb has changed something since this kit was published. What do I do?

Check `08-product-admin/VERSION-NOTES.md` first — if there is a v1.1.0, it will address known policy changes.

If the change is not yet addressed: the affected section's principle usually remains valid even if a specific detail has changed. For example, if Airbnb changes its cancellation policy names, the underlying logic of which policy to choose (firm, not flexible, not strict) likely still applies.

For tax changes: verify with a local accountant annually. Tax sections in this kit are clearly marked as subject to annual change.

---

## Q8: I received a negative review and I want to dispute it. What do I do?

See `04-communication-templates/MSG-14-NEGATIVE-REVIEW-RESPONSE.md` — the final section covers the dispute process.

**Short answer:**
1. Respond to the review publicly (do not argue; acknowledge and state what you changed)
2. If the review contains a false factual statement: flag it via Airbnb (Profile → Reviews → Flag review)
3. If the review contains a personal insult or discriminatory content: report it to Airbnb Support for removal consideration

Airbnb does not remove reviews because the host disagrees with them. They remove reviews that violate policy (personal attacks, non-neutral content, extortion). Factual disagreements are not grounds for removal.

See `02-sops-and-checklists/SOP-09-REVIEW-COLLECTION.md` Section 7 for the full process.

---

## Q9: I'm setting up PriceLabs. The default settings look very different from the multipliers in Section 2 of the Pricing Playbook. Which do I use?

Use the multipliers from Section 2 as **overrides**, not as default settings.

**Setup sequence:**
1. Connect PriceLabs to Airbnb
2. Set your base price (your Monday–Thursday low-season rate from Section 1 of the Pricing Playbook)
3. Set minimum and maximum prices
4. Let PriceLabs generate its default day-of-week and seasonal suggestions
5. Compare PriceLabs' suggestions to Section 2's multipliers
6. Override PriceLabs manually for any date where the Section 2 multiplier gives a significantly different result

In most European markets, PriceLabs' defaults will be directionally similar to Section 2's multipliers. The main differences tend to be on specific local events (PriceLabs' event detection is excellent) and on vacancy management (PriceLabs tends to drop prices earlier in the vacancy window than Section 2 recommends).

---

## Q10: I want to use this kit for a second property. Do I need to buy another licence?

Per the licence agreement (`08-product-admin/LICENSE.md`), each licence covers one owner-operator's properties — meaning all properties you personally host. You do not need separate licences for your own second or third property.

If you are sharing this kit with another host (friend, family member, or business partner managing their own separate properties), that would require them to purchase their own licence.

If you are a property manager running STR properties on behalf of clients, each client's property would require their own licence, or you should contact the creator to discuss a team licence.

---

*Support Guide · Airbnb Host Starter Kit · v1.0.0 · June 2026*
