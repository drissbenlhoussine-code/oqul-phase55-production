# Notion Workspace Overview
## Master Workspace Map · Build Order · Database Relationships

---

## HOW TO USE THIS DOCUMENT

Build the Notion workspace in the order listed in Section 2. Each database must exist before the pages that reference it. The build takes approximately 3–4 hours for a new Notion user; 90 minutes for an experienced one.

**Prerequisite:** A Notion account (free plan supports this entire workspace). Notion app installed on your phone — you will use it during stays to check booking details and log maintenance notes.

---

## SECTION 1 — WORKSPACE ARCHITECTURE

```
[HOST NAME]'s Property Workspace
│
├── 🏠 Property Hub (PAGE-02)
│   ├── Property details, appliance info, contractor list
│   └── Links to all 5 databases
│
├── ⚡ Command Center (PAGE-01)
│   ├── Today's check-ins and check-outs (filtered DB-01 view)
│   ├── Open tasks (filtered DB-03 view)
│   ├── Recent maintenance issues (filtered DB-05 view)
│   └── This month's revenue snapshot
│
├── 📅 Weekly Review (PAGE-03)
│   └── Structured weekly ops review template
│
├── 📦 Databases (5 total)
│   ├── DB-01: Bookings
│   ├── DB-02: Guests
│   ├── DB-03: Tasks + SOPs
│   ├── DB-04: Expenses
│   └── DB-05: Maintenance
```

---

## SECTION 2 — BUILD ORDER

Build in this sequence. Databases first, then pages that reference them.

| Order | Item | File | Time |
|---|---|---|---|
| 1 | DB-01: Bookings | DB-01-BOOKINGS.md | 20 min |
| 2 | DB-02: Guests | DB-02-GUESTS.md | 15 min |
| 3 | DB-03: Tasks | DB-03-TASKS.md | 20 min |
| 4 | DB-04: Expenses | DB-04-EXPENSES.md | 20 min |
| 5 | DB-05: Maintenance | DB-05-MAINTENANCE.md | 15 min |
| 6 | PAGE-02: Property Hub | PAGE-02-PROPERTY-HUB.md | 20 min |
| 7 | PAGE-01: Command Center | PAGE-01-COMMAND-CENTER.md | 25 min |
| 8 | PAGE-03: Weekly Review | PAGE-03-WEEKLY-REVIEW.md | 10 min |

**Total: ~2.5 hours** if you have all your property details to hand.

---

## SECTION 3 — DATABASE RELATIONSHIPS

Notion databases are linked using the "Relation" property type. These links power the rollup summaries across the workspace.

| Relation | From | To | Property Name | Purpose |
|---|---|---|---|---|
| Guest linked to booking | DB-02: Guests | DB-01: Bookings | "Bookings" | See all bookings for each guest |
| Booking linked to guest | DB-01: Bookings | DB-02: Guests | "Guest" | Link each booking to a guest record |
| Task linked to booking | DB-03: Tasks | DB-01: Bookings | "Booking" | Link SOP tasks to a specific booking |
| Expense linked to booking | DB-04: Expenses | DB-01: Bookings | "Booking Ref" | Link variable costs to specific stays |
| Maintenance linked to booking | DB-05: Maintenance | DB-01: Bookings | "Booking Ref" | Link issues to the stay that triggered them |

---

## SECTION 4 — VIEWS TO CREATE IN EACH DATABASE

Each database should have multiple views for different operational contexts:

**DB-01: Bookings**
- Table view: All bookings, default sort by check-in date descending
- Calendar view: Check-in dates calendar
- Board view: Grouped by Status (Upcoming / Active / Completed / Cancelled)
- Filtered table: Active stays only (Check-In ≤ today AND Check-Out > today)

**DB-02: Guests**
- Table view: All guests, sort by last stay date
- Gallery view: Guest profile cards
- Filtered table: Guests with 2+ stays (repeat guests)

**DB-03: Tasks**
- Table view: All tasks
- Board view (Kanban): Grouped by Status (To Do / In Progress / Done)
- Filtered table: Open tasks only (Status ≠ Done)
- Filtered table: Upcoming booking tasks (filter by related booking check-in date)

**DB-04: Expenses**
- Table view: All expenses, sort by date descending
- Filtered table: Current month only
- Grouped table: By Category

**DB-05: Maintenance**
- Table view: All issues
- Board view: Grouped by Severity
- Filtered table: Open issues only (Status = Open or In Progress)

---

## SECTION 5 — PHONE SETUP

Install the Notion mobile app. Pin these views to your sidebar for quick access during operations:

1. Command Center (PAGE-01) — for daily check at 8am
2. DB-01 Active Stays view — to check guest status at any time
3. DB-03 Open Tasks view — for task completion on the go
4. DB-05 Open Issues view — to log and track maintenance

On Android: Notion has a home screen widget for quick database entry. Set this up for DB-05 (Maintenance) — logging issues on the spot prevents forgetting to record them later.

---

*Last updated: v1.0.0 · Build databases before pages — the page links will fail otherwise*
