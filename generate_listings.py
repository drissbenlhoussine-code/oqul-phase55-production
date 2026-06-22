#!/usr/bin/env python3
"""Generate formatted Etsy listing files for all 15 products"""
import os

OUT = "/home/user/oqul-phase55-production/etsy-listings/formatted/"
os.makedirs(OUT, exist_ok=True)

PRODUCTS = [

# ─── 01 ───────────────────────────────────────────────────────────────────────
{
"file": "01_MortgageBroker.txt",
"title": "Mortgage Broker OS | Client Pipeline, Pre-Approval Tracker, Referral System, 60+ Files",
"description": """\
Launch and scale your mortgage brokerage with this complete operating system. Built for mortgage brokers, loan officers, and independent brokers who want a professional, organized business from day one.

WHAT'S INSIDE:
- Business plan template with revenue projections
- Loan pipeline tracker (Excel) with status, stage, and close date
- Pre-approval checklist (20-step process)
- Client onboarding workflow and welcome packet
- Referral partner system and tracking spreadsheet
- Mortgage product comparison calculator
- Rate quote email templates
- Realtor partnership outreach scripts
- Compliance and disclosure checklist
- Notion databases: client CRM, loan pipeline, referral tracker
- Marketing plan: 90-day lead generation strategy
- Pitch deck for referral partner presentations
- Complete guide PDF

WHO IT'S FOR: Mortgage brokers, loan officers, and financial advisors looking to systemize client acquisition and loan management.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "mortgage broker kit, loan officer tools, mortgage business, mortgage templates, client pipeline, loan tracker, mortgage crm, broker business kit, referral system, mortgage planner, financial broker, digital download, instant download"
},

# ─── 02 ───────────────────────────────────────────────────────────────────────
{
"file": "02_RecruitingAgency.txt",
"title": "Recruiting Agency OS | Candidate Pipeline, Client Management, Invoicing System, 70+ Files",
"description": """\
Run a professional recruiting agency with this complete operating system. Everything from business setup to candidate sourcing and client billing -- built for independent recruiters and boutique agencies.

WHAT'S INSIDE:
- Business plan with fee structure and revenue model
- Candidate pipeline tracker (Excel): sourcing to placement
- Job order management system
- Client service agreement (Word, fully editable)
- Placement fee invoice template
- LinkedIn sourcing playbook with Boolean search strings
- Candidate assessment scorecard
- Interview scheduling and feedback templates
- Client onboarding questionnaire
- Cold outreach email scripts for clients and candidates
- Notion databases: candidate CRM, client tracker, job orders
- Agency pitch deck for new client presentations
- KPI dashboard: fill rate, time-to-fill, revenue
- Complete guide PDF

WHO IT'S FOR: Independent recruiters, headhunters, and staffing agency founders ready to operate at a professional level.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "recruiting agency, recruitment os, recruiter toolkit, candidate tracker, hiring templates, recruiter business, talent sourcing, recruitment crm, hr agency tools, headhunter kit, recruiter planner, digital download, instant download"
},

# ─── 03 ───────────────────────────────────────────────────────────────────────
{
"file": "03_BookkeepingBusiness.txt",
"title": "Bookkeeping Business OS | Client Tracker, Service Menu, Contracts, Pricing, 65+ Files",
"description": """\
Run a fully professional bookkeeping business with this complete operating system. From landing your first client to scaling to a full roster -- every system, template, and tool you need.

WHAT'S INSIDE:
- Business plan with niche selection guide
- Service menu (15+ bookkeeping services with pricing guidance)
- Client pricing calculator (Excel)
- Bookkeeping service agreement (Word, fully editable)
- Client onboarding checklist and welcome packet
- Monthly bookkeeping workflow (step-by-step SOP)
- Chart of accounts template
- Month-end closing checklist (15 steps)
- QBO / Xero setup guide
- Client outreach email templates
- Notion databases: client CRM, task tracker, revenue log
- 52-week content calendar for social media
- Services overview pitch deck
- Tax prep checklist for clients
- Complete guide PDF

WHO IT'S FOR: Freelance bookkeepers, accounting professionals, and small firm owners building a scalable client base.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "bookkeeping business, bookkeeper os, accounting tools, bookkeeper crm, bookkeeping kit, client tracker, accounting business, bookkeeper system, financial services, bookkeeping planner, small biz cpa kit, digital download, instant download"
},

# ─── 04 ───────────────────────────────────────────────────────────────────────
{
"file": "04_RealEstateAgent.txt",
"title": "Real Estate Agent OS | Lead Tracker, Listing System, Client CRM, Marketing Plan, 70+ Files",
"description": """\
The complete operating system for real estate agents who want to close more deals and run a more organized business. Every system from lead generation to closing -- in one download.

WHAT'S INSIDE:
- Business plan with GCI goal calculator
- Lead tracking CRM (Excel): source, status, follow-up date
- Buyer and seller consultation framework
- Listing presentation template (PowerPoint, Canva-ready)
- Open house sign-in sheet and follow-up sequence
- Buyer guide and seller guide templates
- Transaction coordinator checklist (30-step closing process)
- Email and text follow-up scripts (10 templates)
- Social media content calendar (52 weeks)
- Referral tracking and past client re-engagement system
- Notion databases: lead CRM, listing tracker, closing checklist
- Marketing plan: sphere, farming, digital lead gen
- KPI dashboard: conversion rate, GCI, pipeline value
- Complete guide PDF

WHO IT'S FOR: New and experienced real estate agents and realtors building a systemized, scalable business.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "real estate agent, realtor tools, real estate os, lead tracker crm, listing system, realtor business, real estate crm, agent templates, property tracker, realtor planner, home buyer guide, digital download, instant download"
},

# ─── 05 ───────────────────────────────────────────────────────────────────────
{
"file": "05_InsuranceAgency.txt",
"title": "Insurance Agency OS | Client CRM, Policy Tracker, Sales Pipeline, Referral System, 60+ Files",
"description": """\
Run a professional, organized insurance agency with this complete operating system. Built for independent insurance agents and agency owners who want better client management and higher retention.

WHAT'S INSIDE:
- Agency business plan with revenue and commission projections
- Client CRM (Excel): policy type, renewal date, premium, status
- Policy renewal tracker with automated alert system
- Sales pipeline tracker (prospect to bound policy)
- Referral partner system (attorneys, CPAs, realtors)
- Client needs analysis questionnaire
- Quote follow-up email sequences (5 templates)
- Claims support workflow for clients
- Annual policy review checklist
- Cross-sell and upsell opportunity tracker
- Notion databases: client CRM, policy tracker, referral log
- Agency pitch deck for referral partner presentations
- KPI dashboard: retention rate, premium volume, conversion
- Complete guide PDF

WHO IT'S FOR: Independent insurance agents and agency owners in P&C, life, health, or multi-line insurance.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "insurance agency, insurance agent os, policy tracker, insurance crm, agency templates, insurance sales, client management, insurance business, agent business kit, insurance planner, sales pipeline, digital download, instant download"
},

# ─── 06 ───────────────────────────────────────────────────────────────────────
{
"file": "06_AISocialMediaAgency.txt",
"title": "AI Social Media Agency OS | Client Management, Content System, Pricing, 80+ Files",
"description": """\
Launch and run a profitable AI-powered social media marketing agency with this complete operating system. Every system, template, and tool you need -- from landing your first client to delivering results at scale.

WHAT'S INSIDE:
- Business plan with pricing tiers and revenue projections
- Service menu (30+ SMMA services with pricing)
- Client proposal and pitch deck template
- Social media management contract (Word, fully editable)
- Client onboarding system and welcome pack
- 90-day content calendar template (all platforms)
- AI content creation workflow (ChatGPT + Canva)
- Monthly reporting template for clients
- Lead generation outreach scripts (email + DM)
- Cold outreach email sequence (5-email flow)
- Notion databases: client CRM, content tracker, revenue log
- Agency pitch deck (PowerPoint, Canva-importable)
- KPI dashboard: reach, engagement, leads, ROI
- Tools and tech stack guide (20 essential tools)
- Complete guide PDF

WHO IT'S FOR: Social media agency founders, freelance social media managers, and digital marketers ready to build a client-based business.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "social media agency, smma business kit, agency starter kit, social media tools, content calendar, client management, agency templates, digital marketing, business planner, smma templates, freelancer tools, digital download, instant download"
},

# ─── 07 ───────────────────────────────────────────────────────────────────────
{
"file": "07_BookkeeperLaunchSystem.txt",
"title": "Bookkeeper Practice Launch Kit | Client Tracker, Pricing, Contracts, 50+ Files | Instant Download",
"description": """\
Start your bookkeeping practice the right way with this complete launch system. Designed specifically for people transitioning into bookkeeping or launching their first solo practice.

WHAT'S INSIDE:
- 12-month business plan with milestone roadmap
- Niche selection guide (8 best bookkeeping niches)
- Tiered service packages with pricing calculator (Excel)
- Bookkeeping service agreement (Word, legally structured)
- Client database tracker (8 sample clients pre-filled)
- Month-end closing checklist (15 tasks)
- Chart of accounts template (24 standard accounts)
- Tax planning guide for clients
- 52-week social media content calendar (CSV)
- LinkedIn + Facebook outreach email scripts
- Client welcome packet template
- Services overview presentation (PowerPoint)
- Notion databases: client CRM, task log, income tracker
- QBO onboarding guide for new clients
- Complete guide PDF

WHO IT'S FOR: New bookkeepers, accounting graduates, and professionals launching a solo bookkeeping practice.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "bookkeeper business, bookkeeping launch, accounting templates, bookkeeper startup, client onboarding, bookkeeper kit, accounting business, bookkeeper tools, financial templates, small business cpa, bookkeeper planner, digital download, instant download"
},

# ─── 08 ───────────────────────────────────────────────────────────────────────
{
"file": "08_StaffingAgency.txt",
"title": "Staffing Agency OS | Candidate Pipeline, Fee Calculator, LinkedIn Sourcing, 60+ Files",
"description": """\
Build and run a professional staffing and recruitment agency with this complete operating system. From business setup to candidate placement -- every tool, template, and system you need.

WHAT'S INSIDE:
- Business plan with fee structure (contingency + retained)
- Staffing fee calculator (Excel): placement fees by salary level
- Candidate pipeline tracker (8 stages, 8 sample candidates)
- Candidate scorecard and assessment framework
- LinkedIn sourcing playbook with Boolean search strings
- Client service agreement (Word, fully editable)
- Job order intake template
- Recruiter call scripts vault (client + candidate scripts)
- Compliance checklist (EEOC, FLSA, background check)
- Notion databases: candidate CRM, client tracker, job orders, glossary
- Agency pitch deck and candidate profile template (PowerPoint)
- 90-day business launch plan
- KPI dashboard: fill rate, time-to-fill, gross margin
- Complete guide PDF

WHO IT'S FOR: Independent recruiters, boutique staffing agency founders, and HR professionals going independent.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "staffing agency kit, recruiting business, recruitment agency, staffing templates, candidate tracker, recruiter toolkit, agency business kit, hr business tools, staffing planner, talent acquisition, hiring manager tool, digital download, instant download"
},

# ─── 09 ───────────────────────────────────────────────────────────────────────
{
"file": "09_AIAutomationAgency.txt",
"title": "AI Automation Agency Kit | 30 Blueprints, Proposal Templates, Client System, 55+ Files",
"description": """\
Launch an AI automation agency and sell done-for-you workflow automation to businesses -- no coding required. Includes 30 ready-to-sell automation blueprints across 9 industries.

WHAT'S INSIDE:
- Business plan with service tiers and pricing model
- 30 automation blueprints (lead gen, email, e-commerce, real estate, healthcare, finance, and more)
- Financial model and pricing calculator (Excel)
- Lead pipeline tracker with outreach status
- 5-phase client delivery SOP
- Automation proposal template (Word, fully editable)
- Service menu (30+ automation services)
- AI tools directory (20 essential tools with pricing)
- Cold outreach email templates
- Notion databases: client projects, automation library, revenue tracker
- Agency pitch deck (PowerPoint, Canva-importable)
- Notion setup guide
- Complete guide PDF

WHO IT'S FOR: Entrepreneurs, freelancers, and consultants who want to build an automation agency using Make.com, Zapier, or n8n -- no coding needed.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "ai automation kit, automation agency, ai business tools, automation startup, ai agency starter, workflow automation, automation templates, ai entrepreneur, business automation, make.com templates, zapier templates, digital download, instant download"
},

# ─── 10 ───────────────────────────────────────────────────────────────────────
{
"file": "10_VABusiness.txt",
"title": "Virtual Assistant Business OS | Contracts, Pricing, 80+ Services, SOPs, 60+ Files",
"description": """\
Launch and scale a professional virtual assistant business with this complete operating system. Everything from your first client outreach to running a full VA practice -- in one download.

WHAT'S INSIDE:
- Business plan with niche options (admin, social media, executive VA)
- Tiered service packages with pricing calculator (4 packages)
- VA service agreement + NDA (Word, fully editable)
- 80-service menu with descriptions and pricing guidance
- LinkedIn and Facebook outreach scripts
- Discovery call framework and script
- SOPs for 20 common VA tasks
- Tech stack guide (20 essential tools)
- Notion databases: client CRM, task tracker, income log
- 52 client email templates (CSV)
- VA services pitch deck (PowerPoint, Canva-importable)
- Client onboarding checklist and welcome packet
- Rate increase email templates
- Complete guide PDF

WHO IT'S FOR: Freelance VAs, online business managers, and executive assistants transitioning to independent work.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "virtual assistant, va business kit, va starter kit, freelancer tools, remote work tools, va business plan, online business os, va client tracker, freelance business, va service menu, va templates, digital download, instant download"
},

# ─── 11 ───────────────────────────────────────────────────────────────────────
{
"file": "11_AirbnbCoHost.txt",
"title": "Airbnb CoHost System | Co-Host Agreement, Revenue Dashboard, Guest Templates, 50+ Files",
"description": """\
Build a professional Airbnb co-hosting business with this complete management system. Everything you need to pitch property owners, manage listings, and deliver 5-star guest experiences.

WHAT'S INSIDE:
- Co-host pitch deck for property owner presentations
- Portfolio and booking tracker (5 properties, Excel)
- Co-host management agreement (Word, fully editable)
- Fee structure guide: typical co-host commission rates
- Guest message templates for every situation (7 templates)
- Turnover cleaning checklist (kitchen, bathrooms, bedrooms, final check)
- Revenue dashboard with dynamic pricing guide (Excel)
- Maintenance request tracker
- House rules template
- Notion databases: property tracker, booking log, maintenance log
- 90-day business launch plan
- Guest review response templates
- Complete guide PDF

WHO IT'S FOR: Airbnb co-hosts, property managers, and short-term rental entrepreneurs managing properties for others.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "airbnb cohost, airbnb host tools, cohost management, airbnb templates, property manager, short term rental, airbnb business, rental management, cohost contract, airbnb planner, str management, digital download, instant download"
},

# ─── 12 ───────────────────────────────────────────────────────────────────────
{
"file": "12_NotionClientPortal.txt",
"title": "Notion Client Portal for Agencies | 5 Databases, KPI Dashboard, Project Tracker | Download",
"description": """\
Set up a professional Notion client portal for your agency in hours. Includes everything from client onboarding to project delivery -- fully structured and ready to import.

WHAT'S INSIDE:
- 5 Notion-importable CSV databases:
  - Client Master Database
  - Project Tracker
  - Content Calendar
  - Invoice and Payments Log
  - Analytics Report Log
- Sprint board and deliverables tracker (CSV)
- Client onboarding workbook (Word)
- Monthly report template (Word)
- Agency-client communication SOP (Word)
- Agency KPI Dashboard (Excel): revenue, utilization, project health
- Complete Notion setup guide (Markdown)
- Client portal overview pitch deck (PowerPoint, Canva-importable)
- Asset manifest

WHO IT'S FOR: Agency owners, freelancers, and consultants who want a professional Notion workspace to manage clients and projects.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, Markdown\
""",
"tags": "notion template, client portal, agency notion kit, client management, project tracker, notion dashboard, agency templates, client onboarding, notion workspace, client database, freelancer notion, digital download, instant download"
},

# ─── 13 ───────────────────────────────────────────────────────────────────────
{
"file": "13_UGCBrandDealKit.txt",
"title": "UGC Creator Brand Deal Kit | Rate Card, Contracts, 50 Hooks, Pitch Templates, 50+ Files",
"description": """\
Land your first brand deal (and your 10th) with this complete UGC creator business system. Everything a content creator needs to run a professional brand partnership business from day one.

WHAT'S INSIDE:
- Rate card system with pricing calculator (Excel)
- Media kit creation guide
- Brand pitch playbook (10+ email templates + DM scripts)
- UGC service agreement (Word, fully editable)
- Content brief template to send every brand
- 50 proven scroll-stopping UGC hooks
- 5-step production workflow (brief to delivery)
- Content performance analytics dashboard (Excel)
- Negotiation scripts for every scenario
- Client onboarding and delivery system
- Notion databases: brand deal tracker, content library, income log
- Creator pitch deck (PowerPoint, Canva-importable)
- Annual revenue planner
- Complete guide PDF

WHO IT'S FOR: UGC creators, content creators, and social media freelancers ready to build a professional brand deal business.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "ugc creator kit, brand deal kit, ugc templates, ugc contract, ugc rate card, creator business, brand pitch kit, ugc outreach, content creator, ugc media kit, brand deal tools, digital download, instant download"
},

# ─── 14 ───────────────────────────────────────────────────────────────────────
{
"file": "14_CreatorSponsorshipTracker.txt",
"title": "Creator Sponsorship Tracker | Brand Deals, Income, YouTube Instagram TikTok, 50+ Files",
"description": """\
Track every brand deal from first pitch to final payment with this complete sponsorship management system. Built for creators on YouTube, Instagram, and TikTok who want professional systems for managing sponsorships.

WHAT'S INSIDE:
- Master sponsorship tracker (Excel, 10 columns, 10 sample deals)
- 8-stage brand deal pipeline (outreach to paid)
- Income and tax tracker with quarterly estimates
- Monthly sponsored content calendar (Excel)
- Full 12-month annual content plan (CSV)
- Brand pitch system with templates for every platform
- Channel analytics dashboard (subscribers, views, CTR)
- Video performance tracker (views, engagement, sponsor revenue)
- Full sponsorship agreement template (Word)
- Invoice guide and recommended tools
- Notion databases: sponsorship master DB, brand contact database
- YouTube, Instagram, and TikTok-specific playbooks (Word)
- Sponsorship rate guide by platform and follower count
- Creator pitch deck (PowerPoint, Canva-importable)
- Complete guide PDF

WHO IT'S FOR: YouTube creators, Instagram influencers, and TikTok creators ready to manage sponsorships like a business.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "sponsorship tracker, brand deal tracker, creator income, youtube sponsor, influencer tools, creator contract, sponsor tracker, content creator, creator business, instagram deals, tiktok sponsor, digital download, instant download"
},

# ─── 15 ───────────────────────────────────────────────────────────────────────
{
"file": "15_EtsySEOSystem.txt",
"title": "Etsy SEO Listing System | AI Prompts, Keywords, Title Templates, Tag Vault, 60+ Files",
"description": """\
Get your Etsy listings found in search with this complete SEO system. The exact keyword strategy, title formulas, tag vaults, and AI prompts used by top Etsy sellers -- in one download.

WHAT'S INSIDE:
- Etsy SEO masterclass (how Etsy search actually works)
- 5-source keyword research method + tracker (Excel)
- 200+ listing title formula templates by category
- 3 complete description templates (digital, physical, custom)
- 13-tag framework with 6 ready-to-use tag sets
- Tag vault database (CSV, 78 validated tags with character counts)
- 6 AI prompts for ChatGPT, Claude, and Gemini:
  - Complete listing generator (title + tags + description)
  - Title optimizer (3 variations)
  - Tag generator with volume ratings
  - Description rewriter with headers and FAQ
  - Keyword research assistant (60+ keywords)
  - Seasonal listing optimizer
- Shop optimization guide (shop title, sections, About, policies)
- Analytics tracker (views, conversion, revenue by listing)
- Notion databases: listing SEO DB, keyword master database
- Niche keyword packs (300+ keywords across digital, gifts, home decor)
- 30-point Etsy SEO audit checklist
- Etsy SEO pitch deck (PowerPoint, Canva-importable)
- Complete guide PDF

WHO IT'S FOR: New and experienced Etsy sellers who want more organic search traffic without paid ads.

INSTANT DOWNLOAD: All files available immediately after purchase.
FORMATS: Excel, Word, CSV (Notion-importable), PowerPoint, PDF\
""",
"tags": "etsy seo system, etsy listing tips, etsy keywords, etsy tag template, etsy title help, etsy seller tools, etsy seo guide, etsy description, etsy ai prompts, etsy shop help, etsy printable, digital download, instant download"
},

]  # end PRODUCTS


# ── Write each file ────────────────────────────────────────────────────────────
for p in PRODUCTS:
    path = OUT + p["file"]
    with open(path, "w", encoding="utf-8") as f:
        f.write("TITLE:\n")
        f.write(p["title"] + "\n\n")
        f.write("DESCRIPTION:\n")
        f.write(p["description"] + "\n\n")
        f.write("TAGS:\n")
        f.write(p["tags"] + "\n")
    print(f"  wrote {p['file']}")

print(f"\nAll {len(PRODUCTS)} listing files written to {OUT}")

# ── Verify tag lengths ─────────────────────────────────────────────────────────
print("\nTag length audit:")
for p in PRODUCTS:
    tags = [t.strip() for t in p["tags"].split(",")]
    bad = [t for t in tags if len(t) > 20]
    status = "OK" if not bad else f"OVER 20: {bad}"
    count = len(tags)
    print(f"  {p['file']}: {count} tags -- {status}")
