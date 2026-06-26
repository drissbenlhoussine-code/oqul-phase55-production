# TAB-05: Maintenance Log
## Spreadsheet Tab Specification

**Tab name:** Maintenance  
**Purpose:** Record and track every maintenance issue, repair, and planned improvement  
**Updated:** As issues arise; review monthly

---

## COLUMN HEADERS

| Column | Header | Data Type | Input or Formula | Notes |
|---|---|---|---|---|
| A | Date Reported | Date | Input | When issue was discovered or reported |
| B | Reported By | Dropdown | Input | Guest / Host / Cleaner / Inspection |
| C | Priority | Dropdown | Input | P1-Emergency / P2-Urgent / P3-Standard / P4-Cosmetic |
| D | Category | Dropdown | Input | See list below |
| E | Location | Text | Input | Room or area in the property |
| F | Issue Description | Text | Input | Clear description of the problem |
| G | Assigned To | Text | Input | Contractor name or "Self" |
| H | Contractor Phone | Text | Input | |
| I | Date Scheduled | Date | Input | When repair is booked |
| J | Date Completed | Date | Input | When repair was confirmed done |
| K | Resolution Time (hrs) | Number | Formula: =(J2-A2)*24 | Hours from report to resolution |
| L | Status | Dropdown | Input | Open / In Progress / Completed / Deferred |
| M | Cost (€) | Currency | Input | Cost of repair |
| N | Paid To | Text | Input | Who was paid |
| O | Receipt Ref | Text | Input | For expense ledger cross-reference |
| P | Guest Compensation Given? | Dropdown | Input | Yes / No |
| Q | Compensation Amount (€) | Currency | Input | If applicable |
| R | Root Cause | Text | Input | Why did this happen? |
| S | Preventive Action | Text | Input | What will prevent this recurring? |
| T | Notes | Text | Input | |

---

## ISSUE CATEGORIES (dropdown options for Column D)

- Plumbing
- Electrical
- Heating/Boiler
- Air Conditioning
- Smart Lock / Access
- WiFi / Internet
- Kitchen Appliance
- Laundry Appliance
- Furniture
- Flooring
- Walls / Paintwork
- Windows / Doors
- Outdoor / Garden
- Cleaning Issue
- Pest / Infestation
- Structural
- Other

---

## 3 EXAMPLE ROWS

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 15/01/26 | Guest | P2-Urgent | Heating/Boiler | Utility cupboard | Guest reports no hot water — boiler showing E1 error | João Plumbing | +351 912 345 678 | 15/01/26 | 15/01/26 | 6 | Completed | €120 | João Plumbing | EXP-2026-015 | No | — | Boiler pressure dropped to 0.5 bar | Posted pressure-reset card near boiler | Guest back within 1hr |
| 22/01/26 | Cleaner | P4-Cosmetic | Walls / Paintwork | Hallway | Small scuff mark on hallway wall, approx 10cm | Self | — | 25/01/26 | 25/01/26 | 72 | Completed | €8 | DIY | — | No | — | Guest moving luggage | Add luggage rack to prevent | Touch-up paint in utility |
| 28/01/26 | Host | P3-Standard | Kitchen Appliance | Kitchen | Microwave door handle loose — still functional | Handyman | +351 934 567 890 | 02/02/26 | 02/02/26 | 120 | Completed | €45 | Handyman | EXP-2026-022 | No | — | Normal wear | Annual appliance check added to calendar | Screw was loose — tightened |

---

## SUMMARY METRICS

| Metric | Formula | Target |
|---|---|---|
| Total issues this year | =COUNTA(A:A)-1 | Track trend |
| Open issues | =COUNTIF(L:L,"Open") | 0 |
| P1 avg resolution time | =AVERAGEIFS(K:K,C:C,"P1*") | <4 hours |
| P2 avg resolution time | =AVERAGEIFS(K:K,C:C,"P2*") | <24 hours |
| Total maintenance spend | =SUM(M:M) | vs. budget |
| Guest compensation total | =SUM(Q:Q) | Track cost of poor maintenance |

---

## PREVENTIVE MAINTENANCE CALENDAR

Use a separate section at the bottom of this tab for planned maintenance:

| Task | Frequency | Last Done | Next Due | Assigned To | Status |
|---|---|---|---|---|---|
| Boiler service | Annual | September 2025 | September 2026 | João Plumbing | Scheduled |
| Smoke alarm test & battery | 6 months | January 2026 | July 2026 | Self | Upcoming |
| AC service and filter clean | Annual | May 2025 | May 2026 | AC Company | Upcoming |
| Washing machine drum clean | Monthly | January 2026 | February 2026 | Cleaner | Routine |
| Grout inspection | Annual | November 2025 | November 2026 | Self | Upcoming |
| Mattress protector replace | Every 18 months | June 2025 | December 2026 | Self | OK |
| Linen refresh (replace worn) | Annual | January 2026 | January 2027 | Self | Done |
| Exterior camera check | Monthly | January 2026 | February 2026 | Self | Routine |
| Smart lock battery check | Every 6 months | November 2025 | May 2026 | Self | Upcoming |
| EICR electrical check | Every 5 years | 2023 | 2028 | Electrician | Scheduled |

---

## RECURRING ISSUES WATCH LIST

If any issue appears more than twice in a year, it moves to the watch list:

| Issue Type | Occurrences | Root Cause Identified | Long-Term Fix | Status |
|---|---|---|---|---|
| Hot water pressure drop | 3 | Boiler aging | Budget for boiler replacement in Q4 | In progress |
| WiFi drops in bedroom | 2 | Signal dead zone | WiFi extender installed | Resolved |
