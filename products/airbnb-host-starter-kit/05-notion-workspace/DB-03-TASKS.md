# DB-03: Tasks + SOPs Database
## Tasks Database Spec · Properties · Views · Recurring Task Templates

---

## DATABASE SETUP

**Name:** Tasks
**Icon:** ✅
**Location:** Full-page database in workspace root.

---

## PROPERTIES (COLUMNS)

| Property Name | Type | Values / Notes |
|---|---|---|
| Task Name | Title | Descriptive task name |
| Status | Select | To Do / In Progress / Done / Blocked |
| Priority | Select | High / Medium / Low |
| Due Date | Date | When this task must be completed |
| Category | Select | Booking / Maintenance / Admin / Review / Marketing / Finance |
| SOP Reference | Select | SOP-01 through SOP-10 / None |
| Booking | Relation | Links to DB-01: Bookings (for booking-specific tasks) |
| Maintenance | Relation | Links to DB-05: Maintenance (for maintenance follow-up tasks) |
| Notes | Text | Task details or instructions |
| Completed | Date | Date the task was actually completed |
| Assignee | Select | You / Cleaner / Contractor / Co-host |

---

## VIEWS TO CREATE

**View 1 — All Open Tasks (Filtered Table)**
- Filter: Status ≠ Done
- Sort: Due Date ascending
- Show: Task Name, Status, Priority, Due Date, Assignee

**View 2 — Today's Tasks (Filtered Table)**
- Filter: Due Date = today
- Filter: Status ≠ Done
- This is your morning checklist

**View 3 — Kanban Board**
- Group by: Status
- Shows all tasks in To Do / In Progress / Done columns
- Drag tasks between columns as you complete them

**View 4 — By Booking (Grouped)**
- Group by: Booking relation
- Shows all tasks associated with each booking

**View 5 — Overdue (Filtered)**
- Filter: Due Date is before today
- Filter: Status ≠ Done
- Conditional format: fill red

---

## RECURRING TASK TEMPLATES

Create these as template buttons in Notion (use the blue "Template" button in the database). Each template creates a pre-filled task entry.

**Template 1: New Booking Task Set**

When a new booking is confirmed, click this template to auto-create all required tasks for the stay:

> Task: MSG-01 Booking Confirmation | Due: Today (booking day) | SOP: None | Priority: High
> Task: SOP-03 Pre-Arrival Prep | Due: 48h before check-in | SOP: SOP-03 | Priority: High
> Task: MSG-02 Pre-Arrival Info | Due: 48h before check-in | SOP: None | Priority: High
> Task: MSG-03 Check-In Instructions | Due: Morning of check-in | SOP: None | Priority: High
> Task: MSG-04 Mid-Stay Check-In | Due: Day 2 of stay | SOP: SOP-06 | Priority: Medium
> Task: MSG-05 Checkout Reminder | Due: Evening before checkout | SOP: None | Priority: High
> Task: SOP-07 Checkout + Damage Review | Due: Day of checkout | SOP: SOP-07 | Priority: High
> Task: MSG-06 Post-Checkout Thanks | Due: Day of checkout +3h | SOP: None | Priority: Medium
> Task: MSG-07 Review Request | Due: Day of checkout +6h | SOP: SOP-09 | Priority: Medium
> Task: Leave Host Review | Due: Day of checkout +24h | SOP: SOP-09 | Priority: Medium
> Task: SOP-04 Cleaning Confirmed | Due: Day of checkout | SOP: SOP-04 | Priority: High

**Template 2: Maintenance Issue**

> Task: Contact Contractor | Due: Today | Category: Maintenance | Priority: [Set by severity] | SOP: SOP-08
> Task: Confirm Resolution | Due: [Contractor estimated date] | Category: Maintenance | Priority: Medium
> Task: Check AirCover Claim Window (14 days) | Due: +14 days from checkout | Category: Admin | Priority: High

**Template 3: Monthly Review**

> Task: Pull Revenue Data from TAB-01 | Due: 1st of month | Category: Finance | SOP: SOP-10 | Priority: High
> Task: Pull Expense Data from TAB-02 | Due: 1st of month | Category: Finance | SOP: SOP-10 | Priority: High
> Task: Review TAB-06 Review Scores | Due: 1st of month | Category: Review | SOP: SOP-10 | Priority: Medium
> Task: Check Superhost Criteria | Due: 1st of month | Category: Admin | SOP: SOP-10 | Priority: Medium
> Task: Review Next 30-Day Calendar | Due: 1st of month | Category: Booking | SOP: SOP-10 | Priority: Medium

---

## TASK ENTRY PROCEDURE

For booking-specific tasks: use Template 1 at booking confirmation time. Link all tasks to the booking in DB-01.

For ad hoc tasks: create a new entry, set Due Date, link to relevant database record, assign to the responsible person.

Mark tasks as Done immediately when completed — do not batch-update at end of week. The value of the task database is real-time visibility into what is open.

---

*Last updated: v1.0.0 · Set up templates before your first booking is confirmed*
