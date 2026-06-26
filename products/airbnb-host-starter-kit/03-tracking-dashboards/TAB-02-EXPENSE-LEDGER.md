# TAB-02: Expense Ledger
## Operating Expenses · Columns · Formulas · Category Codes

---

## PURPOSE

One row per expense. Every outgoing payment related to the property gets an entry. This tab feeds the cost side of your P&L and generates the deductible expense list for your tax filing.

---

## COLUMN STRUCTURE

| Col | Header | Format | Data Entry |
|---|---|---|---|
| A | Date | Date DD/MM/YYYY | Date payment was made |
| B | Vendor / Description | Text | Who you paid and what for (e.g., "Maria — turnover clean 15 Jan") |
| C | Category Code | Dropdown | Use the category codes in Section 2 |
| D | Category Name | Text | Auto-fill from Category Code if using a lookup, or type manually |
| E | Booking Ref | Text | Leave blank for fixed costs; enter Airbnb booking ref for variable costs |
| F | Amount (€) | Currency | Amount paid |
| G | VAT (€) | Currency | VAT portion if you are VAT-registered; leave blank if not |
| H | Net Amount (€) | Currency | =F2-G2 (or =F2 if not VAT-registered) |
| I | Payment Method | Dropdown | Bank transfer / Card / Cash / Direct debit |
| J | Invoice Ref | Text | Invoice or receipt number for your records |
| K | Tax Deductible | Dropdown | Yes / No / Partial |
| L | Notes | Text | Any additional context |

---

## SECTION 2 — CATEGORY CODES

Use these codes consistently. They are the basis for your expense summary by category in TAB-07.

| Code | Category | Type | Examples |
|---|---|---|---|
| FX-INS | Insurance | Fixed | STR property insurance premium |
| FX-UTL | Utilities — Electricity/Gas | Fixed | Monthly utility bill |
| FX-WTR | Utilities — Water | Fixed | Monthly water bill |
| FX-NET | WiFi/Internet | Fixed | Monthly broadband subscription |
| FX-LCK | Smart Lock Subscription | Fixed | Yale, Nuki, Igloohome monthly fee |
| FX-NSM | Noise Monitor | Fixed | Minut or NoiseAware subscription |
| FX-PMS | Property Management Software | Fixed | Hostaway Lite or equivalent |
| FX-OTH | Other Fixed | Fixed | Any fixed cost not above |
| VR-CLN | Cleaning — Labour | Variable | Per-turnover cleaning service |
| VR-LIN | Laundry/Linen Service | Variable | Per-turnover linen laundering |
| VR-CSM | Consumables | Variable | Toiletries, pods, tea, coffee, bin bags |
| VR-WLC | Welcome Basket | Variable | Wine, snacks, card |
| VR-OTH | Other Variable | Variable | Any per-stay cost not above |
| MN-PLM | Maintenance — Plumbing | One-off | Plumber call-out |
| MN-ELC | Maintenance — Electrical | One-off | Electrician call-out |
| MN-GEN | Maintenance — General | One-off | Handyman, general repairs |
| MN-APL | Maintenance — Appliance | One-off | Appliance repair or replacement |
| ST-PHT | Setup — Photography | One-time | Professional listing photos |
| ST-LIN | Setup — Linen/Bedding | One-time | Initial linen set purchase |
| ST-LCK | Setup — Smart Lock | One-time | Smart lock purchase and installation |
| ST-DCR | Setup — Décor/Staging | One-time | Initial décor and staging |
| ST-OTH | Other Setup | One-time | Any other Year 1 setup cost |
| TAX | Tax/Professional Fees | Annual | Accountant, local licence fees |
| OTH | Other | Other | Anything not categorised above |

---

## FORMULA ROWS

**Monthly Summary (add below data rows, at approximately row 205):**

For each category code, create a SUMIF row:

`=SUMIF(C2:C200,"VR-CLN",F2:F200)` — total cleaning costs
`=SUMIF(C2:C200,"FX-INS",F2:F200)` — total insurance
[Repeat for all categories]

**Total Fixed Costs Monthly:**
`=SUMIF(D2:D200,"Fixed",F2:F200)` — if the Type column (D) shows "Fixed"
Or: sum all FX- category rows.

**Total Variable Costs Monthly:**
Sum all VR- category rows.

**Total Operating Costs:**
`=SUM(all category monthly totals)` — exclude ST- (setup) rows after Year 1

**Tax Deductible Total:**
`=SUMIF(K2:K200,"Yes",F2:F200)` — sum of all rows marked "Yes" in tax deductible column

---

## EXAMPLE DATA

| A | B | C | D | E | F | K |
|---|---|---|---|---|---|---|
| 15/01/2026 | Maria Santos — turnover clean | VR-CLN | Variable | HM3K5V6YB | 55.00 | Yes |
| 15/01/2026 | Linen service — Jan 15 stay | VR-LIN | Variable | HM3K5V6YB | 18.00 | Yes |
| 15/01/2026 | Toiletries + consumables | VR-CSM | Variable | HM3K5V6YB | 12.00 | Yes |
| 15/01/2026 | Welcome basket | VR-WLC | Variable | HM3K5V6YB | 8.50 | Yes |
| 01/01/2026 | Property insurance — January | FX-INS | Fixed | | 80.00 | Yes |
| 01/01/2026 | Electricity + gas — January | FX-UTL | Fixed | | 115.00 | Yes |
| 01/01/2026 | WiFi — January | FX-NET | Fixed | | 35.00 | Yes |

---

## ANNUAL TAX SUMMARY (Build After 12 Months)

At year-end, produce this summary for your accountant:

| Category | Annual Total (€) | Tax Deductible? |
|---|---|---|
| Total Gross Revenue | | — |
| Airbnb Service Fees | | Yes |
| Insurance | | Yes |
| Utilities (electricity, gas, water) | | Yes (proportion if also personal use) |
| WiFi | | Yes |
| Platform/Software Subscriptions | | Yes |
| Cleaning Services | | Yes |
| Laundry/Linen | | Yes |
| Consumables | | Yes |
| Maintenance and Repairs | | Yes (repairs, not improvements) |
| Professional Photography | | Yes (in Year 1) |
| Initial Setup Costs | | Country-dependent (ask accountant) |
| Accountant/Tax Fees | | Yes |
| **Total Deductible Expenses** | | |
| **Net Taxable Income** | | |

---

*Last updated: v1.0.0 · Enter every expense within 7 days of payment — delay leads to missing receipts*
