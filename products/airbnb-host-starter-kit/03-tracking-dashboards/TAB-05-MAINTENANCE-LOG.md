# TAB-05: Maintenance Log
## Issue Tracker · Columns · Contractor Record · Preventive Schedule

---

## PURPOSE

One row per maintenance issue. Every reported or discovered problem goes here — from a dead light bulb to a burst pipe. This tab is your maintenance history, your contractor performance record, and your evidence base for insurance or AirCover claims.

---

## COLUMN STRUCTURE

| Col | Header | Format | Data Entry |
|---|---|---|---|
| A | Date Reported | Date DD/MM/YYYY | When the issue was first reported or discovered |
| B | Booking Ref | Text | Booking ref if reported during a stay; blank if found during inspection |
| C | Reported By | Dropdown | Guest / Cleaner / Host Inspection / Contractor |
| D | Issue Description | Text | Specific description: "Boiler pilot light out — no hot water" |
| E | Room/Area | Dropdown | Bedroom / Bathroom / Kitchen / Living Area / Entry / Building / General |
| F | Severity | Dropdown | Critical / High / Medium / Low |
| G | Photo Taken | Checkbox | ✓ when issue photographed |
| H | Contractor Assigned | Text | Name of contractor assigned |
| I | Contractor Phone | Text | Their contact number (for quick reference) |
| J | Date Assigned | Date | When contractor was contacted |
| K | Estimated Completion | Date | Contractor's estimated fix date |
| L | Actual Completion | Date | When issue was actually resolved |
| M | Response Time (hours) | Number | =J2-A2 (days) × 24 — time from report to contractor assignment |
| N | Resolution Time (hours) | Number | =(L2-A2) (days) × 24 — time from report to resolution |
| O | Cost (€) | Currency | Total cost of repair or replacement |
| P | AirCover Claim Filed | Checkbox | ✓ if claim was submitted |
| Q | AirCover Amount Recovered (€) | Currency | Amount received if claim approved |
| R | Insurance Claim Filed | Checkbox | ✓ if STR insurance claim submitted |
| S | Guest Impact | Dropdown | None / Minor inconvenience / Stay affected / Partial refund issued / Full refund issued |
| T | Root Cause | Dropdown | Normal wear / Guest damage / Installation failure / Age/deterioration / Preventive miss |
| U | Preventive Action | Text | What will prevent this recurring (e.g., "Add boiler pressure check to monthly schedule") |
| V | Status | Dropdown | Open / In Progress / Resolved / On Hold |

---

## SECTION 2 — PRIORITY RESPONSE TRACKING

Sort or filter by Severity (Column F) and Status (Column V) to manage open issues:

**Critical + Open/In Progress:** These are your urgent issues. Check daily.
**High + Open:** Check every 2 days.
**Medium + Open:** Include in weekly review.
**Low + Open:** Review monthly.

Add a conditional formatting rule: Any row where Status = "Open" AND Date Reported is more than [X] days ago — fill red. Use:
- Critical: red if open > 4 hours
- High: red if open > 24 hours
- Medium: red if open > 72 hours
- Low: red if open > 30 days

---

## SECTION 3 — CONTRACTOR PERFORMANCE TRACKING

After 6+ months, this tab gives you data to assess contractor performance. Build a summary view:

| Contractor | Jobs Completed | Avg Response Time (hrs) | Avg Resolution Time (hrs) | Avg Cost (€) | Issues Rate (% of their jobs with callbacks) |
|---|---|---|---|---|---|
| [Name] | | | | | |

A contractor with a low callback rate, fast response, and accurate quotes is worth paying a premium over. A contractor who repeatedly requires 3 visits for the same issue costs more than their invoice.

---

## SECTION 4 — PREVENTIVE MAINTENANCE TRACKING

In addition to reactive issues, record preventive tasks here. These entries have no Booking Ref and are typically Low severity with Root Cause = "Preventive maintenance."

| Preventive Task | Frequency | Last Done | Next Due | Status |
|---|---|---|---|---|
| Boiler pressure check | Monthly | | | |
| Smoke detector test | Monthly | | | |
| Smart lock battery check | Monthly | | | |
| WiFi speed test | Monthly | | | |
| Fire extinguisher check | Quarterly | | | |
| Boiler annual service | Annually | | | |
| Electrical inspection | Every 3 years | | | |

Create a separate filter view for preventive tasks (where Booking Ref is blank and Reported By = "Host Inspection") to keep them separate from reactive issues.

---

## SECTION 5 — AirCover CLAIM PREPARATION

For any issue caused by a guest that warrants an AirCover claim, this log provides the documentation structure.

When preparing a claim, pull:
- Column A: Date of discovery (must be within 14 days of checkout)
- Column D: Issue description (paste directly into AirCover claim)
- Column G: Photo (required attachment)
- Column O: Cost (must include quote or invoice)
- The Booking Ref from Column B (links claim to the specific booking)

The 14-day clock for AirCover claims starts at checkout, not at date of discovery. If cleaning team discovers damage 3 days after checkout, you have 11 days remaining to file.

---

## EXAMPLE DATA

| A | B | C | D | E | F | H | L | O | S | V |
|---|---|---|---|---|---|---|---|---|---|---|
| 18/01/2026 | HM3K5V6YB | Cleaner | Shower head limescale blocking flow | Bathroom | Low | Self-fixed | 18/01/2026 | 0 | None | Resolved |
| 22/02/2026 | HP4M8W9TS | Guest | Boiler pressure dropped — no hot water for 2 hours | General | Critical | Marco Plumbing | 22/02/2026 | 180 | Minor inconvenience | Resolved |

---

*Last updated: v1.0.0 · Log every issue within 24 hours of discovery — delayed entries cause missed claim windows*
