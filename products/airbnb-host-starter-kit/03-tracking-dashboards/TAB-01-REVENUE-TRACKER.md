# TAB-01: Revenue Tracker
## Booking Revenue · Columns · Formulas · Example Data

---

## PURPOSE

One row per booking. Every booking that generates revenue gets an entry. This tab is the source of truth for all revenue KPIs: ADR, RevPAN, occupancy rate, and monthly gross revenue.

---

## COLUMN STRUCTURE

Set up these columns in Google Sheets in this exact order:

| Col | Header | Format | Data Entry |
|---|---|---|---|
| A | Booking Ref | Text | Airbnb booking ID (found in the booking details) |
| B | Guest Name | Text | First name only or full name — consistent choice |
| C | Check-In Date | Date DD/MM/YYYY | Actual check-in date |
| D | Check-Out Date | Date DD/MM/YYYY | Actual check-out date |
| E | Nights | Number | =D2-C2 (formula — do not enter manually) |
| F | Guests | Number | Number of guests as booked |
| G | Accommodation Rate (€) | Currency | Total accommodation revenue before Airbnb fee. This is the rate × nights. |
| H | Cleaning Fee Collected (€) | Currency | Cleaning fee charged to guest (as listed on Airbnb) |
| I | Gross Revenue (€) | Currency | =G2+H2 (accommodation + cleaning fee) |
| J | Airbnb Fee 3% (€) | Currency | =I2*0.03 |
| K | Net Revenue (€) | Currency | =I2-J2 |
| L | Payout Received (€) | Currency | Actual payout from Airbnb (cross-check against bank) |
| M | Payout Date | Date DD/MM/YYYY | Date funds arrived in your bank account |
| N | Booking Date | Date DD/MM/YYYY | Date the guest made the booking |
| O | Lead Time (days) | Number | =C2-N2 |
| P | Source | Dropdown | Airbnb / Booking.com / VRBO / Direct |
| Q | Review Score | Number (1–5) | Overall guest review score (fill in after review received) |
| R | Notes | Text | Any relevant notes: early check-in, damage, special request |

---

## FORMULA ROWS

At the bottom of your data (leave 200 rows for data first), add a **Monthly Summary Block** starting approximately at row 205:

**Row 205 header:** `MONTHLY SUMMARY — [YEAR]`

| Row | Label | Formula | Notes |
|---|---|---|---|
| 206 | Total Booked Nights | `=SUMIF(C2:C200,">="&DATE(YEAR,MONTH,1),E2:E200)` | Adjust YEAR and MONTH for each month |
| 207 | Total Gross Revenue | `=SUMIF(C2:C200,">="&DATE(YEAR,MONTH,1),I2:I200)` | |
| 208 | Total Net Revenue | `=SUMIF(C2:C200,">="&DATE(YEAR,MONTH,1),K2:K200)` | |
| 209 | ADR | `=Row207/Row206` (actual cell refs) | Average daily rate |
| 210 | Occupancy Rate | `=Row206/Days_in_Month` | Enter days in month manually |
| 211 | Average Lead Time | `=AVERAGEIF(C2:C200,">="&DATE(YEAR,MONTH,1),O2:O200)` | |

**Note on SUMIF formulas:** Replace YEAR and MONTH with the actual year and month numbers (e.g., 2026 and 1 for January 2026). Google Sheets date functions use numeric months (1=January, 12=December).

Simpler alternative: Use a filter view and sort by check-in month. Then use `=SUM` on the visible range. This approach is faster to set up and accurate for manual monthly reviews.

---

## ANNUAL TOTALS ROW

After all 12 monthly summaries, create an annual totals row:

| Metric | Formula | Target (from Business Plan) |
|---|---|---|
| Total Booked Nights | `=SUM(all monthly booked nights)` | 277 |
| Total Gross Revenue | `=SUM(all monthly gross revenue)` | €31,557 |
| Total Net Revenue | `=SUM(all monthly net revenue)` | €30,608 |
| Annual ADR | `=Total Gross Revenue/Total Booked Nights` | €110 avg |
| Annual Occupancy | `=Total Booked Nights/365` | 76% |

---

## EXAMPLE DATA (Enter These Three Rows to Test Formulas, Then Delete)

| A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|
| HM3K5V6YB | Maria Santos | 15/01/2026 | 18/01/2026 | =D2-C2 → 3 | 2 | 240.00 | 65.00 | 305.00 | 9.15 | 295.85 |
| HN7X2Q4PR | James Taylor | 22/01/2026 | 25/01/2026 | 3 | 1 | 240.00 | 65.00 | 305.00 | 9.15 | 295.85 |
| HP4M8W9TS | Sophie Laurent | 03/02/2026 | 10/02/2026 | 7 | 2 | 595.00 | 65.00 | 660.00 | 19.80 | 640.20 |

After confirming your formulas calculate correctly from these rows (Col E should auto-calculate, Col I should sum G+H, Col J should be 3% of Col I), delete the example data and begin entering real bookings.

---

## CONDITIONAL FORMATTING (Optional but Recommended)

Apply to Col Q (Review Score):
- Score 5: Green fill
- Score 4: Yellow fill
- Score 3 or below: Red fill

This gives you an instant visual scan of review performance across the year.

Apply to Col O (Lead Time):
- Lead time below 7 days: Orange fill (last-minute booking — flag for pricing review)

---

*Last updated: v1.0.0 · Build this tab before your first booking is confirmed*
