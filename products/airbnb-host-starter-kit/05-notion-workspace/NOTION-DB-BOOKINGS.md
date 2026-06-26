# Notion Database: Bookings
## Complete Build Specification

---

## DATABASE SETUP

**Name:** 📅 Bookings  
**Icon:** 📅  
**Type:** Full-page database (not inline)  
**Location:** Create at the root of your workspace, then link to Command Center

---

## PROPERTIES (FIELDS)

Build each property in this exact order:

| Property Name | Type | Options / Notes |
|---|---|---|
| Booking Title | Title | Auto-format: "[Guest Name] — [Dates]" |
| Status | Select | Confirmed / Checked In / Active / Checked Out / Completed / Cancelled |
| Guest | Relation | → Links to Guests Database |
| Check-In Date | Date | Date only (no time) |
| Check-Out Date | Date | Date only (no time) |
| Nights | Formula | `dateBetween(prop("Check-Out Date"), prop("Check-In Date"), "days")` |
| Nightly Rate | Number | Currency format: €_ |
| Gross Booking Value | Number | Currency format: €_ |
| Cleaning Fee | Number | Currency format: €_ |
| Net Revenue | Formula | `prop("Gross Booking Value") * 0.97` |
| Number of Guests | Number | Integer |
| Airbnb Booking Ref | Text | e.g., HM123456789 |
| Pre-Arrival Msg | Checkbox | Default: unchecked |
| Check-In Msg | Checkbox | Default: unchecked |
| Mid-Stay Msg | Checkbox | Default: unchecked |
| Checkout Msg | Checkbox | Default: unchecked |
| Review Request | Checkbox | Default: unchecked |
| Review Received | Select | Pending / 5 Stars / 4 Stars / 3 Stars / Below 3 / No Review |
| Star Rating | Number | 1–5 |
| Issues During Stay | Text | Free text |
| Damage Claim | Select | None / Filed / Resolved |
| Notes | Text | Free text |
| Month | Formula | `formatDate(prop("Check-In Date"), "MMMM YYYY")` |
| Turnover Required | Checkbox | Auto-check on every new booking |

---

## VIEWS

### View 1: Active Bookings (DEFAULT VIEW)
- **Type:** Table
- **Filter:** Status is NOT "Completed" AND Status is NOT "Cancelled"
- **Sort:** Check-In Date ascending
- **Visible columns:** Booking Title, Status, Check-In Date, Check-Out Date, Nights, Guest, Net Revenue
- **Group by:** None

### View 2: This Month Calendar
- **Type:** Calendar
- **Calendar by:** Check-In Date
- **Filter:** Check-In Date is "This month"
- **Purpose:** Visual calendar of arrival dates

### View 3: Communication Checklist
- **Type:** Table
- **Filter:** Status = "Confirmed" or "Checked In" or "Active"
- **Visible columns:** Booking Title, Guest, Check-In Date, Pre-Arrival Msg, Check-In Msg, Mid-Stay Msg, Checkout Msg, Review Request
- **Conditional formatting:** Unchecked boxes for dates that have passed = red flag
- **Purpose:** Track messaging compliance at a glance

### View 4: Revenue by Month
- **Type:** Table
- **Group by:** Month
- **Show aggregates:** Sum of Net Revenue, Count of Bookings
- **Sort:** Month ascending
- **Purpose:** Monthly revenue rollup

### View 5: Completed Bookings Archive
- **Type:** Table
- **Filter:** Status = "Completed"
- **Sort:** Check-Out Date descending
- **Purpose:** Historical record

---

## TEMPLATE: "New Booking"

When creating a new booking from this template, the following fields auto-populate:
- Status: Confirmed
- Turnover Required: ✓ (checked)
- All message checkboxes: unchecked (to-do)

---

## RELATIONS & ROLLUPS

**Relation to Guests Database:**
- Property: Guest (Relation)
- This links the booking to the guest's profile
- In the Guests database, this shows as "Bookings" rollup (count of times this guest has booked)
