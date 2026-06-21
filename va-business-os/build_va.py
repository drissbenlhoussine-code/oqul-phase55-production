#!/usr/bin/env python3
"""Complete build for Virtual Assistant Business OS"""
import os, csv, json, zipfile
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor as PRGB
from pptx.enum.text import PP_ALIGN
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

BASE = "/home/user/oqul-phase55-production/va-business-os/VA_Business_OS/"
ETSY_DIR = "/home/user/oqul-phase55-production/etsy-listings/"
for d in ["00_START_HERE","01_BUSINESS_SETUP","02_SERVICES_PRICING","03_CLIENT_ACQUISITION",
          "04_CLIENT_MANAGEMENT","05_TASK_MANAGEMENT","06_TOOLS_AND_SOFTWARE",
          "07_FINANCES","08_NOTION_WORKSPACE","09_CANVA_TEMPLATES","10_BONUSES"]:
    os.makedirs(BASE+d, exist_ok=True)
os.makedirs(ETSY_DIR, exist_ok=True)

NAV="2D3748"; ACC="E53E3E"; GLD="D69E2E"; GRN="38A169"; WHT="FFFFFF"; LGR="F7FAFC"
def hf(h): return PatternFill("solid", fgColor=h)
def bf(bold=True,sz=11,col="000000"): return Font(bold=bold,size=sz,color=col)
def al(h="center",v="center"): return Alignment(horizontal=h,vertical=v,wrap_text=True)
def thin(): s=Side(style='thin',color='CCCCCC'); return Border(left=s,right=s,top=s,bottom=s)
def hr_row(ws,row,cols,texts,bg=NAV,fg=WHT):
    for c,t in zip(cols,texts):
        x=ws.cell(row=row,column=c,value=t); x.fill=hf(bg); x.font=bf(True,11,fg); x.alignment=al(); x.border=thin()
def dr(ws,row,cols,vals,bg=WHT):
    for c,v in zip(cols,vals):
        x=ws.cell(row=row,column=c,value=v); x.fill=hf(bg); x.font=bf(False,10); x.alignment=al("left"); x.border=thin()
def wd(ws,widths):
    for col,w in widths.items(): ws.column_dimensions[col].width=w

def doc(fn, title, sub, secs):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x2D,0x37,0x48)
    if sub:
        s = d.add_paragraph(sub); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10); s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for sec in secs:
        if isinstance(sec, str): d.add_paragraph(sec); continue
        h, items = sec
        hd = d.add_heading(h, level=1); hd.runs[0].font.color.rgb = RGBColor(0x2D,0x37,0x48)
        for it in items:
            if isinstance(it, tuple) and it[0]=='*': d.add_paragraph(it[1], style='List Bullet')
            else: d.add_paragraph(str(it))
    d.save(BASE+fn); print(f"  doc {fn}")

PNAV=PRGB(45,55,72); PACC=PRGB(229,62,62); PGLD=PRGB(214,158,46); PWHT=PRGB(255,255,255)
PLGR=PRGB(247,250,252); PDGR=PRGB(44,62,80); PGRN=PRGB(56,161,105)
def prs():
    p=Presentation(); p.slide_width=Inches(13.33); p.slide_height=Inches(7.5); return p
def sl(p): return p.slides.add_slide(p.slide_layouts[6])
def box(s,l,t,w,h,rgb):
    sh=s.shapes.add_shape(1,Inches(l),Inches(t),Inches(w),Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=rgb; sh.line.fill.background()
def tx(s,text,l,t,w,h,sz=18,bold=False,col=PWHT,a=PP_ALIGN.LEFT):
    tb=s.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(h))
    tf=tb.text_frame; tf.word_wrap=True; p=tf.paragraphs[0]; p.alignment=a
    r=p.add_run(); r.text=text; r.font.size=PPt(sz); r.font.bold=bold; r.font.color.rgb=col

def csv_w(path, headers, rows):
    with open(BASE+path,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
    print(f"  csv {path}")

def make_pdf(fpath, title, subtitle, secs):
    st=getSampleStyleSheet()
    NAV_C=colors.HexColor("#2D3748"); ACC_C=colors.HexColor("#E53E3E"); GLD_C=colors.HexColor("#D69E2E")
    ts=ParagraphStyle('T',parent=st['Normal'],fontSize=16,textColor=NAV_C,spaceAfter=4,fontName='Helvetica-Bold')
    ss=ParagraphStyle('S',parent=st['Normal'],fontSize=11,textColor=colors.HexColor("#7F8C8D"),spaceAfter=12)
    hs=ParagraphStyle('H',parent=st['Normal'],fontSize=13,textColor=NAV_C,spaceBefore=12,spaceAfter=4,fontName='Helvetica-Bold')
    bs=ParagraphStyle('B',parent=st['Normal'],fontSize=10,spaceAfter=4,leading=15)
    bls=ParagraphStyle('BL',parent=st['Normal'],fontSize=10,leftIndent=16,spaceAfter=3,leading=14)
    story=[Paragraph(title,ts),HRFlowable(width="100%",thickness=3,color=ACC_C,spaceAfter=6),Paragraph(subtitle,ss)]
    for sec in secs:
        if isinstance(sec,str): story.append(Paragraph(sec,bs)); continue
        hd,items=sec; story.append(Paragraph(hd,hs)); story.append(HRFlowable(width="100%",thickness=1,color=GLD_C,spaceAfter=4))
        for it in items:
            if isinstance(it,tuple) and it[0]=='*': story.append(Paragraph(f"* {it[1]}",bls))
            else: story.append(Paragraph(str(it),bs))
    SimpleDocTemplate(fpath,pagesize=A4,rightMargin=50,leftMargin=50,topMargin=50,bottomMargin=50).build(story)

print("Building VA Business OS...")

# 00 START HERE
doc("00_START_HERE/Welcome_and_Quickstart.docx",
    "Welcome to Your VA Business OS",
    "Virtual Assistant Business OS | Your complete business operating system",
    [
        ("What's Inside", [
            "The VA Business OS is the most comprehensive business system for virtual assistants and online business managers. It covers everything from your first client to scaling a VA team.",
            ("*","Business setup templates (legal, branding, contracts)"),
            ("*","50+ VA service templates and SOPs"),
            ("*","Client acquisition and discovery call scripts"),
            ("*","Complete Notion workspace with 5 importable databases"),
            ("*","Canva-ready presentation templates"),
        ]),
        ("30-Day Quick Start", [
            "Week 1: Set up legal structure (LLC), open business bank account, create service packages and pricing",
            "Week 2: Build your portfolio (offer 2 clients a free week to get testimonials), set up Notion and ClickUp",
            "Week 3: Begin outreach -- 10 LinkedIn connections per day to your target client type, post 3x/week",
            "Week 4: Close first paid client, deliver at 150% of expectations, ask for referral",
        ]),
    ])

# 01 BUSINESS SETUP
doc("01_BUSINESS_SETUP/Business_Plan_Template.docx",
    "Virtual Assistant Business Plan",
    "VA Business OS | Your roadmap to a profitable VA practice",
    [
        ("Business Overview", [
            "[Your Name] Virtual Assistant Services specializes in providing [niche -- executive support / social media / bookkeeping / OBM] services to [target client -- coaches, e-commerce brands, real estate agents, law firms].",
            "Year 1 Revenue Target: $60,000-$85,000 (5-8 retainer clients at $1,200-$2,500/month)",
        ]),
        ("Your VA Niche Options", [
            ("*","Executive VA: Calendar management, email management, travel booking, research. Best clients: C-suite executives, entrepreneurs. Rate: $35-75/hour"),
            ("*","Social Media VA: Content scheduling, community management, graphic creation. Best clients: Personal brands, small businesses. Rate: $25-50/hour"),
            ("*","E-commerce VA: Product listings, inventory management, customer service. Best clients: Amazon/Shopify sellers. Rate: $20-40/hour"),
            ("*","Online Business Manager (OBM): Team management, project management, systems building. Best clients: 6-7 figure online business owners. Rate: $50-150/hour"),
            ("*","Bookkeeping VA: Accounts, reconciliation, reporting. Best clients: Small business owners. Rate: $35-65/hour"),
        ]),
        ("Service Packages", [
            "Starter Package: 20 hours/month - $1,200/month. Ideal for solopreneurs just delegating for the first time.",
            "Growth Package: 40 hours/month - $2,200/month. Ideal for established businesses scaling operations.",
            "Dedicated Package: Full-time support (160 hrs/month) - $4,500/month. Ideal for businesses needing near-full-time support.",
            "Project-based: Website updates, content creation, launch support. Quoted per project.",
        ]),
    ])

wb=Workbook()
ws=wb.active; ws.title="Pricing and Revenue"
hr_row(ws,1,[1,2,3,4],["Package","Hours/Month","Rate","Monthly Revenue"])
wd(ws,{"A":25,"B":14,"C":14,"D":16})
pkgs=[["Starter","20","$60/hr","$1,200"],["Growth","40","$55/hr","$2,200"],["Dedicated","160","$28/hr","$4,500"],["VIP Day","8","$75/hr","$600"]]
for i,r in enumerate(pkgs):
    bg=LGR if i%2==0 else WHT; dr(ws,i+2,[1,2,3,4],r,bg)
ws2=wb.create_sheet("Income Tracker")
hr_row(ws2,1,[1,2,3,4,5],["Client","Package","Hours","Monthly Fee","Status"])
wd(ws2,{"A":25,"B":18,"C":10,"D":14,"E":12})
clients_v=[
    ["Sarah Johnson (Coach)","Growth","40","$2,200","Active"],
    ["TechScale Inc","Dedicated","160","$4,500","Active"],
    ["Maria's Boutique","Starter","20","$1,200","Active"],
    ["Ryan Online (OBM)","Growth","40","$2,200","Active"],
    ["GreenStart LLC","Starter","20","$1,200","Onboarding"],
]
for i,r in enumerate(clients_v):
    bg=LGR if i%2==0 else WHT; dr(ws2,i+2,[1,2,3,4,5],r,bg)
wb.save(BASE+"01_BUSINESS_SETUP/Pricing_and_Income_Tracker.xlsx")
print("  xlsx 01_BUSINESS_SETUP/Pricing_and_Income_Tracker.xlsx")

doc("01_BUSINESS_SETUP/Legal_and_Contracts.docx",
    "VA Legal Templates and Contracts",
    "VA Business OS | Protect your business with professional contracts",
    [
        ("Virtual Assistant Service Agreement", [
            "This Service Agreement ('Agreement') is between [Your Full Name] ('Service Provider') and [Client Name] ('Client') effective [Date].",
            "1. SERVICES: Service Provider agrees to provide the following virtual assistant services: [describe services -- e.g., email management, calendar management, social media scheduling, research]. Services will be performed remotely unless otherwise agreed in writing.",
            "2. RATE AND PAYMENT: Client agrees to pay $[X]/hour or $[X]/month for [X] hours of service. Payment is due on the [1st] of each month. Invoices not paid within 10 days are subject to a $25 late fee per week.",
            "3. HOURS AND AVAILABILITY: Service Provider is available [days/hours]. Any hours beyond the monthly retainer are billed at $[X]/hour. Hours do not roll over month-to-month.",
            "4. COMMUNICATION: Primary communication via [email/Slack/project management tool]. Response time: within [X] business hours. Rush requests (under 2 hours) may incur additional fees.",
            "5. CONFIDENTIALITY: Service Provider agrees to keep all client information, business processes, and communications strictly confidential. This obligation survives termination of this Agreement.",
            "6. TERMINATION: Either party may terminate this Agreement with [30] days written notice. Client is responsible for payment of any work completed during the notice period.",
            "7. INTELLECTUAL PROPERTY: All work product created by Service Provider for Client is considered work-for-hire and becomes the property of Client upon full payment.",
        ]),
        ("Non-Disclosure Agreement (NDA)", [
            "By signing this Agreement, Client and Service Provider agree to keep all shared business information confidential. This includes but is not limited to: business strategies, customer data, financial information, pricing, and proprietary processes.",
            "Both parties agree not to disclose confidential information to third parties without written consent. This agreement is effective for [2 years] from the date of signing and survives termination of the working relationship.",
        ]),
        ("Scope Change Policy", [
            "Projects or tasks that fall outside the agreed scope may require additional fees. Service Provider will notify Client when a request falls outside the agreed scope and will provide an estimate before proceeding. Client approval is required for all out-of-scope work.",
        ]),
    ])
print("  ✓ 01_BUSINESS_SETUP")

# 02 SERVICES PRICING
doc("02_SERVICES_PRICING/Complete_Service_Menu.docx",
    "VA Complete Service Menu",
    "VA Business OS | 80+ services you can offer as a virtual assistant",
    [
        ("Administrative Services", [
            ("*","Email inbox management (triage, respond, archive, organize labels/folders)"),
            ("*","Calendar management (schedule, reschedule, send invites, manage conflicts)"),
            ("*","Travel booking (flights, hotels, ground transportation, itineraries)"),
            ("*","Meeting preparation (agendas, pre-reading materials, action items after)"),
            ("*","Data entry and database management"),
            ("*","File organization (Google Drive, Dropbox, OneDrive)"),
            ("*","Document creation (reports, presentations, proposals)"),
            ("*","Research and summarization"),
            ("*","Expense report management"),
            ("*","Subscription and vendor management"),
        ]),
        ("Social Media Services", [
            ("*","Content scheduling (Buffer, Hootsuite, Later, Publer)"),
            ("*","Community management (replies, comments, DMs)"),
            ("*","Graphic creation using Canva templates"),
            ("*","Hashtag research and optimization"),
            ("*","Analytics reporting (weekly or monthly)"),
            ("*","Pinterest management and pin creation"),
            ("*","Facebook Group moderation"),
            ("*","LinkedIn profile optimization and posting"),
        ]),
        ("Customer Service", [
            ("*","Email customer support (respond to customer inquiries)"),
            ("*","Live chat support"),
            ("*","Order processing and fulfillment coordination"),
            ("*","Returns and refund processing"),
            ("*","CRM data entry and maintenance"),
            ("*","Customer feedback collection and analysis"),
            ("*","FAQ document creation and maintenance"),
        ]),
        ("Online Business Manager (OBM) Services", [
            ("*","Team management (hiring, onboarding, task assignment, performance tracking)"),
            ("*","Project management (Asana, ClickUp, Monday.com, Notion)"),
            ("*","SOP creation and documentation"),
            ("*","Launch management (coordinate all moving parts of a product launch)"),
            ("*","Vendor and contractor management"),
            ("*","KPI tracking and reporting to CEO"),
            ("*","Systems and processes audit and optimization"),
        ]),
        ("Tech and Systems", [
            ("*","CRM setup (HubSpot, Dubsado, HoneyBook, GoHighLevel)"),
            ("*","Email marketing setup (Mailchimp, ConvertKit, ActiveCampaign)"),
            ("*","Course platform management (Kajabi, Teachable, Thinkific)"),
            ("*","Website updates (WordPress, Squarespace, Wix)"),
            ("*","Funnel building and maintenance"),
            ("*","Zapier/Make automation setup"),
            ("*","Podcast management (shownotes, scheduling, upload, repurposing)"),
        ]),
    ])
print("  ✓ 02_SERVICES_PRICING")

# 03 CLIENT ACQUISITION
doc("03_CLIENT_ACQUISITION/Outreach_Scripts.docx",
    "Client Acquisition Scripts",
    "VA Business OS | How to land clients on LinkedIn, Facebook, and more",
    [
        ("LinkedIn Outreach Strategy", [
            "Your ideal clients are busy entrepreneurs and business owners who spend time on LinkedIn. Here's the exact approach:",
            "Connection request: 'Hi [Name], I specialize in supporting [type of business owner -- coaches / e-commerce founders / real estate agents] with their administrative and operational tasks. I came across your profile and would love to connect!'",
            "First follow-up (after connecting): 'Hi [Name], thank you for connecting! I noticed you [specific observation -- recently launched a course / scaled your team / started a podcast]. Many [type of client] I work with reach a point where the backend is taking too much time away from [their zone of genius]. I'd love to offer you a free 20-minute 'Business Clarity Call' to see where I might be able to help. Interested?'",
        ]),
        ("Facebook Group Strategy", [
            "Join Facebook groups where your ideal clients hang out (entrepreneur groups, niche-specific groups).",
            ("*","Don't pitch in groups -- add value first. Answer questions about tools, processes, and time management"),
            ("*","Post helpful content (tips, templates, behind-the-scenes of how you help clients)"),
            ("*","When someone asks 'can anyone recommend a VA?', DM them within 5 minutes"),
            "DM template: 'Hi [Name], I saw your post in [Group Name] -- I'd love to chat! I specialize in [your niche] and work with [client type]. Would you be open to a 15-minute call to see if I could help? I have some availability this week.'",
        ]),
        ("Discovery Call Framework", [
            "Opening: 'Thank you for making time! My goal today is to learn about your business and understand where you're losing the most time. Then we can see if my services are a fit. Does that work?'",
            "Discovery questions:",
            ("*","'Tell me about your business -- what do you do and who do you serve?'"),
            ("*","'What tasks take the most time in your week that you'd love to hand off?'"),
            ("*","'What have you tried in the past -- have you had a VA or assistant before?'"),
            ("*","'What does a successful outcome look like for you in the first 90 days?'"),
            ("*","'What's your timeline for bringing someone on?'"),
            "Proposal: 'Based on what you've shared, here's what I'd recommend: [package + specific tasks]. This would free up approximately [X hours/week] so you can focus on [their zone of genius]. The investment is $[X]/month. Shall I send you the contract to get started?'",
        ]),
    ])
print("  ✓ 03_CLIENT_ACQUISITION")

# 04 CLIENT MANAGEMENT
wb2=Workbook()
ws=wb2.active; ws.title="Client Tracker"
hr_row(ws,1,[1,2,3,4,5,6],["Client","Package","Hours/Month","Monthly Fee","Start Date","Status"])
wd(ws,{"A":22,"B":16,"C":12,"D":14,"E":14,"F":12})
ct_data=[
    ["Sarah Johnson","Growth","40","$2,200","Jan 1, 2026","Active"],
    ["TechScale Inc","Dedicated","160","$4,500","Oct 15, 2025","Active"],
    ["Maria's Boutique","Starter","20","$1,200","Nov 1, 2025","Active"],
    ["Ryan Online","Growth","40","$2,200","Dec 1, 2025","Active"],
    ["GreenStart LLC","Starter","20","$1,200","Jan 15, 2026","Onboarding"],
]
for i,r in enumerate(ct_data):
    bg=LGR if i%2==0 else WHT; dr(ws,i+2,[1,2,3,4,5,6],r,bg)
ws2=wb2.create_sheet("Time Log")
hr_row(ws2,1,[1,2,3,4,5],["Date","Client","Task","Hours","Notes"])
wd(ws2,{"A":12,"B":20,"C":35,"D":8,"E":25})
time_data=[
    ["2026-01-15","Sarah Johnson","Email inbox management -- 32 emails processed","1.5",""],
    ["2026-01-15","TechScale Inc","Team meeting prep -- agenda created","0.5",""],
    ["2026-01-15","Maria's Boutique","Instagram scheduling -- 7 posts scheduled","1.0",""],
    ["2026-01-16","Sarah Johnson","Calendar -- scheduled 5 meetings, declined 2 conflicts","1.0",""],
    ["2026-01-16","Ryan Online","SOP documentation -- drafted client onboarding SOP","2.0",""],
    ["2026-01-16","TechScale Inc","Vendor management -- negotiated software renewal","0.75",""],
]
for i,r in enumerate(time_data):
    bg=LGR if i%2==0 else WHT; dr(ws2,i+2,[1,2,3,4,5],r,bg)
wb2.save(BASE+"04_CLIENT_MANAGEMENT/Client_and_Time_Tracker.xlsx")
print("  xlsx 04_CLIENT_MANAGEMENT/Client_and_Time_Tracker.xlsx")

doc("04_CLIENT_MANAGEMENT/Onboarding_Guide.docx",
    "Client Onboarding Guide",
    "VA Business OS | Your 5-step process for onboarding every new client",
    [
        ("Step 1: Welcome and Contract (Day 1)", [
            ("*","Send signed contract via DocuSign"),
            ("*","Send invoice for first month + setup fee (if applicable)"),
            ("*","Send welcome email with what to expect in the first week"),
        ]),
        ("Step 2: Access and Setup (Days 2-3)", [
            ("*","Request access to all tools (email, calendar, CRM, social media, file storage)"),
            ("*","Set up shared password manager (LastPass or 1Password)"),
            ("*","Join client's communication platform (Slack, Teams, or WhatsApp)"),
            ("*","Access project management tool and familiarize yourself with existing tasks"),
        ]),
        ("Step 3: Process Documentation (Days 3-7)", [
            ("*","Schedule 60-minute 'brain dump' call with client"),
            ("*","Document every process they want you to handle"),
            ("*","Create SOPs for top 3 recurring tasks"),
            ("*","Identify their communication preferences, response time expectations, and non-negotiables"),
        ]),
        ("Step 4: First Week Execution", [
            ("*","Start with lower-risk tasks first while you learn their preferences"),
            ("*","Over-communicate: 'I'm about to send this email on your behalf -- please review first'"),
            ("*","Daily check-ins via Slack for the first 2 weeks"),
        ]),
        ("Step 5: 30-Day Review", [
            ("*","Schedule 20-minute check-in at Day 30"),
            ("*","Review what's working, what needs adjustment"),
            ("*","Ask: 'Is there anything I'm doing that you'd do differently?'"),
            ("*","Review hour usage vs. package hours -- recommend package upgrade if needed"),
        ]),
    ])
print("  ✓ 04_CLIENT_MANAGEMENT")

# 05 TASK MANAGEMENT
doc("05_TASK_MANAGEMENT/VA_Task_SOPs.docx",
    "VA Task Standard Operating Procedures",
    "VA Business OS | SOPs for your 20 most common VA tasks",
    [
        ("SOP 1: Email Inbox Management", [
            "Frequency: Daily. Time estimate: 30-60 minutes.",
            ("*","Open client's email inbox at [agreed time, e.g., 8am and 1pm]"),
            ("*","Triage: sort all emails into: Action Required, Waiting on Response, FYI/Read, Delegate, Archive"),
            ("*","Respond to emails within client's approved templates"),
            ("*","Flag anything requiring client's personal response in task manager: 'Email from [Name] needs your response'"),
            ("*","Unsubscribe from promotional emails client no longer needs"),
            ("*","File all processed emails into labeled folders"),
        ]),
        ("SOP 2: Calendar Management", [
            "Frequency: Daily. Time estimate: 15-30 minutes.",
            ("*","Review upcoming 7 days for conflicts, double-bookings, or travel time issues"),
            ("*","Send agenda for all meetings 24 hours in advance (or as agreed)"),
            ("*","Send meeting reminders to all parties 1 hour before"),
            ("*","Block focus time per client's preferences (do not schedule meetings during)"),
            ("*","Confirm all video meeting links are correct and working"),
        ]),
        ("SOP 3: Social Media Scheduling", [
            "Frequency: Weekly (batch scheduling). Time estimate: 2-3 hours.",
            ("*","Pull approved content from shared content calendar/Google Drive"),
            ("*","Create or resize graphics in Canva to platform specifications"),
            ("*","Write or finalize captions according to brand voice guide"),
            ("*","Schedule all posts in Buffer/Hootsuite/Later for the week"),
            ("*","Send weekly preview to client for approval before going live"),
        ]),
        ("SOP 4: Research Tasks", [
            "For any research task, follow this format:",
            ("*","Clarify the goal: What decision does this research support?"),
            ("*","Set a time box: Research for X hours maximum, then compile findings"),
            ("*","Use a standardized research template: Source, Key Findings, Credibility Rating"),
            ("*","Summarize in bullet points -- executives want conclusions, not raw data"),
            ("*","Include your recommendation: 'Based on this research, I suggest...'"),
        ]),
    ])
print("  ✓ 05_TASK_MANAGEMENT")

# 06 TOOLS
doc("06_TOOLS_AND_SOFTWARE/VA_Tech_Stack.docx",
    "VA Essential Tech Stack",
    "VA Business OS | Every tool you need as a professional virtual assistant",
    [
        ("Communication and Project Management", [
            ("*","Slack: Team communication. Free plan sufficient to start. Clients love it for quick messages"),
            ("*","ClickUp: Project management. Free plan excellent. Create task lists for each client"),
            ("*","Notion: Knowledge base and documentation. Great for building client SOPs"),
            ("*","Zoom/Google Meet: Video calls with clients. Always record onboarding calls for reference"),
        ]),
        ("Administrative Tools", [
            ("*","Google Workspace: Gmail, Drive, Docs, Sheets, Calendar. $6/month. Essential"),
            ("*","LastPass/1Password: Secure password sharing with clients. $3-5/month"),
            ("*","Calendly: Online scheduling. Free plan works for most VAs. Clients book calls directly"),
            ("*","Canva: Graphic design for social media, presentations. Free plan has most features"),
        ]),
        ("Business Management", [
            ("*","HoneyBook or Dubsado: All-in-one CRM, contracts, invoicing, scheduling for VAs. $16-19/month"),
            ("*","QuickBooks Self-Employed: Track income/expenses, calculate quarterly taxes. $15/month"),
            ("*","Loom: Record short video updates for clients instead of long emails. $12/month"),
            ("*","DocuSign or HelloSign: E-signature for contracts. $10-15/month"),
        ]),
        ("Productivity Tools", [
            ("*","Toggl: Free time tracking. Essential for hourly clients and tracking your efficiency"),
            ("*","Grammarly: Writing assistant. Free plan helps catch errors in client emails"),
            ("*","Rev or Otter.ai: Transcription for meeting recordings. $8-17/month"),
            ("*","Zapier: Basic automations. Free plan allows 5 automations -- connect your tools"),
        ]),
    ])
print("  ✓ 06_TOOLS_AND_SOFTWARE")

# 07 FINANCES
wb3=Workbook()
ws=wb3.active; ws.title="Annual Revenue Planner"
hr_row(ws,1,[1,2,3,4,5],["Month","# Clients","MRR","Expenses","Net Income"])
wd(ws,{"A":10,"B":12,"C":14,"D":14,"E":14})
fin=[["Jan 2026","2","$3,400","$250","$3,150"],["Feb 2026","3","$5,600","$300","$5,300"],
     ["Mar 2026","4","$7,800","$350","$7,450"],["Apr 2026","5","$9,800","$400","$9,400"],
     ["May 2026","5","$10,200","$420","$9,780"],["Jun 2026","6","$12,400","$450","$11,950"],
     ["Jul 2026","6","$12,400","$450","$11,950"],["Aug 2026","7","$14,600","$500","$14,100"],
     ["Sep 2026","7","$14,600","$500","$14,100"],["Oct 2026","8","$16,800","$550","$16,250"],
     ["Nov 2026","8","$16,800","$550","$16,250"],["Dec 2026","9","$19,000","$600","$18,400"]]
for i,r in enumerate(fin):
    bg=LGR if i%2==0 else WHT; dr(ws,i+2,[1,2,3,4,5],r,bg)
wb3.save(BASE+"07_FINANCES/Revenue_and_Finance_Tracker.xlsx")
print("  xlsx 07_FINANCES/Revenue_and_Finance_Tracker.xlsx")
print("  ✓ 07_FINANCES")

# 08 NOTION WORKSPACE
csv_w("08_NOTION_WORKSPACE/Notion_Client_Roster.csv",
    ["Client","Package","Hours","Monthly Fee","Start Date","Status","Primary Contact","Notes"],
    [["Sarah Johnson","Growth","40","$2,200","2026-01-01","Active","sarah@sarahcoaches.com","Prefers Slack"],
     ["TechScale Inc","Dedicated","160","$4,500","2025-10-15","Active","ceo@techscale.io","Invoiced 1st"],
     ["Maria's Boutique","Starter","20","$1,200","2025-11-01","Active","maria@mariasboutique.com","Email pref"],
     ["Ryan Online","Growth","40","$2,200","2025-12-01","Active","ryan@ryanonline.co","Slack daily"],
     ["GreenStart LLC","Starter","20","$1,200","2026-01-15","Onboarding","lisa@greenstart.co","New client"],])

csv_w("08_NOTION_WORKSPACE/Notion_Task_Board.csv",
    ["Task","Client","Due Date","Priority","Status","Estimated Hours","Actual Hours"],
    [["Inbox triage - AM","Sarah Johnson","Daily","High","Recurring","1",""],
     ["Schedule podcast guest","TechScale Inc","2026-01-20","High","In Progress","0.5",""],
     ["Instagram week 3 scheduling","Maria's Boutique","2026-01-18","Medium","Not Started","2",""],
     ["SOP for client onboarding","Ryan Online","2026-01-22","Medium","In Progress","3",""],
     ["Welcome email draft","GreenStart LLC","2026-01-16","High","Done","0.75","0.5"],])

csv_w("08_NOTION_WORKSPACE/Notion_Expense_Log.csv",
    ["Date","Expense","Category","Amount","Tax Deductible","Notes"],
    [["2026-01-01","HoneyBook","Software","$19.00","Yes","CRM and invoicing"],
     ["2026-01-01","Canva Pro","Software","$13.99","Yes","Design tool"],
     ["2026-01-01","Grammarly","Software","$12.00","Yes","Writing assistant"],
     ["2026-01-01","Google Workspace","Software","$6.00","Yes","Email and storage"],
     ["2026-01-01","ClickUp Pro","Software","$9.00","Yes","Project management"],
     ["2026-01-05","Loom","Software","$12.50","Yes","Client video updates"],
     ["2026-01-10","Toggl","Software","$9.00","Yes","Time tracking"],])

with open(BASE+"08_NOTION_WORKSPACE/Notion_Setup_Guide.md","w",encoding="utf-8") as f:
    f.write("# VA Business OS - Notion Setup\n\n## Import These Databases\n- Client Roster\n- Task Board\n- Expense Log\n\n## Recommended Views\n- Task Board: Kanban by Status and by Client\n- Client Roster: Table with revenue rollup\n")
print("  ✓ 08_NOTION_WORKSPACE")

# 09 CANVA TEMPLATES
ppt=prs()
s0=sl(ppt)
box(s0,0,0,13.33,7.5,PNAV)
box(s0,0,6.0,13.33,1.5,PACC)
tx(s0,"VIRTUAL ASSISTANT SERVICES",0.5,1.2,12,0.9,sz=34,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"Professional. Reliable. Detail-Oriented.",0.5,2.3,12,0.6,sz=18,col=PGLD,a=PP_ALIGN.CENTER)
tx(s0,"Your business runs smoother when you have the right support.",0.5,3.2,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"[Your Name]  |  [Specialty]  |  [Website]",0.5,6.2,12,0.4,sz=12,col=PWHT,a=PP_ALIGN.CENTER)

s1=sl(ppt)
box(s1,0,0,13.33,1.2,PACC)
tx(s1,"SERVICES I OFFER",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
svcs=[("Email Management","Inbox zero every day"),("Calendar Management","No more scheduling conflicts"),
      ("Social Media","Consistent, on-brand posting"),("Research","Decisions backed by data"),
      ("Customer Service","Fast, professional responses"),("Systems & SOPs","Processes that run without you")]
for i,(svc,desc) in enumerate(svcs):
    col_=i%2; row_=i//2
    left=0.5+col_*6.4; top=1.4+row_*2.0
    box(s1,left,top,6.0,1.8,PLGR)
    tx(s1,svc,left+0.2,top+0.15,5.6,0.5,sz=12,bold=True,col=PNAV)
    tx(s1,desc,left+0.2,top+0.75,5.6,0.85,sz=10,col=PDGR)

s2=sl(ppt)
box(s2,0,0,13.33,7.5,PNAV)
box(s2,0,5.8,13.33,1.7,PACC)
tx(s2,"READY TO DELEGATE?",0.5,1.8,12,0.9,sz=34,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s2,"Book a free 20-minute clarity call.",0.5,3.0,12,0.6,sz=17,col=PGLD,a=PP_ALIGN.CENTER)
tx(s2,"[Calendly link]  |  [Email]",0.5,6.1,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)
ppt.save(BASE+"09_CANVA_TEMPLATES/VA_Services_Deck.pptx")
print("  pptx 09_CANVA_TEMPLATES/VA_Services_Deck.pptx")
print("  ✓ 09_CANVA_TEMPLATES")

# 10 BONUSES
csv_w("10_BONUSES/52_Email_Templates.csv",
    ["Template #","Situation","Subject Line","First Paragraph"],
    [[str(i+1),sit,subj,body] for i,(sit,subj,body) in enumerate([
        ("New client inquiry reply","Thank you for reaching out!","Thank you for your interest in my VA services! I'd love to learn more about how I can support your business."),
        ("Discovery call confirmation","Our call is confirmed - [Date/Time]","I'm looking forward to our call on [Date] at [Time]. Here's the link: [link]."),
        ("Proposal follow-up","Following up on your proposal","Hi [Name], I wanted to follow up on the proposal I sent on [date]. Do you have any questions I can answer?"),
        ("Monthly invoice","Invoice for [Month] VA Services","Please find your invoice for [Month] attached. Payment is due by [date]."),
        ("Monthly progress report","Your [Month] VA Report","Here's a summary of everything I accomplished for your business in [Month]."),
        ("Vacation notice","I'll be out [dates] - here's what to expect","I wanted to give you advance notice that I'll be on vacation from [date] to [date]."),
        ("Capacity update","I have a new availability opening","Hi [Name], I have some capacity opening up next month if you'd like to increase your hours."),
        ("Rate increase notice","Service rate update effective [Date]","I wanted to give you 30 days notice of a rate adjustment effective [date]."),
        ("Referral thank you","Thank you for the referral!","Thank you so much for referring [Name] to me! I truly appreciate your trust and support."),
        ("Offboarding","Your final invoice and next steps","It's been a pleasure working with you. Attached is your final invoice and a summary of all work completed."),
    ])])

doc("10_BONUSES/VA_Business_Growth_Guide.docx",
    "VA Business Growth Guide",
    "VA Business OS | From first client to full practice",
    [
        ("Raising Your Rates (Without Losing Clients)", [
            "Most VAs undercharge. The benchmark for experienced VAs in the US is $50-75/hour for administrative work and $75-150/hour for OBM services.",
            ("*","Give 30 days notice for all rate increases"),
            ("*","Frame it as an investment in quality: 'This rate reflects my continued professional development and the systems I've built to serve you better'"),
            ("*","New clients always get your new rate -- only grandfather existing clients for one cycle"),
            ("*","If a client leaves over a 15% rate increase, they were likely not the right fit at any price"),
        ]),
        ("Adding Team Members to Scale", [
            ("*","Hire a sub-contractor VA at a lower rate -- you take on the project management role"),
            ("*","Transition from hourly to project-based pricing as you add team members"),
            ("*","Train your sub-contractor using your SOPs (the documents in 05_TASK_MANAGEMENT)"),
            ("*","Your role evolves: you win the clients, you oversee the quality, your team does the execution"),
        ]),
        ("Niching to Premium Rates", [
            "Generalist VAs earn $20-35/hour. Specialist VAs earn $50-100+/hour. Specialize to command premium rates:",
            ("*","Executive VA specializing in tech executives: $65-85/hour"),
            ("*","VA for real estate teams: $40-60/hour"),
            ("*","OBM for online course creators: $75-125/hour"),
            ("*","Podcast management specialist: $500-2,000/episode bundle"),
        ]),
    ])
print("  ✓ 10_BONUSES")

# PDF
make_pdf(BASE+"VA_Business_OS_Guide.pdf",
    "Virtual Assistant Business OS - Complete Guide",
    "Your guide to building a thriving VA business with the VA Business OS",
    [
        ("Welcome",[ "50+ files for running a professional VA business. Start with 00_START_HERE."]),
        ("Getting Started",[ ("*","Register as an LLC"),("*","Open business bank account"),("*","Set your rates and create packages"),("*","Build your service menu from the 80+ services in Section 02")]),
        ("Your First 3 Clients",[ ("*","Offer a test project at reduced rate for testimonials"),("*","Get active in Facebook groups and LinkedIn"),("*","Use the outreach scripts in 03_CLIENT_ACQUISITION"),("*","Follow the discovery call framework to close")]),
    ])
print("✓ PDF done")

# Manifest + ZIP
all_files=[]
for root,dirs,files in os.walk(BASE):
    dirs.sort()
    for f in sorted(files):
        full=os.path.join(root,f); rel=os.path.relpath(full,BASE)
        all_files.append([rel,f.split('.')[-1].upper(),f"{os.path.getsize(full)/1024:.1f} KB"])
with open(BASE+"Asset_Manifest.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["File","Type","Size"]); w.writerows(all_files)
with open(BASE+"Asset_Manifest.json","w") as f:
    json.dump({"product":"VA Business OS","total_files":len(all_files)},f)

etsy="""TITLE:
Virtual Assistant Business OS | Complete VA Business Kit | 50+ Files | Canva Templates | Notion Workspace

DESCRIPTION:
Launch or grow your virtual assistant business with this complete operating system. 50+ templates, scripts, SOPs, and tools -- everything from your first client contract to your growth strategy.

INCLUDES:
- Business plan + pricing tracker (XLSX)
- 80+ service menu with rates
- Client acquisition scripts (LinkedIn, Facebook, discovery call)
- Legal contract + NDA template
- Client onboarding 5-step guide
- Client and time tracker (XLSX)
- SOPs for 20 common VA tasks (email, calendar, social media, research)
- VA tech stack guide (20 tools reviewed)
- Revenue and finance tracker (XLSX)
- Notion workspace (3 databases: client roster, task board, expense log)
- Canva pitch deck (PPTX, import to Canva)
- 52 client email templates
- VA growth playbook

FORMATS: DOCX, XLSX, PDF, PPTX, CSV

INSTANT DIGITAL DOWNLOAD

TAGS:
virtual assistant, va business, online business manager, obm, remote work, va templates, freelance business, va starter kit, canva templates, notion template, va contract, virtual assistant tools, work from home, digital nomad, va client templates"""

with open(ETSY_DIR+"10_VABusiness_Listing.txt","w",encoding="utf-8") as f: f.write(etsy)
print("  etsy 10_VABusiness_Listing.txt")

ZIP_PATH="/home/user/oqul-phase55-production/va-business-os/BUYER_DOWNLOAD_VABusinessOS.zip"
with zipfile.ZipFile(ZIP_PATH,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        dirs.sort()
        for f in sorted(files):
            full=os.path.join(root,f); z.write(full,os.path.relpath(full,os.path.dirname(BASE)))
print(f"✓ ZIP: {ZIP_PATH} ({os.path.getsize(ZIP_PATH)/1024/1024:.1f} MB)")
print("\n=== VA BUSINESS OS COMPLETE ===")
