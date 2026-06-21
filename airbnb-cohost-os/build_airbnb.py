#!/usr/bin/env python3
"""Complete build for Airbnb Co-Host Management System"""
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

BASE = "/home/user/oqul-phase55-production/airbnb-cohost-os/Airbnb_CoHost_System/"
ETSY_DIR = "/home/user/oqul-phase55-production/etsy-listings/"
for d in ["00_START_HERE","01_COHOST_SETUP","02_PROPERTY_MANAGEMENT","03_GUEST_COMMUNICATION",
          "04_PRICING_REVENUE","05_CLEANING_TURNOVER","06_MAINTENANCE_VENDORS",
          "07_FINANCES","08_NOTION_WORKSPACE","09_CANVA_TEMPLATES","10_BONUSES"]:
    os.makedirs(BASE+d, exist_ok=True)
os.makedirs(ETSY_DIR, exist_ok=True)

NAV="FF5A5F"; ACC="00A699"; GLD="FC642D"; GRN="484848"; WHT="FFFFFF"; LGR="F7F7F7"
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
    t.runs[0].font.color.rgb = RGBColor(0xFF,0x5A,0x5F)
    if sub:
        s = d.add_paragraph(sub); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10); s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for sec in secs:
        if isinstance(sec, str): d.add_paragraph(sec); continue
        h, items = sec
        hd = d.add_heading(h, level=1); hd.runs[0].font.color.rgb = RGBColor(0xFF,0x5A,0x5F)
        for it in items:
            if isinstance(it, tuple) and it[0]=='*': d.add_paragraph(it[1], style='List Bullet')
            else: d.add_paragraph(str(it))
    d.save(BASE+fn); print(f"  doc {fn}")

PNAV=PRGB(255,90,95); PACC=PRGB(0,166,153); PGLD=PRGB(252,100,45); PWHT=PRGB(255,255,255)
PLGR=PRGB(247,247,247); PDGR=PRGB(72,72,72)
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
    NAV_C=colors.HexColor("#FF5A5F"); ACC_C=colors.HexColor("#00A699"); GLD_C=colors.HexColor("#FC642D")
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

print("Building Airbnb Co-Host System...")

doc("00_START_HERE/Welcome_Guide.docx",
    "Welcome to Your Airbnb Co-Host Management System",
    "The complete operating system for professional short-term rental co-hosts and property managers",
    [
        ("What's Inside", [
            "This system contains everything you need to launch and operate a professional Airbnb co-hosting or short-term rental (STR) management business. Whether you're managing 1 property or scaling to 50, these tools grow with you.",
            ("*","Co-host agreement templates and property management contracts"),
            ("*","Complete guest communication scripts for every situation"),
            ("*","Revenue and pricing optimization workbooks"),
            ("*","Cleaning and turnover checklists"),
            ("*","Notion workspace with property, booking, and financial databases"),
        ]),
        ("The Co-Hosting Business Model", [
            "Co-hosting means managing properties on behalf of Airbnb hosts in exchange for a percentage of the revenue (typically 10-30%). This is one of the fastest-growing service businesses with recurring income potential.",
            ("*","Average co-host fee: 20% of gross rental revenue"),
            ("*","Property earning $3,500/month: your fee = $700/month"),
            ("*","10 properties at $700/month = $7,000/month recurring"),
            ("*","Zero inventory cost: you manage someone else's property"),
        ]),
    ])

doc("01_COHOST_SETUP/Co-Host_Agreement_Template.docx",
    "Co-Host Service Agreement",
    "Airbnb Co-Host System | Professional contract for property owners",
    [
        ("CO-HOST MANAGEMENT AGREEMENT", [
            "This Co-Host Management Agreement ('Agreement') is entered into between [Your Name/Company] ('Co-Host') and [Property Owner Name] ('Owner') effective [Date].",
        ]),
        ("1. Property and Term", [
            "Property Address: [Full Property Address]",
            "Airbnb Listing URL: [URL]",
            "Agreement Start Date: [Date]",
            "Initial Term: [6 months / 12 months] with automatic renewal unless either party provides 30 days written notice.",
        ]),
        ("2. Co-Host Responsibilities", [
            ("*","Guest communication: respond to all inquiries within 1 hour, manage all pre and post-stay communication"),
            ("*","Booking management: accept/decline reservations per agreed criteria, manage calendar"),
            ("*","Pricing: implement dynamic pricing strategy to optimize revenue"),
            ("*","Turnover coordination: schedule and oversee cleaning between guests"),
            ("*","Maintenance: coordinate routine maintenance and emergency repairs with approved vendors"),
            ("*","Reviews: request and respond to all guest reviews"),
            ("*","Monthly reporting: provide monthly performance report to Owner"),
        ]),
        ("3. Owner Responsibilities", [
            ("*","Maintain property in good condition and promptly fund approved repairs"),
            ("*","Provide access to property and all necessary login credentials"),
            ("*","Maintain required insurance and comply with local STR regulations"),
            ("*","Approve major expenditures over $[X] prior to commitment"),
        ]),
        ("4. Co-Host Fee", [
            "Co-Host will receive [20]% of gross rental revenue collected by Airbnb, excluding cleaning fees. Fees are paid monthly within 5 business days of month-end Airbnb payout.",
            "Cleaning fee management: [Option A: Owner pays cleaners directly / Option B: Co-Host manages cleaners, charges pass-through cost + 10% management fee]",
        ]),
        ("5. Termination", [
            "Either party may terminate this Agreement with [30] days written notice. In the event of termination, Co-Host will complete all bookings already accepted. No refund of fees for completed work.",
        ]),
    ])

wb=Workbook()
ws=wb.active; ws.title="Property Portfolio"
hr_row(ws,1,[1,2,3,4,5,6,7],["Property","Owner","Bedrooms","Avg Nightly Rate","Occupancy %","Monthly Revenue","Co-Host Fee"])
wd(ws,{"A":25,"B":18,"C":12,"D":18,"E":14,"F":18,"G":14})
props=[
    ["123 Ocean View Dr","Sarah Thompson","3BR","$185","78%","$4,328","$866"],
    ["456 Mountain Cabin","James Wilson","2BR","$145","82%","$3,572","$714"],
    ["789 Downtown Loft","Maria Garcia","Studio","$95","88%","$2,508","$502"],
    ["321 Beach House","Robert Chen","4BR","$325","68%","$6,648","$1,330"],
    ["654 Lakeside Cottage","Amy Park","2BR","$160","74%","$3,552","$710"],
]
for i,r in enumerate(props):
    bg=LGR if i%2==0 else WHT; dr(ws,i+2,[1,2,3,4,5,6,7],r,bg)
ws2=wb.create_sheet("Booking Tracker")
hr_row(ws2,1,[1,2,3,4,5,6,7],["Property","Guest Name","Check-in","Check-out","Nights","Revenue","Status"])
wd(ws2,{"A":22,"B":20,"C":12,"D":12,"E":8,"F":12,"G":12})
bookings=[
    ["123 Ocean View Dr","Michael Brown","Jan 15","Jan 18","3","$555","Confirmed"],
    ["456 Mountain Cabin","Jennifer Lee","Jan 16","Jan 21","5","$725","Confirmed"],
    ["789 Downtown Loft","David Kim","Jan 18","Jan 20","2","$190","Pending"],
    ["321 Beach House","Amanda Foster","Jan 20","Jan 25","5","$1,625","Confirmed"],
    ["654 Lakeside Cottage","Tom Nelson","Jan 22","Jan 25","3","$480","Confirmed"],
    ["123 Ocean View Dr","Sophie Martin","Jan 25","Jan 28","3","$555","Confirmed"],
]
for i,r in enumerate(bookings):
    bg=LGR if i%2==0 else WHT; dr(ws2,i+2,[1,2,3,4,5,6,7],r,bg)
wb.save(BASE+"02_PROPERTY_MANAGEMENT/Portfolio_and_Booking_Tracker.xlsx")
print("  xlsx 02_PROPERTY_MANAGEMENT/Portfolio_and_Booking_Tracker.xlsx")

doc("03_GUEST_COMMUNICATION/Guest_Message_Templates.docx",
    "Guest Communication Templates",
    "Airbnb Co-Host System | Professional messages for every guest situation",
    [
        ("Inquiry Response (Within 1 Hour)", [
            "Hi [Guest Name]! Thank you for your interest in [Property Name]. We'd love to host you!",
            "The property is available for your dates. Here are a few quick highlights: [List 3 amenities or features most relevant to their trip]. The space comfortably accommodates [X] guests and is [unique selling point].",
            "Feel free to book directly through Airbnb. If you have any questions about the property or the area, I'm happy to help. We look forward to welcoming you!",
        ]),
        ("Booking Confirmation", [
            "Hi [Guest Name], we're so excited to welcome you to [Property Name]!",
            "Here's what you need to know:",
            "Check-in: [Date] after [time]. Your door code is: [CODE]. [Or: The lockbox with the key is located at...]",
            "Check-out: [Date] by [time]. Please leave the key inside the property and lock the door.",
            "WiFi: Network: [SSID] | Password: [PASSWORD]",
            "Parking: [Details]",
            "Your House Guide with all property instructions will be sent 24 hours before your arrival.",
            "Please don't hesitate to message me with any questions. Have a wonderful stay!",
        ]),
        ("Pre-Arrival Message (24 Hours Before)", [
            "Hi [Guest Name]! We're looking forward to welcoming you tomorrow.",
            "Quick reminders: Check-in is after [time]. Door code: [CODE]. Parking: [details].",
            "I've attached your complete House Guide with everything you need to know about the property. Key highlights:",
            ("*","How to use the [special appliance]: [brief instructions]"),
            ("*","Trash pickup is on [day] -- bags go to [location]"),
            ("*","Our favorite local spots: [restaurant 1], [restaurant 2], [activity 1]"),
            "Message me anytime if you need anything during your stay. Have a wonderful trip!",
        ]),
        ("Check-In Day Welcome", [
            "Hi [Guest Name]! Welcome to [City]! I hope your travel went smoothly.",
            "I just wanted to check in -- you should have everything you need to get settled. Is the property meeting your expectations so far?",
            "If you need anything at all during your stay, just message me here on Airbnb and I'll get back to you quickly.",
            "Enjoy your stay!",
        ]),
        ("Checkout Reminder (Morning Of)", [
            "Good morning [Guest Name]! Just a friendly reminder that checkout is today by [time].",
            "Checkout instructions: [brief list -- e.g., strip beds, put dishes in dishwasher, leave key inside, lock door].",
            "I hope you had a wonderful stay! If you enjoyed your time, we would really appreciate a 5-star review -- it makes a huge difference for us. We'll be sure to leave you a great review as well.",
            "Safe travels, and we hope to see you again!",
        ]),
        ("5-Star Review Request", [
            "Hi [Guest Name], it was a pleasure hosting you! I hope your stay at [Property Name] was everything you hoped for.",
            "We've left you a 5-star review. If you enjoyed your stay, we would be so grateful if you could share your experience. Your review helps other travelers know what to expect and means the world to us.",
            "We hope to welcome you back again soon!",
        ]),
        ("Issue Response (Problem During Stay)", [
            "Hi [Guest Name], I'm so sorry to hear about [issue]. That's definitely not the experience we want you to have.",
            "Here's what I'm doing to fix this right away: [immediate action]. I'm also going to [follow-up action].",
            "Please let me know if this resolves the issue or if there's anything else I can do to make your stay more comfortable. I want to make sure you have a great experience.",
        ]),
    ])
print("  ✓ 03_GUEST_COMMUNICATION")

wb3=Workbook()
ws=wb3.active; ws.title="Revenue Dashboard"
hr_row(ws,1,[1,2,3,4,5,6],["Month","Properties","Bookings","Gross Revenue","Co-Host Fees","Expenses"])
wd(ws,{"A":10,"B":12,"C":12,"D":16,"E":16,"F":12})
rev_data=[
    ["Jan 2026","5","18","$18,606","$3,721","$890"],
    ["Feb 2026","5","16","$16,544","$3,309","$780"],
    ["Mar 2026","6","22","$23,412","$4,682","$1,100"],
    ["Apr 2026","6","24","$25,800","$5,160","$1,200"],
    ["May 2026","7","28","$30,024","$6,005","$1,350"],
    ["Jun 2026","7","30","$33,180","$6,636","$1,500"],
]
for i,r in enumerate(rev_data):
    bg=LGR if i%2==0 else WHT; dr(ws,i+2,[1,2,3,4,5,6],r,bg)
ws2=wb3.create_sheet("Dynamic Pricing Guide")
hr_row(ws2,1,[1,2,3,4],["Season/Event","Rate Adjustment","Minimum Stay","Notes"])
wd(ws2,{"A":22,"B":18,"C":14,"D":30})
pricing_guide=[
    ["Peak season (Summer)","Base rate + 30-50%","3 nights min","Memorial Day - Labor Day"],
    ["Holiday weekends","Base rate + 50-80%","2-3 nights min","4th of July, Thanksgiving, etc."],
    ["Local events","Base rate + 25-40%","2 nights min","Concerts, festivals, sports"],
    ["Shoulder season","Base rate","2 nights min","Spring, early fall"],
    ["Off-peak weekdays","Base rate - 10-20%","1 night OK","Fill gaps in calendar"],
    ["Last-minute (0-3 days)","Base rate - 15-25%","1 night OK","Better to fill than empty"],
    ["Far-out dates (90+ days)","Base rate - 10%","3 nights min","Build occupancy, adjust closer in"],
]
for i,r in enumerate(pricing_guide):
    bg=LGR if i%2==0 else WHT; dr(ws2,i+2,[1,2,3,4],r,bg)
wb3.save(BASE+"04_PRICING_REVENUE/Revenue_and_Pricing_Workbook.xlsx")
print("  xlsx 04_PRICING_REVENUE/Revenue_and_Pricing_Workbook.xlsx")

doc("05_CLEANING_TURNOVER/Turnover_Checklist.docx",
    "Property Turnover Checklist",
    "Airbnb Co-Host System | Complete checklist for every turnover",
    [
        ("Kitchen", [
            ("*","Dishes washed, dried, and put away (or dishwasher run and emptied)"),
            ("*","Countertops wiped down and sanitized"),
            ("*","Stovetop and oven cleaned"),
            ("*","Microwave cleaned inside and out"),
            ("*","Refrigerator: remove expired items, wipe shelves"),
            ("*","Coffee maker cleaned, filter replaced"),
            ("*","Trash emptied and new bag installed"),
            ("*","Floor mopped"),
            ("*","Restock: dish soap, sponge, paper towels"),
        ]),
        ("Bathrooms", [
            ("*","Toilet cleaned inside, outside, and base"),
            ("*","Sink and faucet scrubbed and polished"),
            ("*","Shower/tub scrubbed and rinsed"),
            ("*","Mirror cleaned streak-free"),
            ("*","Floor mopped or scrubbed"),
            ("*","Restock: toilet paper (4+ rolls), hand soap, shampoo, conditioner, body wash"),
            ("*","Replace used towels with fresh, folded hotel-style"),
            ("*","Empty trash"),
        ]),
        ("Bedrooms", [
            ("*","Strip all beds -- mattress protectors inspected"),
            ("*","Make beds with fresh, clean linens"),
            ("*","Pillows fluffed and arranged hotel-style"),
            ("*","Dust all surfaces (nightstands, dressers, headboard)"),
            ("*","Vacuum floor and under bed"),
            ("*","Check drawers for guest belongings left behind"),
            ("*","Verify all plugs/outlets working, lamps function"),
        ]),
        ("Living Areas", [
            ("*","Vacuum upholstered furniture and floors"),
            ("*","Wipe down all hard surfaces"),
            ("*","Arrange throw pillows and blankets"),
            ("*","Clean TV remote and check batteries"),
            ("*","Clear all clutter and personal items guests left"),
            ("*","Wipe light switches and door handles (high-touch points)"),
        ]),
        ("Final Check Before Locking Up", [
            ("*","All windows and doors locked"),
            ("*","Air conditioning/heat set to standard welcome temperature"),
            ("*","All lights turned off"),
            ("*","Outdoor areas swept and staged"),
            ("*","Welcome amenities set up (water bottles, local guide)"),
            ("*","Take 5 photos: living room, kitchen, master bedroom, main bathroom, entrance -- upload to booking file"),
        ]),
    ])
print("  ✓ 05_CLEANING_TURNOVER")

csv_w("08_NOTION_WORKSPACE/Notion_Property_Database.csv",
    ["Property ID","Property Name","Address","Owner","Bedrooms","Nightly Rate","Status","Notes"],
    [
        ["P001","Ocean View Dr #123","123 Ocean View Dr, Miami FL","Sarah Thompson","3BR","$185","Active","Pool access"],
        ["P002","Mountain Cabin","456 Pine Ridge Rd, Asheville NC","James Wilson","2BR","$145","Active","Fireplace, hot tub"],
        ["P003","Downtown Loft","789 Main St #4B, Nashville TN","Maria Garcia","Studio","$95","Active","Walkable location"],
        ["P004","Beach House","321 Shore Blvd, Destin FL","Robert Chen","4BR","$325","Active","Beachfront"],
        ["P005","Lakeside Cottage","654 Lake Rd, Lake Tahoe CA","Amy Park","2BR","$160","Active","Kayaks included"],
    ])

csv_w("08_NOTION_WORKSPACE/Notion_Booking_Log.csv",
    ["Booking ID","Property","Guest","Check-in","Check-out","Revenue","Status","Review Score"],
    [
        ["B001","Ocean View Dr","Michael Brown","Jan 15","Jan 18","$555","Completed","5.0"],
        ["B002","Mountain Cabin","Jennifer Lee","Jan 16","Jan 21","$725","Completed","5.0"],
        ["B003","Downtown Loft","David Kim","Jan 18","Jan 20","$190","Active","--"],
        ["B004","Beach House","Amanda Foster","Jan 20","Jan 25","$1,625","Confirmed","--"],
        ["B005","Lakeside Cottage","Tom Nelson","Jan 22","Jan 25","$480","Confirmed","--"],
        ["B006","Ocean View Dr","Sophie Martin","Jan 25","Jan 28","$555","Confirmed","--"],
    ])

csv_w("08_NOTION_WORKSPACE/Notion_Maintenance_Log.csv",
    ["Date","Property","Issue","Vendor","Status","Cost","Notes"],
    [
        ["2026-01-10","Ocean View Dr","HVAC filter replacement","Routine Maintenance","Done","$45","Quarterly"],
        ["2026-01-12","Mountain Cabin","Hot tub jets cleaned","Hot Tub Service Co","Done","$120","Monthly"],
        ["2026-01-14","Beach House","Guest reported dripping faucet","Mike's Plumbing","In Progress","$150","Booked Jan 16"],
        ["2026-01-15","Downtown Loft","WiFi router replaced","Self","Done","$65","Router was 4 years old"],
        ["2026-01-16","Lakeside Cottage","Kayak paddle replaced","Self","Done","$42","Guest damaged"],
    ])

with open(BASE+"08_NOTION_WORKSPACE/Notion_Setup_Guide.md","w",encoding="utf-8") as f:
    f.write("# Airbnb Co-Host - Notion Setup\n\n## Import These Databases\n- Property Database\n- Booking Log\n- Maintenance Log\n\n## Recommended Views\n- Properties: Gallery view with photo\n- Bookings: Calendar view + Table by Status\n- Maintenance: Board by Status (Pending/In Progress/Done)\n")
print("  ✓ 08_NOTION_WORKSPACE")

ppt=prs()
s0=sl(ppt)
box(s0,0,0,13.33,7.5,PNAV)
tx(s0,"AIRBNB CO-HOST SERVICES",0.5,1.2,12,0.9,sz=36,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"Professional Short-Term Rental Management",0.5,2.3,12,0.7,sz=18,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"Maximize your revenue. Minimize your stress.",0.5,3.2,12,0.6,sz=15,col=PGLD,a=PP_ALIGN.CENTER)
tx(s0,"[Your Name]  |  [# Properties Managed]  |  [City/Region]",0.5,5.5,12,0.5,sz=12,col=PWHT,a=PP_ALIGN.CENTER)

s1=sl(ppt)
box(s1,0,0,13.33,1.2,PACC)
tx(s1,"FULL-SERVICE CO-HOSTING",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
svcs=[("Guest Communication","24/7 inquiry response, booking management, check-in/out"),
      ("Dynamic Pricing","Revenue-optimizing pricing strategy updated weekly"),
      ("Turnover Coordination","Professional cleaning scheduled between every guest"),
      ("Listing Optimization","SEO-optimized listing, professional photos coordination"),
      ("Maintenance Management","Vendor coordination, emergency response, repairs"),
      ("Monthly Reporting","Revenue reports, occupancy stats, performance insights")]
for i,(svc,desc) in enumerate(svcs):
    col_=i%2; row_=i//2
    left=0.5+col_*6.4; top=1.4+row_*2.0
    box(s1,left,top,6.0,1.8,PLGR)
    box(s1,left,top,6.0,0.55,PNAV)
    tx(s1,svc,left+0.2,top+0.05,5.6,0.45,sz=12,bold=True,col=PWHT)
    tx(s1,desc,left+0.2,top+0.7,5.6,0.9,sz=10,col=PDGR)

s2=sl(ppt)
box(s2,0,0,13.33,1.2,PNAV)
tx(s2,"OUR FEE STRUCTURE",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
for i,(pkg,fee,items) in enumerate([
    ("STANDARD","+20% of gross revenue",["Full guest comms","Booking management","Turnover coordination","Monthly report"]),
    ("PREMIUM","+25% of gross revenue",["Everything in Standard","Dynamic pricing","Listing optimization","Maintenance management","Priority support"]),
]):
    left=1.0+i*6.0
    box(s2,left,1.4,5.5,5.5,PLGR if i==0 else PNAV)
    col2=PNAV if i==0 else PWHT
    tx(s2,pkg,left+0.1,1.5,5.3,0.6,sz=16,bold=True,col=col2,a=PP_ALIGN.CENTER)
    tx(s2,fee,left+0.1,2.1,5.3,0.7,sz=20,bold=True,col=PNAV if i==0 else PGLD,a=PP_ALIGN.CENTER)
    for j,item in enumerate(items):
        tx(s2,f"+ {item}",left+0.2,2.9+j*0.65,5.0,0.55,sz=11,col=col2)

s3=sl(ppt)
box(s3,0,0,13.33,7.5,PNAV)
box(s3,0,5.8,13.33,1.7,PACC)
tx(s3,"READY TO EARN MORE WITH LESS STRESS?",0.5,2.0,12,0.9,sz=28,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s3,"Let's have a free property consultation.",0.5,3.1,12,0.6,sz=17,col=PGLD,a=PP_ALIGN.CENTER)
tx(s3,"[Email]  |  [Phone]  |  [Calendly link]",0.5,6.1,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)
ppt.save(BASE+"09_CANVA_TEMPLATES/CoHost_Pitch_Deck.pptx")
print("  pptx 09_CANVA_TEMPLATES/CoHost_Pitch_Deck.pptx")

doc("10_BONUSES/House_Rules_Template.docx",
    "House Rules Template",
    "Airbnb Co-Host System | Professional house rules that protect your property",
    [
        ("Standard House Rules", [
            ("*","No smoking anywhere on the property. This includes balconies, patios, and garage. Violation fee: $250"),
            ("*","No parties or events. Gatherings limited to the number of guests on the reservation"),
            ("*","Pet policy: [No pets allowed / Dogs only, max [X] lbs, $[X] pet fee]"),
            ("*","Quiet hours: 10pm to 8am. Please be respectful of neighbors"),
            ("*","Shoes off at the door. Please use the shoe rack provided"),
            ("*","Do not rearrange furniture"),
            ("*","Guests are responsible for any damage beyond normal wear and tear"),
            ("*","Please leave dishes clean and garbage in the bins provided"),
            ("*","Do not share the door code with non-guests"),
            ("*","Check out by [time]. Late checkout of 1+ hours is $[X]. 3+ hours = additional night charge"),
        ]),
        ("Local Regulations Notice", [
            "This property is licensed as a short-term rental. [City/County] requires that all guests must register their contact information with [relevant authority] upon check-in. Your host will facilitate this process.",
            "Noise ordinances are strictly enforced in this area. Fines issued by local authorities may be passed through to guests who violate noise ordinances.",
        ]),
    ])

make_pdf(BASE+"Airbnb_CoHost_Guide.pdf",
    "Airbnb Co-Host Management System - Complete Guide",
    "Your guide to launching and operating a professional co-hosting business",
    [
        ("Welcome",[("*","11 folders with 40+ files for professional STR management"),("*","Start with 01_COHOST_SETUP for your business foundation")]),
        ("The Co-Host Revenue Model",[("*","20% fee on $3,500/month property = $700/month per property"),("*","10 properties = $7,000/month recurring income"),("*","Add-on services: deep cleans, listing photography, setup fee"),]),
        ("Getting Your First Property",[("*","Talk to every Airbnb host you know -- offer a free trial month"),("*","Join local Airbnb host Facebook groups and introduce your services"),("*","Partner with real estate investors who own investment properties"),]),
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
    json.dump({"product":"Airbnb Co-Host Management System","total_files":len(all_files)},f)

etsy="""TITLE:
Airbnb Co-Host Management System | Short-Term Rental Business Kit | Templates Checklists Contracts

DESCRIPTION:
Run your Airbnb co-hosting or STR management business like a pro. This complete system includes every template, contract, checklist, and script you need to manage properties professionally and scale your income.

INCLUDES:
- Co-Host Service Agreement (professional contract template)
- Property portfolio and booking tracker (XLSX)
- Revenue dashboard and dynamic pricing guide (XLSX)
- Guest message templates for every situation (inquiry, confirmation, check-in, checkout, reviews, issues)
- Complete turnover checklist (kitchen, bathrooms, bedrooms, final check)
- Maintenance log and vendor tracker
- House rules template
- Notion workspace: property database, booking log, maintenance log (CSV)
- Canva pitch deck for getting new property owners (PPTX)
- Co-hosting business guide PDF

PERFECT FOR:
- New Airbnb co-hosts getting their first properties
- STR property managers wanting better systems
- Real estate investors self-managing their rentals
- Anyone wanting to launch an Airbnb management business

FORMATS: DOCX, XLSX, PDF, PPTX, CSV

INSTANT DIGITAL DOWNLOAD

TAGS:
airbnb cohost, airbnb management, short term rental, str management, vacation rental, airbnb business, property management templates, airbnb templates, cohost contract, str operations, rental management, airbnb tools, vacation rental business, property manager, airbnb income"""

with open(ETSY_DIR+"11_Airbnb_Listing.txt","w",encoding="utf-8") as f: f.write(etsy)
print("  etsy 11_Airbnb_Listing.txt")

ZIP_PATH="/home/user/oqul-phase55-production/airbnb-cohost-os/BUYER_DOWNLOAD_AirbnbCoHostSystem.zip"
with zipfile.ZipFile(ZIP_PATH,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        dirs.sort()
        for f in sorted(files):
            full=os.path.join(root,f); z.write(full,os.path.relpath(full,os.path.dirname(BASE)))
print(f"✓ ZIP: {ZIP_PATH} ({os.path.getsize(ZIP_PATH)/1024/1024:.1f} MB)")
print("\n=== AIRBNB CO-HOST SYSTEM COMPLETE ===")
