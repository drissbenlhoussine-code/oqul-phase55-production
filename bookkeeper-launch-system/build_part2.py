import os, csv, json, zipfile
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/bookkeeper-launch-system/Ultimate_Bookkeeper_Launch_System/"

# DOCX helper
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
        if isinstance(section, str): d.add_paragraph(section); continue
        heading, items = section
        h = d.add_heading(heading, level=1)
        h.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
        for item in items:
            if isinstance(item, tuple) and item[0] == '•':
                d.add_paragraph(item[1], style='List Bullet')
            else: d.add_paragraph(str(item))
    d.save(BASE + filename); print(f"  ✓ {filename}")

# XLSX helpers
NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"; ORG="F39C12"; RED="E74C3C"
def hf(h): return PatternFill("solid", fgColor=h)
def bf(bold=True,sz=11,color="000000"): return Font(bold=bold,size=sz,color=color)
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

print("=== BUILD PART 2: 04_CLIENT_ACQUISITION, 05_CLIENT_ONBOARDING, 06_SERVICE_DELIVERY, 07_CLIENT_COMMUNICATION + XLSX ===\n")

# ── 04_CLIENT_ACQUISITION ─────────────────────────────────────────────────────

doc("04_CLIENT_ACQUISITION/Cold_Outreach_Email_Templates.docx",
    "Cold Outreach Email Templates for Bookkeepers",
    "5 proven email templates to land your first bookkeeping clients",
    [
        ("HOW TO USE THESE TEMPLATES", [
            "Personalize every email before sending. Replace [NAME], [COMPANY], and [SPECIFIC DETAIL] with real information from your research.",
            "Send from a professional email address (yourname@yourdomain.com) — never Gmail or Yahoo.",
            "Follow up 3 times if no response: Day 1, Day 4, Day 10. Most replies come on follow-ups.",
            "Track opens and clicks using a tool like Mailtrack (free) or Lemlist (paid).",
            "Aim for a 30-40% open rate and 5-10% reply rate on cold outreach.",
        ]),
        ("EMAIL 1 — THE PAIN POINT EMAIL (Best for small business owners)", [
            "SUBJECT LINE OPTIONS:",
            ('•', '"Quick question about your books, [First Name]"'),
            ('•', '"Are you still doing your own bookkeeping, [First Name]?"'),
            ('•', '"[Company Name] + bookkeeping question"'),
            "",
            "EMAIL BODY:",
            "Hi [First Name],",
            "",
            "I came across [Company Name] on [LinkedIn/Instagram/Google] and noticed you're running a [type of business] — congratulations on what you've built!",
            "",
            "I work with [industry] business owners like yourself who are ready to stop spending evenings reconciling bank statements and start making confident decisions from clean, accurate financials.",
            "",
            "Most of my clients came to me when they realized: (1) they were spending 5-10 hours/month doing something they hated, (2) they weren't sure their numbers were right, or (3) tax season was a nightmare.",
            "",
            "Does any of that resonate with your current situation?",
            "",
            "If so, I'd love to offer a free 20-minute call to show you how I work and what that would look like for [Company Name].",
            "",
            "Would [Day] or [Day] this week work for a quick call?",
            "",
            "Best,",
            "[Your Name]",
            "[Your Business Name] | Bookkeeping & Financial Clarity",
            "[Phone] | [Website]",
        ]),
        ("EMAIL 2 — THE REFERRAL INTRO EMAIL (Best for warm leads)", [
            "SUBJECT LINE: '[Referrer Name] suggested I reach out'",
            "",
            "Hi [First Name],",
            "",
            "[Referrer Name] mentioned you might be looking for help getting your books organized — they thought we'd be a great fit.",
            "",
            "I help [industry] businesses like yours maintain clean, accurate books so you always know exactly where you stand financially. My clients typically save 8-15 hours per month and avoid the tax-season scramble.",
            "",
            "Here's what [Referrer Name] said about working with me: [Insert brief testimonial or paraphrase].",
            "",
            "I'd love to learn more about your business and share how I might help. Would you be open to a quick 20-minute call this week?",
            "",
            "Looking forward to connecting,",
            "[Your Name]",
        ]),
        ("EMAIL 3 — THE VALUE-FIRST EMAIL (Best for LinkedIn outreach)", [
            "SUBJECT LINE: 'One thing that could save [Company Name] $X in taxes'",
            "",
            "Hi [First Name],",
            "",
            "I was looking at businesses in [city/industry] and noticed [Company Name] — impressive growth!",
            "",
            "I want to share one quick insight that saves most [industry] business owners money: Many businesses in your sector are missing [specific deduction or bookkeeping practice relevant to industry]. On average, this costs them $2,000-5,000 per year in overpaid taxes.",
            "",
            "I'm a bookkeeper who specializes in [industry], and I've helped [X] clients recapture those dollars by keeping their books categorized correctly from day one.",
            "",
            "I'd love to do a free 15-minute financial snapshot review for [Company Name] — no commitment, just real insight.",
            "",
            "Interested? Reply here or grab a time: [Calendly link]",
            "",
            "Best,",
            "[Your Name]",
        ]),
        ("EMAIL 4 — THE FOLLOW-UP EMAIL (Day 4 after Email 1)", [
            "SUBJECT LINE: 'Re: Quick question about your books, [First Name]'",
            "",
            "Hi [First Name],",
            "",
            "Just circling back in case my last email got buried — completely understand how busy things get!",
            "",
            "I wanted to ask directly: Is managing your own books currently taking more time than you'd like?",
            "",
            "If yes, I have a few ideas that could help. If it's not the right time, no worries at all — just let me know and I'll follow up in a few months.",
            "",
            "Either way, I respect your time. What would be most helpful?",
            "",
            "Best,",
            "[Your Name]",
        ]),
        ("EMAIL 5 — THE BREAK-UP EMAIL (Day 10, last follow-up)", [
            "SUBJECT LINE: 'Should I close the loop?'",
            "",
            "Hi [First Name],",
            "",
            "I've reached out a couple of times and haven't heard back — which tells me one of three things:",
            ('•', "You're swamped and this isn't the right time (completely understandable)"),
            ('•', "You already have bookkeeping support in place (great!)"),
            ('•', "My emails aren't hitting the mark for you (fair enough)"),
            "",
            "I'll stop following up after this, but I did want to leave the door open: if bookkeeping ever becomes a pain point for [Company Name], I'm here.",
            "",
            "Wishing you and your business all the best.",
            "",
            "[Your Name]",
            "P.S. — If you know anyone who might benefit from clean books and financial clarity, I'd love an introduction. I offer a referral thank-you gift for every client who signs on.",
        ]),
        ("COLD OUTREACH BEST PRACTICES", [
            ('•', "Research before sending: Know the business, their industry, and at least one specific detail"),
            ('•', "Send 10 personalized emails per week rather than 100 generic blasts"),
            ('•', "Use Calendly or Acuity to make scheduling frictionless — link in every email"),
            ('•', "Track every outreach in your CRM (see Client_Lead_Tracker_CRM.xlsx)"),
            ('•', "Block 30 minutes each weekday for outreach — consistency beats volume"),
            ('•', "A/B test subject lines: send version A to 10 prospects, version B to 10 more, track opens"),
            ('•', "Always reply to their reply within 2 hours during business hours — speed signals professionalism"),
        ]),
    ]
)

doc("04_CLIENT_ACQUISITION/Discovery_Call_Script.docx",
    "Discovery Call Script for Bookkeepers",
    "Full word-for-word script: intro → pain discovery → solution presentation → close → objection handling",
    [
        ("BEFORE THE CALL — PRE-CALL CHECKLIST", [
            ('•', "Research the prospect's business: Google them, check their website, LinkedIn, and social media"),
            ('•', "Look up their industry to understand common pain points"),
            ('•', "Have your pricing packages in front of you"),
            ('•', "Set up your screen share in case you want to show your work"),
            ('•', "Have a quiet space, good lighting (for video), and water"),
            ('•', "Set a timer for 30 minutes — respect their time"),
            ('•', "Mindset: You are a consultant discovering whether you can help, not a salesperson begging for business"),
        ]),
        ("OPENING (Minutes 1-3)", [
            "SCRIPT:",
            '"Hi [Name], great to connect! Thanks for making time today. Before we dive in, I just want to confirm — we have about 30 minutes together, is that still good for you?"',
            "",
            "[Wait for confirmation]",
            "",
            '"Perfect. Here\'s what I\'d like to do: I\'ll spend the first part asking you some questions about your business and your current bookkeeping situation. Then I\'ll share a bit about how I work and what that might look like for you. And at the end, we\'ll decide together whether it makes sense to move forward. Sound good?"',
            "",
            "[Wait for yes]",
            "",
            '"Great. So tell me a little about [Company Name] — how long have you been in business and what does your day-to-day look like?"',
            "",
            "[LISTEN. Take notes. Show genuine interest. This builds rapport.]",
        ]),
        ("PAIN DISCOVERY (Minutes 3-15)", [
            "Ask these questions ONE AT A TIME. Do not rush. The gold is in their answers.",
            "",
            "QUESTION 1 (Current situation):",
            '"How are you currently handling your bookkeeping? Are you doing it yourself, or do you have someone helping?"',
            "",
            "QUESTION 2 (Pain point):",
            '"What\'s the biggest frustration you have with how your books are currently managed?"',
            "",
            "QUESTION 3 (Time cost):",
            '"Roughly how many hours per month do you spend on bookkeeping-related tasks — including bank reconciliation, expense tracking, and getting ready for your accountant?"',
            "",
            "QUESTION 4 (Financial clarity):",
            '"When you want to know how your business is doing financially — like your profit margin or cash position — how easy is it for you to get that answer right now?"',
            "",
            "QUESTION 5 (Tax situation):",
            '"How did last tax season go? Were your books in good shape, or was it more of a scramble to pull everything together?"',
            "",
            "QUESTION 6 (Goals):",
            '"What does success look like for your business over the next 12 months? What do you need from your financials to achieve that?"',
            "",
            "[LISTEN DEEPLY. Reflect back what you hear. Use phrases like: 'That makes total sense' / 'A lot of business owners tell me the same thing' / 'I can see why that would be frustrating']",
        ]),
        ("TRANSITION TO SOLUTION (Minutes 15-22)", [
            "BRIDGE STATEMENT:",
            '"Based on what you\'ve shared, it sounds like the main challenges are [summarize 2-3 pain points they mentioned]. Does that sound right?"',
            "",
            "[Wait for confirmation]",
            "",
            '"Good. Those are exactly the kinds of things I help business owners solve. Let me share a bit about how I work..."',
            "",
            "EXPLAIN YOUR PROCESS (Keep to 3-4 minutes max):",
            '"I work with [type of business] owners to keep their books clean, current, and meaningful — not just compliant. Every month, I handle [list your core services]. You\'ll receive a simple monthly report that tells you exactly how your business is performing — no accounting degree required to understand it."',
            "",
            '"What makes my service different is [your unique value: e.g., industry specialization, responsiveness, the way you present reports, etc.]."',
            "",
            "SOCIAL PROOF:",
            '"For example, one of my clients — a [similar business type] — came to me in [situation]. Within [timeframe], we were able to [result]. They now [positive outcome]."',
        ]),
        ("PRESENTING YOUR PACKAGES (Minutes 22-27)", [
            "TRANSITION:",
            '"Based on what you\'ve described, I have a couple of options I think could work well for [Company Name]. Can I walk you through those?"',
            "",
            "PRESENT 2 OPTIONS (not 3 — reduces decision fatigue in the close):",
            '"Option A is our [Package Name] — this covers [scope] and is $[price]/month. This would be a great fit if [condition]."',
            "",
            '"Option B is our [Package Name] — this includes everything in Option A plus [additional services] for $[price]/month. This makes more sense if [condition]."',
            "",
            '"Based on what you told me about [specific pain point they mentioned], I actually think [Option B] would serve you better — here\'s why: [specific reason tied to their situation]."',
            "",
            "[Pause. Let them respond. Do NOT fill the silence.]",
        ]),
        ("THE CLOSE (Minutes 27-30)", [
            "CLOSING QUESTION:",
            '"Does one of those options feel like the right fit for where you are right now?"',
            "",
            "IF YES:",
            '"Excellent! Here\'s what happens next: I\'ll send you our engagement agreement and onboarding questionnaire today. Once those are signed and returned, I\'ll send you a setup link and we can have you onboarded within [timeframe]. Does that work?"',
            "",
            "IF THEY NEED TIME:",
            '"Completely understand. What information would help you feel confident about moving forward?"',
            "[Address their concern, then:] \"When do you think you\'ll be ready to make a decision? I want to make sure I can hold a spot in my client roster for you.\"",
        ]),
        ("OBJECTION HANDLING SCRIPTS", [
            "OBJECTION: 'It's too expensive / I can't afford it right now'",
            "RESPONSE: \"I hear you. Let me ask — what's your current hourly rate? [Wait for answer] So if you're spending 8 hours a month on bookkeeping, that's actually costing your business $[calculation]. Our service is $[price], which means you come out ahead while getting expertise you likely don't have. Does that reframe the investment at all?\"",
            "",
            "OBJECTION: 'I already have a CPA who does my books'",
            "RESPONSE: \"That's great — CPAs are wonderful for tax strategy. Here's the thing: most CPAs charge $150-300/hour, and they don't want to do monthly reconciliation — it's not the best use of their time or your money. I handle the ongoing bookkeeping so your CPA only touches your books at tax time, when it's actually worth their rate. Many of my clients have a CPA and use me for the day-to-day. Would it be worth a quick conversation with your CPA about that arrangement?\"",
            "",
            "OBJECTION: 'I need to think about it'",
            "RESPONSE: \"Of course. What specifically would you like to think through? I'd rather help you work through any concerns now than leave you with unanswered questions.\"",
            "",
            "OBJECTION: 'My business is too small for this'",
            "RESPONSE: \"The businesses that benefit most from professional bookkeeping are actually smaller ones — because every dollar matters more. And our Starter package is designed specifically for businesses at your stage. When you're growing, clean books are what help you grow faster, not slower.\"",
            "",
            "OBJECTION: 'I'll just use QuickBooks and do it myself'",
            "RESPONSE: \"QuickBooks is a great tool — I use it with my clients. The issue most business owners run into is that the software is only as good as the person using it. Miscategorized transactions and missed reconciliations can cost you thousands in overpaid taxes or bad business decisions. Would it be worth 20 minutes to see what a professionally maintained set of books actually looks like?\"",
        ]),
        ("POST-CALL FOLLOW-UP", [
            ('•', "Send a follow-up email within 1 hour of the call"),
            ('•', "Include: thank you, summary of what you discussed, the package(s) you recommended, next steps"),
            ('•', "Attach your engagement agreement if they said yes"),
            ('•', "If they said 'think about it': include a 2-3 bullet ROI summary and a specific follow-up date"),
            ('•', "Add to your CRM with status and next action date"),
        ]),
    ]
)

doc("04_CLIENT_ACQUISITION/Referral_Partner_Program.docx",
    "Referral Partner Program Guide",
    "Build a referral network that sends you a steady stream of ideal clients",
    [
        ("WHY REFERRAL PARTNERSHIPS ARE YOUR BEST GROWTH CHANNEL", [
            "Referred clients close at 3-5x the rate of cold outreach leads.",
            "They come with built-in trust, making the sales conversation faster.",
            "The lifetime value of a referred client is typically 25% higher.",
            "Referral partnerships are free to build and compound over time.",
            "For bookkeepers, the best referral partners are people who serve your exact target clients.",
        ]),
        ("TOP REFERRAL PARTNER CATEGORIES", [
            "TIER 1 — HIGHEST VALUE PARTNERS:",
            ('•', "CPAs and Tax Preparers: They need clean books to do tax returns. They HATE doing monthly bookkeeping. Position yourself as their bookkeeping arm — they refer clients to you, you refer tax work to them."),
            ('•', "Business Attorneys: Clients forming LLCs and corporations immediately need bookkeeping. Attorneys are trusted advisors and a single relationship can yield 5-10 clients/year."),
            ('•', "Business Bankers: SBA loan officers see new businesses every week. When a client gets a loan, they need bookkeeping. One banker relationship is gold."),
            "",
            "TIER 2 — STRONG VALUE PARTNERS:",
            ('•', "Financial Planners and Wealth Advisors: They serve business owner clients who often need bookkeeping help."),
            ('•', "Insurance Agents (especially commercial): Every business needs insurance, and good agents know everyone."),
            ('•', "Business Coaches and Consultants: They work with growth-stage businesses that are often overwhelmed."),
            ('•', "Fractional CFOs: They need a bookkeeper to handle day-to-day tasks while they do high-level advisory."),
            "",
            "TIER 3 — NICHE PARTNERS (depends on your specialization):",
            ('•', "Restaurant Consultants / Food Service Reps: If you specialize in restaurants"),
            ('•', "Real Estate Agents and Brokers: If you specialize in real estate investors"),
            ('•', "E-commerce Consultants / Shopify Experts: If you specialize in online sellers"),
            ('•', "Nonprofit Consultants: If you specialize in nonprofits"),
        ]),
        ("HOW TO APPROACH A REFERRAL PARTNER — SCRIPTS", [
            "INITIAL OUTREACH EMAIL TO A CPA:",
            "Subject: Partnering with [CPA Firm Name] — could be mutually valuable",
            "",
            "Hi [Name],",
            "",
            "I'm [Your Name], a bookkeeper who specializes in [industry/type of client]. I help business owners keep their books clean and current throughout the year so tax season is smooth and your job is easier.",
            "",
            "I've been looking to build a relationship with a CPA partner for client referrals — and I noticed that [Firm Name] serves a lot of [type of client], which is exactly who I work with.",
            "",
            "Here's what I'm thinking: when I have a client who needs tax strategy or a return, I refer them to you. When you have a client who needs monthly bookkeeping, you refer them to me. No fees, just a good working relationship.",
            "",
            "Would you be open to a 20-minute coffee to see if we're a good fit?",
            "",
            "Best,",
            "[Your Name]",
            "",
            "IN-PERSON MEETING SCRIPT:",
            "After pleasantries: 'I'd love to learn more about the kinds of clients you typically work with. What does your ideal client look like?'",
            "[Listen. Then:] 'That's interesting — a lot of the clients I work with are [similar description]. I find that they often struggle with [pain point] until they get proper bookkeeping in place. Does that show up in your practice too?'",
            "[Build connection. Then:] 'I've been building partnerships with CPAs because I think we complement each other perfectly. I handle the monthly work, you handle tax strategy — and together the client gets full financial support. Would you be open to sending referrals back and forth?'",
        ]),
        ("REFERRAL PARTNER TRACKING SYSTEM", [
            "Track every referral partner in a dedicated spreadsheet. Key fields:",
            ('•', "Partner Name | Company | Type (CPA/Attorney/etc.) | Date Met | Status (Prospect/Active/Inactive)"),
            ('•', "Referrals Received | Referrals Given | Last Contact Date | Notes"),
            "",
            "MONTHLY PARTNER RELATIONSHIP ACTIVITIES:",
            ('•', "Week 1: Email or text check-in to top 3 active partners"),
            ('•', "Week 2: Share a useful resource (article, checklist) with your partner network"),
            ('•', "Week 3: Schedule a coffee or lunch with a new potential partner"),
            ('•', "Week 4: Send referrals proactively — reciprocity is the foundation of strong partnerships"),
        ]),
        ("REFERRAL THANK-YOU PROTOCOL", [
            "When a partner sends you a referral (whether or not the prospect becomes a client):",
            ('•', "Step 1: Email the partner within 24 hours to say thank you and confirm you'll reach out to the prospect"),
            ('•', "Step 2: Send a handwritten thank-you card (rare enough to be memorable)"),
            ('•', "Step 3: If the referral becomes a paying client: send a gift card ($25-$50), a gift basket, or a restaurant gift certificate"),
            ('•', "Step 4: Update your referral tracking log"),
            ('•', "Step 5: Make it a priority to refer business back to that partner within 30 days if possible"),
            "",
            "NOTE ON PAYING FOR REFERRALS: Be careful with referral fees. In some states, CPAs and attorneys cannot accept referral fees from non-licensed professionals. Always check local regulations. Gift cards and gifts (not cash) are typically fine.",
        ]),
    ]
)

doc("04_CLIENT_ACQUISITION/LinkedIn_Strategy_Guide.docx",
    "LinkedIn Strategy Guide for Bookkeepers",
    "Build authority, attract clients, and grow your network on LinkedIn",
    [
        ("PROFILE OPTIMIZATION — YOUR DIGITAL STOREFRONT", [
            "HEADLINE (most important field — appears in search results):",
            ('•', "BAD: 'Bookkeeper at ABC Bookkeeping'"),
            ('•', "GOOD: 'Bookkeeper for [Niche] Businesses | Clean Books → Clear Decisions | Helping [Location] Business Owners Save 10+ Hours/Month'"),
            ('•', "Test 2-3 versions and track which gets more profile views"),
            "",
            "ABOUT SECTION FORMULA:",
            ('•', "Line 1-2: Who you help and the transformation you deliver"),
            ('•', "Line 3-5: What makes you different / your approach"),
            ('•', "Line 6-8: Proof (clients served, years experience, certifications)"),
            ('•', "Line 9-10: Call to action (DM me / book a free call)"),
            "",
            "FEATURED SECTION: Add your best content or a lead magnet (free checklist PDF).",
            "",
            "EXPERIENCE SECTION: Write results-focused bullet points, not just duties.",
            ('•', "BAD: 'Performed bank reconciliations and categorized transactions'"),
            ('•', "GOOD: 'Managed books for 15+ small businesses, averaging $500K ARR, reducing close time from 3 weeks to 3 days'"),
            "",
            "SKILLS & ENDORSEMENTS: Add QuickBooks Online, Xero, Bookkeeping, Financial Reporting, Tax Preparation, Payroll Processing. Ask clients and colleagues to endorse these.",
        ]),
        ("CONTENT STRATEGY — WHAT TO POST", [
            "Post 3-5 times per week. Rotate through these content types:",
            "",
            "TYPE 1 — EDUCATIONAL (40% of posts):",
            ('•', "Tip-based: '3 things every [industry] business owner should track monthly'"),
            ('•', "Myth-busting: 'The biggest bookkeeping myth that costs business owners thousands'"),
            ('•', "How-to: 'How to reconcile your bank account in 20 minutes'"),
            "",
            "TYPE 2 — SOCIAL PROOF (20% of posts):",
            ('•', "Share client wins (anonymized if needed): 'A client came to me with 6 months of unreconciled books. Here's what we found and how we fixed it...'"),
            ('•', "Share testimonials: Screenshot or quote with client permission"),
            "",
            "TYPE 3 — BEHIND THE SCENES (20% of posts):",
            ('•', "Your process: 'Here's exactly what happens in the first 30 days of working with me'"),
            ('•', "Tools you use: 'The 5 tools I use to deliver bookkeeping that my clients actually understand'"),
            ('•', "Day in the life: What a month-end close actually looks like"),
            "",
            "TYPE 4 — ENGAGEMENT POSTS (20% of posts):",
            ('•', "Questions: 'What's your biggest bookkeeping headache? Drop it in the comments.'"),
            ('•', "Polls: 'Do you do your own books? A) Yes B) No C) I should probably hand this off'"),
            ('•', "Hot takes: 'Unpopular opinion: Most small businesses don't need accounting software in year one'"),
        ]),
        ("LINKEDIN OUTREACH TEMPLATES", [
            "CONNECTION REQUEST (never use the default):",
            '"Hi [Name], I came across your profile while connecting with [industry] business owners in [city]. I help businesses like yours keep clean books and make confident financial decisions. Would love to connect!"',
            "",
            "FOLLOW-UP MESSAGE AFTER CONNECTING:",
            '"Thanks for connecting, [Name]! I see you run [Company] — impressive. Quick question: are you handling your own bookkeeping right now, or do you have support in place?"',
            "",
            "[If they engage:] 'I love helping [industry] businesses get their finances under control. I actually have a free resource — [checklist/guide] — that might be useful. Want me to send it over?'",
            "",
            "MESSAGING SEQUENCE FOR WARM LEADS:",
            "Day 1: Connect + personalized note",
            "Day 3: Thank-you message + one value-add (article, tip, insight)",
            "Day 7: Soft ask: 'I'd love to learn more about your business. Would you be open to a quick 15-minute call?'",
            "Day 14: One more touch if no response, then move to 'long-game' (comment on their posts monthly)",
        ]),
        ("LINKEDIN ANALYTICS — WHAT TO TRACK WEEKLY", [
            ('•', "Profile views (goal: increase 10% month-over-month)"),
            ('•', "Post impressions and engagement rate (aim for 2-5% engagement)"),
            ('•', "Connection requests sent vs. accepted (track acceptance rate)"),
            ('•', "Messages sent vs. replies received"),
            ('•', "Discovery calls booked from LinkedIn (the only metric that truly matters)"),
            "",
            "WEEKLY LINKEDIN ROUTINE (30 minutes/day):",
            ('•', "Morning (10 min): Engage with 5 posts in your feed (meaningful comments, not just 'Great post!')"),
            ('•', "Midday (10 min): Send 5 connection requests to ideal clients"),
            ('•', "Afternoon (10 min): Respond to all messages and comments on your posts"),
            ('•', "Once per week (30 min): Write and publish one long-form post"),
        ]),
        ("LINKEDIN QUICK WINS FOR NEW BOOKKEEPERS", [
            ('•', "Announce your launch: 'Exciting news — I just launched my bookkeeping practice!' post gets strong engagement"),
            ('•', "Ask for testimonials from anyone you've helped, even informally"),
            ('•', "Join LinkedIn groups where your target clients hang out (e.g., 'Restaurant Owners Network')"),
            ('•', "Tag referral partners in educational posts — they'll share with their audience"),
            ('•', "Add a Calendly link to your profile so prospects can book directly without DMing first"),
        ]),
    ]
)

doc("04_CLIENT_ACQUISITION/Local_Networking_Guide.docx",
    "Local Networking Guide for Bookkeepers",
    "Build a local client pipeline through in-person networking events, BNI, and chambers of commerce",
    [
        ("WHY LOCAL NETWORKING WORKS FOR BOOKKEEPERS", [
            "People hire bookkeepers they trust. Trust is built faster in person than online.",
            "Local businesses often prefer local service providers — especially for financial services.",
            "A single strong local referral network can fill your entire client roster.",
            "Networking events are low-cost and have compounding returns over time.",
        ]),
        ("TOP LOCAL NETWORKING VENUES", [
            "1. CHAMBER OF COMMERCE",
            ('•', "Join your local chamber — typically $200-500/year"),
            ('•', "Attend monthly mixers and business after-hours events"),
            ('•', "Volunteer for a committee to build deeper relationships faster"),
            ('•', "Ask to speak at a chamber event on bookkeeping basics (great authority builder)"),
            "",
            "2. BNI (BUSINESS NETWORK INTERNATIONAL)",
            ('•', "BNI chapters have ONE bookkeeper per chapter — if the slot is open, take it"),
            ('•', "BNI members are committed to giving each other referrals"),
            ('•', "Attend a chapter meeting as a visitor first; BNI is high-commitment but high-reward"),
            ('•', "POWER PARTNERS in BNI for bookkeepers: CPAs, attorneys, financial advisors, insurance agents"),
            "",
            "3. INDUSTRY ASSOCIATION EVENTS",
            ('•', "Restaurant Association meetings if you target restaurants"),
            ('•', "Real Estate Investor Association (REIA) if you target real estate investors"),
            ('•', "Local eCommerce or entrepreneur meetups"),
            ('•', "SCORE mentoring events — attendees are often new business owners who need bookkeeping"),
            "",
            "4. SMALL BUSINESS DEVELOPMENT CENTER (SBDC)",
            ('•', "SBDCs offer free workshops for new business owners — volunteer to co-present"),
            ('•', "Ask the SBDC director to refer clients who need bookkeeping help"),
        ]),
        ("30-SECOND ELEVATOR PITCH (Customize for your niche)", [
            "FORMULA: I help [WHO] to [TRANSFORMATION] so they can [OUTCOME].",
            "",
            "EXAMPLES:",
            ('•', "Generalist: 'I help small business owners keep their books clean and current, so they can make confident financial decisions and never dread tax season again.'"),
            ('•', "Restaurant niche: 'I help restaurant owners track food costs, labor percentages, and daily sales so they can protect their margins and know exactly what's profitable on their menu.'"),
            ('•', "eCommerce niche: 'I help online sellers reconcile sales across platforms and keep their inventory and COGS accurate, so their books actually reflect their real profit.'"),
            "",
            "FOLLOW-UP QUESTION: After your pitch, always ask: 'What about you — what do you do?'",
            "Then LISTEN and look for ways to help them or connect them with someone in your network.",
        ]),
        ("CONVERSATION SCRIPTS FOR NETWORKING EVENTS", [
            "STARTING A CONVERSATION:",
            '"Hi, I\'m [Name]. First time at this event — have you been before?"',
            "[Or:] 'How did you hear about this group?'",
            "",
            "TRANSITIONING TO BUSINESS:",
            "After some rapport: 'So what kind of work do you do?'",
            "[After they answer:] 'Interesting! How long have you been doing that?'",
            "[After they answer:] 'And how are things going on the business side?' [This often opens up pain points]",
            "",
            "BRINGING UP YOUR WORK NATURALLY:",
            "'I actually work with a lot of [similar] business owners. I'm a bookkeeper — I help them keep their finances organized so they can focus on running the business instead of doing data entry.'",
            "",
            "THE SOFT CLOSE AT A NETWORKING EVENT:",
            "'It sounds like we might have some good reasons to stay connected. Would you be open to grabbing coffee next week? I'd love to learn more about what you do.'",
        ]),
        ("FOLLOW-UP AFTER NETWORKING EVENTS — THE 24-HOUR RULE", [
            ('•', "Connect on LinkedIn within 24 hours with a personalized note referencing where you met"),
            ('•', "Send a brief email if you exchanged cards: 'Great to meet you at [event] last night...'"),
            ('•', "If they expressed interest in your services, invite them to a discovery call within 48 hours"),
            ('•', "If they're a potential referral partner, suggest coffee within the week"),
            ('•', "Add them to your CRM and set a follow-up reminder for 30 days"),
            ('•', "Pro tip: Write a note on the back of their business card immediately after the conversation so you remember details to personalize your follow-up"),
        ]),
    ]
)

# ── 05_CLIENT_ONBOARDING ───────────────────────────────────────────────────────

doc("05_CLIENT_ONBOARDING/Client_Onboarding_SOP.docx",
    "Client Onboarding Standard Operating Procedure",
    "Step-by-step process from signed engagement letter to first month delivery",
    [
        ("OVERVIEW — THE ONBOARDING EXPERIENCE", [
            "Your onboarding process is your first chance to prove your value and set expectations. A smooth onboarding builds client confidence, reduces miscommunication, and prevents scope creep.",
            "Timeline: Most clients should be fully onboarded within 5-7 business days of signing.",
            "Goal: By the end of onboarding, you have access to all accounts, a clear understanding of their business, and a first month's work plan.",
        ]),
        ("PHASE 1 — AGREEMENT SIGNED (Day 0-1)", [
            ('•', "Step 1.1: Send engagement agreement via DocuSign, HelloSign, or PDF email"),
            ('•', "Step 1.2: Send invoice for first month's payment via your invoicing platform"),
            ('•', "Step 1.3: Mark 'Pending' in your CRM — do not begin work until payment received"),
            ('•', "Step 1.4: As soon as payment clears, send Welcome Email #1 (see Welcome_Email_Sequence.docx)"),
            ('•', "Step 1.5: Create client folder in your document management system"),
            ('•', "Step 1.6: Set up client record in your practice management software"),
        ]),
        ("PHASE 2 — INTAKE AND ACCESS (Day 1-3)", [
            ('•', "Step 2.1: Send Client Intake Form (see Client_Intake_Form.docx) — give 48 hours to complete"),
            ('•', "Step 2.2: Send Welcome Email #2 with access setup checklist (see Welcome_Email_Sequence.docx)"),
            ('•', "Step 2.3: Gain access to accounting software — client should add you as an accountant user"),
            ('•', "Step 2.4: Gain access to bank feeds — either direct connect in software or client exports"),
            ('•', "Step 2.5: Gather prior period financials (last 12 months statements or prior bookkeeper files)"),
            ('•', "Step 2.6: Confirm payroll provider if applicable — request reports or access"),
            ('•', "Step 2.7: Add client to your time tracking software with correct billing rate"),
        ]),
        ("PHASE 3 — SETUP AND HISTORICAL CLEANUP (Day 3-7)", [
            ('•', "Step 3.1: Review prior period books — note any obvious errors, miscategorizations, or missing transactions"),
            ('•', "Step 3.2: Reconcile opening balance — ensure your starting point is clean"),
            ('•', "Step 3.3: Set up or review chart of accounts — confirm it matches the industry and client needs"),
            ('•', "Step 3.4: Set up bank and credit card feeds in accounting software"),
            ('•', "Step 3.5: Set up recurring transactions and rules for common vendors"),
            ('•', "Step 3.6: Document client-specific categorization preferences in your notes"),
            ('•', "Step 3.7: Complete initial cleanup if prior books were a mess — bill separately per engagement agreement"),
        ]),
        ("PHASE 4 — KICKOFF CALL (End of Week 1)", [
            "The kickoff call is 30-45 minutes and happens after you've reviewed their books.",
            "",
            "KICKOFF CALL AGENDA:",
            ('•', "Welcome and introduction (5 min)"),
            ('•', "Review what you found in their books — share your initial observations (10 min)"),
            ('•', "Confirm your monthly process: what you'll do, when you'll deliver it, what format (10 min)"),
            ('•', "Set expectations: what you need from them monthly (receipts, explanations, bank access) (5 min)"),
            ('•', "Questions and answers (10 min)"),
            ('•', "Confirm next delivery date and communication preferences"),
            "",
            "Send Welcome Email #3 (kickoff confirmation) after the call.",
        ]),
        ("PHASE 5 — FIRST MONTH DELIVERY", [
            ('•', "Complete first month's bookkeeping according to your service agreement"),
            ('•', "Prepare the monthly financial package (P&L, Balance Sheet, any additional reports per agreement)"),
            ('•', "Write a brief narrative summary (3-5 sentences) explaining the key numbers"),
            ('•', "Schedule a report walkthrough call for the first 2-3 months"),
            ('•', "Send the report delivery email with attached financials"),
            ('•', "After delivering: add month to time tracking log and generate invoice for next period"),
            ('•', "Update client record: last delivery date, next delivery date, status = Active"),
        ]),
        ("ONBOARDING QUALITY CHECKLIST", [
            "Before marking onboarding complete, confirm all boxes are checked:",
            ('•', "[ ] Engagement agreement signed and filed"),
            ('•', "[ ] First payment received"),
            ('•', "[ ] Intake form completed and filed"),
            ('•', "[ ] Access to accounting software confirmed"),
            ('•', "[ ] Bank feeds connected"),
            ('•', "[ ] Chart of accounts reviewed and adjusted"),
            ('•', "[ ] Opening balance reconciled"),
            ('•', "[ ] Client preferences documented"),
            ('•', "[ ] Kickoff call completed"),
            ('•', "[ ] First delivery date set and communicated"),
            ('•', "[ ] Client added to monthly workflow calendar"),
        ]),
    ]
)

doc("05_CLIENT_ONBOARDING/Client_Intake_Form.docx",
    "Client Intake Form",
    "Comprehensive intake questionnaire for new bookkeeping clients",
    [
        ("SECTION 1 — BUSINESS INFORMATION", [
            "Business Legal Name: ___________________________________________________",
            "DBA (if different): ____________________________________________________",
            "Business Type: [ ] Sole Proprietorship  [ ] LLC  [ ] S-Corp  [ ] C-Corp  [ ] Partnership",
            "Year Business Started: ______",
            "EIN / Tax ID: ___________________________",
            "State of Formation: __________________________",
            "Business Address: _____________________________________________________",
            "Website: ______________________________________________________________",
            "Primary Industry: ______________________________________________________",
            "Brief Description of What Your Business Does: ___________________________",
        ]),
        ("SECTION 2 — CONTACT INFORMATION", [
            "Owner / Primary Contact Name: __________________________________________",
            "Email Address: ________________________________________________________",
            "Phone Number (preferred): ______________________________________________",
            "Preferred Contact Method: [ ] Email  [ ] Phone  [ ] Text  [ ] Video Call",
            "Best Time to Reach You: _______________________________________________",
            "Bookkeeping Contact (if different from owner): ___________________________",
            "Accountant / CPA Name and Contact: _____________________________________",
        ]),
        ("SECTION 3 — CURRENT BOOKKEEPING SITUATION", [
            "Are you currently using accounting software?  [ ] Yes  [ ] No",
            "If yes, which software: [ ] QuickBooks Online  [ ] Xero  [ ] Wave  [ ] FreshBooks  [ ] Other: ______",
            "How long have you been using it? ________",
            "Login/access details will be provided via: [ ] Accountant Invitation  [ ] Shared Login  [ ] Other",
            "",
            "Who has been handling your bookkeeping?",
            "[ ] I do it myself  [ ] Employee  [ ] Previous bookkeeper  [ ] No one  [ ] Other: _____________",
            "",
            "How current are your books?",
            "[ ] Up to date  [ ] A few months behind  [ ] 6+ months behind  [ ] I'm not sure",
            "",
            "Please describe any known issues with your current books: _______________",
        ]),
        ("SECTION 4 — BANK ACCOUNTS AND CREDIT CARDS", [
            "Please list all business bank accounts:",
            "Account 1: Bank Name _________________ Account Type _____________ Last 4 digits _______",
            "Account 2: Bank Name _________________ Account Type _____________ Last 4 digits _______",
            "Account 3: Bank Name _________________ Account Type _____________ Last 4 digits _______",
            "",
            "Please list all business credit cards:",
            "Card 1: Bank/Issuer ________________ Card Type ______________ Last 4 digits ___________",
            "Card 2: Bank/Issuer ________________ Card Type ______________ Last 4 digits ___________",
            "",
            "Do you use PayPal, Stripe, Square, or other payment processors?  [ ] Yes  [ ] No",
            "If yes, please list: __________________________________________________",
            "",
            "Do you have loans or lines of credit?  [ ] Yes  [ ] No",
            "If yes, lender name and balance: ______________________________________",
        ]),
        ("SECTION 5 — PAYROLL AND CONTRACTORS", [
            "Do you have employees?  [ ] Yes  [ ] No   If yes, how many: _______",
            "Payroll software / provider: _____________________________________________",
            "Pay frequency: [ ] Weekly  [ ] Bi-weekly  [ ] Semi-monthly  [ ] Monthly",
            "",
            "Do you pay independent contractors?  [ ] Yes  [ ] No",
            "If yes, how many contractors in a typical month: _______",
            "Do you currently issue 1099s?  [ ] Yes  [ ] No  [ ] I'm not sure",
        ]),
        ("SECTION 6 — FINANCIAL GOALS AND PAIN POINTS", [
            "What is your #1 goal for having your books managed professionally?",
            "____________________________________________________________________________",
            "",
            "What has been your biggest frustration with bookkeeping in the past?",
            "____________________________________________________________________________",
            "",
            "What financial reports are most important to you? (check all that apply)",
            "[ ] Profit & Loss (Income Statement)  [ ] Balance Sheet  [ ] Cash Flow Statement",
            "[ ] Budget vs. Actual  [ ] Sales by Product/Service  [ ] Accounts Receivable Aging",
            "[ ] Custom Reports — describe: _________________________________________",
            "",
            "Is there anything specific you'd like me to pay attention to in your books?",
            "____________________________________________________________________________",
        ]),
    ]
)

doc("05_CLIENT_ONBOARDING/Bookkeeping_Engagement_Agreement.docx",
    "Bookkeeping Services Engagement Agreement",
    "Professional client agreement template — review with an attorney before use",
    [
        ("AGREEMENT OVERVIEW", [
            "This Bookkeeping Services Agreement ('Agreement') is entered into as of [DATE] between:",
            "",
            "Service Provider: [YOUR BUSINESS NAME], a [State] [LLC/Sole Proprietorship] ('Bookkeeper')",
            "Address: [Your Address]",
            "Email: [Your Email]",
            "",
            "AND",
            "",
            "Client: [CLIENT BUSINESS NAME], a [State] [Business Type] ('Client')",
            "Address: [Client Address]",
            "Email: [Client Email]",
            "",
            "Together referred to as the 'Parties.'",
        ]),
        ("1. SCOPE OF SERVICES", [
            "The Bookkeeper agrees to provide the following services on a monthly basis:",
            "",
            "[ ] Bank and credit card reconciliation for up to [X] accounts",
            "[ ] Transaction categorization and coding",
            "[ ] Monthly Profit & Loss Statement preparation",
            "[ ] Monthly Balance Sheet preparation",
            "[ ] Accounts payable tracking",
            "[ ] Accounts receivable tracking",
            "[ ] Payroll entry (client uses third-party payroll service)",
            "[ ] Sales tax tracking and filing preparation",
            "[ ] Monthly financial summary and report delivery",
            "[ ] Unlimited email support (response within 1 business day)",
            "",
            "EXCLUDED SERVICES (available at additional cost):",
            ('•', "Tax preparation and filing"),
            ('•', "Payroll processing"),
            ('•', "Historical cleanup of prior period books"),
            ('•', "CFO advisory services"),
            ('•', "Any service not expressly listed above"),
        ]),
        ("2. FEES AND PAYMENT TERMS", [
            "Monthly Service Fee: $[AMOUNT] per month",
            "Payment Due: [1st / 15th] of each month",
            "Payment Method: [Credit Card / ACH / Check]",
            "",
            "LATE PAYMENT: Invoices unpaid after [15] days will incur a late fee of 1.5% per month. Work may be suspended for accounts more than [30] days past due.",
            "",
            "SETUP / CLEANUP FEE: If prior period cleanup is required, a one-time fee of $[AMOUNT] will be billed separately and is due upon engagement.",
            "",
            "RATE INCREASES: Bookkeeper reserves the right to adjust monthly fees with [30] days written notice. Client may terminate without penalty if they do not accept the new rate.",
        ]),
        ("3. CLIENT RESPONSIBILITIES", [
            "Client agrees to:",
            ('•', "Provide accurate and complete financial information in a timely manner"),
            ('•', "Grant access to all required bank accounts, credit cards, and financial platforms within 5 business days of signing this Agreement"),
            ('•', "Respond to information requests within [5] business days"),
            ('•', "Provide source documents (receipts, invoices) upon request"),
            ('•', "Notify Bookkeeper of any significant business changes (new accounts, loans, ownership changes) within 30 days"),
            ('•', "Review delivered financials and notify Bookkeeper of any discrepancies within [14] days of delivery"),
        ]),
        ("4. TERM AND TERMINATION", [
            "TERM: This Agreement begins on [START DATE] and continues on a month-to-month basis unless terminated.",
            "",
            "TERMINATION BY CLIENT: Client may terminate this Agreement with [30] days written notice. Client is responsible for fees for services rendered through the termination date.",
            "",
            "TERMINATION BY BOOKKEEPER: Bookkeeper may terminate this Agreement with [30] days written notice, or immediately in the event of non-payment, fraudulent activity, or breach of this Agreement.",
            "",
            "UPON TERMINATION: Bookkeeper will provide all client financial records in an export format within [14] days of the termination date. Outstanding balances are due immediately upon termination.",
        ]),
        ("5. CONFIDENTIALITY AND DATA SECURITY", [
            "Bookkeeper agrees to:",
            ('•', "Keep all client financial information strictly confidential"),
            ('•', "Not disclose client information to any third party without written consent, except as required by law"),
            ('•', "Use industry-standard security measures to protect client data"),
            ('•', "Not use client information for any purpose other than providing the services described herein"),
            "",
            "DISCLAIMER: Bookkeeper is not responsible for errors caused by client providing inaccurate or incomplete information. Client acknowledges that bookkeeping services do not constitute tax advice.",
        ]),
        ("6. SIGNATURES", [
            "By signing below, both parties agree to the terms of this Agreement.",
            "",
            "SERVICE PROVIDER SIGNATURE:",
            "Name: _________________________________ Date: ____________",
            "Title: _________________________________",
            "Signature: _____________________________",
            "",
            "CLIENT SIGNATURE:",
            "Name: _________________________________ Date: ____________",
            "Title: _________________________________",
            "Signature: _____________________________",
            "",
            "LEGAL DISCLAIMER: This template is provided for informational purposes only and does not constitute legal advice. Consult a licensed attorney before using this agreement with clients.",
        ]),
    ]
)

doc("05_CLIENT_ONBOARDING/Welcome_Email_Sequence.docx",
    "Welcome Email Sequence — 3-Email Onboarding Series",
    "Copy-paste email templates for a seamless client onboarding experience",
    [
        ("EMAIL 1 — WELCOME AND NEXT STEPS (Send immediately after payment)", [
            "SUBJECT: Welcome to [Your Business Name] — Here's what happens next",
            "",
            "Hi [Client First Name],",
            "",
            "Welcome! I'm so excited to start working together. Your payment has been received and you're officially onboarded. Let me walk you through what comes next.",
            "",
            "Here's what to expect in the next 7 days:",
            "",
            "TODAY: You'll receive a client intake form via [email/link]. Please complete this within 48 hours — it helps me understand your business, accounts, and goals.",
            "",
            "DAYS 2-3: I'll send you a separate email with instructions for granting me access to your accounting software and bank feeds. Please watch for this — access is the biggest bottleneck in onboarding.",
            "",
            "DAYS 4-7: I'll review your books and set everything up on my end. If I have questions, I'll reach out via email (I aim to respond within 24 hours on business days).",
            "",
            "END OF WEEK 1: We'll schedule a 30-minute kickoff call to review my initial findings, walk through our process, and set expectations. You'll receive a calendar invite.",
            "",
            "A few things to know about working with me:",
            "✓ Monthly reports delivered by the [date] of each month",
            "✓ Questions answered within 1 business day via email",
            "✓ You'll always know where your money is going",
            "",
            "I'm here to make your financial life simpler. Please don't hesitate to reach out with any questions.",
            "",
            "Warmly,",
            "[Your Name]",
            "[Business Name] | [Phone] | [Email]",
        ]),
        ("EMAIL 2 — ACCESS SETUP CHECKLIST (Send 24 hours after Email 1)", [
            "SUBJECT: Action needed: Granting me access to your accounts",
            "",
            "Hi [Client First Name],",
            "",
            "To get your books set up correctly, I need access to a few things. This email walks you through exactly how to do it — most clients complete this in under 15 minutes.",
            "",
            "STEP 1 — ACCOUNTING SOFTWARE ACCESS:",
            "[ ] In QuickBooks Online: Click the Gear icon → Manage Users → Invite Accountant → Enter [your email]",
            "[ ] In Xero: Click your organization name → Settings → Users → Invite a User → Enter [your email] → Role: Advisor",
            "[ ] Other software: Reply to this email and I'll send specific instructions",
            "",
            "STEP 2 — BANK FEED CONNECTION:",
            "Most banks connect automatically through your accounting software. If your bank requires manual statements, please:",
            "[ ] Download CSV or PDF statements for all business accounts (last 3 months)",
            "[ ] Upload to [Google Drive folder link / Dropbox / your document portal]",
            "",
            "STEP 3 — INTAKE FORM:",
            "[ ] If you haven't completed the intake form yet, please do so here: [link]",
            "",
            "STEP 4 — PAYROLL (if applicable):",
            "[ ] Please add me as a user or send me a copy of your last 3 months of payroll reports",
            "",
            "If you run into any issues with these steps, reply to this email or text me at [phone]. I'm happy to hop on a quick screen share to walk you through it.",
            "",
            "Best,",
            "[Your Name]",
        ]),
        ("EMAIL 3 — KICKOFF CALL CONFIRMATION (Send after kickoff call is scheduled)", [
            "SUBJECT: Your kickoff call is confirmed + what to expect",
            "",
            "Hi [Client First Name],",
            "",
            "Your kickoff call is confirmed for:",
            "",
            "DATE: [Day, Month Date]",
            "TIME: [Time] [Timezone]",
            "LINK: [Zoom/Google Meet link]",
            "DURATION: 30 minutes",
            "",
            "Here's our agenda for the call:",
            "1. My initial review of your books — what I found and what we'll address",
            "2. Walk through our monthly process and what you'll receive each month",
            "3. Set expectations: what I need from you and when",
            "4. Q&A — any questions you have about working together",
            "",
            "TO MAKE THE MOST OF OUR CALL, it would be helpful if you could think about:",
            ('•', "Any specific transactions or categories you've been uncertain about"),
            ('•', "The financial reports that matter most to you in running your business"),
            ('•', "Any upcoming changes in your business (new employees, loans, expansions)"),
            "",
            "I've already done a preliminary review of your accounts and I'm looking forward to sharing what I found.",
            "",
            "See you [day]!",
            "",
            "[Your Name]",
            "",
            "P.S. — If you need to reschedule, please use this link: [reschedule link] or reply to this email at least 24 hours in advance.",
        ]),
    ]
)

doc("05_CLIENT_ONBOARDING/Client_Portal_Setup_Guide.docx",
    "Client Portal Setup Guide",
    "How to set up a professional client portal for document sharing and communication",
    [
        ("WHY YOU NEED A CLIENT PORTAL", [
            "A client portal eliminates email attachment chaos, keeps all documents organized, and signals professionalism to new clients.",
            "Benefits: Secure document sharing, automatic version control, client self-service for uploading receipts, professional branded experience.",
        ]),
        ("OPTION 1 — GOOGLE DRIVE (Free, beginner-friendly)", [
            ('•', "Create a Google Drive folder structure: /Clients/[Client Name]/[Year]/[Month]"),
            ('•', "Share the client's top-level folder with their Google account (View or Comment access)"),
            ('•', "Create subfolders: Financial Reports, Source Documents, Agreements, Tax Documents"),
            ('•', "Use Google Drive's 'Request files' feature to let clients upload without seeing all contents"),
            ('•', "Pros: Free, familiar, reliable | Cons: Not branded, not purpose-built for bookkeeping"),
        ]),
        ("OPTION 2 — LISCIO (Best dedicated client portal for bookkeepers)", [
            ('•', "Liscio is a practice management + client portal platform built for accounting firms"),
            ('•', "Features: Secure messaging, document sharing, e-signatures, task management, mobile app"),
            ('•', "Cost: ~$49/month for solo practitioners"),
            ('•', "Setup: Create firm account → Add clients → Invite via email → Clients download Liscio app"),
            ('•', "Clients love the mobile app for uploading receipts on the go"),
        ]),
        ("OPTION 3 — FINANCIAL CENTS (Best all-in-one for growing firms)", [
            ('•', "Financial Cents includes client portal + practice management + time tracking"),
            ('•', "Features: Client requests, document storage, workflow templates, reporting"),
            ('•', "Cost: ~$19/month per team member"),
            ('•', "Best for bookkeepers with 10+ clients who want everything in one place"),
        ]),
        ("PORTAL SETUP CHECKLIST", [
            ('•', "[ ] Choose your portal platform"),
            ('•', "[ ] Create folder/workspace structure for each client"),
            ('•', "[ ] Add your branding (logo, colors) if platform supports it"),
            ('•', "[ ] Create a template folder structure to duplicate for new clients"),
            ('•', "[ ] Write a portal welcome guide for clients (link in Email 1)"),
            ('•', "[ ] Test the client experience by creating a test account"),
            ('•', "[ ] Add portal link to your onboarding email sequence"),
        ]),
    ]
)

# ── 06_SERVICE_DELIVERY ────────────────────────────────────────────────────────

doc("06_SERVICE_DELIVERY/Monthly_Bookkeeping_Checklist.docx",
    "Monthly Bookkeeping Checklist",
    "40-item monthly checklist for professional bookkeeping service delivery",
    [
        ("WEEK 1 — TRANSACTION PROCESSING", [
            ('•', "[ ] Download and import all bank statements for the month"),
            ('•', "[ ] Download and import all credit card statements for the month"),
            ('•', "[ ] Process all pending transactions in accounting software"),
            ('•', "[ ] Categorize all income transactions with correct revenue accounts"),
            ('•', "[ ] Categorize all expense transactions with correct expense accounts"),
            ('•', "[ ] Match transactions to open invoices (accounts receivable)"),
            ('•', "[ ] Match transactions to outstanding bills (accounts payable)"),
            ('•', "[ ] Record any cash transactions from client-provided documentation"),
            ('•', "[ ] Process all credit card receipts and match to transactions"),
            ('•', "[ ] Enter payroll journal entry or sync payroll software"),
        ]),
        ("WEEK 2 — RECONCILIATION", [
            ('•', "[ ] Reconcile all business checking accounts to bank statements"),
            ('•', "[ ] Reconcile all business savings accounts"),
            ('•', "[ ] Reconcile all business credit cards to statements"),
            ('•', "[ ] Reconcile PayPal/Stripe/Square accounts if applicable"),
            ('•', "[ ] Reconcile petty cash fund if applicable"),
            ('•', "[ ] Confirm all reconciliations show $0 difference"),
            ('•', "[ ] Investigate and resolve any uncleared transactions older than 30 days"),
            ('•', "[ ] Review and clear any duplicate transactions"),
        ]),
        ("WEEK 3 — REVIEW AND ADJUSTMENTS", [
            ('•', "[ ] Review Profit & Loss for any unusual or misclassified transactions"),
            ('•', "[ ] Review Balance Sheet for any accounts with unexpected balances"),
            ('•', "[ ] Check accounts receivable aging — flag invoices over 30 days past due"),
            ('•', "[ ] Check accounts payable — ensure all bills entered and nothing past due"),
            ('•', "[ ] Record prepaid expenses and depreciation entries if applicable"),
            ('•', "[ ] Record any loan principal vs. interest splits"),
            ('•', "[ ] Confirm owner draws and contributions are properly recorded"),
            ('•', "[ ] Review equity accounts for accuracy"),
            ('•', "[ ] Update fixed asset schedule if any purchases or disposals occurred"),
            ('•', "[ ] Accrue any significant expenses not yet invoiced"),
        ]),
        ("WEEK 4 — REPORTING AND DELIVERY", [
            ('•', "[ ] Run final Profit & Loss Statement for the month"),
            ('•', "[ ] Run final Balance Sheet as of month end"),
            ('•', "[ ] Run Cash Flow Statement if included in client package"),
            ('•', "[ ] Prepare any additional reports per engagement agreement"),
            ('•', "[ ] Write 3-5 sentence financial narrative summary (key highlights and flags)"),
            ('•', "[ ] Format reports for client delivery (PDF preferred)"),
            ('•', "[ ] Upload to client portal or send via secure email"),
            ('•', "[ ] Send monthly report delivery email with summary"),
            ('•', "[ ] Schedule report walkthrough call if included in client's package"),
            ('•', "[ ] Log hours worked in time tracking software"),
            ('•', "[ ] Generate client invoice for next month if on monthly billing"),
            ('•', "[ ] Update client record: last delivery date, notes, next action"),
        ]),
    ]
)

doc("06_SERVICE_DELIVERY/Bank_Reconciliation_SOP.docx",
    "Bank Reconciliation Standard Operating Procedure",
    "Step-by-step reconciliation process to ensure accurate books every month",
    [
        ("WHAT IS A BANK RECONCILIATION AND WHY IT MATTERS", [
            "A bank reconciliation compares your accounting software records to the official bank statement. It ensures every transaction is recorded, catches errors, and prevents fraud.",
            "Reconciling monthly (or even weekly) is a fundamental control that every professional bookkeeper must perform.",
            "A completed reconciliation with a $0 difference is your proof that the books are accurate.",
        ]),
        ("STEP 1 — GATHER YOUR MATERIALS", [
            ('•', "Bank or credit card statement for the period being reconciled (PDF or paper)"),
            ('•', "Access to accounting software (QuickBooks Online, Xero, etc.)"),
            ('•', "Prior month's reconciliation report (to confirm ending balance carried forward correctly)"),
            ('•', "List of any outstanding checks from prior months"),
        ]),
        ("STEP 2 — ENTER TRANSACTIONS (if not already done)", [
            ('•', "Ensure all transactions for the period are entered in the software"),
            ('•', "This includes: deposits, withdrawals, ACH transfers, wire transfers, interest income, fees"),
            ('•', "In QBO: Banking → Bank Feeds → review and accept/categorize all transactions"),
            ('•', "In Xero: Accounting → Bank Accounts → review imported transactions"),
        ]),
        ("STEP 3 — BEGIN THE RECONCILIATION IN YOUR SOFTWARE", [
            "IN QUICKBOOKS ONLINE:",
            ('•', "Go to Accounting → Reconcile → Select the account"),
            ('•', "Enter the Statement Ending Date and Ending Balance from your bank statement"),
            ('•', "Click Start Reconciling"),
            "",
            "IN XERO:",
            ('•', "Go to Accounting → Bank Accounts → Reconcile"),
            ('•', "The system auto-matches transactions — review and confirm each match"),
        ]),
        ("STEP 4 — MATCH TRANSACTIONS", [
            ('•', "Check off each transaction in the software that appears on the bank statement"),
            ('•', "For QBO: Check the box next to each matching transaction"),
            ('•', "For deposits: match by date and amount"),
            ('•', "For checks: match by check number and amount"),
            ('•', "For ACH/wire: match by date and description"),
            ('•', "Running difference should decrease to $0 as you check off transactions"),
        ]),
        ("STEP 5 — INVESTIGATE DISCREPANCIES", [
            "If the reconciliation does not balance to $0, systematically investigate:",
            ('•', "Transposition errors: Did you enter a number like $1,290 instead of $1,920?"),
            ('•', "Duplicate entries: Is any transaction recorded twice in the software?"),
            ('•', "Missing transactions: Is any bank transaction not recorded in the software?"),
            ('•', "Wrong amount: Was a transaction entered for the wrong amount?"),
            ('•', "Bank errors: Did the bank post an incorrect amount? (rare, but happens)"),
            ('•', "Prior period issues: Did the opening balance carry forward correctly?"),
        ]),
        ("STEP 6 — FINALIZE AND DOCUMENT", [
            ('•', "Once difference = $0, click Finish Now (QBO) or Mark as Reconciled (Xero)"),
            ('•', "Print or export the Reconciliation Report"),
            ('•', "Save the bank statement in the client's document folder"),
            ('•', "Note the date reconciled and initials in your work log"),
            ('•', "If you cannot achieve $0 balance: document the discrepancy, note what you investigated, and consult your client before making an adjusting entry"),
        ]),
    ]
)

doc("06_SERVICE_DELIVERY/Month_End_Close_Procedure.docx",
    "Month-End Close Procedure",
    "Complete timeline and steps for closing the books each month",
    [
        ("MONTH-END CLOSE OVERVIEW", [
            "The month-end close is the process of finalizing your financial records for a given period. A clean close ensures your reports are accurate, complete, and audit-ready.",
            "Target timeline: Complete close and deliver reports within [5-10] business days of month end.",
            "Adjust this timeline based on client complexity and your service agreement.",
        ]),
        ("DAY 1-2 AFTER MONTH END — TRANSACTION IMPORT", [
            ('•', "Download all bank statements (typically available by the 2nd of the month)"),
            ('•', "Import or sync transactions into accounting software"),
            ('•', "Send 'Document Request Email' to client for any receipts or explanations needed"),
            ('•', "Note any transactions flagged for categorization clarification"),
        ]),
        ("DAY 3-5 — PROCESSING AND CODING", [
            ('•', "Categorize all transactions"),
            ('•', "Process payroll entries"),
            ('•', "Enter any bills or invoices not yet recorded"),
            ('•', "Record owner draws, contributions, or equity transactions"),
            ('•', "Process any journal entries needed (depreciation, prepaid expenses, accruals)"),
        ]),
        ("DAY 6-8 — RECONCILIATION", [
            ('•', "Reconcile all bank accounts (per Bank Reconciliation SOP)"),
            ('•', "Reconcile all credit card accounts"),
            ('•', "Reconcile PayPal/Stripe/other payment processors"),
            ('•', "Review AR aging and AP aging"),
            ('•', "Confirm loan balances match lender statements"),
        ]),
        ("DAY 8-10 — REVIEW AND REPORTING", [
            ('•', "Review P&L: check for unusual spikes or missing amounts vs. prior months"),
            ('•', "Review Balance Sheet: confirm all asset, liability, and equity accounts make sense"),
            ('•', "Run final reports and format for delivery"),
            ('•', "Write client financial narrative (key highlights, notable changes, flags/questions)"),
            ('•', "Deliver reports to client via portal or email"),
        ]),
    ]
)

doc("06_SERVICE_DELIVERY/Data_Entry_Standards.docx",
    "Data Entry Standards and Coding Guide",
    "Consistency rules for transaction naming, categorization, and documentation",
    [
        ("WHY STANDARDS MATTER", [
            "Consistent data entry makes financial reports reliable, auditable, and meaningful.",
            "When every bookkeeper on your team (or just you) follows the same rules, clients get consistent results and your own quality reviews become faster.",
        ]),
        ("PAYEE NAMING CONVENTIONS", [
            ('•', "Always use the official vendor name, not abbreviations. 'Amazon Web Services' not 'AWS'"),
            ('•', "For recurring vendors, create a memorized transaction or rule to auto-populate"),
            ('•', "Capitalize properly: 'Staples Business Advantage' not 'staples business advantage'"),
            ('•', "For personal names (contractors): 'Last Name, First Name' — e.g., 'Smith, John'"),
            ('•', "Remove bank noise from imported names: 'AMZN*MA3X9F2 408-653-1079' → 'Amazon'"),
        ]),
        ("CATEGORIZATION RULES", [
            ('•', "When in doubt, ask the client — never guess on a large or unusual transaction"),
            ('•', "Meals: Use 'Meals & Entertainment' for client meals; 'Meals - Non-Client' for team meals"),
            ('•', "Office Supplies vs. Equipment: Under $2,500 → Office Supplies; Over $2,500 → Equipment (asset)"),
            ('•', "Software subscriptions: Code to 'Software & Technology' or 'Computer Expenses'"),
            ('•', "Mixed personal/business transactions: Flag for owner to clarify; never assume personal = business"),
            ('•', "Split transactions when one payment covers multiple expense types"),
        ]),
        ("DOCUMENTATION STANDARDS", [
            ('•', "Attach receipts to transactions over $75 (IRS recommendation for business meals/entertainment is $50)"),
            ('•', "For large or unusual items, add a memo explaining the purpose"),
            ('•', "Journal entries must include a memo explaining the reason for the entry"),
            ('•', "Reconciliation discrepancies must be documented even if resolved"),
            ('•', "All documents saved in PDF format, named: YYYY-MM-DD_VendorName_Amount.pdf"),
        ]),
        ("RED FLAG TRANSACTIONS — ESCALATE TO REVIEW", [
            ('•', "Any transaction over $5,000 not clearly explained by context"),
            ('•', "Transactions at round-dollar amounts (often estimates that should be actual amounts)"),
            ('•', "Duplicate payments to the same vendor in the same amount"),
            ('•', "Vendor names that are people's names (potential fraud or owner compensation)"),
            ('•', "Transactions coded to 'Other Expenses' or 'Miscellaneous' repeatedly"),
            ('•', "Prior-period transactions (transactions dated in a closed period)"),
        ]),
    ]
)

# ── 07_CLIENT_COMMUNICATION ────────────────────────────────────────────────────

doc("07_CLIENT_COMMUNICATION/Email_Template_Library.docx",
    "Client Email Template Library",
    "15 professional email templates for every bookkeeping scenario",
    [
        ("TEMPLATE 1 — MONTHLY REPORT DELIVERY", [
            "SUBJECT: [Month] Financial Reports — [Company Name]",
            "",
            "Hi [First Name],",
            "",
            "Your [Month] financial reports are ready! Here's a quick summary of the highlights:",
            "",
            "📊 Revenue: $[X] ([+/-X%] vs. prior month)",
            "💰 Net Profit: $[X] (Profit Margin: [X]%)",
            "🏦 Cash Balance: $[X] as of [date]",
            "",
            "[2-3 sentence narrative: e.g., 'Revenue increased by 12% compared to September, driven primarily by [service category]. Your largest expense this month was [category] at $X. One item to be aware of: [any flag or observation].']",
            "",
            "Your reports are attached below:",
            "• Profit & Loss Statement — [Month] [Year]",
            "• Balance Sheet — [Month] [Year]",
            "",
            "Would you like to schedule a 15-minute call to walk through these numbers? Reply here or grab a time: [Calendly link]",
            "",
            "Best,",
            "[Your Name]",
        ]),
        ("TEMPLATE 2 — DOCUMENT REQUEST", [
            "SUBJECT: Documents needed for [Month] bookkeeping — [Company Name]",
            "",
            "Hi [First Name],",
            "",
            "I'm working on your [Month] books and need a few items to keep things moving:",
            "",
            "[ ] [Specific item: e.g., 'Receipt for the $1,240 charge at Office Depot on Oct 3']",
            "[ ] [Specific item: e.g., 'Explanation of the $3,500 transfer from personal account on Oct 15']",
            "[ ] [Specific item: e.g., 'October payroll report from Gusto']",
            "",
            "Please upload these to [client portal link] or reply to this email by [DATE] so I can complete your books on schedule.",
            "",
            "Thanks so much!",
            "[Your Name]",
        ]),
        ("TEMPLATE 3 — DEADLINE REMINDER", [
            "SUBJECT: Quick reminder — [specific item] needed by [DATE]",
            "",
            "Hi [First Name],",
            "",
            "Just a friendly reminder that I'm waiting on [specific item] to finalize your [Month] books. Your reports are scheduled to be delivered by [date].",
            "",
            "If I don't receive the information by [date], I may need to push your delivery date back.",
            "",
            "You can upload documents here: [portal link]",
            "Or just reply to this email — whatever is easier for you.",
            "",
            "Thank you!",
            "[Your Name]",
        ]),
        ("TEMPLATE 4 — LATE PAYMENT NOTICE — FIRST NOTICE", [
            "SUBJECT: Invoice #[XXX] — Payment reminder",
            "",
            "Hi [First Name],",
            "",
            "I hope everything is going well! I wanted to reach out regarding Invoice #[XXX] for $[AMOUNT], which was due on [DATE].",
            "",
            "If you've already sent payment, please disregard this email — sometimes timing creates these notices.",
            "",
            "If payment is still pending, you can pay via [payment link / Venmo / bank transfer] at your earliest convenience.",
            "",
            "If there's anything I can do to help, please don't hesitate to reach out.",
            "",
            "Thank you,",
            "[Your Name]",
        ]),
        ("TEMPLATE 5 — LATE PAYMENT NOTICE — SECOND NOTICE (14+ days past due)", [
            "SUBJECT: Important: Invoice #[XXX] — [14 / 30] days past due",
            "",
            "Hi [First Name],",
            "",
            "I'm reaching out again regarding Invoice #[XXX] for $[AMOUNT], now [14/30] days past due.",
            "",
            "Per our engagement agreement, a late fee of 1.5% per month has been applied, bringing the total to $[AMOUNT+FEE].",
            "",
            "Please submit payment by [DATE] to avoid service interruption. You can pay via [payment link].",
            "",
            "If you're experiencing a cash flow issue, I'd be happy to discuss a payment plan. Please reply to this email or call me at [phone].",
            "",
            "Thank you for your prompt attention to this matter.",
            "[Your Name]",
        ]),
        ("TEMPLATE 6 — RATE INCREASE NOTICE", [
            "SUBJECT: Update to your monthly service rate — effective [DATE]",
            "",
            "Hi [First Name],",
            "",
            "I'm writing to let you know that I'll be making a small adjustment to service rates, effective [DATE].",
            "",
            "Your new monthly rate will be $[NEW AMOUNT] (currently $[OLD AMOUNT]).",
            "",
            "This adjustment reflects [increases in software costs / expanded scope of our work together / annual pricing review]. I remain fully committed to delivering the same quality and responsiveness you've experienced.",
            "",
            "If you have any questions or would like to discuss, please don't hesitate to reach out. Per our agreement, you may terminate without penalty if you prefer not to continue at the new rate.",
            "",
            "Thank you for being such a valued client. I truly enjoy working with [Company Name] and look forward to continuing our partnership.",
            "",
            "Warmly,",
            "[Your Name]",
        ]),
        ("TEMPLATE 7 — MISSING INFORMATION FOLLOW-UP (Friendly but firm)", [
            "SUBJECT: Still waiting on [item] — can you help?",
            "",
            "Hi [First Name],",
            "",
            "I sent a request on [DATE] for [specific information] and haven't heard back yet. I want to make sure this doesn't delay your monthly reports.",
            "",
            "Could you please send this by [DATE]? If you're unsure what I need or how to get it, I'm happy to hop on a quick call.",
            "",
            "Thanks for your help!",
            "[Your Name]",
        ]),
        ("TEMPLATE 8 — YEAR-END PREPARATION", [
            "SUBJECT: Getting ready for tax season — action items for [Company Name]",
            "",
            "Hi [First Name],",
            "",
            "It's that time of year! Here's what we need to do to make sure your year-end close goes smoothly:",
            "",
            "BY JANUARY 15:",
            "[ ] Confirm all 1099 vendor information is correct (I'll send you a list of eligible vendors)",
            "[ ] Review any large personal/business expense questions from Q4",
            "[ ] Confirm your business structure and any ownership changes in [year]",
            "",
            "BY JANUARY 31:",
            "[ ] 1099s must be filed (I'll handle this if included in your package, or flag if you need to work with your CPA)",
            "[ ] December books will be finalized and delivered",
            "",
            "I'll be in touch with more specifics. Is there anything on your end I should know about for year-end?",
            "",
            "Best,",
            "[Your Name]",
        ]),
        ("TEMPLATE 9 — ASKING FOR A TESTIMONIAL", [
            "SUBJECT: A quick favor — would you share your experience?",
            "",
            "Hi [First Name],",
            "",
            "It's been [X months] since we started working together, and I hope you've found the experience as valuable as I have!",
            "",
            "I'm building my practice and one of the most powerful ways I can reach other business owners is through real testimonials from clients like you.",
            "",
            "Would you be willing to leave a brief review? It only takes 2-3 minutes and would mean the world to me.",
            "",
            "You can leave a review here: [Google Business link / LinkedIn recommendation request]",
            "",
            "Or if you'd prefer, you can just reply to this email and I can turn your words into a testimonial for my website (with your permission, of course).",
            "",
            "Thank you so much,",
            "[Your Name]",
        ]),
        ("TEMPLATE 10 — ASKING FOR A REFERRAL", [
            "SUBJECT: Could you introduce me to someone?",
            "",
            "Hi [First Name],",
            "",
            "I'm so glad we've been able to help [Company Name] stay on top of the numbers. It's been a pleasure working with you.",
            "",
            "I'm growing my practice and my best new clients have always come from referrals from people like you. Is there anyone in your network — a business owner friend, colleague, or fellow entrepreneur — who might benefit from cleaner books and financial clarity?",
            "",
            "If so, I'd be grateful for an introduction. You can simply forward this email, or send them my website: [website].",
            "",
            "As a thank-you for any referral that becomes a client, [insert your referral reward: gift card, month of free service, etc.].",
            "",
            "Thank you for thinking of me!",
            "[Your Name]",
        ]),
        ("ADDITIONAL TEMPLATES (11-15) — QUICK REFERENCE", [
            "TEMPLATE 11 — ONBOARDING DELAY: 'Hi [Name], just a quick note — your onboarding is taking a bit longer than expected due to [reason]. I expect to have your books set up by [new date]. Thank you for your patience!'",
            "",
            "TEMPLATE 12 — SERVICE PAUSE REQUEST: 'Hi [Name], I wanted to flag that based on your request to pause services for [month], I'll resume bookkeeping in [month]. Please confirm this is still the plan and I'll update your account accordingly.'",
            "",
            "TEMPLATE 13 — SCOPE EXPANSION: 'Hi [Name], as discussed, I'm happy to add [service] to your monthly package. This will increase your monthly rate from $[X] to $[Y], effective [date]. Please reply to confirm and I'll update our agreement.'",
            "",
            "TEMPLATE 14 — ERROR CORRECTION: 'Hi [Name], I identified an error in [month]'s books — [brief description]. I've made the correction and updated your reports. The corrected P&L is attached. I apologize for any confusion and have added a check to prevent this going forward.'",
            "",
            "TEMPLATE 15 — OFFBOARDING: 'Hi [Name], I'm sorry to see you go and wish [Company] all the best. As discussed, [date] will be your final day of service. I'll deliver all files in an export format by [date]. It's been a pleasure working with you.'",
        ]),
    ]
)

doc("07_CLIENT_COMMUNICATION/Monthly_Report_Walkthrough_Script.docx",
    "Monthly Report Walkthrough Script",
    "Word-for-word script for walking clients through their monthly financials",
    [
        ("BEFORE THE CALL — PREPARATION", [
            ('•', "Review the reports yourself first and identify 3-5 key talking points"),
            ('•', "Note any significant changes from prior month (up or down)"),
            ('•', "Flag any items requiring client action or decision"),
            ('•', "Have the reports open in front of you, ready to share screen if on video"),
            ('•', "Check your notes from last month's call — did you follow up on any action items?"),
        ]),
        ("OPENING THE CALL (2 minutes)", [
            '"Hi [Name]! Great to connect. Thanks for making time — I know how busy things get."',
            "",
            '"I just pulled up your [Month] reports. We have about 20-30 minutes — I\'ll walk you through the key numbers, flag a few things I want you to be aware of, and then we\'ll have time for any questions you have. Sound good?"',
            "",
            "[Small talk — one genuine question about their business, team, or something they mentioned last month]",
        ]),
        ("WALKING THROUGH THE P&L (10-15 minutes)", [
            "START AT THE TOP:",
            '"Let\'s start with revenue. In [month], your total revenue was $[X]. That\'s [up/down] [X%] compared to [prior month]. [Explain the reason if you know it, or ask: \'Do you know what drove that change?\'']"',
            "",
            "COST OF GOODS SOLD (if applicable):",
            '"Your cost of goods sold was $[X], giving you a gross profit of $[X] — a gross margin of [X]%. [Compare to prior month or benchmark.]"',
            "",
            "OPERATING EXPENSES:",
            '"Moving down to expenses — total operating expenses for the month were $[X]. The top three expense categories were [Category 1] at $[X], [Category 2] at $[X], and [Category 3] at $[X]."',
            "",
            '"One thing I want to flag: [any unusual expense, spike, or item needing discussion]."',
            "",
            "NET PROFIT:",
            '"At the bottom line, your net profit for [month] was $[X] — a profit margin of [X]%. [Put this in plain language: \'For every dollar you brought in, you kept X cents.\']"',
            "",
            "TREND COMMENT:",
            '"Comparing the last three months: [Month1] $[X], [Month2] $[X], [Month3] $[X]. [Identify the trend and what it means for them.]"',
        ]),
        ("CASH POSITION (5 minutes)", [
            '"Let\'s look at your cash position. As of [last day of month], you had $[X] in your checking and $[X] in savings — total liquid cash of $[X]."',
            "",
            '"That\'s [up/down] from last month\'s $[X], mainly because [reason: strong sales, large vendor payment, equipment purchase, etc.]."',
            "",
            '"Your current cash runway — if revenue stopped today — would be approximately [X months]. [This is reassuring / something to keep an eye on.]"',
        ]),
        ("ACTION ITEMS AND CLOSE (5 minutes)", [
            '"Before we wrap up, I have [X] things I need from you or that need your attention:"',
            "",
            "List each action item clearly. For example:",
            ('•', "'I need a receipt for the $850 charge at [Vendor] on [date] — can you email that to me?'"),
            ('•', "'Your Q3 estimated tax payment is due [date] — have you spoken with your CPA about the amount?'"),
            ('•', "'We have an invoice from [Vendor] that's 45 days past due — do you want me to reach out or will you handle that?'"),
            "",
            "CLOSE:",
            '"Any questions on the numbers or anything you\'d like me to look into for next month?"',
            "",
            "[Address questions]",
            "",
            '"Great. I\'ll send you a follow-up email summarizing these action items. Your [next month] books will be ready by [date]. Thanks, [Name] — great talking with you!"',
        ]),
    ]
)

doc("07_CLIENT_COMMUNICATION/Client_Satisfaction_Survey.docx",
    "Client Satisfaction Survey",
    "Quarterly survey to measure satisfaction and identify growth opportunities",
    [
        ("SURVEY INTRODUCTION (Send via email)", [
            "SUBJECT: Quick 3-minute survey — help me serve you better",
            "",
            "Hi [Name],",
            "",
            "Every quarter, I send a short survey to my clients to make sure I'm delivering the value you expect. Your honest feedback helps me improve and ensure we're always aligned.",
            "",
            "It takes less than 3 minutes. Thank you so much for taking the time!",
            "",
            "[SURVEY LINK] or complete below:",
        ]),
        ("SECTION 1 — OVERALL SATISFACTION", [
            "1. On a scale of 1-10, how satisfied are you with our bookkeeping services overall?",
            "[ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5  [ ] 6  [ ] 7  [ ] 8  [ ] 9  [ ] 10",
            "",
            "2. How likely are you to recommend our services to another business owner? (1=Not at all, 10=Definitely)",
            "[ ] 1  [ ] 2  [ ] 3  [ ] 4  [ ] 5  [ ] 6  [ ] 7  [ ] 8  [ ] 9  [ ] 10",
        ]),
        ("SECTION 2 — SERVICE QUALITY", [
            "3. How satisfied are you with the accuracy of your monthly financial reports?",
            "[ ] Very Satisfied  [ ] Satisfied  [ ] Neutral  [ ] Dissatisfied  [ ] Very Dissatisfied",
            "",
            "4. How satisfied are you with our communication and responsiveness?",
            "[ ] Very Satisfied  [ ] Satisfied  [ ] Neutral  [ ] Dissatisfied  [ ] Very Dissatisfied",
            "",
            "5. How clearly do you understand your financial reports after receiving them?",
            "[ ] Very Clearly  [ ] Mostly Clearly  [ ] Somewhat  [ ] Not Very Clearly  [ ] Not at All",
        ]),
        ("SECTION 3 — OPEN FEEDBACK", [
            "6. What do you appreciate most about our service?",
            "____________________________________________________________________________",
            "",
            "7. What could we do better or differently?",
            "____________________________________________________________________________",
            "",
            "8. Is there any additional service you'd like us to offer that we're not currently providing?",
            "[ ] Payroll  [ ] Tax filing support  [ ] Budgeting/Forecasting  [ ] CFO advisory",
            "[ ] Sales tax filing  [ ] Other: _______________________________________________",
            "",
            "9. Any other comments or suggestions?",
            "____________________________________________________________________________",
        ]),
        ("USING SURVEY RESULTS", [
            ('•', "Send this survey in Month 3 (quarterly) of every client relationship"),
            ('•', "Review results within 48 hours and respond to any low scores personally"),
            ('•', "For scores of 7 or below: Schedule a call to address concerns immediately"),
            ('•', "For scores of 9-10: Ask if they'd be willing to share that feedback publicly as a testimonial"),
            ('•', "Track scores over time to identify trends in your service quality"),
            ('•', "Use open-ended answers to identify new service offerings or process improvements"),
        ]),
    ]
)

# ── XLSX FILES ─────────────────────────────────────────────────────────────────

print("\n  Creating XLSX files...")

# Pricing_Calculator.xlsx
wb = Workbook()
ws1 = wb.active; ws1.title = "Hourly Rate Calculator"

ws1.merge_cells('A1:D1')
c = ws1['A1']; c.value = "HOURLY RATE CALCULATOR"; c.fill = hf(NAV); c.font = bf(True,14,WHT); c.alignment = al()
ws1.row_dimensions[1].height = 32

ws1.merge_cells('A2:D2')
c2 = ws1['A2']; c2.value = "Fill in the yellow cells to calculate your required hourly rate"
c2.fill = hf("FFF9E6"); c2.font = bf(False,10,"555555"); c2.alignment = al()

headers_r = ["INPUT", "DESCRIPTION", "MONTHLY AMOUNT", "ANNUAL AMOUNT"]
hrow(ws1,3,[1,2,3,4],headers_r,NAV,WHT)

rows_input = [
    ("Monthly Overhead", "Rent, software, insurance, phone, misc", 850, "=C4*12"),
    ("Owner's Salary Goal", "What you want to pay yourself per month", 6000, "=C5*12"),
    ("Self-Employment Tax", "~15.3% of net profit (estimated)", 1100, "=C6*12"),
    ("Retirement / Benefits", "Health insurance, 401k, etc.", 400, "=C7*12"),
    ("Profit Margin Buffer", "Extra for savings, investments, growth", 500, "=C8*12"),
]
for i, (inp,desc,mo,yr) in enumerate(rows_input):
    r = 4+i; bg = LGR if i%2==0 else WHT
    drow(ws1,r,[1,2],[inp,desc],bg)
    for col,val in [(3,mo),(4,yr)]:
        c=ws1.cell(row=r,column=col,value=val)
        c.fill=hf(GLD+"33"); c.font=bf(True,10); c.alignment=al("center"); c.border=thin()
        c.number_format = '"$"#,##0'

ws1.cell(row=9,column=1,value="TOTAL MONTHLY NEED").font=bf(True,11,WHT)
ws1.cell(row=9,column=1).fill=hf(ACC)
ws1.cell(row=9,column=2,value="Sum of all monthly costs above").fill=hf(ACC)
ws1.cell(row=9,column=2).font=bf(False,10,WHT)
for col,val in [(3,"=SUM(C4:C8)"),(4,"=SUM(D4:D8)")]:
    c=ws1.cell(row=9,column=col,value=val)
    c.fill=hf(ACC); c.font=bf(True,11,WHT); c.alignment=al("center"); c.border=thin()
    c.number_format = '"$"#,##0'

ws1.append([])
ws1.append(["HOURS CALCULATION","","",""])
hrow(ws1,11,[1,2,3,4],["FACTOR","DESCRIPTION","VALUE","NOTES"],NAV,WHT)
hours_rows = [
    ("Available Hours/Month","Total hours you COULD work (40hrs×4.33wks)",173,"Full-time equivalent"),
    ("Non-Billable Hours","Admin, marketing, sales, professional dev",40,"Estimate 20-25% of time"),
    ("Vacation/Sick Days","Hours lost per month on average",16,"2 weeks/year ÷ 12"),
    ("Billable Hours/Month","Hours actually working for clients","=C12-C13-C14","Your productive capacity"),
]
for i,(f,d,v,n) in enumerate(hours_rows):
    r=12+i; bg=LGR if i%2==0 else WHT
    for col,val in [(1,f),(2,d),(3,v),(4,n)]:
        cc=ws1.cell(row=r,column=col,value=val)
        cc.fill=hf(bg); cc.font=bf(False,10); cc.alignment=al("left"); cc.border=thin()

ws1.append([])
hrow(ws1,17,[1,2,3,4],["RESULT","","YOUR RATE","HOW TO USE"],ACC,WHT)
ws1.cell(row=18,column=1,value="Required Hourly Rate").font=bf(True,12)
ws1.cell(row=18,column=1).fill=hf(GRN+"33")
formula = "=C9/C15"
rc=ws1.cell(row=18,column=3,value=formula)
rc.number_format = '"$"#,##0.00'
rc.fill=hf(GRN); rc.font=bf(True,14,WHT); rc.alignment=al("center"); rc.border=thin()
ws1.cell(row=18,column=4,value="This is your MINIMUM hourly rate. Add 20-30% for client value pricing.").font=bf(False,9)
ws1.cell(row=18,column=4).alignment=al("left")

ws1.column_dimensions['A'].width = 26
ws1.column_dimensions['B'].width = 38
ws1.column_dimensions['C'].width = 18
ws1.column_dimensions['D'].width = 32

# Sheet 2 — Package Builder
ws2 = wb.create_sheet("Package Builder")
ws2.merge_cells('A1:G1')
c=ws2['A1']; c.value="SERVICE PACKAGE BUILDER"; c.fill=hf(NAV); c.font=bf(True,14,WHT); c.alignment=al()
ws2.row_dimensions[1].height=32

hrow(ws2,2,[1,2,3,4,5,6,7],["SERVICE LINE ITEM","INCLUDED?","EST HOURS/MO","HOURLY RATE","LINE TOTAL","PACKAGE","NOTES"],NAV,WHT)
services = [
    ("Bank Reconciliation (1 account)","Yes",1.5,"","=IF(B3=\"Yes\",C3*$C$20,0)","All","Core service"),
    ("Additional Bank Accounts (ea)","Yes",0.5,"","=IF(B4=\"Yes\",C4*$C$20,0)","Starter+","Per account"),
    ("Credit Card Reconciliation","Yes",1.0,"","=IF(B5=\"Yes\",C5*$C$20,0)","All","Per card"),
    ("Transaction Categorization","Yes",2.0,"","=IF(B6=\"Yes\",C6*$C$20,0)","All","Estimate for <150 txn/mo"),
    ("Monthly P&L Report","Yes",0.5,"","=IF(B7=\"Yes\",C7*$C$20,0)","All","Standard delivery"),
    ("Balance Sheet Preparation","Yes",0.5,"","=IF(B8=\"Yes\",C8*$C$20,0)","All","Monthly"),
    ("Email Support (unlimited)","Yes",1.0,"","=IF(B9=\"Yes\",C9*$C$20,0)","All","Response <1 bus. day"),
    ("AP Tracking","No",1.0,"","=IF(B10=\"Yes\",C10*$C$20,0)","Professional+","Bill entry & aging"),
    ("AR Tracking","No",1.0,"","=IF(B11=\"Yes\",C11*$C$20,0)","Professional+","Invoice tracking"),
    ("Payroll Journal Entries","No",0.5,"","=IF(B12=\"Yes\",C12*$C$20,0)","Professional+","Sync from payroll provider"),
    ("Sales Tax Tracking","No",0.5,"","=IF(B13=\"Yes\",C13*$C$20,0)","Professional+","Tracking only, not filing"),
    ("Monthly Report Call","No",0.75,"","=IF(B14=\"Yes\",C14*$C$20,0)","Professional+","30-min walkthrough call"),
    ("Cash Flow Statement","No",0.5,"","=IF(B15=\"Yes\",C15*$C$20,0)","Premium","Monthly"),
    ("Budget vs. Actual Report","No",0.75,"","=IF(B16=\"Yes\",C16*$C$20,0)","Premium","Requires budget setup"),
    ("CFO Advisory Call","No",1.0,"","=IF(B17=\"Yes\",C17*$C$20,0)","Premium","Monthly strategy call"),
    ("Sales Tax Filing","No",0.5,"","=IF(B18=\"Yes\",C18*$C$20,0)","Premium","1 state included"),
]
for i,(svc,inc,hrs,rate,tot,pkg,notes) in enumerate(services):
    r=3+i; bg=LGR if i%2==0 else WHT
    for col,val in [(1,svc),(2,inc),(3,hrs),(4,rate),(5,tot),(6,pkg),(7,notes)]:
        cc=ws2.cell(row=r,column=col,value=val)
        cc.fill=hf(bg); cc.font=bf(False,10); cc.alignment=al("left"); cc.border=thin()
        if col==2:
            cc.font=bf(True,10,"27AE60" if inc=="Yes" else "E74C3C")
        if col==5:
            cc.number_format='"$"#,##0.00'

# Rate input cell
ws2.cell(row=20,column=1,value="YOUR HOURLY RATE:").font=bf(True,12)
ws2.cell(row=20,column=3,value=65); ws2.cell(row=20,column=3).fill=hf(GLD+"44")
ws2.cell(row=20,column=3).font=bf(True,12); ws2.cell(row=20,column=3).number_format='"$"#,##0'
ws2.cell(row=20,column=4,value="← Change this cell").font=bf(False,9,"E94560")

ws2.cell(row=21,column=1,value="TOTAL PACKAGE COST (based on Yes items):").font=bf(True,11,WHT)
ws2.cell(row=21,column=1).fill=hf(GRN)
tc=ws2.cell(row=21,column=5,value="=SUM(E3:E18)")
tc.number_format='"$"#,##0.00'; tc.fill=hf(GRN); tc.font=bf(True,12,WHT); tc.alignment=al("center")

for col,w in [(1,32),(2,12),(3,14),(4,12),(5,14),(6,14),(7,28)]:
    ws2.column_dimensions[chr(64+col)].width=w

wb.save(BASE+"03_PRICING_PACKAGING/Pricing_Calculator.xlsx"); print("  ✓ 03_PRICING_PACKAGING/Pricing_Calculator.xlsx")

# Client_Lead_Tracker_CRM.xlsx
wb2 = Workbook()
ws_leads = wb2.active; ws_leads.title = "Lead Tracker"

ws_leads.merge_cells('A1:J1')
c=ws_leads['A1']; c.value="CLIENT LEAD TRACKER — CRM"; c.fill=hf(NAV); c.font=bf(True,14,WHT); c.alignment=al()
ws_leads.row_dimensions[1].height=30

lead_headers = ["Name","Company","Source","Status","Date Added","Est. Monthly Value","Next Action","Notes","Phone","Email"]
hrow(ws_leads,2,list(range(1,11)),lead_headers,NAV,WHT)

status_colors = {"New":"1A5276","Contacted":ORG,"Proposal":"8E44AD","Won":GRN,"Lost":RED}
leads = [
    ("Sarah Mitchell","Mitchell Catering Co.","LinkedIn","Contacted","2024-01-08",650,"Follow-up call Jan 15","Interested but busy — reach back in Q2","(555)234-5678","sarah@mitchellcatering.com"),
    ("James Torres","Torres HVAC Services","Referral - CPA","Proposal","2024-01-10",900,"Send engagement letter","Reviewed packages, wants Professional","(555)345-6789","jtorres@torreshvac.com"),
    ("Amanda Chen","Chen Yoga Studio","Google Search","New","2024-01-12",450,"Initial email sent","Found us through 'bookkeeper near me'","(555)456-7890","amanda@chenyoga.com"),
    ("Michael Davis","Davis Landscaping","Networking - BNI","Won","2023-12-20",750,"Start onboarding","Signed 12/22, starting Jan 1","(555)567-8901","mdavis@davislandscaping.com"),
    ("Lisa Nguyen","Nguyen Dental Practice","Referral - Atty","Proposal","2024-01-05",1400,"Call follow-up Jan 14","High-value prospect, needs payroll too","(555)678-9012","lnguyen@nguyendental.com"),
    ("Robert Kim","Kim Real Estate Inv.","Cold Email","Contacted","2024-01-09",850,"Send case study","Has 4 rental properties, self-managing","(555)789-0123","rkim@kimrei.com"),
    ("Patricia Brown","Brown Bakery & Cafe","Chamber Event","New","2024-01-11",550,"Discovery call booked","Met at chamber mixer Jan 10","(555)890-1234","pbrown@brownbakery.com"),
    ("David Martinez","Martinez Consulting","LinkedIn","Lost","2023-11-15",700,"Archive","Went with a family friend","(555)901-2345","d.martinez@mconsult.com"),
    ("Jennifer Wilson","Wilson Photography","Instagram","Contacted","2024-01-07",400,"Send free tip sheet","Part-time photographer, solo","(555)012-3456","jwilson@wilsonphoto.com"),
    ("Thomas Anderson","Anderson Auto Repair","Walk-in","New","2024-01-13",600,"Call scheduled Jan 16","Came into our office, cash-based business","(555)123-4567","tanderson@andersonauto.com"),
]
for i, row_data in enumerate(leads):
    r=3+i; bg=LGR if i%2==0 else WHT
    drow(ws_leads,r,list(range(1,11)),row_data,bg)
    # Color the status cell
    status_cell = ws_leads.cell(row=r,column=4)
    status_val = row_data[3]
    scol = status_colors.get(status_val,NAV)
    status_cell.fill=hf(scol); status_cell.font=bf(True,10,WHT); status_cell.alignment=al("center")
    # Format monthly value
    vc=ws_leads.cell(row=r,column=6); vc.number_format='"$"#,##0'

for col,w in [(1,18),(2,22),(3,18),(4,12),(5,14),(6,16),(7,24),(8,28),(9,14),(10,26)]:
    ws_leads.column_dimensions[chr(64+col)].width=w

ws_active = wb2.create_sheet("Active Clients")
ws_active.merge_cells('A1:H1')
c=ws_active['A1']; c.value="ACTIVE CLIENT ROSTER"; c.fill=hf(GRN); c.font=bf(True,14,WHT); c.alignment=al()
ws_active.row_dimensions[1].height=30

active_headers=["Client Name","Company","Start Date","Monthly Rate","Software","Package","Next Report Due","Notes"]
hrow(ws_active,2,list(range(1,9)),active_headers,NAV,WHT)
active_clients=[
    ("Davis, Michael","Davis Landscaping","2024-01-01",750,"QuickBooks Online","Professional","2024-02-08","Seasonal business, slow Jan-Feb"),
    ("Nguyen, Lisa","Nguyen Dental Practice","2023-10-01",1400,"QuickBooks Online","Premium","2024-02-05","Monthly call 2nd Tuesday"),
    ("Garcia, Maria","Garcia Boutique","2023-07-15",500,"Xero","Starter","2024-02-07","Retail, high transaction volume"),
    ("Park, Steve","Park IT Solutions","2023-09-01",900,"QuickBooks Online","Professional","2024-02-06","Invoices clients net-30"),
    ("White, Jennifer","White Events Co.","2023-11-01",650,"FreshBooks","Starter","2024-02-08","Event-based, variable monthly revenue"),
]
for i,row_data in enumerate(active_clients):
    r=3+i; bg=LGR if i%2==0 else WHT
    drow(ws_active,r,list(range(1,9)),row_data,bg)
    vc=ws_active.cell(row=r,column=4); vc.number_format='"$"#,##0'

for col,w in [(1,18),(2,22),(3,14),(4,14),(5,20),(6,14),(7,18),(8,28)]:
    ws_active.column_dimensions[chr(64+col)].width=w

ws_wonlost = wb2.create_sheet("Won Lost Log")
ws_wonlost.merge_cells('A1:G1')
c=ws_wonlost['A1']; c.value="WON / LOST LOG — SALES ANALYTICS"; c.fill=hf(NAV); c.font=bf(True,14,WHT); c.alignment=al()
ws_wonlost.row_dimensions[1].height=30
hrow(ws_wonlost,2,list(range(1,8)),["Lead Name","Company","Outcome","Close Date","Monthly Value","Lost Reason","Sales Notes"],NAV,WHT)
wl_rows=[
    ("Davis, Michael","Davis Landscaping","WON","2023-12-22",750,"N/A","Closed after 2nd discovery call"),
    ("Martinez, David","Martinez Consulting","LOST","2023-11-15",700,"Personal relationship","Hired family friend instead"),
    ("Thompson, Gary","Thompson Plumbing","WON","2023-11-01",600,"N/A","Referral from BNI — easy close"),
    ("Brooks, Sandra","Brooks Photography","LOST","2023-10-10",350,"Price","Said too expensive for part-time biz"),
    ("Nguyen, Lisa","Nguyen Dental Practice","WON","2023-09-28",1400,"N/A","Value pricing worked — saw ROI clearly"),
]
for i,rd in enumerate(wl_rows):
    r=3+i; bg=LGR if i%2==0 else WHT
    drow(ws_wonlost,r,list(range(1,8)),rd,bg)
    oc=ws_wonlost.cell(row=r,column=3)
    oc.fill=hf(GRN) if rd[2]=="WON" else hf(RED)
    oc.font=bf(True,10,WHT); oc.alignment=al("center")
    vc=ws_wonlost.cell(row=r,column=5); vc.number_format='"$"#,##0'

for col,w in [(1,18),(2,22),(3,10),(4,14),(5,14),(6,20),(7,28)]:
    ws_wonlost.column_dimensions[chr(64+col)].width=w

wb2.save(BASE+"04_CLIENT_ACQUISITION/Client_Lead_Tracker_CRM.xlsx"); print("  ✓ 04_CLIENT_ACQUISITION/Client_Lead_Tracker_CRM.xlsx")

print("\n=== PART 2 COMPLETE ===")
