#!/usr/bin/env python3
"""Complete build for Bookkeeper Practice Launch System (folders 04-12 + PDFs + ZIP + Etsy listing)"""
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

BASE = "/home/user/oqul-phase55-production/bookkeeper-launch-system/Ultimate_Bookkeeper_Launch_System/"
ETSY_DIR = "/home/user/oqul-phase55-production/etsy-listings/"
for d in ["04_CLIENT_MANAGEMENT","05_BOOKKEEPING_SYSTEMS","06_TAX_PREP_SUPPORT",
          "07_SOFTWARE_TOOLS","08_BUSINESS_OPERATIONS","09_NOTION_WORKSPACE",
          "10_CANVA_TEMPLATES","11_BONUSES","12_ETSY_RESOURCES"]:
    os.makedirs(BASE+d, exist_ok=True)
os.makedirs(ETSY_DIR, exist_ok=True)

NAV="1B4F72"; ACC="E74C3C"; GLD="F39C12"; GRN="27AE60"; WHT="FFFFFF"; LGR="EBF5FB"
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

def doc(fn, title, sub, secs):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x1B,0x4F,0x72)
    if sub:
        s = d.add_paragraph(sub); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10); s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for sec in secs:
        if isinstance(sec, str): d.add_paragraph(sec); continue
        h, items = sec
        hd = d.add_heading(h, level=1); hd.runs[0].font.color.rgb = RGBColor(0x1B,0x4F,0x72)
        for it in items:
            if isinstance(it, tuple) and it[0]=='*': d.add_paragraph(it[1], style='List Bullet')
            else: d.add_paragraph(str(it))
    d.save(BASE+fn); print(f"  doc {fn}")

PNAV=PRGB(27,79,114); PACC=PRGB(231,76,60); PGLD=PRGB(243,156,18); PWHT=PRGB(255,255,255)
PLGR=PRGB(235,245,251); PDGR=PRGB(44,62,80)
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
    NAV_C=colors.HexColor("#1B4F72"); ACC_C=colors.HexColor("#E74C3C"); GLD_C=colors.HexColor("#F39C12")
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

# ── 04 CLIENT MANAGEMENT ──────────────────────────────────────────────────────
p04="04_CLIENT_MANAGEMENT/"
print("Building 04_CLIENT_MANAGEMENT...")

wb=Workbook()
ws1=wb.active; ws1.title="Client Database"
hr(ws1,1,[1,2,3,4,5,6,7,8],["Client ID","Business Name","Owner Name","Email","Phone","Service Plan","Monthly Fee","Status"])
wd(ws1,{"A":10,"B":25,"C":20,"D":28,"E":16,"F":18,"G":14,"H":12})
clients=[
    ["BK001","Rodriguez Family LLC","Maria Rodriguez","maria@rodriguez-llc.com","(555)201-1001","Full-Service Bookkeeping","$450","Active"],
    ["BK002","Coastal Plumbing Co.","James Chen","jchen@coastalplumbing.com","(555)201-1002","Bookkeeping + Payroll","$650","Active"],
    ["BK003","Sunrise Yoga Studio","Amy Park","amy@sunriseyoga.com","(555)201-1003","Monthly Bookkeeping","$350","Active"],
    ["BK004","Hartwell Construction","Tom Hartwell","tom@hartwellconstruction.com","(555)201-1004","Full-Service + Tax Prep","$950","Active"],
    ["BK005","Blossom Boutique","Sandra Kim","sandra@blossomsf.com","(555)201-1005","Monthly Bookkeeping","$350","Active"],
    ["BK006","TechStart Solutions","David Okonkwo","d.okonkwo@techstart.io","(555)201-1006","Bookkeeping + Payroll","$650","Onboarding"],
    ["BK007","Green Valley Farm","Carlos Reyes","c.reyes@gvfarm.com","(555)201-1007","Quarterly Bookkeeping","$220","Active"],
    ["BK008","Summit Real Estate","Lisa Thornton","l.thornton@summitrealty.com","(555)201-1008","Monthly Bookkeeping","$400","Active"],
]
for i,r in enumerate(clients):
    bg=LGR if i%2==0 else WHT
    dr(ws1,i+2,[1,2,3,4,5,6,7,8],r,bg)

ws2=wb.create_sheet("Contact Log")
hr(ws2,1,[1,2,3,4,5],["Date","Client ID","Contact Method","Summary","Follow-up Required"])
wd(ws2,{"A":12,"B":10,"C":16,"D":40,"E":20})
contacts=[
    ["2026-01-15","BK001","Email","Sent January statement","No"],
    ["2026-01-16","BK002","Phone Call","Discussed payroll schedule change for Q1","Yes - confirm by 01/20"],
    ["2026-01-17","BK003","Zoom","Monthly review call -- all accounts reconciled","No"],
    ["2026-01-18","BK004","Email","Tax prep documents requested","Yes - deadline 02/01"],
    ["2026-01-20","BK005","Email","Sent January statement","No"],
    ["2026-01-21","BK006","Zoom","Onboarding meeting -- access to QuickBooks granted","Yes - send welcome kit"],
]
for i,r in enumerate(contacts):
    bg=LGR if i%2==0 else WHT
    dr(ws2,i+2,[1,2,3,4,5],r,bg)

ws3=wb.create_sheet("Revenue Dashboard")
hr(ws3,1,[1,2,3,4],["Month","Total Revenue","New Clients","Churned Clients"])
wd(ws3,{"A":14,"B":18,"C":14,"D":16})
rev=[["Jan 2026","$3,020","1","0"],["Feb 2026","$3,670","1","0"],["Mar 2026","$3,670","0","0"],
     ["Apr 2026","$4,120","1","0"],["May 2026","$4,570","1","0"],["Jun 2026","$4,570","0","1"]]
for i,r in enumerate(rev):
    bg=LGR if i%2==0 else WHT
    dr(ws3,i+2,[1,2,3,4],r,bg)
wb.save(BASE+p04+"Client_Database_Tracker.xlsx"); print(f"  xlsx {p04}Client_Database_Tracker.xlsx")

doc(p04+"Client_Onboarding_Guide.docx",
    "Client Onboarding Guide",
    "Bookkeeper Launch System | Your Step-by-Step Client Onboarding Process",
    [
        ("Before the First Meeting", [
            ("*","Send welcome email with onboarding questionnaire (template in 03_CONTRACTS_PROPOSALS)"),
            ("*","Request list of bank accounts, credit cards, and loans the client has"),
            ("*","Ask for previous year's tax return and any existing bookkeeping records"),
            ("*","Confirm which accounting software the client is using or wants to use"),
            ("*","Send software invitation (QuickBooks, Wave, FreshBooks, or Xero)"),
        ]),
        ("First Client Meeting (60 Minutes)", [
            "Agenda for your first meeting with a new bookkeeping client:",
            ("*","Minutes 1-10: Introductions. Share your background, your process, your communication style"),
            ("*","Minutes 10-25: Business discovery. Understand the business model, revenue streams, expense categories"),
            ("*","Minutes 25-40: Software walkthrough. Review their current setup, identify clean-up needed"),
            ("*","Minutes 40-55: Process agreement. Explain your workflow, document requirements, monthly routine"),
            ("*","Minutes 55-60: Next steps. Set access credentials, confirm timeline for first deliverable"),
        ]),
        ("First 30 Days: Clean-Up Phase", [
            "Most new clients will have some historical data to clean up. Here's your process:",
            ("*","Week 1: Complete Chart of Accounts review and setup"),
            ("*","Week 2: Import or enter all transactions from the current year"),
            ("*","Week 3: Reconcile all bank and credit card accounts"),
            ("*","Week 4: Generate and review first clean financial statements with client"),
        ]),
        ("Setting Up Ongoing Processes", [
            ("*","Monthly routine: Collect receipts by the 5th, reconcile by the 15th, deliver reports by the 20th"),
            ("*","Payroll clients: Confirm pay schedule, employee count, and payroll software access"),
            ("*","Tax prep clients: Create a year-end document checklist shared in Google Drive or Notion"),
            ("*","Communication: Schedule monthly 20-minute check-in calls for all full-service clients"),
        ]),
        ("Client Success Checklist", [
            ("*","Software access confirmed and tested"),
            ("*","Chart of Accounts set up according to industry best practices"),
            ("*","Historical data entered and reconciled"),
            ("*","First financial statements delivered and reviewed"),
            ("*","Monthly routine agreed upon in writing"),
            ("*","Emergency contact and deadline communication established"),
        ]),
    ])

doc(p04+"Client_Communication_Templates.docx",
    "Client Communication Templates",
    "Bookkeeper Launch System | Professional Templates for Every Client Situation",
    [
        ("Welcome Email (New Client)", [
            "Subject: Welcome to [Your Practice Name] -- Let's Get Started!",
            "Dear [Client Name],",
            "I'm so excited to welcome [Business Name] to [Your Practice Name]. You've made a great decision to outsource your bookkeeping, and I'm committed to making your experience seamless and stress-free.",
            "Here's what happens next:",
            ("*","Step 1: Please complete the attached onboarding questionnaire (takes about 15 minutes)"),
            ("*","Step 2: I'll send you a software invitation to [QuickBooks/Wave/Xero] by [date]"),
            ("*","Step 3: Our first meeting is scheduled for [date/time] via [Zoom/phone]"),
            "In the meantime, please gather: [prior year tax return, list of bank accounts, any existing records]. I'll take it from there.",
            "Questions? Reply to this email or call me at [phone number]. I'm here to help.",
            "Warmly, [Your Name]",
        ]),
        ("Monthly Financial Statement Delivery", [
            "Subject: [Business Name] | [Month] Financial Statements Ready",
            "Hi [Client Name],",
            "Your [Month] financial statements are ready! Here's a quick summary:",
            ("*","Total Revenue: $[X] (up/down X% from last month)"),
            ("*","Total Expenses: $[X]"),
            ("*","Net Income: $[X]"),
            ("*","Cash Balance: $[X] as of [month end date]"),
            "The full reports are attached. Key highlights: [1-2 sentences about anything notable].",
            "Schedule your monthly review call here: [Calendly link]. Our call is a great time to discuss any questions or upcoming financial decisions.",
            "Best, [Your Name]",
        ]),
        ("Late Document Follow-Up", [
            "Subject: Friendly Reminder: [Month] Documents Needed",
            "Hi [Client Name],",
            "Just a friendly reminder that I'm still waiting on the following to complete your [Month] bookkeeping:",
            ("*","[Item 1 -- e.g., Bank statements for [Account Name]]"),
            ("*","[Item 2 -- e.g., Receipts for purchases over $50]"),
            ("*","[Item 3 -- e.g., Payroll records for [pay period]]"),
            "My deadline for receiving these is [date] to deliver your statements on schedule. After that date, there may be a small delay in your report delivery.",
            "If you have any questions or need help accessing these documents, I'm happy to walk you through it!",
            "Thank you, [Your Name]",
        ]),
        ("Price Increase Notice", [
            "Subject: Update to Your Service Rate -- Effective [Date]",
            "Dear [Client Name],",
            "I value our working relationship and want to be transparent about an upcoming change.",
            "Effective [date], your monthly service fee will increase from $[current rate] to $[new rate]. This represents a [X]% increase, my first rate adjustment in [X] years.",
            "This adjustment reflects increased operating costs and ongoing investments in software, continuing education, and the quality of service I provide.",
            "Your current service package -- [describe services] -- will remain exactly the same.",
            "If you have any questions, I'd welcome a call to discuss. Thank you for your continued trust.",
            "Sincerely, [Your Name]",
        ]),
    ])
print("✓ 04_CLIENT_MANAGEMENT done")

# ── 05 BOOKKEEPING SYSTEMS ────────────────────────────────────────────────────
p05="05_BOOKKEEPING_SYSTEMS/"
print("Building 05_BOOKKEEPING_SYSTEMS...")

wb2=Workbook()
ws=wb2.active; ws.title="Month-End Checklist"
hr(ws,1,[1,2,3,4],["Task","Category","Due Date","Status"])
wd(ws,{"A":40,"B":20,"C":14,"D":12})
tasks=[
    ["Import all bank and credit card transactions","Reconciliation","5th of month",""],
    ["Code all uncategorized transactions","Categorization","8th of month",""],
    ["Reconcile all bank accounts to statements","Reconciliation","10th of month",""],
    ["Reconcile all credit card accounts","Reconciliation","10th of month",""],
    ["Review accounts receivable -- flag overdue invoices","A/R Review","12th of month",""],
    ["Review accounts payable -- flag upcoming bills","A/P Review","12th of month",""],
    ["Run and review Profit and Loss statement","Financial Review","15th of month",""],
    ["Run and review Balance Sheet","Financial Review","15th of month",""],
    ["Run and review Cash Flow Statement","Financial Review","15th of month",""],
    ["Review payroll entries for accuracy","Payroll Review","15th of month",""],
    ["Review fixed asset depreciation (quarterly)","Asset Management","15th of month",""],
    ["Prepare and send client financial summary email","Client Delivery","20th of month",""],
    ["Update year-to-date tax estimate tracker","Tax Planning","20th of month",""],
    ["File any monthly sales tax returns","Tax Compliance","Per state due dates",""],
    ["Archive month-end reports to client folder","Documentation","20th of month",""],
]
for i,r in enumerate(tasks):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4],r,bg)

ws2b=wb2.create_sheet("Chart of Accounts")
hr(ws2b,1,[1,2,3,4],["Account Number","Account Name","Account Type","Notes"])
wd(ws2b,{"A":16,"B":30,"C":18,"D":35})
coa=[
    ["1000","Checking Account","Bank","Primary operating account"],
    ["1010","Savings Account","Bank","Reserve / tax savings"],
    ["1100","Accounts Receivable","Accounts Receivable","Outstanding client invoices"],
    ["1200","Undeposited Funds","Other Current Asset","Payments received not yet deposited"],
    ["1500","Equipment","Fixed Asset","Computers, office equipment"],
    ["1510","Accumulated Depreciation","Fixed Asset","Contra account to Equipment"],
    ["2000","Accounts Payable","Accounts Payable","Outstanding vendor bills"],
    ["2100","Credit Card Payable","Credit Card","Business credit cards"],
    ["2200","Sales Tax Payable","Other Current Liability","Collected sales tax owed"],
    ["2500","Owner's Equity","Equity","Owner investment in business"],
    ["3000","Owner's Draw","Equity","Money taken out by owner"],
    ["4000","Service Revenue","Income","Bookkeeping service fees"],
    ["4010","Payroll Service Revenue","Income","Payroll processing fees"],
    ["4020","Tax Prep Revenue","Income","Tax preparation fees"],
    ["5000","Software Subscriptions","Expense","QuickBooks, apps, tools"],
    ["5010","Professional Development","Expense","Training, certifications, education"],
    ["5020","Marketing","Expense","Website, advertising, social media"],
    ["5030","Office Supplies","Expense","Paper, postage, misc supplies"],
    ["5040","Bank Service Charges","Expense","Monthly bank fees"],
    ["5050","Professional Services","Expense","Attorney, CPA, consultants"],
    ["5060","Telephone & Internet","Expense","Business phone and internet"],
    ["5070","Home Office","Expense","Prorated home office expenses"],
    ["5080","Meals & Entertainment","Expense","Client meals, business entertainment"],
    ["5090","Insurance","Expense","E&O, general liability, health insurance"],
]
for i,r in enumerate(coa):
    bg=LGR if i%2==0 else WHT
    dr(ws2b,i+2,[1,2,3,4],r,bg)

ws3b=wb2.create_sheet("Pricing Calculator")
hr(ws3b,1,[1,2],["Service","Details"])
wd(ws3b,{"A":35,"B":35})
ws3b.cell(row=2,column=1,value="Hourly Rate Target").font=bf(True)
ws3b.cell(row=2,column=2,value="$65/hour (adjust to your market)").font=bf(False,10)
ws3b.cell(row=3,column=1,value="Monthly Bookkeeping - Micro (under $100k revenue)").font=bf(False,10)
ws3b.cell(row=3,column=2,value="$250-350/month (4-6 hours)").font=bf(False,10)
ws3b.cell(row=4,column=1,value="Monthly Bookkeeping - Small ($100k-500k revenue)").font=bf(False,10)
ws3b.cell(row=4,column=2,value="$400-600/month (6-9 hours)").font=bf(False,10)
ws3b.cell(row=5,column=1,value="Monthly Bookkeeping - Medium ($500k-2M revenue)").font=bf(False,10)
ws3b.cell(row=5,column=2,value="$700-1,200/month (10-16 hours)").font=bf(False,10)
ws3b.cell(row=6,column=1,value="Payroll Processing Add-on (per employee per month)").font=bf(False,10)
ws3b.cell(row=6,column=2,value="$20-35 per employee").font=bf(False,10)
ws3b.cell(row=7,column=1,value="Tax Return Preparation - Business (Schedule C)").font=bf(False,10)
ws3b.cell(row=7,column=2,value="$400-800").font=bf(False,10)
ws3b.cell(row=8,column=1,value="Tax Return - S-Corp or Partnership (1120-S/1065)").font=bf(False,10)
ws3b.cell(row=8,column=2,value="$800-1,500").font=bf(False,10)
ws3b.cell(row=9,column=1,value="Catch-Up Bookkeeping (per month of backlog)").font=bf(False,10)
ws3b.cell(row=9,column=2,value="$200-450 per month of backlog").font=bf(False,10)
ws3b.cell(row=10,column=1,value="QuickBooks Setup and Training").font=bf(False,10)
ws3b.cell(row=10,column=2,value="$300-600 one-time").font=bf(False,10)
wb2.save(BASE+p05+"Bookkeeping_Systems_Workbook.xlsx"); print(f"  xlsx {p05}Bookkeeping_Systems_Workbook.xlsx")

doc(p05+"Reconciliation_Guide.docx",
    "Bank Reconciliation Guide",
    "Bookkeeper Launch System | Step-by-Step Reconciliation Process",
    [
        ("Why Reconciliation Matters", [
            "Bank reconciliation is the process of matching your client's accounting records to their bank statements. It catches errors, identifies fraud, ensures accuracy, and gives you confidence in the financial statements you produce.",
            "As a professional bookkeeper, your reconciliation process is the foundation of your credibility. Every month, without exception.",
        ]),
        ("The 10-Step Reconciliation Process", [
            ("*","Step 1: Obtain the official bank statement (download from online banking or request PDF from client)"),
            ("*","Step 2: Note the statement ending date and ending balance"),
            ("*","Step 3: In your accounting software, open the bank reconciliation module"),
            ("*","Step 4: Enter the statement ending date and ending balance from the bank statement"),
            ("*","Step 5: Match every cleared transaction in the software to the bank statement"),
            ("*","Step 6: For each unmatched item, determine if it's: (a) a timing difference (in transit), (b) an error in the books, or (c) an unrecorded transaction"),
            ("*","Step 7: Add any missing transactions (bank fees, interest, auto-payments not yet recorded)"),
            ("*","Step 8: Verify that outstanding checks and deposits in transit are legitimate and not old"),
            ("*","Step 9: Confirm the reconciliation difference is zero before completing"),
            ("*","Step 10: Save and print the reconciliation report. Archive in client folder."),
        ]),
        ("Common Reconciliation Issues and Fixes", [
            ("*","Difference is exactly $X: Look for a missing transaction of that amount -- often a bank fee, interest, or NSF charge"),
            ("*","Difference is double: A transaction may have been entered twice in the books"),
            ("*","Difference matches a previous period: An old outstanding item was cleared without being recorded"),
            ("*","Large unexplained difference: Check for journal entries that may have inadvertently affected the bank account"),
            ("*","Bank statement doesn't match software opening balance: Run a previous period reconciliation to find where the discrepancy started"),
        ]),
        ("Credit Card Reconciliation", [
            "Credit card reconciliation follows the same process but uses the credit card statement instead of the bank statement.",
            ("*","Reconcile every business credit card, every month -- even if used infrequently"),
            ("*","Confirm that the credit card liability balance matches the outstanding balance on the statement"),
            ("*","Code all credit card transactions before reconciling to avoid reclassification after the fact"),
            ("*","Flag any personal purchases on business credit cards and discuss with client (treat as owner's draw or request reimbursement)"),
        ]),
    ])

doc(p05+"Financial_Statements_Guide.docx",
    "Financial Statements Guide",
    "Bookkeeper Launch System | How to Prepare and Present Financial Reports",
    [
        ("The Three Core Financial Statements", [
            "Every bookkeeper should understand and be able to explain three fundamental financial statements to their clients. These statements tell the complete financial story of the business.",
        ]),
        ("Profit & Loss Statement (Income Statement)", [
            "The P&L shows revenue and expenses over a time period (month, quarter, or year). It tells you whether the business made or lost money.",
            ("*","Revenue section: All income sources. For most small businesses, this is service revenue or product sales"),
            ("*","Cost of Goods Sold (COGS): Direct costs of delivering products or services. For service businesses, this is often minimal or zero"),
            ("*","Gross Profit: Revenue minus COGS. The money left before overhead expenses"),
            ("*","Operating Expenses: Overhead costs -- rent, utilities, marketing, salaries, software"),
            ("*","Net Income: The bottom line. Revenue minus all expenses. Positive = profit. Negative = loss"),
            "When presenting to clients: Lead with Net Income trend. Then explain what drove changes (revenue up? expenses up?). Give a benchmark (what's typical for this industry).",
        ]),
        ("Balance Sheet", [
            "The Balance Sheet is a snapshot of what the business owns (assets), owes (liabilities), and the owner's equity on a specific date.",
            ("*","Assets: Cash, accounts receivable, equipment, inventory"),
            ("*","Liabilities: Accounts payable, credit cards, loans, sales tax owed"),
            ("*","Owner's Equity: What would be left if all liabilities were paid. Retained earnings + owner investments - owner draws"),
            ("*","Key equation: Assets = Liabilities + Equity (must always balance)"),
            "Watch for: declining cash, growing A/R (clients not paying), debt growing faster than assets.",
        ]),
        ("Cash Flow Statement", [
            "Cash flow shows where money actually came from and went during the period. Profitable businesses can still run out of cash.",
            ("*","Operating Activities: Cash generated by the core business operations"),
            ("*","Investing Activities: Cash used for or received from assets (buying equipment, selling property)"),
            ("*","Financing Activities: Cash from or to loans, owner investments, or owner draws"),
            "Client education tip: 'Your P&L shows profit, but your Cash Flow shows reality. A business can be profitable on paper and still fail if cash timing is poor.'",
        ]),
    ])
print("✓ 05_BOOKKEEPING_SYSTEMS done")

# ── 06 TAX PREP SUPPORT ───────────────────────────────────────────────────────
p06="06_TAX_PREP_SUPPORT/"
print("Building 06_TAX_PREP_SUPPORT...")

doc(p06+"Tax_Prep_Document_Checklist.docx",
    "Tax Prep Document Checklist",
    "Bookkeeper Launch System | Year-End Tax Preparation Document Request",
    [
        ("Income Documents", [
            ("*","All 1099-NEC forms received (from clients/customers who paid $600+)"),
            ("*","All 1099-K forms (from payment processors like PayPal, Stripe, Square)"),
            ("*","All 1099-MISC forms"),
            ("*","Total cash income not captured in 1099s (if applicable)"),
            ("*","Any other income sources: rental income, interest, royalties"),
        ]),
        ("Expense Documents", [
            ("*","Bank statements (all 12 months for all business accounts)"),
            ("*","Credit card statements (all 12 months for all business cards)"),
            ("*","Receipts for cash purchases over $75"),
            ("*","Vehicle mileage log (if deducting vehicle use)"),
            ("*","Home office measurements (square footage of office vs. total home)"),
            ("*","Health insurance premiums paid (for self-employed deduction)"),
            ("*","Retirement contributions (SEP-IRA, Solo 401k, SIMPLE IRA)"),
            ("*","Business insurance premiums"),
            ("*","Professional development, education, and training receipts"),
        ]),
        ("Payroll Documents (if applicable)", [
            ("*","Annual payroll summary from payroll provider"),
            ("*","W-2 forms filed with employees"),
            ("*","Copies of all quarterly 941 payroll tax returns"),
            ("*","State unemployment tax returns"),
        ]),
        ("Asset and Loan Information", [
            ("*","Purchases of equipment over $2,500 (cost and date purchased)"),
            ("*","Sales of any business assets"),
            ("*","Year-end loan balances and annual interest statements (1098)"),
            ("*","Lease agreements for equipment or vehicles"),
        ]),
        ("Prior Year Information", [
            ("*","Prior year tax return (for reference)"),
            ("*","Prior year depreciation schedule"),
            ("*","Any carryforward items (NOL, capital loss, etc.)"),
        ]),
    ])

wb3=Workbook()
ws=wb3.active; ws.title="Quarterly Tax Tracker"
hr(ws,1,[1,2,3,4,5,6],["Quarter","Estimated Revenue","Estimated Profit","Estimated Tax (25%)","Payment Due Date","Payment Made"])
wd(ws,{"A":12,"B":20,"C":18,"D":20,"E":18,"F":15})
qtax=[
    ["Q1 2026","$12,500","$7,200","$1,800","April 15, 2026",""],
    ["Q2 2026","$13,800","$8,100","$2,025","June 15, 2026",""],
    ["Q3 2026","$14,200","$8,400","$2,100","September 15, 2026",""],
    ["Q4 2026","$15,500","$9,200","$2,300","January 15, 2027",""],
]
for i,r in enumerate(qtax):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5,6],r,bg)
ws2t=wb3.create_sheet("Deduction Tracker")
hr(ws2t,1,[1,2,3,4],["Category","YTD Total","Notes","% of Revenue"])
wd(ws2t,{"A":30,"B":15,"C":35,"D":15})
deds=[
    ["Software & Subscriptions","$1,840","QuickBooks, Microsoft 365, Zoom","4.8%"],
    ["Professional Development","$620","CPE courses, webinars, books","1.6%"],
    ["Marketing & Advertising","$1,200","Website, social media ads","3.1%"],
    ["Office Supplies","$380","Paper, printer ink, misc","1.0%"],
    ["Phone & Internet","$1,440","Business portion of phone/internet","3.8%"],
    ["Home Office Deduction","$2,160","Based on 15% of home for office use","5.7%"],
    ["Professional Services","$800","Attorney consultation","2.1%"],
    ["Insurance","$1,800","E&O and general liability","4.7%"],
    ["Bank Fees","$180","Monthly service charges","0.5%"],
    ["Meals & Entertainment","$420","Client meals (50% deductible)","1.1%"],
]
for i,r in enumerate(deds):
    bg=LGR if i%2==0 else WHT
    dr(ws2t,i+2,[1,2,3,4],r,bg)
wb3.save(BASE+p06+"Tax_Planning_Workbook.xlsx"); print(f"  xlsx {p06}Tax_Planning_Workbook.xlsx")

doc(p06+"Tax_Basics_Guide.docx",
    "Small Business Tax Basics Guide",
    "Bookkeeper Launch System | What Every Bookkeeper and Client Needs to Know",
    [
        ("Entity Types and Tax Treatment", [
            ("*","Sole Proprietor: Files Schedule C with personal 1040. Simple but no liability protection"),
            ("*","Single-Member LLC: Same tax treatment as sole prop by default. Can elect S-Corp treatment"),
            ("*","S-Corporation: Files Form 1120-S. Owners take reasonable salary + distributions. Can save on self-employment tax"),
            ("*","Partnership/Multi-Member LLC: Files Form 1065, issues K-1s to partners"),
            ("*","C-Corporation: Files Form 1120. Subject to double taxation. Rarely chosen for small businesses"),
        ]),
        ("Self-Employment Tax", [
            "Self-employed individuals pay 15.3% self-employment tax on net business income (up to Social Security wage base). This covers both the employee and employer portions of Social Security and Medicare.",
            ("*","On $100,000 net income: self-employment tax is approximately $14,130"),
            ("*","S-Corp election strategy: take $60,000 salary, $40,000 distribution. SE tax only applies to salary"),
            ("*","Estimated taxes: self-employed individuals must make quarterly estimated tax payments"),
        ]),
        ("Key Deductions for Small Business Owners", [
            ("*","Home office deduction: simplified method ($5/sq ft up to 300 sq ft) or actual expense method"),
            ("*","Vehicle deduction: standard mileage rate (67 cents/mile in 2024) or actual expenses"),
            ("*","Self-employed health insurance: 100% deductible above the line"),
            ("*","Retirement contributions: SEP-IRA allows up to 25% of net earnings, max $69,000 (2024)"),
            ("*","Section 179: Deduct cost of equipment in year of purchase (up to $1.16M in 2023)"),
            ("*","Qualified Business Income (QBI) Deduction: Up to 20% of net business income for pass-through entities"),
        ]),
        ("Bookkeeper's Role in Tax Season", [
            "Important note: As a bookkeeper (not a CPA), your role is to prepare clean, accurate financial records. Tax ADVICE and tax FILING are services that require a CPA or Enrolled Agent license in most states.",
            ("*","Provide: Clean P&L and Balance Sheet, bank reconciliations, expense categorization, 1099 tracking"),
            ("*","Refer out: Tax strategy advice, tax return preparation, IRS representation"),
            ("*","Build referral relationships with 2-3 CPAs in your area. You refer clients to them; they refer clients to you"),
        ]),
    ])
print("✓ 06_TAX_PREP_SUPPORT done")

# ── 07 SOFTWARE TOOLS ─────────────────────────────────────────────────────────
p07="07_SOFTWARE_TOOLS/"
print("Building 07_SOFTWARE_TOOLS...")

doc(p07+"Software_Comparison_Guide.docx",
    "Bookkeeping Software Comparison Guide",
    "Bookkeeper Launch System | Choosing the Right Tools for You and Your Clients",
    [
        ("QuickBooks Online (QBO)", [
            ("*","Best for: Most small to medium businesses, especially those with employees"),
            ("*","Pricing: $30-200/month (Simple Start, Essentials, Plus, Advanced)"),
            ("*","Strengths: Industry standard, most integrations, payroll built-in, excellent reporting"),
            ("*","Weaknesses: Can be expensive, interface can be overwhelming for non-accountants"),
            ("*","Bookkeeper tip: Get QuickBooks Online ProAdvisor certification (free). It's the most recognized credential in the industry and opens the door to QBO's accountant directory"),
        ]),
        ("Xero", [
            ("*","Best for: Businesses with international operations, tech-savvy clients"),
            ("*","Pricing: $13-70/month"),
            ("*","Strengths: Beautiful interface, unlimited users at no extra cost, strong bank feeds"),
            ("*","Weaknesses: Payroll is limited, customer support can be slow"),
            ("*","Bookkeeper tip: Xero partner certification is free and positions you well in the ecosystem"),
        ]),
        ("Wave (Free)", [
            ("*","Best for: Sole proprietors and micro-businesses with simple financials"),
            ("*","Pricing: Free (pay for payroll and payment processing)"),
            ("*","Strengths: Free forever, easy to use, good invoicing"),
            ("*","Weaknesses: Limited integrations, no inventory, less robust reporting"),
            ("*","Bookkeeper tip: Great starter option for your very small clients. Positions you to upsell QuickBooks as they grow"),
        ]),
        ("FreshBooks", [
            ("*","Best for: Freelancers and service businesses that prioritize invoicing"),
            ("*","Pricing: $17-55/month"),
            ("*","Strengths: Exceptional invoicing and time tracking, easy to use"),
            ("*","Weaknesses: Not true double-entry bookkeeping, limited for complex businesses"),
        ]),
        ("Recommended Tech Stack for Your Bookkeeping Practice", [
            ("*","Accounting: QuickBooks Online (primary) + Wave for micro clients"),
            ("*","Document collection: Hubdoc or Dext for receipt capture and bank statement import"),
            ("*","Communication: Gmail or Outlook, Calendly for scheduling"),
            ("*","File storage: Google Drive or Dropbox (organized by client)"),
            ("*","E-signature: DocuSign or HelloSign for contracts"),
            ("*","Invoicing: QuickBooks or Wave invoice features (avoid separate invoicing software)"),
            ("*","Password management: LastPass or 1Password (essential for managing client software access)"),
        ]),
    ])

doc(p07+"QuickBooks_Setup_Guide.docx",
    "QuickBooks Online Setup Guide",
    "Bookkeeper Launch System | Setting Up a New Client in QuickBooks Online",
    [
        ("Creating a New QBO Company", [
            ("*","Sign in to QuickBooks Accountant and select 'Add Client'"),
            ("*","Choose the correct subscription level based on client needs (Simple Start, Essentials, or Plus)"),
            ("*","Set the fiscal year start (most small businesses use January 1)"),
            ("*","Select the industry from the dropdown -- this pre-populates a starter Chart of Accounts"),
            ("*","Add the business contact info, EIN, and business type"),
        ]),
        ("Chart of Accounts Setup", [
            ("*","Go to Accounting > Chart of Accounts"),
            ("*","Review and edit the auto-populated accounts to match the client's business"),
            ("*","Add any missing accounts from the Chart of Accounts template in 05_BOOKKEEPING_SYSTEMS"),
            ("*","Delete or deactivate accounts that don't apply"),
            ("*","Set up subaccounts where needed (e.g., Revenue > Service Revenue, Revenue > Product Revenue)"),
        ]),
        ("Bank and Credit Card Connections", [
            ("*","Go to Banking > Bank Accounts"),
            ("*","Click 'Link Account' and search for the client's bank"),
            ("*","Connect using the client's online banking credentials (or have them connect while you watch)"),
            ("*","Set the start date to January 1 of the current year (or earlier if doing catch-up)"),
            ("*","Repeat for all credit cards"),
            ("*","Allow QBO to import all transactions before starting categorization"),
        ]),
        ("Payroll Setup (If Applicable)", [
            ("*","Go to Payroll > Get Started"),
            ("*","Enter all employee information: name, SSN, W-4 information, pay rate"),
            ("*","Confirm pay schedule (weekly, biweekly, semi-monthly, monthly)"),
            ("*","Set up direct deposit with employee's bank account information"),
            ("*","Enter year-to-date payroll history if setting up mid-year"),
            ("*","Run a test payroll calculation before the first live run"),
        ]),
    ])
print("✓ 07_SOFTWARE_TOOLS done")

# ── 08 BUSINESS OPERATIONS ────────────────────────────────────────────────────
p08="08_BUSINESS_OPERATIONS/"
print("Building 08_BUSINESS_OPERATIONS...")

wb4=Workbook()
ws=wb4.active; ws.title="Annual Revenue Plan"
hr(ws,1,[1,2,3,4,5],["Month","Target Clients","Target Revenue","Actual Revenue","Variance"])
wd(ws,{"A":12,"B":16,"C":18,"D":18,"E":12})
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
targets=[3500,3500,4000,4200,4500,4500,5000,5200,5500,5500,6000,6500]
for i,(m,t) in enumerate(zip(months,targets)):
    bg=LGR if i%2==0 else WHT
    dr(ws,i+2,[1,2,3,4,5],[f"{m} 2026",str(i//2+4),f"${t:,}","",""],bg)
ws2b=wb4.create_sheet("KPI Dashboard")
hr(ws2b,1,[1,2,3],["KPI","Target","Current"])
wd(ws2b,{"A":30,"B":18,"C":18})
kpis=[
    ["Monthly Recurring Revenue (MRR)","$5,000","$4,570"],
    ["Total Active Clients","10","8"],
    ["Average Revenue Per Client","$500","$571"],
    ["Client Retention Rate","95%","100%"],
    ["Monthly Hours Worked","80","75"],
    ["Effective Hourly Rate","$62","$61"],
    ["New Clients This Month","1","1"],
    ["Churn This Month","0","0"],
    ["Overdue A/R Balance","$0","$0"],
    ["Net Profit Margin","65%","68%"],
]
for i,r in enumerate(kpis):
    bg=LGR if i%2==0 else WHT
    dr(ws2b,i+2,[1,2,3],r,bg)
wb4.save(BASE+p08+"Business_Planning_Workbook.xlsx"); print(f"  xlsx {p08}Business_Planning_Workbook.xlsx")

doc(p08+"Marketing_Guide.docx",
    "Marketing Your Bookkeeping Practice",
    "Bookkeeper Launch System | How to Get Clients Without Cold Calling",
    [
        ("The Bookkeeper Marketing Funnel", [
            "Unlike SMMA or other service businesses, bookkeeping clients are NOT found on social media. They are found through trust, referrals, and professional networks. Your marketing strategy should reflect this.",
            ("*","Top of funnel: Visibility (local networking, LinkedIn, niche communities)"),
            ("*","Middle of funnel: Credibility (testimonials, case studies, credentials displayed)"),
            ("*","Bottom of funnel: Conversion (discovery calls, proposal, close)"),
        ]),
        ("Where Bookkeeping Clients Come From", [
            ("*","CPA and accountant referrals (best source): CPAs often can't do bookkeeping for every client. Build 3-5 CPA referral partners"),
            ("*","Business Facebook Groups: Join local business owner groups and add value before promoting"),
            ("*","Chamber of Commerce: Attend monthly mixers. Bookkeepers who attend consistently get referrals"),
            ("*","BNI (Business Network International): Paid networking group with one professional per category. Worth evaluating"),
            ("*","LinkedIn: Post 2-3 times per week about bookkeeping tips for small business owners"),
            ("*","Alignable: Free local business network. Many small business owners are on it"),
            ("*","Google My Business: A free listing with reviews is one of the most powerful local marketing tools available"),
        ]),
        ("Your Niche Strategy", [
            "Bookkeepers who specialize in an industry earn 30-50% more per client and get more referrals because clients feel understood.",
            ("*","Top bookkeeping niches: restaurants and food service, real estate investors, medical/dental practices, e-commerce, contractors and trades"),
            ("*","To choose your niche: what businesses do you understand? What's your professional background? What industries are underserved in your market?"),
            ("*","Niche marketing message example: 'I specialize in bookkeeping for real estate investors. I understand rental income, depreciation, 1031 exchanges, and how to keep your portfolio organized for tax season.'"),
        ]),
        ("Content Ideas for Bookkeepers", [
            ("*","'3 signs your bookkeeping is a mess' (list post, gets shared)"),
            ("*","'How much should small business bookkeeping cost?' (great for SEO)"),
            ("*","'Common tax deductions small business owners miss' (evergreen content)"),
            ("*","'QuickBooks tip of the week' (positions you as the expert)"),
            ("*","'Client success story: how we cleaned up 2 years of messy books in 3 weeks'"),
            ("*","'What's the difference between a bookkeeper and a CPA?' (answers a common question)"),
        ]),
    ])
print("✓ 08_BUSINESS_OPERATIONS done")

# ── 09 NOTION WORKSPACE ───────────────────────────────────────────────────────
p09="09_NOTION_WORKSPACE/"
print("Building 09_NOTION_WORKSPACE...")

csv_w(p09+"Notion_Client_Roster.csv",
    ["Client ID","Business Name","Industry","Service Plan","Monthly Fee","Start Date","Status","Notes"],
    [
        ["BK001","Rodriguez Family LLC","Professional Services","Full-Service","$450","2025-03-01","Active",""],
        ["BK002","Coastal Plumbing Co.","Trades","Bookkeeping + Payroll","$650","2025-05-15","Active",""],
        ["BK003","Sunrise Yoga Studio","Wellness","Monthly Bookkeeping","$350","2025-07-01","Active",""],
        ["BK004","Hartwell Construction","Construction","Full-Service + Tax","$950","2025-01-15","Active","Priority client"],
        ["BK005","Blossom Boutique","Retail","Monthly Bookkeeping","$350","2025-09-01","Active",""],
        ["BK006","TechStart Solutions","Technology","Bookkeeping + Payroll","$650","2026-01-10","Onboarding",""],
        ["BK007","Green Valley Farm","Agriculture","Quarterly Bookkeeping","$220","2025-04-01","Active","Seasonal adjustments"],
        ["BK008","Summit Real Estate","Real Estate","Monthly Bookkeeping","$400","2025-08-20","Active",""],
    ])

csv_w(p09+"Notion_Monthly_Task_Board.csv",
    ["Task","Client","Month","Due Date","Status","Priority","Notes"],
    [
        ["Reconcile bank accounts","Coastal Plumbing Co.","June 2026","Jun 10","In Progress","High",""],
        ["Deliver monthly statements","Rodriguez Family LLC","June 2026","Jun 20","Not Started","High",""],
        ["Run payroll","TechStart Solutions","June 2026","Jun 28","Not Started","High","Bi-weekly"],
        ["Quarterly tax estimate","Hartwell Construction","Q2 2026","Jun 15","Not Started","Medium",""],
        ["Send document request","Hartwell Construction","Tax Prep 2026","Mar 1","Complete","High",""],
        ["QuickBooks setup","TechStart Solutions","Jan 2026","Jan 20","Complete","High",""],
    ])

csv_w(p09+"Notion_Expense_Log.csv",
    ["Date","Vendor","Category","Amount","Payment Method","Tax Deductible","Notes"],
    [
        ["2026-01-02","QuickBooks","Software","$80.00","Credit Card","Yes","Monthly subscription - 8 clients"],
        ["2026-01-05","Dext","Software","$44.00","Credit Card","Yes","Receipt capture software"],
        ["2026-01-10","GoDaddy","Website","$12.99","Credit Card","Yes","Domain renewal"],
        ["2026-01-15","Canva Pro","Software","$13.99","Credit Card","Yes","Marketing design tool"],
        ["2026-02-01","Zoom","Software","$14.99","Credit Card","Yes","Video calls with clients"],
        ["2026-02-10","Amazon","Office Supplies","$42.87","Credit Card","Yes","Printer ink and paper"],
        ["2026-02-20","Local CPA Lunch","Meals","$48.50","Credit Card","50% Deductible","Referral partner meeting"],
        ["2026-03-01","Continuing Ed Course","Education","$299.00","Credit Card","Yes","Advanced bookkeeping course"],
    ])

csv_w(p09+"Notion_Lead_Pipeline.csv",
    ["Lead Name","Business","Industry","Source","Status","Est. Value","Next Action","Date"],
    [
        ["Sandra Nguyen","Nguyen Bakery","Food Service","Facebook Group","Proposal Sent","$380/mo","Follow up","2026-02-01"],
        ["Michael Torres","Torres Landscaping","Trades","CPA Referral","Discovery Call Booked","$450/mo","Prep for call","2026-02-05"],
        ["Amy Johnson","Johnson Photography","Creative","LinkedIn","Initial Contact","$300/mo","Send intro email","2026-02-10"],
        ["Robert Kim","Kim Auto Repair","Auto","Chamber Referral","Qualified","$500/mo","Send proposal","2026-02-08"],
        ["Lisa Chang","Serenity Spa","Wellness","Google","Contacted","$350/mo","Send follow up","2026-02-15"],
    ])

csv_w(p09+"Notion_Invoice_Log.csv",
    ["Invoice #","Client","Issue Date","Due Date","Amount","Status","Payment Date","Method"],
    [
        ["INV-2026-001","Rodriguez Family LLC","Jan 1, 2026","Jan 15, 2026","$450","Paid","Jan 12, 2026","ACH"],
        ["INV-2026-002","Coastal Plumbing Co.","Jan 1, 2026","Jan 15, 2026","$650","Paid","Jan 14, 2026","Check"],
        ["INV-2026-003","Sunrise Yoga Studio","Jan 1, 2026","Jan 15, 2026","$350","Paid","Jan 10, 2026","ACH"],
        ["INV-2026-004","Hartwell Construction","Jan 1, 2026","Jan 15, 2026","$950","Paid","Jan 8, 2026","ACH"],
        ["INV-2026-005","Blossom Boutique","Jan 1, 2026","Jan 15, 2026","$350","Paid","Jan 16, 2026","Credit Card"],
        ["INV-2026-006","TechStart Solutions","Jan 1, 2026","Jan 15, 2026","$650","Outstanding","",""],
    ])

with open(BASE+p09+"Notion_Setup_Guide.md","w",encoding="utf-8") as f:
    f.write("""# Bookkeeper Practice Notion Workspace - Setup Guide

## Step 1: Create Your Workspace
1. Open Notion and click **+ New page** in the sidebar
2. Name it: **Bookkeeping Practice OS**
3. Set the icon to a calculator or money emoji

## Step 2: Import Your Databases
For each CSV file in this folder:
1. Create a new page inside your workspace
2. Click the `/` command and choose **Table - Full page**
3. Click the **...** menu > **Import** > **CSV**
4. Select the file and map columns

## Databases to Import:
- `Notion_Client_Roster.csv` → Your master client list
- `Notion_Monthly_Task_Board.csv` → Monthly work tracker
- `Notion_Expense_Log.csv` → Business expense tracking
- `Notion_Lead_Pipeline.csv` → Prospect tracking
- `Notion_Invoice_Log.csv` → Invoice and payment tracking

## Step 3: Link Databases
- Add a **Relation** property to Task Board linking to Client Roster
- Add a **Relation** property to Invoice Log linking to Client Roster
- This creates a connected workspace where all data ties together

## Step 4: Add Views
For the Task Board, add these views:
- **Board view** (Kanban): Group by Status
- **Calendar view**: Group by Due Date
- **Filter by Month**: For monthly planning
""")
print(f"  md {p09}Notion_Setup_Guide.md")
print("✓ 09_NOTION_WORKSPACE done")

# ── 10 CANVA TEMPLATES ────────────────────────────────────────────────────────
p10="10_CANVA_TEMPLATES/"
print("Building 10_CANVA_TEMPLATES...")

# Services Overview Deck
ppt=prs()
s0=sl(ppt)
box(s0,0,0,13.33,7.5,PNAV)
box(s0,0,5.5,13.33,2.0,PACC)
tx(s0,"BOOKKEEPING SERVICES",0.5,0.8,12,1.0,sz=36,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"Professional. Accurate. Reliable.",0.5,2.0,12,0.7,sz=20,col=PGLD,a=PP_ALIGN.CENTER)
tx(s0,"[Your Name, CB/QuickBooks ProAdvisor]",0.5,2.9,12,0.6,sz=14,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"[Your Business Name]  |  [City, State]",0.5,6.1,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)

s1=sl(ppt)
box(s1,0,0,13.33,1.2,PACC)
tx(s1,"WHAT WE OFFER",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
services=[
    ("Monthly Bookkeeping","Transaction coding, reconciliation, monthly financial statements"),
    ("Payroll Processing","Setup, processing, tax deposits, W-2 preparation"),
    ("Tax Preparation Support","Year-end cleanup, document prep, CPA coordination"),
    ("QuickBooks Setup & Training","Initial setup, Chart of Accounts, team training"),
    ("Catch-Up Bookkeeping","Getting behind? We clean up months or years of backlog"),
    ("CFO Advisory","Monthly financial reviews, cash flow forecasting, KPI tracking"),
]
for i,(svc,desc) in enumerate(services):
    col_=i%2; row_=i//2
    left=0.5+col_*6.4; top=1.4+row_*2.0
    box(s1,left,top,6.0,1.8,PLGR)
    tx(s1,svc,left+0.2,top+0.1,5.6,0.6,sz=12,bold=True,col=PNAV)
    tx(s1,desc,left+0.2,top+0.7,5.6,0.9,sz=10,col=PDGR)

s2=sl(ppt)
box(s2,0,0,13.33,1.2,PNAV)
tx(s2,"OUR PACKAGES & PRICING",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
pkgs=[
    ("ESSENTIALS","$250-350/mo",["Monthly transaction coding","Bank reconciliation","Monthly P&L and Balance Sheet","Email support"]),
    ("PROFESSIONAL","$400-600/mo",["Everything in Essentials","Accounts payable tracking","Payroll add-on available","Monthly video call","Year-end tax prep coordination"]),
    ("PREMIUM","$700-1,200/mo",["Everything in Professional","Payroll included","Quarterly tax estimates","CFO advisory calls","Priority response SLA"]),
]
for i,(pkg,price,feats) in enumerate(pkgs):
    left=0.5+i*4.2
    box(s2,left,1.4,3.9,5.5,PLGR if i!=1 else PNAV)
    col2=PNAV if i!=1 else PWHT
    tx(s2,pkg,left+0.1,1.5,3.7,0.55,sz=13,bold=True,col=col2,a=PP_ALIGN.CENTER)
    tx(s2,price,left+0.1,2.05,3.7,0.65,sz=19,bold=True,col=PACC if i!=1 else PGLD,a=PP_ALIGN.CENTER)
    for j,feat in enumerate(feats):
        tx(s2,f"+ {feat}",left+0.2,2.8+j*0.65,3.5,0.55,sz=10,col=col2)

s3=sl(ppt)
box(s3,0,0,13.33,1.2,PACC)
tx(s3,"WHY CLIENTS CHOOSE US",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
for i,(num,label) in enumerate([("[X]+","Clients Served"),("[X] Years","In Practice"),("100%","Accuracy Guarantee"),("QuickBooks","ProAdvisor Certified")]):
    left=0.5+i*3.1
    box(s3,left,1.4,2.8,2.2,PNAV)
    tx(s3,num,left+0.1,1.5,2.6,1.1,sz=22,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
    tx(s3,label,left+0.1,2.6,2.6,0.8,sz=10,col=PWHT,a=PP_ALIGN.CENTER)
for i,r in enumerate(["You focus on running your business. We handle the numbers.","Never wonder if your books are right again.","Monthly financial statements delivered by the 20th, every month.","Year-round support from a dedicated bookkeeper who knows your business."]):
    tx(s3,f"  {r}",0.5,3.9+i*0.65,12,0.55,sz=11,col=PDGR)

s4=sl(ppt)
box(s4,0,0,13.33,7.5,PNAV)
box(s4,0,5.8,13.33,1.7,PACC)
tx(s4,"READY TO GET YOUR BOOKS IN ORDER?",0.5,1.5,12,1.0,sz=28,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s4,"Book a free 30-minute consultation today.",0.5,2.7,12,0.6,sz=17,col=PGLD,a=PP_ALIGN.CENTER)
tx(s4,"[Calendly link or phone number]",0.5,3.5,12,0.6,sz=15,col=PWHT,a=PP_ALIGN.CENTER)
tx(s4,"[Your Name]  |  [Email]  |  [Website]",0.5,6.1,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)

ppt.save(BASE+p10+"Services_Overview_Deck.pptx")
print(f"  pptx {p10}Services_Overview_Deck.pptx")

# Client Welcome Deck
ppt2=prs()
w0=sl(ppt2)
box(w0,0,0,13.33,7.5,PNAV)
box(w0,0,0,4.5,7.5,PACC)
tx(w0,"WELCOME",0.5,1.0,3.5,1.0,sz=32,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(w0,"TO YOUR NEW BOOKKEEPING PRACTICE",0.5,2.2,3.5,1.5,sz=16,col=PWHT,a=PP_ALIGN.CENTER)
tx(w0,"[CLIENT BUSINESS NAME]",5.0,1.5,8.0,0.9,sz=28,bold=True,col=PWHT)
tx(w0,"You've made a smart decision.",5.0,2.6,8.0,0.7,sz=16,col=PGLD)
tx(w0,"Welcome to stress-free bookkeeping. Here's everything you need to know about what happens next.",5.0,3.5,7.5,1.5,sz=13,col=PWHT)

w1=sl(ppt2)
box(w1,0,0,13.33,1.2,PACC)
tx(w1,"YOUR FIRST 30 DAYS",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
steps=[("Week 1","Onboarding & Access","We get access to your software and bank accounts, review your existing records, and set up your Chart of Accounts"),
       ("Week 2","Historical Clean-Up","We enter and categorize any backlogged transactions to start from a clean foundation"),
       ("Week 3","First Reconciliation","All accounts reconciled for accuracy. You'll see your books balanced for the first time"),
       ("Week 4","First Report Delivery","You receive your first clean financial statements with a plain-English summary")]
for i,(week,title,desc) in enumerate(steps):
    left=0.5+i*3.1
    box(w1,left,1.4,2.9,5.5,PLGR)
    box(w1,left,1.4,2.9,0.6,PNAV)
    tx(w1,week,left+0.1,1.45,2.7,0.5,sz=12,bold=True,col=PWHT)
    tx(w1,title,left+0.1,2.1,2.7,0.6,sz=11,bold=True,col=PNAV)
    tx(w1,desc,left+0.1,2.8,2.7,3.5,sz=10,col=PDGR)

w2=sl(ppt2)
box(w2,0,0,13.33,1.2,PNAV)
tx(w2,"HOW WE WORK TOGETHER",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
for i,(title,body) in enumerate([
    ("Documents to Send Us Monthly","Bank statements, credit card statements, receipts for large purchases, any payroll records, invoices issued"),
    ("Your Monthly Deadline","Send documents by the [5th] of each month. We deliver your statements by the [20th]."),
    ("How We Communicate","[Primary: email] [Secondary: monthly Zoom call] [Response time: within 1 business day]"),
    ("Your Client Portal","[Link to shared folder or Notion workspace] -- all reports archived here"),
]):
    left=0.5+(i%2)*6.4; top=1.4+(i//2)*2.9
    box(w2,left,top,6.0,2.6,PLGR)
    tx(w2,title,left+0.2,top+0.15,5.6,0.6,sz=12,bold=True,col=PNAV)
    tx(w2,body,left+0.2,top+0.85,5.6,1.6,sz=11,col=PDGR)

w3=sl(ppt2)
box(w3,0,0,13.33,7.5,PNAV)
box(w3,0,6.0,13.33,1.5,PACC)
tx(w3,"YOU'RE IN GOOD HANDS.",0.5,1.8,12,0.9,sz=34,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(w3,"We take the numbers seriously so you don't have to.",0.5,3.0,12,0.6,sz=17,col=PGLD,a=PP_ALIGN.CENTER)
tx(w3,"Questions? [Email] | [Phone]",0.5,4.0,12,0.6,sz=14,col=PWHT,a=PP_ALIGN.CENTER)
tx(w3,"[Your Name]  |  [Your Business Name]",0.5,6.2,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)

ppt2.save(BASE+p10+"Client_Welcome_Deck.pptx")
print(f"  pptx {p10}Client_Welcome_Deck.pptx")
print("✓ 10_CANVA_TEMPLATES done")

# ── 11 BONUSES ────────────────────────────────────────────────────────────────
p11="11_BONUSES/"
print("Building 11_BONUSES...")

doc(p11+"Bookkeeper_Scripts_Vault.docx",
    "Bookkeeper Scripts Vault",
    "Bookkeeper Launch System | Scripts for Every Client Situation",
    [
        ("Cold Outreach Script (Email)", [
            "Subject: Bookkeeping for [Business Type] in [City]",
            "Hi [Name],",
            "I specialize in bookkeeping for [industry] businesses in [city area], and I came across [Business Name] while [how you found them].",
            "Many of my [industry] clients come to me with the same challenges: [problem 1], [problem 2], and spending too much time on paperwork instead of running their business.",
            "I'd love to offer you a complimentary 30-minute financial overview call -- no obligation. I'll review your current setup and give you 3 actionable tips you can use right away, whether you hire me or not.",
            "Interested? Here's my calendar: [Calendly link]",
            "Best, [Your Name] | [Credentials] | [Phone]",
        ]),
        ("Discovery Call Script", [
            "Opening: 'Thanks for taking the time today. My goal for this call is to learn about your business and see if what I offer is a good fit. There's absolutely no pressure to hire me -- I just want to understand where you are and where you want to go. Does that sound good?'",
            "Business discovery questions:",
            ("*","'Tell me about your business -- how long have you been operating and what do you do?'"),
            ("*","'How are you currently handling your bookkeeping?'"),
            ("*","'What's the biggest pain point with your finances right now?'"),
            ("*","'Do you know your current profit margin? Is your cash flow where you want it to be?'"),
            ("*","'Are you working with a CPA for your taxes?'"),
            "Transition to proposal: 'Based on what you've shared, here's what I'd recommend for your situation...'",
            "Closing: 'Does this sound like what you're looking for? I'd love to put together a formal proposal for you this week. When are you hoping to get started?'",
        ]),
        ("Proposal Objection Handling", [
            ("*","'I'll do it myself' -- 'I completely understand -- many business owners feel that way at first. Can I ask: how many hours do you spend on bookkeeping each month? At what point would your time be better spent running your business? Most of my clients save 8-12 hours per month and have books that are actually accurate for the first time.'"),
            ("*","'My spouse/partner handles it' -- 'That's great that you have support. How confident are you both that the books are accurate and tax-ready? Many businesses I take over from family bookkeepers discover errors or missed deductions that cost them more than my fee.'"),
            ("*","'I already have QuickBooks' -- 'Perfect -- I work in QuickBooks every day. Having the software is step one. But are the transactions properly categorized, reconciled monthly, and ready to hand to your CPA? That's what I handle.'"),
            ("*","'Your price is too high' -- 'I understand. What budget were you thinking? [Listen]. The reason my rate is $X is because [value]. Consider what one missed tax deduction or one audit could cost you -- most clients find that my fee pays for itself quickly.'"),
        ]),
    ])

# 52 Weeks content calendar for bookkeepers
with open(BASE+p11+"52_Week_Content_Calendar.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    w.writerow(["Week","Date (Monday)","Content Topic","Platform","Format","Caption Hook"])
    topics=[
        "3 signs your small business bookkeeping is a disaster","How to read your Profit & Loss statement",
        "Why you need to reconcile your bank accounts every month","Tax deductions most small business owners miss",
        "The difference between a bookkeeper and a CPA","How much should bookkeeping cost?",
        "Why cash flow is more important than profit","QuickBooks tip: how to categorize transactions",
        "What is Chart of Accounts and why it matters","End-of-year bookkeeping checklist for small business",
        "How to prepare for tax season starting January 1","Should you use Wave or QuickBooks?",
        "The true cost of DIY bookkeeping for a small business","How to pay yourself as a business owner",
        "What is self-employment tax and how to plan for it","S-Corp election: could it save you money?",
        "The 5 accounts every business owner should track weekly","How to handle personal expenses on a business card",
        "What documents should you send your bookkeeper monthly","How to set up a business bank account",
        "The most expensive bookkeeping mistake small businesses make","Quarterly estimated taxes: how to calculate them",
        "Home office deduction: how to claim it correctly","Vehicle deduction: mileage method vs. actual expenses",
        "How to build a 6-month cash reserve for your business","What to look for when hiring a bookkeeper",
        "Red flags in your financial statements","How to use bookkeeping to make better business decisions",
        "What is accounts receivable and how to manage it","Client success story: from shoe-box receipts to clean books",
        "My 10-step monthly bookkeeping routine (for business owners)","The right way to handle owner draws and investments",
        "Why your accountant needs clean books before tax season","How AI is changing bookkeeping (what it means for you)",
        "Should you use accrual or cash basis accounting?","10 questions to ask before hiring a bookkeeper",
        "The most common audit triggers for small businesses","What is a business entity type and which is best?",
        "How to fire your current bookkeeper professionally","Year-end financial review checklist",
        "How to organize your business receipts (a simple system)","What does a bank reconciliation actually do?",
        "Building business credit: what your bookkeeper needs you to know","Payroll basics for the small business owner",
        "What is a budget and how to build one for your business","How to read a Balance Sheet in 5 minutes",
        "The one financial metric that predicts business failure","End-of-year letter from your bookkeeper",
    ]
    platforms=["LinkedIn","Instagram","Facebook","LinkedIn","Instagram"]
    formats=["Text Post","Carousel","Video","Text Post","Story"]
    for i,topic in enumerate(topics):
        week=i+1
        plat=platforms[i%5]
        fmt=formats[i%5]
        hook=f"Most business owners don't know this about {topic.lower()[:30]}..." if i%3==0 else f"'{topic[:40]}...' -- here's the truth"
        w.writerow([f"Week {week}",f"2026-01-{(i*7+5)%28+1:02d}" if i<4 else f"2026-{(i//4+1):02d}-{((i%4)*7+5)%28+1:02d}",topic,plat,fmt,hook])
print(f"  csv {p11}52_Week_Content_Calendar.csv")

doc(p11+"Bookkeeper_Growth_Playbook.docx",
    "Bookkeeper Practice Growth Playbook",
    "Bookkeeper Launch System | From First Client to Full Practice",
    [
        ("Your First 3 Clients: The Foundation", [
            "The first 3 clients are the hardest -- and the most important. They give you experience, testimonials, and referrals that fuel all future growth.",
            ("*","Client 1: Ask everyone you know. Family, friends, former colleagues. Offer a discounted rate in exchange for a testimonial and permission to use their business as a case study"),
            ("*","Client 2: Join 2 local business Facebook groups. Answer questions about bookkeeping and taxes. Don't pitch -- just help. DMs will come"),
            ("*","Client 3: Contact 5 local CPAs and introduce yourself as a bookkeeper looking for overflow clients. CPAs turn away bookkeeping work daily"),
        ]),
        ("The Referral Engine", [
            "After your first 3 months, your primary growth engine should be referrals. Here's how to build it:",
            ("*","After every positive client interaction, say: 'I really enjoy working with [Business Name]. If you know anyone else who could use clean books, I'd love an introduction.'"),
            ("*","Send a formal 'referral program' letter to all clients after 90 days: 10% commission for any referral that becomes a client for 3+ months"),
            ("*","At year-end, send every client a thank-you card with a handwritten note. Include 2 business cards"),
            ("*","Stay top of mind with a monthly email newsletter -- one tip, one resource, and a gentle reminder that you have availability"),
        ]),
        ("Scaling Beyond Solo", [
            "When you have 8-10 clients, you'll hit a capacity wall. Here's how to scale:",
            ("*","Hire a bookkeeping contractor: find a part-time bookkeeper on Upwork or Indeed. Train them on your processes. Start them with your simpler clients"),
            ("*","Build SOPs before hiring: document every process so new team members can do the work to your standard"),
            ("*","Move from doer to reviewer: your role evolves from doing the bookkeeping to reviewing and managing"),
            ("*","Target higher-value clients: as you grow, replace lower-paying clients with higher-value ones"),
            ("*","Add services: payroll, CFO advisory, and tax prep support increase average revenue per client by 40-80%"),
        ]),
    ])
print("✓ 11_BONUSES done")

# ── 12 ETSY RESOURCES (bonus section) ────────────────────────────────────────
p12="12_ETSY_RESOURCES/"
print("Building 12_ETSY_RESOURCES...")
doc(p12+"Etsy_Bookkeeping_Resource_Guide.docx",
    "Etsy Seller Bookkeeping Guide",
    "Bookkeeper Launch System | A Bonus Resource for Etsy Seller Clients",
    [
        ("Why Etsy Sellers Need a Bookkeeper", [
            "Etsy sellers are one of the fastest-growing niches for bookkeepers. Most don't track income accurately, don't separate business and personal finances, and miss dozens of deductions.",
            ("*","Revenue tracking: Etsy pays out via 1099-K for sellers over $5,000 in payments. Many sellers don't realize this is taxable income"),
            ("*","Expense tracking: shipping costs, materials, listing fees, shipping supplies, Etsy fees -- all deductible"),
            ("*","Sales tax complexity: Etsy collects sales tax in most states, but some states require separate filings"),
        ]),
        ("Etsy Seller Deductions Checklist", [
            ("*","Etsy listing fees and transaction fees"),
            ("*","Etsy advertising costs (Etsy Ads)"),
            ("*","Raw materials and supplies used to make products"),
            ("*","Shipping costs and packaging materials"),
            ("*","Home office deduction (if crafting/packaging at home)"),
            ("*","Photography equipment and editing software"),
            ("*","Canva Pro and design software subscriptions"),
            ("*","PayPal/Stripe fees for sales outside Etsy"),
            ("*","Business bank account fees"),
            ("*","Marketing and social media advertising"),
        ]),
    ])
print("✓ 12_ETSY_RESOURCES done")

# ── PDFs ──────────────────────────────────────────────────────────────────────
print("Building PDFs...")
make_pdf(BASE+"Bookkeeper_Launch_Guide.pdf",
    "Bookkeeper Practice Launch Guide",
    "Everything you need to launch your professional bookkeeping practice -- from zero to first client",
    [
        ("Welcome to Your Bookkeeper Launch System", [
            "This system was built for one purpose: to help you launch a professional, profitable bookkeeping practice as fast as possible. Whether you're a complete beginner or an experienced bookkeeper going independent, this system has everything you need.",
            ("*","Section overview: 12 organized folders with 50+ files covering every aspect of a bookkeeping practice"),
            ("*","Start with folder 00_START_HERE for your 30-day launch checklist"),
            ("*","Import all CSVs in 09_NOTION_WORKSPACE for your complete digital workspace"),
            ("*","Use PPTX files in 10_CANVA_TEMPLATES by importing to Canva"),
        ]),
        ("Your First 30 Days: Launch Checklist", [
            ("*","Days 1-3: Set up your business structure (LLC recommended), business bank account, and EIN"),
            ("*","Days 4-7: Get QuickBooks Online ProAdvisor certification (free at intuit.com/accountants)"),
            ("*","Days 8-14: Build your service packages using the pricing calculator in Section 05"),
            ("*","Days 15-21: Create your professional materials (contracts from Section 03, proposal from Section 02)"),
            ("*","Days 22-28: Begin outreach -- 5 CPAs for referral partnerships, 3 Facebook groups to join"),
            ("*","Day 29-30: Book your first discovery call"),
        ]),
        ("The Bookkeeper's Unfair Advantage: Credentials", [
            "Credentials are the fastest way to overcome the trust barrier with new clients. Three worth getting:",
            ("*","QuickBooks Online ProAdvisor (free): The most recognized credential. Gets you listed in Intuit's Find-a-ProAdvisor directory"),
            ("*","Bookkeeper Launch Certified: Ben Robinson's program is the industry standard for trained bookkeepers"),
            ("*","Enrolled Agent (advanced): Allows you to represent clients before the IRS and significantly expand your service menu"),
        ]),
        ("Pricing with Confidence", [
            "Most new bookkeepers underprice. Here's the framework to price right from day one:",
            ("*","Track your time for your first 3 clients. Calculate your effective hourly rate"),
            ("*","Target minimum $60/hour effective rate. Most experienced bookkeepers achieve $80-120/hour"),
            ("*","Quote retainers, not hourly. Clients prefer predictable monthly fees"),
            ("*","Your first client might be at a discount. Your third client should be at full rate"),
            ("*","Never apologize for your prices. Confidence in pricing is confidence in your service"),
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
manifest={"product":"Ultimate Bookkeeper Launch System","version":"2.0","total_files":len(all_files),
          "files":[{"path":r[0],"type":r[1],"size":r[2]} for r in all_files]}
with open(BASE+"Asset_Manifest.json","w") as f: json.dump(manifest,f,indent=2)
print(f"  Manifest: {len(all_files)} files")

# ── Etsy Listing ──────────────────────────────────────────────────────────────
etsy="""TITLE:
Bookkeeper Practice Launch System | Complete Business Kit | 50+ Files | Canva Templates | Notion Workspace

DESCRIPTION:
Launch your professional bookkeeping practice with the most complete business toolkit available. This system gives you every template, spreadsheet, guide, and resource you need to land clients, deliver exceptional service, and build a practice that generates consistent recurring revenue.

WHAT'S INCLUDED (50+ files across 12 folders):

00 START HERE
- 30-day launch checklist and action plan
- System overview and quick-start guide

01 BUSINESS SETUP
- Business plan template
- Legal structure guide
- Service menu and pricing guide
- Professional bio template

02 CLIENT ACQUISITION
- Lead generation tracker
- Cold email and DM templates
- Discovery call script
- CPA referral partnership template

03 PROPOSALS & CONTRACTS
- Professional proposal template
- Bookkeeping service agreement
- Scope of work template
- Engagement letter template

04 CLIENT MANAGEMENT
- Client database tracker (XLSX with 8 sample clients)
- Contact log and communication history
- Revenue dashboard
- Client onboarding guide
- Client communication templates (welcome, monthly statements, follow-ups)

05 BOOKKEEPING SYSTEMS
- Month-end checklist (15-step process)
- Chart of Accounts template (24 accounts)
- Bank reconciliation guide
- Financial statements guide (P&L, Balance Sheet, Cash Flow)
- Pricing calculator

06 TAX PREP SUPPORT
- Tax document checklist for clients
- Quarterly tax planning workbook (XLSX)
- Small business tax basics guide

07 SOFTWARE TOOLS
- QuickBooks vs. Xero vs. Wave comparison guide
- QuickBooks Online setup guide (step-by-step)
- Recommended tech stack for bookkeepers

08 BUSINESS OPERATIONS
- Annual revenue planning workbook (XLSX)
- KPI dashboard
- Marketing your bookkeeping practice guide

09 NOTION WORKSPACE
- 5 Notion-importable databases (CSV)
- Client roster, task board, expense log, lead pipeline, invoice log
- Notion setup guide

10 CANVA TEMPLATES (PPTX - import directly to Canva)
- Services overview presentation deck
- Client welcome deck

11 BONUSES
- Bookkeeper scripts vault (discovery calls, objections, email scripts)
- 52-week content calendar (CSV - 52 social media topics for bookkeepers)
- Practice growth playbook

12 BONUS: ETSY SELLER NICHE GUIDE
- Bookkeeping guide specifically for Etsy seller clients

PERFECT FOR:
- Bookkeepers starting their own practice
- Accountants going independent
- Virtual bookkeepers building a client roster
- Experienced bookkeepers who want better systems
- CPAs looking for bookkeeping SOPs to delegate to staff

FORMATS INCLUDED:
- DOCX (editable Word documents)
- XLSX (spreadsheets with formulas and color-coded design)
- PDF (print-ready guides)
- PPTX (Canva-importable presentation templates)
- CSV (Notion-importable databases)

INSTANT DIGITAL DOWNLOAD - No physical product shipped.
You receive a ZIP file immediately after purchase with all 50+ files organized in 12 clearly labeled folders.

TAGS:
bookkeeper, bookkeeping business, bookkeeping templates, small business bookkeeping, bookkeeper starter kit, accounting templates, quickbooks templates, notion template, canva templates, business templates, bookkeeper tools, financial templates, bookkeeping course, bookkeeper resources, accounting business"""

with open(ETSY_DIR+"07_Bookkeeper_Listing.txt","w",encoding="utf-8") as f:
    f.write(etsy)
print("  etsy 07_Bookkeeper_Listing.txt")

# ── ZIP ───────────────────────────────────────────────────────────────────────
print("Creating ZIP...")
ZIP_PATH="/home/user/oqul-phase55-production/bookkeeper-launch-system/BUYER_DOWNLOAD_BookkeeperLaunchSystem.zip"
with zipfile.ZipFile(ZIP_PATH,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        dirs.sort()
        for f in sorted(files):
            full=os.path.join(root,f)
            arc=os.path.relpath(full,os.path.dirname(BASE))
            z.write(full,arc)
size_mb=os.path.getsize(ZIP_PATH)/1024/1024
print(f"✓ ZIP: {ZIP_PATH} ({size_mb:.1f} MB)")
print("\n=== BOOKKEEPER LAUNCH SYSTEM COMPLETE ===")
