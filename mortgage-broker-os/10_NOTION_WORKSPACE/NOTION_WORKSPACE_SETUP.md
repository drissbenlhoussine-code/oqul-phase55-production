# Ultimate Mortgage Broker OS — Notion Workspace

## Top-Level Pages
1. Broker HQ
2. Lead Pipeline
3. Clients
4. Applications
5. Tasks
6. Referral Partners
7. Compliance Log
8. KPI Dashboard
9. SOP Library
10. Archive

## Recommended Relations
- Lead Pipeline → Clients when a lead converts
- Clients → Applications (all loans for this client)
- Clients → Tasks (action items per client)
- Applications → Compliance Log
- Referral Partners → Clients (who referred them)
- SOP Library → Tasks (link tasks to their SOPs)

## Core Views
- Lead Pipeline: Board by stage, Follow-up today, Qualified leads, New this week
- Clients: Active, Onboarding, In underwriting, Clear to close, Closed, At risk
- Applications: By stage, Closing this week, Conditions open, Rate lock expiring
- Tasks: My tasks, Due today, By client, By category
- Referral Partners: By type, Top by volume, Last contact, Next action
- KPI Dashboard: Monthly production, Pipeline volume, Income YTD
- Compliance Log: Missing disclosures, Upcoming deadlines, HMDA pending

Import each CSV as a database, then add relations using the field map in Database_Field_Map.csv.
