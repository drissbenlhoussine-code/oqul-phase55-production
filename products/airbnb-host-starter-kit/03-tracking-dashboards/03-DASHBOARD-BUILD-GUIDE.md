# Dashboard Build Guide
## How to Build All 7 Tabs · Google Sheets Setup · Formula Reference

---

## HOW TO USE THIS DOCUMENT

Build TAB-01 first — it is the only tab you need on Day 1. Build the remaining tabs over the first 7 days as you have time. Each tab spec is in its own file. This guide covers setup, formatting, and formulas that appear across multiple tabs.

---

## SECTION 1 — GOOGLE SHEETS SETUP

### File Naming

Create one Google Sheets file per property:
`[Property Name] — Host Operations [YEAR]`

Example: `Alfama Studio — Host Operations 2026`

Create a new file each year. Keep the previous year's file for tax reference — do not delete it.

### Tab Order and Names

Create 7 tabs in this exact order (colour-code them for navigation):

| Tab | Name | Colour | Build Priority |
|---|---|---|---|
| 1 | Revenue Tracker | Green | Day 1 |
| 2 | Expense Ledger | Red | Day 3 |
| 3 | Booking Log | Blue | Day 3 |
| 4 | Cleaning Schedule | Orange | Day 5 |
| 5 | Maintenance Log | Purple | Day 5 |
| 6 | Review Scorecard | Yellow | Day 7 |
| 7 | KPI Dashboard | Grey | Day 7 |

To colour a tab: right-click the tab → Change colour.

### General Formatting Rules

Apply these to all tabs:

- Row 1: Column headers. Bold. Background colour: match tab colour at 30% opacity.
- Row 2 onward: Data rows. Alternating white and light grey for readability.
- Column widths: widen any column where content is being cut off — Google Sheets default widths are too narrow.
- Number format: All currency columns: Format → Number → Custom → `€#,##0.00`
- Percentage format: Format → Number → Percent (with 1 decimal: `0.0%`)
- Date format: Format → Number → Date → `DD/MM/YYYY`
- Freeze row 1 on all tabs: View → Freeze → 1 row

---

## SECTION 2 — FORMULA REFERENCE

These formulas appear across multiple tabs. Copy-paste them exactly, replacing cell references to match your column layout.

### SUM for Total Column

Use to total a range: `=SUM(D2:D200)`

### Running Total (Cumulative)

For a column that shows year-to-date totals: `=SUM($D$2:D2)`
Apply this to the first data row, then drag down. The `$D$2` anchors the start row while the end reference moves.

### Occupancy Rate

`=C2/B2` where C2 = booked nights, B2 = available nights
Apply the Percent format to this cell.

### ADR (Average Daily Rate)

`=E2/C2` where E2 = accommodation revenue, C2 = booked nights
This gives the average rate per night booked. Apply currency format.

### RevPAN (Revenue Per Available Night)

`=E2/B2` where E2 = accommodation revenue, B2 = available nights
Apply currency format.

### ALOS (Average Length of Stay)

`=C2/F2` where C2 = booked nights, F2 = number of bookings in that period

### Variance vs. Projection

`=(D2-E2)/E2` where D2 = actual, E2 = projected
Format as percent. Positive = above projection. Negative = below.

Conditional formatting: highlight negative variance red, positive green:
- Format → Conditional formatting → "Less than 0" → fill red
- Format → Conditional formatting → "Greater than 0" → fill green

### COUNTIF for Review Count

`=COUNTIF(B2:B200,">0")` counts all non-empty entries in column B.

### AVERAGEIF for Subcategory Averages

`=AVERAGEIF(C2:C200,"<>",C2:C200)` calculates average of non-empty cells in column C.

---

## SECTION 3 — DATA ENTRY RULES

Apply these rules consistently across all tabs to prevent formula errors:

1. **Never merge cells.** Merged cells break formulas, filters, and sorting.
2. **Never leave blank rows between data rows.** Blank rows interrupt SUM ranges and COUNTIF functions.
3. **Enter dates in `DD/MM/YYYY` format.** Inconsistent date entry is the most common cause of broken date-based formulas.
4. **Currency: enter numbers only.** The column format handles the € symbol. Do not type "€85" — type "85" and let the format display it as €85.00.
5. **Use dropdown menus** for category columns (Status, Category, Severity) to prevent spelling variants: Data → Data validation → List of items.

---

## SECTION 4 — PROTECTING YOUR DATA

Once you have more than 10 bookings of data, take these precautions:

**Version history:** Google Sheets auto-saves. Access version history via File → Version history → See version history. This allows you to restore any previous state if formulas are accidentally deleted.

**Monthly snapshot:** On the 1st of each month, duplicate the entire sheet file: File → Make a copy → Name it "[Property Name] — [Month] [Year] Snapshot." Store these in a dedicated Google Drive folder for tax reference.

**Share access:** Share view-only access with your accountant. Avoids the need to email exports and keeps data current.

---

## SECTION 5 — IMPORTING AIRBNB DATA

### Airbnb Transaction History Export

Location: Airbnb.com → Account → Transaction history → Export transactions

This CSV contains:
- All payouts received
- Airbnb service fee deductions
- Refunds issued
- Resolution payments

Import this monthly into TAB-01 as a check against your manual entries. The Airbnb payout figure already has the 3% service fee deducted — your gross revenue is the payout plus the fee.

*Formula to back out gross revenue from net payout:*
`=Payout/0.97` (divides net payout by 0.97 to gross up to the pre-fee revenue)

### Matching Airbnb Payouts to Bookings

Airbnb pays out 24 hours after guest check-in, not at the time of booking. Map each payout to the check-in date, not the booking date, when entering to TAB-01.

---

## SECTION 6 — TAX PREPARATION FROM YOUR SPREADSHEET

At year-end (December 31 or whenever your tax year ends), pull these figures from your tabs:

| Figure | Tab | Column | Notes |
|---|---|---|---|
| Total Gross Revenue | TAB-01 | Gross Revenue total row | Include cleaning fees |
| Total Airbnb Fees Paid | TAB-01 | Airbnb Fee total row | Deductible expense |
| Total Cleaning Costs | TAB-02 | Cleaning category total | Deductible expense |
| Total Consumables | TAB-02 | Consumables total | Deductible expense |
| Total Maintenance | TAB-05 | Total cost column | Deductible if repair, not improvement |
| Total Fixed Costs | TAB-02 | Fixed category total | Deductible |
| Net Operating Profit | TAB-07 | Net Profit row | This is the taxable income base |

Print or export these figures and pass to your accountant with the Airbnb Transaction History CSV export. The combination of your spreadsheet and Airbnb's export is all the documentation needed for a standard rental income tax filing.

---

*Last updated: v1.0.0 · Build TAB-01 today. Build the rest over the next 7 days.*
