# Bookkeeper Practice Notion Workspace - Setup Guide

## Step 1: Create Your Workspace
1. Open Notion and click **+ New page** in the sidebar
2. Name it: **Bookkeeping Practice OS**
3. Set the icon to a calculator or money emoji

## Step 2: Import Your Databases
For each CSV file in this folder:
1. Create a new page inside your workspace
2. Click the `/` command and choose **Table - Full page**
3. Click the **...** menu > **Import** > **CSV**
4. Select the file and map columns

## Databases to Import:
- `Notion_Client_Roster.csv` → Your master client list
- `Notion_Monthly_Task_Board.csv` → Monthly work tracker
- `Notion_Expense_Log.csv` → Business expense tracking
- `Notion_Lead_Pipeline.csv` → Prospect tracking
- `Notion_Invoice_Log.csv` → Invoice and payment tracking

## Step 3: Link Databases
- Add a **Relation** property to Task Board linking to Client Roster
- Add a **Relation** property to Invoice Log linking to Client Roster
- This creates a connected workspace where all data ties together

## Step 4: Add Views
For the Task Board, add these views:
- **Board view** (Kanban): Group by Status
- **Calendar view**: Group by Due Date
- **Filter by Month**: For monthly planning
