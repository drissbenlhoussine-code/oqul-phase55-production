# AI SMMA Operating System — Notion Setup Guide

## Step 1: Create Your Notion Workspace

1. Go to notion.so and create a free account (or use your existing workspace)
2. Create a new page called "SMMA Agency Dashboard"
3. This will be your master hub — all databases will live here

## Step 2: Import Each Database

For each of the 7 CSV files in this folder:
1. In Notion, create a new page inside your dashboard
2. Type `/table` and select "Table - Full page"
3. Click "Import" in the top menu → CSV
4. Select the CSV file and click Import
5. Notion will create a database with all your data

**Import order:**
1. Notion_Client_Database.csv → Name: "Clients"
2. Notion_Lead_Tracker.csv → Name: "Lead Pipeline"
3. Notion_Content_Calendar.csv → Name: "Content Calendar"
4. Notion_Task_Board.csv → Name: "Task Board"
5. Notion_Proposal_Pipeline.csv → Name: "Proposals"
6. Notion_Invoice_Log.csv → Name: "Invoices"
7. Notion_Referral_Partners.csv → Name: "Referral Partners"

## Step 3: Create Linked Views

After importing, create linked database views on your main dashboard:
- Filter "Clients" by Status = Active → "Active Clients" view
- Filter "Task Board" by Status = In Progress → "Today's Tasks" view
- Filter "Lead Pipeline" by Stage = Discovery Call → "Hot Leads" view
- Filter "Content Calendar" by this week → "This Week's Content" view

## Step 4: Customize Properties

Add these calculated properties:
- In Clients DB: "Days as Client" = formula using Start Date
- In Task Board: "Overdue" = formula checking Due Date vs today
- In Invoices: "Days Outstanding" = formula for unpaid invoices

## Step 5: Daily Use

**Morning routine (10 mins):**
1. Open Task Board → filter by today → work on high-priority tasks
2. Check Content Calendar → confirm today's posts are scheduled
3. Review Lead Pipeline → any follow-ups needed today?

**End of month (2 hrs):**
1. Update all Client health scores
2. Create new month's content calendar rows
3. Generate invoices and log in Invoice DB
