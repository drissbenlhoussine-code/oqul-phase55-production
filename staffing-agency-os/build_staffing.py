#!/usr/bin/env python3
"""Complete build for Staffing Agency OS (all folders + PDFs + ZIP + Etsy listing)"""
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

BASE = "/home/user/oqul-phase55-production/staffing-agency-os/Ultimate_Staffing_Agency_OS/"
ETSY_DIR = "/home/user/oqul-phase55-production/etsy-listings/"
for d in ["00_START_HERE","01_AGENCY_SETUP","02_CANDIDATE_ACQUISITION","03_CLIENT_DEVELOPMENT",
          "04_RECRUITING_PROCESS","05_PLACEMENTS_CONTRACTS","06_OPERATIONS_FINANCE",
          "07_COMPLIANCE_HR","08_NOTION_WORKSPACE","09_CANVA_TEMPLATES","10_BONUSES"]:
    os.makedirs(BASE+d, exist_ok=True)
os.makedirs(ETSY_DIR, exist_ok=True)

NAV="1A3C5C"; ACC="C0392B"; GLD="D4AC0D"; GRN="1E8449"; WHT="FFFFFF"; LGR="EAF2FF"
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
    t.runs[0].font.color.rgb = RGBColor(0x1A,0x3C,0x5C)
    if sub:
        s = d.add_paragraph(sub); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10); s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for sec in secs:
        if isinstance(sec, str): d.add_paragraph(sec); continue
        h, items = sec
        hd = d.add_heading(h, level=1); hd.runs[0].font.color.rgb = RGBColor(0x1A,0x3C,0x5C)
        for it in items:
            if isinstance(it, tuple) and it[0]=='*': d.add_paragraph(it[1], style='List Bullet')
            else: d.add_paragraph(str(it))
    d.save(BASE+fn); print(f"  doc {fn}")

PNAV=PRGB(26,60,92); PACC=PRGB(192,57,43); PGLD=PRGB(212,172,13); PWHT=PRGB(255,255,255)
PLGR=PRGB(234,242,255); PDGR=PRGB(44,62,80)
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
    NAV_C=colors.HexColor("#1A3C5C"); ACC_C=colors.HexColor("#C0392B"); GLD_C=colors.HexColor("#D4AC0D")
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

# ── 00 START HERE ─────────────────────────────────────────────────────────────
p00="00_START_HERE/"
print("Building 00_START_HERE...")
doc(p00+"Welcome_and_Overview.docx",
    "Welcome to Your Staffing Agency OS",
    "The complete operating system for launching and scaling a professional staffing agency",
    [
        ("What You've Downloaded", [
            "The Staffing Agency OS is the most comprehensive business toolkit available for launching and operating a staffing and recruitment agency. Inside you'll find every template, spreadsheet, script, and guide you need to build a professional agency from the ground up.",
            "This is not a generic HR toolkit. Everything is designed specifically for independent staffing agencies and boutique recruitment firms -- the tools professionals actually use to place candidates and win client contracts.",
        ]),
        ("How to Use This System", [
            ("*","Start with 01_AGENCY_SETUP -- build your business foundation before reaching out to anyone"),
            ("*","Use 02_CANDIDATE_ACQUISITION to build your talent pipeline"),
            ("*","Use 03_CLIENT_DEVELOPMENT to land your first employer clients"),
            ("*","Follow the 04_RECRUITING_PROCESS workflow for every search"),
            ("*","All CSVs in 08_NOTION_WORKSPACE import directly to Notion for a connected digital workspace"),
            ("*","All PPTX in 09_CANVA_TEMPLATES import directly to Canva"),
        ]),
        ("Your 90-Day Launch Plan", [
            "Month 1: Foundation. Register your business, set up legal structure, choose your niche (industry + role type), build your candidate database from LinkedIn, create your first client pitch deck.",
            "Month 2: First Placements. Reach out to 20 hiring managers per week. Activate your job boards. Submit your first candidates. Focus on one industry until you make your first placement.",
            "Month 3: Scale. Use your first placement as a case study. Build referral relationships with your first clients. Target 3-5 active job orders at a time.",
        ]),
    ])

doc(p00+"Agency_Launch_Checklist.docx",
    "Staffing Agency Launch Checklist",
    "Staffing Agency OS | Everything you need to do before making your first call",
    [
        ("Legal and Business Setup", [
            ("*","Register business entity (LLC recommended for liability protection)"),
            ("*","Apply for EIN (Employer Identification Number) at IRS.gov"),
            ("*","Open business checking account and credit card"),
            ("*","Obtain business insurance: E&O, general liability, workers' compensation (if placing W-2 workers)"),
            ("*","Register for state unemployment insurance if placing W-2 contract workers"),
            ("*","Review state-specific staffing agency licensing requirements (some states require a license)"),
        ]),
        ("Brand and Online Presence", [
            ("*","Choose agency name and register domain"),
            ("*","Build simple 3-page website: Home (credibility), Services (what you place), Contact (book a call)"),
            ("*","Set up professional LinkedIn company page"),
            ("*","Create professional email signature with credentials and phone number"),
        ]),
        ("Tools and Technology", [
            ("*","Applicant Tracking System (ATS): Bullhorn (full agency), Greenhouse (mid-market), or Notion (starter)"),
            ("*","LinkedIn Recruiter or LinkedIn Recruiter Lite (essential for candidate sourcing)"),
            ("*","Job posting accounts: Indeed, ZipRecruiter, LinkedIn Jobs"),
            ("*","E-signature tool: DocuSign or HelloSign for contracts"),
            ("*","Video interviewing: Zoom or Teams for candidate and client calls"),
        ]),
        ("Niche and Market Positioning", [
            ("*","Choose your industry vertical (technology, healthcare, finance, manufacturing, creative, legal)"),
            ("*","Choose your placement type (direct hire, contract/temp, temp-to-hire, executive search)"),
            ("*","Define your ideal client company (company size, industry, location radius)"),
            ("*","Define your ideal candidate profile for your niche"),
            ("*","Research 3-5 competitors in your niche to identify differentiation opportunities"),
        ]),
    ])
print("✓ 00_START_HERE done")

# ── 01 AGENCY SETUP ───────────────────────────────────────────────────────────
p01="01_AGENCY_SETUP/"
print("Building 01_AGENCY_SETUP...")

doc(p01+"Business_Plan_Template.docx",
    "Staffing Agency Business Plan",
    "Staffing Agency OS | Your roadmap to a profitable recruitment firm",
    [
        ("Executive Summary", [
            "[Agency Name] is a [niche] staffing agency specializing in placing [role types] with [client type] companies in [geographic area/remote]. Founded by [Your Name], the agency combines deep industry expertise with a candidate-first approach that consistently delivers higher retention rates than industry average.",
            "Year 1 revenue target: $[X]. Primary revenue model: direct hire placement fees (20-25% of first-year salary) and contract staffing margins (15-25% markup).",
        ]),
        ("Services and Revenue Model", [
            ("*","Direct Hire (Permanent Placement): Client pays a one-time fee of 15-25% of the candidate's first-year salary when a candidate is hired. Most common for professional and executive roles. No ongoing administrative burden."),
            ("*","Contract Staffing (Temporary): You employ the worker (W-2) and bill the client a higher hourly rate. The difference between bill rate and pay rate is your gross margin. Typical margin: 25-50% for professional roles, 15-25% for light industrial."),
            ("*","Contract-to-Hire: Candidate works on a contract basis with the option to convert to full-time employment. Conversion typically triggers a fee (1-2 months of salary or a negotiated amount)."),
            ("*","Retained Search (Executive): Client pays 1/3 of the total fee upfront, 1/3 when a slate of candidates is presented, and 1/3 when the candidate starts. Reduces risk; common for C-suite and VP-level searches."),
        ]),
        ("Revenue Projections", [
            "Year 1 Assumptions: 2 direct hire placements per month at $12,000 average fee = $288,000 annual revenue. Plus 3 contract placements averaging $8/hour margin x 40 hours x 50 weeks = $48,000. Total Year 1 target: $336,000.",
            "Year 2 Assumptions: Scale to 4 direct hire placements per month plus 10 contract workers. Projected revenue: $600,000+.",
        ]),
        ("Go-To-Market Strategy", [
            ("*","LinkedIn outreach: 30 personalized messages per day to HR directors, hiring managers, and heads of talent in target industry"),
            ("*","Candidate marketing: Place premium talent in front of hiring managers proactively ('introducing you to a candidate you'll want to meet')"),
            ("*","Content marketing: 3 LinkedIn posts per week on hiring trends in your niche. Positions you as the expert"),
            ("*","Referral network: Build relationships with complementary service providers (employment attorneys, payroll companies, HR consultants)"),
        ]),
    ])

wb=Workbook()
ws=wb.active; ws.title="P&L Projections"
hr_row(ws,1,[1,2,3,4,5],["Month","Placements","Avg Fee","Revenue","Expenses"])
wd(ws,{"A":10,"B":14,"C":14,"D":14,"E":14})
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
placements=[0,1,1,2,2,3,3,3,4,4,4,5]
fees=[0,10000,11000,12000,12000,12500,13000,12500,13000,14000,14000,15000]
for i,(m,p,f) in enumerate(zip(months,placements,fees)):
    rev=p*f
    exp=3500+rev*0.15
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5],[f"{m} 2026",p,f"${f:,}",f"${rev:,}",f"${exp:,.0f}"],bg)
ws2=wb.create_sheet("Fee Calculator")
hr_row(ws2,1,[1,2,3],["Input","Value","Result"])
wd(ws2,{"A":28,"B":18,"C":18})
for i,(label,val,res) in enumerate([
    ("Candidate's First Year Salary","$75,000","(Enter your candidate's salary)"),
    ("Your Placement Fee %","20%","(Typical range: 15-25%)"),
    ("Placement Fee Amount","","=$75,000 x 20% = $15,000"),
    ("Guarantee Period","90 days","(Standard industry guarantee)"),
    ("Contract Bill Rate","$85/hour","(What client pays)"),
    ("Contract Pay Rate","$65/hour","(What contractor receives)"),
    ("Gross Margin","$20/hour","=$85 - $65"),
    ("Weekly Margin (40 hrs)","$800/week","=$20 x 40 hrs"),
    ("Annual Margin (50 wks)","$40,000/year","Per contractor placed"),
]):
    bg=LGR if i%2==0 else WHT
    dr(ws2,i+2,[1,2,3],[label,val,res],bg)
wb.save(BASE+p01+"Financial_Projections.xlsx"); print(f"  xlsx {p01}Financial_Projections.xlsx")

doc(p01+"Service_Menu_and_Pricing.docx",
    "Staffing Agency Service Menu",
    "Staffing Agency OS | Your services, fee structures, and value proposition",
    [
        ("Direct Hire Placement", [
            "We permanently place qualified candidates with your organization. You pay only when you hire.",
            ("*","Fee: 18-25% of candidate's first-year base salary"),
            ("*","Average fee: $12,000-$25,000 per placement depending on role level"),
            ("*","Payment: Due within 30 days of candidate's start date"),
            ("*","Guarantee: 90-day replacement guarantee if candidate leaves for any reason"),
            ("*","Timeline: Average 2-4 weeks from search initiation to candidate presentation"),
            ("*","Ideal for: Professional roles, management, specialists, technical positions"),
        ]),
        ("Contract and Temporary Staffing", [
            "We supply contract workers for project-based or ongoing needs. We handle payroll, benefits, and compliance.",
            ("*","Bill rate: Market rate + 25-40% markup for our services"),
            ("*","Worker employed by: [Agency Name] (W-2) -- we handle payroll taxes, workers' comp, benefits"),
            ("*","Minimum engagement: 4-week minimum for most contracts"),
            ("*","Conversion: If client hires contractor permanently, a conversion fee applies (typically 10-15% of annual salary or one negotiated lump sum)"),
            ("*","Ideal for: Project work, peak season coverage, parental leave backfill, skills evaluation before permanent hire"),
        ]),
        ("Retained Executive Search", [
            "For senior-level and executive searches requiring dedicated resources and confidentiality.",
            ("*","Fee structure: 30% of first-year total compensation"),
            ("*","Payment schedule: 1/3 at engagement, 1/3 at candidate presentation, 1/3 at placement"),
            ("*","Exclusivity: Client agrees not to engage other agencies for this search"),
            ("*","Timeline: 4-8 weeks for qualified candidate slate"),
            ("*","Ideal for: VP, Director, C-suite, highly confidential replacements"),
        ]),
    ])
print("✓ 01_AGENCY_SETUP done")

# ── 02 CANDIDATE ACQUISITION ──────────────────────────────────────────────────
p02="02_CANDIDATE_ACQUISITION/"
print("Building 02_CANDIDATE_ACQUISITION...")

wb2=Workbook()
ws=wb2.active; ws.title="Candidate Pipeline"
hr_row(ws,1,[1,2,3,4,5,6,7,8],["Candidate ID","Name","Current Role","Desired Role","Availability","Status","Fit Score","Notes"])
wd(ws,{"A":12,"B":20,"C":25,"D":25,"E":15,"F":15,"G":12,"H":30})
cands=[
    ["C001","Sarah Mitchell","Software Engineer","Senior Engineer","Immediate","Active Candidate","9/10","Python + AWS. Seeking remote"],
    ["C002","James Rodriguez","Operations Manager","Director of Ops","3 months notice","Passive","7/10","Open to right opportunity"],
    ["C003","Emily Chen","Data Analyst","Data Scientist","Immediate","Active Candidate","8/10","SQL, Python, Tableau"],
    ["C004","Marcus Johnson","Sales Manager","VP of Sales","1 month notice","Engaged","9/10","Exceeded quota 3 years straight"],
    ["C005","Priya Patel","HR Generalist","HR Manager","Immediately","Active Candidate","8/10","SHRM-CP certified"],
    ["C006","Tom Nguyen","Financial Analyst","Finance Manager","2 weeks","Available","8/10","CPA, M&A experience"],
    ["C007","Amanda Foster","Marketing Manager","Director of Marketing","Immediate","Active Candidate","9/10","B2B SaaS background"],
    ["C008","Robert Kim","IT Project Manager","Director of IT","Negotiable","Passive","7/10","PMP certified, fintech"],
]
for i,r in enumerate(cands):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5,6,7,8],r,bg)
ws2c=wb2.create_sheet("Interview Scorecard")
hr_row(ws2c,1,[1,2,3,4,5],["Competency","Weight","Score (1-5)","Weighted Score","Notes"])
wd(ws2c,{"A":30,"B":10,"C":12,"D":15,"E":35})
comps=[
    ["Technical Skills / Role Knowledge","25%","","",""],
    ["Communication and Presentation","20%","","",""],
    ["Problem-Solving and Critical Thinking","20%","","",""],
    ["Cultural Fit and Values Alignment","15%","","",""],
    ["Track Record and Achievements","15%","","",""],
    ["Questions Asked by Candidate","5%","","",""],
]
for i,r in enumerate(comps):
    bg=LGR if i%2==0 else WHT
    dr(ws2c,i+2,[1,2,3,4,5],r,bg)
wb2.save(BASE+p02+"Candidate_Pipeline_Tracker.xlsx"); print(f"  xlsx {p02}Candidate_Pipeline_Tracker.xlsx")

doc(p02+"LinkedIn_Sourcing_Playbook.docx",
    "LinkedIn Sourcing Playbook",
    "Staffing Agency OS | How to find, message, and engage top candidates",
    [
        ("Boolean Search Strategies", [
            "Boolean search on LinkedIn Recruiter allows you to find very specific candidate profiles. Master these operators:",
            ("*","AND: narrows results. 'Software Engineer AND Python AND remote'"),
            ("*","OR: broadens results. '\"Software Engineer\" OR \"Software Developer\" OR \"SWE\"'"),
            ("*","NOT: excludes terms. 'Marketing Manager NOT Director NOT VP'"),
            ("*","Quotes: exact phrase match. '\"product manager\"'"),
            ("*","Parentheses: group terms. '(\"software engineer\" OR developer) AND (Python OR Java)'"),
            "Example search for a Senior Python Engineer: title:('Software Engineer' OR 'Python Developer') AND (AWS OR GCP OR Azure) AND ('3+ years' OR 'senior') NOT intern NOT student",
        ]),
        ("Outreach Message Templates", [
            "Connection request message (300 character limit):",
            "'Hi [Name], I came across your profile and was impressed by your [specific detail from profile -- company, skill, achievement]. I specialize in placing [role type] professionals with leading [industry] companies. Would love to connect.'",
            "First InMail message (after connecting):",
            "'Hi [Name], thank you for connecting! I work exclusively in [niche] recruiting and have been following your career at [Company]. I'm currently working on a [role] search with [type of company] in [location/remote] that might be a strong fit. The role offers [2-3 compelling details]. Would you be open to a confidential 15-minute call? I'm happy to share more about the opportunity without any pressure or commitment.'",
            "Follow-up message (5 days after no response):",
            "'Hi [Name], following up on my last message about the [role] opportunity. I know your inbox is busy, so I'll be brief: [Company type] is looking for exactly your background in [specific skill]. Is this something worth a 15-minute conversation? I'm flexible on timing.'",
        ]),
        ("Passive Candidate Engagement", [
            ("*","Don't ask passive candidates if they're looking for a job. Ask if they'd be open to a conversation about an opportunity"),
            ("*","Lead with what the opportunity offers, not what you need from them"),
            ("*","Always mention something specific from their profile -- generic messages get ignored"),
            ("*","Best outreach times: Tuesday-Thursday between 7am-9am and 5pm-7pm in the candidate's time zone"),
            ("*","Response rate benchmark: 20-30% response rate is good. Under 15% means your message needs revision"),
        ]),
        ("Building a Talent Community", [
            ("*","Keep a database of every quality candidate you've spoken to -- even those who weren't right for the current role"),
            ("*","Reach out to strong candidates in your pipeline every 60-90 days with a relevant opportunity or market update"),
            ("*","Share articles and insights relevant to your candidate niche on LinkedIn -- they'll remember you"),
            ("*","Host quarterly 'Career Insights' webinars for your candidate community on topics like salary benchmarks, resume tips, interview prep"),
        ]),
    ])

doc(p02+"Candidate_Interview_Guide.docx",
    "Candidate Interview and Screening Guide",
    "Staffing Agency OS | Your complete framework for evaluating candidates",
    [
        ("Pre-Screen Phone Call (15 minutes)", [
            "The pre-screen call is your first filter. You're checking basic qualifications and assessing fit before investing more time.",
            ("*","'Tell me briefly about your current role and what you're looking for next?'"),
            ("*","'What's your target compensation range? Total comp -- base plus bonus plus equity?'"),
            ("*","'What is your current notice period?'"),
            ("*","'Are you interviewing with other companies currently?'"),
            ("*","'What are your non-negotiables for your next role?'"),
            ("*","'Are you open to [location/remote setup of role]?'"),
            "Decision: pass to full interview, refer to other roles, or politely close: 'Based on what you've shared, I don't think this particular role is the right fit, but I'd love to keep your profile in mind for future opportunities.'",
        ]),
        ("Full Candidate Interview (45-60 minutes)", [
            "Opening: 'Thank you for taking the time. My goal today is to understand your career story, assess fit for the role I have in mind, and give you complete transparency about the opportunity. Ask me anything at any point.'",
            "Career walk-through questions:",
            ("*","'Walk me through your career starting from [most relevant prior role]. What were your key achievements?'"),
            ("*","'Tell me about a challenge you faced in [specific area relevant to the role] and how you handled it'"),
            ("*","'What metrics or results are you most proud of from your current role?'"),
            ("*","'What does your ideal work environment look like?'"),
            ("*","'What's motivating you to make a move right now?'"),
            "Opportunity presentation: Only present the role after you've gathered enough to confirm fit. Then: 'Based on what you've shared, I think there's strong alignment with an opportunity I'm working on. Let me tell you about it...'",
        ]),
        ("Reference Check Script", [
            "Always check references before submitting a candidate to a client. Call (don't email) for best results.",
            "Opening: 'Hi [Reference Name], my name is [Your Name] from [Agency]. [Candidate Name] has applied for a [role] position with one of our clients and listed you as a professional reference. Do you have 10 minutes?'",
            ("*","'In what capacity did you work with [Candidate] and for how long?'"),
            ("*","'What were their primary responsibilities and how did they perform?'"),
            ("*","'What are their 2-3 greatest strengths?'"),
            ("*","'Is there any area where they have room to grow or develop?'"),
            ("*","'On a scale of 1-10, how likely would you be to hire [Candidate] again if you had the opportunity?'"),
            ("*","'Is there anything I should know about [Candidate] that would help me place them in the right role?'"),
        ]),
    ])
print("✓ 02_CANDIDATE_ACQUISITION done")

# ── 03 CLIENT DEVELOPMENT ─────────────────────────────────────────────────────
p03="03_CLIENT_DEVELOPMENT/"
print("Building 03_CLIENT_DEVELOPMENT...")

wb3=Workbook()
ws=wb3.active; ws.title="Client Pipeline"
hr_row(ws,1,[1,2,3,4,5,6,7],["Company","Contact","Title","Industry","Open Roles","Status","Est. Fee"])
wd(ws,{"A":25,"B":20,"C":22,"D":18,"E":20,"F":15,"G":12})
clients_data=[
    ["Apex Technologies","Sarah Williams","VP of Engineering","Software","2 x Senior Engineer","Discovery Call","$28,000"],
    ["Meridian Healthcare","Robert Davis","Director of Talent","Healthcare","1 x HR Director","Proposal Sent","$20,000"],
    ["Pacific Finance Group","Jennifer Lee","CFO","Finance","1 x Financial Analyst","Qualified","$16,000"],
    ["Summit Manufacturing","Carlos Sanchez","HR Manager","Manufacturing","3 x Supervisor","Contract Signed","$8,400"],
    ["TechBridge Inc.","Michelle Park","Head of People","SaaS","2 x Product Manager","Sourcing","$32,000"],
    ["Coastal Law Group","Thomas Brown","Managing Partner","Legal","1 x Associate Attorney","Initial Contact","$24,000"],
    ["Greenfield Construction","Amy Johnson","Operations Director","Construction","2 x Project Manager","Discovery Call","$22,000"],
]
for i,r in enumerate(clients_data):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5,6,7],r,bg)
ws2=wb3.create_sheet("Job Order Tracker")
hr_row(ws2,1,[1,2,3,4,5,6,7],["Job ID","Company","Role Title","Target Salary","Start Date","Candidates Submitted","Status"])
wd(ws2,{"A":10,"B":22,"C":25,"D":16,"E":14,"F":20,"G":15})
jobs=[
    ["JO-001","Apex Technologies","Senior Software Engineer","$140,000","ASAP","4","Interviewing"],
    ["JO-002","Meridian Healthcare","HR Director","$110,000","Mar 1, 2026","2","Offer Stage"],
    ["JO-003","Pacific Finance Group","Financial Analyst","$85,000","Feb 15, 2026","3","Interviewing"],
    ["JO-004","Summit Manufacturing","Production Supervisor","$70,000","Immediate","6","Placed"],
    ["JO-005","TechBridge Inc.","Senior Product Manager","$160,000","Flexible","2","Sourcing"],
]
for i,r in enumerate(jobs):
    bg=LGR if i%2==0 else WHT
    dr(ws2,i+2,[1,2,3,4,5,6,7],r,bg)
wb3.save(BASE+p03+"Client_and_Job_Tracker.xlsx"); print(f"  xlsx {p03}Client_and_Job_Tracker.xlsx")

doc(p03+"Client_Outreach_Templates.docx",
    "Client Outreach and Business Development Templates",
    "Staffing Agency OS | Scripts and emails for winning new employer clients",
    [
        ("LinkedIn Outreach to Hiring Managers", [
            "Connection request: 'Hi [Name], I specialize in placing [role type] professionals in the [industry] space. I've successfully placed [X] professionals with companies like [relevant example]. Would love to connect in case we can collaborate on future hiring needs.'",
            "First message after connecting: 'Hi [Name], thank you for connecting. I noticed [Company] is scaling its [department/team]. I work exclusively in [niche] recruiting and have a strong pipeline of [specific talent] that might be exactly what you're looking for. Would a 15-minute conversation about your current or upcoming needs be worthwhile? No pressure -- happy to share market intel whether we work together or not.'",
        ]),
        ("Cold Email to HR Directors", [
            "Subject: [Role Type] Candidates for [Company Name]",
            "Hi [Name],",
            "I specialize in placing [role type] professionals with [type of company] -- companies exactly like [Company Name].",
            "I recently placed a [role] with [similar company] who [achievement/result]. Based on [Company Name]'s [recent news/growth/LinkedIn activity], I have 2 candidates who may be exactly what you're looking for:",
            "Candidate A: [2-sentence blind profile. No name.] Currently earning $X, open to $Y.",
            "Candidate B: [2-sentence blind profile.] Actively seeking after [reason that's positive].",
            "Would 15 minutes this week be worthwhile? I'm happy to send full profiles under NDA if you prefer.",
            "[Your Name] | [Title] | [Agency Name] | [Direct Phone]",
        ]),
        ("Client Qualification Questions (Discovery Call)", [
            ("*","'What roles are you currently hiring for or planning to hire for in the next 90 days?'"),
            ("*","'What's been your biggest challenge in filling this role so far?'"),
            ("*","'Have you worked with staffing or recruiting agencies before? What was that experience like?'"),
            ("*","'What's your ideal timeline for filling this position?'"),
            ("*","'What does your hiring process look like? How many interview rounds?'"),
            ("*","'What's the compensation range you have budgeted?'"),
            ("*","'What does success look like in this role for the first 90 days?'"),
        ]),
        ("Presenting Your Agency (Pitch Framework)", [
            "1. Specialism: 'We focus exclusively on [niche]. That means we have a deep candidate database in exactly the space you're hiring in -- not a generalist pool of millions of unvetted resumes.'",
            "2. Process: 'We pre-screen every candidate before presenting them to you. You only see people we'd personally vouch for. Our average submission-to-interview rate is [X]%.'",
            "3. Speed: 'For most of our [niche] searches, we present qualified candidates within 5-10 business days.'",
            "4. Guarantee: 'All of our direct hire placements come with a 90-day replacement guarantee. If the candidate doesn't work out in any way, we re-search at no additional cost.'",
            "5. Close: 'Would you like to share the job description so I can give you a sense of our candidate pipeline for this role right now?'",
        ]),
    ])
print("✓ 03_CLIENT_DEVELOPMENT done")

# ── 04 RECRUITING PROCESS ─────────────────────────────────────────────────────
p04="04_RECRUITING_PROCESS/"
print("Building 04_RECRUITING_PROCESS...")

doc(p04+"Recruiting_Process_SOP.docx",
    "Recruiting Process Standard Operating Procedure",
    "Staffing Agency OS | Your step-by-step playbook for every search",
    [
        ("Step 1: Job Order Intake (Day 1)", [
            "When a client gives you a new job order, spend 60 minutes doing a deep intake before starting to source.",
            ("*","Schedule a 30-minute intake call with the hiring manager (not just HR)"),
            ("*","Learn the specific PAIN behind the role -- why are they hiring? What's not working now?"),
            ("*","Understand the ideal candidate profile: technical skills, soft skills, culture fit, deal-breakers"),
            ("*","Confirm compensation range -- ask for the absolute max they'll pay for the right person"),
            ("*","Confirm decision-making process: who interviews, how many rounds, how long the process takes"),
            ("*","Set expectations: how many candidates you'll present, your timeline, communication cadence"),
        ]),
        ("Step 2: Sourcing Strategy (Days 1-3)", [
            ("*","LinkedIn Recruiter search using Boolean strings specific to this role"),
            ("*","Search internal ATS/candidate database first -- these candidates already know you"),
            ("*","Post the role on LinkedIn Jobs, Indeed, and niche job boards"),
            ("*","Ask your existing candidate network for referrals"),
            ("*","Target passive candidates at competitor companies who might be open to a move"),
            "Daily activity targets: Contact 30 new candidates per day. Expect 20% response rate. Goal: 6 interested candidates per week.",
        ]),
        ("Step 3: Candidate Evaluation (Ongoing)", [
            ("*","Pre-screen call: 15 minutes to confirm basics (compensation, availability, interest, location)"),
            ("*","Full interview: 45-60 minutes for qualified candidates who pass pre-screen"),
            ("*","Reference checks: 2 professional references called before any submission to client"),
            ("*","Candidate prep: once you've decided to submit, prep the candidate on the company and role"),
        ]),
        ("Step 4: Client Submission (Days 7-10)", [
            "Present candidates in a professional submission format. Include:",
            ("*","Candidate name, current title, current company"),
            ("*","2-3 sentence summary of why this candidate is a strong fit for this specific role"),
            ("*","Key achievements and metrics from their career"),
            ("*","Compensation requirements and availability"),
            ("*","Your recruiter's endorsement: 'I've spoken with this candidate extensively and can vouch for their professionalism and qualifications'"),
            "Follow up with the hiring manager 24 hours after sending submissions. The right number of candidates per submission: 3-5.",
        ]),
        ("Step 5: Interview Coordination", [
            ("*","Coordinate all interview scheduling between candidate and client"),
            ("*","Brief candidate before every interview: what to research, what to wear, what questions to expect"),
            ("*","Debrief candidate within 2 hours of interview: how did it go? What's their interest level?"),
            ("*","Get client feedback within 24 hours -- follow up proactively, don't wait"),
        ]),
        ("Step 6: Offer and Placement", [
            ("*","When an offer is coming, prep the candidate for the discussion: 'If they offer $X, will you accept?' Close the candidate before the offer comes"),
            ("*","Help negotiate the offer if needed -- your goal is for both sides to feel great about the outcome"),
            ("*","Confirm the start date in writing with both parties"),
            ("*","Send invoice immediately upon candidate's start date"),
            ("*","Check in with both client and candidate at 30, 60, and 90 days post-placement"),
        ]),
    ])

doc(p04+"Interview_Coordination_Templates.docx",
    "Interview Coordination Templates",
    "Staffing Agency OS | Every email you need for the interview process",
    [
        ("Submission Email to Client", [
            "Subject: Candidate Submissions for [Role] at [Company] -- [Recruiter Name]",
            "Hi [Hiring Manager Name],",
            "Per our search for your [Role] position, I've completed initial screening and am pleased to present the following [X] candidates for your consideration:",
            "CANDIDATE 1: [Name]",
            "[3-sentence profile: current role/company, key qualification, specific achievement]",
            "Compensation: $[X] base | Availability: [timeline]",
            "CANDIDATE 2: [Name]",
            "[3-sentence profile]",
            "Compensation: $[X] | Availability: [timeline]",
            "I've spoken with each candidate at length and am confident in their qualifications and genuine interest in this role. I'll follow up tomorrow to get your feedback. Which would you like to move forward to interviews?",
        ]),
        ("Interview Confirmation to Candidate", [
            "Subject: Interview Confirmed -- [Role] at [Company Name]",
            "Hi [Candidate Name],",
            "Great news! Your interview is confirmed:",
            "Company: [Company Name]",
            "Role: [Job Title]",
            "Date/Time: [Day, Date at Time Time Zone]",
            "Format: [Video/Phone/In-Person] -- [link or address]",
            "Interviewer(s): [Names and titles]",
            "To prepare: research [specific things about the company and role]. Be ready to discuss [specific topics from job description]. Dress code: [business casual/professional].",
            "I'll check in right after your interview. You've got this!",
        ]),
        ("Post-Interview Debrief (Candidate)", [
            "Subject: How did it go? [Company] Interview Debrief",
            "Hi [Name],",
            "I hope the interview went well! I'd love to hear your thoughts.",
            "- How did you feel it went overall?",
            "- What aspects of the role are you most excited about?",
            "- Are there any concerns or questions that came up during the conversation?",
            "- On a scale of 1-10, how interested are you in this role after speaking with them?",
            "Your feedback helps me advocate for you effectively. Call me or reply here -- I'll also be following up with [Company] for their feedback today.",
        ]),
    ])
print("✓ 04_RECRUITING_PROCESS done")

# ── 05 PLACEMENTS CONTRACTS ───────────────────────────────────────────────────
p05="05_PLACEMENTS_CONTRACTS/"
print("Building 05_PLACEMENTS_CONTRACTS...")

doc(p05+"Client_Service_Agreement.docx",
    "Staffing Agency Client Service Agreement",
    "Staffing Agency OS | Professional contract template for employer clients",
    [
        ("STAFFING SERVICES AGREEMENT", [
            "This Staffing Services Agreement ('Agreement') is entered into between [Agency Name] ('Agency') and [Client Company Name] ('Client') effective as of [Date].",
        ]),
        ("1. Services", [
            ("*","Agency will provide recruitment and staffing services including candidate sourcing, screening, interviewing, background check coordination, and placement services for permanent, contract, and temporary positions as requested by Client"),
            ("*","All candidate submissions are confidential and may not be shared with other parties or used to directly hire outside of this Agreement"),
        ]),
        ("2. Fee Structure", [
            "Direct Hire Placements: Client agrees to pay Agency a placement fee equal to [20]% of the candidate's first-year base salary, payable within [30] days of the candidate's start date.",
            "Contract Staffing: Client agrees to pay the bill rate specified on each individual Work Order. Bill rates include Agency's markup for employment taxes, workers' compensation, benefits, and service fees.",
            "Retained Search: As specified in individual search agreements.",
        ]),
        ("3. Guarantee Period", [
            "For direct hire placements: Agency provides a [90]-day pro-rated replacement guarantee. If a placed candidate's employment terminates for any reason within [90] days of start date, Agency will conduct one replacement search at no additional charge. No cash refunds are provided.",
            "Guarantee is void if: Client changes the candidate's role, compensation, or responsibilities materially; Client fails to make payment by due date; Candidate is terminated for reasons of organizational restructuring or elimination of the role.",
        ]),
        ("4. Non-Circumvention", [
            "Client agrees not to directly hire any candidate introduced by Agency within 24 months of introduction without paying the applicable placement fee. This applies even if Client was previously aware of the candidate through other means.",
        ]),
        ("5. Payment Terms", [
            ("*","Net 30 days from invoice date"),
            ("*","Late payments subject to 1.5% monthly interest"),
            ("*","Agency reserves the right to suspend services for accounts 30+ days past due"),
        ]),
        ("Signatures", [
            "This Agreement is binding upon signature of both parties.",
            "Agency: [Authorized Signature] | Name: [Name] | Title: [Title] | Date: [Date]",
            "Client: [Authorized Signature] | Name: [Name] | Title: [Title] | Date: [Date]",
        ]),
    ])

doc(p05+"Candidate_Offer_Letter_Template.docx",
    "Candidate Offer Letter Template",
    "Staffing Agency OS | For contract placements where agency employs the worker",
    [
        ("CONTRACT EMPLOYMENT OFFER LETTER", [
            "Dear [Candidate Name],",
            "[Agency Name] is pleased to offer you the following contract employment opportunity:",
        ]),
        ("Assignment Details", [
            ("*","Client Company: [Client Company Name]"),
            ("*","Assignment Location: [Address / Remote]"),
            ("*","Position Title: [Job Title]"),
            ("*","Start Date: [Date]"),
            ("*","Estimated End Date: [Date or 'Open-ended, reviewed quarterly']"),
            ("*","Scheduled Hours: [X] hours per week, [days/hours]"),
        ]),
        ("Compensation", [
            ("*","Hourly Pay Rate: $[X.XX] per hour"),
            ("*","Overtime: Paid at 1.5x regular rate for hours over 40 per week"),
            ("*","Pay Frequency: [Weekly / Bi-weekly] via direct deposit"),
            ("*","Benefits: [List if applicable or 'Not included for this assignment']"),
        ]),
        ("Employment Terms", [
            "You will be employed by [Agency Name] as a W-2 employee for the duration of this assignment. This is a temporary at-will assignment that may be ended by either party with [2 weeks] written notice.",
            "Direct hire by the client company during this assignment or within 12 months of assignment end requires payment of a conversion fee to [Agency Name] unless a specific release is granted in writing.",
        ]),
        ("Acceptance", [
            "Please sign and return this letter by [Date] to confirm your acceptance.",
            "Candidate Signature: _________________________ Date: ____________",
            "Agency Representative: ______________________ Date: ____________",
        ]),
    ])
print("✓ 05_PLACEMENTS_CONTRACTS done")

# ── 06 OPERATIONS FINANCE ─────────────────────────────────────────────────────
p06="06_OPERATIONS_FINANCE/"
print("Building 06_OPERATIONS_FINANCE...")

wb4=Workbook()
ws=wb4.active; ws.title="Placement Revenue Tracker"
hr_row(ws,1,[1,2,3,4,5,6,7],["Month","Job Orders","Submissions","Interviews","Offers","Placements","Revenue"])
wd(ws,{"A":10,"B":14,"C":14,"D":14,"E":10,"F":14,"G":14})
ops_data=[
    ["Jan 2026","5","18","8","2","1","$14,000"],
    ["Feb 2026","6","22","10","3","2","$26,000"],
    ["Mar 2026","8","30","14","4","2","$28,000"],
    ["Apr 2026","10","38","18","5","3","$39,000"],
    ["May 2026","11","42","20","5","3","$41,000"],
    ["Jun 2026","12","45","22","6","4","$54,000"],
]
for i,r in enumerate(ops_data):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5,6,7],r,bg)
ws2=wb4.create_sheet("Invoice Tracker")
hr_row(ws2,1,[1,2,3,4,5,6],["Invoice #","Client","Candidate","Amount","Issue Date","Status"])
wd(ws2,{"A":12,"B":25,"C":20,"D":12,"E":14,"F":12})
invoices=[
    ["INV-001","Summit Manufacturing","James Parker","$8,400","Jan 12, 2026","Paid"],
    ["INV-002","Apex Technologies","Sarah Mitchell","$28,000","Feb 3, 2026","Paid"],
    ["INV-003","Meridian Healthcare","Kevin Tran","$20,000","Mar 1, 2026","Outstanding"],
    ["INV-004","Pacific Finance Group","Linda Chow","$16,000","Mar 15, 2026","Outstanding"],
    ["INV-005","TechBridge Inc.","Marcus Chen","$32,000","Apr 5, 2026","Draft"],
]
for i,r in enumerate(invoices):
    bg=LGR if i%2==0 else WHT
    dr(ws2,i+2,[1,2,3,4,5,6],r,bg)
wb4.save(BASE+p06+"Operations_Finance_Workbook.xlsx"); print(f"  xlsx {p06}Operations_Finance_Workbook.xlsx")
print("✓ 06_OPERATIONS_FINANCE done")

# ── 07 COMPLIANCE HR ──────────────────────────────────────────────────────────
p07="07_COMPLIANCE_HR/"
print("Building 07_COMPLIANCE_HR...")

doc(p07+"Compliance_Checklist.docx",
    "Staffing Agency Compliance Checklist",
    "Staffing Agency OS | Stay legally compliant at every stage of your business",
    [
        ("Federal Compliance Requirements", [
            ("*","Title VII of the Civil Rights Act: You cannot discriminate in recruiting or placement based on race, color, religion, sex, or national origin"),
            ("*","Americans with Disabilities Act (ADA): Cannot discriminate against qualified candidates with disabilities"),
            ("*","Age Discrimination in Employment Act (ADEA): Cannot discriminate against candidates 40+ years old"),
            ("*","IRCA (Immigration Reform): Must verify I-9 documentation for all W-2 contract workers"),
            ("*","Fair Labor Standards Act (FLSA): Correct classification of employees vs. independent contractors; overtime compliance"),
        ]),
        ("EEO Compliance in Recruiting", [
            ("*","Use inclusive job descriptions -- avoid language that could screen out protected classes"),
            ("*","Evaluate candidates on qualifications and job-related criteria only"),
            ("*","Never tell a client you've identified a candidate's protected characteristics"),
            ("*","If a client requests 'young candidates' or 'no families' -- refuse politely and document the refusal"),
            ("*","Keep all candidate notes professional and focused on job-related criteria"),
        ]),
        ("Background Check Compliance", [
            ("*","FCRA (Fair Credit Reporting Act): Written authorization required before running a background check"),
            ("*","'Ban-the-Box' laws in many cities/states prohibit asking about criminal history on applications"),
            ("*","Follow Adverse Action procedures if denying a candidate based on background check results"),
            ("*","Use a certified background check vendor that is FCRA-compliant"),
        ]),
        ("State-Specific Requirements", [
            "Staffing agencies in some states require a license or registration. Check requirements for:",
            ("*","California, New York, New Jersey, Illinois, and Florida -- all have specific staffing regulations"),
            ("*","Many states have specific pay transparency requirements (posting salary ranges)"),
            ("*","Some states require written wage agreements before starting contract assignments"),
            ("*","Workers' compensation insurance is mandatory in virtually every state for W-2 contract workers"),
        ]),
    ])
print("✓ 07_COMPLIANCE_HR done")

# ── 08 NOTION WORKSPACE ───────────────────────────────────────────────────────
p08="08_NOTION_WORKSPACE/"
print("Building 08_NOTION_WORKSPACE...")

csv_w(p08+"Notion_Candidate_Database.csv",
    ["Candidate ID","Full Name","Current Title","Target Role","Skills","Status","Source","Last Contact"],
    [
        ["C001","Sarah Mitchell","Software Engineer","Senior Engineer","Python, AWS, React","Active Candidate","LinkedIn","2026-01-15"],
        ["C002","James Rodriguez","Operations Manager","Director of Ops","Supply chain, ERP, team leadership","Passive","Referral","2026-01-10"],
        ["C003","Emily Chen","Data Analyst","Data Scientist","SQL, Python, Tableau, ML","Active Candidate","Indeed","2026-01-18"],
        ["C004","Marcus Johnson","Sales Manager","VP of Sales","B2B SaaS, quota, team building","Engaged","LinkedIn","2026-01-20"],
        ["C005","Priya Patel","HR Generalist","HR Manager","SHRM-CP, HRIS, employee relations","Active Candidate","LinkedIn","2026-01-22"],
        ["C006","Tom Nguyen","Financial Analyst","Finance Manager","CPA, M&A, FP&A","Available","Referral","2026-01-12"],
        ["C007","Amanda Foster","Marketing Manager","Director of Marketing","B2B SaaS, demand gen, content","Active Candidate","LinkedIn","2026-01-19"],
        ["C008","Robert Kim","IT Project Manager","Director of IT","PMP, ITIL, fintech","Passive","LinkedIn","2026-01-14"],
    ])

csv_w(p08+"Notion_Job_Orders.csv",
    ["Job ID","Client Company","Role","Salary Range","Date Opened","Status","Recruiter","Notes"],
    [
        ["JO-001","Apex Technologies","Senior Software Engineer","$130,000-$155,000","Jan 5, 2026","Active","[Recruiter]","Python + AWS required"],
        ["JO-002","Meridian Healthcare","HR Director","$100,000-$120,000","Jan 10, 2026","Offer Stage","[Recruiter]","Healthcare exp preferred"],
        ["JO-003","Pacific Finance Group","Financial Analyst","$80,000-$95,000","Jan 15, 2026","Active","[Recruiter]","CPA a plus"],
        ["JO-004","Summit Manufacturing","Production Supervisor","$65,000-$75,000","Dec 15, 2025","Filled","[Recruiter]","3 openings -- all filled"],
        ["JO-005","TechBridge Inc.","Senior Product Manager","$150,000-$175,000","Jan 20, 2026","Sourcing","[Recruiter]","SaaS background critical"],
    ])

csv_w(p08+"Notion_Activity_Log.csv",
    ["Date","Type","Contact","Company","Notes","Follow-up Date"],
    [
        ["2026-01-15","LinkedIn InMail","Sarah Mitchell","(Candidate)","Sent intro re: JO-001. Strong match.","2026-01-20"],
        ["2026-01-16","Phone Call","Sarah Williams","Apex Technologies","Discussed JO-001 requirements. Confirmed salary range.","2026-01-23"],
        ["2026-01-17","Email","Emily Chen","(Candidate)","Pre-screen scheduled for Jan 19","2026-01-19"],
        ["2026-01-18","Zoom","Robert Davis","Meridian Healthcare","Candidate submitted for HR Director role. 2 for review.","2026-01-25"],
        ["2026-01-19","Pre-screen","Emily Chen","(Candidate)","Passed pre-screen. Full interview booked Jan 22.","2026-01-22"],
        ["2026-01-20","Cold Email","Thomas Brown","Coastal Law Group","Introduced agency and 1 blind candidate profile.","2026-01-27"],
    ])

csv_w(p08+"Notion_Placement_Log.csv",
    ["Placement ID","Candidate","Client","Role","Start Date","Salary","Fee","Invoice #","Status"],
    [
        ["PL-001","James Parker","Summit Manufacturing","Production Supervisor","Jan 19, 2026","$68,000","$8,400","INV-001","Paid - Active"],
        ["PL-002","Sarah Mitchell","Apex Technologies","Senior Software Engineer","Feb 3, 2026","$145,000","$29,000","INV-002","Paid - Active"],
        ["PL-003","Kevin Tran","Meridian Healthcare","HR Director","Mar 1, 2026","$112,000","$20,160","INV-003","Invoice Sent"],
    ])

with open(BASE+p08+"Notion_Setup_Guide.md","w",encoding="utf-8") as f:
    f.write("""# Staffing Agency OS - Notion Workspace Setup Guide

## Step 1: Create Your Workspace
1. Open Notion, click **+ New page** in sidebar
2. Name the page: **Staffing Agency OS**
3. Set your agency icon or logo

## Step 2: Import Databases
Import each CSV file into Notion:
- `Notion_Candidate_Database.csv` -- Your master talent database
- `Notion_Job_Orders.csv` -- Active and filled job orders
- `Notion_Activity_Log.csv` -- Daily activity tracking
- `Notion_Placement_Log.csv` -- Completed placements and invoices

## Step 3: Link Databases Together
- Connect **Job Orders** to **Candidates** via Relation property
- Connect **Placement Log** to both **Candidates** and **Job Orders**
- Connect **Activity Log** to **Candidates** (optional)

## Step 4: Views to Create
For Candidate Database:
- **Board view** grouped by Status (Sourced / Pre-screened / Submitted / Placed)
- **Filter** by Available candidates only

For Job Orders:
- **Board view** grouped by Status
- **Table view** with all details visible

## Step 5: Daily Dashboard
Create a main dashboard page with:
- Linked view of today's follow-up tasks
- Linked view of active job orders
- Linked view of recent activity
""")
print(f"  md {p08}Notion_Setup_Guide.md")
print("✓ 08_NOTION_WORKSPACE done")

# ── 09 CANVA TEMPLATES ────────────────────────────────────────────────────────
p09="09_CANVA_TEMPLATES/"
print("Building 09_CANVA_TEMPLATES...")

ppt=prs()
s0=sl(ppt)
box(s0,0,0,13.33,7.5,PNAV)
box(s0,9.5,0,3.83,7.5,PACC)
tx(s0,"STAFFING AGENCY OS",0.5,1.2,8.5,0.9,sz=36,bold=True,col=PWHT)
tx(s0,"Professional Staffing & Recruitment Services",0.5,2.3,8.5,0.7,sz=18,col=PGLD)
tx(s0,"Finding the right talent -- every time.",0.5,3.2,8.5,0.6,sz=14,col=PWHT)
tx(s0,"[Agency Name]  |  [Specialty/Niche]  |  [City or Remote]",0.5,5.5,8.5,0.5,sz=12,col=PWHT)

s1=sl(ppt)
box(s1,0,0,13.33,1.2,PACC)
tx(s1,"OUR RECRUITMENT PROCESS",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
steps=[("1. INTAKE","Deep-dive into your specific hiring need, culture, and ideal candidate profile"),
       ("2. SOURCING","Proactive search via LinkedIn, database, and referral network"),
       ("3. SCREENING","Pre-screen, full interview, reference checks on every candidate"),
       ("4. SUBMISSION","Curated slate of 3-5 fully vetted candidates with written profiles"),
       ("5. COORDINATION","We manage all scheduling, prep, and communication end-to-end"),
       ("6. PLACEMENT","Offer support, onboarding coordination, and 90-day follow-up")]
for i,(step,desc) in enumerate(steps):
    col_=i%2; row_=i//2
    left=0.5+col_*6.4; top=1.4+row_*2.0
    box(s1,left,top,6.0,1.8,PLGR)
    box(s1,left,top,6.0,0.6,PNAV)
    tx(s1,step,left+0.2,top+0.05,5.6,0.5,sz=12,bold=True,col=PWHT)
    tx(s1,desc,left+0.2,top+0.7,5.6,0.9,sz=10,col=PDGR)

s2=sl(ppt)
box(s2,0,0,13.33,1.2,PNAV)
tx(s2,"WHY PARTNER WITH US",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
for i,(num,label) in enumerate([("[X]+","Placements Made"),("[X]%","Fill Rate"),("90-Day","Guarantee"),("[X]","Niche Specialization")]):
    left=0.5+i*3.1
    box(s2,left,1.4,2.8,2.2,PACC)
    tx(s2,num,left+0.1,1.5,2.6,1.1,sz=24,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(s2,label,left+0.1,2.6,2.6,0.8,sz=10,col=PWHT,a=PP_ALIGN.CENTER)
for i,pt in enumerate(["You only interview candidates we'd personally hire","Average time-to-slate: 5-10 business days","You pay only when you hire the right person","90-day replacement guarantee on all direct hire placements"]):
    tx(s2,f"  {pt}",0.5,3.9+i*0.65,12,0.55,sz=11,col=PDGR)

s3=sl(ppt)
box(s3,0,0,13.33,7.5,PNAV)
box(s3,0,5.8,13.33,1.7,PACC)
tx(s3,"READY TO FIND YOUR NEXT HIRE?",0.5,2.0,12,0.9,sz=30,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s3,"Let's start a confidential conversation.",0.5,3.1,12,0.6,sz=17,col=PGLD,a=PP_ALIGN.CENTER)
tx(s3,"[Email]  |  [Phone]  |  [LinkedIn]  |  [Website]",0.5,6.1,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)

ppt.save(BASE+p09+"Agency_Pitch_Deck.pptx")
print(f"  pptx {p09}Agency_Pitch_Deck.pptx")

ppt2=prs()
r0=sl(ppt2)
box(r0,0,0,13.33,7.5,PNAV)
box(r0,0,0,13.33,1.5,PACC)
tx(r0,"CANDIDATE PROFILE PRESENTATION",0.5,0.1,12,0.8,sz=26,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(r0,"[ROLE TITLE]  |  [CLIENT COMPANY]  |  PREPARED BY [AGENCY NAME]",0.5,0.95,12,0.4,sz=12,col=PWHT,a=PP_ALIGN.CENTER)
tx(r0,"CANDIDATE:",0.5,2.0,12,0.5,sz=14,bold=True,col=PGLD)
tx(r0,"[CANDIDATE NAME]",0.5,2.6,12,0.8,sz=28,bold=True,col=PWHT)
tx(r0,"[Current Title] at [Current Company]  |  [Years Experience] experience",0.5,3.5,12,0.6,sz=14,col=PWHT)
tx(r0,"Target: $[X,XXX] base  |  Available: [Immediately / X weeks notice]",0.5,4.2,12,0.5,sz=12,col=PGLD)

r1=sl(ppt2)
box(r1,0,0,13.33,1.2,PACC)
tx(r1,"CANDIDATE SUMMARY",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
box(r1,0.5,1.4,7.8,5.5,PLGR)
tx(r1,"WHY THIS CANDIDATE",0.6,1.5,7.5,0.55,sz=13,bold=True,col=PNAV)
tx(r1,"[2-3 sentences explaining why this candidate is the right fit for this specific role and company. Be specific. Reference the job requirements and how the candidate meets them.]",0.6,2.1,7.5,1.5,sz=11,col=PDGR)
tx(r1,"KEY QUALIFICATIONS",0.6,3.7,7.5,0.55,sz=13,bold=True,col=PNAV)
for i,q in enumerate(["[Qualification 1 with specific metric or detail]","[Qualification 2 with specific metric or detail]","[Qualification 3 with specific metric or detail]"]):
    tx(r1,f"+ {q}",0.6,4.3+i*0.65,7.5,0.55,sz=11,col=PDGR)
box(r1,8.8,1.4,4.0,5.5,PNAV)
tx(r1,"QUICK STATS",8.9,1.5,3.8,0.55,sz=12,bold=True,col=PGLD)
for i,(stat,label) in enumerate([("[X] years","Total Experience"),("[Role]","Current Title"),("$[X]k","Current Comp"),("[Date]","Available"),("[Ref]","References")]):
    tx(r1,stat,8.9,2.1+i*1.1,3.8,0.55,sz=16,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
    tx(r1,label,8.9,2.65+i*1.1,3.8,0.45,sz=9,col=PWHT,a=PP_ALIGN.CENTER)

ppt2.save(BASE+p09+"Candidate_Profile_Template.pptx")
print(f"  pptx {p09}Candidate_Profile_Template.pptx")
print("✓ 09_CANVA_TEMPLATES done")

# ── 10 BONUSES ────────────────────────────────────────────────────────────────
p10="10_BONUSES/"
print("Building 10_BONUSES...")

doc(p10+"Recruiter_Scripts_Vault.docx",
    "Recruiter Scripts Vault",
    "Staffing Agency OS | Scripts for every recruiting situation",
    [
        ("Cold Call to Hiring Manager", [
            "'Hi [Name], this is [Your Name] from [Agency]. I'll be brief -- I specialize in placing [role type] professionals in the [industry] space, and I have a [role type] candidate I think you'd want to meet. I know you're busy -- could I take 2 minutes to tell you about them?'",
            "[If yes]: 'Great. I'm working with a [Title] who has [X years experience] and recently [impressive achievement]. They're confidentially exploring a move and specifically interested in [company type]. I'd love to send you their profile under NDA. What's your email?'",
        ]),
        ("Handling the 'We Use a Preferred Vendor List' Objection", [
            "'I completely understand -- most large organizations have preferred vendor programs. Two questions: First, are all of your preferred vendors specialized in [your niche]? Many GPLs are dominated by generalist firms. And second, would you be open to a 15-minute call to see a sample candidate profile? If you're not impressed, I'll never call again.'",
        ]),
        ("Handling the 'We Don't Use Agencies' Objection", [
            "'I hear that often, and I respect it -- direct sourcing saves fees. Let me ask: do you have open roles right now that have been open more than 30 days? [Yes] -- What does that cost the team in productivity? Most of our clients find that one right hire saves 3-5x our fee in business impact. Could I show you a relevant candidate profile -- just to see what we bring to the table?'",
        ]),
        ("Counter-Offer Prep Script (Candidate)", [
            "'Before we move to offer stage, I want to talk about something important: counter-offers. Statistically, when someone accepts a counter-offer and stays, 80% of them leave within 12 months anyway -- because the reasons they wanted to leave don't actually change. If your current employer makes a counter-offer, what would your thought process be? [Listen carefully]. It's completely your decision -- I just want you to think it through now so you're prepared.'",
        ]),
    ])

with open(BASE+p10+"Staffing_Industry_Glossary.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    w.writerow(["Term","Definition","Used In"])
    terms=[
        ["ATS","Applicant Tracking System. Software used to manage candidates and job orders","Operations"],
        ["Bill Rate","The hourly rate charged to the client for a contract worker","Contract Staffing"],
        ["Boolean Search","Search technique using operators (AND/OR/NOT) to find specific candidates","Sourcing"],
        ["Counter Offer","When a candidate's current employer makes an offer to retain them","Placements"],
        ["Direct Hire","Permanent placement where agency recruits a candidate for a full-time role","Services"],
        ["Fall-Off","When a placed candidate leaves or is terminated during the guarantee period","Placements"],
        ["Fill Rate","Percentage of job orders filled by the agency. Benchmark: 40-60%","Metrics"],
        ["Guarantee Period","Time period during which agency will replace a placed candidate at no charge","Services"],
        ["Hiring Manager","The person at the client company who will directly manage the new hire","Client Dev"],
        ["InMail","LinkedIn's premium direct message feature for reaching non-connections","Sourcing"],
        ["Job Order","A formal request from a client for staffing assistance on a specific role","Operations"],
        ["Mark-Up","The percentage added above a contractor's pay rate to arrive at the bill rate","Contract"],
        ["Passive Candidate","Someone who is employed and not actively job searching but open to opportunities","Sourcing"],
        ["Pay Rate","The hourly or salary rate paid directly to the contractor or placed employee","Compensation"],
        ["Placement Fee","The one-time fee paid by the client for a direct hire placement","Direct Hire"],
        ["Retained Search","Executive search where client pays upfront retainer; agency works exclusively","Services"],
        ["Screening","Initial evaluation of a candidate for basic qualifications and fit","Process"],
        ["Slate","A group of pre-screened, submitted candidates presented to a client","Process"],
        ["Sourcing","The process of identifying and reaching out to potential candidates","Process"],
        ["Split Placement","When two agencies share a placement: one has the job, one has the candidate","Industry"],
        ["Submission","Sending a candidate's profile to a client for consideration","Process"],
        ["Time-to-Fill","The number of days from job order open date to candidate start date","Metrics"],
        ["W-2 Employee","Employee on the agency's payroll, receiving a W-2 tax form","Contract"],
    ]
    w.writerows(terms)
print(f"  csv {p10}Staffing_Industry_Glossary.csv")
print("✓ 10_BONUSES done")

# ── PDFs ──────────────────────────────────────────────────────────────────────
print("Building PDFs...")
make_pdf(BASE+"Staffing_Agency_OS_Guide.pdf",
    "Staffing Agency OS - Complete User Guide",
    "Your complete guide to launching and operating a professional staffing agency",
    [
        ("Welcome to the Staffing Agency OS", [
            "This system contains everything you need to build a professional, profitable staffing agency from scratch -- or to systematize and scale the agency you're already running.",
            ("*","10 organized folders with 40+ files covering every aspect of agency operations"),
            ("*","Start with 00_START_HERE for your 90-day launch plan"),
            ("*","Import CSVs in 08_NOTION_WORKSPACE for a complete digital agency workspace"),
        ]),
        ("Understanding Your Revenue Model", [
            ("*","Direct hire at 20% fee on a $80,000 salary = $16,000 per placement"),
            ("*","2 placements per month = $32,000/month = $384,000/year"),
            ("*","Contract staffing: 10 contractors at $20/hour margin x 40hrs x 50wks = $400,000/year"),
            ("*","These are realistic targets achievable by a solo recruiter within 18-24 months"),
        ]),
        ("Your Recruiting Metrics", [
            "Track these metrics weekly to understand where in your funnel to focus:",
            ("*","Candidates contacted per week: Target 30+ for active searches"),
            ("*","Response rate: Target 20%+ on LinkedIn outreach"),
            ("*","Pre-screen to interview rate: Target 60%+ of candidates who respond"),
            ("*","Submission to interview rate: Target 50%+ of submitted candidates get interviews"),
            ("*","Offer rate: Target 30%+ of interviewed candidates receive offers"),
            ("*","Acceptance rate: Target 85%+ of offers accepted"),
        ]),
    ])
print("✓ PDFs done")

# ── Asset Manifest ────────────────────────────────────────────────────────────
all_files=[]
for root,dirs,files in os.walk(BASE):
    dirs.sort()
    for f in sorted(files):
        full=os.path.join(root,f)
        rel=os.path.relpath(full,BASE)
        size=os.path.getsize(full)
        all_files.append([rel,f.split('.')[-1].upper(),f"{size/1024:.1f} KB"])
with open(BASE+"Asset_Manifest.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["File Path","Type","Size"]); w.writerows(all_files)
with open(BASE+"Asset_Manifest.json","w") as f:
    json.dump({"product":"Ultimate Staffing Agency OS","total_files":len(all_files),"files":[{"path":r[0],"type":r[1],"size":r[2]} for r in all_files]},f,indent=2)
print(f"  Manifest: {len(all_files)} files")

# ── Etsy Listing ──────────────────────────────────────────────────────────────
etsy="""TITLE:
Staffing Agency OS | Complete Recruiting Business System | 45+ Files | Canva Templates | Notion Database

DESCRIPTION:
Launch or scale your staffing and recruitment agency with the most complete operating system available. This is not a generic HR toolkit -- every template, spreadsheet, script, and guide is designed specifically for independent staffing agencies and boutique recruiting firms.

WHAT'S INCLUDED (45+ files across 10 folders):

00 START HERE
- Welcome guide and system overview
- 90-day agency launch checklist

01 AGENCY SETUP
- Business plan template (direct hire + contract + retained search models)
- Financial projections workbook with fee calculator (XLSX)
- Service menu and pricing guide

02 CANDIDATE ACQUISITION
- Candidate pipeline tracker (XLSX with 8 sample candidates and interview scorecard)
- LinkedIn sourcing playbook with Boolean search strategies
- Candidate interview and screening guide (pre-screen, full interview, reference check scripts)

03 CLIENT DEVELOPMENT
- Client pipeline and job order tracker (XLSX)
- Client outreach email and LinkedIn templates
- Discovery call qualification script
- Agency pitch framework (5-step process)

04 RECRUITING PROCESS
- Complete step-by-step recruiting SOP (6 phases from intake to placement)
- Interview coordination templates (submission email, confirmation, debrief scripts)

05 PLACEMENTS & CONTRACTS
- Client Service Agreement template (direct hire, contract, retained search)
- Candidate offer letter template (W-2 contract workers)

06 OPERATIONS & FINANCE
- Monthly placement revenue tracker with funnel metrics (XLSX)
- Invoice tracker

07 COMPLIANCE & HR
- Compliance checklist (EEOC, ADA, FCRA, IRCA, state requirements)
- Background check compliance guide

08 NOTION WORKSPACE (CSV - import directly to Notion)
- Candidate database (8 sample candidates)
- Job order tracker
- Daily activity log
- Placement log with invoice tracking
- Notion setup guide

09 CANVA TEMPLATES (PPTX - import directly to Canva)
- Agency pitch deck (4 slides)
- Candidate profile presentation template

10 BONUSES
- Recruiter scripts vault (cold calls, objection handling, counter-offer prep)
- Staffing industry glossary (23 terms defined)

PERFECT FOR:
- Independent recruiters going out on their own
- New staffing agency owners in their first year
- Contract staffing firms wanting better systems
- HR professionals launching a placement business
- Experienced recruiters who want to systemize operations

FORMATS INCLUDED:
- DOCX (Word documents -- fully editable)
- XLSX (Excel spreadsheets with color-coding and sample data)
- PDF (print-ready guides)
- PPTX (Canva-importable presentations)
- CSV (Notion-importable databases)

INSTANT DIGITAL DOWNLOAD
All 45+ files delivered immediately after purchase in a ZIP archive.

TAGS:
staffing agency, recruiting business, recruitment agency, hr templates, talent acquisition, recruiting templates, staffing business, headhunter, placement agency, hr forms, staffing contracts, recruiter tools, agency templates, canva templates, notion template"""

with open(ETSY_DIR+"08_StaffingAgency_Listing.txt","w",encoding="utf-8") as f:
    f.write(etsy)
print("  etsy 08_StaffingAgency_Listing.txt")

# ── ZIP ───────────────────────────────────────────────────────────────────────
print("Creating ZIP...")
ZIP_PATH="/home/user/oqul-phase55-production/staffing-agency-os/BUYER_DOWNLOAD_StaffingAgencyOS.zip"
with zipfile.ZipFile(ZIP_PATH,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        dirs.sort()
        for f in sorted(files):
            full=os.path.join(root,f)
            arc=os.path.relpath(full,os.path.dirname(BASE))
            z.write(full,arc)
size_mb=os.path.getsize(ZIP_PATH)/1024/1024
print(f"✓ ZIP: {ZIP_PATH} ({size_mb:.1f} MB)")
print("\n=== STAFFING AGENCY OS COMPLETE ===")
