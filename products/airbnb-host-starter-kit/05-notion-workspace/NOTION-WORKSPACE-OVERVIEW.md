# Notion Workspace Overview
## Complete Build Guide — Airbnb Host HQ

---

## WORKSPACE STRUCTURE

Build this workspace in sequence. Each database must be created before the pages that reference it.

```
🏠 [Property Name] — Host HQ
│
├── 📊 DATABASES (build first)
│   ├── 📅 Bookings Database
│   ├── 👤 Guests Database
│   ├── ✅ Tasks & SOPs Database
│   ├── 💰 Expenses Database
│   └── 🔧 Maintenance Database
│
├── 📄 PAGES (build after databases)
│   ├── 🎯 Command Center
│   ├── 🏡 Property Hub
│   └── 📆 Weekly Review
│
└── 🗂️ ARCHIVE
    └── [Past bookings and resolved issues move here]
```

---

## BUILD ORDER

### Step 1: Create Workspace Root Page
- Create a full-page Notion page
- Title: "[Your Property Name] — Host HQ"
- Icon: 🏠 (house emoji)
- Cover: A photo of your property (add from Notion cover options or upload your hero shot)
- Add a divider and the five database links as you build them

### Step 2: Build Databases (see individual database files)
Build in this exact order — later databases reference earlier ones:
1. Guests Database (no dependencies)
2. Bookings Database (references Guests)
3. Tasks & SOPs Database (no dependencies)
4. Expenses Database (no dependencies)
5. Maintenance Database (references Bookings)

### Step 3: Build Pages
1. Command Center (references all databases)
2. Property Hub (standalone)
3. Weekly Review (references Bookings, Maintenance, Reviews in Bookings)

---

## COLOUR AND ICON CONVENTIONS

| Database/Page | Icon | Colour |
|---|---|---|
| Bookings | 📅 | Blue |
| Guests | 👤 | Purple |
| Tasks & SOPs | ✅ | Green |
| Expenses | 💰 | Yellow |
| Maintenance | 🔧 | Orange |
| Command Center | 🎯 | Red |
| Property Hub | 🏡 | Brown |
| Weekly Review | 📆 | Gray |

Using consistent colours lets you navigate by colour at a glance.

---

## TEMPLATE SETUP IN NOTION

For each database, create a **Template** that auto-populates the correct fields when a new entry is created:

**Bookings template name:** "New Booking"
**Guests template name:** "New Guest Profile"
**Tasks template name:** "New SOP Task"
**Expenses template name:** "New Expense"
**Maintenance template name:** "New Issue"

Templates save approximately 3 minutes per entry and ensure fields are never missed.

---

## MOBILE SETUP

Install Notion on your phone. Pin the following pages as favourites:
1. Command Center (check daily)
2. Bookings Database (filtered: "Active this week")
3. Maintenance Database (filtered: "Status = Open")

With these three views on your phone, you can manage your entire hosting operation from anywhere in under 5 minutes per day.

---

*See individual Notion database and page files for complete build specifications.*
