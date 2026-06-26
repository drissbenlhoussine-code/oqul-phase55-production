# Notion Database: Expenses
## Complete Build Specification

---

## DATABASE SETUP

**Name:** 💰 Expenses  
**Icon:** 💰  
**Type:** Full-page database  
**Location:** Workspace root; linked to Command Center

---

## PROPERTIES (FIELDS)

| Property Name | Type | Options / Notes |
|---|---|---|
| Expense Name | Title | Brief description |
| Date | Date | Date expense incurred |
| Category | Select | Cleaning / Laundry / Consumables / Utilities / Insurance / Software / Smart Home / Maintenance / Furnishings / Photography / Professional Services / Tourist Tax / Other |
| Amount (€) | Number | Currency format |
| Supplier | Text | Who you paid |
| Payment Method | Select | Bank Transfer / Card / Direct Debit / Cash |
| Receipt Ref | Text | Invoice or order number |
| Tax Deductible | Select | Yes / No / Partial |
| Fixed or Variable | Select | Fixed / Variable / One-Time |
| Related Booking | Relation | → Bookings Database (for per-booking costs like cleaning) |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Notes | Text | |

---

## VIEWS

### View 1: All Expenses (DEFAULT)
- **Type:** Table
- **Sort:** Date descending
- **Visible columns:** Expense Name, Date, Category, Amount, Supplier, Tax Deductible
- **Show sum:** Amount column (running total visible at bottom)

### View 2: By Category (Monthly)
- **Type:** Table
- **Group by:** Category
- **Filter:** Month = "This month" (update filter each month)
- **Show aggregate:** Sum of Amount per category

### View 3: Tax Deductible
- **Type:** Table
- **Filter:** Tax Deductible = "Yes"
- **Show sum:** Amount (total deductible amount)
- **Purpose:** Year-end tax preparation

### View 4: Per-Booking Costs
- **Type:** Table
- **Filter:** Related Booking is not empty
- **Group by:** Related Booking
- **Purpose:** See all costs associated with a specific booking (cleaning, consumables, etc.)

---

## MONTHLY EXPENSE SUMMARY (add as a linked database view on the Command Center)

Create a filtered view on the Command Center page:
- Filter: Month = current month
- Group by: Category
- Show: Sum of Amount per group
- Title: "This Month's Expenses"

This gives you a live expense snapshot without opening the full database.

---

## TEMPLATE: "New Expense"

Auto-populates:
- Date: Today
- Tax Deductible: Yes (default — change to No if not applicable)
- Fixed or Variable: Variable (default — change as needed)
