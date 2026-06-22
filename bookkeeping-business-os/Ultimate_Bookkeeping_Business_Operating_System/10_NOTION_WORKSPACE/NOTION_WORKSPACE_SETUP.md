# Bookkeeping Business Notion Workspace Setup

## Overview
Your Notion workspace organizes every aspect of your bookkeeping practice — from client management to monthly deadlines, document tracking, and SOP library.

---

## Top-Level Pages to Create

| Page Name | Icon | Purpose |
|---|---|---|
| 👥 Clients | People | All client accounts and service details |
| ✅ Tasks | Checkbox | Daily and weekly task management |
| 📅 Monthly Deadlines | Calendar | Track every close and filing deadline |
| 📄 Document Requests | Folder | Track outstanding documents per client |
| 🛠 Services | Gear | Your service menu and pricing |
| 📚 SOP Library | Book | All operating procedures |
| 📊 Dashboard | Chart | Linked view of key items across all databases |

---

## Step 1 — Import CSV Files

1. Open Notion → New Page → Import → CSV
2. Upload each file:
   - `Clients_Database.csv`
   - `Tasks_Database.csv`
   - `Monthly_Deadlines_Database.csv`
   - `Document_Requests_Database.csv`
   - `Services_Database.csv`
   - `SOP_Library.csv`
3. Rename each imported page to match the table above.

---

## Step 2 — Set Up Database Relations

- **Tasks ↔ Clients**: Every task linked to a client (or "Internal" for non-client work)
- **Monthly Deadlines ↔ Clients**: Each deadline linked to a specific client
- **Document Requests ↔ Clients**: Track outstanding documents by client

---

## Step 3 — Recommended Views

### Clients Database
- **Table view**: All clients sorted by start date
- **Filter: Active**: Show only Status = Active
- **Gallery view**: Quick visual overview

### Tasks Database
- **Board view**: Group by Priority (Urgent / High / Medium / Low)
- **Calendar view**: By Due Date
- **Filter: This Week**: Due Date = this week

### Monthly Deadlines
- **Calendar view**: By Due Date — visual close schedule
- **Filter: In Progress**: Status = In Progress or Upcoming
- **Sort: Due Date ascending**: See what's due soonest

---

## Step 4 — Build Your Dashboard Page

Create a Dashboard page with these linked database views:
- Overdue tasks (filter: Due Date < today, Status ≠ Complete)
- In-progress deadlines (filter: Status = In Progress)
- Outstanding document requests (filter: Status = Pending)
- Clients due for monthly report this week

---

## Step 5 — Monthly Close Workflow in Notion

1. Start of month: Tasks auto-populate via template (set up recurring task template)
2. Daily: Update task status as work is completed
3. Mid-month: Check Monthly Deadlines calendar; send any outstanding Document Requests
4. By delivery date: Mark deadline as Complete; log delivery date in Clients database
