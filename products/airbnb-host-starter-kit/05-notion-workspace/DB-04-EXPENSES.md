# DB-04: Expenses Database
## Expenses Database Spec · Properties · Views · Tax Export

---

## DATABASE SETUP

**Name:** Expenses
**Icon:** 💳
**Location:** Full-page database in workspace root.

---

## PROPERTIES (COLUMNS)

| Property Name | Type | Values / Notes |
|---|---|---|
| Expense Title | Title | Descriptive name: "Maria — Cleaning 15 Jan" |
| Date | Date | Date payment was made |
| Amount (€) | Number | Amount paid (numbers only) |
| Category | Select | See category list below |
| Type | Select | Fixed / Variable / One-Time / Maintenance |
| Tax Deductible | Select | Yes / No / Partial |
| Vendor | Text | Who was paid |
| Invoice Ref | Text | Invoice or receipt number |
| Payment Method | Select | Bank Transfer / Card / Cash / Direct Debit |
| Booking Ref | Relation | Links to DB-01: Bookings (for variable/per-booking costs) |
| Notes | Text | Any additional context |
| Receipt Uploaded | Checkbox | ✓ when digital receipt saved (in a linked Google Drive folder) |

---

## CATEGORY OPTIONS

Set these as the Select options for the Category property:

- Insurance (STR)
- Utilities — Electricity/Gas
- Utilities — Water
- WiFi/Internet
- Smart Lock Subscription
- Noise Monitor
- Property Management Software
- Cleaning — Labour
- Laundry/Linen
- Consumables
- Welcome Basket
- Photography (Setup)
- Linen/Bedding (Setup)
- Smart Lock (Setup)
- Décor/Staging (Setup)
- Maintenance — Plumbing
- Maintenance — Electrical
- Maintenance — General
- Maintenance — Appliance
- Tax/Professional Fees
- Other Fixed
- Other Variable
- Other Setup

---

## VIEWS TO CREATE

**View 1 — All Expenses (Table)**
- Sort by Date descending
- Show: Expense Title, Date, Amount, Category, Type, Tax Deductible

**View 2 — This Month (Filtered)**
- Filter: Date is within this month
- Show all columns
- Useful for monthly review

**View 3 — By Category (Grouped)**
- Group by: Category
- Show sum of Amount for each category group
- This generates your expense breakdown at a glance

**View 4 — Tax Deductible Only (Filtered)**
- Filter: Tax Deductible = Yes
- Sum of Amount shown at bottom
- Export this view for your accountant

**View 5 — Variable Costs by Booking (Filtered)**
- Filter: Type = Variable
- Group by: Booking Ref relation
- Shows cleaning and variable costs per booking

---

## MONTHLY COST SUMMARY (BUILD AS A ROLLUP IN THE WORKSPACE)

After 3 months of data, you can query Notion's built-in summaries:

In DB-04 in "Group by Category" view, Notion shows the sum per category automatically at the bottom of each group. Screenshot or export this monthly as your P&L input.

Alternatively, use a linked database view on PAGE-03 (Weekly Review) that shows only the current month's expenses grouped by category with sum.

---

## RECEIPT MANAGEMENT

Create a Google Drive folder named: `[PROPERTY NAME] — Receipts [YEAR]`

Sub-folders:
- Fixed Costs
- Cleaning
- Maintenance
- Setup

When entering an expense in DB-04, upload or photograph the receipt to the relevant subfolder immediately. In Notion, you can link to the Google Drive file using the URL property or paste the Drive link in the Notes field.

At tax time: you have a complete digital receipt archive linked to every expense entry.

---

## TAX EXPORT PROCESS

At year-end:
1. Open the "Tax Deductible Only" view
2. Sort by Category
3. Export to CSV (from Notion: ··· menu → Export → CSV)
4. Open in Google Sheets; sum each category
5. Pass to accountant with the Airbnb Transaction History CSV

The two files together provide a complete income and expense picture for your rental income tax filing.

---

*Last updated: v1.0.0 · Upload receipts immediately — delayed uploads lead to missing records*
