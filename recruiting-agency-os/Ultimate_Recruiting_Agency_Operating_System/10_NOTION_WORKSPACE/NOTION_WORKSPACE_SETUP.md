# Recruiting Agency Notion Workspace Setup Guide

## Overview
Your Notion workspace is organized around the full recruiting lifecycle — from business development through placement and retention.

---

## Top-Level Pages to Create

| Page Name | Icon | Purpose |
|---|---|---|
| 🎯 Business Development | Target | BD pipeline, prospect tracking |
| 👥 Clients | Building | Active client management |
| 📋 Job Orders | Clipboard | Open and filled roles |
| 🙋 Candidates | Person | Full candidate database |
| ✅ Placements | Check | Completed placements & guarantees |
| ✅ Tasks | Checkbox | Daily task management |
| 📅 Content Calendar | Calendar | LinkedIn/marketing content |
| 📚 SOP Library | Book | All agency SOPs |

---

## Step 1 — Import CSV Databases

1. Open Notion → Click **New Page** → Select **Import**
2. Choose **CSV** and upload each database file:
   - `Candidates_Database.csv`
   - `Clients_Database.csv`
   - `Job_Orders_Database.csv`
   - `Placements_Database.csv`
   - `Tasks_Database.csv`
   - `Business_Development_Database.csv`
   - `Content_Calendar_Database.csv`
   - `SOP_Library.csv`
3. After import, rename each page to match the table above.

---

## Step 2 — Set Up Database Relations

Link related databases for a connected workspace:

- **Job Orders ↔ Clients**: Every job order linked to a client
- **Candidates ↔ Job Orders**: Candidates linked to the role they're being considered for
- **Placements ↔ Candidates + Clients**: Track who was placed where
- **Tasks ↔ Job Orders + Clients**: Tasks linked to relevant searches

---

## Step 3 — Create Key Views

### Candidates Database
- **Board view**: Group by Stage (Phone Screen / Submitted / Interviewing / Offer / Placed)
- **Table view**: Full candidate list sorted by Score
- **Filter view**: "Active" — exclude Rejected

### Job Orders
- **Board view**: Group by Status (Sourcing / Active / Interviewing / Offer / Filled)
- **Calendar view**: Grouped by Start Date Target

### Tasks
- **Board view**: Group by Priority
- **Calendar view**: By Due Date

### BD Pipeline
- **Board view**: Group by Stage
- **Filter**: Show only active prospects (not Lost)

---

## Step 4 — Add Formula Properties

After import, add these calculated fields:

- **Candidates**: Days Since Screen = `dateBetween(now(), prop("Phone Screen Date"), "days")`
- **Placements**: Guarantee Remaining = `dateBetween(prop("Guarantee End"), now(), "days")`
- **Job Orders**: Days Open = `dateBetween(now(), prop("Date Opened"), "days")`

---

## Step 5 — Weekly Dashboard Page

Create a **Dashboard** page with linked database views:
- This Week's Tasks (filter: Due Date = this week)
- Active Job Orders (filter: Status = Active)
- Candidates in Offer Stage
- Overdue BD Follow-ups (filter: Next Action date past)
