# DB-01: Bookings Database
## Bookings Database Spec · Properties · Views · Entry Guide

---

## DATABASE SETUP

**Name:** Bookings
**Icon:** 📅
**Location:** Create as a full-page database in your workspace root.

---

## PROPERTIES (COLUMNS)

Create these properties in Notion. Property type in brackets.

| Property Name | Type | Values / Notes |
|---|---|---|
| Booking Title | Title | Auto-name: "[GUEST NAME] — [CHECK-IN DATE]" |
| Status | Select | Upcoming / Active / Completed / Cancelled |
| Guest | Relation | Links to DB-02: Guests |
| Check-In Date | Date | Date only (no time) |
| Check-Out Date | Date | Date only |
| Nights | Formula | `dateBetween(prop("Check-Out Date"), prop("Check-In Date"), "days")` |
| Guests | Number | Number of guests |
| Booking Ref | Text | Airbnb booking reference |
| Source | Select | Airbnb / Booking.com / VRBO / Direct |
| Accommodation Rate (€) | Number | Format: Number with prefix € |
| Cleaning Fee (€) | Number | Format: Number with prefix € |
| Gross Revenue (€) | Formula | `prop("Accommodation Rate (€)") + prop("Cleaning Fee (€)")` |
| Airbnb Fee (€) | Formula | `round(prop("Gross Revenue (€)") * 0.03 * 100) / 100` |
| Net Revenue (€) | Formula | `prop("Gross Revenue (€)") - prop("Airbnb Fee (€)")` |
| Pre-Arrival Sent | Checkbox | ✓ when MSG-02 sent |
| Check-In Sent | Checkbox | ✓ when MSG-03 sent |
| Mid-Stay Sent | Checkbox | ✓ when MSG-04 sent |
| Checkout Reminder Sent | Checkbox | ✓ when MSG-05 sent |
| Post-Checkout Sent | Checkbox | ✓ when MSG-06 sent |
| Review Request Sent | Checkbox | ✓ when MSG-07 sent |
| Review Score | Number | Overall score from guest review (1–5) |
| Review Left by Host | Select | Positive / Neutral / Negative / Not Yet |
| Special Occasion | Select | None / Birthday / Anniversary / Honeymoon / Business / Other |
| Notes | Text | Operational notes for this booking |
| Tasks | Relation | Links to DB-03: Tasks |
| Expenses | Relation | Links to DB-04: Expenses |
| Maintenance | Relation | Links to DB-05: Maintenance |

---

## VIEWS TO CREATE

**View 1 — All Bookings (Table)**
- Default view, sort by Check-In Date descending
- Show: Booking Title, Status, Check-In Date, Check-Out Date, Nights, Guests, Gross Revenue, Review Score

**View 2 — Upcoming (Filtered Table)**
- Filter: Check-In Date is on or after today
- Filter: Status = Upcoming
- Sort: Check-In Date ascending
- This is the view you check every morning

**View 3 — Active Stays (Filtered Table)**
- Filter: Check-In Date ≤ today AND Check-Out Date > today
- Status = Active

**View 4 — Calendar**
- Date property: Check-In Date
- Shows the full month view of incoming bookings

**View 5 — Revenue by Month (Table)**
- Group by: Check-In Date (by month)
- Show sum of Gross Revenue and Net Revenue for each group

---

## ENTRY PROCEDURE

Add a new entry for every booking immediately when confirmed on Airbnb:

1. Create new entry in DB-01
2. Title: "[GUEST FIRST NAME] — [CHECK-IN DATE in format DD Mon, e.g., 15 Jan]"
3. Set Status: Upcoming
4. Link Guest: Find or create guest in DB-02
5. Enter all date and revenue fields
6. Create linked tasks in DB-03 (one task per SOP trigger):
   - [48h before check-in] SOP-03: Pre-Arrival Prep
   - [Day of check-in] SOP-05: Check-In (confirm smart lock and message)
   - [Day 2] SOP-06: Mid-Stay Check-In
   - [Day before checkout] MSG-05: Checkout Reminder
   - [Day of checkout] SOP-07: Checkout + Damage Review
   - [Post-checkout] MSG-06 + MSG-07: Thank You + Review Request
   - [Post-checkout] SOP-09: Leave Guest Review

---

## ROLLUP PROPERTIES (Add After Linking Other Databases)

**Total Expenses (from DB-04):** Rollup → Expenses relation → Sum → Amount (€)

**Task Count (from DB-03):** Rollup → Tasks relation → Count all

**Tasks Completed:** Rollup → Tasks relation → Count values where Status = Done

---

*Last updated: v1.0.0 · Create this database first, before all other workspace items*
