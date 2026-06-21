"""Real Estate Agent OS — Part 1: folders 00–03"""
import os
from docx import Document
from docx.shared import Pt, RGBColor

BASE = "/home/user/oqul-phase55-production/real-estate-agent-os/Ultimate_Real_Estate_Agent_Operating_System/"

FOLDERS = [
    "00_START_HERE","01_LEAD_GENERATION","02_BUYER_SERVICES",
    "03_SELLER_SERVICES","04_NEGOTIATION","05_TRANSACTION_MANAGEMENT",
    "06_CLIENT_COMMUNICATION","07_COMPLIANCE_LEGAL","08_POST_CLOSING_RETENTION",
    "09_BUSINESS_OPERATIONS","10_NOTION_WORKSPACE","11_BONUSES",
    "12_CANVA_IMPORTABLE_TEMPLATES"
]
for f in FOLDERS:
    os.makedirs(BASE + f, exist_ok=True)

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

# ── 00_START_HERE ──────────────────────────────────────────────────────────────
with open(BASE + "00_START_HERE/README_FIRST.txt", "w") as f:
    f.write("""ULTIMATE REAL ESTATE AGENT OPERATING SYSTEM

Start with START_HERE_Implementation_Guide.pdf.

EDITABLE FORMATS
- DOCX: edit in Microsoft Word or upload to Google Docs.
- XLSX/CSV: edit in Excel or upload to Google Sheets.
- PPTX: upload to Canva to convert into editable Canva designs.
- Notion assets: import CSV databases and copy the workspace structure.

IMPORTANT
Contracts, agreements, and legal templates are generic educational resources only.
They are not legal advice. Real estate contracts vary significantly by state and jurisdiction.
Always use your brokerage-approved forms and consult a licensed attorney before use.
""")
print("  ✓ 00_START_HERE/README_FIRST.txt")

# ── 01_LEAD_GENERATION ────────────────────────────────────────────────────────
doc("01_LEAD_GENERATION/Cold_Outreach_Templates.docx",
    "Cold Outreach Templates",
    "Real Estate Agent Operating System | Lead Generation",
    [
        ("EXPIRED LISTING OUTREACH", [
            ("•", "Mailer: 'Hi [Name], I noticed your home at [Address] came off the market recently. I specialize in relisting homes that didn't sell the first time — usually with a different strategy and a fresh buyer pool. Could we meet for 15 minutes to talk about what happened and what's possible? — [Your Name], [Brokerage]'"),
            ("•", "Phone script: 'Hi [Name], this is [Your Name] with [Brokerage]. I saw that [Address] came off the market. I know that's frustrating. I've helped several expired sellers in [Neighborhood] successfully sell — could I share what I would do differently?'"),
            ("•", "Email: Subject: '[Address] — I Have a Plan to Get It Sold.' Hi [Name], your home at [Address] recently expired. Before you give up or re-list with the same approach, I'd love to share a different strategy. I've sold [X] homes in [Area] in the last [12 months], including [X] that previously expired. Worth a conversation?"),
        ]),
        ("FOR SALE BY OWNER (FSBO) OUTREACH", [
            ("•", "Day 1 — Offer help: 'Hi [Name], I saw your home at [Address] for sale. I'm not calling to ask for the listing — I just wanted to offer a free CMA (Comparative Market Analysis) so you know if you're priced right. No strings attached. Would that be helpful?'"),
            ("•", "Day 7 — Value add: 'Hi [Name], following up. I put together a quick market report for homes like yours in [Area]. Happy to email it to you — it might help you price or negotiate. Would you like it?'"),
            ("•", "Day 14 — Plant seed: 'Hi [Name], how's the FSBO going? The biggest challenge I hear from sellers is managing showings and negotiating directly. If you ever want backup, I offer a reduced commission for FSBOs who've already been working on it. Just an option.'"),
            ("•", "Day 30 — Convert: 'Hi [Name], it's been about a month. If your home hasn't sold yet, I'd love to sit down and show you what I'd do. I typically sell homes [X days] faster than average in this zip code. 20-minute meeting?'"),
        ]),
        ("SPHERE OF INFLUENCE (SOI) OUTREACH", [
            ("•", "Annual check-in: 'Hi [Name], it's [Your Name] — [personal connection]. I know it's been a while! I'm always here if you or anyone you know is thinking about buying or selling. No pressure — just wanted to reconnect.'"),
            ("•", "Market update: 'Hi [Name], just sending a quick note — the market in [Area] is [trending up/very active/shifting]. If you've been wondering what your home is worth or whether now is a good time to buy/sell, I'd love to share what I'm seeing. Happy to grab coffee!'"),
            ("•", "Referral ask: 'Hi [Name], I'm growing my real estate business and referrals from people I trust mean everything. If you hear of anyone thinking about buying or selling, I'd be honored if you'd mention my name. I promise to take great care of them.'"),
        ]),
        ("OPEN HOUSE FOLLOW-UP", [
            ("•", "Same day text: 'Hi [Name], it was great meeting you at [Address] today! If you have any questions or want to see other properties, I'm happy to help. — [Your Name]'"),
            ("•", "Day 2 email: 'Hi [Name], thanks for stopping by [Address] on [Day]. Here are [X] similar homes in the area that just came on the market — [link or attachment]. Let me know if any catch your eye!'"),
            ("•", "Day 7: 'Hi [Name], checking back in. The market is moving quickly right now. Are you still actively looking, or has your timeline changed? Happy to set up a search for you.'"),
        ]),
    ])

doc("01_LEAD_GENERATION/Sphere_Of_Influence_System.docx",
    "Sphere of Influence System",
    "Real Estate Agent Operating System | Lead Generation",
    [
        ("WHY YOUR SOI IS YOUR BEST SOURCE OF BUSINESS", [
            "Studies consistently show that 60–80% of real estate business comes from people an agent already knows — or from referrals from those people. Your sphere of influence is not a fallback; it's your foundation. The agents who nurture it systematically always outperform those who don't.",
        ]),
        ("BUILDING YOUR SOI DATABASE", [
            "Start by listing every person you know in these categories:",
            ("•", "Family members"),
            ("•", "Close friends"),
            ("•", "Past clients (your most valuable group)"),
            ("•", "Neighbors (current and past)"),
            ("•", "Former colleagues and classmates"),
            ("•", "Service providers you use (dentist, accountant, contractor, etc.)"),
            ("•", "Gym, church, club, community members"),
            ("•", "Social media connections you have real relationships with"),
            "Target: 200–500 names in your database. Add everyone — you never know who knows someone.",
        ]),
        ("THE 33-TOUCH ANNUAL PLAN", [
            "Agents with systematic SOI contact programs average [3–4x] more referrals. Aim for 33 meaningful touches per person per year.",
            ("•", "12 touches: Monthly market update email or text"),
            ("•", "4 touches: Seasonal card or gift (holidays, spring, back-to-school, Thanksgiving)"),
            ("•", "4 touches: Birthday, home anniversary, life events (new baby, graduation)"),
            ("•", "6 touches: Personal calls — no agenda, just connection"),
            ("•", "3 touches: Community events or open house invitations"),
            ("•", "4 touches: Valuable content (market report, home tips, local news)"),
        ]),
        ("CLIENT EVENTS", [
            ("•", "Annual client appreciation event: Pizza party, bowling night, pumpkin patch — low cost, high relationship value"),
            ("•", "Pop-by gifts: Seasonal items dropped at past clients' doors — pie at Thanksgiving, seeds in spring, hand sanitizer kits"),
            ("•", "Community giveaway: Back-to-school supply drive, food drive, charity event tied to your brand"),
        ]),
        ("SOI TRACKING IN YOUR CRM", [
            ("•", "Tag everyone as: SOI | Past Client | Referral Source | Potential Buyer | Potential Seller"),
            ("•", "Log every contact with date and method"),
            ("•", "Set annual birthday and home anniversary reminders"),
            ("•", "Review your SOI list monthly — who haven't you touched in 60+ days?"),
        ]),
    ])

doc("01_LEAD_GENERATION/Open_House_Lead_System.docx",
    "Open House Lead System",
    "Real Estate Agent Operating System | Lead Generation",
    [
        ("PRE-OPEN HOUSE PREPARATION", [
            ("•", "Post the open house on Zillow, Realtor.com, Redfin, and MLS 5–7 days in advance"),
            ("•", "Create a Facebook/Instagram event and boost to surrounding zip codes"),
            ("•", "Door-knock or leave flyers at 20+ neighboring homes: 'Your new neighbor could be coming to this open house!'"),
            ("•", "Prepare your sign-in system: iPad with email capture or paper sign-in sheet"),
            ("•", "Prepare a neighborhood CMA / market report to hand out"),
            ("•", "Set up a property brochure — home features, school info, local amenities"),
        ]),
        ("DURING THE OPEN HOUSE", [
            "Greet every visitor at the door within 30 seconds. Avoid sitting or being on your phone.",
            ("•", "Opening: 'Welcome! Have you been to any other open houses today? Are you working with an agent?'"),
            ("•", "If working with agent: 'Great — I'll let you look around freely. Let me know if you have questions about the home.'"),
            ("•", "If not working with agent: 'I'd love to learn a bit about what you're looking for. Do you have a few minutes to chat?'"),
            ("•", "Ask: 'What's your timeline?' / 'What area are you focused on?' / 'Have you been pre-approved?'"),
            ("•", "Before they leave: 'Could I email you a market update for this neighborhood? What's your email?'"),
        ]),
        ("SIGN-IN CAPTURE QUESTIONS", [
            ("•", "Name"),
            ("•", "Email"),
            ("•", "Phone (optional)"),
            ("•", "Are you working with an agent? Yes / No"),
            ("•", "What's your timeline? 0–3 months / 3–6 months / 6+ months / Just looking"),
            ("•", "Are you also considering selling? Yes / No / Maybe"),
        ]),
        ("POST-OPEN HOUSE FOLLOW-UP", [
            ("•", "Same day (text): 'Hi [Name], great meeting you at [Address] today! Here's a link to the listing: [link]. Let me know if you'd like to see it again or explore other options.'"),
            ("•", "Day 2 (email): 'Hi [Name], here are [X] similar homes in the area — [links]. Happy to schedule private showings this week.'"),
            ("•", "Day 7: 'Hi [Name], the market in [Area] is moving fast. Just wanted to check in — are you still actively searching?'"),
            ("•", "Day 30: 'Hi [Name], it's been about a month since we met at [Address]. If you're still looking, I'd love to set up a buyer consultation to make sure you don't miss the right home.'"),
        ]),
    ])

doc("01_LEAD_GENERATION/Digital_Lead_Nurture_Sequence.docx",
    "Digital Lead Nurture Sequence",
    "Real Estate Agent Operating System | Lead Generation",
    [
        ("OVERVIEW", [
            "Digital leads from Zillow, Realtor.com, Facebook, or your website require a fast response and a consistent long-term nurture sequence. 80% of leads transact within 12 months — but often not in the first 30 days. Don't abandon leads who don't respond immediately.",
        ]),
        ("MINUTE 1–5 RESPONSE (Critical)", [
            "Leads contacted within 5 minutes are [21x] more likely to convert than those contacted after 30 minutes.",
            ("•", "Text: 'Hi [Name], this is [Your Name] with [Brokerage]. I saw you were interested in [Property/Area]. Are you available for a quick call?'"),
            ("•", "Email: 'Hi [Name], thanks for your interest in [Property/Area]. I specialize in that neighborhood and can help you move quickly when the right home comes up. Best time to connect: [time options]?'"),
        ]),
        ("WEEK 1 SEQUENCE", [
            ("•", "Day 1 (1 min): Text — initial response"),
            ("•", "Day 1 (10 min): Email — value-add (neighborhood overview, market report)"),
            ("•", "Day 2: Phone call attempt"),
            ("•", "Day 3: Text follow-up"),
            ("•", "Day 5: Email — new listings matching their criteria"),
            ("•", "Day 7: Phone call attempt #2"),
        ]),
        ("MONTH 1 SEQUENCE (After First Contact)", [
            ("•", "Week 2: Email — 'Are these listings still relevant to you?' + 2–3 new matches"),
            ("•", "Week 3: Text — market insight or stat for their target area"),
            ("•", "Week 4: Phone call — 'Just checking in. Has anything changed with your search?'"),
        ]),
        ("LONG-TERM NURTURE (Months 2–12)", [
            ("•", "Monthly: Automated listing alerts (set up in your MLS)"),
            ("•", "Monthly: Market update email"),
            ("•", "Quarterly: Personal check-in text or call"),
            "Do NOT remove a lead from nurture because they haven't responded. Keep sending value. When they're ready, you'll be top of mind.",
        ]),
        ("EMAIL SUBJECT LINES THAT GET OPENED", [
            ("•", "'3 homes in [Neighborhood] under $[X] — just listed'"),
            ("•", "'What's happening in the [Area] market this month'"),
            ("•", "'[Name], is this the one?' [include photo of relevant listing]"),
            ("•", "'Home values in [Zip Code] — what they're selling for'"),
            ("•", "'Quick question about your home search'"),
        ]),
    ])

doc("01_LEAD_GENERATION/Referral_Partner_Scripts.docx",
    "Referral Partner Scripts",
    "Real Estate Agent Operating System | Lead Generation",
    [
        ("KEY REFERRAL PARTNER CATEGORIES", [
            ("•", "Mortgage brokers and loan officers (your #1 partner)"),
            ("•", "Estate attorneys and probate attorneys"),
            ("•", "Divorce attorneys"),
            ("•", "Financial planners and wealth managers"),
            ("•", "CPAs (clients who receive inheritances, sell businesses, need 1031 exchanges)"),
            ("•", "Employers and HR departments (relocation referrals)"),
            ("•", "Insurance agents"),
            ("•", "Home inspectors, stagers, and contractors"),
        ]),
        ("INITIAL OUTREACH TO MORTGAGE LENDERS", [
            "'Hi [Name], I'm [Your Name] with [Brokerage]. I specialize in [Area] and close [X] transactions a year. I'm always looking for a lender I can confidently refer my buyers to — someone who communicates clearly and closes on time. Could we grab coffee and see if there's a good fit?'",
        ]),
        ("ATTORNEY REFERRAL PARTNER PITCH", [
            "'Hi [Name], I work with many clients in [Area] who are in probate, divorce, or estate situations and need to sell or buy real estate. I understand the sensitivity of those transactions and treat clients with care. I wanted to introduce myself in case any of your clients need real estate representation.'",
        ]),
        ("MAINTAINING PARTNER RELATIONSHIPS", [
            ("•", "Monthly check-in: 1 text, call, or coffee meeting per month"),
            ("•", "Send client referrals both ways — actively look for opportunities to refer back"),
            ("•", "Co-host a first-time buyer seminar: you cover the buying process; lender covers financing"),
            ("•", "Send a thank-you gift for every closed referral"),
            ("•", "Tag partners in social media content and share their content"),
        ]),
        ("CO-MARKETING IDEAS WITH LENDERS", [
            ("•", "Monthly 'Market Update + Mortgage Rate Check' email — sent to both databases"),
            ("•", "Joint first-time buyer seminar or webinar"),
            ("•", "Co-branded open house flyer: 'Questions about buying? Meet [Lender Name] at the open house.'"),
            ("•", "Instagram/Facebook Live — 'Ask a Realtor + Lender' Q&A session"),
        ]),
    ])

doc("01_LEAD_GENERATION/Social_Media_Lead_Strategy.docx",
    "Social Media Lead Strategy",
    "Real Estate Agent Operating System | Lead Generation",
    [
        ("PLATFORM PRIORITIES", [
            ("•", "Facebook: Strongest ROI for real estate leads (paid ads, community groups, Marketplace)"),
            ("•", "Instagram: Brand building and community connection; visual platform for listings"),
            ("•", "YouTube: Highest-value content for buyer/seller education; long-term SEO value"),
            ("•", "LinkedIn: Referral partner outreach and relocation/corporate buyer leads"),
            ("•", "TikTok: Fast-growing; strong for younger buyers and neighborhood content"),
        ]),
        ("CONTENT PILLARS (Post 5x/Week)", [
            ("•", "Market Updates (Mon): 'What sold in [Neighborhood] this week' / 'Prices in [Area] right now'"),
            ("•", "Just Listed / Just Sold (as available): Always tag neighborhood and include price"),
            ("•", "Community (Wed): Local restaurants, events, schools, hidden gems in your farm area"),
            ("•", "Education (Thu): First-time buyer tips, seller prep guide, inspection what-to-expect"),
            ("•", "Personal Brand (Fri): Behind-the-scenes, client wins, your story, your values"),
        ]),
        ("FACEBOOK ADS FOR BUYER LEADS", [
            ("•", "Audience: [Target zip codes], age 25–55, homeownership interest"),
            ("•", "Hook: 'Homes in [Area] under $[X] — see what's available'"),
            ("•", "Lead magnet: Free buyers guide, free CMA, free neighborhood report"),
            ("•", "Budget: Start at $5–10/day; optimize toward cost-per-lead under $20"),
        ]),
        ("INSTAGRAM REELS THAT PERFORM", [
            ("•", "'I sold this home in 5 days — here's why' — listing story + behind scenes"),
            ("•", "'3 things I wish buyers knew before making an offer' — educational"),
            ("•", "'What $[X] buys you in [City] right now' — visual listing tour"),
            ("•", "'I asked 50 buyers what they regret — here's what they said' — engagement"),
            ("•", "'Day in the life of a real estate agent in [City]' — personal brand"),
        ]),
        ("TURNING FOLLOWERS INTO LEADS", [
            ("•", "Reply to every comment within 2 hours — conversations lead to DMs"),
            ("•", "Use stories polls: 'Buying or selling this year? Yes / Not yet / Just curious'"),
            ("•", "Pin a lead magnet to your profile: 'DM me HOME for the free buyers guide'"),
            ("•", "Add a 'book a call' link in bio — Calendly or similar"),
            ("•", "Story CTA weekly: 'DM me if you're thinking about buying/selling in [Area]'"),
        ]),
    ])

print("✓ 01_LEAD_GENERATION complete")

# ── 02_BUYER_SERVICES ─────────────────────────────────────────────────────────
doc("02_BUYER_SERVICES/Buyer_Consultation_Script.docx",
    "Buyer Consultation Script",
    "Real Estate Agent Operating System | Buyer Services",
    [
        ("PURPOSE OF THE BUYER CONSULTATION", [
            "The buyer consultation is your most important meeting with a buyer client. It sets expectations, establishes your value, builds trust, and positions you to secure a signed buyer representation agreement. Never skip it — even for buyers who 'just want to see a house.'",
        ]),
        ("OPENING (0–3 min)", [
            "'[Name], thanks for coming in. My goal today is to understand exactly what you're looking for, walk you through how the buying process works, and make sure you're fully prepared so when the right home comes up — and they do go fast — you're ready to move. Sound good?'",
        ]),
        ("UNDERSTANDING THEIR SITUATION (3–12 min)", [
            ("•", "What's motivating the move? Growing family, job change, first home, upsizing?"),
            ("•", "What area(s) are you focused on, and what's important about that location?"),
            ("•", "What does your ideal home look like — size, layout, must-haves vs. nice-to-haves?"),
            ("•", "Have you been pre-approved for a mortgage? With whom?"),
            ("•", "What's your price range?"),
            ("•", "What's your timeline — are you renting, or do you have a home to sell first?"),
            ("•", "Have you been looking already? Any homes you've seen that you liked?"),
        ]),
        ("EDUCATING ON THE PROCESS (12–22 min)", [
            "Walk through each stage:",
            ("•", "Pre-approval: Why it's required before we write any offer"),
            ("•", "Home search: How I'll set up a customized MLS search for you"),
            ("•", "Making an offer: What a competitive offer looks like in today's market"),
            ("•", "Inspection and due diligence: What to expect and how to handle issues"),
            ("•", "Financing and appraisal: What happens after an accepted offer"),
            ("•", "Closing: What you need to bring and what to expect"),
        ]),
        ("YOUR VALUE PROPOSITION (22–27 min)", [
            "'Here's what working with me looks like: I will set up a custom search and alert you the moment a home matching your criteria hits the market. In this market, that matters because good homes are going fast. I'll prepare every offer strategically so it competes. I'll negotiate on your behalf from inspection through closing. And I get paid by the seller — there's no cost to you as a buyer.'",
        ]),
        ("BUYER AGREEMENT AND CLOSE (27–30 min)", [
            "'Before we start viewing homes, I ask all my buyers to sign a buyer representation agreement. This formalizes our working relationship and means I'm legally obligated to represent your best interests. Do you have any questions about that?'",
            "If hesitation: 'What concerns do you have? I'm happy to walk through it.'",
        ]),
    ])

doc("02_BUYER_SERVICES/Home_Showing_Checklist.docx",
    "Home Showing Checklist",
    "Real Estate Agent Operating System | Buyer Services",
    [
        ("BEFORE THE SHOWING", [
            ("•", "[ ] Confirm showing appointment with listing agent 24 hours in advance"),
            ("•", "[ ] Review the listing in detail — price history, days on market, seller disclosures"),
            ("•", "[ ] Pull comparable sales in the neighborhood"),
            ("•", "[ ] Prepare buyer with what to look for — condition, layout, red flags"),
            ("•", "[ ] Confirm buyer has pre-approval letter (before writing any offer)"),
        ]),
        ("DURING THE SHOWING — WHAT TO LOOK FOR", [
            ("•", "Curb appeal and exterior condition: roof, gutters, siding, foundation"),
            ("•", "Lot: drainage, grading, neighbor proximity, noise"),
            ("•", "Mechanicals: age of HVAC, water heater, electrical panel"),
            ("•", "Basement/crawl space: moisture, cracks, musty smell"),
            ("•", "Attic: insulation, roof decking condition, ventilation"),
            ("•", "Kitchen and bathrooms: counter condition, cabinet quality, plumbing fixtures"),
            ("•", "Windows and doors: drafts, condition, double-pane"),
            ("•", "Signs of water damage: stains, soft spots, mold smell"),
        ]),
        ("BUYER DEBRIEF QUESTIONS", [
            ("•", "'On a scale of 1–10, how did you feel about that home?'"),
            ("•", "'What did you like most? What would you change?'"),
            ("•", "'How did it compare to [previous home]?'"),
            ("•", "'Is this a home you could see yourself living in?'"),
            ("•", "'Any concerns or questions about the condition?'"),
        ]),
        ("NOTES TEMPLATE (Per Showing)", [
            "Property: ___________________________",
            "Date Shown: _________________________",
            "Buyer Rating (1–10): _________________",
            "Pros: _______________________________",
            "Cons: _______________________________",
            "Condition Concerns: __________________",
            "Buyer Interest Level: [ ] Yes  [ ] Maybe  [ ] No",
            "Next Step: __________________________",
        ]),
    ])

doc("02_BUYER_SERVICES/Offer_Writing_SOP.docx",
    "Offer Writing SOP",
    "Real Estate Agent Operating System | Buyer Services",
    [
        ("PRE-OFFER RESEARCH", [
            ("•", "Pull all comparable sold properties within [0.5 mile / similar size] in the last 90 days"),
            ("•", "Review price reductions and days on market for the subject property"),
            ("•", "Research the seller's situation (if possible): how long have they owned, motivation signals"),
            ("•", "Confirm buyer's pre-approval covers the offer price"),
            ("•", "Discuss offer strategy with buyer: price, terms, contingencies, timeline"),
        ]),
        ("OFFER COMPONENTS", [
            ("•", "Purchase price: Justified by comps; competitive in current market"),
            ("•", "Earnest money deposit: Typically 1–3% of purchase price; more = stronger offer"),
            ("•", "Contingencies: Financing, inspection, appraisal — discuss which to include/waive"),
            ("•", "Closing date: Align with seller preference when known"),
            ("•", "Inclusions/exclusions: Appliances, fixtures, personal property"),
            ("•", "Seller concessions: Closing cost credit, price reduction in lieu of repairs"),
        ]),
        ("MAKING THE OFFER COMPETITIVE", [
            ("•", "Escalation clause: Automatically beat competing offers up to a max price"),
            ("•", "Personal letter: From buyer to seller — humanizes the offer (check fair housing guidelines)"),
            ("•", "Shorter inspection period: 7 days vs. standard 10–14"),
            ("•", "Pre-approval from strong lender: local credit unions and direct lenders often win"),
            ("•", "Flexible closing date: Match the seller's preferred timeline"),
            ("•", "Larger earnest money: Shows commitment"),
        ]),
        ("PRESENTING THE OFFER", [
            "Call listing agent before sending: 'Hi [Name], my clients are very interested in [Address]. I wanted to give you a heads-up before we send an offer. Is there anything about the seller's situation or timeline that would help us write the strongest offer?'",
            ("•", "Send offer via email with a brief cover note explaining buyer's situation and enthusiasm"),
            ("•", "Follow up with a call or text within 1 hour of sending"),
            ("•", "Set a short response deadline (24 hours) to create urgency"),
        ]),
        ("AFTER THE OFFER", [
            ("•", "Accepted: Immediately email buyer — walk through next steps (deposit, inspection, timeline)"),
            ("•", "Counter-offer: Review with buyer and respond within hours — don't let it go cold"),
            ("•", "Rejected: Ask for feedback — 'What would have made us more competitive?'"),
        ]),
    ])

doc("02_BUYER_SERVICES/First_Time_Buyer_Guide.docx",
    "First-Time Buyer Guide",
    "Real Estate Agent Operating System | Buyer Services",
    [
        ("STEP 1 — GET YOUR FINANCES READY", [
            ("•", "Check your credit score: 620 minimum for most loans; 740+ for best rates"),
            ("•", "Calculate your budget: Down payment (3.5–20%) + closing costs (2–5% of purchase price)"),
            ("•", "Get pre-approved — not just pre-qualified. A pre-approval is a full review of your finances and carries more weight with sellers."),
            ("•", "Avoid new debt, job changes, or large purchases during the home buying process"),
        ]),
        ("STEP 2 — UNDERSTAND YOUR LOAN OPTIONS", [
            ("•", "Conventional loan: 3–20% down; best for strong credit and stable income"),
            ("•", "FHA loan: 3.5% down; more flexible credit requirements; requires mortgage insurance"),
            ("•", "VA loan: 0% down for eligible veterans and military; no PMI"),
            ("•", "USDA loan: 0% down for eligible rural properties"),
            ("•", "First-time buyer programs: many states offer down payment assistance and grants"),
        ]),
        ("STEP 3 — DEFINE YOUR WANTS AND NEEDS", [
            ("•", "Must-haves: Bedrooms, bathrooms, location, schools, commute"),
            ("•", "Nice-to-haves: Garage, yard, updated kitchen, home office"),
            ("•", "Deal-breakers: HOA restrictions, flood zone, busy street"),
            ("•", "5-year vision: Where will you need to be in 5 years — size, location, life changes?"),
        ]),
        ("STEP 4 — THE HOME SEARCH", [
            ("•", "Your agent will set up an MLS search that alerts you the moment a matching home is listed"),
            ("•", "In active markets, be ready to see new listings within 24 hours"),
            ("•", "Track homes you've seen: rate them 1–10 and note pros/cons"),
            ("•", "Remember: no home is perfect. Focus on non-changeable factors: location, lot, layout"),
        ]),
        ("STEP 5 — MAKING AN OFFER", [
            ("•", "Your agent will prepare a competitive offer based on comparable sales"),
            ("•", "Include contingencies: financing, inspection, and appraisal protect you"),
            ("•", "Earnest money deposit (typically 1–3%) shows you're serious"),
            ("•", "Response time: most sellers respond within 24–48 hours"),
        ]),
        ("STEP 6 — INSPECTION AND DUE DILIGENCE", [
            ("•", "Schedule a licensed home inspector immediately after offer acceptance"),
            ("•", "Attend the inspection — it's a learning experience about your future home"),
            ("•", "Negotiate repairs or credits based on findings"),
            ("•", "Additional inspections to consider: sewer scope, radon, mold, structural"),
        ]),
        ("STEP 7 — CLOSING", [
            ("•", "Final walkthrough 24 hours before closing — confirm condition matches expectations"),
            ("•", "Wire closing funds only to verified accounts — confirm via phone call"),
            ("•", "Bring: government ID, cashier's check or wire confirmation, any required documents"),
            ("•", "Closing day: sign documents, receive keys, and celebrate!"),
        ]),
    ])

print("✓ 02_BUYER_SERVICES complete")

# ── 03_SELLER_SERVICES ────────────────────────────────────────────────────────
doc("03_SELLER_SERVICES/Listing_Presentation_Script.docx",
    "Listing Presentation Script",
    "Real Estate Agent Operating System | Seller Services",
    [
        ("PRE-LISTING PREPARATION", [
            ("•", "Research the property on tax records, prior sales, current Zestimate vs. market reality"),
            ("•", "Run a full Comparative Market Analysis (CMA)"),
            ("•", "Research competing listings: price, days on market, condition"),
            ("•", "Prepare your marketing plan specific to this home"),
            ("•", "Know the seller's story: Why are they moving? Timeline? What have they done to the home?"),
        ]),
        ("OPENING (0–5 min)", [
            "'[Name], thank you for having me. Before I talk about myself or pricing, I'd love to learn about your situation. Every seller's goals are different — some need to close fast, some want maximum price, some need certainty. What's most important to you in this process?'",
        ]),
        ("LEARNING THEIR SITUATION (5–15 min)", [
            ("•", "What's prompting the move, and what's your ideal timeline?"),
            ("•", "Have you made any improvements to the home since you purchased?"),
            ("•", "Are you buying another home? Is the sale contingent on that?"),
            ("•", "Have you had the home appraised or received any previous offers?"),
            ("•", "What has your experience been like with other agents? (if applicable)"),
        ]),
        ("PRESENTING YOUR MARKETING PLAN (15–25 min)", [
            "Cover each element of your plan:",
            ("•", "Professional photography (and video / Matterport / drone if applicable)"),
            ("•", "MLS listing with full remarks and all media"),
            ("•", "Zillow, Realtor.com, Redfin, Trulia syndication"),
            ("•", "Social media campaign: targeted Facebook/Instagram ads"),
            ("•", "Email campaign to your buyer database"),
            ("•", "Open house strategy"),
            ("•", "Agent outreach: top buyer's agents in the area"),
            ("•", "Yard signage, lockbox, and showing management"),
        ]),
        ("PRICING CONVERSATION (25–35 min)", [
            "'Based on my analysis, I recommend a list price of $[X]. Let me show you how I arrived there...' [Walk through CMA]",
            "If they want to price higher: 'I understand you want to leave room to negotiate. The data shows that overpriced homes in this market sit longer, receive lower offers, and ultimately sell for less than homes priced correctly from day one. Can I show you that data?'",
            "Pricing anchor: 'Homes in this range are seeing [X] offers / selling in [X] days. If we price at $[X], here's what I expect to happen...'",
        ]),
        ("ASKING FOR THE LISTING (35–40 min)", [
            "'Based on everything we've discussed, I'm confident I can get you top dollar within your timeline with my marketing approach. I'd love the opportunity to represent you. Are you ready to move forward?'",
        ]),
    ])

doc("03_SELLER_SERVICES/Pricing_Strategy_Guide.docx",
    "Pricing Strategy Guide",
    "Real Estate Agent Operating System | Seller Services",
    [
        ("THE IMPORTANCE OF ACCURATE PRICING", [
            "Pricing is the single most important factor in how quickly a home sells and what price it achieves. Homes priced correctly sell faster and for more money. Overpriced homes sit, get stigmatized, and ultimately sell below their potential.",
        ]),
        ("BUILDING A COMPARATIVE MARKET ANALYSIS", [
            "Step 1: Select comparables (comps) sold in the last 90 days within [0.5 mile] with similar:",
            ("•", "Square footage (within 15%)"),
            ("•", "Bedrooms and bathrooms"),
            ("•", "Lot size (for single-family homes)"),
            ("•", "Condition and updates"),
            "Step 2: Calculate price per square foot for each comp",
            "Step 3: Adjust for differences: newer roof (+), dated kitchen (-), extra garage bay (+)",
            "Step 4: Establish a value range; recommend pricing at or just below market for maximum interest",
        ]),
        ("PRICING STRATEGIES BY MARKET CONDITIONS", [
            ("•", "Seller's market (low inventory): Price at or slightly below market to trigger multiple offers; allows you to drive the price up"),
            ("•", "Balanced market: Price accurately at market value; one week on market is normal"),
            ("•", "Buyer's market (high inventory): Price at the lower end of your range; competition from similar homes is real"),
        ]),
        ("COMMON PRICING MISTAKES", [
            ("•", "Pricing for 'room to negotiate': Buyers skip overpriced homes — they never start negotiating"),
            ("•", "Pricing based on what seller 'needs': The market doesn't care what the seller owes"),
            ("•", "Pricing based on Zestimate: Automated tools have [5–15]% error rates in many markets"),
            ("•", "Ignoring recent price reductions on active listings: They signal what buyers won't pay"),
        ]),
        ("THE PRICE REDUCTION CONVERSATION", [
            "After [7–14] days on market with no offers:",
            "'[Name], we've had [X] showings but no offers. The feedback I'm hearing is [price / condition / specific items]. The market is telling us something. I recommend we consider a price adjustment to $[X]. Homes at that price in this area are selling in [X] days. I want to get you sold.'",
        ]),
    ])

doc("03_SELLER_SERVICES/Listing_Marketing_Checklist.docx",
    "Listing Marketing Checklist",
    "Real Estate Agent Operating System | Seller Services",
    [
        ("BEFORE GOING LIVE", [
            ("•", "[ ] Professional photographer scheduled (and video if budget allows)"),
            ("•", "[ ] 3D Matterport / virtual tour scheduled (for homes over $[X])"),
            ("•", "[ ] Drone photos arranged if lot or location warrants"),
            ("•", "[ ] Staging consultation completed (or home prepared using your staging checklist)"),
            ("•", "[ ] All photos reviewed and edited before upload"),
            ("•", "[ ] MLS listing input — all fields complete, no errors"),
            ("•", "[ ] Full listing remarks written (compelling, SEO-rich, accurate)"),
            ("•", "[ ] Disclosures prepared and ready to provide to buyers"),
        ]),
        ("WEEK 1 MARKETING LAUNCH", [
            ("•", "[ ] Listed on MLS with Coming Soon status 3–5 days before active (if allowed)"),
            ("•", "[ ] Zillow, Realtor.com, Redfin — confirm syndication correct"),
            ("•", "[ ] Facebook and Instagram posts with professional photos"),
            ("•", "[ ] Facebook/Instagram ad campaign launched"),
            ("•", "[ ] Email blast to buyer database"),
            ("•", "[ ] Email to top 20 buyer's agents in the area"),
            ("•", "[ ] Yard sign installed"),
            ("•", "[ ] Lockbox installed; showing service activated"),
            ("•", "[ ] Open house scheduled for first weekend"),
        ]),
        ("ONGOING MARKETING", [
            ("•", "[ ] Weekly showing feedback collected and reported to seller"),
            ("•", "[ ] Social media refreshed with new angles / price updates as needed"),
            ("•", "[ ] Open houses held as needed while active"),
            ("•", "[ ] Any price adjustments reflected immediately across all platforms"),
        ]),
        ("HOME PREPARATION CHECKLIST (for sellers)", [
            ("•", "Declutter all rooms and closets — remove personal photos if possible"),
            ("•", "Deep clean entire home including windows, baseboards, appliances"),
            ("•", "Touch up paint in high-traffic areas"),
            ("•", "Enhance curb appeal: freshly mowed lawn, trimmed shrubs, clean front door"),
            ("•", "Repair any obvious defects: dripping faucets, broken fixtures, scuffed walls"),
            ("•", "Remove excess furniture — buyers need to visualize their furniture"),
        ]),
    ])

doc("03_SELLER_SERVICES/Seller_Communication_SOP.docx",
    "Seller Communication SOP",
    "Real Estate Agent Operating System | Seller Services",
    [
        ("WEEKLY COMMUNICATION STANDARD", [
            "Every active listing receives a weekly update, every week, even if there is nothing new to report. Silence creates anxiety. Regular communication creates trust.",
        ]),
        ("WEEKLY UPDATE EMAIL TEMPLATE", [
            "Subject: Weekly Update — [Address] | Week [X] on Market",
            "Hi [Name], here's your weekly update for [Address].",
            ("•", "Showings this week: [X]"),
            ("•", "Total showings to date: [X]"),
            ("•", "Feedback received: [Summary of buyer comments]"),
            ("•", "Online views on Zillow/Realtor.com: [X]"),
            ("•", "Competing homes: [X] homes listed / [X] homes sold in your price range this week"),
            "My assessment: [2–3 sentences on market activity, feedback themes, any recommended actions]",
            "Next steps: [Upcoming open house, price discussion, showing adjustment, etc.]",
        ]),
        ("AFTER EVERY SHOWING", [
            ("•", "Text buyer's agent within 1 hour: 'Hi [Name], any feedback on [Address]?'"),
            ("•", "If no response in 48 hours: Follow up once more"),
            ("•", "Log all feedback — patterns matter. Three agents saying the same thing is signal, not noise."),
        ]),
        ("AFTER EVERY OPEN HOUSE", [
            ("•", "Email seller same day: number of visitors, any offers expected, notable feedback"),
            ("•", "Include: What visitors said, their apparent interest level, any concerns raised"),
        ]),
        ("OFFER RECEIVED COMMUNICATION", [
            "Call immediately — do not text or email first for an offer. 'Hi [Name], we have an offer I'd like to walk you through. Are you available now or in the next [hour]?'",
            "Present the full offer: price, earnest money, contingencies, closing date, and your recommendation.",
        ]),
    ])

doc("03_SELLER_SERVICES/Price_Reduction_Scripts.docx",
    "Price Reduction Scripts",
    "Real Estate Agent Operating System | Seller Services",
    [
        ("WHEN TO HAVE THE CONVERSATION", [
            ("•", "After 10–14 days on market with no offers"),
            ("•", "After 5+ showings with consistent 'too expensive' feedback"),
            ("•", "When a competing home nearby sells at a lower price"),
            ("•", "When your online metrics (views, saves) are declining"),
        ]),
        ("SCRIPT 1 — DATA-DRIVEN APPROACH", [
            "'[Name], I want to review the numbers with you. In the last [14] days, we've had [X] showings. The consistent feedback is [price/condition/both]. At the same time, [X] similar homes have sold in the area at $[range]. Our current price is [X]% above where buyers are transacting. I believe a price adjustment to $[X] would bring us into the active buyer range. What are your thoughts?'",
        ]),
        ("SCRIPT 2 — MARKET REPOSITIONING", [
            "'[Name], every week we're on the market at this price, buyers are looking at us versus newer listings coming on at lower prices. We're helping sell those homes instead of ours. I want to make a proactive adjustment before we become a stale listing. Homes that are fresh on the market get the most attention — we still have momentum, but the window is closing.'",
        ]),
        ("SCRIPT 3 — URGENCY (Approaching Major Events)", [
            "'[Name], with [school year / holiday season / end of quarter] approaching, buyer activity in this price range will [slow significantly / shift to different areas]. If we want to close before [date], we need to create movement in the next [X] days. A price adjustment now gives us the best shot at catching the current buyer pool.'",
        ]),
        ("HANDLING SELLER PUSHBACK", [
            ("•", "Seller: 'I'm not willing to go that low.' — 'I understand. My goal is to get you as much as possible. What I want to avoid is a situation where we go below this number six months from now because the home has been sitting. Would you consider meeting in the middle at $[X]?'"),
            ("•", "Seller: 'Let's just wait a few more weeks.' — 'We can absolutely do that. I want to make sure you're aware that statistically, the longer a home sits, the more buyers wonder what's wrong with it. I'd rather move with the market than against it.'"),
        ]),
    ])

print("✓ 03_SELLER_SERVICES complete")
print("PART 1 DONE")
