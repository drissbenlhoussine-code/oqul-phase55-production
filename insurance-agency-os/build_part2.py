#!/usr/bin/env python3
"""Insurance Agency OS - Part 2: Folders 04-07 + XLSX files"""
import os
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/insurance-agency-os/Ultimate_Insurance_Agency_Operating_System/"
NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"

def hf(h): return PatternFill("solid", fgColor=h)
def bf(bold=True,sz=11,color="000000"): return Font(bold=bold,size=sz,color=color)
def al(h="center",v="center"): return Alignment(horizontal=h,vertical=v,wrap_text=True)
def thin():
    s=Side(style='thin',color='CCCCCC'); return Border(left=s,right=s,top=s,bottom=s)
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

# ─── 04_CLAIMS_SUPPORT ─────────────────────────────────────────────────────────
p04 = "04_CLAIMS_SUPPORT/"

doc(p04+"First_Notice_Of_Loss_SOP.docx",
    "First Notice of Loss (FNOL) SOP",
    "Insurance Agency OS | Claims Reporting Protocol",
    [
        ("What to Do When a Client Reports a Claim", [
            "When a client calls to report a loss, your response in the first 5 minutes sets the tone for the entire claims experience. Be empathetic, take immediate action, and guide them through every step.",
        ]),
        ("FNOL Phone Script", [
            '"[Name], I\'m so sorry to hear this happened. Let\'s make sure we get this taken care of right away. First — are you and your family safe? [...] Good. Now, here\'s what we\'re going to do..."',
            '"I\'m going to report this claim to [Carrier] right now on your behalf. I\'ll need a few pieces of information from you — can you tell me [Date/Time/Description]? [...] Perfect. I\'m filing this as we speak. Your claim number will be [Number]. A claims adjuster will contact you within [24-48 hours]."',
            '"Here\'s my personal cell number — please call me if you have any issues with the claims process. I\'m your advocate throughout this entire process."',
        ]),
        ("Information to Collect at FNOL", [
            ("•", "Date and time of loss"),
            ("•", "Location of loss"),
            ("•", "Description of what happened (in client's own words)"),
            ("•", "Extent of damage — property, vehicles, injuries"),
            ("•", "Other parties involved (for auto accidents: name, insurance, license plate)"),
            ("•", "Police report number (if applicable)"),
            ("•", "Photos taken by client at the scene"),
            ("•", "Temporary repairs needed to prevent further damage"),
        ]),
        ("After the Claim is Filed", [
            ("•", "Follow up with client within 24 hours to confirm adjuster contact was made"),
            ("•", "Check in at 7 days if claim is still open"),
            ("•", "Advocate with the carrier if the client encounters delays or disputes"),
            ("•", "Document all claim contacts in the client CRM file"),
            ("•", "Send a 'Claim Resolution Follow-Up' note when the claim closes"),
        ]),
        ("Claims Advocacy — When to Step In", [
            ("•", "When the carrier is taking longer than the promised timeline to respond"),
            ("•", "When the client believes the settlement offer is unfair"),
            ("•", "When the client is confused about coverage being applied"),
            ("•", "When a claim is being denied and you believe coverage exists"),
            ("•", "Always: Your role is to educate and advocate — not to promise outcomes"),
        ]),
    ])

doc(p04+"Claims_Advocacy_Guide.docx",
    "Claims Advocacy Guide",
    "Insurance Agency OS | Representing Your Clients Through the Claims Process",
    [
        ("Your Role in the Claims Process", [
            "As an independent agent, you are uniquely positioned to serve as your client's advocate during the claims process. Unlike direct-to-consumer models, clients who purchase through independent agents have a professional in their corner who knows the policy, knows the carrier, and can escalate on their behalf.",
        ]),
        ("Understanding the Claims Lifecycle", [
            ("•", "FNOL (First Notice of Loss): Client reports the loss — to you or directly to carrier"),
            ("•", "Assignment: Carrier assigns an adjuster and sends acknowledgment"),
            ("•", "Investigation: Adjuster reviews the loss, inspects property, interviews parties"),
            ("•", "Coverage Determination: Carrier determines if the loss is covered"),
            ("•", "Valuation: Adjuster determines the value of the covered loss"),
            ("•", "Payment/Resolution: Carrier issues payment or denial"),
            ("•", "Closure: Claim is closed; follow up with client"),
        ]),
        ("Escalation Paths When Claims Stall", [
            "Level 1: Call the assigned adjuster directly. Get a specific timeline commitment.",
            "Level 2: Request the adjuster's supervisor. Explain the delay and its impact on your client.",
            "Level 3: Contact your agency's carrier representative/underwriter. They have influence over claims handling.",
            "Level 4: File a complaint with the state insurance department. This escalates within the carrier immediately.",
            "Level 5: Recommend public adjuster or insurance attorney for complex, disputed claims.",
        ]),
        ("Claim Denial Review Process", [
            "When a claim is denied, take these steps:",
            ("•", "Request the denial letter in writing with full explanation and policy citations"),
            ("•", "Read the policy language yourself — identify potential ambiguities"),
            ("•", "Research case law or regulatory guidance on the coverage interpretation"),
            ("•", "Write a formal letter of appeal with supporting documentation"),
            ("•", "If appropriate, recommend the client seek a public adjuster or attorney"),
        ]),
        ("Post-Claim Client Communication", [
            '"[Name], I just wanted to follow up now that your claim has been resolved. How do you feel about how the process went? [...] Is there anything I can clarify about how the claim was handled?"',
            '"I also want to take a moment to review your coverage in light of this claim. Sometimes a loss reveals a gap or an opportunity to strengthen your protection going forward. Would you have 15 minutes for a quick review?"',
        ]),
    ])

doc(p04+"Claims_Communication_Templates.docx",
    "Claims Communication Templates",
    "Insurance Agency OS | Client Emails and Scripts for Every Claims Scenario",
    [
        ("Auto Accident — Initial Contact Email", [
            "Subject: Your Auto Claim — We're Here to Help",
            "Hi [Name],",
            "I'm so sorry to hear about your accident. I want to make sure this claims process goes as smoothly as possible for you.",
            "Here's what to expect over the next few days:",
            "Your claim number is: [Number]",
            "Your assigned adjuster is: [Name] at [Phone/Email]",
            "Estimated timeline: An adjuster will contact you within 24-48 hours.",
            "If you need a rental vehicle, here's how to arrange it: [Instructions]",
            "Please don't hesitate to call me directly at [Phone] if you have any questions or encounter any issues. I'm your advocate throughout this entire process.",
            "[Signature]",
        ]),
        ("Property Loss — Initial Contact Email", [
            "Subject: Your Property Claim — Important Next Steps",
            "Hi [Name],",
            "I understand how stressful property damage can be, and I want you to know we're on top of this.",
            "Important reminder: If there is an active risk of further damage, you may make temporary repairs to prevent it — just save all receipts, as these costs may be reimbursable.",
            "Please DO NOT dispose of damaged items until the adjuster has had a chance to inspect them.",
            "Your claim number is: [Number]",
            "Expected adjuster contact: Within [24-72] hours",
            "I'll be checking in with you in 48 hours to make sure you've been contacted. Don't hesitate to reach out before then.",
            "[Signature]",
        ]),
        ("Claim Delay — Follow-Up Email", [
            "Subject: Following Up on Your [Claim Type] Claim",
            "Hi [Name],",
            "I wanted to check in on the status of your claim (#[Number]). I understand it's been [X days] since we filed, and I want to make sure things are moving forward.",
            "I've reached out to [Carrier] on your behalf today and was told: [Update]",
            "If you have not heard from your adjuster by [Date], please let me know immediately and I will escalate this directly to [Carrier's] management team.",
            "Thank you for your patience — I'm here to make sure this gets resolved properly.",
            "[Signature]",
        ]),
    ])

print("✓ 04_CLAIMS_SUPPORT complete")

# ─── 05_CLIENT_COMMUNICATION ───────────────────────────────────────────────────
p05 = "05_CLIENT_COMMUNICATION/"

doc(p05+"Client_Email_Templates.docx",
    "Client Email Templates",
    "Insurance Agency OS | Professional Email Library for Every Situation",
    [
        ("Welcome Email — New Client", [
            "Subject: Welcome to [Agency Name], [First Name]!",
            "Hi [Name],",
            "Welcome to [Agency Name] — I'm thrilled to have you as a client!",
            "Here's what you can expect from me:",
            "• A confirmation of your coverage will be in your inbox within 24 hours",
            "• I'll reach out at renewal time to review your policy and rates",
            "• You can reach me anytime at [Phone] or [Email] — I'm always here",
            "One request: if you ever need to make a change to your policy or have a question, please reach out to me directly rather than calling the carrier. I can often resolve things faster and make sure your interests are protected.",
            "Thank you for trusting [Agency Name] with your insurance needs!",
            "[Signature]",
        ]),
        ("Renewal Reminder Email", [
            "Subject: Your [Policy Type] Policy Renews in 30 Days — Here's What to Know",
            "Hi [Name],",
            "Your [policy type] policy with [Carrier] renews on [Date]. I've been reviewing your coverage and want to touch base before your renewal.",
            "Here's a quick summary: [Coverage Details / Rate Change Note]",
            "I'd love to schedule a quick 15-minute annual review call to make sure your coverage still fits your needs and that you're getting the best available rate.",
            "Are you free for a quick call on [Suggested Date]? Or pick a time that works for you: [Calendly Link]",
            "[Signature]",
        ]),
        ("Referral Thank-You Email", [
            "Subject: Thank You for Referring [Name]!",
            "Hi [Name],",
            "I just wanted to send a quick note to say THANK YOU for referring [Referral Name] to me. Referrals are the greatest compliment I can receive, and I promise to take exceptional care of them.",
            "I've already reached out and we have a call scheduled for [Date]. I'll keep you posted on how it goes!",
            "As a token of my appreciation, I'm [sending you a gift card / making a donation in your name / inviting you to our client event]. Look for a note in the mail!",
            "Thanks again — you're the best!",
            "[Signature]",
        ]),
        ("Holiday / Seasonal Email", [
            "Subject: Happy [Holiday], [Name]!",
            "Hi [Name],",
            "As [holiday season] approaches, I wanted to take a moment to reach out and wish you and your family a wonderful [holiday].",
            "It's been a privilege serving your insurance needs this year, and I'm grateful for the trust you've placed in [Agency Name].",
            "Quick reminder: if you have any holiday travel plans, new purchases, or guests staying with you, give me a quick call — sometimes temporary coverage adjustments make sense.",
            "Wishing you a safe and joyful holiday season!",
            "[Signature]",
        ]),
    ])

doc(p05+"Text_Message_Templates.docx",
    "Text Message Templates",
    "Insurance Agency OS | Professional SMS Communication Scripts",
    [
        ("Lead Follow-Up Texts", [
            "Text 1 — Initial Lead Response (within 5 minutes):",
            '"Hi [Name], this is [Agent] from [Agency]. I saw your quote request and wanted to reach out right away. Do you have 5 minutes for a quick call? 📞"',
            "Text 2 — No-Response Follow-Up (24 hours later):",
            '"Hey [Name] — [Agent] from [Agency] here. Just following up on your insurance quote. Happy to text back and forth if that\'s easier. What type of coverage were you looking for?"',
            "Text 3 — Final Attempt (Day 5):",
            '"Hi [Name], last follow-up from [Agent] at [Agency]. I don\'t want to bug you — but if you\'re still looking for insurance quotes, I\'m here! Call, text, or email anytime. Have a great day 😊"',
        ]),
        ("Client Service Texts", [
            "Policy Change Confirmation:",
            '"Hi [Name], your [policy change] has been processed. Effective [Date]. Let me know if you have any questions! — [Agent], [Agency]"',
            "Claim Filed Confirmation:",
            '"[Name], your claim has been filed. Claim # [Number]. Adjuster will contact you within 24-48 hrs. I\'m here if you need anything. — [Agent]"',
            "Renewal Reminder Text:",
            '"Hi [Name]! Your [policy type] renews [Date]. Quick review call this week? 15 mins to make sure everything still fits. Reply YES and I\'ll send a link to schedule! — [Agent]"',
            "Annual Review Invitation:",
            '"Hi [Name], it\'s been a year since we set up your policy! Time for a quick 15-minute review. Lots has changed in the market — I may be able to save you money. Interested? — [Agent]"',
        ]),
    ])

doc(p05+"Phone_Script_Library.docx",
    "Phone Script Library",
    "Insurance Agency OS | Outbound and Inbound Call Scripts",
    [
        ("Inbound Lead Call — Personal Lines", [
            '"Thank you for calling [Agency Name], this is [Agent]. How can I help you today?"',
            '"Great — so you\'re looking for [coverage type]. I can definitely help with that. Let me ask you a few quick questions to make sure I find the best options for you. Is that okay?"',
            "Key discovery questions:",
            ("•", "'What is your current insurance situation?'"),
            ("•", "'Are you looking to bundle home and auto together?'"),
            ("•", "'When does your current policy renew?'"),
            ("•", "'What's most important to you — price, coverage quality, or both?'"),
        ]),
        ("Inbound Call — Existing Client", [
            '"[Agency Name], this is [Agent], how can I help you?"',
            '"Hi [Name]! Great to hear from you. What can I do for you today?"',
            "If they're calling about a claim: Use the FNOL script from 04_CLAIMS_SUPPORT",
            "If they're calling about a bill: 'I\'d love to help with that — let me pull up your account. Can I confirm your policy number or date of birth?'",
            "If they're calling about a change: 'Absolutely, let me get the details and we\'ll get that taken care of right away.'",
        ]),
        ("Outbound Renewal Call", [
            '"Hi [Name], this is [Agent] from [Agency]. I\'m calling because your [policy type] renews in [X weeks] and I want to do a quick annual review before it auto-renews. Do you have about 10 minutes?"',
            '"Great. I want to make sure your coverage still makes sense for your situation and that you\'re getting the best available rate. A lot can change in a year — so let me ask you a few questions..."',
        ]),
    ])

doc(p05+"Client_Newsletter_Template.docx",
    "Client Newsletter Template",
    "Insurance Agency OS | Monthly Agency Newsletter Framework",
    [
        ("Newsletter Structure", [
            ("•", "Header: Agency name, logo, 'Monthly Insurance Insider' or similar title"),
            ("•", "Personal Note from Agent (3-4 sentences — personal and warm)"),
            ("•", "Featured Article: Insurance education topic (300-400 words)"),
            ("•", "Quick Tips Section: 3 bullet-point insurance tips"),
            ("•", "Client Spotlight or Community Section"),
            ("•", "Call to Action: 'Schedule your annual review' or 'Share with a friend'"),
            ("•", "Footer: Contact information, social links, unsubscribe"),
        ]),
        ("Newsletter Content Calendar — 12 Months", [
            ("•", "January: New Year policy review — 'Start the year with the right coverage'"),
            ("•", "February: Life insurance awareness — 'Have you protected your family?'"),
            ("•", "March: Spring home maintenance checklist — 'Protect your biggest investment'"),
            ("•", "April: Tax season tip — 'Can you deduct home insurance on your taxes?'"),
            ("•", "May: Storm preparation guide — 'Is your property ready for severe weather?'"),
            ("•", "June: Summer travel tips — 'Does your policy cover you on vacation?'"),
            ("•", "July: Home security and liability — 'Pools, trampolines, and your insurance'"),
            ("•", "August: Teen driver safety — 'What parents need to know about insuring young drivers'"),
            ("•", "September: Business insurance for home-based workers"),
            ("•", "October: Cyber security and identity theft coverage options"),
            ("•", "November: Holiday hosting liability — 'What happens if someone is injured at your party?'"),
            ("•", "December: Year-in-review, thank-you message, New Year renewal reminder"),
        ]),
        ("Sample Article — 'What Is an Independent Insurance Agent?'", [
            "When you buy insurance through an independent agent, you're doing something most consumers don't realize: you're hiring a professional to shop the entire market on your behalf.",
            "Unlike captive agents who represent only one company, independent agents like [Agency Name] work with dozens of insurance carriers. That means when your policy renews, we can compare rates across multiple options to make sure you're still getting the best deal.",
            "We also serve as your advocate when things go wrong. If you have a claim, we help you navigate the process, escalate when needed, and make sure you're treated fairly.",
            "The best part? Our service costs you nothing extra — we're compensated by the carriers, and our goal is always to find YOU the best combination of coverage and value.",
        ]),
    ])

print("✓ 05_CLIENT_COMMUNICATION complete")

# ─── 06_COMPLIANCE_LICENSING ───────────────────────────────────────────────────
p06 = "06_COMPLIANCE_LICENSING/"

doc(p06+"E_and_O_Best_Practices.docx",
    "E&O (Errors & Omissions) Best Practices Guide",
    "Insurance Agency OS | Protecting Yourself from Professional Liability Claims",
    [
        ("What Is E&O Insurance?", [
            "Errors & Omissions (E&O) insurance protects you and your agency if a client claims financial harm due to a mistake, omission, or failure to recommend appropriate coverage. Every licensed insurance agent should carry E&O coverage — it's both a professional necessity and often a carrier appointment requirement.",
        ]),
        ("Top Causes of E&O Claims in Insurance Agencies", [
            ("•", "Failure to obtain coverage the client requested"),
            ("•", "Binding or quoting incorrect coverage amounts"),
            ("•", "Missing a renewal and leaving a client without coverage"),
            ("•", "Failure to advise client of a coverage gap or available endorsement"),
            ("•", "Processing an endorsement incorrectly or late"),
            ("•", "Client claims they were not informed of a policy exclusion"),
            ("•", "Incorrect named insured on the policy"),
        ]),
        ("E&O Prevention Checklist", [
            ("•", "Document EVERYTHING: Every client conversation, coverage recommendation, and client decision"),
            ("•", "Coverage declination form: If a client declines recommended coverage, get it in writing"),
            ("•", "Binding confirmation: Always confirm coverage in writing before assuming it's in force"),
            ("•", "Renewal diarization: Never let a policy expire without proactive contact"),
            ("•", "Application review: Verify all information before submitting to carrier"),
            ("•", "Policy delivery: Confirm client received their policy and declarations page"),
        ]),
        ("Coverage Declination Documentation", [
            "Use this language whenever a client declines a coverage recommendation:",
            '"We discussed the following coverage options with [Client Name] on [Date]: [Coverage Type] — [Client] declined this coverage. [Client] was advised of the risks of not carrying this coverage, including [specific risks]."',
            "Have the client sign and date this documentation. Store in the client file.",
        ]),
        ("E&O Incident Response", [
            "If you receive a complaint or potential E&O claim:",
            ("•", "Do NOT admit fault or make any promises — contact your E&O carrier immediately"),
            ("•", "Preserve all documentation: emails, notes, applications, policies"),
            ("•", "Do not discuss the matter with the claimant without your E&O carrier's guidance"),
            ("•", "Cooperate fully with your E&O carrier's investigation"),
            ("•", "Document the incident with a detailed timeline of events"),
        ]),
    ])

doc(p06+"Compliance_Checklist.docx",
    "Agency Compliance Checklist",
    "Insurance Agency OS | Annual Compliance Review for Independent Agencies",
    [
        ("License Maintenance", [
            ("•", "All agent licenses current and in good standing in all states you write business"),
            ("•", "Continuing education credits completed and documented"),
            ("•", "License renewal dates logged in your calendar with 90-day advance reminder"),
            ("•", "All licensed staff verified — no lapsed licenses"),
            ("•", "Non-resident license status confirmed for states you write in"),
        ]),
        ("Carrier Appointments", [
            ("•", "All carrier appointment agreements reviewed for compliance requirements"),
            ("•", "No writing in lines/states for which you're not appointed"),
            ("•", "Appointment renewal dates tracked"),
            ("•", "Any terminated appointments properly communicated to affected clients"),
        ]),
        ("Agency Operations", [
            ("•", "E&O coverage current — limits adequate for your book size"),
            ("•", "Premium trust account reconciled monthly"),
            ("•", "Client funds never commingled with agency operating funds"),
            ("•", "Client data security measures in place (encryption, access controls, backup)"),
            ("•", "Privacy policy updated and available to clients"),
        ]),
        ("Sales and Marketing Compliance", [
            ("•", "No misrepresentation in advertising — all claims factual and verifiable"),
            ("•", "Carrier logos and names used only as permitted under appointment agreements"),
            ("•", "Social media and website reviewed for compliance with insurance advertising rules"),
            ("•", "Testimonials reviewed for compliance (no guaranteed outcomes claims)"),
            ("•", "CAN-SPAM / TCPA compliance for email and text marketing"),
        ]),
        ("Claims and Service Compliance", [
            ("•", "Claims handling procedures documented and followed"),
            ("•", "No unauthorized claims adjusting or settlement negotiations"),
            ("•", "Client complaints logged, responded to, and resolved within required timeframes"),
            ("•", "All complaints reported to state insurance department if required"),
        ]),
    ])

doc(p06+"State_Licensing_Guide.docx",
    "State Licensing Guide",
    "Insurance Agency OS | Multi-State Licensing for Independent Agents",
    [
        ("Resident vs. Non-Resident Licenses", [
            ("•", "Resident license: Required in your home state — grants you authority to transact insurance there"),
            ("•", "Non-resident license: Required in any other state where you transact insurance"),
            ("•", "Reciprocity: Most states offer reciprocal licensing — if you pass your resident exam, other states grant a license without requiring another exam"),
            ("•", "The NIPR (National Insurance Producer Registry) is the central platform for managing multi-state licenses"),
        ]),
        ("Common License Lines of Authority", [
            ("•", "Property & Casualty (P&C): Homeowner, auto, commercial lines"),
            ("•", "Life & Health (L&H): Life insurance, disability, health insurance"),
            ("•", "Variable Products: Requires FINRA Series 6 or 7 in addition to state license"),
            ("•", "Surplus Lines: Required to access E&S (non-admitted) carriers"),
            ("•", "Title Insurance: Separate license in most states"),
        ]),
        ("Continuing Education Requirements", [
            ("•", "Most states require 24 hours of CE every 2-year license period"),
            ("•", "Ethics CE is mandatory in most states (usually 3-6 hours)"),
            ("•", "Life insurance-specific CE may be required for L&H licensees"),
            ("•", "Track CE credits in your state's producer portal or through your CE provider"),
            ("•", "Approved CE providers: The National Alliance, CPCU Society, WebCE, ExamFX"),
        ]),
        ("License Maintenance Best Practices", [
            ("•", "Set calendar reminders 90 days before each license expiration"),
            ("•", "Keep a spreadsheet of all licenses: state, license number, type, expiration date"),
            ("•", "Verify license status after any CE submission — processing can take days"),
            ("•", "Always renew on time — a lapsed license = E&O exposure and potential disciplinary action"),
        ]),
    ])

doc(p06+"Carrier_Appointment_SOP.docx",
    "Carrier Appointment SOP",
    "Insurance Agency OS | Getting Appointed and Maintaining Carrier Relationships",
    [
        ("Understanding Carrier Appointments", [
            "A carrier appointment is an agreement between you and an insurance company that authorizes you to sell their products. Without an appointment, you cannot legally bind coverage with that carrier. Managing your appointments is critical to your market access and business viability.",
        ]),
        ("How to Get Appointed", [
            ("•", "Research the carrier's appointment process on their agent portal or contact their producer development team"),
            ("•", "Submit an appointment application with: E&O certificate, license copies, business plan, and production projections"),
            ("•", "Some carriers have minimum production requirements — understand these before applying"),
            ("•", "Large carriers (Progressive, Travelers, Nationwide) have their own processes"),
            ("•", "Consider joining an aggregator (SIAA, Smart Choice, Keystone) for access to multiple carriers with one agreement"),
        ]),
        ("Maintaining Your Appointments", [
            ("•", "Meet minimum production requirements — loss of appointment often comes from inactivity"),
            ("•", "Attend carrier training and product update webinars"),
            ("•", "Build relationships with your carrier's territory manager/BDM"),
            ("•", "Keep loss ratios in acceptable ranges — high loss ratios lead to appointment terminations"),
            ("•", "Know your carriers' underwriting guidelines and don't submit unprofitable risks"),
        ]),
        ("Appointment Termination — What to Do", [
            "If a carrier terminates your appointment:",
            ("•", "Review termination letter for cause and effective date"),
            ("•", "Notify affected clients and move to a replacement carrier proactively"),
            ("•", "Request a 'for cause' vs. 'without cause' determination — affects non-compete clauses"),
            ("•", "Document all client notifications in their files"),
            ("•", "Review your state's requirements for notice to clients upon appointment loss"),
        ]),
    ])

print("✓ 06_COMPLIANCE_LICENSING complete")

# ─── 07_CARRIER_RELATIONSHIPS ──────────────────────────────────────────────────
p07 = "07_CARRIER_RELATIONSHIPS/"

doc(p07+"Carrier_Negotiation_Guide.docx",
    "Carrier Negotiation Guide",
    "Insurance Agency OS | Maximizing Markets, Rates, and Support",
    [
        ("Understanding Your Leverage as an Agent", [
            "As an independent agent, you bring carriers business volume. That's leverage — and the best agents use it strategically. Your book of business, loss ratios, and growth trajectory all affect your ability to negotiate better terms, faster service, and exclusive programs.",
        ]),
        ("What You Can Negotiate with Carriers", [
            ("•", "Commission levels: Standard vs. contingency commissions based on volume and loss ratio"),
            ("•", "Underwriting flexibility: Special pricing for hard-to-place risks from a trusted agent"),
            ("•", "Service levels: Dedicated underwriter, faster turnaround, priority handling"),
            ("•", "Marketing co-op funds: Carriers often provide marketing support for producing agents"),
            ("•", "Training and certification access: Advanced designations, carrier-specific training"),
        ]),
        ("Annual Carrier Review Meeting Agenda", [
            ("•", "Our production with you this year: [premium volume, policy count, growth %]"),
            ("•", "Our loss ratio with you: [X%] — discuss claims trends"),
            ("•", "Market and appetite: What lines are you looking for more or less of?"),
            ("•", "Service feedback: Areas where service could improve"),
            ("•", "2025 goals and initiatives: How can we grow together?"),
            ("•", "Contingency and profit sharing: What are the thresholds and current trajectory?"),
        ]),
        ("Building Your Carrier Scorecard", [
            "Rate each carrier quarterly on:",
            ("•", "Competitive pricing in your key market segments (1-5 scale)"),
            ("•", "Underwriting flexibility and turnaround time (1-5)"),
            ("•", "Claims handling and adjuster responsiveness (1-5)"),
            ("•", "Policy service and endorsement processing speed (1-5)"),
            ("•", "Technology (quoting system, portal, digital tools) (1-5)"),
            ("•", "Relationship quality with territory manager (1-5)"),
        ]),
    ])

doc(p07+"Underwriting_Submission_Guide.docx",
    "Underwriting Submission Guide",
    "Insurance Agency OS | How to Get the Best Underwriting Decisions",
    [
        ("Why Submission Quality Matters", [
            "Underwriters approve, modify, or decline coverage based on the information you provide. A well-organized, complete submission with a strong agent narrative gets better pricing and faster decisions. Poorly prepared submissions invite declinations and damage carrier relationships.",
        ]),
        ("Elements of a Winning Submission", [
            ("•", "Complete application with no missing fields"),
            ("•", "Agent narrative: 2-4 paragraph explanation of the risk in your own words"),
            ("•", "Loss runs: Last 3-5 years (commercial) or claims history (personal)"),
            ("•", "Supporting documentation: Inspection reports, financial statements, photos (as needed)"),
            ("•", "Framing the risk favorably: Lead with strengths, address concerns proactively"),
        ]),
        ("The Agent Narrative — Best Practices", [
            "Include these elements in every commercial submission narrative:",
            ("•", "Business description: What they do, how long, management experience"),
            ("•", "Risk controls in place: Safety programs, employee training, security systems"),
            ("•", "Loss history context: If claims exist, explain what was done to prevent recurrence"),
            ("•", "Unique characteristics: Why this is a better-than-average risk for its class"),
            ("•", "Why you chose this carrier: 'This risk fits your appetite for [X] because...'"),
        ]),
        ("Declination Recovery Strategy", [
            "If a submission is declined:",
            ("•", "Request detailed decline reasons in writing"),
            ("•", "Address concerns if possible (additional documentation, safety improvements)"),
            ("•", "Resubmit to 2-3 other carriers with lessons learned"),
            ("•", "For hard-to-place risks: Consider E&S markets or specialty carriers"),
            ("•", "Inform the client transparently: 'We've had a challenge placing this — here's our plan'"),
        ]),
    ])

doc(p07+"Market_Access_Strategy.docx",
    "Market Access Strategy",
    "Insurance Agency OS | Building a Competitive Carrier Portfolio",
    [
        ("Why Market Access Matters", [
            "The value you provide as an independent agent is directly tied to your market access. The more carriers you represent, the more competitive options you can offer clients, and the harder it is for clients to leave (and find the same market access elsewhere).",
        ]),
        ("Core Personal Lines Carrier Portfolio", [
            "Target: 6-10 personal lines carriers covering all client segments",
            ("•", "2-3 preferred market carriers (for excellent credit, no claims clients)"),
            ("•", "2-3 standard market carriers (for average risk profiles)"),
            ("•", "1-2 non-standard carriers (for high-risk profiles: DUI, poor credit, lapse)"),
            ("•", "1 specialty carrier (condo, high-value home, coastal)"),
        ]),
        ("Core Commercial Lines Carrier Portfolio", [
            "Target: 8-12 commercial carriers with diversified appetite",
            ("•", "General liability and BOP carriers (2-3)"),
            ("•", "Commercial auto (2)"),
            ("•", "Workers compensation (2-3)"),
            ("•", "Professional liability and D&O (1-2)"),
            ("•", "Specialty commercial (cyber, EPLI, contractors) (2-3)"),
            ("•", "E&S market access for hard-to-place risks (1 E&S broker relationship)"),
        ]),
        ("Aggregator Advantages", [
            ("•", "SIAA: Largest independent agency alliance — carrier access + profit sharing"),
            ("•", "Smart Choice: Access to 40+ carriers with no production minimums for each"),
            ("•", "Keystone: Regional focus, strong carrier relationships, agency development"),
            ("•", "Advantage: Access to markets you could never get alone as a new agency"),
        ]),
    ])

print("✓ 07_CARRIER_RELATIONSHIPS complete")

# ─── XLSX FILES ────────────────────────────────────────────────────────────────

# XLSX 1: Agency CRM (01_LEAD_GENERATION)
wb1 = Workbook()
ws = wb1.active; ws.title = "Lead Tracker"
for col,w in zip(['A','B','C','D','E','F','G','H','I','J','K'],
                 [18,25,16,28,14,14,18,22,16,22,28]):
    ws.column_dimensions[col].width = w
hrow(ws,1,list(range(1,12)),
    ["Lead ID","Full Name","Phone","Email","Source","Type","Status","Policy Lines","Premium Est.","Last Contact","Next Step"],
    NAV)
lead_data = [
    ["L001","James Parker","(555) 201-3344","jparker@email.com","Zillow Ad","Personal","Hot","Home+Auto","$2,400/yr","2024-01-10","Send quote"],
    ["L002","Susan Hill","(555) 312-4455","shill@email.com","Referral","Personal","Warm","Auto Only","$1,100/yr","2024-01-11","Follow-up call"],
    ["L003","Robert Chen","(555) 423-5566","rchen@email.com","LinkedIn","Commercial","Hot","BOP+WC","$8,500/yr","2024-01-12","Appointment set"],
    ["L004","Maria Gonzalez","(555) 534-6677","mgonzalez@email.com","Facebook","Personal","Warm","Home+Auto+Life","$4,200/yr","2024-01-13","Needs analysis"],
    ["L005","David Kim","(555) 645-7788","dkim@email.com","Cold Call","Commercial","Cold","GL Only","$3,200/yr","2024-01-14","Email follow-up"],
    ["L006","Jennifer White","(555) 756-8899","jwhite@email.com","SOI","Personal","Hot","Home+Auto+Umbrella","$5,100/yr","2024-01-15","Quote presentation"],
    ["L007","Carlos Rivera","(555) 867-9900","crivera@email.com","Chamber","Commercial","Warm","BOP+Auto","$6,800/yr","2024-01-16","Send questionnaire"],
    ["L008","Amy Johnson","(555) 978-0011","ajohnson@email.com","Website","Personal","Cold","Auto Only","$900/yr","2024-01-17","Send email"],
]
for i, row in enumerate(lead_data):
    bg = LGR if i%2==0 else WHT
    drow(ws,i+2,list(range(1,12)),row,bg)

ws2 = wb1.create_sheet("Active Clients")
for col,w in zip(['A','B','C','D','E','F','G','H','I','J'],
                 [14,25,16,28,20,16,16,16,16,28]):
    ws2.column_dimensions[col].width = w
hrow(ws2,1,list(range(1,11)),
    ["Client ID","Full Name","Phone","Email","Policies","Annual Premium","Carrier(s)","Next Renewal","Last Review","Notes"],
    NAV)
client_data = [
    ["C001","Thomas Brown","(555) 111-2222","tbrown@email.com","Home+Auto","$2,850","Travelers","2024-06-15","2024-01-10","Strong relationship, referred 2 clients"],
    ["C002","Patricia Davis","(555) 222-3333","pdavis@email.com","Home+Auto+Umbrella","$4,100","Nationwide","2024-07-01","2024-01-05","VIP client, long tenure"],
    ["C003","Michael Lee","(555) 333-4444","mlee@email.com","BOP+WC+Auto","$11,200","Hartford","2024-08-15","2023-08-10","Commercial client, growing business"],
    ["C004","Sandra Wilson","(555) 444-5555","swilson@email.com","Home+Auto+Life","$5,400","Progressive","2024-05-30","2023-12-15","Recently added life insurance"],
    ["C005","Kevin Thompson","(555) 555-6666","kthompson@email.com","Auto Only","$1,100","GEICO Direct","2024-09-01","2024-01-08","Single policy, upsell opportunity"],
    ["C006","Linda Martinez","(555) 666-7777","lmartinez@email.com","Home+Auto+Flood","$3,900","Allstate","2024-04-15","2023-10-15","Coastal property, flood added last year"],
]
for i, row in enumerate(client_data):
    bg = LGR if i%2==0 else WHT
    drow(ws2,i+2,list(range(1,11)),row,bg)

ws3 = wb1.create_sheet("Policy Pipeline")
for col,w in zip(['A','B','C','D','E','F','G','H'],
                 [18,25,20,16,18,16,16,20]):
    ws3.column_dimensions[col].width = w
hrow(ws3,1,list(range(1,9)),
    ["Application #","Client Name","Policy Type","Carrier","Status","Annual Premium","Effective Date","Notes"],
    NAV)
pipeline_data = [
    ["APP-001","James Parker","Home+Auto","Travelers","Submitted","$2,400","2024-02-01","Awaiting underwriting approval"],
    ["APP-002","Jennifer White","Home+Auto+Umbrella","Nationwide","Quoted","$5,100","2024-02-15","Proposal sent, pending acceptance"],
    ["APP-003","Robert Chen","BOP+WC","Hartford","In Process","$8,500","2024-03-01","Loss runs received, submitting Monday"],
    ["APP-004","Maria Gonzalez","Home+Auto+Life","Progressive","Needs Analysis","$4,200","TBD","Life needs analysis scheduled 1/20"],
]
for i, row in enumerate(pipeline_data):
    bg = LGR if i%2==0 else WHT
    drow(ws3,i+2,list(range(1,9)),row,bg)

wb1.save(BASE+"01_LEAD_GENERATION/Agency_CRM.xlsx")
print(f"  ✓ 01_LEAD_GENERATION/Agency_CRM.xlsx")

# XLSX 2: Policy Renewal Tracker (03_POLICY_SERVICES)
wb2 = Workbook()
ws = wb2.active; ws.title = "Renewal Tracker"
for col,w in zip(['A','B','C','D','E','F','G','H','I'],
                 [14,25,22,18,16,16,16,18,28]):
    ws.column_dimensions[col].width = w
hrow(ws,1,list(range(1,10)),
    ["Client ID","Client Name","Policy Type","Carrier","Renewal Date","Current Premium","New Premium","Status","Action Needed"],
    NAV)
renewal_data = [
    ["C001","Thomas Brown","Home+Auto","Travelers","2024-06-15","$2,850","$2,950","Active","Send renewal quote by 5/15"],
    ["C002","Patricia Davis","Home+Auto+Umbrella","Nationwide","2024-07-01","$4,100","$4,250","Active","Annual review scheduled 6/1"],
    ["C003","Michael Lee","BOP+WC+Auto","Hartford","2024-08-15","$11,200","Pending","Active","Loss runs needed for renewal"],
    ["C004","Sandra Wilson","Home+Auto+Life","Progressive","2024-05-30","$5,400","$5,600","Review Needed","Call client 4/30"],
    ["C005","Kevin Thompson","Auto Only","GEICO Direct","2024-09-01","$1,100","$1,175","Active","Upsell homeowner at renewal"],
    ["C006","Linda Martinez","Home+Auto+Flood","Allstate","2024-04-15","$3,900","$4,100","Urgent","Renewal in 30 days — call NOW"],
    ["C007","Frank Garcia","Home Only","State Farm","2024-05-01","$1,800","$1,950","Active","Shop alternate carriers"],
    ["C008","Helen Zhang","Auto+Umbrella","Progressive","2024-06-30","$2,200","$2,350","Active","Send renewal comparison"],
]
for i, row in enumerate(renewal_data):
    bg = LGR if i%2==0 else WHT
    drow(ws,i+2,list(range(1,10)),row,bg)

ws2 = wb2.create_sheet("Annual Review Schedule")
for col,w in zip(['A','B','C','D','E','F','G'],
                 [14,25,18,16,18,18,25]):
    ws2.column_dimensions[col].width = w
hrow(ws2,1,list(range(1,8)),
    ["Client ID","Client Name","Policy Type","Annual Premium","Last Review","Next Review","Review Status"],
    NAV)
review_data = [
    ["C001","Thomas Brown","Home+Auto","$2,850","2024-01-10","2025-01-10","Complete"],
    ["C002","Patricia Davis","Home+Auto+Umbrella","$4,100","2024-01-05","2025-01-05","Complete"],
    ["C003","Michael Lee","BOP+WC+Auto","$11,200","2023-08-10","2024-08-10","Scheduled 8/5"],
    ["C004","Sandra Wilson","Home+Auto+Life","$5,400","2023-12-15","2024-12-15","Due Q4"],
    ["C005","Kevin Thompson","Auto Only","$1,100","2024-01-08","2025-01-08","Complete"],
    ["C006","Linda Martinez","Home+Auto+Flood","$3,900","2023-10-15","2024-10-15","Due Q4"],
]
for i, row in enumerate(review_data):
    bg = LGR if i%2==0 else WHT
    drow(ws2,i+2,list(range(1,8)),row,bg)

wb2.save(BASE+"03_POLICY_SERVICES/Policy_Renewal_Tracker.xlsx")
print(f"  ✓ 03_POLICY_SERVICES/Policy_Renewal_Tracker.xlsx")

# XLSX 3: Agency KPI Dashboard (08_AGENCY_OPERATIONS)
wb3 = Workbook()
ws = wb3.active; ws.title = "Monthly KPIs"
for col,w in zip(['A','B','C','D','E','F'],
                 [28,14,14,14,14,14]):
    ws.column_dimensions[col].width = w
hrow(ws,1,[1,2,3,4,5,6],["KPI Metric","January","February","March","April","May"],NAV)
kpi_data = [
    ["New Policies Written","22","25","21","28","30"],
    ["New Leads Generated","89","95","78","102","115"],
    ["Lead-to-Policy Conversion Rate","24.7%","26.3%","26.9%","27.5%","26.1%"],
    ["Total Policies in Force","412","427","438","456","476"],
    ["Monthly New Premium Written","$18,500","$21,200","$17,800","$24,100","$26,500"],
    ["Policy Retention Rate","91%","92%","90%","93%","92%"],
    ["Cancellations","8","7","9","6","7"],
    ["Claims Filed by Clients","12","9","14","11","10"],
    ["Average Premium Per Policy","$1,850","$1,870","$1,880","$1,895","$1,920"],
    ["Revenue (Estimated)","$9,250","$10,600","$8,900","$12,050","$13,250"],
    ["Annual Reviews Completed","18","22","19","25","28"],
    ["Referrals Received","14","17","13","19","22"],
]
for i, row in enumerate(kpi_data):
    bg = LGR if i%2==0 else WHT
    drow(ws,i+2,[1,2,3,4,5,6],row,bg)

ws2 = wb3.create_sheet("Carrier Production")
for col,w in zip(['A','B','C','D','E','F'],
                 [22,16,16,16,16,16]):
    ws2.column_dimensions[col].width = w
hrow(ws2,1,[1,2,3,4,5,6],
    ["Carrier","Policies","Annual Premium","Loss Ratio","Commission %","YTD Commission"],
    NAV)
carrier_data = [
    ["Travelers","87","$195,000","52%","12%","$23,400"],
    ["Nationwide","64","$148,000","58%","11%","$16,280"],
    ["Hartford Commercial","28","$312,000","61%","10%","$31,200"],
    ["Progressive","95","$112,000","47%","13%","$14,560"],
    ["Allstate","43","$98,000","55%","11%","$10,780"],
    ["State Farm","31","$71,000","49%","12%","$8,520"],
    ["Liberty Mutual","22","$52,000","63%","10%","$5,200"],
    ["Other Carriers","8","$18,000","45%","12%","$2,160"],
]
for i, row in enumerate(carrier_data):
    bg = LGR if i%2==0 else WHT
    drow(ws2,i+2,[1,2,3,4,5,6],row,bg)

wb3.save(BASE+"08_AGENCY_OPERATIONS/Agency_KPI_Dashboard.xlsx")
print(f"  ✓ 08_AGENCY_OPERATIONS/Agency_KPI_Dashboard.xlsx")

print("\nPART 2 DONE")
