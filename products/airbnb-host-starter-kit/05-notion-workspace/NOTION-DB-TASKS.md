# Notion Database: Tasks & SOPs
## Complete Build Specification

---

## DATABASE SETUP

**Name:** ✅ Tasks & SOPs  
**Icon:** ✅  
**Type:** Full-page database  
**Location:** Workspace root; linked to Command Center

---

## PROPERTIES (FIELDS)

| Property Name | Type | Options / Notes |
|---|---|---|
| Task Name | Title | Descriptive name |
| Type | Select | SOP / Task / Maintenance / Improvement / Seasonal |
| Status | Select | Not Started / In Progress / Completed / Blocked / Recurring Template |
| Priority | Select | P1-Critical / P2-High / P3-Standard / P4-Low |
| Assigned To | Person or Select | Host / Cleaner / Contractor / Co-Host |
| Related Booking | Relation | → Links to Bookings Database (for booking-specific tasks) |
| Due Date | Date | |
| Repeat | Select | One-Time / Every Booking / Weekly / Monthly / Quarterly / Annually |
| SOP Reference | Text | e.g., "SOP-04" — links to the SOP document |
| Description | Text | Full task description or abbreviated SOP |
| Completed Date | Date | |
| Notes | Text | |

---

## VIEWS

### View 1: Active Tasks (DEFAULT)
- **Type:** Board (Kanban)
- **Group by:** Status
- **Filter:** Status ≠ "Completed" AND Status ≠ "Recurring Template"
- **Columns:** Not Started | In Progress | Blocked
- **Purpose:** See what's in progress and what's stuck

### View 2: Upcoming by Due Date
- **Type:** Table
- **Filter:** Due Date is "Next 7 days" OR Due Date is "This week"
- **Sort:** Due Date ascending
- **Visible columns:** Task Name, Type, Status, Priority, Assigned To, Due Date

### View 3: SOP Templates (Recurring Tasks)
- **Type:** Table
- **Filter:** Status = "Recurring Template"
- **Visible columns:** Task Name, Repeat, SOP Reference, Assigned To
- **Purpose:** Library of all recurring tasks — duplicate these to create actual task instances

### View 4: Completed Archive
- **Type:** Table
- **Filter:** Status = "Completed"
- **Sort:** Completed Date descending

### View 5: Per-Booking Tasks (created from Active Booking)
- **Type:** Table
- **Filter:** Related Booking = [current booking]
- **Visible columns:** Task Name, Status, Assigned To, Due Date
- **Purpose:** From any booking page, see all tasks for that booking

---

## CORE SOP TEMPLATES TO ADD ON DAY 1

Create these 10 entries in the Tasks database with Status = "Recurring Template":

| Task Name | SOP Ref | Repeat | Assigned To |
|---|---|---|---|
| Turnover Cleaning | SOP-04 | Every Booking | Cleaner |
| Pre-Arrival Prep | SOP-03 | Every Booking | Host |
| Check-In Process | SOP-05 | Every Booking | Host |
| Mid-Stay Check-In | SOP-06 | Every Booking | Host |
| Checkout Process | SOP-07 | Every Booking | Host |
| Review Collection | SOP-09 | Every Booking | Host |
| Guest Screening | SOP-02 | Every Booking | Host |
| Monthly Host Review | SOP-10 | Monthly | Host |
| Listing Optimisation | Platform Guide | Quarterly | Host |
| Property Maintenance Audit | SOP-08 | Quarterly | Host |

When a new booking is created, duplicate the relevant SOP templates and link them to that booking.

---

## USING THE KANBAN BOARD

The board view is your daily operational view. Each morning, open the Board view and:
1. Move any "Not Started" items that are due today to "In Progress"
2. Check "In Progress" items for blockers
3. Move completed items to "Completed"

This is the most effective 5-minute daily hosting habit.
