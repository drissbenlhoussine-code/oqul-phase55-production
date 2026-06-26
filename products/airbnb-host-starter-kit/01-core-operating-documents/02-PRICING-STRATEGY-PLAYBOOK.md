# Pricing Strategy Playbook
## Dynamic Pricing System · Seasonal Calendar · Competitor Benchmarking

---

## HOW TO USE THIS DOCUMENT

Set your base rate in Section 1. Apply the multipliers in Section 2 to every future 90-day calendar block. Run the competitor audit in Section 3 every quarter. Never use Airbnb Smart Pricing — it consistently underprices by 15–22% in European mid-tier markets.

---

## SECTION 1 — BASE RATE CALIBRATION

Your base rate is the Monday–Thursday rate in a non-peak, non-event week. Everything else is a multiplier on this number.

**Step 1 — Find your comp set.**

Search Airbnb for properties matching:
- Same neighbourhood or within 1.5 km
- Same capacity (±1 bedroom)
- Similar amenities (WiFi, private bathroom, kitchen access)
- Superhost status preferred (they price more accurately)

Record 5 properties. Note their:
- Monday–Thursday rate
- Saturday rate
- July rate vs. January rate

**Step 2 — Position yourself.**

| Your Review Count | Your Rating | Base Rate vs. Comp Set |
|---|---|---|
| 0–9 reviews | Any | -15% (new listing discount, temporary) |
| 10–24 reviews | Below 4.7 | -10% |
| 10–24 reviews | 4.8+ | At market |
| 25–49 reviews | 4.8+ | +5% |
| 50+ reviews, Superhost | 4.9+ | +10–15% |

New listings: start at -15% below your 5 comparable properties' average. Once you have 10 reviews above 4.8, move to market rate. Once you hit Superhost, apply the +10% premium — it holds because Superhost filters are used by the highest-spending guests.

---

## SECTION 2 — MULTIPLIER SYSTEM

Apply these multipliers to your base rate. When multiple multipliers apply (e.g., weekend + summer + local festival), multiply them together, not add.

*Example: Base €100. Weekend (×1.25) + July (×1.35) = €100 × 1.25 × 1.35 = **€169***

### Day-of-Week Multipliers

| Day | Multiplier | Notes |
|---|---|---|
| Monday | ×1.00 | Base |
| Tuesday | ×1.00 | Base |
| Wednesday | ×1.05 | Mid-week bump |
| Thursday | ×1.10 | Pre-weekend demand starts |
| Friday | ×1.30 | High demand |
| Saturday | ×1.30 | High demand |
| Sunday | ×1.15 | Checkout day, lower but above base |

### Seasonal Multipliers (European Market)

| Period | Multiplier | Months |
|---|---|---|
| Peak summer | ×1.35 | July 1 – August 31 |
| Spring shoulder | ×1.15 | April 1 – June 30 |
| Autumn shoulder | ×1.10 | September 1 – October 31 |
| Low season | ×0.82 | January (excl. New Year) |
| Low season | ×0.88 | November (excl. events) |
| Standard winter | ×1.00 | February, March, December (excl. holidays) |

### Event and Holiday Multipliers

Apply these on top of seasonal and day-of-week multipliers.

| Event Type | Multiplier | Advance Notice to Apply |
|---|---|---|
| Christmas Eve + Christmas Day | ×1.45 | Set by October 1 |
| New Year's Eve + New Year's Day | ×1.50 | Set by October 1 |
| Easter long weekend (4 nights) | ×1.40 | Set by January 1 |
| Major local festival (music, carnival) | ×1.35 | Set 90 days before |
| Large conference or trade fair | ×1.30 | Set 90 days before |
| Public holiday long weekend | ×1.25 | Set 90 days before |
| Local marathon / half marathon | ×1.15 | Set 60 days before |

**How to find local events:** Google "[your city] events calendar 2026" + Eventbrite, Songkick, Ticketmaster for concert dates. Set a quarterly calendar reminder to check Q3 events in April, Q4 events in July, Q1 events in October, Q2 events in January.

### Minimum Stay Rules

| Period | Minimum Stay | Why |
|---|---|---|
| Standard (year-round) | 2 nights | Prevents 1-night turnovers at same cost |
| Peak summer (Jul–Aug) | 3 nights | Reduces turnover frequency, increases ADR |
| Bank holidays | 3 nights | High-value slots; 1-night filler not worth it |
| Christmas + NYE | 4 nights | Blocks prime dates from being split |
| January (vacancy management) | 1 night | Flexibility beats empty nights |

---

## SECTION 3 — VACANCY MANAGEMENT PROTOCOL

An empty night earns €0. The protocol below maximises recovery.

### 7-Day Vacancy Rule

If a date has been open for 7+ days with no booking, apply the following in sequence:

**Day 7 of vacancy (more than 14 days from the open date):**
Apply -10% below your current listed rate. Re-check at Day 14.

**Day 14 of vacancy (still more than 7 days out):**
Apply -20% below base rate. Switch minimum stay to 1 night for the open window.

**Day 7 of vacancy (within 7 days of the open date — last-minute slots):**
Apply -25% below base rate. Last-minute guests have different price sensitivity. €75 is better than €0.

**Day of vacancy (same-day or next-day arrival):**
Price at -30% to -35%. Same-day bookings rarely happen above market rate — price to fill.

### Gap Night Strategy

A "gap night" is a single open night between two bookings. Example: Guest A checks out Thursday, Guest B checks in Saturday — Friday is a gap.

Gap nights earn €0 at standard minimum-stay settings. Options:
1. Drop minimum stay to 1 night for the gap, price at -15%
2. Offer the previous or next guest a 1-night extension at -20% (send via Airbnb message)
3. Leave it open — only accept if it does not create back-to-back turnovers your cleaner cannot cover

---

## SECTION 4 — DYNAMIC PRICING TOOL SETUP

Use one of these tools. Manual pricing is viable with up to 2 properties; above that, use software.

### PriceLabs (Recommended)

**Why:** Most granular control. Separate controls for base price, minimum price, day-of-week adjustments, and event detection. Works with Airbnb, Booking.com, and VRBO.

**Setup sequence:**
1. Connect Airbnb account via API (Settings → Integrations in PriceLabs)
2. Set your base price (your Monday–Thursday low-season rate from Section 1)
3. Set minimum price: never below 60% of base rate (protects against algorithm errors)
4. Set maximum price: 250% of base rate (allows full event capture)
5. Enable Local Events detection — it pulls Eventbrite + concert data automatically
6. Set day-of-week adjustments to match Section 2 multipliers (override PriceLabs defaults)
7. Check the 90-day calendar every Sunday. Manually override any dates where local knowledge beats the algorithm

**Cost:** ~€19/month per listing. ROI positive in the first month for any ADR above €70.

### Wheelhouse (Alternative)

Similar feature set to PriceLabs. Slightly more automated, slightly less granular. Better for hosts who want less manual oversight. Setup is the same sequence as above.

### Beyond (Third Option)

Revenue management focus over raw dynamic pricing. Better for multi-property hosts who care about portfolio-level RevPAN. Higher cost (~€30/month per listing). Only consider if you have 3+ properties.

### Do Not Use Airbnb Smart Pricing

Airbnb Smart Pricing optimises for booking volume, not revenue. It will fill your calendar at rates 15–22% below market during high-demand periods. A full calendar at suppressed rates generates less annual revenue than 80% occupancy at accurate market rates. Turn it off. Use the multiplier system in Section 2 instead.

---

## SECTION 5 — QUARTERLY COMPETITOR ANALYSIS

Run this every quarter. Record in TAB-01 (Revenue Tracker) under the "Market Notes" column.

### Competitor Audit Table

| Comp Property | URL / Airbnb ID | ADR This Quarter (€) | Occupancy (visible) | Review Count | Your Rate vs. Theirs |
|---|---|---|---|---|---|
| Comp 1 | | | | | |
| Comp 2 | | | | | |
| Comp 3 | | | | | |
| Comp 4 | | | | | |
| Comp 5 | | | | | |
| **Your Property** | | | | | |

**How to estimate competitor occupancy:** Check their calendar. Count booked nights (greyed out) over the next 30 days. Express as a percentage. Airbnb does not show occupancy directly, but calendar availability is a reliable proxy.

**What to do with this data:**
- If 3 of 5 comps are priced above you at similar occupancy: raise your base by €5–€10
- If 3 of 5 comps are priced below you and your occupancy trails: drop base by €5–€10 for 30 days
- If your comp set has changed (new Superhost, new property opened near yours): update the table

---

## SECTION 6 — ANNUAL PRICING CALENDAR TEMPLATE

Set these in your calendar every January for the full year. These are non-negotiable date blocks that require manual pricing attention.

| Date Block | Action Required | Multiplier | Set By |
|---|---|---|---|
| Jan 1–7 (post-NYE) | Drop minimum stay to 1 night; apply -15% | ×0.85 | Dec 15 |
| Easter weekend | Block 4 nights; apply event multiplier | ×1.40 | Jan 15 |
| May bank holidays | Check local calendar; apply event if applicable | ×1.25 | Mar 1 |
| July 1 | Switch to peak summer pricing | ×1.35 | Jun 15 |
| August event check | Review local festival calendar | +×1.35 | Jun 15 |
| Sep 1 | Drop from peak to shoulder | ×1.10 | Aug 15 |
| Nov 1 | Drop to low season | ×0.88 | Oct 15 |
| Dec 20–Jan 1 | Christmas + NYE premium | ×1.45–×1.50 | Oct 1 |

**Standing rule:** Never open a new quarter's calendar without reviewing event listings for that quarter. Events found late cannot be priced in advance — every event discovered 90+ days out is priced; every event found 7 days out is likely already at peak demand and probably booked.

---

## SECTION 7 — PRICING DECISION LOG

Record every pricing change you make. If you don't log it, you cannot learn from it.

| Date | Change Made | Reason | Outcome (fill in 30 days later) |
|---|---|---|---|
| | Base rate: €___ → €___ | | |
| | Added event premium: [event] | | |
| | Applied vacancy discount: [date range] | | |
| | Adjusted minimum stay: [period] | | |

After 12 months, review this log before setting next year's rates. The entries where you raised rates and occupancy held are your most important data points.

---

*Last updated: v1.0.0 · Run quarterly competitor audit every January, April, July, October*
