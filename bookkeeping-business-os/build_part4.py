"""Bookkeeping Business OS — Part 4: Bonuses (365 CSV + DOCX) + PDFs + PPTX + Manifest + ZIP"""
import os, csv, json, zipfile
from docx import Document
from docx.shared import Pt, RGBColor
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import cm
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor as PRGB
from pptx.enum.text import PP_ALIGN

BASE = "/home/user/oqul-phase55-production/bookkeeping-business-os/Ultimate_Bookkeeping_Business_Operating_System/"

NAV_RGB=(15,52,96); ACC_RGB=(233,69,96); GLD_RGB=(245,166,35)
GRN_RGB=(39,174,96); WHT_RGB=(255,255,255); LGR_RGB=(248,249,250)
PNAV=PRGB(15,52,96); PACC=PRGB(233,69,96); PGLD=PRGB(245,166,35)
PGRN=PRGB(39,174,96); PWHT=PRGB(255,255,255)

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

# ── 365 CAPTIONS ──────────────────────────────────────────────────────────────
categories = {
    "Education": [
        "The difference between profit and cash flow — and why both matter for your business.",
        "What your Profit & Loss statement actually tells you (and what it doesn't).",
        "Bank reconciliation explained in plain English. No accounting degree required.",
        "Why your Balance Sheet is the most underrated financial report in your business.",
        "Accounts Receivable vs. Accounts Payable: what they are and why they matter.",
        "The chart of accounts: the backbone of every bookkeeping system.",
        "Gross profit vs. net profit: know the difference before your next pricing decision.",
        "What is a journal entry? The basics every business owner should understand.",
        "Cash basis vs. accrual accounting: which one is right for your business?",
        "Understanding depreciation: why your equipment isn't worth what you paid for it.",
        "What is COGS and how does it affect your margins?",
        "The 3 financial statements every business owner should review monthly.",
        "How to read your Profit & Loss statement in 5 minutes.",
        "What 'net 30' payment terms actually mean and how they affect your cash flow.",
        "The difference between a bookkeeper and a CPA — and when you need each.",
        "Why categorizing transactions correctly matters more than you think.",
        "Sales tax 101: when you need to collect it and what happens if you don't.",
        "What is an operating expense vs. a capital expense?",
        "How your accounting software connects to your bank — and why that matters.",
        "The most commonly missed tax deductions for small business owners.",
        "What is a 1099 and who needs to receive one from you?",
        "Opening balance equity: what it is and why you need to resolve it.",
        "How to track business mileage correctly for maximum deduction.",
        "What is a break-even analysis and how can it improve your pricing?",
        "EBITDA explained: why investors care about it and whether you should.",
        "How to calculate your profit margin and whether it's healthy for your industry.",
        "What are accruals and why do accountants love them?",
        "Fixed vs. variable costs: understanding your business cost structure.",
        "Why you should never mix personal and business finances.",
        "What happens if you don't file taxes on time? The penalties explained.",
    ],
    "Tax Tips": [
        "Quarterly estimated taxes: what they are and how to calculate them simply.",
        "The home office deduction: who qualifies and how to calculate it correctly.",
        "Vehicle deductions: the standard mileage rate vs. actual expenses method.",
        "Section 179: how to deduct the full cost of equipment in year one.",
        "Meal deductions: what's 50% deductible and what's 100% deductible.",
        "The QBI deduction (Section 199A): a significant tax break many owners miss.",
        "How to deduct your health insurance premiums as a self-employed business owner.",
        "Retirement accounts for self-employed owners: SEP-IRA vs. SIMPLE IRA vs. Solo 401(k).",
        "What is the Augusta Rule and can your business use it?",
        "Self-employment tax: what it is, how much it is, and how to reduce it.",
        "Should you form an S-Corp? The math behind the decision.",
        "Travel deductions: what qualifies and what documentation you need.",
        "The gift deduction limit and how to maximize it without crossing the line.",
        "Starting a business this year? Here are the startup costs you can deduct.",
        "How bonus depreciation works and whether it makes sense for your situation.",
        "What is a reasonable salary for an S-Corp owner? This matters more than you think.",
        "Charitable contributions from a business: what's deductible and how to record it.",
        "The pass-through deduction: a quick explanation for LLC and S-Corp owners.",
        "Bad debt deductions: when and how to write off uncollectible invoices.",
        "Education and training expenses: when they're deductible for your business.",
        "How to handle mixed-use assets (personal and business) on your taxes.",
        "Internet and phone deductions: what percentage you can actually claim.",
        "The carry-forward net operating loss: how losses this year can reduce future taxes.",
        "Why your tax return and your P&L don't always match (and why that's normal).",
        "Business insurance premiums: which ones are deductible.",
        "Software subscriptions and SaaS tools: fully deductible business expenses.",
        "The tax implications of owner draws vs. salary in different entity types.",
        "How to handle a 1099-K from Stripe, PayPal, or Square at tax time.",
        "What to do if you missed a quarterly estimated tax payment.",
        "Year-end tax planning moves every small business owner should consider.",
    ],
    "Cash Flow": [
        "Profitable on paper. Broke in the bank. This is the cash flow gap — and it's fixable.",
        "Your cash runway is your business survival metric. Do you know yours?",
        "Sending invoices on the same day you deliver the work: the fastest way to improve cash flow.",
        "Net 15 vs. Net 30 vs. Net 60: the payment terms that matter most for your cash.",
        "How to negotiate better payment terms with vendors to protect your cash flow.",
        "A business line of credit is best set up before you need it, not after.",
        "The easiest cash flow improvement: stop waiting to invoice. Bill the same day.",
        "Cash flow forecasting: how to predict shortfalls 30–60 days before they happen.",
        "Why a 10% profit margin business can still run out of cash.",
        "Days Sales Outstanding (DSO): the metric that shows how fast your clients pay.",
        "If your AR is over 30 days overdue, your cash flow problem has a name: collections.",
        "Recurring revenue businesses have better cash flow visibility than project businesses. Here's why.",
        "The biggest cash flow mistake seasonal businesses make — and how to avoid it.",
        "How to create a simple 13-week cash flow forecast in a spreadsheet.",
        "Prepayments from clients: the ultimate cash flow tool for service businesses.",
        "Understanding the difference between the cash method and accrual method for cash planning.",
        "Cash flow vs. revenue: why a $500K business can still miss payroll.",
        "The 3 levers of cash flow improvement: collect faster, pay slower, spend smarter.",
        "Retainer agreements create predictable monthly cash — here's how to propose one.",
        "Late payment fees: are you using them? Should you?",
        "How inventory management directly impacts your cash flow.",
        "Owner's draw timing: how to take money from your business without hurting cash flow.",
        "Emergency fund for businesses: how much cash should you keep in reserve?",
        "The 'cash conversion cycle' and why it matters for product businesses.",
        "How to stop subsidizing your clients' cash flow with your own.",
        "Subscription billing: the cash flow model that changed SaaS businesses. Can it work for yours?",
        "Why growth can destroy cash flow — and what to do about it.",
        "The payment terms conversation every freelancer and service provider should have.",
        "Setting up an operating account and a tax savings account: a simple cash management strategy.",
        "Cash flow review: the one monthly habit that gives business owners peace of mind.",
    ],
    "Bookkeeping Tips": [
        "Reconcile your books every month. Catching a $50 error now is better than a $5,000 surprise at tax time.",
        "Keep your business and personal finances completely separate. Always.",
        "Your accounting software is only as good as the data you put in it.",
        "The 3 documents every bookkeeper needs to do their job: bank statements, receipts, context.",
        "Cloud accounting software connects your bank feeds — manual data entry is 2015.",
        "Photo your receipts immediately. Receipt Bank, Dext, or just your camera roll. Before you lose them.",
        "Every expense needs a category and a purpose. 'Miscellaneous' is not a category.",
        "QuickBooks, Xero, or Wave? For most small businesses, any of these is better than a spreadsheet.",
        "Year-end bookkeeping is infinitely easier when your books are clean all year.",
        "Your chart of accounts should match your business — not a generic template.",
        "Running a business on your personal bank account will cost you more in taxes and accounting fees.",
        "What does a bookkeeper actually do? A day-in-the-life breakdown.",
        "The difference between 'cleaning up your books' and 'keeping clean books.'",
        "Your bookkeeper needs timely responses. Delays in document requests = delays in your reports.",
        "What's a bank feed and why should every business owner care?",
        "Owner's draws are not a business expense. Record them correctly or your tax return will be wrong.",
        "Transfer entries in QuickBooks: why they're different from expenses and how to record them.",
        "The golden rule of bookkeeping: every transaction has two sides.",
        "Why credit card payments should never be recorded as expenses.",
        "What is payroll reconciliation and why does it matter?",
        "Vendor bills vs. expenses: knowing the difference keeps your AP clean.",
        "How to handle a refund in your accounting software — the right way.",
        "Opening a business bank account: what you need and what to look for.",
        "Accounts receivable aging: the report that tells you who owes you what — and for how long.",
        "What a clean set of books actually looks like at year-end.",
        "How to record owner contributions to the business correctly.",
        "The monthly bookkeeping checklist every business owner should have.",
        "What is a retained earnings account and why does it matter?",
        "Why your bookkeeper and CPA should be communicating directly (with your permission).",
        "The one bookkeeping habit that saves business owners thousands per year: categorize weekly, not annually.",
    ],
    "Engagement": [
        "What's the most confusing financial term in your business? I'll explain it.",
        "Honest question: how current are your books right now? 30 days? 6 months? Let's talk.",
        "What's the biggest financial surprise you've had in your business? I'll go first.",
        "Poll: Do you know your profit margin off the top of your head? Yes / No / Getting there",
        "Hot take: the majority of small business tax bills are higher than they need to be. Agree?",
        "What financial report do you check most often — or do you avoid looking altogether?",
        "Be honest: are you doing your own bookkeeping? How many hours a month is it taking you?",
        "What would you do with 10 extra hours a month? (Because that's what clean systems can give you.)",
        "If you could instantly know one number about your business right now, what would it be?",
        "What's the best financial advice you've ever received for your business?",
        "What's the worst financial mistake you made in your first year of business?",
        "Do you know your break-even point? Drop your industry below and I'll share what it typically looks like.",
        "What's the one financial thing you wish you understood better?",
        "If I could fix one thing about your finances today, what would it be?",
        "What's your current least favorite part of running your business financially?",
        "How confident are you in your financials going into tax season? 1–10?",
        "What's a common belief about bookkeeping that you've found to be wrong?",
        "Small business owners: what did you not expect about managing money when you started?",
        "What would give you the most peace of mind about your business finances?",
        "For every bookkeeper in my network: what's the most common mistake you see clients make?",
    ],
    "Social Proof": [
        "A restaurant owner came to me with 8 months of unreconciled books. We found $4,200 in uncategorized deductions. Clean books pay for themselves.",
        "A client was paying $900/month in duplicate software subscriptions. We caught it on the first reconciliation.",
        "First year working together: client's CPA said 'these are the cleanest books I've seen.' That's the goal.",
        "We helped a contractor understand his true job margins for the first time. He dropped his 3 least profitable clients and increased revenue.",
        "A client called panicked about a tax notice. Because their books were current, we had the answer in 20 minutes.",
        "Client switched from DIY bookkeeping to our service. Saved 8 hours/month. Got $3,100 back at tax time. Decision made.",
        "Year two with a growing e-commerce client: revenue doubled and we scaled the system with them.",
        "A new client had been running their business on a personal bank account for 3 years. We untangled it. Then we gave them a clean financial picture for the first time.",
        "An S-Corp client was paying herself too much salary. After our review and CPA consult: $7,000 in payroll tax savings annually.",
        "Client goal: understand their numbers enough to make a hiring decision. Within 60 days: they hired.",
        "A cash-based business (salon) didn't know their daily revenue. We built a system. Now they track it to the hour.",
        "Year-end close finished in one week this year. Because their books were clean all year.",
        "A client's previous bookkeeper left their books in chaos. We completed a 14-month clean-up in 6 weeks.",
        "Landed a bank loan. The lender said the clean financials made the decision easy.",
        "Client started our relationship stressed. Three months in: 'I finally feel in control of my business.'",
    ],
    "Authority": [
        "I've reconciled hundreds of business bank accounts. Here's the most common mistake I see.",
        "After [X] years in bookkeeping, here's what I know distinguishes businesses that thrive financially.",
        "The 3 financial reports I always review before making any recommendation to a client.",
        "The onboarding question I ask every new client that changes how I set up their books.",
        "Why I specialize in [industry] bookkeeping — and what it means for my clients.",
        "My process for catching tax deductions that clients didn't know they had.",
        "The one thing I always check first when a client asks 'why don't my numbers make sense.'",
        "How I explain cash flow to clients who never studied accounting — and why it clicks.",
        "Why I recommend monthly reconciliations over quarterly — and the data behind it.",
        "What I've learned about [industry] bookkeeping that you won't find in a textbook.",
        "The question every business owner should be able to answer before making a major purchase.",
        "The tax deduction conversation I have with every client at year-end.",
        "My take on the QuickBooks vs. Xero debate for [industry] businesses.",
        "Why every bookkeeper should specialize in a niche — from someone who learned the hard way.",
        "What 'closing the books' actually involves — and why it takes longer than clients expect.",
    ],
    "Lead Generation": [
        "Is your bookkeeper delivering monthly reports by the 15th? If not, your books might not be as clean as you think.",
        "Behind on your books? I specialize in catch-up bookkeeping. DM me and let's get you current before tax season.",
        "Do you know your profit margin? If not, let's fix that. I offer a complimentary 20-minute financial review.",
        "I have one monthly client slot available for a [industry] business. Interested? DM me this week.",
        "Tax season is [X months] away. Are your books ready? I can tell you in 15 minutes.",
        "Small business owner managing your own books? I can probably take that off your plate for less than you'd expect.",
        "I specialize in bookkeeping for [industry] businesses. If that's you, I'd love to connect.",
        "New business owner? The best time to set up clean books is month one. Let me help you start right.",
        "I'm accepting [X] new monthly bookkeeping clients this quarter. If you're interested, reply here.",
        "What if your financial reports were ready by the 15th of every month — without you lifting a finger?",
        "Free resource: my [Month] [Industry] Bookkeeping Checklist. DM me 'checklist' and I'll send it over.",
        "Do you have a bookkeeper but aren't sure they're doing a good job? I offer a second-opinion review.",
        "Moving from DIY to professional bookkeeping? I'll make the transition seamless. DM me.",
        "Running your business on spreadsheets? Let me show you a better way in a 20-minute call.",
        "Every month you're doing your own books is a month you're not running your business. Let's change that.",
    ],
    "Myth Busting": [
        "Myth: 'I only need a bookkeeper at tax time.' Truth: Good bookkeeping is year-round. Tax time is just when you see the results.",
        "Myth: 'I can just do it myself in QuickBooks.' Truth: You can. But miscategorizations add up — and often cost more in taxes than a bookkeeper's fee.",
        "Myth: 'My accountant does my bookkeeping.' Truth: Most CPAs do taxes. Bookkeeping is a separate, ongoing service.",
        "Myth: 'Bookkeeping is just data entry.' Truth: It's data entry + categorization + reconciliation + analysis. Very different things.",
        "Myth: 'I'll clean up my books before tax season.' Truth: If you have a year of transactions to review, 'clean up' takes weeks and costs extra.",
        "Myth: 'I don't make enough to need a bookkeeper.' Truth: The less you make, the more you need to track every dollar.",
        "Myth: 'My business is too small.' Truth: A business with any transactions needs records. There is no 'too small.'",
        "Myth: 'All bookkeepers are the same.' Truth: Specialization matters enormously. A bookkeeper who knows your industry catches things generalists miss.",
        "Myth: 'If I use QuickBooks, I'm fine.' Truth: QuickBooks is a tool. Without accurate inputs and reconciliation, it produces inaccurate reports.",
        "Myth: 'Bookkeepers and CPAs are in competition.' Truth: Great bookkeepers and CPAs work as a team. Clean books make tax prep faster and cheaper.",
        "Myth: 'I can wait until I'm more established.' Truth: The 'I'll get organized later' approach is exactly how businesses end up with 2 years of catch-up work.",
        "Myth: 'I know my numbers because I watch my bank account.' Truth: Your bank balance is not your profit. You need a P&L for that.",
        "Myth: 'A bookkeeper just files my taxes.' Truth: Bookkeepers don't file taxes. We keep records accurate so tax filing is fast and accurate.",
        "Myth: 'The IRS doesn't audit small businesses.' Truth: Small businesses with home offices, high cash usage, and certain deductions are audited regularly.",
        "Myth: 'I have nothing to hide, so I don't need organized books.' Truth: Audits aren't about hiding — they're about documentation. No documentation = failed audit.",
    ],
    "Seasonal": [
        "January: Is your year-end close on your calendar? It should be.",
        "January: 1099s go out by January 31. Have you checked your contractor list?",
        "February: Tax documents are arriving. Set up a folder now — digital or physical.",
        "February: If your books aren't reconciled through December, now is the time to catch up.",
        "March: Filing deadline is approaching. Clean books make CPA work faster (and cheaper).",
        "April 15: Last day to file (or extend). Have you taken care of your quarterly estimates?",
        "April: Q1 estimated tax payment is due. Did you calculate yours?",
        "May: Off-season for tax season but peak season for catching up on Q1 books.",
        "June: Q2 estimated taxes due June 15. Set a calendar alert now.",
        "June: Mid-year financial review: are you on track for the year? Pull your YTD P&L.",
        "July: Half the year is gone. Where do you stand against your annual goals?",
        "July: Q2 tax return due for Q2 payments. File or extend by July 31 (Form 941).",
        "August: Now is the time to review your expense categories before the year gets away from you.",
        "September: Q3 estimated taxes due September 15. Are you on track?",
        "October: Start thinking about year-end. What purchases should you make before December 31?",
        "November: Year-end planning season. Talk to your bookkeeper and CPA before December.",
        "December: Any equipment you want to depreciate must be placed in service by December 31.",
        "December: Review your 1099 vendor list now. W-9s need to be collected before year-end.",
        "December 31: Last day to make retirement contributions, deductible purchases, and record charitable donations.",
        "Year-round: The one habit that makes every tax season easy — reconcile every month.",
    ],
}

rows = []
n = 1
all_cats = list(categories.keys())
while n <= 365:
    cat = all_cats[(n-1) % len(all_cats)]
    captions = categories[cat]
    caption = captions[(n-1) // len(all_cats) % len(captions)]
    rows.append([str(n), cat, caption, "#bookkeeping #smallbusiness #accounting #taxes #cashflow"])
    n += 1

with open(BASE+"11_BONUSES/365_Bookkeeping_Content_Captions.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["Day","Category","Caption","Hashtags"]); w.writerows(rows)
print("  ✓ 11_BONUSES/365_Bookkeeping_Content_Captions.csv")

doc("11_BONUSES/100_Bookkeeping_Content_Ideas.docx",
    "100 Bookkeeping Content Ideas",
    "Bookkeeping Business Operating System | Bonuses",
    [
        ("EDUCATION (1–30)", [
            ("•","1. What is a Profit & Loss statement and how to read it"),
            ("•","2. What is a Balance Sheet and what does it tell you"),
            ("•","3. Cash flow vs. profit: why they're different and both important"),
            ("•","4. The chart of accounts: what it is and how to set it up right"),
            ("•","5. Gross profit margin explained with a real example"),
            ("•","6. What does 'reconciling your books' actually mean"),
            ("•","7. Cash basis vs. accrual basis: which one to use for your business"),
            ("•","8. The 3 financial statements every business owner must understand"),
            ("•","9. QuickBooks vs. Xero vs. Wave: which is right for your business"),
            ("•","10. What is accounts receivable and why does it matter"),
            ("•","11. What is accounts payable and how to manage it"),
            ("•","12. Owner's draw vs. salary: what you need to know"),
            ("•","13. What is depreciation and why it reduces your taxable income"),
            ("•","14. Fixed vs. variable costs: understanding your expense structure"),
            ("•","15. What does a bookkeeper actually do day-to-day"),
            ("•","16. Bookkeeper vs. CPA: the difference and when you need each"),
            ("•","17. What is a 1099 and who needs to send/receive one"),
            ("•","18. How to track business mileage for tax purposes"),
            ("•","19. The home office deduction: who qualifies and how to calculate it"),
            ("•","20. What is COGS and how it affects your pricing"),
            ("•","21. How to calculate break-even for your business"),
            ("•","22. What is retained earnings and why does it matter"),
            ("•","23. How bank reconciliation catches fraud and errors"),
            ("•","24. What is a journal entry (simplified for non-accountants)"),
            ("•","25. Why separating personal and business finances is non-negotiable"),
            ("•","26. What is a cash flow statement"),
            ("•","27. How to read an accounts receivable aging report"),
            ("•","28. The most commonly miscategorized expenses in small business"),
            ("•","29. What happens if you don't file taxes on time"),
            ("•","30. Sales tax 101: when to collect it and what to do with it"),
        ]),
        ("TAX TIPS (31–55)", [
            ("•","31. The 20 most commonly missed deductions for small business owners"),
            ("•","32. Quarterly estimated taxes: how to calculate them simply"),
            ("•","33. Should you form an S-Corp? The math made simple"),
            ("•","34. Vehicle deductions: standard mileage vs. actual expenses"),
            ("•","35. Section 179 explained: deduct equipment costs immediately"),
            ("•","36. How to deduct your health insurance as a self-employed owner"),
            ("•","37. Solo 401(k) vs. SEP-IRA: which retirement account is better"),
            ("•","38. The QBI deduction: what it is and how to qualify"),
            ("•","39. How to handle a 1099-K from PayPal or Stripe at tax time"),
            ("•","40. Travel deductions: what qualifies and what documentation you need"),
            ("•","41. Year-end tax moves to make before December 31"),
            ("•","42. The self-employment tax: what it is and how to reduce it"),
            ("•","43. Business meal deductions: 50% or 100% — how to know"),
            ("•","44. Can you deduct your phone and internet? Yes — here's how"),
            ("•","45. How to handle an IRS notice (without panicking)"),
            ("•","46. What is bonus depreciation and when to use it"),
            ("•","47. The Augusta Rule: rent your home to your business tax-free"),
            ("•","48. Reasonable compensation for S-Corp owners: what it means"),
            ("•","49. How to deduct start-up costs in your first year"),
            ("•","50. What is a Net Operating Loss and can it save you taxes next year"),
            ("•","51. Education deductions: when they're business expenses"),
            ("•","52. Charitable contributions from your business: what's deductible"),
            ("•","53. The carry-forward loss: how this year's losses can offset future taxes"),
            ("•","54. What to do if you missed your estimated tax payment"),
            ("•","55. Year-end review: the financial checklist for December"),
        ]),
        ("CASH FLOW & GROWTH (56–75)", [
            ("•","56. Cash flow forecasting: a simple spreadsheet method"),
            ("•","57. How to improve cash flow without getting a loan"),
            ("•","58. Days Sales Outstanding: the KPI that tells you how fast clients pay"),
            ("•","59. How to negotiate better payment terms with vendors"),
            ("•","60. Retainer pricing: how recurring revenue changes your business"),
            ("•","61. The 3 levers of cash flow: collect faster, pay slower, spend smarter"),
            ("•","62. When to use a business line of credit"),
            ("•","63. The cash conversion cycle explained with a simple example"),
            ("•","64. How seasonal businesses should manage cash reserves"),
            ("•","65. Revenue vs. cash: why profitable businesses still run out of money"),
            ("•","66. The client payment terms conversation you need to have"),
            ("•","67. Why owner draws should be planned, not spontaneous"),
            ("•","68. How to price for profit, not just to stay busy"),
            ("•","69. When to hire: the financial signals that tell you you're ready"),
            ("•","70. How to build a simple 90-day cash flow forecast"),
            ("•","71. The financial preparation before approaching a bank for a loan"),
            ("•","72. How to calculate if a price increase is financially justified"),
            ("•","73. The minimum cash reserve every business should maintain"),
            ("•","74. How to track KPIs specific to your industry"),
            ("•","75. Profitable on paper, broke in the bank: how this happens and how to fix it"),
        ]),
        ("ENGAGEMENT & STORIES (76–100)", [
            ("•","76. The strangest thing I've ever seen in a client's books"),
            ("•","77. A day in the life of a bookkeeper during tax season"),
            ("•","78. The question clients ask that tells me they're ready to grow"),
            ("•","79. Why I became a bookkeeper and what keeps me here"),
            ("•","80. The client win I'll never forget"),
            ("•","81. My biggest mistake in my bookkeeping career and what it taught me"),
            ("•","82. The financial habit that separates thriving businesses from struggling ones"),
            ("•","83. What I wish business owners knew before they came to me"),
            ("•","84. The most common financial stress I see — and how we solve it"),
            ("•","85. How a client went from 'I don't know my numbers' to 'I love my reports'"),
            ("•","86. Behind the scenes: what closing the books actually looks like"),
            ("•","87. The tool I couldn't do my job without"),
            ("•","88. What it means to give a small business owner financial peace of mind"),
            ("•","89. The first time a client saw a clean P&L: what they said"),
            ("•","90. Why I specialize in [niche] bookkeeping and what it changes"),
            ("•","91. The tax deduction I found that paid for my services 3x over"),
            ("•","92. What financial clarity does for a business owner beyond the money"),
            ("•","93. The question I start every discovery call with"),
            ("•","94. How my bookkeeping process protects my clients in an audit"),
            ("•","95. What good books actually look like — and how to get there"),
            ("•","96. The moment I knew a client was going to succeed"),
            ("•","97. 3 financial red flags I look for in a new client's books"),
            ("•","98. How I helped a client stop losing money without knowing it"),
            ("•","99. The report no one looks at — but should"),
            ("•","100. What financial freedom means for a small business owner"),
        ]),
    ])

doc("11_BONUSES/Bookkeeper_Success_Framework.docx",
    "Bookkeeper Success Framework",
    "Bookkeeping Business Operating System | Bonuses",
    [
        ("THE 5 PILLARS OF A SUCCESSFUL BOOKKEEPING BUSINESS", []),
        ("PILLAR 1 — TECHNICAL EXCELLENCE", [
            ("•","Master your accounting software (QuickBooks ProAdvisor, Xero Certified, or Wave Advisor)"),
            ("•","Understand tax fundamentals (you don't prepare taxes, but you must understand implications)"),
            ("•","Stay current on regulation changes that affect your clients (payroll, sales tax, 1099 rules)"),
            ("•","Build industry-specific knowledge for your niche clients"),
        ]),
        ("PILLAR 2 — SYSTEMS AND PROCESSES", [
            ("•","Document every process — your SOP library is your most valuable asset"),
            ("•","Build repeatable workflows that allow you to scale or delegate"),
            ("•","Use project management tools to track every client's monthly close"),
            ("•","Automate where possible: bank feeds, recurring invoices, automated reminders"),
        ]),
        ("PILLAR 3 — CLIENT RELATIONSHIPS", [
            ("•","Deliver reports on time, every time — reliability is your product"),
            ("•","Communicate proactively, not just reactively"),
            ("•","Educate clients to understand their numbers — educated clients stay longer"),
            ("•","Anticipate needs: flag a cash flow concern before they ask about it"),
        ]),
        ("PILLAR 4 — BUSINESS DEVELOPMENT", [
            ("•","Your best clients come from referrals — build a referral system intentionally"),
            ("•","Niche down: specializing in one industry makes you more referable and more valuable"),
            ("•","Content marketing: 3 posts per week on LinkedIn builds authority and inbound leads"),
            ("•","CPA partnerships: your most powerful referral channel — nurture them"),
        ]),
        ("PILLAR 5 — FINANCIAL MANAGEMENT OF YOUR OWN BUSINESS", [
            ("•","Track your own MRR, client count, and churn monthly"),
            ("•","Price for value — your pricing should reflect the time and expertise invested"),
            ("•","Reinvest in tools, training, and systems before hiring"),
            ("•","Separate your business and personal finances (yes, bookkeepers make this mistake too)"),
        ]),
        ("MONTHLY SELF-ASSESSMENT", [
            "Rate yourself 1–10 on each pillar:",
            ("•","Technical Excellence: ___/10"),
            ("•","Systems and Processes: ___/10"),
            ("•","Client Relationships: ___/10"),
            ("•","Business Development: ___/10"),
            ("•","Own Financial Management: ___/10"),
        ]),
    ])

doc("11_BONUSES/Bookkeeping_Business_Growth_Roadmap.docx",
    "Bookkeeping Business Growth Roadmap",
    "Bookkeeping Business Operating System | Bonuses",
    [
        ("STAGE 1 — LAUNCH ($0–$3,000 MRR)", [
            ("•","Get QuickBooks ProAdvisor or Xero Certified (free through their programs)"),
            ("•","Define your niche: 1–2 industries you'll specialize in"),
            ("•","Set up your legal entity, bank account, and service agreement"),
            ("•","First 3 clients: offer a discounted rate in exchange for a testimonial"),
            ("•","Build your portfolio and social proof"),
            ("•","Target: 5–10 clients at $300–$400/month = $1,500–$4,000 MRR"),
        ]),
        ("STAGE 2 — GROW ($3,000–$10,000 MRR)", [
            ("•","Raise prices on new clients — $400–$750/month is achievable with specialization"),
            ("•","Build your referral network: 3–5 CPA partnerships"),
            ("•","Launch content marketing: LinkedIn 3x/week"),
            ("•","Add first add-on service: payroll or quarterly estimates"),
            ("•","Consider your first hire: virtual bookkeeping assistant"),
            ("•","Target: 15–25 clients averaging $500/month"),
        ]),
        ("STAGE 3 — SCALE ($10,000–$30,000 MRR)", [
            ("•","Hire 1–2 bookkeepers to handle client work"),
            ("•","Add premium advisory/CFO service tier"),
            ("•","Build automated client portal and reporting workflow"),
            ("•","Develop team training system and quality control process"),
            ("•","Add a second niche or geographic market"),
            ("•","Target: 40–80 clients; team of 3–5; revenues of $120K–$360K/year"),
        ]),
        ("STAGE 4 — LEAD ($30,000+ MRR)", [
            ("•","Operations manager to run day-to-day client delivery"),
            ("•","Become a thought leader in your niche through speaking, content, or certifications"),
            ("•","Consider acquiring smaller bookkeeping books of business"),
            ("•","Offer white-label services to CPAs and financial advisors"),
            ("•","Target: $500K+ annual revenue; systemized team"),
        ]),
        ("KEY MILESTONES TO CELEBRATE", [
            ("•","First paying client"),
            ("•","First $1,000 MRR"),
            ("•","First $5,000 MRR"),
            ("•","First team hire"),
            ("•","First $10,000 MRR"),
            ("•","First $100K year"),
        ]),
    ])

print("✓ 11_BONUSES complete")

# ── PDFs ──────────────────────────────────────────────────────────────────────
def make_pdf(path, title, sections):
    d = SimpleDocTemplate(path, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    NAV_C = colors.Color(15/255,52/255,96/255)
    ACC_C = colors.Color(233/255,69/255,96/255)
    title_style = ParagraphStyle('T',parent=styles['Normal'],fontSize=20,textColor=NAV_C,
        spaceAfter=6,fontName='Helvetica-Bold')
    h1_style = ParagraphStyle('H1',parent=styles['Normal'],fontSize=13,textColor=NAV_C,
        spaceAfter=4,spaceBefore=14,fontName='Helvetica-Bold')
    body_style = ParagraphStyle('B',parent=styles['Normal'],fontSize=10,spaceAfter=4,leading=14)
    bullet_style = ParagraphStyle('BU',parent=styles['Normal'],fontSize=10,spaceAfter=3,
        leading=14,leftIndent=15,bulletIndent=5)
    story=[Paragraph(title,title_style),HRFlowable(width="100%",thickness=2,color=ACC_C,spaceAfter=10)]
    for heading,items in sections:
        story.append(Paragraph(heading,h1_style))
        for item in items:
            if item.startswith('• '):
                story.append(Paragraph(item,bullet_style))
            else:
                story.append(Paragraph(item,body_style))
    d.build(story)
    print(f"  ✓ {os.path.relpath(path,BASE)}")

make_pdf(BASE+"00_START_HERE/START_HERE_Implementation_Guide.pdf",
    "Ultimate Bookkeeping Business Operating System — Implementation Guide",
    [
        ("WELCOME",[
            "Congratulations on your investment in the Ultimate Bookkeeping Business Operating System. This guide walks you through implementation in a logical sequence so you can use every resource from day one.",
        ]),
        ("WHAT'S INCLUDED",[
            "• 01_CLIENT_ACQUISITION — Cold outreach, discovery call script, proposal template, follow-up sequence, objection handling, pricing guide, BD CRM",
            "• 02_CLIENT_ONBOARDING — Welcome emails, intake form, kickoff script, service agreement, onboarding SOP, tracker",
            "• 03_BOOKKEEPING_SERVICES — Monthly bookkeeping SOP, chart of accounts guide, bank reconciliation SOP, AP and AR SOPs",
            "• 04_PAYROLL_SERVICES — Payroll processing SOP, compliance checklist, new employee setup, troubleshooting guide",
            "• 05_TAX_PREPARATION — Tax season SOP, document checklist, quarterly estimates guide, year-end close checklist",
            "• 06_CLIENT_COMMUNICATION — Monthly report emails, difficult conversation scripts, client Q&A scripts, newsletter templates",
            "• 07_COMPLIANCE_LEGAL — Service agreement, engagement letter, data security policy, confidentiality policy, legal guide",
            "• 08_FINANCIAL_REPORTING — Monthly report template, cash flow guide, KPI reporting guide, review meeting script, dashboard",
            "• 09_BUSINESS_OPERATIONS — Goals workbook, team management, training manual, KPI dashboard",
            "• 10_NOTION_WORKSPACE — 6 databases, setup guide, Notion MD, import-ready CSVs",
            "• 11_BONUSES — 365 captions, 100 content ideas, success framework, growth roadmap",
            "• 12_CANVA_IMPORTABLE_TEMPLATES — 4 PPTX Canva templates (Proposal, Monthly Report, Tax Checklist, Social Pack)",
        ]),
        ("IMPLEMENTATION SEQUENCE",[
            "Week 1 — Legal Foundation: Customize 07_COMPLIANCE_LEGAL documents. Have attorney review before use.",
            "Week 2 — Client Acquisition: Customize 01_CLIENT_ACQUISITION templates. Begin outreach. Set up Client_Acquisition_CRM.xlsx.",
            "Week 3 — Onboarding Ready: Customize 02_CLIENT_ONBOARDING docs. Set up Notion workspace from 10_NOTION_WORKSPACE.",
            "Week 4 — Operations Live: Use 03–05 SOPs for all service delivery. Track KPIs in 09 dashboards.",
            "Ongoing — Growth: Post 3x/week on LinkedIn using 11_BONUSES captions. Deliver reports with 06 email templates.",
        ]),
        ("CANVA IMPORT INSTRUCTIONS",[
            "• Go to canva.com → Create a design → Import file",
            "• Upload the .pptx file from 12_CANVA_IMPORTABLE_TEMPLATES",
            "• Canva converts it to an editable design automatically",
            "• Replace colors, fonts, and content with your brand",
        ]),
        ("PRICING REFERENCE",[
            "• Original Price: €149  |  Launch Price: €39",
            "Note: Tax and financial content is educational only. Consult a licensed CPA for jurisdiction-specific advice.",
        ]),
    ])

make_pdf(BASE+"07_COMPLIANCE_LEGAL/Legal_Template_Use_Guide.pdf",
    "Legal Template Use Guide — Bookkeeping Business OS",
    [
        ("IMPORTANT NOTICE",[
            "The legal documents in this system are generic educational templates. They do not constitute legal advice. Have a qualified attorney review before commercial use.",
        ]),
        ("DOCUMENTS INCLUDED",[
            "• Service_Agreement_Template.docx — Full contract covering services, fees, liability, termination",
            "• Engagement_Letter_Template.docx — Shorter alternative for simpler client relationships",
            "• Confidentiality_Policy.docx — Internal policy for protecting client financial data",
            "• Data_Security_Policy.docx — Procedures for securing sensitive client information",
        ]),
        ("KEY CUSTOMIZATION STEPS",[
            "1. Replace all [bracketed placeholders] with your specific information",
            "2. Review fee amounts, payment terms, and guarantee language",
            "3. Confirm governing law matches your state",
            "4. Have a licensed attorney review before signing with any client",
            "5. Store signed copies securely — 7-year retention recommended",
        ]),
        ("IMPORTANT DISCLAIMERS",[
            "• You are a bookkeeper, not a tax professional — be clear about scope",
            "• Never provide tax advice — refer clients to their CPA for tax questions",
            "• Errors & Omissions (E&O) insurance is strongly recommended",
            "• Review your state's licensing requirements for bookkeeping services",
        ]),
    ])

make_pdf(BASE+"10_NOTION_WORKSPACE/Notion_Workspace_Setup_Guide.pdf",
    "Notion Workspace Setup Guide — Bookkeeping Business OS",
    [
        ("OVERVIEW",[
            "Your Notion workspace keeps every client, deadline, task, and document request organized in one place — accessible from any device, always current.",
        ]),
        ("DATABASES INCLUDED",[
            "• Clients_Database.csv — All client accounts, services, fees, and software",
            "• Tasks_Database.csv — Daily and recurring task management",
            "• Monthly_Deadlines_Database.csv — Track every close and filing deadline",
            "• Document_Requests_Database.csv — Outstanding documents per client",
            "• Services_Database.csv — Your service menu and pricing guide",
            "• SOP_Library.csv — All your standard operating procedures",
        ]),
        ("IMPORT STEPS",[
            "1. Open Notion → New Page → Import → CSV",
            "2. Upload each CSV file and rename to match the page names",
            "3. Open NOTION_WORKSPACE_SETUP.md for relation and view setup",
            "4. Build your Dashboard page with linked views for today's tasks, deadlines, and pending documents",
        ]),
        ("RECOMMENDED FIRST WEEK SETUP",[
            "• Day 1: Import all 6 databases",
            "• Day 2: Create relations between Tasks, Clients, and Monthly Deadlines",
            "• Day 3: Set up board view for Tasks (grouped by Priority)",
            "• Day 4: Set up calendar view for Monthly Deadlines",
            "• Day 5: Build your Dashboard page with linked views",
        ]),
    ])

print("✓ PDFs done")

# ── PPTX CANVA TEMPLATES ──────────────────────────────────────────────────────
def new_prs():
    prs=Presentation(); prs.slide_width=Inches(13.33); prs.slide_height=Inches(7.5); return prs
def blank(prs): return prs.slides.add_slide(prs.slide_layouts[6])
def rect(sl,l,t,w,h,r,g,b):
    sh=sl.shapes.add_shape(1,Inches(l),Inches(t),Inches(w),Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=PRGB(r,g,b); sh.line.fill.background(); return sh
def txt(sl,text,l,t,w,h,sz=18,bold=False,color=PWHT,align=PP_ALIGN.LEFT):
    tb=sl.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(h))
    tf=tb.text_frame; tf.word_wrap=True
    p=tf.paragraphs[0]; p.alignment=align
    run=p.add_run(); run.text=text
    run.font.size=PPt(sz); run.font.bold=bold; run.font.color.rgb=color
def line(sl,l,t,w):
    ln=sl.shapes.add_shape(1,Inches(l),Inches(t),Inches(w),Inches(0.04))
    ln.fill.solid(); ln.fill.fore_color.rgb=PACC; ln.line.fill.background()

# 1. Client Proposal
prs=new_prs()
sl=blank(prs)
rect(sl,0,0,13.33,7.5,*NAV_RGB); rect(sl,0,0,4.5,7.5,*GRN_RGB)
txt(sl,"BOOKKEEPING PROPOSAL",5,1.5,8,0.8,34,True,PWHT)
txt(sl,"[Client Business Name]",5,2.5,8,0.6,22,False,PWHT)
txt(sl,"Prepared by [Your Business Name]  |  [Date]",5,3.2,8,0.5,13,False,PRGB(180,180,180))
txt(sl,"Clean Books.\nAccurate Reports.\nPeace of Mind.",0.3,2.5,3.9,2,20,True,PWHT)

sl=blank(prs)
rect(sl,0,0,13.33,7.5,*LGR_RGB); rect(sl,0,0,13.33,1.2,*NAV_RGB)
txt(sl,"YOUR BOOKKEEPING CHALLENGES",0.4,0.25,12,0.7,22,True,PWHT)
items=[("Too many hours on bookkeeping","Time you can't spend growing your business"),
       ("Unclear financial picture","You don't always know your profit or cash position"),
       ("Tax season surprises","Unexpected bills because books weren't current"),
       ("CPA overcharging","Messy books mean higher accounting fees")]
for i,(prob,impact) in enumerate(items):
    y=1.4+i*1.3
    rect(sl,0.4,y,6,1.1,*NAV_RGB); rect(sl,6.8,y,6,1.1,*WHT_RGB)
    txt(sl,prob,0.55,y+0.2,5.7,0.7,13,True,PWHT)
    txt(sl,impact,6.95,y+0.2,5.7,0.7,12,False,PRGB(50,50,50))

sl=blank(prs)
rect(sl,0,0,13.33,7.5,*NAV_RGB); rect(sl,0,0,13.33,1.2,*GRN_RGB)
txt(sl,"WHAT'S INCLUDED IN YOUR PLAN",0.4,0.25,12,0.7,22,True,PWHT)
services=["Monthly bank & credit card reconciliation",
    "Monthly Profit & Loss Statement","Monthly Balance Sheet",
    "Plain-English financial summary","Year-end CPA coordination",
    "Priority email support"]
for i,s in enumerate(services):
    x=0.4+(i%2)*6.5; y=1.5+(i//2)*1.5
    rect(sl,x,y,6,1.2,*PRGB(*ACC_RGB).__class__(*ACC_RGB))
    txt(sl,f"✓  {s}",x+0.2,y+0.3,5.6,0.6,13,False,PWHT)

sl=blank(prs)
rect(sl,0,0,13.33,7.5,*LGR_RGB); rect(sl,0,0,13.33,1.2,*NAV_RGB)
txt(sl,"INVESTMENT & NEXT STEPS",0.4,0.25,12,0.7,22,True,PWHT)
rect(sl,0.4,1.4,5.5,5,*NAV_RGB)
txt(sl,"YOUR PLAN",0.6,1.7,5,0.5,14,True,PWHT)
txt(sl,"[Starter / Growth / Established]",0.6,2.3,5,0.5,16,True,PGLD)
txt(sl,"$[X]/month",0.6,3.0,5,0.8,32,True,PWHT)
txt(sl,"• Bank reconciliation\n• P&L + Balance Sheet\n• Monthly summary\n• [Add-ons]",0.6,3.9,5,1.5,12,False,PRGB(180,200,220))
rect(sl,6.3,1.4,6.6,5,*WHT_RGB)
txt(sl,"NEXT STEPS",6.5,1.7,6.2,0.5,14,True,PNAV)
for i,(num,step) in enumerate([("1","Sign the Engagement Letter"),
    ("2","Complete the Client Intake Form"),("3","Grant software access"),
    ("4","Kickoff call — scope + delivery date"),("5","First reports by [date]")],0):
    y=2.3+i*0.85
    rect(sl,6.5,y,0.6,0.6,*NAV_RGB)
    txt(sl,num,6.55,y+0.08,0.5,0.4,13,True,PWHT,PP_ALIGN.CENTER)
    txt(sl,step,7.3,y+0.08,5.3,0.5,12,False,PRGB(50,50,50))

prs.save(BASE+"12_CANVA_IMPORTABLE_TEMPLATES/Canva_Import_Client_Proposal.pptx")
print("  ✓ 12_CANVA_IMPORTABLE_TEMPLATES/Canva_Import_Client_Proposal.pptx")

# 2. Monthly Financial Report
prs=new_prs()
sl=blank(prs)
rect(sl,0,0,13.33,7.5,*NAV_RGB); rect(sl,9.5,0,3.83,7.5,*GRN_RGB)
txt(sl,"MONTHLY\nFINANCIAL\nREPORT",0.5,1.2,8.5,2.5,44,True,PWHT)
txt(sl,"[Month] [Year]",0.5,3.9,8.5,0.7,22,False,PWHT)
txt(sl,"[Client Business Name]",0.5,4.6,8.5,0.5,16,False,PRGB(180,200,220))
txt(sl,"Prepared by [Your Business Name]",9.7,6.5,3.3,0.5,11,False,PWHT)

sl=blank(prs)
rect(sl,0,0,13.33,7.5,*LGR_RGB); rect(sl,0,0,13.33,1.2,*NAV_RGB)
txt(sl,"EXECUTIVE SUMMARY — [Month] [Year]",0.4,0.25,12,0.7,20,True,PWHT)
kpis=[("Revenue","$[X]","[+/-X]% vs last month"),("Expenses","$[X]","[+/-X]% vs last month"),
      ("Net Profit","$[X]","[X]% margin"),("Cash Balance","$[X]","As of [date]")]
for i,(label,val,note) in enumerate(kpis):
    x=0.4+i*3.2
    rect(sl,x,1.5,2.9,2.5,*NAV_RGB)
    txt(sl,label,x+0.2,1.7,2.5,0.4,12,True,PRGB(180,200,220))
    txt(sl,val,x+0.2,2.1,2.5,0.8,26,True,PWHT)
    txt(sl,note,x+0.2,3.0,2.5,0.5,11,False,PRGB(180,200,220))
txt(sl,"KEY OBSERVATIONS",0.4,4.2,12.5,0.4,13,True,PNAV)
for i,obs in enumerate(["[Observation 1 — revenue driver or trend]",
    "[Observation 2 — notable expense change]","[Observation 3 — cash or AR note]"],0):
    txt(sl,f"• {obs}",0.4,4.8+i*0.65,12.5,0.5,12,False,PRGB(50,50,50))

sl=blank(prs)
rect(sl,0,0,13.33,7.5,*NAV_RGB); rect(sl,0,0,13.33,1.2,*GRN_RGB)
txt(sl,"INCOME & EXPENSE BREAKDOWN",0.4,0.25,12,0.7,20,True,PWHT)
txt(sl,"TOP INCOME SOURCES",0.4,1.4,6,0.4,13,True,PGLD)
for i,row in enumerate([("[Income Category 1]","$[X]","[X]%"),
    ("[Income Category 2]","$[X]","[X]%"),("[Income Category 3]","$[X]","[X]%")],0):
    y=2.0+i*0.8
    rect(sl,0.4,y,5.5,0.65,*PRGB(*ACC_RGB).__class__(*ACC_RGB))
    txt(sl,row[0],0.6,y+0.12,3,0.4,11,False,PWHT)
    txt(sl,row[1],3.7,y+0.12,1.2,0.4,11,True,PWHT)
    txt(sl,row[2],5.0,y+0.12,0.8,0.4,11,False,PGLD)
txt(sl,"TOP EXPENSES",7,1.4,6,0.4,13,True,PGLD)
for i,row in enumerate([("[Expense Category 1]","$[X]","[X]%"),
    ("[Expense Category 2]","$[X]","[X]%"),("[Expense Category 3]","$[X]","[X]%")],0):
    y=2.0+i*0.8
    rect(sl,7,y,6,0.65,*PRGB(20,80,120).__class__(20,80,120))
    txt(sl,row[0],7.2,y+0.12,3.3,0.4,11,False,PWHT)
    txt(sl,row[1],10.5,y+0.12,1.2,0.4,11,True,PWHT)
    txt(sl,row[2],11.8,y+0.12,0.8,0.4,11,False,PGLD)
txt(sl,"GROSS MARGIN: [X]%   |   NET MARGIN: [X]%",0.4,5.8,12.5,0.6,16,True,PGLD)

sl=blank(prs)
rect(sl,0,0,13.33,7.5,*LGR_RGB); rect(sl,0,0,13.33,1.2,*NAV_RGB)
txt(sl,"ACTION ITEMS & NEXT STEPS",0.4,0.25,12,0.7,22,True,PWHT)
for i,(label,item) in enumerate([
    ("ACTION NEEDED","[Specific action required from client, if any]"),
    ("WATCH ITEM","[Item to monitor — e.g., expense trending up]"),
    ("UPCOMING","[e.g., Q2 estimated tax due June 15 — approx $[X]]"),
    ("NEXT REPORT","[Date] — covering [Month+1]")],0):
    y=1.5+i*1.3
    rect(sl,0.4,y,3,1.1,*NAV_RGB); rect(sl,3.6,y,9.3,1.1,*WHT_RGB)
    txt(sl,label,0.55,y+0.25,2.7,0.5,12,True,PWHT)
    txt(sl,item,3.75,y+0.25,9,0.6,12,False,PRGB(50,50,50))

prs.save(BASE+"12_CANVA_IMPORTABLE_TEMPLATES/Canva_Import_Monthly_Report.pptx")
print("  ✓ 12_CANVA_IMPORTABLE_TEMPLATES/Canva_Import_Monthly_Report.pptx")

# 3. Tax Season Checklist (client-facing)
prs=new_prs()
sl=blank(prs)
rect(sl,0,0,13.33,7.5,*NAV_RGB); rect(sl,0,5,13.33,2.5,*ACC_RGB)
txt(sl,"TAX SEASON\nCHECKLIST",0.7,1.0,11,2,52,True,PWHT)
txt(sl,"Everything you need to gather before your tax appointment.",0.7,3.2,11,0.6,16,False,PRGB(180,200,220))
txt(sl,"[Your Business Name]  |  Prepared for [Client Name]",0.7,5.2,11,0.5,14,False,PWHT)

sl=blank(prs)
rect(sl,0,0,13.33,7.5,*LGR_RGB); rect(sl,0,0,13.33,1.2,*NAV_RGB)
txt(sl,"INCOME DOCUMENTS",0.4,0.25,12,0.7,22,True,PWHT)
docs=[("Form W-2","From any employer where you had taxes withheld"),
      ("Form 1099-NEC","Nonemployee compensation received"),
      ("Form 1099-K","Payment card income: Stripe, PayPal, Square"),
      ("Form 1099-INT","Bank interest income"),
      ("Any other income","Cash income, rental income, investment sales")]
for i,(label,desc) in enumerate(docs):
    y=1.4+i*1.1
    rect(sl,0.4,y,0.5,0.85,*GRN_RGB)
    txt(sl,"□",0.45,y+0.15,0.4,0.5,20,True,PWHT,PP_ALIGN.CENTER)
    txt(sl,label,1.1,y+0.05,3.5,0.4,13,True,PNAV)
    txt(sl,desc,1.1,y+0.5,11.8,0.3,11,False,PRGB(80,80,80))

sl=blank(prs)
rect(sl,0,0,13.33,7.5,*NAV_RGB); rect(sl,0,0,13.33,1.2,*ACC_RGB)
txt(sl,"EXPENSE RECORDS & SUPPORTING DOCUMENTS",0.4,0.25,12,0.7,18,True,PWHT)
expense_docs=[("Receipts for major purchases","Equipment, assets over $500"),
    ("Vehicle mileage log","Business miles driven and purpose"),
    ("Home office details","Square footage of office and total home"),
    ("Business loan statements","Year-end balances as of Dec 31"),
    ("Prior year tax return","All pages — speeds up tax prep significantly")]
for i,(label,desc) in enumerate(expense_docs):
    y=1.5+i*1.1
    rect(sl,0.4,y,0.5,0.85,*PGLD.__class__(*GLD_RGB))
    txt(sl,"□",0.45,y+0.15,0.4,0.5,20,True,PNAV,PP_ALIGN.CENTER)
    txt(sl,label,1.1,y+0.05,3.5,0.4,13,True,PWHT)
    txt(sl,desc,1.1,y+0.5,11.8,0.3,11,False,PRGB(180,200,220))

prs.save(BASE+"12_CANVA_IMPORTABLE_TEMPLATES/Canva_Import_Tax_Season_Checklist.pptx")
print("  ✓ 12_CANVA_IMPORTABLE_TEMPLATES/Canva_Import_Tax_Season_Checklist.pptx")

# 4. Social Post Pack
prs=new_prs()
posts=[
    ("MYTH","Bookkeeping is just data entry.","It's reconciliation, categorization, analysis, and clean reporting. The data entry is 20% of the work.",NAV_RGB),
    ("TAX TIP","Quarterly taxes are due 4 times a year.","Jan 15 · Apr 15 · Jun 15 · Sep 15. Missing them costs you. Save the dates.",ACC_RGB),
    ("FACT","A profitable business can still run out of cash.","Profit and cash flow are different numbers. Know both.",NAV_RGB),
    ("CHECKLIST","Year-end tax prep: get ready now.","✓ Reconcile all accounts\n✓ Collect contractor W-9s\n✓ Review deductions\n✓ Calculate estimates",ACC_RGB),
    ("QUESTION","What's your biggest financial headache as a business owner?","Drop it in the comments. I'll answer everyone.",NAV_RGB),
    ("TIP","Send invoices the same day you deliver the work.","The #1 easiest cash flow improvement. No new tools required.",ACC_RGB),
    ("CLIENT WIN","8 months of messy books. Cleaned in 6 weeks.","Found $4,200 in uncategorized deductions. Clean books pay for themselves.",NAV_RGB),
    ("CTA","Ready for clean books by the 15th every month?","DM me. I have [X] client slots open this quarter.",ACC_RGB),
]
for label,headline,body,bg in posts:
    sl=blank(prs)
    rect(sl,0,0,13.33,7.5,*bg)
    opp_rgb=ACC_RGB if bg==NAV_RGB else NAV_RGB
    rect(sl,0,0,13.33,1.2,*opp_rgb)
    txt(sl,label,0.4,0.25,12,0.7,14,True,PWHT)
    txt(sl,headline,0.5,1.5,12.3,1.5,30,True,PWHT)
    txt(sl,body,0.5,3.4,12.3,3,16,False,PRGB(200,220,240))
    txt(sl,"[Your Business Name]  |  #bookkeeping #smallbusiness #taxes",0.5,6.8,12.3,0.4,11,False,PRGB(150,170,190))

prs.save(BASE+"12_CANVA_IMPORTABLE_TEMPLATES/Canva_Import_Social_Post_Pack.pptx")
print("  ✓ 12_CANVA_IMPORTABLE_TEMPLATES/Canva_Import_Social_Post_Pack.pptx")
print("✓ PPTX done")

# ── MANIFEST + ZIP ────────────────────────────────────────────────────────────
all_files=[]
for root,dirs,files in os.walk(BASE):
    for fn in sorted(files):
        rel=os.path.relpath(os.path.join(root,fn),BASE)
        folder=rel.split(os.sep)[0]
        ext=fn.rsplit('.',1)[-1].upper()
        all_files.append((rel,folder,ext))
all_files.sort(key=lambda x:x[0])

with open(BASE+"00_START_HERE/Asset_Manifest.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    w.writerow(["File Path","Folder","Format","Editable In"])
    fmt={"DOCX":"Microsoft Word / Google Docs","XLSX":"Excel / Google Sheets","PDF":"View only",
         "CSV":"Excel / Google Sheets / Notion","PPTX":"Upload to Canva / PowerPoint",
         "MD":"Notion / Text Editor","TXT":"Any text editor","JSON":"Any text editor"}
    for rel,folder,ext in all_files:
        w.writerow([rel,folder,ext,fmt.get(ext,ext)])

with open(BASE+"00_START_HERE/Asset_Manifest.json","w") as f:
    json.dump({"product":"Ultimate Bookkeeping Business Operating System","version":"1.0",
        "total_files":len(all_files),"folders":13,
        "pricing":{"original":"€149","launch":"€39"},
        "formats":list(set(e for _,_,e in all_files)),
        "files":[{"path":r,"folder":fo,"format":e} for r,fo,e in all_files]},f,indent=2)
print(f"  ✓ Manifest: {len(all_files)} files")

zip_path="/home/user/oqul-phase55-production/bookkeeping-business-os/BUYER_DOWNLOAD_BookkeepingBusinessOS.zip"
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as zf:
    for root,dirs,files in os.walk(BASE):
        for fn in files:
            fp=os.path.join(root,fn)
            arc=os.path.relpath(fp,os.path.dirname(BASE))
            zf.write(fp,arc)
size_mb=os.path.getsize(zip_path)/1024/1024
print(f"\n✅ ZIP: {zip_path}")
print(f"   Size: {size_mb:.1f} MB | Files: {len(all_files)}")
