#!/usr/bin/env python3
"""Complete build for Notion Client Portal for Agencies"""
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

BASE = "/home/user/oqul-phase55-production/notion-client-portal/Notion_Client_Portal/"
ETSY_DIR = "/home/user/oqul-phase55-production/etsy-listings/"
for d in ["01_CLIENT_PORTAL_DATABASES","02_PROJECT_MANAGEMENT","03_ONBOARDING_TEMPLATES",
          "04_REPORTING_TEMPLATES","05_COMMUNICATION_HUB","06_CANVA_TEMPLATES",
          "07_SETUP_GUIDES","08_BONUS_TEMPLATES"]:
    os.makedirs(BASE+d, exist_ok=True)
os.makedirs(ETSY_DIR, exist_ok=True)

NAV="191919"; ACC="6366F1"; GLD="F59E0B"; GRN="10B981"; WHT="FFFFFF"; LGR="F8F8F8"
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
    t.runs[0].font.color.rgb = RGBColor(0x63,0x66,0xF1)
    if sub:
        s = d.add_paragraph(sub); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10); s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for sec in secs:
        if isinstance(sec, str): d.add_paragraph(sec); continue
        h, items = sec
        hd = d.add_heading(h, level=1); hd.runs[0].font.color.rgb = RGBColor(0x63,0x66,0xF1)
        for it in items:
            if isinstance(it, tuple) and it[0]=='*': d.add_paragraph(it[1], style='List Bullet')
            else: d.add_paragraph(str(it))
    d.save(BASE+fn); print(f"  doc {fn}")

PNAV=PRGB(25,25,25); PACC=PRGB(99,102,241); PGLD=PRGB(245,158,11); PWHT=PRGB(255,255,255)
PLGR=PRGB(248,248,248); PDGR=PRGB(51,51,51)
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
    NAV_C=colors.HexColor("#6366F1"); ACC_C=colors.HexColor("#191919"); GLD_C=colors.HexColor("#F59E0B")
    ts=ParagraphStyle('T',parent=st['Normal'],fontSize=16,textColor=NAV_C,spaceAfter=4,fontName='Helvetica-Bold')
    ss=ParagraphStyle('S',parent=st['Normal'],fontSize=11,textColor=colors.HexColor("#7F8C8D"),spaceAfter=12)
    hs=ParagraphStyle('H',parent=st['Normal'],fontSize=13,textColor=NAV_C,spaceBefore=12,spaceAfter=4,fontName='Helvetica-Bold')
    bs=ParagraphStyle('B',parent=st['Normal'],fontSize=10,spaceAfter=4,leading=15)
    bls=ParagraphStyle('BL',parent=st['Normal'],fontSize=10,leftIndent=16,spaceAfter=3,leading=14)
    story=[Paragraph(title,ts),HRFlowable(width="100%",thickness=3,color=NAV_C,spaceAfter=6),Paragraph(subtitle,ss)]
    for sec in secs:
        if isinstance(sec,str): story.append(Paragraph(sec,bs)); continue
        hd,items=sec; story.append(Paragraph(hd,hs)); story.append(HRFlowable(width="100%",thickness=1,color=GLD_C,spaceAfter=4))
        for it in items:
            if isinstance(it,tuple) and it[0]=='*': story.append(Paragraph(f"* {it[1]}",bls))
            else: story.append(Paragraph(str(it),bs))
    SimpleDocTemplate(fpath,pagesize=A4,rightMargin=50,leftMargin=50,topMargin=50,bottomMargin=50).build(story)

print("Building Notion Client Portal...")

# 01 Client Portal Databases
csv_w("01_CLIENT_PORTAL_DATABASES/Client_Master_Database.csv",
    ["Client ID","Client Name","Industry","Package","MRR","Start Date","Status","Primary Contact","Email","Notes"],
    [
        ["C001","TechVenture Inc","SaaS","Growth","$3,500","2025-09-01","Active","Alex Kim","alex@techventure.io","Quarterly reviews"],
        ["C002","Bloom Marketing","Marketing Agency","Starter","$2,000","2025-11-01","Active","Sarah Chen","s.chen@bloom.co","Monthly calls"],
        ["C003","Pacific Dental Group","Healthcare","Premium","$5,500","2025-07-15","Active","Dr. James","james@pacificdentalgroup.com","Bi-weekly"],
        ["C004","Green Living Co","E-Commerce","Growth","$3,500","2025-10-01","Active","Maria Torres","maria@greenliving.co","Prefers Slack"],
        ["C005","Summit Law Firm","Legal","Starter","$2,000","2025-12-01","Active","Robert Walsh","r.walsh@summitlaw.com","Email preferred"],
        ["C006","Creative Studio X","Creative Agency","Growth","$3,500","2026-01-10","Onboarding","Lisa Park","lisa@creativestudiox.com","New client"],
    ])

csv_w("01_CLIENT_PORTAL_DATABASES/Project_Tracker.csv",
    ["Project ID","Client","Project Name","Type","Status","Start Date","Due Date","Owner","Priority","Notes"],
    [
        ["P001","TechVenture Inc","Q1 Social Media Campaign","Campaign","In Progress","Jan 1","Mar 31","[Team Member]","High","Performance tracked"],
        ["P002","Bloom Marketing","Website Redesign Content","Content","In Review","Jan 5","Jan 31","[Team Member]","High","Client review pending"],
        ["P003","Pacific Dental Group","Email Marketing Setup","Setup","Complete","Dec 15","Jan 15","[Team Member]","Medium","Delivered on time"],
        ["P004","Green Living Co","February Content Calendar","Content","Not Started","Jan 20","Jan 25","[Team Member]","High",""],
        ["P005","Summit Law Firm","LinkedIn Strategy Build","Strategy","In Progress","Jan 10","Jan 30","[Team Member]","Medium",""],
        ["P006","Creative Studio X","Onboarding & Brand Discovery","Onboarding","In Progress","Jan 10","Jan 17","[Team Member]","High","New client setup"],
    ])

csv_w("01_CLIENT_PORTAL_DATABASES/Content_Calendar.csv",
    ["Week","Platform","Content Type","Caption/Description","Status","Client","Scheduled Date","Notes"],
    [
        ["Week 1","Instagram","Reel","Behind-the-scenes of [topic]","Approved","TechVenture Inc","Jan 8","High engagement expected"],
        ["Week 1","LinkedIn","Text Post","Thought leadership: [topic]","In Review","TechVenture Inc","Jan 9","Client to review"],
        ["Week 1","Instagram","Carousel","5 tips for [topic]","Approved","Bloom Marketing","Jan 9","",""],
        ["Week 2","Facebook","Image Post","Product feature spotlight","Draft","Green Living Co","Jan 13","",""],
        ["Week 2","Instagram","Story","Poll: [question]","Approved","Pacific Dental Group","Jan 14","",""],
        ["Week 2","LinkedIn","Article","Industry insight: [topic]","Draft","Summit Law Firm","Jan 15","",""],
    ])

csv_w("01_CLIENT_PORTAL_DATABASES/Invoice_and_Payments.csv",
    ["Invoice #","Client","Month","Amount","Issue Date","Due Date","Status","Payment Method"],
    [
        ["INV-2026-001","TechVenture Inc","January 2026","$3,500","Jan 1, 2026","Jan 10, 2026","Paid","ACH"],
        ["INV-2026-002","Bloom Marketing","January 2026","$2,000","Jan 1, 2026","Jan 10, 2026","Paid","Credit Card"],
        ["INV-2026-003","Pacific Dental Group","January 2026","$5,500","Jan 1, 2026","Jan 10, 2026","Paid","ACH"],
        ["INV-2026-004","Green Living Co","January 2026","$3,500","Jan 1, 2026","Jan 10, 2026","Outstanding",""],
        ["INV-2026-005","Summit Law Firm","January 2026","$2,000","Jan 1, 2026","Jan 10, 2026","Paid","Check"],
        ["INV-2026-006","Creative Studio X","January 2026","$3,500","Jan 10, 2026","Jan 20, 2026","Draft",""],
    ])

csv_w("01_CLIENT_PORTAL_DATABASES/Analytics_Report_Log.csv",
    ["Month","Client","Reach","Engagement Rate","Followers","New Followers","Top Post","Report Delivered"],
    [
        ["December 2025","TechVenture Inc","42,500","4.2%","8,200","+185","[Post link]","Jan 5, 2026"],
        ["December 2025","Bloom Marketing","18,800","3.8%","3,400","+72","[Post link]","Jan 5, 2026"],
        ["December 2025","Pacific Dental Group","12,200","5.1%","2,100","+48","[Post link]","Jan 5, 2026"],
        ["December 2025","Green Living Co","28,500","3.5%","6,800","+156","[Post link]","Jan 5, 2026"],
        ["December 2025","Summit Law Firm","8,400","2.9%","1,200","+28","[Post link]","Jan 6, 2026"],
    ])
print("  ✓ 01_CLIENT_PORTAL_DATABASES")

# 02 Project Management templates
csv_w("02_PROJECT_MANAGEMENT/Sprint_Board.csv",
    ["Task","Assigned To","Client","Priority","Status","Due Date","Notes"],
    [
        ["Write 8 Instagram captions","[Team A]","TechVenture Inc","High","In Progress","Jan 12",""],
        ["Design carousel graphics (5 slides)","[Team B]","Bloom Marketing","High","Not Started","Jan 14",""],
        ["Monthly analytics pull","[Team A]","All Clients","Medium","Not Started","Jan 20",""],
        ["Write LinkedIn article","[Team C]","Summit Law Firm","Medium","Draft","Jan 16",""],
        ["Schedule 15 posts in Buffer","[Team A]","Green Living Co","Medium","Approved","Jan 10","Ready to schedule"],
        ["Client report: Pacific Dental","[Manager]","Pacific Dental Group","High","In Progress","Jan 20",""],
    ])

csv_w("02_PROJECT_MANAGEMENT/Deliverables_Tracker.csv",
    ["Deliverable","Client","Month","Status","Delivery Date","Approved","Notes"],
    [
        ["Monthly content calendar","TechVenture Inc","January 2026","Delivered","Jan 5","Yes","12 posts + 15 stories"],
        ["Monthly report","TechVenture Inc","December 2025","Delivered","Jan 5","Yes",""],
        ["Website blog (4 posts)","Bloom Marketing","January 2026","In Progress","Jan 20","","Draft 2/4 done"],
        ["Email newsletter (2x)","Pacific Dental Group","January 2026","Delivered","Jan 8","Yes",""],
        ["Ad creative (3 variants)","Green Living Co","January 2026","In Review","Jan 12","Pending","Client reviewing"],
        ["LinkedIn calendar","Summit Law Firm","January 2026","Draft","Jan 18","","8 posts"],
    ])
print("  ✓ 02_PROJECT_MANAGEMENT")

# 03 Onboarding Templates
doc("03_ONBOARDING_TEMPLATES/Client_Onboarding_Workbook.docx",
    "Client Onboarding Workbook",
    "Notion Client Portal | Complete guide for onboarding new agency clients",
    [
        ("Welcome Page (Send to Client)", [
            "Welcome to [Agency Name]! We are so excited to have [Company Name] as our newest client. This workbook will guide you through our onboarding process -- it should take about 20 minutes to complete and sets us up to do amazing work together.",
            "What happens after you complete this: we'll review your responses within 2 business days, then schedule your 60-minute Strategy Kickoff Call where we'll finalize your content strategy and launch plan.",
        ]),
        ("Section 1: Your Brand Identity", [
            ("*","Brand Name: ________________________"),
            ("*","Tagline or slogan: ________________________"),
            ("*","Brand voice (check all that apply): [ ] Professional  [ ] Conversational  [ ] Humorous  [ ] Inspirational  [ ] Educational  [ ] Bold  [ ] Nurturing"),
            ("*","Brands we admire and why: ________________________"),
            ("*","Brands we DON'T want to be like: ________________________"),
            ("*","Our unique value proposition (what makes us different): ________________________"),
        ]),
        ("Section 2: Target Audience", [
            ("*","Primary audience age range: ________________________"),
            ("*","Primary audience location: ________________________"),
            ("*","Primary audience interests and pain points: ________________________"),
            ("*","What transformation do we provide for customers: ________________________"),
            ("*","Common objections or hesitations our audience has: ________________________"),
        ]),
        ("Section 3: Content and Marketing Goals", [
            ("*","Top 3 goals for social media (check): [ ] Brand awareness  [ ] Lead generation  [ ] Sales  [ ] Community  [ ] Authority/thought leadership  [ ] Website traffic"),
            ("*","Which platforms are you currently on: ________________________"),
            ("*","Content you've had success with in the past: ________________________"),
            ("*","Content you've tried that didn't work: ________________________"),
            ("*","Upcoming promotions, launches, or events in the next 90 days: ________________________"),
        ]),
        ("Section 4: Access and Logistics", [
            ("*","Primary contact name and email: ________________________"),
            ("*","Content approval process: Who needs to approve content before it's published? ________________________"),
            ("*","Approval timeline: How many hours/days do you need to review content? ________________________"),
            ("*","Preferred communication method: ________________________"),
            ("*","Best time to reach you: ________________________"),
        ]),
    ])
print("  ✓ 03_ONBOARDING_TEMPLATES")

# 04 Reporting Templates
doc("04_REPORTING_TEMPLATES/Monthly_Report_Template.docx",
    "Monthly Performance Report Template",
    "Notion Client Portal | Professional monthly report for every client",
    [
        ("MONTHLY PERFORMANCE REPORT", [
            "Client: [Client Name]",
            "Reporting Period: [Month Year]",
            "Prepared by: [Agency Name]",
            "Date: [Report Date]",
        ]),
        ("Executive Summary", [
            "This report covers [Client Name]'s social media performance for [Month Year]. Overall: [one-sentence summary of performance -- positive framing]. Key highlights and areas of focus are detailed below.",
        ]),
        ("Platform Performance", [
            "INSTAGRAM:",
            ("*","Accounts Reached: [X] (vs. [X] last month: +/- X%)"),
            ("*","Total Impressions: [X]"),
            ("*","Engagement Rate: [X]% (benchmark: 2-5%)"),
            ("*","New Followers: +[X] (Total: [X])"),
            ("*","Story Views (avg): [X]"),
            ("*","Saves: [X] | Shares: [X]"),
            "FACEBOOK:",
            ("*","Page Reach: [X]"),
            ("*","Post Engagement: [X] ([X]% rate)"),
            ("*","New Page Likes: +[X]"),
        ]),
        ("Top Performing Content", [
            "Post #1: [Post type/description] -- [X] reach, [X]% engagement. Why it worked: [brief analysis]",
            "Post #2: [Post type/description] -- [X] reach, [X]% engagement. Why it worked: [brief analysis]",
            "Post #3: [Post type/description] -- [X] reach, [X]% engagement. Why it worked: [brief analysis]",
        ]),
        ("Next Month Strategy", [
            "Based on this month's performance, here's our focus for [Next Month]:",
            ("*","[Strategy point 1 based on what worked]"),
            ("*","[Strategy point 2 -- new tactic to test]"),
            ("*","[Upcoming promotion or campaign to prepare for]"),
            ("*","Content mix adjustment: [what to increase/decrease based on data]"),
        ]),
    ])
print("  ✓ 04_REPORTING_TEMPLATES")

# 05 Communication Hub
doc("05_COMMUNICATION_HUB/Agency_Communication_SOP.docx",
    "Agency-Client Communication SOP",
    "Notion Client Portal | Standards for professional client communication",
    [
        ("Response Time Standards", [
            ("*","Standard inquiries (non-urgent): respond within 4 business hours"),
            ("*","Urgent issues (platform down, negative viral post, ad emergency): respond within 1 hour"),
            ("*","Approval requests (content, copy, ads): client has 48 hours to approve. If no response, it's considered approved"),
            ("*","After-hours messages: acknowledged first thing next business day"),
        ]),
        ("Monthly Communication Rhythm", [
            ("*","Day 1-5 of month: Deliver previous month's performance report via email"),
            ("*","Day 5-10: Monthly strategy call (20-30 min). Review report, align on next month"),
            ("*","Day 10-15: Send next month's content calendar for client review and approval"),
            ("*","Day 15-20: All approved content scheduled"),
            ("*","Ongoing: Weekly check-in message via Slack/email with current status"),
        ]),
        ("Content Approval Workflow", [
            "1. Agency creates content (copy + graphics) and uploads to shared Notion workspace or Google Drive",
            "2. Agency sends 'Content Ready for Review' email with direct link",
            "3. Client has [48 hours] to review and approve or request changes",
            "4. Client leaves comments directly in document/Notion page",
            "5. Agency makes requested changes and re-sends for final approval",
            "6. Once approved, agency schedules content in scheduling tool",
            "Key rule: Content is NOT published without written approval. Client approval via email, Slack, or Notion comment all count.",
        ]),
    ])
print("  ✓ 05_COMMUNICATION_HUB")

# 06 Canva Templates
ppt=prs()
s0=sl(ppt)
box(s0,0,0,13.33,7.5,PNAV)
box(s0,0,0,13.33,0.5,PACC)
box(s0,0,7.0,13.33,0.5,PACC)
tx(s0,"CLIENT PORTAL",0.5,1.5,12,0.9,sz=42,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"[AGENCY NAME] x [CLIENT NAME]",0.5,2.7,12,0.7,sz=20,col=PGLD,a=PP_ALIGN.CENTER)
tx(s0,"Your hub for strategy, deliverables, and performance.",0.5,3.6,12,0.6,sz=14,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"Confidential  |  [Month Year]",0.5,5.5,12,0.4,sz=11,col=PWHT,a=PP_ALIGN.CENTER)

s1=sl(ppt)
box(s1,0,0,13.33,1.2,PACC)
tx(s1,"WHAT'S IN YOUR CLIENT PORTAL",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
sections=[
    ("Strategy Hub","Your content pillars, audience personas, brand voice guidelines, and annual goals"),
    ("Content Calendar","Month-by-month content calendar with all posts, approvals, and scheduling"),
    ("Deliverables","All files, reports, and assets delivered to you -- organized by month"),
    ("Performance","Monthly analytics reports and year-to-date performance dashboard"),
    ("Communication","Meeting notes, action items, and key decisions documented"),
    ("Resources","Brand assets, style guides, and reference materials"),
]
for i,(title,desc) in enumerate(sections):
    col_=i%2; row_=i//2
    left=0.5+col_*6.4; top=1.4+row_*2.0
    box(s1,left,top,6.0,1.8,PLGR)
    tx(s1,title,left+0.2,top+0.15,5.6,0.5,sz=12,bold=True,col=PACC)
    tx(s1,desc,left+0.2,top+0.75,5.6,0.85,sz=10,col=PDGR)

s2=sl(ppt)
box(s2,0,0,13.33,1.2,PNAV)
tx(s2,"YOUR MONTHLY TIMELINE",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
milestones=[("Day 1-5","Monthly report delivered"),("Day 5-10","Strategy call"),("Day 10-15","Content calendar for approval"),("Day 15-20","Content scheduled")]
for i,(day,label) in enumerate(milestones):
    left=0.5+i*3.1
    box(s2,left,1.4,2.8,2.0,PACC)
    tx(s2,day,left+0.1,1.5,2.6,0.7,sz=14,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(s2,label,left+0.1,2.2,2.6,1.0,sz=11,col=PWHT,a=PP_ALIGN.CENTER)
box(s2,0.5,3.7,12.3,3.2,PLGR)
tx(s2,"COMMUNICATION STANDARDS",0.7,3.8,12,0.5,sz=13,bold=True,col=PNAV)
for i,std in enumerate(["Standard response time: within 4 business hours","Urgent issues response: within 1 hour","Content approval window: 48 hours (auto-approved after)","Monthly strategy calls: [X] of every month"]):
    tx(s2,f"  {std}",0.7,4.4+i*0.55,12,0.5,sz=11,col=PDGR)

ppt.save(BASE+"06_CANVA_TEMPLATES/Client_Portal_Overview_Deck.pptx")
print("  pptx 06_CANVA_TEMPLATES/Client_Portal_Overview_Deck.pptx")
print("  ✓ 06_CANVA_TEMPLATES")

# 07 Setup Guides
with open(BASE+"07_SETUP_GUIDES/Notion_Portal_Setup_Guide.md","w",encoding="utf-8") as f:
    f.write("""# Notion Client Portal - Complete Setup Guide

## Overview
This Notion Client Portal system gives your agency and clients a shared workspace for project management, approvals, communication, and reporting.

## Step 1: Create Your Agency Workspace
1. Go to Notion.so and create a new workspace called "[Agency Name] Operations"
2. This is YOUR internal workspace -- clients won't see this

## Step 2: Create Client Portals
For each client:
1. Create a new Page called "[Client Name] Portal"
2. Set the page icon to their logo or brand color
3. Share ONLY this page with the client (not your full workspace)

## Step 3: Import Databases
Import each CSV from 01_CLIENT_PORTAL_DATABASES:
- `Client_Master_Database.csv` -- Internal client tracking (don't share with clients)
- `Project_Tracker.csv` -- Share with clients (filtered to their projects only)
- `Content_Calendar.csv` -- Share with clients for content approval
- `Invoice_and_Payments.csv` -- Internal only
- `Analytics_Report_Log.csv` -- Internal tracking

## Step 4: Client Portal Page Structure
Each client portal should have:
```
[Client Name] Portal
  |-- Welcome & Quick Links
  |-- Content Calendar (linked database, filtered to this client)
  |-- Project Status (linked database, filtered to this client)
  |-- Monthly Reports (archived reports)
  |-- Deliverables (file uploads)
  |-- Brand Assets (their logos, colors, fonts)
  |-- Meeting Notes
```

## Step 5: Set Up Sharing
- Click Share on the client portal page
- Enter client's email address
- Set permission to "Can Comment" (so they can approve content)
- Do NOT give "Full Access" -- clients shouldn't edit your databases

## Step 6: Content Approval Workflow in Notion
1. Create content as a Notion page inside the Content Calendar database
2. Set status to "Ready for Review"
3. Client opens the page and leaves a comment: "Approved" or feedback
4. You update status to "Approved" or "Needs Revision"

## Notion Features to Use
- **Synced Blocks**: Same content block appears on multiple pages
- **Database Filters**: Show clients only their projects/content
- **Database Views**: Give clients a clean Calendar view of their content
- **Comments**: Client approvals tracked as comments on content pages
- **Notion AI**: Generate content ideas, draft reports, summarize meetings

## Common Questions
Q: Can clients accidentally see other clients' data?
A: No -- share only their specific Portal page, not the databases directly.

Q: How do clients approve content?
A: They comment on the content page in Notion. Set up a "Needs Approval" status and the client changes it to "Approved".
""")
print(f"  md 07_SETUP_GUIDES/Notion_Portal_Setup_Guide.md")
print("  ✓ 07_SETUP_GUIDES")

# 08 Bonus Templates
wb=Workbook()
ws=wb.active; ws.title="Agency KPI Dashboard"
hr_row(ws,1,[1,2,3,4,5],["KPI","Target","Current","% to Goal","Trend"])
wd(ws,{"A":30,"B":15,"C":15,"D":12,"E":10})
kpis=[
    ["Monthly Recurring Revenue (MRR)","$20,000","$18,000","90%","Up"],
    ["Total Active Clients","10","9","90%","Stable"],
    ["Average Revenue per Client","$2,000","$2,000","100%","Stable"],
    ["Client Retention Rate","95%","100%","105%","Up"],
    ["Net Promoter Score (NPS)","70+","75","107%","Up"],
    ["Avg Content Approval Rate","90%","87%","97%","Stable"],
    ["Report Delivery On Time","100%","100%","100%","Stable"],
    ["New Clients This Month","1","1","100%","On Track"],
    ["Churned Clients This Month","0","0","100%","On Track"],
    ["Avg Client Tenure (months)","18","14","78%","Growing"],
]
for i,r in enumerate(kpis):
    bg=LGR if i%2==0 else WHT; dr(ws,i+2,[1,2,3,4,5],r,bg)
wb.save(BASE+"08_BONUS_TEMPLATES/Agency_KPI_Dashboard.xlsx")
print("  xlsx 08_BONUS_TEMPLATES/Agency_KPI_Dashboard.xlsx")

make_pdf(BASE+"Notion_Client_Portal_Guide.pdf",
    "Notion Client Portal for Agencies - Setup Guide",
    "Your complete guide to setting up and using this Notion Client Portal system",
    [
        ("What's Included",[("*","5 Notion-importable CSV databases"),("*","Project management templates"),("*","Client onboarding workbook"),("*","Monthly report template"),("*","Communication SOPs"),("*","Canva pitch deck"),("*","Complete setup guide"),]),
        ("Why Notion for Client Portals",[("*","Free for clients (they don't need a paid plan to comment and view)"),("*","Beautiful, customizable layout with your brand colors"),("*","Real-time collaboration -- no email attachments"),("*","Clients can approve content with a comment"),("*","Everything in one place: strategy, content, reports, communication"),]),
        ("Getting Started in 30 Minutes",[("*","Step 1: Import all 5 CSV files into your Notion workspace (10 min)"),("*","Step 2: Create your first client portal page using the structure guide (10 min)"),("*","Step 3: Share the page with your first client (5 min)"),("*","Step 4: Send your client the welcome message template (5 min)"),]),
    ])
print("✓ PDF done")

all_files=[]
for root,dirs,files in os.walk(BASE):
    dirs.sort()
    for f in sorted(files):
        full=os.path.join(root,f); rel=os.path.relpath(full,BASE)
        all_files.append([rel,f.split('.')[-1].upper(),f"{os.path.getsize(full)/1024:.1f} KB"])
with open(BASE+"Asset_Manifest.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["File","Type","Size"]); w.writerows(all_files)
with open(BASE+"Asset_Manifest.json","w") as f:
    json.dump({"product":"Notion Client Portal for Agencies","total_files":len(all_files)},f)

etsy="""TITLE:
Notion Client Portal for Agencies | Client Management System | 5 Databases | Canva Templates | Editable

DESCRIPTION:
Give your agency clients a premium, professional client experience with this complete Notion-based client portal system. Stop sending files via email -- centralize everything in a beautiful, branded workspace.

WHAT'S INCLUDED:

CLIENT PORTAL DATABASES (5 CSV files - import directly to Notion):
- Client Master Database (track all clients, packages, MRR, status)
- Project Tracker (all deliverables with status, due dates, owners)
- Content Calendar (post planning with approval workflow)
- Invoice and Payments Log
- Analytics Report Log

PROJECT MANAGEMENT TEMPLATES (CSV):
- Sprint Board template
- Deliverables Tracker

CLIENT ONBOARDING:
- Complete onboarding workbook (brand discovery, audience, goals, access)

REPORTING TEMPLATES:
- Professional monthly report template (platform metrics, top content, next month strategy)

COMMUNICATION HUB:
- Agency-client communication SOP (response times, monthly rhythm, content approval workflow)

CANVA TEMPLATES:
- Client Portal Overview Deck (3 slides, PPTX - import to Canva)

SETUP GUIDES:
- Complete Notion setup guide (step-by-step, 6 pages)

BONUS:
- Agency KPI Dashboard (XLSX)

PERFECT FOR:
- Social media agencies wanting professional client portals
- Marketing agencies tired of email chains
- Freelancers ready to impress clients with a polished system
- OBMs and VAs wanting a client-facing workspace
- Any agency wanting to reduce client confusion and increase retention

HOW IT WORKS:
1. Import CSVs to Notion
2. Create a portal page for each client
3. Share ONLY their page with them
4. Clients approve content, view reports, and communicate -- all in one place

FORMATS: CSV (Notion), DOCX, XLSX, PDF, PPTX (Canva), MD (Markdown)

INSTANT DIGITAL DOWNLOAD

TAGS:
notion template, client portal, agency client management, notion client portal, social media agency, project management notion, client management system, notion database, agency templates, client onboarding, notion agency, content calendar notion, crm notion, client dashboard, agency toolkit"""

with open(ETSY_DIR+"12_NotionPortal_Listing.txt","w",encoding="utf-8") as f: f.write(etsy)
print("  etsy 12_NotionPortal_Listing.txt")

ZIP_PATH="/home/user/oqul-phase55-production/notion-client-portal/BUYER_DOWNLOAD_NotionClientPortal.zip"
with zipfile.ZipFile(ZIP_PATH,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        dirs.sort()
        for f in sorted(files):
            full=os.path.join(root,f); z.write(full,os.path.relpath(full,os.path.dirname(BASE)))
print(f"✓ ZIP: {ZIP_PATH} ({os.path.getsize(ZIP_PATH)/1024/1024:.1f} MB)")
print("\n=== NOTION CLIENT PORTAL COMPLETE ===")
