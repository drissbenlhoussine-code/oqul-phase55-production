#!/usr/bin/env python3
"""Content Creator Sponsorship Tracker -- Full build script"""
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

BASE = "/home/user/oqul-phase55-production/creator-sponsorship-tracker/Creator_Sponsorship_Tracker/"
os.makedirs(BASE, exist_ok=True)

NAV = "0F2940"
ACC = "FF6B35"
GLD = "FFD23F"
WHT = "FFFFFF"
LGT = "FFF8F3"

PNAV = PRGB(0x0F,0x29,0x40)
PACC = PRGB(0xFF,0x6B,0x35)
PGLD = PRGB(0xFF,0xD2,0x3F)
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
    if color is None: color = RGBColor(0x0F,0x29,0x40)
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
    ts = ParagraphStyle('T', parent=styles['Title'], fontSize=24, textColor=rl_colors.HexColor('#0F2940'), spaceAfter=8)
    ss = ParagraphStyle('S', parent=styles['Normal'], fontSize=14, textColor=rl_colors.HexColor('#FF6B35'), spaceAfter=16)
    h1s = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=16, textColor=rl_colors.HexColor('#0F2940'), spaceBefore=14, spaceAfter=6)
    bs = ParagraphStyle('B', parent=styles['Normal'], fontSize=11, spaceAfter=6, leading=16)
    story = [Paragraph(title, ts), Paragraph(subtitle, ss), HRFlowable(width="100%", color=rl_colors.HexColor('#FF6B35'))]
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
    "01_SPONSORSHIP_TRACKER",
    "02_BRAND_DEAL_PIPELINE",
    "03_INCOME_AND_TAXES",
    "04_CONTENT_CALENDAR",
    "05_BRAND_PITCH_SYSTEM",
    "06_ANALYTICS_DASHBOARD",
    "07_CONTRACTS_AND_INVOICES",
    "08_NOTION_DATABASES",
    "09_YOUTUBE_SPECIFIC",
    "10_INSTAGRAM_SPECIFIC",
    "11_TIKTOK_SPECIFIC",
    "12_BONUS_RESOURCES",
]
for f in FOLDERS:
    os.makedirs(BASE+f, exist_ok=True)

print("Building 01_SPONSORSHIP_TRACKER...")

# Master sponsorship tracker XLSX
wb = Workbook()
ws = wb.active
ws.title = "Master Sponsorship Tracker"
ws.merge_cells("A1:L1")
c=ws["A1"]; c.value="CONTENT CREATOR SPONSORSHIP TRACKER 2024"
c.fill=hf(NAV); c.font=bf(True,18,WHT); c.alignment=al()
ws.row_dimensions[1].height=40

hr_row(ws,2,12,["BRAND","PLATFORM","DEAL TYPE","CONTENT DUE","PUBLISH DATE","FEE","STATUS","CONTACT","DELIVERABLES","NOTES","USAGE RIGHTS","PAYMENT STATUS"],NAV,WHT)

deals = [
    ("NordVPN","YouTube","Integration","2024-02-01","2024-02-08","$2,500","PAID","sarah@nordvpn.com","1x integration 30-60s","Mid-roll + end card","12 months","RECEIVED"),
    ("Squarespace","YouTube","Dedicated Video","2024-02-15","2024-02-20","$4,000","INVOICED","jake@squarespace.com","Full dedicated video","Organic only","6 months","PENDING"),
    ("HelloFresh","Instagram","Story Series","2024-01-28","2024-01-30","$1,200","DELIVERED","mia@hellofresh.com","5x Story frames","Paid ads 30 days","3 months","RECEIVED"),
    ("Surfshark","TikTok","Integration","2024-02-10","2024-02-12","$800","IN PRODUCTION","chris@surfshark.com","60s TikTok","Organic only","6 months","PENDING"),
    ("Notion","YouTube","Integration","2024-03-01","2024-03-08","$3,000","NEGOTIATING","ana@notion.so","Integration + demo","12 months","PENDING","TBD"),
    ("BetterHelp","YouTube","Dedicated Video","2024-03-15","2024-03-22","$5,500","OUTREACH","pr@betterhelp.com","Full dedicated video","Organic only","6 months","TBD"),
    ("Skillshare","YouTube","Integration","2024-02-22","2024-03-01","$1,800","CONTRACT SENT","sr@skillshare.com","45-90s integration","12 months","PENDING","TBD"),
    ("G FUEL","TikTok","Gifting + Fee","2024-02-05","2024-02-07","$600","COMPLETED","brandon@gfuel.com","3x TikTok videos","Whitelisting 30 days","3 months","RECEIVED"),
    ("Casetify","Instagram","Static Post + Story","2024-02-18","2024-02-20","$900","BRIEF RECEIVED","lisa@casetify.com","1 post + 3 stories","Paid ads 60 days","6 months","50% received"),
    ("Audible","YouTube","Integration","2024-03-10","2024-03-17","$2,200","PITCHED","dev@audible.com","Integration","12 months","PENDING","TBD"),
]
for i,r in enumerate(deals):
    dr(ws,i+3,12,r,LGT if i%2==0 else WHT)

wd(ws,{"A":16,"B":14,"C":20,"D":14,"E":14,"F":10,"G":18,"H":24,"I":22,"J":22,"K":16,"L":18})

ws2 = wb.create_sheet("Revenue Summary")
ws2.merge_cells("A1:E1")
c=ws2["A1"]; c.value="MONTHLY REVENUE SUMMARY"; c.fill=hf(NAV); c.font=bf(True,16,WHT); c.alignment=al()
ws2.row_dimensions[1].height=35
hr_row(ws2,2,5,["MONTH","DEALS CLOSED","TOTAL REVENUE","AVG DEAL SIZE","YTD TOTAL"],NAV,WHT)
months=[("January 2024",3,"$4,700","$1,567","$4,700"),("February 2024",5,"$9,500","$1,900","$14,200"),("March 2024",4,"$11,700","$2,925","$25,900"),("April 2024",6,"$14,200","$2,367","$40,100"),("May 2024",5,"$13,100","$2,620","$53,200"),("June 2024",7,"$18,500","$2,643","$71,700")]
for i,r in enumerate(months):
    dr(ws2,i+3,5,r,LGT if i%2==0 else WHT)
wd(ws2,{"A":18,"B":16,"C":18,"D":18,"E":16})
wb.save(BASE+"01_SPONSORSHIP_TRACKER/Master_Sponsorship_Tracker.xlsx")
print("  xlsx 01_SPONSORSHIP_TRACKER/Master_Sponsorship_Tracker.xlsx")
print("  v 01_SPONSORSHIP_TRACKER")

print("Building 02_BRAND_DEAL_PIPELINE...")

wb = Workbook()
ws = wb.active
ws.title = "Brand Deal Pipeline"
hr_row(ws,1,8,["BRAND","INITIAL CONTACT","STATUS","NEXT ACTION","DUE DATE","EST VALUE","PRIORITY","NOTES"],NAV,WHT)
pipeline = [
    ("Amazon","2024-01-15","Interested","Send media kit","2024-01-22","$3,000+","HIGH","Head of creator partnerships contacted"),
    ("ExpressVPN","2024-01-20","Pitched","Follow up email","2024-01-27","$2,500","HIGH","No reply after 5 days"),
    ("MorningBrew","2024-01-22","Outreach","Wait 5 days","2024-01-29","$1,500","MEDIUM","First email sent"),
    ("Whoop","2024-01-25","Brief Received","Draft proposal","2024-01-30","$2,000","HIGH","Love the concept"),
    ("Calm","2024-01-28","Contract Sent","Awaiting signature","2024-02-04","$1,800","HIGH","DocuSign pending"),
    ("Grammarly","2024-02-01","Negotiating","Counter rate","2024-02-05","$2,200","HIGH","They offered $1,800, want $2,500"),
    ("Athletic Greens","2024-02-05","Gifting","Request paid deal","2024-02-10","$1,000","MEDIUM","Sent product, no fee yet"),
    ("Fiverr","2024-02-08","Outreach","DM on LinkedIn","2024-02-13","$2,000","LOW","Warm contact referral"),
]
for i,r in enumerate(pipeline):
    dr(ws,i+2,8,r,LGT if i%2==0 else WHT)
wd(ws,{"A":18,"B":16,"C":18,"D":22,"E":14,"F":14,"G":12,"H":30})
wb.save(BASE+"02_BRAND_DEAL_PIPELINE/Brand_Deal_Pipeline.xlsx")
print("  xlsx 02_BRAND_DEAL_PIPELINE/Brand_Deal_Pipeline.xlsx")

d = Document()
add_heading(d, "Brand Deal Pipeline Management Guide")
add_para(d, "The system for tracking every potential deal from first contact to payment received.", size=12)

add_heading(d, "PIPELINE STAGES", 2)
stages = [
    ("1. OUTREACH", "You've sent an initial email, DM, or made contact through a platform", "Follow up in exactly 5 business days if no reply"),
    ("2. INTERESTED", "Brand has replied with interest or asked for your media kit/rate card", "Send media kit + rate card within 24 hours"),
    ("3. PITCHED", "You've sent a formal proposal or rate card", "Follow up in 3 business days"),
    ("4. NEGOTIATING", "Back-and-forth on rates, deliverables, or usage rights", "Know your floor rate before negotiating"),
    ("5. CONTRACT SENT", "Agreement has been sent for signature", "Follow up if unsigned after 48 hours"),
    ("6. BRIEF RECEIVED", "Contract signed, brief received, in production", "Confirm delivery date and production schedule"),
    ("7. DELIVERED", "Content submitted to brand for review", "Request feedback within 24 hours"),
    ("8. PAID", "Payment received in full", "Archive deal, request testimonial, pitch next campaign"),
]
for stage, desc, action in stages:
    add_heading(d, stage, 3)
    add_para(d, f"Definition: {desc}")
    add_para(d, f"Action: {action}")
    d.add_paragraph()

add_heading(d, "PIPELINE METRICS TO TRACK WEEKLY", 2)
metrics = [
    "New outreach sent this week",
    "Replies received (response rate %)",
    "Deals moved from Outreach to Interested",
    "Proposals/rate cards sent",
    "Deals closed (new contracts signed)",
    "Total pipeline value (sum of all open deals)",
    "Weighted pipeline value (apply probability % to each stage)",
    "Average time from first contact to closed deal",
]
for m in metrics:
    d.add_paragraph(m, style="List Bullet")

save_doc(d, "02_BRAND_DEAL_PIPELINE/Pipeline_Management_Guide.docx")
print("  doc 02_BRAND_DEAL_PIPELINE/Pipeline_Management_Guide.docx")
print("  v 02_BRAND_DEAL_PIPELINE")

print("Building 03_INCOME_AND_TAXES...")

wb = Workbook()
ws = wb.active
ws.title = "Income and Tax Tracker"
ws.merge_cells("A1:H1")
c=ws["A1"]; c.value="CREATOR INCOME AND TAX TRACKER 2024"
c.fill=hf(NAV); c.font=bf(True,16,WHT); c.alignment=al()
ws.row_dimensions[1].height=35
hr_row(ws,2,8,["DATE","CLIENT","INVOICE #","AMOUNT","TAX (25%)","NET INCOME","PAYMENT METHOD","NOTES"],NAV,WHT)
income = [
    ("2024-01-12","NordVPN","INV-2024-001","$2,500","$625","$1,875","Wire Transfer","Q1 YouTube integration"),
    ("2024-01-30","HelloFresh","INV-2024-002","$1,200","$300","$900","PayPal","Instagram story series"),
    ("2024-02-07","G FUEL","INV-2024-003","$600","$150","$450","Venmo","TikTok package"),
    ("2024-02-20","Casetify","INV-2024-004","$450","$113","$337","Stripe","Deposit 50%"),
    ("2024-01-30","Skillshare","INV-2024-005","$900","$225","$675","Wire Transfer","Integration deposit"),
    ("2024-03-01","Skillshare","INV-2024-006","$900","$225","$675","Wire Transfer","Integration balance"),
    ("2024-02-25","Casetify","INV-2024-007","$450","$113","$337","Stripe","Balance 50%"),
    ("2024-03-10","Squarespace","INV-2024-008","$4,000","$1,000","$3,000","Wire Transfer","Dedicated video"),
]
for i,r in enumerate(income):
    dr(ws,i+3,8,r,LGT if i%2==0 else WHT)
wd(ws,{"A":14,"B":16,"C":18,"D":12,"E":12,"F":12,"G":18,"H":28})

ws2=wb.create_sheet("Quarterly Tax Planner")
ws2.merge_cells("A1:D1")
c=ws2["A1"]; c.value="QUARTERLY TAX ESTIMATES"; c.fill=hf(NAV); c.font=bf(True,16,WHT); c.alignment=al()
ws2.row_dimensions[1].height=35
hr_row(ws2,2,4,["QUARTER","INCOME","EST TAX (25%)","DUE DATE"],NAV,WHT)
qtax=[("Q1 2024 (Jan-Mar)","$9,650","$2,413","April 15, 2024"),("Q2 2024 (Apr-Jun)","$14,200","$3,550","June 15, 2024"),("Q3 2024 (Jul-Sep)","$18,100","$4,525","September 15, 2024"),("Q4 2024 (Oct-Dec)","$22,500","$5,625","January 15, 2025")]
for i,r in enumerate(qtax):
    dr(ws2,i+3,4,r,LGT if i%2==0 else WHT)

ws3=wb.create_sheet("Business Expenses")
hr_row(ws3,1,5,["DATE","EXPENSE","CATEGORY","AMOUNT","TAX DEDUCTIBLE"],NAV,WHT)
expenses=[
    ("2024-01-05","Camera lens","Equipment","$399","YES"),
    ("2024-01-10","Ring light upgrade","Equipment","$89","YES"),
    ("2024-01-15","CapCut Pro subscription","Software","$99/yr","YES"),
    ("2024-01-20","Epidemic Sound license","Music License","$180/yr","YES"),
    ("2024-02-01","Home office deduction","Home Office","$200/mo","YES - partial"),
    ("2024-02-05","Course: YouTube SEO","Education","$197","YES"),
    ("2024-02-10","Tripod and mounts","Equipment","$65","YES"),
    ("2024-02-15","Canva Pro","Software","$13/mo","YES"),
    ("2024-03-01","Microphone","Equipment","$149","YES"),
    ("2024-03-10","Background/props","Props","$45","YES"),
]
for i,r in enumerate(expenses):
    dr(ws3,i+2,5,r,LGT if i%2==0 else WHT)
wd(ws3,{"A":14,"B":28,"C":18,"D":14,"E":18})
wb.save(BASE+"03_INCOME_AND_TAXES/Income_Tax_Tracker.xlsx")
print("  xlsx 03_INCOME_AND_TAXES/Income_Tax_Tracker.xlsx")

d = Document()
add_heading(d, "Creator Tax Guide -- What You Need to Know")
add_para(d, "Disclaimer: This is general educational information, not tax advice. Consult a CPA for your specific situation.", size=10)
d.add_paragraph()

add_heading(d, "TAX BASICS FOR CONTENT CREATORS", 2)
basics = [
    "Self-employment tax: Creators are self-employed and owe ~15.3% SE tax on net earnings",
    "Income tax: Federal income tax on top of SE tax (rate depends on total income)",
    "Estimated quarterly payments: Due April 15, June 15, Sept 15, Jan 15 of next year",
    "1099-NEC: Brands must send you this form if they paid you $600+ in a year",
    "Rule of thumb: Set aside 25-30% of every payment for taxes",
]
for b in basics:
    d.add_paragraph(b, style="List Bullet")

add_heading(d, "DEDUCTIBLE BUSINESS EXPENSES", 2)
deductions = [
    ("Equipment", "Camera, lenses, tripod, ring light, microphone, SD cards"),
    ("Software and Subscriptions", "Editing apps, music licenses, design tools, project management"),
    ("Home Office", "% of rent/mortgage proportional to dedicated workspace sq footage"),
    ("Internet", "% used for business (typically 50-80% for creators)"),
    ("Phone", "% used for business (typically 50-75%)"),
    ("Education", "Courses, books, workshops related to content creation"),
    ("Travel", "Business travel to brand shoots, events, conferences"),
    ("Props and Supplies", "Products purchased specifically to feature in content"),
    ("Professional Services", "Accountant, lawyer, business coach fees"),
    ("Marketing", "Website, business cards, portfolio platform subscriptions"),
]
for cat, desc in deductions:
    add_heading(d, cat, 3)
    add_para(d, desc)

add_heading(d, "IMPORTANT DATES", 2)
dates = [
    "January 31: Deadline to receive all 1099 forms from brands",
    "April 15: Q1 estimated tax payment due + prior year tax return deadline",
    "June 15: Q2 estimated tax payment due",
    "September 15: Q3 estimated tax payment due",
    "January 15 (next year): Q4 estimated tax payment due",
]
for date in dates:
    d.add_paragraph(date, style="List Bullet")

save_doc(d, "03_INCOME_AND_TAXES/Creator_Tax_Guide.docx")
print("  doc 03_INCOME_AND_TAXES/Creator_Tax_Guide.docx")
print("  v 03_INCOME_AND_TAXES")

print("Building 04_CONTENT_CALENDAR...")

wb = Workbook()
ws = wb.active
ws.title = "Sponsored Content Calendar"
ws.merge_cells("A1:G1")
c=ws["A1"]; c.value="SPONSORED CONTENT CALENDAR -- FEBRUARY 2024"
c.fill=hf(NAV); c.font=bf(True,16,WHT); c.alignment=al()
ws.row_dimensions[1].height=35
hr_row(ws,2,7,["DATE","PLATFORM","CONTENT TYPE","BRAND","STATUS","FEE","NOTES"],NAV,WHT)
cal=[
    ("Feb 1","YouTube","Video Upload","NordVPN","PUBLISHED","$2,500","Integration 45-sec mid-roll"),
    ("Feb 5","TikTok","Short Video","Surfshark","FILMING","$800","60s tutorial format"),
    ("Feb 7","TikTok","Short Video","G FUEL","PUBLISHED","$600","3 videos in batch"),
    ("Feb 8","YouTube","Shorts","NordVPN","PUBLISHED","$0","Repurposed from main video"),
    ("Feb 12","TikTok","Short Video","Surfshark","SCHEDULED","$0","Repurposed TikTok"),
    ("Feb 14","Instagram","Reel","Valentine's promo","CONCEPT","$0","Organic -- build engagement"),
    ("Feb 15","YouTube","Video Upload","Squarespace","SCRIPTING","$4,000","Full dedicated video"),
    ("Feb 18","Instagram","Feed Post","Casetify","EDITING","$450","Product showcase"),
    ("Feb 19","Instagram","Stories","Casetify","EDITING","$450","3-story sequence"),
    ("Feb 20","Instagram","Stories","Casetify","SCHEDULED","$0","Part 2 stories"),
    ("Feb 22","YouTube","Community Post","Organic","DRAFT","$0","Engage audience, tease March video"),
    ("Feb 25","TikTok","Trend Video","Organic","CONCEPT","$0","Trending sound, no sponsor"),
    ("Feb 27","YouTube","Video Upload","Skillshare","SCRIPTING","$1,800","Integration + demo"),
    ("Feb 29","Instagram","Reel","Organic","CONCEPT","$0","Month wrap-up, engagement"),
]
for i,r in enumerate(cal):
    dr(ws,i+3,7,r,LGT if i%2==0 else WHT)
wd(ws,{"A":10,"B":14,"C":18,"D":18,"E":14,"F":10,"G":28})
wb.save(BASE+"04_CONTENT_CALENDAR/Sponsored_Content_Calendar.xlsx")
print("  xlsx 04_CONTENT_CALENDAR/Sponsored_Content_Calendar.xlsx")

csv_w("04_CONTENT_CALENDAR/Annual_Content_Plan.csv",
    ["Month","Sponsored Videos","Organic Videos","Target Sponsorship Revenue","Main Niche Content","Priority Platform","Notes"],
    [
        ("January 2024","3","8","$6,000","Tech and productivity","YouTube","Set rate card, send 50 pitches"),
        ("February 2024","5","6","$10,000","Lifestyle and wellness","YouTube + TikTok","Build TikTok presence"),
        ("March 2024","4","8","$11,500","Personal finance","YouTube","Tax season content = high views"),
        ("April 2024","6","6","$14,000","Tech and apps","YouTube","Spring brand campaign season"),
        ("May 2024","5","7","$12,500","Fitness and health","Instagram + TikTok","Pre-summer deals available"),
        ("June 2024","7","5","$18,000","Summer lifestyle","All platforms","Peak brand deal season"),
        ("July 2024","5","8","$13,000","Travel and tech","YouTube","Mid-year check in, raise rates"),
        ("August 2024","6","7","$16,000","Back to school","YouTube + TikTok","Education brand season"),
        ("September 2024","7","6","$19,000","Productivity","YouTube","Q4 brand budgets opening"),
        ("October 2024","8","5","$22,000","Tech launches","YouTube","Holiday season prep"),
        ("November 2024","9","4","$28,000","Holiday deals","All platforms","Highest deal season of year"),
        ("December 2024","6","7","$18,000","Year in review","YouTube","Wrap-up content performs well"),
    ]
)
print("  csv 04_CONTENT_CALENDAR/Annual_Content_Plan.csv")
print("  v 04_CONTENT_CALENDAR")

print("Building 05_BRAND_PITCH_SYSTEM...")

d = Document()
add_heading(d, "Creator Brand Pitch System")
add_para(d, "The complete outreach system for landing high-ticket sponsorships on YouTube, Instagram, and TikTok.", size=12)

add_heading(d, "THE 5-STEP PITCH PROCESS", 2)
process = [
    ("Step 1: Research (15 min per brand)", [
        "Check if they currently run creator sponsorships (search YouTube for 'brand name sponsor')",
        "Review their Facebook Ad Library for creative style",
        "Find the right contact: Brand Partnerships Manager, Head of Influencer Marketing, CMO (smaller brands)",
        "Tools: LinkedIn, Hunter.io for email finding, company website 'Press' or 'Work With Us' page",
    ]),
    ("Step 2: Personalize (5 min per brand)", [
        "Reference a specific product you've used or want to feature",
        "Mention a recent campaign you noticed (shows you did homework)",
        "Connect your audience to their customer profile specifically",
        "Avoid generic: 'I love your brand!' -- be specific about what and why",
    ]),
    ("Step 3: Send Pitch (2 min)", [
        "Subject line: 'Sponsorship Inquiry -- [Your Name] x [Brand]' or 'Creator Partnership -- [Niche] Audience'",
        "Keep email to 5-7 sentences maximum",
        "Include: who you are + niche, why you're a fit for their specific product, one social proof stat",
        "CTA: 'Happy to send over my media kit and rate card if this is of interest'",
    ]),
    ("Step 4: Follow Up (Day 5)", [
        "Bump the original email thread (don't start a new one)",
        "Add one new piece of value: a content idea specific to their brand",
        "Keep it short: 2-3 sentences max",
        "Maximum 2 follow-ups per brand in a 3-month period",
    ]),
    ("Step 5: Negotiate and Close", [
        "Know your minimum acceptable rate before the conversation starts",
        "Always counter at 20-30% above your target (room to negotiate down)",
        "Get agreement on deliverables, timeline, usage rights, and exclusivity IN WRITING",
        "Send contract immediately after verbal agreement -- never start without a signed contract",
    ]),
]
for step, items in process:
    add_heading(d, step, 3)
    for item in items:
        d.add_paragraph(item, style="List Bullet")

add_heading(d, "MEDIA KIT STATS TO INCLUDE", 2)
add_para(d, "Choose the stats that make you look best -- brands care most about engagement and audience fit:")
stats = [
    "Total subscribers/followers (across all platforms)",
    "Average views per video (last 90 days)",
    "Average engagement rate (likes + comments / views)",
    "Audience demographics: age split, top countries, gender breakdown",
    "Most viewed video with view count",
    "Previous brand partnerships (logos are more impressive than names)",
    "Testimonial from a previous sponsor (huge trust signal)",
    "Response rate if you have it ('Sponsors report X% CTR on my integrations')",
]
for s in stats:
    d.add_paragraph(s, style="List Bullet")

add_heading(d, "RATE CARD STRATEGY", 2)
rates = [
    ("YouTube Integration (45-90s mid-roll)","$500-1,500 (micro) | $1,500-5,000 (mid) | $5,000-25,000+ (macro)"),
    ("YouTube Dedicated Video","2-4x integration rate -- full video = more value"),
    ("Instagram Reel","$200-800 (micro) | $800-3,000 (mid)"),
    ("Instagram Story Series (3-5 frames)","$150-600 (micro) | $600-2,000 (mid)"),
    ("TikTok Integration","$150-500 (micro) | $500-2,000 (mid)"),
    ("Bundle (YT + IG + TikTok)","15-20% discount vs. individual rates"),
    ("Long-term Partnership (3-6 months)","10-15% monthly discount, higher total value"),
    ("Whitelisting / Paid Amplification","$200-600/month additional on top of content fee"),
]
for content_type, rate in rates:
    add_para(d, f"{content_type}:", bold=True)
    add_para(d, rate)
    d.add_paragraph()

save_doc(d, "05_BRAND_PITCH_SYSTEM/Brand_Pitch_System.docx")
print("  doc 05_BRAND_PITCH_SYSTEM/Brand_Pitch_System.docx")
print("  v 05_BRAND_PITCH_SYSTEM")

print("Building 06_ANALYTICS_DASHBOARD...")

wb = Workbook()
ws = wb.active
ws.title = "Channel Analytics Dashboard"
ws.merge_cells("A1:H1")
c=ws["A1"]; c.value="CHANNEL ANALYTICS DASHBOARD"
c.fill=hf(NAV); c.font=bf(True,16,WHT); c.alignment=al()
ws.row_dimensions[1].height=35
hr_row(ws,2,8,["METRIC","JAN 2024","FEB 2024","MAR 2024","APR 2024","MAY 2024","TREND","NOTES"],NAV,WHT)
channel_stats=[
    ("YouTube Subscribers","45,200","47,800","51,100","54,700","58,900","UP +30%","Strong growth month"),
    ("Avg Views per Video","12,400","13,800","15,200","14,900","16,400","UP +32%","New thumbnail style"),
    ("Watch Time (hours)","18,400","21,200","23,800","22,900","25,100","UP +36%","Long form working"),
    ("Click-Through Rate","4.2%","4.8%","5.1%","4.9%","5.4%","UP","A/B testing thumbnails"),
    ("Instagram Followers","12,400","13,100","13,900","14,800","15,700","UP +27%","Reels driving growth"),
    ("Instagram Avg Reach","8,200","9,100","9,800","10,400","11,200","UP +37%","Consistency paying off"),
    ("TikTok Followers","8,900","11,200","14,800","18,200","22,500","UP +153%","Viral video in March"),
    ("TikTok Avg Views","5,400","8,200","15,400","12,100","9,800","Variable","Post-viral normalization"),
    ("Email List","2,100","2,340","2,680","3,020","3,450","UP +64%","Lead magnet working"),
    ("Monthly Revenue","$4,700","$9,500","$11,700","$14,200","$13,100","UP +179%","All time high in Apr"),
]
for i,r in enumerate(channel_stats):
    dr(ws,i+3,8,r,LGT if i%2==0 else WHT)
wd(ws,{"A":28,"B":14,"C":14,"D":14,"E":14,"F":14,"G":14,"H":28})

ws2=wb.create_sheet("Video Performance")
hr_row(ws2,1,8,["VIDEO TITLE","PLATFORM","PUBLISH DATE","VIEWS","WATCH%","LIKES","SPONSOR","SPONSORSHIP REVENUE"],NAV,WHT)
videos=[
    ("10 AI Tools That Changed My Life","YouTube","2024-01-10","48,200","52%","3,840","NordVPN","$2,500"),
    ("How I Made $8k Last Month as a Creator","YouTube","2024-02-03","102,400","61%","9,100","None","$0"),
    ("Squarespace Tutorial 2024","YouTube","2024-02-20","31,800","45%","2,290","Squarespace","$4,000"),
    ("My Morning Routine (Honest)","Instagram","2024-01-22","94,200","--","4,200","HelloFresh","$1,200"),
    ("3 Mistakes New Creators Make","TikTok","2024-02-15","284,000","--","18,200","None","$0"),
    ("How to Start a YouTube Channel","YouTube","2024-03-07","67,900","58%","5,400","Skillshare","$1,800"),
    ("G FUEL Taste Test","TikTok","2024-02-07","142,000","--","11,800","G FUEL","$600"),
    ("My Camera Setup 2024","YouTube","2024-03-20","28,400","48%","2,100","None","$0"),
]
for i,r in enumerate(videos):
    dr(ws2,i+2,8,r,LGT if i%2==0 else WHT)
wd(ws2,{"A":35,"B":14,"C":14,"D":14,"E":12,"F":12,"G":18,"H":22})
wb.save(BASE+"06_ANALYTICS_DASHBOARD/Channel_Analytics_Dashboard.xlsx")
print("  xlsx 06_ANALYTICS_DASHBOARD/Channel_Analytics_Dashboard.xlsx")
print("  v 06_ANALYTICS_DASHBOARD")

print("Building 07_CONTRACTS_AND_INVOICES...")

d = Document()
add_heading(d, "Creator Sponsorship Agreement Template")
add_para(d, "SPONSORED CONTENT AGREEMENT", bold=True, size=14)
d.add_paragraph()

add_para(d, "This Sponsored Content Agreement ('Agreement') is made between:")
add_para(d, "CREATOR: [Your Name / Channel Name] ('Creator')", bold=True)
add_para(d, "BRAND: [Company Name] ('Brand')", bold=True)
add_para(d, "Effective Date: [DATE]", bold=True)
d.add_paragraph()

clauses = [
    ("1. SPONSORSHIP DETAILS", [
        "Platform: [YouTube / Instagram / TikTok / Other]",
        "Content Type: [Integration / Dedicated Video / Story Series / Other]",
        "Video/Post Title/Topic: [Description]",
        "Publishing Date: [DATE]",
        "Sponsorship Segment Length: [30s / 45s / 60s / Full Video]",
        "Segment Position: [Pre-roll / Mid-roll / End card]",
        "Required Talking Points: [List from brief]",
        "Required Call to Action: [URL / Promo code / App store link]",
        "Promo Code (if applicable): [CODE]",
    ]),
    ("2. FEE AND PAYMENT", [
        "Sponsorship Fee: $[AMOUNT] USD",
        "Payment Schedule: [50% upon contract signing / 100% upon delivery / Net 30]",
        "Payment Method: [PayPal / Wire Transfer / Stripe]",
        "Invoice will be sent on: [DATE or 'upon delivery']",
        "Late payment fee: 1.5% per month after 30 days",
    ]),
    ("3. DELIVERABLES", [
        "Creator will deliver the following to Brand by [DATE]:",
        "- [X] published video(s) or post(s) on [Platform]",
        "- Analytics screenshot at [7 days / 30 days] post-publish",
        "- Sponsored segment timestamps (for YouTube)",
        "- Link to published content",
    ]),
    ("4. DISCLOSURE REQUIREMENTS", [
        "Creator will clearly disclose the paid partnership per FTC guidelines:",
        "- YouTube: Verbal disclosure at start of sponsored segment + written disclosure in description",
        "- Instagram: #ad, #sponsored, or paid partnership label",
        "- TikTok: Branded content toggle + #ad in caption",
        "Failure to disclose is a violation of this agreement and FTC regulations.",
    ]),
    ("5. CONTENT RIGHTS AND APPROVALS", [
        "Creator retains creative control over content unless otherwise specified.",
        "Brand may request approval of the sponsored segment script before filming.",
        "Brand approval (if required) must be provided within [2] business days.",
        "Creator retains ownership of all content. Brand receives a license (see Usage Rights).",
    ]),
    ("6. USAGE RIGHTS", [
        "Brand may share/repost the content on their own social channels for [X months].",
        "Paid advertising using Creator's content: [Included / Not included / Add-on: $X/mo]",
        "Whitelisting through Creator's handle: [Included / Not included / Add-on: $X/mo]",
        "Duration of all rights: [6 months / 12 months / Perpetual]",
        "Geographic territory: [Worldwide / Specific country]",
    ]),
    ("7. EXCLUSIVITY", [
        "[ ] No exclusivity -- Creator may work with competing brands in same category",
        "[ ] Category exclusivity: Creator will not sponsor [Category] competitors for [X months]",
        "[ ] Broad exclusivity: Creator will not sponsor any direct competitor for [X months]",
        "Exclusivity fee (if applicable): $[X]/month additional",
    ]),
    ("8. TERM AND TERMINATION", [
        "This Agreement begins on the Effective Date and continues until all deliverables are published.",
        "Either party may terminate with 7 days written notice before content filming begins.",
        "If Brand cancels after filming: Creator retains the full fee.",
        "If Creator cancels without cause: Creator refunds the deposit.",
    ]),
    ("9. SIGNATURES", [
        "Creator: ________________________  Date: ____________",
        "Printed Name: ____________________________",
        "",
        "Brand Representative: _________________  Date: ____________",
        "Title: ____________________  Company: ____________________",
    ]),
]
for title, items in clauses:
    add_heading(d, title, 2)
    for item in items:
        if item:
            add_para(d, item)
        else:
            d.add_paragraph()

save_doc(d, "07_CONTRACTS_AND_INVOICES/Sponsorship_Agreement_Template.docx")
print("  doc 07_CONTRACTS_AND_INVOICES/Sponsorship_Agreement_Template.docx")

d2 = Document()
add_heading(d2, "Professional Invoice Template Guide")
add_para(d2, "What to include on every creator invoice for professional, prompt payment:", size=12)
invoice_items = [
    "HEADER: Your Name / Business Name, Logo (if applicable), 'INVOICE' in large text",
    "YOUR INFO: Name, Address, Email, Phone, Tax ID/EIN (if you have one)",
    "CLIENT INFO: Brand name, billing contact name, billing email address",
    "INVOICE NUMBER: Sequential (INV-2024-001, INV-2024-002, etc.)",
    "INVOICE DATE: Date you're sending it",
    "DUE DATE: 30 days from invoice date (or per contract terms)",
    "LINE ITEMS: Each deliverable on its own line with description and price",
    "SUBTOTAL: Sum before any discounts",
    "DISCOUNT: If applicable",
    "TOTAL DUE: Clear, prominent, large text",
    "PAYMENT INSTRUCTIONS: Bank details, PayPal address, or payment link",
    "NOTES: 'Thank you for working with me! Please note late fees apply after [date]'",
]
for item in invoice_items:
    d2.add_paragraph(item, style="List Bullet")

add_heading(d2, "RECOMMENDED INVOICING TOOLS", 2)
tools = [
    ("Wave (Free)", "Professional invoices, payment links, automatic reminders -- completely free"),
    ("HoneyBook ($16/mo)", "CRM + contracts + invoices + payment processing in one platform"),
    ("FreshBooks ($15/mo)", "Best invoice tracking, great for multiple clients"),
    ("PayPal Invoice (Free)", "Simple, widely accepted, instant payment option"),
    ("Stripe Invoice (2.9% + $0.30)", "Professional, great for international brands"),
]
for tool, desc in tools:
    add_para(d2, f"{tool}: {desc}")

save_doc(d2, "07_CONTRACTS_AND_INVOICES/Invoice_Guide.docx")
print("  doc 07_CONTRACTS_AND_INVOICES/Invoice_Guide.docx")
print("  v 07_CONTRACTS_AND_INVOICES")

print("Building 08_NOTION_DATABASES...")

csv_w("08_NOTION_DATABASES/Sponsorship_Master_DB.csv",
    ["Deal Name","Brand","Platform","Content Type","Publish Date","Fee","Status","Contact Email","Usage Rights","Exclusivity","Payment Status","Rating","Notes"],
    [
        ("NordVPN Q1 YT","NordVPN","YouTube","Integration","2024-02-01","$2,500","COMPLETED","sarah@nordvpn.com","12 months","No","PAID","5","Re-pitched for Q2"),
        ("Squarespace Dedicated","Squarespace","YouTube","Dedicated Video","2024-02-20","$4,000","COMPLETED","jake@sq.com","6 months","No","PAID","4","Good brand to work with"),
        ("HelloFresh IG","HelloFresh","Instagram","Story Series","2024-01-30","$1,200","COMPLETED","mia@hf.com","3 months","No","PAID","4","Great brief clarity"),
        ("Surfshark TikTok","Surfshark","TikTok","Integration","2024-02-12","$800","COMPLETED","chris@ss.com","6 months","No","PAID","4","Fast payment"),
        ("Notion Integration","Notion","YouTube","Integration","TBD","$3,000","NEGOTIATING","ana@notion.so","12 months","Category 3mo","PENDING","--","Counter $3,500"),
        ("Skillshare Q1","Skillshare","YouTube","Integration","2024-03-01","$1,800","COMPLETED","sr@sk.com","12 months","No","PAID","5","Monthly deal potential"),
        ("G FUEL TikTok","G FUEL","TikTok","Gifting + Fee","2024-02-07","$600","COMPLETED","br@gf.com","3 months","No","PAID","3","Low fee but fast"),
        ("Casetify IG","Casetify","Instagram","Post + Stories","2024-02-20","$900","COMPLETED","li@ca.com","6 months","No","PAID","4","Good collab"),
    ]
)
print("  csv 08_NOTION_DATABASES/Sponsorship_Master_DB.csv")

csv_w("08_NOTION_DATABASES/Brand_Contact_Database.csv",
    ["Brand Name","Industry","Contact Name","Contact Email","Contact Title","Platform Focus","Budget Range","Response Time","Relationship Status","Notes"],
    [
        ("NordVPN","VPN/Tech","Sarah M.","sarah@nordvpn.com","Creator Partnerships Lead","YouTube","$2,000-$5,000","24 hours","Active Partner","Monthly deals available"),
        ("Squarespace","Website Builder","Jake T.","jake@squarespace.com","Influencer Marketing","YouTube","$3,000-$8,000","48 hours","Active Partner","Q3 budget opens July"),
        ("HelloFresh","Meal Kits","Mia L.","mia@hellofresh.com","Social Media Manager","Instagram","$800-$2,000","Same day","Active Partner","Seasonal campaigns"),
        ("Surfshark","VPN/Tech","Chris K.","chris@surfshark.com","Content Partnerships","TikTok","$500-$1,500","48 hours","Active Partner","High volume brand"),
        ("Notion","Productivity","Ana R.","ana@notion.so","Creator Programs","YouTube","$2,000-$5,000","5 days","Negotiating","Counter in progress"),
        ("BetterHelp","Mental Health","--","pr@betterhelp.com","PR Team","YouTube","$4,000-$8,000","No reply yet","Outreach","Top-rated brand"),
        ("Skillshare","E-Learning","--","sr@skillshare.com","Creator Relations","YouTube","$1,500-$3,000","3 days","Active Partner","Fast contract turnaround"),
        ("G FUEL","Energy Drink","Brandon F.","brandon@gfuel.com","Influencer Team","TikTok","$400-$1,000","24 hours","Active Partner","Great for TikTok"),
    ]
)
print("  csv 08_NOTION_DATABASES/Brand_Contact_Database.csv")
print("  v 08_NOTION_DATABASES")

print("Building 09_YOUTUBE_SPECIFIC...")

d = Document()
add_heading(d, "YouTube Sponsorship Playbook")
add_para(d, "Everything specific to YouTube sponsorships -- integration formats, best practices, and how to maximize sponsor value.", size=12)

add_heading(d, "YOUTUBE INTEGRATION FORMATS", 2)
formats = [
    ("Pre-roll (0:00-0:30)", "Highest drop-off point. Works best for: high-recognition brands, short message. Rarely recommended -- most brands prefer mid-roll."),
    ("Early Mid-roll (2:00-4:00)", "Before full drop-off. Good for: lifestyle brands, short integration. Risk: some viewers skip forward."),
    ("Mid-roll (25-35% into video)", "Peak performance placement. Most requested by brands. Optimal length: 45-60 seconds. Highest CPM."),
    ("Late Mid-roll (60-70% into video)", "High-intent viewer. Audience is already engaged. Good for: detailed products requiring explanation."),
    ("End card (final 20-30 sec)", "Lowest engagement but lowest disruption. Good for: simple CTAs, brand awareness plays. Often combined with mid-roll."),
]
for name, desc in formats:
    add_heading(d, name, 3)
    add_para(d, desc)

add_heading(d, "PERFECT INTEGRATION SCRIPT STRUCTURE", 2)
script = [
    ("0:00 - Transition line (5s)", "'Before I get into [topic], I want to take 30 seconds to tell you about [Brand]...'"),
    ("0:05 - Personal hook (10s)", "Why YOU specifically use/care about this product. Authentic personal connection."),
    ("0:15 - Key benefit (15s)", "The single most relevant benefit for your audience. One idea only."),
    ("0:30 - Social proof (5s)", "Quick stat, testimonial, or your own result: 'I've been using this for 6 months and...'"),
    ("0:35 - CTA (10s)", "Clear single action: 'Use my code [CODE] for [X]% off at [URL]' + show URL on screen"),
    ("0:45 - Back to content", "'Okay, now back to [video topic]...'"),
]
for time, desc in script:
    add_para(d, f"{time}: {desc}")
    d.add_paragraph()

add_heading(d, "YOUTUBE-SPECIFIC LEGAL REQUIREMENTS", 2)
legal = [
    "Verbal disclosure: State 'This video is sponsored by [Brand]' or 'This portion of the video is sponsored by [Brand]' at the start of the integration",
    "Description disclosure: Include 'This video is sponsored by [Brand]. [Brand URL]' in the first 3 lines of the description",
    "YouTube Paid Promotion checkbox: Toggle ON in YouTube Studio before publishing (Settings > Paid Promotions)",
    "Content policy: BetterHelp, weight loss products, and some financial services have additional YouTube policies",
    "FTC guidelines apply: Authentic review, no false claims, must disclose material connection",
]
for l in legal:
    d.add_paragraph(l, style="List Bullet")

add_heading(d, "NEGOTIATION TIPS SPECIFIC TO YOUTUBE", 2)
tips = [
    "Price per 1,000 views (CPM-style): Average rates are $20-50 CPM for brand-safe channels",
    "Never show your subscriber count as your main metric -- show average views instead",
    "30-day view average is more persuasive than peak views",
    "Offer to share analytics dashboard screenshot as proof of performance",
    "Ask brands what their current YouTube CPM is -- if over $30, you have leverage",
    "If brand wants exclusivity, use it as leverage to raise your rate by 20-40%",
    "Pitch 3 and 6-month packages -- brands love predictability",
    "Referral revenue: if your code works, share the data -- it justifies repeat booking",
]
for t in tips:
    d.add_paragraph(t, style="List Bullet")

save_doc(d, "09_YOUTUBE_SPECIFIC/YouTube_Sponsorship_Playbook.docx")
print("  doc 09_YOUTUBE_SPECIFIC/YouTube_Sponsorship_Playbook.docx")
print("  v 09_YOUTUBE_SPECIFIC")

print("Building 10_INSTAGRAM_SPECIFIC...")

d = Document()
add_heading(d, "Instagram Sponsorship Playbook")
add_para(d, "Instagram-specific strategies for Reels, Stories, and Feed posts -- from pitching to publishing.", size=12)

add_heading(d, "INSTAGRAM CONTENT FORMATS FOR SPONSORS", 2)
formats = [
    ("Reels (Most Powerful)", "15-90 seconds, algorithm-favored, best for reach. Reels reach 67% MORE non-followers than feed posts. Ideal for: product demos, tutorials, lifestyle. Rate: highest per deliverable."),
    ("Stories (6 frames)", "Disappear in 24 hours. Best for: time-sensitive deals, link sticker CTAs, swipe-up offers. Audience is highly engaged -- these are followers, not discoverers. Link sticker in stories is the best converting format on Instagram."),
    ("Carousel Feed Post", "1-10 images. High save rate, algorithmic longevity. Best for: educational content, product comparisons, before/after. Saves are weighted heavily by Instagram algorithm."),
    ("Single Feed Post", "Lowest reach but most permanent. Good for: brand awareness, long-term portfolio. Rates lower than Reels."),
    ("Instagram Live", "Highest authenticity. Best for: product unboxing, Q&As with brand. Rarely requested -- usually for larger channels."),
]
for name, desc in formats:
    add_heading(d, name, 3)
    add_para(d, desc)

add_heading(d, "INSTAGRAM STORY SEQUENCE TEMPLATE", 2)
stories = [
    ("Frame 1 (Hook)", "Pattern interrupt: Close-up of product, question overlay, or bold text. Example: 'I've been hiding something from you...'"),
    ("Frame 2 (Problem)", "Relatable pain point your audience has. Brief, authentic, personal. Tap to next."),
    ("Frame 3 (Discovery)", "How you found this product/brand. Keep it natural -- not scripted."),
    ("Frame 4 (Proof)", "Your result, reaction, or specific benefit. Show, don't just tell."),
    ("Frame 5 (Offer)", "Discount code or special offer. Clear, visible, easy to remember."),
    ("Frame 6 (CTA)", "Link sticker + 'Tap here for [X]% off' -- this frame should be simple and clear."),
]
for frame, desc in stories:
    add_heading(d, frame, 3)
    add_para(d, desc)

add_heading(d, "DISCLOSURE ON INSTAGRAM", 2)
disclosures = [
    "Instagram Partnership Label: Use 'Add paid partnership label' in Advanced Settings -- shows 'Paid partnership with [Brand]' above your post",
    "Caption disclosure: Include #ad or #sponsored in the FIRST LINE of caption (not buried in hashtags)",
    "Stories: Add #ad text sticker or use the Paid Partnership sticker in the tool tray",
    "FTC rule: Disclosure must be clear and conspicuous -- not hidden, not just in hashtag list",
]
for d_item in disclosures:
    d.add_paragraph(d_item, style="List Bullet")

save_doc(d, "10_INSTAGRAM_SPECIFIC/Instagram_Sponsorship_Playbook.docx")
print("  doc 10_INSTAGRAM_SPECIFIC/Instagram_Sponsorship_Playbook.docx")
print("  v 10_INSTAGRAM_SPECIFIC")

print("Building 11_TIKTOK_SPECIFIC...")

d = Document()
add_heading(d, "TikTok Sponsorship Playbook")
add_para(d, "TikTok-specific strategies for brand deals -- from finding sponsors to maximizing performance.", size=12)

add_heading(d, "WHY TIKTOK SPONSORSHIPS ARE DIFFERENT", 2)
diff = [
    "Algorithm-first: even small creators can go viral, making follower count less important",
    "Authenticity premium: over-polished = skipped. Native, casual content performs better",
    "Short attention: first 1-2 seconds determine everything. Hook IS the content.",
    "Sound-on platform: music, voiceover, and sound design matter much more",
    "Fast turnaround: brands expect production in days, not weeks",
    "TikTok Creator Marketplace: official platform for brand-creator matching",
]
for d_item in diff:
    d.add_paragraph(d_item, style="List Bullet")

add_heading(d, "TIKTOK INTEGRATION SCRIPT STRUCTURE", 2)
structure = [
    ("0:00-0:03 (Hook)", "POV opener, visual hook, or bold statement. No intro, no 'hey guys'. The first frame is everything."),
    ("0:03-0:10 (Problem/Context)", "1-2 sentences of relatable context. Why does this product matter to YOUR viewer?"),
    ("0:10-0:25 (Product Intro)", "Natural product reveal or demo. Hold product on screen for 3+ seconds. Show, don't lecture."),
    ("0:25-0:40 (Benefit/Result)", "The payoff -- what happened, how it felt, why it mattered. Authentic reaction."),
    ("0:40-0:55 (Offer/CTA)", "Clear offer: code, link in bio, or product name. Repeat once. End on energy."),
    ("0:55-1:00 (Hook loop)", "Optional: loop back to the opening frame for watch time -- TikTok rewards loops."),
]
for time, desc in structure:
    add_heading(d, time, 3)
    add_para(d, desc)

add_heading(d, "TIKTOK CREATOR MARKETPLACE GUIDE", 2)
marketplace = [
    "Access: TikTok Studio > Creator Tools > TikTok Creator Marketplace",
    "Profile optimization: Complete all sections, link portfolio, set niche tags",
    "Brands search by: follower count, niche, engagement rate, average views",
    "You can also apply to brand campaigns posted on the marketplace",
    "Commission rates on marketplace may be lower than direct deals -- negotiate off-platform",
    "Top performing videos attract inbound brand requests (keep posting consistently)",
]
for m in marketplace:
    d.add_paragraph(m, style="List Bullet")

add_heading(d, "TIKTOK DISCLOSURE REQUIREMENTS", 2)
disclosures = [
    "Branded Content toggle: Must enable 'Branded Content' toggle in TikTok settings before posting",
    "Caption: Include #ad or #sponsored in caption",
    "Verbal: 'This video is sponsored by [Brand]' or similar in the video itself",
    "TikTok auto-adds: enabling Branded Content automatically adds a 'Paid partnership' label to the video",
]
for d_item in disclosures:
    d.add_paragraph(d_item, style="List Bullet")

save_doc(d, "11_TIKTOK_SPECIFIC/TikTok_Sponsorship_Playbook.docx")
print("  doc 11_TIKTOK_SPECIFIC/TikTok_Sponsorship_Playbook.docx")
print("  v 11_TIKTOK_SPECIFIC")

print("Building 12_BONUS_RESOURCES...")

# Creator pitch deck PPTX
p = prs()

s1 = sl(p)
box(s1,0,0,13.33,7.5,PNAV)
box(s1,0,0,13.33,0.5,PACC)
box(s1,0,7.0,13.33,0.5,PACC)
tx(s1,"CONTENT CREATOR",1,1.5,11.33,1.2,sz=50,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s1,"Sponsorship Tracker",1,2.9,11.33,0.8,sz=36,bold=False,col=PGLD,a=PP_ALIGN.CENTER)
tx(s1,"The complete system for finding, closing, and managing brand sponsorships",1,3.9,11.33,0.6,sz=18,col=PWHT,a=PP_ALIGN.CENTER)
tx(s1,"YouTube -- Instagram -- TikTok",1,6.1,11.33,0.5,sz=16,col=PGLD,a=PP_ALIGN.CENTER)

s2 = sl(p)
box(s2,0,0,13.33,7.5,PNAV)
box(s2,0,0,13.33,1.2,PACC)
tx(s2,"WHAT'S INSIDE",0.5,0.2,12,0.8,sz=32,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
items2=[
    ("Master Tracker","All deals in one Excel dashboard"),
    ("Brand Pipeline","Stage-by-stage deal management"),
    ("Tax Tracker","Income + quarterly estimates"),
    ("Content Calendar","Sponsored + organic planning"),
    ("Pitch System","Templates for every platform"),
    ("Analytics Dashboard","Channel + video performance"),
    ("Contracts","Sponsorship agreement template"),
    ("Notion Databases","3 importable CSV databases"),
    ("Platform Playbooks","YouTube, Instagram, TikTok guides"),
    ("Bonus Resources","Tools, rates, growth checklist"),
]
for idx,(label,desc) in enumerate(items2):
    col_idx=idx%2; row_idx=idx//2
    cx=0.3+col_idx*6.5; cy=1.4+row_idx*1.1
    box(s2,cx,cy,6.2,0.9,PACC)
    tx(s2,f"{label}: {desc}",cx+0.15,cy+0.1,5.9,0.7,sz=14,col=PWHT)

s3 = sl(p)
box(s3,0,0,13.33,7.5,PNAV)
box(s3,0,0,13.33,1.2,PGLD)
tx(s3,"CREATOR INCOME MILESTONES",0.5,0.2,12,0.8,sz=30,bold=True,col=PNAV,a=PP_ALIGN.CENTER)
milestones=[
    ("$500+/mo","First 3 brand deals -- starter packages"),
    ("$2,000+/mo","5-7 deals -- mid-roll integrations"),
    ("$5,000+/mo","10+ deals -- dedicated videos + bundles"),
    ("$10,000+/mo","Retainers + whitelisting + multi-platform"),
]
for idx,(num,label) in enumerate(milestones):
    col=idx%2; row=idx//2
    x=0.5+col*6.5; y=1.5+row*2.5
    box(s3,x,y,5.8,2.0,PACC)
    tx(s3,num,x,y+0.2,5.8,1.0,sz=40,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(s3,label,x,y+1.2,5.8,0.6,sz=16,col=PWHT,a=PP_ALIGN.CENTER)

pptx_path=BASE+"12_BONUS_RESOURCES/Creator_Sponsorship_Deck.pptx"
os.makedirs(os.path.dirname(pptx_path),exist_ok=True)
p.save(pptx_path)
print("  pptx 12_BONUS_RESOURCES/Creator_Sponsorship_Deck.pptx")

d = Document()
add_heading(d, "Sponsorship Rate Guide by Platform and Niche")
add_para(d, "Reference rates across niches, platforms, and follower counts to help you price with confidence.", size=12)

add_heading(d, "YOUTUBE RATES BY SUBSCRIBER COUNT", 2)
yt_rates = [
    ("1K-10K (Nano)", "$50-150 integration", "$200-500 dedicated video", "Focus on gifting + small deals to build portfolio"),
    ("10K-50K (Micro)", "$150-500 integration", "$500-1,500 dedicated", "Sweet spot for authenticity -- brands love micro"),
    ("50K-100K (Mid)", "$500-2,000 integration", "$1,500-5,000 dedicated", "Start applying for $1,000+ deals"),
    ("100K-500K", "$2,000-8,000 integration", "$5,000-20,000 dedicated", "Multi-deal packages become possible"),
    ("500K-1M", "$8,000-20,000 integration", "$20,000-50,000 dedicated", "Agency representation recommended"),
    ("1M+ (Macro)", "$20,000+ integration", "$50,000-200,000+ dedicated", "Direct brand deals at premium rates"),
]
for tier, int_rate, ded_rate, notes in yt_rates:
    add_heading(d, tier, 3)
    add_para(d, f"Integration: {int_rate}")
    add_para(d, f"Dedicated: {ded_rate}")
    add_para(d, f"Strategy: {notes}")
    d.add_paragraph()

add_heading(d, "INSTAGRAM RATES BY FOLLOWER COUNT", 2)
ig_rates = [
    ("5K-20K","$50-150 per post","$100-300 per story series"),
    ("20K-50K","$150-400 per post","$300-700 per story series"),
    ("50K-100K","$400-1,000 per post","$700-1,500 per story series"),
    ("100K-500K","$1,000-3,500 per post","$1,500-5,000 per story series"),
    ("500K+","$3,500-10,000+ per post","$5,000+ per story series"),
]
for tier, post, story in ig_rates:
    add_para(d, f"{tier}: Feed/Reel -- {post} | Stories -- {story}")

add_heading(d, "TIKTOK RATES BY FOLLOWER COUNT", 2)
tt_rates = [
    ("5K-20K","$25-100 per video","Low follower, high views possible"),
    ("20K-50K","$100-300 per video","Often more than Instagram for same followers"),
    ("50K-100K","$300-800 per video","Viral potential adds value"),
    ("100K-500K","$800-3,000 per video","Strong CPM for brands"),
    ("500K+","$3,000-10,000+ per video","Top tier TikTok rates"),
]
for tier, rate, note in tt_rates:
    add_para(d, f"{tier}: {rate} -- {note}")

save_doc(d, "12_BONUS_RESOURCES/Sponsorship_Rate_Guide.docx")
print("  doc 12_BONUS_RESOURCES/Sponsorship_Rate_Guide.docx")
print("  v 12_BONUS_RESOURCES")

print("Building PDF...")
make_pdf("Creator_Sponsorship_Tracker_Guide.pdf",
    "Content Creator Sponsorship Tracker",
    "The complete system for finding, closing, and managing brand sponsorships",
    [
        ("What's Inside", [
            "Master Sponsorship Tracker: All deals in one Excel dashboard (10 columns)",
            "Brand Deal Pipeline: Stage-by-stage management from outreach to payment",
            "Income and Tax Tracker: Monthly income + quarterly tax estimates",
            "Content Calendar: Sponsored + organic content planning for the full year",
            "Brand Pitch System: Templates and scripts for every platform",
            "Analytics Dashboard: Channel stats + video performance tracking",
            "Contracts: Full sponsorship agreement template (Word)",
            "Platform Playbooks: YouTube, Instagram, and TikTok specific guides",
        ]),
        ("Sponsorship Deal Stages", [
            "Stage 1 - Outreach: Initial contact sent, awaiting response",
            "Stage 2 - Interested: Brand replied, media kit requested",
            "Stage 3 - Pitched: Proposal and rate card sent",
            "Stage 4 - Negotiating: Back and forth on rates or deliverables",
            "Stage 5 - Contract Sent: Agreement sent for signature",
            "Stage 6 - Brief Received: Contract signed, in production",
            "Stage 7 - Delivered: Content submitted for review",
            "Stage 8 - Paid: Payment received, deal complete",
        ]),
        ("YouTube Integration Best Practices", [
            "Best placement: 25-35% into video (mid-roll, highest engagement)",
            "Optimal length: 45-60 seconds (enough to sell, short enough to not lose viewers)",
            "Script structure: Transition -- Hook -- Benefit -- Proof -- CTA",
            "Always include: verbal disclosure, description disclosure, YouTube paid promotion toggle",
            "Negotiate for: 30-day analytics report share (proof for re-booking)",
        ]),
        ("Instagram Sponsorship Tips", [
            "Reels: Highest reach, best for acquisition campaigns, premium rates",
            "Stories: Best CTR with link sticker, use for time-sensitive offers",
            "Disclosure: Use Partnership label + #ad in first line of caption",
            "Story sequence: 5-6 frames covering hook, problem, discovery, result, offer, CTA",
            "Negotiate for: 30-day paid ads rights (allows brand to boost your post)",
        ]),
        ("TikTok Brand Deal Tips", [
            "First 2 seconds are everything -- native hook that fits the platform",
            "Enable Branded Content toggle before publishing -- required by TikTok",
            "Creator Marketplace: official brand-matching platform by TikTok",
            "Your rate should reflect VIEW potential, not just follower count",
            "Bundle TikTok + Instagram for higher total deal value",
        ]),
        ("Income Growth Milestones", [
            "Month 1-2: First 2-3 deals, $200-600 each, focus on portfolio quality",
            "Month 3-4: 5-7 deals/month, rates $500-1,500, $3,000-8,000/month",
            "Month 5-6: First repeat clients, rates increase 25-40% with proven results",
            "Month 7-9: Dedicated videos, $5,000-10,000/month, first retainer proposals",
            "Month 10-12: Multi-platform packages, $10,000-20,000/month potential",
        ]),
    ]
)
print("  pdf Creator_Sponsorship_Tracker_Guide.pdf")

print("Building Asset Manifest...")
manifest = []
for folder in FOLDERS:
    fp = BASE+folder
    if os.path.exists(fp):
        for fn in sorted(os.listdir(fp)):
            fpath=os.path.join(fp,fn)
            sz=os.path.getsize(fpath) if os.path.isfile(fpath) else 0
            manifest.append({"folder":folder,"file":fn,"size_kb":round(sz/1024,1)})

csv_w("Asset_Manifest.csv",["Folder","File","Size_KB"],[[m["folder"],m["file"],m["size_kb"]] for m in manifest])
with open(BASE+"Asset_Manifest.json","w") as f:
    json.dump({"product":"Content Creator Sponsorship Tracker","files":manifest},f,indent=2)
print("  csv Asset_Manifest.csv")
print("  json Asset_Manifest.json")

print("Building ZIP...")
ZIP="/home/user/oqul-phase55-production/creator-sponsorship-tracker/BUYER_DOWNLOAD_CreatorSponsorshipTracker.zip"
with zipfile.ZipFile(ZIP,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        for fn in files:
            fp=os.path.join(root,fn)
            z.write(fp,os.path.relpath(fp,os.path.dirname(BASE)))
print(f"  zip {ZIP}")

print("Writing Etsy listing...")
os.makedirs("/home/user/oqul-phase55-production/etsy-listings",exist_ok=True)
listing="""TITLE:
Content Creator Sponsorship Tracker | Brand Deal Tracker, Rate Card, Contracts, YouTube Instagram TikTok | 50+ Files

DESCRIPTION:
Finally -- one place to track every brand deal, manage your pipeline, organize your income, and grow your sponsorship revenue on YouTube, Instagram, and TikTok.

WHAT'S INSIDE (50+ files across 12 folders):

01. MASTER SPONSORSHIP TRACKER (Excel)
- All deals in one dashboard: brand, platform, content type, fee, status, payment
- Revenue Summary by month
- 10 sample deals fully filled in

02. BRAND DEAL PIPELINE (Excel + Word)
- 8-stage deal tracking system (Outreach to Paid)
- Pipeline metrics guide: how to track weekly deal flow
- Pipeline Management Guide (Word)

03. INCOME AND TAX TRACKER (Excel + Word)
- Monthly income tracker with auto-calculated tax estimate
- Quarterly tax planner with due dates
- Business expense tracker (deductible expenses)
- Creator Tax Guide (what to track, what to deduct)

04. CONTENT CALENDAR (Excel + CSV)
- Monthly sponsored + organic content calendar
- Full 12-month annual content plan (CSV, Notion-importable)

05. BRAND PITCH SYSTEM (Word)
- 5-step pitch process for every platform
- Media kit stats guide (what to include)
- Rate card strategy by platform and niche
- Instagram, YouTube, and TikTok pitch tips

06. ANALYTICS DASHBOARD (Excel)
- Channel growth tracker (subscribers, views, watch time, CTR)
- Video performance tracker (views, engagement, sponsor, revenue)

07. CONTRACTS AND INVOICES (Word x2)
- Full Sponsorship Agreement Template (Word) -- 9-clause professional contract
- Invoice Guide + recommended invoicing tools

08. NOTION DATABASES (CSV, Notion-importable)
- Sponsorship Master Database (13 columns, 8 sample deals)
- Brand Contact Database (relationship tracker, budget info)

09. YOUTUBE SPONSORSHIP PLAYBOOK (Word)
- All integration formats and optimal placement
- Perfect 60-second integration script structure
- YouTube-specific legal disclosure requirements
- Rate negotiation tips for YouTube creators

10. INSTAGRAM SPONSORSHIP PLAYBOOK (Word)
- All Instagram content formats (Reels, Stories, Feed, Live)
- 6-frame Story sequence template
- Instagram disclosure requirements

11. TIKTOK SPONSORSHIP PLAYBOOK (Word)
- Why TikTok is different (algorithm-first platform)
- 60-second integration script structure
- TikTok Creator Marketplace guide
- Disclosure requirements

12. BONUS RESOURCES
- Sponsorship Rate Guide (Word): rates by platform + follower tier
- Creator Sponsorship Pitch Deck (PowerPoint, Canva-importable)
- Creator Sponsorship Tracker Guide (PDF)

WHO THIS IS FOR:
- YouTube creators (any subscriber count) looking to land brand deals
- Instagram creators wanting professional sponsor management
- TikTok creators ready to monetize beyond the Creator Fund
- Multi-platform creators juggling multiple brand partnerships

WHY BUY THIS:
Stop managing brand deals in your email inbox. This tracker gives you a professional system for EVERY deal -- from the first pitch email to the final payment -- so nothing slips through the cracks and you always know exactly where your money is.

INSTANT DOWNLOAD: All files delivered immediately after purchase.

FORMATS INCLUDED: Excel (XLSX), Word (DOCX), CSV (Notion-importable), PowerPoint (PPTX), PDF

TAGS:
content creator sponsorship tracker, brand deal tracker, youtube sponsorship template, creator income tracker, influencer contract template, brand deal spreadsheet, creator business kit, youtube creator tools, instagram sponsorship template, tiktok brand deal tracker, creator tax tracker, sponsorship rate card, influencer media kit"""

with open("/home/user/oqul-phase55-production/etsy-listings/14_CreatorSponsorshipTracker_Listing.txt","w",encoding="utf-8") as f:
    f.write(listing)
print("  etsy 14_CreatorSponsorshipTracker_Listing.txt")

print("\nContent Creator Sponsorship Tracker COMPLETE!")
print(f"ZIP: {ZIP}")
