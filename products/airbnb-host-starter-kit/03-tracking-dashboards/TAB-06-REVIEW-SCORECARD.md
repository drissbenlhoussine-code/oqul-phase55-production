# TAB-06: Review Scorecard
## Spreadsheet Tab Specification

**Tab name:** Reviews  
**Purpose:** Track every guest review received, analyse patterns, and monitor rating trajectory  
**Updated:** Within 24 hours of each review received

---

## COLUMN HEADERS

| Column | Header | Data Type | Input or Formula | Notes |
|---|---|---|---|---|
| A | Review Date | Date | Input | When guest posted the review |
| B | Guest Name | Text | Input | First name only |
| C | Booking Ref | Text | Input | Cross-reference to Bookings tab |
| D | Overall Rating | Number (1–5) | Input | Overall star rating |
| E | Cleanliness | Number (1–5) | Input | Sub-category rating |
| F | Accuracy | Number (1–5) | Input | Sub-category rating |
| G | Check-In | Number (1–5) | Input | Sub-category rating |
| H | Communication | Number (1–5) | Input | Sub-category rating |
| I | Location | Number (1–5) | Input | Sub-category rating |
| J | Value | Number (1–5) | Input | Sub-category rating |
| K | Review Text | Text | Input | Copy the full review text here |
| L | Review Request Sent? | Checkbox | Input | |
| M | Review Request Timing | Number | Input | Hours after checkout when request sent |
| N | Response Posted? | Checkbox | Input | Did you respond publicly? |
| O | Response Date | Date | Input | When you responded |
| P | Response Template Used | Text | Input | Which MSG template |
| Q | Primary Theme (positive) | Text | Input | Main thing they praised |
| R | Primary Theme (concern) | Text | Input | Main thing they flagged (if any) |
| S | Action Taken | Text | Input | What you changed based on this review |

---

## 3 EXAMPLE ROWS

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13/01/26 | Sophie | HM123456 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | "Absolutely perfect stay. The apartment was immaculate and the welcome basket was a lovely touch. Maria was incredibly responsive. We'll definitely be back." | ✓ | 2 | ✓ | 14/01/26 | MSG-13 | Cleanliness; welcome basket | None | None needed |
| 22/01/26 | James | HM987654 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | "Great apartment, very clean. Check-in was seamless. Bedroom could use a second pillow option. Would recommend." | ✓ | 2 | ✓ | 23/01/26 | MSG-13 | Check-in experience | Pillow quantity | Added extra pillows to both beds |
| 07/02/26 | Mia | HM456123 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | "Wonderful stay in a beautiful city. The apartment is even nicer than the photos — and they're already stunning. Host communication was excellent. Location is perfect for exploring Alfama. Highly recommend." | ✓ | 2 | ✓ | 08/02/26 | MSG-13 | Property exceeds listing | Location context | None needed |

---

## SUMMARY METRICS SECTION

Place at top of sheet:

| Metric | Formula | Current Value | Target |
|---|---|---|---|
| Total reviews | =COUNTA(D:D)-1 | | ≥30 |
| Overall avg rating | =AVERAGE(D:D) | | ≥4.85 |
| Avg cleanliness | =AVERAGE(E:E) | | ≥4.9 |
| Avg accuracy | =AVERAGE(F:F) | | ≥4.9 |
| Avg check-in | =AVERAGE(G:G) | | ≥4.9 |
| Avg communication | =AVERAGE(H:H) | | ≥4.9 |
| Avg location | =AVERAGE(I:I) | | ≥4.8 |
| Avg value | =AVERAGE(J:J) | | ≥4.7 |
| Review conversion rate | =COUNTA(D:D)/[total bookings] | | ≥70% |
| % reviews responded to | =COUNTIF(N:N,TRUE)/COUNTA(D:D) | | 100% |
| Avg response time (hrs) | =AVERAGE(O:O - A:A in hours) | | ≤24 |

---

## RATING TREND CHART

Create a line chart using:
- X-axis: Review Date (Column A)
- Y-axis: Overall Rating (Column D)
- Add a horizontal reference line at 4.85 (Superhost threshold)

This makes rating trends visible at a glance. A declining trend needs immediate action.

---

## THEME ANALYSIS (QUARTERLY)

Tally all entries in Column Q and R:

| Theme | Count (Positive) | Count (Concern) | Net |
|---|---|---|---|
| Cleanliness | 18 | 2 | +16 |
| Check-in | 12 | 0 | +12 |
| Welcome extras | 11 | 0 | +11 |
| WiFi | 3 | 1 | +2 |
| Pillow/bedding | 2 | 2 | 0 |
| Parking | 0 | 3 | -3 |

Items with a negative net score get added to your monthly improvement action (SOP-10 Step 5).

---

## SUPERHOST TRACKING SECTION

Airbnb resets Superhost status twice a year (April 1 and October 1, based on Jan–June and July–Dec performance).

| Period | Stays Required (≥10) | Rating Required (≥4.8) | Response Rate (≥90%) | Cancellations (0%) | Superhost Eligible? |
|---|---|---|---|---|---|
| Jan–Jun 2026 | | | | | |
| Jul–Dec 2026 | | | | | |

Update this section monthly from your Airbnb dashboard.
