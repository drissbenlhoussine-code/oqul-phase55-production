# Pricing Strategy Playbook
## Dynamic Pricing System for Airbnb Hosts

---

## HOW TO USE THIS DOCUMENT

This is not a set-and-forget document. Work through it once to set your base structure, then review it every Sunday for the following two weeks. After that, a weekly 10-minute check is sufficient.

---

## SECTION 1 — PRICING HIERARCHY

Your pricing has four layers. Set them in this order.

### Layer 1: Base Rate (your floor)
The minimum you'll ever charge. Below this, you lose money.

**Base Rate Formula:**
```
Base Rate = (Monthly Fixed Costs ÷ Target Booked Nights) + (Variable Cost Per Night) + (Minimum Profit Per Night)
```

**Example Calculation:**
```
Monthly Fixed Costs:    €258 / 22 target nights = €11.73/night
Variable Cost/Night:    €28 / 2 avg nights per booking = €14.00/night
Minimum Profit/Night:   €40.00
─────────────────────────────────────────────────
Base Rate Floor:        €65.73 → round to €70/night
```

Set your Airbnb minimum price to your Base Rate. Never go below it for promotions.

### Layer 2: Standard Rate (your default weekday price)
Your standard rate targets an occupancy of 65–70% on weekdays.

**Standard Rate Formula:**
```
Standard Rate = Base Rate × 1.35 to 1.50
```

For the example above: €70 × 1.40 = **€98/night** (round to €95 or €100)

### Layer 3: Weekend Rate (Friday & Saturday nights)
Weekends command a 20–30% premium in virtually every market.

```
Weekend Rate = Standard Rate × 1.25
```
Example: €98 × 1.25 = **€123/night** (round to €120)

### Layer 4: Seasonal Adjustments (applied on top of weekend/weekday rates)

| Season Type | Modifier | When | Example (base €98) |
|---|---|---|---|
| Peak High Season | +35% | School holidays, local festivals, summer peak | €132 |
| Peak Mid Season | +20% | Spring break, bank holidays, events nearby | €118 |
| Standard | 0% | Normal periods | €98 |
| Low Season | -15% | Jan, Feb, Nov (non-holiday weeks) | €83 |
| Distress Pricing | -25% | 7+ days out with <40% occupancy | €74 |

---

## SECTION 2 — LOCAL MARKET BENCHMARKING

Run this analysis before setting any rate. Repeat quarterly.

### Step 1: Pull Competitive Set
On Airbnb, search your area with the following filters:
- Dates: Next available 2-week window
- Guests: Your property's max capacity
- Property type: Same as yours (entire place, etc.)
- Superhost filter: OFF (you want the full market)

Record the 10 closest competitors (nearest, most similar).

### Competitor Analysis Table

| # | Listing Name | Bedrooms | Reviews | Rating | Weekday Rate | Weekend Rate | Notes |
|---|---|---|---|---|---|---|---|
| 1 | [Name] | [#] | [#] | [#] | €___ | €___ | [Superhost? Views?] |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

### Step 2: Calculate Your Market Position
```
Market Average Weekday = Sum of competitor weekday rates ÷ 10
Your target position = Market Average × 1.0 (match) to × 1.15 (premium)
```

**Positioning rule:** If you have:
- Under 10 reviews → Price 5% BELOW market average to drive bookings
- 10–30 reviews, under 4.7 rating → Price AT market average
- 30+ reviews, 4.8+ rating → Price 10–15% ABOVE market average
- Superhost, 50+ reviews, 4.9+ → Price 20–25% ABOVE market average

---

## SECTION 3 — DYNAMIC PRICING CALENDAR

### Weekly Pricing Review (every Sunday, 15 minutes)

**Check the next 60 days. For each week, ask:**

1. **Is occupancy <30% with <14 days until that week?** → Apply -15% flash discount immediately
2. **Is a local event happening?** → Apply event premium: +25 to +45%
3. **Are school holidays coming?** → Apply +25% 6 weeks in advance
4. **Is a weekend already 75%+ booked?** → Raise remaining nights by +10%

### Event Price Premium Guide

| Event Type | Premium Range | Lead Time to Apply |
|---|---|---|
| Major music festival (city-wide) | +45 to +60% | 3–6 months ahead |
| Sports finals / international match | +35 to +50% | 2–4 months ahead |
| Marathon / triathlon | +25 to +35% | 4–8 weeks ahead |
| Local art/food festival (3+ days) | +20 to +30% | 4–8 weeks ahead |
| Conference / trade show | +20 to +30% | 6–10 weeks ahead |
| Bank holiday long weekend | +20 to +25% | 4–8 weeks ahead |
| School half-term week | +15 to +20% | 4–6 weeks ahead |

**How to find events:** Google "[your city] events [month]" and check local tourism websites monthly.

---

## SECTION 4 — LENGTH-OF-STAY STRATEGY

### Minimum Stay Settings by Period

| Period | Minimum Stay | Reason |
|---|---|---|
| Peak weeks (Aug, bank holidays) | 3 nights | Maximise revenue, reduce turnover cost |
| Standard weekdays | 2 nights | Prevent single-night gaps |
| Weekends (Fri–Sun) | 2 nights | Capture weekend travellers |
| Last-minute (<5 days out, gaps) | 1 night | Fill gaps; better than empty |
| Low season (Jan, Nov) | 1 night | Volume over margin |

### Gap Management Rule
If you have a 1-night gap between two bookings, and it's within 7 days, switch that night to a 1-night minimum at -10% off your standard rate. A booked night at 90% price beats an empty night every time.

---

## SECTION 5 — CLEANING FEE STRATEGY

The cleaning fee is a pricing lever, not just a cost recovery. Set it wrong and it kills your click-through rate.

**Cleaning Fee Formula:**
```
Cleaning Fee = Actual Cleaning Cost + 15% buffer
```

**But calibrate against your nightly rate:**
- If your ADR is under €80/night: Keep cleaning fee under €45
- If your ADR is €80–€120/night: Cleaning fee of €50–€70 is acceptable
- If your ADR is over €120/night: Cleaning fee up to €100 won't deter guests

**Strategy tip:** Airbnb shows a "total price" toggle in search results. Higher cleaning fees hurt you on 1–2 night searches. Consider baking 50% of your cleaning cost into the nightly rate and reducing the cleaning fee if you're targeting short stays.

---

## SECTION 6 — AUTOMATED PRICING TOOLS

Do not manually update pricing if you have more than 1 property or more than 20 open dates to manage. Use a tool.

### Recommended Tools (by budget)

| Tool | Monthly Cost | Best For | Key Feature |
|---|---|---|---|
| PriceLabs | $19.99/property | Serious hosts, single or multi-property | Hyper-local demand data, custom rules |
| Wheelhouse | $19.99/property | Hosts who want less manual input | Automated seasonal logic |
| Beyond | $25/property | Hosts who want a managed experience | Revenue manager support |
| Airbnb Smart Pricing | Free | New hosts only — DO NOT rely on it | Consistently underprices listings |

**Recommendation:** Use PriceLabs with the following base settings:
- Base price: Your Standard Rate from Section 1
- Min price: Your Base Rate Floor
- Max price: Your Standard Rate × 2.5
- Last-minute discount: 10% inside 3 days
- Far-out premium: +5% for dates 90+ days ahead

---

## SECTION 7 — REVENUE OPTIMISATION CHECKLIST

Run this monthly:

- [ ] Reviewed and updated competitor rates from Competitive Set
- [ ] Checked local event calendar for next 90 days
- [ ] Updated seasonal pricing adjustments in Airbnb calendar
- [ ] Reviewed any 1-night gaps and activated 1-night minimums
- [ ] Reviewed previous month's ADR vs. target — adjust if variance >10%
- [ ] Confirmed cleaning fee is calibrated to current nightly rate
- [ ] Checked PriceLabs/Wheelhouse override rules are active
- [ ] Reviewed Airbnb's "suggested price" (for reference only — do not follow blindly)

---

*Last updated: v1.0.0 | Review quarterly or after any market shift*
