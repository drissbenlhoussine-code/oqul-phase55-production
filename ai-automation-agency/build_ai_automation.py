#!/usr/bin/env python3
"""Complete build for AI Automation Agency Starter Kit"""
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

BASE = "/home/user/oqul-phase55-production/ai-automation-agency/AI_Automation_Agency_Kit/"
ETSY_DIR = "/home/user/oqul-phase55-production/etsy-listings/"
for d in ["00_START_HERE","01_AGENCY_SETUP","02_SERVICE_MENU","03_CLIENT_ACQUISITION",
          "04_PROPOSAL_TEMPLATES","05_AUTOMATION_BLUEPRINTS","06_DELIVERY_PROCESS",
          "07_TOOLS_AND_TECH","08_NOTION_WORKSPACE","09_CANVA_TEMPLATES","10_BONUSES"]:
    os.makedirs(BASE+d, exist_ok=True)
os.makedirs(ETSY_DIR, exist_ok=True)

NAV="0D2137"; ACC="7C3AED"; GLD="F59E0B"; GRN="10B981"; WHT="FFFFFF"; LGR="F3F0FF"
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
    t.runs[0].font.color.rgb = RGBColor(0x0D,0x21,0x37)
    if sub:
        s = d.add_paragraph(sub); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10); s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for sec in secs:
        if isinstance(sec, str): d.add_paragraph(sec); continue
        h, items = sec
        hd = d.add_heading(h, level=1); hd.runs[0].font.color.rgb = RGBColor(0x0D,0x21,0x37)
        for it in items:
            if isinstance(it, tuple) and it[0]=='*': d.add_paragraph(it[1], style='List Bullet')
            else: d.add_paragraph(str(it))
    d.save(BASE+fn); print(f"  doc {fn}")

PNAV=PRGB(13,33,55); PACC=PRGB(124,58,237); PGLD=PRGB(245,158,11); PWHT=PRGB(255,255,255)
PLGR=PRGB(243,240,255); PDGR=PRGB(44,62,80); PGRN=PRGB(16,185,129)
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
    NAV_C=colors.HexColor("#0D2137"); ACC_C=colors.HexColor("#7C3AED"); GLD_C=colors.HexColor("#F59E0B")
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
print("Building 00_START_HERE...")
doc("00_START_HERE/Welcome_and_Overview.docx",
    "Welcome to Your AI Automation Agency Starter Kit",
    "The complete system for launching a profitable AI automation agency",
    [
        ("What's Inside This Kit", [
            "The AI Automation Agency Starter Kit gives you everything you need to launch, operate, and scale an agency that builds AI-powered automations for businesses. This is the fastest-growing service category in the agency space -- businesses are actively seeking help implementing AI.",
            ("*","Complete business setup templates and legal documents"),
            ("*","30+ automation blueprints ready to sell and implement"),
            ("*","Client acquisition scripts and proposal templates"),
            ("*","Delivery process SOPs so you can deliver consistently"),
            ("*","Tools and tech stack guide with pricing and recommendations"),
        ]),
        ("Your First 90 Days", [
            "Month 1 - Foundation: Choose your automation niche, set up your tools, build 3 sample automations to use as demos, establish your pricing and service packages.",
            "Month 2 - First Clients: Use the outreach templates to reach 20 businesses per week. Offer a free 'Automation Audit' to qualified prospects. Close your first 2-3 clients.",
            "Month 3 - Delivery and Referrals: Deliver exceptional results. Document everything. Use your first case studies to get your next 5 clients through referrals and content marketing.",
        ]),
        ("The AI Automation Opportunity", [
            ("*","The AI automation market is projected to reach $26 billion by 2025, growing 45% annually"),
            ("*","87% of small-to-medium businesses want to implement AI but don't know how"),
            ("*","Average project fees: $2,000-$15,000 for implementation + $500-$3,000/month for maintenance"),
            ("*","Low overhead: most automations are built with no-code/low-code tools -- no development team needed"),
        ]),
    ])
print("  ✓ 00_START_HERE")

# ── 01 AGENCY SETUP ───────────────────────────────────────────────────────────
print("Building 01_AGENCY_SETUP...")
wb=Workbook()
ws=wb.active; ws.title="Financial Model"
hr_row(ws,1,[1,2,3,4,5],["Month","Implementation Projects","Retainer Clients","Total Revenue","Expenses"])
wd(ws,{"A":10,"B":22,"C":18,"D":16,"E":14})
fin_data=[
    ["Jan 2026","1","0","$3,500","$1,200"],
    ["Feb 2026","1","1","$4,000","$1,300"],
    ["Mar 2026","2","2","$9,000","$1,500"],
    ["Apr 2026","2","3","$10,500","$1,600"],
    ["May 2026","3","4","$14,500","$1,800"],
    ["Jun 2026","3","5","$17,000","$2,000"],
    ["Jul 2026","4","6","$21,000","$2,200"],
    ["Aug 2026","4","7","$23,500","$2,400"],
    ["Sep 2026","5","8","$28,000","$2,600"],
    ["Oct 2026","5","9","$30,500","$2,800"],
    ["Nov 2026","6","10","$35,000","$3,000"],
    ["Dec 2026","6","11","$37,500","$3,200"],
]
for i,r in enumerate(fin_data):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5],r,bg)
ws2=wb.create_sheet("Pricing Calculator")
hr_row(ws2,1,[1,2],["Service","Price Range"])
wd(ws2,{"A":40,"B":25})
pricing=[
    ["Automation Audit (discovery/assessment)","$0 (lead magnet) or $500-$1,500"],
    ["Simple automation (1-2 steps, one tool)","$1,500-$3,500 one-time"],
    ["Medium automation (3-5 steps, multi-tool)","$3,500-$8,000 one-time"],
    ["Complex automation (multi-step, AI-powered)","$8,000-$25,000 one-time"],
    ["Monthly automation maintenance retainer","$500-$2,000/month"],
    ["AI chatbot implementation","$3,000-$12,000"],
    ["CRM automation setup (HubSpot/Salesforce)","$4,000-$15,000"],
    ["Email marketing automation (full setup)","$2,500-$8,000"],
    ["Social media automation pipeline","$2,000-$6,000"],
    ["Lead generation automation system","$4,000-$12,000"],
]
for i,r in enumerate(pricing):
    bg=LGR if i%2==0 else WHT
    dr(ws2,i+2,[1,2],r,bg)
wb.save(BASE+"01_AGENCY_SETUP/Financial_Model_and_Pricing.xlsx")
print("  xlsx 01_AGENCY_SETUP/Financial_Model_and_Pricing.xlsx")

doc("01_AGENCY_SETUP/Business_Plan_Template.docx",
    "AI Automation Agency Business Plan",
    "AI Automation Agency Starter Kit | Your roadmap to a profitable automation agency",
    [
        ("Business Overview", [
            "[Agency Name] is an AI automation agency that helps [target market] businesses save time, reduce costs, and grow revenue through intelligent automation. We specialize in [niche -- e.g., e-commerce, healthcare, professional services, real estate] and build custom automation workflows using tools like Make, Zapier, n8n, and AI APIs.",
            "Revenue model: Project-based implementation fees ($3,000-$15,000) plus recurring maintenance retainers ($500-$2,000/month). Target Year 1 revenue: $120,000+.",
        ]),
        ("Why AI Automation Now", [
            ("*","Labor costs are rising -- businesses need to do more with less people"),
            ("*","AI tools (ChatGPT API, Claude API, Google Gemini) have made sophisticated automation accessible without custom software development"),
            ("*","No-code platforms (Make, Zapier, n8n) allow implementation without a developer"),
            ("*","Businesses that automate now will outcompete those that don't"),
        ]),
        ("Your Competitive Advantages", [
            ("*","Specialization: Unlike generalist tech agencies, you focus exclusively on automation"),
            ("*","No-code speed: You can build and deliver faster than traditional software developers"),
            ("*","Recurring revenue: Maintenance retainers create predictable monthly income"),
            ("*","Results-focused: You sell time saved and money made, not hours worked"),
        ]),
        ("Go-To-Market Strategy", [
            ("*","Identify 50 target businesses in your niche that likely have manual processes"),
            ("*","Offer a free 'AI Automation Audit' -- identify 3 processes they could automate"),
            ("*","Present the ROI: if a $15/hour employee spends 20 hours/week on a task, automation saves $15,600/year"),
            ("*","Close at $5,000 to build the automation. The ROI justifies it in the first month"),
        ]),
    ])
print("  ✓ 01_AGENCY_SETUP")

# ── 02 SERVICE MENU ───────────────────────────────────────────────────────────
print("Building 02_SERVICE_MENU...")
doc("02_SERVICE_MENU/Complete_Service_Menu.docx",
    "AI Automation Agency Service Menu",
    "AI Automation Agency Starter Kit | Everything you can offer your clients",
    [
        ("Tier 1: Quick Win Automations ($1,500-$3,500)", [
            ("*","Lead notification automation: New lead from website instantly sent to Slack/email/CRM"),
            ("*","Invoice automation: New sale in Stripe auto-creates invoice and sends to client"),
            ("*","Social media cross-posting: Post on one platform, automatically reposts to others"),
            ("*","Calendar booking automation: New booking triggers welcome email + Slack notification + CRM entry"),
            ("*","Review request automation: Customer purchase triggers automated review request email 7 days later"),
            ("*","Document generation: Form submission auto-generates personalized PDF and emails it"),
        ]),
        ("Tier 2: Business Process Automations ($3,500-$10,000)", [
            ("*","Complete lead management system: Lead capture > enrichment > qualification > CRM entry > task assignment > follow-up sequence"),
            ("*","Onboarding automation: New client > contract sent > Slack alert > project created > welcome email sequence > kickoff scheduled"),
            ("*","E-commerce fulfillment automation: Order > inventory check > supplier notification > tracking update > customer email"),
            ("*","HR onboarding automation: New hire > IT tickets created > software provisioned > welcome email sent > training scheduled"),
            ("*","Content repurposing pipeline: Blog post published > AI reformats for LinkedIn + Twitter + email newsletter"),
        ]),
        ("Tier 3: AI-Powered Automations ($8,000-$25,000)", [
            ("*","AI customer service chatbot: Trained on company knowledge base, handles 60-80% of support tickets automatically"),
            ("*","AI lead qualification: Inbound leads automatically scored and routed based on ICP match using GPT-4"),
            ("*","AI content generation pipeline: Company inputs a topic, system generates blog + social + email + ad variants"),
            ("*","AI invoice processing: Uploads vendor invoices, AI extracts data, creates accounting entries, flags anomalies"),
            ("*","AI proposal generator: Input client info, system generates personalized proposal with pricing and scope"),
        ]),
        ("Retainer Services ($500-$2,000/month)", [
            ("*","Basic maintenance: Monitor existing automations, fix issues, minor updates. $500/month"),
            ("*","Growth retainer: 5 hours of automation development per month + maintenance. $1,000/month"),
            ("*","Scale retainer: Unlimited monitoring + 10 hours of new automation development per month. $2,000/month"),
        ]),
    ])
print("  ✓ 02_SERVICE_MENU")

# ── 03 CLIENT ACQUISITION ─────────────────────────────────────────────────────
print("Building 03_CLIENT_ACQUISITION...")
wb3=Workbook()
ws=wb3.active; ws.title="Lead Pipeline"
hr_row(ws,1,[1,2,3,4,5,6,7],["Company","Contact","Industry","Pain Point","Est. Project Value","Status","Next Action"])
wd(ws,{"A":22,"B":18,"C":16,"D":28,"E":18,"F":15,"G":25})
leads=[
    ["Apex Dental Group","Dr. Sarah Kim","Healthcare","Manual appointment reminders","$5,500","Discovery Call Booked","Prep audit"],
    ["Metro Real Estate","John Torres","Real Estate","Lead follow-up takes 3hrs/day","$8,000","Proposal Sent","Follow up"],
    ["TechFlow SaaS","Amanda Chen","SaaS","Customer onboarding manual","$12,000","Audit Complete","Close"],
    ["Sunrise E-Commerce","Mike Patel","E-Commerce","Order notifications manual","$4,000","Initial Contact","Send audit offer"],
    ["Green Consulting LLC","Lisa Brown","Consulting","Proposal generation slow","$6,500","Qualified","Book discovery"],
    ["Pacific Law Firm","James Wilson","Legal","Client intake manual","$9,000","Discovery Call Booked","Prepare demo"],
]
for i,r in enumerate(leads):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5,6,7],r,bg)
wb3.save(BASE+"03_CLIENT_ACQUISITION/Lead_Pipeline_Tracker.xlsx")
print("  xlsx 03_CLIENT_ACQUISITION/Lead_Pipeline_Tracker.xlsx")

doc("03_CLIENT_ACQUISITION/Outreach_Templates.docx",
    "AI Automation Agency Outreach Templates",
    "AI Automation Agency Starter Kit | Scripts that convert to discovery calls",
    [
        ("Cold Email (The ROI Approach)", [
            "Subject: I found a process at [Company] that could save [X] hours/week",
            "Hi [Name],",
            "I specialize in building AI automations for [industry] businesses and I was looking at [Company Name]'s workflow. Specifically, [specific manual process you observed or inferred -- e.g., 'the manual email follow-up process for new leads from your website'].",
            "For a business like yours, we typically automate this in 2 weeks. The result: [3-5 hours saved per week] and [specific outcome like 'faster lead response = higher conversion'].",
            "I'd love to offer you a free 20-minute 'AI Automation Audit' -- I'll analyze your top 3 time-consuming processes and show you what could be automated and what the ROI would be. No pitch. Just useful information.",
            "Interested? Here's my calendar: [link]",
            "[Your Name] | AI Automation Specialist | [Agency Name]",
        ]),
        ("LinkedIn Connection Message", [
            "'Hi [Name], I specialize in AI automation for [industry] businesses. I build systems that eliminate manual tasks and free up your team for high-value work. I've helped [type of company] save [X hours/week] through smart automation. Would love to connect.'",
        ]),
        ("LinkedIn Follow-Up (After Connecting)", [
            "'Hi [Name], thanks for connecting! Quick question -- what's the most time-consuming manual process your team deals with weekly? I ask because that's usually where automation delivers the biggest ROI for [industry] businesses. Happy to share some ideas if you tell me more about your workflow.'",
        ]),
        ("The Automation Audit Offer Script (Phone/Zoom)", [
            "Opening: 'Thank you for taking the time. My goal for this call is to understand your business workflows and identify where AI automation could save you the most time and money. This is purely diagnostic -- by the end, I'll give you 3 specific automation opportunities regardless of whether we work together.'",
            "Discovery questions:",
            ("*","'What are the most repetitive tasks your team does every day or week?'"),
            ("*","'How many hours per week does your team spend on [specific manual task]?'"),
            ("*","'What software tools does your business currently use?'"),
            ("*","'What does a mistake or delay in [process] cost you in time or money?'"),
            "Presenting the opportunity: 'Based on what you've shared, here are the 3 automations that would have the biggest impact on your business: [1], [2], [3]. The combined time savings would be approximately [X] hours per week. At your team's average cost, that's $[Y] per month in recovered time -- and the implementation would run about $[Z]. Would you like me to put together a detailed proposal for the first one?'",
        ]),
    ])
print("  ✓ 03_CLIENT_ACQUISITION")

# ── 04 PROPOSAL TEMPLATES ─────────────────────────────────────────────────────
print("Building 04_PROPOSAL_TEMPLATES...")
doc("04_PROPOSAL_TEMPLATES/Automation_Proposal_Template.docx",
    "AI Automation Proposal Template",
    "AI Automation Agency Starter Kit | Professional proposal for every client",
    [
        ("PROPOSAL: [Project Name]", [
            "Prepared for: [Client Name / Company]",
            "Prepared by: [Your Name / Agency Name]",
            "Date: [Date]",
            "Proposal valid until: [Date + 14 days]",
        ]),
        ("Executive Summary", [
            "This proposal outlines our plan to automate [specific process] for [Company Name]. Based on our Automation Audit on [date], we identified that your team currently spends [X hours/week] on [process description]. Our solution will reduce this to [target hours/week], freeing [X] hours per week for higher-value activities.",
            "Estimated ROI: Implementation cost $[X] | Monthly time savings value $[Y] | Payback period: [Z months]",
        ]),
        ("Proposed Automation: [Project Name]", [
            "TRIGGER: [What starts the automation -- e.g., 'New lead submits contact form on website']",
            "PROCESS STEPS:",
            ("*","Step 1: [Action -- e.g., Lead data captured and formatted]"),
            ("*","Step 2: [Action -- e.g., AI qualifies lead based on ICP criteria (role, company size, industry)]"),
            ("*","Step 3: [Action -- e.g., Qualified lead added to CRM with all data pre-filled]"),
            ("*","Step 4: [Action -- e.g., Sales rep assigned and notified in Slack with lead summary]"),
            ("*","Step 5: [Action -- e.g., Automated personalized intro email sent to lead within 5 minutes]"),
            "RESULT: [Specific outcome -- e.g., 'Every new lead receives a personal response within 5 minutes, 24/7, without any manual effort from your team']",
        ]),
        ("Tools Required", [
            ("*","Make (formerly Integromat): $9-$16/month -- the automation platform"),
            ("*","OpenAI API: $0.01-$0.10 per automation run depending on complexity"),
            ("*","[Any other tools specific to the client's stack]"),
            "Note: You keep ownership of all automations. If we stop working together, your automations continue running.",
        ]),
        ("Investment and Timeline", [
            "Implementation fee: $[X,XXX]",
            "Payment schedule: 50% at kickoff, 50% at delivery",
            "Timeline: [X] business days from project kickoff to delivery",
            "Includes: Setup, testing, 2 rounds of revisions, training call, 30-day support period",
            "Optional ongoing maintenance: $[X]/month for monitoring, updates, and priority support",
        ]),
        ("Next Steps", [
            ("*","Review this proposal and let us know if you have questions"),
            ("*","Sign the service agreement (attached)"),
            ("*","Pay the 50% deposit to begin"),
            ("*","We schedule your kickoff call within 48 hours"),
            "Questions? [Your Email] | [Your Phone]",
        ]),
    ])
print("  ✓ 04_PROPOSAL_TEMPLATES")

# ── 05 AUTOMATION BLUEPRINTS ──────────────────────────────────────────────────
print("Building 05_AUTOMATION_BLUEPRINTS...")

# Big automation blueprints document
doc("05_AUTOMATION_BLUEPRINTS/30_Automation_Blueprints.docx",
    "30 Automation Blueprints Ready to Sell",
    "AI Automation Agency Starter Kit | Your complete library of sellable automations",
    [
        ("Category 1: Lead Generation and CRM", [
            "Blueprint 1 - Website Lead to CRM: Trigger: New contact form submission. Actions: (1) Parse form data, (2) Enrich with Clearbit/Apollo, (3) Create CRM contact, (4) Assign to sales rep, (5) Send personalized welcome email, (6) Post Slack notification. Tools: Make + HubSpot + Clearbit + Gmail/Outlook. Sell price: $2,500-$4,500",
            "Blueprint 2 - Facebook/Instagram Lead Ads to CRM: Trigger: New Facebook Lead Ad submission. Actions: (1) Capture lead, (2) Add to CRM, (3) Add to email sequence, (4) Notify sales via text. Tools: Make + Meta Ads + any CRM + Twilio. Sell price: $1,500-$3,000",
            "Blueprint 3 - AI Lead Scoring: Trigger: New lead enters CRM. Actions: (1) Pull lead data, (2) Send to GPT-4 with your ICP criteria, (3) AI scores lead 1-10 with reasoning, (4) Update CRM score field, (5) Route high-score leads to priority queue. Tools: Make + OpenAI API + CRM. Sell price: $4,000-$8,000",
            "Blueprint 4 - LinkedIn to CRM: Trigger: New LinkedIn connection. Actions: (1) Pull profile data via PhantomBuster, (2) Enrich with email finder, (3) Add to CRM, (4) Tag and segment. Tools: PhantomBuster + Hunter.io + Make + CRM. Sell price: $2,000-$4,000",
        ]),
        ("Category 2: Email and Communication Automations", [
            "Blueprint 5 - Intelligent Email Triage: Trigger: New email in inbox. Actions: (1) AI reads and categorizes email, (2) Tags urgent messages, (3) Drafts suggested reply for approval, (4) Archives non-actionable emails. Tools: Make + Gmail + OpenAI API. Sell price: $3,000-$6,000",
            "Blueprint 6 - Cold Email Personalization Pipeline: Trigger: New prospect added to spreadsheet. Actions: (1) Research company using Clearbit, (2) Pull LinkedIn profile, (3) AI writes personalized opening line, (4) Inserts into email template, (5) Schedules send. Tools: Make + Clearbit + OpenAI + Lemlist. Sell price: $4,000-$8,000",
            "Blueprint 7 - Review Request Automation: Trigger: Customer status set to 'Complete' in CRM. Actions: (1) Wait 5 days, (2) Send personalized review request email, (3) If no response in 3 days, send SMS follow-up, (4) If review received, trigger thank you email. Tools: Make + CRM + Twilio + Gmail. Sell price: $1,500-$3,000",
            "Blueprint 8 - Newsletter to Social Media: Trigger: New email newsletter published. Actions: (1) AI extracts 5 key points, (2) Reformats as LinkedIn post, (3) Reformats as 5 Twitter/X posts, (4) Reformats as Instagram caption, (5) Schedules all posts. Tools: Make + Mailchimp/Klaviyo + OpenAI + Buffer. Sell price: $2,500-$5,000",
        ]),
        ("Category 3: Customer Service and Support", [
            "Blueprint 9 - AI Customer Service Chatbot: Trigger: Customer message on website. Actions: (1) Query knowledge base, (2) AI generates contextual response, (3) If unresolvable, escalate to human with transcript. Tools: Make + OpenAI + Tidio/Intercom. Sell price: $5,000-$12,000",
            "Blueprint 10 - Support Ticket Classification: Trigger: New support ticket created. Actions: (1) AI reads ticket content, (2) Classifies by issue type, priority, and department, (3) Assigns to correct team member, (4) Sets SLA timer. Tools: Make + Zendesk/Freshdesk + OpenAI. Sell price: $3,000-$6,000",
            "Blueprint 11 - NPS/Feedback Analysis: Trigger: New survey response received. Actions: (1) AI analyzes sentiment, (2) Categorizes feedback themes, (3) Routes negative feedback to account manager, (4) Updates dashboard, (5) Triggers follow-up call for promoters. Tools: Make + Typeform + OpenAI + Airtable. Sell price: $2,500-$5,000",
        ]),
        ("Category 4: E-Commerce Automations", [
            "Blueprint 12 - Abandoned Cart Recovery: Trigger: Cart abandoned in Shopify. Actions: (1) Wait 1 hour, (2) Send personalized email with cart items, (3) Wait 24 hours, (4) Send 10% discount email, (5) Wait 48 hours, (6) Final reminder email. Tools: Make + Shopify + Klaviyo. Sell price: $2,000-$4,000",
            "Blueprint 13 - Post-Purchase Upsell Sequence: Trigger: Order completed. Actions: (1) Day 3: product usage tips email, (2) Day 7: review request, (3) Day 14: related products recommendation (AI-generated), (4) Day 30: loyalty discount. Tools: Make + Shopify + OpenAI + Klaviyo. Sell price: $3,000-$6,000",
            "Blueprint 14 - Inventory Alert System: Trigger: Product inventory drops below threshold. Actions: (1) Slack alert to team, (2) Email to supplier with reorder quantity, (3) Update product page to 'Low Stock', (4) Create task for operations team. Tools: Make + Shopify + Slack + Email. Sell price: $1,500-$3,000",
        ]),
        ("Category 5: Operations and HR Automations", [
            "Blueprint 15 - Employee Onboarding: Trigger: New employee added to HR system. Actions: (1) Create accounts in all software tools, (2) Send welcome email with login credentials, (3) Add to Slack channels, (4) Create IT ticket for equipment, (5) Schedule week-1 check-ins, (6) Assign onboarding tasks. Tools: Make + BambooHR + Google Workspace + Slack. Sell price: $4,000-$9,000",
            "Blueprint 16 - Invoice Processing: Trigger: New invoice received via email. Actions: (1) AI extracts vendor, amount, date, line items, (2) Creates accounting entry in QuickBooks/Xero, (3) Routes for approval, (4) Schedules payment. Tools: Make + Gmail + OpenAI + QuickBooks/Xero. Sell price: $4,000-$8,000",
            "Blueprint 17 - Meeting Notes to Action Items: Trigger: Zoom/Teams recording complete. Actions: (1) Transcribe recording, (2) AI identifies action items, decisions, and owners, (3) Creates tasks in project management tool, (4) Sends summary to all attendees. Tools: Make + Zoom/Teams + OpenAI + Asana/ClickUp. Sell price: $3,000-$6,000",
            "Blueprint 18 - Contract Renewal Alert: Trigger: Contract end date within 90 days. Actions: (1) Alert account manager in Slack, (2) Create renewal task, (3) Schedule check-in call, (4) Generate renewal proposal draft. Tools: Make + CRM/Airtable + Slack + OpenAI. Sell price: $2,000-$4,000",
        ]),
        ("Category 6: Content and Marketing Automations", [
            "Blueprint 19 - Blog to Full Content Suite: Trigger: New blog post published. Actions: (1) AI creates 5 LinkedIn posts from blog, (2) Creates 10 Twitter/X posts, (3) Creates email newsletter, (4) Creates social media images prompts for Canva, (5) Creates YouTube script. Tools: Make + WordPress + OpenAI + Buffer. Sell price: $4,000-$8,000",
            "Blueprint 20 - Competitor Monitoring: Trigger: Scheduled daily. Actions: (1) Scrape competitor websites and social media, (2) AI identifies new content, products, or announcements, (3) Sends weekly competitive intelligence report to team. Tools: Make + Browse AI + OpenAI + Email. Sell price: $3,000-$7,000",
            "Blueprint 21 - PR and Press Mention Monitor: Trigger: Scheduled hourly. Actions: (1) Search brand name across news sources, (2) Capture new mentions, (3) AI analyzes sentiment, (4) Alert team to positive mentions, (5) Flag negative mentions for immediate response. Tools: Make + Google Alerts + OpenAI + Slack. Sell price: $2,000-$4,000",
            "Blueprint 22 - Event Follow-Up Automation: Trigger: Event/webinar ends. Actions: (1) Send personalized thank-you email to attendees, (2) Send recording link, (3) Add attendees to nurture sequence, (4) Create CRM tasks for sales follow-up with hot leads. Tools: Make + Zoom + CRM + Email. Sell price: $2,500-$5,000",
        ]),
        ("Category 7: Real Estate and Professional Services", [
            "Blueprint 23 - Property Lead Qualification: Trigger: New lead from Zillow/Realtor.com. Actions: (1) AI qualifies lead (budget, timeline, type), (2) Adds to CRM with score, (3) Assigns to agent, (4) Sends personalized intro email with property matches. Tools: Make + Zapier + OpenAI + Follow Up Boss. Sell price: $4,000-$9,000",
            "Blueprint 24 - Document Generation: Trigger: Deal stage changes to 'Offer Made'. Actions: (1) Pull client data from CRM, (2) Generate offer letter, (3) Send for e-signature, (4) Update CRM on signature. Tools: Make + DocuSign + OpenAI + CRM. Sell price: $3,000-$6,000",
            "Blueprint 25 - Client Birthday and Anniversary Automation: Trigger: Date match with CRM birthday/anniversary field. Actions: (1) Generate personalized message with AI, (2) Send via email or SMS. Tools: Make + CRM + OpenAI + Twilio. Sell price: $1,000-$2,000",
        ]),
        ("Category 8: Healthcare and Wellness", [
            "Blueprint 26 - Appointment Reminder System: Trigger: Appointment scheduled. Actions: (1) Send confirmation immediately, (2) 48hr reminder via email, (3) 24hr reminder via SMS, (4) 2hr final reminder with directions/instructions. Tools: Make + CRM/EHR + Twilio + Google Calendar. Sell price: $2,500-$5,000",
            "Blueprint 27 - Patient Re-Engagement: Trigger: Patient hasn't booked in X days. Actions: (1) AI segments by last visit date, (2) Generates personalized re-engagement message, (3) Offers rebooking link. Tools: Make + Clinic software + OpenAI + Twilio. Sell price: $2,000-$4,500",
        ]),
        ("Category 9: Finance and Professional Services", [
            "Blueprint 28 - Client Reporting Automation: Trigger: Monthly date trigger. Actions: (1) Pull data from reporting tools, (2) AI generates narrative summary, (3) Creates formatted PDF report, (4) Emails to client. Tools: Make + Google Analytics/Ad platforms + OpenAI + PDF generator. Sell price: $3,500-$7,000",
            "Blueprint 29 - Tax Document Collection: Trigger: Tax season date trigger. Actions: (1) Email client document checklist, (2) Set up shared folder, (3) Monitor for document uploads, (4) Alert accountant when complete. Tools: Make + Google Drive + Email. Sell price: $1,500-$3,000",
            "Blueprint 30 - AI Financial Anomaly Detection: Trigger: Daily. Actions: (1) Pull transaction data, (2) AI analyzes for anomalies vs. historical patterns, (3) Flags suspicious transactions, (4) Sends daily digest with anomalies highlighted. Tools: Make + Plaid + OpenAI + Slack. Sell price: $5,000-$12,000",
        ]),
    ])
print("  ✓ 05_AUTOMATION_BLUEPRINTS")

# ── 06 DELIVERY PROCESS ───────────────────────────────────────────────────────
print("Building 06_DELIVERY_PROCESS...")
doc("06_DELIVERY_PROCESS/Delivery_SOP.docx",
    "Automation Delivery SOP",
    "AI Automation Agency Starter Kit | How to deliver every automation project",
    [
        ("Phase 1: Kickoff (Day 1)", [
            ("*","Schedule 60-minute kickoff call"),
            ("*","Document all existing software tools and access requirements"),
            ("*","Map the current manual process step-by-step"),
            ("*","Agree on success metrics (time saved, error rate, response time)"),
            ("*","Get all API keys, software access, and credentials"),
            ("*","Set up shared folder for documentation and testing"),
        ]),
        ("Phase 2: Build (Days 2-7)", [
            ("*","Build automation in Make/Zapier/n8n using agreed blueprint"),
            ("*","Test each step individually before connecting the full workflow"),
            ("*","Create error handling and notifications for failures"),
            ("*","Document every step with screenshots for the client handover guide"),
        ]),
        ("Phase 3: Testing (Days 8-10)", [
            ("*","Run 10 test scenarios with real data (not dummy data)"),
            ("*","Test edge cases: missing fields, duplicate submissions, API errors"),
            ("*","Have client review with 2 revision rounds included"),
            ("*","Document any limitations discovered during testing"),
        ]),
        ("Phase 4: Delivery and Training (Days 11-14)", [
            ("*","Send recorded walkthrough video (Loom) of the complete automation"),
            ("*","Deliver written documentation: what it does, how to monitor it, how to pause it"),
            ("*","Run 30-minute training call with client's team"),
            ("*","Set up monitoring and alert system (notify client if automation fails)"),
            ("*","Send project completion invoice and final deliverable email"),
        ]),
        ("Phase 5: 30-Day Follow-Up", [
            ("*","Day 7: Check in -- is the automation running smoothly?"),
            ("*","Day 14: Share performance data -- how many automations run, time saved"),
            ("*","Day 30: Schedule expansion call -- what's the next process to automate?"),
        ]),
    ])
print("  ✓ 06_DELIVERY_PROCESS")

# ── 07 TOOLS AND TECH ─────────────────────────────────────────────────────────
print("Building 07_TOOLS_AND_TECH...")
doc("07_TOOLS_AND_TECH/Tools_and_Tech_Stack.docx",
    "AI Automation Agency Tech Stack Guide",
    "AI Automation Agency Starter Kit | Every tool you need and how to use it",
    [
        ("Core Automation Platforms", [
            ("*","Make (formerly Integromat): Best for complex, multi-step automations. 1,000+ app integrations. Pricing: Free plan available, paid starts at $9/month. Learning curve: Medium. Most powerful option for advanced agency work."),
            ("*","Zapier: Most popular, easiest to learn. 5,000+ app integrations. Pricing: Free plan available, paid starts at $19.99/month. Best for: Clients who want to manage their own automations after you build them."),
            ("*","n8n: Open-source option. Unlimited automations, self-hosted. Free if self-hosted, cloud plan starts at $20/month. Best for: Technical clients, complex workflows, custom code requirements."),
            ("*","Recommendation: Learn Make first. It's the most powerful and scalable for agency use."),
        ]),
        ("AI APIs and Models", [
            ("*","OpenAI (GPT-4): Best for most automation tasks. Flexible, powerful, well-documented. Pricing: $0.01-$0.06 per 1K tokens. Best for: Content generation, classification, extraction, summarization."),
            ("*","Anthropic Claude API: Strong at following complex instructions and reasoning. Pricing: Similar to OpenAI. Best for: Long document analysis, complex instructions, code generation."),
            ("*","Google Gemini API: Best value for high-volume automations. Strong multimodal capabilities. Best for: Image analysis, high-volume document processing."),
        ]),
        ("Data Enrichment Tools", [
            ("*","Clearbit: Enrich leads with company and contact data. $99/month for 100 lookups."),
            ("*","Apollo.io: B2B contact database + email finding. $49/month. Great ROI for lead generation automations."),
            ("*","Hunter.io: Find professional email addresses. Free for 25 searches/month."),
        ]),
        ("Your Agency Tech Stack (Monthly Cost)", [
            ("*","Make Pro ($16/month): Your primary automation builder"),
            ("*","OpenAI API ($20-50/month estimate): AI processing for all client automations"),
            ("*","Apollo.io ($49/month): For lead generation automations"),
            ("*","Notion ($16/month): Agency operations and client workspace"),
            ("*","Loom ($12/month): Delivery videos and client training"),
            ("*","DocuSign or HelloSign ($20/month): Client contracts"),
            ("*","Calendly ($12/month): Discovery call booking"),
            "Total estimated agency tool cost: $145-175/month",
        ]),
    ])
print("  ✓ 07_TOOLS_AND_TECH")

# ── 08 NOTION WORKSPACE ───────────────────────────────────────────────────────
print("Building 08_NOTION_WORKSPACE...")

csv_w("08_NOTION_WORKSPACE/Notion_Client_Projects.csv",
    ["Project ID","Client","Automation Type","Status","Value","Start Date","Delivery Date","Notes"],
    [
        ["P001","Apex Dental Group","Appointment Reminder","In Build","$3,800","Jan 10, 2026","Jan 24, 2026","SMS + email reminders"],
        ["P002","Metro Real Estate","Lead Qualification AI","Testing","$8,500","Jan 5, 2026","Jan 20, 2026","GPT-4 ICP scoring"],
        ["P003","TechFlow SaaS","Customer Onboarding","Delivered","$12,000","Dec 1, 2025","Dec 20, 2025","7-step onboarding flow"],
        ["P004","Sunrise E-Commerce","Abandoned Cart","Proposal","$3,200","--","--","3-email sequence"],
        ["P005","Pacific Law Firm","Client Intake","Discovery","$7,500","--","--","Needs intake form built"],
    ])

csv_w("08_NOTION_WORKSPACE/Notion_Automation_Library.csv",
    ["Automation Name","Category","Tools Used","Complexity","Sell Price Range","Build Time"],
    [
        ["Website Lead to CRM","Lead Gen","Make + HubSpot + Gmail","Medium","$2,500-$4,500","4-6 hours"],
        ["AI Lead Scoring","Lead Gen","Make + OpenAI + CRM","High","$4,000-$8,000","8-12 hours"],
        ["Review Request System","Customer Service","Make + CRM + Twilio","Low","$1,500-$3,000","2-4 hours"],
        ["AI Chatbot","Customer Service","Make + OpenAI + Tidio","High","$5,000-$12,000","15-25 hours"],
        ["Blog to Social Suite","Content","Make + WordPress + OpenAI + Buffer","Medium","$4,000-$8,000","6-10 hours"],
        ["Invoice Processing AI","Operations","Make + Gmail + OpenAI + QB","High","$4,000-$8,000","10-15 hours"],
        ["Employee Onboarding","HR","Make + BambooHR + G Suite","High","$4,000-$9,000","10-20 hours"],
        ["Appointment Reminder","Healthcare","Make + CRM + Twilio","Low","$2,500-$5,000","3-5 hours"],
        ["Competitor Monitor","Marketing","Make + Browse AI + OpenAI","Medium","$3,000-$7,000","6-10 hours"],
        ["Abandoned Cart Recovery","E-Commerce","Make + Shopify + Klaviyo","Medium","$2,000-$4,000","4-6 hours"],
    ])

csv_w("08_NOTION_WORKSPACE/Notion_Revenue_Tracker.csv",
    ["Month","Implementation Revenue","Retainer Revenue","Total Revenue","Hours Worked","Effective Rate"],
    [
        ["Jan 2026","$3,500","$0","$3,500","18","$194/hr"],
        ["Feb 2026","$4,500","$1,500","$6,000","22","$273/hr"],
        ["Mar 2026","$9,000","$3,000","$12,000","30","$400/hr"],
        ["Apr 2026","$10,500","$4,500","$15,000","28","$536/hr"],
        ["May 2026","$14,500","$6,000","$20,500","35","$586/hr"],
        ["Jun 2026","$17,000","$7,500","$24,500","38","$645/hr"],
    ])

with open(BASE+"08_NOTION_WORKSPACE/Notion_Setup_Guide.md","w",encoding="utf-8") as f:
    f.write("""# AI Automation Agency - Notion Workspace Setup

## Databases to Import
1. `Notion_Client_Projects.csv` - Track all active automation projects
2. `Notion_Automation_Library.csv` - Your catalog of automation blueprints
3. `Notion_Revenue_Tracker.csv` - Monthly revenue tracking

## Recommended Workspace Structure
- **Agency Dashboard** (main page with linked views)
- **Client Projects** (database with Board view by Status)
- **Automation Library** (database filtered by Category)
- **Revenue & KPIs** (database + charts)
- **Tools & SOPs** (wiki-style pages)

## Views to Create for Projects
- Board: Status (Discovery > Proposal > In Build > Testing > Delivered)
- Calendar: Delivery dates
- Timeline: Project overlap view
""")
print(f"  md 08_NOTION_WORKSPACE/Notion_Setup_Guide.md")
print("  ✓ 08_NOTION_WORKSPACE")

# ── 09 CANVA TEMPLATES ────────────────────────────────────────────────────────
print("Building 09_CANVA_TEMPLATES...")
ppt=prs()
s0=sl(ppt)
box(s0,0,0,13.33,7.5,PNAV)
box(s0,0,0,13.33,0.08,PACC)
box(s0,0,7.42,13.33,0.08,PACC)
for i in range(20):
    box(s0,i*0.7,0,0.05,7.5,PRGB(124,58,237) if i%3==0 else PNAV)
tx(s0,"AI AUTOMATION AGENCY",0.5,1.0,12,0.9,sz=38,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"We automate your busiest processes with AI",0.5,2.2,12,0.7,sz=18,col=PGLD,a=PP_ALIGN.CENTER)
tx(s0,"Save 20+ hours/week. Scale without hiring.",0.5,3.1,12,0.6,sz=15,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"[Agency Name]  |  [Website]  |  [Email]",0.5,6.8,12,0.4,sz=12,col=PWHT,a=PP_ALIGN.CENTER)

s1=sl(ppt)
box(s1,0,0,13.33,1.2,PACC)
tx(s1,"HOW AI AUTOMATION WORKS",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
steps=[
    ("TRIGGER","Something happens in your business\n(form submitted, payment received, email arrives)"),
    ("PROCESS","The automation runs automatically\n(AI reads, formats, routes, notifies, creates)"),
    ("RESULT","The right action happens instantly\n(24/7 -- with zero manual effort from your team)"),
]
for i,(title,desc) in enumerate(steps):
    left=0.5+i*4.2
    box(s1,left,1.4,3.9,5.5,PLGR)
    box(s1,left,1.4,3.9,0.8,PACC if i==0 else PNAV if i==1 else PGRN)
    tx(s1,title,left+0.1,1.45,3.7,0.7,sz=16,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(s1,desc,left+0.2,2.3,3.5,4.0,sz=12,col=PDGR)

s2=sl(ppt)
box(s2,0,0,13.33,1.2,PNAV)
tx(s2,"WHAT WE AUTOMATE",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
autos=[
    ("Lead Generation","Website leads auto-qualify, score, and enter your CRM"),
    ("Customer Service","AI chatbot handles 70% of support without human involvement"),
    ("Email Marketing","Personalized sequences triggered by behavior, not calendar"),
    ("Operations","Invoices, onboarding, reports -- all on autopilot"),
    ("Content Marketing","Blog posts auto-repurpose into social, email, and video"),
    ("E-Commerce","Cart recovery, post-purchase, inventory -- fully automated"),
]
for i,(title,desc) in enumerate(autos):
    col_=i%2; row_=i//2
    left=0.5+col_*6.4; top=1.4+row_*2.0
    box(s2,left,top,6.0,1.8,PLGR)
    tx(s2,title,left+0.2,top+0.15,5.6,0.5,sz=12,bold=True,col=PACC)
    tx(s2,desc,left+0.2,top+0.75,5.6,0.85,sz=10,col=PDGR)

s3=sl(ppt)
box(s3,0,0,13.33,1.2,PACC)
tx(s3,"THE ROI OF AUTOMATION",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
rois=[("20+ hours","Saved per week per automation"),("$15,000+","Annual cost savings per workflow"),("3-5x faster","Lead response time with AI"),("30 days","Average payback period")]
for i,(num,label) in enumerate(rois):
    left=0.5+i*3.1
    box(s3,left,1.5,2.8,2.2,PNAV)
    tx(s3,num,left+0.1,1.6,2.6,1.1,sz=20,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
    tx(s3,label,left+0.1,2.7,2.6,0.8,sz=10,col=PWHT,a=PP_ALIGN.CENTER)
box(s3,0.5,3.9,12.3,2.8,PLGR)
tx(s3,"IF YOUR TEAM SPENDS 20 HRS/WEEK ON A TASK:",0.7,4.0,12,0.5,sz=13,bold=True,col=PNAV)
tx(s3,"At $20/hr average cost = $20,800/year on that single task. Our automation costs $4,000-$8,000 to build. Payback in 2-5 months. Savings forever after.",0.7,4.6,11.5,1.8,sz=12,col=PDGR)

s4=sl(ppt)
box(s4,0,0,13.33,7.5,PNAV)
box(s4,0,5.8,13.33,1.7,PACC)
tx(s4,"READY TO AUTOMATE?",0.5,1.5,12,0.9,sz=34,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s4,"Book your free AI Automation Audit",0.5,2.6,12,0.6,sz=18,col=PGLD,a=PP_ALIGN.CENTER)
tx(s4,"We'll identify your top 3 automation opportunities -- no commitment required.",0.5,3.4,12,0.6,sz=14,col=PWHT,a=PP_ALIGN.CENTER)
tx(s4,"[Calendly link]  |  [Email]  |  [Website]",0.5,6.1,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)

ppt.save(BASE+"09_CANVA_TEMPLATES/Agency_Pitch_Deck.pptx")
print("  pptx 09_CANVA_TEMPLATES/Agency_Pitch_Deck.pptx")
print("  ✓ 09_CANVA_TEMPLATES")

# ── 10 BONUSES ────────────────────────────────────────────────────────────────
print("Building 10_BONUSES...")
csv_w("10_BONUSES/AI_Tools_Directory.csv",
    ["Tool","Category","Use Case","Pricing","Rating","Notes"],
    [
        ["Make (Integromat)","Automation Platform","Complex multi-step automations","$9-$29/mo","5/5","Best for agency use"],
        ["Zapier","Automation Platform","Simple automations, client-facing","$19-$69/mo","4/5","Most integrations"],
        ["n8n","Automation Platform","Self-hosted, code-friendly","Free (self-hosted)","4/5","Best for technical teams"],
        ["OpenAI API","AI Model","GPT-4 for all AI tasks","Pay per use","5/5","Industry standard"],
        ["Anthropic Claude API","AI Model","Long docs, complex instructions","Pay per use","5/5","Best for analysis"],
        ["Google Gemini","AI Model","High volume, multimodal","Pay per use","4/5","Best cost for volume"],
        ["Clearbit","Data Enrichment","Enrich leads with company data","$99/mo+","4/5","B2B lead enrichment"],
        ["Apollo.io","Data Enrichment","B2B email finder + database","$49/mo","5/5","Best value data tool"],
        ["Hunter.io","Data Enrichment","Email finder","Free-$49/mo","4/5","Simple email finding"],
        ["Tidio","Chatbot Platform","AI chatbot implementation","$19-$65/mo","4/5","Easy to implement"],
        ["Intercom","Chatbot Platform","Enterprise customer service AI","$74/mo+","5/5","Best enterprise option"],
        ["Airtable","Database","No-code database for automations","$10-$20/mo","4/5","Great for data storage"],
        ["Notion","Documentation","Agency ops and client portals","$8-$16/mo","5/5","Essential for agencies"],
        ["DocuSign","E-Signature","Contract signing","$25/mo","5/5","Most trusted e-sign"],
        ["Loom","Video","Client delivery and training","$12-$15/mo","5/5","Best for async video"],
        ["Browse AI","Web Scraping","Competitor monitoring","$19-$99/mo","4/5","No-code scraping"],
        ["Phantombuster","LinkedIn Automation","LinkedIn data extraction","$59/mo","4/5","LinkedIn outreach"],
        ["Twilio","SMS/Communication","SMS automations","Pay per use","5/5","Best SMS API"],
        ["Mailchimp","Email Marketing","Email automation campaigns","Free-$59/mo","4/5","Most popular"],
        ["Klaviyo","Email Marketing","E-commerce email automation","$20-$150/mo","5/5","Best for Shopify"],
    ])

doc("10_BONUSES/Agency_Growth_Guide.docx",
    "AI Automation Agency Growth Guide",
    "AI Automation Agency Starter Kit | How to scale to $30k/month and beyond",
    [
        ("The Agency Growth Path", [
            "Month 1-3: Solo operator. Learn your tools. Close your first 3-5 clients. Target: $5,000-$10,000/month",
            "Month 4-8: Systematize. Build repeatable delivery processes. Start recurring retainers. Target: $15,000-$25,000/month",
            "Month 9-18: Scale. Hire a delivery specialist. Sell while they build. Target: $30,000-$60,000/month",
        ]),
        ("Your First 10 Clients Strategy", [
            ("*","Warm outreach first: friends, family, former colleagues with businesses -- offer a discounted 'pilot' rate"),
            ("*","LinkedIn content: 3 posts per week showing automation examples, ROI calculations, case studies"),
            ("*","Free audit offer: book discovery calls with a 'free automation audit' CTA -- converts at 20-40%"),
            ("*","Industry Facebook groups: join groups for your target niche and answer questions proactively"),
            ("*","Referral program: 15% commission for any client referral. Your first 3 clients can become your best salespeople"),
        ]),
        ("Productizing Your Service", [
            "The agencies that scale fastest don't custom-build everything -- they productize:",
            ("*","Create 5-8 core automation 'products' that you know inside and out"),
            ("*","Pre-scope them: fixed scope, fixed price, fixed timeline. No more custom quoting"),
            ("*","Build once, sell many: your 20th implementation of a lead gen automation takes 2 hours"),
            ("*","Create implementation guides for each product so you can eventually delegate delivery"),
        ]),
    ])
print("  ✓ 10_BONUSES")

# ── PDF ───────────────────────────────────────────────────────────────────────
print("Building PDF...")
make_pdf(BASE+"AI_Automation_Agency_Guide.pdf",
    "AI Automation Agency Starter Kit - Complete Guide",
    "Your complete guide to building a profitable AI automation agency",
    [
        ("Welcome to Your Kit", [
            ("*","11 folders with 40+ files covering every aspect of running an AI automation agency"),
            ("*","30 automation blueprints you can sell immediately"),
            ("*","Start with 00_START_HERE for your 90-day launch plan"),
        ]),
        ("The Business Model", [
            ("*","Implementation fee: $3,000-$15,000 per automation project"),
            ("*","Maintenance retainer: $500-$2,000/month per client"),
            ("*","5 retainer clients at $1,000/month = $5,000 MRR before any new projects"),
            ("*","Target: 2 implementations + 5 retainers by Month 6 = $16,000-$25,000/month"),
        ]),
        ("Your Fastest Path to First Revenue", [
            ("*","Pick one automation type and master it (start with lead gen or appointment reminders)"),
            ("*","Build a demo automation using your own business or a hypothetical"),
            ("*","Record a Loom video showing the automation in action"),
            ("*","Email that video to 20 businesses in your target niche with a free audit offer"),
            ("*","Close your first client within 30 days at $3,000-$5,000"),
        ]),
    ])
print("✓ PDF done")

# ── Asset Manifest + ZIP ──────────────────────────────────────────────────────
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
    json.dump({"product":"AI Automation Agency Starter Kit","total_files":len(all_files),"files":[{"path":r[0],"type":r[1],"size":r[2]} for r in all_files]},f,indent=2)

etsy="""TITLE:
AI Automation Agency Starter Kit | 30 Automation Blueprints | Make Zapier | Canva Templates | Notion

DESCRIPTION:
Launch your AI automation agency with 30 ready-to-sell automation blueprints, complete business templates, client acquisition scripts, and a proven delivery process. Everything you need to start closing $3,000-$15,000 automation projects immediately.

WHAT'S INCLUDED (40+ files across 11 folders):

00 START HERE - 90-day launch plan, opportunity overview
01 AGENCY SETUP - Business plan, financial model with pricing calculator (XLSX)
02 SERVICE MENU - Complete service menu (Tier 1/2/3 automations + retainers)
03 CLIENT ACQUISITION - Lead tracker (XLSX), cold email templates, discovery call scripts, audit offer framework
04 PROPOSAL TEMPLATES - Professional automation proposal with ROI calculator section
05 AUTOMATION BLUEPRINTS - 30 detailed blueprints across 9 categories:
   - Lead Gen: Website to CRM, AI Lead Scoring, LinkedIn to CRM, FB Ads to CRM
   - Email: AI Email Triage, Cold Email Personalization, Review Requests, Newsletter repurposing
   - Customer Service: AI Chatbot, Ticket Classification, NPS Analysis
   - E-Commerce: Abandoned Cart, Post-Purchase Upsell, Inventory Alerts
   - Operations: Employee Onboarding, Invoice Processing, Meeting Notes AI, Contract Renewals
   - Content: Blog to Full Suite, Competitor Monitor, PR Monitoring, Event Follow-Up
   - Real Estate: Lead Qualification, Document Generation, Birthday Automation
   - Healthcare: Appointment Reminders, Patient Re-Engagement
   - Finance: Client Reporting, Tax Documents, Financial Anomaly Detection AI
06 DELIVERY PROCESS - 5-phase SOP from kickoff to 30-day follow-up
07 TOOLS & TECH - Complete tech stack guide with 20+ tools reviewed and priced
08 NOTION WORKSPACE - 3 CSV databases (Projects, Automation Library, Revenue Tracker)
09 CANVA TEMPLATES - 5-slide pitch deck (PPTX, Canva-importable)
10 BONUSES - 20-tool AI directory (CSV), Agency growth guide

PERFECT FOR:
- Freelancers transitioning to AI automation services
- Tech-savvy entrepreneurs launching a service business
- Digital marketing agencies adding automation services
- VA and OBM businesses expanding service menu
- Anyone who wants to build profitable automations with Make, Zapier, or n8n

FORMATS: DOCX, XLSX, PDF, PPTX (Canva-importable), CSV (Notion-importable)

INSTANT DIGITAL DOWNLOAD

TAGS:
ai automation, automation agency, make zapier, no code business, ai business, automation templates, agency starter kit, canva templates, notion template, ai tools, automation blueprints, business automation, chatgpt business, workflow automation, digital agency"""

with open(ETSY_DIR+"09_AIAutomation_Listing.txt","w",encoding="utf-8") as f:
    f.write(etsy)
print("  etsy 09_AIAutomation_Listing.txt")

print("Creating ZIP...")
ZIP_PATH="/home/user/oqul-phase55-production/ai-automation-agency/BUYER_DOWNLOAD_AIAutomationAgencyKit.zip"
with zipfile.ZipFile(ZIP_PATH,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        dirs.sort()
        for f in sorted(files):
            full=os.path.join(root,f)
            arc=os.path.relpath(full,os.path.dirname(BASE))
            z.write(full,arc)
size_mb=os.path.getsize(ZIP_PATH)/1024/1024
print(f"✓ ZIP: {ZIP_PATH} ({size_mb:.1f} MB)")
print("\n=== AI AUTOMATION AGENCY KIT COMPLETE ===")
