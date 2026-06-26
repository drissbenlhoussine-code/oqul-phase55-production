# TAB-04: Cleaning Schedule
## Spreadsheet Tab Specification

**Tab name:** Cleaning  
**Purpose:** Schedule and confirm every turnover cleaning; track cleaning team performance  
**Updated:** At booking confirmation (schedule) and post-cleaning (confirmation)

---

## COLUMN HEADERS

| Column | Header | Data Type | Input or Formula | Notes |
|---|---|---|---|---|
| A | Checkout Date | Date | Input | The day the outgoing guest leaves |
| B | Check-In Date | Date | Input | The day the incoming guest arrives |
| C | Gap (Hours) | Number | Formula: =(B2-A2)*24 | Hours between checkout and check-in |
| D | Booking Ref (Out) | Text | Input | Outgoing guest's booking ref |
| E | Booking Ref (In) | Text | Input | Incoming guest's booking ref |
| F | Cleaner Assigned | Text | Dropdown | Primary cleaner name |
| G | Cleaning Start Time | Time | Input | Agreed start time |
| H | Cleaning End Time | Time | Input | Actual finish time |
| I | Duration (Hrs) | Number | Formula: =H2-G2 | |
| J | Confirmed? | Checkbox | Input | Did cleaner confirm the booking? |
| K | Completed? | Checkbox | Input | Did cleaner report completion? |
| L | Photos Received? | Checkbox | Input | Did cleaner send post-clean photos? |
| M | Host Inspected? | Checkbox | Input | Did host or co-host inspect? |
| N | Quality Rating | Number (1–5) | Input | Your rating of this cleaning |
| O | Issues Found | Text | Input | Any issues noted during inspection |
| P | Cleaning Fee Paid (€) | Currency | Input | Amount paid to cleaner |
| Q | Notes | Text | Input | |

---

## 3 EXAMPLE ROWS

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13/01/26 | 14/01/26 | 24 | HM123456 | HM555001 | Maria S | 10:30 | 12:45 | 2.25 | ✓ | ✓ | ✓ | ✓ | 5 | None | €55 | Same-day turn |
| 22/01/26 | 23/01/26 | 24 | HM987654 | HM555002 | Maria S | 10:30 | 13:00 | 2.50 | ✓ | ✓ | ✓ | No | 4 | Hair in shower drain | €55 | Follow-up required |
| 07/02/26 | 09/02/26 | 48 | HM456123 | HM555003 | Maria S | 11:30 | 13:30 | 2.00 | ✓ | ✓ | ✓ | ✓ | 5 | None | €55 | 2-day gap, no rush |

---

## SUMMARY METRICS

| Metric | Formula | Target |
|---|---|---|
| Total turnovers | =COUNTIF(K:K,TRUE) | Track monthly |
| Average cleaning duration | =AVERAGE(I:I) | ≤2.5 hrs (1BR) |
| Average quality rating | =AVERAGE(N:N) | ≥4.5 |
| % completed on time | =COUNTIF(K:K,TRUE)/COUNTA(A:A) | 100% |
| % photos received | =COUNTIF(L:L,TRUE)/COUNTA(A:A) | 100% |
| Total cleaning costs | =SUM(P:P) | Track vs. budget |

---

## SCHEDULE VIEW (CALENDAR-STYLE)

For visual planning, create a weekly view:

| Week | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| 12–18 Jan | | Turnover (9→13) | | | | Turnover (10→13) | |
| 19–25 Jan | | Turnover (10→13) | | | | | |

Colour code: BLUE = turnover cleaning | GREEN = confirmed | RED = not yet confirmed

---

## CLEANER PERFORMANCE SCORECARD

Track each cleaner separately if you use more than one:

| Cleaner | Total Turnovers | Avg Rating | Avg Duration | Issues Reported | Reliability % |
|---|---|---|---|---|---|
| Maria Santos | 24 | 4.8 | 2.2 hrs | 2 | 100% |
| Backup Cleaner | 3 | 4.3 | 2.7 hrs | 1 | 100% |

Use this data quarterly to: affirm good performers, identify training needs, and make decisions about replacing underperforming cleaners.

---

## SHORT-TURNAROUND ALERT

Apply conditional formatting:  
- Column C (Gap in Hours) < 8 → highlight RED — same-day turn with less than 8 hours: flag as high risk, confirm extra resources  
- Column C < 24 → highlight YELLOW — less than 1 day turnaround: confirm cleaner has adequate time  
- Column J (Confirmed) = unchecked when Checkout Date is within 48 hours → highlight RED

This prevents an unconfirmed cleaning from slipping through and causing a check-in with a dirty property.
