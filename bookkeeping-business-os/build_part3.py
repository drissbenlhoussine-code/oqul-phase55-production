"""Bookkeeping Business OS — Part 3: folders 08–10 + XLSX + CSVs + MD"""
import os, csv
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/bookkeeping-business-os/Ultimate_Bookkeeping_Business_Operating_System/"
NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"

def hf(hex_): return PatternFill("solid", fgColor=hex_)
def bf(bold=True, sz=11, color="000000"): return Font(bold=bold, size=sz, color=color)
def al(h="center",v="center"): return Alignment(horizontal=h,vertical=v,wrap_text=True)
def thin(): s=Side(style='thin',color='CCCCCC'); return Border(left=s,right=s,top=s,bottom=s)
def hrow(ws,row,cols,texts,bg=NAV,fg=WHT):
    for col,text in zip(cols,texts):
        c=ws.cell(row=row,column=col,value=text)
        c.fill=hf(bg); c.font=bf(True,11,fg); c.alignment=al(); c.border=thin()
def drow(ws,row,cols,vals,bg=WHT):
    for col,val in zip(cols,vals):
        c=ws.cell(row=row,column=col,value=val)
        c.fill=hf(bg); c.font=bf(False,10); c.alignment=al("left"); c.border=thin()

def doc(filename, title, subtitle, sections):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
    if subtitle:
        s = d.add_paragraph(subtitle); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10)
        s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
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

def write_csv(path, headers, rows):
    with open(BASE+path, "w", newline="", encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
    print(f"  ✓ {path}")

# ── 08_FINANCIAL_REPORTING ────────────────────────────────────────────────────
doc("08_FINANCIAL_REPORTING/Monthly_Financial_Report_Template.docx",
    "Monthly Financial Report Template",
    "Bookkeeping Business Operating System | Financial Reporting",
    [
        ("REPORT COVER PAGE", [
            "[Client Business Name]",
            "Monthly Financial Report — [Month] [Year]",
            "Prepared by [Your Business Name]",
            "Delivered: [Date]",
        ]),
        ("SECTION 1 — EXECUTIVE SUMMARY", [
            "Revenue: $[X] (vs. $[X] last month | vs. $[X] same month last year)",
            "Total Expenses: $[X]",
            "Net Profit: $[X] | Profit Margin: [X]%",
            "Cash Balance: $[X] as of [date]",
            "",
            "KEY OBSERVATIONS:",
            ("•", "[Observation 1 — e.g., Revenue increased 12% driven by [service/product]]"),
            ("•", "[Observation 2 — e.g., Marketing spend up $[X] this month for [campaign]]"),
            ("•", "[Observation 3 — e.g., Accounts receivable aging: $[X] overdue 30+ days]"),
            "",
            "ACTION ITEMS:",
            ("•", "[Action 1 — specific, with deadline if applicable]"),
            ("•", "[Action 2]"),
        ]),
        ("SECTION 2 — PROFIT & LOSS HIGHLIGHTS", [
            "Top Revenue Categories:",
            ("•", "[Category 1]: $[X] ([X]% of total revenue)"),
            ("•", "[Category 2]: $[X] ([X]% of total revenue)"),
            "",
            "Top Expense Categories:",
            ("•", "[Category 1]: $[X] ([X]% of expenses)"),
            ("•", "[Category 2]: $[X] ([X]% of expenses)"),
            "",
            "Gross Profit: $[X] | Gross Margin: [X]%",
            "Net Operating Income: $[X]",
        ]),
        ("SECTION 3 — BALANCE SHEET SNAPSHOT", [
            "Total Assets: $[X]",
            ("•", "Current Assets: $[X] (cash + receivables + inventory)"),
            ("•", "Fixed Assets: $[X] (net of depreciation)"),
            "Total Liabilities: $[X]",
            ("•", "Current Liabilities: $[X] (due within 12 months)"),
            ("•", "Long-Term Liabilities: $[X]"),
            "Owner's Equity: $[X]",
        ]),
        ("SECTION 4 — CASH FLOW NOTES", [
            ("•", "Beginning cash balance: $[X]"),
            ("•", "Cash received from operations: $[X]"),
            ("•", "Cash paid for expenses: $[X]"),
            ("•", "Ending cash balance: $[X]"),
            ("•", "[ ] Cash flow is healthy  [ ] Tight — monitor  [ ] Concern — discuss with client"),
        ]),
    ])

doc("08_FINANCIAL_REPORTING/Cash_Flow_Analysis_Guide.docx",
    "Cash Flow Analysis Guide",
    "Bookkeeping Business Operating System | Financial Reporting",
    [
        ("WHY CASH FLOW MATTERS MORE THAN PROFIT", [
            "A business can show a profit on paper while running out of cash. This happens when revenue is earned but not collected, or when expenses are paid before revenue comes in. Understanding cash flow prevents this common trap.",
        ]),
        ("THE THREE TYPES OF CASH FLOW", [
            ("•", "Operating Cash Flow: Cash from core business activities (sales, payroll, vendor payments)"),
            ("•", "Investing Cash Flow: Cash from buying/selling assets (equipment, property)"),
            ("•", "Financing Cash Flow: Cash from loans, owner contributions, or owner draws"),
        ]),
        ("CASH FLOW ANALYSIS PROCESS", [
            "Step 1: Identify beginning and ending cash balance from bank statements",
            "Step 2: Run Statement of Cash Flows from accounting software",
            "Step 3: Compare operating cash flow to net income — large differences signal timing issues",
            "Step 4: Identify the biggest cash uses — are they one-time or recurring?",
            "Step 5: Calculate cash runway: Cash balance / Monthly burn rate = months of runway",
        ]),
        ("COMMON CASH FLOW PROBLEMS AND SOLUTIONS", [
            ("•", "Slow-paying customers: Tighten AR terms; offer early payment discounts; send reminders at 7 days past due"),
            ("•", "High inventory: Review slow-moving items; negotiate longer payment terms with suppliers"),
            ("•", "Seasonal revenue: Build cash reserves in strong months; use a line of credit for slow periods"),
            ("•", "Fast growth: Growth consumes cash — model funding needs before expanding payroll or inventory"),
            ("•", "Owner draws exceeding profit: Ensure draws are calibrated to actual profit, not revenue"),
        ]),
        ("CASH FLOW METRICS TO TRACK MONTHLY", [
            ("•", "Cash runway (months): Cash balance / Monthly average expenses"),
            ("•", "Days Sales Outstanding (DSO): Average AR / Daily revenue — measures how fast clients pay"),
            ("•", "Days Payable Outstanding (DPO): Average AP / Daily COGS — measures vendor payment timing"),
            ("•", "Operating cash flow margin: Operating cash flow / Revenue"),
        ]),
    ])

doc("08_FINANCIAL_REPORTING/KPI_Reporting_Guide.docx",
    "KPI Reporting Guide",
    "Bookkeeping Business Operating System | Financial Reporting",
    [
        ("WHAT IS A KPI AND WHY TRACK THEM", [
            "Key Performance Indicators (KPIs) are specific, measurable metrics that indicate business health. Monthly KPI reporting gives clients a quick-read dashboard so they can make informed decisions, not just react to surprises.",
        ]),
        ("UNIVERSAL BUSINESS KPIs", [
            ("•", "Revenue growth rate: (This month - Last month) / Last month × 100"),
            ("•", "Gross profit margin: (Revenue - COGS) / Revenue × 100"),
            ("•", "Net profit margin: Net profit / Revenue × 100"),
            ("•", "Operating expense ratio: Total opex / Revenue × 100"),
            ("•", "Cash runway: Cash balance / Monthly burn rate (in months)"),
        ]),
        ("INDUSTRY-SPECIFIC KPIs", [
            ("•", "Restaurants: Food cost %, Labor %, Prime cost %, Revenue per seat"),
            ("•", "Retail / E-commerce: COGS %, Inventory turnover, Return rate, Average order value"),
            ("•", "Service businesses: Revenue per client, Client retention rate, Average project value"),
            ("•", "Construction: Job gross margin %, Backlog value, Revenue per employee"),
            ("•", "SaaS/Subscription: MRR, Churn rate, LTV, Customer acquisition cost"),
        ]),
        ("HOW TO PRESENT KPIS TO CLIENTS", [
            "Keep it simple: highlight 5–7 KPIs maximum on the monthly summary",
            ("•", "Format: Current month → Last month → Same month last year"),
            ("•", "Use color coding: green (on target), yellow (watch), red (action needed)"),
            ("•", "Provide context: 'Your labor cost % was 32% — the industry average is 28–35%'"),
            ("•", "Focus on trends, not single data points: one month is noise; three months is a pattern"),
        ]),
        ("KPI REPORTING SETUP IN ACCOUNTING SOFTWARE", [
            ("•", "QuickBooks: Use 'Business Overview' dashboard; create custom reports by category"),
            ("•", "Xero: Analytics Plus provides KPI tracking; use watchlists for key accounts"),
            ("•", "Wave: Run custom P&L with percentage columns for margin visibility"),
            ("•", "Third-party tools: Fathom, Spotlight Reporting, Jirav for advanced KPI dashboards"),
        ]),
    ])

doc("08_FINANCIAL_REPORTING/Financial_Review_Meeting_Script.docx",
    "Financial Review Meeting Script",
    "Bookkeeping Business Operating System | Financial Reporting",
    [
        ("WHEN TO HOLD FINANCIAL REVIEW MEETINGS", [
            "Offer quarterly review meetings to all clients — monthly for high-touch clients. These are 30–45 minute calls where you walk through the numbers and help clients understand their business health. This deepens client relationships and creates upsell opportunities.",
        ]),
        ("OPENING (0–3 min)", [
            "'[Name], thanks for making time. The goal today is to walk through your [quarter/month] financials, share what I'm seeing, and make sure we're aligned on what the numbers mean for your business. Sound good?'",
        ]),
        ("REVENUE REVIEW (3–10 min)", [
            ("•", "'Your revenue for [period] was $[X] — [up/down] [X]% from [prior period]. What's your sense of why? [Let client talk]'"),
            ("•", "'Your best revenue month was [month] — what drove that?'"),
            ("•", "'Are you tracking toward your annual goal of $[X]?'"),
        ]),
        ("EXPENSE REVIEW (10–18 min)", [
            ("•", "'Total expenses were $[X]. Your biggest categories were [1], [2], [3].'"),
            ("•", "'I noticed [specific item] increased significantly — what was that for?'"),
            ("•", "'Is there anything in the expenses that doesn't look right to you?'"),
        ]),
        ("CASH AND BALANCE SHEET (18–25 min)", [
            ("•", "'Your cash position is $[X]. [Strong/tight]. Here's my concern: [if any].'"),
            ("•", "'You have $[X] in outstanding receivables — [X] of that is over 30 days old. Want me to flag those for you?'"),
            ("•", "'Your loans are on track — current balance is $[X] and you're paying $[X]/month.'"),
        ]),
        ("FORWARD LOOK AND OPPORTUNITIES (25–35 min)", [
            ("•", "'Based on your YTD numbers, I'd estimate you'll finish the year at approximately $[X] revenue and $[X] net profit. Does that align with where you think you're headed?'"),
            ("•", "'One area I think is worth watching: [specific opportunity or risk].'"),
            ("•", "'Is there anything coming up — a new hire, big purchase, seasonal change — I should factor into next quarter's close?'"),
        ]),
        ("CLOSE (35–40 min)", [
            "'Any questions before we wrap up? Great. I'll have your next report to you by [date]. If anything comes up, just email me.'",
        ]),
    ])

print("✓ 08_FINANCIAL_REPORTING complete")

# ── 09_BUSINESS_OPERATIONS ────────────────────────────────────────────────────
doc("09_BUSINESS_OPERATIONS/Business_Goals_Workbook.docx",
    "Business Goals Workbook",
    "Bookkeeping Business Operating System | Business Operations",
    [
        ("CURRENT STATE ASSESSMENT", [
            ("•", "Current number of clients: _______"),
            ("•", "Monthly recurring revenue (MRR): $_______"),
            ("•", "Annual revenue last year: $_______"),
            ("•", "Average monthly fee per client: $_______"),
            ("•", "Number of hours worked per week: _______"),
            ("•", "Revenue per hour: $_______"),
            ("•", "Biggest time drain: _______________________________"),
            ("•", "Services offered: _______________________________"),
        ]),
        ("ANNUAL GOALS", [
            ("•", "Revenue goal: $_______"),
            ("•", "Target number of clients: _______"),
            ("•", "Target average monthly fee: $_______"),
            ("•", "Maximum hours per week: _______"),
            ("•", "Revenue per hour target: $_______"),
            ("•", "One new service to launch: _______________________________"),
            ("•", "One niche to specialize in: _______________________________"),
        ]),
        ("QUARTERLY SPRINT (90 Days)", [
            ("•", "Revenue target: $_______"),
            ("•", "New clients to add: _______"),
            ("•", "BD activities per week: _______"),
            ("•", "Priority #1: _______________________________"),
            ("•", "Priority #2: _______________________________"),
            ("•", "One system to improve: _______________________________"),
        ]),
        ("MONTHLY REVENUE CALCULATOR", [
            "Formula: Monthly clients × Average fee = MRR",
            ("•", "To hit $10,000 MRR: need [X] clients at $[avg fee]"),
            ("•", "To hit $20,000 MRR: need [X] clients at $[avg fee]"),
            ("•", "To hit $50,000 MRR: need [X] clients or higher-value clients"),
            "",
            "My current MRR: $_______",
            "My target MRR: $_______",
            "Clients needed at my average fee: _______",
        ]),
        ("MONTHLY REVIEW", [
            ("•", "Clients added: _______"),
            ("•", "Clients churned: _______"),
            ("•", "MRR this month: $_______"),
            ("•", "Hours worked: _______"),
            ("•", "Biggest win: _______________________________"),
            ("•", "What I'll improve next month: _______________________________"),
        ]),
    ])

doc("09_BUSINESS_OPERATIONS/Team_Management_Guide.docx",
    "Team Management Guide",
    "Bookkeeping Business Operating System | Business Operations",
    [
        ("WHEN TO HIRE YOUR FIRST TEAM MEMBER", [
            ("•", "You are working more than 45 hours/week consistently"),
            ("•", "You're turning away clients or missing deadlines"),
            ("•", "MRR is consistently above $[8,000–10,000]/month"),
            ("•", "You have documented processes that could be taught to someone else"),
        ]),
        ("FIRST HIRE OPTIONS", [
            ("•", "Virtual bookkeeping assistant: $15–25/hour; handles data entry, categorization, bank feed management"),
            ("•", "Part-time bookkeeper: Can handle more complex work; $25–45/hour"),
            ("•", "Offshore bookkeeping team: Lower cost for high-volume data entry; requires strong QC process"),
        ]),
        ("WHAT TO DELEGATE FIRST", [
            ("•", "Transaction categorization"),
            ("•", "Bank statement downloading and organizing"),
            ("•", "Invoice entry and AP tracking"),
            ("•", "Client communication follow-ups"),
            ("•", "Report formatting and delivery"),
        ]),
        ("QUALITY CONTROL PROCESS", [
            ("•", "Never deliver reports without reviewing them yourself (for now)"),
            ("•", "Use a reconciliation checklist before sign-off on any client file"),
            ("•", "Review team member's work for the first 90 days on every client"),
            ("•", "Spot-check 20% of transactions randomly each month"),
        ]),
        ("TEAM COMMUNICATION AND TOOLS", [
            ("•", "Project management: Asana, ClickUp, or Monday for task tracking per client"),
            ("•", "Communication: Slack for team; email for clients"),
            ("•", "File sharing: Shared cloud folder (Google Drive or Dropbox) per client"),
            ("•", "Time tracking: Harvest or Toggl if billing hourly or tracking team efficiency"),
        ]),
    ])

doc("09_BUSINESS_OPERATIONS/Bookkeeper_Training_Manual.docx",
    "Bookkeeper Training Manual",
    "Bookkeeping Business Operating System | Business Operations",
    [
        ("WEEK 1 — FOUNDATION", [
            ("•", "Day 1: Business overview, our standards, tools setup"),
            ("•", "Day 2: QuickBooks/Xero overview; chart of accounts deep-dive"),
            ("•", "Day 3: Bank reconciliation training — 3 practice accounts"),
            ("•", "Day 4: Transaction categorization practice with sample files"),
            ("•", "Day 5: AR and AP processes; review of SOP library"),
        ]),
        ("WEEK 2 — CLIENT WORKFLOW", [
            ("•", "Shadow experienced bookkeeper on 2 existing client closes"),
            ("•", "Practice monthly P&L and Balance Sheet export and formatting"),
            ("•", "Learn client communication process and email templates"),
            ("•", "Complete one full client month close under supervision"),
        ]),
        ("WEEK 3 — QUALITY STANDARDS", [
            ("•", "Review common categorization errors and how to spot them"),
            ("•", "Learn discrepancy resolution process"),
            ("•", "Practice writing monthly summary notes for client reports"),
            ("•", "Complete quality checklist training"),
        ]),
        ("WEEK 4 — SOLO OPERATION", [
            ("•", "Manage assigned clients independently with QC review"),
            ("•", "Handle document requests with client communication templates"),
            ("•", "Complete 30/60/90 day plan with individual KPI targets"),
        ]),
        ("STAFF KPIs", [
            ("•", "Clients closed on time (by the [X]th): Target 100%"),
            ("•", "Client reports requiring revision: Target <5%"),
            ("•", "Document requests to clients: Target <2 per client per month"),
            ("•", "Response time to client questions: Target 24 hours"),
        ]),
    ])

# KPI Dashboard XLSX
wb=Workbook()
ws=wb.active; ws.title="KPI Dashboard"
ws.merge_cells('A1:E1')
c=ws['A1']; c.value="BOOKKEEPING BUSINESS — KPI DASHBOARD"
c.fill=hf(NAV); c.font=bf(True,14,WHT); c.alignment=al()
for col,w in zip("ABCDE",[28,15,15,15,15]):
    ws.column_dimensions[col].width=w
hrow(ws,2,list(range(1,6)),["Metric","Target","Jan","Feb","Mar"],ACC,WHT)
metrics=[
    ("Monthly Recurring Revenue","$10,000","$8,400","$9,200","$10,000"),
    ("Active Clients","25","21","23","25"),
    ("Avg Fee Per Client","$400","$400","$400","$400"),
    ("New Clients Added","2","1","2","2"),
    ("Clients Churned","0","0","1","0"),
    ("Reports Delivered On Time","100%","95%","100%","100%"),
    ("Hours Worked / Week","40","44","42","40"),
    ("Revenue Per Hour","$62","$53","$57","$62"),
    ("Client Satisfaction Score","9/10","8.5","9","9"),
    ("Overdue AR (own invoices)","$0","$800","$400","$0"),
]
for i,r in enumerate(metrics,3):
    drow(ws,i,list(range(1,6)),list(r),LGR if i%2==0 else WHT)
ws2=wb.create_sheet("Revenue Projection")
for col,w in zip("ABCD",[20,18,18,18]):
    ws2.column_dimensions[col].width=w
hrow(ws2,1,[1,2,3,4],["Month","Active Clients","Avg Fee","MRR"],GLD,"000000")
for i,m in enumerate(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],2):
    drow(ws2,i,[1,2,3,4],[m,"","$400","=B{}*C{}".format(i,i)],LGR if i%2==0 else WHT)
wb.save(BASE+"09_BUSINESS_OPERATIONS/Business_KPI_Dashboard.xlsx")
print("  ✓ 09_BUSINESS_OPERATIONS/Business_KPI_Dashboard.xlsx")

# Financial Dashboard XLSX
wb3=Workbook()
ws=wb3.active; ws.title="Monthly Dashboard"
ws.merge_cells('A1:F1')
c=ws['A1']; c.value="CLIENT FINANCIAL DASHBOARD"
c.fill=hf(NAV); c.font=bf(True,14,WHT); c.alignment=al()
for col,w in zip("ABCDEF",[25,15,15,15,15,15]):
    ws.column_dimensions[col].width=w
hrow(ws,2,list(range(1,7)),["Client","MRR","YTD Revenue","Last Report Sent","Status","Notes"])
clients=[
    ("Joe's Plumbing","$400","$4,800","Jan 20","Current","On track"),
    ("Riverdale Cafe","$600","$7,200","Jan 15","Current","Strong month"),
    ("Green Lawn LLC","$350","$4,200","Jan 10","Current","Seasonal slow"),
    ("StyleHouse Salon","$300","$900","Jan 25","Setup","Awaiting access"),
    ("BuildRight Co","$800","$9,600","Jan 18","Current","Job cost review needed"),
]
for i,r in enumerate(clients,3):
    drow(ws,i,list(range(1,7)),list(r),LGR if i%2==0 else WHT)
wb3.save(BASE+"08_FINANCIAL_REPORTING/Financial_Dashboard.xlsx")
print("  ✓ 08_FINANCIAL_REPORTING/Financial_Dashboard.xlsx")

print("✓ 09_BUSINESS_OPERATIONS complete")

# ── 10_NOTION_WORKSPACE — CSVs ────────────────────────────────────────────────
write_csv("10_NOTION_WORKSPACE/Clients_Database.csv",
    ["Client Name","Owner","Email","Phone","Entity Type","Industry","Services","Monthly Fee","Software","Status","Start Date","CPA Contact"],
    [
        ["Joe's Plumbing","Joe Morales","joe@joes.com","555-0101","LLC","Plumbing","Bookkeeping + Payroll","$650","QuickBooks","Active","Jan 2024","[CPA]"],
        ["Riverdale Cafe","Maria Chen","maria@rcafe.com","555-0102","S-Corp","Restaurant","Bookkeeping","$600","Xero","Active","Jan 2024","[CPA]"],
        ["Green Lawn LLC","Brian Park","brian@green.com","555-0103","LLC","Landscaping","Bookkeeping","$350","QuickBooks","Active","Dec 2023","[CPA]"],
        ["StyleHouse Salon","Amy Wu","amy@style.com","555-0104","Sole Prop","Beauty","Bookkeeping","$300","Wave","Onboarding","Jan 2024","None"],
        ["BuildRight Co","Tom Davis","tom@build.com","555-0105","S-Corp","Construction","Bookkeeping + Job Costing","$800","QuickBooks","Active","Nov 2023","[CPA]"],
    ])

write_csv("10_NOTION_WORKSPACE/Tasks_Database.csv",
    ["Task","Client","Category","Priority","Due Date","Status","Notes"],
    [
        ["Complete December reconciliation","Joe's Plumbing","Monthly Close","High","Jan 15","In Progress","Bank feeds connected"],
        ["Deliver January report","Riverdale Cafe","Report Delivery","High","Jan 20","To Do","",""],
        ["Send Q4 estimated tax calculation","BuildRight Co","Tax","High","Jan 15","To Do","Coordinate with CPA"],
        ["Request missing receipt — Dec 28","Green Lawn LLC","Document Request","Medium","Jan 12","To Do","$340 Home Depot charge"],
        ["Set up chart of accounts","StyleHouse Salon","Onboarding","High","Jan 14","In Progress","Review categories"],
        ["Send 1099s","All Clients","Tax","Urgent","Jan 31","To Do","Check vendor list for each client"],
        ["Post LinkedIn content","Marketing","Marketing","Low","Jan 17","To Do","Tax tip post"],
    ])

write_csv("10_NOTION_WORKSPACE/Monthly_Deadlines_Database.csv",
    ["Deadline","Client","Type","Due Date","Status","Notes"],
    [
        ["January Close — Joe's Plumbing","Joe's Plumbing","Monthly Close","Jan 20","In Progress",""],
        ["January Close — Riverdale Cafe","Riverdale Cafe","Monthly Close","Jan 15","Complete","Delivered Jan 14"],
        ["January Close — Green Lawn LLC","Green Lawn LLC","Monthly Close","Jan 20","In Progress",""],
        ["January Close — BuildRight Co","BuildRight Co","Monthly Close","Jan 20","In Progress",""],
        ["Q4 941 Filing","All Payroll Clients","Payroll Tax","Jan 31","To Do","Gusto handles automatically"],
        ["1099-NEC to Contractors","All Clients","Tax","Jan 31","To Do","Review each client vendor list"],
        ["W-2s to Employees","Joe's Plumbing, BuildRight Co","Payroll Tax","Jan 31","To Do","Via Gusto"],
        ["Q1 Estimated Taxes","BuildRight Co","Tax","Apr 15","Upcoming","Calculate by Mar 31"],
    ])

write_csv("10_NOTION_WORKSPACE/Document_Requests_Database.csv",
    ["Document Needed","Client","Date Requested","Date Received","Status","Notes"],
    [
        ["Receipt for $340 Home Depot Dec 28","Green Lawn LLC","Jan 11","","Pending","Asked via email"],
        ["December bank statement — checking","StyleHouse Salon","Jan 10","Jan 12","Received",""],
        ["Q4 payroll summary from Gusto","Joe's Plumbing","Jan 5","Jan 5","Received","Auto-downloaded"],
        ["Year-end loan statement — equipment loan","BuildRight Co","Jan 8","","Pending","Follow up Jan 15"],
        ["W-9 for new subcontractor — ABC Electric","BuildRight Co","Dec 20","Dec 22","Received","1099 required"],
    ])

write_csv("10_NOTION_WORKSPACE/Services_Database.csv",
    ["Service","Description","Standard Price","Pricing Basis","Add-On Notes"],
    [
        ["Monthly Bookkeeping — Starter","Up to 100 transactions, 1–2 accounts, P&L + Balance Sheet","$200–$400","Per month",""],
        ["Monthly Bookkeeping — Growth","101–300 transactions, 2–4 accounts, all standard reports","$400–$750","Per month",""],
        ["Monthly Bookkeeping — Established","301–600 transactions, 4–6 accounts, payroll coordination","$750–$1,200","Per month",""],
        ["Payroll Processing","Payroll processing for 1–5 employees; federal and state filing","$50–$150","Per month","$15–$25 per additional employee"],
        ["Sales Tax Filing","Prepare and file state sales tax return","$75–$150","Per filing per state",""],
        ["Quarterly Estimated Taxes","Calculate and document quarterly estimates","$100–$200","Per quarter",""],
        ["Catch-Up Bookkeeping","Bring books current for prior months","1.5–2x monthly rate","Per month of backlog",""],
        ["Year-End Close Coordination","Year-end close and CPA coordination","$200–$500","Annual",""],
        ["1099 Preparation","Prepare and file 1099-NEC for contractors","$50/form + $100 base","Per form",""],
        ["CFO Advisory Services","Monthly financial review, KPI reporting, strategy","$500–$2,000","Per month",""],
    ])

write_csv("10_NOTION_WORKSPACE/SOP_Library.csv",
    ["SOP Name","Category","Version","Last Updated","Owner","Summary"],
    [
        ["Monthly Bookkeeping SOP","Bookkeeping","v1.0","Jan 2024","[Owner]","Full monthly close process from transaction import to report delivery"],
        ["Bank Reconciliation SOP","Bookkeeping","v1.0","Jan 2024","[Owner]","Step-by-step reconciliation with discrepancy resolution"],
        ["Payroll Processing SOP","Payroll","v1.0","Jan 2024","[Owner]","Pre-payroll through tax filing and bookkeeping entry"],
        ["Client Onboarding SOP","Operations","v1.0","Jan 2024","[Owner]","Day-by-day process from signed agreement to first report"],
        ["Tax Season SOP","Tax","v1.0","Jan 2024","[Owner]","January through April tax season workflow and deadlines"],
        ["Year-End Close SOP","Tax","v1.0","Jan 2024","[Owner]","December actions and January close procedures"],
    ])

write_csv("10_NOTION_WORKSPACE/Database_Field_Map.csv",
    ["Database","Field Name","Field Type","Description"],
    [
        ["Clients","Status","Select","Prospect / Onboarding / Active / Paused / Churned"],
        ["Clients","Services","Multi-Select","Bookkeeping / Payroll / Sales Tax / Tax Prep / CFO Advisory"],
        ["Tasks","Priority","Select","Low / Medium / High / Urgent"],
        ["Tasks","Category","Select","Monthly Close / Report Delivery / Tax / Payroll / Onboarding / Marketing"],
        ["Monthly Deadlines","Status","Select","Upcoming / In Progress / Complete / Overdue"],
        ["Document Requests","Status","Select","Pending / Received / Not Required"],
        ["Services","Pricing Basis","Select","Per month / Per filing / Per form / Annual / Per quarter"],
        ["SOP Library","Version","Text","v1.0, v1.1, v2.0 etc."],
    ])

# Notion Setup MD
with open(BASE+"10_NOTION_WORKSPACE/NOTION_WORKSPACE_SETUP.md","w",encoding="utf-8") as f:
    f.write("""# Bookkeeping Business Notion Workspace Setup

## Overview
Your Notion workspace organizes every aspect of your bookkeeping practice — from client management to monthly deadlines, document tracking, and SOP library.

---

## Top-Level Pages to Create

| Page Name | Icon | Purpose |
|---|---|---|
| 👥 Clients | People | All client accounts and service details |
| ✅ Tasks | Checkbox | Daily and weekly task management |
| 📅 Monthly Deadlines | Calendar | Track every close and filing deadline |
| 📄 Document Requests | Folder | Track outstanding documents per client |
| 🛠 Services | Gear | Your service menu and pricing |
| 📚 SOP Library | Book | All operating procedures |
| 📊 Dashboard | Chart | Linked view of key items across all databases |

---

## Step 1 — Import CSV Files

1. Open Notion → New Page → Import → CSV
2. Upload each file:
   - `Clients_Database.csv`
   - `Tasks_Database.csv`
   - `Monthly_Deadlines_Database.csv`
   - `Document_Requests_Database.csv`
   - `Services_Database.csv`
   - `SOP_Library.csv`
3. Rename each imported page to match the table above.

---

## Step 2 — Set Up Database Relations

- **Tasks ↔ Clients**: Every task linked to a client (or "Internal" for non-client work)
- **Monthly Deadlines ↔ Clients**: Each deadline linked to a specific client
- **Document Requests ↔ Clients**: Track outstanding documents by client

---

## Step 3 — Recommended Views

### Clients Database
- **Table view**: All clients sorted by start date
- **Filter: Active**: Show only Status = Active
- **Gallery view**: Quick visual overview

### Tasks Database
- **Board view**: Group by Priority (Urgent / High / Medium / Low)
- **Calendar view**: By Due Date
- **Filter: This Week**: Due Date = this week

### Monthly Deadlines
- **Calendar view**: By Due Date — visual close schedule
- **Filter: In Progress**: Status = In Progress or Upcoming
- **Sort: Due Date ascending**: See what's due soonest

---

## Step 4 — Build Your Dashboard Page

Create a Dashboard page with these linked database views:
- Overdue tasks (filter: Due Date < today, Status ≠ Complete)
- In-progress deadlines (filter: Status = In Progress)
- Outstanding document requests (filter: Status = Pending)
- Clients due for monthly report this week

---

## Step 5 — Monthly Close Workflow in Notion

1. Start of month: Tasks auto-populate via template (set up recurring task template)
2. Daily: Update task status as work is completed
3. Mid-month: Check Monthly Deadlines calendar; send any outstanding Document Requests
4. By delivery date: Mark deadline as Complete; log delivery date in Clients database
""")
print("  ✓ 10_NOTION_WORKSPACE/NOTION_WORKSPACE_SETUP.md")

print("PART 3 DONE")
