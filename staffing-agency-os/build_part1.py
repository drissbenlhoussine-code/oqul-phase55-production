import os, csv, json, zipfile
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/staffing-agency-os/Ultimate_Staffing_Agency_OS/"

def doc(filename, title, subtitle, sections):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
    if subtitle:
        s = d.add_paragraph(subtitle); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10)
        s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for section in sections:
        if isinstance(section, str): d.add_paragraph(section); continue
        heading, items = section
        h = d.add_heading(heading, level=1)
        h.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
        for item in items:
            if isinstance(item, tuple) and item[0] == '•':
                d.add_paragraph(item[1], style='List Bullet')
            else: d.add_paragraph(str(item))
    d.save(BASE + filename); print(f"  ✓ {filename}")

NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"
def hf(h): return PatternFill("solid", fgColor=h)
def bf(bold=True,sz=11,color="000000"): return Font(bold=bold,size=sz,color=color)
def al(h="center",v="center"): return Alignment(horizontal=h,vertical=v,wrap_text=True)
def thin(): s=Side(style='thin',color='CCCCCC'); return Border(left=s,right=s,top=s,bottom=s)
def hrow(ws,row,cols,texts,bg=NAV,fg=WHT):
    for col,text in zip(cols,texts):
        c=ws.cell(row=row,column=col,value=text)
        c.fill=hf(bg); c.font=bf(True,11,fg); c.alignment=al(); c.border=thin()
def drow(ws,row,cols,vals,bg=WHT):
    for col,val in zip(cols,vals):
        c=ws.cell(row=row,column=col,value=val)
        c.fill=hf(bg); c.font=bf(False,10); c.alignment=al("left"); c.border=thin()

def write_csv(path, headers, rows):
    with open(BASE+path,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
    print(f"  ✓ {path}")

print("\n=== PART 1: Folders + 00/01/02/03 ===\n")

# ── 00_START_HERE ──────────────────────────────────────────────────────────────
print("00_START_HERE...")

with open(BASE+"00_START_HERE/README_FIRST.txt","w",encoding="utf-8") as f:
    f.write("""WELCOME TO THE ULTIMATE STAFFING AGENCY OPERATING SYSTEM
==========================================================

Thank you for purchasing the most comprehensive staffing agency toolkit available.
This system covers EVERYTHING you need to run a professional temp/contract AND
direct-placement staffing agency from day one.

WHAT YOU HAVE:
--------------
67 professionally crafted files across 13 organized folders — scripts, templates,
spreadsheets, Canva-ready decks, Notion databases, compliance guides, and bonuses.

QUICK NAVIGATION:
-----------------
00_START_HERE/       → You are here. Read Quick_Start_Checklist.docx next.
01_BUSINESS_DEV/     → Client prospecting, cold outreach, pitch decks, BD CRM
02_CLIENT_MGMT/      → Intake forms, job orders, agreements, communication SOPs
03_CANDIDATE_SOURCE/ → LinkedIn playbook, boolean strings, outreach scripts
04_CANDIDATE_SCREEN/ → Phone screens, competency interviews, scorecards, references
05_TEMP_PLACEMENT/   → Assignment confirmations, onboarding, timesheets
06_DIRECT_PLACEMENT/ → Interview prep, offer negotiation, post-placement follow-up
07_COMPLIANCE_LEGAL/ → Agreements, EEOC, FCRA, co-employment, NDAs
08_BILLING_PAYROLL/  → Fee invoices, markup calculations, payroll integration
09_AGENCY_OPS/       → Recruiter training, KPI dashboards, operations manual
10_NOTION_WORKSPACE/ → 7 import-ready CSV databases + setup guide
11_BONUSES/          → 365 captions, scripts vault, growth playbook, salary guide
12_CANVA_TEMPLATES/  → 4 presentation decks ready to brand in Canva

DAY 1 PRIORITIES:
-----------------
1. Read Quick_Start_Checklist.docx in this folder
2. Set up your Notion workspace using 10_NOTION_WORKSPACE/Notion_Setup_Guide.md
3. Import Business_Development_CRM.xlsx into your workflow
4. Study Client_Prospecting_Scripts.docx — make your first BD call today
5. Review 07_COMPLIANCE_LEGAL/Client_Service_Agreement_Template.docx

IMPORTANT NOTES:
----------------
• All legal templates should be reviewed by your attorney before use
• Fee percentages are industry examples — adjust to your market
• CSV files open best in Excel or Google Sheets
• PPTX files can be imported into Canva for branding

Questions? The Agency_Operations_Manual.docx in 09_AGENCY_OPS answers most FAQs.

Good luck — you have everything you need to build a thriving staffing agency.
""")
print("  ✓ 00_START_HERE/README_FIRST.txt")

doc("00_START_HERE/Quick_Start_Checklist.docx",
    "STAFFING AGENCY OS — QUICK START CHECKLIST",
    "Your action plan for Days 1, 7, and 30",
    [
        ("DAY 1: FOUNDATIONS (Today)", [
            ("•","Read this entire checklist before doing anything else"),
            ("•","Set up your business entity if not already done (LLC recommended)"),
            ("•","Open a dedicated business checking account"),
            ("•","Register for an EIN at IRS.gov (free, instant online)"),
            ("•","Purchase business liability insurance and E&O coverage"),
            ("•","Set up a professional email (yourname@agencyname.com)"),
            ("•","Import Notion CSV files from 10_NOTION_WORKSPACE/ into Notion.so"),
            ("•","Customize the Client_Service_Agreement_Template.docx with your details"),
            ("•","Study the Client_Prospecting_Scripts.docx — memorize the cold call opener"),
            ("•","Make your first 10 business development calls using the BD scripts"),
        ]),
        ("WEEK 1: FIRST CLIENT PURSUIT", [
            ("•","Identify your niche (Healthcare, Finance, Manufacturing, Tech, etc.)"),
            ("•","Build your target company list — aim for 50 companies in your niche"),
            ("•","Set up LinkedIn Sales Navigator or use free LinkedIn strategically"),
            ("•","Send 20 cold outreach emails using Cold_Outreach_Templates.docx"),
            ("•","Schedule at least 2 discovery calls with potential clients"),
            ("•","Prepare your pitch using Client_Pitch_Deck_Framework.docx"),
            ("•","Post 5 social media posts using 365_Social_Media_Captions.csv"),
            ("•","Complete your agency profile: website, LinkedIn company page, Google Business"),
            ("•","Set up your BD tracking in Business_Development_CRM.xlsx"),
            ("•","Review all fee structures in 08_BILLING_PAYROLL/Fee_Structure_And_Invoice_Templates.docx"),
        ]),
        ("WEEK 2-4: FIRST SEARCHES", [
            ("•","Sign your first client using Search_Assignment_Agreement.docx"),
            ("•","Complete a thorough intake using Client_Intake_And_Discovery_Form.docx"),
            ("•","Create your first Job Order using Job_Order_Template.docx"),
            ("•","Source 20 candidates using LinkedIn_Sourcing_Playbook.docx strategy"),
            ("•","Screen top 5 candidates using Phone_Screen_Interview_Guide.docx"),
            ("•","Submit 3 qualified candidates to your client"),
            ("•","Track all activity in Notion_Recruiter_Activity.csv"),
            ("•","Schedule your first candidate interviews with the client"),
            ("•","Follow up post-interview using Client_Communication_SOP.docx cadence"),
            ("•","Study Compliance_Checklist.docx — EEOC and FCRA compliance is non-negotiable"),
        ]),
        ("MONTH 1: BUILD MOMENTUM", [
            ("•","Target: 3+ active job orders by end of month"),
            ("•","Target: 1 placement confirmed (temp or perm)"),
            ("•","Target: Invoice sent and payment received"),
            ("•","Set up payroll partner if doing temp placements (see Payroll_Integration_Guide.docx)"),
            ("•","Begin building your candidate database — aim for 50 qualified candidates"),
            ("•","Start tracking KPIs in KPI_Dashboard.xlsx weekly"),
            ("•","Join your local NAPS, ASA, or SHRM chapter for networking"),
            ("•","Review Agency_Growth_Playbook.docx for months 2-6 strategy"),
            ("•","Post consistently on social media — use the 365 captions daily"),
            ("•","Celebrate your first placement — you are now a staffing professional!"),
        ]),
        ("ONGOING WEEKLY HABITS", [
            ("•","Monday: Review pipeline in Client_Pipeline_Tracker.xlsx"),
            ("•","Daily: 20-30 BD calls + 20 BD emails minimum"),
            ("•","Daily: Source 10 new candidates per open role"),
            ("•","Weekly: Send client updates per Client_Communication_SOP.docx"),
            ("•","Weekly: Update all tracking spreadsheets and Notion databases"),
            ("•","Monthly: Review KPIs and adjust strategy using KPI_Dashboard.xlsx"),
            ("•","Monthly: Add new content from 365_Social_Media_Captions.csv"),
            ("•","Quarterly: Review and update fee structures and service agreements"),
        ]),
    ])

doc("00_START_HERE/Product_Overview.docx",
    "STAFFING AGENCY OPERATING SYSTEM — COMPLETE PRODUCT OVERVIEW",
    "Everything you need to run a professional staffing agency",
    [
        ("ABOUT THIS SYSTEM", [
            "The Staffing Agency Operating System is the most comprehensive toolkit available for independent recruiters, boutique staffing agencies, and established firms looking to systematize their operations. Built by industry professionals with decades of combined staffing experience.",
            "This system covers BOTH temp/contract staffing AND direct (permanent) placement — the only toolkit you will ever need.",
        ]),
        ("FOLDER 00: START HERE", [
            ("•","README_FIRST.txt — Welcome file and navigation guide"),
            ("•","Quick_Start_Checklist.docx — Day 1, Week 1, Month 1 action plan"),
            ("•","Product_Overview.docx — This file"),
        ]),
        ("FOLDER 01: BUSINESS DEVELOPMENT", [
            ("•","Client_Prospecting_Scripts.docx — Cold call scripts for 4 industries, LinkedIn and email outreach"),
            ("•","Business_Development_Email_Sequences.docx — Complete 5-email BD nurture sequence"),
            ("•","Client_Pitch_Deck_Framework.docx — How to win client meetings and close agreements"),
            ("•","Cold_Outreach_Templates.docx — 10 email + 5 LinkedIn cold outreach templates"),
            ("•","Business_Development_CRM.xlsx — 3-sheet CRM: prospects, activity log, revenue pipeline"),
        ]),
        ("FOLDER 02: CLIENT MANAGEMENT", [
            ("•","Client_Intake_And_Discovery_Form.docx — 6-section deep discovery process"),
            ("•","Job_Order_Template.docx — Complete job specification template"),
            ("•","Search_Assignment_Agreement.docx — Professional fee agreement with guarantee terms"),
            ("•","Client_Communication_SOP.docx — Cadence, scripts, escalation procedures"),
        ]),
        ("FOLDER 03: CANDIDATE SOURCING", [
            ("•","LinkedIn_Sourcing_Playbook.docx — Boolean strategy, passive ID, InMail templates"),
            ("•","Boolean_Search_String_Library.docx — 20+ ready-to-use boolean strings by role"),
            ("•","Passive_Candidate_Outreach_Scripts.docx — 15 scripts for LinkedIn, email, phone"),
            ("•","Job_Board_Optimization_Guide.docx — Indeed, LinkedIn, ZipRecruiter, niche board strategy"),
        ]),
        ("FOLDER 04: CANDIDATE SCREENING", [
            ("•","Phone_Screen_Interview_Guide.docx — 40+ screening questions with flow guide"),
            ("•","Competency_Based_Interview_Questions.docx — 50 questions across 10 competencies"),
            ("•","Candidate_Assessment_Scorecard.docx — Scoring rubric with rating scales"),
            ("•","Reference_Check_Scripts.docx — Reference call script + red flag guide"),
            ("•","Background_Check_SOP.docx — FCRA-compliant background check process"),
        ]),
        ("FOLDER 05: TEMP PLACEMENT", [
            ("•","Temp_Assignment_Confirmation.docx — Assignment letter for temp workers"),
            ("•","Temp_Worker_Onboarding_Checklist.docx — I-9, W-4, safety orientation checklist"),
            ("•","Timesheet_Management_SOP.docx — Timesheet process, approval, dispute resolution"),
            ("•","Client_Assignment_Communication.docx — Confirming temp worker to client"),
        ]),
        ("FOLDER 06: DIRECT PLACEMENT", [
            ("•","Interview_Preparation_Guide.docx — STAR method, company research, prep scripts"),
            ("•","Offer_Negotiation_Scripts.docx — Present offers, handle counteroffers"),
            ("•","Counteroffer_Prevention_Scripts.docx — Pre-close, resignation support, day-1 check-in"),
            ("•","Placement_Confirmation_SOP.docx — Confirmed placement process and fee invoicing"),
            ("•","Post_Placement_Follow_Up_System.docx — 30-60-90 day check-in scripts"),
        ]),
        ("FOLDER 07: COMPLIANCE & LEGAL", [
            ("•","Client_Service_Agreement_Template.docx — Full legal service agreement"),
            ("•","Candidate_Placement_Agreement.docx — Candidate terms of representation"),
            ("•","Retained_Search_Agreement.docx — Retainer structure and milestones"),
            ("•","Confidentiality_And_NonCompete_Guide.docx — NDA best practices"),
            ("•","Compliance_Checklist.docx — EEOC, Title VII, ADA, FCRA, state requirements"),
            ("•","Staffing_Compliance_Reference_Guide.pdf — Quick-reference compliance PDF"),
        ]),
        ("FOLDER 08: BILLING & PAYROLL", [
            ("•","Fee_Structure_And_Invoice_Templates.docx — Contingency, retainer, temp markup invoices"),
            ("•","Billing_And_Collections_SOP.docx — Invoicing, payment terms, collections"),
            ("•","Markup_Calculation_Guide.docx — How to calculate temp markup profitably"),
            ("•","Payroll_Integration_Guide.docx — In-house vs PEO vs payroll company options"),
        ]),
        ("FOLDER 09: AGENCY OPERATIONS", [
            ("•","Recruiter_Daily_Activity_Guide.docx — Ideal recruiter day with daily targets"),
            ("•","Recruiter_Training_Program.docx — 90-day curriculum: learning, shadowing, independent"),
            ("•","Agency_Operations_Manual.docx — Complete operations manual"),
            ("•","KPI_Dashboard.xlsx — Recruiter KPIs, revenue tracking, conversion rate analytics"),
            ("•","90_Day_Growth_Workbook.pdf — 0 to $50k billing roadmap"),
        ]),
        ("FOLDER 10: NOTION WORKSPACE", [
            ("•","7 import-ready CSV databases for Notion"),
            ("•","Notion_Setup_Guide.md — Import instructions and database linking guide"),
            ("•","Staffing_Agency_OS_User_Guide.pdf — Complete user guide PDF"),
        ]),
        ("FOLDER 11: BONUSES", [
            ("•","365_Social_Media_Captions.csv — One caption per day for a full year"),
            ("•","Staffing_Scripts_Vault.docx — 50+ scripts for every situation"),
            ("•","Agency_Growth_Playbook.docx — From solo recruiter to agency owner"),
            ("•","Salary_Benchmarking_Template.docx — Build market salary guides"),
        ]),
        ("FOLDER 12: CANVA TEMPLATES", [
            ("•","Client_Pitch_Deck.pptx — 6-slide branded pitch presentation"),
            ("•","Candidate_Presentation.pptx — 5-slide candidate summary deck"),
            ("•","Market_Report_Template.pptx — 5-slide market intelligence report"),
            ("•","Social_Media_Content_Pack.pptx — 4 ready-to-brand social graphics"),
        ]),
    ])

# ── 01_BUSINESS_DEVELOPMENT ────────────────────────────────────────────────────
print("\n01_BUSINESS_DEVELOPMENT...")

doc("01_BUSINESS_DEVELOPMENT/Client_Prospecting_Scripts.docx",
    "CLIENT PROSPECTING SCRIPTS",
    "Cold Call, LinkedIn, and Email Scripts for New Business Development",
    [
        ("COLD CALL OPENING SCRIPT (Universal)", [
            "Use this script for your initial cold call to a new prospect. Practice until it feels natural — the goal is a 15-minute discovery call, not a sale.",
            "",
            "RING RING...",
            "[Prospect answers]",
            "",
            'YOU: "Hi [Name], this is [Your Name] with [Agency Name]. I know this is out of the blue — I\'ll be quick. We work exclusively with [Industry] companies in [City/Region] helping them fill [roles] faster and with better retention. I\'m not calling to sell you anything today — I\'m just curious, what\'s your current process when you need to bring on a [role] quickly?"',
            "",
            '[Prospect responds — listen carefully]',
            "",
            'YOU: "Got it. We actually specialize in exactly that situation. I\'ve placed [X] [roles] in the last 90 days and the average time-to-fill was [X days]. Would it make sense to grab 15 minutes this week or next to see if we\'d be a fit for your team?"',
        ]),
        ("COLD CALL — GATEKEEPER SCRIPT", [
            'GATEKEEPER: "What is this regarding?"',
            'YOU: "Sure — I\'m following up on a message I left for [Name] about their hiring process for [role type]. Could you let them know [Your Name] from [Agency] is calling?"',
            "",
            'GATEKEEPER: "They\'re not available."',
            'YOU: "No problem. What\'s the best way to reach them — email or a direct line? I want to make sure I\'m not wasting anyone\'s time."',
        ]),
        ("COLD CALL — MANUFACTURING INDUSTRY SCRIPT", [
            'YOU: "Hi [Name], this is [Your Name] with [Agency]. We focus exclusively on placing skilled trades and operations talent in manufacturing facilities in [Region]. Quick question — when you\'re short-staffed on the floor or need a Maintenance Tech or Quality Inspector quickly, who do you typically call?"',
            "",
            '[Listen and respond to their answer]',
            "",
            'YOU: "That makes sense. The challenge we hear most often in manufacturing is finding people who actually show up and know the equipment. We pre-screen for attendance history and do skills verification before anyone steps foot on a client\'s floor. Would it be worth 15 minutes to show you how our pre-screening works?"',
        ]),
        ("COLD CALL — HEALTHCARE INDUSTRY SCRIPT", [
            'YOU: "Hi [Name], this is [Your Name] with [Agency]. We place clinical and administrative healthcare talent — RNs, Medical Assistants, Billers, Coders — with practices and health systems in [Region]. I\'m calling because we\'ve had great success helping practices reduce overtime costs by keeping qualified per-diem staff on call. Is that something that comes up for your team?"',
        ]),
        ("COLD CALL — FINANCE/ACCOUNTING INDUSTRY SCRIPT", [
            'YOU: "Hi [Name], this is [Your Name] with [Agency]. We specialize in placing accounting and finance professionals — Staff Accountants, Controllers, CFOs — on both temp and permanent basis. We\'re especially strong during month-end crunch and year-end audits when teams need reinforcement. Does that type of situation come up for you?"',
        ]),
        ("COLD CALL — TECHNOLOGY INDUSTRY SCRIPT", [
            'YOU: "Hi [Name], this is [Your Name] with [Agency]. We work with tech companies in [Region] placing software engineers, DevOps, data engineers, and product managers. We\'re known for finding engineers who are genuinely passive — not actively job hunting — which means less competition and often better quality. Is that something you\'d want to explore?"',
        ]),
        ("OBJECTION HANDLING", [
            "OBJECTION: 'We use preferred vendor agreements / we have a PSL.'",
            "RESPONSE: 'Totally understand — most of our best clients said the same thing before we worked together. We don\'t ask to replace anyone. We ask for one search to prove our value. If we perform, we earn a spot. If we don\'t, you\'ve lost nothing. Would that be fair?'",
            "",
            "OBJECTION: 'We do our own recruiting in-house.'",
            "RESPONSE: 'That\'s actually our favorite situation — internal teams are great, but when a search goes long, or the position is confidential, or the candidate pool is tight, having us as backup means you never go without. When was the last time a search took longer than you wanted?'",
            "",
            "OBJECTION: 'We\'re not hiring right now.'",
            "RESPONSE: 'Perfect timing then — the best time to build a relationship is before you have an urgent need. Most companies that call us on Monday need someone by Wednesday. Can we get on a 15-minute call so when that happens, you know exactly who to call?'",
            "",
            "OBJECTION: 'Your fees are too high.'",
            "RESPONSE: 'I hear that. Our fee is [X]% — but consider this: a bad hire costs 2-3x the annual salary in lost productivity, retraining, and morale. Our guarantee period and pre-screening process means you only pay when we deliver the right person. Can I show you how that math works?'",
        ]),
        ("LINKEDIN OUTREACH SCRIPTS", [
            "CONNECTION REQUEST NOTE (LinkedIn limit: 300 chars):",
            "'Hi [Name] — I work exclusively with [Industry] companies in [Region] on [role type] hiring. Would love to connect — even if the timing isn\'t right now, it\'s great to know each other.'",
            "",
            "FOLLOW-UP MESSAGE AFTER CONNECTION (Day 3):",
            "'Thanks for connecting, [Name]. No pitch here — I just wanted to share that we recently placed a [Role] at a similar [Industry] company in [X days]. If you ever need a reliable recruiting partner, I\'d love to be on your shortlist. Happy to share more details if helpful.'",
            "",
            "LINKEDIN INMAIL — DIRECT APPROACH:",
            "'Hi [Name], I noticed your team has been growing in [area]. We help [Industry] companies in [Region] find [role type] talent faster and with a 90-day guarantee. Would it make sense to have a quick conversation? I have availability [Day] or [Day] — whatever works for you.'",
        ]),
        ("EMAIL PROSPECTING SEQUENCE OVERVIEW", [
            "See Business_Development_Email_Sequences.docx for the full 5-email sequence.",
            "Rule of thumb: Follow up 5-7 times before removing a prospect from your active list.",
            "Space touches: Day 1, Day 3, Day 7, Day 14, Day 21.",
            "Always provide value in each touch — tip, stat, case study, or insight.",
        ]),
    ])

doc("01_BUSINESS_DEVELOPMENT/Business_Development_Email_Sequences.docx",
    "BUSINESS DEVELOPMENT EMAIL SEQUENCES",
    "5-Email Nurture Sequence for New Client Prospects",
    [
        ("HOW TO USE THIS SEQUENCE", [
            "This 5-email sequence is designed to convert cold prospects into discovery call bookings over 21 days. Use it for prospects who have not yet responded to your cold calls.",
            "Personalize the [brackets] for each prospect. Send from your business email. Subject lines are tested for open rates above 35%.",
        ]),
        ("EMAIL 1 — DAY 1: INTRODUCTION", [
            "SUBJECT: Quick question about your [role] hiring",
            "",
            "Hi [First Name],",
            "",
            "My name is [Your Name], and I run [Agency Name] — we're a boutique staffing firm that specializes in [niche] placements for [Industry] companies in [Region].",
            "",
            "I'll be direct: I'm not trying to flood your inbox. I'm reaching out because we recently helped [similar company type] cut their time-to-fill for [role type] from 47 days to 18 days — and I think we could do the same for your team.",
            "",
            "Would you be open to a 15-minute call this week or next to see if we'd be a fit?",
            "",
            "If the timing isn't right, no worries at all — I just wanted to make sure you knew we existed before you had an urgent need.",
            "",
            "Best,",
            "[Your Name]",
            "[Agency Name] | [Phone] | [Email]",
        ]),
        ("EMAIL 2 — DAY 3: VALUE ADD", [
            "SUBJECT: Something useful for [Company Name]'s hiring",
            "",
            "Hi [First Name],",
            "",
            "Following up on my note from [Day]. No response needed if the timing isn't right.",
            "",
            "I wanted to share something useful: the #1 thing [Industry] hiring managers tell us slows down their recruiting is the resume screening bottleneck. By the time a job is posted, screened, and scheduled for interviews, top candidates are already gone.",
            "",
            "We solve this by pre-building a bench of pre-screened [role type] candidates so that when you have an opening, we can deliver qualified names within 48-72 hours — not 3-4 weeks.",
            "",
            "Is that a pain point for your team? Happy to share how it works in 15 minutes.",
            "",
            "[Your Name]",
        ]),
        ("EMAIL 3 — DAY 7: CASE STUDY", [
            "SUBJECT: How [Company Type] hired a [Role] in 12 days",
            "",
            "Hi [First Name],",
            "",
            "I'll keep this short. Here's a quick story:",
            "",
            "A [Industry] client of ours needed a [Role] fast. Their internal team had been searching for 6 weeks with no success. They called us on a Tuesday. We submitted 3 candidates by Thursday. They hired one the following Monday.",
            "",
            "Total time from first call to offer accepted: 12 business days.",
            "",
            "I share this not to brag, but because that's a repeatable result for us in [Industry]. We have the candidate pipeline and the process to move fast when you need it.",
            "",
            "If you ever find yourself in that situation, I want to be the first call you make. Would a quick intro call make sense?",
            "",
            "[Your Name]",
        ]),
        ("EMAIL 4 — DAY 14: FOLLOW-UP", [
            "SUBJECT: Still worth a conversation, [First Name]?",
            "",
            "Hi [First Name],",
            "",
            "I've reached out a couple of times — I want to be respectful of your inbox, so this will be one of my last notes for a while.",
            "",
            "I work with about [X] companies in [Region]'s [Industry] space. Most of them tell me they wish they'd called sooner — either because they had an urgent need they could have planned for, or because they were using a generalist recruiter who didn't really know the [role] market.",
            "",
            "We're a specialist. We know the talent pool, we know the salary ranges, and we know how to find candidates who aren't on job boards.",
            "",
            "If any of that resonates, I'd love 15 minutes. If not, no hard feelings — I'll check back in a few months.",
            "",
            "[Your Name]",
        ]),
        ("EMAIL 5 — DAY 21: BREAKUP EMAIL", [
            "SUBJECT: Closing the loop, [First Name]",
            "",
            "Hi [First Name],",
            "",
            "I've reached out a few times and haven't heard back — which usually means one of three things:",
            "",
            "1. You're slammed and this hasn't been a priority (totally fair)",
            "2. You have a great recruiting process and don't need us (also fair)",
            "3. My emails have been landing in spam (less fair, but happens!)",
            "",
            "I'm going to close the loop on my end. If you ever have a critical [role type] need and want a specialist who can move fast, I hope you'll reach out.",
            "",
            "I'll make it easy: [Calendar link] — grab a 15-minute slot any time.",
            "",
            "Wishing [Company Name] continued success.",
            "",
            "[Your Name]",
            "",
            "P.S. If there's a better contact at [Company] for staffing conversations, I'd appreciate a quick note — I'll reach out to them instead.",
        ]),
    ])

doc("01_BUSINESS_DEVELOPMENT/Client_Pitch_Deck_Framework.docx",
    "CLIENT PITCH DECK FRAMEWORK",
    "How to Win Client Meetings and Close Search Agreements",
    [
        ("THE 10-STEP WINNING PITCH FLOW", [
            "1. OPEN WITH THEIR PROBLEM (2 min): Don't talk about yourself first. Ask: 'Before I share about us, can you tell me about your most recent hiring challenge? What made it difficult?'",
            "2. REFLECT AND VALIDATE (1 min): Repeat their problem back to them. 'So what I'm hearing is...' This builds trust and shows you listened.",
            "3. QUANTIFY THE COST (2 min): 'Do you know what it costs to have that [role] unfilled for 60 days? Between lost productivity and overtime, most companies we work with estimate [X]...'",
            "4. INTRODUCE YOUR SOLUTION (3 min): Now introduce your agency — but frame it as the solution to THEIR problem, not a general introduction.",
            "5. PROVE IT WITH DATA (3 min): Share 2-3 specific results: 'We filled a Controller role at a [similar company] in 19 days. Our average time-to-fill for [role] is [X] days versus the industry average of [Y].'",
            "6. EXPLAIN YOUR PROCESS (5 min): Walk through your sourcing, screening, and submittal process. Show how you're different from job board posting.",
            "7. ADDRESS YOUR GUARANTEE (2 min): Proactively bring up your guarantee. 'If the candidate leaves within 90 days for any reason, we redo the search at no charge.' This removes the risk objection.",
            "8. DISCUSS FEE STRUCTURE (3 min): Present fee with confidence. 'Our fee is [X]% of first-year base salary, invoiced upon start date.' Don't apologize for your fee.",
            "9. HANDLE OBJECTIONS (varies): Use the objection scripts from Client_Prospecting_Scripts.docx",
            "10. CLOSE FOR THE AGREEMENT (2 min): 'Based on what we've discussed, does it make sense to move forward with an agreement? I can have the paperwork to you by tomorrow.'",
        ]),
        ("VALUE PROPOSITIONS BY INDUSTRY", [
            "MANUFACTURING: Speed + compliance. 'We verify OSHA training, equipment certifications, and drug test before submittal. Your floor supervisor isn't wasting time interviewing unqualified candidates.'",
            "HEALTHCARE: Credential verification + per-diem bench. 'We maintain licensure verification on every candidate. We can also build you a per-diem bench so you never pay agency overtime.'",
            "FINANCE/ACCOUNTING: Niche depth + confidentiality. 'We recruit passively — most of our candidates aren't on job boards. We also understand the confidentiality requirements of financial roles.'",
            "TECHNOLOGY: Passive talent + culture fit. 'We source engineers who are employed and performing — not the ones refreshing job boards. We also assess for cultural fit before any submittal.'",
            "GENERAL: Three core value props that work universally:",
            ("•","SPEED: 'We can typically deliver 3 qualified candidates within 5-7 business days.'"),
            ("•","QUALITY: 'We submit no more than 3-5 candidates per search — only the best fits.'"),
            ("•","GUARANTEE: '90-day replacement guarantee means zero risk to your company.'"),
        ]),
        ("COMPETITIVE DIFFERENTIATION", [
            "vs. LARGE NATIONAL STAFFING FIRMS:",
            ("•","'We're specialists, not generalists. A large firm will send your search to a junior recruiter. You'll work directly with me.'"),
            ("•","'We know every candidate personally. No database dumps — curated shortlists only.'"),
            "",
            "vs. IN-HOUSE RECRUITING:",
            ("•","'We complement your internal team. We take on the searches where time pressure or confidentiality is highest.'"),
            ("•","'We have passive candidates they can't reach — people who aren't looking but would move for the right role.'"),
            "",
            "vs. DOING NOTHING:",
            ("•","'Every day the role is open costs approximately [X] in lost productivity. Our fee pays for itself in reduced vacancy time alone.'"),
        ]),
        ("CLOSING LANGUAGE", [
            "'What would need to be true for you to move forward today?'",
            "'Is there anyone else who would need to be involved in this decision?'",
            "'If I can get the agreement to you by end of day, can we kick off the search this week?'",
            "'I'd rather start and prove our value than spend another meeting convincing you — what do you say?'",
        ]),
    ])

doc("01_BUSINESS_DEVELOPMENT/Cold_Outreach_Templates.docx",
    "COLD OUTREACH TEMPLATES",
    "10 Email Templates + 5 LinkedIn Templates for New Business",
    [
        ("EMAIL TEMPLATE 1 — GENERAL INTRODUCTION", [
            "SUBJECT: [Agency Name] — Staffing specialists in [Industry/Region]",
            "Hi [Name], I'm [Your Name] with [Agency]. We specialize in [niche] placements and have placed [X] professionals with [Industry] companies in [Region] this year. I'd love 15 minutes to introduce ourselves before you have an urgent need. Any time this week work?",
        ]),
        ("EMAIL TEMPLATE 2 — PAIN POINT OPENER", [
            "SUBJECT: The #1 hiring challenge for [Industry] companies right now",
            "Hi [Name], We talk to [Industry] hiring managers daily. The #1 challenge we hear: qualified candidates are off the market within 10 days of starting a search. We solve this with a pre-built bench of screened candidates for high-demand roles. Worth a 15-minute conversation?",
        ]),
        ("EMAIL TEMPLATE 3 — REFERRAL MENTION", [
            "SUBJECT: [Mutual Contact] suggested I reach out",
            "Hi [Name], [Mutual Contact] at [Company] mentioned you might be dealing with some hiring challenges for [role type]. We helped their team fill a [role] recently and they thought we might be able to do the same for you. Would a quick call make sense?",
        ]),
        ("EMAIL TEMPLATE 4 — TRIGGER EVENT (COMPANY GROWTH)", [
            "SUBJECT: Congrats on the [funding/expansion/news] — quick question",
            "Hi [Name], Saw the news about [Company]'s [event] — congrats! Growth like that usually means hiring pressure. We specialize in helping [Industry] companies scale their teams quickly without sacrificing quality. Happy to share how we work if useful.",
        ]),
        ("EMAIL TEMPLATE 5 — JOB POSTING RESPONSE", [
            "SUBJECT: Re: Your open [Role] position",
            "Hi [Name], I noticed you're hiring a [Role]. We work with [Industry] companies specifically on this type of search and have candidates currently in our pipeline for this exact role. I won't send a resume without talking first — but I'd love 15 minutes to see if our candidates might be a fit.",
        ]),
        ("EMAIL TEMPLATE 6 — DIRECT VALUE OFFER", [
            "SUBJECT: Free [Industry] salary guide for [Region]",
            "Hi [Name], We recently compiled salary benchmarks for [Role] positions in [Region] based on our recent placement activity. I'd be happy to share it with you — no strings attached. If it's useful, maybe we can grab a quick call to discuss the market. Interested?",
        ]),
        ("EMAIL TEMPLATE 7 — SHORT AND DIRECT", [
            "SUBJECT: [Role] candidates — 48-hour delivery",
            "Hi [Name], Quick question: if I could deliver 3 pre-screened [Role] candidates to you within 48 hours of a kick-off call, would that be worth a 15-minute conversation? That's our standard for [Industry] clients in [Region]. Available [Day] or [Day]?",
        ]),
        ("EMAIL TEMPLATE 8 — END OF QUARTER", [
            "SUBJECT: Q[X] hiring — are you on track?",
            "Hi [Name], Q[X] end is [X weeks] away. Are you on track with your hiring plan? We work with [Industry] companies to fill critical roles before quarter-end so teams hit their goals. If you have any open roles, I'd love to help. Quick call this week?",
        ]),
        ("EMAIL TEMPLATE 9 — COMPETITOR PLACEMENT MENTION", [
            "SUBJECT: We just placed a [Role] at [Competitor/Similar Company]",
            "Hi [Name], We just completed a [Role] search for a [similar company type] in [Region] — hired in [X days], candidate is performing excellently. I wanted to reach out in case you have similar needs. Happy to share details on the process if interested.",
        ]),
        ("EMAIL TEMPLATE 10 — LONG-TERM RELATIONSHIP BUILD", [
            "SUBJECT: Not pitching — just connecting",
            "Hi [Name], I'm not reaching out about a specific need right now. I just make it a point to connect with [Industry] hiring leaders in [Region] so when the time comes, we already know each other. I'd love to grab a virtual coffee sometime — no agenda, just a conversation. Interested?",
        ]),
        ("LINKEDIN TEMPLATE 1 — CONNECTION REQUEST", [
            "(300 characters max)",
            "Hi [Name] — I place [role type] talent with [Industry] companies in [Region]. I'd love to connect — no pitch, just building a network of great people in the space.",
        ]),
        ("LINKEDIN TEMPLATE 2 — POST-CONNECTION MESSAGE", [
            "Thanks for connecting, [Name]! I noticed [Company] has been growing — congrats. We specialize in [niche] staffing if you ever need a recruiting partner. Happy to share more about what we do if the timing's ever right.",
        ]),
        ("LINKEDIN TEMPLATE 3 — INMAIL TO COLD PROSPECT", [
            "Hi [Name], I lead [Agency] — we focus exclusively on [Industry] staffing in [Region]. I won't pitch you unless there's a fit. Quick question: what's your biggest recruiting pain point right now? I'd genuinely like to know, even if we can't help.",
        ]),
        ("LINKEDIN TEMPLATE 4 — AFTER THEY LIKE A POST", [
            "Hi [Name], noticed you engaged with my post about [topic] — glad it resonated. We work on exactly that with [Industry] companies in [Region]. Would you be open to a quick chat about your hiring situation?",
        ]),
        ("LINKEDIN TEMPLATE 5 — JOB POSTING SPOTTED", [
            "Hi [Name], I saw [Company] is looking for a [Role]. We have that profile in our current pipeline. I won't send anyone unsolicited — but if you'd like to hear about our process, I'm happy to spend 15 minutes walking you through it.",
        ]),
    ])

# Business Development CRM
print("  Building Business_Development_CRM.xlsx...")
wb = Workbook()

ws1 = wb.active; ws1.title = "Client Prospects"
hrow(ws1,1,range(1,11),["Company","Contact Name","Title","Industry","Phone","Email","Status","Last Contact","Next Step","Notes"])
prospects = [
    ["Meridian Manufacturing Co.","Sarah Chen","VP Operations","Manufacturing","312-555-0192","s.chen@meridianmfg.com","Warm Lead","2026-06-15","Send proposal","Expressed interest in temp workers"],
    ["BlueCrest Financial Group","James Harmon","CFO","Finance","617-555-0341","j.harmon@bluecrest.com","Cold","2026-06-10","Follow-up call","Saw our LinkedIn ad"],
    ["Summit Health Systems","Dr. Maria Lopez","Dir. HR","Healthcare","404-555-0287","m.lopez@summithlth.com","Contacted","2026-06-18","Schedule discovery","Needs RN and MA placements"],
    ["Vertex Technologies","Nathan Park","CTO","Technology","408-555-0156","n.park@vertextech.com","Proposal Sent","2026-06-12","Awaiting decision","Engineering team expansion"],
    ["Great Lakes Logistics","Diana Foster","COO","Logistics","312-555-0449","d.foster@gllogs.com","Active Client","2026-06-20","Monthly check-in","2nd year partnership"],
    ["Pinnacle Accounting","Robert Vasquez","Managing Partner","Accounting","713-555-0273","r.vasquez@pinnacleacct.com","Warm Lead","2026-06-17","Send case study","Looking for seasonal help"],
    ["NorthStar Retail Group","Amanda Kim","HR Manager","Retail","214-555-0388","a.kim@northstarretail.com","Cold","2026-06-08","Initial outreach","High volume hiring"],
    ["Coastal Engineering LLC","Marcus Webb","President","Engineering","503-555-0211","m.webb@coastaleng.com","Contacted","2026-06-19","Discovery call booked","Civil engineers needed"],
    ["Heritage Foods Inc.","Patricia Monroe","Dir. Talent","Food & Bev","612-555-0365","p.monroe@heritagefoods.com","Proposal Sent","2026-06-14","Decision pending","5 production roles open"],
    ["Cascade Software","Elena Russo","VP HR","Software","425-555-0199","e.russo@cascadesw.com","Warm Lead","2026-06-16","Demo scheduled","DevOps and backend roles"],
]
for i,row in enumerate(prospects,2): drow(ws1,i,range(1,11),row, WHT if i%2==0 else LGR)
for col,w in zip("ABCDEFGHIJ",[25,20,20,18,16,28,15,14,22,30]): ws1.column_dimensions[col].width=w

ws2 = wb.create_sheet("BD Activity Log")
hrow(ws2,1,range(1,9),["Date","Recruiter","Calls Made","Emails Sent","LinkedIn Msgs","Meetings Held","Proposals Sent","Notes"])
activity = [
    ["2026-06-14","Alex Rivera",22,15,8,2,1,"Booked 2 discovery calls"],
    ["2026-06-15","Alex Rivera",18,20,10,1,0,"Followed up on Vertex proposal"],
    ["2026-06-16","Jordan Smith",25,12,6,3,2,"Strong day — 3 meetings"],
    ["2026-06-17","Alex Rivera",20,18,9,2,1,"Heritage Foods proposal sent"],
    ["2026-06-18","Jordan Smith",15,22,11,1,0,"Focus on email campaign"],
    ["2026-06-19","Alex Rivera",28,10,7,4,2,"Best day this week — 4 meetings"],
    ["2026-06-20","Jordan Smith",19,16,8,2,1,"Cascade demo scheduled"],
    ["2026-06-21","Alex Rivera",12,14,5,1,0,"Monday morning start"],
    ["2026-06-14","Jordan Smith",21,13,7,2,1,"Solid prospecting day"],
    ["2026-06-15","Jordan Smith",17,19,9,0,1,"Email heavy day"],
]
for i,row in enumerate(activity,2): drow(ws2,i,range(1,9),row, WHT if i%2==0 else LGR)
for col,w in zip("ABCDEFGH",[14,16,14,14,16,16,16,30]): ws2.column_dimensions[col].width=w

ws3 = wb.create_sheet("Revenue Pipeline")
hrow(ws3,1,range(1,9),["Company","Role","Type","Est. Fee ($)","Probability %","Weighted Value ($)","Expected Close","Status"])
pipeline = [
    ["Vertex Technologies","Senior DevOps Engineer","Direct",24000,75,18000,"2026-07-10","Finalist round"],
    ["Summit Health Systems","Registered Nurse (x3)","Temp",18000,60,10800,"2026-07-01","Candidates submitted"],
    ["Heritage Foods Inc.","Production Supervisor","Direct",16500,80,13200,"2026-06-30","Offer stage"],
    ["Meridian Manufacturing","Maintenance Technician","Temp",9600,90,8640,"2026-06-28","Starting Monday"],
    ["BlueCrest Financial","Senior Accountant","Direct",19500,40,7800,"2026-07-25","Proposal pending"],
    ["Cascade Software","Backend Engineer","Direct",22000,65,14300,"2026-07-15","Phone screens scheduled"],
    ["Coastal Engineering","Project Manager","Direct",21000,50,10500,"2026-08-01","Early stages"],
    ["Pinnacle Accounting","Staff Accountant (seasonal)","Temp",7200,85,6120,"2026-06-27","Contract being reviewed"],
]
for i,row in enumerate(pipeline,2): drow(ws3,i,range(1,9),row, WHT if i%2==0 else LGR)
for col,w in zip("ABCDEFGH",[25,28,10,14,14,16,16,20]): ws3.column_dimensions[col].width=w
wb.save(BASE+"01_BUSINESS_DEVELOPMENT/Business_Development_CRM.xlsx")
print("  ✓ 01_BUSINESS_DEVELOPMENT/Business_Development_CRM.xlsx")

# ── 02_CLIENT_MANAGEMENT ───────────────────────────────────────────────────────
print("\n02_CLIENT_MANAGEMENT...")

doc("02_CLIENT_MANAGEMENT/Client_Intake_And_Discovery_Form.docx",
    "CLIENT INTAKE & DISCOVERY FORM",
    "Complete this form during or immediately after every new client discovery call",
    [
        ("SECTION 1: COMPANY INFORMATION", [
            "Company Name: _______________________________________________",
            "Industry: ___________________________________________________",
            "Company Size (# employees): __________________________________",
            "Annual Revenue (approx): _____________________________________",
            "Primary Office Location: _____________________________________",
            "Website: ____________________________________________________",
            "Hiring Manager Name: ________________________________________",
            "Hiring Manager Title: ________________________________________",
            "Hiring Manager Email: ________________________________________",
            "Hiring Manager Phone: _______________________________________",
            "HR Contact (if different): ____________________________________",
            "Who else is involved in the hiring decision? ___________________",
        ]),
        ("SECTION 2: THE ROLE", [
            "Job Title: __________________________________________________",
            "Department: _________________________________________________",
            "Type: [ ] Temp/Contract  [ ] Temp-to-Perm  [ ] Direct Hire",
            "How many openings? __________________________________________",
            "Reporting to (Title): _________________________________________",
            "Work location: [ ] On-site  [ ] Remote  [ ] Hybrid (___days/wk)",
            "Start date needed: __________________________________________",
            "Is this a backfill or new position? ___________________________",
            "If backfill — why did the previous person leave? _______________",
            "How long has this role been open? ____________________________",
            "What have you tried so far to fill it? _________________________",
            "What happened with previous candidates or hires? ______________",
        ]),
        ("SECTION 3: REQUIREMENTS & IDEAL PROFILE", [
            "MUST-HAVE qualifications (non-negotiable):",
            "1. _________________________________________________________",
            "2. _________________________________________________________",
            "3. _________________________________________________________",
            "NICE-TO-HAVE qualifications:",
            "1. _________________________________________________________",
            "2. _________________________________________________________",
            "Education requirements: ______________________________________",
            "Years of experience required: _________________________________",
            "Specific software/systems/tools required: _____________________",
            "Certifications or licenses required: ___________________________",
            "Industry background preferred: ________________________________",
            "Describe your IDEAL candidate in 3 words: ____________________",
            "Who is the best person you've ever hired for a similar role and what made them great? ____________________",
        ]),
        ("SECTION 4: COMPENSATION & BENEFITS", [
            "Salary range (base): $_______________ to $_________________",
            "Is this range firm or flexible? _______________________________",
            "Bonus/commission structure: __________________________________",
            "Benefits (check all that apply):",
            "  [ ] Medical  [ ] Dental  [ ] Vision  [ ] 401k  [ ] PTO",
            "  [ ] Equity/Stock  [ ] Tuition  [ ] Remote Stipend  [ ] Other: ____",
            "For temp roles — Bill rate: $________/hr  Pay rate budget: $________/hr",
            "Overtime expectations: _______________________________________",
            "Relocation assistance available? [ ] Yes  [ ] No",
            "Visa sponsorship available? [ ] Yes  [ ] No",
        ]),
        ("SECTION 5: COMPANY CULTURE & ENVIRONMENT", [
            "How would you describe your company culture in 3 words? ________",
            "Work pace: [ ] Fast-paced  [ ] Steady  [ ] Varies by season",
            "Team size of this department: ________________________________",
            "Management style of the hiring manager: ______________________",
            "What does a typical day look like for someone in this role? _____",
            "What are the biggest challenges someone in this role will face? _",
            "Why do people love working at your company? __________________",
            "Why do people leave your company? ___________________________",
            "How does this team like to communicate? (Slack, email, meetings) _",
        ]),
        ("SECTION 6: PROCESS & NEXT STEPS", [
            "Interview process (number of rounds): ________________________",
            "Interview format: [ ] Phone  [ ] Video  [ ] In-person  [ ] All",
            "Who will interview the candidate? ____________________________",
            "Decision timeline: ___________________________________________",
            "What would cause you to move fast on a candidate? ____________",
            "What would be an automatic disqualifier? ______________________",
            "How quickly can you make an offer once you find the right person? _",
            "Have you worked with staffing agencies before? [ ] Yes  [ ] No",
            "If yes — what did you like/dislike about the experience? ________",
            "RECRUITER NOTES: ___________________________________________",
            "Fee agreed: _______% of first-year base. Guarantee: _____ days.",
            "Agreement sent: [ ] Yes — Date: ________  [ ] Pending",
        ]),
    ])

doc("02_CLIENT_MANAGEMENT/Job_Order_Template.docx",
    "JOB ORDER TEMPLATE",
    "Complete one of these for every active search — your search roadmap",
    [
        ("JOB ORDER DETAILS", [
            "Job Order #: _____________  Date Opened: ___________________",
            "Client Company: ____________________________________________",
            "Client Contact: _____________________________________________",
            "Recruiter Assigned: _________________________________________",
            "Job Title: __________________________________________________",
            "Location: __________________________________________________",
            "Search Type: [ ] Contingency  [ ] Retained  [ ] Temp  [ ] T-T-P",
            "Fee/Rate: ___________________________________________________",
            "Priority Level: [ ] URGENT  [ ] HIGH  [ ] STANDARD",
        ]),
        ("ROLE SUMMARY", [
            "Write a 3-5 sentence summary of the role as you would describe it to a candidate:",
            "",
            "_______________________________________________________________",
            "_______________________________________________________________",
            "_______________________________________________________________",
        ]),
        ("REQUIREMENTS", [
            "Education: _________________________________________________",
            "Years of Experience: ________________________________________",
            "Technical Skills (required): __________________________________",
            "Technical Skills (preferred): _________________________________",
            "Soft Skills (critical): _______________________________________",
            "Industry Background: ________________________________________",
            "Certifications/Licenses: _____________________________________",
            "Work Authorization: [ ] US Citizen  [ ] GC  [ ] Any Auth  [ ] Must have visa",
        ]),
        ("COMPENSATION", [
            "Salary Range: $____________ to $____________",
            "Bonus: _____________________________________________________",
            "Total Comp: ________________________________________________",
            "Benefits Highlights: ________________________________________",
            "Equity: ____________________________________________________",
        ]),
        ("INTERVIEW PROCESS", [
            "Round 1: ___________________________________________________",
            "Round 2: ___________________________________________________",
            "Round 3 (if applicable): ____________________________________",
            "Final Step: ________________________________________________",
            "Decision Maker: ____________________________________________",
            "Typical Timeline from Interview to Offer: ____________________",
        ]),
        ("SOURCING STRATEGY", [
            "Target companies to source from: ____________________________",
            "Job titles to search: ________________________________________",
            "LinkedIn boolean string to use: _______________________________",
            "Job boards to post on: _______________________________________",
            "Referral sources to contact: __________________________________",
        ]),
        ("CANDIDATE SUBMITTAL LOG", [
            "Candidate 1: ________________  Date Submitted: _____  Status: ______",
            "Candidate 2: ________________  Date Submitted: _____  Status: ______",
            "Candidate 3: ________________  Date Submitted: _____  Status: ______",
            "Candidate 4: ________________  Date Submitted: _____  Status: ______",
            "Candidate 5: ________________  Date Submitted: _____  Status: ______",
        ]),
        ("OUTCOME", [
            "Placement: [ ] Yes  [ ] No  [ ] In Progress",
            "Placed Candidate: __________________________________________",
            "Start Date: ________________________________________________",
            "Fee Invoiced: $____________  Invoice #: ____________",
            "Guarantee End Date: _______________________________________",
            "Days Open: _________________  Total Submittals: ______________",
        ]),
    ])

doc("02_CLIENT_MANAGEMENT/Search_Assignment_Agreement.docx",
    "SEARCH ASSIGNMENT AGREEMENT",
    "Professional Service Agreement — Review with your attorney before use",
    [
        ("PARTIES", [
            "This Search Assignment Agreement ('Agreement') is entered into between:",
            "",
            "[AGENCY NAME] ('Agency'), a [State] [entity type] located at [Address]",
            "",
            "AND",
            "",
            "[CLIENT COMPANY NAME] ('Client'), a [entity type] located at [Address]",
            "",
            "Effective Date: _______________________________________________",
        ]),
        ("SECTION 1: SCOPE OF SEARCH", [
            "1.1 Agency agrees to conduct a search for qualified candidates for the following position(s):",
            "    Position Title: __________________________________________",
            "    Department: _____________________________________________",
            "    Location: _______________________________________________",
            "    Number of openings: _____________________________________",
            "",
            "1.2 Search Type:",
            "    [ ] CONTINGENCY SEARCH — Fee paid only upon successful placement",
            "    [ ] RETAINED SEARCH — Fee paid in installments regardless of outcome",
            "    [ ] TEMP/CONTRACT PLACEMENT — Hourly markup arrangement",
        ]),
        ("SECTION 2: FEES", [
            "CONTINGENCY ARRANGEMENT:",
            "  Fee: ______% of candidate's first-year annualized base salary",
            "  Payment due: Within 30 days of candidate's start date",
            "  Late payment: 1.5% per month after 30 days",
            "",
            "RETAINED ARRANGEMENT:",
            "  Total fee: ______% of estimated first-year base salary",
            "  Payment Schedule:",
            "    Installment 1 (upon signing): 33.3% = $_____________",
            "    Installment 2 (upon first submittal): 33.3% = $_____________",
            "    Installment 3 (upon placement): 33.3% = $_____________",
            "  Retainer payments are non-refundable.",
            "",
            "TEMP/CONTRACT ARRANGEMENT:",
            "  Bill Rate: $______/hour  (includes agency markup of ______%)",
            "  Overtime: 1.5x bill rate for hours over 40/week",
            "  Payment: Net 30 from invoice date",
        ]),
        ("SECTION 3: GUARANTEE PERIOD", [
            "3.1 If a placed candidate voluntarily resigns or is terminated for cause within ______ (90) calendar days of their start date, Agency will conduct one (1) replacement search at no additional fee.",
            "",
            "3.2 The guarantee is void if:",
            ("•","Client makes material changes to the role, compensation, or responsibilities"),
            ("•","Client fails to pay Agency's invoice within agreed terms"),
            ("•","Candidate is laid off due to Client restructuring or elimination of the role"),
            ("•","Client hires the candidate on a temp basis and converts to a different role"),
        ]),
        ("SECTION 4: EXCLUSIVITY", [
            "[ ] EXCLUSIVE SEARCH: Client agrees not to engage other staffing agencies or conduct internal recruiting for this position during the search period.",
            "",
            "[ ] NON-EXCLUSIVE SEARCH: Client may engage multiple sources. Agency will proceed on a contingency basis.",
            "",
            "Exclusivity Period (if applicable): ______ days from signing",
        ]),
        ("SECTION 5: CONFIDENTIALITY", [
            "5.1 Both parties agree to maintain strict confidentiality regarding candidate identities, client business information, compensation details, and search parameters.",
            "5.2 Client agrees not to contact Agency's candidates directly without Agency's written consent during and for 12 months following the search.",
            "5.3 If Client hires an Agency-introduced candidate outside of this Agreement, the full fee will be owed.",
        ]),
        ("SECTION 6: GOVERNING LAW & SIGNATURES", [
            "This Agreement shall be governed by the laws of the State of [State].",
            "",
            "FOR CLIENT:",
            "Signature: _______________________________  Date: ___________",
            "Print Name: ______________________________",
            "Title: ___________________________________",
            "",
            "FOR AGENCY:",
            "Signature: _______________________________  Date: ___________",
            "Print Name: ______________________________",
            "Title: ___________________________________",
        ]),
    ])

doc("02_CLIENT_MANAGEMENT/Client_Communication_SOP.docx",
    "CLIENT COMMUNICATION SOP",
    "How to communicate with clients throughout the search — cadence, scripts, escalation",
    [
        ("WEEKLY UPDATE CADENCE", [
            "Every active search requires a weekly update to the client — even if you have nothing new to report. Silence kills client relationships.",
            "",
            "MONDAY: Review all active searches and plan the week's outreach strategy",
            "WEDNESDAY: Send mid-week status update email to all active clients",
            "FRIDAY: Send end-of-week summary with next steps",
        ]),
        ("WEEKLY UPDATE EMAIL TEMPLATE", [
            "SUBJECT: [Role Title] Search Update — Week of [Date]",
            "",
            "Hi [Name],",
            "",
            "Quick update on your [Role Title] search:",
            "",
            "THIS WEEK:",
            "• Sourced [X] candidates from LinkedIn and referrals",
            "• Phone screened [X] candidates",
            "• [X] candidates meet your criteria and are being prepared for submittal",
            "",
            "SUBMITTALS (if any):",
            "• [Candidate Name] — [Brief description, e.g., '7 years in role, currently at XYZ Corp']",
            "",
            "NEXT WEEK:",
            "• Planning to submit [X] additional candidates",
            "• Following up on interview feedback from [Candidate Name]",
            "",
            "QUESTION FOR YOU:",
            "After reviewing the profiles, is there anything you'd like us to adjust in our candidate criteria?",
            "",
            "Best,",
            "[Your Name]",
        ]),
        ("HOW TO DELIVER BAD NEWS", [
            "Scenario 1: The search is taking longer than expected",
            "SCRIPT: 'I want to be transparent with you — this search is more competitive than we initially anticipated. Here's what we're seeing in the market... Here's what I'm doing to adjust our strategy... I want to reset expectations: I believe we'll have strong candidates to you by [new date].'",
            "",
            "Scenario 2: A finalist candidate declined",
            "SCRIPT: 'I have some disappointing news — [Candidate] has decided not to move forward. Here's what they told me... [honest reason]. I'm already working on our next round. I think we're very close to finding the right person. I'll have more to share by [date].'",
            "",
            "Scenario 3: A placed candidate resigned during guarantee",
            "SCRIPT: 'I want to call you personally about this — [Candidate] came to me this morning and gave notice. I'm deeply sorry this happened. We have a 90-day guarantee and I'm going to honor it fully. I'd like to get on a call today to debrief on what happened and kick off the replacement search immediately.'",
        ]),
        ("CLIENT ESCALATION PROCESS", [
            "Level 1 — Unhappy with candidates: 'Thank you for the feedback. Can we do a quick call to realign on what you're looking for? I want to make sure I'm presenting only what matches your vision.'",
            "",
            "Level 2 — Threatening to use another agency: 'I understand your frustration. Before you make that decision, I want to share what I'm working on right now and give you a clear timeline. Can we get on a call in the next hour?'",
            "",
            "Level 3 — Disputing the fee: Involve a senior person immediately. Never negotiate fee via email. Always call.",
        ]),
        ("COMMUNICATION LOG FORMAT", [
            "Keep a running log for every client:",
            "[DATE] [TYPE: Call/Email/Meeting] [WHO YOU SPOKE TO] [KEY POINTS] [ACTION ITEMS] [FOLLOW-UP DATE]",
            "",
            "Example:",
            "2026-06-21 | Phone Call | Sarah Chen, VP Ops | Reviewed 2 candidates, likes Profile A, wants to see someone with more ISO experience | Send 2 more by Wed | 2026-06-23",
        ]),
    ])

# ── 03_CANDIDATE_SOURCING ──────────────────────────────────────────────────────
print("\n03_CANDIDATE_SOURCING...")

doc("03_CANDIDATE_SOURCING/LinkedIn_Sourcing_Playbook.docx",
    "LINKEDIN SOURCING PLAYBOOK",
    "Find and engage the best passive candidates on LinkedIn",
    [
        ("THE PASSIVE CANDIDATE MINDSET", [
            "The best candidates are NOT looking for a job. They are employed, performing well, and not browsing job boards. Your job is to find them, engage them professionally, and create enough curiosity that they'll take a 15-minute call.",
            "80% of your placements should come from passive candidates. Active candidates (applying to your postings) are important but compete with everyone else. Passive candidates are yours alone.",
        ]),
        ("LINKEDIN SEARCH STRATEGY", [
            "STEP 1 — DEFINE YOUR SEARCH PARAMETERS:",
            ("•","Job Title (use multiple variations)"),
            ("•","Location (city, state, or 'within X miles')"),
            ("•","Industry filter (narrow your results)"),
            ("•","Company size (match to client's expected background)"),
            ("•","Seniority level (filter out overqualified/underqualified)"),
            "",
            "STEP 2 — RUN YOUR BOOLEAN SEARCH:",
            "Use the search string from Boolean_Search_String_Library.docx for your target role.",
            "",
            "STEP 3 — READ PROFILES STRATEGICALLY:",
            ("•","Look at current role title AND previous title — progression matters"),
            ("•","Check tenure: 2-5 years in current role = prime sourcing target"),
            ("•","Read the About section for communication style and self-awareness"),
            ("•","Look at their activity feed — are they engaging with content? Good sign."),
            ("•","Mutual connections = warm approach opportunity"),
            "",
            "STEP 4 — PRIORITIZE YOUR OUTREACH LIST:",
            "Score each prospect 1-3: 1=Excellent fit, 2=Good fit, 3=Possible fit. Start all outreach with your 1s.",
        ]),
        ("PASSIVE CANDIDATE IDENTIFICATION SIGNALS", [
            "GREEN FLAGS — Signs they may be open to conversations:",
            ("•","Profile updated recently (within 90 days)"),
            ("•","Open to Work badge (even 'Open to Opportunities — Recruiters Only')"),
            ("•","Following your agency or posting about job search tips"),
            ("•","Tenure of 3-5 years — statistically prime for a move"),
            ("•","Company had layoffs, restructuring, or leadership change recently"),
            ("•","Profile says 'former' somewhere in recent history"),
            "",
            "AMBER FLAGS — Proceed carefully:",
            ("•","Just started a new role (less than 6 months) — still reach out for pipeline"),
            ("•","Profile photo is their company headshot — very loyal to employer"),
            ("•","Volunteer board member at their company — invested in culture"),
        ]),
        ("INMAIL TEMPLATE 1 — STANDARD PASSIVE OUTREACH", [
            "SUBJECT: [Role Title] opportunity — your background caught my eye",
            "",
            "Hi [Name],",
            "",
            "I came across your profile while searching for [Role Title] professionals in [City]. Your experience at [Current Company] — particularly [specific detail from profile] — is exactly the profile my client is looking for.",
            "",
            "I represent a [industry type] company in [Region] that's looking to add a [Role Title]. The role offers [brief value prop — e.g., 'leadership over a team of 8 and direct C-suite visibility'].",
            "",
            "I know you may not be actively looking — that's actually why I'm reaching out. Would you be open to a 15-minute conversation to hear more details? No pressure at all if the timing isn't right.",
            "",
            "Best,",
            "[Your Name]",
        ]),
        ("INMAIL TEMPLATE 2 — MUTUAL CONNECTION", [
            "SUBJECT: [Mutual Name] suggested I reach out",
            "",
            "Hi [Name],",
            "",
            "[Mutual Connection] mentioned your name when I described a [Role Title] opportunity I'm working on for a [Industry] company in [Region]. [He/She] spoke highly of your work at [Company].",
            "",
            "I'd love to tell you more about the role — it may or may not be a fit, but it's worth a 15-minute conversation. Are you available [Day] or [Day] for a quick call?",
        ]),
        ("INMAIL TEMPLATE 3 — COMPANY-SPECIFIC APPROACH", [
            "SUBJECT: [Their Company] background — perfect for what my client needs",
            "",
            "Hi [Name],",
            "",
            "I work with several companies who specifically look for candidates with [Their Company] experience — your time there is genuinely valued in the market.",
            "",
            "I'm currently filling a [Role Title] role that would be a strong next step for someone with your background. Happy to share details. Would you have 15 minutes this week?",
        ]),
        ("INMAIL TEMPLATE 4 — ACHIEVEMENT-BASED", [
            "SUBJECT: Your [achievement/project] stood out to me",
            "",
            "Hi [Name],",
            "",
            "I noticed on your profile that you [specific achievement — led team, implemented system, grew revenue]. That kind of experience is exactly what my client is searching for.",
            "",
            "They're a [company description] looking for a [Role Title] who can [parallel to their achievement]. Would you be open to a brief conversation?",
        ]),
        ("INMAIL TEMPLATE 5 — BRIEF AND DIRECT", [
            "SUBJECT: Quick question",
            "",
            "Hi [Name],",
            "",
            "[Role Title] role in [City] — [Industry], [salary range if appropriate], reports to [level]. Strong company, great culture. Your profile matches closely.",
            "",
            "Open to a 15-minute conversation this week?",
        ]),
    ])

doc("03_CANDIDATE_SOURCING/Boolean_Search_String_Library.docx",
    "BOOLEAN SEARCH STRING LIBRARY",
    "20+ ready-to-use boolean strings for LinkedIn and Google X-Ray searches",
    [
        ("HOW TO USE BOOLEAN SEARCH", [
            "Boolean search uses logical operators to refine results:",
            "AND — both terms must appear (narrows results)",
            "OR — either term appears (broadens results)",
            "NOT — excludes a term",
            'Quotation marks \"\" — searches for exact phrase',
            "Parentheses () — groups terms together",
            "",
            "In LinkedIn: Enter boolean strings in the Keywords field of the search bar.",
            "For Google X-Ray: site:linkedin.com/in + your boolean string in Google Search.",
        ]),
        ("1. STAFF ACCOUNTANT", [
            '("Staff Accountant" OR "Junior Accountant" OR "Accountant I") AND ("QuickBooks" OR "NetSuite" OR "SAP") AND ("accounts payable" OR "accounts receivable" OR "general ledger") NOT "Senior" NOT "Manager"',
        ]),
        ("2. SENIOR ACCOUNTANT / CPA", [
            '("Senior Accountant" OR "Accounting Manager" OR "CPA") AND ("GAAP" OR "month-end close" OR "financial reporting") AND ("Excel" OR "ERP") NOT "Director" NOT "VP"',
        ]),
        ("3. SOFTWARE ENGINEER — BACKEND", [
            '("Software Engineer" OR "Backend Engineer" OR "Software Developer") AND ("Python" OR "Java" OR "Go" OR "Node.js") AND ("REST API" OR "microservices" OR "AWS" OR "Kubernetes") NOT "intern" NOT "junior"',
        ]),
        ("4. FULL STACK DEVELOPER", [
            '("Full Stack Developer" OR "Full Stack Engineer") AND ("React" OR "Angular" OR "Vue") AND ("Node" OR "Python" OR "Java") AND ("SQL" OR "MongoDB" OR "PostgreSQL")',
        ]),
        ("5. DEVOPS ENGINEER", [
            '("DevOps Engineer" OR "Site Reliability Engineer" OR "SRE" OR "Platform Engineer") AND ("Kubernetes" OR "Docker" OR "Terraform") AND ("CI/CD" OR "Jenkins" OR "GitHub Actions") AND ("AWS" OR "Azure" OR "GCP")',
        ]),
        ("6. MARKETING MANAGER", [
            '("Marketing Manager" OR "Senior Marketing Manager" OR "Marketing Lead") AND ("digital marketing" OR "demand generation" OR "content marketing") AND ("HubSpot" OR "Salesforce" OR "Google Analytics") NOT "intern" NOT "coordinator"',
        ]),
        ("7. OPERATIONS MANAGER", [
            '("Operations Manager" OR "Director of Operations" OR "Operations Lead") AND ("process improvement" OR "Lean" OR "Six Sigma" OR "KPI") AND ("team management" OR "cross-functional") NOT "VP" NOT "SVP"',
        ]),
        ("8. SALES DIRECTOR / VP SALES", [
            '("Director of Sales" OR "VP of Sales" OR "Sales Director" OR "Head of Sales") AND ("B2B" OR "SaaS" OR "enterprise sales") AND ("Salesforce" OR "CRM") AND ("quota" OR "revenue growth" OR "sales strategy")',
        ]),
        ("9. ACCOUNT EXECUTIVE", [
            '("Account Executive" OR "Sales Representative" OR "Business Development Representative") AND ("SaaS" OR "B2B") AND ("cold calling" OR "prospecting" OR "pipeline") NOT "Manager" NOT "Director"',
        ]),
        ("10. HR MANAGER / HR GENERALIST", [
            '("HR Manager" OR "HR Generalist" OR "Human Resources Manager") AND ("HRIS" OR "Workday" OR "ADP" OR "BambooHR") AND ("employee relations" OR "benefits" OR "recruiting") AND (SHRM OR SPHR OR PHR)',
        ]),
        ("11. FINANCE MANAGER / CONTROLLER", [
            '("Finance Manager" OR "Controller" OR "Assistant Controller" OR "Financial Planning") AND ("FP&A" OR "budgeting" OR "forecasting") AND ("ERP" OR "SAP" OR "Oracle") NOT "VP" NOT "CFO"',
        ]),
        ("12. PROJECT MANAGER", [
            '("Project Manager" OR "Senior Project Manager" OR "Program Manager") AND ("PMP" OR "Agile" OR "Scrum" OR "Waterfall") AND ("stakeholder management" OR "risk management" OR "budget") NOT "IT Project" NOT "Technical"',
        ]),
        ("13. REGISTERED NURSE (RN)", [
            '("Registered Nurse" OR "RN" OR "Staff Nurse") AND ("ICU" OR "Med-Surg" OR "Emergency" OR "Telemetry") AND ("BLS" OR "ACLS") NOT "Travel" NOT "Agency" NOT "LPN"',
        ]),
        ("14. MEDICAL ASSISTANT", [
            '("Medical Assistant" OR "CMA" OR "RMA") AND ("phlebotomy" OR "EHR" OR "Epic" OR "vital signs") AND ("clinical" OR "outpatient" OR "primary care")',
        ]),
        ("15. DATA ANALYST", [
            '("Data Analyst" OR "Business Intelligence Analyst" OR "BI Analyst") AND ("SQL" OR "Python" OR "R") AND ("Tableau" OR "Power BI" OR "Looker") AND ("data visualization" OR "reporting" OR "dashboard") NOT "Senior" NOT "Engineer"',
        ]),
        ("16. SUPPLY CHAIN MANAGER", [
            '("Supply Chain Manager" OR "Logistics Manager" OR "Supply Chain Analyst") AND ("ERP" OR "SAP" OR "Oracle") AND ("vendor management" OR "procurement" OR "inventory") AND ("APICS" OR "CPIM" OR "CSCP")',
        ]),
        ("17. CUSTOMER SERVICE MANAGER", [
            '("Customer Service Manager" OR "Customer Experience Manager" OR "Call Center Manager") AND ("team lead" OR "supervision" OR "coaching") AND ("Zendesk" OR "Salesforce Service Cloud" OR "CRM") AND ("KPI" OR "NPS" OR "CSAT")',
        ]),
        ("18. CONTROLLER / DIRECTOR OF ACCOUNTING", [
            '("Controller" OR "Director of Accounting" OR "VP Finance") AND ("CPA" OR "public accounting") AND ("GAAP" OR "financial statements" OR "audit") AND ("team management" OR "department head")',
        ]),
        ("19. WAREHOUSE MANAGER", [
            '("Warehouse Manager" OR "Distribution Center Manager" OR "Logistics Supervisor") AND ("WMS" OR "SAP" OR "RF scanner") AND ("inventory control" OR "shipping" OR "receiving") AND ("team management")',
        ]),
        ("20. MECHANICAL ENGINEER", [
            '("Mechanical Engineer" OR "Senior Mechanical Engineer") AND ("SolidWorks" OR "AutoCAD" OR "CATIA") AND ("design" OR "manufacturing" OR "product development") AND ("PE" OR "BSME" OR "MSME")',
        ]),
        ("GOOGLE X-RAY TEMPLATE", [
            "To search LinkedIn profiles via Google (when you don't have InMail credits):",
            "",
            'site:linkedin.com/in "[Job Title]" "[City, State]" "[Required Skill]" "[Required Skill 2]"',
            "",
            "Example:",
            'site:linkedin.com/in "Software Engineer" "Austin, Texas" "Python" "AWS"',
            "",
            "Then click the LinkedIn result to view the profile. Connect or contact directly.",
        ]),
    ])

doc("03_CANDIDATE_SOURCING/Passive_Candidate_Outreach_Scripts.docx",
    "PASSIVE CANDIDATE OUTREACH SCRIPTS",
    "15 scripts for LinkedIn, email, and phone outreach to passive candidates",
    [
        ("PHONE SCRIPT 1 — COLD CALL TO PASSIVE CANDIDATE", [
            'YOU: "Hi [Name], this is [Your Name] with [Agency]. I know this is totally out of the blue and I\'ll be brief — I came across your profile while working on a search for a [Role Title] with a [Industry] company in [City]. Your background at [Current Company] stood out. Is this a decent time for a 2-minute conversation?"',
            "",
            '[Candidate: yes/no response]',
            "",
            'IF YES: "Great. Here\'s the short version: [Company type], [role], [salary range if appropriate], [one compelling thing about the role]. It\'s not meant to replace what you have — I just thought it was worth a conversation. Are you at all open to hearing more?"',
            "",
            'IF NO: "Completely understand — when would be better? I\'d love to just have a 10-minute conversation, even if the timing isn\'t right for a move."',
        ]),
        ("PHONE SCRIPT 2 — WARM FOLLOW-UP (THEY RESPONDED TO YOUR LINKEDIN)", [
            'YOU: "Hi [Name], this is [Your Name] — we connected on LinkedIn about the [Role] opportunity. Thanks so much for responding. I have about 10 minutes — is now a good time?"',
            "",
            'Tell me a bit about your current situation — how long have you been at [Company] and what does your role look like day to day?',
            "",
            '[Listen, then:]',
            "",
            '"I appreciate you sharing that. Here\'s a bit more about what I\'m working on... [describe role]. Based on what you just told me, I actually think this could be an interesting fit because [specific reason]. Would you be open to a more formal call with me later this week to go deeper?"',
        ]),
        ("PHONE SCRIPT 3 — REFERRAL OUTREACH", [
            '"Hi [Name], I was speaking with [Referral Name] at [Company] and they suggested I reach out to you. They thought you might be a great fit for a [Role Title] I\'m working on — or that you might know someone who is. Either way, I thought it was worth a call. Do you have 5 minutes?"',
        ]),
        ("PHONE SCRIPT 4 — FOLLOW-UP VOICEMAIL", [
            '"Hi [Name], this is [Your Name] with [Agency] — I left a voicemail [X days] ago about a [Role Title] opportunity. I don\'t want to keep calling if the timing isn\'t right, but I did want to try one more time because I genuinely think this is worth 10 minutes of your time. If you get a chance, I\'m at [number]. No pressure either way. Thanks, [Name]."',
        ]),
        ("PHONE SCRIPT 5 — CHECKING IN ON PREVIOUS CANDIDATE", [
            '"Hi [Name], this is [Your Name] with [Agency] — we spoke about [X months] ago about a [Role] opportunity. I know the timing wasn\'t right then. I\'m calling because I\'m working on a new search that made me think of you immediately. It\'s a [brief description]. Has anything changed in your situation? Would you be open to hearing about it?"',
        ]),
        ("EMAIL SCRIPT 1 — INITIAL OUTREACH", [
            "SUBJECT: [Role Title] in [City] — your profile stood out",
            "",
            "Hi [Name],",
            "",
            "I found your profile while sourcing for a [Role Title] with a [Industry] company in [City]. Your experience with [specific skill or company] is exactly what they're looking for.",
            "",
            "The role is [brief description — 1-2 sentences]. Compensation is [range if appropriate].",
            "",
            "I know you're probably not actively looking — that's actually why I'm reaching out. The best candidates rarely are.",
            "",
            "Would you have 15 minutes this week for a confidential conversation?",
            "",
            "Best,",
            "[Your Name] | [Agency] | [Phone]",
        ]),
        ("EMAIL SCRIPT 2 — FOLLOW-UP (NO RESPONSE TO EMAIL 1)", [
            "SUBJECT: Re: [Role Title] — following up",
            "",
            "Hi [Name],",
            "",
            "Following up on my note from [X days ago]. No worries if the timing isn't right — I just wanted to make sure my email didn't get buried.",
            "",
            "If you're open to a quick conversation, I'm available [Day] or [Day]. If not, I completely understand.",
            "",
            "[Your Name]",
        ]),
        ("EMAIL SCRIPT 3 — CAREER OPPORTUNITY ANGLE", [
            "SUBJECT: A career step worth knowing about",
            "",
            "Hi [Name],",
            "",
            "I recruit exclusively in [Industry] and I came across your background while working on a search. I want to be straightforward: the company I represent is offering something that doesn't come up often — [unique aspect: promotion, equity, remote, leadership, etc.].",
            "",
            "This isn't about whether you're actively looking. It's about whether this is worth 15 minutes of your time. I think it is.",
            "",
            "Would you be open to a brief conversation?",
        ]),
        ("EMAIL SCRIPT 4 — COMPETITOR COMPANY APPROACH", [
            "SUBJECT: Your [Industry] background is exactly what's needed",
            "",
            "Hi [Name],",
            "",
            "Companies in [Industry] frequently ask me for candidates with your specific background — particularly experience at organizations like [Their Company].",
            "",
            "I'm working on a [Role Title] search right now where that background would be a significant advantage. Would you be open to a quick conversation, even if you're happy where you are?",
        ]),
        ("EMAIL SCRIPT 5 — BRIEF AND DIRECT", [
            "SUBJECT: Quick question",
            "",
            "Hi [Name],",
            "",
            "[Role] | [City] | [Salary range] | [One compelling sentence about the role].",
            "",
            "Worth 15 minutes? I'm available [Day] or [Day].",
            "",
            "[Your Name]",
        ]),
        ("LINKEDIN MESSAGE SCRIPTS (Short — LinkedIn limits)", [
            "SCRIPT 1 (Connection Request): 'Hi [Name], I'm a recruiter specializing in [Industry]. Your experience caught my eye for a search I'm working on. Would love to connect — no pressure, just a conversation when the time is right.'",
            "",
            "SCRIPT 2 (Post-connection): 'Thanks for connecting! I'm working on a [Role Title] search in [City] — your background is a strong fit. Would you be open to a 15-minute call this week?'",
            "",
            "SCRIPT 3 (Achievement angle): 'Hi [Name] — I noticed you [achievement from profile]. My client is specifically looking for someone with that kind of experience. Would you be open to a quick conversation?'",
            "",
            "SCRIPT 4 (Referral ask): 'Hi [Name], I'm looking for a [Role Title] in [City]. You likely know the space well — if it's not a fit for you, would you know anyone I should speak with?'",
            "",
            "SCRIPT 5 (Company follower): 'Hi [Name], I saw you follow [Agency/Company] on LinkedIn. I'm working on a [Role] search that might interest you. Happy to share details if you'd like.'",
        ]),
    ])

doc("03_CANDIDATE_SOURCING/Job_Board_Optimization_Guide.docx",
    "JOB BOARD OPTIMIZATION GUIDE",
    "Maximize results from Indeed, LinkedIn Jobs, ZipRecruiter, and niche boards",
    [
        ("INDEED STRATEGY", [
            "POSTING BEST PRACTICES:",
            ("•","Job title: Use the EXACT title candidates search for — not internal titles"),
            ("•","Salary: ALWAYS include — postings with salary get 3x more applicants"),
            ("•","Location: Include city and state. Remote? Say it in the title AND description."),
            ("•","Description: 600-800 words ideal. Use bullet points, not paragraphs."),
            ("•","Indeed uses keyword-matching: include required skills in the body text naturally"),
            "",
            "SPONSORED VS. ORGANIC:",
            ("•","Organic posts get pushed down after 3-5 days — sponsor for critical roles"),
            ("•","Set a daily budget of $10-30 to stay visible for important searches"),
            ("•","Use 'Pay per application' vs 'Pay per click' — better ROI for quality"),
            "",
            "INDEED PERFORMANCE METRICS TO WATCH:",
            ("•","Application rate: (Applications / Views) > 5% is strong"),
            ("•","Cost per application: Under $15 for mid-level roles"),
            ("•","If views are low: Refresh the title or boost sponsorship"),
            ("•","If views are high but applications are low: Rewrite the description"),
        ]),
        ("LINKEDIN JOBS STRATEGY", [
            "BEST FOR: Professional/white-collar roles, management, director-level+",
            "",
            "FREE POSTING LIMITS: LinkedIn allows 1 free posting per 30 days. For agency volume, you need a LinkedIn Recruiter or Job Slots subscription.",
            "",
            "OPTIMIZATION TIPS:",
            ("•","Post from your Agency Company Page for brand visibility"),
            ("•","Include a compelling company culture section — candidates research you"),
            ("•","'Easy Apply' gets more volume; 'Apply on Website' gets more quality"),
            ("•","Use the skill assessments feature — filters out weak applicants"),
            ("•","Refresh postings every 2 weeks to stay algorithm-ranked"),
            "",
            "USING LINKEDIN RECRUITER (If you have it):",
            ("•","InMail 3x response rate when referencing a job posting"),
            ("•","Use 'Open Candidates' filter to find passive candidates open to roles"),
            ("•","Spotlights feature shows candidates who engaged with your company"),
        ]),
        ("ZIPRECRUITER STRATEGY", [
            "BEST FOR: Volume hiring, light industrial, admin, customer service, retail",
            "",
            "UNIQUE FEATURE: ZipRecruiter distributes your posting to 100+ job boards automatically. One post = 100+ sites.",
            "",
            "OPTIMIZATION:",
            ("•","Use ZipRecruiter's Invite-to-Apply feature — proactively sends your post to matching candidates"),
            ("•","Premium plan allows unlimited invitations"),
            ("•","Strong for markets where Indeed is expensive — compare CPL between platforms quarterly"),
            "",
            "CANDIDATE QUALITY MANAGEMENT:",
            ("•","Set up screening questions (3-5 max) to filter applicants"),
            ("•","Use ZipRecruiter's rating system: thumb up/down as you review to train the algorithm"),
        ]),
        ("NICHE JOB BOARDS BY INDUSTRY", [
            "HEALTHCARE: Health eCareers, NurseFly, Vivian Health, Nurses.com, MedZilla",
            "TECHNOLOGY: Dice, Stack Overflow Jobs, GitHub Jobs, AngelList (startups), Hired.com",
            "FINANCE/ACCOUNTING: eFinancialCareers, Accounting Fly, CPA Trendlines",
            "ENGINEERING: EngineeringJobs.com, Engineering.com, IEEE Job Site",
            "LEGAL: Lawjobs.com, Martindale-Avvo, BCG Attorney Search",
            "CREATIVE/MARKETING: Behance, Coroflot, AIGA Design Jobs, Working Not Working",
            "LOGISTICS/SUPPLY CHAIN: FreightWaves, Logistics Jobs, CSCMP Career Center",
            "MANUFACTURING: ManufacturingJobs.com, Tooling U-SME, Automation Alley",
            "EDUCATION: HigherEdJobs.com, Teachers-Teachers.com, EdJoin",
            "NONPROFIT: Idealist.org, NonprofitJobs.org, Work for Good",
        ]),
        ("POSTING CADENCE RECOMMENDATIONS", [
            "Critical roles (must fill in <30 days): Post on Indeed + LinkedIn + 1 niche board, sponsor on Indeed, send InMails simultaneously",
            "Standard roles: Post on Indeed + LinkedIn, monitor for 5 days before sponsoring",
            "Specialty roles: Lead with niche board, supplement with LinkedIn, skip Indeed",
            "Volume/temp roles: ZipRecruiter primary, Indeed secondary",
            "Refresh all active postings every 14 days to maintain algorithmic visibility",
        ]),
        ("PERFORMANCE METRICS TO TRACK WEEKLY", [
            "Views per posting (target: 200+ in first 7 days)",
            "Application rate (target: 5%+ of views)",
            "Qualified application rate (target: 20%+ of total applicants)",
            "Cost per qualified applicant (target: under $30)",
            "Time from posting to first interview (target: under 7 days)",
            "Source of hire tracking: Which board produced your actual placements?",
        ]),
    ])

print("\n=== PART 1 COMPLETE ===")
print(f"Files created in {BASE}")
