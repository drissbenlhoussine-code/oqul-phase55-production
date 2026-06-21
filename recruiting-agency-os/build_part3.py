"""Recruiting Agency OS — Part 3: folders 08–09 + KPI XLSX + 10 Notion CSVs/MD"""
import os, csv
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/recruiting-agency-os/Ultimate_Recruiting_Agency_Operating_System/"

NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"

def hf(hex_): return PatternFill("solid", fgColor=hex_)
def bf(bold=True, sz=11, color="000000"): return Font(bold=bold, size=sz, color=color)
def al(h="center", v="center"): return Alignment(horizontal=h, vertical=v, wrap_text=True)
def thin_border():
    s = Side(style='thin', color='CCCCCC')
    return Border(left=s, right=s, top=s, bottom=s)
def hrow(ws, row, cols, texts, bg=NAV, fg=WHT, bold=True, sz=11):
    for col, text in zip(cols, texts):
        c = ws.cell(row=row, column=col, value=text)
        c.fill = hf(bg); c.font = bf(bold, sz, fg)
        c.alignment = al(); c.border = thin_border()
def drow(ws, row, cols, vals, bg=WHT, sz=10):
    for col, val in zip(cols, vals):
        c = ws.cell(row=row, column=col, value=val)
        c.fill = hf(bg); c.font = bf(False, sz)
        c.alignment = al("left"); c.border = thin_border()

def doc(filename, title, subtitle, sections):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
    if subtitle:
        s = d.add_paragraph(subtitle); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10)
        s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    for section in sections:
        if isinstance(section, str):
            d.add_paragraph(section); continue
        heading, items = section
        h = d.add_heading(heading, level=1)
        h.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
        for item in items:
            if isinstance(item, tuple) and item[0] == '•':
                d.add_paragraph(item[1], style='List Bullet')
            else:
                d.add_paragraph(str(item))
    d.save(BASE + filename)
    print(f"  ✓ {filename}")

def write_csv(path, headers, rows):
    with open(BASE + path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow(headers); w.writerows(rows)
    print(f"  ✓ {path}")

# ── 08_BUSINESS_OPERATIONS ────────────────────────────────────────────────────
doc("08_BUSINESS_OPERATIONS/Business_Goals_Workbook.docx",
    "Business Goals Workbook",
    "Recruiting Agency Operating System | Business Operations",
    [
        ("CURRENT STATE ASSESSMENT", [
            ("•", "Annual revenue last year: $_______"),
            ("•", "Number of placements last year: _______"),
            ("•", "Average fee per placement: $_______"),
            ("•", "Number of active clients: _______"),
            ("•", "Average time-to-fill: _______ days"),
            ("•", "Biggest strength: _______________________________"),
            ("•", "Biggest weakness: _______________________________"),
        ]),
        ("ANNUAL GOALS", [
            ("•", "Revenue goal: $_______"),
            ("•", "Placements goal: _______"),
            ("•", "New clients goal: _______"),
            ("•", "Average fee target: $_______"),
            ("•", "Target time-to-fill: _______ days"),
            ("•", "Niche focus for the year: _______________________________"),
        ]),
        ("Q1 SPRINT (90 Days)", [
            ("•", "Revenue target: $_______"),
            ("•", "Placements target: _______"),
            ("•", "New client calls: _______"),
            ("•", "Proposals sent: _______"),
            ("•", "Priority #1: _______________________________"),
            ("•", "Priority #2: _______________________________"),
            ("•", "Priority #3: _______________________________"),
        ]),
        ("MONTHLY REVIEW TEMPLATE (Use Each Month)", [
            ("•", "Placements this month: _______"),
            ("•", "Revenue this month: $_______"),
            ("•", "New clients added: _______"),
            ("•", "BD calls made: _______"),
            ("•", "Biggest win: _______________________________"),
            ("•", "What I'll do differently next month: _______________________________"),
        ]),
        ("WEEKLY FOCUS TEMPLATE", [
            ("•", "Top 3 priorities this week: 1. ___ 2. ___ 3. ___"),
            ("•", "BD activities planned: _______"),
            ("•", "Candidate submissions target: _______"),
            ("•", "Interviews to schedule: _______"),
            ("•", "Offers to close: _______"),
        ]),
    ])

doc("08_BUSINESS_OPERATIONS/Team_Management_Guide.docx",
    "Team Management Guide",
    "Recruiting Agency Operating System | Business Operations",
    [
        ("RECRUITING TEAM STRUCTURE", [
            ("•", "Solo Recruiter (0–$300K revenue): Owner handles all BD and delivery"),
            ("•", "Small Team (1–3 recruiters, $300K–$1M): Owner + 1–2 junior recruiters"),
            ("•", "Growth Stage (4–10 recruiters, $1M–$3M): BD team + Delivery team + Admin"),
            ("•", "Scale Stage (10+ recruiters, $3M+): Multiple verticals, team leads, operations manager"),
        ]),
        ("RECRUITER KPIs TO TRACK", [
            ("•", "BD calls per week: Target [X]"),
            ("•", "New clients signed per month: Target [X]"),
            ("•", "Active job orders per recruiter: Target [X]"),
            ("•", "Candidate phone screens per week: Target [X]"),
            ("•", "Profiles submitted per week: Target [X]"),
            ("•", "Placements per quarter: Target [X]"),
            ("•", "Average fee per placement: Target $_______"),
        ]),
        ("WEEKLY TEAM MEETING AGENDA", [
            "1. Pipeline review (15 min): Each recruiter covers active searches",
            "2. Wins and blockers (10 min): What's working, what needs help",
            "3. Training moment (10 min): Role play, objection handling, market update",
            "4. Priorities for the week (5 min): Top 3 for each person",
        ]),
        ("COMPENSATION STRUCTURES FOR RECRUITERS", [
            ("•", "Base + Commission: Base salary ($[X]K) + [25–35]% of personal billings after threshold"),
            ("•", "Draw Against Commission: Monthly draw + commission; draw repaid from earnings"),
            ("•", "Straight Commission: No base; [35–50]% of billings; for experienced producers"),
            ("•", "Commission threshold: Often set at 3–4x annual base salary"),
        ]),
        ("PERFORMANCE REVIEW FRAMEWORK", [
            ("•", "Quarterly review: KPIs vs target, qualitative feedback, development goals"),
            ("•", "Annual review: Full performance evaluation, comp review, career path discussion"),
            ("•", "PIP process: If recruiter misses target 2 consecutive quarters, implement 30/60/90 day plan"),
        ]),
    ])

doc("08_BUSINESS_OPERATIONS/Recruiter_Training_Manual.docx",
    "Recruiter Training Manual",
    "Recruiting Agency Operating System | Business Operations",
    [
        ("WEEK 1 — FOUNDATIONS", [
            ("•", "Day 1: Company overview, values, tools setup (ATS, LinkedIn, email)"),
            ("•", "Day 2: Recruiting industry overview; how agencies make money; fee structures"),
            ("•", "Day 3: LinkedIn Recruiter deep dive; Boolean search training"),
            ("•", "Day 4: Phone screen training; shadow senior recruiter on 3 calls"),
            ("•", "Day 5: Job board training; candidate assessment framework"),
        ]),
        ("WEEK 2 — CANDIDATE SKILLS", [
            ("•", "Conducting excellent phone screens: practice and role play"),
            ("•", "Writing compelling candidate profiles"),
            ("•", "Reference check training"),
            ("•", "Managing candidate pipeline in ATS"),
            ("•", "Passive candidate outreach via LinkedIn and email"),
        ]),
        ("WEEK 3 — CLIENT SKILLS", [
            ("•", "Business development 101: cold outreach, discovery calls, proposals"),
            ("•", "Client onboarding process"),
            ("•", "Candidate submittal best practices"),
            ("•", "Client communication and weekly updates"),
            ("•", "Handling objections — training with scripts"),
        ]),
        ("WEEK 4 — FULL CYCLE", [
            ("•", "End-to-end simulation: source to placement"),
            ("•", "Offer management and negotiation role play"),
            ("•", "Difficult conversations training"),
            ("•", "Compliance and EEOC review"),
            ("•", "Individual production plan for first 90 days"),
        ]),
        ("30-60-90 DAY TARGETS FOR NEW RECRUITERS", [
            ("•", "Day 30: Complete training, 1 active search assigned, 5 candidate screens/week"),
            ("•", "Day 60: 1 client signed independently, 3 active searches, first submission delivered"),
            ("•", "Day 90: First placement closed, $[X]K in fees billed, 5+ active client relationships"),
        ]),
    ])

print("✓ 08_BUSINESS_OPERATIONS DOCX complete")

# ── 09_MARKETING_GROWTH ───────────────────────────────────────────────────────
doc("09_MARKETING_GROWTH/Content_Marketing_Strategy.docx",
    "Content Marketing Strategy",
    "Recruiting Agency Operating System | Marketing & Growth",
    [
        ("WHY CONTENT MARKETING FOR RECRUITERS", [
            "Content builds credibility with both clients (they trust you with their hiring) and candidates (they trust you with their career). Consistent, useful content generates inbound leads and reduces cold outreach dependence.",
        ]),
        ("CONTENT PILLARS (3–5 Core Themes)", [
            ("•", "Pillar 1 — Hiring Insights: Salary trends, hiring market data, interview best practices (audience: clients/hiring managers)"),
            ("•", "Pillar 2 — Career Advice: Resume tips, interview prep, career growth (audience: candidates)"),
            ("•", "Pillar 3 — Industry News: [Niche industry] trends, workforce news, legislation (audience: both)"),
            ("•", "Pillar 4 — Social Proof: Placement stories, client wins, candidate success (audience: both)"),
            ("•", "Pillar 5 — Behind the Scenes: How you recruit, your process, your team (audience: both)"),
        ]),
        ("CONTENT CALENDAR FRAMEWORK", [
            ("•", "Monday: Career advice / candidate-facing post"),
            ("•", "Wednesday: Hiring insight / client-facing post"),
            ("•", "Friday: Industry news, social proof, or engagement question"),
            ("•", "Target: 3 posts per week on LinkedIn; repurpose to email newsletter monthly"),
        ]),
        ("LEAD GENERATION CONTENT ASSETS", [
            ("•", "Salary guide: '[Year] [Niche] Salary Guide' — collect emails on your website"),
            ("•", "Hiring checklist: '10 Questions to Ask Before Hiring a Recruiter'"),
            ("•", "Webinar: 'How to Attract Top [Role] Talent in [Year]'"),
            ("•", "Case study: '[Company] Filled Their [Role] in 9 Days'"),
        ]),
        ("POSTING BEST PRACTICES", [
            ("•", "Hook in first 2 lines — no context window truncation"),
            ("•", "Write for skimmability: short paragraphs, line breaks"),
            ("•", "End every post with a question or CTA"),
            ("•", "Respond to every comment within 2 hours for the first 60 minutes"),
            ("•", "Use 3–5 relevant hashtags"),
        ]),
    ])

doc("09_MARKETING_GROWTH/LinkedIn_Growth_Playbook.docx",
    "LinkedIn Growth Playbook",
    "Recruiting Agency Operating System | Marketing & Growth",
    [
        ("PROFILE OPTIMIZATION", [
            ("•", "Headline: [Niche] Recruiter | Helping [Client type] Hire [Role type] in [Timeframe]"),
            ("•", "About section: 3-paragraph story — who you help, how you help them, proof, CTA"),
            ("•", "Featured section: Case study PDF, salary guide, testimonial screenshot"),
            ("•", "Experience: Quantify results ('Placed 50+ [role] professionals in [industry]')"),
            ("•", "Skills: Add 10 relevant skills; ask connections to endorse top 3"),
        ]),
        ("CONTENT STRATEGY (3 Posts/Week)", [
            ("•", "Post types: Text, carousel (3–8 slides), video (60–90 sec), polls"),
            ("•", "Best times: Tue–Thu, 7–9am or 5–7pm in your audience's timezone"),
            ("•", "Engagement hack: Comment meaningfully on 5–10 posts daily (yours + others)"),
        ]),
        ("CONNECTION GROWTH STRATEGY", [
            ("•", "Connect with 20–30 target prospects per day (max LinkedIn allows)"),
            ("•", "Personalize every connection note (2 sentences max)"),
            ("•", "Engage with connections' posts before reaching out"),
            ("•", "Join and participate in 3–5 relevant LinkedIn groups"),
        ]),
        ("THOUGHT LEADERSHIP CONTENT IDEAS", [
            ("•", "'The #1 mistake I see hiring managers make when interviewing candidates'"),
            ("•", "'I reviewed 200 resumes this month. Here's what stands out.'"),
            ("•", "'5 signs a job offer is too good to be true'"),
            ("•", "'What separates a $90K candidate from a $130K candidate (same role)'"),
            ("•", "'I asked 50 candidates why they left their last job. The answers surprised me.'"),
        ]),
        ("NEWSLETTER / DM CAMPAIGNS", [
            ("•", "LinkedIn Newsletter: 'The [Niche] Hiring Report' — monthly trends and insights"),
            ("•", "DM campaign to followers: 'I share weekly hiring tips — want to be on the list?'"),
            ("•", "Conversion: LinkedIn followers → email list → booked calls"),
        ]),
    ])

doc("09_MARKETING_GROWTH/Referral_Partner_System.docx",
    "Referral Partner System",
    "Recruiting Agency Operating System | Marketing & Growth",
    [
        ("WHO TO TARGET AS REFERRAL PARTNERS", [
            ("•", "Employment attorneys (non-competing; serve same clients)"),
            ("•", "HR consultants and fractional HR professionals"),
            ("•", "Business coaches and executive coaches"),
            ("•", "Payroll and benefits providers"),
            ("•", "Outplacement firms (they place exiting employees — you place new ones)"),
            ("•", "Business bankers and commercial lenders"),
            ("•", "EAP and wellness providers serving employers"),
        ]),
        ("REFERRAL PARTNER OUTREACH SCRIPT", [
            "'Hi [Name], I'm [Your Name] from [Agency]. I specialize in [niche] recruiting. I work with many of the same companies you do, and I've found that my clients often need [HR/legal/payroll] support. I'd love to explore a referral relationship — we send business each other's way. Are you open to a 20-minute call?'",
        ]),
        ("REFERRAL PROGRAM STRUCTURE", [
            ("•", "Client referral (from existing clients): $[X] gift card or [X]% fee credit"),
            ("•", "Partner referral (from referral partners): [X]% of placement fee, paid on placement"),
            ("•", "Candidate referral (from placed candidates): $[X] gift card per referred hire"),
            ("•", "Define: Referral must be a warm introduction (not just a name); valid for [12] months"),
        ]),
        ("KEEPING PARTNERS ENGAGED", [
            ("•", "Monthly check-in: 1 email or call per month with market update"),
            ("•", "Co-content: Joint webinar, co-branded article, guest post on each other's newsletter"),
            ("•", "Annual partner event: Breakfast, dinner, or virtual meetup for your referral network"),
            ("•", "Thank you gifts: For every referral (regardless of outcome) — a handwritten note + small gift"),
        ]),
    ])

doc("09_MARKETING_GROWTH/Personal_Brand_Guide.docx",
    "Personal Brand Guide",
    "Recruiting Agency Operating System | Marketing & Growth",
    [
        ("DEFINING YOUR PERSONAL BRAND", [
            ("•", "Niche: What specific role type and industry do you specialize in?"),
            ("•", "Value proposition: What do you do better or differently than other recruiters?"),
            ("•", "Personality: Professional but approachable? Data-driven? Empathetic? Direct?"),
            ("•", "Story: Why did you get into recruiting? What drives you?"),
        ]),
        ("YOUR BRAND STATEMENT", [
            "Template: 'I help [client type] hire [role type] professionals in [timeframe/context] so they can [outcome].'",
            "Example: 'I help fintech startups hire senior engineers in under 2 weeks so they can ship products without being bottlenecked by talent.'",
        ]),
        ("CONTENT VOICE GUIDELINES", [
            ("•", "Write like you talk — conversational, clear, no jargon"),
            ("•", "Share opinions — not just information (opinions = engagement)"),
            ("•", "Be honest about challenges — vulnerability builds trust"),
            ("•", "Avoid: Clichés ('passionate', 'guru', 'rockstar'), vague generalizations, excessive self-promotion"),
        ]),
        ("VISUAL BRAND BASICS", [
            ("•", "Professional headshot: Updated, good lighting, approachable expression"),
            ("•", "LinkedIn banner: Name + niche + tagline + logo if applicable"),
            ("•", "Consistent color palette and fonts across all content"),
            ("•", "Logo: Simple wordmark is sufficient for solo recruiters"),
        ]),
        ("CHANNELS TO PRIORITIZE", [
            ("•", "LinkedIn: Primary channel for both clients and candidates"),
            ("•", "Email newsletter: Owned audience; most valuable long-term asset"),
            ("•", "Instagram/X: Optional; useful for employer brand and candidate attraction"),
            ("•", "YouTube/Podcast: Long-form authority content (advanced stage)"),
        ]),
    ])

print("✓ 09_MARKETING_GROWTH DOCX complete")

# ── KPI Dashboard XLSX ────────────────────────────────────────────────────────
wb = Workbook()
ws = wb.active; ws.title = "KPI Dashboard"
ws.column_dimensions['A'].width = 30
ws.column_dimensions['B'].width = 15
ws.column_dimensions['C'].width = 15
ws.column_dimensions['D'].width = 15
ws.column_dimensions['E'].width = 15

# Production metrics section
ws.merge_cells('A1:E1')
c = ws['A1']; c.value = "RECRUITING AGENCY — KPI DASHBOARD"
c.fill = hf(NAV); c.font = bf(True, 14, WHT); c.alignment = al()

hrow(ws, 2, [1,2,3,4,5], ["Metric","Target","Jan","Feb","Mar"], ACC, WHT)
metrics = [
    ("Placements","8","6","7","8"),
    ("Revenue","$144,000","$108,000","$126,000","$144,000"),
    ("Avg Fee","$18,000","$18,000","$18,000","$18,000"),
    ("New Clients","3","2","3","3"),
    ("BD Calls Made","60","48","54","60"),
    ("Proposals Sent","12","9","10","12"),
    ("Time-to-Fill (days)","18","22","20","18"),
    ("Candidate Screens","80","65","72","80"),
    ("Profiles Submitted","40","32","36","40"),
    ("Offer Accept Rate","85%","78%","82%","85%"),
]
for i, row in enumerate(metrics, 3):
    drow(ws, i, [1,2,3,4,5], list(row), LGR if i%2==0 else WHT)

ws2 = wb.create_sheet("Revenue Projection")
ws2.column_dimensions['A'].width = 20
ws2.column_dimensions['B'].width = 18
ws2.column_dimensions['C'].width = 18
ws2.column_dimensions['D'].width = 18

hrow(ws2, 1, [1,2,3,4], ["Month","Placements","Avg Fee","Revenue"], GLD, "000000")
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
for i, m in enumerate(months, 2):
    drow(ws2, i, [1,2,3,4], [m,"","$18,000","=B{0}*C{0}".format(i)], LGR if i%2==0 else WHT)

wb.save(BASE + "08_BUSINESS_OPERATIONS/Business_KPI_Dashboard.xlsx")
print("  ✓ 08_BUSINESS_OPERATIONS/Business_KPI_Dashboard.xlsx")

# ── 10_NOTION_WORKSPACE — CSV databases ─────────────────────────────────────

write_csv("10_NOTION_WORKSPACE/Candidates_Database.csv",
    ["Name","Current Title","Current Company","Target Role","Salary Expectation","Availability","Stage","Client Match","Recruiter","Phone Screen Date","Score","Notes"],
    [
        ["Alex Turner","Sr. Account Executive","TechCorp","VP of Sales","$140,000","2 weeks","Submitted","Acme Corp","[Recruiter]","Jan 10","8","Strong closer; great culture fit"],
        ["Maria Santos","Engineering Manager","StartupX","Sr. Engineer","$160,000","1 month","Phone Screen","Beta Inc","[Recruiter]","Jan 11","7","Solid technical background; verify React depth"],
        ["James Liu","Marketing Director","BrandCo","Marketing Manager","$120,000","Immediate","Offer Stage","Gamma Co","[Recruiter]","Jan 5","9","Top candidate; managing competing offer"],
    ])

write_csv("10_NOTION_WORKSPACE/Clients_Database.csv",
    ["Company","Primary Contact","Title","Email","Phone","Industry","Active Roles","Placements YTD","Total Fees YTD","Status","Account Owner","Contract Signed"],
    [
        ["Acme Corp","Sarah Johnson","VP HR","sarah@acme.com","555-0101","SaaS","2","3","$54,000","Active","[Recruiter]","Yes"],
        ["Beta Inc","Mike Chen","CEO","mike@beta.com","555-0102","Fintech","1","1","$18,000","Active","[Recruiter]","Yes"],
        ["Gamma Co","Lisa Park","HR Director","lisa@gamma.com","555-0103","Healthcare","1","5","$90,000","Active","[Recruiter]","Yes"],
        ["Delta LLC","Tom Rodriguez","COO","tom@delta.com","555-0104","E-commerce","1","0","$0","Onboarding","[Recruiter]","Yes"],
    ])

write_csv("10_NOTION_WORKSPACE/Job_Orders_Database.csv",
    ["Job Order ID","Client","Role Title","Department","Salary Min","Salary Max","Location","Remote","Start Date Target","Date Opened","Status","Recruiter","Priority"],
    [
        ["JO-001","Acme Corp","VP of Sales","Sales","$130,000","$150,000","New York, NY","Hybrid","Feb 1","Jan 5","Active","[Recruiter]","High"],
        ["JO-002","Beta Inc","Senior Engineer","Engineering","$150,000","$180,000","Remote","Full Remote","Feb 15","Jan 3","Interviewing","[Recruiter]","High"],
        ["JO-003","Gamma Co","Marketing Manager","Marketing","$110,000","$130,000","Chicago, IL","Hybrid","Jan 20","Dec 28","Offer Stage","[Recruiter]","Urgent"],
        ["JO-004","Delta LLC","Operations Director","Operations","$120,000","$140,000","Austin, TX","On-Site","Mar 1","Jan 10","Sourcing","[Recruiter]","Medium"],
    ])

write_csv("10_NOTION_WORKSPACE/Placements_Database.csv",
    ["Placement ID","Candidate Name","Client Company","Role Placed","Start Date","Base Salary","Fee %","Fee Amount","Guarantee End","Status","Recruiter"],
    [
        ["PL-001","Previous Candidate A","Acme Corp","Director of Sales","Oct 1","$145,000","20%","$29,000","Dec 30","Active — Guaranteed","[Recruiter]"],
        ["PL-002","Previous Candidate B","Beta Inc","Sr. Engineer","Nov 15","$165,000","20%","$33,000","Feb 13","Active — Guaranteed","[Recruiter]"],
        ["PL-003","Previous Candidate C","Gamma Co","CFO","Sep 1","$210,000","25%","$52,500","Nov 30","Guarantee Expired","[Recruiter]"],
    ])

write_csv("10_NOTION_WORKSPACE/Tasks_Database.csv",
    ["Task","Related To","Type","Priority","Due Date","Status","Assigned To","Notes"],
    [
        ["Send weekly update to Acme Corp","Acme Corp — JO-001","Client Communication","High","Jan 15","To Do","[Recruiter]","Include 3 new profiles"],
        ["Screen Alex Turner for VP Sales","JO-001 / Alex Turner","Candidate Screen","High","Jan 12","In Progress","[Recruiter]","Phone screen scheduled 10am"],
        ["Prepare offer letter for James Liu","JO-003 / James Liu","Offer Management","Urgent","Jan 13","To Do","[Recruiter]","Client approved $122K base"],
        ["Post LinkedIn content","Marketing","Content","Medium","Jan 14","To Do","[Recruiter]","Career advice post"],
        ["Follow up with Delta LLC onboarding","Delta LLC","Client Communication","Medium","Jan 15","To Do","[Recruiter]","Send kickoff call link"],
    ])

write_csv("10_NOTION_WORKSPACE/Business_Development_Database.csv",
    ["Company","Contact","Title","Email","Stage","First Outreach","Last Touch","Next Action","Est Fee","Source","Notes"],
    [
        ["Prospect Corp","Jane Smith","VP HR","jane@prospect.com","Discovery Call","Jan 5","Jan 10","Send proposal","$20,000","LinkedIn","Very interested; hiring 3 roles"],
        ["Growth Inc","Bob Lee","CEO","bob@growth.com","Cold Outreach","Jan 8","Jan 8","Follow up Day 3","$16,000","Referral","Referred by Acme Corp"],
        ["Scale LLC","Amy Davis","COO","amy@scale.com","Proposal Sent","Jan 2","Jan 9","Follow up","$24,000","Cold Email","Proposal sent Jan 9"],
    ])

write_csv("10_NOTION_WORKSPACE/Content_Calendar_Database.csv",
    ["Post Title","Pillar","Format","Platform","Publish Date","Status","CTA","Engagement Notes"],
    [
        ["5 Signs a Candidate Will Resign Within 90 Days","Hiring Insights","Text","LinkedIn","Jan 15","Drafted","DM me if you want the full checklist",""],
        ["Resume Red Flags I See Every Week","Career Advice","Text","LinkedIn","Jan 17","Planned","Save this post",""],
        ["How We Filled a CTO Role in 11 Days","Social Proof","Carousel","LinkedIn","Jan 20","Planned","Comment 'case study' for the full story",""],
        ["The Candidate Market in Q1 2025","Industry News","Text","LinkedIn","Jan 22","Planned","What are you seeing in your industry?",""],
    ])

write_csv("10_NOTION_WORKSPACE/SOP_Library.csv",
    ["SOP Name","Category","Version","Last Updated","Owner","Summary"],
    [
        ["New Client Onboarding SOP","Client Management","v1.0","Jan 2024","[Agency Owner]","Day-by-day process from signed agreement to first profiles delivered"],
        ["Candidate Phone Screen SOP","Candidate Management","v1.0","Jan 2024","[Agency Owner]","20-minute screen structure; scoring; next steps"],
        ["Offer Management SOP","Placement Process","v1.0","Jan 2024","[Agency Owner]","Verbal offer to signed acceptance; counter-offer prevention"],
        ["BD Outreach SOP","Business Development","v1.0","Jan 2024","[Agency Owner]","7-touch sequence; objection handling; proposal process"],
    ])

write_csv("10_NOTION_WORKSPACE/Database_Field_Map.csv",
    ["Database","Field Name","Field Type","Description"],
    [
        ["Candidates","Name","Title","Candidate full name"],
        ["Candidates","Stage","Select","Phone Screen / Submitted / Interviewing / Offer / Placed / Rejected"],
        ["Candidates","Score","Number","1–10 assessment score"],
        ["Job Orders","Status","Select","Sourcing / Active / Interviewing / Offer / Filled / On Hold / Cancelled"],
        ["Job Orders","Priority","Select","Low / Medium / High / Urgent"],
        ["Clients","Status","Select","Prospect / Onboarding / Active / Inactive"],
        ["Placements","Guarantee End","Date","90 days from start date"],
        ["Tasks","Priority","Select","Low / Medium / High / Urgent"],
        ["BD Pipeline","Stage","Select","Cold / Contacted / Discovery / Proposal / Negotiation / Won / Lost"],
        ["Content Calendar","Status","Select","Idea / Drafted / Scheduled / Published"],
    ])

# Notion Setup Guide (MD)
with open(BASE + "10_NOTION_WORKSPACE/NOTION_WORKSPACE_SETUP.md", "w", encoding="utf-8") as f:
    f.write("""# Recruiting Agency Notion Workspace Setup Guide

## Overview
Your Notion workspace is organized around the full recruiting lifecycle — from business development through placement and retention.

---

## Top-Level Pages to Create

| Page Name | Icon | Purpose |
|---|---|---|
| 🎯 Business Development | Target | BD pipeline, prospect tracking |
| 👥 Clients | Building | Active client management |
| 📋 Job Orders | Clipboard | Open and filled roles |
| 🙋 Candidates | Person | Full candidate database |
| ✅ Placements | Check | Completed placements & guarantees |
| ✅ Tasks | Checkbox | Daily task management |
| 📅 Content Calendar | Calendar | LinkedIn/marketing content |
| 📚 SOP Library | Book | All agency SOPs |

---

## Step 1 — Import CSV Databases

1. Open Notion → Click **New Page** → Select **Import**
2. Choose **CSV** and upload each database file:
   - `Candidates_Database.csv`
   - `Clients_Database.csv`
   - `Job_Orders_Database.csv`
   - `Placements_Database.csv`
   - `Tasks_Database.csv`
   - `Business_Development_Database.csv`
   - `Content_Calendar_Database.csv`
   - `SOP_Library.csv`
3. After import, rename each page to match the table above.

---

## Step 2 — Set Up Database Relations

Link related databases for a connected workspace:

- **Job Orders ↔ Clients**: Every job order linked to a client
- **Candidates ↔ Job Orders**: Candidates linked to the role they're being considered for
- **Placements ↔ Candidates + Clients**: Track who was placed where
- **Tasks ↔ Job Orders + Clients**: Tasks linked to relevant searches

---

## Step 3 — Create Key Views

### Candidates Database
- **Board view**: Group by Stage (Phone Screen / Submitted / Interviewing / Offer / Placed)
- **Table view**: Full candidate list sorted by Score
- **Filter view**: "Active" — exclude Rejected

### Job Orders
- **Board view**: Group by Status (Sourcing / Active / Interviewing / Offer / Filled)
- **Calendar view**: Grouped by Start Date Target

### Tasks
- **Board view**: Group by Priority
- **Calendar view**: By Due Date

### BD Pipeline
- **Board view**: Group by Stage
- **Filter**: Show only active prospects (not Lost)

---

## Step 4 — Add Formula Properties

After import, add these calculated fields:

- **Candidates**: Days Since Screen = `dateBetween(now(), prop("Phone Screen Date"), "days")`
- **Placements**: Guarantee Remaining = `dateBetween(prop("Guarantee End"), now(), "days")`
- **Job Orders**: Days Open = `dateBetween(now(), prop("Date Opened"), "days")`

---

## Step 5 — Weekly Dashboard Page

Create a **Dashboard** page with linked database views:
- This Week's Tasks (filter: Due Date = this week)
- Active Job Orders (filter: Status = Active)
- Candidates in Offer Stage
- Overdue BD Follow-ups (filter: Next Action date past)
""")
print("  ✓ 10_NOTION_WORKSPACE/NOTION_WORKSPACE_SETUP.md")

print("PART 3 DONE")
