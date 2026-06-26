# DB-02: Guests Database
## Guests Database Spec · Properties · Views · Entry Guide

---

## DATABASE SETUP

**Name:** Guests
**Icon:** 👤
**Location:** Full-page database in workspace root.

---

## PROPERTIES (COLUMNS)

| Property Name | Type | Values / Notes |
|---|---|---|
| Guest Name | Title | Full name (as shown on Airbnb profile) |
| Airbnb Profile URL | URL | Link to their Airbnb profile page |
| Country | Select | Country of origin |
| Verified | Select | ID Verified / Not Verified / Unknown |
| Review Count (at booking) | Number | Number of reviews on their profile when they booked |
| Screening Score | Number | Score from SOP-02 matrix (0–16) |
| Bookings | Relation | Links to DB-01: Bookings (all stays for this guest) |
| Total Stays | Rollup | Count of linked bookings |
| Total Revenue | Rollup | Sum of Gross Revenue across linked bookings |
| Last Stay | Rollup | Latest value of Check-Out Date across linked bookings |
| Average Review Given | Rollup | Average of Review Score across linked bookings |
| Special Notes | Text | Persistent notes about this guest (not booking-specific) |
| Tags | Multi-select | Great Guest / Return Guest / Flagged / Business / Family |

---

## VIEWS TO CREATE

**View 1 — All Guests (Table)**
- Sort by Last Stay descending
- Show: Guest Name, Country, Total Stays, Total Revenue, Average Review Given, Tags

**View 2 — Repeat Guests (Filtered)**
- Filter: Total Stays ≥ 2
- These are your high-value guest relationships

**View 3 — Flagged Guests (Filtered)**
- Filter: Tags contains "Flagged"
- Use for guests with prior issues — quick reference before accepting future bookings

**View 4 — Gallery**
- Useful for at-a-glance recognition
- Cover property: set to Guest Name initial card (Notion does not support photos from external URLs)

---

## ENTRY PROCEDURE

Create a guest entry at the time of booking confirmation. Check if the guest already has an entry (return visit) before creating a new one.

1. New entry: Guest's full name as the title
2. Add Airbnb profile URL
3. Enter country (visible on their profile)
4. Set Verified status
5. Enter their review count at the time of booking
6. Run the SOP-02 screening matrix; enter score
7. Link to their DB-01 booking entry

For return guests: do not create a new entry. Find the existing entry and add the new booking as an additional linked booking. The Rollup properties will update automatically.

---

## GUEST TAGS — WHEN TO APPLY

| Tag | Apply When |
|---|---|
| Great Guest | Guest left a 5-star review AND property was left in excellent condition |
| Return Guest | Guest has stayed more than once |
| Flagged | Any concern during stay: noise, extra guests, damage, difficult communication |
| Business | Guest was on a business or work trip |
| Family | Guest travelling with children |

Do not remove a "Flagged" tag after a negative stay — it is a permanent record. If a flagged guest books again, you have visibility to screen more carefully.

---

## PRIVACY NOTE

This database is for operational hosting purposes only. Keep it private (Notion default). Do not share with anyone outside your hosting operation. Guest data should be handled in compliance with GDPR (if you are based in or hosting guests from the EU) — this means storing only what is necessary for hosting purposes and deleting upon request.

---

*Last updated: v1.0.0 · Check for existing guest entry before creating a new one*
