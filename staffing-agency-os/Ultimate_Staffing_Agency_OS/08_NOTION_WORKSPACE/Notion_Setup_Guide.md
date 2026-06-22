# Staffing Agency OS - Notion Workspace Setup Guide

## Step 1: Create Your Workspace
1. Open Notion, click **+ New page** in sidebar
2. Name the page: **Staffing Agency OS**
3. Set your agency icon or logo

## Step 2: Import Databases
Import each CSV file into Notion:
- `Notion_Candidate_Database.csv` -- Your master talent database
- `Notion_Job_Orders.csv` -- Active and filled job orders
- `Notion_Activity_Log.csv` -- Daily activity tracking
- `Notion_Placement_Log.csv` -- Completed placements and invoices

## Step 3: Link Databases Together
- Connect **Job Orders** to **Candidates** via Relation property
- Connect **Placement Log** to both **Candidates** and **Job Orders**
- Connect **Activity Log** to **Candidates** (optional)

## Step 4: Views to Create
For Candidate Database:
- **Board view** grouped by Status (Sourced / Pre-screened / Submitted / Placed)
- **Filter** by Available candidates only

For Job Orders:
- **Board view** grouped by Status
- **Table view** with all details visible

## Step 5: Daily Dashboard
Create a main dashboard page with:
- Linked view of today's follow-up tasks
- Linked view of active job orders
- Linked view of recent activity
