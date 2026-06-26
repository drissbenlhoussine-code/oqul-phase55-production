# TAB-06: Review Scorecard
## Review Tracker · Subcategory Scores · Trend Analysis

---

## PURPOSE

One row per review received. This tab tracks every guest review across all six Airbnb subcategories, identifies trends, and feeds the review performance section of TAB-07 (KPI Dashboard). The 90-day rolling averages from this tab are the input for your monthly host review (SOP-10).

---

## COLUMN STRUCTURE

| Col | Header | Format | Data Entry |
|---|---|---|---|
| A | Review Date | Date DD/MM/YYYY | Date the review was published on Airbnb |
| B | Booking Ref | Text | Corresponding booking reference |
| C | Guest Name | Text | Guest's first name |
| D | Overall Score | Number 1–5 | Overall star rating |
| E | Cleanliness | Number 1–5 | Cleanliness subcategory |
| F | Accuracy | Number 1–5 | Accuracy subcategory |
| G | Check-In | Number 1–5 | Check-in subcategory |
| H | Communication | Number 1–5 | Communication subcategory |
| I | Location | Number 1–5 | Location subcategory |
| J | Value | Number 1–5 | Value subcategory |
| K | Review Text | Text | Guest's written review (copy-paste from Airbnb) |
| L | Host Response | Dropdown | Sent / Not Sent |
| M | Response Date | Date | When you responded |
| N | Response Type | Dropdown | Positive (MSG-13) / Negative (MSG-14) / Custom |
| O | Issue Mentioned | Dropdown | None / Cleanliness / Accuracy / Check-in / Comm / Location / Value / Multiple |
| P | Action Taken | Text | What you changed as a result (if anything) |
| Q | Verified | Checkbox | ✓ when you have confirmed scores in Airbnb match what you recorded here |

---

## SECTION 2 — RUNNING AVERAGES SECTION

Below your data rows (leave 200 rows), create a Running Averages block:

| Metric | Last 5 Reviews | Last 10 Reviews | Last 30 Days | All Time |
|---|---|---|---|---|
| Overall | `=AVERAGE(D[-5]:D[-1])` | `=AVERAGE(D[-10]:D[-1])` | AVERAGEIFS with date range | `=AVERAGE(D2:D[last])` |
| Cleanliness | | | | |
| Accuracy | | | | |
| Check-In | | | | |
| Communication | | | | |
| Location | | | | |
| Value | | | | |

**Simpler approach:** Use the AVERAGEIFS function to calculate averages for date ranges:
`=AVERAGEIFS(D2:D200,A2:A200,">="&DATE(2026,1,1),A2:A200,"<="&DATE(2026,3,31))`
This averages Column D (Overall Score) for reviews between January 1 and March 31, 2026. Adjust dates per quarter.

---

## SECTION 3 — TREND CHART

After 10 reviews, create a line chart:
1. Select Column A (dates) and Column D (overall scores)
2. Insert → Chart → Line chart
3. Title: "Review Trend — Overall Score"
4. Set Y-axis minimum to 3.0 and maximum to 5.0 (the relevant range)

This chart should live on TAB-07 (KPI Dashboard) but is built from TAB-06 data.

**What to look for:**
- Any downward trend over 3+ consecutive reviews: investigate immediately
- Any subcategory consistently below others: root cause analysis
- Any review after a maintenance event: did the issue affect the score?

---

## SECTION 4 — COMPETITIVE BENCHMARKS

Use these to assess your review performance:

| Benchmark | Target |
|---|---|
| Superhost eligibility | ≥4.8 overall |
| Top 10% listing tier | ≥4.9 overall |
| Airbnb Guest Favourite status | ≥4.9 + 50+ reviews |
| No ranking suppression | ≥4.7 overall |
| No Superhost loss risk | ≥4.8 in assessment window |

If your overall score is between 4.7 and 4.79: you are in the risk zone. Any single 3-star review moves you below Superhost threshold. Identify your weakest subcategory and address it in the next turnover.

---

## SECTION 5 — REVIEW TEXT ANALYSIS (Quarterly)

Every quarter, read through all review texts from the past 90 days. Create a simple tally:

**Positive mentions (what guests specifically praised):**

| Theme | Count | Example Quote |
|---|---|---|
| Location | | |
| Cleanliness | | |
| Check-in process | | |
| Host communication | | |
| Specific amenity (WiFi, coffee, etc.) | | |
| Value | | |

**Negative or neutral mentions:**

| Theme | Count | Action Taken |
|---|---|---|
| | | |

The positive mentions with high counts are your conversion assets — they should appear in your listing description.

The negative mentions that appear 2+ times are systemic issues. Fix them.

---

## EXAMPLE DATA

| A | B | C | D | E | F | G | H | I | J | L |
|---|---|---|---|---|---|---|---|---|---|---|
| 21/01/2026 | HM3K5V6YB | Maria | 5 | 5 | 5 | 5 | 5 | 4 | 5 | Sent |
| 28/01/2026 | HN7X2Q4PR | James | 5 | 5 | 5 | 5 | 5 | 4 | 5 | Sent |
| 14/02/2026 | HP4M8W9TS | Sophie | 5 | 5 | 5 | 5 | 5 | 4 | 5 | Sent |

*Note: Location scores of 4 are common for city-centre properties — guests often reserve a 5 for properties with exceptional views or premium locations. A consistent 4 on Location is not a problem if it matches your honest description.*

---

*Last updated: v1.0.0 · Log every review within 48 hours of receiving it — never batch*
