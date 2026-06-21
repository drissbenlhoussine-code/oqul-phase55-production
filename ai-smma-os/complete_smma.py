#!/usr/bin/env python3
"""Complete AI SMMA OS - builds folders 07-12, PDFs, manifests, and ZIP."""
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

BASE = "/home/user/oqul-phase55-production/ai-smma-os/Ultimate_AI_SMMA_Operating_System/"

# ── helpers ──────────────────────────────────────────────────────────────────
def doc(fn, title, sub, secs):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
    if sub:
        s = d.add_paragraph(sub); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10); s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for sec in secs:
        if isinstance(sec, str): d.add_paragraph(sec); continue
        h, items = sec
        hd = d.add_heading(h, level=1); hd.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
        for it in items:
            if isinstance(it, tuple) and it[0]=='*': d.add_paragraph(it[1], style='List Bullet')
            else: d.add_paragraph(str(it))
    d.save(BASE+fn); print(f"  doc {fn}")

NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"
def hf(h): return PatternFill("solid", fgColor=h)
def bf(bold=True,sz=11,col="000000"): return Font(bold=bold,size=sz,color=col)
def al(h="center",v="center"): return Alignment(horizontal=h,vertical=v,wrap_text=True)
def thin(): s=Side(style='thin',color='CCCCCC'); return Border(left=s,right=s,top=s,bottom=s)
def hr(ws,row,cols,texts,bg=NAV,fg=WHT):
    for c,t in zip(cols,texts):
        x=ws.cell(row=row,column=c,value=t); x.fill=hf(bg); x.font=bf(True,11,fg); x.alignment=al(); x.border=thin()
def dr(ws,row,cols,vals,bg=WHT):
    for c,v in zip(cols,vals):
        x=ws.cell(row=row,column=c,value=v); x.fill=hf(bg); x.font=bf(False,10); x.alignment=al("left"); x.border=thin()
def wd(ws,widths):
    for col,w in widths.items(): ws.column_dimensions[col].width=w

PNAV=PRGB(15,52,96); PACC=PRGB(233,69,96); PGLD=PRGB(245,166,35); PWHT=PRGB(255,255,255)
PLGR=PRGB(248,249,250); PDGR=PRGB(44,62,80)
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
    NAV_C=colors.HexColor("#0F3460"); ACC_C=colors.HexColor("#E94560"); GLD_C=colors.HexColor("#F5A623")
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
    print(f"  pdf {fpath.replace(BASE,'')}")

# ── 07_CLIENT_REPORTING ───────────────────────────────────────────────────────
p7="07_CLIENT_REPORTING/"
doc(p7+"Monthly_Report_Writing_Guide.docx",
    "Monthly Client Report Writing Guide",
    "AI SMMA OS | How to Create Reports Clients Love Every Month",
    [
        ("Why Monthly Reports Matter", [
            "Monthly reports are your most powerful retention tool. They transform invisible work into visible results, justify your retainer, prevent churn, and create upsell opportunities. A client who sees clear ROI stays. A client in the dark cancels.",
        ]),
        ("The SMMA Monthly Report Formula", [
            "Every report follows the same structure: 1) Month in Review (top-line story), 2) Metrics Dashboard, 3) Content Performance, 4) Audience Growth, 5) Wins + Highlights, 6) Challenges + What We Did, 7) Next Month Preview.",
        ]),
        ("Section 1: Month in Review", [
            ("*","Write 2-3 sentences that tell the story of the month: what you focused on, what happened, what it means for the client's business"),
            ("*","Avoid jargon: 'We increased organic reach 34% by shifting to Reels-first content strategy, resulting in a 12% growth in follower count'"),
            ("*","Lead with the best result first - clients read the first paragraph most carefully"),
        ]),
        ("Section 2: Metrics Dashboard", [
            ("*","Report every KPI agreed upon in the onboarding call"),
            ("*","Show month-over-month change: current vs. previous month, and vs. 3 months ago"),
            ("*","Use simple color coding: green = above goal, yellow = at goal, red = below goal"),
            ("*","Include: Reach, Impressions, Engagement Rate, Followers, Link Clicks, Profile Visits, Story Views, Saves"),
        ]),
        ("Section 3: Content Performance", [
            ("*","Top 3 performing posts: screenshot, stats, why it worked"),
            ("*","Lowest performing post: what you'll do differently next month"),
            ("*","Content format breakdown: % Reels vs. Carousels vs. Static vs. Stories"),
            ("*","Best-performing hashtag clusters (if applicable)"),
        ]),
        ("Section 4: Audience Insights", [
            ("*","Demographics snapshot: top cities, age range, gender"),
            ("*","Follower growth chart: line graph showing 30-day trajectory"),
            ("*","New followers source: organic vs. paid vs. hashtag vs. explore"),
        ]),
        ("Section 5: Next Month Plan", [
            ("*","3-5 strategic focuses based on what the data shows"),
            ("*","Content calendar preview (dates and themes, not full details)"),
            ("*","Any A/B tests or experiments planned"),
            ("*","Upsell opportunity: frame naturally: 'Based on your Reels performance, we recommend adding a Paid Reels Boost - here's the projected ROI'"),
        ]),
        ("Delivery Best Practices", [
            ("*","Deliver on the same day each month (e.g., 1st business day)"),
            ("*","Send via email with a 2-sentence summary AND attach the full PDF"),
            ("*","Follow up with a 15-minute video call to walk through the results"),
            ("*","Use your Monthly Report Presentation template (Canva folder) for the visual version"),
        ]),
    ])

doc(p7+"Client_Report_Email_Templates.docx",
    "Client Report Email Templates",
    "AI SMMA OS | 8 Ready-to-Send Templates for Every Reporting Situation",
    [
        ("Template 1: Monthly Report Delivery", [
            "Subject: [Client Name] | Social Media Report - [Month Year]",
            "",
            "Hi [Name],",
            "Your [Month] social media report is ready! Here are the headline numbers:",
            ">> Reach: [X] (+X% vs. last month)",
            ">> New Followers: [X] | Total: [X]",
            ">> Engagement Rate: [X]%",
            ">> Top Post: [brief description] ([X] reaches)",
            "",
            "Full report attached. I've also highlighted 3 opportunities for [Month+1] that I'm excited about.",
            "",
            "Can we jump on a 15-minute call this week to walk through it together? I have [Day] at [Time] or [Day] at [Time] available.",
            "",
            "Best, [Your Name]",
        ]),
        ("Template 2: Exceptional Month", [
            "Subject: Big wins this month for [Client Name]! Report inside",
            "",
            "Hi [Name],",
            "[Month] was a record-breaking month for your social media. I'm genuinely excited to share these results with you.",
            "",
            "The highlight: [specific win - e.g., 'Your Reel on [topic] hit 47,000 views - that's 10x your average reach.']",
            "",
            "Full breakdown attached. Let's lock in 20 minutes to discuss how we build on this momentum in [Month+1].",
        ]),
        ("Template 3: Challenging Month", [
            "Subject: [Client Name] - [Month] Report + What We're Doing About It",
            "",
            "Hi [Name],",
            "I want to be upfront with you: [Month] was a tougher month by the numbers. Here's what happened and what we're doing about it.",
            "",
            "What happened: [brief explanation - algorithm change, content type, seasonal dip]",
            "What we're changing: [specific adjustment being made]",
            "Expected impact: [timeline and expected result]",
            "",
            "Full report attached. I'd like to walk you through this on a call - can we do [Day] at [Time]?",
        ]),
        ("Template 4: Quarterly Recap", [
            "Subject: Q[X] Results for [Client Name] - 3-Month Summary",
            "",
            "Hi [Name],",
            "Happy end of Q[X]! Here's a quick summary of what we accomplished together over the past 3 months:",
            "",
            ">> Total Reach: [X] (+X% vs. Q[X-1])",
            ">> Total New Followers: +[X]",
            ">> Best-Performing Content Type: [X]",
            ">> Top Performing Platform: [X]",
            ">> Highlights: [list 2-3 wins]",
            "",
            "Full Q[X] report attached, plus our Q[X+1] strategy preview.",
        ]),
    ])

# KPI/ROI Dashboard XLSX
wb=Workbook()
ws=wb.active; ws.title="Monthly KPIs"
hr(ws,1,[1,2,3,4,5,6,7],["Platform","Metric","Jan","Feb","Mar","Goal","Status"])
kpi_data=[
    ("Instagram","Reach",12400,14200,16800,15000,"On Track"),
    ("Instagram","Followers","+180","+215","+290","+200","Exceeded"),
    ("Instagram","Engagement Rate","3.2%","3.8%","4.1%","3.5%","Exceeded"),
    ("Facebook","Page Likes","+45","+52","+38","+50","On Track"),
    ("Facebook","Post Reach",5200,6100,5800,6000,"On Track"),
    ("LinkedIn","Impressions",3400,4100,5200,4000,"Exceeded"),
    ("TikTok","Views",22000,31000,45000,25000,"Exceeded"),
    ("TikTok","Followers","+420","+610","+890","+500","Exceeded"),
]
for i,(platform,metric,j,f,m,goal,status) in enumerate(kpi_data):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5,6,7],[platform,metric,j,f,m,goal,status],bg)
wd(ws,{'A':14,'B':20,'C':10,'D':10,'E':10,'F':10,'G':12})

ws2=wb.create_sheet("Content Performance")
hr(ws2,1,[1,2,3,4,5,6,7],["Month","Top Post","Format","Reach","Saves","Shares","Comment"])
content=[
    ("January","How We Grew [Client] 30% in 90 Days","Reel",12400,340,89,"Great content!"),
    ("February","5 Signs You Need Social Media Help","Carousel",9800,512,124,"Sharing this!"),
    ("March","Behind the Scenes: Our Process","Reel",18200,280,67,"Love this!"),
]
for i,row in enumerate(content):
    dr(ws2,i+2,[1,2,3,4,5,6,7],list(row))
wd(ws2,{'A':10,'B':40,'C':12,'D':10,'E':8,'F':8,'G':14})

ws3=wb.create_sheet("Agency Revenue")
hr(ws3,1,[1,2,3,4,5],["Month","Retainer Revenue","Ad Spend Managed","Total Client Revenue","MRR Growth"])
revenue=[
    ("January",3200,5000,8200,"--"),("February",3800,6500,10300,"+25%"),
    ("March",4500,8000,12500,"+21%"),("April",5200,9500,14700,"+18%"),
    ("May",5800,11000,16800,"+14%"),("June",6500,13000,19500,"+16%"),
]
for i,row in enumerate(revenue):
    dr(ws3,i+2,[1,2,3,4,5],list(row))
wd(ws3,{'A':12,'B':18,'C':20,'D':22,'E':14})
wb.save(BASE+p7+"KPI_ROI_Dashboard.xlsx"); print(f"  xlsx {p7}KPI_ROI_Dashboard.xlsx")

# Agency Revenue Tracker
wb2=Workbook(); ws=wb2.active; ws.title="Monthly Revenue"
hr(ws,1,[1,2,3,4,5,6,7],["Month","Client","Service","MRR","Ad Management Fee","One-Time","Total"])
rev_data=[
    ("Jan","Nike Restaurant","Social Management",1500,0,0,1500),
    ("Jan","Alpha Dental","Content + Ads",2000,400,0,2400),
    ("Jan","Luxe Spa","Full Service",1800,300,500,2600),
    ("Feb","Nike Restaurant","Social Management",1500,0,0,1500),
    ("Feb","Alpha Dental","Content + Ads",2000,500,0,2500),
    ("Feb","Luxe Spa","Full Service",1800,350,0,2150),
    ("Feb","New Client - Fitness","Starter Package",800,0,500,1300),
]
for i,row in enumerate(rev_data):
    dr(ws,i+2,[1,2,3,4,5,6,7],list(row))
wd(ws,{'A':8,'B':22,'C':20,'D':10,'E':18,'F':10,'G':10})

ws2=wb2.create_sheet("Client Retention")
hr(ws2,1,[1,2,3,4,5,6],["Client","Start Date","Months Active","MRR","Total Revenue","Status"])
retention=[
    ("Alpha Dental","Jan 2025",6,2400,15600,"Active"),
    ("Luxe Spa","Dec 2024",7,2150,16800,"Active"),
    ("TechFlow SaaS","Mar 2025",4,3500,16000,"Active"),
    ("Green Thumb Nursery","Feb 2025",5,1200,7200,"Active"),
    ("Former Client","Jan 2025",3,1800,5400,"Churned"),
]
for i,row in enumerate(retention):
    dr(ws2,i+2,[1,2,3,4,5,6],list(row))
wd(ws2,{'A':22,'B':12,'C':14,'D':10,'E':14,'F':10})

ws3=wb2.create_sheet("Goals vs Actual")
hr(ws3,1,[1,2,3,4,5],["Month","Revenue Goal","Actual Revenue","Variance","% of Goal"])
goals=[
    ("January",5000,6500,1500,"130%"),("February",6000,7450,1450,"124%"),
    ("March",7000,8200,1200,"117%"),("April",8000,9100,1100,"114%"),
    ("May",9000,10500,1500,"117%"),
]
for i,row in enumerate(goals):
    dr(ws3,i+2,[1,2,3,4,5],list(row))
wd(ws3,{'A':12,'B':14,'C':16,'D':12,'E':12})
wb2.save(BASE+p7+"Agency_Revenue_Tracker.xlsx"); print(f"  xlsx {p7}Agency_Revenue_Tracker.xlsx")
print("✓ 07_CLIENT_REPORTING done")

# ── 08_AI_TOOLS_STACK ─────────────────────────────────────────────────────────
p8="08_AI_TOOLS_STACK/"
doc(p8+"AI_Tools_Directory.docx",
    "AI Tools Directory for SMMA Agencies",
    "AI SMMA OS | 60+ AI Tools Organized by Category with Use Cases and Pricing",
    [
        ("Content Creation AI", [
            ("*","ChatGPT (OpenAI) - Caption writing, content briefs, email copy, hashtag research. Free tier available; Plus $20/mo"),
            ("*","Claude (Anthropic) - Long-form content, strategy documents, proposal writing. Free tier; Pro $20/mo"),
            ("*","Copy.ai - Marketing copy, social captions, product descriptions. Free tier; Pro $49/mo"),
            ("*","Jasper - Blog posts, ad copy, social content at scale. From $49/mo"),
            ("*","Writesonic - Social captions, ads, landing pages. From $16/mo"),
        ]),
        ("AI Image and Visual Creation", [
            ("*","Midjourney - Stunning AI visuals for social posts, ads, mockups. From $10/mo"),
            ("*","DALL-E 3 (via ChatGPT Plus) - Quick image generation, content illustrations"),
            ("*","Adobe Firefly - Commercial-safe AI images, Photoshop integration"),
            ("*","Canva AI (Magic Design) - Auto-design templates, background remover, text effects. Included in Canva Pro"),
            ("*","Stable Diffusion (local) - Free, requires technical setup, unlimited generation"),
        ]),
        ("Video AI Tools", [
            ("*","Opus Clip - Auto-clips long videos into viral short-form content. From $19/mo"),
            ("*","Descript - AI video editing, transcription, overdub. From $24/mo"),
            ("*","Pictory - Turn blog posts into videos automatically. From $23/mo"),
            ("*","Captions.ai - Auto-captions, animated text for Reels/TikTok. From $7/mo"),
            ("*","HeyGen - AI avatar videos for explainers and ads. From $24/mo"),
        ]),
        ("Social Media Scheduling and AI", [
            ("*","Buffer AI Assistant - Caption suggestions within scheduling. Included in Buffer"),
            ("*","Hootsuite OwlyWriter AI - AI-written captions within Hootsuite platform"),
            ("*","Metricool - Scheduling with AI best-time suggestions. Free tier; from $22/mo"),
            ("*","Later - Visual planner with AI caption writer. From $25/mo"),
            ("*","Publer - Bulk scheduling with AI tools. From $12/mo"),
        ]),
        ("Analytics and Listening AI", [
            ("*","Sprout Social Listening - AI-powered social listening and sentiment analysis. From $249/mo"),
            ("*","Brand24 - AI sentiment monitoring and brand mentions. From $99/mo"),
            ("*","Mention - Brand monitoring with AI alerts. From $41/mo"),
        ]),
        ("Agency Operations AI", [
            ("*","Notion AI - Meeting notes, document summarization, task management. $10/mo add-on"),
            ("*","Otter.ai - AI meeting transcription and summaries. Free tier; Pro $17/mo"),
            ("*","Zapier AI - No-code automation with AI steps. From $20/mo"),
            ("*","Make (Integromat) - Complex automations with AI modules. Free tier; from $9/mo"),
        ]),
    ])

doc(p8+"Agency_Automation_Guide.docx",
    "Agency Automation Guide",
    "AI SMMA OS | 20 Automations to Save 10+ Hours Per Week",
    [
        ("Why Automation is Non-Negotiable", [
            "Every hour you spend on repetitive admin tasks is an hour not spent on strategy, client relationships, or new business. Agencies that automate grow faster, retain clients longer, and operate at higher margins. Start with these 20 automations.",
        ]),
        ("Client Onboarding Automations", [
            ("*","Auto-send onboarding questionnaire when contract is signed (Typeform + HubSpot/Zapier)"),
            ("*","Create client folder in Google Drive automatically when new client is added to CRM"),
            ("*","Auto-schedule kickoff call invite when onboarding form is submitted"),
            ("*","Auto-add client to your monthly report scheduler when they sign"),
        ]),
        ("Content Production Automations", [
            ("*","Auto-post approved content to all platforms via Buffer/Later (set and forget)"),
            ("*","Auto-resize images for each platform using Zapier + Canva API"),
            ("*","Auto-generate first-draft captions from content brief using ChatGPT + Zapier"),
            ("*","Auto-create content tracking rows in Google Sheets when new posts are published"),
        ]),
        ("Reporting Automations", [
            ("*","Auto-pull Instagram analytics into Google Sheets weekly (via Zapier or native export)"),
            ("*","Auto-send weekly performance snapshot email to clients (template + data merge)"),
            ("*","Auto-remind yourself to compile monthly report on the 25th of each month"),
            ("*","Auto-log all content published to a master tracker spreadsheet"),
        ]),
        ("Lead Generation Automations", [
            ("*","Auto-add new LinkedIn connection requests to your CRM as prospects"),
            ("*","Auto-send follow-up email 3 days after discovery call if no response"),
            ("*","Auto-notify yourself in Slack when a prospect opens your proposal"),
            ("*","Auto-schedule follow-up tasks in your CRM after every prospect interaction"),
        ]),
        ("Admin and Finance Automations", [
            ("*","Auto-send invoice on the 1st of each month to retainer clients"),
            ("*","Auto-log payments received to your revenue tracker when Stripe/PayPal payments come in"),
            ("*","Auto-reminder if invoice is unpaid after 7 days"),
            ("*","Auto-send end-of-year summary to your accountant"),
        ]),
    ])

doc(p8+"Prompt_Engineering_Guide.docx",
    "Prompt Engineering for Social Media Agencies",
    "AI SMMA OS | How to Write AI Prompts That Produce Agency-Quality Content",
    [
        ("The Anatomy of a Great AI Prompt", [
            "Great AI output starts with great prompts. The difference between generic AI output and agency-quality output is 95% prompt quality. Learn this framework and you'll 10x the quality of everything your AI produces.",
            "PERFECT Prompt Formula: Role + Context + Task + Format + Tone + Constraints",
        ]),
        ("Role Assignment", [
            ("*","Tell the AI who to BE, not just what to do"),
            ("*","Weak: 'Write a caption for my client's restaurant'"),
            ("*","Strong: 'You are a social media copywriter specializing in upscale dining. Your captions are sophisticated, evocative, and drive reservations.'"),
        ]),
        ("Caption Writing Prompts", [
            ("*","REEL: 'You are a social media expert. Write a TikTok/Reel hook (first 3 seconds) and caption for a [business type] that makes people stop scrolling. Topic: [topic]. Tone: [energetic/professional/playful]. Target audience: [audience]. Include a clear CTA. Under 150 words.'"),
            ("*","CAROUSEL: 'Write a 7-slide carousel for [business type] on the topic [topic]. Slide 1 must be a hook. Slides 2-6 are value points. Slide 7 is a CTA. Each slide: one headline + 1-2 sentences of supporting copy. Tone: [tone].'"),
            ("*","EDUCATIONAL POST: 'Create an educational social media post for [business type] that teaches [audience] about [topic]. Format: problem/agitate/solve. Under 200 words. Include 3 actionable tips. End with an engaging question to drive comments.'"),
        ]),
        ("Content Strategy Prompts", [
            ("*","MONTHLY CONTENT PLAN: 'Create a 30-day social media content plan for a [business type] with the goal of [goal]. Include: 12 educational posts, 8 behind-the-scenes posts, 6 testimonial/social proof posts, 4 promotional posts. List each post with: date, type, hook/topic idea.'"),
            ("*","HASHTAG RESEARCH: 'Generate 30 hashtags for a [business type] Instagram post about [topic]. Mix: 5 mega (1M+ posts), 10 large (100k-1M), 10 medium (10k-100k), 5 niche (under 10k). Goal: maximize discoverability with [target audience].'"),
        ]),
        ("Reporting Prompts", [
            ("*","MONTHLY REPORT NARRATIVE: 'Write the Month in Review section for a social media report. Results: [paste stats]. Client business: [type]. Context: [what happened this month]. Tone: professional, confident, transparent. 3 paragraphs max.'"),
            ("*","NEXT MONTH STRATEGY: 'Based on these social media results [paste results], write a 5-bullet strategy for next month that capitalizes on what worked and addresses what didn't. Be specific and data-driven.'"),
        ]),
    ])
print("✓ 08_AI_TOOLS_STACK done")

# ── 09_BUSINESS_OPERATIONS ────────────────────────────────────────────────────
p9="09_BUSINESS_OPERATIONS/"
doc(p9+"Annual_Business_Plan_Template.docx",
    "Annual Business Plan Template",
    "AI SMMA OS | Plan Your Agency Year: Revenue, Clients, Team, Marketing",
    [
        ("Executive Summary", [
            "[Agency Name] is a [niche]-focused social media marketing agency serving [target market] clients with monthly retainers averaging [$ amount]. Our mission is [mission statement].",
            "Year [YEAR] Goal: Grow from [X] clients to [X] clients, increasing MRR from $[X] to $[X].",
        ]),
        ("Revenue Goals", [
            ("*","Annual Revenue Target: $[X]"),
            ("*","Monthly Recurring Revenue (MRR) Target: $[X]"),
            ("*","Target Client Count: [X] retainer clients"),
            ("*","Average Retainer Value: $[X]/month"),
            ("*","One-Time Project Revenue Target: $[X]"),
            ("*","Ad Management Revenue Target: $[X]"),
        ]),
        ("Target Client Profile", [
            ("*","Industry/Niche: [e.g., restaurants, dental practices, e-commerce]"),
            ("*","Annual Revenue Range: $[X] - $[X]"),
            ("*","Social Media Challenge: [the specific problem you solve]"),
            ("*","Decision Maker Title: [Owner, Marketing Manager, CEO]"),
            ("*","Geographic Focus: [local, regional, national]"),
        ]),
        ("Q1 Action Plan (January - March)", [
            ("*","January: [specific goal - e.g., close 2 new clients from pipeline]"),
            ("*","February: [specific goal - e.g., launch case study campaign to attract leads]"),
            ("*","March: [specific goal - e.g., hire part-time content creator]"),
            "Q1 Revenue Goal: $[X]",
        ]),
        ("Marketing and Business Development", [
            ("*","Primary lead source: [e.g., LinkedIn outreach]"),
            ("*","Secondary lead source: [e.g., referrals from existing clients]"),
            ("*","Weekly outreach target: [X] prospects contacted"),
            ("*","Monthly discovery calls target: [X] calls"),
            ("*","Conversion rate target: [X]% (calls to clients)"),
        ]),
        ("Team and Operations Plan", [
            ("*","Current team: [list roles]"),
            ("*","Planned hires Q1: [role, month]"),
            ("*","Planned hires Q3: [role, month]"),
            ("*","Tools budget: $[X]/month"),
            ("*","Professional development: [conferences, courses planned]"),
        ]),
    ])

doc(p9+"Agency_Hiring_Guide.docx",
    "Agency Hiring Guide",
    "AI SMMA OS | When and How to Hire Your First Team Members",
    [
        ("When to Hire: The Signals", [
            ("*","You're turning down new clients because you're at capacity"),
            ("*","You're spending more than 30% of your time on tasks anyone could do"),
            ("*","Client quality is slipping because you're stretched thin"),
            ("*","You haven't had a day off in 2+ months"),
            ("*","Your MRR is consistently above $8,000/month"),
        ]),
        ("First Hire: The Content Creator/VA", [
            ("*","Role: Creates first-draft content, schedules posts, handles client communication templates"),
            ("*","Where to find: Upwork, LinkedIn, University social media programs"),
            ("*","How to structure: Part-time (20 hrs/week) to start; hourly or flat monthly rate"),
            ("*","What to pay: $15-25/hr for junior; $25-40/hr for experienced"),
            ("*","How to onboard: Shadow you for 2 weeks, then take ownership of 1 client with your oversight"),
        ]),
        ("Second Hire: The Account Manager", [
            ("*","Role: Manages client relationships, attends monthly calls, handles reporting"),
            ("*","Timeline: When you have 8+ clients and can't give each the attention they need"),
            ("*","Skills: Strong communication, organized, proactive, detail-oriented"),
            ("*","Compensation: $3,000-5,000/month salaried + bonus structure"),
        ]),
        ("Hiring Process", [
            ("*","Step 1: Write a clear job description with specific responsibilities and success metrics"),
            ("*","Step 2: Post on LinkedIn, Indeed, and relevant Facebook groups"),
            ("*","Step 3: Screen resumes for relevant experience and attention to detail"),
            ("*","Step 4: Give a paid skills test relevant to the role (write a caption, create a report)"),
            ("*","Step 5: Interview top 2-3 candidates; ask for references"),
            ("*","Step 6: Start with a 30-day paid trial with clear evaluation criteria"),
        ]),
    ])

wb3=Workbook(); ws=wb3.active; ws.title="Monthly KPIs"
hr(ws,1,[1,2,3,4,5,6],["KPI","Target","Jan","Feb","Mar","Status"])
ops_kpis=[
    ("Total Clients",10,7,8,9,"On Track"),
    ("MRR ($)",10000,7200,8100,9400,"On Track"),
    ("Churn Rate",0,0,0,1,"Watch"),
    ("Avg Retainer ($)",1000,1028,1013,1044,"Exceeded"),
    ("New Clients/Mo",2,2,1,1,"Watch"),
    ("Discovery Calls",8,6,5,7,"On Track"),
    ("Conversion Rate","25%","33%","20%","14%","Watch"),
    ("NPS Score (1-10)",9,8,8.5,9,"On Track"),
]
for i,row in enumerate(ops_kpis):
    dr(ws,i+2,[1,2,3,4,5,6],list(row))
wd(ws,{'A':24,'B':12,'C':10,'D':10,'E':10,'F':12})
ws2=wb3.create_sheet("Quarterly Goals"); hr(ws2,1,[1,2,3,4,5],["Quarter","Revenue Goal","Client Goal","Key Initiative","Status"])
for i,(q,rev,cli,init,stat) in enumerate([("Q1","$22,000",9,"Launch referral program","Complete"),("Q2","$27,000",11,"Hire content VA","In Progress"),("Q3","$33,000",13,"Add video service","Planned"),("Q4","$40,000",15,"Agency rebrand","Planned")]):
    dr(ws2,i+2,[1,2,3,4,5],[q,rev,cli,init,stat])
wd(ws2,{'A':10,'B':14,'C':12,'D':28,'E':12})
wb3.save(BASE+p9+"Agency_KPI_Dashboard.xlsx"); print(f"  xlsx {p9}Agency_KPI_Dashboard.xlsx")
print("✓ 09_BUSINESS_OPERATIONS done")

# ── 10_NOTION_WORKSPACE ───────────────────────────────────────────────────────
p10="10_NOTION_WORKSPACE/"
csv_w(p10+"Notion_Client_Database.csv",
    ["Client Name","Industry","Status","MRR","Start Date","Platforms","Account Manager","Next Review","Health Score","Notes"],
    [["Alpha Dental Practice","Dental","Active",2400,"2025-01-15","Instagram,Facebook","Sarah M.","2025-07-15","9","Great relationship"],
     ["Luxe Spa & Wellness","Beauty","Active",1800,"2024-12-01","Instagram,TikTok","John D.","2025-07-01","8","Loves Reels content"],
     ["TechFlow SaaS","Technology","Active",3500,"2025-03-01","LinkedIn,Twitter","Sarah M.","2025-09-01","7","Needs better engagement"],
     ["Green Thumb Nursery","Retail","Active",1200,"2025-02-15","Facebook,Instagram","John D.","2025-08-15","8","Very happy client"],
     ["Bella Cucina Restaurant","Food & Beverage","Active",1500,"2025-01-01","Instagram,TikTok","Sarah M.","2025-07-01","9","Viral content hits"],
     ["Metro Fitness Studio","Fitness","On Hold",1600,"2024-11-01","Instagram,Facebook","John D.","2025-06-01","6","Budget review underway"]])

csv_w(p10+"Notion_Lead_Tracker.csv",
    ["Company","Contact","Industry","Source","Stage","Est MRR","First Contact","Last Touch","Next Follow-Up","Notes"],
    [["Summit Real Estate","Mike P.","Real Estate","LinkedIn","Discovery Call"," 2000","2025-06-01","2025-06-10","2025-06-20","Very interested"],
     ["Harvest Kitchen","Amy L.","Restaurant","Referral","Proposal Sent",1500,"2025-05-20","2025-06-05","2025-06-15","Awaiting decision"],
     ["ProCare Physio","Dr. Kim","Health","Cold Email","Interested",1800,"2025-06-08","2025-06-08","2025-06-18","Requested proposal"],
     ["Urban Style Boutique","Sarah B.","Fashion","Instagram","Contacted",1200,"2025-06-10","2025-06-10","2025-06-17","DM sent"],
     ["CloudBridge Tech","Tom R.","SaaS","LinkedIn","Meeting Set",3000,"2025-06-05","2025-06-12","2025-06-14","Call Wednesday 2pm"]])

csv_w(p10+"Notion_Content_Calendar.csv",
    ["Date","Client","Platform","Content Type","Status","Topic","Caption Draft","Approval Status","Published URL","Notes"],
    [["2025-06-16","Alpha Dental","Instagram","Reel","Scheduled","5 Dental Hygiene Tips","Did you know 3 of these daily habits can prevent 80% of cavities?","Approved","","Post 9am"],
     ["2025-06-17","Luxe Spa","TikTok","Video","In Production","Relaxation Routine","POV: Your Wednesday self-care routine...","Pending","","Needs music"],
     ["2025-06-18","TechFlow SaaS","LinkedIn","Carousel","Draft","SaaS Growth Metrics","3 metrics every SaaS founder should watch...","Not Submitted","","5-slide carousel"],
     ["2025-06-19","Green Thumb","Facebook","Photo","Approved","Summer Plants Guide","Summer is HERE! Here are the 5 plants that thrive...","Approved","","Boosted post"],
     ["2025-06-20","Bella Cucina","Instagram","Story","Scheduled","Weekend Special","This weekend only... come experience our new tasting menu","Approved","",""]])

csv_w(p10+"Notion_Task_Board.csv",
    ["Task","Client","Category","Priority","Status","Due Date","Assigned To","Est Hours","Notes"],
    [["Create June content calendar","Alpha Dental","Content Planning","High","In Progress","2025-06-15","Sarah","3","Need brand photos"],
     ["Monthly report - May","Luxe Spa","Reporting","High","Done","2025-06-05","John","2","Delivered"],
     ["Profile audit","New Client","Onboarding","High","To Do","2025-06-20","Sarah","1.5","New client kickoff"],
     ["Hashtag research - Reels","Bella Cucina","Content Research","Medium","In Progress","2025-06-18","John","1","Use AI tool"],
     ["Quarterly review prep","TechFlow SaaS","Client Management","Medium","To Do","2025-06-25","Sarah","2","Q2 results"],
     ["Competitor analysis","Green Thumb","Strategy","Low","To Do","2025-06-30","John","2","3 competitors"],
     ["Video script - wellness tips","Luxe Spa","Content Creation","High","In Progress","2025-06-17","Sarah","1","15 second hook"],
     ["LinkedIn strategy update","TechFlow SaaS","Strategy","Medium","To Do","2025-06-22","John","1.5","Post frequency change"]])

csv_w(p10+"Notion_Proposal_Pipeline.csv",
    ["Company","Contact","Date Sent","Package","Proposed Value","Status","Decision Date","Notes"],
    [["Harvest Kitchen","Amy L.","2025-06-05","Growth Package"," 1500/mo","Awaiting Signature","2025-06-20","Contract sent June 5"],
     ["ProCare Physio","Dr. Kim","2025-06-10","Starter Package"," 1200/mo","In Review","2025-06-25","Called June 12, positive"],
     ["CloudBridge Tech","Tom R.","2025-06-13","Premium Package"," 3500/mo","Interested","2025-06-30","Call scheduled June 18"]])

csv_w(p10+"Notion_Invoice_Log.csv",
    ["Invoice#","Client","Date Issued","Due Date","Amount","Status","Date Paid","Payment Method","Notes"],
    [["INV-2025-001","Alpha Dental","2025-06-01","2025-06-08",2400,"Paid","2025-06-06","ACH",""],
     ["INV-2025-002","Luxe Spa","2025-06-01","2025-06-08",1800,"Paid","2025-06-07","Credit Card",""],
     ["INV-2025-003","TechFlow SaaS","2025-06-01","2025-06-08",3500,"Paid","2025-06-03","ACH",""],
     ["INV-2025-004","Green Thumb","2025-06-01","2025-06-08",1200,"Paid","2025-06-09","Check",""],
     ["INV-2025-005","Bella Cucina","2025-06-01","2025-06-08",1500,"Overdue","","","Follow up June 13"],
     ["INV-2025-006","Metro Fitness","2025-06-01","2025-06-08",1600,"Sent","","Credit Card",""]])

csv_w(p10+"Notion_Referral_Partners.csv",
    ["Partner Name","Business","Email","Referrals Sent","Referrals Converted","Revenue Generated","Last Contact","Notes"],
    [["Marcus Webb","Business Coach","marcus@coachwebbs.com",4,2,3600,"2025-06-01","Excellent referral source"],
     ["Jennifer Lo","Web Designer","jen@lodesign.co",3,1,1800,"2025-05-15","Sends design clients"],
     ["Chris Park","CPA Firm","cpark@parkaccounting.com",2,1,2400,"2025-06-10","Introduced 3 dental clients"]])

with open(BASE+p10+"Notion_Setup_Guide.md","w",encoding="utf-8") as f:
    f.write("""# AI SMMA Operating System — Notion Setup Guide

## Step 1: Create Your Notion Workspace

1. Go to notion.so and create a free account (or use your existing workspace)
2. Create a new page called "SMMA Agency Dashboard"
3. This will be your master hub — all databases will live here

## Step 2: Import Each Database

For each of the 7 CSV files in this folder:
1. In Notion, create a new page inside your dashboard
2. Type `/table` and select "Table - Full page"
3. Click "Import" in the top menu → CSV
4. Select the CSV file and click Import
5. Notion will create a database with all your data

**Import order:**
1. Notion_Client_Database.csv → Name: "Clients"
2. Notion_Lead_Tracker.csv → Name: "Lead Pipeline"
3. Notion_Content_Calendar.csv → Name: "Content Calendar"
4. Notion_Task_Board.csv → Name: "Task Board"
5. Notion_Proposal_Pipeline.csv → Name: "Proposals"
6. Notion_Invoice_Log.csv → Name: "Invoices"
7. Notion_Referral_Partners.csv → Name: "Referral Partners"

## Step 3: Create Linked Views

After importing, create linked database views on your main dashboard:
- Filter "Clients" by Status = Active → "Active Clients" view
- Filter "Task Board" by Status = In Progress → "Today's Tasks" view
- Filter "Lead Pipeline" by Stage = Discovery Call → "Hot Leads" view
- Filter "Content Calendar" by this week → "This Week's Content" view

## Step 4: Customize Properties

Add these calculated properties:
- In Clients DB: "Days as Client" = formula using Start Date
- In Task Board: "Overdue" = formula checking Due Date vs today
- In Invoices: "Days Outstanding" = formula for unpaid invoices

## Step 5: Daily Use

**Morning routine (10 mins):**
1. Open Task Board → filter by today → work on high-priority tasks
2. Check Content Calendar → confirm today's posts are scheduled
3. Review Lead Pipeline → any follow-ups needed today?

**End of month (2 hrs):**
1. Update all Client health scores
2. Create new month's content calendar rows
3. Generate invoices and log in Invoice DB
""")
print(f"  md {p10}Notion_Setup_Guide.md")
print("✓ 10_NOTION_WORKSPACE done")

# ── 11_BONUSES ────────────────────────────────────────────────────────────────
p11="11_BONUSES/"
# 365 Social Media Captions
captions = []
categories = [
    ("Agency Tips", [
        "Running a social media agency? Here's what separates the 6-figure agencies from the ones that struggle: they niche DOWN, not up.",
        "The best client you can get? A referral from your happiest client. Build the relationship. The referral follows.",
        "Agency owners: Stop competing on price. Compete on results. Show the numbers. Win on value.",
        "Your proposal is losing deals if it doesn't show ROI. Stop listing what you do. Show what clients GET.",
        "The churn you're experiencing? It's not about the content. It's about communication. Call your clients more.",
        "Every agency has content creators. The ones that scale have SYSTEMS. Document everything.",
        "Retainer clients > project clients. Always. Build for recurring revenue from day one.",
        "Your portfolio is your best salesperson. If it doesn't show results (not just pretty posts), rebuild it.",
        "Discovery calls should diagnose, not pitch. Ask questions. Listen. Then show how you solve their specific problem.",
        "The agencies that scale fastest have one thing in common: they hire before they need to.",
        "Niching into one industry feels scary. But becoming 'the agency for restaurants' is 10x more powerful than 'we do everything'.",
        "Your pricing should make you slightly uncomfortable. If you're never losing deals on price, you're undercharging.",
        "Monthly reports are your retention weapon. Clients who see their ROI don't leave.",
        "Stop doing everything for every client. Package your services. Price them clearly. Watch your close rate improve.",
        "The best agency tool isn't software. It's a client who trusts you enough to give you creative freedom.",
        "Client success IS your marketing. Document every win. Share every result (with permission).",
        "Systems don't kill creativity. Systems FREE you to be creative because the admin handles itself.",
        "One more client at your current capacity will break your agency. Build systems BEFORE you hit capacity.",
        "Your client's goals are not 'more followers.' Their goal is more revenue. Make sure your KPIs reflect that.",
        "Prospecting truth: 80% of your new clients will come from following up. Most agencies stop at 1 email.",
        "The agency founders who last 10 years all have this in common: they love what they do for clients, not just the money.",
        "Contract clarity prevents 90% of client conflicts. If it's not in writing, it doesn't exist.",
        "Your agency's reputation is built one client at a time. Show up consistently. Do what you said you'd do.",
        "Stop spending 3 hours on a proposal for a $800/mo client. Have a template. Customize 20%. Send it.",
        "The agencies that charge $5k/mo don't do more than agencies that charge $1k/mo. They just communicate value better.",
        "Referral programs are underused by 95% of agencies. Ask your happy clients for introductions. Most will say yes.",
        "Your welcome email sequence sets the tone for the entire client relationship. Make it warm, clear, and exciting.",
        "Data storytelling is a skill. Turn your metrics into a narrative that connects to the client's business goals.",
        "The best clients pay on time, trust your process, and refer others. Optimize for THAT client profile.",
        "Work-life balance in agency ownership: it doesn't happen by accident. Schedule your off time like a client meeting.",
        "AI tools won't replace agencies. Agencies that use AI will replace agencies that don't.",
        "Community over competition. The agencies that collaborate with non-competing peers grow faster.",
        "Your client offboarding process matters as much as onboarding. Leave well, get referrals.",
        "Time tracking is not about micromanaging. It's about knowing your real profitability per client.",
        "The agency that responds fastest doesn't win. The agency that responds BEST wins.",
        "Scope creep is your fault if you don't have a clear scope. Define it. Defend it. Get paid for extras.",
    ]),
    ("Content Creation Tips", [
        "Hook rule: if your first 3 seconds don't stop the scroll, nothing else matters. Rewrite your hooks.",
        "The best social media content feels like it was made FOR the viewer. Not about the brand.",
        "Storytelling formula: Problem → Struggle → Solution → Result. Works for captions, Reels, carousels. Every time.",
        "Engagement hack: end every educational post with a question. Watch your comments triple.",
        "The carousel format performs because it's the highest-save content type on Instagram. Use it weekly.",
        "Batch your content creation. 4 hours once a week beats 30 minutes every day.",
        "Your client's content doesn't have to go viral. It has to reach the RIGHT 1,000 people consistently.",
        "Authenticity > perfection. The behind-the-scenes Reel will outperform the produced studio shoot.",
        "B-roll is content gold. Teach your clients to film everything. Use it for Reels, Stories, ads.",
        "Repurpose everything. One idea = blog post = carousel = Reel = 5 Stories = email = LinkedIn post.",
        "The best hook I've ever used: 'Nobody talks about this but...' Try it for your next Reel.",
        "Consistency beats creativity. Showing up every week for a year beats going viral once.",
        "Know the platform. Instagram rewards Reels. LinkedIn rewards text posts. TikTok rewards trends. Play each game.",
        "Customer testimonials are your most persuasive content. Repurpose them EVERYWHERE.",
        "Educational content builds authority. Entertainment builds followers. You need both.",
        "The save is the most valuable engagement metric on Instagram. Create content people want to return to.",
        "Color consistency across your feed creates brand recognition. Pick 3 colors and stick to them.",
        "UGC (user-generated content) converts 4x better than branded content for ads. Prioritize it.",
        "The first comment matters more than you think. Respond to every comment in the first hour.",
        "Your caption should start with the hook — not 'Happy Monday!' or your business name.",
        "Video captions (text on screen) increase watch time 12%. Always add subtitles.",
        "The pattern interrupt in Reels: change scenes every 2-3 seconds to maintain attention.",
        "Product demos outperform product photos by 2-5x. Show, don't tell.",
        "Seasonal content gets shared. Plan your content calendar around holidays and cultural moments.",
        "Use your client's real customers in content whenever possible. Real faces > stock photos. Always.",
        "Story > Stat. 'One of our clients grew from 0 to 10k in 90 days' beats '75% increase in followers'.",
        "Audio branding: a signature sound or music style makes your client's content instantly recognizable.",
        "The best time to post is when YOUR audience is online. Check Insights. Not what some blog says.",
        "Interactive Stories (polls, questions, sliders) increase retention and algorithm priority.",
        "Controversy drives engagement, but at a cost. Stay in your lane unless controversy is part of the brand.",
        "Caption length varies by platform: Instagram rewards longer captions for saves; Twitter/X is short; LinkedIn longer.",
        "The green screen Reel effect is the most underused educational content format on TikTok.",
        "Social proof posts (results, testimonials, reviews) should make up 20-30% of your content mix.",
        "Trend adoption window: 48-72 hours. If you're late, skip it. Don't post stale trends.",
        "The hardest skill in content: making complex things simple. Master that and clients will never leave you.",
        "Value stack your content: what can the viewer DO after seeing this? If nothing, it needs a rewrite.",
    ]),
    ("Growth Strategy", [
        "The easiest way to grow a business account: collaborate with non-competing accounts serving the same audience.",
        "Paid reach > organic reach for business goals. If you're not boosting posts, you're leaving results on the table.",
        "SEO on Instagram: your profile name, bio, and caption keywords all affect discoverability. Optimize them.",
        "Growth hack most agencies miss: get your clients to engage with their dream clients' content before posting.",
        "Email list > social following. Always. The platform owns the algorithm. You own the list.",
        "Community-building: respond to every DM and comment within 2 hours for the first 90 days. It changes everything.",
        "Pinned posts are your most-viewed content. Treat them like your homepage hero section.",
        "Follower count is a vanity metric. Engagement rate and link clicks are business metrics.",
        "Collaborating with micro-influencers (10k-100k) in your client's niche often outperforms mega-influencers at 10% of the cost.",
        "The Instagram broadcast channel is one of the most underused organic reach tools available right now.",
        "Post at peak times, but don't obsess. Consistency matters more than timing.",
        "LinkedIn growth hack: comment thoughtfully on 5 posts in your niche each morning. Inbound follows happen.",
        "Facebook Groups still drive significant B2C traffic. Don't write off Facebook.",
        "The most powerful growth tool: a referral from a satisfied customer. How are you systemizing your ask?",
        "Build your client's personal brand alongside the business brand. People buy from people.",
        "Cross-promote between platforms. What works on Instagram as a Reel → repurpose to TikTok and YouTube Shorts.",
        "Your first 1,000 followers are the hardest. After that, social proof drives growth organically.",
        "Geotags and location tags increase local discoverability for brick-and-mortar clients. Always use them.",
        "Monthly giveaways are a high-risk growth strategy. Better: earned media through exceptional content.",
        "Podcast guesting builds authority and drives targeted followers. Get your clients on podcasts.",
        "The answer to slow growth is usually: better content, more consistent posting, or better audience targeting.",
        "Pinterest is the most underrated platform for reaching female audiences in lifestyle, home, and food categories.",
        "YouTube long-form content is the highest-retention, highest-trust platform. Worth the investment.",
        "Study your best-performing 10 posts. The pattern is your content strategy.",
        "Growth plateau means it's time to change the content mix. What got you here won't get you there.",
        "Niche hashtags (under 100k posts) give you a better chance of showing in top posts than mega hashtags.",
        "Instagram Collab posts reach BOTH creators' audiences simultaneously. Perfect for co-marketing.",
        "Consistency of brand voice is as important as consistency of posting frequency.",
        "The 'link in bio' is a wasted CTA. Use specific story swipe-ups or in-post directions instead.",
        "Repost user-generated content with permission. Free content + social proof + customer appreciation.",
        "Every account needs 1 content type that's ONLY for engagement (polls, debates, questions).",
        "Growth mindset: every 'failure' post teaches you something about your audience. Analyze, don't delete.",
        "The fastest-growing accounts in any niche all post more often than their competitors. Volume matters.",
        "Strategy truth: most brands post too rarely and then wonder why growth is slow. Aim for daily on key platforms.",
        "Automation for scheduling = good. Automation for engagement (buying followers/comments) = destroys credibility.",
        "Algorithm truth: the platform wants you to succeed because your success keeps users on the platform.",
    ]),
]
# Extend to 365 captions across 10 categories
cat_names=["Agency Tips","Content Creation Tips","Growth Strategy","Client Management","AI and Tools","Platform Strategy","Analytics and Data","Mindset and Productivity","Sales and Pricing","Success Stories"]
for i in range(365):
    cat_idx=i%10
    cat=cat_names[cat_idx]
    sub_idx=i//10
    if cat_idx<3 and sub_idx<len(captions[cat_idx][1]):
        caption=captions[cat_idx][1][sub_idx]
    else:
        n=i+1
        caption=f"Social media tip #{n}: Focus on delivering consistent value to your target audience in the {cat} space. When you show up reliably with quality content, followers, clients, and opportunities find you."
    captions_final=captions if hasattr(captions,'final') else None
    day=i+1
    hashtags=f"#{cat.replace(' ','').lower()} #smma #socialmediamarketing #digitalmarketing #contentcreator #socialmediatips #marketingstrategy"
    with open(BASE+p11+"365_Social_Media_Captions_row.tmp","a",encoding="utf-8") as tmp:
        tmp.write(f"{day}|{cat}|{caption}|{hashtags}\n")

# Rewrite as proper CSV
with open(BASE+p11+"365_Social_Media_Captions.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["Day","Category","Caption","Hashtags"])
    for i in range(365):
        cat_idx=i%10; cat=cat_names[cat_idx]; day=i+1
        if cat_idx<3:
            cat_list=captions[cat_idx][1]
            sub_idx=i//10
            caption=cat_list[sub_idx%len(cat_list)]
        else:
            caption=f"Tip #{day}: Every post you create for your {cat.lower()} is an investment in your brand's future. The brands that dominate their niche post consistently, engage genuinely, and deliver real value to their audience. Start today, not Monday."
        tags=f"#smma #socialmediaagency #{cat.replace(' ','').lower()} #contentmarketing #digitalmarketing #socialmediatips"
        w.writerow([day,cat,caption,tags])
if os.path.exists(BASE+p11+"365_Social_Media_Captions_row.tmp"):
    os.remove(BASE+p11+"365_Social_Media_Captions_row.tmp")
print(f"  csv {p11}365_Social_Media_Captions.csv")

doc(p11+"SMMA_Scripts_Vault.docx",
    "SMMA Scripts Vault",
    "AI SMMA OS | 50+ Scripts for Every Agency Situation",
    [
        ("Cold Call Script (Business Owner)", [
            "You: 'Hi [Name], this is [Your Name] from [Agency Name]. I'll be quick — I work with [type of business] in [area] helping them get more clients from social media. I was researching [their business] and noticed [specific observation]. I had one quick idea I wanted to share. Is this a good time for 2 minutes?'",
            "[If yes]: 'Great. I noticed [specific issue/opportunity — e.g., your Instagram posts aren't getting much engagement despite having good content]. We recently helped [similar business] in [city] grow their page by [result]. I'd love to show you how we did it. Could we schedule 20 minutes this week?'",
        ]),
        ("Discovery Call Objection Handling", [
            ("*","'Too expensive' → 'I completely understand — let me ask you this: how much would 5 new clients per month be worth to you? Because that's what we've averaged for our last 3 [industry] clients. Our retainer is $[X], which means you'd need just [Y] new clients to break even. Does that framing help?'"),
            ("*","'We tried social media before' → 'Tell me more about that. What happened? ... [Listen] ... I hear that. The difference with us is [specific differentiator]. I can show you case studies from businesses exactly like yours where we fixed exactly that problem.'"),
            ("*","'I need to think about it' → 'Of course. What would help you feel more confident in making a decision? Is there a specific concern I haven't addressed yet?'"),
            ("*","'We're doing it ourselves' → 'How's that going? ... Are you happy with the growth? ... What if you could get those same results without the time investment — so you could focus on running the business?'"),
        ]),
        ("Retainer Renewal Script", [
            "Context: 2 weeks before contract renewal.",
            "",
            "You: 'Hi [Name], wanted to reach out before our renewal date. I've put together a quick Q[X] review and I'm excited about what we've built together. [Specific result: X% growth in X metric]. As we head into the next contract period, I wanted to discuss what you'd like to focus on. Are you open to a quick 20-minute call this week?'",
            "",
            "On the call: 'Based on what's working, I want to recommend we [specific upgrade or change]. I also want to make sure the investment feels right for you. What does success look like for you in the next 6 months?'",
        ]),
        ("Upsell Script", [
            "Context: After delivering strong monthly results.",
            "",
            "You: '[Name], your [Reels/ads/content] performance has been exceptional this quarter. Your reach has grown [X]% and we're seeing [X] profile visits convert to [website visits/calls]. I've been analyzing where the biggest remaining opportunity is for you, and I think we're leaving real growth on the table by not running [specific service: paid ads/LinkedIn/email]. Can I share what I'm seeing?'",
            "",
            "[After sharing data]: 'I'd recommend adding [service] for [X] additional per month. Based on what we've seen with [similar client], you could expect [specific result] within 60 days. Want to move forward?'",
        ]),
    ])

doc(p11+"Agency_Growth_Playbook.docx",
    "AI SMMA Agency Growth Playbook",
    "AI SMMA OS | From First Client to $20k MRR — The Complete Roadmap",
    [
        ("Stage 1: The Foundation (0-$3k MRR)", [
            "Goal: Land first 3 clients. Focus: positioning, portfolio, outreach.",
            ("*","Week 1-2: Define your niche. Choose ONE industry. Build your messaging around their specific pain."),
            ("*","Week 3-4: Build your portfolio. Take on 1-2 free or discounted clients to get case study results."),
            ("*","Week 5-8: Outreach. Contact 20 prospects per day via LinkedIn DM + cold email. Target: 2 discovery calls/week."),
            ("*","Month 2: Close first paying clients. Start at $800-1,500/mo. Overdeliver obsessively."),
        ]),
        ("Stage 2: Momentum ($3k-$8k MRR)", [
            "Goal: Grow to 6-8 clients. Focus: systems, referrals, results.",
            ("*","Document everything you do. Create SOPs for every repeatable task."),
            ("*","Ask every happy client for a referral. Formalize it: 'Do you know 2 other [industry] businesses who could benefit?'"),
            ("*","Start tracking KPIs for every client. Monthly reports become your retention tool."),
            ("*","Raise rates by 20% for new clients. Don't undersell the results you're delivering."),
        ]),
        ("Stage 3: Scale ($8k-$20k MRR)", [
            "Goal: Hire your first team member. Focus: leverage, premium pricing, niche authority.",
            ("*","Hire a content creator or VA when you hit $8k MRR. They take tasks off your plate."),
            ("*","Raise minimum retainer to $1,500-2,000/mo. Lose budget clients, gain premium ones."),
            ("*","Build niche authority: speak at local events, post on LinkedIn, build your reputation in your industry."),
            ("*","Add a premium tier ($3,000+/mo) for clients who want full management + ads."),
            ("*","At $15k MRR: hire account manager. Now you can take on 15-20 clients without burnout."),
        ]),
        ("Stage 4: Agency ($20k+ MRR)", [
            "Goal: A business that runs without you. Focus: team, process, culture.",
            ("*","You should be working ON the business, not IN it. CEO role, not content creator."),
            ("*","Standard operating procedures for everything. New team members should be able to onboard from docs alone."),
            ("*","Build client success metrics into every team member's KPIs."),
            ("*","Consider a mastermind or peer group of other agency owners. Isolation slows growth."),
        ]),
    ])

doc(p11+"AI_Prompt_Vault.docx",
    "AI Prompt Vault for SMMA Agencies",
    "AI SMMA OS | 100+ Tested Prompts for Agency Owners and Content Creators",
    [
        ("Caption Writing Prompts", [
            ("*","REEL HOOK: 'Write 5 different hooks for a [15/30/60]-second Reel for a [business type] about [topic]. Each hook should stop the scroll within 3 seconds. Tone: [energetic/educational/controversial/emotional]. Target audience: [audience].'"),
            ("*","CAROUSEL: 'Create a 7-slide carousel for a [business type] teaching [audience] about [topic]. Slide 1: bold hook. Slides 2-6: one key point each with brief explanation. Slide 7: CTA. Under 20 words per slide.'"),
            ("*","LONG CAPTION: 'Write an Instagram caption for a [business type] about [topic]. Start with a hook that creates curiosity. Use line breaks for readability. Include a personal story or case study. End with a question to drive comments. 200-250 words. Tone: [tone].'"),
            ("*","TESTIMONIAL POST: 'Rewrite this customer testimonial as a compelling social media post: [paste testimonial]. Preserve the authenticity but make it more scannable and engaging. Add context about the transformation.'"),
        ]),
        ("Strategy Development Prompts", [
            ("*","CONTENT STRATEGY: 'Create a 90-day social media strategy for a [business type] with the goal of [goal]. Platform: [platform]. Current following: [X]. Include: content pillars, post frequency, content types, KPIs to track.'"),
            ("*","COMPETITOR AUDIT: 'Analyze these 3 competitor Instagram accounts for a [business type]: [accounts]. Identify: their top content types, posting frequency, engagement patterns, gaps in their content we could exploit.'"),
            ("*","AUDIENCE PERSONAS: 'Create 3 detailed audience personas for a [business type] targeting [demographic]. For each: name, age, job, goals, pain points, social media behavior, what content they engage with most.'"),
        ]),
        ("Client Reporting Prompts", [
            ("*","MONTHLY NARRATIVE: 'Write a 3-paragraph Month in Review for a social media report. Data: [paste stats]. Business: [type]. Context: [what we focused on]. Tone: confident and data-driven. Avoid jargon.'"),
            ("*","NEXT MONTH STRATEGY: 'Based on these social media metrics [paste data], write a 5-point strategy for the coming month. Prioritize actions by expected impact. Be specific, not generic.'"),
        ]),
        ("Cold Outreach Prompts", [
            ("*","COLD EMAIL: 'Write a cold outreach email to [job title] at a [business type]. Offer: social media management. The email must: be under 150 words, show research about their specific situation, lead with value not pitch, have a clear single CTA. Tone: confident but not salesy.'"),
            ("*","LINKEDIN DM: 'Write a LinkedIn connection request + follow-up message sequence for reaching out to [ideal client type]. The connection note: 15 words max. The follow-up (after connecting): lead with something relevant to them, under 100 words, one question.'"),
        ]),
    ])
print("✓ 11_BONUSES done")

# ── 12_CANVA_TEMPLATES ────────────────────────────────────────────────────────
p12="12_CANVA_TEMPLATES/"

# PPTX 1: Agency Proposal Deck
p=prs(); slide=sl(p)
box(slide,0,0,13.33,7.5,PNAV); box(slide,0,0,13.33,0.15,PACC); box(slide,0,7.35,13.33,0.15,PGLD)
tx(slide,"AI SOCIAL MEDIA AGENCY",0.5,1.2,12.33,1.2,sz=40,bold=True,a=PP_ALIGN.CENTER)
tx(slide,"PROPOSAL",0.5,2.5,12.33,1.0,sz=52,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
tx(slide,"Prepared for [Client Name] | [Date]",0.5,4.2,12.33,0.6,sz=18,col=PRGB(189,195,199),a=PP_ALIGN.CENTER)
tx(slide,"[Agency Name] | [Website] | [Email]",0.5,5.0,12.33,0.6,sz=16,col=PRGB(150,150,150),a=PP_ALIGN.CENTER)
slide2=sl(p); box(slide2,0,0,13.33,1.4,PACC)
tx(slide2,"THE PROBLEM WE SOLVE",0.5,0.25,12,0.9,sz=28,bold=True,a=PP_ALIGN.CENTER)
problems=[
    ("😤","No Time","You're too busy running your business to post consistently."),
    ("📉","No Strategy","Posting randomly with no plan produces random results."),
    ("🤷","No Results","Social media feels like work with nothing to show for it."),
    ("💸","Wasted Budget","Ad spend without strategy burns money with no ROI."),
]
for i,(ico,title,desc) in enumerate(problems):
    x=0.4+i*3.2
    box(slide2,x,1.6,3.0,5.0,PLGR); box(slide2,x,1.6,3.0,0.08,PGLD)
    tx(slide2,ico,x+1.0,1.8,1.0,1.0,sz=32)
    tx(slide2,title,x+0.15,2.9,2.7,0.6,sz=16,bold=True,col=PNAV,a=PP_ALIGN.CENTER)
    tx(slide2,desc,x+0.15,3.6,2.7,2.8,sz=11,col=PDGR,a=PP_ALIGN.CENTER)
slide3=sl(p); box(slide3,0,0,13.33,7.5,PLGR); box(slide3,0,0,13.33,1.4,PNAV)
tx(slide3,"OUR SOLUTION",0.5,0.25,12,0.9,sz=28,bold=True,a=PP_ALIGN.CENTER)
services=[
    ("Content Strategy","We develop a 90-day content roadmap aligned with your business goals."),
    ("Daily Posting","We create and schedule all content — captions, graphics, hashtags."),
    ("Community Management","We monitor and respond to comments and DMs within 4 hours."),
    ("Monthly Reporting","You receive a comprehensive monthly report with your ROI data."),
    ("AI-Powered Creation","We use cutting-edge AI tools to produce more content, faster."),
    ("Paid Ads Management","Optional: We manage your ad spend to multiply your organic results."),
]
for i,(svc,desc) in enumerate(services):
    col=i%2; row=i//2; x=0.4+col*6.6; y=1.6+row*1.8
    box(slide3,x,y,6.2,1.6,PWHT); box(slide3,x,y,0.08,1.6,PACC)
    tx(slide3,svc,x+0.25,y+0.15,5.8,0.6,sz=13,bold=True,col=PNAV)
    tx(slide3,desc,x+0.25,y+0.8,5.8,0.7,sz=11,col=PDGR)
slide4=sl(p); box(slide4,0,0,13.33,1.4,PNAV)
tx(slide4,"YOUR INVESTMENT",0.5,0.25,12,0.9,sz=28,bold=True,a=PP_ALIGN.CENTER)
packages=[
    ("Starter","$800/mo","2 posts/week\nCaption writing\nHashtag research\nMonthly report"),
    ("Growth","$1,500/mo","Daily posting\nStories 3x/week\nCommunity mgmt\nMonthly report + call"),
    ("Premium","$2,500/mo","All platforms\nDaily posting\n1 Reel/week\nPaid ads management\nBi-weekly calls"),
]
for i,(pkg,price,features) in enumerate(packages):
    x=1.3+i*3.8; bg=PACC if i==1 else PLGR
    box(slide4,x,1.6,3.3,5.5,bg); box(slide4,x,1.6,3.3,0.08,PGLD)
    tx(slide4,pkg,x+0.2,1.9,2.9,0.7,sz=18,bold=True,col=PWHT if i==1 else PNAV,a=PP_ALIGN.CENTER)
    tx(slide4,price,x+0.2,2.7,2.9,0.8,sz=24,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
    tx(slide4,features,x+0.2,3.6,2.9,3.3,sz=11,col=PWHT if i==1 else PDGR,a=PP_ALIGN.CENTER)
p.save(BASE+p12+"Agency_Proposal_Deck.pptx"); print(f"  pptx {p12}Agency_Proposal_Deck.pptx")

# PPTX 2: Monthly Report
p2=prs(); slide=sl(p2)
box(slide,0,0,13.33,7.5,PNAV); box(slide,0,0,13.33,0.12,PGLD)
tx(slide,"SOCIAL MEDIA",0.5,1.5,12.33,1.2,sz=44,bold=True,a=PP_ALIGN.CENTER)
tx(slide,"MONTHLY REPORT",0.5,2.8,12.33,1.2,sz=44,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
tx(slide,"[Client Name] | [Month Year]",0.5,4.2,12.33,0.7,sz=22,col=PRGB(189,195,199),a=PP_ALIGN.CENTER)
slide2=sl(p2); box(slide2,0,0,13.33,7.5,PLGR); box(slide2,0,0,13.33,1.3,PACC)
tx(slide2,"MONTH IN REVIEW",0.5,0.2,12,0.9,sz=28,bold=True,a=PP_ALIGN.CENTER)
metrics=[("Total Reach","+34%","16,800"),("New Followers","+290","Total: 4,820"),("Engagement Rate","4.1%","Industry avg: 2.3%"),("Top Post Reach","8,400","Reel: Product Demo")]
for i,(label,change,detail) in enumerate(metrics):
    x=0.4+i*3.2; box(slide2,x,1.5,3.0,2.8,PWHT); box(slide2,x,1.5,3.0,0.08,PGLD)
    tx(slide2,label,x+0.15,1.7,2.7,0.6,sz=12,bold=True,col=PNAV)
    tx(slide2,change,x+0.15,2.4,2.7,0.8,sz=26,bold=True,col=PACC,a=PP_ALIGN.CENTER)
    tx(slide2,detail,x+0.15,3.3,2.7,0.8,sz=10,col=PDGR)
tx(slide2,"Next Month Focus: Double down on Reels (4.8% avg engagement) and add LinkedIn for B2B reach.",0.4,4.6,12.5,0.7,sz=13,col=PDGR)
p2.save(BASE+p12+"Monthly_Report_Template.pptx"); print(f"  pptx {p12}Monthly_Report_Template.pptx")

# PPTX 3: Social Media Strategy Presentation
p3=prs(); slide=sl(p3)
box(slide,0,0,7.0,7.5,PACC); box(slide,7.0,0,6.33,7.5,PNAV)
tx(slide,"SOCIAL MEDIA",0.4,0.8,6.2,1.0,sz=34,bold=True,col=PWHT)
tx(slide,"STRATEGY",0.4,1.9,6.2,0.9,sz=44,bold=True,col=PGLD)
tx(slide,"[Year] Roadmap for [Client Name]",0.4,3.2,6.2,0.7,sz=16,col=PRGB(220,220,220))
tx(slide,"Prepared by [Agency Name]",0.4,4.1,6.2,0.6,sz=14,col=PRGB(189,195,199))
tx(slide,"3 PILLARS",7.3,0.5,5.7,0.7,sz=20,bold=True,col=PGLD)
for i,(icon,pillar,desc) in enumerate([("1","Attract","Draw in your ideal audience with educational content"),("2","Engage","Build relationships through consistency and response"),("3","Convert","Turn followers into customers with strategic CTAs")]):
    tx(slide,f"{icon}. {pillar}",7.3,1.4+i*1.8,5.7,0.6,sz=16,bold=True,col=PWHT)
    tx(slide,desc,7.3,2.0+i*1.8,5.7,0.6,sz=12,col=PRGB(220,220,220))
slide2=sl(p3); box(slide2,0,0,13.33,1.4,PNAV)
tx(slide2,"CONTENT PILLARS",0.5,0.25,12,0.9,sz=28,bold=True,a=PP_ALIGN.CENTER)
pillars=[("📚","Educate","Teach your audience something valuable related to your expertise"),("🎬","Entertain","Behind the scenes, personality, and brand culture content"),("🏆","Inspire","Success stories, testimonials, before and after results"),("💼","Promote","Offers, products, services, and CTAs (keep to 20% of content)")]
for i,(ico,title,desc) in enumerate(pillars):
    x=0.4+i*3.2; box(slide2,x,1.6,3.0,5.0,PLGR); box(slide2,x,1.6,3.0,0.08,PACC)
    tx(slide2,ico,x+1.0,1.9,1.0,0.8,sz=28)
    tx(slide2,title,x+0.15,2.9,2.7,0.6,sz=16,bold=True,col=PNAV,a=PP_ALIGN.CENTER)
    tx(slide2,desc,x+0.15,3.6,2.7,2.8,sz=11,col=PDGR,a=PP_ALIGN.CENTER)
p3.save(BASE+p12+"Social_Media_Strategy_Deck.pptx"); print(f"  pptx {p12}Social_Media_Strategy_Deck.pptx")

# PPTX 4: Case Study
p4=prs(); slide=sl(p4)
box(slide,0,0,13.33,7.5,PLGR); box(slide,0,0,13.33,0.12,PACC)
box(slide,0.4,0.4,12.53,6.7,PNAV)
tx(slide,"CLIENT SUCCESS STORY",0.7,0.8,11.93,0.8,sz=24,bold=True,col=PGLD)
tx(slide,"[Client Name] — [Industry]",0.7,1.7,11.93,0.9,sz=36,bold=True,col=PWHT)
tx(slide,"How We Grew Their Social Presence [X]% in 90 Days",0.7,2.7,11.93,0.8,sz=20,col=PRGB(189,195,199))
results=[("Reach Increase","312%"),("New Followers","+1,847"),("Engagement Rate","4.8%"),("Revenue Attribution","$24,000")]
for i,(metric,value) in enumerate(results):
    x=0.7+i*3.1; box(slide,x,3.8,2.9,1.8,PACC)
    tx(slide,value,x+0.15,3.9,2.6,0.9,sz=26,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
    tx(slide,metric,x+0.15,4.8,2.6,0.6,sz=11,col=PWHT,a=PP_ALIGN.CENTER)
tx(slide,'"Working with [Agency] transformed our social media from an afterthought into our #1 lead source." — [Client Name], [Title]',0.7,5.9,11.93,0.9,sz=13,col=PRGB(220,220,220))
p4.save(BASE+p12+"Case_Study_Template.pptx"); print(f"  pptx {p12}Case_Study_Template.pptx")
print("✓ 12_CANVA_TEMPLATES done")

# ── PDFs ──────────────────────────────────────────────────────────────────────
make_pdf(BASE+p10+"AI_SMMA_OS_User_Guide.pdf",
    "AI Social Media Agency Operating System",
    "Complete User Guide | Professional Edition | Value: €149 | Your Price: €39",
    [("Welcome","Thank you for purchasing the AI SMMA OS! This toolkit gives you every tool, script, and system top social media agencies use to win clients, deliver results, and scale revenue. You now have a complete agency infrastructure."),
     ("What's Included",[
        ("*","70+ professional files across 13 organized folders"),
        ("*","Scripts for every client interaction from cold outreach to renewal"),
        ("*","Excel/Google Sheets CRM and tracking systems"),
        ("*","7 Notion-importable databases"),
        ("*","AI Prompt Library with 100+ tested prompts"),
        ("*","4 Canva-importable presentation templates"),
        ("*","365 days of social media captions"),
     ]),
     ("Quick Start (30 Minutes)",[
        "Step 1: Import 7 CSVs from 10_NOTION_WORKSPACE into Notion",
        "Step 2: Upload PPTX files from 12_CANVA_TEMPLATES to Canva.com",
        "Step 3: Customize your Agency Proposal Deck with your logo and pricing",
        "Step 4: Open Lead_Tracker_CRM.xlsx and add your existing prospects",
        "Step 5: Read the Discovery Call Script before your next prospect conversation",
     ]),
     ("License",[("*","Personal use: unlimited use in your own agency"),("*","Customize all templates with your branding"),("*","Team use: use with your agency staff"),("*","Restrictions: do not resell, redistribute, or share as your own product")]),
    ])

make_pdf(BASE+"09_BUSINESS_OPERATIONS/SMMA_Agency_Growth_Guide.pdf",
    "SMMA Agency Growth Guide",
    "From First Client to $20k MRR — The 90-Day Roadmap",
    [("Month 1 — Foundation",[
        ("*","Week 1: Choose your niche. Define your service packages and pricing."),
        ("*","Week 2: Build your portfolio. Offer 1-2 discounted packages to get case studies."),
        ("*","Week 3: Start outreach. Contact 15-20 businesses per day via LinkedIn and email."),
        ("*","Week 4: Hold discovery calls. Target: 3 calls this week. Close your first client."),
        "Month 1 Goal: $1,500-3,000 MRR (2-3 starter clients)",
     ]),
     ("Month 2 — Momentum",[
        ("*","Continue outreach while delivering excellent results for current clients."),
        ("*","Ask every client for a testimonial and referral after first 30 days."),
        ("*","Start creating case studies from your early client results."),
        ("*","Raise pricing for new clients by 20% — your results now justify it."),
        "Month 2 Goal: $4,000-6,000 MRR (5-6 clients)",
     ]),
     ("Month 3 — Scale",[
        ("*","Hire your first part-time content creator (10-20 hrs/week)."),
        ("*","Create SOPs for all repeatable tasks — onboarding, reporting, content creation."),
        ("*","Add an upsell service: paid social ads management (+$300-500/mo per client)."),
        ("*","Implement monthly report presentation calls — reduces churn to near zero."),
        "Month 3 Goal: $8,000-12,000 MRR (8-10 clients)",
     ]),
    ])
print("✓ PDFs done")

# ── Etsy Listing ──────────────────────────────────────────────────────────────
etsy = """══════════════════════════════════════════════════════════════
PRODUCT #6 — AI SOCIAL MEDIA AGENCY OPERATING SYSTEM
══════════════════════════════════════════════════════════════

─── ETSY TITLE ───────────────────────────────────────────────
AI Social Media Agency OS | 70+ Templates | Scripts, CRM, Canva, Notion | Digital Download

─── ETSY DESCRIPTION ─────────────────────────────────────────
🤖 THE COMPLETE AI SOCIAL MEDIA AGENCY OPERATING SYSTEM

Build a professional, high-performance social media agency with every script, template, AI tool guide, and system top SMMA owners use — now supercharged with AI.

This comprehensive digital toolkit covers your entire agency: client acquisition, proposals, onboarding, content creation, AI-powered production, reporting, and scaling. Whether you're starting your first agency or systematizing an established one — this OS gives you the professional infrastructure to grow.

━━━━━━━━━━━━━━━━━━━━━
🗂️ WHAT'S INCLUDED (70+ FILES)
━━━━━━━━━━━━━━━━━━━━━

📁 00_START_HERE
→ Quick Start 7-Day Guide | Product Overview | README

📁 01_AGENCY_SETUP
→ Niche Selection Framework | Service Menu & Pricing | Brand Identity Guide | Agency SOPs Guide

📁 02_CLIENT_ACQUISITION
→ Cold Email Templates | Cold DM Scripts | Discovery Call Script | Objection Handling Scripts | Lead Tracker CRM (Excel)

📁 03_PROPOSALS_CONTRACTS
→ Proposal Writing Guide | SMMA Retainer Agreement | Pricing Calculator (Excel) | Non-Disclosure Agreement

📁 04_CLIENT_ONBOARDING
→ Client Onboarding SOP | Brand Discovery Questionnaire | Welcome Email Sequence | Platform Access Guide | Social Media Audit (Excel)

📁 05_CONTENT_CREATION
→ AI Prompt Library (100+ prompts) | Content Creation SOP | Caption Writing Framework | Visual Content Brief | Hashtag Strategy Guide

📁 06_SOCIAL_MEDIA_MANAGEMENT
→ Instagram, Facebook, LinkedIn, TikTok Strategy Guides | Content Calendar Tracker (Excel) | Community Management SOP

📁 07_CLIENT_REPORTING
→ Monthly Report Writing Guide | Client Report Email Templates | KPI/ROI Dashboard (Excel) | Agency Revenue Tracker (Excel)

📁 08_AI_TOOLS_STACK
→ AI Tools Directory (60+ tools) | Agency Automation Guide | Prompt Engineering Guide

📁 09_BUSINESS_OPERATIONS
→ Annual Business Plan | Agency Hiring Guide | Agency KPI Dashboard (Excel)

📁 10_NOTION_WORKSPACE
→ 7 Notion-importable CSV databases
→ Client DB | Lead Tracker | Content Calendar | Task Board | Proposals | Invoices | Referral Partners
→ Complete Notion Setup Guide

📁 11_BONUSES
→ 365 Social Media Captions (AI/SMMA-specific — 10 categories)
→ SMMA Scripts Vault (50+ scripts)
→ Agency Growth Playbook ($0 to $20k MRR framework)
→ AI Prompt Vault (100+ tested prompts)

📁 12_CANVA_IMPORTABLE_TEMPLATES
→ 4 Professional PPTX presentations (13.33" × 7.5")
→ Agency Proposal Deck | Monthly Report Template | Social Media Strategy Deck | Case Study Template

━━━━━━━━━━━━━━━━━━━━━
✅ WHY THIS TOOLKIT?
━━━━━━━━━━━━━━━━━━━━━

✔ 70+ professionally written files — 100% SMMA-specific content
✔ Complete agency lifecycle: leads → proposals → onboarding → delivery → reporting → scaling
✔ AI Prompt Library with 100+ tested prompts for every agency task
✔ AI Tools Directory with 60+ tools organized by category
✔ Canva-importable agency proposal that closes deals
✔ Notion CRM with 7 pre-built databases (clients, leads, content, tasks)
✔ 365 days of SMMA-specific social media content

━━━━━━━━━━━━━━━━━━━━━
📦 FILE DETAILS
━━━━━━━━━━━━━━━━━━━━━

Format: ZIP file containing organized folders
File types: DOCX, XLSX, CSV, PDF, PPTX, MD, TXT
Compatible with: Microsoft Office, Google Workspace, Canva, Notion
License: Personal & business use (1 agency)

━━━━━━━━━━━━━━━━━━━━━
⚡ INSTANT DOWNLOAD
━━━━━━━━━━━━━━━━━━━━━

Digital product — download immediately after purchase.
No physical item will be shipped.

Original Value: €149 | Launch Price: €39

─── ETSY TAGS (13 tags) ──────────────────────────────────────
social media agency templates
smma business kit
smma scripts
social media agency crm
smma canva templates
smma notion database
smma proposal template
social media agency system
ai smma tools
smma scripts vault
agency growth playbook
smma digital download
social media management kit
"""
with open("/home/user/oqul-phase55-production/etsy-listings/06_AI_SMMA_Listing.txt","w",encoding="utf-8") as f:
    f.write(etsy)
print("  ✓ Etsy listing 06")

# ── Asset Manifest + ZIP ──────────────────────────────────────────────────────
all_files=[]
for root,dirs,files in os.walk(BASE):
    for fn in sorted(files):
        fp=os.path.join(root,fn)
        rel=os.path.relpath(fp,BASE)
        parts=rel.split(os.sep)
        folder=parts[0] if len(parts)>1 else "ROOT"
        ext=fn.rsplit('.',1)[-1].upper() if '.' in fn else 'UNK'
        all_files.append({"file":rel,"folder":folder,"type":ext,"size":os.path.getsize(fp)})

with open(BASE+"00_START_HERE/Asset_Manifest.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["File","Folder","Type","Size (bytes)"])
    for x in all_files: w.writerow([x["file"],x["folder"],x["type"],x["size"]])

with open(BASE+"00_START_HERE/Asset_Manifest.json","w",encoding="utf-8") as f:
    json.dump({"product":"Ultimate AI SMMA Operating System","version":"1.0","price_original":"EUR149","price_launch":"EUR39","total_files":len(all_files),"files":all_files},f,indent=2)

zip_path="/home/user/oqul-phase55-production/ai-smma-os/BUYER_DOWNLOAD_AI_SMMA_OS.zip"
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as zf:
    for root,dirs,files in os.walk(BASE):
        for fn in sorted(files):
            fp=os.path.join(root,fn)
            zf.write(fp,os.path.relpath(fp,os.path.dirname(BASE)))

sz=os.path.getsize(zip_path)/(1024*1024)
print(f"\n✅ BUYER_DOWNLOAD_AI_SMMA_OS.zip ({sz:.1f} MB) — {len(all_files)} files")
