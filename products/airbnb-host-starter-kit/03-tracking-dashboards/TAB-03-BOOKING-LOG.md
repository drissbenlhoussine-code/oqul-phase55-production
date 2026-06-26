# TAB-03: Booking Log
## Guest Log · Columns · Formulas · Guest History

---

## PURPOSE

One row per booking. This tab is a guest management record — separate from revenue tracking. It stores guest information, screening data, communication history, and notes that help you host better over time. Reference this before every check-in.

---

## COLUMN STRUCTURE

| Col | Header | Format | Data Entry |
|---|---|---|---|
| A | Booking Ref | Text | Airbnb booking reference |
| B | Guest Name | Text | Full name |
| C | Airbnb Profile URL | Text | Guest's Airbnb profile link |
| D | Check-In | Date | DD/MM/YYYY |
| E | Check-Out | Date | DD/MM/YYYY |
| F | Nights | Number | =E2-D2 |
| G | Guests | Number | Number booked |
| H | Country of Origin | Text | Where guest is from (visible on profile) |
| I | Guest Reviews | Number | Number of reviews on their profile at time of booking |
| J | Screening Score | Number 0–16 | Score from SOP-02 matrix |
| K | Screening Decision | Dropdown | Approved / Approved with conditions / Declined |
| L | Special Requests | Text | Any requests made at booking stage |
| M | Special Occasion | Dropdown | None / Birthday / Anniversary / Honeymoon / Business |
| N | Mid-Stay Message Sent | Checkbox | ✓ when MSG-04 sent |
| O | Issue During Stay | Dropdown | None / Minor / Major |
| P | Issue Description | Text | Brief description if applicable |
| Q | Review Left by Guest | Number 1–5 | Overall review score |
| R | Review Left by Host | Dropdown | Positive / Neutral / Negative |
| S | Repeat Guest | Checkbox | ✓ if this guest has stayed before |
| T | Notes | Text | Anything notable: early check-in, late check-out, damage, great guest |

---

## SECTION 2 — COUNTRY OF ORIGIN ANALYSIS

After 20+ bookings, the Country of Origin column becomes useful. Sort or filter by country to identify:

- Which nationalities are your most frequent guests
- Whether guests from certain countries tend to have higher review scores
- Whether any market (Germany, France, Netherlands) warrants a translated welcome guide

This analysis is most useful when considering platform diversification. If 40% of your guests are from Germany and you have no German-language listing, a translated title and first paragraph could increase conversion from German-language Airbnb searches.

---

## SECTION 3 — RETURNING GUEST MANAGEMENT

When a guest who has stayed before messages to enquire about a return stay:

1. Check column T (Notes) from their previous booking. Any positive notes should inform your welcome.
2. Mark column S (Repeat Guest) as checked.
3. Offer a 5–10% returning guest discount if your occupancy allows — this costs little and generates strong review language ("our go-to apartment").
4. Reference their previous stay in the MSG-10 inquiry response: "Great to hear from you again — [PROPERTY NAME] will be ready for your return."

---

## SECTION 4 — SPECIAL OCCASION PROTOCOL

If a guest has noted a special occasion (birthday, anniversary, honeymoon) at booking:

- Note it in column M
- Add a handwritten card to the welcome basket mentioning the occasion: "Wishing you a wonderful anniversary — enjoy your stay."
- Cost: €0 additional (the welcome basket is already included)
- Review language effect: guests mentioning a celebration who receive acknowledgement mention it specifically in 67% of reviews

---

## SECTION 5 — QUICK REFERENCE FILTERS

Set up these filter views (Data → Create a filter view) for quick access during operations:

**Filter 1 — Upcoming Check-Ins (Next 7 Days)**
- Check-In date between today and today+7
- Use to: confirm pre-arrival prep is underway for upcoming guests

**Filter 2 — Current Guests (Active Stays)**
- Check-In ≤ today AND Check-Out > today
- Use to: see who is currently in the property

**Filter 3 — Missing Reviews (No Score in Col Q)**
- Review Left by Guest = blank
- Use to: identify bookings where a review has not yet been received (chase within 14-day window)

**Filter 4 — Issues (Any During-Stay Issue)**
- Issue During Stay = Minor OR Major
- Use to: identify patterns in problems over time

---

## EXAMPLE DATA

| A | B | D | E | F | G | J | K | M | Q | R |
|---|---|---|---|---|---|---|---|---|---|---|
| HM3K5V6YB | Maria Santos | 15/01/2026 | 18/01/2026 | 3 | 2 | 14 | Approved | None | 5 | Positive |
| HN7X2Q4PR | James Taylor | 22/01/2026 | 25/01/2026 | 3 | 1 | 12 | Approved | None | 5 | Positive |
| HP4M8W9TS | Sophie Laurent | 03/02/2026 | 10/02/2026 | 7 | 2 | 15 | Approved | Anniversary | 5 | Positive |

---

*Last updated: v1.0.0 · Update within 24 hours of each booking confirmed*
