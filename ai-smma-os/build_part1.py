#!/usr/bin/env python3
"""AI SMMA OS - Part 1: Folders 00,01,02 + Lead_Tracker_CRM.xlsx + Social_Media_Audit_Template.xlsx"""
import os, csv
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/ai-smma-os/Ultimate_AI_SMMA_Operating_System/"
NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"

FOLDERS = [
    "00_START_HERE","01_AGENCY_SETUP","02_CLIENT_ACQUISITION","03_PROPOSALS_CONTRACTS",
    "04_CLIENT_ONBOARDING","05_CONTENT_CREATION","06_SOCIAL_MEDIA_MANAGEMENT",
    "07_CLIENT_REPORTING","08_AI_TOOLS_STACK","09_BUSINESS_OPERATIONS",
    "10_NOTION_WORKSPACE","11_BONUSES","12_CANVA_TEMPLATES",
]
for folder in FOLDERS:
    os.makedirs(BASE + folder, exist_ok=True)
print("✓ All 13 folders created")

def doc(filename, title, subtitle, sections):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
    if subtitle:
        s = d.add_paragraph(subtitle); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10)
        s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
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

def xlsx_header_fill(): return PatternFill("solid", fgColor=NAV)
def xlsx_alt_fill(): return PatternFill("solid", fgColor=LGR)
def xlsx_white_fill(): return PatternFill("solid", fgColor=WHT)
def hdr_font(): return Font(bold=True, color=WHT, size=11)
def nav_font(): return Font(bold=True, color=NAV, size=11)
def set_col_widths(ws, widths):
    for col, width in widths.items():
        ws.column_dimensions[col].width = width

# ─── 00_START_HERE ─────────────────────────────────────────────────────────────
with open(BASE+"00_START_HERE/README_FIRST.txt","w",encoding="utf-8") as f:
    f.write("""WELCOME TO YOUR ULTIMATE AI SOCIAL MEDIA AGENCY OPERATING SYSTEM
=================================================================
Original Value: €297 | Your Launch Price: €69

Congratulations! You now own the most comprehensive AI-powered Social Media Marketing
Agency (SMMA) operating system available. This is not a collection of random templates —
it is a fully integrated business management system built by agency owners, for agency owners.

WHAT'S INSIDE (70+ Professional Files):
-----------------------------------------
00_START_HERE          → You are here! Read this first. 7-day quick start guide.
01_AGENCY_SETUP        → Brand guide, service menu, SOPs, niche framework
02_CLIENT_ACQUISITION  → Cold DM scripts, cold emails, discovery call, objections, CRM
03_PROPOSALS_CONTRACTS → Proposal guide, retainer agreement, NDA, pricing calculator
04_CLIENT_ONBOARDING   → Onboarding SOP, welcome emails, brand questionnaire, audit template
05_CONTENT_CREATION    → Content SOPs, caption frameworks, hashtag strategy, AI prompt library
06_SOCIAL_MEDIA_MANAGEMENT → Platform strategies, community management, content calendar
07_CLIENT_REPORTING    → Monthly report guide, weekly updates, KPI dashboard
08_AI_TOOLS_STACK      → AI tools guide, ChatGPT workflows, Midjourney prompts
09_BUSINESS_OPERATIONS → Business plan, churn prevention, team management, revenue tracker
10_NOTION_WORKSPACE    → 8 Notion databases + comprehensive setup guide
11_BONUSES             → 365 social media captions, scripts vault, growth playbook
12_CANVA_TEMPLATES     → 4 professional presentation templates (PPTX, Canva-importable)

QUICK START (1 HOUR):
----------------------
1. Read Quick_Start_7Day_Guide.docx — your day-by-day setup roadmap
2. Import the 8 CSVs from 10_NOTION_WORKSPACE into Notion
3. Upload PPTX files from 12_CANVA_TEMPLATES to Canva.com
4. Customize Brand_Identity_Guide.docx with your agency details
5. Open Lead_Tracker_CRM.xlsx and enter your first 10 prospects
6. Schedule your first discovery call using Discovery_Call_Script.docx
7. Post your first content using 365_Social_Media_Captions.csv

IMPORTANT NOTES:
-----------------
- All DOCX files: Replace [Agency Name], [Your Name], [Your Email] with your details
- All XLSX files: Sample data is included — replace with your real data
- PPTX files: Upload to Canva.com for easy design customization
- CSVs: Import directly into Notion (Database > Import > CSV)
- This product is for personal use in your own agency — do not resell

Ultimate AI SMMA Operating System | Professional Edition | Version 1.0
Purchased from Etsy | Digital Download | No Refunds on Digital Products
""")
print("  ✓ 00_START_HERE/README_FIRST.txt")

doc("00_START_HERE/Quick_Start_7Day_Guide.docx",
    "Quick Start 7-Day Setup Guide",
    "Ultimate AI SMMA OS | From Download to Running Agency in 7 Days",
    [
        ("Welcome — How to Use This Guide", [
            "This 7-day guide is designed to take you from zero to a fully operational social media marketing agency. Each day has specific, actionable tasks that build on each other. Do not skip ahead — the order matters. By day 7, you will have your agency brand established, your first systems running, and your outreach pipeline active.",
            ("•", "Time commitment: 2-4 hours per day for 7 days"),
            ("•", "What you need: A laptop, internet access, a Notion account (free), and Canva (free)"),
            ("•", "Goal: By Day 7, you will have sent your first 20 outreach messages and have your agency ready for clients"),
        ]),
        ("Day 1 — Foundation and Brand", [
            "Your first day is about establishing your agency identity. Nothing else happens effectively until you know who you are, what you do, and who you serve.",
            ("•", "Open Brand_Identity_Guide.docx and complete every section — agency name, tagline, colors, fonts, target niche"),
            ("•", "Open Service_Menu_and_Pricing.docx and decide which 2-3 packages you will lead with as a new agency"),
            ("•", "Open Niche_Selection_Framework.docx and commit to your primary niche for the first 90 days"),
            ("•", "Create your agency email address (yourname@youragency.com or Gmail with agency name)"),
            ("•", "Set up a simple Linktree or landing page with your agency name and contact info"),
            ("•", "Day 1 Success Metric: Your agency has a name, a niche, and a contact method"),
        ]),
        ("Day 2 — Systems Setup", [
            "Today you build the infrastructure that will run your agency. These are one-time setup tasks that will save you hundreds of hours over the coming months.",
            ("•", "Import all 8 CSVs from 10_NOTION_WORKSPACE into Notion (follow Notion_Setup_Guide.md exactly)"),
            ("•", "Open Lead_Tracker_CRM.xlsx and familiarize yourself with the pipeline columns"),
            ("•", "Upload all 4 PPTX files from 12_CANVA_TEMPLATES to Canva.com"),
            ("•", "Customize the Agency_Proposal_Template.pptx with your agency name, colors, and services"),
            ("•", "Open Agency_Revenue_Tracker.xlsx and enter your monthly financial goals for the next 6 months"),
            ("•", "Set up a simple project management system using Team_Tasks.csv in Notion"),
            ("•", "Day 2 Success Metric: Notion workspace is live, CRM is ready, proposal template is branded"),
        ]),
        ("Day 3 — Client Acquisition Prep", [
            "Today you prepare your outreach. You will not send anything yet — today is about having everything ready so that tomorrow you can move fast.",
            ("•", "Open Cold_DM_Scripts.docx and select 3 scripts that feel natural to you. Personalize each one"),
            ("•", "Open Cold_Email_Templates.docx and customize 2 templates for your niche"),
            ("•", "Open Objection_Handling_Scripts.docx and practice the top 10 responses out loud"),
            ("•", "Create a list of 50 target businesses in your niche — use Instagram, Google, or LinkedIn"),
            ("•", "Enter all 50 leads into Lead_Tracker_CRM.xlsx with their platform, contact info, and estimated package"),
            ("•", "Review Discovery_Call_Script.docx — read the entire 60-minute script and understand each section"),
            ("•", "Day 3 Success Metric: 50 qualified leads in your CRM, outreach scripts are personalized and ready"),
        ]),
        ("Day 4 — First Outreach Wave", [
            "Today you launch your outreach. The goal is not to close clients — the goal is to start conversations. Done is better than perfect.",
            ("•", "Send 10 cold DMs on Instagram using Cold_DM_Scripts.docx Script 1"),
            ("•", "Send 5 LinkedIn connection requests with your personalized message"),
            ("•", "Send 5 cold emails using Cold_Email_Templates.docx Template A with your niche customizations"),
            ("•", "Update Lead_Tracker_CRM.xlsx with Last Contact date and Next Step for all 20 outreaches"),
            ("•", "Set follow-up reminders in your calendar for Day 3 and Day 7 of each outreach"),
            ("•", "If anyone responds today — use the Discovery_Call_Script.docx to book a call"),
            ("•", "Day 4 Success Metric: 20 outreach messages sent, all logged in CRM, follow-up dates set"),
        ]),
        ("Day 5 — Content and AI Workflow", [
            "Today you set up your content production system. This is how you deliver results for clients and create content for your own agency brand.",
            ("•", "Open AI_Prompt_Library.docx and test 10 prompts in ChatGPT — save the results that impress you"),
            ("•", "Open Content_Creation_SOP.docx and map your workflow: brief → draft → design → review → schedule"),
            ("•", "Open Caption_Writing_Framework.docx and write 5 captions using AIDA, PAS, and storytelling frameworks"),
            ("•", "Set up your own agency's social media posting schedule using Content_Calendar_Tracker.xlsx"),
            ("•", "Create your first 7 pieces of content for your agency's own social media using AI_Prompt_Library.docx"),
            ("•", "Open AI_Content_Production_SOP.docx and build your human-AI hybrid workflow"),
            ("•", "Day 5 Success Metric: 7 pieces of agency content ready to post, AI workflow documented"),
        ]),
        ("Day 6 — Discovery Calls and Proposals", [
            "By Day 6, you should have at least 1-3 positive responses from your outreach. Today you prepare to have those conversations and close your first client.",
            ("•", "If you have a discovery call booked: rehearse Discovery_Call_Script.docx section by section"),
            ("•", "Open Proposal_Writing_Guide.docx and understand the 7-section proposal structure"),
            ("•", "Customize Agency_Proposal_Template.pptx in Canva for your first prospect"),
            ("•", "Open SMMA_Retainer_Agreement_Template.docx and customize with your agency details"),
            ("•", "Review Pricing_Calculator.xlsx — know your numbers before every sales conversation"),
            ("•", "If no responses yet: send 10 more DMs and 5 more emails from your lead list"),
            ("•", "Day 6 Success Metric: Proposal template is ready, contract is customized, you are prepared to close"),
        ]),
        ("Day 7 — Launch and Momentum", [
            "Day 7 is your official launch day. You now have systems, scripts, templates, and prospects. The goal today is to commit to your weekly routine and plant seeds for your first client.",
            ("•", "Post your first piece of content on your agency social media — use 365_Social_Media_Captions.csv Day 1"),
            ("•", "Send your Day 3 follow-ups to everyone you contacted on Day 4"),
            ("•", "Schedule your next 4 weeks of outreach in your calendar (20 messages per day, 5 days per week)"),
            ("•", "Read Agency_Growth_Playbook.docx — commit to the Month 1-3 plan"),
            ("•", "Open Annual_Business_Plan.docx and set your 90-day revenue goal"),
            ("•", "Join 2 SMMA Facebook groups and introduce yourself to the community"),
            ("•", "Day 7 Success Metric: You are a running agency with systems, a pipeline, and a weekly routine"),
        ]),
        ("Week 2+ — Your Weekly Rhythm", [
            "After your first 7 days, maintain this weekly rhythm to grow consistently:",
            ("•", "Monday: Review CRM, plan the week, set outreach targets"),
            ("•", "Tuesday-Thursday: Active outreach (20+ messages/day), discovery calls, proposal sends"),
            ("•", "Friday: Follow-ups, client reporting, content scheduling for next week"),
            ("•", "Daily: 30 minutes of engagement on your agency social media"),
            ("•", "Monthly: Review KPI_ROI_Dashboard.xlsx, update Agency_Revenue_Tracker.xlsx, plan next month"),
            ("•", "Quarterly: Review service pricing, update packages, refresh proposal templates"),
        ]),
    ])

doc("00_START_HERE/Product_Overview.docx",
    "Product Overview — Ultimate AI SMMA Operating System",
    "Everything You Need to Run a Professional, Profitable Social Media Marketing Agency",
    [
        ("What Is the AI SMMA Operating System?", [
            "The Ultimate AI Social Media Marketing Agency (SMMA) Operating System is a comprehensive, professional toolkit designed for agency owners who are serious about building a sustainable, scalable business. Unlike generic social media templates, this system covers every aspect of running an agency — from your first cold DM to managing a team of freelancers and reporting to 10+ clients simultaneously.",
            "Built by combining the best practices of successful SMMA owners with the power of modern AI tools, this system gives you a significant competitive advantage from day one. You are not starting from scratch — you are starting from where experienced agency owners left off.",
        ]),
        ("What Makes This Different", [
            ("•", "Completeness: 70+ files covering every stage of agency operations — nothing is missing"),
            ("•", "AI-First Design: The AI_Prompt_Library.docx alone contains 200 specific, tested prompts for SMMA workflows"),
            ("•", "Real-World Scripts: Every script, template, and SOP was written for actual agency use — not theoretical"),
            ("•", "Multi-Platform System: Covers Instagram, LinkedIn, TikTok, Facebook, and X (Twitter) strategies"),
            ("•", "Professional Quality: Canva-ready PPTX presentations that match agency-grade design standards"),
            ("•", "Notion Integration: 8 databases ready to import — your entire business in one workspace"),
            ("•", "Financial Tools: Revenue tracker, pricing calculator, and P&L sheet for business control"),
        ]),
        ("Who Is This For?", [
            ("•", "New SMMA owners who want to skip the 12-month learning curve and launch with professional systems"),
            ("•", "Existing agency owners who are disorganized and need to systematize their operations"),
            ("•", "Freelancers transitioning from individual gig work to a scalable agency model"),
            ("•", "Digital marketing professionals who want to add SMMA services to their existing business"),
            ("•", "Entrepreneurs who see the SMMA business model and want a complete roadmap to execute it"),
        ]),
        ("Complete File Directory", [
            ("•", "00_START_HERE: README_FIRST.txt, Quick_Start_7Day_Guide.docx, Product_Overview.docx, Asset_Manifest.csv/.json"),
            ("•", "01_AGENCY_SETUP: Brand Identity Guide, Service Menu & Pricing, Agency SOPs, Niche Selection Framework"),
            ("•", "02_CLIENT_ACQUISITION: Cold DM Scripts, Cold Email Templates, Discovery Call Script, Objection Handling, Lead Tracker CRM"),
            ("•", "03_PROPOSALS_CONTRACTS: Proposal Writing Guide, Retainer Agreement, NDA, Pricing Calculator"),
            ("•", "04_CLIENT_ONBOARDING: Onboarding SOP, Welcome Email Sequence, Brand Questionnaire, Platform Access Guide, Social Media Audit"),
            ("•", "05_CONTENT_CREATION: Content Creation SOP, Caption Writing Framework, Hashtag Strategy Guide, AI Prompt Library, Visual Brief Template"),
            ("•", "06_SOCIAL_MEDIA_MANAGEMENT: Instagram, LinkedIn, TikTok, Facebook Strategy Guides, Community Management SOP, Content Calendar"),
            ("•", "07_CLIENT_REPORTING: Monthly Report Guide, Weekly Update Script, Reporting SOP, KPI ROI Dashboard"),
            ("•", "08_AI_TOOLS_STACK: AI Tools Guide, ChatGPT Workflow SOPs, AI Content Production SOP, Midjourney Prompt Pack"),
            ("•", "09_BUSINESS_OPERATIONS: Annual Business Plan, Client Churn Prevention, Team & Freelancer Management, Revenue Tracker"),
            ("•", "10_NOTION_WORKSPACE: 8 CSV databases + Notion Setup Guide + Complete User Guide PDF"),
            ("•", "11_BONUSES: 365 Social Media Captions, SMMA Scripts Vault, Agency Growth Playbook"),
            ("•", "12_CANVA_TEMPLATES: Agency Proposal, Monthly Client Report, Social Media Strategy Deck, Case Study (all PPTX)"),
        ]),
        ("License and Usage", [
            ("•", "Personal Use License: Use in your own agency with unlimited clients"),
            ("•", "Customization: Fully customize all templates, logos, colors, and content"),
            ("•", "Team Use: Share with your agency team members and freelancers"),
            ("•", "Restrictions: Do not resell, redistribute, or offer as your own product"),
            ("•", "No refunds on digital downloads — please contact Etsy support if you have issues accessing your files"),
        ]),
    ])

print("✓ 00_START_HERE complete")

# ─── 01_AGENCY_SETUP ──────────────────────────────────────────────────────────
p01 = "01_AGENCY_SETUP/"

doc(p01+"Brand_Identity_Guide.docx",
    "Agency Brand Identity Guide",
    "Ultimate AI SMMA OS | Define Your Agency Brand, Positioning, and Voice",
    [
        ("Why Brand Identity Matters for Your SMMA", [
            "In the crowded social media agency marketplace, your brand is often the first thing a potential client evaluates before ever speaking to you. A professional, consistent brand signals credibility, authority, and attention to detail — all qualities clients expect in an agency that will manage their brand. This guide walks you through building a complete brand identity system that positions you as a premium agency worthy of premium prices.",
            ("•", "Agencies with strong brand identities command 30-50% higher retainers than faceless competitors"),
            ("•", "Your brand should communicate your niche, your results, and your personality at first glance"),
            ("•", "Consistency across all touchpoints (website, social, proposals, emails) builds trust"),
        ]),
        ("Agency Name Strategy", [
            "Your agency name is your most permanent brand decision. Choose carefully. The best SMMA names fall into these categories:",
            ("•", "Founder Name + Agency: '[Your Name] Media', '[Last Name] Social' — personal brand approach, good for solo operators"),
            ("•", "Outcome-Focused: 'Growthify', 'Reach Labs', 'ClickFlow Agency' — communicates what you deliver"),
            ("•", "Premium/Abstract: 'Apex Social', 'Pinnacle Media', 'Luminary Creative' — signals quality without limiting scope"),
            ("•", "Niche-Specific: 'RestaurantReach', 'RealEstate Social', 'CoachLaunch' — clear target market"),
            "Action: Write 5 potential agency names. Test each against: Is it memorable? Easy to spell? Available as a domain? Available as a social handle?",
            "[FILL IN] My Agency Name: _______________",
            "[FILL IN] Tagline (8 words or less): _______________",
        ]),
        ("Visual Brand Identity", [
            "Your visual identity should be professional and consistent. You do not need an expensive designer — Canva Pro has everything you need.",
            ("•", "Primary Color: Your main brand color (navy, black, and deep blue signal premium; bright colors signal energy)"),
            ("•", "Accent Color: Used for CTAs, highlights, and visual interest (often a contrasting warm color)"),
            ("•", "Font Pairing: One bold display font for headlines + one clean sans-serif for body text"),
            ("•", "Logo Style: Text-based logos (wordmarks) work well for agencies — simple and professional"),
            "[FILL IN] Primary Color (hex): _______________",
            "[FILL IN] Accent Color (hex): _______________",
            "[FILL IN] Primary Font: _______________ | Secondary Font: _______________",
        ]),
        ("Agency Positioning Statement", [
            "Your positioning statement defines who you help, how you help them, and what makes you different. It guides all your messaging.",
            "Template: 'We help [TARGET NICHE] businesses [SPECIFIC OUTCOME] through [YOUR METHOD] so they can [ULTIMATE BENEFIT].'",
            "Example 1: 'We help e-commerce brands scale to 7 figures through AI-powered social media advertising and organic content so they can reduce CAC and grow without adding headcount.'",
            "Example 2: 'We help local restaurant owners fill their tables through high-converting Instagram and Google campaigns so they can stop relying on delivery apps and own their customers.'",
            "[FILL IN] Your Positioning Statement: _______________",
        ]),
        ("Elevator Pitch (30 Seconds)", [
            "Script A — Discovery Event Version:",
            '"I run a social media marketing agency that specializes in [niche]. Most [niche] businesses I talk to are posting consistently but not seeing real business results from it. We fix that — we build a complete social strategy tied to actual revenue goals, not just likes. Our clients typically see a [X]% increase in inquiries within the first 60 days."',
            "Script B — Direct Message Version:",
            '"Hey [Name], I help [niche] businesses grow through social media. I came across your profile and noticed your content has great potential — I think there are some specific things we could do to turn your engagement into actual leads. Would you be open to a quick 15-minute chat?"',
            "Script C — LinkedIn Version:",
            '"I specialize in AI-powered social media management for [niche] businesses. My agency focuses exclusively on [niche] so we understand the buyer psychology, seasonal patterns, and content formats that actually convert in your industry. Happy to share what\'s been working."',
        ]),
        ("Brand Voice and Tone Guidelines", [
            "Your brand voice should be consistent across all content — social posts, emails, proposals, and calls.",
            ("•", "Professional but Human: Write like an expert who is also a real person — not a corporate robot"),
            ("•", "Results-Oriented: Always connect your communication back to business outcomes, not just vanity metrics"),
            ("•", "Confident without Arrogant: State what you know and what you deliver without overselling"),
            ("•", "Educational: Share knowledge freely in your marketing — expertise is your most valuable signal"),
            ("•", "Words to Use: 'results', 'growth', 'strategy', 'data-driven', 'ROI', 'pipeline', 'scale'"),
            ("•", "Words to Avoid: 'cheap', 'quick fix', 'guaranteed results', 'go viral', 'just posting'"),
        ]),
        ("Competitor Analysis Framework", [
            "Research 5 SMMA agencies in your niche or region. For each, note:",
            ("•", "Their positioning (who they say they help and how)"),
            ("•", "Their pricing (if visible)"),
            ("•", "Their visual brand quality"),
            ("•", "Their case study / social proof strength"),
            ("•", "What they do NOT emphasize (this is your differentiation opportunity)"),
            "The goal is not to copy competitors but to identify gaps in the market where you can position uniquely.",
        ]),
    ])

doc(p01+"Service_Menu_and_Pricing.docx",
    "Service Menu and Pricing Guide",
    "Ultimate AI SMMA OS | 5-Tier Service Structure from €500 to Enterprise",
    [
        ("Pricing Philosophy for SMMA", [
            "Your pricing communicates your value before you say a word. Agencies that price too low attract the worst clients — those who are price-sensitive, demanding, and never satisfied. Premium pricing attracts premium clients who respect your expertise and become long-term partners. This guide outlines a 5-tier structure that allows you to serve different client types while maintaining healthy profit margins at every level.",
            ("•", "Never discount your core packages — offer smaller scopes instead"),
            ("•", "Price for the outcome you deliver, not the hours you spend"),
            ("•", "Raise your prices every 6-12 months as your portfolio grows"),
            ("•", "Always quote retainer fees, not one-off projects — predictable MRR is your business foundation"),
        ]),
        ("Tier 1 — Starter Package: €500/month", [
            "Best For: Local small businesses, solo operators, businesses with limited social media presence",
            "Platforms Managed: 1 platform (Instagram or Facebook)",
            "Included Deliverables:",
            ("•", "12 posts per month (feed posts: mix of graphics and reels)"),
            ("•", "Caption writing and hashtag strategy for every post"),
            ("•", "Community management (responding to comments, 5 days/week)"),
            ("•", "Monthly performance report (reach, engagement, follower growth)"),
            ("•", "Content calendar shared 2 weeks in advance for client approval"),
            "Revision Policy: 1 round of revisions per post batch (4 posts per batch = 3 batches/month)",
            "Response Time: Within 24 hours on business days",
            "Contract Term: 3-month minimum, then rolling monthly",
            "Your Cost to Deliver (estimate): 8-12 hours/month | Profit Margin: 60-70%",
        ]),
        ("Tier 2 — Growth Package: €1,500/month", [
            "Best For: Established local businesses, coaches, consultants, service businesses ready to invest in growth",
            "Platforms Managed: 2 platforms (Instagram + LinkedIn, or Instagram + Facebook)",
            "Included Deliverables:",
            ("•", "20 posts per month across both platforms (format mix: reels, carousels, graphics, stories)"),
            ("•", "Full caption writing, hashtag strategy, and content theme planning"),
            ("•", "Daily community management (comments, DMs, engagement outreach)"),
            ("•", "Monthly strategy call (30 minutes) + detailed performance report"),
            ("•", "Quarterly content strategy review with updated pillars"),
            ("•", "Basic Facebook/Instagram ad management (ad spend up to €500/month excluded)"),
            "Revision Policy: 2 rounds of revisions per content batch",
            "Response Time: Within 12 hours on business days",
            "Contract Term: 3-month minimum, then rolling monthly",
            "Your Cost to Deliver (estimate): 20-25 hours/month | Profit Margin: 55-65%",
        ]),
        ("Tier 3 — Pro Package: €3,000/month", [
            "Best For: Growing brands, e-commerce, coaches with existing audiences, businesses targeting B2B leads",
            "Platforms Managed: 3 platforms (Instagram + LinkedIn + TikTok or Facebook)",
            "Included Deliverables:",
            ("•", "30+ posts per month across all platforms (full multi-format content calendar)"),
            ("•", "Short-form video scripts + direction (client records, we edit)"),
            ("•", "Advanced community management + proactive engagement strategy"),
            ("•", "Facebook/Instagram ad management (ad spend up to €1,500/month excluded)"),
            ("•", "Bi-weekly strategy calls (30 minutes each)"),
            ("•", "Competitor monitoring and monthly trend report"),
            ("•", "Monthly detailed ROI report with next-month strategy document"),
            "Revision Policy: Unlimited revisions within agreed scope",
            "Response Time: Within 4 hours on business days",
            "Contract Term: 6-month minimum",
            "Your Cost to Deliver (estimate): 35-45 hours/month | Profit Margin: 50-60%",
        ]),
        ("Tier 4 — Elite Package: €5,000/month", [
            "Best For: Scale-ups, funded startups, established brands wanting full-service social media management",
            "Platforms Managed: All relevant platforms (Instagram, LinkedIn, TikTok, Facebook, X/Twitter)",
            "Included Deliverables:",
            ("•", "50+ pieces of content per month across all platforms"),
            ("•", "Full video production management (scripting, direction, editing via your team)"),
            ("•", "Paid advertising management on Meta + LinkedIn or TikTok (ad spend up to €5,000 excluded)"),
            ("•", "Weekly strategy calls (45 minutes) + monthly executive presentation"),
            ("•", "Dedicated account manager (client's single point of contact)"),
            ("•", "Influencer outreach and partnership coordination"),
            ("•", "Crisis communications support and brand monitoring"),
            ("•", "Custom monthly analytics dashboard with full attribution reporting"),
            "Revision Policy: Unlimited revisions, rapid turnaround (24-hour)",
            "Response Time: Within 2 hours during business hours; emergency line available",
            "Contract Term: 6-month minimum, quarterly reviews",
            "Your Cost to Deliver (estimate): 60-80 hours/month with team | Profit Margin: 45-55%",
        ]),
        ("Tier 5 — Enterprise: Custom Pricing", [
            "Best For: Large companies, franchise networks, multi-location businesses, international brands",
            "This is a fully custom engagement scoped based on the client's specific needs, team size, market, and objectives.",
            "Typical Enterprise inclusions:",
            ("•", "Multi-location or multi-brand social media management"),
            ("•", "Dedicated agency team (account manager + content creator + paid ads specialist)"),
            ("•", "White-label reporting and branded dashboards"),
            ("•", "In-person or live video content production coordination"),
            ("•", "Custom SLA (Service Level Agreement) with guaranteed response times"),
            ("•", "Monthly board-level reporting and quarterly strategic planning sessions"),
            "Pricing Range: €8,000-€25,000+/month",
            "Qualification Criteria: Annual revenue > €2M, marketing budget > €50K/year, need for 3+ platform management",
        ]),
        ("Add-On Services (Upsell Opportunities)", [
            ("•", "Paid Advertising Setup Fee: €500-€1,500 one-time (for new ad account setup and pixel installation)"),
            ("•", "Content Audit: €500 one-time (full audit of all platforms with recommendations report)"),
            ("•", "Brand Photography Direction: €300-€800 per shoot (we direct, client arranges photographer)"),
            ("•", "Custom Canva Template Set: €250-€500 (5-10 branded Canva templates for client)"),
            ("•", "Influencer Campaign: €800-€2,000 per campaign (identification, outreach, negotiation, tracking)"),
            ("•", "Social Media Training Session: €500 per session (train client's internal team)"),
            ("•", "Extra Platform: +€400-€800/month per additional platform beyond package scope"),
        ]),
    ])

doc(p01+"Agency_SOPs_Master_Guide.docx",
    "Agency SOPs Master Guide",
    "Ultimate AI SMMA OS | Standards for Quality, Communication, Delivery, and Revisions",
    [
        ("Why SOPs Are the Foundation of a Scalable Agency", [
            "Standard Operating Procedures (SOPs) are the difference between an agency that runs you and an agency you run. Without SOPs, your quality depends on how you feel each day. With SOPs, quality is consistent regardless of who on your team executes the work. This guide covers the four critical SOP categories: quality standards, client communication, content delivery, and revision management.",
            ("•", "SOPs allow you to onboard team members and freelancers without re-training from scratch"),
            ("•", "SOPs protect you from client disputes — the process is clear and agreed upon from day one"),
            ("•", "SOPs help you identify bottlenecks and continuously improve your operations"),
        ]),
        ("Quality Standards SOP", [
            "Every piece of content leaving your agency must meet these standards before client delivery:",
            ("•", "Visual Standard: All graphics must use the client's approved brand colors, fonts, and logo — no exceptions"),
            ("•", "Caption Standard: Captions must include a clear hook (first 2 lines before 'More'), a body that delivers value, and a CTA"),
            ("•", "Hashtag Standard: Use the approved hashtag bank from the client's Hashtag_Strategy_Guide — never random hashtags"),
            ("•", "Grammar Standard: All captions spell-checked in Grammarly and reviewed for tone consistency with brand voice"),
            ("•", "Dimension Standard: Every image and video must meet the current platform specifications (stored in Content_Creation_SOP.docx)"),
            ("•", "Approval Standard: Nothing is published without client approval via the content calendar — no exceptions"),
            ("•", "Performance Benchmark: After 30 days, compare results to industry averages for the client's niche. If below benchmark, escalate to strategy review"),
        ]),
        ("Client Communication SOP", [
            "How you communicate with clients is as important as the work you produce. These standards protect the client relationship.",
            ("•", "Response Time: All client emails and messages responded to within 4 business hours (Elite and Enterprise: 2 hours)"),
            ("•", "Content Calendar Delivery: Minimum 10 business days before the start of the month covered"),
            ("•", "Monthly Report Delivery: Within 5 business days of the end of the reporting month"),
            ("•", "Meeting Scheduling: All meetings booked via a calendar link — never 'what time works for you?' back-and-forth"),
            ("•", "Proactive Updates: If anything changes (platform algorithm update, content delay, ad issue) — tell the client before they ask"),
            ("•", "Escalation Protocol: If a client raises a concern, acknowledge within 1 hour, provide a resolution plan within 24 hours"),
            ("•", "Offboarding: When a contract ends, provide a full transition document within 5 business days"),
        ]),
        ("Content Delivery SOP", [
            "Step 1 — Brief Creation (Day 1 of monthly cycle):",
            ("•", "Create the monthly content brief based on client goals, upcoming events, and content pillars"),
            "Step 2 — AI-Assisted Draft (Day 2-3):",
            ("•", "Use AI_Prompt_Library.docx to generate caption drafts and content ideas"),
            ("•", "Design graphics using client's Canva brand kit"),
            "Step 3 — Internal Review (Day 4-5):",
            ("•", "Review all content against quality standards checklist"),
            ("•", "Peer review: second team member checks all content before client delivery"),
            "Step 4 — Client Review (Day 6-10):",
            ("•", "Share content calendar in Notion or Google Sheets for client review"),
            ("•", "Provide 5 business days for client feedback"),
            "Step 5 — Revisions and Finalization (Day 11-13):",
            ("•", "Process all revision requests within 48 hours"),
            ("•", "Get final written approval before scheduling"),
            "Step 6 — Scheduling (Day 14+):",
            ("•", "Schedule all approved content using Buffer, Hootsuite, or Later"),
            ("•", "Confirm scheduling in client's content calendar with 'SCHEDULED' status"),
        ]),
        ("Revision Policy SOP", [
            "Clear revision policies prevent scope creep and protect your team's time.",
            ("•", "Revision Definition: A revision is a change to copy or design that falls within the original agreed brief"),
            ("•", "Out of Scope: Changes to core brand strategy, new content themes, or complete redesigns are not revisions — quote separately"),
            ("•", "Revision Rounds by Package: Starter = 1 round per batch; Growth = 2 rounds; Pro = unlimited; Elite = unlimited + 24hr turnaround"),
            ("•", "Revision Request Format: All revisions must be submitted in a single consolidated document — not drip-fed over multiple messages"),
            ("•", "Timeline: Revisions are delivered within 2-3 business days (1 business day for Elite/Enterprise)"),
            ("•", "Content That Cannot Be Revised: Once content is published per client approval, revisions are not possible — client is responsible for all approvals"),
        ]),
        ("Team and Subcontractor Standards", [
            ("•", "All subcontractors sign an NDA before accessing any client information"),
            ("•", "Brief all subcontractors using the client's Brand Discovery Questionnaire"),
            ("•", "Quality check all subcontractor work before delivery to client"),
            ("•", "Track subcontractor deliverables in Team_Tasks.csv in Notion"),
            ("•", "Pay subcontractors within 5 business days of invoice submission"),
        ]),
    ])

doc(p01+"Niche_Selection_Framework.docx",
    "SMMA Niche Selection Framework",
    "Ultimate AI SMMA OS | How to Choose Your Agency Niche for Maximum Revenue",
    [
        ("Why Niche Selection Is the Most Important Decision You Will Make", [
            "The biggest mistake new SMMA owners make is trying to serve everyone. 'We help all businesses with social media' sounds broad and appealing — but it actually attracts fewer clients and commands lower rates. The agencies charging €5,000-€10,000/month are almost always specialists. This guide walks you through a systematic process for choosing a niche that is profitable, accessible, and aligned with your skills and interests.",
            ("•", "Niche agencies close deals 3x faster because prospects see instant relevance"),
            ("•", "Niche case studies are 5x more persuasive than generic ones"),
            ("•", "Niche specialists command 40-80% higher rates than generalists"),
        ]),
        ("High-Performing SMMA Niches (2024-2025)", [
            "Tier A — Highest Average Client Value (€3,000-€10,000+/month):",
            ("•", "Real Estate Agencies and Agents: High competition but consistent deal-focused need for lead gen"),
            ("•", "Medical and Aesthetic Clinics: High margins, regulated content, needs specialist knowledge"),
            ("•", "Law Firms: Growing social media adoption, high-value client acquisition, strong case study potential"),
            ("•", "Financial Advisors and Wealth Management: High compliance complexity but premium rates"),
            ("•", "SaaS Companies: B2B LinkedIn focus, strong ROI measurement, scale potential"),
            "Tier B — Strong Volume and Accessibility (€1,500-€3,000/month):",
            ("•", "Restaurants and Food & Beverage: Visual content-heavy, strong Instagram/TikTok alignment, local focus"),
            ("•", "Personal Trainers and Fitness Coaches: Strong content demand, clear transformation results"),
            ("•", "E-commerce Brands: Product-focused content, strong paid ads alignment, scalable"),
            ("•", "Business Coaches and Consultants: Audience-building focus, high-quality content needs"),
            ("•", "Wedding and Events Vendors: Visual-heavy, referral culture, seasonal patterns"),
        ]),
        ("Niche Evaluation Matrix", [
            "Score your top 3 niche candidates against these 6 criteria (1-5 each, max 30 points):",
            ("•", "Market Size: Are there thousands of potential clients in your country/region? (1=very small, 5=massive)"),
            ("•", "Average Client Value: What is the realistic MRR from this niche? (1=<€500, 5=>€3,000)"),
            ("•", "Pain Point Clarity: Is the social media problem obvious and well-understood? (1=vague, 5=crystal clear)"),
            ("•", "Your Existing Knowledge: Do you understand this industry's buyer, vocabulary, and culture? (1=none, 5=expert)"),
            ("•", "Content Richness: Does this niche produce content-friendly subject matter? (1=dry/difficult, 5=very visual/engaging)"),
            ("•", "Competitive Density: How many established agencies are already serving this niche? (1=saturated, 5=open market)"),
            "[FILL IN] Niche 1: _______________ Total Score: ___/30",
            "[FILL IN] Niche 2: _______________ Total Score: ___/30",
            "[FILL IN] Niche 3: _______________ Total Score: ___/30",
        ]),
        ("How to Validate Your Niche Before Committing", [
            "Before you invest heavily in a niche, validate that clients in that niche will actually pay for SMMA services.",
            "Validation Step 1 — Market Research:",
            ("•", "Search '[niche] social media agency' on Google. Are there competitors? That means a market exists."),
            ("•", "Search the niche on LinkedIn. Are there 1,000+ potential clients in your country?"),
            "Validation Step 2 — Price Test:",
            ("•", "Reach out to 10 businesses in the niche. Offer a free audit and discovery call. Track the response rate."),
            ("•", "On the discovery call, present your Starter package. Gauge resistance to the price."),
            "Validation Step 3 — Commitment Test:",
            ("•", "Aim to close 1 paying client in 30 days. If you cannot close 1 client at any price, reconsider the niche."),
            ("•", "If you close 1 client: deliver exceptional results and build a case study. This validates the niche."),
        ]),
        ("Building Your Niche Authority", [
            "Once you select a niche, commit to becoming visibly known in that community:",
            ("•", "Create content specifically about social media strategies for your niche (not generic SMMA content)"),
            ("•", "Join the niche's industry associations, Facebook groups, and LinkedIn groups"),
            ("•", "Study the niche deeply: read their trade publications, understand their business cycles and pain points"),
            ("•", "Build a niche-specific case study within your first 3 months — even if you work for a reduced rate"),
            ("•", "Your agency's social media should speak directly to your niche: 'We help [niche] businesses...'"),
        ]),
    ])

print("✓ 01_AGENCY_SETUP complete")

# ─── 02_CLIENT_ACQUISITION ─────────────────────────────────────────────────────
p02 = "02_CLIENT_ACQUISITION/"

doc(p02+"Cold_DM_Scripts.docx",
    "Cold DM Scripts — 25+ Templates",
    "Ultimate AI SMMA OS | Instagram DMs, LinkedIn Messages, Twitter/X Outreach",
    [
        ("Cold DM Strategy Overview", [
            "Cold DMs are one of the fastest ways to start conversations with potential SMMA clients. The key is personalization — a copy-paste message is immediately obvious and gets ignored. These scripts are starting points. Spend 60 seconds researching each prospect before sending. Mention something specific — a recent post, a milestone, a product launch. That single detail multiplies your response rate by 3-5x.",
            ("•", "Target: 20-30 DMs per day maximum (Instagram will flag higher volumes)"),
            ("•", "Timing: Send Tuesday-Thursday between 9am-12pm local time for best open rates"),
            ("•", "Platform Sequencing: If no response in 5 days, try the same prospect on a different platform"),
            ("•", "First Message Rule: Never pitch in the first message. Start a conversation."),
        ]),
        ("Instagram DM Scripts — First Message", [
            "Script IG-1 — Compliment + Curiosity:",
            '"Hey [Name]! I was scrolling through [niche] accounts and your profile stood out — especially your [specific post or reel]. Quick question: are you currently running any specific strategy to turn that engagement into bookings / leads / sales?"',
            "Script IG-2 — Specific Observation:",
            '"Hi [Name], I just came across your reel about [topic] — that was really well done. I noticed you post consistently but don\'t have a ton of engagement yet. I specialize in helping [niche] businesses fix exactly that. Would it be okay if I sent over a quick voice note with a couple ideas I had for your account?"',
            "Script IG-3 — Value-First Opener:",
            '"Hey [Name]! Your content is great but I noticed you might not be using [Reels/Stories/Carousels] to their full potential. I just helped a [niche] business like yours grow from [X] to [Y] followers in 90 days using a simple strategy. Would you be open to hearing how it works?"',
            "Script IG-4 — Direct and Confident:",
            '"Hi [Name]! I help [niche] businesses get more [clients/bookings/sales] from Instagram. Looked at your profile and have 3 specific ideas I think could make a real difference. Can I share them with you?"',
            "Script IG-5 — Audit Offer:",
            '"Hi [Name], I run a social media agency specializing in [niche]. I do free mini-audits for [niche] businesses — takes about 10 minutes and I give you specific, actionable feedback on your profile and content. Interested?"',
        ]),
        ("Instagram DM Scripts — Follow-Up Messages", [
            "Follow-Up IG-F1 (Day 3 — No Response):",
            '"Hey [Name]! Just wanted to bump my previous message in case it got buried. No pressure at all — just thought my ideas could be useful for your [niche] business. Let me know if you\'d like to chat!"',
            "Follow-Up IG-F2 (Day 7 — Still No Response):",
            '"Hi [Name], last message from me! I completely understand if now isn\'t the right time. I\'m actually putting together a free guide on [niche-specific topic] — would you like me to send it over? No strings attached."',
            "Follow-Up IG-F3 (After Positive Response — Moving to Call):",
            '"Awesome! Really glad you\'re open to a chat. I usually do a quick 15-minute call to understand your goals before sharing anything — that way my ideas are actually relevant to YOUR situation. Here\'s my calendar: [LINK]. Does any of those slots work?"',
        ]),
        ("LinkedIn Message Scripts", [
            "Script LI-1 — Connection Request Message (300 character max):",
            '"Hi [Name], I specialize in social media strategy for [niche] businesses and noticed your company — impressive work. Would love to connect and potentially share some ideas about what\'s working in your industry right now."',
            "Script LI-2 — After Connection Is Accepted:",
            '"Thanks for connecting, [Name]! I noticed [Company] is doing [specific thing]. I work with [niche] businesses to [specific outcome]. I\'d love to share a couple of ideas specific to [Company]. Would a 15-minute call this week or next be feasible?"',
            "Script LI-3 — InMail (Paid, Higher Response Rate):",
            "Subject: Quick thought on [Company Name]'s social media strategy",
            '"Hi [Name], I\'ve been following [Company Name] and noticed your [specific observation about their content]. I specialize in helping [niche] B2B companies use LinkedIn and Instagram to [specific outcome]. I have 2-3 specific ideas I\'d love to share that are working well for similar companies. Would you be open to a 15-minute virtual coffee? [CALENDAR LINK]"',
            "Script LI-4 — Referral-Based LinkedIn:",
            '"Hi [Name], I noticed we\'re both connected to [Mutual Connection]. I work with [niche] companies on their social media strategy and have helped similar businesses achieve [result]. Given your role at [Company], I thought you might find what we\'re doing relevant. Happy to share more if you\'re open to it."',
        ]),
        ("Twitter/X DM Scripts", [
            "Script X-1 — Engage Then DM:",
            '"[After liking/replying to their tweet] Hey [Name]! Just replied to your tweet about [topic] — great take. I actually specialize in social media for [niche] and had a thought about how you could turn that kind of content into actual business. Mind if I DM you with the idea?"',
            "Script X-2 — Direct DM:",
            '"Hi [Name]! Noticed you tweet about [topic] regularly — that\'s smart positioning. I help [niche] businesses turn their Twitter presence into lead generation. Would love to share 1-2 things I\'d try differently on your profile. Interested?"',
        ]),
        ("Qualifying Questions for Discovery Call Booking", [
            "After a positive DM response, use these questions to qualify before booking:",
            ("•", "What platforms are you currently active on? How often do you post?"),
            ("•", "What are your main business goals right now — more leads, more brand awareness, or sales?"),
            ("•", "Do you currently work with anyone on your social media, or is it all done in-house?"),
            ("•", "What would be the ideal outcome if we worked together?"),
            "Qualifying criteria: They have budget awareness, they have a specific goal, they are not satisfied with current results.",
        ]),
    ])

doc(p02+"Cold_Email_Templates.docx",
    "Cold Email Templates — 8 High-Converting Templates",
    "Ultimate AI SMMA OS | Subject Lines, Body Copy, and Follow-Up Sequences",
    [
        ("Cold Email Strategy for SMMA", [
            "Cold email is one of the highest ROI outreach channels for B2B SMMA lead generation because it is asynchronous, professional, and allows for personalized, longer messaging than DMs. The key to great cold email is a compelling subject line (determines open rate) and a clear value proposition that speaks to a specific pain the prospect has right now.",
            ("•", "Target open rate: 40-60% with good subject lines and from-domain (not Gmail)"),
            ("•", "Target reply rate: 5-15% with strong personalization and relevant offers"),
            ("•", "Send sequence: Email 1 → Wait 3 days → Follow-up 1 → Wait 4 days → Follow-up 2 → Wait 7 days → Final breakup email"),
            ("•", "Email length: Under 150 words for cold email. Shorter = higher response rate."),
            ("•", "Personalization: Reference something specific in the first 2 lines — otherwise it reads as spam"),
        ]),
        ("Template 1 — Restaurant / F&B", [
            "Subject: [Restaurant Name] — I have 3 ideas for your Instagram",
            "Hi [Owner Name],",
            "I was browsing restaurants in [City] and came across [Restaurant Name] — your food photography is genuinely impressive. But I noticed your Instagram engagement is much lower than your food quality deserves.",
            "I specialize in social media marketing for restaurants and recently helped [Similar Restaurant] increase their walk-in bookings by 34% in 60 days using a specific Instagram and Google approach.",
            "Would you be open to a quick 15-minute call this week? I have 3 specific ideas for [Restaurant Name] I'd love to share — no pitch, just ideas.",
            "[Your Name] | [Agency Name] | [Phone/Calendar Link]",
        ]),
        ("Template 2 — Fitness / Personal Trainer", [
            "Subject: Quick question about your [City] fitness coaching business",
            "Hi [Name],",
            "I came across your profile while researching fitness coaches in [City]. Your transformation content is great — but I think there's a much bigger audience that should be seeing it.",
            "I help personal trainers and fitness coaches turn their social media content into a consistent client acquisition machine. Last month, I helped a PT in [City/Country] go from 5 new clients per month to 18 by making 4 specific changes to their Instagram strategy.",
            "I do free 15-minute strategy calls for coaches who are serious about scaling. Would Thursday or Friday work for you?",
            "[Calendar Link]",
            "[Your Name]",
        ]),
        ("Template 3 — E-Commerce Brand", [
            "Subject: I noticed something about [Brand Name]'s social media",
            "Hi [Name],",
            "I've been following [Brand Name] for a while and love what you're building. I noticed your products are getting great reviews but your social media isn't yet reflecting that momentum — specifically, I think you're leaving significant Instagram and TikTok traffic on the table.",
            "I run an e-commerce social media agency and we specialize in turning product-based brands into social-first businesses. Our clients average a 2.8x increase in social-driven revenue within 90 days.",
            "I put together a quick 3-point observation about [Brand Name]'s social presence. Can I send it over?",
            "[Your Name] | [Agency Name]",
        ]),
        ("Template 4 — Real Estate Agent / Agency", [
            "Subject: How [City] real estate agents are generating leads on Instagram in 2024",
            "Hi [Name],",
            "I specialize in social media marketing for real estate professionals in [Region]. Most agents I talk to post listings and get almost no engagement — and it's not their fault. The algorithm rewards a very different type of content.",
            "I recently helped a real estate agent in [City] generate 11 qualified buyer leads in a single month from Instagram alone using a content strategy that most agents aren't using yet.",
            "Would you be open to a 20-minute call to see if this could work for your business? I promise it's worth your time.",
            "[Your Name] | [Calendar Link]",
        ]),
        ("Template 5 — Business Coach / Consultant", [
            "Subject: Your content is good. Here's how to make it convert.",
            "Hi [Name],",
            "I've been following your [LinkedIn/Instagram] and your content is genuinely insightful. But I've noticed something: your engagement is strong but your CTA to actual inquiries seems low.",
            "I work with business coaches and consultants to build social media systems that convert followers into high-ticket clients. The approach is different from what most 'content creators' recommend — it's built around conversion, not just views.",
            "I'd love to share a 5-minute voice note with a specific observation about your current strategy. Would you be open to that?",
            "[Your Name]",
        ]),
        ("Template 6 — Medical / Aesthetic Clinic", [
            "Subject: Growing [Clinic Name]'s new patient bookings through social media",
            "Hi [Name],",
            "I specialize in social media marketing for aesthetic and medical clinics, and I came across [Clinic Name] while researching [City] practices. Your results look impressive — I believe a targeted Instagram and Facebook strategy could significantly increase your new patient inquiries.",
            "I've helped clinics similar to yours increase monthly new patient bookings by 40-60% within 90 days without increasing their ad spend — just by optimizing their organic content and social strategy.",
            "I have 2 specific ideas for your clinic's social presence I'd love to share on a quick call. Are you the right person to speak with about this?",
            "[Your Name] | [Agency Name]",
        ]),
        ("Template 7 — Follow-Up Email 1 (Day 3)", [
            "Subject: Re: [Original Subject Line]",
            "Hi [Name],",
            "Just following up on my message from a few days ago. I know inboxes get busy!",
            "I genuinely believe there's an opportunity here for [Business Name] — specifically around [one specific thing you noticed]. Happy to share what I've seen work for similar [niche] businesses.",
            "If now isn't the right time, no worries at all. But if you have 15 minutes this week, I promise you'll leave with at least one actionable idea.",
            "[Calendar Link]",
            "[Your Name]",
        ]),
        ("Template 8 — Breakup Email (Day 18)", [
            "Subject: Closing the loop, [Name]",
            "Hi [Name],",
            "I've reached out a couple of times and haven't heard back — so I'm assuming the timing isn't right for [Business Name] right now. Totally understood.",
            "I'll stop reaching out after this, but I did want to leave you with something useful: [attach or link to a free resource relevant to their niche].",
            "If social media marketing ever becomes a priority for your business, I'm always happy to reconnect. Feel free to reach out anytime.",
            "Best of luck with everything!",
            "[Your Name] | [Agency Name]",
        ]),
    ])

doc(p02+"Discovery_Call_Script.docx",
    "Discovery Call Script — Complete 60-Minute Framework",
    "Ultimate AI SMMA OS | From Introduction to Close in One Call",
    [
        ("Discovery Call Overview", [
            "The discovery call is where your SMMA business is won or lost. Clients buy from agencies they trust, and trust is built in this conversation. Your goal is not to pitch — your goal is to understand the client's situation so deeply that they feel heard, and then to show them exactly how you solve their specific problem. Follow this framework and your close rate will increase dramatically.",
            ("•", "Duration: 45-60 minutes (never less than 30, rarely more than 75)"),
            ("•", "Format: Video call preferred (Zoom, Google Meet) — never audio only with a new prospect"),
            ("•", "Pre-call: Research the client for 10 minutes — check all their social media, their website, their Google reviews"),
            ("•", "Have ready: A blank notepad for notes, your pricing guide, and your agency proposal template"),
        ]),
        ("Part 1 — Introduction (Minutes 0-5)", [
            '"Hi [Name], great to meet you! Thanks so much for making time for this call. I\'ve had a chance to look at [Business Name] ahead of our call — really impressive [something specific you noticed]. I want to make sure this call is genuinely useful for you, so I\'ll be doing a lot of listening today. Does that work?"',
            '"Before we dive in, let me take 60 seconds to tell you about what we do, and then I\'d love to spend most of our time understanding your situation."',
            "[Brief Agency Intro — 60 seconds max]:",
            '"We\'re a social media marketing agency that specializes in [niche]. We\'ve worked with [X] businesses in [niche/region] and our average client sees [specific result] within the first 90 days. But honestly, we\'re pretty selective about who we work with — this call is as much about figuring out if we\'re the right fit for you as anything else."',
        ]),
        ("Part 2 — Discovery Questions (Minutes 5-30)", [
            "Business Understanding Questions:",
            ("•", '"Can you tell me about the business? How long have you been operating and what does growth look like right now?"'),
            ("•", '"Who is your ideal customer and what makes someone a great client for you?"'),
            ("•", '"What\'s your current primary channel for acquiring new clients? What\'s working? What\'s not?"'),
            "Social Media Specific Questions:",
            ("•", '"Walk me through your current social media — what platforms are you on, who manages it, and how much time is spent on it?"'),
            ("•", '"What results are you seeing from your current social media presence? Be specific if you can."'),
            ("•", '"Have you ever worked with a social media agency or freelancer before? What was that experience like?"'),
            "Pain Point and Goal Questions:",
            ("•", '"If social media was working perfectly for your business, what would that look like in 6 months?"'),
            ("•", '"What\'s your biggest frustration right now with your online presence?"'),
            ("•", '"On a scale of 1-10, how important is growing your social media to your business goals this year?"'),
            "Budget Discovery (Ask This Way):",
            '"Most of our clients in [niche] invest between €1,500 and €5,000 per month in social media management, depending on scope. Is that a range that feels aligned with where you are, or would we need to think about a different scope?"',
        ]),
        ("Part 3 — Your Solution (Minutes 30-50)", [
            '"Based on everything you\'ve shared, here\'s what I\'m hearing: [Summarize their situation in 3-4 sentences using THEIR words]. Does that sound right?"',
            '"Here\'s what I think the opportunity looks like for [Business Name]..."',
            "[Present your recommendation — not a generic pitch, but a specific recommendation based on what they told you]:",
            ("•", "Reference the specific platform they should focus on and why"),
            ("•", "Reference the content type that works for their niche and audience"),
            ("•", "Reference the specific outcome they said they wanted and how you deliver it"),
            '"The package that makes the most sense for what you\'ve described is our [Package Name] at €[Price]/month. Let me walk you through exactly what\'s included..."',
            "[Walk through deliverables clearly — 1 sentence per deliverable]",
            '"Does this feel like it addresses what you\'re trying to achieve?"',
        ]),
        ("Part 4 — Handling Questions and Objections (Minutes 50-60)", [
            "If they ask about results/guarantees:",
            '"I don\'t make specific result guarantees because every business is different — but what I can tell you is our average [niche] client sees [X result] within [timeframe]. I can share a couple of case studies after this call if that would help."',
            "If they say they need to think about it:",
            '"Of course — this is an important decision. Can I ask, is there something specific that\'s making you hesitate? I want to make sure you have everything you need to feel confident."',
            "If they say it\'s too expensive:",
            '"I appreciate you being honest about that. Can I ask — is it the investment itself, or is it about certainty on the return? [...] We do have a Starter package at €500/month that\'s a lower-risk way to start. Would it be useful to look at that scope?"',
        ]),
        ("Part 5 — Close and Next Steps (Last 5 Minutes)", [
            '"This all feels like a really strong potential fit. Here\'s what I\'d suggest as next steps: I\'ll send over a formal proposal today that captures everything we discussed, including the package details and the contract. You can review it in your own time, and we can schedule a quick follow-up if you have any questions. Does that work for you?"',
            '"Is there anyone else on your side who would need to be involved in this decision? If so, is it possible to loop them in before I send the proposal?"',
            '"Great! I\'ll have the proposal in your inbox within [X hours]. Really looking forward to the possibility of working together."',
        ]),
    ])

doc(p02+"Objection_Handling_Scripts.docx",
    "Objection Handling Scripts — 35+ Responses",
    "Ultimate AI SMMA OS | Responses to Every Common SMMA Sales Objection",
    [
        ("Price and Budget Objections", [
            "'It's too expensive':",
            '"I hear that — and I want to make sure we\'re comparing apples to apples. Can I ask: too expensive compared to what? If it\'s compared to doing it in-house, let\'s look at the actual cost of a hired content creator plus your time. If it\'s compared to another agency, I\'d love to understand what they\'re offering because the outcomes can be very different. What would feel like fair value to you?"',
            "'We don\'t have the budget right now':",
            '"I completely understand — and I respect that. Can I ask, is this a timing thing (you will have budget in Q2, for example) or is it more that you\'re not yet seeing social media as a budget priority? The reason I ask is because if it\'s timing, I\'d love to stay in touch. And if it\'s priority, I might be able to share some data about ROI in your specific niche that could change the picture."',
            "'We can just do it ourselves':",
            '"Absolutely — and many businesses do. Here\'s the question worth asking: how much is your time worth per hour, and how many hours per week would you need to invest to do this at the level that actually moves the needle? Most business owners we work with found they were spending 10-15 hours per week on social media and getting inconsistent results. For less than the cost of a part-time hire, you get an entire specialist agency."',
            "'Your competitor charges less':",
            '"That\'s worth exploring. Do you know what\'s included in their package? The price difference almost always comes down to what\'s not included — the number of posts, the quality of the content, the ad management, the reporting depth. I\'d love to do a direct comparison if you can share what they proposed. What matters most is the return on your investment, not the fee itself."',
        ]),
        ("Trust and Authority Objections", [
            "'I've never heard of your agency':",
            '"Fair point — we\'re selective about our clients, so we intentionally stay niche rather than trying to be everywhere. What I can share is [specific result or case study relevant to their industry]. Would it help to speak with one of our current clients in [their niche]? I\'m happy to arrange a reference call."',
            "'Do you have experience in my industry?':",
            '"Great question — and it\'s the right one to ask. We specialize in [niche/niche adjacent], which means we understand [specific industry vocabulary and pain point]. Here\'s a case study from a very similar business... [share specific example]. The strategies we use are tailored to how [niche] buyers make decisions online."',
            "'I've been burned by agencies before':",
            '"That\'s unfortunately common, and I\'m sorry you went through that. Can I ask what happened specifically? I want to understand what went wrong so I can show you how we\'ve built our systems differently. We have a clear onboarding process, a content approval workflow, and monthly reporting that keeps you in full visibility at all times. There are no surprises."',
            "'How do I know this will actually work?':",
            '"That\'s the most important question you can ask. I won\'t promise you specific numbers because every business is different. What I will commit to is a clear strategy backed by data, monthly reporting on every KPI we agreed to, and a monthly strategy call where we review what\'s working and optimize what isn\'t. Here\'s what our clients in [your niche] typically see in the first 90 days: [specific range]."',
        ]),
        ("Timing Objections", [
            "'Now isn't the right time':",
            '"I understand — when would be the right time? I ask because the best time to build your social media presence is always a little before you urgently need it. Social media takes 60-90 days to show momentum, so starting in [current month] means you\'ll see results by [future month]. Is there a specific milestone I should follow up after?"',
            "'We're too busy right now':",
            '"That\'s actually one of the most common reasons people reach out to us — they\'re busy doing what they\'re good at and don\'t have time for social media. Our onboarding process requires about 2 hours of your time in the first month and then 30 minutes per month for reviews. We handle everything else. Would that level of involvement feel manageable?"',
            "'We\'re waiting until after [event/season/quarter]':",
            '"That makes sense — and I respect the timing. The good news is we can use this time to prepare: do a full social media audit, build your content calendar, and have everything ready to launch the moment you give the green light. Would it be worth scheduling a planning call so we\'re ready to hit the ground running?"',
        ]),
        ("Commitment Objections", [
            "'Can we start with just one month?':",
            '"I completely understand wanting to test before committing. Here\'s the honest challenge: social media results compound over time. In the first month, we\'re setting up systems, understanding your audience, and experimenting. Months 2-3 is when optimization kicks in and results become visible. A one-month trial would end right before you start seeing the value. That\'s why we have a 3-month minimum — it\'s the minimum time to demonstrate real results. Could we structure it as a 3-month pilot with a clear review at the end?"',
            "'Can I see a proposal before committing to a call?':",
            '"I could send over a template, but it wouldn\'t mean much without understanding your specific situation — every proposal I create is custom. What if we did a 20-minute call first? I promise it\'s not a hard pitch — it\'s a diagnostic conversation, and you\'ll leave with specific ideas regardless of whether we work together."',
            "'I need to talk to my business partner / spouse':",
            '"Of course — this is a joint decision. Would it be possible to get both of you on a call so I can address any questions directly? It\'s always more efficient than trying to relay the proposal through a third party, and I want to make sure your partner has the full picture. When would work for both of you?"',
        ]),
    ])

# Lead Tracker CRM XLSX
wb = Workbook()
ws1 = wb.active
ws1.title = "Lead Pipeline"

pipeline_headers = ["Lead ID","Business Name","Owner/Contact","Platform","Status",
                    "Source","Package Interest","Est MRR (€)","Last Contact","Next Step","Notes"]
ws1.append(pipeline_headers)
for cell in ws1[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

pipeline_data = [
    ["LD-001","Bella Vita Restaurant","Marco Rossi","Instagram","Contacted","Cold DM","Growth €1,500","1500","2024-01-15","Send follow-up DM Day 3","Liked last 3 posts before DM, responded positively"],
    ["LD-002","FitLife Coaching","Sarah Chen","LinkedIn","Discovery Call Booked","Cold Email","Pro €3,000","3000","2024-01-16","Call 2024-01-22 at 2pm","Very interested, already had bad experience with agency"],
    ["LD-003","Luxe Aesthetics Clinic","Dr. Anna Müller","Instagram","Proposal Sent","Referral","Elite €5,000","5000","2024-01-17","Follow up if no reply by Jan 24","Referred by Marco Rossi, reviewed proposal PDF"],
    ["LD-004","TechFlow SaaS","James Wilson","LinkedIn","Negotiating","LinkedIn Search","Pro €3,000","3000","2024-01-18","Call back Thursday to discuss contract","Budget approved, wants to start Feb 1"],
    ["LD-005","Green Harvest Ecom","Priya Patel","Instagram","Not Interested","Cold DM","Starter €500","0","2024-01-10","Archive — try again in Q2","Said managing in-house, not ready to outsource"],
    ["LD-006","Kairos Real Estate","Thomas Baker","Cold Email","New Lead","Cold Email","Growth €1,500","1500","2024-01-19","First DM pending","Saw listing content is low quality, strong opportunity"],
    ["LD-007","Mindset Academy","Lisa Torres","Instagram","Contacted","Instagram Search","Growth €1,500","1500","2024-01-19","Follow up Day 3 = Jan 22","Coach with 8K followers, posts daily but low engagement"],
    ["LD-008","Bloom Wedding Co.","Emma Wright","LinkedIn","Proposal Sent","Referral","Starter €500","500","2024-01-14","Call Friday to answer contract questions","Small budget but wants to test for 3 months"],
]
for i, row in enumerate(pipeline_data):
    ws1.append(row)
    for cell in ws1[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

col_widths1 = {"A":10,"B":22,"C":18,"D":12,"E":20,"F":14,"G":20,"H":12,"I":14,"J":28,"K":35}
for col, width in col_widths1.items():
    ws1.column_dimensions[col].width = width

# Follow-Up Tracker Sheet
ws2 = wb.create_sheet("Follow-Up Tracker")
fu_headers = ["Lead","Business Name","Day 1 Action","Day 1 Result","Day 3 Action","Day 3 Result",
              "Day 7 Action","Day 7 Result","Day 14 Action","Day 14 Result","Day 30 Action","Day 30 Result"]
ws2.append(fu_headers)
for cell in ws2[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=10)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

fu_data = [
    ["LD-001","Bella Vita Restaurant","Sent IG DM (Script IG-1)","Read, no reply","DM Follow-up F1","Replied! Interested","Booked discovery call","Call confirmed","Discovery call held","Proposal sent","Follow-up call","Closed - Growth pkg"],
    ["LD-002","FitLife Coaching","Sent cold email (T2)","Opened, no reply","Email follow-up F1","Replied, booked call","Discovery call","Proposal sent","Proposal follow-up","Negotiating","Contract review","Pending signature"],
    ["LD-003","Luxe Aesthetics Clinic","Referral intro email","Immediate reply","Discovery call","Very interested","Sent proposal","Reviewing internally","Check in call","Requested changes","Revised proposal","Waiting decision"],
    ["LD-004","TechFlow SaaS","LinkedIn connection","Accepted","LinkedIn message LI-2","Booked call","Discovery call","Sent proposal","Budget approval","Approved","Contract sent","Signing Thursday"],
    ["LD-006","Kairos Real Estate","Cold email T4","No reply","Email follow-up F1","Opened no reply","DM on Instagram","Read no reply","Try LinkedIn","Pending","—","—"],
    ["LD-007","Mindset Academy","IG DM Script IG-3","Replied interested","Voice note sent","Loved the ideas","Booked discovery call","Call tomorrow","—","—","—","—"],
    ["LD-008","Bloom Wedding Co.","Referral email","Immediate reply","Discovery call held","Budget confirmed","Starter proposal sent","Reviewing","Contract questions","Pending call","—","—"],
]
for i, row in enumerate(fu_data):
    ws2.append(row)
    for cell in ws2[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col in ["A","B","C","D","E","F","G","H","I","J","K","L"]:
    ws2.column_dimensions[col].width = 22

# Lead Source Analytics Sheet
ws3 = wb.create_sheet("Lead Source Analytics")
analytics_headers = ["Source","Leads Generated","Meetings Booked","Clients Closed","Revenue (€)","Close Rate (%)","Avg Deal Value (€)"]
ws3.append(analytics_headers)
for cell in ws3[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

analytics_data = [
    ["Instagram Cold DM","24","8","3","5500","12.5%","1833"],
    ["LinkedIn Outreach","18","6","2","6000","11.1%","3000"],
    ["Cold Email","32","7","2","3000","6.3%","1500"],
    ["Referrals","6","6","4","16000","66.7%","4000"],
    ["Inbound (Website)","4","4","2","8000","50.0%","4000"],
    ["Twitter/X DM","10","2","0","0","0%","—"],
    ["Networking Events","5","3","1","1500","20.0%","1500"],
    ["TOTAL","99","36","14","40000","14.1%","2857"],
]
for i, row in enumerate(analytics_data):
    ws3.append(row)
    for cell in ws3[i+2]:
        fill_color = "E94560" if row[0] == "TOTAL" else (LGR if i % 2 == 0 else WHT)
        cell.fill = PatternFill("solid", fgColor=fill_color)
        if row[0] == "TOTAL":
            cell.font = Font(bold=True, color=WHT, size=11)
        cell.alignment = Alignment(horizontal="center", vertical="center")

for col, w in [("A",22),("B",18),("C",18),("D",16),("E",16),("F",16),("G",18)]:
    ws3.column_dimensions[col].width = w

wb.save(BASE + p02 + "Lead_Tracker_CRM.xlsx")
print(f"  ✓ {p02}Lead_Tracker_CRM.xlsx")

# Social Media Audit Template XLSX
wb2 = Workbook()
ws_a = wb2.active
ws_a.title = "Platform Audit"
audit_headers = ["Platform","Followers","Avg Engagement Rate","Post Frequency (per wk)","Bio Optimized?",
                 "Link in Bio","Top Content Type","Main Weaknesses","Priority Score (1-10)"]
ws_a.append(audit_headers)
for cell in ws_a[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

audit_data = [
    ["Instagram","4,200","1.8%","3x/week","Partial - no CTA","linktree.com/client","Static graphics","Low video content, weak story strategy, inconsistent posting",7],
    ["Facebook","1,800","0.6%","1x/week","No","Website homepage","Shared posts from IG","No original content, no community engagement, no ads",5],
    ["LinkedIn","890","3.2%","1x/week","Yes","Website","Long-form thought leadership","Irregular posting, no employee advocacy, no company page strategy",6],
    ["TikTok","120","0.9%","0x/week","No","Not set up","N/A — no real presence","No reels, no trending audio, account barely active",8],
    ["Twitter/X","340","0.4%","5x/week","No","Website","Retweets and comments","No original content strategy, no brand voice consistency",4],
    ["YouTube","0","N/A","0x/week","N/A","N/A","No presence","Not started — could be powerful for educational content in niche",3],
]
for i, row in enumerate(audit_data):
    ws_a.append(row)
    for cell in ws_a[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",14),("B",12),("C",20),("D",22),("E",16),("F",22),("G",22),("H",38),("I",16)]:
    ws_a.column_dimensions[col].width = w

# Competitor Analysis Sheet
ws_b = wb2.create_sheet("Competitor Analysis")
comp_headers = ["Competitor Name","Followers (IG)","Engagement Rate","Posting Freq","Content Mix","Key Strengths","Identified Gaps","Our Opportunity"]
ws_b.append(comp_headers)
for cell in ws_b[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

comp_data = [
    ["[Competitor A]","12,400","3.4%","7x/week","70% Reels, 20% Carousels, 10% Static","High video production quality, strong CTA","No LinkedIn presence, weak written captions, no stories strategy","Target their followers with strong caption-driven content and DM strategy"],
    ["[Competitor B]","5,600","1.9%","4x/week","50% Static, 30% Stories, 20% Reels","Consistent posting, good brand aesthetics","Low engagement per post, no video, no community management","Offer superior community management and video content"],
    ["[Competitor C]","8,900","2.8%","5x/week","60% Educational Carousels, 40% Reels","Strong educational content, high saves","No paid ads, no LinkedIn, no monthly reporting","Position as full-service vs. their content-only approach"],
    ["[Competitor D]","22,100","1.2%","Daily","Mixed — no clear strategy","Large following, frequent posting","Very low engagement despite large audience — posting without strategy","Show results per follower vs. vanity metrics"],
    ["[Competitor E]","3,200","5.1%","2x/week","All Reels, highly produced","Exceptional quality, high engagement","Low frequency, no text/carousel content","Match their quality but add consistency and multi-format strategy"],
]
for i, row in enumerate(comp_data):
    ws_b.append(row)
    for cell in ws_b[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",22),("B",15),("C",17),("D",14),("E",28),("F",30),("G",32),("H",35)]:
    ws_b.column_dimensions[col].width = w

# Content Gap Analysis Sheet
ws_c = wb2.create_sheet("Content Gap Analysis")
gap_headers = ["Content Category","Current Frequency","Competitor Average","Gap (behind/ahead)","Priority","Content Ideas to Fill Gap","Estimated Impact"]
ws_c.append(gap_headers)
for cell in ws_c[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

gap_data = [
    ["Short-Form Video (Reels/TikTok)","1x/week","4x/week","Behind by 3x","HIGH","Behind-the-scenes reels, transformation reveals, quick tips, trending audio","Reach +200%, Follower growth +40%"],
    ["Educational Carousels","0x/week","2x/week","Behind by 2x","HIGH","How-to guides, myth-busting, industry stats, step-by-step frameworks","Saves +300%, Profile visits +80%"],
    ["User-Generated Content","0x/week","1x/week","Behind by 1x","MEDIUM","Client testimonial reposts, review screenshots, case study visuals","Trust signals +100%"],
    ["Stories (Interactive)","2x/week","5x/week","Behind by 3x","MEDIUM","Polls, Q&As, quizzes, behind-the-scenes stories, product teasers","Retention +60%, DMs +40%"],
    ["Long-Form Captions (Value Posts)","1x/week","3x/week","Behind by 2x","MEDIUM","Storytelling, lessons learned, process breakdowns, opinion pieces","Comments +150%, Shares +80%"],
    ["Trending Audio/Sounds","0x/month","8x/month","Behind by 8x","HIGH","Trend-jacking with relevant niche content, participating in challenges","Reach +400%, New followers +50%"],
    ["LinkedIn Articles / Long-form","0x/month","4x/month","Behind by 4x","LOW","Thought leadership pieces, industry predictions, case studies","B2B leads +30%, Authority building"],
]
for i, row in enumerate(gap_data):
    ws_c.append(row)
    for cell in ws_c[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",25),("B",18),("C",20),("D",20),("E",12),("F",42),("G",28)]:
    ws_c.column_dimensions[col].width = w

wb2.save(BASE + "04_CLIENT_ONBOARDING/Social_Media_Audit_Template.xlsx")
print(f"  ✓ 04_CLIENT_ONBOARDING/Social_Media_Audit_Template.xlsx")

print("✓ 02_CLIENT_ACQUISITION complete")
print("\nPART 1 DONE")
