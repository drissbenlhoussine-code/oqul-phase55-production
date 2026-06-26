# Notion Database: Guests
## Complete Build Specification

---

## DATABASE SETUP

**Name:** 👤 Guests  
**Icon:** 👤  
**Type:** Full-page database  
**Location:** Workspace root; linked to Command Center and Bookings database

---

## PROPERTIES (FIELDS)

| Property Name | Type | Options / Notes |
|---|---|---|
| Guest Name | Title | First and last name |
| Airbnb Profile URL | URL | Link to their Airbnb profile |
| Nationality | Select | [Country dropdown — add as you receive bookings] |
| First Stay | Date | Date of their first booking |
| Total Stays | Rollup | Count of related Bookings entries |
| Total Nights | Rollup | Sum of "Nights" field across all related bookings |
| Total Revenue | Rollup | Sum of "Net Revenue" across all related bookings |
| Average Rating Given | Number | Rating you gave them (average across stays) |
| Average Rating Received | Rollup | Average of "Star Rating" from all related bookings |
| Guest Status | Select | Prospect / First-Time / Returning / VIP |
| Screening Notes | Text | Private host notes from SOP-02 screening |
| Invited to Return | Checkbox | Have you sent them a "welcome back" offer? |
| Tags | Multi-select | Business Traveller / Couple / Family / Solo / Long-Stay / Remote Worker |
| Communication Style | Select | Minimal contact preferred / Chatty / Standard |
| Special Requirements | Text | Dietary, accessibility, preferences |
| Notes | Text | Any other notes for future reference |

---

## VIEWS

### View 1: All Guests (DEFAULT)
- **Type:** Table
- **Sort:** First Stay descending (newest first)
- **Visible columns:** Guest Name, Guest Status, Total Stays, Total Revenue, Average Rating Given, Average Rating Received, Tags

### View 2: VIP Guests
- **Type:** Gallery
- **Filter:** Guest Status = "VIP" or Total Stays ≥ 3
- **Gallery card:** Guest Name + Total Stays + Total Revenue
- **Purpose:** Quick view of your best guests for targeted re-engagement

### View 3: Returning Guests
- **Type:** Table
- **Filter:** Total Stays ≥ 2
- **Sort:** Total Revenue descending
- **Purpose:** Understand your returning guest base

### View 4: Business Travellers
- **Type:** Table
- **Filter:** Tags contains "Business Traveller" or "Remote Worker"
- **Purpose:** Segment for targeted promotions (weekday discounts, workspace mentions)

---

## GUEST STATUS CRITERIA

| Status | Criteria |
|---|---|
| Prospect | Inquiry received; no confirmed booking yet |
| First-Time | 1 completed stay |
| Returning | 2+ completed stays |
| VIP | 3+ stays OR lifetime value > €500 OR left multiple 5-star reviews |

**VIP treatment:** VIP guests receive the long-stay welcome message regardless of length, a premium welcome basket, and a handwritten note rather than a printed card.

---

## TEMPLATE: "New Guest Profile"

Auto-populates:
- Guest Status: First-Time
- Invited to Return: unchecked
