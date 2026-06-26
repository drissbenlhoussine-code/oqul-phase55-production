# Dashboard Build Guide
## How to Build Your Airbnb Host Tracking Spreadsheet

---

## OVERVIEW

Your tracking system is a single spreadsheet file with 7 tabs. Every tab in this section is a complete specification — column headers, data types, formula logic, and 3 rows of example data. You can build these in Google Sheets, Excel, or Notion (databases).

**Recommended platform:** Google Sheets (free, cloud-synced, accessible on mobile)  
**File name:** `[Property Name] — Host Operations Dashboard vYYYY`  
**Sharing:** Set to "View only" for your accountant; "Edit" for your co-host (if applicable)

---

## HOW TO BUILD EACH TAB

1. Create a new Google Sheets document  
2. Create 7 tabs at the bottom, named exactly as listed:  
   - **Revenue** | **Expenses** | **Bookings** | **Cleaning** | **Maintenance** | **Reviews** | **KPI Dashboard**  
3. Follow each spec file (TAB-01 through TAB-07) to build the column headers for each tab  
4. Apply the formulas described in each spec  
5. Enter example rows to verify formulas are working, then delete example rows and enter real data

---

## COLOUR CODING CONVENTION (apply across all tabs)

| Colour | Meaning |
|---|---|
| Light blue header row | Column headers |
| White rows | Input data (type here) |
| Light grey rows | Calculated/formula cells (don't type here) |
| Green cells | Target met or exceeded |
| Yellow cells | Warning — needs attention |
| Red cells | Below target — action required |

---

## DATA ENTRY DISCIPLINE

- Enter data within 24 hours of each event (booking, expense, cleaning)
- Never enter estimated data as if it were actual — use a "Projected" flag column
- Keep one year per file — at December 31, archive the file and open a new one for January 1
- Back up monthly: File → Download → Excel (.xlsx)

---

## LINKING TABS (Google Sheets formula syntax)

To pull data between tabs:  
`='Tab Name'!A2` — pulls the exact value from cell A2 on that tab  
`=SUMIF('Bookings'!B:B,"January",'Bookings'!F:F)` — sums revenue for all January bookings

The KPI Dashboard tab (TAB-07) pulls automatically from all other tabs. Build it last.

---

*See TAB-01 through TAB-07 for complete specifications.*
