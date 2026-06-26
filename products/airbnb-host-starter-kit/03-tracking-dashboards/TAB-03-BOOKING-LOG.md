# TAB-03: Booking Log
## Spreadsheet Tab Specification

**Tab name:** Bookings  
**Purpose:** Complete record of every booking — guest, dates, financials, outcome  
**Updated:** At booking confirmation and updated at checkout

---

## COLUMN HEADERS

| Column | Header | Data Type | Input or Formula | Notes |
|---|---|---|---|---|
| A | Booking Ref | Text | Input | Airbnb reference (HMxxxxxxx) |
| B | Status | Dropdown | Input | Confirmed / Checked In / Completed / Cancelled |
| C | Guest First Name | Text | Input | |
| D | Guest Profile Link | URL | Input | Copy from Airbnb guest profile |
| E | Guest Rating (received) | Number (0–5) | Input | Rating you gave them |
| F | Number of Guests | Number | Input | |
| G | Check-In Date | Date | Input | |
| H | Check-Out Date | Date | Input | |
| I | Nights | Number | Formula: =H2-G2 | |
| J | Nightly Rate (€) | Currency | Input | |
| K | Total Booking Value (€) | Currency | Input | Total guest paid |
| L | Cleaning Fee (€) | Currency | Input | |
| M | Net Revenue (€) | Currency | Formula: =K2*0.97 | After 3% Airbnb fee |
| N | Pre-Arrival Msg Sent | Checkbox | Input | |
| O | Check-In Msg Sent | Checkbox | Input | |
| P | Mid-Stay Msg Sent | Checkbox | Input | |
| Q | Check-Out Msg Sent | Checkbox | Input | |
| R | Review Request Sent | Checkbox | Input | |
| S | Guest Review Received | Dropdown | Input | Yes / No / Pending |
| T | Star Rating Received | Number (1–5) | Input | |
| U | Issues During Stay | Text | Input | Brief description or "None" |
| V | Damage Claim Filed | Dropdown | Input | Yes / No |
| W | Claim Amount (€) | Currency | Input | If applicable |
| X | Notes | Text | Input | Any other notes |

---

## 3 EXAMPLE ROWS

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HM123456 | Completed | Sophie | [link] | 5 | 2 | 10/01/26 | 13/01/26 | 3 | €95 | €345 | €60 | €334.65 | ✓ | ✓ | ✓ | ✓ | ✓ | Yes | 5 | None | No | — | Great guests |
| HM987654 | Completed | James | [link] | 5 | 1 | 19/01/26 | 22/01/26 | 3 | €95 | €345 | €60 | €334.65 | ✓ | ✓ | ✓ | ✓ | ✓ | Yes | 4 | None | No | — | Left window open |
| HM456123 | Completed | Mia | [link] | 5 | 3 | 02/02/26 | 07/02/26 | 5 | €100 | €560 | €60 | €543.20 | ✓ | ✓ | ✓ | ✓ | ✓ | Yes | 5 | None | No | — | Excellent guests — invite back |

---

## FORMULA SUMMARY ROW

Place at top of sheet or bottom of data:

| Metric | Formula |
|---|---|
| Total Bookings | =COUNTA(A:A)-1 |
| Total Nights | =SUM(I:I) |
| Total Revenue | =SUM(K:K) |
| Total Net Revenue | =SUM(M:M) |
| Avg Booking Value | =AVERAGE(K:K) |
| Avg Length of Stay | =AVERAGE(I:I) |
| Avg Rating Received | =AVERAGEIF(T:T,">0",T:T) |
| % Reviews Received | =COUNTIF(S:S,"Yes")/COUNTA(A:A)-1 |
| Issues Rate | =COUNTIF(U:U,"<>None")/COUNTA(A:A)-1 |

---

## COMMUNICATION COMPLETION VIEW

Use conditional formatting to track message compliance:

- Columns N, O, Q must all be checked (✓) by day 1 of stay — if any are unchecked after check-in date: highlight RED
- Column P must be checked by Day 2 — if unchecked: highlight YELLOW
- Column R must be checked within 4 hours of checkout — if unchecked by end of checkout day: highlight RED

This view ensures no communication step is ever missed.

---

## GUEST RETURN RATE TRACKING

Create a small table at the bottom of the Bookings sheet:

| Guest Name | Total Bookings | Last Stay | Invited Back? | Returned? |
|---|---|---|---|---|
| Sophie M | 2 | March 2026 | Yes | Yes |
| James T | 1 | January 2026 | Yes | No (yet) |

Track returning guests — they are your most valuable segment. A returning guest costs €0 in acquisition and typically leaves 5-star reviews.
