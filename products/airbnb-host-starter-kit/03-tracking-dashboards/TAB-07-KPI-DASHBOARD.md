# TAB-07: KPI Dashboard
## Spreadsheet Tab Specification — Monthly Summary Dashboard

**Tab name:** KPI Dashboard  
**Purpose:** Single-page view of all key metrics, pulling from every other tab  
**Updated:** Monthly (first Monday of each month per SOP-10)

---

## DASHBOARD STRUCTURE

This tab is read-only (no direct input). All values pull from other tabs via formula.

---

## SECTION A: REVENUE OVERVIEW

| Metric | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gross Revenue (€) | | | | | | | | | | | | | |
| Net Revenue (€) | | | | | | | | | | | | | |
| ADR (€) | | | | | | | | | | | | | |
| RevPAN (€) | | | | | | | | | | | | | |
| Target Net Revenue (€) | [from Business Plan] | | | | | | | | | | | | |
| vs. Target (%) | Formula: =(Actual/Target)-1 | | | | | | | | | | | | |

**Formulas for each month column:**
```
Gross Revenue: =SUMIFS(Revenue!I:I, Revenue!B:B, "January 2026")
Net Revenue: =SUMIFS(Revenue!L:L, Revenue!B:B, "January 2026")
ADR: =Net Revenue / Booked Nights
RevPAN: =Net Revenue / 31 (days in month)
```

---

## SECTION B: OCCUPANCY METRICS

| Metric | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Available Nights | 31 | 28 | 31 | 30 | 31 | 30 | 31 | 31 | 30 | 31 | 30 | 31 | 365 |
| Booked Nights | | | | | | | | | | | | | |
| Occupancy Rate (%) | | | | | | | | | | | | | |
| Target Occupancy (%) | [from Business Plan] | | | | | | | | | | | | |
| vs. Target (pp) | | | | | | | | | | | | | |
| Bookings Completed | | | | | | | | | | | | | |
| Avg Length of Stay | | | | | | | | | | | | | |

---

## SECTION C: QUALITY METRICS

| Metric | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reviews Received | | | | | | | | | | | | | |
| Cumulative Reviews | | | | | | | | | | | | | |
| Overall Rating (avg) | | | | | | | | | | | | | |
| Cleanliness Rating | | | | | | | | | | | | | |
| Check-in Rating | | | | | | | | | | | | | |
| Communication Rating | | | | | | | | | | | | | |
| Response Rate (%) | | | | | | | | | | | | | |
| Superhost Status | | | | | | | | | | | | | |

---

## SECTION D: COST & PROFIT SUMMARY

| Metric | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fixed Costs (€) | | | | | | | | | | | | | |
| Variable Costs (€) | | | | | | | | | | | | | |
| Total Costs (€) | | | | | | | | | | | | | |
| Gross Profit (€) | | | | | | | | | | | | | |
| Gross Margin (%) | | | | | | | | | | | | | |
| Target Margin (%) | 65% | 65% | 65% | 65% | 65% | 65% | 65% | 65% | 65% | 65% | 65% | 65% | 65% |

---

## SECTION E: OPERATIONAL METRICS

| Metric | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | YTD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Total Turnovers | | | | | | | | | | | | | |
| Maintenance Issues | | | | | | | | | | | | | |
| P1/P2 Issues | | | | | | | | | | | | | |
| Maintenance Spend (€) | | | | | | | | | | | | | |
| Avg Issue Resolution (hrs) | | | | | | | | | | | | | |

---

## SECTION F: STATUS INDICATORS (TRAFFIC LIGHT SYSTEM)

| KPI | Value | Target | Status |
|---|---|---|---|
| Overall Rating | [=AVERAGE(Reviews!D:D)] | ≥4.85 | 🟢 / 🟡 / 🔴 |
| Occupancy Rate | [=last month] | ≥72% | 🟢 / 🟡 / 🔴 |
| Response Rate | [=from Airbnb] | ≥98% | 🟢 / 🟡 / 🔴 |
| Gross Margin | [=calculated] | ≥65% | 🟢 / 🟡 / 🔴 |
| Open Maintenance Issues | [=COUNTIF(Maintenance!L:L,"Open")] | 0 | 🟢 / 🔴 |
| Superhost Status | [Manual input] | Active | 🟢 / 🔴 |

Apply conditional formatting:
- Green if at or above target
- Yellow if within 5% below target
- Red if more than 5% below target

---

## 3 EXAMPLE ROWS (Annual View)

| Metric | Full Year Example |
|---|---|
| Total Gross Revenue | €32,410 |
| Total Net Revenue | €31,438 |
| Annual Occupancy | 76.2% (278 nights / 365) |
| Annual ADR | €113.05 |
| Annual RevPAN | €86.13 |
| Average Rating | 4.91 |
| Total Reviews | 87 |
| Net Profit (after costs) | €23,620 |
| Net Margin | 72.8% |

---

## NOTES

- All green = your hosting operation is performing. Maintain current standards.
- One yellow = monitor closely; identify the drag and address within 2 weeks.
- One red = this month's improvement action (SOP-10) must address this KPI specifically.
- Two or more red = investigate immediately; something structural has changed.

---

*Update monthly on the first Monday | All values pull from other tabs — do not manually enter here*
