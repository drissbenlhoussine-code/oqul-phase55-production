# Insurance Agency OS — Notion Workspace Setup Guide

## Overview
This guide walks you through importing your 7 Insurance Agency OS databases into Notion, creating your complete digital agency management system in under 30 minutes.

## Files Included
| File | Notion Database | Purpose |
|------|----------------|---------|
| Lead_Database.csv | Lead Database | Track all incoming prospects |
| Client_Database.csv | Client Database | Manage your book of business |
| Claims_Tracker.csv | Claims Tracker | Monitor open and closed claims |
| Referral_Partner_Database.csv | Partner Network | Manage COI relationships |
| Policy_Renewal_Queue.csv | Renewal Queue | Never miss a renewal |
| Producer_Activity_Log.csv | Activity Log | Track daily sales activities |
| Commission_Tracker.csv | Commission Tracker | Monitor revenue by carrier |

## Import Instructions

### Step 1 — Create Your Agency Hub
1. Open Notion and click **+ New Page**
2. Title it: "Insurance Agency OS"
3. Add icon: 🛡️ and a professional cover image

### Step 2 — Import Each Database
For each CSV file:
1. Click **+ New Page** inside your Agency OS page
2. Select **Import** → **CSV**
3. Upload the CSV file → Click **Import**
4. Notion creates a table database automatically

### Step 3 — Recommended Views Per Database

**Lead Database:**
- Table View (default): All leads
- Board View: Group by Status (Hot/Warm/Cold)
- Filter View: "Hot Leads" — Status = Hot, sorted by Last Contact
- Filter View: "Follow Up Today" — Next Action date = Today

**Policy Renewal Queue:**
- Table View: All renewals
- Board View: Group by Priority (HIGH/MEDIUM/LOW)
- Calendar View: Group by Renewal Date
- Filter View: "Urgent" — Priority = HIGH

**Claims Tracker:**
- Table View: All claims
- Board View: Group by Status (Open/Settled)
- Filter View: "Open Claims" — Status = Open, sorted by Days Open

### Step 4 — Link Your Databases
1. In **Claims Tracker**: Add Relation → Client Database
2. In **Policy Renewal Queue**: Add Relation → Client Database
3. In **Producer Activity Log**: Add Relation → Lead Database

### Step 5 — Daily Dashboard Page
Create a "Daily Dashboard" page with linked views:
- Hot Leads (filtered from Lead Database)
- Today's Follow-Ups (filtered from Activity Log)
- Urgent Renewals (filtered from Renewal Queue)
- Open Claims requiring action

## Pro Tips
- Log every client contact in Producer Activity Log same day
- Update Lead Status immediately after each conversation
- Set Renewal Queue reminders 90 days in advance
- Review Commission Tracker monthly to verify carrier payments

---
*Insurance Agency Operating System | Professional Edition*
*Original Price: €149 | Your Price: €39*
