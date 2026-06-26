# DB-05: Maintenance Database
## Maintenance Database Spec · Properties · Views · Issue Tracking

---

## DATABASE SETUP

**Name:** Maintenance
**Icon:** 🔧
**Location:** Full-page database in workspace root.

---

## PROPERTIES (COLUMNS)

| Property Name | Type | Values / Notes |
|---|---|---|
| Issue Title | Title | Brief description: "Boiler — no hot water" |
| Date Reported | Date | When the issue was first identified |
| Status | Select | Open / In Progress / Resolved / On Hold |
| Severity | Select | Critical / High / Medium / Low |
| Room/Area | Select | Bedroom / Bathroom / Kitchen / Living Area / Entry / Building / General |
| Reported By | Select | Guest / Cleaner / Host Inspection / Contractor |
| Description | Text | Full description of the issue |
| Photo Taken | Checkbox | ✓ when issue photographed |
| Contractor Assigned | Text | Name of contractor handling the issue |
| Contractor Phone | Text | Quick-access number |
| Date Assigned | Date | When contractor was contacted |
| Estimated Completion | Date | Contractor's ETA |
| Actual Completion | Date | When resolved |
| Cost (€) | Number | Total repair/replacement cost |
| AirCover Claim | Checkbox | ✓ if AirCover claim submitted |
| Amount Recovered (€) | Number | AirCover payment received |
| Guest Impact | Select | None / Minor / Stay Affected / Refund Issued |
| Root Cause | Select | Normal Wear / Guest Damage / Installation Failure / Age / Preventive Miss |
| Preventive Action | Text | What prevents recurrence |
| Booking | Relation | Links to DB-01: Bookings |
| Tasks | Relation | Links to DB-03: Tasks (follow-up tasks for this issue) |

---

## VIEWS TO CREATE

**View 1 — All Issues (Table)**
- Sort by Date Reported descending
- Show: Issue Title, Status, Severity, Room/Area, Contractor Assigned, Cost, Actual Completion

**View 2 — Open Issues (Filtered)**
- Filter: Status = Open OR Status = In Progress
- Sort: Severity (Critical first), then Date Reported
- **This is the view you check daily**

**View 3 — By Severity (Board)**
- Group by: Severity
- Gives a visual overview of what is critical vs. minor

**View 4 — Guest-Reported (Filtered)**
- Filter: Reported By = Guest
- These issues had direct impact on a stay — prioritise resolution and review for AirCover windows

**View 5 — AirCover Claims (Filtered)**
- Filter: AirCover Claim = ✓
- Track claim status and recovery amounts

**View 6 — Preventive Schedule (Filtered)**
- Filter: Root Cause = Preventive Miss
- Identify recurring themes to build into your SOP-08 maintenance schedule

---

## URGENCY PROTOCOL

When a Critical issue is logged:
1. Set Status = In Progress immediately
2. Link to the active booking in DB-01
3. Create a task in DB-03: "Call [CONTRACTOR] immediately" with Due Date = today
4. Set Estimated Completion
5. After resolution: record Actual Completion and update Status = Resolved

For issues where a guest is present: log the issue first (30 seconds), then call the contractor. Do not delay the call to complete the log.

---

## AirCover 14-DAY WINDOW TRACKING

In the Date Reported field, Notion can be used to track the AirCover claim deadline:

Create a formula property: `AirCover Deadline`
Formula: `dateAdd(prop("Date Reported"), 14, "days")`

Add this as a column in the Guest-Reported view. Any issue approaching its deadline (within 2 days) should be highlighted.

Conditional formatting: Turn on "Show as" → "Ring" in the formula property to highlight approaching deadlines. Or simply sort this column and check it during your weekly review.

---

## MONTHLY MAINTENANCE ANALYSIS

During SOP-10 (Monthly Host Review), filter DB-05 for the previous month and review:

- Total maintenance costs
- Number of issues by severity
- Any pattern in Room/Area (bathroom issues 3× = systemic problem)
- Root causes: how many were preventive misses?

One action item per pattern identified. Log it in DB-03 as a task.

---

*Last updated: v1.0.0 · Log every issue within 2 hours of discovery — AirCover clock starts at checkout*
