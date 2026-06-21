# Notion Client Portal - Complete Setup Guide

## Overview
This Notion Client Portal system gives your agency and clients a shared workspace for project management, approvals, communication, and reporting.

## Step 1: Create Your Agency Workspace
1. Go to Notion.so and create a new workspace called "[Agency Name] Operations"
2. This is YOUR internal workspace -- clients won't see this

## Step 2: Create Client Portals
For each client:
1. Create a new Page called "[Client Name] Portal"
2. Set the page icon to their logo or brand color
3. Share ONLY this page with the client (not your full workspace)

## Step 3: Import Databases
Import each CSV from 01_CLIENT_PORTAL_DATABASES:
- `Client_Master_Database.csv` -- Internal client tracking (don't share with clients)
- `Project_Tracker.csv` -- Share with clients (filtered to their projects only)
- `Content_Calendar.csv` -- Share with clients for content approval
- `Invoice_and_Payments.csv` -- Internal only
- `Analytics_Report_Log.csv` -- Internal tracking

## Step 4: Client Portal Page Structure
Each client portal should have:
```
[Client Name] Portal
  |-- Welcome & Quick Links
  |-- Content Calendar (linked database, filtered to this client)
  |-- Project Status (linked database, filtered to this client)
  |-- Monthly Reports (archived reports)
  |-- Deliverables (file uploads)
  |-- Brand Assets (their logos, colors, fonts)
  |-- Meeting Notes
```

## Step 5: Set Up Sharing
- Click Share on the client portal page
- Enter client's email address
- Set permission to "Can Comment" (so they can approve content)
- Do NOT give "Full Access" -- clients shouldn't edit your databases

## Step 6: Content Approval Workflow in Notion
1. Create content as a Notion page inside the Content Calendar database
2. Set status to "Ready for Review"
3. Client opens the page and leaves a comment: "Approved" or feedback
4. You update status to "Approved" or "Needs Revision"

## Notion Features to Use
- **Synced Blocks**: Same content block appears on multiple pages
- **Database Filters**: Show clients only their projects/content
- **Database Views**: Give clients a clean Calendar view of their content
- **Comments**: Client approvals tracked as comments on content pages
- **Notion AI**: Generate content ideas, draft reports, summarize meetings

## Common Questions
Q: Can clients accidentally see other clients' data?
A: No -- share only their specific Portal page, not the databases directly.

Q: How do clients approve content?
A: They comment on the content page in Notion. Set up a "Needs Approval" status and the client changes it to "Approved".
