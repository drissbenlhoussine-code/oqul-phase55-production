# TAB-04: Cleaning Schedule
## Turnover Schedule · Cleaner Coordination · Quality Tracking

---

## PURPOSE

One row per cleaning event. This tab is the operational schedule for your cleaning team and your quality assurance record. Use it to dispatch cleaners, track completion, and log quality issues.

---

## COLUMN STRUCTURE

| Col | Header | Format | Data Entry |
|---|---|---|---|
| A | Cleaning Date | Date DD/MM/YYYY | Date cleaning should occur (checkout day) |
| B | Booking Ref (Out) | Text | Booking reference of guest checking out |
| C | Checkout Time | Time | Standard checkout time (e.g., 10:00) |
| D | Booking Ref (In) | Text | Booking reference of guest checking in |
| E | Check-In Time | Time | Standard check-in time (e.g., 15:00) |
| F | Cleaning Window | Number (hours) | =E2-C2 — hours available for cleaning |
| G | Cleaner Name | Text | Which cleaner is assigned |
| H | Cleaner Confirmed | Checkbox | ✓ when cleaner has confirmed the booking |
| I | Cleaning Start Time | Time | Actual time cleaner arrived |
| J | Cleaning End Time | Time | Actual time cleaner finished |
| K | Duration (mins) | Number | =(J2-I2)*1440 (converts fraction-of-day to minutes) |
| L | Photo Confirmation | Dropdown | Received / Not Received |
| M | Quality Score | Dropdown | Pass / Minor Issues / Major Issues |
| N | Issues Found | Text | Description if M = Minor or Major Issues |
| O | Welcome Items Set | Checkbox | ✓ when welcome basket and consumables confirmed |
| P | Supplies Needed | Text | Any items needed for next cleaning |
| Q | Cost (€) | Currency | Amount invoiced by cleaner |
| R | Paid | Checkbox | ✓ when payment made |
| S | Notes | Text | Any operational notes |

---

## SECTION 2 — CLEANING WINDOW ANALYSIS

The Cleaning Window (Column F) is the hours between the previous guest's checkout and the next guest's check-in. Track this because:

- Under 2 hours: high risk. One delay causes a chain reaction. Flag these in advance and confirm cleaner availability.
- 2–4 hours: standard. The cleaning team should complete in 90–120 minutes, leaving buffer.
- 4+ hours: comfortable. No coordination risk.

**Formula for cleaning window:** If C (checkout time) is entered as a time value and E (check-in time) is also a time value: `=E2-C2` and format as Number to display hours.

**Conditional formatting:**
- Cleaning Window < 2h: Red fill (risk)
- Cleaning Window 2–4h: Yellow fill (standard)
- Cleaning Window > 4h: Green fill (comfortable)

---

## SECTION 3 — CLEANER MANAGEMENT

### Minimum Cleaner Coverage

Never operate with one cleaner. You need a minimum of two cleaners who can cover the property:
- Primary cleaner: your regular
- Backup cleaner: available at short notice, briefed on SOP-04, has access to the property

**Backup cleaner onboarding:** Give them SOP-04, take them through one turnover together, confirm they have the property access details.

### Cleaner Communication Template

Send this the day before every turnover:

> "Hi [NAME], reminder — cleaning at [PROPERTY NAME] tomorrow [DATE]:
> Checkout: [TIME]
> Check-in: [TIME]
> Window: [X] hours
> Previous guest: [any relevant notes e.g., "reported shower running slow"]
> Please message me when you arrive and when you're done. Thanks."

For back-to-back turnovers (same-day checkout and check-in), also specify: "Please send a photo of the bedroom and bathroom when finished."

---

## SECTION 4 — QUALITY SCORING PROTOCOL

After each cleaning, record a quality score based on the photo confirmation and any guest feedback:

**Pass:** Photos show bed made correctly, bathroom clean, kitchen surfaces clear. Guest checks in without any cleanliness comments.

**Minor Issues:** Photo shows a small issue (pillow not straight, one supply item missing), or guest mentions a minor cleanliness issue in the mid-stay message (e.g., "found a hair in the shower").

**Major Issues:** Photo shows a significant problem (bed not made, bathroom not cleaned), or guest mentions a significant cleanliness issue that requires action during the stay.

**Protocol for Major Issues:**
1. Call the cleaner immediately
2. Determine whether the guest's stay is affected
3. Offer to send the cleaner back within 2 hours if guest agrees
4. Note in TAB-05 (Maintenance Log) if any property issue contributed
5. Brief discussion with cleaner: "This is the standard I need — let me show you [specific issue]"

**If Major Issues occur 3 times in 30 days:** Schedule a full SOP-04 re-training session with the cleaner. If issues continue: find a replacement cleaner.

---

## SECTION 5 — MONTHLY CLEANING SUMMARY

At the bottom of the tab, add a monthly summary section:

| Month | Turnovers | Avg Duration (mins) | Pass Rate | Major Issues | Total Cost (€) | Fees Collected (€) |
|---|---|---|---|---|---|---|
| January | | | | | | |
| February | | | | | | |
| [continue] | | | | | | |

**Pass Rate formula:** `=COUNTIF(M2:M200,"Pass")/COUNTA(M2:M200)` — format as percentage.

**Cost Recovery Rate:** Fees Collected ÷ Total Cost. Target: ≥95%.

---

## EXAMPLE DATA

| A | B | C | D | E | F | G | H | L | M | Q |
|---|---|---|---|---|---|---|---|---|---|---|
| 18/01/2026 | HM3K5V6YB | 10:00 | HN7X2Q4PR | 15:00 | 5 | Maria Santos | ✓ | Received | Pass | 55.00 |
| 25/01/2026 | HN7X2Q4PR | 10:00 | HP4M8W9TS | 15:00 | 5 | Maria Santos | ✓ | Received | Pass | 55.00 |

---

*Last updated: v1.0.0 · Update immediately when cleaning is confirmed — do not batch-update at month end*
