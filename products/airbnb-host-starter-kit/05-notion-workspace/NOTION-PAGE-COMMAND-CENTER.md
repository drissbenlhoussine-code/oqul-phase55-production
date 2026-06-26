# Notion Page: Command Center
## Complete Build Specification

---

## PAGE SETUP

**Title:** 🎯 Command Center  
**Icon:** 🎯  
**Location:** Top level of workspace (pin as favourite)  
**Purpose:** The one page you open every morning. Everything you need to run today's operations without navigating the full workspace.

---

## PAGE STRUCTURE

Build the page in this exact order, top to bottom:

---

### BLOCK 1: HEADER

```
# 🎯 [Property Name] — Command Center

> "What needs attention today?"
```

Add a divider below.

---

### BLOCK 2: TODAY AT A GLANCE

Create 3 columns (use the `/columns` command in Notion):

**Column 1 — Today's Check-Ins**
- Insert a linked view of the Bookings database
- Filter: Check-In Date = Today
- View type: List
- Show: Booking Title, Guest name, Number of Guests
- Title: "✈️ Arriving Today"

**Column 2 — Today's Check-Outs**
- Insert a linked view of the Bookings database
- Filter: Check-Out Date = Today
- View type: List
- Show: Booking Title, Guest name
- Title: "🧳 Checking Out Today"

**Column 3 — Open Maintenance Issues**
- Insert a linked view of the Maintenance database
- Filter: Status = "Open" OR Status = "In Progress"
- View type: List
- Show: Issue Name, Priority
- Title: "🔧 Open Issues"

---

### BLOCK 3: COMMUNICATION CHECKLIST

- Insert a linked view of the Bookings database
- Filter: Status = "Confirmed" OR Status = "Active" OR Status = "Checked In"
- View type: Table
- Show columns: Booking Title, Guest, Check-In Date, Pre-Arrival Msg ✓, Check-In Msg ✓, Mid-Stay Msg ✓, Checkout Msg ✓, Review Request ✓
- Title: "📋 Communication Status — Active Bookings"
- Sort: Check-In Date ascending

*This block shows at a glance which guests still need a message. Unchecked boxes are your to-do list.*

---

### BLOCK 4: THIS WEEK'S CALENDAR

- Insert a linked view of the Bookings database
- View type: Calendar
- Calendar by: Check-In Date
- Filter: Check-In Date is "This week"
- Title: "📅 This Week"

---

### BLOCK 5: REVENUE SNAPSHOT

- Insert a linked view of the Bookings database
- View type: Table
- Group by: Month
- Filter: Check-In Date is "This year"
- Aggregate: Sum of Net Revenue, Count of Bookings
- Show: Month, Bookings count, Net Revenue sum
- Title: "💰 Revenue This Year"

---

### BLOCK 6: ACTIVE TASKS

- Insert a linked view of the Tasks & SOPs database
- Filter: Status = "In Progress" OR (Status = "Not Started" AND Due Date is "This week")
- View type: List
- Show: Task Name, Status, Due Date, Assigned To
- Title: "✅ Active Tasks"

---

### BLOCK 7: QUICK LINKS

Create a simple list of links to the most-used documents:

```
## 🔗 Quick Links

- [[📅 Bookings Database]]
- [[👤 Guests Database]]
- [[🔧 Maintenance Database]]
- [[💰 Expenses Database]]
- [[SOP-04 Turnover Cleaning]]
- [[SOP-03 Pre-Arrival Prep]]
- [[Pricing Strategy Playbook]]
- [[Guest Experience Standards]]
```

---

## DAILY USE WORKFLOW (5 Minutes)

1. Open Command Center
2. Block 2: Check today's arrivals and departures
3. Block 3: Send any pending messages (check unchecked boxes)
4. Block 6: Update task statuses — what's done? What's next?
5. Block "Open Issues": Any new issues to address?

This takes 5 minutes. Everything else in the workspace is for deeper work during your monthly review.
