# TAB-02: Expense Ledger
## Spreadsheet Tab Specification

**Tab name:** Expenses  
**Purpose:** Track every operating cost — fixed and variable — for tax and P&L  
**Updated:** As expenses occur (same day or weekly minimum)

---

## COLUMN HEADERS

| Column | Header | Data Type | Input or Formula | Notes |
|---|---|---|---|---|
| A | Date | Date (DD/MM/YYYY) | Input | Date expense incurred |
| B | Month | Text | Formula: =TEXT(A2,"MMMM YYYY") | |
| C | Expense Category | Dropdown | Input | See category list below |
| D | Subcategory | Text | Input | More specific description |
| E | Supplier / Vendor | Text | Input | Who you paid |
| F | Description | Text | Input | Brief note of what it was for |
| G | Amount (€) | Currency | Input | Amount paid |
| H | Currency | Text | Input | EUR / GBP / USD |
| I | Payment Method | Dropdown | Input | Bank Transfer / Card / Cash |
| J | Receipt Ref | Text | Input | Receipt or invoice number |
| K | Tax Deductible | Dropdown | Input | Yes / No / Partial |
| L | Fixed or Variable | Dropdown | Input | Fixed / Variable / One-Time |
| M | Notes | Text | Input | Any notes for accountant |

---

## EXPENSE CATEGORIES (use as dropdown options in Column C)

- Cleaning
- Laundry & Linen
- Consumables & Supplies
- Welcome Pack
- Utilities — Electric
- Utilities — Gas
- Utilities — Water
- Internet/WiFi
- Insurance
- Platform Fees (Airbnb) — record from Revenue tab
- Software & Subscriptions
- Smart Home (smart lock, noise monitor, thermostat)
- Maintenance & Repairs
- Furnishings & Equipment
- Photography
- Professional Services (accountant, lawyer)
- Marketing (if any)
- Tourist Tax Remittance
- Other

---

## 3 EXAMPLE ROWS

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12/01/2026 | January 2026 | Cleaning | Turnover clean | Maria Santos | Post-checkout clean — Jan 10 booking | €55.00 | EUR | Bank Transfer | INV-2026-001 | Yes | Variable | — |
| 31/01/2026 | January 2026 | Utilities — Electric | Monthly electricity | EDP Portugal | January electricity bill | €68.40 | EUR | Direct Debit | DD-JAN-26 | Yes | Fixed | Higher due to heating |
| 05/01/2026 | January 2026 | Consumables & Supplies | Nespresso pods × 60 | Amazon | Bulk restock - pods | €22.90 | EUR | Card | ORD-1234567 | Yes | Variable | Split over 10 bookings |

---

## MONTHLY SUMMARY SECTION

Place at the top of the sheet or in a separate section:

| Category | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | TOTAL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cleaning | | | | | | | | | | | | | |
| Laundry & Linen | | | | | | | | | | | | | |
| Consumables | | | | | | | | | | | | | |
| Utilities | | | | | | | | | | | | | |
| Insurance | | | | | | | | | | | | | |
| Software | | | | | | | | | | | | | |
| Maintenance | | | | | | | | | | | | | |
| Other | | | | | | | | | | | | | |
| **TOTAL** | | | | | | | | | | | | | |

Formula for each month: `=SUMIFS(Expenses!G:G, Expenses!B:B, "January 2026", Expenses!C:C, "Cleaning")`

---

## TAX SUMMARY SECTION (year-end)

| Category | Total Spend | % Tax Deductible | Deductible Amount |
|---|---|---|---|
| Cleaning | =SUMIF(C:C,"Cleaning",G:G) | 100% | =previous × 1.0 |
| Utilities | =SUMIF(C:C,"Utilities*",G:G) | 100% | =previous × 1.0 |
| Insurance | =SUMIF(C:C,"Insurance",G:G) | 100% | |
| Maintenance | =SUMIF(C:C,"Maintenance*",G:G) | 100% | |
| Furnishings | =SUMIF(C:C,"Furnishings*",G:G) | See accountant | |
| **TOTAL DEDUCTIBLE** | | | =SUM(above) |

*Confirm deductibility with your local accountant — varies by jurisdiction*

---

## RECEIPT FILING SYSTEM

Store digital copies of all receipts in a cloud folder:
```
[Property Name] — Receipts/
├── 2026/
│   ├── January/
│   │   ├── INV-2026-001_Cleaning_12Jan.pdf
│   │   ├── DD-JAN-26_Electricity_31Jan.pdf
│   │   └── ORD-1234567_Amazon_05Jan.pdf
│   ├── February/
│   └── [etc.]
```

Name format: `REF_Category_Date.pdf`  
Keep for minimum 7 years (most tax authorities require this)
