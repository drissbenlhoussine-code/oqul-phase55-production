"""Recruiting Agency OS — Part 1: folders 00–03"""
import os, json, csv
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = "/home/user/oqul-phase55-production/recruiting-agency-os/Ultimate_Recruiting_Agency_Operating_System/"

FOLDERS = [
    "00_START_HERE","01_BUSINESS_DEVELOPMENT","02_CLIENT_ONBOARDING",
    "03_CANDIDATE_SOURCING","04_CANDIDATE_MANAGEMENT","05_CLIENT_MANAGEMENT",
    "06_COMPLIANCE_LEGAL","07_PLACEMENT_PROCESS","08_BUSINESS_OPERATIONS",
    "09_MARKETING_GROWTH","10_NOTION_WORKSPACE","11_BONUSES",
    "12_CANVA_IMPORTABLE_TEMPLATES"
]
for f in FOLDERS:
    os.makedirs(BASE + f, exist_ok=True)

def doc(filename, title, subtitle, sections):
    d = Document()
    t = d.add_paragraph(title)
    t.style = d.styles['Normal']
    t.runs[0].bold = True
    t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
    if subtitle:
        s = d.add_paragraph(subtitle)
        s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10)
        s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    for section in sections:
        if isinstance(section, str):
            d.add_paragraph(section)
            continue
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
    f.write("""ULTIMATE RECRUITING AGENCY OPERATING SYSTEM

Start with START_HERE_Implementation_Guide.pdf.

EDITABLE FORMATS
- DOCX: edit in Microsoft Word or upload to Google Docs.
- XLSX/CSV: edit in Excel or upload to Google Sheets.
- PPTX: upload to Canva to convert into editable Canva designs.
- Notion assets: import CSV databases and copy the workspace structure.

IMPORTANT
Contracts, policies, and agreements are generic educational templates and are not legal advice.
Have a qualified professional review them before commercial use.
""")
print("  ✓ 00_START_HERE/README_FIRST.txt")

# ── 01_BUSINESS_DEVELOPMENT ───────────────────────────────────────────────────
doc("01_BUSINESS_DEVELOPMENT/Cold_Outreach_Templates.docx",
    "Cold Outreach Templates",
    "Recruiting Agency Operating System | Business Development",
    [
        ("LINKEDIN CONNECTION REQUEST TEMPLATES", [
            "Use these short, personalized messages to connect with decision-makers on LinkedIn.",
            ("•", "Hiring Manager (Generic): Hi [Name], I specialize in placing top [role] talent for [industry] companies. I'd love to connect and share how we've helped similar teams scale."),
            ("•", "Startup Founder: Hi [Name], congrats on the recent [funding/launch]. As you scale your team, I'd love to connect — we specialize in fast placements for growth-stage companies."),
            ("•", "HR Director: Hi [Name], I work with HR teams to cut time-to-fill on hard-to-fill [role] positions. Thought it would be great to connect."),
            ("•", "VP of Engineering: Hi [Name], I help engineering leaders find senior [stack] developers quickly. Happy to share results from similar placements."),
        ]),
        ("COLD EMAIL TEMPLATES", [
            "Send these to HR contacts, hiring managers, and C-suite via email.",
            ("•", "Subject: Faster [Role] Hires for [Company Name]\nHi [Name], I noticed [Company] is growing its [department]. We specialize in placing [role] professionals for companies like yours — typically within 10–14 days. Worth a 15-minute call? — [Your Name]"),
            ("•", "Subject: 3 [Role] Candidates Ready to Interview\nHi [Name], I have 3 pre-vetted [role] candidates available immediately. All have [X] years experience and strong references. Interested in profiles? — [Your Name]"),
            ("•", "Subject: How [Similar Company] Filled Their [Role] in 9 Days\nHi [Name], thought this case study would be relevant for [Company]. We helped [Similar Company] close a [role] search in 9 days after 3 months of searching in-house. Happy to share our process. — [Your Name]"),
        ]),
        ("PHONE COLD CALL SCRIPT", [
            "Opening: 'Hi [Name], this is [Your Name] from [Agency]. I work with [industry] companies to place top [role] talent quickly. Do you have 2 minutes?'",
            "Value statement: 'We typically deliver 3–5 qualified candidates within 5 business days and guarantee our placements for 90 days.'",
            "Question: 'Are you currently hiring for any [role] positions, or do you anticipate needs in the next quarter?'",
            "Objection — We use internal HR: 'Understood. Many of our clients have internal HR teams — we complement them by handling sourcing and initial screening, saving your team 20+ hours per search.'",
            "Close: 'Could we schedule a 15-minute call this week to explore if there's a fit?'",
        ]),
        ("FOLLOW-UP SEQUENCE (No Response)", [
            ("•", "Day 3: 'Hi [Name], following up on my message about [role] placements. Happy to share a quick case study relevant to [Company].'"),
            ("•", "Day 7: 'Hi [Name], I know hiring is time-consuming. We handle the full sourcing and screening process — you only meet pre-qualified candidates. Open to a 15-minute call?'"),
            ("•", "Day 14: 'Hi [Name], last follow-up. If timing isn't right now, I'd love to reconnect when you have an opening. Here's my calendar: [link]'"),
        ]),
        ("REFERRAL OUTREACH", [
            ("•", "To current clients: '[Name], I'm expanding my client base in [industry]. Do you know any HR leaders or hiring managers who might benefit from our services? Happy to offer you [referral incentive].'"),
            ("•", "To placed candidates: '[Name], congrats again on your new role! If you know anyone in your network looking for opportunities in [field], I'd love an introduction.'"),
        ]),
    ])

doc("01_BUSINESS_DEVELOPMENT/Discovery_Call_Script.docx",
    "Discovery Call Script",
    "Recruiting Agency Operating System | Business Development",
    [
        ("OPENING (0–2 min)", [
            "Thank you for taking the time, [Name]. I want to make sure this call is valuable for you, so I'll ask a few questions about your hiring situation and we can see if there's a good fit.",
        ]),
        ("SITUATION QUESTIONS (2–8 min)", [
            ("•", "Tell me about your current team structure for [department]."),
            ("•", "How many open roles do you have right now, and which are the most urgent?"),
            ("•", "What does your current hiring process look like from job posting to offer?"),
            ("•", "How long has your most urgent role been open?"),
            ("•", "Have you worked with recruiting agencies before? What was that experience like?"),
        ]),
        ("PAIN IDENTIFICATION (8–15 min)", [
            ("•", "What's the biggest challenge you're facing in filling this role?"),
            ("•", "What happens to the business if this role stays open another 30–60 days?"),
            ("•", "What type of candidate have you been struggling to find?"),
            ("•", "What's your internal HR team's capacity right now?"),
        ]),
        ("GOALS & CRITERIA (15–20 min)", [
            ("•", "Walk me through the ideal candidate profile — experience, skills, culture fit."),
            ("•", "What salary range are you working with?"),
            ("•", "Is this a permanent role, contract, or contract-to-hire?"),
            ("•", "What does a successful first 90 days look like for this person?"),
        ]),
        ("PRESENTING YOUR SOLUTION (20–25 min)", [
            "Based on what you've shared, here's how we work: We conduct a deep search of our network and active/passive candidates, screen everyone against your criteria, and deliver 3–5 qualified profiles within [X] business days. You only interview candidates we've already vetted.",
            "Our fee is [X]% of first-year base salary, with a [90]-day replacement guarantee.",
        ]),
        ("CLOSE (25–30 min)", [
            ("•", "Does this sound like what you're looking for?"),
            ("•", "If we can deliver strong profiles within 5 business days, would you be ready to start interviews?"),
            ("•", "The next step would be signing our service agreement and completing a job order form. Can we do that this week?"),
        ]),
    ])

doc("01_BUSINESS_DEVELOPMENT/Client_Proposal_Template.docx",
    "Client Proposal Template",
    "Recruiting Agency Operating System | Business Development",
    [
        ("EXECUTIVE SUMMARY", [
            "[Agency Name] is pleased to present this proposal to [Client Company] for recruiting services for the [Role Title] position.",
            "Based on our conversation on [Date], we understand you need a [seniority] [role] to [primary objective] within [timeframe].",
        ]),
        ("OUR UNDERSTANDING OF YOUR NEEDS", [
            ("•", "Role: [Job Title]"),
            ("•", "Department: [Department]"),
            ("•", "Salary Range: [Range]"),
            ("•", "Start Date Target: [Date]"),
            ("•", "Must-Have Skills: [List from intake]"),
            ("•", "Culture Fit: [Notes from discovery call]"),
        ]),
        ("OUR APPROACH", [
            "Week 1: Deep search of our proprietary database, LinkedIn Recruiter, and niche job boards. We will identify 20–40 potential candidates.",
            "Week 1–2: Phone screen all candidates against your criteria. We conduct competency-based interviews and reference pre-checks.",
            "Week 2: Deliver 3–5 fully profiled candidates with our written assessment of fit, compensation expectations, and availability.",
            "Ongoing: Manage interview scheduling, provide candidate prep, gather feedback, manage offer stage, and support onboarding handoff.",
        ]),
        ("FEE STRUCTURE", [
            ("•", "Retained Search: [X]% upfront, remainder on placement"),
            ("•", "Contingency Search: [X]% of first-year base salary, due on start date"),
            ("•", "Contract/Interim: [X]% markup on hourly rate"),
            ("•", "Guarantee: [90]-day replacement at no additional fee if candidate leaves or is terminated"),
        ]),
        ("WHY [AGENCY NAME]", [
            ("•", "[X] years specializing in [industry/function] recruiting"),
            ("•", "Average time-to-fill: [X] business days"),
            ("•", "Placement retention rate: [X]% at 12 months"),
            ("•", "Current database: [X]+ pre-vetted [role] professionals"),
        ]),
        ("NEXT STEPS", [
            "1. Review and sign the attached Service Agreement",
            "2. Complete the Job Order Intake Form (15 minutes)",
            "3. Schedule kickoff call with our lead recruiter",
            "4. Receive first candidate profiles within [X] business days",
        ]),
    ])

doc("01_BUSINESS_DEVELOPMENT/Follow_Up_Sequence.docx",
    "Follow-Up Sequence",
    "Recruiting Agency Operating System | Business Development",
    [
        ("7-TOUCH FOLLOW-UP FRAMEWORK", [
            "Research shows it takes 5–7 touches to convert a cold prospect. Use this sequence consistently.",
        ]),
        ("TOUCH 1 — DAY 1 (Initial Outreach)", [
            ("•", "Channel: LinkedIn or email"),
            ("•", "Goal: Introduce yourself and create curiosity"),
            ("•", "Message: [See Cold Outreach Templates]"),
        ]),
        ("TOUCH 2 — DAY 3 (Value Add)", [
            ("•", "Channel: Same as Touch 1"),
            ("•", "Goal: Provide value without asking for anything"),
            ("•", "Message: 'Hi [Name], I thought you might find this useful — [brief insight about hiring trends in their industry]. No response needed, just thought it was relevant.'"),
        ]),
        ("TOUCH 3 — DAY 7 (Social Proof)", [
            ("•", "Channel: Email or phone"),
            ("•", "Goal: Share a relevant case study or result"),
            ("•", "Message: 'Hi [Name], we recently helped [similar company] fill a [role] in 8 days after they had been searching for 3 months. Happy to share how. Worth a quick call?'"),
        ]),
        ("TOUCH 4 — DAY 14 (Direct Ask)", [
            ("•", "Channel: Phone call"),
            ("•", "Goal: Get a decision — yes, no, or not now"),
            ("•", "Script: 'Hi [Name], I've reached out a couple of times about [role] recruiting support. I don't want to keep bothering you — can I ask, is this something you'd consider exploring, or would you rather I circle back in [timeframe]?'"),
        ]),
        ("TOUCH 5 — DAY 30 (Re-engage)", [
            ("•", "Message: 'Hi [Name], it's been a few weeks. Hiring landscape has shifted a bit in [industry] — thought you might like to know [relevant trend]. Still happy to chat if timing works.'"),
        ]),
        ("TOUCH 6 — DAY 60 (New Angle)", [
            ("•", "Message: 'Hi [Name], I have a [role] candidate that just became available — [2-sentence profile]. Thought of you immediately. Is this a profile you'd want to see?'"),
        ]),
        ("TOUCH 7 — DAY 90 (Final Check-In)", [
            ("•", "Message: 'Hi [Name], I'll stop following up after this — I know your inbox is busy. If you ever need recruiting support for [role type], I'm here. Here's my calendar: [link]. Wishing [Company] continued success.'"),
        ]),
    ])

doc("01_BUSINESS_DEVELOPMENT/Objection_Handling_Scripts.docx",
    "Objection Handling Scripts",
    "Recruiting Agency Operating System | Business Development",
    [
        ("OBJECTION: 'YOUR FEES ARE TOO HIGH'", [
            "Acknowledge: 'I understand — our fee is a meaningful investment.'",
            "Reframe: 'Consider this: an unfilled role typically costs [2–3x monthly salary] in lost productivity. If we fill it in 10 days vs. 60 days in-house, the ROI is significant.'",
            "Option: 'We also offer a payment plan / retained structure that may work better for your budget. Would that help?'",
        ]),
        ("OBJECTION: 'WE USE IN-HOUSE HR'", [
            "Acknowledge: 'That's great — internal HR is valuable for culture and onboarding.'",
            "Reframe: 'We're not a replacement — we extend your team's reach. Your HR focuses on what they do best; we handle the sourcing and screening volume that slows them down.'",
            "Proof: 'We've worked alongside internal HR at [example companies]. They typically save 15–20 hours per search.'",
        ]),
        ("OBJECTION: 'WE TRIED AGENCIES BEFORE AND WERE DISAPPOINTED'", [
            "Empathize: 'That's a valid concern. Can I ask what went wrong?'",
            "Differentiate: 'We specialize exclusively in [niche] — we're not a generalist shop sending out bulk profiles. Every candidate is personally screened by our team.'",
            "De-risk: 'We offer a [90]-day guarantee. If it doesn't work out, we replace at no additional fee.'",
        ]),
        ("OBJECTION: 'WE'RE NOT HIRING RIGHT NOW'", [
            "Acknowledge: 'Completely understand.'",
            "Plant seed: 'Many of our best partnerships started with a conversation before there was an urgent need. When you do hire, you'll already know who to call.'",
            "Schedule: 'Could I check back in with you in [30/60/90] days? I'll send a quick note — no pressure.'",
        ]),
        ("OBJECTION: 'WE NEED TO GET BUDGET APPROVAL'", [
            "Support: 'Of course. I can provide a brief ROI summary you can share internally — it outlines the cost of an open role vs. our fee. Would that help make the case?'",
            "Next step: 'Who else is typically involved in this decision? Could we schedule a brief call with that person as well?'",
        ]),
        ("OBJECTION: 'WE POST ON LINKEDIN AND INDEED OURSELVES'", [
            "Acknowledge: 'Those are great tools for active candidates.'",
            "Differentiate: 'The best candidates — the top 20% who are currently employed and performing — aren't browsing job boards. We reach them directly through our network and outreach.'",
        ]),
    ])

doc("01_BUSINESS_DEVELOPMENT/Pricing_Guide.docx",
    "Pricing Guide",
    "Recruiting Agency Operating System | Business Development",
    [
        ("PRICING MODELS OVERVIEW", [
            "There are four main pricing models used by recruiting agencies. Choose the one that fits your niche and client type.",
        ]),
        ("1. CONTINGENCY (Most Common)", [
            ("•", "Fee: 15–25% of candidate's first-year base salary"),
            ("•", "When paid: Upon candidate start date"),
            ("•", "Best for: Permanent placements, new clients, smaller roles"),
            ("•", "Guarantee: 30–90 day replacement clause standard"),
            ("•", "Example: $80,000 salary × 20% = $16,000 fee"),
        ]),
        ("2. RETAINED SEARCH", [
            ("•", "Fee: 25–33% of first-year total compensation"),
            ("•", "Payment structure: 1/3 upfront, 1/3 at shortlist delivery, 1/3 on placement"),
            ("•", "Best for: Senior, executive, or confidential searches"),
            ("•", "Advantage: Exclusive commitment from agency; deeper search"),
            ("•", "Example: $150,000 salary × 30% = $45,000 (paid in three $15,000 installments)"),
        ]),
        ("3. CONTRACT / TEMP STAFFING", [
            ("•", "Fee: Bill rate = (pay rate × markup %). Typical markup: 40–60%"),
            ("•", "When paid: Weekly or bi-weekly invoicing"),
            ("•", "Best for: Short-term projects, seasonal, contract-to-hire"),
            ("•", "Example: Candidate paid $40/hr → bill client $58/hr (45% markup)"),
        ]),
        ("4. FLAT FEE / PROJECT-BASED", [
            ("•", "Fee: Fixed price per search or project (e.g., $5,000–$15,000)"),
            ("•", "Best for: Volume hiring, startups with budget constraints"),
            ("•", "Considerations: Define deliverables clearly (# of profiles, timeline, revisions)"),
        ]),
        ("GUARANTEE POLICY", [
            ("•", "Standard guarantee: [90] days from candidate start date"),
            ("•", "If candidate leaves or is terminated within guarantee period: free replacement search"),
            ("•", "Exclusions: Layoffs, role elimination, mutual agreement"),
        ]),
        ("SAMPLE FEE SCHEDULE", [
            ("•", "Entry-level roles ($30–50K): 15–18%"),
            ("•", "Mid-level roles ($50–100K): 18–22%"),
            ("•", "Senior roles ($100–200K): 22–28%"),
            ("•", "Executive roles ($200K+): 28–33% retained"),
        ]),
    ])

print("✓ 01_BUSINESS_DEVELOPMENT complete")

# ── 02_CLIENT_ONBOARDING ──────────────────────────────────────────────────────
doc("02_CLIENT_ONBOARDING/Welcome_Email_Templates.docx",
    "Welcome Email Templates",
    "Recruiting Agency Operating System | Client Onboarding",
    [
        ("EMAIL 1 — AGREEMENT SIGNED", [
            "Subject: Welcome to [Agency Name] — Let's Get Started",
            "Hi [Name],",
            "Welcome aboard! We're excited to partner with [Company] on your [Role] search.",
            "Here's what happens next:",
            ("•", "Step 1: Complete the Job Order Intake Form (link below) — 15 minutes"),
            ("•", "Step 2: We schedule your 30-minute Kickoff Call"),
            ("•", "Step 3: We begin sourcing immediately — first profiles in [X] business days"),
            "Please complete the intake form here: [Link]",
            "Your dedicated recruiter is [Recruiter Name] — [email] | [phone].",
            "Talk soon,\n[Your Name]",
        ]),
        ("EMAIL 2 — AFTER KICKOFF CALL", [
            "Subject: Search Confirmed — [Role] at [Company]",
            "Hi [Name],",
            "Great call today! Here's a summary of what we aligned on:",
            ("•", "Role: [Title]"),
            ("•", "Target profile: [2-sentence summary]"),
            ("•", "Salary range: [Range]"),
            ("•", "Target start date: [Date]"),
            ("•", "First profiles expected: [Date]"),
            "We'll be in touch the moment we have strong candidates to share. Feel free to reach out anytime.",
            "Best,\n[Your Name]",
        ]),
        ("EMAIL 3 — FIRST CANDIDATE PROFILES DELIVERED", [
            "Subject: [X] Candidates for [Role] — [Company]",
            "Hi [Name],",
            "Attached are [X] candidate profiles for the [Role] position. Each has been screened against your criteria.",
            "For each candidate I've included: current role, relevant experience, salary expectations, availability, and my assessment.",
            "Please review and let me know:",
            ("•", "Which candidates you'd like to interview"),
            ("•", "Any feedback on profile fit"),
            ("•", "Preferred interview format and availability"),
            "I'm available to schedule interviews within 24 hours of your feedback.",
            "Best,\n[Your Name]",
        ]),
        ("EMAIL 4 — WEEKLY STATUS UPDATE", [
            "Subject: Weekly Search Update — [Role] | [Company]",
            "Hi [Name],",
            "Quick update on your [Role] search:",
            ("•", "Candidates sourced this week: [X]"),
            ("•", "Screened and qualified: [X]"),
            ("•", "Profiles submitted to date: [X]"),
            ("•", "Interviews scheduled: [X]"),
            ("•", "Pipeline status: [On track / Adjusting criteria / Expanding search]"),
            "Next steps: [Specific actions]",
            "Let me know if you have any questions or feedback.",
            "Best,\n[Your Name]",
        ]),
    ])

doc("02_CLIENT_ONBOARDING/Job_Order_Intake_Form.docx",
    "Job Order Intake Form",
    "Recruiting Agency Operating System | Client Onboarding",
    [
        ("CLIENT INFORMATION", [
            ("•", "Company Name: _______________________________"),
            ("•", "Primary Contact Name: _______________________________"),
            ("•", "Title: _______________________________"),
            ("•", "Email: _______________________________"),
            ("•", "Phone: _______________________________"),
        ]),
        ("ROLE DETAILS", [
            ("•", "Job Title: _______________________________"),
            ("•", "Department: _______________________________"),
            ("•", "Reports To: _______________________________"),
            ("•", "Location: _______________________________"),
            ("•", "Remote / Hybrid / On-Site: _______________________________"),
            ("•", "Employment Type: [ ] Permanent  [ ] Contract  [ ] Contract-to-Hire"),
            ("•", "Target Start Date: _______________________________"),
        ]),
        ("COMPENSATION", [
            ("•", "Base Salary Range: $_______ to $_______"),
            ("•", "Bonus / Commission: _______________________________"),
            ("•", "Benefits Package: _______________________________"),
        ]),
        ("CANDIDATE REQUIREMENTS", [
            ("•", "Required Education: _______________________________"),
            ("•", "Required Years of Experience: _______________________________"),
            ("•", "Must-Have Skills (Top 5): _______________________________"),
            ("•", "Nice-to-Have Skills: _______________________________"),
            ("•", "Industry Background Required: _______________________________"),
            ("•", "Tools / Software Required: _______________________________"),
        ]),
        ("CULTURE & FIT", [
            ("•", "Describe your team culture in 3 words: _______________________________"),
            ("•", "What makes top performers succeed here? _______________________________"),
            ("•", "What type of candidate has NOT worked out before? _______________________________"),
        ]),
        ("INTERVIEW PROCESS", [
            ("•", "Number of interview rounds: _______"),
            ("•", "Round 1: _______________________________"),
            ("•", "Round 2: _______________________________"),
            ("•", "Round 3 (if applicable): _______________________________"),
            ("•", "Assessment required: [ ] Yes  [ ] No   Type: _______________________________"),
            ("•", "Decision timeline after final interview: _______________________________"),
        ]),
        ("SEARCH NOTES", [
            ("•", "Why is this role open? _______________________________"),
            ("•", "Previous search history (internal or agency): _______________________________"),
            ("•", "Competitors or companies to avoid sourcing from: _______________________________"),
            ("•", "Any other context we should know: _______________________________"),
        ]),
    ])

doc("02_CLIENT_ONBOARDING/Client_Kickoff_Call_Script.docx",
    "Client Kickoff Call Script",
    "Recruiting Agency Operating System | Client Onboarding",
    [
        ("BEFORE THE CALL", [
            ("•", "Review the signed service agreement and job order intake form"),
            ("•", "Research [Company]'s LinkedIn, Glassdoor, and recent news"),
            ("•", "Prepare initial thoughts on sourcing strategy"),
        ]),
        ("OPENING (0–3 min)", [
            "'[Name], thanks for making time. I've reviewed the job order form and I'm ready to dig in. The goal for today is to make sure I have everything I need to send you strong candidates quickly. Sound good?'",
        ]),
        ("ROLE DEEP-DIVE (3–15 min)", [
            ("•", "Walk me through a day in the life of this role."),
            ("•", "What would you say this person does in their first 30/60/90 days?"),
            ("•", "You listed [skill] as must-have — can you tell me more about how that's used?"),
            ("•", "Have you promoted someone into a similar role? What made them great?"),
            ("•", "Tell me about the team this person will join — size, dynamic, management style."),
        ]),
        ("INTERVIEW PROCESS ALIGNMENT (15–20 min)", [
            ("•", "Walk me through your ideal interview process."),
            ("•", "Who is the final decision maker?"),
            ("•", "How quickly can you move from first interview to offer if you find the right person?"),
            ("•", "What's caused searches to stall in the past?"),
        ]),
        ("COMMUNICATION CADENCE (20–25 min)", [
            "'Here's how we'll stay in sync: I'll send a weekly update every [day] with pipeline status. I'll contact you immediately when I have profiles ready to share. What's the best way to reach you for quick questions — email or text?'",
        ]),
        ("CLOSE (25–30 min)", [
            "'Any questions for me before we kick off? Great. I'll begin sourcing today and expect to have your first profiles by [date]. Talk soon.'",
        ]),
    ])

doc("02_CLIENT_ONBOARDING/Client_Expectations_Guide.docx",
    "Client Expectations Guide",
    "Recruiting Agency Operating System | Client Onboarding",
    [
        ("WHAT YOU CAN EXPECT FROM US", [
            ("•", "First candidate profiles delivered within [5–7] business days of kickoff"),
            ("•", "3–5 fully screened, qualified candidates per submission"),
            ("•", "Weekly search status updates every [Day]"),
            ("•", "24-hour response time on all communications"),
            ("•", "Interview scheduling handled within 24 hours of your feedback"),
            ("•", "Offer management and negotiation support"),
            ("•", "[90]-day replacement guarantee on all permanent placements"),
        ]),
        ("WHAT WE NEED FROM YOU", [
            ("•", "Feedback on submitted profiles within 3 business days"),
            ("•", "Interview availability within 5 business days of profile approval"),
            ("•", "Timely communication on offer decisions"),
            ("•", "One primary point of contact for the search"),
            ("•", "Advance notice of any changes to role requirements or timeline"),
        ]),
        ("TIMELINE EXPECTATIONS", [
            ("•", "Average time from kickoff to shortlist: 5–10 business days"),
            ("•", "Average time from shortlist to offer: 10–21 business days"),
            ("•", "Total average time-to-fill: 3–6 weeks (varies by role seniority and market)"),
            ("•", "Factors that can extend timelines: slow interview scheduling, changing role requirements, competitive candidate market"),
        ]),
        ("HOW TO GET THE BEST RESULTS", [
            ("•", "Be decisive: Top candidates are typically off the market within 7–10 days of entering a search"),
            ("•", "Provide specific feedback: 'Not enough experience in X' helps us adjust quickly"),
            ("•", "Move interviews quickly: Lengthy processes cause candidate drop-off"),
            ("•", "Keep us informed: Any changes to budget, scope, or timeline affect our strategy"),
        ]),
        ("GUARANTEE POLICY", [
            "All permanent placements include a [90]-day replacement guarantee. If the candidate leaves voluntarily or is terminated for performance within [90] days, we will conduct a replacement search at no additional fee.",
            "Guarantee exclusions: layoffs, role elimination, candidate misconduct undetected during screening, or mutual agreement to end employment.",
        ]),
    ])

doc("02_CLIENT_ONBOARDING/SOP_For_New_Clients.docx",
    "SOP For New Clients",
    "Recruiting Agency Operating System | Client Onboarding",
    [
        ("DAY 1 — AGREEMENT SIGNED", [
            ("•", "Send Welcome Email with job order intake form link"),
            ("•", "Create client record in CRM"),
            ("•", "Schedule kickoff call (within 48 hours)"),
            ("•", "Share Expectations Guide"),
        ]),
        ("DAY 2 — INTAKE FORM RECEIVED", [
            ("•", "Review intake form thoroughly"),
            ("•", "Research company on LinkedIn, Glassdoor, website"),
            ("•", "Draft initial sourcing strategy and boolean search strings"),
            ("•", "Identify 3–5 top job boards/sources for this role"),
        ]),
        ("DAY 2–3 — KICKOFF CALL", [
            ("•", "Complete kickoff call using Kickoff Call Script"),
            ("•", "Clarify any gaps in intake form"),
            ("•", "Confirm communication cadence and first delivery date"),
            ("•", "Send post-kickoff summary email same day"),
        ]),
        ("DAY 3–7 — ACTIVE SOURCING", [
            ("•", "Launch LinkedIn Recruiter search"),
            ("•", "Post to relevant job boards if applicable"),
            ("•", "Begin outreach to passive candidates"),
            ("•", "Screen inbound applications"),
            ("•", "Conduct phone screens with qualified candidates"),
        ]),
        ("DAY 7–10 — FIRST SUBMISSION", [
            ("•", "Select top 3–5 candidates from pipeline"),
            ("•", "Prepare candidate profiles (summary, experience, salary, availability)"),
            ("•", "Send profiles with cover note and assessment"),
            ("•", "Follow up within 24 hours if no response"),
        ]),
        ("ONGOING — WEEKLY CADENCE", [
            ("•", "Send weekly update every [Day]"),
            ("•", "Schedule all requested interviews within 24 hours"),
            ("•", "Gather structured feedback after each interview"),
            ("•", "Adjust sourcing strategy based on feedback"),
        ]),
    ])

print("✓ 02_CLIENT_ONBOARDING DOCX complete")

# ── 03_CANDIDATE_SOURCING ─────────────────────────────────────────────────────
doc("03_CANDIDATE_SOURCING/LinkedIn_Sourcing_Playbook.docx",
    "LinkedIn Sourcing Playbook",
    "Recruiting Agency Operating System | Candidate Sourcing",
    [
        ("LINKEDIN RECRUITER SEARCH STRATEGY", [
            "Use LinkedIn Recruiter (or Sales Navigator as an alternative) for the most powerful sourcing. These steps work with the free search as well, though with fewer filters.",
        ]),
        ("STEP 1 — DEFINE YOUR SEARCH CRITERIA", [
            ("•", "Job title keywords (use variations: 'Sales Manager', 'Head of Sales', 'Director of Sales')"),
            ("•", "Industry filters"),
            ("•", "Geography (city, radius, remote)"),
            ("•", "Years of experience"),
            ("•", "Company size (target companies similar to your client)"),
            ("•", "Skills keywords"),
        ]),
        ("STEP 2 — BOOLEAN SEARCH STRINGS", [
            "Build boolean strings to increase precision. See Boolean Search Library document for full library.",
            ("•", "Basic: 'Sales Manager' AND 'SaaS' AND 'B2B'"),
            ("•", "Exclude: 'Sales Manager' AND 'SaaS' NOT 'Recruiter'"),
            ("•", "Or variations: ('Sales Manager' OR 'Account Executive') AND 'enterprise'"),
        ]),
        ("STEP 3 — PROFILE EVALUATION CHECKLIST", [
            ("•", "Current title matches or is one level below target"),
            ("•", "Relevant industry experience in current or previous roles"),
            ("•", "Tenure: 2+ years in most recent role (avoid job hoppers unless explained)"),
            ("•", "Profile completeness indicates active job seeker or open to opportunities"),
            ("•", "Mutual connections or shared groups (increases response rate)"),
            ("•", "Recent activity on LinkedIn (posts, likes, comments = higher engagement)"),
        ]),
        ("STEP 4 — OUTREACH CADENCE", [
            ("•", "Connection request with short note (Day 1)"),
            ("•", "If accepted, send intro message within 24 hours"),
            ("•", "Follow up if no response after 5 days"),
            ("•", "Final follow-up at Day 10; move on if no reply"),
        ]),
        ("PROFILE OPEN-TO-WORK SIGNALS", [
            ("•", "#OpenToWork frame on profile photo"),
            ("•", "Career Interests settings visible to recruiters"),
            ("•", "Profile updated recently with new skills or summary"),
            ("•", "Connections with multiple recruiters in your network"),
        ]),
    ])

doc("03_CANDIDATE_SOURCING/Boolean_Search_Library.docx",
    "Boolean Search Library",
    "Recruiting Agency Operating System | Candidate Sourcing",
    [
        ("HOW TO USE THIS LIBRARY", [
            "Copy these strings directly into LinkedIn Recruiter, Google (for X-Ray search), or any ATS. Replace [brackets] with role-specific terms.",
        ]),
        ("SALES ROLES", [
            ("•", "AE / Account Executive: ('Account Executive' OR 'AE' OR 'Sales Representative') AND ('SaaS' OR 'B2B' OR 'enterprise')"),
            ("•", "Sales Manager: ('Sales Manager' OR 'Head of Sales') AND ('team' OR 'quota' OR 'revenue') NOT 'recruiting'"),
            ("•", "VP of Sales: ('VP of Sales' OR 'Vice President of Sales' OR 'Chief Revenue Officer' OR 'CRO')"),
        ]),
        ("ENGINEERING / TECH ROLES", [
            ("•", "Software Engineer: ('Software Engineer' OR 'Software Developer') AND ('Python' OR 'Java' OR 'React') NOT 'intern'"),
            ("•", "DevOps: ('DevOps' OR 'Site Reliability' OR 'SRE') AND ('AWS' OR 'Azure' OR 'GCP')"),
            ("•", "Data Scientist: ('Data Scientist' OR 'ML Engineer' OR 'Machine Learning') AND ('Python' OR 'TensorFlow' OR 'PyTorch')"),
        ]),
        ("MARKETING ROLES", [
            ("•", "Digital Marketing: ('Digital Marketing Manager' OR 'Growth Manager') AND ('SEO' OR 'SEM' OR 'paid media')"),
            ("•", "Content: ('Content Strategist' OR 'Content Manager') AND ('B2B' OR 'SaaS' OR 'editorial')"),
        ]),
        ("FINANCE & ACCOUNTING", [
            ("•", "CFO: ('CFO' OR 'Chief Financial Officer' OR 'VP Finance') AND ('Series' OR 'startup' OR 'public company')"),
            ("•", "Controller: ('Controller' OR 'Accounting Manager') AND ('CPA' OR 'GAAP' OR 'financial reporting')"),
        ]),
        ("GOOGLE X-RAY SEARCH (for free sourcing)", [
            "Search Google with: site:linkedin.com/in [job title] [city] [skill]",
            ("•", "Example: site:linkedin.com/in 'account executive' 'San Francisco' 'Salesforce'"),
            ("•", "Example: site:linkedin.com/in 'software engineer' 'remote' 'Python' 'Django'"),
        ]),
        ("GITHUB X-RAY (for engineers)", [
            ("•", "site:github.com [language] [location] stars:>10"),
            ("•", "Example: site:github.com Python Austin 'open source'"),
        ]),
    ])

doc("03_CANDIDATE_SOURCING/Job_Board_Strategy_Guide.docx",
    "Job Board Strategy Guide",
    "Recruiting Agency Operating System | Candidate Sourcing",
    [
        ("JOB BOARD SELECTION BY ROLE TYPE", [
            "Not all job boards are equal. Match your posting strategy to the role type and candidate level.",
        ]),
        ("GENERAL PROFESSIONAL ROLES", [
            ("•", "LinkedIn Jobs: Best for professional and technical roles, $[X]/post or subscription"),
            ("•", "Indeed: Highest traffic, good for volume hiring, cost-per-click model"),
            ("•", "ZipRecruiter: Good for mid-market roles, broad distribution"),
        ]),
        ("TECH / ENGINEERING", [
            ("•", "Stack Overflow Jobs: Developers trust this platform; good quality applicants"),
            ("•", "Dice: US-focused tech roles, strong for contract/IT positions"),
            ("•", "AngelList / Wellfound: Startup-focused engineering roles"),
            ("•", "GitHub Jobs: Passive developer community"),
        ]),
        ("EXECUTIVE SEARCH", [
            ("•", "LinkedIn Recruiter: Primary tool for executive and passive candidate outreach"),
            ("•", "ExecuNet: Senior executive-focused network"),
            ("•", "BlueSteps (AESC): Global executive search platform"),
        ]),
        ("SPECIALIZED NICHES", [
            ("•", "Behance / Dribbble: Creative and design roles"),
            ("•", "Doximity: Healthcare professionals"),
            ("•", "eFinancialCareers: Finance and banking"),
            ("•", "Lawjobs: Legal professionals"),
            ("•", "Jobvite Marketplace: Distributed through aggregators"),
        ]),
        ("JOB POSTING BEST PRACTICES", [
            ("•", "Write the title candidates search for — not internal titles"),
            ("•", "Lead with what the candidate gets, not just what you need"),
            ("•", "Include salary range (increases apply rate by 30–40%)"),
            ("•", "Keep requirements list to 5–7 must-haves; avoid 'wish list' JDs"),
            ("•", "Mobile-optimize: 60%+ of applications come from mobile devices"),
            ("•", "Refresh postings every 2 weeks to stay at top of results"),
        ]),
    ])

doc("03_CANDIDATE_SOURCING/Passive_Candidate_Outreach.docx",
    "Passive Candidate Outreach",
    "Recruiting Agency Operating System | Candidate Sourcing",
    [
        ("UNDERSTANDING PASSIVE CANDIDATES", [
            "70–80% of the workforce is passively employed — not actively looking but open to the right opportunity. These are typically the highest performers. Reaching them requires a different approach than active job seekers.",
        ]),
        ("LINKEDIN OUTREACH MESSAGES", [
            ("•", "Message 1 — Curiosity Hook: 'Hi [Name], I work with [niche] companies to match them with top [role] talent. I came across your profile and thought you'd be worth a conversation — not necessarily about a job, more about where the market is heading. Are you open to a 15-minute call?'"),
            ("•", "Message 2 — Opportunity Specific: 'Hi [Name], I'm working on an exciting [role] opportunity with a [description] company. Comp is $[range] + [perks]. Given your background in [specific skill/company], I thought you might find it interesting. Confidential for now — want the details?'"),
            ("•", "Message 3 — Referral Ask: 'Hi [Name], I'm looking for a strong [role] for a [industry] client. You might not be looking, but do you know anyone in your network who might be? Happy to pay a referral fee if you make an intro that leads to a placement.'"),
        ]),
        ("EMAIL OUTREACH TO PASSIVE CANDIDATES", [
            ("•", "Subject line options: 'Confidential Opportunity — [Role]' / '[Company type] looking for someone with your background' / 'Quick question about your career'"),
            ("•", "Keep emails under 100 words"),
            ("•", "Lead with what makes this opportunity unique"),
            ("•", "Make the ask specific and easy: 15-minute call, not 'let me know if interested'"),
        ]),
        ("WHAT PASSIVE CANDIDATES CARE ABOUT", [
            ("•", "Compensation uplift (typically need 15–20% increase to move)"),
            ("•", "Career advancement / title upgrade"),
            ("•", "Better culture or leadership"),
            ("•", "Flexibility (remote, hybrid, hours)"),
            ("•", "Learning and growth opportunities"),
            ("•", "Mission or product they believe in"),
        ]),
        ("TIPS TO INCREASE RESPONSE RATES", [
            ("•", "Personalize the first line — reference their specific experience or achievement"),
            ("•", "Keep it short — 3–5 sentences max"),
            ("•", "Mention compensation range upfront"),
            ("•", "Include company name if it's a strong brand; omit if small/unknown"),
            ("•", "Send Tuesday–Thursday between 7–9am or 5–7pm"),
        ]),
    ])

doc("03_CANDIDATE_SOURCING/Candidate_Sourcing_Checklist.docx",
    "Candidate Sourcing Checklist",
    "Recruiting Agency Operating System | Candidate Sourcing",
    [
        ("PRE-SEARCH SETUP", [
            ("•", "[ ] Job order intake form reviewed and all fields complete"),
            ("•", "[ ] Kickoff call completed with client"),
            ("•", "[ ] Boolean search strings drafted"),
            ("•", "[ ] Target companies identified"),
            ("•", "[ ] Job boards selected for this role type"),
            ("•", "[ ] Job posting written and live (if applicable)"),
        ]),
        ("ACTIVE SOURCING CHECKLIST", [
            ("•", "[ ] LinkedIn Recruiter search live"),
            ("•", "[ ] Indeed / ZipRecruiter posting active"),
            ("•", "[ ] Niche job board posting active"),
            ("•", "[ ] Internal database searched"),
            ("•", "[ ] Referral outreach sent to placed candidates in similar roles"),
            ("•", "[ ] Google X-Ray search performed"),
        ]),
        ("CANDIDATE EVALUATION CHECKLIST", [
            ("•", "[ ] Experience matches minimum requirements"),
            ("•", "[ ] Location / remote match confirmed"),
            ("•", "[ ] Salary expectations within client range"),
            ("•", "[ ] Availability aligns with target start date"),
            ("•", "[ ] No obvious red flags (unexplained gaps, frequent job changes)"),
            ("•", "[ ] Culture fit indicators assessed"),
        ]),
        ("PHONE SCREEN CHECKLIST", [
            ("•", "[ ] Current role and responsibilities confirmed"),
            ("•", "[ ] Compensation expectations confirmed"),
            ("•", "[ ] Notice period / availability confirmed"),
            ("•", "[ ] Key skills verified with specific examples"),
            ("•", "[ ] Motivation for looking / openness to move confirmed"),
            ("•", "[ ] Interview process explained and candidate is prepared"),
            ("•", "[ ] Candidate interest level rated 1–10"),
        ]),
        ("SUBMISSION CHECKLIST", [
            ("•", "[ ] Candidate profile written (current role, relevant experience, compensation, availability)"),
            ("•", "[ ] Recruiter assessment note included"),
            ("•", "[ ] Profiles reviewed for typos and formatting"),
            ("•", "[ ] Submitted to client via email with clear subject line"),
            ("•", "[ ] Candidate notified their profile has been submitted"),
        ]),
    ])

print("✓ 03_CANDIDATE_SOURCING DOCX complete")
print("PART 1 DONE")
