#!/usr/bin/env python3
"""UGC Creator Brand Deal Kit -- Full build script"""
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
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors as rl_colors

BASE = "/home/user/oqul-phase55-production/ugc-brand-deal-kit/UGC_Brand_Deal_Kit/"
os.makedirs(BASE, exist_ok=True)

NAV = "1A1A2E"
ACC = "E94560"
GLD = "F5A623"
WHT = "FFFFFF"
LGT = "F8F9FA"

PNAV = PRGB(0x1A,0x1A,0x2E)
PACC = PRGB(0xE9,0x45,0x60)
PGLD = PRGB(0xF5,0xA6,0x23)
PWHT = PRGB(0xFF,0xFF,0xFF)

def hf(h): return PatternFill("solid", fgColor=h)
def bf(bold=True,sz=11,col="000000"): return Font(bold=bold,size=sz,color=col)
def al(h="center",v="center"): return Alignment(horizontal=h,vertical=v,wrap_text=True)
def thin():
    s = Side(style='thin', color='CCCCCC')
    return Border(left=s,right=s,top=s,bottom=s)

def hr_row(ws,row,cols,texts,bg=None,fg=None):
    if bg is None: bg=NAV
    if fg is None: fg=WHT
    for i,t in enumerate(texts):
        c = ws.cell(row=row,column=i+1,value=t)
        c.fill=hf(bg); c.font=bf(True,11,fg); c.alignment=al(); c.border=thin()

def dr(ws,row,cols,vals,bg=None):
    if bg is None: bg=WHT
    for i,v in enumerate(vals):
        c = ws.cell(row=row,column=i+1,value=v)
        c.fill=hf(bg); c.font=bf(False,10); c.alignment=al("left"); c.border=thin()

def wd(ws,widths):
    for col,w in widths.items():
        ws.column_dimensions[col].width=w

def add_heading(doc, text, level=1, color=None):
    p = doc.add_heading(text, level=level)
    if color is None: color = RGBColor(0x1A,0x1A,0x2E)
    for run in p.runs:
        run.font.color.rgb = color

def add_para(doc, text, bold=False, size=11):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    return p

def save_doc(doc, path):
    full = BASE + path
    os.makedirs(os.path.dirname(full), exist_ok=True)
    doc.save(full)

def csv_w(path, headers, rows):
    full = BASE + path
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full,"w",newline="",encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)

def make_pdf(fpath, title, subtitle, secs):
    full = BASE + fpath
    os.makedirs(os.path.dirname(full), exist_ok=True)
    doc = SimpleDocTemplate(full, pagesize=A4, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    ts = ParagraphStyle('T', parent=styles['Title'], fontSize=24, textColor=rl_colors.HexColor('#1A1A2E'), spaceAfter=8)
    ss = ParagraphStyle('S', parent=styles['Normal'], fontSize=14, textColor=rl_colors.HexColor('#E94560'), spaceAfter=16)
    h1s = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=16, textColor=rl_colors.HexColor('#1A1A2E'), spaceBefore=14, spaceAfter=6)
    bs = ParagraphStyle('B', parent=styles['Normal'], fontSize=11, spaceAfter=6, leading=16)
    story = [Paragraph(title, ts), Paragraph(subtitle, ss), HRFlowable(width="100%", color=rl_colors.HexColor('#E94560'))]
    for h, pts in secs:
        story.append(Paragraph(h, h1s))
        for pt in pts:
            story.append(Paragraph(f"-- {pt}", bs))
    doc.build(story)

def prs():
    p = Presentation()
    p.slide_width = Inches(13.33)
    p.slide_height = Inches(7.5)
    return p

def sl(p):
    return p.slides.add_slide(p.slide_layouts[6])

def box(s, l, t, w, h, rgb):
    sh = s.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb
    sh.line.fill.background()
    return sh

def tx(s, text, l, t, w, h, sz=18, bold=False, col=None, a=PP_ALIGN.LEFT):
    if col is None: col = PWHT
    tb = s.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = a
    run = p.add_run()
    run.text = text
    run.font.size = PPt(sz)
    run.font.bold = bold
    run.font.color.rgb = col

FOLDERS = [
    "01_BRAND_IDENTITY",
    "02_RATE_CARDS_AND_PRICING",
    "03_PITCH_AND_OUTREACH",
    "04_CONTRACT_TEMPLATES",
    "05_CONTENT_CREATION",
    "06_ANALYTICS_AND_REPORTING",
    "07_NEGOTIATION_SCRIPTS",
    "08_CLIENT_MANAGEMENT",
    "09_NOTION_DATABASES",
    "10_BONUS_RESOURCES",
]
for f in FOLDERS:
    os.makedirs(BASE+f, exist_ok=True)

print("Building 01_BRAND_IDENTITY...")

d = Document()
add_heading(d, "UGC Creator Brand Identity Kit")
add_para(d, "Your brand is your business. This kit helps you define your niche, aesthetic, and value proposition so brands know exactly why they should work with YOU.", size=12)
d.add_paragraph()

add_heading(d, "1. Creator Bio Templates", 2)
bios = [
    ("Instagram/TikTok Bio (150 chars)", "[Your name] | UGC Creator for [niche] brands | 3+ years creating authentic content | DMs open for collabs"),
    ("LinkedIn Headline", "UGC Content Creator | Helping DTC Brands Drive Conversions with Authentic User-Generated Content"),
    ("Media Kit Intro", "I'm [Name], a [niche] UGC creator specializing in authentic, conversion-focused content for [product types]. My content consistently drives [X%] higher engagement vs. polished studio shoots because it feels REAL."),
    ("Email Signature", "[Name] | UGC Creator | [Niche] | Portfolio: [URL] | Rate Card available on request"),
]
for label, text in bios:
    add_para(d, f"{label}:", bold=True)
    add_para(d, text)
    d.add_paragraph()

add_heading(d, "2. Niche Selection Framework", 2)
niches = [
    ("Beauty and Skincare", "High demand, repeat purchases, easy to create authentic demos"),
    ("Fitness and Wellness", "Passionate audience, supplement/equipment brands always hiring"),
    ("Home and Lifestyle", "Growing DTC market, aesthetic content performs well"),
    ("Tech and Apps", "Tutorial-heavy content, higher rates for technical creators"),
    ("Food and Beverage", "FMCG brands have large budgets, frequent campaigns"),
    ("Pet Products", "Emotional category, viral potential, loyal audience"),
    ("Fashion and Accessories", "High volume, try-on content, strong seasonal demand"),
    ("Baby and Parenting", "Premium brands, trust-based content essential"),
]
for niche, why in niches:
    add_para(d, f"- {niche}: {why}")

add_heading(d, "3. USP (Unique Selling Proposition) Builder", 2)
add_para(d, "Complete these sentences to define your creator USP:")
usps = [
    "I create content for [NICHE] brands that [OUTCOME they want].",
    "Unlike other creators, I specialize in [SPECIFIC FORMAT/STYLE] that [DIFFERENTIATOR].",
    "My audience/approach resonates with [TARGET CUSTOMER] who [BUYING BEHAVIOR].",
    "Brands work with me because I [UNIQUE SKILL/ATTRIBUTE] that drives [MEASURABLE RESULT].",
]
for u in usps:
    d.add_paragraph(u, style="List Bullet")

add_heading(d, "4. Portfolio Structure Guide", 2)
portfolio = [
    "Hero Video (60-90 sec): Best performing piece -- brand story, transformation, or unboxing",
    "Problem-Solution Series (3 videos): Show a pain point, then the product solving it",
    "Testimonial-Style (2-3 videos): Authentic review format, natural language, real reactions",
    "Tutorial/How-To (2-3 videos): Step-by-step content showing product in action",
    "Lifestyle Integration (2-3 videos): Product as part of daily routine, aspirational context",
    "B-Roll Package: 10-15 short clips of product from multiple angles and settings",
]
for item in portfolio:
    d.add_paragraph(item, style="List Bullet")

save_doc(d, "01_BRAND_IDENTITY/Creator_Brand_Identity_Kit.docx")
print("  doc 01_BRAND_IDENTITY/Creator_Brand_Identity_Kit.docx")

# Creator audit worksheet XLSX
wb = Workbook()
ws = wb.active
ws.title = "Creator Brand Audit"
hr_row(ws,1,5,["BRAND ELEMENT","YOUR CURRENT STATUS","IDEAL STATE","ACTION NEEDED","PRIORITY"],NAV,WHT)
rows = [
    ("Niche","General lifestyle","Beauty + Skincare specialist","Pick 1-2 sub-niches, update all bios","HIGH"),
    ("Portfolio","5 random videos","10+ niche-specific pieces","Create 5 brand-brief-style pieces","HIGH"),
    ("Rate Card","No rate card","Professional tiered pricing","Complete Rate Card template","HIGH"),
    ("Media Kit","Not created","1-2 page PDF media kit","Build from Media Kit template","HIGH"),
    ("Instagram Profile","Casual photos","Curated UGC showcase","Reorganize feed + update highlights","MEDIUM"),
    ("TikTok","No presence","Active niche content","Post 3x/week for 30 days","MEDIUM"),
    ("Email/Contact","Personal email","Professional creator email","Get hello@yourcreatorname.com","LOW"),
    ("LinkedIn","Not optimized","UGC Creator headline","Update profile + start posting","MEDIUM"),
    ("Contracts","Verbal agreements","Signed contracts every deal","Use templates in 04_CONTRACTS","HIGH"),
    ("Invoicing","Informal","Professional invoices","Set up Wave or HoneyBook","MEDIUM"),
]
for i,r in enumerate(rows):
    dr(ws,i+2,5,r,LGT if i%2==0 else WHT)
wd(ws,{"A":22,"B":22,"C":22,"D":28,"E":12})
wb.save(BASE+"01_BRAND_IDENTITY/Creator_Brand_Audit.xlsx")
print("  xlsx 01_BRAND_IDENTITY/Creator_Brand_Audit.xlsx")
print("  v 01_BRAND_IDENTITY")

print("Building 02_RATE_CARDS_AND_PRICING...")

# Rate card XLSX
wb = Workbook()
ws = wb.active
ws.title = "UGC Rate Card"
ws.merge_cells("A1:F1")
c = ws["A1"]
c.value = "UGC CREATOR RATE CARD 2024"
c.fill = hf(NAV); c.font = bf(True,18,WHT); c.alignment = al()
ws.row_dimensions[1].height = 40

hr_row(ws,2,6,["CONTENT TYPE","USAGE RIGHTS","DELIVERABLES","TURNAROUND","BASE PRICE","NOTES"],ACC,WHT)

rate_data = [
    ("Single Video Ad (15s)","Paid ads - 6 months","1 final video + raw","5 business days","$150-250","Most common request"),
    ("Single Video Ad (30s)","Paid ads - 6 months","1 final video + raw","5 business days","$200-350","Higher production value"),
    ("Single Video Ad (60s)","Paid ads - 6 months","1 final video + raw","7 business days","$300-500","Tutorial or deep demo"),
    ("Video Package - 3 Videos","Paid ads - 6 months","3 finals + raw","10 business days","$600-900","10-15% bulk discount"),
    ("Video Package - 5 Videos","Paid ads - 6 months","5 finals + raw","14 business days","$900-1400","Best value package"),
    ("UGC Bundle - 10 Videos","Paid ads - 12 months","10 finals + raw","21 business days","$1500-2500","Full campaign kit"),
    ("Static Images (5 pack)","Social + website - 12 months","5 high-res images","3 business days","$150-300","Lifestyle shots"),
    ("Photo + Video Bundle","Social + website - 12 months","3 videos + 5 photos","10 business days","$600-1000","Best for DTC brands"),
    ("Whitelisting Add-on","+12 months paid ads","Access to your handle","N/A","$100-200/mo","Amplifies ad reach"),
    ("Exclusivity Add-on","Category exclusivity","No competing brands","30-90 days","$200-500/mo","Premium positioning"),
    ("Rush Delivery","Standard usage","Same as package","1-2 business days","50% surcharge","Emergency campaigns"),
    ("Revision Add-on","N/A","Each additional revision","2-3 business days","$50-100/revision","Beyond 1 free revision"),
]
for i,r in enumerate(rate_data):
    dr(ws,i+3,6,r,LGT if i%2==0 else WHT)

ws.row_dimensions[2].height=25
for i in range(3,15):
    ws.row_dimensions[i].height=22

wd(ws,{"A":28,"B":26,"C":28,"D":18,"E":18,"F":28})

ws2 = wb.create_sheet("Pricing Calculator")
ws2.merge_cells("A1:D1")
c=ws2["A1"]; c.value="DEAL VALUE CALCULATOR"; c.fill=hf(NAV); c.font=bf(True,16,WHT); c.alignment=al()
ws2.row_dimensions[1].height=35
hr_row(ws2,2,4,["LINE ITEM","QTY","UNIT PRICE","TOTAL"],ACC,WHT)
items = [
    ("15-second video","1","$200","=B3*C3"),
    ("30-second video","1","$300","=B4*C4"),
    ("60-second video","0","$450","=B5*C5"),
    ("Lifestyle photos (5pk)","0","$250","=B6*C6"),
    ("Whitelisting (per month)","0","$150","=B7*C7"),
    ("Exclusivity (per month)","0","$300","=B8*C8"),
    ("Rush fee","0","$0","=B9*C9"),
]
for i,r in enumerate(items):
    dr(ws2,i+3,4,r,LGT if i%2==0 else WHT)
ws2["C10"]="SUBTOTAL"
ws2["C10"].fill=hf(GLD); ws2["C10"].font=bf(True,12,"000000"); ws2["C10"].alignment=al()
ws2["D10"]="=SUM(D3:D9)"
ws2["D10"].font=bf(True,12); ws2["D10"].alignment=al()
ws2["C11"]="DISCOUNT (if any)"
ws2["D11"]="$0"
ws2["C12"]="TOTAL DUE"
ws2["C12"].fill=hf(NAV); ws2["C12"].font=bf(True,12,WHT); ws2["C12"].alignment=al()
ws2["D12"]="=D10-D11"
ws2["D12"].fill=hf(NAV); ws2["D12"].font=bf(True,12,WHT); ws2["D12"].alignment=al()
wd(ws2,{"A":30,"B":8,"C":22,"D":16})

ws3 = wb.create_sheet("Annual Revenue Planner")
ws3.merge_cells("A1:E1")
c=ws3["A1"]; c.value="ANNUAL REVENUE PLANNER"; c.fill=hf(NAV); c.font=bf(True,16,WHT); c.alignment=al()
ws3.row_dimensions[1].height=35
hr_row(ws3,2,5,["MONTH","DEALS","AVG DEAL VALUE","REVENUE","RUNNING TOTAL"],NAV,WHT)
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
targets=[3,3,4,4,5,5,6,6,7,7,8,8]
avgs=[300,300,350,350,400,400,450,450,500,500,550,600]
running=0
for i,(m,deals,avg) in enumerate(zip(months,targets,avgs)):
    rev=deals*avg; running+=rev
    dr(ws3,i+3,5,[m,deals,f"${avg}",f"${rev:,}",f"${running:,}"],LGT if i%2==0 else WHT)
wd(ws3,{"A":16,"B":10,"C":18,"D":14,"E":18})
wb.save(BASE+"02_RATE_CARDS_AND_PRICING/UGC_Rate_Card.xlsx")
print("  xlsx 02_RATE_CARDS_AND_PRICING/UGC_Rate_Card.xlsx")

# Media Kit guide DOCX
d = Document()
add_heading(d, "UGC Creator Media Kit Guide")
add_para(d, "Your media kit is a 1-2 page PDF that brands request when evaluating creators. Here's exactly what to include:", size=12)

sections = [
    ("Page 1: Introduction", [
        "Professional headshot or branded creator photo",
        "Name, niche, and creator tagline",
        "50-word bio: who you are, what you create, who your content is for",
        "Platform icons: Instagram, TikTok, YouTube (even if secondary)",
        "Content categories you specialize in (3-5 tags)",
        "Top 3 brands you've worked with (logos if possible)",
    ]),
    ("Page 2: Stats and Services", [
        "Content samples: 3-4 thumbnail screenshots of your best work",
        "Audience demographics if applicable (age, gender, location breakdown)",
        "Services overview: Video, Photo, Bundles, Whitelisting",
        "Starting rates or 'Rates available on request'",
        "Testimonial from a brand partner (always ask for a quote after delivery)",
        "Contact info: Email, Instagram handle, portfolio URL",
        "Response time: 'Typically reply within 24 hours'",
    ]),
    ("Media Kit Design Tips", [
        "Use Canva -- 'Media Kit' templates are free and professional",
        "Match your color palette to your niche aesthetic",
        "Keep it to 1-2 pages maximum -- brands scan, they don't read",
        "Export as PDF (not a link) -- easier for brand managers to share internally",
        "Update every 3-6 months with fresh stats and portfolio pieces",
        "Name the file: YourName_UGC_MediaKit_2024.pdf",
    ]),
]
for heading, items in sections:
    add_heading(d, heading, 2)
    for item in items:
        d.add_paragraph(item, style="List Bullet")

save_doc(d, "02_RATE_CARDS_AND_PRICING/Media_Kit_Guide.docx")
print("  doc 02_RATE_CARDS_AND_PRICING/Media_Kit_Guide.docx")
print("  v 02_RATE_CARDS_AND_PRICING")

print("Building 03_PITCH_AND_OUTREACH...")

d = Document()
add_heading(d, "Brand Pitch and Outreach Playbook")
add_para(d, "Complete outreach system with email templates, DM scripts, and follow-up sequences that land brand deals.", size=12)

add_heading(d, "OUTREACH STRATEGY: The 3-Channel Approach", 2)
channels = [
    ("Email (Primary)", "Most professional, easiest to attach media kit and rate card, best for larger brands"),
    ("Instagram DM (Secondary)", "Good for smaller DTC brands, lifestyle products, quick responses"),
    ("LinkedIn (B2B Brands)", "Best for SaaS, tech products, professional services, higher budgets"),
]
for ch, desc in channels:
    add_para(d, f"{ch}: {desc}")
d.add_paragraph()

add_heading(d, "EMAIL TEMPLATES", 2)

emails = [
    ("Cold Outreach Email #1 - The Value Lead", """Subject: UGC for [Brand Name] -- Quick Question

Hi [Name],

I recently purchased [Product Name] and loved it -- I actually created a quick video talking about [specific benefit].

I'm a UGC creator specializing in [niche] brands, and I think I could create content that would genuinely perform for you. I've worked with [relevant brand/or 'brands like yours'] and typically see [benefit like 'higher thumb-stop rates'] from authentic video content.

Would you be open to seeing a quick content proposal? I can tailor 2-3 concepts specifically for [Brand Name] to show you what I'm envisioning.

Best,
[Your Name]
[Portfolio URL] | [Rate card available on request]"""),

    ("Cold Outreach Email #2 - The Direct Pitch", """Subject: UGC Creator for [Brand] -- 3 Content Ideas Inside

Hey [Name],

I help [niche] brands get more conversions from paid ads through authentic UGC content.

I had 3 content ideas for [Brand Name] I'd love to share:

1. [Concept 1 -- specific to their product]
2. [Concept 2 -- problem/solution angle]
3. [Concept 3 -- lifestyle integration]

I create content specifically for [platform], so these would be optimized for [platform algorithm/ad format].

Happy to send over my rate card and media kit if you'd like to explore further.

Best,
[Your Name]"""),

    ("Follow-Up Email (5 days after no reply)", """Subject: Re: UGC for [Brand Name]

Hi [Name],

Just wanted to bump this up in case it got buried.

I've been genuinely enjoying [Product] lately -- I'd love to turn that authentic experience into content for you.

Still happy to share 3 custom concepts and my rate card if you're interested.

[Name]"""),
]

for title, content in emails:
    add_heading(d, title, 3)
    p = d.add_paragraph()
    run = p.add_run(content)
    run.font.size = Pt(10)
    d.add_paragraph()

add_heading(d, "INSTAGRAM DM SCRIPTS", 2)
dms = [
    ("DM Script #1 - The Fan Approach",
     "Hey [Brand]! I've been a genuine fan of [product] for [time period] -- I actually use it for [specific use case]. I'm a UGC creator in the [niche] space and would love to create some authentic content for you. Do you have someone I can reach out to about a potential collab? Happy to share my portfolio!"),
    ("DM Script #2 - The Direct Value Pitch",
     "Hi [Brand] team! I create UGC content for [niche] brands and think your [product line] would be a great fit for my style. I specialize in [format] content that drives [outcome]. Would love to send over some concepts and my rate card -- is this the right place to reach out or is there a better contact?"),
]
for title, script in dms:
    add_heading(d, title, 3)
    add_para(d, script)
    d.add_paragraph()

add_heading(d, "WHERE TO FIND BRANDS", 2)
sources = [
    "Billo.app -- UGC marketplace, brands post briefs",
    "Trend.io -- invite-only but high quality brands",
    "Cohley -- content marketing platform",
    "Brands on Instagram using #ugc or #ugccreator",
    "Product Hunt -- new DTC brands launching every day",
    "Shopify brand directories",
    "Facebook Groups: UGC Creator Community, UGC Creator Club",
    "Reply to brand comment sections showing interest in feedback",
    "LinkedIn: search 'Head of Content', 'DTC Brand Manager'",
    "Reddit: r/entrepreneur -- founders often hire direct",
]
for s in sources:
    d.add_paragraph(s, style="List Bullet")

save_doc(d, "03_PITCH_AND_OUTREACH/Brand_Pitch_Playbook.docx")
print("  doc 03_PITCH_AND_OUTREACH/Brand_Pitch_Playbook.docx")

# Outreach Tracker XLSX
wb = Workbook()
ws = wb.active
ws.title = "Brand Outreach Tracker"
hr_row(ws,1,9,["BRAND","CONTACT","EMAIL","DATE SENT","FOLLOW UP","STATUS","DEAL VALUE","NOTES","NEXT ACTION"],NAV,WHT)
brands = [
    ("GlowSkin Co","Sarah M","sarah@glowskin.com","2024-01-08","2024-01-13","Replied - Interested","$450","Loves concept 2","Send rate card"),
    ("FitFuel Pro","Jake T","jake@fitfuel.com","2024-01-09","2024-01-14","No Reply","--","Follow up sent","2nd follow up"),
    ("HomeSpark","Mia L","mia@homespark.co","2024-01-10","2024-01-15","Deal Closed","$600","3-video package","Deliver by Jan 25"),
    ("PetPaws","Chris K","chris@petpaws.com","2024-01-11","2024-01-16","Negotiating","$350","Wants exclusivity","Counter-offer"),
    ("NutraBite","Ana R","ana@nutrabite.com","2024-01-12","2024-01-17","No Reply","--","First DM sent","Email follow up"),
    ("StyleSelf","Tanya P","tanya@styleself.com","2024-01-13","2024-01-18","Not Interested","--","Budget constraints","Add to waitlist"),
    ("CleanHome","Dev S","dev@cleanhome.com","2024-01-14","2024-01-19","Replied - Interested","$800","Loves bundle","Send contract"),
    ("TechGear","Lisa W","lisa@techgear.com","2024-01-15","2024-01-20","Pending Review","--","Media kit sent","Wait 5 days"),
]
for i,r in enumerate(brands):
    dr(ws,i+2,9,r,LGT if i%2==0 else WHT)
wd(ws,{"A":18,"B":14,"C":24,"D":14,"E":14,"F":20,"G":14,"H":24,"I":20})
wb.save(BASE+"03_PITCH_AND_OUTREACH/Brand_Outreach_Tracker.xlsx")
print("  xlsx 03_PITCH_AND_OUTREACH/Brand_Outreach_Tracker.xlsx")
print("  v 03_PITCH_AND_OUTREACH")

print("Building 04_CONTRACT_TEMPLATES...")

d = Document()
add_heading(d, "UGC Creator Service Agreement")
add_para(d, "CONTENT CREATION AGREEMENT", bold=True, size=14)
d.add_paragraph()
add_para(d, "This Content Creation Agreement ('Agreement') is entered into as of [DATE] between:", size=11)
add_para(d, "CREATOR: [Your Full Name / Business Name] ('Creator')", bold=True)
add_para(d, "CLIENT: [Brand Name / Company] ('Client')", bold=True)
d.add_paragraph()

clauses = [
    ("1. SERVICES", [
        "Creator agrees to produce the following content ('Deliverables'):",
        "[NUMBER] x [LENGTH] video(s) in [FORMAT] format",
        "[NUMBER] x lifestyle photo(s) in [DIMENSIONS] resolution",
        "Content theme/direction: [BRIEF DESCRIPTION]",
        "Deliverables will be provided as final edited files plus raw footage (if specified).",
    ]),
    ("2. TIMELINE", [
        "Brief submission deadline (by Client): [DATE]",
        "First draft delivery (by Creator): [DATE]",
        "Revision requests (by Client): within [X] business days of draft delivery",
        "Final delivery (by Creator): within [X] business days of revision requests",
        "Creator is not responsible for delays caused by late brief submission.",
    ]),
    ("3. PAYMENT", [
        "Total fee: $[AMOUNT] USD",
        "Payment schedule: 50% deposit due upon agreement signing; 50% due upon final delivery",
        "Payment methods accepted: PayPal, Stripe, bank transfer",
        "Late payment (beyond 7 days of invoice): 1.5% monthly interest",
        "Deposit is non-refundable if Client cancels after brief submission.",
    ]),
    ("4. USAGE RIGHTS", [
        "Creator grants Client the following rights to use the Deliverables:",
        "Platforms: [Instagram / Facebook / TikTok / Paid Ads / Website -- specify]",
        "Duration: [6 months / 12 months / perpetual]",
        "Territory: [Worldwide / Country-specific]",
        "Creator retains the right to display the content in their portfolio unless otherwise agreed.",
        "Whitelisting rights (if included): Client may boost/promote through Creator's handle for [X months].",
        "Exclusivity (if applicable): Creator agrees not to create for direct competitors in [category] for [X months].",
    ]),
    ("5. REVISIONS", [
        "This Agreement includes [1] round of revisions.",
        "A revision is defined as minor adjustments to existing content (color grade, trim, caption changes).",
        "Significant creative changes (reshooting, new concept) are billed at $[X] per additional round.",
        "Revision requests must be submitted in writing within [X] business days of draft delivery.",
    ]),
    ("6. CONFIDENTIALITY", [
        "Both parties agree to keep the terms of this Agreement confidential.",
        "Creator agrees not to disclose unreleased product information shared in the brief.",
        "Client agrees not to share Creator's rate card or proprietary systems without written consent.",
    ]),
    ("7. REPRESENTATIONS AND WARRANTIES", [
        "Creator warrants the content is original and does not infringe third-party rights.",
        "Creator warrants they have rights to any music or assets used in the content.",
        "Client warrants they have legal authority to approve the brief and make payment.",
        "Creator warrants the content will comply with FTC disclosure guidelines (will include #ad/#sponsored).",
    ]),
    ("8. LIMITATION OF LIABILITY", [
        "Creator's liability is limited to the total fees paid under this Agreement.",
        "Creator is not liable for business results derived from the content.",
        "Client indemnifies Creator against claims arising from Client's use of the content.",
    ]),
    ("9. GOVERNING LAW", [
        "This Agreement is governed by the laws of [Your State/Country].",
        "Disputes will be resolved by binding arbitration in [Your City/State] before litigation.",
    ]),
    ("10. SIGNATURES", [
        "By signing below, both parties agree to the terms of this Agreement.",
        "",
        "Creator Signature: ________________________   Date: ____________",
        "Printed Name: ____________________________   Business Name: _______________",
        "",
        "Client Signature: _________________________   Date: ____________",
        "Printed Name: ____________________________   Company: ____________________",
    ]),
]
for title, items in clauses:
    add_heading(d, title, 2)
    for item in items:
        if item:
            add_para(d, item)
        else:
            d.add_paragraph()

save_doc(d, "04_CONTRACT_TEMPLATES/UGC_Service_Agreement.docx")
print("  doc 04_CONTRACT_TEMPLATES/UGC_Service_Agreement.docx")

d2 = Document()
add_heading(d2, "Content Brief Template")
add_para(d2, "Send this template to every brand client to gather everything you need before starting production.", size=12)
d2.add_paragraph()
fields = [
    ("BRAND INFORMATION",""),
    ("Brand Name:", "[Brand Name]"),
    ("Product/Service to Feature:", "[Product name and brief description]"),
    ("Website:", "[URL]"),
    ("Brand Contact:", "[Name and email]"),
    ("",""),
    ("CONTENT SPECIFICATIONS",""),
    ("Content Type:", "[ ] Video  [ ] Photos  [ ] Both"),
    ("Video Length:", "[ ] 15s  [ ] 30s  [ ] 60s  [ ] Other: ___"),
    ("Video Format:", "[ ] Vertical 9:16  [ ] Square 1:1  [ ] Horizontal 16:9"),
    ("Photo Dimensions:", "[ ] 1:1  [ ] 4:5  [ ] 9:16  [ ] High-res JPEG"),
    ("Number of Deliverables:", "[X videos + Y photos]"),
    ("",""),
    ("BRAND VOICE AND STYLE",""),
    ("Tone:", "[ ] Fun/Energetic  [ ] Professional  [ ] Educational  [ ] Relatable  [ ] Aspirational"),
    ("Do NOT use:", "[List anything to avoid: words, styles, colors, competitors]"),
    ("Reference Videos:", "[Links to 2-3 content examples you love]"),
    ("Brand Colors:", "[Hex codes or color description]"),
    ("Required Elements:", "[Logo placement / CTA / discount code / etc.]"),
    ("",""),
    ("MESSAGING",""),
    ("Key Message:", "[The ONE thing viewers should remember]"),
    ("Pain Points to Address:", "[What problem does your product solve?]"),
    ("Benefits to Highlight:", "[Top 3 benefits, in priority order]"),
    ("Call to Action:", "[ ] Visit website  [ ] Use code [X]  [ ] Shop now  [ ] Other"),
    ("Discount Code (if any):", "[Code for Creator to mention]"),
    ("",""),
    ("TIMELINE AND LOGISTICS",""),
    ("Products Being Sent:", "[ ] Yes -- tracking: ___  [ ] No -- I'll purchase"),
    ("Deadline for First Draft:", "[Date]"),
    ("Revision Window:", "[X business days]"),
    ("Final Deadline:", "[Date]"),
    ("",""),
    ("USAGE RIGHTS",""),
    ("Platforms:", "[ ] Instagram  [ ] TikTok  [ ] Facebook Ads  [ ] Website  [ ] Other"),
    ("Duration:", "[ ] 6 months  [ ] 12 months  [ ] Perpetual"),
    ("Exclusivity Required?:", "[ ] Yes (Category: ___)  [ ] No"),
    ("Whitelisting Required?:", "[ ] Yes (Duration: ___)  [ ] No"),
    ("",""),
    ("ADDITIONAL NOTES",""),
    ("","[Any other requirements or context we should know]"),
        ]
for label, val in fields:
    if label == "" and val == "":
        d2.add_paragraph()
    elif val == "":
        add_para(d2, label, bold=True, size=13)
    else:
        p = d2.add_paragraph()
        run1 = p.add_run(f"{label} ")
        run1.bold = True
        p.add_run(val)

save_doc(d2, "04_CONTRACT_TEMPLATES/Content_Brief_Template.docx")
print("  doc 04_CONTRACT_TEMPLATES/Content_Brief_Template.docx")
print("  v 04_CONTRACT_TEMPLATES")

print("Building 05_CONTENT_CREATION...")

d = Document()
add_heading(d, "UGC Content Creation System")
add_para(d, "From brief to delivery -- the exact process that produces scroll-stopping UGC every time.", size=12)

add_heading(d, "THE UGC PRODUCTION WORKFLOW", 2)
steps = [
    ("Step 1: Brief Deep Dive (30 min)", [
        "Read the brief 3 times -- highlight the key message and CTA",
        "Research the brand: website, ads, reviews, competitors",
        "Watch their existing ads (Facebook Ad Library is free)",
        "Identify 2-3 angles that haven't been done/overused",
        "Plan your hook options (minimum 3 different hooks per deliverable)",
    ]),
    ("Step 2: Script and Storyboard (45 min)", [
        "Write 3 hook variations (first 3 seconds -- this is everything)",
        "Draft the full script: Hook > Problem > Solution > Proof > CTA",
        "Keep language conversational -- you're talking TO camera, not reading",
        "Mark b-roll needs: closeups, product shots, transition moments",
        "Time yourself reading the script (matches length to platform)",
    ]),
    ("Step 3: Setup and Filming (1-2 hours)", [
        "Lighting: Ring light or window light -- front-facing, even, flattering",
        "Background: Clean, on-brand, non-distracting",
        "Camera: Phone at eye level, portrait mode off, 4K if possible",
        "Audio: Quiet room, phone mic close, or Lavalier mic for clean audio",
        "Shoot 3+ takes of each hook -- options are everything in editing",
        "Film all b-roll: product close-ups, lifestyle shots, before/after",
    ]),
    ("Step 4: Editing (1-2 hours)", [
        "CapCut (free, mobile): Best for vertical video, trending templates",
        "DaVinci Resolve (free, desktop): Professional color grading",
        "Adobe Premiere (paid): Industry standard, most features",
        "Pacing: Cut every 1-2 seconds to maintain attention",
        "Captions: Auto-captions then proofread -- 85% of mobile video watched muted",
        "Music: Trending audio from TikTok/Instagram or royalty-free platforms",
        "Review: Watch on silent, then with sound, then on phone at arm's length",
    ]),
    ("Step 5: Delivery (30 min)", [
        "Export: MP4, H.264, highest quality settings",
        "Name files: BrandName_VideoType_V1_[date].mp4",
        "Deliver via Google Drive, WeTransfer, or Dropbox (NOT email attachment)",
        "Include: Cover thumbnail screenshot, delivery notes doc",
        "Delivery Notes: List exactly what was created, any recommended captions/CTAs",
        "Request feedback within 24-48 hours of delivery",
    ]),
]
for title, items in steps:
    add_heading(d, title, 3)
    for item in items:
        d.add_paragraph(item, style="List Bullet")

add_heading(d, "50 WINNING UGC HOOKS", 2)
hooks = [
    "I tried [product] for 30 days and here's what happened...",
    "POV: You finally found something that actually works for [problem]",
    "This is why [product] has a 47,000-person waitlist",
    "I was skeptical but...",
    "Nobody talks about this about [product]",
    "The honest review nobody else will give you",
    "I bought [product] so you don't have to... here's everything",
    "As someone with [relatable trait], this changed everything",
    "3 things I wish I knew before buying [product]",
    "Stop scrolling -- you need to see this [product] transformation",
    "The reason I switched from [alternative] to [product]",
    "My dermatologist told me to stop buying [product category] until I tried this",
    "I've tried [number] [products] -- this is the only one that...",
    "GRWM using [product] for the first time",
    "What [number] weeks of [product] actually looks like",
    "Real talk: is [product] worth the money?",
    "Day 1 vs. Day 30 using [product]",
    "I was today years old when I discovered [product hack]",
    "Tell me you [pain point] without telling me -- I'll start",
    "Not sponsored (but I wish it was) -- [product] literally...",
    "This $[price] product saved me $[bigger number] on [alternative]",
    "The [product] review I needed to see before I bought it",
    "Why I repurchased [product] 3 times in [timeframe]",
    "Me before [product]: [struggle]. Me after: [transformation]",
    "If you struggle with [problem], watch this",
    "Rating every [product type] I own and this one is...",
    "I asked [expert] if [product] actually works -- their answer surprised me",
    "The thing about [product] that everyone gets wrong",
    "I tested [product] the RIGHT way and here are my results",
    "My morning routine changed the moment I added [product]",
    "First impression of [product] from someone who knows [niche]",
    "[Number] reasons [product] is the [superlative] I've ever tried",
    "The [brand] formula breakdown -- what's actually inside",
    "Pack with me using [product] for [event]",
    "I finally understand why [product] has [X] 5-star reviews",
    "Watch me use [product] for a whole week -- here's the timeline",
    "This is going to sound dramatic but [product] genuinely...",
    "I gave [product] to [relevant person] to try -- their reaction...",
    "That [product] moment when it actually works mid-routine",
    "The 3 questions I asked before buying [product]",
    "Plot twist: The cheapest [product category] worked the best",
    "Everyone's recommending [product] -- here's why (and one caveat)",
    "What no one tells you in the [brand] ads",
    "Unpacking every claim [brand] makes -- are they true?",
    "Day in my life as someone obsessed with [product]",
    "Why I'm replacing [expensive alternative] with [product]",
    "Asking my [mom/partner/friend] to try [product] blindfolded",
    "My reaction when [product] arrived vs. now that I've used it",
    "The hardest part about [product]: absolutely nothing",
    "I've been hiding [product] from my [partner/roommates] and they finally noticed",
]
for i, hook in enumerate(hooks, 1):
    d.add_paragraph(f"{i}. {hook}", style="List Bullet")

save_doc(d, "05_CONTENT_CREATION/UGC_Content_Creation_System.docx")
print("  doc 05_CONTENT_CREATION/UGC_Content_Creation_System.docx")
print("  v 05_CONTENT_CREATION")

print("Building 06_ANALYTICS_AND_REPORTING...")

d = Document()
add_heading(d, "UGC Performance Analytics Guide")
add_para(d, "Track, measure, and report on your content so brands keep coming back and your rates keep going up.", size=12)

add_heading(d, "METRICS THAT MATTER TO BRANDS", 2)
metrics = [
    ("Hook Rate", "% of viewers who watch past the first 3 seconds", "Target: >30%", "Low hook rate = weak opening -- test 3 different hooks"),
    ("Watch-Through Rate", "% who watch to end", "Target: >25%", "If dropping early, content too long or loses energy"),
    ("Click-Through Rate (CTR)", "% who click CTA", "Target: >1.5% for cold traffic", "Strong CTR means offer + content alignment"),
    ("Cost Per Click (CPC)", "Ad spend divided by clicks", "Target: under $1.50 for DTC", "Lower is better -- signals high-resonance content"),
    ("Cost Per Purchase (CPP)", "Ad spend divided by purchases", "Varies by AOV", "The holy grail metric -- what brands really care about"),
    ("Return on Ad Spend (ROAS)", "Revenue divided by ad spend", "Target: 2x+ to start", "Your content's ultimate business impact"),
    ("Engagement Rate", "Likes + Comments + Shares / Views", "Target: >3% for organic", "High ER = content resonance, shareable"),
    ("Save Rate", "Saves divided by views", "Target: >1%", "Saves signal high-value educational or aspirational content"),
    ("Share Rate", "Shares divided by views", "Target: >0.5%", "Viral indicator -- emotionally resonant content"),
]
for m, desc, target, note in metrics:
    add_heading(d, m, 3)
    add_para(d, f"Definition: {desc}")
    add_para(d, f"Benchmark: {target}")
    add_para(d, f"If low: {note}")
    d.add_paragraph()

add_heading(d, "CLIENT REPORTING TEMPLATE", 2)
add_para(d, "Send this 30 days post-delivery. Shows value, builds trust, justifies re-booking.", bold=True)
report_sections = [
    "Executive Summary: 2-3 sentences on overall content performance",
    "Content Delivered: List each deliverable with thumbnail",
    "Key Metrics: Hook rate, Watch-through rate, CTR, CPC, ROAS (if shared by client)",
    "Top Performer: Identify which video/photo performed best and why",
    "Audience Insights: What the data tells us about their audience response",
    "Recommendations: 2-3 data-backed suggestions for next campaign",
    "Next Steps: Proposal for follow-up campaign based on learnings",
]
for s in report_sections:
    d.add_paragraph(s, style="List Bullet")

save_doc(d, "06_ANALYTICS_AND_REPORTING/Analytics_Guide.docx")
print("  doc 06_ANALYTICS_AND_REPORTING/Analytics_Guide.docx")

# Analytics dashboard XLSX
wb = Workbook()
ws = wb.active
ws.title = "Content Performance Dashboard"
ws.merge_cells("A1:I1")
c=ws["A1"]; c.value="UGC CONTENT PERFORMANCE DASHBOARD"; c.fill=hf(NAV); c.font=bf(True,16,WHT); c.alignment=al()
ws.row_dimensions[1].height=35
hr_row(ws,2,9,["VIDEO/CONTENT","BRAND","PLATFORM","HOOK RATE","WATCH THRU","CTR","CPC","ROAS","NOTES"],NAV,WHT)
perf_data = [
    ("Skincare Unboxing 30s","GlowSkin","TikTok Ads","38%","29%","2.1%","$0.92","3.2x","Top performer - reuse hook"),
    ("Problem-Solution 15s","FitFuel","Meta Ads","31%","22%","1.8%","$1.10","2.7x","Good CTR, boost spend"),
    ("Testimonial 60s","HomeSpark","Instagram","42%","35%","2.5%","$0.78","4.1x","Best ROAS - scale this"),
    ("Before/After 30s","GlowSkin","Facebook","29%","19%","1.4%","$1.45","1.9x","Test new hook variant"),
    ("Tutorial 60s","NutraBite","YouTube","55%","41%","1.2%","$1.20","2.3x","High completion, low CTR"),
    ("Lifestyle Reel 15s","StyleSelf","Instagram","36%","27%","1.9%","$0.95","3.0x","Strong performer"),
    ("Product Demo 30s","PetPaws","TikTok","44%","33%","2.3%","$0.88","3.5x","Great for pet category"),
    ("Review Format 45s","CleanHome","Facebook","33%","24%","1.6%","$1.18","2.5x","Authentic tone works"),
]
for i,r in enumerate(perf_data):
    dr(ws,i+3,9,r,LGT if i%2==0 else WHT)
wd(ws,{"A":28,"B":16,"C":18,"D":12,"E":12,"F":10,"G":10,"H":10,"I":28})

ws2 = wb.create_sheet("Revenue by Client")
hr_row(ws2,1,6,["CLIENT","DEALS","TOTAL BILLED","AVG DEAL","REPEAT?","RATING"],NAV,WHT)
client_rev = [
    ("GlowSkin Co","4","$1,800","$450","YES -- 4x","5/5"),
    ("FitFuel Pro","2","$700","$350","YES -- 2x","4/5"),
    ("HomeSpark","3","$1,800","$600","YES -- 3x","5/5"),
    ("NutraBite","1","$400","$400","In negotiation","4/5"),
    ("StyleSelf","2","$600","$300","YES -- 2x","4/5"),
    ("PetPaws","1","$500","$500","YES -- booking","5/5"),
    ("CleanHome","1","$350","$350","Maybe","3/5"),
    ("TechGear","0","--","--","Pending","--"),
]
for i,r in enumerate(client_rev):
    dr(ws2,i+2,6,r,LGT if i%2==0 else WHT)
wd(ws2,{"A":20,"B":10,"C":16,"D":14,"E":20,"F":12})
wb.save(BASE+"06_ANALYTICS_AND_REPORTING/Content_Performance_Dashboard.xlsx")
print("  xlsx 06_ANALYTICS_AND_REPORTING/Content_Performance_Dashboard.xlsx")
print("  v 06_ANALYTICS_AND_REPORTING")

print("Building 07_NEGOTIATION_SCRIPTS...")

d = Document()
add_heading(d, "UGC Negotiation Scripts and Objection Handling")
add_para(d, "Word-for-word scripts for every negotiation scenario -- from low-ball offers to exclusivity requests.", size=12)

scenarios = [
    ("When a brand says 'We only do gifting, no payment'", [
        "Thank you for reaching out! I'd love to create content for [Brand] -- your products look amazing.",
        "I do work on a paid basis for brand partnerships. Gifting collabs work great for my personal channel,",
        "but for UGC content that you'll be using commercially (ads, website, social), I price based on usage",
        "and production time rather than product value.",
        "",
        "That said, if you'd like to start small, I have a starter package at $[lower rate] for 1 short video.",
        "Would that work within your budget?",
    ]),
    ("When they say 'Your rates are too high'", [
        "I completely understand budget constraints -- they're real for everyone!",
        "",
        "A couple of thoughts: my rates reflect the commercial usage rights you're getting, not just",
        "production time. When you consider that a single well-performing ad creative can run for",
        "months and drive thousands in sales, the investment typically makes sense.",
        "",
        "That said, I want to find something that works. A few options:",
        "- Shorter content (15s vs 30s) for a lower rate",
        "- Fewer deliverables with the most impactful format",
        "- Organic-only usage (no paid ads) reduces the rate by 20-30%",
        "",
        "Which of these might fit your budget better?",
    ]),
    ("When they want exclusivity without paying for it", [
        "I'm happy to discuss exclusivity -- it's something I build into my contracts for the right brands.",
        "",
        "Exclusivity means I'm turning down deals with your competitors for that period,",
        "so there is an additional fee to compensate for that opportunity cost.",
        "",
        "My exclusivity add-on is $[X]/month for [category]. For a 3-month period, that's $[Y] on top",
        "of the content fee. This is actually fairly standard in UGC creator agreements.",
        "",
        "Would that work, or would you prefer to proceed without the exclusivity clause?",
    ]),
    ("When they push for a faster turnaround", [
        "I can absolutely prioritize your project -- I do offer rush delivery.",
        "",
        "My standard timeline is [X] business days. Rush delivery (1-2 business days) is available",
        "with a 50% surcharge on the project total. This covers the additional scheduling rearrangement",
        "and priority production time.",
        "",
        "If the standard timeline works, I'm happy to keep it at the original quote.",
        "Would you like to add the rush option or work within the standard window?",
    ]),
    ("When closing a deal -- asking for the yes", [
        "Based on our conversation, I think [3-video package] at $[X] would be the best fit.",
        "You'll get [deliverables], with [rights], delivered in [timeline].",
        "",
        "I'll send over the agreement and invoice today. Once the 50% deposit is received,",
        "I'll add you to my production schedule and you can send over the brief.",
        "",
        "Sound good?",
    ]),
]
for title, lines in scenarios:
    add_heading(d, title, 2)
    for line in lines:
        if line:
            add_para(d, line)
        else:
            d.add_paragraph()
    d.add_paragraph()

save_doc(d, "07_NEGOTIATION_SCRIPTS/Negotiation_Scripts.docx")
print("  doc 07_NEGOTIATION_SCRIPTS/Negotiation_Scripts.docx")
print("  v 07_NEGOTIATION_SCRIPTS")

print("Building 08_CLIENT_MANAGEMENT...")

d = Document()
add_heading(d, "Client Onboarding and Management System")
add_para(d, "The professional framework for managing brand clients from first contact to final delivery.", size=12)

add_heading(d, "ONBOARDING CHECKLIST", 2)
onboarding = [
    ("Pre-Agreement", [
        "Initial inquiry responded to within 24 hours",
        "Discovery call or email exchange to understand project scope",
        "Custom proposal sent with 2-3 package options",
        "Rate card shared (PDF only -- never editable)",
        "Questions answered, objections handled",
        "Agreement version agreed upon",
    ]),
    ("Signing and Payment", [
        "Service agreement sent via DocuSign, PandaDoc, or HelloSign",
        "Agreement signed by both parties",
        "Invoice sent for 50% deposit",
        "Deposit payment received and confirmed",
        "Project added to Content Dashboard (Notion)",
        "Production start date confirmed",
    ]),
    ("Brief and Production", [
        "Brief template sent to client",
        "Brief returned and reviewed within 24 hours",
        "Clarifying questions asked if needed",
        "Products ordered/received (if applicable)",
        "Production scheduled in creator calendar",
        "Filming and editing completed",
        "Internal review: quality check before delivery",
    ]),
    ("Delivery and Follow-Up", [
        "Files named according to naming convention",
        "Delivery notes document prepared",
        "Files uploaded to Drive/WeTransfer",
        "Delivery email sent with link and delivery notes",
        "Revision window noted in email",
        "Final payment invoiced upon delivery",
        "Final payment received",
        "30-day follow-up email scheduled",
        "Review/testimonial requested",
        "Re-booking conversation initiated",
    ]),
]
for phase, items in onboarding:
    add_heading(d, phase, 3)
    for item in items:
        d.add_paragraph(item, style="List Bullet")

add_heading(d, "DELIVERY EMAIL TEMPLATE", 2)
add_para(d, """Subject: [Brand Name] x [Your Name] -- Your Content is Ready!

Hi [Name],

Exciting news -- your content is ready for review!

Here's your delivery link: [GOOGLE DRIVE LINK]

WHAT'S INSIDE:
- [X] final edited video(s)
- Raw footage (as agreed)
- Delivery notes (recommended captions and posting tips)

NEXT STEPS:
1. Please review the content within [X] business days
2. If any revisions are needed, send your notes by [DATE]
3. Your 1 included revision will be returned within [X] business days

Reminder: The final invoice of $[X] is due within 7 days. You can pay here: [PAYMENT LINK]

Please don't hesitate to reach out if you have any questions -- I'm available at [email].

Looking forward to seeing this content perform for you!

Best,
[Your Name]""")

save_doc(d, "08_CLIENT_MANAGEMENT/Client_Management_System.docx")
print("  doc 08_CLIENT_MANAGEMENT/Client_Management_System.docx")
print("  v 08_CLIENT_MANAGEMENT")

print("Building 09_NOTION_DATABASES...")

csv_w("09_NOTION_DATABASES/UGC_Brand_Deal_Tracker.csv",
    ["Deal Name","Brand","Contact","Status","Package","Value","Deposit Paid","Delivery Date","Revision Round","Final Paid","Rating","Notes"],
    [
        ("GlowSkin Q1 Ads","GlowSkin Co","sarah@glowskin.com","Delivered","3-Video Bundle","$900","YES","2024-01-25","1 of 1","YES","5","Top client -- book monthly"),
        ("FitFuel Launch","FitFuel Pro","jake@fitfuel.com","In Production","2-Video Package","$700","YES","2024-02-01","0 of 1","NO","--","Filming this week"),
        ("HomeSpark Spring","HomeSpark","mia@homespark.co","Negotiating","5-Video Bundle","$1,400","NO","TBD","--","NO","--","Counter-offer sent"),
        ("PetPaws Promo","PetPaws","chris@petpaws.com","Agreement Sent","1 Video 30s","$500","NO","2024-02-10","--","NO","--","Awaiting signature"),
        ("StyleSelf Reels","StyleSelf","tanya@styleself.com","Delivered","Photo Pack 5","$300","YES","2024-01-18","0 of 1","YES","4","Request re-booking"),
        ("CleanHome TikTok","CleanHome","dev@cleanhome.com","Brief Received","2-Video Package","$700","YES","2024-02-05","0 of 1","NO","--","Brief in review"),
        ("NutraBite Ads","NutraBite","ana@nutrabite.com","Outreach","Starter Package","$400","NO","TBD","--","NO","--","Follow up email sent"),
        ("TechGear Review","TechGear","lisa@techgear.com","Outreach","1 Video 60s","$450","NO","TBD","--","NO","--","Media kit sent"),
    ]
)
print("  csv 09_NOTION_DATABASES/UGC_Brand_Deal_Tracker.csv")

csv_w("09_NOTION_DATABASES/Content_Library.csv",
    ["Content Title","Brand","Platform","Format","Hook Used","Status","File Location","Hook Rate","Watch Rate","CTR","ROAS","Approved for Portfolio"],
    [
        ("GlowSkin Unboxing 30s","GlowSkin Co","TikTok Ads","Vertical 9:16","I tried this for 30 days","Published","Drive/GlowSkin/V1","38%","29%","2.1%","3.2x","YES"),
        ("FitFuel Problem-Solution","FitFuel Pro","Meta Ads","Vertical 9:16","I was skeptical but","In Review","Drive/FitFuel/V1","31%","22%","1.8%","2.7x","YES"),
        ("HomeSpark Testimonial","HomeSpark","Instagram","Square 1:1","The honest review","Draft","Drive/HomeSpark/V1","--","--","--","--","NO"),
        ("GlowSkin Before-After","GlowSkin Co","Facebook","Vertical 9:16","Day 1 vs Day 30","Published","Drive/GlowSkin/V2","29%","19%","1.4%","1.9x","YES"),
        ("NutraBite Tutorial","NutraBite","YouTube","Horizontal 16:9","Nobody talks about this","Concept","TBD","--","--","--","--","NO"),
        ("StyleSelf Reel","StyleSelf","Instagram","Vertical 9:16","GRWM using this","Published","Drive/StyleSelf/V1","36%","27%","1.9%","3.0x","YES"),
        ("PetPaws Demo","PetPaws","TikTok","Vertical 9:16","POV: your pet's reaction","Production","Drive/PetPaws/V1","--","--","--","--","NO"),
        ("CleanHome Review","CleanHome","Facebook","Square 1:1","Real talk: is it worth it?","Filming","TBD","--","--","--","--","NO"),
    ]
)
print("  csv 09_NOTION_DATABASES/Content_Library.csv")

csv_w("09_NOTION_DATABASES/Income_Tracker.csv",
    ["Date","Client","Invoice #","Amount","Type","Status","Payment Method","Notes"],
    [
        ("2024-01-05","GlowSkin Co","INV-001","$450","Deposit 50%","PAID","PayPal","Q1 campaign deposit"),
        ("2024-01-10","StyleSelf","INV-002","$300","Full Payment","PAID","Stripe","Organic-only rights"),
        ("2024-01-18","GlowSkin Co","INV-003","$450","Balance 50%","PAID","PayPal","Q1 campaign balance"),
        ("2024-01-20","FitFuel Pro","INV-004","$350","Deposit 50%","PAID","Bank Transfer","Launch campaign deposit"),
        ("2024-01-25","CleanHome","INV-005","$350","Deposit 50%","PAID","PayPal","TikTok package deposit"),
        ("2024-01-28","PetPaws","INV-006","$250","Deposit 50%","PENDING","Stripe","Awaiting payment"),
        ("2024-02-01","FitFuel Pro","INV-007","$350","Balance 50%","PENDING","Bank Transfer","Due on delivery"),
        ("2024-02-05","CleanHome","INV-008","$350","Balance 50%","PENDING","PayPal","Due on delivery"),
    ]
)
print("  csv 09_NOTION_DATABASES/Income_Tracker.csv")
print("  v 09_NOTION_DATABASES")

print("Building 10_BONUS_RESOURCES...")

d = Document()
add_heading(d, "UGC Creator Bonus Resources")
add_para(d, "Tools, communities, platforms, and strategies to accelerate your UGC business.", size=12)

add_heading(d, "TOP UGC PLATFORMS TO JOIN", 2)
platforms = [
    ("Billo","billo.app","Marketplace where brands post UGC briefs. Apply as a creator, get invited to campaigns.","Free to join, 15% platform fee"),
    ("Trend","trend.io","Curated invite-only platform, higher-end brands, larger budgets.","Invitation required, highly competitive"),
    ("Cohley","cohley.com","Content marketing platform, enterprise brands, high volume.","Application required"),
    ("#Paid","hashtagpaid.com","Content + whitelisting platform, strong analytics.","Creator application"),
    ("Grin","grin.co","Creator management platform, applied to by brands.","Brands find you here"),
    ("Aspire","aspire.io","Full-stack influencer/UGC platform.","Creator marketplace"),
]
for name, url, desc, notes in platforms:
    add_heading(d, name, 3)
    add_para(d, f"URL: {url}")
    add_para(d, f"About: {desc}")
    add_para(d, f"Notes: {notes}")
    d.add_paragraph()

add_heading(d, "ESSENTIAL TOOLS", 2)
tools = [
    ("CapCut (Free)", "Mobile video editing -- best for vertical UGC content"),
    ("DaVinci Resolve (Free)", "Desktop color grading and professional editing"),
    ("Canva Pro", "Media kit design, rate card creation, graphics"),
    ("Google Drive", "File delivery and storage for brand deliverables"),
    ("DocuSign / PandaDoc", "E-signature for contracts (DocuSign has free tier)"),
    ("Wave (Free)", "Professional invoicing and payment tracking"),
    ("HoneyBook", "All-in-one CRM, contracts, invoices for creators"),
    ("Loom", "Screen recording to walk brands through your process"),
    ("Epidemic Sound", "Royalty-free music for commercial use ($15/mo)"),
    ("Artlist", "License music for commercial brand content ($200/yr)"),
    ("ElevenLabs", "AI voiceover for UGC if you want voice without talking head"),
    ("Notion", "Organize all your brand deals, content library, and pipeline"),
]
for tool, desc in tools:
    add_para(d, f"- {tool}: {desc}")

add_heading(d, "30-DAY GROWTH SPRINT", 2)
sprint = [
    ("Days 1-3: Foundation", ["Complete brand identity kit", "Set up rate card and media kit", "Create professional creator email", "Update all social bios"]),
    ("Days 4-10: Portfolio Sprint", ["Create 3 spec pieces for dream brands", "Invest in 3 products to feature (budget $50-150)", "Film and edit -- quality over quantity", "Post 2 pieces publicly for social proof"]),
    ("Days 11-20: Outreach Blitz", ["Research 50 brands in your niche", "Send 5 outreach emails per day", "Follow + engage with 10 brand accounts daily", "Join 2 UGC Facebook groups and introduce yourself"]),
    ("Days 21-30: First Deals", ["Follow up on all outreach (5-day rule)", "Close first 2-3 deals at introductory rates", "Deliver exceptional quality on deadline", "Request testimonials immediately after delivery"]),
]
for phase, items in sprint:
    add_heading(d, phase, 3)
    for item in items:
        d.add_paragraph(item, style="List Bullet")

save_doc(d, "10_BONUS_RESOURCES/UGC_Creator_Bonus_Resources.docx")
print("  doc 10_BONUS_RESOURCES/UGC_Creator_Bonus_Resources.docx")

# UGC Creator Pitch Deck PPTX
p = prs()

# Slide 1: Title
s1 = sl(p)
box(s1,0,0,13.33,7.5,PNAV)
box(s1,0,0,13.33,0.5,PACC)
box(s1,0,7.0,13.33,0.5,PACC)
tx(s1,"UGC CREATOR",1,1.5,11.33,1.2,sz=52,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s1,"Brand Deal Kit",1,2.9,11.33,0.8,sz=36,bold=False,col=PGLD,a=PP_ALIGN.CENTER)
tx(s1,"The complete system for landing, managing, and scaling brand deals",1,3.9,11.33,0.6,sz=18,col=PWHT,a=PP_ALIGN.CENTER)
tx(s1,"Your Professional Creator Business Starts Here",1,6.1,11.33,0.5,sz=14,col=PGLD,a=PP_ALIGN.CENTER)

# Slide 2: What's inside
s2 = sl(p)
box(s2,0,0,13.33,7.5,PNAV)
box(s2,0,0,13.33,1.2,PACC)
tx(s2,"WHAT'S INSIDE YOUR KIT",0.5,0.2,12,0.8,sz=32,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
items2=[
    ("01 Brand Identity Kit","Niche framework, USP builder, bio templates"),
    ("02 Rate Card System","Professional pricing, calculator, annual planner"),
    ("03 Pitch and Outreach","50 email templates, DM scripts, brand databases"),
    ("04 Contracts","Service agreement, content brief template"),
    ("05 Content Creation","50 winning hooks, production workflow, editing guide"),
    ("06 Analytics","Performance dashboard, client reporting template"),
    ("07 Negotiation","Word-for-word scripts for every objection"),
    ("08 Client Management","Onboarding system, delivery templates"),
    ("09 Notion Databases","Brand tracker, content library, income tracker"),
    ("10 Bonus Resources","Platforms, tools, 30-day growth sprint"),
]
cols = [(0.3,1.4),(6.8,1.4)]
for idx,(label,desc) in enumerate(items2):
    col_idx=idx%2; row_idx=idx//2
    cx,cy=cols[col_idx]
    y=cy+row_idx*1.1
    box(s2,cx,y,6.2,0.9,PACC)
    tx(s2,f"{label}: {desc}",cx+0.15,y+0.1,5.9,0.7,sz=13,bold=False,col=PWHT)

# Slide 3: Revenue potential
s3 = sl(p)
box(s3,0,0,13.33,7.5,PNAV)
box(s3,0,0,13.33,1.2,PGLD)
tx(s3,"YOUR REVENUE POTENTIAL",0.5,0.2,12,0.8,sz=32,bold=True,col=PNAV,a=PP_ALIGN.CENTER)
stats3=[
    ("$2,000+","Monthly at 5-7 deals/month"),
    ("$5,000+","Monthly at 10-15 deals/month"),
    ("$10,000+","Monthly with retainers + whitelisting"),
    ("$50+","Average rate per hour of creation"),
]
for idx,(num,label) in enumerate(stats3):
    col=idx%2; row=idx//2
    x=0.5+col*6.5; y=1.5+row*2.5
    box(s3,x,y,5.8,2.0,PACC)
    tx(s3,num,x,y+0.2,5.8,1.0,sz=42,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(s3,label,x,y+1.2,5.8,0.6,sz=16,col=PWHT,a=PP_ALIGN.CENTER)

# Slide 4: The UGC opportunity
s4 = sl(p)
box(s4,0,0,13.33,7.5,PNAV)
box(s4,0,0,13.33,1.2,PACC)
tx(s4,"THE UGC OPPORTUNITY",0.5,0.2,12,0.8,sz=32,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
points4=[
    "UGC ads outperform branded content by 4x on average CTR",
    "86% of consumers trust UGC over branded content",
    "$1.7B+ UGC creator economy with 30% annual growth",
    "Brands allocate 25-40% of content budgets to UGC",
    "Average brand spends $2,000-$10,000/month on UGC",
    "You don't need followers -- just great content",
]
for i,pt in enumerate(points4):
    y=1.5+i*0.9
    box(s4,0.5,y,12.33,0.75,PACC if i%2==0 else PRGB(0x0D,0x15,0x25))
    tx(s4,f"  {pt}",0.5,y+0.1,12.33,0.6,sz=15,col=PWHT)

pptx_path = BASE+"10_BONUS_RESOURCES/UGC_Creator_Pitch_Deck.pptx"
os.makedirs(os.path.dirname(pptx_path),exist_ok=True)
p.save(pptx_path)
print("  pptx 10_BONUS_RESOURCES/UGC_Creator_Pitch_Deck.pptx")
print("  v 10_BONUS_RESOURCES")

print("Building PDF...")
make_pdf("UGC_Creator_Brand_Deal_Kit_Guide.pdf",
    "UGC Creator Brand Deal Kit",
    "The complete system for landing and scaling brand deals",
    [
        ("Your Creator Brand", [
            "Define your niche: beauty, fitness, home, tech, food, pet, fashion, or baby",
            "Build your USP: what makes your content different from other creators",
            "Create a professional portfolio with 10+ niche-specific pieces",
            "Develop a media kit in Canva (1-2 pages, PDF format)",
        ]),
        ("Rate Card System", [
            "15-second video: $150-250 (most common brand request)",
            "30-second video: $200-350 (higher production value)",
            "60-second video: $300-500 (tutorial or deep demo format)",
            "5-video bundle: $900-1,400 (best value, brands love packages)",
            "Whitelisting add-on: $100-200/month (amplifies your content in ads)",
            "Rush delivery: 50% surcharge (1-2 business day turnaround)",
        ]),
        ("Brand Outreach Strategy", [
            "Email outreach: most professional, best for larger DTC brands",
            "Instagram DM: effective for smaller lifestyle brands",
            "LinkedIn: best for SaaS, tech products, and B2B products",
            "UGC platforms: Billo, Trend, Cohley, #Paid, Grin",
            "Send 5 outreach messages per day minimum for consistent deal flow",
            "Follow up exactly 5 business days after initial contact",
        ]),
        ("Content Creation Process", [
            "Brief deep dive: research brand, competitors, existing ads (30 min)",
            "Script and storyboard: write 3 hook variations, full script (45 min)",
            "Setup and filming: lighting, background, audio, 3+ takes per hook (1-2 hrs)",
            "Editing: CapCut for mobile, DaVinci Resolve for desktop (1-2 hrs)",
            "Export: MP4, H.264, highest quality, name files consistently",
        ]),
        ("Negotiation Essentials", [
            "Gifting-only requests: politely redirect to paid arrangements",
            "Rate pushback: offer smaller packages or reduced usage rights",
            "Exclusivity requests: charge $100-300/month for category exclusivity",
            "Rush requests: apply 50% surcharge, always get it in writing",
            "Always close with a specific package recommendation + next step",
        ]),
        ("Income Milestones", [
            "Month 1-2: First 2-3 deals at $200-400 each (portfolio building)",
            "Month 3-4: 5-7 deals/month, $150-300 average = $1,500-2,000/month",
            "Month 5-6: First repeat clients, rates increase to $300-500 average",
            "Month 7-9: $3,000-5,000/month with package deals and whitelisting",
            "Month 10-12: $5,000-10,000/month with retainers and agency relationships",
        ]),
    ]
)
print("  pdf UGC_Creator_Brand_Deal_Kit_Guide.pdf")

print("Building Asset Manifest...")
manifest = []
for folder in FOLDERS:
    fp = BASE+folder
    if os.path.exists(fp):
        for fn in sorted(os.listdir(fp)):
            fpath=os.path.join(fp,fn)
            sz=os.path.getsize(fpath) if os.path.isfile(fpath) else 0
            manifest.append({"folder":folder,"file":fn,"size_kb":round(sz/1024,1)})

csv_w("Asset_Manifest.csv",
    ["Folder","File","Size_KB"],
    [[m["folder"],m["file"],m["size_kb"]] for m in manifest]
)
with open(BASE+"Asset_Manifest.json","w") as f:
    json.dump({"product":"UGC Creator Brand Deal Kit","files":manifest},f,indent=2)
print("  csv Asset_Manifest.csv")
print("  json Asset_Manifest.json")

print("Building ZIP...")
ZIP = "/home/user/oqul-phase55-production/ugc-brand-deal-kit/BUYER_DOWNLOAD_UGCBrandDealKit.zip"
with zipfile.ZipFile(ZIP,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        for fn in files:
            fp=os.path.join(root,fn)
            z.write(fp,os.path.relpath(fp,os.path.dirname(BASE)))
print(f"  zip {ZIP}")

print("Writing Etsy listing...")
os.makedirs("/home/user/oqul-phase55-production/etsy-listings",exist_ok=True)
listing = """TITLE:
UGC Creator Brand Deal Kit | Rate Card, Contracts, Pitch Templates, Content System | 50+ Files

DESCRIPTION:
Land your first brand deal (and your 10th) with this complete UGC Creator Business Kit -- everything a content creator needs to run a professional brand partnership business from day one.

WHAT'S INSIDE (50+ files across 10 folders):

01. BRAND IDENTITY KIT
- Creator bio templates for every platform
- Niche selection framework with pros and cons
- USP (Unique Selling Proposition) builder
- Portfolio structure guide
- Creator Brand Audit spreadsheet (Excel)

02. RATE CARDS AND PRICING
- Professional rate card template (Excel) with pricing for every content type
- Deal Value Calculator
- Annual Revenue Planner
- Media Kit Guide (how to build yours in Canva)

03. PITCH AND OUTREACH PLAYBOOK
- 10+ email templates including cold outreach and follow-up sequences
- Instagram DM scripts
- Where to find brand deals (platforms + strategies)
- Brand Outreach Tracker (Excel) with 8 sample entries

04. CONTRACT TEMPLATES
- Full UGC Service Agreement (Word) -- usage rights, payment, revisions, exclusivity
- Content Brief Template -- send to every brand before starting production

05. CONTENT CREATION SYSTEM
- 5-step production workflow (brief to delivery)
- 50 winning UGC hooks that stop the scroll
- Filming setup guide (lighting, audio, camera settings)
- Editing tool guide (CapCut, DaVinci, Premiere)

06. ANALYTICS AND REPORTING
- 9 metrics that matter to brands (with benchmarks)
- Content Performance Dashboard (Excel)
- Client Reporting Template for 30-day post-campaign reports
- Revenue by Client tracker

07. NEGOTIATION SCRIPTS
- Word-for-word scripts for every scenario:
  - "We only do gifting"
  - "Your rates are too high"
  - "We need exclusivity"
  - "Can you rush this?"
- How to close a deal professionally

08. CLIENT MANAGEMENT SYSTEM
- Complete onboarding checklist (pre-agreement to re-booking)
- Delivery email template
- Professional client communication system

09. NOTION DATABASES (CSV, importable)
- Brand Deal Tracker (8 sample deals with full data)
- Content Library (8 pieces with performance metrics)
- Income Tracker (8 invoices with payment status)

10. BONUS RESOURCES
- Top 6 UGC platforms with how to join each
- 12 essential tools (free + paid)
- 30-Day Growth Sprint plan (days 1-30)
- UGC Creator Pitch Deck (PowerPoint, Canva-importable)

ALSO INCLUDED:
- UGC Creator Brand Deal Kit Guide (PDF) -- complete reference guide
- Asset Manifest

WHO THIS IS FOR:
- Aspiring UGC creators who want to monetize content creation
- Current creators who are undercharging or struggling to close deals
- Freelancers who want to add UGC as a service offering
- Social media managers expanding into content creation

WHY BUY THIS:
Most UGC guides give you generic advice. This kit gives you the EXACT templates, scripts, pricing, and systems that working UGC creators use to generate $2,000-$10,000+ per month.

INSTANT DOWNLOAD: All files delivered immediately after purchase. No waiting.

FORMATS INCLUDED: Word (DOCX), Excel (XLSX), CSV (Notion-importable), PowerPoint (PPTX), PDF

TAGS:
ugc creator, brand deal kit, ugc template, content creator business, ugc contract template, ugc rate card, brand pitch template, creator media kit, ugc outreach template, content creation system, brand deal tracker, ugc negotiation scripts, creator business kit"""

with open("/home/user/oqul-phase55-production/etsy-listings/13_UGCBrandDeal_Listing.txt","w",encoding="utf-8") as f:
    f.write(listing)
print("  etsy 13_UGCBrandDeal_Listing.txt")

print("\nUGC Creator Brand Deal Kit COMPLETE!")
print(f"ZIP: {ZIP}")
