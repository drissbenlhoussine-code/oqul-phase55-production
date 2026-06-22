#!/usr/bin/env python3
"""AI SMMA OS - Part 2: Folders 03,04,05,06 + Pricing_Calculator.xlsx + Content_Calendar_Tracker.xlsx"""
import os
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment

BASE = "/home/user/oqul-phase55-production/ai-smma-os/Ultimate_AI_SMMA_Operating_System/"
NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"

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

# ─── 03_PROPOSALS_CONTRACTS ────────────────────────────────────────────────────
p03 = "03_PROPOSALS_CONTRACTS/"

doc(p03+"Proposal_Writing_Guide.docx",
    "Proposal Writing Guide — How to Write Proposals That Close",
    "Ultimate AI SMMA OS | Psychology, Structure, and Pricing Presentation for SMMA Proposals",
    [
        ("Why Most Agency Proposals Fail", [
            "The majority of SMMA proposals lose deals not because of price — but because they are generic, feature-focused documents that fail to connect the agency's services to the client's specific goals. Winning proposals feel personal, demonstrate deep understanding, and make the client feel that saying yes is the obvious next step. This guide teaches you to write proposals that close.",
        ]),
        ("The Psychology of a Winning Proposal", [
            ("•", "Mirror Their Words: Use the language the client used in the discovery call. If they said 'we need more bookings', your proposal talks about booking growth — not 'follower count increase'"),
            ("•", "Show, Don't Tell: Replace 'we're a results-driven agency' with 'we helped [similar business] generate 23 leads in 45 days' — every claim should be supported with evidence"),
            ("•", "Anchor High: Present the Premium package first (even if the client said a lower budget). This anchors the perception of value before they see the package they actually want"),
            ("•", "Create FOMO: 'We typically work with 5-7 clients per quarter to ensure quality — we currently have 2 slots available' — creates urgency without pressure"),
            ("•", "Remove Risk: Include a clear onboarding process, revision policy, and reporting schedule — the more transparent your process, the more confident they feel"),
        ]),
        ("The 7-Section Proposal Structure", [
            "Section 1 — Cover Page:",
            ("•", "Client's business name, logo if available, 'Prepared exclusively for [Client Name]'"),
            ("•", "Your agency name, your name, contact details, date"),
            ("•", "Tagline: Something that speaks directly to their goal: 'Your roadmap to [X outcome] through social media'"),
            "Section 2 — Executive Summary (1 page):",
            ("•", "1 paragraph: Demonstrate you understand their situation. Use their exact words from the discovery call."),
            ("•", "1 paragraph: What you will do and what outcome it creates. Be specific — numbers and timeframes."),
            ("•", "1 sentence: Why you are the right agency for this. Make it specific to their niche or situation."),
            "Section 3 — Situation Analysis:",
            ("•", "Brief audit findings: What you noticed about their current social media presence"),
            ("•", "Key opportunities: 2-3 specific areas where there is clear upside"),
            ("•", "Current risk: What is it costing them to NOT act (lost leads, competitor growth, etc.)"),
            "Section 4 — Our Recommended Strategy:",
            ("•", "The platforms you will focus on and why (based on their niche and audience)"),
            ("•", "Content pillars: The 3-5 themes that will drive their content strategy"),
            ("•", "Key tactics: Specific formats, posting frequency, and distribution strategy"),
            "Section 5 — Deliverables and Timeline:",
            ("•", "Clear list of every deliverable included in the retainer"),
            ("•", "Month 1 timeline: onboarding, strategy, first content batch"),
            ("•", "Ongoing monthly deliverable schedule"),
            "Section 6 — Investment Options:",
            ("•", "Present your recommended package first, in full detail"),
            ("•", "Present one alternative (up-tier or down-tier) to give choice without overwhelming"),
            ("•", "Show total monthly investment, what's included, and any excluded items (ad spend)"),
            "Section 7 — Next Steps:",
            ("•", "Clear 3-step action: Review proposal → Sign contract → Pay first invoice"),
            ("•", "Your availability: 'I can have you onboarded and content ready within [X] days of signing'"),
            ("•", "Contact details and calendar link for questions"),
        ]),
        ("Pricing Presentation Techniques", [
            "Always Present Monthly First, Annual Second:",
            '"The investment is €1,500 per month — or €16,200 per year if you prefer annual billing (saving €1,800)."',
            "The Per-Day Technique:",
            '"For less than €50 per day, you get a complete social media management team dedicated to your business."',
            "ROI Framing:",
            '"At €1,500/month, if we generate even 2 new clients for you from social media at your average client value of €3,000, you\'ve paid for 4 months of our services from a single month\'s work."',
            "Anchoring Technique:",
            '"Let me share three options. Our Elite solution at €5,000 is the most comprehensive. Our Pro at €3,000 is what most businesses in your situation choose. Our Growth at €1,500 is a great starting point if you want to test the results first. Based on your goals, I\'d recommend the Pro."',
        ]),
        ("Common Proposal Mistakes to Avoid", [
            ("•", "Generic Proposals: Never send a template with just the name changed. Clients feel this immediately."),
            ("•", "Too Long: A proposal should be 8-12 pages maximum. More than that and it doesn't get read."),
            ("•", "Features Over Outcomes: List what each deliverable achieves, not just what it is."),
            ("•", "No Follow-Up Plan: Always schedule a follow-up call when sending the proposal. 'I\'ll call you Thursday at 3pm to walk through any questions' — never just send and wait."),
            ("•", "No Expiry Date: Add 'This proposal is valid for 14 days' — creates urgency and keeps your calendar clean."),
        ]),
    ])

doc(p03+"SMMA_Retainer_Agreement_Template.docx",
    "SMMA Retainer Agreement Template",
    "Ultimate AI SMMA OS | Complete Legal Contract Template for Social Media Marketing Services",
    [
        ("IMPORTANT LEGAL DISCLAIMER", [
            "This is a template agreement intended for educational and reference purposes. It should be reviewed and customized by a qualified legal professional in your jurisdiction before use. Laws vary by country and region. This template does not constitute legal advice.",
        ]),
        ("SOCIAL MEDIA MARKETING SERVICES RETAINER AGREEMENT", [
            "This Agreement is entered into as of [DATE] between:",
            "SERVICE PROVIDER: [AGENCY NAME], a [business type] organized under the laws of [Country/State], with its principal place of business at [Address] ('Agency')",
            "CLIENT: [CLIENT BUSINESS NAME], a [business type] organized under the laws of [Country/State], with its principal place of business at [Address] ('Client')",
            "Together referred to as 'the Parties'.",
        ]),
        ("1. SERVICES", [
            "1.1 Scope of Services: Agency agrees to provide the following social media marketing services to Client during the term of this Agreement (the 'Services'):",
            "[LIST ALL DELIVERABLES FROM CHOSEN PACKAGE — e.g.:]",
            ("•", "Content creation and management for [specified platforms]"),
            ("•", "[X] posts per month including copywriting, design, and scheduling"),
            ("•", "Community management including comment responses and DM management"),
            ("•", "Monthly performance reporting"),
            ("•", "[Any additional services from package]"),
            "1.2 Exclusions: The Services do not include paid advertising spend (which remains Client's responsibility), graphic design outside agreed scope, or services not explicitly listed in Section 1.1.",
            "1.3 Modifications to Services: Any modifications to the scope of Services must be agreed in writing by both Parties and may result in adjusted fees.",
        ]),
        ("2. FEES AND PAYMENT", [
            "2.1 Monthly Retainer: Client agrees to pay Agency a monthly retainer fee of €[AMOUNT] per month for the Services.",
            "2.2 Payment Schedule: The monthly retainer is due on the [1st / 15th] of each month. The first payment is due upon signing of this Agreement.",
            "2.3 Payment Method: Payments shall be made via [bank transfer / Stripe / PayPal] to Agency's designated account.",
            "2.4 Late Payment: Invoices not paid within 7 days of the due date may be subject to a late fee of 1.5% per month on the outstanding balance. Agency reserves the right to pause Services if payment is more than 14 days overdue.",
            "2.5 Price Increases: Agency may adjust monthly fees with 30 days' written notice. Client may terminate with 30 days' notice if they do not agree to the increase.",
            "2.6 Ad Spend: Any paid advertising budget is separate from and in addition to the monthly retainer. Client is responsible for all advertising spend directly.",
        ]),
        ("3. TERM AND TERMINATION", [
            "3.1 Initial Term: This Agreement shall commence on [START DATE] and continue for a minimum term of [3/6] months ('Initial Term').",
            "3.2 Renewal: Following the Initial Term, this Agreement will automatically renew on a month-to-month basis unless terminated by either Party.",
            "3.3 Termination by Client: After the Initial Term, Client may terminate this Agreement by providing 30 days' written notice to Agency.",
            "3.4 Termination by Agency: Agency may terminate this Agreement with 30 days' written notice, or immediately if Client breaches any material term of this Agreement.",
            "3.5 Early Termination: If Client terminates during the Initial Term, Client agrees to pay a termination fee equal to the remaining months in the Initial Term.",
        ]),
        ("4. INTELLECTUAL PROPERTY", [
            "4.1 Client Ownership: Upon full payment of all fees, Client owns all final deliverables created specifically for Client under this Agreement, including all social media content, graphics, and copy.",
            "4.2 Agency Portfolio Rights: Agency retains the right to display work created for Client in Agency's portfolio, website, and marketing materials, unless Client requests otherwise in writing.",
            "4.3 Pre-Existing Materials: Any tools, templates, processes, or systems used by Agency to create deliverables remain Agency's intellectual property.",
            "4.4 Client-Provided Materials: Client grants Agency a limited license to use Client's logos, brand assets, images, and content solely for the purpose of providing the Services.",
        ]),
        ("5. CONFIDENTIALITY", [
            "5.1 Mutual Confidentiality: Both Parties agree to keep confidential all non-public information disclosed by the other Party in connection with this Agreement.",
            "5.2 Duration: Confidentiality obligations survive termination of this Agreement for a period of 2 years.",
            "5.3 Exclusions: Confidentiality obligations do not apply to information that is publicly available, independently developed, or required to be disclosed by law.",
        ]),
        ("6. WARRANTIES AND LIMITATION OF LIABILITY", [
            "6.1 Agency Warranties: Agency warrants that Services will be performed professionally and in accordance with industry standards.",
            "6.2 No Results Guarantee: Agency makes no guarantee of specific follower growth, engagement rates, sales, or revenue outcomes from the Services.",
            "6.3 Limitation of Liability: Agency's maximum liability under this Agreement shall not exceed the fees paid by Client in the 3 months preceding the claim.",
            "6.4 Indemnification: Client agrees to indemnify Agency against any claims arising from Client-provided content that infringes third-party rights.",
        ]),
        ("7. SIGNATURES", [
            "By signing below, both Parties agree to be bound by the terms of this Agreement.",
            "AGENCY:",
            "Signature: _______________________",
            "Printed Name: _______________________",
            "Title: _______________________",
            "Date: _______________________",
            "CLIENT:",
            "Signature: _______________________",
            "Printed Name: _______________________",
            "Title: _______________________",
            "Date: _______________________",
        ]),
    ])

doc(p03+"Non_Disclosure_Agreement.docx",
    "Non-Disclosure Agreement (NDA)",
    "Ultimate AI SMMA OS | Mutual NDA for Client Business Information",
    [
        ("IMPORTANT LEGAL DISCLAIMER", [
            "This is a template NDA intended for educational and reference purposes. Have a legal professional review before use in your jurisdiction.",
        ]),
        ("MUTUAL NON-DISCLOSURE AGREEMENT", [
            "This Non-Disclosure Agreement ('Agreement') is entered into as of [DATE] between:",
            "Party A: [AGENCY NAME], located at [Address]",
            "Party B: [CLIENT NAME / BUSINESS NAME], located at [Address]",
            "(Each a 'Party' and collectively the 'Parties')",
        ]),
        ("1. PURPOSE", [
            "The Parties intend to explore a potential business relationship in which each Party may disclose confidential information to the other. This Agreement establishes the terms under which each Party will protect the other's confidential information.",
        ]),
        ("2. DEFINITION OF CONFIDENTIAL INFORMATION", [
            "2.1 'Confidential Information' means any non-public information disclosed by either Party that is marked as confidential or that a reasonable person would understand to be confidential given the context, including:",
            ("•", "Business strategies, marketing plans, and financial data"),
            ("•", "Client lists, customer data, and prospect information"),
            ("•", "Proprietary processes, systems, and methodologies"),
            ("•", "Technical data, trade secrets, and intellectual property"),
            ("•", "Any information designated as confidential by the disclosing Party"),
        ]),
        ("3. OBLIGATIONS", [
            "3.1 Each receiving Party agrees to:",
            ("•", "Keep all Confidential Information strictly confidential"),
            ("•", "Not disclose Confidential Information to any third parties without prior written consent"),
            ("•", "Use Confidential Information solely for the purpose of evaluating the potential business relationship"),
            ("•", "Limit access to Confidential Information to personnel who need it to fulfil the above purpose"),
            ("•", "Notify the disclosing Party promptly upon discovery of any unauthorized disclosure"),
        ]),
        ("4. EXCLUSIONS", [
            "4.1 This Agreement does not apply to information that:",
            ("•", "Was already publicly known at the time of disclosure"),
            ("•", "Becomes publicly known through no fault of the receiving Party"),
            ("•", "Was independently developed by the receiving Party without use of Confidential Information"),
            ("•", "Must be disclosed by law or court order (receiving Party will give prompt notice)"),
        ]),
        ("5. TERM", [
            "This Agreement shall remain in effect for 2 years from the date of signing. The confidentiality obligations with respect to any Confidential Information disclosed during the term shall survive for 3 years from the date of disclosure.",
        ]),
        ("6. REMEDIES", [
            "The Parties acknowledge that breach of this Agreement would cause irreparable harm for which monetary damages would be inadequate. Each Party is entitled to seek injunctive relief in addition to any other remedies available at law.",
        ]),
        ("7. GOVERNING LAW", [
            "This Agreement shall be governed by the laws of [Country/Jurisdiction]. Any disputes shall be resolved in the courts of [City/Jurisdiction].",
        ]),
        ("8. SIGNATURES", [
            "Party A Signature: _______________________  Date: _______________",
            "Printed Name: _______________________",
            "Party B Signature: _______________________  Date: _______________",
            "Printed Name: _______________________",
        ]),
    ])

# Pricing Calculator XLSX
wb = Workbook()
ws1 = wb.active
ws1.title = "Service Pricing"
ws1.append(["AI SMMA OS — Service Pricing Calculator"])
ws1["A1"].font = Font(bold=True, size=14, color=NAV)
ws1.append([""])
sp_headers = ["Deliverable","Unit","Cost to Deliver (€)","Markup %","Client Price (€)","Profit (€)","Margin %"]
ws1.append(sp_headers)
for cell in ws1[3]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

sp_data = [
    ["Static Graphic Post","Per post","8","250%","28","20","71%"],
    ["Carousel Post (5-7 slides)","Per carousel","18","200%","54","36","67%"],
    ["Reel Script + Caption","Per reel","12","225%","39","27","69%"],
    ["Reel Editing","Per reel","25","180%","70","45","64%"],
    ["Story Set (3 stories)","Per set","6","233%","20","14","70%"],
    ["Long-Form Caption Writing","Per caption","10","200%","30","20","67%"],
    ["Community Management","Per hour","15","200%","45","30","67%"],
    ["Monthly Report","Per report","30","200%","90","60","67%"],
    ["Ad Campaign Setup","Per campaign","80","188%","230","150","65%"],
    ["Ad Copy (1 ad set)","Per set","20","225%","65","45","69%"],
    ["Strategy Call (30 min)","Per call","25","200%","75","50","67%"],
    ["Competitor Research","Per month","20","250%","70","50","71%"],
    ["Content Calendar Creation","Per month","25","200%","75","50","67%"],
    ["Hashtag Research","Per set","10","200%","30","20","67%"],
    ["Platform Setup/Optimization","One-time","60","233%","200","140","70%"],
]
for i, row in enumerate(sp_data):
    ws1.append(row)
    for cell in ws1[i+4]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(horizontal="center", vertical="center")

for col, w in [("A",32),("B",14),("C",20),("D",12),("E",18),("F",12),("G",10)]:
    ws1.column_dimensions[col].width = w

# Package Builder Sheet
ws2 = wb.create_sheet("Package Builder")
ws2.append(["SMMA Package Builder — Build Custom Packages"])
ws2["A1"].font = Font(bold=True, size=14, color=NAV)
ws2.append([""])
pb_headers = ["Deliverable","Qty/Month","Unit Cost (€)","Total Cost (€)","Included in Package?"]
ws2.append(pb_headers)
for cell in ws2[3]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

pb_data = [
    ["Static Graphic Posts","8","28","=B4*C4","YES"],
    ["Carousel Posts","4","54","=B5*C5","YES"],
    ["Reel Scripts + Captions","4","39","=B6*C6","YES"],
    ["Story Sets","8","20","=B7*C7","YES"],
    ["Community Management (hrs)","10","45","=B8*C8","YES"],
    ["Monthly Report","1","90","=B9*C9","YES"],
    ["Strategy Call","1","75","=B10*C10","YES"],
    ["Ad Campaign Management","0","230","=B11*C11","NO"],
    ["Ad Copy","0","65","=B12*C12","NO"],
    ["Competitor Research","1","70","=B13*C13","YES"],
    ["Influencer Outreach","0","200","=B14*C14","NO"],
]
for i, row in enumerate(pb_data):
    ws2.append(row)
    for cell in ws2[i+4]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(horizontal="center")

ws2.append([""])
ws2.append(["TOTAL COST TO DELIVER","","","=SUM(D4:D14)",""])
ws2.append(["TARGET CLIENT PRICE (€)","1500","","","Enter your package price here"])
ws2.append(["GROSS PROFIT","","","=B17-D16",""])
ws2.append(["GROSS MARGIN %","","","=D18/B17","Format this cell as %"])
for col, w in [("A",32),("B",12),("C",16),("D",16),("E",22)]:
    ws2.column_dimensions[col].width = w

# Break-Even Calculator Sheet
ws3 = wb.create_sheet("Break-Even Calculator")
ws3.append(["Break-Even Calculator — Know Your Numbers"])
ws3["A1"].font = Font(bold=True, size=14, color=NAV)
ws3.append([""])
ws3.append(["MONTHLY FIXED EXPENSES","Amount (€)"])
for cell in ws3[3]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center")

be_expenses = [
    ["Graphic design software (Canva Pro)","15"],
    ["Social media scheduling tool (Buffer/Later)","18"],
    ["AI tools (ChatGPT Plus + Claude)","40"],
    ["Video editing software","25"],
    ["Email marketing tool","30"],
    ["CRM / project management","15"],
    ["Domain + website hosting","10"],
    ["Accounting software","25"],
    ["Workspace / coworking","150"],
    ["Phone and internet","80"],
    ["Marketing (own agency ads/content)","100"],
    ["Education and courses","50"],
    ["TOTAL FIXED EXPENSES","=SUM(B4:B14)"],
]
for i, row in enumerate(be_expenses):
    ws3.append(row)
    if row[0] == "TOTAL FIXED EXPENSES":
        for cell in ws3[i+4]:
            cell.fill = PatternFill("solid", fgColor=NAV)
            cell.font = Font(bold=True, color=WHT)
    else:
        for cell in ws3[i+4]:
            cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)

ws3.append([""])
ws3.append(["PRICING AND HOURS INPUT","Value"])
ws3.append(["Your average package price (€/month)","1500"])
ws3.append(["Hours spent per client per month","20"])
ws3.append(["Your target hourly rate (€/hr)","75"])
ws3.append(["Your personal monthly salary target (€)","3000"])
ws3.append([""])
ws3.append(["BREAK-EVEN OUTPUTS","Calculation"])
ws3.append(["Clients needed to cover fixed expenses","=ROUNDUP(B16/B20,0)"])
ws3.append(["Clients needed to reach salary target","=ROUNDUP((B16+B23)/B20,0)"])
ws3.append(["Max clients before needing to hire (40hr/wk limit)","=INT(160/B21)"])
ws3.append(["Monthly revenue at full capacity","=INT(160/B21)*B20"])
ws3.append(["Annual revenue at full capacity","=INT(160/B21)*B20*12"])
for col, w in [("A",45),("B",20)]:
    ws3.column_dimensions[col].width = w

wb.save(BASE + p03 + "Pricing_Calculator.xlsx")
print(f"  ✓ {p03}Pricing_Calculator.xlsx")
print("✓ 03_PROPOSALS_CONTRACTS complete")

# ─── 04_CLIENT_ONBOARDING ──────────────────────────────────────────────────────
p04 = "04_CLIENT_ONBOARDING/"

doc(p04+"Client_Onboarding_SOP.docx",
    "Client Onboarding SOP — From Signed Contract to First Content",
    "Ultimate AI SMMA OS | Complete 30-Day New Client Onboarding Process",
    [
        ("Why Onboarding Defines the Relationship", [
            "The onboarding experience a new client has with your agency determines whether they stay 3 months or 3 years. A disorganized, reactive onboarding signals to clients that the chaos will continue. A systematic, proactive onboarding builds immediate confidence and sets the tone for a professional, long-term relationship. This SOP covers every step of your onboarding process from day zero through the delivery of your first content.",
        ]),
        ("Day 0 — Contract and First Payment", [
            ("•", "Send signed contract via DocuSign, PandaDoc, or HelloSign — never paper-only"),
            ("•", "Issue first invoice immediately upon contract execution"),
            ("•", "Send welcome email (use Welcome_Email_Sequence.docx Email 1 as template)"),
            ("•", "Create client folder in Google Drive / Notion with: Brand Assets, Content Library, Reports, Contracts"),
            ("•", "Add client to your CRM (Notion Client_Database.csv) and mark status as 'Onboarding'"),
            ("•", "Set calendar reminders: 7-day kickoff, 14-day first check-in, 30-day first report"),
        ]),
        ("Days 1-5 — Information Gathering", [
            ("•", "Send Brand_Discovery_Questionnaire.docx to client — set a 5-day response deadline"),
            ("•", "Send Platform_Access_Setup_Guide.docx to client for granting access"),
            ("•", "Request brand assets: logo files (PNG + SVG), brand colors (hex codes), font names"),
            ("•", "Request any existing content: photos, videos, old social posts to keep or repurpose"),
            ("•", "Request competitor names and any 'inspiration accounts' they like"),
            ("•", "Request access to: Meta Business Manager, Google Analytics, any existing scheduling tools"),
        ]),
        ("Days 5-10 — Strategy Development", [
            ("•", "Complete Social_Media_Audit_Template.xlsx for all the client's current platforms"),
            ("•", "Research 5 competitors using the Competitor Analysis tab"),
            ("•", "Define 3-5 content pillars based on questionnaire responses and niche research"),
            ("•", "Define posting frequency per platform based on package tier"),
            ("•", "Build hashtag bank (50 hashtags per platform) using Hashtag_Strategy_Guide.docx"),
            ("•", "Draft Month 1 content themes and create the first content calendar frame"),
        ]),
        ("Days 10-14 — Kickoff Call", [
            "Kickoff Call Agenda (45 minutes):",
            ("•", "5 min: Introductions, welcome, confirm communication preferences"),
            ("•", "10 min: Present your audit findings from Social_Media_Audit_Template.xlsx"),
            ("•", "10 min: Present your 3-month social media strategy and content pillars"),
            ("•", "5 min: Walk through the content approval workflow — how reviews will work"),
            ("•", "5 min: Clarify any outstanding questionnaire items or asset requests"),
            ("•", "5 min: Set expectations — what they can expect and when, response times, revision policy"),
            ("•", "10 min: Q&A — let the client ask everything they have"),
            "Post-Call Actions:",
            ("•", "Send meeting notes within 24 hours"),
            ("•", "Begin content creation immediately after kickoff"),
        ]),
        ("Days 14-25 — First Content Batch", [
            ("•", "Create Month 1 content using AI_Prompt_Library.docx and Content_Creation_SOP.docx"),
            ("•", "Design all graphics using client's brand kit in Canva"),
            ("•", "Write all captions using Caption_Writing_Framework.docx"),
            ("•", "Conduct internal quality review against Agency_SOPs_Master_Guide.docx standards"),
            ("•", "Share content calendar with client via Notion, Google Sheets, or PDF"),
            ("•", "Allow 5 business days for client review and revision requests"),
        ]),
        ("Days 25-30 — First Publishing Cycle", [
            ("•", "Process all revision requests within 48 hours"),
            ("•", "Obtain written approval ('Looks good!' or 'Approved' message is sufficient) before scheduling"),
            ("•", "Schedule all approved content in Buffer/Hootsuite/Later"),
            ("•", "Publish first post and send client a 'Your first post is live!' message"),
            ("•", "Begin community management monitoring immediately after first post"),
            ("•", "Day 30: Send 1-month check-in message asking for feedback on the process"),
        ]),
    ])

doc(p04+"Welcome_Email_Sequence.docx",
    "Welcome Email Sequence — 5 Emails",
    "Ultimate AI SMMA OS | New Client Email Sequence from Day 0 to Day 14",
    [
        ("Email 1 — Day 0: Welcome and Confirmation", [
            "Subject: Welcome to [Agency Name] — Your journey starts now!",
            "Hi [Client Name],",
            "On behalf of everyone at [Agency Name], welcome! We are genuinely excited to work with you and [Business Name].",
            "Your contract has been received and confirmed. Here is a quick overview of what happens next:",
            "This week: We will send you our Brand Discovery Questionnaire and platform access instructions",
            "Week 2: We will hold your kickoff strategy call (I will send a calendar link shortly)",
            "Week 3-4: Your first content batch will be ready for your review",
            "End of Month 1: Your first content will be live across your platforms",
            "A few things I need from you to get started:",
            "1. Complete the Brand Discovery Questionnaire (arriving in your inbox within 24 hours)",
            "2. Grant platform access following the Platform Access Guide (arriving tomorrow)",
            "3. Share your brand assets: logo files, hex colors, and any brand guidelines",
            "My direct contact details:",
            "Email: [Your Email] | WhatsApp / Phone: [Your Number] | Response time: Within 4 business hours",
            "I am looking forward to building something great together. Please do not hesitate to reach out with any questions.",
            "Warmly,",
            "[Your Name]",
            "[Agency Name]",
        ]),
        ("Email 2 — Day 1: Questionnaire and Access", [
            "Subject: 2 Quick Actions to Start Your Onboarding (Brand Questionnaire + Platform Access)",
            "Hi [Client Name],",
            "As promised, here are the two things I need from you to kick off your social media strategy:",
            "ACTION 1 — Brand Discovery Questionnaire:",
            "[Link to questionnaire or attach Brand_Discovery_Questionnaire.docx]",
            "This typically takes 20-30 minutes. The more detail you provide, the better we can represent your brand voice and values in every piece of content.",
            "ACTION 2 — Platform Access:",
            "Please review the Platform Access Setup Guide attached. It walks you through exactly how to share access to your social media accounts safely.",
            "No passwords are needed — we use official Business Manager and admin access only.",
            "DEADLINE: If possible, please complete both by [Date 5 days from now]. This keeps our strategy and content creation on track.",
            "If you have any questions about any of the steps, just reply to this email and I will help you through it.",
            "Thank you!",
            "[Your Name]",
        ]),
        ("Email 3 — Day 3: Kickoff Call Scheduling", [
            "Subject: Let's book your Strategy Kickoff Call — [Business Name]",
            "Hi [Client Name],",
            "I have been reviewing everything I know about [Business Name] and I am already excited about the strategy we are building for you.",
            "It's time to book your Strategy Kickoff Call. This is a 45-minute video call where we will:",
            "• Present our audit findings from your social media accounts",
            "• Walk through your 3-month content strategy",
            "• Confirm your content pillars and brand voice direction",
            "• Walk through the approval and communication process",
            "Book your kickoff call here: [CALENDAR LINK]",
            "Ideal timing: Within the next 5-7 days",
            "Please also send over any brand assets you have (logo, brand guide, photos) if you have not done so yet — we want to start creating your visual identity as soon as possible.",
            "Looking forward to it!",
            "[Your Name]",
        ]),
        ("Email 4 — Day 7: Kickoff Reminder and Pre-Call Preparation", [
            "Subject: Your Kickoff Call is [Tomorrow / in X days] — Here's What to Prepare",
            "Hi [Client Name],",
            "Your strategy kickoff call is coming up [Tomorrow / in X days]! I am excited to share what we have put together.",
            "To make the most of our 45 minutes together, here is what to have ready:",
            "• Your top 3 business goals for the next 6 months",
            "• 2-3 social media accounts you admire (in any industry)",
            "• Any upcoming promotions, events, or launches in the next 90 days",
            "• Any content 'do nots' — topics, tones, or images you want to avoid",
            "Call details:",
            "Date: [DATE] | Time: [TIME] | Link: [ZOOM/GOOGLE MEET LINK]",
            "See you then!",
            "[Your Name]",
        ]),
        ("Email 5 — Day 14: First Content Check-In", [
            "Subject: Your first content is in progress — quick update from [Agency Name]",
            "Hi [Client Name],",
            "I wanted to give you a quick update on where we are:",
            "COMPLETED:",
            "✓ Platform audit and competitor analysis",
            "✓ Content strategy and pillars finalized (following our kickoff call)",
            "✓ Hashtag bank built",
            "✓ Brand assets imported to Canva",
            "IN PROGRESS:",
            "→ First 10 posts being designed and captioned",
            "→ Content calendar being built for [MONTH]",
            "COMING SOON:",
            "→ Content calendar shared for your review: [TARGET DATE]",
            "→ First posts go live: [TARGET DATE]",
            "If you have any new photos, products, or announcements to include in Month 1, please send them over by [DATE].",
            "Exciting times ahead! Thank you for your patience during setup — the results will be worth it.",
            "[Your Name]",
        ]),
    ])

doc(p04+"Brand_Discovery_Questionnaire.docx",
    "Brand Discovery Questionnaire — 50 Questions",
    "Ultimate AI SMMA OS | Complete Brand Voice, Audience, and Content Discovery",
    [
        ("SECTION 1: Business Fundamentals (Questions 1-10)", [
            "1. What is your business name, and what does it do in one sentence?",
            "2. How long have you been in business, and where are you based?",
            "3. What products or services do you offer? Please list them in order of importance or revenue.",
            "4. What is your average sale/project value?",
            "5. What are your top 3 business goals for the next 12 months?",
            "6. What is your primary marketing challenge right now?",
            "7. What marketing or advertising are you currently doing beyond social media?",
            "8. Do you have a website? What is the URL?",
            "9. Do you have any existing brand guidelines (colors, fonts, logo files)? Please share them.",
            "10. What is your current monthly marketing budget (including our retainer)?",
        ]),
        ("SECTION 2: Target Audience (Questions 11-20)", [
            "11. Describe your ideal customer. How old are they? What do they do for work?",
            "12. Where does your ideal customer live (local, national, or international)?",
            "13. What social media platforms does your ideal customer use most?",
            "14. What does your ideal customer care about most? What are their values?",
            "15. What problem does your ideal customer have that your business solves?",
            "16. What does your ideal customer do before they buy — how do they research and decide?",
            "17. What objections does your typical customer have before purchasing from you?",
            "18. What vocabulary or language does your ideal customer use? Any specific industry terms?",
            "19. Do you have existing customer reviews or testimonials you can share?",
            "20. Can you describe your best-ever customer — why were they ideal?",
        ]),
        ("SECTION 3: Brand Voice and Personality (Questions 21-30)", [
            "21. If your brand were a person, how would you describe their personality in 5 adjectives?",
            "22. What tone should your content use? (Choose all that apply: Professional, Friendly, Humorous, Authoritative, Inspirational, Educational, Bold, Calm, Empathetic)",
            "23. Are there any brands — in any industry — whose voice or social media you admire? Why?",
            "24. What does your brand stand for beyond the product or service you sell?",
            "25. What is your brand's mission statement (or what should it be)?",
            "26. What words, phrases, or expressions should NEVER appear in your content?",
            "27. What topics are completely off-limits for your brand? (Politics, religion, competitors, etc.)",
            "28. How do you want customers to feel after interacting with your content?",
            "29. Do you have a tagline or slogan? If yes, should it appear in content?",
            "30. Rate your current brand voice consistency (1-10) and explain what could be improved.",
        ]),
        ("SECTION 4: Content Preferences (Questions 31-40)", [
            "31. What types of content do you like? (Videos, carousels, photos, text, stories, live videos)",
            "32. What types of content have performed best on your accounts historically?",
            "33. What content do you absolutely NOT want? (E.g., 'no stock photos', 'no motivational quotes')",
            "34. Do you have a library of existing photos or videos we can use? Please share them.",
            "35. Are you willing to be on camera (face of brand)? Or should we avoid showing you?",
            "36. Do you have access to a photographer or videographer for new content?",
            "37. What colors, visual styles, or aesthetics do you like? Share examples if possible.",
            "38. What colors, visual styles, or aesthetics do you dislike?",
            "39. What are the top 3 social media accounts in your niche that you would like to emulate?",
            "40. How do you feel about using trending audio or meme formats? (Fully open / Sometimes / Never)",
        ]),
        ("SECTION 5: Competition and Positioning (Questions 41-50)", [
            "41. Who are your top 3 direct competitors? Please list their names and websites.",
            "42. What do your competitors do well on social media?",
            "43. What do your competitors do poorly on social media?",
            "44. What makes your business different from your competitors?",
            "45. Why do customers choose you over competitors? What have they specifically told you?",
            "46. Do you have any customer success stories or case studies you are willing to share?",
            "47. Are there topics your competitors talk about that you could own better?",
            "48. What is your geographic market? Are there local competitors we should know about?",
            "49. Have you ever lost a client to a competitor? What was the reason?",
            "50. Anything else you want us to know about your business, brand, customers, or goals?",
        ]),
    ])

doc(p04+"Platform_Access_Setup_Guide.docx",
    "Platform Access Setup Guide",
    "Ultimate AI SMMA OS | How to Safely Grant Agency Access to Your Social Media Accounts",
    [
        ("Why We Never Need Your Password", [
            "All major social media platforms have official 'admin access' or 'partner access' systems that allow you to grant our agency the ability to manage your accounts without ever sharing your personal password. This protects your account security while giving us everything we need to do our work. This guide walks you through each platform step by step.",
        ]),
        ("Facebook and Instagram (Meta Business Manager)", [
            "Step 1 — Create a Meta Business Manager (if you don't have one):",
            ("•", "Go to business.facebook.com and click 'Create Account'"),
            ("•", "Enter your business name, your name, and your business email address"),
            ("•", "Follow the prompts to connect your Facebook Page and Instagram account"),
            "Step 2 — Add Us as a Partner:",
            ("•", "In Meta Business Manager, go to Settings > Business Settings > Partners"),
            ("•", "Click 'Add' and select 'Give a partner access to your assets'"),
            ("•", "Enter our Agency Business ID: [YOUR AGENCY BUSINESS MANAGER ID]"),
            ("•", "Grant access to: Your Facebook Page + Instagram Account + Ad Account (if applicable)"),
            ("•", "Set permission level: 'Editor' for organic content, 'Advertiser' if we manage ads"),
            "Step 3 — Connect Instagram to Your Facebook Page:",
            ("•", "In Instagram app: Settings > Account > Linked Accounts > Facebook > Connect"),
            ("•", "This connects Instagram to your Business Manager for full management access"),
            "What We Will Be Able to Do:",
            ("•", "Create, schedule, and publish posts on Facebook and Instagram"),
            ("•", "Manage comments and direct messages"),
            ("•", "Access analytics and insights"),
            ("•", "Manage Instagram Stories and Reels"),
        ]),
        ("LinkedIn", [
            "For LinkedIn Company Pages (Business to Business management):",
            "Step 1 — Add Us as a Super Admin:",
            ("•", "Go to your LinkedIn Company Page"),
            ("•", "Click 'Admin Tools' in the top right > 'Manage Admins'"),
            ("•", "Click 'Add Admin' and search for [Agency Representative Name or LinkedIn URL]"),
            ("•", "Set role as 'Super Admin' for full management access, or 'Content Admin' for content only"),
            "For LinkedIn Personal Profiles (if we manage your personal brand):",
            ("•", "LinkedIn does not allow third-party admin access to personal profiles"),
            ("•", "We will provide content and scheduling instructions for you to post"),
            ("•", "OR: Use a LinkedIn third-party tool like Taplio where you authorize agency access via API"),
        ]),
        ("TikTok", [
            "Step 1 — Switch to a TikTok Business Account (if not already):",
            ("•", "In TikTok: Settings > Manage Account > Switch to Business Account"),
            "Step 2 — Use TikTok Business Center for Agency Access:",
            ("•", "Go to business.tiktok.com and sign in with your business account"),
            ("•", "Go to 'Settings' > 'Business Center' > 'Members'"),
            ("•", "Click 'Add Member' and enter our agency email: [AGENCY EMAIL]"),
            ("•", "Grant 'Operator' or 'Manager' access"),
            "Alternative — Direct Scheduler Access:",
            ("•", "Share access via your TikTok scheduling tool (Later, Hootsuite) by inviting our agency account"),
        ]),
        ("Google Analytics (if we track website conversions)", [
            "Step 1 — Add Agency as a User in Google Analytics 4:",
            ("•", "Go to analytics.google.com > Admin > Account Access Management"),
            ("•", "Click the '+' button > Add Users"),
            ("•", "Enter our agency email: [AGENCY EMAIL]"),
            ("•", "Set role as 'Analyst' (read and report) or 'Editor' (if we manage tracking setup)"),
            "Step 2 — For Google Ads (if we manage ads):",
            ("•", "Go to Google Ads > Tools > Access and Security > Managers"),
            ("•", "Click 'Link a Manager Account' and enter our Manager Account ID: [ID]"),
        ]),
        ("Security Best Practices", [
            ("•", "Enable Two-Factor Authentication on all your social media accounts"),
            ("•", "Review connected apps every 6 months and revoke any you no longer use"),
            ("•", "If you ever feel access has been compromised, change passwords and notify us immediately"),
            ("•", "We will never ask for your personal passwords — if anyone claiming to be us does, it is not us"),
            ("•", "When our contract ends, we will walk you through revoking our access on all platforms"),
        ]),
    ])

print("✓ 04_CLIENT_ONBOARDING complete")

# ─── 05_CONTENT_CREATION ───────────────────────────────────────────────────────
p05 = "05_CONTENT_CREATION/"

doc(p05+"Content_Creation_SOP.docx",
    "Content Creation SOP — From Brief to Published",
    "Ultimate AI SMMA OS | Complete Workflow for Consistent, High-Quality Content Production",
    [
        ("The 7-Stage Content Production Pipeline", [
            "Consistent quality in your agency requires a documented production pipeline. This SOP defines every stage from brief creation to post-publication reporting. Use this as your standard workflow for every client, every month, without exception.",
        ]),
        ("Stage 1 — Content Brief (Day 1-2 of Monthly Cycle)", [
            "The brief is the foundation of great content. A weak brief produces weak content — no matter how good your tools are.",
            ("•", "Review the client's business goals and any upcoming events, promotions, or launches"),
            ("•", "Check previous month's top-performing content for pattern recognition"),
            ("•", "Define monthly content themes (usually 2-3 themes per month, based on content pillars)"),
            ("•", "Specify post types by day and platform (e.g., 'Monday IG Reel, Tuesday LinkedIn carousel, Wednesday IG static + Stories')"),
            ("•", "Include any specific messages the client wants communicated this month"),
            "Brief Template (use for each client):",
            "Month: [MONTH] | Client: [CLIENT NAME] | Primary Goal: [GOAL]",
            "Theme 1: [Theme] — [3-4 post ideas]",
            "Theme 2: [Theme] — [3-4 post ideas]",
            "Special Focus: [Promotion/Event/Launch]",
        ]),
        ("Stage 2 — Research and Ideation (Day 2-3)", [
            ("•", "Spend 30 minutes reviewing competitor content from the past month for inspiration"),
            ("•", "Check trending audio on TikTok/Reels that could be used this month"),
            ("•", "Review industry news and trends relevant to the client's niche"),
            ("•", "Open AI_Prompt_Library.docx and run the content ideation prompts for this month's themes"),
            ("•", "Finalize post ideas and add to the content calendar in Content_Calendar_Tracker.xlsx"),
        ]),
        ("Stage 3 — Content Draft (Day 3-6)", [
            "Captions:",
            ("•", "Use Caption_Writing_Framework.docx (AIDA, PAS, or storytelling format)"),
            ("•", "Write the hook in the first line — test 3 hook options before choosing the best"),
            ("•", "Include CTA on every post (follow, comment, save, click link, DM us)"),
            ("•", "Add hashtags from client's Hashtag Bank (do not use random hashtags)"),
            "Visuals:",
            ("•", "Use client's Canva brand kit for all graphics — never deviate from brand colors"),
            ("•", "Design to platform specifications: IG Feed 1:1 (1080×1080) or 4:5 (1080×1350), Reels/TikTok 9:16 (1080×1920)"),
            ("•", "For carousels: Slide 1 = strong hook, Slides 2-6 = value delivery, Slide 7 = CTA"),
            "Video (if applicable):",
            ("•", "Script all videos using AI_Prompt_Library.docx reel script prompts"),
            ("•", "Send video brief to client or video creator with: script, hook, trend reference, call to action"),
        ]),
        ("Stage 4 — Internal Quality Review (Day 7-8)", [
            "Every piece of content must pass this internal checklist before client delivery:",
            ("•", "Visual: Correct brand colors, fonts, and logo usage?"),
            ("•", "Copy: No spelling errors, correct tone, CTA present?"),
            ("•", "Dimensions: Correct size for each platform?"),
            ("•", "Hashtags: From approved hashtag bank, within platform limits?"),
            ("•", "Completeness: All posts for the period are created and accounted for?"),
            ("•", "Second eyes: A team member reviewed all content for quality and errors?"),
        ]),
        ("Stage 5 — Client Review (Day 8-13)", [
            ("•", "Share content calendar via Notion, Google Sheets, or PDF link — not as individual files"),
            ("•", "Include clear deadline for feedback: 'Please submit all revisions by [DATE]'"),
            ("•", "Be specific in the sharing note: 'Please check captions for accuracy, confirm hashtag use, and approve or request changes for each post'"),
            ("•", "If no response by deadline, follow up by phone or message"),
        ]),
        ("Stage 6 — Revisions and Finalization (Day 13-15)", [
            ("•", "Process all revisions within 2 business days (1 day for Elite clients)"),
            ("•", "Log revision type: Was it a style change? A factual error? Out of scope?"),
            ("•", "Get written approval on final versions — a 'Looks good!' message counts"),
            ("•", "Archive original draft versions in client folder"),
        ]),
        ("Stage 7 — Scheduling and Publication (Day 15-17)", [
            ("•", "Schedule all approved content in your scheduling tool (Buffer, Later, Hootsuite)"),
            ("•", "Double-check publish time against client's audience timezone"),
            ("•", "Mark all content as 'SCHEDULED' in Content_Calendar_Tracker.xlsx"),
            ("•", "Notify client: 'Your [MONTH] content is scheduled! First post goes live [DATE]'"),
            ("•", "Monitor first 24 hours of each post for comments that need moderation"),
        ]),
    ])

doc(p05+"Caption_Writing_Framework.docx",
    "Caption Writing Framework — 30 Examples",
    "Ultimate AI SMMA OS | AIDA, PAS, Storytelling, Hooks, and CTAs for Every Niche",
    [
        ("The Foundation: Every Great Caption Has 3 Parts", [
            "HOOK (Line 1-2): This is the only part that shows before 'More' — it must stop the scroll. Think of it as a headline. If the hook fails, nothing else matters.",
            "BODY (Lines 3-10): Deliver on the promise of the hook. Educate, entertain, inspire, or provoke. Use short paragraphs and line breaks for readability.",
            "CTA (Last 1-2 Lines): Tell people exactly what to do next. One clear action — not three.",
        ]),
        ("Framework 1 — AIDA (Attention, Interest, Desire, Action)", [
            "Template: [Attention-grabbing statement] + [Build interest with relevant info] + [Create desire by showing outcome] + [Clear CTA]",
            "Example 1 (Restaurant):",
            "Hook: The secret ingredient that made our Sunday pasta sell out by noon.",
            "Body: It's not the pasta. It's not even the sauce. It's the 4-hour slow-cook method our head chef brought back from Naples in 2019. We only make 40 portions every Sunday. When they're gone, they're gone.",
            "CTA: Hit the link in bio to reserve yours for this Sunday. Comment 'PASTA' and we'll send you the time it typically sells out.",
            "Example 2 (Fitness Coach):",
            "Hook: I lost 18kg in 5 months. Here's what no one told me would be the hardest part.",
            "Body: Everyone talks about the diet and the workouts. Nobody talks about the 2am moment on week 6 when you've hit a plateau, you're exhausted, and you're wondering if any of it is working. That moment is where most people quit. It's also where the results start.",
            "CTA: If you're at that moment right now, DM me the word 'plateau' and let's talk strategy.",
        ]),
        ("Framework 2 — PAS (Problem, Agitate, Solution)", [
            "Template: [Name the problem] + [Make them feel the pain of the problem] + [Present your solution]",
            "Example 1 (E-Commerce Brand):",
            "Hook: Your competitors are making sales at 2am while you're asleep. Here's why.",
            "Body: They built a social media system that works without them. You're still posting manually, scrambling for ideas, hoping the algorithm shows your content to someone who cares. Every day without a strategy is a day your competitors get further ahead.",
            "CTA: We build that system for brands like yours. Link in bio to see what it looks like.",
            "Example 2 (Real Estate Agent):",
            "Hook: The house you want just sold for €40,000 over asking price. Not because of the market. Because of the agent.",
            "Body: In this market, the difference between getting the home and missing it comes down to two things: preparation and relationships. Most buyers start talking to an agent after they find a house. The buyers who win started 3 months earlier.",
            "CTA: DM me 'READY' if you want to start the conversation now — before the next home you love hits Rightmove.",
        ]),
        ("Framework 3 — Storytelling (Problem → Journey → Resolution → Lesson)", [
            "Example 1 (Business Coach):",
            "Hook: In 2021 I had 3 clients, €800/month in revenue, and was working 70-hour weeks.",
            "Body: I thought more hours meant more money. I was wrong. The turning point came when I had to cancel a client call because I was too exhausted to think straight. That was the moment I realized I wasn't running a business — I was just doing a really stressful job for myself. I spent the next 3 months rebuilding everything: my offers, my pricing, my processes. I fired 2 clients who were taking 80% of my time for 30% of my revenue. Six months later: 7 clients, €8,500/month, 35-hour weeks.",
            "CTA: The strategy I used is in my free guide — link in bio. If you're in the 70-hour-week trap right now, you need it.",
        ]),
        ("50 High-Converting Hook Templates by Category", [
            "Curiosity Hooks:",
            ("•", "The [number] things I wish someone told me before [common mistake]"),
            ("•", "Nobody talks about this part of [topic], but they should."),
            ("•", "Here's what really happens when you [action]."),
            ("•", "This [time] I made a decision that changed everything."),
            ("•", "The [industry] strategy that [big brands] don't want you to know."),
            "Value Hooks:",
            ("•", "[Number] ways to [achieve desired outcome] in [timeframe]."),
            ("•", "The [word] framework I use to [do something valuable]."),
            ("•", "Save this post. You will thank yourself later."),
            ("•", "Free [resource type] for every [target audience] — drop [word] in the comments."),
            ("•", "The only [topic] guide you will ever need."),
            "Emotional Hooks:",
            ("•", "If you have ever felt like [common frustration], this is for you."),
            ("•", "I used to be [current negative state]. Here's how I changed it."),
            ("•", "This is the thing no one tells you about [aspirational outcome]."),
            ("•", "Not every [target audience] will understand this. But you might."),
            ("•", "The moment I stopped [bad habit] was the moment everything changed."),
        ]),
        ("Call-to-Action Templates", [
            ("•", "Drop a [emoji] in the comments if this resonates with you."),
            ("•", "Save this for the next time you [common situation]."),
            ("•", "Tag someone who needs to hear this today."),
            ("•", "DM me [WORD] and I will send you [free resource]."),
            ("•", "Click the link in bio to [specific action]."),
            ("•", "Follow for more [content type] every [posting day]."),
            ("•", "What's your experience with [topic]? Tell me in the comments."),
            ("•", "Share this with [target audience] who needs this today."),
            ("•", "Book your free [consultation/call/audit] — link in bio."),
            ("•", "Comment your biggest challenge with [topic] and I will personally respond."),
        ]),
    ])

doc(p05+"Hashtag_Strategy_Guide.docx",
    "Hashtag Strategy Guide",
    "Ultimate AI SMMA OS | Research Methodology and Platform-Specific Best Practices",
    [
        ("Why Hashtag Strategy Still Matters in 2024-2025", [
            "Despite algorithm changes and platform shifts, hashtags remain one of the most accessible organic reach tools available to SMMA clients who do not have large ad budgets. The key change is that quality over quantity is now critical — Instagram and TikTok's algorithms prioritize relevance over volume. This guide teaches you the modern, research-driven approach to hashtag strategy.",
        ]),
        ("The 4-Tier Hashtag Mix Strategy", [
            "For every piece of content, use a balanced mix of hashtags across four tiers:",
            "Tier 1 — Mega Hashtags (20% of your hashtags): 1M+ posts",
            ("•", "These reach large audiences but have extreme competition. Use for brand awareness, not discoverability."),
            ("•", "Examples: #marketing, #socialmedia, #business, #entrepreneur"),
            "Tier 2 — Macro Hashtags (30% of your hashtags): 100K-1M posts",
            ("•", "Large enough to have active audiences, competitive enough to still be seen."),
            ("•", "Examples: #socialmediastrategy, #digitalmarketing, #contentcreation"),
            "Tier 3 — Mid-Range Hashtags (30% of your hashtags): 10K-100K posts",
            ("•", "The sweet spot. Targeted enough to reach your ideal audience, low enough competition to be seen."),
            ("•", "Examples: #restaurantmarketing, #fitnessbrandbuilding, #smmabusiness"),
            "Tier 4 — Niche Hashtags (20% of your hashtags): Under 10K posts",
            ("•", "Highly specific. Your ideal follower definitely uses these. Lower reach but highest engagement rate."),
            ("•", "Examples: #[yourcity]restaurant, #onlinecoachforwomen, #localfitnesstrainer"),
        ]),
        ("Hashtag Research Methodology", [
            "Step 1 — Start With Your Niche Keyword:",
            ("•", "Search '[niche] + [your service]' on Instagram (e.g., 'restaurant social media')"),
            ("•", "Note the suggested hashtags and post counts"),
            "Step 2 — Analyze Competitor Hashtags:",
            ("•", "Find 5 accounts in your client's niche with strong engagement"),
            ("•", "Review their last 10 posts and record all hashtags used"),
            ("•", "Identify hashtags appearing in 3+ top-performing posts"),
            "Step 3 — Build Your Hashtag Bank:",
            ("•", "Compile 50-100 hashtags per niche per platform"),
            ("•", "Organize them by the 4-tier system above"),
            ("•", "Store in Content_Calendar_Tracker.xlsx Hashtag Bank tab"),
            "Step 4 — Rotate and Test:",
            ("•", "Never use the exact same hashtag set twice in a row — Instagram may flag this as spam"),
            ("•", "Create 3-4 hashtag sets that you rotate monthly"),
            ("•", "Track which sets correlate with higher reach in monthly reports"),
        ]),
        ("Platform-Specific Rules", [
            "Instagram:",
            ("•", "Posts: 5-15 hashtags is optimal (Instagram officially recommends this over the old 30-hashtag approach)"),
            ("•", "Reels: 3-5 focused hashtags — Reels get distributed by content/topic signal more than hashtags"),
            ("•", "Stories: 1-3 hashtags maximum — place in a small area and cover with a sticker"),
            ("•", "Avoid banned hashtags — check bannedhashtags.com before building your bank"),
            "TikTok:",
            ("•", "3-5 hashtags maximum — one broad, one niche, one trending challenge if relevant"),
            ("•", "#fyp, #foryou, #viral are low value — TikTok distributes by engagement, not hashtags"),
            ("•", "Use hashtags that describe your video content — TikTok's algorithm uses them as signals"),
            "LinkedIn:",
            ("•", "3-5 hashtags at the end of posts — use professional industry terms"),
            ("•", "LinkedIn suggests hashtags as you write — check their recommendation"),
            ("•", "Create a branded hashtag for thought leadership content"),
            "Twitter/X:",
            ("•", "1-2 hashtags maximum — native Twitter culture dislikes heavy hashtag use"),
            ("•", "Use trending hashtags only when directly relevant to the tweet content"),
        ]),
    ])

doc(p05+"AI_Prompt_Library.docx",
    "AI Prompt Library — 200 Tested Prompts for SMMA",
    "Ultimate AI SMMA OS | ChatGPT and Claude Prompts for Every Agency Workflow",
    [
        ("How to Use This Prompt Library", [
            "These 200 prompts are organized by use case and designed specifically for social media marketing agency workflows. Every prompt uses the context-framing approach: you tell the AI who it is, what you need, and what format to use. Replace all [bracketed text] with your specific details before using.",
        ]),
        ("SECTION A: Caption Writing Prompts (40 Prompts)", [
            "CA-1: AIDA Caption Framework:",
            '"Write 3 Instagram captions for [CLIENT NAME], a [NICHE] business, using the AIDA framework (Attention, Interest, Desire, Action). The post is about [TOPIC]. Target audience: [AUDIENCE]. Brand voice: [VOICE - e.g., professional but friendly]. Include a strong hook, body that educates or inspires, and a clear CTA. Format: hook, 3-5 short paragraphs, CTA. Length: 150-200 words each."',
            "CA-2: PAS Caption Framework:",
            '"Write a PAS-framework Instagram caption for [CLIENT NAME]. Problem: [specific problem their audience faces]. Agitate: [make them feel the pain of not solving it]. Solution: [how client solves it]. Brand voice: [VOICE]. Topic: [TOPIC]. CTA at the end. Max 200 words."',
            "CA-3: Story-Driven Caption:",
            '"Write a storytelling-style Instagram caption for [CLIENT]. The story follows this arc: (1) Problem/challenge: [describe], (2) Turning point: [describe], (3) Outcome/result: [describe], (4) Lesson/CTA. Brand voice: [VOICE]. First line must be a scroll-stopper hook. 200-250 words."',
            "CA-4: Educational Carousel Caption:",
            '"Write an Instagram caption for a [NUMBER]-slide carousel on the topic [TOPIC] for [CLIENT NAME] in the [NICHE] industry. Caption should tease all [NUMBER] points to create curiosity. Use the hook \'Save this before you scroll past\'. End with a CTA to share or comment. Brand voice: [VOICE]."',
            "CA-5: Quick Tip Caption:",
            '"Write 5 different short Instagram captions (under 80 words each) for [CLIENT NAME] sharing a quick actionable tip about [TOPIC]. Each should have a different hook style: question, bold statement, number, warning, and secret. Target: [AUDIENCE]. CTA: Follow for daily [topic] tips."',
            "CA-6: Product Feature Caption (E-Commerce):",
            '"Write a product-focused Instagram caption for [PRODUCT NAME] by [CLIENT NAME]. Benefits to highlight: [list 3 benefits]. Price: [PRICE]. Target customer: [AUDIENCE DESCRIPTION]. Tone: [VOICE]. Include a CTA to shop now with a sense of urgency. 100-150 words."',
            "CA-7: Behind-the-Scenes Caption:",
            '"Write a behind-the-scenes Instagram caption for [CLIENT NAME], a [NICHE] business. They want to show [SPECIFIC BTS ACTIVITY - e.g., morning prep, team meeting, product creation]. Goal: humanize the brand and build connection. Voice: [VOICE]. 100-120 words. End with a question to prompt comments."',
            "CA-8: Client Testimonial Reshare Caption:",
            '"Rewrite this client review for [CLIENT NAME]\'s social media. Original review: \'[PASTE REVIEW]\'. Create a caption that amplifies the review emotionally, adds brief context, and includes a CTA for new clients to get started. Brand voice: [VOICE]. 80-120 words."',
            "CA-9: Seasonal / Trending Caption:",
            '"Write 3 Instagram captions for [CLIENT NAME] relevant to [SEASON/HOLIDAY/TREND]. Tie in their business in a natural way — not forced. Target: [AUDIENCE]. Brand voice: [VOICE]. Make each one a different emotional tone: warm/nostalgic, energetic/celebratory, and valuable/educational."',
            "CA-10: Competitor Differentiation Caption:",
            '"Write an Instagram caption for [CLIENT NAME] that explains what makes them different from typical [niche] businesses without naming competitors. Key differentiators: [list 2-3]. Voice: [VOICE]. Should feel confident without being arrogant. 100-150 words."',
            "CA-11: Myth-Busting Caption:",
            '"Write a myth-busting Instagram caption for [CLIENT NAME] in the [NICHE] space. Myth to bust: [COMMON MISCONCEPTION]. Explain why it\'s wrong and what the truth is. Make the myth the hook. Voice: [VOICE]. 150-180 words. CTA: What myth do you wish people knew about [topic]?"',
            "CA-12: FAQ-Style Caption:",
            '"Write an Instagram caption for [CLIENT NAME] answering the FAQ: [SPECIFIC QUESTION THEIR CUSTOMERS ASK]. Answer should be direct, educational, and build trust. Voice: [VOICE]. 100-130 words. End with \'What other questions do you have?\'"',
            "CA-13: Transformation / Before-After Caption:",
            '"Write an Instagram caption for [CLIENT NAME] highlighting a client transformation. Before state: [DESCRIBE]. After state: [DESCRIBE]. Process: [BRIEF HOW]. Make the reader feel what it\'s like to experience this transformation. CTA: DM to start your journey. 150-200 words."',
            "CA-14: Industry News Commentary Caption:",
            '"Write an Instagram caption for [CLIENT NAME] reacting to this industry news: [NEWS/TREND]. Their opinion should be: [AGREE/DISAGREE/NUANCED]. Voice: [VOICE]. Position them as a thought leader. End with a question to spark debate. 120-150 words."',
            "CA-15: Event Announcement Caption:",
            '"Write an Instagram caption announcing [EVENT TYPE - e.g., webinar, launch, sale, workshop] for [CLIENT NAME]. Event name: [NAME]. Date/time: [DATE]. What attendees/buyers get: [BENEFIT]. Create urgency with limited spots/time. CTA: Link in bio. 100-130 words."',
        ]),
        ("SECTION B: Hook Writing Prompts (30 Prompts)", [
            "HK-1: Generate 15 unique scroll-stopping hooks for Instagram posts about [TOPIC] targeting [AUDIENCE]. Include hooks in these styles: bold statement (3), question (3), number list (3), 'nobody talks about this' (2), story opener (2), controversial take (2). Rate each hook 1-10 for expected engagement.",
            "HK-2: Write 10 hooks for a Reel about [TOPIC] for [CLIENT]. The hook must work as both an on-screen text overlay AND as the opening line of the caption. Each should be under 10 words. Make the viewer ask 'wait, what?' within 0.5 seconds.",
            "HK-3: I need 5 hooks that create immediate curiosity about [TOPIC] without revealing the answer. Use cliffhanger style. Target: [AUDIENCE]. The hook should make scrolling past feel like leaving money on the table.",
            "HK-4: Write 8 educational hooks for [NICHE] content that position [CLIENT NAME] as an expert without sounding boastful. They should feel like an insider is sharing something only they know.",
            "HK-5: Generate 10 emotional hooks about [PAIN POINT] that make [TARGET AUDIENCE] feel deeply understood. The hooks should trigger the thought 'This is exactly how I feel!' First 10 words must land the emotion.",
        ]),
        ("SECTION C: Content Ideas Prompts (30 Prompts)", [
            "CI-1: Generate a 30-day content calendar for [CLIENT NAME], a [NICHE] business. Include: daily post type (Reel, carousel, static, story), topic, format notes, and CTA. Align with these content pillars: [LIST 3-5 PILLARS]. Make each week have a unifying theme. Use a table format: Day | Post Type | Topic | Caption Hook | CTA.",
            "CI-2: Give me 20 Reel ideas for [CLIENT NAME] in the [NICHE] space. For each: hook, concept (1 sentence), expected primary emotion (funny/inspiring/educational/surprising), and ideal duration (15/30/60 seconds).",
            "CI-3: I run a social media agency serving [NICHE] businesses. Generate 15 content ideas that would resonate with [TARGET AUDIENCE PERSONA: describe in detail]. Each idea should make them stop scrolling because it speaks directly to their daily life or pain point.",
            "CI-4: Create a \'Content Pillar Content Map\' for [CLIENT NAME] with 5 pillars. For each pillar: 4 post ideas, the content format that works best, the emotional hook to use, and the audience this pillar specifically speaks to.",
            "CI-5: What are 10 trending content formats on Instagram and TikTok right now that could be adapted for [NICHE] clients? For each format: describe what it is, why it works, how to adapt for [NICHE], and provide a specific example.",
        ]),
        ("SECTION D: Email and DM Scripts (25 Prompts)", [
            "EM-1: Write a cold outreach email for my social media agency targeting [NICHE] business owners. Agency name: [NAME]. Services: [LIST]. Unique value: [UVP]. Tone: [VOICE]. Subject line included. Max 150 words. End with a low-commitment CTA (quick call or free audit).",
            "EM-2: Write a cold DM script for Instagram targeting [NICHE] business owners. Max 120 characters. Must: feel personal (not templated), mention something specific about their business, ask a single question that qualifies them. Three variations: curious, direct, value-first.",
            "EM-3: Write a 5-email follow-up sequence for leads who requested but did not attend a discovery call. Voice: [VOICE]. Email 1 (immediate): simple reschedule. Email 2 (Day 3): share a relevant case study. Email 3 (Day 7): a quick tip relevant to their niche. Email 4 (Day 14): a free resource. Email 5 (Day 21): breakup email.",
            "EM-4: Write a monthly check-in email from [AGENCY NAME] to client [CLIENT NAME] summarizing this month\'s wins and previewing next month\'s strategy. Wins: [LIST METRICS]. Next month focus: [FOCUS]. Tone: confident, warm, forward-looking. Max 200 words.",
            "EM-5: Write a proposal follow-up email for a prospect who received our SMMA proposal 3 days ago and has not responded. Agency: [NAME]. Proposal value: €[AMOUNT]. Goal: re-open the conversation without being pushy. Include a risk-reversal element. Max 120 words.",
        ]),
        ("SECTION E: Ad Copy Prompts (20 Prompts)", [
            "AD-1: Write 5 Facebook/Instagram ad headlines (under 40 characters each) for [CLIENT NAME] in the [NICHE] space promoting [OFFER]. Target: [AUDIENCE]. Each headline should have a different angle: curiosity, benefit, social proof, urgency, and question.",
            "AD-2: Write a Facebook ad primary text for [CLIENT NAME] promoting [OFFER/SERVICE]. Audience: [TARGET]. Pain point to address: [PAIN POINT]. Unique angle: [ANGLE]. Format: hook + 2-3 short paragraphs + CTA. Max 125 words (before truncation). Include social proof if possible.",
            "AD-3: Write 5 TikTok ad script concepts (15-30 seconds each) for [CLIENT NAME] selling [PRODUCT/SERVICE]. Each concept: hook (first 3 seconds), content (middle 10-20 seconds), CTA (final 3 seconds). Focus on pattern-interrupt and authentic feel. Target: [AUDIENCE].",
            "AD-4: Create a LinkedIn ad copy set for [CLIENT NAME] targeting [JOB TITLE/INDUSTRY]. Headline + 150-character description + body copy (under 600 characters). Objective: lead generation for [SERVICE]. Professional tone. Include a direct value proposition.",
            "AD-5: Write 3 ad creative concepts for a retargeting campaign for [CLIENT NAME]. These are for people who visited the website but did not convert. Include: objection-handling angle, social proof angle, and urgency angle. Each: headline + body (100 words) + CTA.",
        ]),
        ("SECTION F: Strategy Prompts (20 Prompts)", [
            "ST-1: Build a 90-day Instagram growth strategy for [CLIENT NAME], a [NICHE] business with [X] current followers, [Y]% engagement rate, and a goal of [GOAL]. Include: content frequency, content type breakdown, engagement strategy, hashtag approach, collaboration/growth tactics, and monthly milestones.",
            "ST-2: Analyze this Instagram account and give me a detailed growth strategy: [describe or paste account metrics]. Current weakness areas: [describe]. Target audience: [describe]. Goal: [goal]. Give me specific, actionable recommendations in the areas of: posting schedule, content types, engagement strategy, and hashtag approach.",
            "ST-3: I\'m pitching a new [NICHE] client at [PRICE/MONTH]. Help me create a compelling discovery call script focused on their biggest pain points. They currently have: [current situation]. Our services include: [list]. Build a 10-question discovery framework that positions our agency as the obvious solution.",
            "ST-4: Create a social media content audit framework I can use for every new client. Include: what to measure, how to benchmark against competitors, how to identify the top 3 opportunities, and how to present findings in a client-friendly way.",
            "ST-5: I want to create a \'signature content system\' for my SMMA that I can replicate across all [NICHE] clients. Build me a system with: 5 content pillars for this niche, optimal posting frequency per platform, the 3 content formats that drive the most engagement in this niche, and a repeatable monthly content theme structure.",
        ]),
        ("SECTION G: Reporting and Analytics Prompts (15 Prompts)", [
            "RP-1: Write an executive summary for a monthly social media report for [CLIENT NAME]. Metrics this month: Followers: [X] (+[Y]%). Engagement rate: [Z]%. Reach: [N]. Top post: [DESCRIBE]. Write 3 paragraphs: what we achieved, what we learned, what we'll do next month. Tone: confident and forward-looking.",
            "RP-2: I need to explain to a non-marketing client why their engagement rate dropping from 4.2% to 3.1% while their reach increased from 5,000 to 22,000 is actually a positive sign. Write a clear explanation a business owner without marketing knowledge can understand and find reassuring.",
            "RP-3: Generate 5 insights from this data: [paste your monthly analytics data]. Frame each insight as: what happened, why it likely happened, and what action to take next month. Use simple language suitable for a client report.",
            "RP-4: Write a monthly client email update for [CLIENT NAME] sharing their social media performance. Keep it under 200 words. Metrics to reference: [paste metrics]. Tone: excited about wins, honest about challenges, clear on next steps.",
            "RP-5: Help me explain to a client why we are focusing on save rate and share rate instead of likes as our success metrics. Write 2 paragraphs that I can include in our monthly report to educate and align expectations.",
        ]),
        ("SECTION H: Miscellaneous Agency Prompts (20 Prompts)", [
            "MS-1: Write a professional agency bio for [AGENCY NAME] for the About section of our website. Services: [LIST]. Niche: [NICHE]. Founded: [YEAR]. Key differentiator: [DIFFERENTIATOR]. Tone: [VOICE]. 150-200 words. First sentence must hook a potential client.",
            "MS-2: Write 5 LinkedIn posts for the owner of [AGENCY NAME] to establish thought leadership in the SMMA space. Topics: lessons learned running an agency, mistakes to avoid, client results, industry opinions, and a personal story. Each 200-250 words. Professional but personal tone.",
            "MS-3: Create a client retention script for a client who mentions they are thinking about pausing services due to budget. Goal: understand the real reason, reassure, and offer a solution that keeps them without discounting below our minimum. Keep our value intact. 10-15 exchange script.",
            "MS-4: Write an agency case study template for a [NICHE] client who achieved [RESULT] in [TIMEFRAME]. Include: client background, challenge before, strategy we implemented, results achieved, client quote, and call-to-action. Suitable for a website page or PDF.",
            "MS-5: I need to onboard a new freelance content creator to my SMMA team. Write a comprehensive brief template I can fill in for each client they work on. Include: client overview, brand voice, platform specs, content pillars, hashtag rules, revision process, deadlines, and quality standards.",
        ]),
    ])

doc(p05+"Visual_Content_Brief_Template.docx",
    "Visual Content Brief Template",
    "Ultimate AI SMMA OS | Design Brief for Graphics, Videos, and Branded Content",
    [
        ("How to Use This Brief", [
            "This template is used to brief designers, Canva creators, or video editors on visual content for your SMMA clients. Complete a new brief for each client at onboarding and update it quarterly. Share with any team member or freelancer working on the client's account.",
        ]),
        ("CLIENT INFORMATION", [
            "[FILL IN] Client Name: _______________",
            "[FILL IN] Industry/Niche: _______________",
            "[FILL IN] Primary Platform(s): _______________",
            "[FILL IN] Target Audience Description: _______________",
        ]),
        ("BRAND IDENTITY", [
            "[FILL IN] Primary Color (hex): _______________ | Secondary Color (hex): _______________",
            "[FILL IN] Accent Color (hex): _______________ | Background Color (hex): _______________",
            "[FILL IN] Primary Font (headlines): _______________",
            "[FILL IN] Secondary Font (body text): _______________",
            "[FILL IN] Logo: [Attach PNG + SVG files]",
            "[FILL IN] Overall visual style: (Circle one) Minimalist / Bold / Elegant / Playful / Industrial / Organic / Modern",
            "[FILL IN] Color personality: (Circle one) Warm and inviting / Cool and professional / Vibrant and energetic / Dark and luxurious",
        ]),
        ("PLATFORM DIMENSION SPECIFICATIONS", [
            "Instagram Feed Post (Square): 1080 x 1080 px (1:1 ratio)",
            "Instagram Feed Post (Portrait): 1080 x 1350 px (4:5 ratio — recommended for maximum screen space)",
            "Instagram Reel / TikTok / YouTube Short: 1080 x 1920 px (9:16 ratio)",
            "Instagram Story: 1080 x 1920 px (9:16 ratio)",
            "LinkedIn Post: 1080 x 1080 px (1:1) or 1200 x 628 px (landscape for link posts)",
            "Facebook Post: 1080 x 1080 px (1:1) or 1200 x 630 px",
            "Twitter/X Header: 1500 x 500 px | Profile: 400 x 400 px",
        ]),
        ("CONTENT DO'S", [
            "[FILL IN — Examples below, customize per client]",
            ("•", "DO use the brand's exact hex colors — no color approximations"),
            ("•", "DO include the logo on every piece of content (corner watermark or branded footer)"),
            ("•", "DO use real photography when available — stock photos only as last resort"),
            ("•", "DO leave safe zones (10% margin) on all sides — especially for Stories"),
            ("•", "DO make text readable at mobile size — minimum 24pt for body, 40pt for headlines"),
            ("•", "DO use on-brand lifestyle imagery that reflects the target customer's world"),
        ]),
        ("CONTENT DON'TS", [
            "[FILL IN — Examples below, customize per client]",
            ("•", "DON'T use clip art or obvious low-quality stock photography"),
            ("•", "DON'T use fonts outside the approved brand fonts without approval"),
            ("•", "DON'T add too much text to a single slide — 30% text, 70% visual rule"),
            ("•", "DON'T use dark backgrounds with dark text — ensure high contrast"),
            ("•", "DON'T center-align body text on graphic-heavy posts — use left align for readability"),
        ]),
        ("VIDEO SPECIFICATIONS", [
            "[FILL IN] Reel/TikTok average length: _______________ seconds",
            "[FILL IN] Intro style: (e.g., text hook on screen, face to camera, B-roll with voiceover): _______________",
            "[FILL IN] Outro: (e.g., CTA card, logo reveal, subscribe reminder): _______________",
            "[FILL IN] Music: (licensed stock music / trending audio / client-provided / no music): _______________",
            "[FILL IN] Captions/subtitles: YES / NO — Font and color: _______________",
            "Video export specifications: MP4, minimum 1080p, under 350MB for Instagram, under 287.6MB for TikTok",
        ]),
    ])

print("✓ 05_CONTENT_CREATION complete")

# ─── 06_SOCIAL_MEDIA_MANAGEMENT ────────────────────────────────────────────────
p06 = "06_SOCIAL_MEDIA_MANAGEMENT/"

doc(p06+"Instagram_Strategy_Guide.docx",
    "Instagram Strategy Guide",
    "Ultimate AI SMMA OS | Reels, Carousels, Stories, DM Strategy, and Growth Tactics",
    [
        ("Why Instagram Remains the Core Platform for Most SMMA Clients (2024-2025)", [
            "Despite competition from TikTok and the evolution of every major platform, Instagram continues to deliver the highest conversion rates for local businesses, coaches, consultants, and e-commerce brands. Its combination of visual storytelling, short-form video, direct messaging, and shopping features makes it uniquely positioned as both a brand-building and revenue-generating platform. This guide covers the complete Instagram management strategy.",
        ]),
        ("Instagram Algorithm Fundamentals", [
            ("•", "The Instagram algorithm distributes content based on six signals: Interest, Recency, Relationship, Frequency, Following count, and Usage patterns"),
            ("•", "Reels get the most reach to non-followers (discovery content)"),
            ("•", "Carousels and static posts get shown most to existing followers (retention content)"),
            ("•", "Stories are shown primarily to engaged existing followers (loyalty content)"),
            ("•", "Saves and shares are weighted more heavily than likes and comments"),
            ("•", "Early engagement velocity (engagement in first 30-60 minutes) determines post distribution"),
        ]),
        ("Reels Strategy — The Discovery Engine", [
            "Optimal Reel Structure:",
            ("•", "Seconds 0-3: Hook — on-screen text or spoken line that stops scrolling"),
            ("•", "Seconds 3-20: Content delivery — teach, entertain, or inspire"),
            ("•", "Final 5 seconds: CTA — verbal or text overlay directing action"),
            "Reel Content Types That Work:",
            ("•", "Educational Quick Tips: '3 things every [niche] needs to know about [topic]'"),
            ("•", "Behind-the-Scenes: Process videos, team moments, day in the life"),
            ("•", "Before/After: Transformation reveals (applicable to almost any niche)"),
            ("•", "Opinion Piece: Controversial or contrarian take in your niche"),
            ("•", "Trend Adaptation: Take a trending audio or format and apply it to your niche"),
            "Reel Optimization Checklist:",
            ("•", "Caption written before posting (keyword-rich first 2 lines)"),
            ("•", "Cover image chosen (not auto-generated) — should work as a static image"),
            ("•", "Hashtags added (3-5 niche-relevant hashtags)"),
            ("•", "Location tag added for local businesses"),
            ("•", "Shared to Stories immediately after posting"),
        ]),
        ("Carousel Strategy — The Depth Content Engine", [
            "Why Carousels: They get 3x more engagement than static posts and trigger the algorithm's 'multiple interactions per post' signal as users swipe.",
            "Optimal Carousel Structure (7-10 slides):",
            ("•", "Slide 1: Strong hook image + statement that creates curiosity or promises value"),
            ("•", "Slides 2-6: The value content — one point per slide, brief and scannable"),
            ("•", "Slide 7-8: Deeper value, supporting evidence, or alternative takes"),
            ("•", "Slide 9: Summary or key takeaway"),
            ("•", "Slide 10: CTA — follow, save, comment, or visit link"),
            "Caption for Carousels: Keep it short. The hook should reference what's inside: 'Swipe for all 7 →' works.",
        ]),
        ("Stories Strategy — The Relationship Engine", [
            "Stories are the highest-frequency, lowest-friction content format. They build the personal connection that turns followers into buyers.",
            "Weekly Stories Rhythm:",
            ("•", "Monday: Weekly intention or behind-the-scenes peek"),
            ("•", "Tuesday-Thursday: Interactive stories (polls, Q&As, sliders, quizzes)"),
            ("•", "Thursday-Friday: Product/service highlights or client showcases"),
            ("•", "Daily: Reshare content from feed to Stories + engage with followers' stories"),
            "Story Features to Use:",
            ("•", "Polls: Binary choices drive massive engagement ('A or B?', 'Yes or No?')"),
            ("•", "Question Box: 'Ask me anything about [niche]' positions client as expert"),
            ("•", "Countdown Timer: For launches, events, and promotional deadlines"),
            ("•", "Link Sticker: Direct traffic to website, booking page, or offer"),
        ]),
        ("Instagram Bio Optimization", [
            "The 5 elements of a high-converting Instagram bio:",
            ("•", "Line 1 — What you do: 'Social media strategy for [niche] businesses'"),
            ("•", "Line 2 — Who you help: '[Specific audience] grow their [outcome]'"),
            ("•", "Line 3 — Social proof or differentiator: '500+ clients | €2M in client results'"),
            ("•", "Line 4 — CTA: '⬇️ Free [RESOURCE] / Book a call / Shop our [PRODUCT]'"),
            ("•", "Link in Bio: Use Linktree or Beacons to offer multiple destinations"),
        ]),
        ("DM Strategy — Converting Followers to Clients", [
            ("•", "After someone engages with a post, DM them: 'Glad this resonated! Are you working on [related challenge]?'"),
            ("•", "After someone saves a post: DM 'Noticed you saved our [post]. Want the full breakdown?'"),
            ("•", "Story replies: Respond to every story reply within 2 hours — this is the warmest lead possible"),
            ("•", "Welcome DM to new followers (auto or manual): 'Thanks for following! Quick question — what's your biggest challenge with [niche topic] right now?'"),
        ]),
    ])

doc(p06+"LinkedIn_Strategy_Guide.docx",
    "LinkedIn Strategy Guide",
    "Ultimate AI SMMA OS | B2B Content, Thought Leadership, Company Pages, and Lead Generation",
    [
        ("LinkedIn's Unique Position in Your Client's Marketing Mix", [
            "LinkedIn is the only social media platform where professional identity is the primary user motivation. People are on LinkedIn to advance their careers, learn, network, and discover business solutions. This makes it uniquely powerful for B2B businesses, professional services, consultants, coaches, and any business where the decision-maker is a professional. The mindset required for LinkedIn success is fundamentally different from Instagram or TikTok.",
        ]),
        ("LinkedIn Algorithm Essentials", [
            ("•", "LinkedIn distributes text-based content well — long-form posts with line breaks and white space perform strongly"),
            ("•", "Dwell time (how long people spend reading) is heavily weighted"),
            ("•", "Comments trigger much more distribution than likes — prioritize content that sparks conversation"),
            ("•", "External links (website URLs) reduce post reach — mention URLs in comments instead"),
            ("•", "Document/carousel posts (PDF uploads) get high organic reach"),
            ("•", "Early engagement in the first 1-2 hours after posting determines distribution velocity"),
        ]),
        ("LinkedIn Content Pillars for B2B Clients", [
            "Pillar 1 — Industry Expertise and Insights:",
            ("•", "Data-backed opinions about trends in their industry"),
            ("•", "Contrarian takes: 'Everyone in [industry] is doing X wrong, here's why'"),
            ("•", "Predictions: What will change in [industry] in the next 12 months?"),
            "Pillar 2 — Client Success Stories and Case Studies:",
            ("•", "Problem → Strategy → Result format (numbers-driven)"),
            ("•", "Include anonymous or named client details with permission"),
            "Pillar 3 — Personal Brand and Behind-the-Scenes:",
            ("•", "Lessons learned from business experience"),
            ("•", "Personal stories tied to professional insight"),
            ("•", "Team culture and company values"),
            "Pillar 4 — Educational Value Posts:",
            ("•", "Step-by-step frameworks and processes their audience can apply immediately"),
            ("•", "Tools, resources, and recommendations"),
        ]),
        ("LinkedIn Post Formats", [
            "Text-Only Posts (Highest Organic Reach):",
            ("•", "Use line breaks and white space generously — never post a wall of text"),
            ("•", "First line is your hook — no wasted words"),
            ("•", "Keep posts to 200-500 words for maximum dwell time without losing readers"),
            "Document (PDF) Posts:",
            ("•", "Create 5-10 slide PDF carousels on educational topics"),
            ("•", "Cover slide must be visually strong — visible in the feed preview"),
            ("•", "These consistently get the highest reach and save rates on LinkedIn"),
            "Video Posts:",
            ("•", "Keep under 2 minutes — professional, talking-head style works well"),
            ("•", "Always include captions (most users watch muted at work)"),
            ("•", "Native video gets 3x more reach than YouTube links"),
            "Polls:",
            ("•", "Binary or four-option questions related to industry opinions"),
            ("•", "Run 24-hour polls for fresh, timely discussion starters"),
        ]),
        ("LinkedIn Lead Generation Strategy", [
            ("•", "Connection Building: Send 20 targeted connection requests per day to ideal client profiles"),
            ("•", "Profile Optimization: Headline should state what you do and who you help — not just your job title"),
            ("•", "Featured Section: Pin your best case study, lead magnet, or offer to top of profile"),
            ("•", "Engagement Strategy: Comment meaningfully on 5-10 posts per day from potential clients"),
            ("•", "Sales Navigator (if budget available): Advanced filtering for hyper-targeted prospect lists"),
            ("•", "LinkedIn Newsletter: Launch a niche newsletter — grows your connection list organically through subscription"),
        ]),
    ])

doc(p06+"TikTok_Strategy_Guide.docx",
    "TikTok Strategy Guide",
    "Ultimate AI SMMA OS | Hook Formula, Trending Audio, TikTok SEO, and Growth Tactics",
    [
        ("TikTok as a Business Growth Tool", [
            "TikTok is no longer just for Gen Z entertainment. It is a full-scale search engine, discovery platform, and purchase driver. TikTok's algorithm is uniquely egalitarian — a brand-new account can go viral on its first day with the right content. This makes it the highest-potential reach platform for new clients and niche businesses that would take years to grow on Instagram.",
        ]),
        ("TikTok Algorithm Fundamentals", [
            ("•", "TikTok distributes content primarily based on completion rate (what % of the video people watch)"),
            ("•", "Shares are the most powerful signal — a high share rate triggers massive distribution"),
            ("•", "Rewatches indicate high value — the algorithm notices when people replay a video"),
            ("•", "Comments signal debate/interest — controversial or question-prompting content outperforms"),
            ("•", "The For You Page (FYP) is curated by interest, not following — no follower count needed to reach millions"),
            ("•", "Posting frequency: 3-5x per week is the recommended cadence for growth"),
        ]),
        ("The TikTok Hook Formula", [
            "TikTok hooks must work within the first 0-2 seconds. The viewer's thumb is on the screen ready to swipe. You have less time here than any other platform.",
            "Hook Type 1 — Problem Declaration (Stops the scroll with immediate relevance):",
            '"If you\'re a [TARGET AUDIENCE] and you\'re still doing [WRONG THING], stop watching this and go fix it first."',
            "Hook Type 2 — Curiosity Gap:",
            '"This is the number one thing I wish someone told me about [TOPIC] — I learned it the hard way."',
            "Hook Type 3 — Surprising Statement:",
            '"[COUNTER-INTUITIVE CLAIM] — and I can prove it in 60 seconds."',
            "Hook Type 4 — Direct Address:",
            '"Hey [TARGET AUDIENCE], this one is specifically for you."',
            "Hook Type 5 — Story Opener:",
            '"The day I [DRAMATIC EVENT] changed everything about how I approach [TOPIC]."',
        ]),
        ("TikTok SEO — Getting Found Through Search", [
            "TikTok is the fastest-growing search engine for Gen Z and Millennials. 40% of Gen Z users prefer TikTok over Google for certain searches. Optimizing for TikTok search is now an essential strategy.",
            ("•", "In-Video: Say your target keywords OUT LOUD in the video — TikTok transcribes audio"),
            ("•", "Caption: Include your 2-3 primary keywords naturally in the text caption"),
            ("•", "On-Screen Text: Include keywords as text overlays — TikTok reads these"),
            ("•", "Hashtags: Use 1-2 descriptive hashtags that match what people would search"),
            ("•", "Research: Search your topic in TikTok's search bar and look at autocomplete suggestions"),
        ]),
        ("Trending Audio Strategy", [
            ("•", "Check TikTok's 'Trending' sounds section weekly — rotating every 3-7 days"),
            ("•", "When a sound is trending: Adapt it to your niche immediately while reach is high"),
            ("•", "Non-original audio performs better for reach; original audio performs better for brand identity"),
            ("•", "Duet and Stitch: Reacting to viral content in your niche establishes authority and piggybacks on existing distribution"),
        ]),
        ("TikTok Content Strategy by Niche", [
            "Restaurants / F&B:",
            ("•", "Food preparation videos (ASMR cooking, plating reveals, staff morning routines)"),
            ("•", "Behind-the-scenes kitchen content, ingredient sourcing stories"),
            "Coaches / Consultants:",
            ("•", "Quick tip format ('60-second [topic] lesson'), client transformation stories"),
            ("•", "Myth-busting content: 'Everyone in [industry] is doing this wrong'"),
            "E-commerce:",
            ("•", "Unboxing, product demos, packaging ASMR, 'I tried [product] for 30 days'"),
            ("•", "User-generated content reposts, trend-jacking with product tie-ins"),
        ]),
    ])

doc(p06+"Facebook_Strategy_Guide.docx",
    "Facebook Strategy Guide",
    "Ultimate AI SMMA OS | Groups, Business Pages, Ads, Events, and Lead Generation",
    [
        ("Facebook's Continued Importance for Local and B2C Businesses", [
            "While Facebook has ceded cultural relevance to younger platforms, it remains the largest social network by active users globally and the most powerful targeting platform for local and B2C businesses through Meta advertising. For SMMA clients targeting adults 30+, parents, homeowners, and local community members, Facebook is often the highest-ROI channel. This guide covers organic Facebook strategy alongside Meta's paid capabilities.",
        ]),
        ("Facebook Page Optimization", [
            "A fully optimized Facebook Page signals professionalism and helps with local discovery:",
            ("•", "Page Name: Exact business name — do not add keywords (Facebook penalizes this)"),
            ("•", "Category: Choose the most specific category available for your client's business"),
            ("•", "Profile Photo: Logo (minimum 180x180px, displays at 170x170px)"),
            ("•", "Cover Photo: 820x312px — use a strong visual with CTA text"),
            ("•", "About Section: Complete every field — website, hours, location, phone, description"),
            ("•", "Call-to-Action Button: Set to the most relevant action — 'Book Now', 'Call Now', 'Get Quote', 'Send Message'"),
            ("•", "Pinned Post: Pin your best performing post or a current promotion to the top of your Page"),
        ]),
        ("Facebook Content Strategy", [
            "Facebook Organic Reach Reality: Organic reach for business pages averages 2-6% of your followers. This means organic Facebook is primarily for warming existing followers and community building — not discovery. Use Facebook for:",
            ("•", "Sharing valuable long-form content (articles, guides, how-to posts) — text performs well on Facebook"),
            ("•", "Video content (Facebook Watch still drives significant views for native video)"),
            ("•", "Community engagement — responding to every comment and message"),
            ("•", "Events and local promotion"),
            "Post Frequency: 3-5 times per week for business pages",
            "Best Times: Tuesday-Thursday, 10am-3pm in the audience's timezone",
        ]),
        ("Facebook Groups Strategy", [
            "Facebook Groups have 5-10x higher organic reach than Business Pages. This makes them strategic gold for coaches, consultants, and community-driven brands.",
            ("•", "For Client Groups: Create a free community group where the client is the host and expert (e.g., 'Real Estate Investment Club with [Agent Name]', 'Healthy Cooking with [Chef Name]')"),
            ("•", "Group Content: Daily value posts, member spotlights, Q&A sessions, exclusive deals"),
            ("•", "Monetization: The group warms members for paid offers — run monthly promotions and launches to the group"),
            ("•", "Management: Set clear rules, automate welcome questions, remove spam aggressively"),
        ]),
        ("Facebook Events", [
            ("•", "Create events for every webinar, workshop, in-person event, or live stream"),
            ("•", "Invite all page followers and group members to events"),
            ("•", "Update the event daily in the week before with content, previews, and reminders"),
            ("•", "Events appear in local discovery — local businesses should use this for every promotion"),
        ]),
        ("Facebook Ads Integration (Brief Overview)", [
            ("•", "Facebook/Instagram ads run through Meta Ads Manager — same platform, different placements"),
            ("•", "Most effective for SMMA clients: Lead Generation campaigns (built-in lead forms), Traffic campaigns (drive to landing page), Conversion campaigns (purchase/booking events)"),
            ("•", "Audience targeting: Custom Audiences (website visitors, email lists), Lookalike Audiences (similar to best customers), Interest targeting"),
            ("•", "Start small: €10-20/day, test 3-5 creative variations, optimize at €100 spend per ad"),
        ]),
    ])

doc(p06+"Community_Management_SOP.docx",
    "Community Management SOP",
    "Ultimate AI SMMA OS | Response Standards, DM Scripts, Comment Management, Crisis Protocols",
    [
        ("Community Management Is Your Retention Engine", [
            "Most agencies focus on content creation and forget that social media is a two-way conversation. How you respond to comments, DMs, and reviews is as important as the content itself. Exceptional community management builds the emotional connection that turns followers into loyal, paying customers. This SOP ensures consistent, professional community management for every client.",
        ]),
        ("Response Time Standards by Package", [
            ("•", "Starter Package: Comments responded to within 24 hours, DMs within 48 hours"),
            ("•", "Growth Package: Comments within 12 hours, DMs within 24 hours"),
            ("•", "Pro Package: Comments within 6 hours, DMs within 12 hours"),
            ("•", "Elite Package: Comments within 2 hours, DMs within 4 hours (9am-8pm)"),
            ("•", "ALL packages: Urgent/negative content (complaints, PR risks) responded to within 1 hour of discovery"),
        ]),
        ("Comment Response Framework", [
            "Response Tone Categories:",
            ("•", "Positive comments/compliments: Warm, personalized, authentic — never just 'Thanks!'"),
            ("•", "Questions: Full, helpful answers — treat every question as a chance to show expertise"),
            ("•", "Negative comments: Professional, empathetic, never defensive — offer to move the conversation to DM"),
            ("•", "Spam/inappropriate: Delete without engagement"),
            "Template Responses (Always personalize with their name or something from their comment):",
            "Compliment Response: '[Name]! This comment made our day. [Personalized addition]. Thank you so much for being part of our community! 🙏'",
            "Question Response: 'Great question, [Name]! [Full answer]. If you'd like more details on this, feel free to DM us and we can go deeper! 💬'",
            "Negative Response: 'We're so sorry to hear this, [Name]. This is not the experience we want for anyone. We'd love to make this right — could you DM us with more details? We'll resolve this personally.'",
        ]),
        ("DM Management Scripts", [
            "Product/Service Inquiry DM:",
            '"Hi [Name]! Thanks for reaching out. I\'d love to help. Just to make sure I get you the best answer — could you tell me a little more about [what you need]? That way I can point you to exactly the right option. 😊"',
            "Complaint DM:",
            '"Hi [Name], we\'re so sorry you\'ve had this experience — that\'s not our standard at all and I completely understand your frustration. Can you share a little more about what happened? I want to make sure we fix this for you personally and quickly."',
            "After Resolving a Complaint:",
            '"[Name], thank you so much for your patience while we sorted this out. I hope the solution we\'ve offered makes up for the experience. If there\'s anything else I can do for you, please don\'t hesitate to reach out directly."',
        ]),
        ("Crisis Management Protocol", [
            "A social media 'crisis' is any situation that involves negative sentiment spreading rapidly and has the potential to damage the client's reputation. Common crises: a bad review going viral, a staff incident caught on camera, a misjudged post, or a PR scandal.",
            "Step 1 — Identify (Within 30 Minutes):",
            ("•", "Alert client immediately — never handle a crisis without the client's knowledge"),
            ("•", "Document the original post/comment that triggered the crisis"),
            ("•", "Assess: What is the nature of the criticism? Is it factual? Emotional? Coordinated?"),
            "Step 2 — Respond (Within 1 Hour):",
            ("•", "Acknowledge: Never ignore. Silence amplifies crisis."),
            ("•", "Pause scheduled content: Turn off all scheduled posts until the situation is resolved"),
            ("•", "Public statement: Brief, empathetic, non-defensive response on the platform where the crisis originated"),
            "Step 3 — Resolve (Within 24 Hours):",
            ("•", "Take conversation to DM for resolution"),
            ("•", "Work with client on any necessary operational changes"),
            ("•", "If factually false: Politely clarify with evidence"),
            ("•", "If true: Acknowledge, apologize genuinely, explain what will change"),
            "Step 4 — Recovery (Next 7 Days):",
            ("•", "Resume content with positive, community-focused posts"),
            ("•", "Monitor for ongoing negative sentiment"),
            ("•", "Document the crisis for future reference and process improvement"),
        ]),
    ])

# Content Calendar Tracker XLSX
wb2 = Workbook()

# Sheet 1: Annual Calendar
ws1 = wb2.active
ws1.title = "Annual Calendar"
ws1.append(["ANNUAL CONTENT THEMES CALENDAR — [YEAR]"])
ws1["A1"].font = Font(bold=True, size=14, color=NAV)
ws1.append([""])
ac_headers = ["Month","Primary Theme","Secondary Theme","Key Events/Holidays",
              "Campaign Focus","Target Platform","Content Volume Target","Notes"]
ws1.append(ac_headers)
for cell in ws1[3]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

ac_data = [
    ["January","New Year, Fresh Start","Education / How-To","New Year's Day, Resolutions","Launch Campaign or Service Intro","Instagram + LinkedIn","24 posts","High motivation month for audience"],
    ["February","Love and Connection","Community Spotlight","Valentine's Day","Valentine's Campaign or Gift Guide","Instagram + Facebook","22 posts","Great for e-commerce, restaurants, coaches"],
    ["March","Growth and Momentum","Industry Insights","International Women's Day","Spring Launch or Q1 Review","LinkedIn + Instagram","24 posts","B2B audience very active"],
    ["April","Spring Energy","Transformation Stories","Easter, Earth Day","Spring Promotion or Refresh","Instagram + TikTok","22 posts","Visual content performs well"],
    ["May","Achievement and Progress","Expert Positioning","Labour Day, Mother's Day","Mother's Day Campaign or Milestone","Instagram + Facebook","24 posts","High engagement month"],
    ["June","Midyear Review","Community and Events","Summer Solstice, Pride Month","Midyear Sale or Review Content","All Platforms","24 posts","Summer content begins"],
    ["July","Summer Energy","Authenticity BTS","Independence Day (US)","Summer Campaign or Free Content","Instagram + TikTok","20 posts","Slightly lower engagement — fun content works"],
    ["August","Preparation","Education","Back to School","Back to School/Business Campaign","LinkedIn + Instagram","22 posts","Great for coaches, education, B2B"],
    ["September","Q4 Kickoff","Industry Trends","Labour Day (US/CA)","Q4 Preparation Content","LinkedIn + Instagram","24 posts","Strong B2B month"],
    ["October","Depth and Value","Client Results","Halloween","Halloween Campaign or Case Studies","Instagram + Facebook","22 posts","Creative opportunities high"],
    ["November","Gratitude","Business Review","Thanksgiving, Black Friday","BFCM Campaign or Year-in-Review","All Platforms","28 posts","Highest commercial month"],
    ["December","Celebration","Year-End","Christmas, New Year's Eve","Holiday Campaign + 2026 Preview","Instagram + Facebook","20 posts","Warm content, lower posting frequency okay"],
]
for i, row in enumerate(ac_data):
    ws1.append(row)
    for cell in ws1[i+4]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",12),("B",22),("C",22),("D",25),("E",28),("F",18),("G",20),("H",30)]:
    ws1.column_dimensions[col].width = w

# Sheet 2: Monthly Planner
ws2 = wb2.create_sheet("Monthly Planner")
ws2.append(["MONTHLY CONTENT PLANNER — [Month Year] | Client: [Client Name]"])
ws2["A1"].font = Font(bold=True, size=14, color=NAV)
ws2.append([""])
mp_headers = ["Date","Day","Platform","Post Type","Content Topic / Hook","Caption Status",
              "Design Status","Approval","Scheduled?","Published?","Notes"]
ws2.append(mp_headers)
for cell in ws2[3]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=10)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

mp_data = [
    ["2025-01-06","Mon","Instagram","Reel","Hook: '3 things every [niche] owner needs to know in 2025'","DRAFT","DESIGN PENDING","NOT SENT","NO","NO","Educational reel — high reach potential"],
    ["2025-01-07","Tue","LinkedIn","Text Post","Opinion: 'Why most [niche] businesses will fail at social media this year'","DONE","N/A — Text","APPROVED","YES","YES","Strong engagement — 42 comments"],
    ["2025-01-08","Wed","Instagram","Carousel","'The 5 biggest social media mistakes [niche] businesses make'","DONE","DONE","APPROVED","YES","YES","Best performing carousel of Jan"],
    ["2025-01-09","Thu","Facebook","Video","BTS video: day in the life at [Client Business]","SCRIPT DONE","EDITING","NOT SENT","NO","NO","Client to record Thursday morning"],
    ["2025-01-10","Fri","Instagram","Story Set","Weekend promo reveal + poll: 'Saturday or Sunday visit?'","DONE","DONE","APPROVED","YES","NO","Schedule for 10am Friday"],
    ["2025-01-13","Mon","TikTok","TikTok","'The [niche] secret nobody talks about' — trending audio adapted","IN PROGRESS","DESIGN PENDING","NOT SENT","NO","NO","Use trending audio #[AUDIO NAME]"],
    ["2025-01-14","Tue","Instagram","Static","Client testimonial: [Client Name] result highlight","DONE","DONE","APPROVED","YES","YES","Strong social proof post"],
    ["2025-01-15","Wed","LinkedIn","Document","PDF Carousel: '5 steps to [desirable outcome] for [niche]'","DONE","DONE","APPROVED","YES","YES","1,200 impressions in 24 hours"],
]
for i, row in enumerate(mp_data):
    ws2.append(row)
    for cell in ws2[i+4]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",12),("B",8),("C",14),("D",14),("E",38),("F",16),("G",16),("H",14),("I",12),("J",12),("K",28)]:
    ws2.column_dimensions[col].width = w

# Sheet 3: Content Library
ws3 = wb2.create_sheet("Content Library")
cl_headers = ["Content ID","Client","Platform","Type","Topic/Hook","Caption (Brief)","Hashtag Set",
              "Visuals","Status","Scheduled Date","Published Date","Engagement","Reuse Potential"]
ws3.append(cl_headers)
for cell in ws3[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=10)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

cl_data = [
    ["CON-001","[Client A]","Instagram","Reel","'The #1 mistake [niche] owners make'","Hook about common mistake, CTA to follow","Set A — Mid-Range","Reel video file","Published","2025-01-06","2025-01-06","348 likes, 42 comments, 891 saves","HIGH — evergreen topic"],
    ["CON-002","[Client A]","LinkedIn","Text Post","Industry opinion on trends","250-word opinion piece","Set B — Professional","N/A — text only","Published","2025-01-07","2025-01-07","1,240 impressions, 44 reactions, 17 comments","MEDIUM — repost Q3"],
    ["CON-003","[Client A]","Instagram","Carousel","'5 biggest mistakes' — educational","Swipe for all 5 →","Set C — Educational","10-slide Canva carousel","Published","2025-01-08","2025-01-08","211 likes, 687 saves, 33 shares","HIGH — best performer"],
    ["CON-004","[Client B]","TikTok","Video","BTS morning prep routine","Day in my [niche] life...","Set D — TikTok niche","MP4 video file","Scheduled","2025-01-22","—","—","TBD"],
    ["CON-005","[Client B]","Instagram","Static","Client testimonial graphic","[Client] achieved X in Y days...","Set E — Social Proof","Canva PNG - testimonial template","Approved","2025-01-24","—","—","HIGH — duplicate for other clients"],
    ["CON-006","[Client C]","Facebook","Video","Product demo video","Check out how [product] works...","Set F — Facebook mix","MP4 product demo","Draft","—","—","—","MEDIUM — needs update for each product"],
]
for i, row in enumerate(cl_data):
    ws3.append(row)
    for cell in ws3[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",12),("B",14),("C",12),("D",12),("E",32),("F",28),("G",22),("H",22),("I",14),("J",16),("K",16),("L",28),("M",28)]:
    ws3.column_dimensions[col].width = w

# Sheet 4: Hashtag Bank
ws4 = wb2.create_sheet("Hashtag Bank")
hb_headers = ["Niche","Hashtag","Size (Posts)","Tier","Avg Engagement Signal","Best Platform","Notes"]
ws4.append(hb_headers)
for cell in ws4[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

hb_data = [
    ["SMMA / Marketing","#socialmediamarketing","5M+","Tier 1 — Mega","Low per post, high volume","Instagram","Use sparingly — broad audience"],
    ["SMMA / Marketing","#digitalmarketingagency","280K","Tier 2 — Macro","Medium — active community","Instagram + LinkedIn","Good for agency authority posts"],
    ["SMMA / Marketing","#smmastrategy","42K","Tier 3 — Mid","High — niche community engaged","Instagram","Core agency hashtag"],
    ["SMMA / Marketing","#socialmediaagency","95K","Tier 2 — Macro","Medium","Instagram","Use in agency-focused content"],
    ["Restaurant","#restaurantmarketing","68K","Tier 2 — Macro","Medium","Instagram","Niche marketing hashtag"],
    ["Restaurant","#restaurantowner","180K","Tier 2 — Macro","Medium-High","Instagram","Decision-maker audience"],
    ["Restaurant","#foodbusiness","95K","Tier 2 — Macro","Medium","Instagram","Owner perspective content"],
    ["Fitness","#personaltrainerlife","220K","Tier 2 — Macro","High — very engaged niche","Instagram","Coach/PT identity content"],
    ["Fitness","#fitnesstips","8.5M","Tier 1 — Mega","Low per post","Instagram + TikTok","Discovery content only"],
    ["Real Estate","#realestatemarketing","55K","Tier 3 — Mid","High — niche and active","Instagram + LinkedIn","Lead gen and strategy content"],
    ["E-Commerce","#ecommercebrand","120K","Tier 2 — Macro","Medium","Instagram + TikTok","Product and brand content"],
    ["E-Commerce","#shopsmall","6M","Tier 1 — Mega","Low per post, community feel","Instagram","Use for brand building"],
]
for i, row in enumerate(hb_data):
    ws4.append(row)
    for cell in ws4[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",18),("B",30),("C",15),("D",18),("E",28),("F",22),("G",35)]:
    ws4.column_dimensions[col].width = w

wb2.save(BASE + p06 + "Content_Calendar_Tracker.xlsx")
print(f"  ✓ {p06}Content_Calendar_Tracker.xlsx")

print("✓ 06_SOCIAL_MEDIA_MANAGEMENT complete")
print("\nPART 2 DONE")
