# TAB-01: Revenue Tracker
## Spreadsheet Tab Specification

**Tab name:** Revenue  
**Purpose:** Track all income from bookings month by month  
**Updated:** After each Airbnb payout is received (typically weekly or monthly per your settings)

---

## COLUMN HEADERS

| Column | Header | Data Type | Input or Formula | Notes |
|---|---|---|---|---|
| A | Payout Date | Date (DD/MM/YYYY) | Input | Date Airbnb deposited funds |
| B | Month | Text | Formula: =TEXT(A2,"MMMM YYYY") | Auto-calculates from date |
| C | Booking Ref | Text | Input | Airbnb booking reference (starts with HM...) |
| D | Guest Name | Text | Input | First name only is fine |
| E | Check-In Date | Date | Input | |
| F | Check-Out Date | Date | Input | |
| G | Nights | Number | Formula: =F2-E2 | Auto-calculates |
| H | Nightly Rate (€) | Currency | Input | Average nightly rate for this booking |
| I | Gross Booking Amount (€) | Currency | Input | Total guest paid (from Airbnb payout report) |
| J | Cleaning Fee Collected (€) | Currency | Input | Cleaning fee Airbnb collected from guest |
| K | Airbnb Host Fee (€) | Currency | Formula: =I2*0.03 | 3% of gross booking amount |
| L | Net Host Revenue (€) | Currency | Formula: =I2-K2 | What Airbnb pays you |
| M | Tourist Tax Collected (€) | Currency | Input | If you collect tourist tax via Airbnb |
| N | Currency | Text | Input | EUR / GBP / USD |
| O | Notes | Text | Input | Any notes (e.g., "early check-in fee included") |

---

## SUMMARY ROW (below data — row 1000 or use a separate section at top)

| Label | Formula |
|---|---|
| Total Nights Booked | =SUM(G:G) |
| Total Gross Revenue | =SUM(I:I) |
| Total Airbnb Fees Paid | =SUM(K:K) |
| Total Net Revenue | =SUM(L:L) |
| Average ADR | =AVERAGE(H:H) |

---

## 3 EXAMPLE ROWS

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 15/01/2026 | January 2026 | HM123456789 | Sophie | 10/01/2026 | 13/01/2026 | 3 | €95 | €285 | €60 | €8.55 | €276.45 | €9 | EUR | — |
| 22/01/2026 | January 2026 | HM987654321 | James | 19/01/2026 | 22/01/2026 | 3 | €95 | €285 | €60 | €8.55 | €276.45 | €9 | EUR | — |
| 05/02/2026 | February 2026 | HM456123789 | Mia | 02/02/2026 | 07/02/2026 | 5 | €100 | €500 | €60 | €15.00 | €485.00 | €15 | EUR | 5-night discount applied |

---

## MONTHLY PIVOT VIEW

Create a secondary section (or a separate tab called "Revenue by Month") with:

| Month | Booked Nights | Bookings | Gross Revenue | Net Revenue | ADR | RevPAN |
|---|---|---|---|---|---|---|
| January 2026 | 17 | 6 | €1,615 | €1,566 | €95 | €50.52 |
| February 2026 | 17 | 5 | €1,700 | €1,649 | €100 | €58.93 |
| [continue...] | | | | | | |

Formula for RevPAN: `=Net Revenue / Days in Month`

---

## CONDITIONAL FORMATTING RULES

- Column L (Net Revenue): if monthly total < target from Business Plan → highlight RED
- Column G (Nights): any row with 1 night → highlight YELLOW (track 1-night stays vs. revenue impact)
- Column A (Payout Date): if date is more than 7 days past today → highlight RED (chasing unpaid payouts)
