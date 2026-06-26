# TAB-07: KPI Dashboard
## Monthly KPI Summary · 6 Sections · One-Page Property Performance View

---

## PURPOSE

This is the one tab you look at during your monthly host review (SOP-10). It pulls calculated KPIs from TAB-01 through TAB-06 into a single view. Build it last — it is entirely dependent on the other 6 tabs being populated.

---

## DASHBOARD STRUCTURE

TAB-07 is a single read-only view. Do not enter data here directly. All figures should be formulas pulling from the source tabs.

Suggested layout: one column per month (A through M, with A being labels), months January through December in columns B through M, and a YTD total in column N.

---

## SECTION 1 — REVENUE KPIs

| KPI | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Booked Nights | | | | | | | | | | | | | |
| Available Nights | 31 | 28 | 31 | 30 | 31 | 30 | 31 | 31 | 30 | 31 | 30 | 31 | 365 |
| Occupancy Rate | | | | | | | | | | | | | |
| ADR (€) | | | | | | | | | | | | | |
| RevPAN (€) | | | | | | | | | | | | | |
| Gross Revenue (€) | | | | | | | | | | | | | |
| Airbnb Fees (€) | | | | | | | | | | | | | |
| Net Revenue (€) | | | | | | | | | | | | | |
| **Projection (from Business Plan)** | | | | | | | | | | | | | |
| **Variance vs. Projection** | | | | | | | | | | | | | |

**Formula for Occupancy Rate:** Pull from TAB-01 monthly summary. If entering directly: Booked Nights ÷ Available Nights.

**Formula for Variance:** `=(Actual - Projected) / Projected` — format as percentage. Conditional formatting: red if negative, green if positive.

---

## SECTION 2 — BOOKING KPIs

| KPI | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Number of Bookings | | | | | | | | | | | | | |
| ALOS (nights) | | | | | | | | | | | | | |
| Avg Lead Time (days) | | | | | | | | | | | | | |
| Turnovers | | | | | | | | | | | | | |
| Direct Bookings | | | | | | | | | | | | | |

**ALOS formula:** Total Booked Nights ÷ Number of Bookings.

**Turnovers** = Number of Bookings (each booking is one turnover unless the same guest extends).

---

## SECTION 3 — COST KPIs

| KPI | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fixed Costs (€) | | | | | | | | | | | | | |
| Variable Costs — Cleaning (€) | | | | | | | | | | | | | |
| Variable Costs — Linen (€) | | | | | | | | | | | | | |
| Variable Costs — Consumables (€) | | | | | | | | | | | | | |
| Variable Costs — Welcome (€) | | | | | | | | | | | | | |
| Maintenance Costs (€) | | | | | | | | | | | | | |
| **Total Operating Costs (€)** | | | | | | | | | | | | | |
| Cleaning Fees Collected (€) | | | | | | | | | | | | | |
| Net Variable Costs (€) | | | | | | | | | | | | | |
| CPON (€) | | | | | | | | | | | | | |

**Net Variable Costs** = Total Variable Costs − Cleaning Fees Collected
**CPON** = Total Operating Costs ÷ Booked Nights

---

## SECTION 4 — PROFITABILITY KPIs

| KPI | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gross Revenue (€) | | | | | | | | | | | | | |
| Total Operating Costs (€) | | | | | | | | | | | | | |
| Net Operating Profit (€) | | | | | | | | | | | | | |
| Gross Profit Margin (%) | | | | | | | | | | | | | |
| Net Margin (%) | | | | | | | | | | | | | |

**Net Operating Profit** = Net Revenue − Fixed Costs − Net Variable Costs

**Net Margin** = Net Operating Profit ÷ Gross Revenue

**Target (from Business Plan):** Net Margin ≥70% monthly; YTD Net Operating Profit ≥€22,786 for Year 1.

---

## SECTION 5 — REVIEW KPIs

| KPI | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reviews Received | | | | | | | | | | | | | |
| Overall Rating (month avg) | | | | | | | | | | | | | |
| Overall Rating (rolling 90-day) | | | | | | | | | | | | | |
| Cleanliness (avg) | | | | | | | | | | | | | |
| Accuracy (avg) | | | | | | | | | | | | | |
| Check-In (avg) | | | | | | | | | | | | | |
| Communication (avg) | | | | | | | | | | | | | |
| Location (avg) | | | | | | | | | | | | | |
| Value (avg) | | | | | | | | | | | | | |
| Response Rate (Airbnb %) | | | | | | | | | | | | | |
| Total Reviews (cumulative) | | | | | | | | | | | | | |

**Superhost thresholds (highlight if below):**
- Overall Rating: ≥4.8 — conditional format: red if <4.8
- Response Rate: ≥90% — conditional format: red if <90%
- Total stays: track toward 10 minimum

---

## SECTION 6 — SUPERHOST STATUS TRACKER

This section tracks Superhost eligibility in real time.

| Criterion | Threshold | Current | On Track? |
|---|---|---|---|
| Total Stays (trailing 12 months) | ≥10 | | |
| Average Overall Rating | ≥4.8 | | |
| Response Rate (to all inquiries) | ≥90% | | |
| Host Cancellation Rate | 0% | | |
| Next Assessment Date | April 1 or October 1 | | |
| Projected Status | | | |

**On Track? formula:** IF current ≥ threshold, "✓", else "✗"

---

## HOW TO BUILD THIS TAB

1. Build TAB-01 through TAB-06 first.
2. Create TAB-07 with the six sections above.
3. For each KPI cell: write a formula that references the corresponding cell in the source tab. Example: `=TAB01!B206` (if Booked Nights for January is at cell B206 in TAB-01).
4. Add conditional formatting last, after confirming all formulas calculate correctly.
5. Lock the tab (Data → Protect sheets and ranges) to prevent accidental edits to formulas. Leave TAB-01 through TAB-06 editable for data entry.

---

*Last updated: v1.0.0 · Review this tab during every monthly host review (SOP-10)*
