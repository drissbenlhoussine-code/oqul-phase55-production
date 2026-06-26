# Notion Page: Weekly Review
## Complete Build Specification

---

## PAGE SETUP

**Title:** 📆 Weekly Review  
**Icon:** 📆  
**Location:** Top level of workspace  
**Purpose:** 20-minute weekly operational check — reviews the past 7 days and prepares the next 7

---

## PAGE STRUCTURE

Build as a template that you duplicate each Sunday evening:

---

### BLOCK 1: HEADER

```
# 📆 Weekly Review — Week of [DATE]

**Completed by:** [Host name]  
**Review date:** [Date]  
**Next review due:** [Date + 7 days]
```

---

### BLOCK 2: LAST WEEK AT A GLANCE

```
## ✅ Last Week Summary

**Checkouts:** [Number]
**Check-ins:** [Number]
**Active bookings:** [Number]
**Maintenance issues opened:** [Number]
**Maintenance issues resolved:** [Number]
**Messages sent on time:** [All / X missed]
**Reviews received:** [Number] | Average: [Rating]
```

Fill this in manually by referencing your Bookings and Maintenance databases.

---

### BLOCK 3: REVENUE CHECK (LINKED VIEW)

- Insert linked view of Bookings database
- Filter: Check-Out Date is "Last 7 days"
- Show: Booking Title, Guest, Nights, Net Revenue
- Show aggregate: Sum of Net Revenue

Title: "💰 Revenue — Last 7 Days"

---

### BLOCK 4: PRICING REVIEW

```
## 💲 Pricing Check — Next 30 Days

**Current 30-day occupancy:** ___% ([X] nights booked / [Y] available)
**Target occupancy:** 72%

**Action needed?**
[ ] No action — on track
[ ] Apply 10% discount to [specific open dates]
[ ] Raise rates — dates booking faster than expected
[ ] Check for upcoming local events (check [city event calendar])

**Rates set for next 30 days:**
[ ] Weekend premium active (+25%)
[ ] Seasonal adjustments applied
[ ] Last-minute gaps (< 5 days out) set to 1-night minimum
```

---

### BLOCK 5: UPCOMING CHECK-INS PREP

- Insert linked view of Bookings database
- Filter: Check-In Date is "Next 7 days" AND Status = "Confirmed"
- Show: Booking Title, Guest, Check-In Date, Pre-Arrival Msg, Check-In Msg

Title: "✈️ Arrivals This Week — Ready?"

---

### BLOCK 6: OPEN TASKS THIS WEEK

- Insert linked view of Tasks & SOPs database
- Filter: Due Date is "This week" AND Status ≠ "Completed"
- Show: Task Name, Status, Assigned To, Due Date

Title: "✅ Tasks Due This Week"

---

### BLOCK 7: ONE ACTION THIS WEEK

```
## 🎯 This Week's One Action

**What:** [Specific thing to improve, fix, or implement]
**Why:** [What prompted this — review feedback, data, inspection]
**How:** [Exact steps]
**Deadline:** [Day of this week]
**Done?** [ ]
```

---

### BLOCK 8: NOTES

```
## 📝 Notes

[Free text — anything worth noting for future reference]
```

---

## WEEKLY REVIEW ARCHIVE

Create a sub-page under the Weekly Review page for each completed week. Name format: "Week of DD MMM YYYY". This archive becomes a searchable history of your hosting decisions and improvements over time — invaluable when you're diagnosing a rating dip or revenue drop months later.

---

*Time to complete: 20 minutes | Run every Sunday evening*
