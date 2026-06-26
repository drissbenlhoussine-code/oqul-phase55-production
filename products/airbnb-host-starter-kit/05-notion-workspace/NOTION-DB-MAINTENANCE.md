# Notion Database: Maintenance
## Complete Build Specification

---

## DATABASE SETUP

**Name:** 🔧 Maintenance  
**Icon:** 🔧  
**Type:** Full-page database  
**Location:** Workspace root; linked to Command Center

---

## PROPERTIES (FIELDS)

| Property Name | Type | Options / Notes |
|---|---|---|
| Issue Name | Title | Brief, specific description |
| Date Reported | Date | When the issue was discovered |
| Reported By | Select | Guest / Host / Cleaner / Inspection |
| Priority | Select | P1-Emergency / P2-Urgent / P3-Standard / P4-Cosmetic |
| Category | Select | Plumbing / Electrical / Heating / AC / Smart Lock / WiFi / Kitchen Appliance / Laundry / Furniture / Flooring / Walls / Windows / Outdoor / Cleaning / Structural / Other |
| Location | Select | Entrance / Living Room / Bedroom 1 / Bedroom 2 / Bathroom / Kitchen / Utility / Outdoor / Whole Property |
| Status | Select | Open / In Progress / Awaiting Parts / Completed / Deferred |
| Assigned To | Text | Contractor name or "Self" |
| Contractor Phone | Phone | |
| Date Scheduled | Date | When repair is booked |
| Date Completed | Date | When repair was confirmed done |
| Cost (€) | Number | Currency format |
| Guest Compensation | Number | Currency format (€0 if none) |
| Related Booking | Relation | → Bookings Database |
| Root Cause | Text | Why did this happen? |
| Preventive Action | Text | What prevents recurrence? |
| Photos | Files & Media | Before/after photos |
| Notes | Text | |

---

## VIEWS

### View 1: Open Issues (DEFAULT)
- **Type:** Board (Kanban)
- **Group by:** Priority
- **Filter:** Status ≠ "Completed" AND Status ≠ "Deferred"
- **Columns:** P1-Emergency | P2-Urgent | P3-Standard | P4-Cosmetic
- **Purpose:** See open issues by urgency at a glance

### View 2: All Issues Table
- **Type:** Table
- **Filter:** None
- **Sort:** Date Reported descending
- **Visible columns:** Issue Name, Priority, Category, Status, Assigned To, Date Scheduled, Cost

### View 3: This Month's Issues
- **Type:** Table
- **Filter:** Date Reported is "This month"
- **Show aggregate:** Sum of Cost (total maintenance spend this month)

### View 4: Preventive Maintenance Calendar
- **Type:** Calendar
- **Calendar by:** Date Scheduled
- **Filter:** Reported By = "Host" (planned maintenance only, not reactive)
- **Purpose:** See upcoming scheduled maintenance on a calendar

### View 5: Recurring Issues Watch
- **Type:** Table
- **Filter:** Issues with the same Category appearing 2+ times
- **Purpose:** Identify systematic problems (requires manual filtering or Notion formula)

---

## TEMPLATE: "New Issue"

Auto-populates:
- Date Reported: Today
- Status: Open
- Reported By: Guest (most common trigger — change as needed)

---

## ESCALATION NOTIFICATIONS

Set up Notion reminders on the Date Scheduled field:
- P1 issues: remind 1 hour before scheduled repair
- P2 issues: remind same morning as scheduled repair
- P3 issues: remind day before scheduled repair

To set: open any issue entry → click Date Scheduled → click "Remind me" → set timing

This ensures no repair appointment is ever missed.
