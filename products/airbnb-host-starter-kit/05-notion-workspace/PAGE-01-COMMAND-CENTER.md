# PAGE-01: Command Center
## Host Command Center · Daily Operations Dashboard

---

## PAGE SETUP

**Name:** ⚡ Command Center
**Location:** Top level of workspace (pin to sidebar)
**Purpose:** This is the page you open every morning. It shows everything happening today and this week without requiring you to click through multiple databases.

---

## PAGE STRUCTURE

Build this page using Notion's block types. The layout is top-to-bottom, most urgent first.

---

### HEADER

```
⚡ [PROPERTY NAME] — Command Center
Last updated: [Notion auto-date — add with /date]
```

Add a Notion callout block in yellow:
> **Today is [date]. Check-ins: [X]. Check-outs: [X]. Open tasks: [X]. Open maintenance: [X].**

These numbers update manually during your morning check — they are prompts, not formulas. (Notion does not support live dashboard numbers on regular pages without integrations.)

---

### SECTION 1 — TODAY'S ACTIVITY

**Add a Linked Database view of DB-01 (Bookings) with these settings:**
- Title: "Today's Check-Ins and Check-Outs"
- Filter: Check-In Date = today OR Check-Out Date = today
- Columns shown: Booking Title, Status, Check-In Date, Check-Out Date, Guests, Booking Ref
- Sort: Check-In Date ascending

If no check-ins or check-outs today, this section will show empty — which is itself useful information (clear day = no urgent operations).

---

### SECTION 2 — ACTIVE STAYS

**Linked Database view of DB-01:**
- Title: "Guests Currently In Property"
- Filter: Check-In Date ≤ today AND Check-Out Date > today
- Columns: Booking Title, Guest (linked), Check-Out Date, Nights remaining (formula: `dateBetween(prop("Check-Out Date"), now(), "days")`)
- Sort: Check-Out Date ascending

---

### SECTION 3 — OPEN TASKS

**Linked Database view of DB-03 (Tasks):**
- Title: "Open Tasks"
- Filter: Status ≠ Done
- Filter: Due Date ≤ today + 3 days (tasks due within the next 3 days)
- Sort: Due Date ascending, then Priority descending
- Columns: Task Name, Due Date, Priority, Status, Booking (linked)

This shows everything due today through 72 hours from now — the operational window that requires immediate attention.

---

### SECTION 4 — UPCOMING CHECK-INS (Next 7 Days)

**Linked Database view of DB-01:**
- Title: "Next 7 Days"
- Filter: Check-In Date between today and today + 7
- Sort: Check-In Date ascending
- Columns: Booking Title, Check-In Date, Guests, Booking Ref, Pre-Arrival Sent (checkbox), Check-In Sent (checkbox)

The checkbox columns let you see at a glance which upcoming guests have received their pre-arrival messages.

---

### SECTION 5 — OPEN MAINTENANCE

**Linked Database view of DB-05 (Maintenance):**
- Title: "Open Issues"
- Filter: Status = Open OR Status = In Progress
- Sort: Severity (Critical first), then Date Reported
- Columns: Issue Title, Severity, Date Reported, Contractor Assigned, Estimated Completion

---

### SECTION 6 — MONTHLY SNAPSHOT

This section is updated manually during your monthly host review (SOP-10). It is a static text block that you update on the 1st of each month.

```
**[MONTH YEAR] Snapshot** (Updated [DATE])

Revenue: €[ACTUAL] vs. €[PROJECTED PROJECTION] — [X]% variance
Occupancy: [X]% (target: [TARGET]%)
ADR: €[X] (target: €[X])
Review Average: [X]/5 ([X] reviews this month)
Response Rate: [X]%
Superhost Criteria: [ON TRACK / AT RISK — identify which criterion]
```

---

### QUICK LINKS SECTION

Add these as Notion links or page references:

| Quick Link | Destination |
|---|---|
| Today's Tasks | DB-03 filtered by today |
| Revenue Tracker | TAB-01 Google Sheet |
| Pricing Calendar | Airbnb Calendar |
| PriceLabs Dashboard | PriceLabs.co |
| Airbnb Inbox | Airbnb Messages |
| SOP Library | Folder link to 02-sops-and-checklists |
| Message Templates | Airbnb Saved Messages |

---

## MORNING ROUTINE (5 Minutes)

Open the Command Center every morning at 8am:

1. Check Section 1 (Today's Activity): any check-ins or check-outs?
2. Check Section 3 (Open Tasks): anything due today?
3. Check Section 5 (Open Maintenance): any unresolved critical or high issues?
4. If any check-in today: confirm MSG-03 is ready and smart lock code is active
5. If any checkout today: confirm cleaning team is scheduled

That is the daily minimum. Everything else is triggered by events, not by schedule.

---

*Last updated: v1.0.0 · This is your daily starting point — bookmark it on mobile and desktop*
