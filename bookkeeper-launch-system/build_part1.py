import os, csv, json, zipfile
from docx import Document
from docx.shared import Pt, RGBColor

BASE = "/home/user/oqul-phase55-production/bookkeeper-launch-system/Ultimate_Bookkeeper_Launch_System/"

# ── Folder structure ──────────────────────────────────────────────────────────
FOLDERS = [
    "00_START_HERE",
    "01_BUSINESS_SETUP",
    "02_TECH_STACK_SETUP",
    "03_PRICING_PACKAGING",
    "04_CLIENT_ACQUISITION",
    "05_CLIENT_ONBOARDING",
    "06_SERVICE_DELIVERY",
    "07_CLIENT_COMMUNICATION",
    "08_BUSINESS_OPERATIONS",
    "09_GROWTH_SCALING",
    "10_NOTION_WORKSPACE",
    "11_BONUSES",
    "12_CANVA_IMPORTABLE_TEMPLATES",
]

for folder in FOLDERS:
    os.makedirs(BASE + folder, exist_ok=True)
print("✓ All folders created")


# ── Helper: build a .docx ─────────────────────────────────────────────────────
def doc(filename, title, subtitle, sections):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x0F, 0x34, 0x60)
    if subtitle:
        s = d.add_paragraph(subtitle); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10)
        s.runs[0].font.color.rgb = RGBColor(0x7F, 0x8C, 0x8D)
    d.add_paragraph("")
    for section in sections:
        if isinstance(section, str):
            d.add_paragraph(section)
            continue
        heading, items = section
        h = d.add_heading(heading, level=1)
        h.runs[0].font.color.rgb = RGBColor(0x0F, 0x34, 0x60)
        for item in items:
            if isinstance(item, tuple) and item[0] == '•':
                d.add_paragraph(item[1], style='List Bullet')
            else:
                d.add_paragraph(str(item))
    d.save(BASE + filename)
    print(f"  ✓ {filename}")


# ═══════════════════════════════════════════════════════════════════════════════
# 00_START_HERE
# ═══════════════════════════════════════════════════════════════════════════════

# -- README_FIRST.txt ----------------------------------------------------------
readme_text = """\
╔══════════════════════════════════════════════════════════════════════════════╗
║       ULTIMATE BOOKKEEPER PRACTICE LAUNCH SYSTEM — WELCOME                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

Welcome! You now have everything you need to launch a profitable, professional
bookkeeping practice from scratch — or rapidly scale the one you already have.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT'S INCLUDED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  00_START_HERE               You are here. Read this first.
  01_BUSINESS_SETUP           Legal entity, brand, bank accounts, insurance.
  02_TECH_STACK_SETUP         Software selection, chart of accounts, tools.
  03_PRICING_PACKAGING        Service packages, value pricing, proposals.
  04_CLIENT_ACQUISITION       Outreach scripts, LinkedIn, referral systems.
  05_CLIENT_ONBOARDING        Engagement letters, welcome kits, kick-off calls.
  06_SERVICE_DELIVERY         Monthly close process, SOP library, QC checklists.
  07_CLIENT_COMMUNICATION     Email templates, meeting agendas, report delivery.
  08_BUSINESS_OPERATIONS      Capacity planning, billing, contractor hiring.
  09_GROWTH_SCALING           Niche strategy, referral partners, team building.
  10_NOTION_WORKSPACE         Pre-built Notion templates for your entire firm.
  11_BONUSES                  Scripts, swipe files, discovery call framework.
  12_CANVA_IMPORTABLE_TEMPLATES  Branded proposal, welcome packet, report covers.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOW TO USE THIS SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  STEP 1 — Read Product_Overview.docx in this folder for the full roadmap.
  STEP 2 — Open Quick_Start_Checklist.docx and work through Week 1 tasks.
  STEP 3 — Follow folders 01 → 12 in order. Each folder is one phase.
  STEP 4 — Customize every template with your name, logo, and pricing.
  STEP 5 — Use the Notion workspace (10_NOTION_WORKSPACE) to manage clients.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUICK START — YOUR FIRST 7 DAYS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Day 1  — Decide: LLC or sole proprietor? (See 01_BUSINESS_SETUP)
  Day 2  — Register your business name; open a business bank account.
  Day 3  — Sign up for QuickBooks Online Accountant (free for you as a ProAdvisor).
  Day 4  — Define your three service packages and set your pricing.
  Day 5  — Set up your LinkedIn profile using the brand guide.
  Day 6  — Send your first five outreach messages using the scripts in 04.
  Day 7  — Review, adjust, and book time for Week 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMPORTANT NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  • All templates are starting points — customize every document before use.
  • Pricing ranges are market benchmarks; adjust for your local market.
  • Nothing in this system constitutes legal or tax advice. Consult a licensed
    attorney and CPA for your specific situation.
  • This system is updated periodically. Check the version date on each doc.

                    Version 1.0 — Built for bookkeepers, by bookkeepers.
"""

os.makedirs(BASE + "00_START_HERE", exist_ok=True)
with open(BASE + "00_START_HERE/README_FIRST.txt", "w") as f:
    f.write(readme_text)
print("  ✓ 00_START_HERE/README_FIRST.txt")


# -- Quick_Start_Checklist.docx ------------------------------------------------
doc(
    "00_START_HERE/Quick_Start_Checklist.docx",
    "Quick Start Checklist — Bookkeeper Practice Launch System",
    "Complete each section in order. Check off items as you finish them.",
    [
        ("WEEK 1 — Business Setup", [
            "Goal: Your business is legally formed and branded by end of this week.",
            ('•', "Choose your business structure (LLC vs. sole proprietor) — see Business_Registration_Checklist.docx"),
            ('•', "Select and verify your business name (check state registry + Google + USPTO trademark search)"),
            ('•', "Register your LLC with your state (typical cost: $50–$500 depending on state)"),
            ('•', "Apply for your EIN (Employer Identification Number) at IRS.gov — free and instant online"),
            ('•', "Open a dedicated business checking account (do NOT commingle personal and business funds)"),
            ('•', "Apply for a business credit card for trackable expenses"),
            ('•', "Purchase professional liability (E&O) insurance — budget $500–$1,500/year"),
            ('•', "Purchase a bookkeeper's bond ($10,000 bond typically costs $100–$150/year)"),
            ('•', "Set up your business email address (G Suite / Google Workspace recommended)"),
            ('•', "Secure your social media handles: LinkedIn, Facebook Business, Instagram (even if unused now)"),
            ('•', "Create a simple one-page business plan using the template in 01_BUSINESS_SETUP"),
        ]),
        ("WEEK 2 — Tech Stack Setup", [
            "Goal: Your core software is live and configured.",
            ('•', "Sign up for QuickBooks Online Accountant (QBOA) — free ProAdvisor account at quickbooks.intuit.com/accountants"),
            ('•', "Complete QuickBooks ProAdvisor certification (free; takes 6–8 hours; gives you a badge and leads from Intuit)"),
            ('•', "Sign up for Xero Partner program (free practice account + 30% commission on referrals)"),
            ('•', "Choose your practice management tool: Keeper, Financial Cents, or Jetpack Workflow (all have free trials)"),
            ('•', "Set up Toggl Track or Harvest for time tracking (even on fixed-fee work, track time for 90 days)"),
            ('•', "Configure your email signature with your name, credentials, phone, and website/LinkedIn"),
            ('•', "Set up a simple invoicing system (use QBO or FreshBooks to send your own invoices)"),
            ('•', "Create a standard folder structure on Google Drive or SharePoint for client documents"),
            ('•', "Set up LastPass or 1Password for secure password management"),
            ('•', "Download and configure the Chart of Accounts template from 02_TECH_STACK_SETUP"),
        ]),
        ("WEEK 3 — Pricing & Packages", [
            "Goal: You know exactly what you're selling and at what price.",
            ('•', "Read the Service Packages Guide in 03_PRICING_PACKAGING — understand the three-tier model"),
            ('•', "Read the Value Pricing Guide — shift your mindset from hourly billing to monthly retainers"),
            ('•', "Set your Starter package price (suggested: $300–$500/mo for 1-2 bank accounts, up to 150 transactions)"),
            ('•', "Set your Professional package price (suggested: $700–$1,200/mo adds payroll + AP/AR)"),
            ('•', "Set your Premium package price (suggested: $1,500–$2,500/mo full advisory/CFO-lite)"),
            ('•', "Create your proposal template using the Canva file in 12_CANVA_IMPORTABLE_TEMPLATES"),
            ('•', "Write a one-paragraph 'bookkeeping elevator pitch' — what you do and who you help"),
            ('•', "Practice your discovery call script from 11_BONUSES at least three times out loud"),
            ('•', "Decide: will you specialize in a niche? (e.g., restaurants, real estate, e-commerce, law firms)"),
            ('•', "Set your capacity goal: how many clients can you serve at launch? (Recommended: start with 3–5)"),
        ]),
        ("WEEK 4 — First Client Outreach", [
            "Goal: At least 5 discovery calls booked.",
            ('•', "Optimize your LinkedIn profile: professional headshot, clear headline ('Bookkeeper for [Niche] Businesses'), About section with your value proposition"),
            ('•', "Connect with 20 small business owners in your target niche on LinkedIn — personalized connection requests only"),
            ('•', "Send the 'warm outreach' email to 10 people in your existing network (friends, family, former colleagues)"),
            ('•', "Join 2–3 local business Facebook groups and introduce yourself (no spam — provide value first)"),
            ('•', "Register with your local Chamber of Commerce and attend one networking event"),
            ('•', "Reach out to 3 CPAs in your area about a referral partnership (you refer tax clients to them; they refer bookkeeping clients to you)"),
            ('•', "Post your first LinkedIn article: 'Top 3 Bookkeeping Mistakes I See Small Businesses Make'"),
            ('•', "Set up a simple Calendly link for discovery calls (free plan is sufficient)"),
            ('•', "Book your first discovery call — use the script in 11_BONUSES"),
            ('•', "After every discovery call: send a proposal within 24 hours using your template"),
        ]),
        ("ONGOING OPERATIONS — Monthly Rhythm", [
            "Goal: Deliver excellent work consistently; grow methodically.",
            ('•', "Monthly close checklist: run every client through the SOP in 06_SERVICE_DELIVERY by the 10th of each month"),
            ('•', "Invoice all clients on the 1st of each month (or upon contract — net 3 or net 7 is standard for bookkeeping)"),
            ('•', "Send monthly financial summary email to every client using template in 07_CLIENT_COMMUNICATION"),
            ('•', "Schedule a 30-minute quarterly review call with each client (upsell opportunity)"),
            ('•', "Update your capacity tracker in Notion — know when you're ready for the next client"),
            ('•', "Set aside 1 hour/week for continuing education (new QBO features, tax law changes, industry news)"),
            ('•', "Send one referral request per month to your happiest client"),
            ('•', "Track revenue, expenses, and net income monthly — you are your own best client"),
            ('•', "Review and adjust pricing annually — raise rates by 5–10% each year minimum"),
        ]),
    ]
)


# -- Product_Overview.docx -----------------------------------------------------
doc(
    "00_START_HERE/Product_Overview.docx",
    "Product Overview — Ultimate Bookkeeper Practice Launch System",
    "A complete guide to every folder, every file, and how to use this system.",
    [
        ("ABOUT THIS SYSTEM", [
            "The Ultimate Bookkeeper Practice Launch System is a step-by-step operational framework for launching or scaling a professional bookkeeping practice. Every document, template, checklist, and script inside has been built around what actually works for solo bookkeepers and small bookkeeping firms.",
            "The system is organized into 13 folders that follow the natural sequence of building a practice: legal formation → technology → pricing → marketing → client delivery → growth. You can work through them in order, or jump to the section most relevant to your current stage.",
        ]),
        ("FOLDER 00 — START HERE", [
            "Contents: README_FIRST.txt, Quick_Start_Checklist.docx, Product_Overview.docx",
            "Purpose: Orient yourself in the system. The Quick Start Checklist gives you a 4-week action plan with daily tasks. Read the README before opening anything else.",
        ]),
        ("FOLDER 01 — BUSINESS SETUP", [
            "Contents: Business_Registration_Checklist.docx, Business_Plan_Template.docx, Brand_Identity_Guide.docx",
            "Purpose: Build the legal and brand foundation of your practice. Covers LLC formation, EIN, insurance, business banking, naming your firm, logo, and brand colors. Complete this folder before spending money on software or marketing.",
        ]),
        ("FOLDER 02 — TECH STACK SETUP", [
            "Contents: Accounting_Software_Comparison.docx, Chart_of_Accounts_Setup_Guide.docx, Software_Setup_Checklist.docx, Tech_Stack_Recommendations.docx",
            "Purpose: Choose and configure the right software. Includes a side-by-side comparison of QuickBooks Online, Xero, FreshBooks, and Wave. Also includes a standard chart of accounts by industry, setup checklists, and recommendations for practice management, time tracking, and document management tools.",
        ]),
        ("FOLDER 03 — PRICING & PACKAGING", [
            "Contents: Service_Packages_Guide.docx, Value_Pricing_Guide.docx",
            "Purpose: Define exactly what you sell and at what price. The three-tier package model (Starter / Professional / Premium) is the industry standard for recurring revenue. The Value Pricing Guide teaches you to price based on client ROI, not your hours.",
        ]),
        ("FOLDER 04 — CLIENT ACQUISITION", [
            "Contents: Outreach scripts, LinkedIn strategy, referral partner framework, networking guide",
            "Purpose: Fill your pipeline with ideal clients. Includes word-for-word scripts for cold email, LinkedIn outreach, and networking conversations. Also includes a referral partner system for building relationships with CPAs and business advisors.",
        ]),
        ("FOLDER 05 — CLIENT ONBOARDING", [
            "Contents: Engagement letter template, welcome kit, onboarding checklist, kick-off call agenda",
            "Purpose: Start every client relationship professionally. Covers the engagement letter (your contract), welcome packet, data collection form, software access setup, and the 45-minute kick-off call structure.",
        ]),
        ("FOLDER 06 — SERVICE DELIVERY", [
            "Contents: Monthly close SOP, QC checklist, bank reconciliation guide, payroll workflow",
            "Purpose: Deliver consistent, high-quality work. The monthly close SOP is your step-by-step process for every client, every month. The QC checklist ensures nothing is missed before you send reports.",
        ]),
        ("FOLDER 07 — CLIENT COMMUNICATION", [
            "Contents: Email templates, monthly report email, missing document request, late payment reminder",
            "Purpose: Communicate professionally without spending hours writing emails. Every common client communication scenario has a template — from 'I need your bank statements' to 'Your financial report is ready.'",
        ]),
        ("FOLDER 08 — BUSINESS OPERATIONS", [
            "Contents: Capacity planning worksheet, contractor agreement template, billing SOP, KPI tracker",
            "Purpose: Run your practice like a business. Covers how to know when you're at capacity, how to hire your first subcontractor, how to structure your billing, and which KPIs matter (revenue per client, churn rate, average retainer size).",
        ]),
        ("FOLDER 09 — GROWTH & SCALING", [
            "Contents: Niche selection workbook, referral system, pricing increase guide, team structure guide",
            "Purpose: Grow intentionally. Covers how to pick a niche (and why specialists earn 40–80% more), how to build a referral engine, when and how to raise prices, and how to build a team.",
        ]),
        ("FOLDER 10 — NOTION WORKSPACE", [
            "Contents: Pre-built Notion templates for client management, monthly close tracker, task management, and KPI dashboard",
            "Purpose: Run your entire firm from one Notion workspace. Import the templates and have a professional command center from day one.",
        ]),
        ("FOLDER 11 — BONUSES", [
            "Contents: Discovery call script, objection handling guide, bookkeeper elevator pitch swipe file, tax season checklist",
            "Purpose: Extra resources that accelerate your results. The discovery call script alone is worth the price of this system.",
        ]),
        ("FOLDER 12 — CANVA IMPORTABLE TEMPLATES", [
            "Contents: Proposal template, welcome packet cover, monthly report cover, social media graphics",
            "Purpose: Present yourself professionally from day one. These Canva templates are ready to customize with your logo and colors in under an hour.",
        ]),
        ("HOW TO GET THE MOST OUT OF THIS SYSTEM", [
            ('•', "Don't skip folders. Each one builds on the previous. A pricing error in Week 3 is easier to fix than a contract problem in Month 6."),
            ('•', "Customize every template. A generic contract or proposal signals inexperience. Personalize everything."),
            ('•', "Time-box your setup. Give yourself 30 days to complete setup, then START SELLING. Perfection is the enemy of revenue."),
            ('•', "Revisit the system quarterly. As you grow, older sections become more relevant (e.g., the hiring guides in folder 08 and 09)."),
            ('•', "Join a bookkeeping community. The Bookkeeping Side Hustle Facebook Group, QBO ProAdvisor Community, and AIPB forums are great resources alongside this system."),
        ]),
    ]
)


# ═══════════════════════════════════════════════════════════════════════════════
# 01_BUSINESS_SETUP
# ═══════════════════════════════════════════════════════════════════════════════

doc(
    "01_BUSINESS_SETUP/Business_Registration_Checklist.docx",
    "Business Registration Checklist",
    "Step-by-step guide to legally forming your bookkeeping practice.",
    [
        ("SECTION 1 — LLC vs. SOLE PROPRIETORSHIP: WHICH IS RIGHT FOR YOU?", [
            "This is the most important decision in your business formation. Here is a direct comparison:",
            "SOLE PROPRIETORSHIP",
            ('•', "Cost: $0–$50 (just a DBA filing in most states)"),
            ('•', "Taxes: All income reported on Schedule C of your personal return"),
            ('•', "Liability: YOU are personally liable for all business debts and lawsuits"),
            ('•', "Best for: Testing the market with your first 1–2 clients before committing to formation costs"),
            ('•', "Risk: One disgruntled client lawsuit can attach to your personal assets (home, savings, car)"),
            "LLC (Limited Liability Company)",
            ('•', "Cost: $50–$500 state filing fee + $0–$300 registered agent if out-of-state"),
            ('•', "Taxes: Pass-through by default (like sole prop); can elect S-Corp status when income exceeds ~$60,000/year"),
            ('•', "Liability: Your personal assets are protected from business lawsuits (if properly maintained)"),
            ('•', "Best for: Anyone who plans to have 3+ clients or handle client funds in any capacity"),
            ('•', "Recommendation: Form an LLC. The protection is worth the cost."),
            "S-CORP ELECTION (for established bookkeepers earning $60,000+ net)",
            ('•', "When net profit from bookkeeping exceeds ~$60K/year, elect S-Corp status with IRS Form 2553"),
            ('•', "Pay yourself a 'reasonable salary' (typically 50–60% of net profit); take remainder as distributions"),
            ('•', "Distributions are NOT subject to self-employment tax (15.3%) — this saves $4,000–$12,000/year at scale"),
            ('•', "Requires: separate payroll, quarterly payroll filings, and additional accounting — consult a CPA first"),
        ]),
        ("SECTION 2 — STEP-BY-STEP LLC FORMATION", [
            "Complete these steps in order:",
            ('•', "Step 1: Choose your state of formation. Form in the state where you live and work (ignore the Delaware/Wyoming hype for a small service business — it adds cost without benefit until you're raising outside capital)."),
            ('•', "Step 2: Choose your LLC name. It must include 'LLC' or 'Limited Liability Company.' Check availability at your state's Secretary of State website. Also check: Google search, USPTO trademark database (tmsearch.uspto.gov), domain availability."),
            ('•', "Step 3: File Articles of Organization (also called Certificate of Formation in some states). Do this at your state's Secretary of State website. Cost: $50–$500. Processing time: 1 day (expedited) to 2 weeks (standard)."),
            ('•', "Step 4: Get a Registered Agent. Most states require one. You can be your own agent (your address becomes public record) or use a service like Northwest Registered Agent (~$125/year) for privacy."),
            ('•', "Step 5: File a DBA ('Doing Business As') if your LLC name differs from your operating name. E.g., 'Smith Bookkeeping LLC' operating as 'Clear Books Co.' — file DBA with your county clerk (~$20–$50)."),
            ('•', "Step 6: Draft an Operating Agreement. Not always required but strongly recommended. This document governs how your LLC is run. Use the template in this folder or have an attorney draft one (~$300–$500)."),
            ('•', "Step 7: Apply for your EIN (see Section 3 below)."),
            ('•', "Step 8: Check for local business licenses. Many cities and counties require a general business license ($25–$200/year). Check your city/county website."),
            ('•', "Step 9: Check your state for bookkeeping-specific requirements. Most states do NOT require a license to be a bookkeeper (as opposed to a CPA). However, some states restrict certain services. Verify with your state's Board of Accountancy."),
        ]),
        ("SECTION 3 — EIN (EMPLOYER IDENTIFICATION NUMBER) REGISTRATION", [
            "Your EIN is your business's Social Security Number. You need it to open a business bank account, pay taxes, hire employees, and set up payroll.",
            ('•', "Where to apply: IRS.gov/ein — the official IRS website. Do NOT use third-party services that charge $50–$300 for this — it is 100% free directly from the IRS."),
            ('•', "Eligibility: You can apply online if you have a valid SSN or ITIN and your business is in the US."),
            ('•', "Time required: 15 minutes online. You receive your EIN immediately upon completion."),
            ('•', "Online hours: Monday–Friday 7 AM–10 PM ET. The online system is unavailable outside these hours."),
            ('•', "What you'll need: Your SSN, LLC name, business address, nature of business (select 'Bookkeeping/Accounting Services'), and reason for applying (new business)."),
            ('•', "After receiving your EIN: Download and save the confirmation letter (CP 575). You will need this for bank account opening and some vendor relationships."),
            ('•', "Important: If you applied as a sole proprietor and later form an LLC, you need a NEW EIN for the LLC. The EIN is tied to the legal entity, not you personally."),
        ]),
        ("SECTION 4 — BUSINESS BANK ACCOUNT SETUP", [
            "Keeping business and personal finances separate is non-negotiable. Commingling funds 'pierces the corporate veil' and destroys your LLC liability protection.",
            "Recommended banks for bookkeepers:",
            ('•', "Chase Business Complete Banking — widely available, good integrations with QBO and Xero, $15/mo fee waived with $2,000 min balance"),
            ('•', "Bank of America Business Advantage — strong online tools, waived fees with qualifying balances"),
            ('•', "Mercury (mercury.com) — online-only, no fees, excellent API/integration options, great for tech-forward practices"),
            ('•', "Relay (relayfi.com) — built for small businesses, free, supports multiple sub-accounts for different expense categories"),
            "What to bring to open your account:",
            ('•', "Your EIN confirmation letter (CP 575)"),
            ('•', "Articles of Organization or Certificate of Formation"),
            ('•', "Operating Agreement"),
            ('•', "Two forms of personal ID (driver's license + passport or SS card)"),
            ('•', "Minimum opening deposit (varies by bank; typically $25–$1,000)"),
            "Best practices:",
            ('•', "Set up automatic transfers: move 25–30% of every revenue deposit to a separate tax savings account"),
            ('•', "Get a business debit card and a separate business credit card"),
            ('•', "Set up online banking and connect it to QuickBooks Online for your own books"),
        ]),
        ("SECTION 5 — PROFESSIONAL LIABILITY INSURANCE (E&O)", [
            "Professional Liability Insurance (also called Errors & Omissions, or E&O) protects you if a client claims your bookkeeping error caused them financial harm.",
            "Why bookkeepers need E&O:",
            ('•', "Even if you did nothing wrong, defending a lawsuit costs $5,000–$50,000 in legal fees"),
            ('•', "A single data entry error or missed transaction could be blamed for a client's IRS penalty"),
            ('•', "Most professional service clients expect their bookkeeper to carry E&O — it's a trust signal"),
            "Coverage to look for:",
            ('•', "Coverage limit: $1,000,000 per claim / $2,000,000 aggregate is standard"),
            ('•', "Retroactive date: Ensure coverage goes back to when you started practicing"),
            ('•', "Cyber liability: Many E&O policies now include basic cyber coverage — important given the sensitive financial data you handle"),
            "Recommended providers for bookkeepers:",
            ('•', "AIPB (American Institute of Professional Bookkeepers) member insurance program"),
            ('•', "HISCOX Small Business Insurance — online quote in minutes, $500–$1,500/year for bookkeepers"),
            ('•', "Next Insurance — app-based, very fast, competitive pricing for solo practitioners"),
            ('•', "Insureon — marketplace that quotes multiple carriers simultaneously"),
            "Bookkeeper's Bond:",
            ('•', "A fidelity/surety bond (typically $10,000) protects clients if you steal from them"),
            ('•', "Many clients in real estate, property management, and legal will require this before signing"),
            ('•', "Cost: approximately $100–$200/year. Get it from the same provider as your E&O."),
        ]),
        ("SECTION 6 — POST-FORMATION COMPLIANCE CHECKLIST", [
            "After forming your LLC, these ongoing requirements keep you in good standing:",
            ('•', "Annual Report / Biennial Report: Most states require an annual report filing ($25–$300) to keep your LLC active. Calendar this immediately."),
            ('•', "Beneficial Ownership Information (BOI) Report: As of January 2024, most LLCs must file a BOI report with FinCEN within 90 days of formation (free to file at fincen.gov/boi). Penalties for non-compliance: $500/day."),
            ('•', "State income tax registration: Register with your state's department of revenue for income tax and sales tax (bookkeeping services are generally not taxable but verify for your state)."),
            ('•', "Quarterly estimated taxes: As a self-employed person, you must pay estimated taxes quarterly (April 15, June 15, Sept 15, Jan 15). Budget 25–30% of net income."),
            ('•', "Separate accounting: Keep meticulous books for your own practice. Use QBO or Xero — you're a bookkeeper; your own books should be immaculate."),
        ]),
    ]
)


doc(
    "01_BUSINESS_SETUP/Business_Plan_Template.docx",
    "Business Plan Template — Bookkeeping Practice",
    "Complete this template before investing significant time or money in your practice.",
    [
        ("SECTION 1 — EXECUTIVE SUMMARY", [
            "[Complete this section LAST after filling in all other sections]",
            "Business Name: _______________________________________________",
            "Owner(s): ___________________________________________________",
            "Date Founded / Target Launch Date: ___________________________",
            "Business Structure: LLC / Sole Proprietorship / S-Corp",
            "Location: ___________________________________________________",
            "Services Offered (brief): _____________________________________",
            "Target Market (brief): ________________________________________",
            "Revenue Goal — Year 1: $__________  |  Year 2: $__________  |  Year 3: $__________",
            "Funding Required: $________________ (if any)",
            "What makes your practice different: ___________________________",
        ]),
        ("SECTION 2 — SERVICES OFFERED", [
            "List your core services and who they're for. Be specific.",
            "Core Monthly Bookkeeping Services:",
            ('•', "Bank and credit card reconciliation (all accounts, monthly)"),
            ('•', "Transaction categorization per client's chart of accounts"),
            ('•', "Accounts payable management (optional add-on)"),
            ('•', "Accounts receivable / invoice management (optional add-on)"),
            ('•', "Monthly financial statements: Profit & Loss, Balance Sheet, Cash Flow Statement"),
            ('•', "Year-end close and preparation of books for CPA/tax preparer"),
            "Add-on Services (price separately):",
            ('•', "Payroll processing (via Gusto, QBO Payroll, or ADP)"),
            ('•', "Sales tax filing"),
            ('•', "1099 preparation and filing"),
            ('•', "Job costing / project tracking"),
            ('•', "Cash flow forecasting"),
            ('•', "CFO advisory / monthly strategy calls"),
            "Services you will NOT offer (important for scope management):",
            ('•', "Tax return preparation (refer to CPA partners)"),
            ('•', "Financial audits (CPA license required)"),
            ('•', "Legal or HR advice"),
        ]),
        ("SECTION 3 — TARGET MARKET", [
            "Define your ideal client in detail. The more specific, the more effective your marketing.",
            "Primary Target Market:",
            "Industry/Niche: _____________________________________________",
            "Business Size: ___ to ___ employees | Annual Revenue: $______ to $______",
            "Geographic Focus: __________________________________________",
            "Common Pain Points of Your Ideal Client:",
            ('•', "Pain 1: _______________________________________________"),
            ('•', "Pain 2: _______________________________________________"),
            ('•', "Pain 3: _______________________________________________"),
            "Where your ideal clients spend time (for marketing):",
            ('•', "Online: LinkedIn / Instagram / Facebook Groups / Industry Forums"),
            ('•', "Offline: Chamber of Commerce / Industry Conferences / BNI Groups"),
            "Why they would choose YOU over a competitor:",
            ('•', "Differentiator 1: _______________________________________"),
            ('•', "Differentiator 2: _______________________________________"),
            ('•', "Differentiator 3: _______________________________________"),
        ]),
        ("SECTION 4 — COMPETITION ANALYSIS", [
            "Know your competitive landscape. List 3–5 competitors and compare.",
            "Competitor 1: _______________________________________________",
            "Their pricing (if known): $______/mo | Their niche: ___________",
            "Their strengths: ____________________________________________",
            "Their weaknesses: ___________________________________________",
            "Competitor 2: _______________________________________________",
            "Their pricing (if known): $______/mo | Their niche: ___________",
            "Their strengths: ____________________________________________",
            "Their weaknesses: ___________________________________________",
            "Competitor 3 (national/franchise, e.g., Bench, Pilot, Bookkeeper360):",
            ('•', "Bench: Starts at $299/mo; strong brand; high churn; clients dislike lack of personal service"),
            ('•', "Pilot: Targets VC-backed startups; $499–$849/mo; tech-forward but impersonal"),
            ('•', "Your advantage vs. national services: Local knowledge, personal relationship, direct phone access, faster response times, ability to meet in person"),
            "Your Competitive Position:",
            "We compete on: [ ] Price  [ ] Niche expertise  [ ] Personal service  [ ] Technology  [ ] Turnaround time",
        ]),
        ("SECTION 5 — MARKETING STRATEGY", [
            "How you will attract and retain clients.",
            "Primary Marketing Channels (choose 2–3 to start):",
            ('•', "LinkedIn: Optimize profile, post 2x/week, connect with 10 ideal clients/week, publish one article/month"),
            ('•', "Referral Partners: Build relationships with 5–10 CPAs, business attorneys, and financial advisors who serve your target market"),
            ('•', "Networking: Join 1–2 local business groups (BNI, Chamber of Commerce, industry associations) and attend monthly"),
            ('•', "Content Marketing: Write one blog post per month targeting bookkeeping questions your ideal client Googles"),
            ('•', "Cold Email: Use Apollo.io or Hunter.io to find decision-maker emails in your target niche; send personalized 3-email sequences"),
            "Client Retention Strategy:",
            ('•', "Monthly financial summary email with plain-English commentary (not just numbers)"),
            ('•', "Quarterly business review calls proactively scheduled"),
            ('•', "Annual pricing review and value conversation"),
            ('•', "Birthday/anniversary acknowledgments"),
            ('•', "Referral ask after 90 days of successful service"),
            "First 90 Days Marketing Goals:",
            "Discovery calls booked: _______ | Proposals sent: _______ | Clients signed: _______",
        ]),
        ("SECTION 6 — REVENUE GOALS (YEARS 1–3)", [
            "Set specific, measurable revenue targets.",
            "YEAR 1 TARGETS:",
            "Month 1–3 (Ramp):  _____ clients × avg $____/mo = $______/mo revenue",
            "Month 4–6:         _____ clients × avg $____/mo = $______/mo revenue",
            "Month 7–12:        _____ clients × avg $____/mo = $______/mo revenue",
            "Year 1 Total Revenue Goal: $___________",
            "Year 1 Total Expenses (est.): $___________",
            "Year 1 Net Profit Goal: $___________",
            "YEAR 2 TARGETS:",
            "Target: _____ clients × avg $____/mo = $______/mo | Annual: $___________",
            "New hires planned: _____________________________________________",
            "YEAR 3 TARGETS:",
            "Target: _____ clients × avg $____/mo = $______/mo | Annual: $___________",
            "Revenue per team member target: $__________",
            "Typical Milestones for Reference:",
            ('•', "6 months: $3,000–$8,000 MRR (3–10 clients) is realistic for a focused solo bookkeeper"),
            ('•', "12 months: $8,000–$15,000 MRR is achievable with consistent outreach"),
            ('•', "24 months: $15,000–$25,000 MRR often requires first hire or subcontractor"),
            ('•', "$25,000+ MRR (Year 3+): Full team, specialized niche, advisory services added"),
        ]),
        ("SECTION 7 — STARTUP COSTS", [
            "Estimate your initial investment.",
            "ONE-TIME STARTUP COSTS:",
            ('•', "LLC formation filing fee: $50–$500 (varies by state)"),
            ('•', "Registered agent (Year 1): $0–$300"),
            ('•', "Attorney fees (operating agreement, if hiring attorney): $0–$500"),
            ('•', "Business bank account opening deposit: $100–$1,000"),
            ('•', "Website domain + 1 year hosting: $50–$200"),
            ('•', "Logo design (Fiverr/99designs): $50–$500 or DIY on Canva"),
            ('•', "Office equipment (if needed — most bookkeepers work from home): $0–$2,000"),
            "ESTIMATED TOTAL ONE-TIME COSTS: $250 – $5,000",
            "MONTHLY RECURRING COSTS:",
            ('•', "QBO Accountant: Free (you pay per client subscription or use wholesale billing)"),
            ('•', "Practice management software: $0–$150/mo"),
            ('•', "Professional liability insurance: $40–$125/mo"),
            ('•', "Google Workspace: $12–$18/user/mo"),
            ('•', "Calendly Pro: $10/mo"),
            ('•', "Phone/internet (business portion): variable"),
            "ESTIMATED MONTHLY OVERHEAD: $100 – $400/mo at launch",
            "Break-even Analysis:",
            "Monthly overhead: $______ ÷ avg client value $______ = ______ clients to break even",
        ]),
    ]
)


doc(
    "01_BUSINESS_SETUP/Brand_Identity_Guide.docx",
    "Brand Identity Guide — Building a Professional Bookkeeping Brand",
    "How to create a brand that attracts ideal clients and commands premium prices.",
    [
        ("SECTION 1 — CHOOSING YOUR BUSINESS NAME", [
            "Your name is often the first impression. These criteria separate forgettable names from memorable ones:",
            "NAMING CRITERIA CHECKLIST:",
            ('•', "Easy to say and spell: If you have to spell it every time you say it, reconsider"),
            ('•', "Available as a .com domain: Check Namecheap.com or GoDaddy — buy the domain before announcing"),
            ('•', "Not too literal: 'ABC Bookkeeping' is forgettable; 'Clear Ledger' or 'Peak Books' is memorable"),
            ('•', "Not too vague: 'Solutions Group' tells clients nothing about what you do"),
            ('•', "Scalable: Avoid using your own name if you plan to sell the business or hire staff someday"),
            ('•', "Check trademark availability: Search USPTO TESS database before filing your LLC"),
            "NAME FORMULAS THAT WORK FOR BOOKKEEPERS:",
            ('•', "Formula 1: [Clarity/Precision Word] + Books/Ledger/Bookkeeping (e.g., Precise Books, Clear Ledger Co.)"),
            ('•', "Formula 2: [Your Niche] + Financial/Bookkeeping (e.g., Restaurant Financial Services, E-Commerce Books)"),
            ('•', "Formula 3: [Founder Name] + Bookkeeping/Financial (e.g., Rivera Financial Services) — good if you're the brand"),
            ('•', "Formula 4: Abstract/Evocative name (e.g., Summit Books, Anchor Financial, Harbor Bookkeeping)"),
            "NAMES TO AVOID:",
            ('•', "Anything containing 'CPA,' 'Certified Public Accountant,' or 'Accounting Firm' unless licensed"),
            ('•', "Names too similar to well-known brands (Bench Books, QuickLedger, etc.)"),
            ('•', "Overly trendy words that will feel dated in 5 years"),
        ]),
        ("SECTION 2 — LOGO BRIEF TEMPLATE", [
            "Use this brief when working with a designer on Fiverr, 99designs, or a local graphic designer.",
            "Complete this brief before contacting any designer:",
            "Business Name: ________________________________________________",
            "Tagline (if any): ______________________________________________",
            "Industry: Bookkeeping / Accounting / Financial Services",
            "Target Client: (e.g., 'Small restaurants and retail businesses, owners who value trust and clarity')",
            "Brand Personality — circle or check 3:",
            ('•', "[ ] Professional  [ ] Approachable  [ ] Modern  [ ] Traditional  [ ] Bold  [ ] Minimalist  [ ] Playful  [ ] Authoritative"),
            "Colors I'm drawn to: __________________________________________",
            "Colors to AVOID: _______________________________________________",
            "Logo style preference:",
            ('•', "[ ] Wordmark only (text-based logo)"),
            ('•', "[ ] Icon + wordmark (symbol with business name)"),
            ('•', "[ ] Monogram/lettermark (initials)"),
            "Examples of logos I like and WHY: ______________________________",
            "Formats needed: PNG (transparent background), SVG (vector), PDF — always request all three",
            "Budget: $50–$150 on Fiverr (search 'financial logo design') | $300–$800 on 99designs | $500–$2,000 with local designer",
        ]),
        ("SECTION 3 — COLOR PALETTE SELECTION", [
            "Color psychology matters in financial services. Here are proven palettes for bookkeepers:",
            "PALETTE OPTION A — 'Trust & Precision' (Blue-based)",
            ('•', "Primary: Navy Blue (#0F3460) — authority, trust, stability"),
            ('•', "Secondary: Slate Gray (#4A5568) — professionalism, balance"),
            ('•', "Accent: Gold/Amber (#F6AD55) — premium, value"),
            ('•', "Background: Off-White (#F7FAFC) — clean, modern"),
            "PALETTE OPTION B — 'Modern & Fresh' (Teal-based)",
            ('•', "Primary: Deep Teal (#234E52) — calm, reliable, modern"),
            ('•', "Secondary: Warm Gray (#718096) — neutral, balanced"),
            ('•', "Accent: Coral/Orange (#FC8181) — energetic, approachable"),
            ('•', "Background: Light Cream (#FFFAF0)"),
            "PALETTE OPTION C — 'Premium & Sophisticated' (Dark-based)",
            ('•', "Primary: Charcoal (#2D3748) — premium, serious"),
            ('•', "Secondary: Forest Green (#276749) — growth, financial health"),
            ('•', "Accent: Gold (#ECC94B) — success, premium service"),
            ('•', "Background: Pure White (#FFFFFF)"),
            "TYPOGRAPHY PAIRINGS (use Google Fonts — free):",
            ('•', "Professional: Montserrat (headings) + Source Sans Pro (body)"),
            ('•', "Modern: Raleway (headings) + Open Sans (body)"),
            ('•', "Classic: Lato Bold (headings) + Lato Regular (body)"),
        ]),
        ("SECTION 4 — EMAIL & PROFESSIONAL PROFILES SETUP", [
            "Your email address and online profiles are often the first thing prospects check.",
            "BUSINESS EMAIL SETUP (Google Workspace recommended):",
            ('•', "Cost: $6–$12/user/month for Google Workspace Starter"),
            ('•', "Format: firstname@yourdomain.com (e.g., sarah@clearbooksco.com) — NEVER use Gmail/Yahoo for business"),
            ('•', "Setup steps: (1) Buy domain on Namecheap, (2) Sign up at workspace.google.com, (3) Verify domain ownership, (4) Create email account, (5) Configure on all devices"),
            ('•', "Email signature essentials: Full name | Title (e.g., 'Certified Bookkeeper') | Business name | Phone | Website | LinkedIn URL | (Optional) QBO ProAdvisor badge"),
            "LINKEDIN PROFILE OPTIMIZATION:",
            ('•', "Headshot: Professional photo with neutral background. Dress as you would for a client meeting. (A $150 headshot pays for itself with one client.)"),
            ('•', "Headline: '[Your Name] | Bookkeeper for [Niche] Businesses | Helping Owners Stop Flying Blind Financially'"),
            ('•', "About section: 3–5 paragraphs. Open with the client's problem, explain how you solve it, include social proof, end with a call to action ('DM me or book a free call: [Calendly link]')"),
            ('•', "Experience: List your bookkeeping experience prominently. Include relevant prior accounting/finance experience even if from a different industry."),
            ('•', "Certifications: Add QuickBooks ProAdvisor, Xero Advisor, AIPB, or any other credentials"),
            ('•', "Featured section: Add your Calendly link, a client case study post, or a helpful bookkeeping tip article"),
            "OTHER PROFILES TO SET UP:",
            ('•', "Google Business Profile (free): Critical for local search visibility"),
            ('•', "Facebook Business Page: Even if you don't actively use it, claim it before someone else does"),
            ('•', "QuickBooks Find-a-ProAdvisor directory: After completing ProAdvisor certification, your profile appears here — free leads from Intuit"),
            ('•', "Clutch.co or Bark.com: Lead generation platforms for professional services"),
        ]),
        ("SECTION 5 — PROFESSIONAL IMAGE & STANDARDS", [
            "How you present yourself in every interaction shapes whether prospects trust you with their finances.",
            "PROFESSIONAL COMMUNICATION STANDARDS:",
            ('•', "Email response time: Respond to all client emails within 4 business hours. Set this expectation in your engagement letter."),
            ('•', "Phone: Use a dedicated business number (Google Voice is free; RingCentral gives you a professional phone system for $30/mo). Never use your personal cell phone number in marketing materials."),
            ('•', "Video calls: Always appear on camera. Clean background or professional virtual background. Adequate lighting. Test audio before every call."),
            ('•', "Writing: Proofread everything. Use Grammarly (free plan is sufficient). One typo in a proposal undermines the entire message."),
            "WHAT TO WEAR / HOW TO PRESENT:",
            ('•', "Your clients trust you with their most sensitive financial information. Match your image to what 'trustworthy financial professional' looks like in your niche."),
            ('•', "For corporate/professional clients: Business casual at minimum. Blazer for video calls and in-person meetings."),
            ('•', "For restaurant/retail/trades clients: Business casual. Approachable and practical."),
            ('•', "For startups/tech: Smart casual is accepted — but always clean and put-together."),
            "PRICING IMAGE:",
            ('•', "Never apologize for your prices. Confident delivery = client confidence in your expertise."),
            ('•', "Use a professional proposal template (see folder 12) — not a plain Word document or handwritten quote."),
            ('•', "Charge what the market supports. Undercharging signals low quality, not value."),
            "ONGOING PROFESSIONAL DEVELOPMENT (builds credibility):",
            ('•', "QuickBooks ProAdvisor certification: Free, takes 6–8 hours. Complete annually."),
            ('•', "Xero Advisor certification: Free through Xero partner program."),
            ('•', "AIPB Certified Bookkeeper (CB) designation: Gold standard. Requires 2 years experience + exam."),
            ('•', "CPB (Certified Public Bookkeeper through NACPB): Strong US credential."),
            ('•', "Continuing education: 1 hour/week minimum — new software features, tax law changes, industry news."),
        ]),
    ]
)


# ═══════════════════════════════════════════════════════════════════════════════
# 02_TECH_STACK_SETUP
# ═══════════════════════════════════════════════════════════════════════════════

doc(
    "02_TECH_STACK_SETUP/Accounting_Software_Comparison.docx",
    "Accounting Software Comparison — QBO vs. Xero vs. FreshBooks vs. Wave",
    "Choose the right platform for each client type.",
    [
        ("QUICKBOOKS ONLINE (QBO) — THE INDUSTRY STANDARD", [
            "Market share: ~80% of US small businesses use QBO. If you learn only one platform, make it this one.",
            "Pricing (as of 2024):",
            ('•', "Simple Start: $30/mo — 1 user, basic income/expense tracking"),
            ('•', "Essentials: $60/mo — 3 users, adds bill management and time tracking"),
            ('•', "Plus: $90/mo — 5 users, adds project tracking, inventory, budgeting"),
            ('•', "Advanced: $200/mo — 25 users, custom reporting, dedicated support"),
            ('•', "QBO Accountant: FREE for bookkeepers. You manage client subscriptions at a 30% wholesale discount."),
            "Key Features:",
            ('•', "Bank feeds with automatic transaction matching"),
            ('•', "Class and location tracking (for multi-location or multi-department clients)"),
            ('•', "Robust inventory management (Plus and above)"),
            ('•', "Integrated payroll (additional cost: $50–$130/mo base + $6/employee/mo)"),
            ('•', "1099 e-filing built in"),
            ('•', "Hundreds of third-party integrations (Shopify, PayPal, Square, HubSpot, etc.)"),
            ('•', "QuickBooks Payments (built-in payment processing)"),
            "Pros:",
            ('•', "Largest ecosystem of integrations"),
            ('•', "Most CPAs know it — easy handoff at tax time"),
            ('•', "Strong reporting with customizable options"),
            ('•', "QBO ProAdvisor program gives you a free listing that generates leads"),
            "Cons:",
            ('•', "Frequent price increases (raised prices 3x in 2023 alone)"),
            ('•', "Customer support is poor for non-accountant users"),
            ('•', "UI can feel cluttered for simple businesses"),
            "Best for: Nearly every client type. Especially: professional services, e-commerce, retail, construction, real estate.",
        ]),
        ("XERO — THE STRONG ALTERNATIVE", [
            "Market share: #2 globally, dominant in Australia/NZ/UK, growing fast in US.",
            "Pricing (as of 2024):",
            ('•', "Early: $15/mo — 20 invoices, 5 bills/mo (very limited; avoid for active businesses)"),
            ('•', "Growing: $42/mo — unlimited invoices and bills; no payroll"),
            ('•', "Established: $78/mo — adds multi-currency, expense claims, projects"),
            ('•', "Xero Partner Program: Free practice account, 30% revenue share on referrals"),
            "Key Features:",
            ('•', "Cleaner, more modern UI than QBO — many bookkeepers find it faster to use"),
            ('•', "Unlimited users on all plans (huge advantage for businesses with multiple stakeholders)"),
            ('•', "Strong bank rules engine — automate transaction coding very effectively"),
            ('•', "Built-in purchase order management"),
            ('•', "Hubdoc (document capture) included at no extra cost"),
            ('•', "Xero Projects for job costing (Established plan)"),
            "Pros:",
            ('•', "More intuitive UI; shorter learning curve"),
            ('•', "Unlimited users without extra cost"),
            ('•', "Excellent mobile app"),
            ('•', "Strong integrations: Gusto, Shopify, Stripe, Deputy, Vend"),
            "Cons:",
            ('•', "Fewer US-based CPAs know it — may need to export for tax preparer"),
            ('•', "Payroll only available via Gusto integration (additional cost)"),
            ('•', "Fewer integrations than QBO in the US market"),
            "Best for: Tech-forward clients, clients with multiple partners/owners who need access, e-commerce, global businesses, clients coming from QBO who want something cleaner.",
        ]),
        ("FRESHBOOKS — BEST FOR SERVICE BUSINESSES AND FREELANCERS", [
            "Market share: Popular with sole proprietors and very small service businesses.",
            "Pricing (as of 2024):",
            ('•', "Lite: $19/mo — 5 clients"),
            ('•', "Plus: $33/mo — 50 clients, proposals, estimates"),
            ('•', "Premium: $60/mo — unlimited clients, business health reports"),
            ('•', "Select: Custom pricing for $10M+ revenue businesses"),
            "Key Features:",
            ('•', "Best-in-class invoicing and time tracking"),
            ('•', "Strong project management and client portal"),
            ('•', "Retainer billing built in"),
            ('•', "Automatic late payment reminders"),
            "Pros:",
            ('•', "Easiest to use of any accounting software"),
            ('•', "Strong invoicing — clients love the professional look"),
            ('•', "Best for businesses that bill by time (agencies, consultants, attorneys)"),
            "Cons:",
            ('•', "Limited chart of accounts customization"),
            ('•', "Not suitable for inventory-heavy businesses"),
            ('•', "Weaker reporting than QBO or Xero"),
            ('•', "Limited payroll integrations"),
            "Best for: Freelancers, consultants, agencies, attorneys, small service businesses with simple bookkeeping needs. NOT recommended for businesses with employees, inventory, or complex financials.",
        ]),
        ("WAVE — THE FREE OPTION", [
            "Cost: Free for accounting, invoicing, and receipt scanning. Paid plans for payroll and payments.",
            "Pricing:",
            ('•', "Accounting: Free (unlimited invoices, unlimited expense tracking, unlimited users)"),
            ('•', "Payroll: $40/mo base + $6/employee (full-service, 14 states) or $20/mo + $6 (self-service)"),
            ('•', "Payments: 2.9% + $0.60 per transaction (credit card); 1% bank transfer (min $1)"),
            "Key Features:",
            ('•', "Completely free core accounting and invoicing"),
            ('•', "Bank connections and reconciliation"),
            ('•', "Basic financial reports"),
            ('•', "Double-entry accounting"),
            "Pros:",
            ('•', "Free — ideal for clients who cannot afford paid software"),
            ('•', "Simple enough for non-financial business owners to use"),
            ('•', "Good for very small businesses (under $500K revenue)"),
            "Cons:",
            ('•', "Limited integrations"),
            ('•', "No inventory management"),
            ('•', "Customer support is minimal on free plan"),
            ('•', "Not scalable — you'll outgrow it"),
            ('•', "Wave's payroll support has been inconsistent historically"),
            "Best for: Solopreneurs and very small businesses (under $500K revenue) with simple bookkeeping needs. Good as a stepping stone for clients who can't yet afford QBO/Xero.",
            "BOOKKEEPER'S RECOMMENDATION FRAMEWORK:",
            ('•', "Client revenue < $500K, simple: Wave (free) → upgrade as they grow"),
            ('•', "Client has employees, multiple revenue streams: QBO Essentials or Plus"),
            ('•', "Client is tech-forward, values clean UI, international: Xero"),
            ('•', "Client bills by time, is a consultant/agency: FreshBooks"),
            ('•', "Client is in construction/has complex job costing: QBO Plus or Buildertrend + QBO"),
            ('•', "Default recommendation: QBO. It integrates with everything and every CPA knows it."),
        ]),
        ("SOFTWARE COMPARISON QUICK REFERENCE TABLE", [
            "Feature             | QBO      | Xero     | FreshBooks | Wave",
            "─────────────────────────────────────────────────────────────",
            "Starting price      | $30/mo   | $15/mo   | $19/mo     | Free",
            "Users included      | 1–25     | Unlimited| 1–unlimited| Unlimited",
            "Inventory tracking  | Yes      | Yes      | No         | No",
            "Payroll built-in    | Yes (+$) | No       | No         | Yes (+$)",
            "1099 e-filing       | Yes      | No       | No         | No",
            "Multi-currency      | Plus+    | Estab.   | Premium    | No",
            "Job costing         | Plus+    | Estab.   | Yes        | No",
            "Mobile app quality  | Good     | Excellent| Excellent  | Good",
            "US CPA familiarity  | Highest  | Medium   | Low        | Low",
            "Integration count   | 750+     | 800+     | 100+       | 30+",
            "Bookkeeper discount | 30% off  | 30% off  | N/A        | N/A",
        ]),
    ]
)


doc(
    "02_TECH_STACK_SETUP/Chart_of_Accounts_Setup_Guide.docx",
    "Chart of Accounts Setup Guide",
    "Standard account structures by industry with account numbers and descriptions.",
    [
        ("ABOUT THE CHART OF ACCOUNTS", [
            "The Chart of Accounts (COA) is the backbone of any set of books. A well-structured COA makes financial reports meaningful and comparisons over time possible. Set it up correctly at the start — restructuring a COA mid-year is painful.",
            "NUMBERING CONVENTION (use consistently across all clients):",
            ('•', "1000–1999: Assets"),
            ('•', "2000–2999: Liabilities"),
            ('•', "3000–3999: Equity"),
            ('•', "4000–4999: Income / Revenue"),
            ('•', "5000–5999: Cost of Goods Sold (COGS) / Cost of Sales"),
            ('•', "6000–7999: Operating Expenses (Overhead)"),
            ('•', "8000–8999: Other Income"),
            ('•', "9000–9999: Other Expenses / Non-operating"),
        ]),
        ("SERVICE BUSINESS STANDARD CHART OF ACCOUNTS", [
            "Suitable for: Consulting, marketing agencies, staffing, IT services, law firms, accountants.",
            "ASSETS:",
            ('•', "1010 — Checking Account (Operating)"),
            ('•', "1020 — Savings Account / Tax Reserve"),
            ('•', "1030 — Petty Cash"),
            ('•', "1100 — Accounts Receivable"),
            ('•', "1200 — Prepaid Expenses"),
            ('•', "1500 — Office Equipment (Cost)"),
            ('•', "1510 — Accumulated Depreciation — Office Equipment"),
            "LIABILITIES:",
            ('•', "2010 — Accounts Payable"),
            ('•', "2100 — Credit Cards Payable"),
            ('•', "2200 — Payroll Liabilities (Federal Withholding, FICA, State)"),
            ('•', "2300 — Sales Tax Payable (if applicable)"),
            ('•', "2500 — Loans Payable"),
            ('•', "2700 — Deferred Revenue / Unearned Revenue"),
            "EQUITY:",
            ('•', "3000 — Owner's Capital / Member's Equity"),
            ('•', "3100 — Owner's Draw"),
            ('•', "3200 — Retained Earnings"),
            "INCOME:",
            ('•', "4000 — Service Revenue (primary)"),
            ('•', "4100 — Consulting Fees"),
            ('•', "4200 — Retainer Income"),
            ('•', "4900 — Discounts Given (contra-revenue)"),
            "EXPENSES — Operating:",
            ('•', "6010 — Advertising & Marketing"),
            ('•', "6020 — Bank Service Charges"),
            ('•', "6030 — Computer & Software Subscriptions"),
            ('•', "6040 — Contractor / Subcontractor Fees"),
            ('•', "6050 — Dues & Subscriptions (professional memberships)"),
            ('•', "6060 — Insurance — General Liability"),
            ('•', "6070 — Insurance — Professional Liability / E&O"),
            ('•', "6080 — Legal & Professional Fees"),
            ('•', "6090 — Meals & Entertainment (50% deductible)"),
            ('•', "6100 — Office Supplies"),
            ('•', "6110 — Payroll Expenses — Wages"),
            ('•', "6120 — Payroll Expenses — Employer Taxes (FICA, FUTA, SUTA)"),
            ('•', "6130 — Payroll Expenses — Benefits"),
            ('•', "6140 — Postage & Shipping"),
            ('•', "6150 — Rent / Lease — Office"),
            ('•', "6160 — Telephone & Internet"),
            ('•', "6170 — Travel Expenses"),
            ('•', "6180 — Vehicle Expense / Mileage"),
            ('•', "6190 — Continuing Education & Training"),
            ('•', "6200 — Depreciation Expense"),
            ('•', "6900 — Miscellaneous Expense"),
        ]),
        ("RETAIL BUSINESS CHART OF ACCOUNTS", [
            "Additions/modifications from service business template for product-based businesses:",
            "ASSETS (add to service template):",
            ('•', "1300 — Inventory Asset"),
            ('•', "1310 — Inventory — Raw Materials (if manufacturing)"),
            ('•', "1400 — Deposits (vendor deposits)"),
            "INCOME:",
            ('•', "4000 — Sales Revenue — Products"),
            ('•', "4100 — Sales Revenue — Online (Shopify/Amazon/eBay)"),
            ('•', "4200 — Sales Revenue — In-Store (POS)"),
            ('•', "4800 — Shipping Income"),
            ('•', "4900 — Sales Returns & Allowances (contra-revenue)"),
            "COST OF GOODS SOLD (separate from operating expenses):",
            ('•', "5000 — Cost of Goods Sold"),
            ('•', "5010 — Inventory Purchases"),
            ('•', "5020 — Freight-In / Shipping Costs (to receive goods)"),
            ('•', "5030 — Inventory Shrinkage / Write-offs"),
            "OPERATING EXPENSES (add to service template):",
            ('•', "6210 — Credit Card Processing Fees (Shopify, Square, Stripe)"),
            ('•', "6220 — Platform Fees (Amazon seller fees, eBay fees)"),
            ('•', "6230 — Warehouse / Storage Expense"),
        ]),
        ("RESTAURANT CHART OF ACCOUNTS", [
            "Restaurants have unique cost structures — use these industry-specific accounts.",
            "COST OF GOODS SOLD:",
            ('•', "5000 — Food Cost"),
            ('•', "5010 — Beverage Cost — Non-Alcoholic"),
            ('•', "5020 — Beverage Cost — Alcoholic (Beer)"),
            ('•', "5030 — Beverage Cost — Alcoholic (Wine)"),
            ('•', "5040 — Beverage Cost — Alcoholic (Spirits)"),
            ('•', "5050 — Packaging & Supplies (to-go containers, napkins)"),
            "INDUSTRY BENCHMARKS FOR P&L ANALYSIS:",
            ('•', "Food cost target: 28–35% of food revenue"),
            ('•', "Beverage cost target: 20–25% of beverage revenue"),
            ('•', "Labor cost target: 25–35% of total revenue (including taxes and benefits)"),
            ('•', "Prime cost (food + labor) target: under 60% of revenue"),
            "EXPENSE ACCOUNTS (restaurant-specific):",
            ('•', "6300 — Direct Labor — Kitchen"),
            ('•', "6310 — Direct Labor — Front of House"),
            ('•', "6320 — Management Salaries"),
            ('•', "6330 — Payroll Taxes — Restaurant Staff"),
            ('•', "6340 — Smallwares & Kitchen Supplies"),
            ('•', "6350 — Linen & Uniforms"),
            ('•', "6360 — Repair & Maintenance — Equipment"),
            ('•', "6370 — Licenses — Liquor License"),
            ('•', "6380 — Licenses — Health Permit"),
            ('•', "6390 — Delivery Platform Fees (Uber Eats, DoorDash — typically 15–30%)"),
            ('•', "6400 — Music & Entertainment"),
            ('•', "6410 — POS System Fees"),
        ]),
        ("REAL ESTATE CHART OF ACCOUNTS", [
            "For real estate investors, property managers, and real estate agents/brokers.",
            "ASSETS:",
            ('•', "1500 — Real Property — Land (at cost)"),
            ('•', "1510 — Real Property — Buildings (at cost)"),
            ('•', "1520 — Accumulated Depreciation — Buildings"),
            ('•', "1530 — Real Property — Improvements"),
            ('•', "1540 — Escrow Deposits"),
            "INCOME:",
            ('•', "4000 — Rental Income — Residential"),
            ('•', "4010 — Rental Income — Commercial"),
            ('•', "4020 — Laundry & Vending Income"),
            ('•', "4030 — Late Fee Income"),
            ('•', "4040 — Pet Rent"),
            ('•', "4050 — Parking Income"),
            ('•', "4100 — Commission Income (for agents/brokers)"),
            "EXPENSES:",
            ('•', "6100 — Mortgage Interest (rental properties — deductible)"),
            ('•', "6110 — Real Estate Taxes"),
            ('•', "6120 — Insurance — Property"),
            ('•', "6130 — HOA Fees"),
            ('•', "6140 — Property Management Fees"),
            ('•', "6150 — Repairs & Maintenance"),
            ('•', "6160 — Landscaping & Groundskeeping"),
            ('•', "6170 — Utilities — paid by landlord"),
            ('•', "6180 — Depreciation Expense — Buildings (27.5 years residential; 39 years commercial)"),
            ('•', "6190 — Advertising — Vacancy / Rental Listings"),
            ('•', "6200 — Legal Fees — Eviction / Lease"),
            "Note: Each rental property should be tracked as a separate Class or Location in QBO/Xero for property-level P&L reporting.",
        ]),
    ]
)


doc(
    "02_TECH_STACK_SETUP/Software_Setup_Checklist.docx",
    "Software Setup Checklist — QuickBooks Online & Xero",
    "Step-by-step configuration checklist for new client file setup.",
    [
        ("QBO SETUP — PART 1: COMPANY SETTINGS", [
            "Complete these settings immediately after creating a new client file.",
            ('•', "Step 1: Company name, address, phone, email, website — go to Settings > Company Information"),
            ('•', "Step 2: Set fiscal year start month (most companies: January; some use July for non-calendar fiscal year)"),
            ('•', "Step 3: Set accounting method: Cash vs. Accrual (confirm with client and their CPA — this affects how income and expenses are recognized)"),
            ('•', "Step 4: Set industry — helps QBO suggest a starter chart of accounts"),
            ('•', "Step 5: Enable/disable features under Settings > Account and Settings > Advanced:"),
            ('•', "   — Enable: Classes (if client has departments or locations to track separately)"),
            ('•', "   — Enable: Locations (for multi-location businesses)"),
            ('•', "   — Enable: Track projects (for job costing — Plus plan required)"),
            ('•', "   — Enable: Multicurrency (only if client transacts in foreign currencies)"),
            ('•', "Step 6: Set up Users — add client as 'Company Admin' so they can view their own data"),
            ('•', "Step 7: Upload company logo for use on invoices and reports"),
        ]),
        ("QBO SETUP — PART 2: CHART OF ACCOUNTS", [
            ('•', "Step 1: Delete or deactivate default accounts that don't apply to this client's business"),
            ('•', "Step 2: Add industry-specific accounts using the Chart of Accounts Setup Guide"),
            ('•', "Step 3: Verify account types are correct (Asset, Liability, Equity, Income, Expense, COGS) — wrong type = wrong financial statements"),
            ('•', "Step 4: Verify tax line mapping for accounts that flow to Schedule C or S-Corp return — confirm with CPA"),
            ('•', "Step 5: Set up sub-accounts where useful (e.g., Payroll Expenses > Wages; Payroll Expenses > Employer Taxes; Payroll Expenses > Benefits)"),
            ('•', "Step 6: Print/export the final COA and get client confirmation — document in client file"),
        ]),
        ("QBO SETUP — PART 3: BANK FEEDS", [
            ('•', "Step 1: Connect all business bank accounts and credit cards via Settings > Banking"),
            ('•', "Step 2: Set the 'start date' for each connection carefully — do not import transactions before the client's start date with you"),
            ('•', "Step 3: Create bank rules for recurring, predictable transactions (e.g., 'If payee = Amazon and amount < $200, categorize as Office Supplies')"),
            ('•', "Step 4: Do the first review of imported transactions with the client — confirm categorizations before establishing rules"),
            ('•', "Step 5: Set up positive pay / matching rules — bank feed shows bank transactions; match to manually entered transactions if client uses AP module"),
        ]),
        ("QBO SETUP — PART 4: PAYROLL, INVOICING & FINAL STEPS", [
            ('•', "Payroll (if applicable): Connect to QBO Payroll or Gusto integration. Map payroll expenses to correct COA accounts. Confirm pay schedule and pay run dates."),
            ('•', "Invoicing setup: Upload logo, set default payment terms (Net 15 is standard for small businesses), set up QBO Payments if client wants to accept credit cards online"),
            ('•', "1099 setup: Go to Expenses > Vendors > mark each contractor vendor 'Track payments for 1099' before you start paying them"),
            ('•', "Opening balances: Enter as of your start date. Get the trial balance from the previous bookkeeper or prior tax return. Enter as journal entries with prior bookkeeper's sign-off."),
            ('•', "Recurring transactions: Set up recurring journal entries for prepaid expense amortization, depreciation, and any other monthly accruals"),
            ('•', "Report customization: Create and save custom report templates for the monthly financial package you'll deliver"),
        ]),
        ("XERO SETUP CHECKLIST", [
            "Follow in order for each new Xero client.",
            ('•', "Step 1: Organization settings: legal name, trading name, address, phone, email, website, fiscal year start"),
            ('•', "Step 2: Financial settings: accounting basis (cash or accrual), tax period, default currency"),
            ('•', "Step 3: Chart of accounts: customize using the industry template from the Chart of Accounts Setup Guide. Import via CSV for efficiency."),
            ('•', "Step 4: Bank connections: Add > Bank Accounts. Connect directly or import via OFX/CSV if direct connect is unavailable. Set transaction start date."),
            ('•', "Step 5: Bank rules: Settings > Bank Rules. Create rules for regular transactions. More aggressive automation is possible in Xero than QBO."),
            ('•', "Step 6: Contacts: import existing client/vendor list via CSV. Required fields: Contact name, email, account number (for invoicing)."),
            ('•', "Step 7: Hubdoc setup: Connect Hubdoc (included with Xero). Have client install the Hubdoc mobile app for receipt capture."),
            ('•', "Step 8: Users and roles: Invite client as 'Standard' user (can view and enter data) or 'Read Only.' Do not give client 'Adviser' access — that's your role."),
            ('•', "Step 9: Payroll: Set up via Gusto integration (Settings > Payroll, connect Gusto). Map Gusto payroll items to Xero accounts."),
            ('•', "Step 10: Report templates: Create and save custom Xero report templates for monthly financial package. Xero's Report Templates feature allows you to build once and use across all clients."),
        ]),
    ]
)


doc(
    "02_TECH_STACK_SETUP/Tech_Stack_Recommendations.docx",
    "Tech Stack Recommendations — Tools for Running a Modern Bookkeeping Practice",
    "Curated tool recommendations with pricing and use cases.",
    [
        ("PRACTICE MANAGEMENT SOFTWARE", [
            "This is your firm's operating system — where you track clients, tasks, deadlines, and communications.",
            "KEEPER (keeper.app) — RECOMMENDED FOR SOLO AND SMALL FIRMS",
            ('•', "Purpose: Client management, client portal, document requests, task automation"),
            ('•', "Price: ~$8–$12/client/month (scales with client count)"),
            ('•', "Standout feature: Client-facing portal where clients upload documents; automatic reminders for missing items"),
            ('•', "Best for: Bookkeepers with 10–50 clients who want a purpose-built tool"),
            "FINANCIAL CENTS (financialcents.com) — STRONG ALL-ROUNDER",
            ('•', "Purpose: Client tracking, workflow management, time tracking, team management, client requests"),
            ('•', "Price: $39/mo (Solo) | $59/mo (Team, per user)"),
            ('•', "Standout feature: Workflow templates pre-built for bookkeeping firms; capacity management dashboard"),
            ('•', "Best for: Solo bookkeepers planning to hire; small teams of 2–5"),
            "JETPACK WORKFLOW (jetpackworkflow.com) — WORKFLOW-FOCUSED",
            ('•', "Purpose: Workflow and job management, recurring task templates, deadline tracking"),
            ('•', "Price: $45/user/mo"),
            ('•', "Standout feature: Workflow templates with recurring job scheduling; strong for deadline-driven firms"),
            ('•', "Best for: Established firms with a defined workflow that needs systematizing"),
            "STARTING OUT? Use a spreadsheet + Google Drive for your first 3–5 clients. Invest in practice management software at 5+ clients.",
        ]),
        ("TIME TRACKING TOOLS", [
            "Track time even on fixed-fee engagements. You need this data to price future clients and identify unprofitable ones.",
            "TOGGL TRACK (toggl.com/track)",
            ('•', "Price: Free (up to 5 users) | $9/user/mo (Starter)"),
            ('•', "Best features: One-click timer, detailed reporting, integrates with most browsers, tags by client/project"),
            ('•', "Best for: Solo bookkeepers or small teams wanting simple, fast time tracking"),
            "HARVEST (getharvest.com)",
            ('•', "Price: Free (1 user, 2 projects) | $12/user/mo (Pro, unlimited)"),
            ('•', "Best features: Time tracking + built-in invoicing + expense tracking; integrates with Asana, Basecamp, Slack"),
            ('•', "Best for: Bookkeepers who also want to invoice from their time tracker"),
            "CLOCKIFY (clockify.me)",
            ('•', "Price: Free (unlimited users and projects, with limitations) | $5.49–$7.99/user/mo for pro features"),
            ('•', "Best for: Teams that want free time tracking with basic reporting"),
            "HOW TO USE TIME TRACKING DATA:",
            ('•', "Monthly: Compare actual hours vs. estimated hours for each client"),
            ('•', "Calculate your effective hourly rate per client: Monthly fee ÷ Hours spent"),
            ('•', "Any client at < $75/hr effective rate: raise price at renewal or reduce scope"),
            ('•', "Use data to quote future clients accurately ('this type of client takes me X hours/month')"),
        ]),
        ("INVOICING & PAYMENT COLLECTION", [
            "You handle client finances — your own billing should be frictionless and professional.",
            "STRIPE (stripe.com) — RECOMMENDED FOR RECURRING BILLING",
            ('•', "Price: 2.9% + $0.30 per card transaction; 0.8% ACH (max $5)"),
            ('•', "Best for: Setting up recurring monthly retainer billing on autopay"),
            ('•', "Setup: Create subscription products for each service tier; clients enter card once and are billed automatically"),
            "QBO PAYMENTS (built into QuickBooks Online)",
            ('•', "Price: 2.9% + $0.25 (card); 1% ACH (max $10)"),
            ('•', "Best for: Clients who already pay QBO invoices online"),
            "BILL.COM",
            ('•', "Price: $45–$79/mo"),
            ('•', "Best for: Clients with high AP volume who want an automated bill payment workflow"),
            "GUSTO (for your own payroll, if you have employees)",
            ('•', "Price: $40/mo + $6/employee/mo"),
            ('•', "Best for: Running payroll for your own bookkeeping staff"),
            "BEST PRACTICE: Put all clients on ACH auto-pay for retainer billing. Cards fail; bank accounts rarely do. Reduce your collections effort to near zero.",
        ]),
        ("DOCUMENT MANAGEMENT", [
            "You receive and send sensitive financial documents constantly. Security and organization matter.",
            "GOOGLE DRIVE / GOOGLE WORKSPACE",
            ('•', "Price: $6–$12/user/mo (includes Gmail, Drive, Docs, Sheets)"),
            ('•', "Setup: Create a master folder template per client: /Clients/[Client Name]/[Year]/[Month]/"),
            ('•', "Security: Enable 2-factor authentication on all accounts. Do not share login credentials."),
            "SHAREFILE (by Citrix)",
            ('•', "Price: $50–$400+/mo"),
            ('•', "Best for: Firms that need a dedicated secure file-sharing portal with branded client access"),
            "HUBDOC (hubdoc.com)",
            ('•', "Price: Included with Xero; ~$12/mo standalone"),
            ('•', "Best for: Receipt and bill capture — clients email or photograph receipts; Hubdoc extracts data and pushes to QBO/Xero"),
            "DEXT (formerly Receipt Bank)",
            ('•', "Price: $20–$40/mo"),
            ('•', "Best for: High-volume receipt capture; strong mobile app for client use"),
            "SECURITY REQUIREMENTS — NON-NEGOTIABLE:",
            ('•', "Password manager: 1Password ($3/mo) or LastPass ($3/mo) — never reuse passwords"),
            ('•', "2-factor authentication: Enable on every account that touches client data"),
            ('•', "Encrypted email: Consider Proton Mail or Mimecast for sending sensitive documents"),
            ('•', "Data backup: Google Drive / SharePoint provides automatic versioning — verify this is on"),
        ]),
        ("COMMUNICATION & CLIENT COLLABORATION", [
            "Professional, organized communication separates great bookkeepers from average ones.",
            "EMAIL — GOOGLE WORKSPACE (primary)",
            ('•', "Use for: Formal communications, document delivery, proposals, engagement letters"),
            ('•', "Best practice: Create email templates in Gmail for your most frequent emails (see folder 07)"),
            "LOOM (loom.com) — VIDEO MESSAGING",
            ('•', "Price: Free (5 min/video) | $8–$12.50/mo (unlimited)"),
            ('•', "Use for: Explaining financial reports via screen recording; walking clients through their numbers verbally"),
            ('•', "Game-changer: Instead of writing a long email about why their P&L looks a certain way, record a 3-minute Loom video. Clients love it."),
            "CALENDLY (calendly.com) — SCHEDULING",
            ('•', "Price: Free (1 event type) | $8–$12/mo (Professional)"),
            ('•', "Use for: Discovery calls, client kick-off calls, quarterly reviews"),
            ('•', "Setup tip: Block focus time in your calendar before connecting Calendly so clients can't book every slot"),
            "SLACK (optional for larger firms)",
            ('•', "Use for: Internal team communication if you have staff or subcontractors"),
            ('•', "Do NOT use Slack with clients unless they specifically request it — email is auditable and professional"),
        ]),
    ]
)


# ═══════════════════════════════════════════════════════════════════════════════
# 03_PRICING_PACKAGING
# ═══════════════════════════════════════════════════════════════════════════════

doc(
    "03_PRICING_PACKAGING/Service_Packages_Guide.docx",
    "Service Packages Guide — The Three-Tier Bookkeeping Model",
    "How to structure, scope, and price your Starter, Professional, and Premium packages.",
    [
        ("WHY THREE PACKAGES? THE PSYCHOLOGY AND BUSINESS CASE", [
            "Offering three tiers does three things: (1) anchors clients on value rather than price, (2) makes your middle package appear like the 'reasonable choice,' and (3) gives clients a clear upgrade path as their business grows.",
            "The 'good, better, best' model is backed by decades of consumer psychology research. When clients see only one package, they evaluate: 'Is this worth it?' When they see three, they evaluate: 'Which one is right for me?' — a very different question.",
            "Pricing targets are based on national market averages. Adjust ±20–30% for your local market cost of living and competition.",
        ]),
        ("STARTER PACKAGE — $300 to $500 per Month", [
            "TARGET CLIENT: Solopreneurs, freelancers, small businesses with one bank account, under $500K annual revenue, fewer than 150 monthly transactions.",
            "INCLUDED SERVICES:",
            ('•', "Bank reconciliation: 1 checking account + 1 business credit card (monthly)"),
            ('•', "Transaction categorization: up to 150 transactions/month per the agreed chart of accounts"),
            ('•', "Monthly financial statements: Profit & Loss, Balance Sheet (delivered by the 10th of the following month)"),
            ('•', "Annual 1099 preparation: up to 5 contractors included"),
            ('•', "Year-end books cleanup and delivery to CPA in ready-to-file format"),
            ('•', "Email support: responses within 1 business day"),
            "NOT INCLUDED (upgrade or add-on):",
            ('•', "Payroll processing"),
            ('•', "Accounts payable or receivable management"),
            ('•', "Third bank/credit card account (add $50–$75/account/mo)"),
            ('•', "Transactions over 150/mo (add $1.00–$1.50 per additional transaction)"),
            ('•', "Advisory calls or financial planning"),
            "HOW TO PRESENT THIS PACKAGE:",
            ('•', "'The Starter package is perfect for you right now. You get clean, accurate books every month, plus financial statements you can actually use — all for less than the cost of one hour with an attorney. When your business grows past $500K or you hire employees, we'll move you to the Professional package.'"),
            "SCOPE CREEP PROTECTION:",
            ('•', "Define 'transaction' in the engagement letter: any individual line item pulled from bank/credit card feeds"),
            ('•', "Track hours monthly for the first 3 months to validate pricing"),
            ('•', "Add a transaction overage clause: 'If transactions exceed 150/month in 2+ consecutive months, we'll revisit package pricing'"),
        ]),
        ("PROFESSIONAL PACKAGE — $700 to $1,200 per Month", [
            "TARGET CLIENT: Growing businesses with 2–5 employees, $500K–$2M annual revenue, multiple accounts, using payroll, and beginning to need financial insight beyond basic reports.",
            "INCLUDED SERVICES (everything in Starter, plus):",
            ('•', "Bank reconciliation: up to 3 bank/credit card accounts"),
            ('•', "Transaction categorization: up to 300 transactions/month"),
            ('•', "Payroll processing: up to 10 employees via Gusto or QBO Payroll (payroll subscription cost billed separately to client)"),
            ('•', "Payroll tax filings: 941, 940, state payroll tax returns (quarterly)"),
            ('•', "Accounts Payable management: enter and schedule up to 20 bills/month; 2 weekly payment runs"),
            ('•', "Accounts Receivable: create and send invoices (up to 20/month); aging report included in monthly package"),
            ('•', "Monthly financial statements + budget vs. actual comparison (if client provides budget)"),
            ('•', "1099 preparation: up to 15 contractors included"),
            ('•', "Quarterly 30-minute review call to discuss financials"),
            ('•', "Email and phone support during business hours"),
            "NOT INCLUDED:",
            ('•', "Employees over 10 (add $20–$30/employee/month)"),
            ('•', "Transactions over 300/month (additional fee)"),
            ('•', "CFO-level advisory beyond quarterly calls"),
            ('•', "Tax return preparation (refer to CPA partner)"),
            "HOW TO UPSELL FROM STARTER TO PROFESSIONAL:",
            ('•', "'You've crossed $500K in revenue and you're hiring. The Starter package no longer covers everything you need. The Professional package adds payroll, bill pay, and quarterly strategy calls — so you're not just getting bookkeeping, you're getting a financial partner. The additional investment is $X per month, and most clients tell me it saves them at least that much in CPA fees alone.'"),
        ]),
        ("PREMIUM PACKAGE — $1,500 to $2,500+ per Month", [
            "TARGET CLIENT: Established businesses with $2M+ revenue, 10+ employees, multiple revenue streams or locations, business owner who wants a financial partner — not just a record-keeper.",
            "INCLUDED SERVICES (everything in Professional, plus):",
            ('•', "Bank reconciliation: unlimited accounts"),
            ('•', "Transaction categorization: unlimited"),
            ('•', "Payroll: unlimited employees"),
            ('•', "Full AP/AR management (unlimited bills, invoices, payment runs)"),
            ('•', "Monthly financial package with: P&L, Balance Sheet, Cash Flow Statement, Budget vs. Actual, Department/Location breakdown, KPI dashboard"),
            ('•', "Monthly 60-minute CFO advisory call: review financials, discuss trends, answer 'what does this mean for my business?' questions"),
            ('•', "Cash flow forecasting: 13-week rolling cash flow model, updated monthly"),
            ('•', "Annual budget preparation: work with client to build next year's budget"),
            ('•', "Tax projection coordination: quarterly tax estimate calculations shared with client's CPA"),
            ('•', "Dedicated account management: you (or senior team member) as primary contact, 4-hour SLA on communications"),
            ('•', "Unlimited 1099 preparation"),
            "WHO IS THIS FOR:",
            ('•', "Business owners who have scaled past $2M and realize their financial blindspots are costly"),
            ('•', "Businesses that have had IRS problems, cash flow crises, or made a major financial mistake due to bad information"),
            ('•', "Private equity–backed companies that need institutional-quality reporting from an outsourced team"),
            "PREMIUM PACKAGE SALES APPROACH:",
            ('•', "At this price point, you're selling peace of mind and strategic advantage, not just clean books."),
            ('•', "'Most business owners at your revenue level are making decisions based on incomplete financial information — and it's costing them more than they realize. The Premium package gives you a CFO-level financial partner at a fraction of the cost of hiring one in-house. A full-time CFO costs $150,000–$250,000/year in salary alone. We're talking about $1,500–$2,500/month.'"),
        ]),
        ("PRICING CUSTOMIZATION AND ADD-ONS", [
            "Standard add-ons to offer across all packages:",
            ('•', "Additional bank/credit card account: $50–$100/account/month"),
            ('•', "Transaction volume overage: $1.00–$1.50 per transaction over the included limit"),
            ('•', "Payroll per additional employee (over included count): $20–$30/employee/month"),
            ('•', "Sales tax return preparation and filing: $75–$150/state/month"),
            ('•', "Clean-up / catch-up bookkeeping: charge as a project fee. Formula: estimate hours × your desired hourly rate (typically $75–$125/hr for clean-up work). A year of neglected books typically takes 15–40 hours."),
            ('•', "QuickBooks / Xero setup for new client: $500–$1,500 one-time project fee"),
            ('•', "1099 preparation over included limit: $15–$25 per additional contractor"),
            ('•', "Year-end adjustment entries and CPA coordination: typically included in Professional/Premium; $200–$400 add-on for Starter clients"),
            "PRICING REVIEW CADENCE:",
            ('•', "Review all client pricing annually (ideally in October/November, before the new year)"),
            ('•', "Raise rates by 5–10% per year for existing clients — inflation, experience, and demand all justify this"),
            ('•', "New clients always start at current rates — never grandfather new clients at old prices"),
            ('•', "Include a rate adjustment clause in every engagement letter: 'Fees may be adjusted with 30 days written notice'"),
        ]),
    ]
)


doc(
    "03_PRICING_PACKAGING/Value_Pricing_Guide.docx",
    "Value Pricing Guide — How to Price Your Services Based on Value, Not Hours",
    "Stop trading time for money. Build a recurring revenue practice that scales.",
    [
        ("THE PROBLEM WITH HOURLY BILLING", [
            "Hourly billing punishes efficiency. The better you get at bookkeeping, the faster you work — and the less you earn per client. That's backwards.",
            "The real problem with hourly billing for bookkeepers:",
            ('•', "It creates adversarial relationships: clients watch the clock; you feel guilty being efficient"),
            ('•', "It caps your income: you can only work so many hours"),
            ('•', "It makes your income unpredictable: variable hours = variable revenue"),
            ('•', "It positions you as a commodity: 'How much per hour?' is a race to the bottom"),
            "The solution: Monthly retainer pricing based on the value you deliver, not the time it takes.",
            "Value pricing defined: You charge based on the economic benefit the client receives, not the hours you spend. A client with $2M in revenue whose books are a mess might be paying the IRS $15,000/year in penalties and their CPA an extra $5,000 in clean-up fees. You solve that problem for $1,200/month. That's not expensive — that's a 15× ROI.",
        ]),
        ("THE ROI FRAMEWORK — SHOWING CLIENTS THEIR BOOKKEEPER PAYS FOR ITSELF", [
            "Use this framework in every discovery call and proposal. It shifts the conversation from 'cost' to 'investment.'",
            "ROI CALCULATION WORKSHEET:",
            "Ask the client these questions during the discovery call:",
            ('•', "Q1: 'How many hours per month do you personally spend on bookkeeping or trying to understand your finances?' (Average answer: 5–20 hours)"),
            ('•', "Q2: 'What's your effective hourly rate as the business owner?' (Revenue ÷ hours worked, typically $100–$500/hr for the owners you're targeting)"),
            ('•', "Q3: 'How much did you pay your CPA last year for bookkeeping cleanup or extra work because your books weren't ready?' (Common answer: $500–$5,000)"),
            ('•', "Q4: 'Have you ever paid a late fee, penalty, or interest to the IRS because records weren't in order?' (Many say yes)"),
            "CALCULATE THE ROI IN REAL TIME:",
            "Owner time freed up: 10 hours/mo × $200/hr owner value = $2,000/month in recovered owner time",
            "CPA savings: $3,000/year ÷ 12 = $250/month",
            "Penalty avoidance: $1,500/year ÷ 12 = $125/month",
            "Total value delivered: $2,375/month",
            "Your price: $750/month",
            "NET ROI for client: $1,625/month, or 3.2× their investment",
            "SCRIPT: 'Based on what you've shared, hiring me frees up 10 hours a month of your time — time you could spend on $200/hour work. That alone is $2,000 in value. Add the CPA savings and penalty avoidance, and you're looking at $2,375 in value for $750 a month. That's 3× ROI on day one.'",
        ]),
        ("DISCOVERY CALL PRICING STRATEGY", [
            "The discovery call is where price is set — not where you defend it. Here's how to structure the pricing conversation.",
            "BEFORE THE CALL:",
            ('•', "Research the prospect: LinkedIn profile, website, Yelp reviews (to understand their business size and type)"),
            ('•', "Estimate the package they'll need based on what you know"),
            ('•', "Set a minimum: know your 'walk away' price before the call (suggested: $300/month minimum for any client)"),
            "DURING THE CALL — THE PRICE REVEAL SEQUENCE:",
            ('•', "Step 1: Listen first. Spend the first 20 minutes asking questions and understanding their situation. Do NOT mention price until you understand their needs."),
            ('•', "Step 2: Identify their biggest financial pain point. Reflect it back: 'So it sounds like the biggest issue is that you have no idea if you're actually profitable until your CPA tells you — six months after the fact. Is that right?'"),
            ('•', "Step 3: Present the solution. 'What I'd recommend for you is our Professional package. Here's what that includes...' (describe the package)"),
            ('•', "Step 4: ROI bridge. Use the ROI framework above before stating the price."),
            ('•', "Step 5: State the price confidently, then stop talking. 'That's $900 a month. [PAUSE. Let them respond.]'"),
            ('•', "Step 6: Handle objections (see objection scripts in folder 11)"),
            "COMMON MISTAKE: Stating the price and then immediately justifying it ('...but that includes everything, and you won't have to worry about...') signals you're not confident in your price. State it. Be quiet. Let them respond.",
        ]),
        ("HOW TO PRESENT PACKAGES — THE PROPOSAL PROCESS", [
            "After a discovery call, send a proposal within 24 hours. Every hour you wait reduces close rates.",
            "PROPOSAL STRUCTURE:",
            ('•', "Page 1: Executive Summary — one paragraph summarizing their situation and your recommendation"),
            ('•', "Page 2: The Problem — their current pain points (use their exact words from the discovery call)"),
            ('•', "Page 3: The Solution — your recommended package with full scope listed"),
            ('•', "Page 4: Investment — all three packages listed (even if you're recommending one); price the one you recommend prominently"),
            ('•', "Page 5: About You — credentials, certifications, brief bio, 1–2 client testimonials or results"),
            ('•', "Page 6: Next Steps — clear CTA: 'To get started, sign the engagement letter and submit payment for your first month. I'll send both to you within 24 hours of your decision.'"),
            "FOLLOW-UP CADENCE AFTER PROPOSAL:",
            ('•', "Day 1: Send proposal"),
            ('•', "Day 3: Follow up by email: 'Just checking in — any questions about the proposal?'"),
            ('•', "Day 6: Follow up by phone: 'I wanted to connect personally to answer any questions and see if you're ready to move forward'"),
            ('•', "Day 10: Final follow-up: 'I'm closing out proposals from last week. Are you still interested in moving forward? If timing isn't right, I completely understand — I'm happy to reconnect when you're ready.'"),
            "CLOSE RATE TARGETS: 50–60% on qualified prospects (people who agreed to the discovery call and have the budget).",
        ]),
        ("HANDLING PRICE OBJECTIONS", [
            "These are the most common price objections and proven responses.",
            "OBJECTION: 'That's more than I expected to pay.'",
            ('•', "Response: 'I understand. Can I ask — what were you expecting?' [Listen.] 'That's a common starting point. Most of my clients found that when they calculated the time they were spending on their books — and what that time was worth to them — the difference more than paid for itself. Let me show you the math for your situation...' [ROI framework]"),
            "OBJECTION: 'I can get it done cheaper on Fiverr / by my cousin.'",
            ('•', "Response: 'Absolutely — there are cheaper options. The question is what level of risk you're comfortable with. I carry professional liability insurance, I'm a certified bookkeeper, and I back my work. If I make a mistake, I fix it at my cost and my insurance covers damages. Can your cousin's spreadsheet do that? If budget is truly the constraint, let's look at the Starter package and see if that works for now.'"),
            "OBJECTION: 'Can you do it for $X instead?' (lowball counter)",
            ('•', "Response: 'I can't deliver the full service at that price — I'd be doing you a disservice by rushing through your books. What I can do is look at a reduced scope for that price. Would you like me to show you what $X would get you?' [Offer a stripped-down Starter package, or hold firm if the scope doesn't justify it]"),
            "OBJECTION: 'I need to think about it.'",
            ('•', "Response: 'Of course — this is an important decision. What specifically would help you feel confident moving forward? Is there information I haven't provided, or is this more about timing?' [Most 'I need to think about it' objections are actually unspoken concerns — surface them]"),
            "NON-NEGOTIABLE RULE: Never drop your price without removing scope. If you discount without removing services, you've trained the client that your prices are negotiable and your initial quote was inflated.",
        ]),
    ]
)


print("\n✅ Build Part 1 complete!")
print(f"\nFiles created under: {BASE}")
print("\nFolders created:", len(FOLDERS))
created = [
    "00_START_HERE/README_FIRST.txt",
    "00_START_HERE/Quick_Start_Checklist.docx",
    "00_START_HERE/Product_Overview.docx",
    "01_BUSINESS_SETUP/Business_Registration_Checklist.docx",
    "01_BUSINESS_SETUP/Business_Plan_Template.docx",
    "01_BUSINESS_SETUP/Brand_Identity_Guide.docx",
    "02_TECH_STACK_SETUP/Accounting_Software_Comparison.docx",
    "02_TECH_STACK_SETUP/Chart_of_Accounts_Setup_Guide.docx",
    "02_TECH_STACK_SETUP/Software_Setup_Checklist.docx",
    "02_TECH_STACK_SETUP/Tech_Stack_Recommendations.docx",
    "03_PRICING_PACKAGING/Service_Packages_Guide.docx",
    "03_PRICING_PACKAGING/Value_Pricing_Guide.docx",
]
print(f"DOCX/TXT files created: {len(created)}")
