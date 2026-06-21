#!/usr/bin/env python3
"""Insurance Agency OS - Part 1: Folders 00-03 + directory structure"""
import os
from docx import Document
from docx.shared import Pt, RGBColor

BASE = "/home/user/oqul-phase55-production/insurance-agency-os/Ultimate_Insurance_Agency_Operating_System/"

FOLDERS = [
    "00_START_HERE",
    "01_LEAD_GENERATION",
    "02_SALES_PROCESS",
    "03_POLICY_SERVICES",
    "04_CLAIMS_SUPPORT",
    "05_CLIENT_COMMUNICATION",
    "06_COMPLIANCE_LICENSING",
    "07_CARRIER_RELATIONSHIPS",
    "08_AGENCY_OPERATIONS",
    "09_POST_SALE_RETENTION",
    "10_NOTION_WORKSPACE",
    "11_BONUSES",
    "12_CANVA_IMPORTABLE_TEMPLATES",
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

# ─── 00_START_HERE ─────────────────────────────────────────────────────────────
with open(BASE+"00_START_HERE/README_FIRST.txt","w",encoding="utf-8") as f:
    f.write("""WELCOME TO YOUR INSURANCE AGENCY OPERATING SYSTEM
===================================================
Original Value: €149 | Your Launch Price: €39

WHAT'S INSIDE:
--------------
00_START_HERE          → You are here!
01_LEAD_GENERATION     → Prospecting scripts, digital leads, referral strategies
02_SALES_PROCESS       → Needs analysis, quoting, objection handling, closing
03_POLICY_SERVICES     → Onboarding, policy review, cross-sell, endorsements
04_CLAIMS_SUPPORT      → First notice of loss, advocacy, follow-up protocols
05_CLIENT_COMMUNICATION → Email, phone, and text templates for every situation
06_COMPLIANCE_LICENSING → E&O, state licensing, carrier compliance guides
07_CARRIER_RELATIONSHIPS → Appointment management, market access, underwriting tips
08_AGENCY_OPERATIONS   → Hiring, training, workflows, KPI dashboards
09_POST_SALE_RETENTION → Annual review, renewal, VIP programs, testimonials
10_NOTION_WORKSPACE    → 7 Notion-importable databases + setup guide
11_BONUSES             → 365 social captions, scripts vault, growth playbook
12_CANVA_TEMPLATES     → 4 Canva-importable professional presentations

Insurance Agency Operating System | Professional Edition
""")
print("  ✓ 00_START_HERE/README_FIRST.txt")

doc("00_START_HERE/Quick_Start_Checklist.docx",
    "Insurance Agency OS — Quick Start Checklist",
    "Your First 7 Days With This System",
    [
        ("Day 1 — Foundation Setup", [
            ("•", "Import all 7 CSVs from 10_NOTION_WORKSPACE into your Notion account"),
            ("•", "Upload PPTX files from 12_CANVA_TEMPLATES to Canva"),
            ("•", "Open the Agency_CRM.xlsx and import your existing client list"),
            ("•", "Review the Compliance_Checklist.docx and confirm your current E&O status"),
        ]),
        ("Day 2-3 — Lead Generation Setup", [
            ("•", "Customize the Cold_Outreach_Templates.docx with your name and agency"),
            ("•", "Set up the Referral_Partner_Program.docx with your top 10 referral partners"),
            ("•", "Schedule your first 5 prospecting calls using the Phone_Prospecting_Scripts.docx"),
            ("•", "Activate the Digital_Lead_Nurture_Sequence.docx in your email system"),
        ]),
        ("Day 4-5 — Sales Process", [
            ("•", "Practice the Needs_Analysis_Framework.docx with a roleplay partner"),
            ("•", "Customize the Insurance_Proposal_Template.docx with your agency branding"),
            ("•", "Review the Objection_Handling_Scripts.docx — know every response cold"),
            ("•", "Set up your quoting workflow using the Multi_Carrier_Quoting_SOP.docx"),
        ]),
        ("Day 6-7 — Client Systems", [
            ("•", "Send a check-in to your top 20 clients using the Annual_Review_Scripts.docx"),
            ("•", "Schedule 3 Annual Review appointments for next week"),
            ("•", "Post your first social media content using the 365 captions CSV"),
            ("•", "Review your agency's compliance status against the Compliance_Checklist.docx"),
        ]),
    ])

doc("00_START_HERE/Product_Overview.docx",
    "Insurance Agency Operating System — Product Overview",
    "Everything You Need to Run a Professional, Profitable Insurance Agency",
    [
        ("What Is the Insurance Agency OS?", [
            "The Insurance Agency Operating System is a complete business-in-a-box for independent insurance agents and agency owners. It combines proven sales scripts, operational SOPs, client management tools, compliance guides, and marketing templates into one unified system.",
            ("•", "60+ professional templates, tools, and systems"),
            ("•", "Coverage for every major insurance line: P&C, life, health, commercial"),
            ("•", "Compliant frameworks for E&O protection and state licensing"),
            ("•", "Canva-ready client presentation templates"),
            ("•", "Notion-based agency CRM system"),
            ("•", "365 days of insurance-specific social media content"),
        ]),
        ("Who Is This For?", [
            ("•", "Independent insurance agents building their book of business"),
            ("•", "New agents entering the industry who need proven frameworks"),
            ("•", "Agency owners looking to systematize their operations"),
            ("•", "Captive agents transitioning to independent status"),
            ("•", "Insurance agency producers and CSRs seeking professional templates"),
        ]),
        ("How to Get Maximum Value", [
            ("•", "Customize every template with your agency name, logo, and contact info"),
            ("•", "Use the scripts as starting points — make them sound like you"),
            ("•", "Implement one new system per week rather than trying to do everything at once"),
            ("•", "Share the training documents with your team and new hires"),
            ("•", "Return to this system quarterly to refresh your approach"),
        ]),
    ])

print("✓ 00_START_HERE complete")

# ─── 01_LEAD_GENERATION ────────────────────────────────────────────────────────
p01 = "01_LEAD_GENERATION/"

doc(p01+"Phone_Prospecting_Scripts.docx",
    "Phone Prospecting Scripts",
    "Insurance Agency OS | Cold Calling, Warm Leads & Referral Scripts",
    [
        ("Cold Call Opening — Personal Lines", [
            "Script A — Homeowner Prospecting:",
            '"Hi, may I speak with [Name]? [...] Hi [Name], my name is [Agent] with [Agency]. I\'m a local insurance specialist and I work with homeowners in [City] to make sure they\'re getting the best value on their home and auto coverage. I\'m not here to sell you anything today — I just want to offer you a complimentary 5-minute policy review. We typically save clients $300-$800 per year. Would Tuesday or Wednesday be better for a quick call?"',
            "Script B — Auto Insurance Prospect:",
            '"Hi [Name], this is [Agent] from [Agency]. I specialize in helping drivers in [City] get better coverage at lower rates. Quick question — when did you last shop your auto insurance? [...] Most people we talk to are paying $200-$400 more than they need to. Could I take 5 minutes to run a comparison quote for you at no cost?"',
        ]),
        ("Cold Call Opening — Commercial Lines", [
            "Script — Business Owner Prospecting:",
            '"Hello, is this [Business Owner Name]? Hi [Name], I\'m [Agent] with [Agency]. We specialize in commercial insurance for [industry type] businesses in [City]. I noticed your business on [LinkedIn/Google/neighborhood] and wanted to reach out personally. I\'ve helped [X] local businesses just like yours reduce their premiums while improving their coverage. Could I schedule a 15-minute business insurance review this week?"',
        ]),
        ("Warm Lead Follow-Up Scripts", [
            "Web Lead — Callback Within 5 Minutes:",
            '"Hi [Name], this is [Agent] calling from [Agency]. I see you requested an insurance quote on our website just a few minutes ago. I wanted to call personally to make sure I can get you exactly what you need. Do you have 5 minutes right now, or would another time work better?"',
            "Referral Lead — First Call:",
            '"Hi [Name], my name is [Agent] with [Agency]. [Referring Person] suggested I reach out — they mentioned you might be in the market for [insurance type]. [Referring Person] is a great client of mine and I\'d love to help you the same way I\'ve helped them. When would be a good time to sit down for 20 minutes?"',
        ]),
        ("Voicemail Scripts", [
            "Voicemail — Personal Lines Prospect:",
            '"Hi [Name], this is [Agent] at [Agency], number is [Phone]. I\'m a local insurance specialist and I wanted to reach out about your home and auto coverage. We\'ve been helping families in [City] save hundreds per year on their policies. Give me a call back when you have 5 minutes — I think we can do the same for you. Again, that\'s [Agent] at [Phone]. Talk soon!"',
            "Voicemail — Referral:",
            '"Hi [Name], this is [Agent] from [Agency]. Your [friend/colleague] [Name] suggested I reach out — they thought we might be able to help you with your insurance needs. Give me a call at [Phone] when you get a chance. I\'d love to have a quick conversation. Looking forward to connecting!"',
        ]),
        ("Handling Common Gatekeepers", [
            "Gatekeeper: 'They\'re not available right now.'",
            '"Of course — when is the best time to reach [Name]? And is email a good way to follow up in the meantime?"',
            "Gatekeeper: 'We\'re happy with our current insurance.'",
            '"That\'s great to hear — most of our best clients said the same thing before we did a review! We\'re not here to replace your agent, just to make sure you\'re getting maximum value. We find $300-$500 in savings for most families we review. Would [Name] be open to a 5-minute comparison?"',
        ]),
    ])

doc(p01+"Digital_Lead_Nurture_Sequence.docx",
    "Digital Lead Nurture Email Sequence",
    "Insurance Agency OS | 8-Email Follow-Up System for Online Leads",
    [
        ("Sequence Overview", [
            "Send this 8-email sequence to all web-generated leads. The sequence runs over 21 days and is designed to educate, build trust, and convert leads who don't respond to initial phone calls.",
            ("•", "Email 1 (Day 0): Immediate confirmation and introduction"),
            ("•", "Email 2 (Day 1): Value-add tip — '3 things to look for in your current policy'"),
            ("•", "Email 3 (Day 3): Social proof — client success story"),
            ("•", "Email 4 (Day 5): Educational content — insurance myths debunked"),
            ("•", "Email 5 (Day 8): Quote reminder and easy next step"),
            ("•", "Email 6 (Day 12): Market insight — 'What's changing in insurance rates'"),
            ("•", "Email 7 (Day 16): Risk story — 'What happens without the right coverage'"),
            ("•", "Email 8 (Day 21): Final outreach with direct offer"),
        ]),
        ("Email 1 — Immediate Confirmation", [
            "Subject: Your Insurance Quote Request — [Name], I'll Be In Touch Shortly",
            "Hi [Name],",
            "Thank you for reaching out to [Agency Name]! I wanted to personally confirm that I received your request and I'm already working on finding you the best rates available.",
            "A little about me: I'm [Agent Name], a licensed insurance specialist serving [City/Region]. I work with [X] carriers to find the right coverage at the right price for every client.",
            "I'll be calling you at [Phone] within the next few hours. In the meantime, feel free to reach me directly at [Agent Phone] or reply to this email with any questions.",
            "Looking forward to serving you!",
            "[Signature]",
        ]),
        ("Email 3 — Social Proof", [
            "Subject: How I Saved the [Generic Family] Family $687 Last Year",
            "Hi [Name],",
            "I wanted to share a quick story about a family I worked with last year.",
            "The [Family] had been with the same insurance company for 11 years. They assumed loyalty meant they were getting the best rate. When they finally called me for a second opinion, I found them $687 in annual savings — same coverage, better carrier.",
            "This happens more than you might think. Insurance companies often raise rates slowly over time, knowing most people won't shop around.",
            "I'd love to do the same for you. I can run a full comparison in about 10 minutes. Would [Tuesday] or [Wednesday] work for a quick call?",
            "[Signature]",
        ]),
        ("Email 8 — Final Outreach", [
            "Subject: Last chance to save on your insurance, [Name]",
            "Hi [Name],",
            "I've reached out a few times over the past few weeks and I don't want to be a bother — but I also don't want to give up without making sure you had every opportunity to potentially save money on your coverage.",
            "If you're happy with your current policy, that's great! I just want to make sure you know that a free, no-obligation review is always available whenever you're ready.",
            "If now isn't the right time, no worries at all — I'd love to stay in touch and be your resource whenever insurance questions come up.",
            "You can reach me anytime at [Phone] or [Email]. Thanks for considering [Agency Name] — I hope to earn your business someday!",
            "[Signature]",
        ]),
    ])

doc(p01+"Referral_Partner_Program.docx",
    "Referral Partner Program",
    "Insurance Agency OS | Building Your Center of Influence Network",
    [
        ("Why Referral Partners Are Your #1 Lead Source", [
            "Referral leads close at 3-5x the rate of cold leads and have significantly higher lifetime value. Building a network of Centers of Influence (COIs) — professionals who interact with your ideal clients — is the most efficient growth strategy for an insurance agency.",
            ("•", "Top referral partner categories: mortgage brokers, real estate agents, financial advisors, CPAs, attorneys, car dealerships, HR managers"),
            ("•", "Goal: Develop 10-20 active referral partners who each send 2-5 referrals per year"),
            ("•", "Reciprocity is key: Always look for ways to refer business back to your partners"),
        ]),
        ("Referral Partner Outreach Sequence", [
            "Step 1 — Identify: Create a list of 30 local professionals who serve your ideal clients",
            "Step 2 — Research: LinkedIn, website, mutual connections — know their business before reaching out",
            "Step 3 — Connect: Phone call or LinkedIn message introducing yourself",
            "Step 4 — Meet: Coffee or lunch meeting to explore a referral relationship",
            "Step 5 — Formalize: Agree on how referrals will be exchanged and tracked",
            "Step 6 — Nurture: Monthly check-in, quarterly lunch, annual thank-you",
        ]),
        ("Referral Partner Meeting Script", [
            '"[Name], I appreciate you taking the time to meet. I work primarily with [client type] in [City], and I\'ve noticed we serve a lot of the same people. I\'d love to explore whether we could create a mutually beneficial referral relationship."',
            '"Here\'s how I typically work: when I have clients who need [their service], I\'ll refer them directly to you. And when your clients have questions about [insurance type], I hope you\'ll think of me. There\'s no formal agreement required — just a handshake understanding that we\'ll look out for each other\'s clients."',
            '"Would that work for you?"',
        ]),
        ("Referral Tracking System", [
            ("•", "Log every referral received in your CRM: source, date, outcome"),
            ("•", "Send a thank-you note within 24 hours of receiving a referral"),
            ("•", "Update referral partners on outcome: 'Your referral closed — thank you!'"),
            ("•", "Track top referral sources monthly and invest more time in those relationships"),
            ("•", "Review and celebrate: Share top referral partner results quarterly"),
        ]),
        ("Referral Thank-You Program", [
            ("•", "Written thank-you note: Always, within 24 hours of receiving a referral"),
            ("•", "Small gift after closed referral: Gift card, restaurant gift, bottle of wine"),
            ("•", "Annual appreciation: Holiday gift, event invitation, lunch"),
            ("•", "Public recognition: Tag on social media, testimonial feature, LinkedIn recommendation"),
        ]),
    ])

doc(p01+"Cold_Outreach_Templates.docx",
    "Cold Outreach Templates",
    "Insurance Agency OS | Email, LinkedIn & Direct Mail Templates",
    [
        ("Cold Email Templates — Personal Lines", [
            "Template A — Homeowner Cold Email:",
            "Subject: Quick question about your home insurance, [Name]",
            "Hi [Name],",
            "My name is [Agent] and I'm a local insurance specialist serving homeowners in [City]. I help families like yours make sure they have the right coverage without paying more than they need to.",
            "Quick question: when did you last compare your home and auto rates? Most families I work with are overpaying by $300-$800 per year without realizing it.",
            "I'd love to offer you a complimentary 10-minute policy review — no pressure, no obligation. Would [Day] or [Day] work for a quick call?",
            "[Signature]",
        ]),
        ("Cold Email Templates — Commercial Lines", [
            "Template B — Small Business Cold Email:",
            "Subject: Is your business coverage keeping up with your growth, [Name]?",
            "Hi [Name],",
            "I came across [Business Name] while researching [industry] businesses in [City]. Congratulations on your growth — it's clear you're building something impressive.",
            "As businesses grow, insurance needs change — and many owners don't realize their coverage has gaps until a claim occurs. I specialize in helping [industry] businesses make sure their policies match their actual risk profile.",
            "Could I schedule a 20-minute business insurance audit at no cost? I'll identify any coverage gaps and compare your current rates with what's available in the market today.",
            "[Signature]",
        ]),
        ("LinkedIn Outreach Templates", [
            "Connection Request Message:",
            '"Hi [Name], I noticed we\'re both connected to [Mutual Connection] and serve the [City] area. I\'m an independent insurance specialist focused on helping [business owners/families] protect what matters most. Would love to connect!"',
            "Follow-Up After Connection Accepted:",
            '"Thanks for connecting, [Name]! I noticed you\'re in [industry] — I actually work with quite a few [industry] professionals on their insurance needs. Would you be open to a quick 15-minute call to explore whether I might be able to add value for you or your clients?"',
        ]),
        ("Direct Mail Templates", [
            "New Homeowner Postcard (send within 30 days of home purchase):",
            "Headline: CONGRATULATIONS ON YOUR NEW HOME, [NAME]!",
            "Body: As you settle into [City], I'd love to help you make sure your new home is properly protected. As a local insurance specialist, I offer complimentary policy reviews and often find savings of $300-$600 for new homeowners.",
            "Call to Action: Call [Phone] or visit [Website] for a free 10-minute review.",
            "Business Anniversary Mailer:",
            "Subject: Congratulations on [X] years in business, [Name]!",
            "Body: As your business grows, your insurance needs grow too. I'd love to offer a complimentary commercial insurance review to make sure you're protected and not overpaying.",
        ]),
    ])

doc(p01+"Social_Media_Lead_Strategy.docx",
    "Social Media Lead Generation Strategy",
    "Insurance Agency OS | Facebook, Instagram, LinkedIn & YouTube Playbook",
    [
        ("Social Media Platform Strategy", [
            ("•", "Facebook: Best for reaching homeowners and families; great for paid ads targeting by homeownership, age, income"),
            ("•", "Instagram: Best for younger audiences, visual content, stories, and reels about financial protection"),
            ("•", "LinkedIn: Best for commercial lines prospects, business owners, HR managers, and referral partners"),
            ("•", "YouTube: Best for educational content — 'What is [coverage type]?' videos build long-term SEO and trust"),
            ("•", "Nextdoor: Best for hyper-local personal lines leads — neighborhood focus drives trust"),
        ]),
        ("Content Strategy — The 3-2-1 Rule", [
            ("•", "3 posts per week: Educational content (insurance tips, coverage explanations, myth-busting)"),
            ("•", "2 posts per week: Social proof (testimonials, client win stories, reviews)"),
            ("•", "1 post per week: Personal brand (your story, your why, behind-the-scenes agency life)"),
        ]),
        ("Facebook Ad Strategy", [
            ("•", "Target: Homeowners, age 30-65, within 25 miles of your agency"),
            ("•", "Ad Offer: Free insurance review, free quote, '5 mistakes homeowners make with insurance'"),
            ("•", "Budget: Start at $10-$20/day; scale what works"),
            ("•", "Landing page: Simple form — name, phone, email, type of insurance needed"),
            ("•", "Follow-up: Call within 5 minutes of form submission"),
        ]),
        ("LinkedIn Strategy for Commercial Lines", [
            ("•", "Connect with: Business owners, CFOs, HR managers, office managers in your area"),
            ("•", "Post content: Workers comp tips, business interruption coverage, cyber liability risks"),
            ("•", "Message sequence: Connect → value message → meeting request"),
            ("•", "Goal: 5 new commercial prospect connections per week; 2 meetings per month"),
        ]),
        ("Video Content Ideas", [
            ("•", "'Why your homeowner's insurance might not cover [common gap]'"),
            ("•", "'5 questions to ask your insurance agent at renewal'"),
            ("•", "'How umbrella insurance works and why every family needs it'"),
            ("•", "'What IS an independent insurance agent and how are we different?'"),
            ("•", "'Commercial insurance 101 — what every business owner must know'"),
        ]),
    ])

doc(p01+"Networking_Event_Scripts.docx",
    "Networking Event Scripts",
    "Insurance Agency OS | Chamber, BNI, and Community Event Prospecting",
    [
        ("Elevator Pitch Variations", [
            "The 10-Second Version:",
            '"I\'m [Name] — I help families and businesses in [City] make sure they\'re protected without overpaying. Independent insurance."',
            "The 30-Second Version:",
            '"I own [Agency Name], an independent insurance agency in [City]. Unlike captive agents who work for one company, I represent dozens of carriers — so I can shop the entire market to find the best coverage and rates for each client. We specialize in home, auto, life, and commercial insurance. If you\'ve never had someone shop your insurance, I\'d love to buy you coffee and do a quick comparison."',
            "The Story Version (60 seconds):",
            '"A client called me in a panic last year — their basement flooded and they assumed they were covered. They weren\'t. Their standard policy didn\'t cover flooding. I\'ve made it my mission to make sure every client truly understands what they have — and what they don\'t. That\'s what separates a great insurance agent from a policy vendor. I\'m [Name], with [Agency]."',
        ]),
        ("Chamber of Commerce Event Strategy", [
            ("•", "Arrive 15-20 minutes early — meet organizers and early arrivals"),
            ("•", "Goal: Have 5-8 genuine conversations per event — not 30 business card handoffs"),
            ("•", "Ask about them first: 'What does your business do? Who's your ideal client?'"),
            ("•", "Listen for insurance hooks: 'We just hired 10 people,' 'We moved to a new building,' 'We're growing fast'"),
            ("•", "Follow up within 24 hours with a personalized email or LinkedIn message"),
        ]),
        ("BNI and Leads Group Strategy", [
            ("•", "30-second commercial rotation: Vary it every week to stay fresh"),
            ("•", "Focus your 30-second on ONE specific insurance problem each week"),
            ("•", "Ask for specific referrals: 'I'm looking for introductions to business owners with 5+ employees in [industry]'"),
            ("•", "Give first: Refer to BNI members actively before asking for referrals"),
            ("•", "Track ROI: Calculate leads, clients, and premium generated per year from BNI"),
        ]),
    ])

print("✓ 01_LEAD_GENERATION complete")

# ─── 02_SALES_PROCESS ─────────────────────────────────────────────────────────
p02 = "02_SALES_PROCESS/"

doc(p02+"Needs_Analysis_Framework.docx",
    "Insurance Needs Analysis Framework",
    "Insurance Agency OS | Comprehensive Client Discovery Process",
    [
        ("Why Needs Analysis Is the Foundation of Sales", [
            "The best insurance agents don't sell policies — they solve problems. The Needs Analysis is your discovery process: understanding a prospect's full picture before recommending any coverage. Agents who skip this step sell on price. Agents who master it sell on value and build lifetime clients.",
        ]),
        ("Personal Lines Needs Analysis — Key Questions", [
            "Property & Casualty:",
            ("•", "How long have you owned your home? Has it been updated — roof, electrical, plumbing, HVAC?"),
            ("•", "What's the square footage and estimated replacement cost of your home?"),
            ("•", "Do you have any home-based business activities?"),
            ("•", "What personal property do you have that might need a scheduled endorsement (jewelry, art, instruments)?"),
            ("•", "Do you have any water or sewer backup exposure?"),
            "Auto:",
            ("•", "How many vehicles and drivers in the household?"),
            ("•", "What are the annual mileage estimates for each vehicle?"),
            ("•", "Do any household members use vehicles for rideshare (Uber/Lyft) or delivery?"),
            ("•", "Have there been any accidents or violations in the past 5 years?"),
            "Life & Financial:",
            ("•", "Do you have dependents who rely on your income?"),
            ("•", "Do you have existing life insurance? How much and what type?"),
            ("•", "What would happen to your family if you were unable to work for 6 months?"),
            ("•", "Are you familiar with the concept of income replacement?"),
        ]),
        ("Commercial Lines Needs Analysis — Key Questions", [
            ("•", "What type of business do you operate and what are your primary revenue sources?"),
            ("•", "Do you have employees? If yes, how many full-time and part-time?"),
            ("•", "Do you own or lease your commercial space? What is the square footage and value?"),
            ("•", "Do you have business vehicles, equipment, or inventory to insure?"),
            ("•", "Are you required to carry a minimum liability limit by any contracts or clients?"),
            ("•", "Do you handle sensitive customer data or run a website? Cyber liability exposure?"),
            ("•", "What would it cost your business to shut down for 60-90 days unexpectedly?"),
            ("•", "Are you currently satisfied with your agent's responsiveness and coverage explanations?"),
        ]),
        ("The Risk Exposure Summary", [
            "After gathering information, summarize the prospect's risk profile before presenting solutions:",
            '"Based on what you\'ve shared with me, here\'s what I\'m seeing in terms of your risk exposure: [Summary]. The areas where I\'m most concerned about potential gaps are [Gaps]. Here\'s what I\'d recommend we focus on today..."',
        ]),
    ])

doc(p02+"Insurance_Proposal_Template.docx",
    "Insurance Proposal Template",
    "Insurance Agency OS | Professional Quote Presentation Framework",
    [
        ("Proposal Structure", [
            "A professional insurance proposal has 6 sections: Introduction, Risk Summary, Coverage Recommendations, Carrier Options, Premium Comparison, and Next Steps. Always present proposals in person or on a video call — never just email a quote.",
        ]),
        ("Section 1 — Introduction Page", [
            "Include at the top of every proposal:",
            ("•", "Agency name, logo, and agent contact information"),
            ("•", "Client name, date, and 'Prepared exclusively for [Name]'"),
            ("•", "Statement: 'This proposal represents my professional recommendation based on our needs analysis conversation'"),
        ]),
        ("Section 2 — Risk Summary", [
            "Summarize what you learned in the needs analysis. This shows the client you listened:",
            '"Based on our conversation on [Date], here\'s a summary of your insurance needs: You\'re looking for coverage for [property/vehicles/business]. Key exposures we identified include [exposures]. Your primary goals are [price savings / better coverage / specific gap fills]."',
        ]),
        ("Section 3 — Coverage Recommendations", [
            ("•", "List each recommended coverage line with plain-English explanations"),
            ("•", "Explain WHY each coverage is recommended (not just what it covers)"),
            ("•", "Highlight any coverage gaps from their current policy that your proposal fills"),
            ("•", "Use comparison tables: Current Coverage vs. Recommended Coverage"),
        ]),
        ("Section 4 — Carrier Options", [
            ("•", "Present 2-3 carrier options with brief carrier profiles and ratings"),
            ("•", "Explain what differentiates each carrier (claims service, financial strength, specialty coverages)"),
            ("•", "Make a clear recommendation: 'Based on your needs, I recommend [Carrier] because...'"),
        ]),
        ("Section 5 — Premium Comparison", [
            ("•", "Show current premium vs. proposed premium side-by-side"),
            ("•", "Calculate annual savings and 5-year savings"),
            ("•", "Break down the premium by coverage type"),
            ("•", "Include payment options: annual, semi-annual, monthly"),
        ]),
        ("Proposal Presentation Script", [
            '"[Name], I\'ve put together a proposal based on everything we discussed. What I\'d like to do is walk you through it section by section so you can see exactly what I\'m recommending and why. [Walk through proposal]. Does this coverage picture make sense for your situation?"',
            '"Now, looking at the numbers — you\'re currently paying $[Current] per year. My recommendation comes in at $[Proposed] — that\'s a savings of $[Savings] annually. And importantly, the coverage is actually stronger in [specific areas]. Does that feel like a good value to you?"',
        ]),
    ])

doc(p02+"Objection_Handling_Scripts.docx",
    "Objection Handling Scripts",
    "Insurance Agency OS | Responses to Every Common Sales Objection",
    [
        ("Price Objections", [
            "'Your price is higher than what I'm paying now':",
            '"That\'s a fair point, and I appreciate you bringing it up. Can I ask — when you\'re comparing prices, are you comparing the exact same coverage? The most common reason someone finds a lower price elsewhere is because coverage is being reduced somewhere — sometimes in ways that aren\'t obvious. Let me pull up a side-by-side comparison so we can look at this together."',
            "'I can't afford insurance right now':",
            '"I completely understand — budgets are tight for everyone. Here\'s what I want you to think about though: the cost of being without the right insurance is almost always far greater than the premium. Can we look at what options exist at different price points? There may be ways to get essential coverage within your budget."',
            "'I got a quote online for less':",
            '"Online quotes are a starting point, not a final price. What you see online is almost always based on estimated data — and when they pull the actual reports (MVR, credit, claims history), the price often changes. Also, online quotes can\'t analyze your specific risk exposures the way I can. Let me show you what a properly structured policy looks like for your situation."',
        ]),
        ("Loyalty Objections", [
            "'I've been with my company for 20 years':",
            '"That\'s loyalty, and I respect it. I\'m not asking you to necessarily leave them. What I AM asking is: has anyone reviewed your coverage and compared your rates in the last 3 years? Insurance companies don\'t reward loyalty the way people think. Let me run a comparison — if they\'re still the best option, great! You\'ll have peace of mind. If not, you\'ll have valuable information."',
        ]),
        ("Trust Objections", [
            "'I don't know you / I need to think about it':",
            '"Of course — I\'d expect you to want to think it over. Can I ask what specifically you\'d like to think about? I want to make sure I\'ve given you everything you need to make a decision. Is it the price, the coverage, or something about me or my agency?"',
            "'I want to ask my [spouse/partner]':",
            '"Absolutely — this is a household decision. Would it be possible to get [spouse/partner] on a call this week? I\'m happy to do a quick 15-minute review with both of you so we can answer questions together. When would work for you both?"',
        ]),
    ])

doc(p02+"Multi_Carrier_Quoting_SOP.docx",
    "Multi-Carrier Quoting SOP",
    "Insurance Agency OS | Efficient, Compliant Quoting Workflow",
    [
        ("Step 1 — Gather Required Information", [
            "Personal Lines — Required Info:",
            ("•", "Full legal names and dates of birth for all applicants"),
            ("•", "Social Security Numbers (required for most personal lines carriers)"),
            ("•", "Driver's license numbers and years licensed"),
            ("•", "Property address, year built, square footage, construction type"),
            ("•", "Current carrier, current premium, and coverage limits"),
            "Commercial Lines — Required Info:",
            ("•", "Business legal name, DBA, FEIN"),
            ("•", "Years in business, number of locations, gross revenue"),
            ("•", "Number of employees (full-time and part-time)"),
            ("•", "Claims history for the past 5 years (loss runs)"),
        ]),
        ("Step 2 — Market Selection", [
            ("•", "Personal Lines: Start with your top 3-4 standard market carriers"),
            ("•", "If non-standard risk (poor credit, prior claims, lapse): Move to E&S or specialty markets"),
            ("•", "Commercial: Match the risk to the carrier's appetite — always check underwriting guidelines first"),
            ("•", "Always quote a minimum of 2-3 carriers per client to demonstrate market access value"),
        ]),
        ("Step 3 — Quote and Compare", [
            ("•", "Run quotes in each carrier's system with identical coverage parameters"),
            ("•", "Document all quotes with premium, carrier, AM Best rating, and coverage differences"),
            ("•", "Note any variances in coverage terms between carriers"),
            ("•", "Calculate comparable pricing by adjusting to same deductibles and limits"),
        ]),
        ("Step 4 — Quote Review Checklist", [
            ("•", "Verify all information entered matches what client provided"),
            ("•", "Confirm coverage limits meet state minimums and client's exposure"),
            ("•", "Check for any exclusions that need to be disclosed to client"),
            ("•", "Confirm carrier is currently admitted and in good standing in the client's state"),
            ("•", "Review payment options and note installment fees"),
        ]),
        ("Step 5 — Present and Bind", [
            ("•", "Present proposal in person or via video call — never email-only"),
            ("•", "Get verbal agreement before collecting payment or running applications"),
            ("•", "Collect signed applications and authorization before binding"),
            ("•", "Issue binder immediately upon binding and send to client"),
            ("•", "Send new client welcome email and onboarding instructions"),
        ]),
    ])

doc(p02+"Closing_Techniques.docx",
    "Insurance Sales Closing Techniques",
    "Insurance Agency OS | Assumptive, Summary & Action-Oriented Closes",
    [
        ("The Assumptive Close", [
            "After presenting the proposal and getting positive signals:",
            '"So based on everything we\'ve gone through, it looks like [Carrier] with [Coverage] is the right fit for you. To get this started, I\'ll just need your credit card for the first payment and your signature on the application. Does that work for you?"',
        ]),
        ("The Summary Close", [
            "Recap the key benefits before asking for the decision:",
            '"Let me just recap what we\'re putting together for you: [Coverage A] protects your home, [Coverage B] covers your vehicles, and [Coverage C] adds that extra liability layer we talked about. All together, that\'s $[Premium]/month — and you\'re saving $[X] compared to what you\'re paying now. Are you ready to move forward?"',
        ]),
        ("The Fear of Loss Close", [
            "Use sparingly and only when a real risk exists:",
            '"I want to make sure you understand what happens if something occurs before we get this in place. Your current policy expires on [Date], and with no coverage in force, a single incident could result in a claim you\'d have to pay entirely out of pocket. I can have your new coverage effective today — can we get this signed now?"',
        ]),
        ("The Trial Close", [
            "Use throughout the presentation to gauge interest:",
            '"How does this coverage compare to what you have now?"',
            '"Is the premium in the range you were expecting?"',
            '"If this were the coverage you decided to go with, when would you want it to start?"',
        ]),
        ("Handling 'I need to think about it'", [
            '"Of course — I want you to be comfortable with this decision. Can I ask, is it the price, the coverage, or the carrier that you want to think through? Often I can answer those questions right now and save you some time."',
            '"What would need to happen for you to feel comfortable moving forward?"',
        ]),
    ])

print("✓ 02_SALES_PROCESS complete")

# ─── 03_POLICY_SERVICES ────────────────────────────────────────────────────────
p03 = "03_POLICY_SERVICES/"

doc(p03+"New_Client_Onboarding_SOP.docx",
    "New Client Onboarding SOP",
    "Insurance Agency OS | From Bind to Loyal Client in 30 Days",
    [
        ("Onboarding Objectives", [
            "The first 30 days of a client relationship set the tone for the next 10 years. A systematic onboarding process reduces early cancellations, generates referrals, and positions you as a trusted advisor rather than just a policy vendor.",
        ]),
        ("Day 0 — Binding Day", [
            ("•", "Issue binder immediately and email to client"),
            ("•", "Send 'Welcome to [Agency]!' email with what to expect next"),
            ("•", "Create client file in your CRM with all policy details"),
            ("•", "Set up reminders for 30-day check-in, 6-month review, and annual renewal"),
            ("•", "For home/auto: Confirm mortgage company and lender received proof of insurance"),
        ]),
        ("Day 3 — Policy Delivery Call", [
            '"Hi [Name], this is [Agent] from [Agency]. I\'m calling to confirm that your new [policy type] policy has been issued and to walk you through your policy documents. Do you have a few minutes? [...] Your policy number is [Number], effective [Date]. I want to make sure you know exactly who to call in case of a claim — and I\'ll give you my personal cell number as well."',
            ("•", "Walk through the declarations page"),
            ("•", "Explain the claims process"),
            ("•", "Answer any questions"),
            ("•", "Ask for referrals: 'By the way, if you know anyone who might benefit from a policy review, I\'d be honored if you\'d pass along my name.'"),
        ]),
        ("Day 30 — New Client Check-In", [
            ("•", "Call or email: 'Just wanted to check in and make sure everything is going smoothly with your new policy'"),
            ("•", "Confirm auto ID cards were received (for auto policies)"),
            ("•", "Confirm mortgagee received insurance verification"),
            ("•", "Ask: 'Is there anything about your coverage we didn\'t discuss that you have questions about?'"),
            ("•", "Note any upcoming life changes: new vehicle, home renovation, business expansion"),
        ]),
        ("Day 90 — Cross-Sell Touchpoint", [
            "At the 90-day mark, review what other coverage needs the client may have:",
            ("•", "Personal lines: Do they have life insurance? Umbrella? Flood? Jewelry rider?"),
            ("•", "Commercial lines: Do they have cyber liability? Employment practices? Workers comp?"),
            ("•", "Use the cross-sell script: 'Now that we\'ve had a few months together and you\'ve seen how I work, I\'d love to take a look at your [life/umbrella/commercial] coverage as well. Many clients find additional value when we look at their complete picture.'"),
        ]),
    ])

doc(p03+"Annual_Policy_Review_SOP.docx",
    "Annual Policy Review SOP",
    "Insurance Agency OS | The Most Powerful Retention and Cross-Sell Tool",
    [
        ("Why Annual Reviews Are Non-Negotiable", [
            "The annual policy review is the most important activity in your retention strategy. Clients who receive annual reviews stay 60% longer and generate 3x more referrals. It also gives you a structured opportunity to identify coverage gaps and cross-sell additional policies.",
            ("•", "Schedule annual reviews 60-90 days before each client's renewal date"),
            ("•", "Review every client — not just 'problem' accounts"),
            ("•", "Use a structured checklist to ensure consistency across all reviews"),
        ]),
        ("Pre-Review Preparation", [
            ("•", "Pull the client's current policy declarations pages"),
            ("•", "Review claims history for the past year"),
            ("•", "Check for any rate changes at renewal"),
            ("•", "Research if any carrier changes affect the client's coverage"),
            ("•", "Note any life changes from CRM: new car, home renovation, new baby, business growth"),
        ]),
        ("Annual Review Call Script", [
            '"Hi [Name], this is [Agent] from [Agency]. I\'m calling because your [policy type] renewal is coming up in [X weeks], and I schedule an annual review with every client to make sure your coverage still makes sense for your situation. Do you have about 15 minutes?"',
            '"A few things I want to cover: your current coverage limits, any changes in your situation this past year, and I also want to make sure you\'re getting the best rate available. Does that sound good?"',
        ]),
        ("Annual Review Checklist", [
            ("•", "Property: Any renovations, additions, or improvements? Updated replacement cost value?"),
            ("•", "Vehicles: Any new vehicles, drivers, or usage changes?"),
            ("•", "Life Changes: Marriage, divorce, new baby, children leaving home?"),
            ("•", "Business: Any new business activities from the home? Business vehicles?"),
            ("•", "Liabilities: Any new exposures — pool, trampoline, vacation rental?"),
            ("•", "Coverage Gaps: Do they have umbrella, flood, cyber, or other needed coverages?"),
            ("•", "Claims: Any unreported incidents that could affect coverage?"),
        ]),
        ("Cross-Sell Opportunities Identified in Reviews", [
            ("•", "Homeowner without umbrella: 'Your liability limits are $300K — for most families, we recommend an umbrella policy for an extra $1-2M of protection at around $200-$300/year. Want me to include that in your renewal?'"),
            ("•", "Family without life insurance: 'I noticed we don\'t have any life insurance on file for you. Do you have coverage elsewhere, or is this something we should talk about?'"),
            ("•", "Business owner without commercial coverage: 'Are you still working from home on [business activity]? I want to make sure you know that standard homeowner's policies typically exclude business activities.'"),
        ]),
    ])

doc(p03+"Policy_Endorsement_Request_SOP.docx",
    "Policy Endorsement Request SOP",
    "Insurance Agency OS | Processing Changes, Additions & Modifications",
    [
        ("Types of Endorsements", [
            ("•", "Add a vehicle or driver"),
            ("•", "Remove a vehicle or driver"),
            ("•", "Change address or primary garage location"),
            ("•", "Add a lienholder or mortgagee"),
            ("•", "Increase or decrease coverage limits"),
            ("•", "Add a scheduled personal property item"),
            ("•", "Add or remove a named insured"),
            ("•", "Add a business use endorsement"),
        ]),
        ("Endorsement Request Process", [
            "Step 1: Receive request from client (phone, email, text, or portal)",
            "Step 2: Verify client identity and confirm policy number",
            "Step 3: Assess the change request and any underwriting implications",
            "Step 4: Process in carrier portal or send to carrier's service team",
            "Step 5: Confirm change was processed and document in CRM",
            "Step 6: Send updated declarations page or ID card to client",
            "Step 7: Note any premium changes and confirm with client",
        ]),
        ("Same-Day vs. Next-Day Service Standards", [
            ("•", "Same-day priority: Adding a new vehicle (coverage needed immediately), adding a driver after a life event, address change for active claims"),
            ("•", "Next business day: Coverage limit changes, removing listed items, adding scheduled property"),
            ("•", "Notify client of timeline within 1 hour of receiving the request"),
        ]),
        ("Endorsement Communication Template", [
            "Subject: Policy Update Confirmation — [Client Name]",
            "Hi [Name],",
            "Your policy change request has been processed. Here's a summary:",
            "Change Made: [Description]",
            "Effective Date: [Date]",
            "Premium Impact: [+ or - $ per month / year]",
            "Please review your updated declarations page attached. If anything looks incorrect, please contact me immediately.",
            "[Signature]",
        ]),
    ])

doc(p03+"Cross_Sell_Upsell_Playbook.docx",
    "Cross-Sell & Upsell Playbook",
    "Insurance Agency OS | Maximizing Client Lifetime Value",
    [
        ("Cross-Sell Philosophy", [
            "The best cross-sell isn't a sales pitch — it's an act of service. Your job is to identify coverage gaps that expose clients to risk, then educate them about solutions. Clients who carry 3+ policies with your agency have an 85% retention rate vs. 50% for single-policy clients.",
        ]),
        ("The Cross-Sell Trigger Map", [
            "Life Event → Insurance Opportunity:",
            ("•", "Bought a new home → Homeowner's + flood + umbrella + life"),
            ("•", "Got married → Bundle home/auto + life insurance review"),
            ("•", "Had a child → Life insurance + disability + education savings"),
            ("•", "Started a business → BOP + commercial auto + cyber + workers comp"),
            ("•", "Purchased a boat/RV → Watercraft/recreational vehicle policy"),
            ("•", "Parent moved in → Additional named insured + life review"),
            ("•", "Teen driver added → Umbrella upgrade recommendation"),
            ("•", "Retirement approaching → Medicare supplement + annuity + life review"),
        ]),
        ("Cross-Sell Scripts", [
            "Umbrella Cross-Sell:",
            '"I want to bring something to your attention. You have $300,000 in personal liability on your home policy and $250,000 on your auto. In today\'s world, a serious auto accident or someone getting hurt on your property could easily exceed those limits. A personal umbrella policy gives you an extra $1-2 million of coverage for about $200-$300 per year. It\'s one of the best values in insurance. Can I run a quick quote for you?"',
            "Life Insurance Cross-Sell:",
            '"I noticed we handle your property and auto coverage but I don\'t see any life insurance on file. Do you have coverage somewhere else, or is this something that hasn\'t been on your radar? [...] I\'d love to do a quick needs analysis — it takes about 10 minutes and I can tell you exactly what you\'d need to protect your family\'s financial future."',
        ]),
        ("The Multi-Policy Presentation", [
            '"Many of my clients find it convenient to consolidate all their insurance with one agent they trust. When you have multiple policies with me, you get: one call for all your needs, better discounts (bundling saves most families $200-$600/year), a coordinated approach so there are no gaps between policies, and an annual review that looks at your complete picture. Would you like to see what your full insurance picture would look like with our agency?"',
        ]),
    ])

print("✓ 03_POLICY_SERVICES complete")
print("\nPART 1 DONE")
