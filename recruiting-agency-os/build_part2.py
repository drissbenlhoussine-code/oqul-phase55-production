"""Recruiting Agency OS — Part 2: folders 04–07 + XLSX files"""
import os
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/recruiting-agency-os/Ultimate_Recruiting_Agency_Operating_System/"

NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"; MGR="ECF0F1"

def hf(hex_): return PatternFill("solid", fgColor=hex_)
def bf(bold=True, sz=11, color="000000"): return Font(bold=bold, size=sz, color=color)
def al(h="center", v="center"): return Alignment(horizontal=h, vertical=v, wrap_text=True)
def thin_border():
    s = Side(style='thin', color='CCCCCC')
    return Border(left=s, right=s, top=s, bottom=s)

def hrow(ws, row, cols, texts, bg=NAV, fg=WHT, bold=True, sz=11):
    for col, text in zip(cols, texts):
        c = ws.cell(row=row, column=col, value=text)
        c.fill = hf(bg); c.font = bf(bold, sz, fg)
        c.alignment = al(); c.border = thin_border()

def drow(ws, row, cols, vals, bg=WHT, sz=10):
    for col, val in zip(cols, vals):
        c = ws.cell(row=row, column=col, value=val)
        c.fill = hf(bg); c.font = bf(False, sz)
        c.alignment = al("left"); c.border = thin_border()

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

# ── 04_CANDIDATE_MANAGEMENT ───────────────────────────────────────────────────
doc("04_CANDIDATE_MANAGEMENT/Candidate_Screening_Script.docx",
    "Candidate Screening Script",
    "Recruiting Agency Operating System | Candidate Management",
    [
        ("OPENING (0–2 min)", [
            "'Hi [Name], this is [Your Name] from [Agency]. Thanks for connecting / applying for the [Role] opportunity. Is now still a good time for a quick 20-minute conversation?'",
        ]),
        ("CURRENT SITUATION (2–8 min)", [
            ("•", "Tell me about your current role at [Company]."),
            ("•", "What does your day-to-day look like?"),
            ("•", "How long have you been in that role, and how long with the company?"),
            ("•", "What are your biggest accomplishments in this position?"),
        ]),
        ("MOTIVATION & AVAILABILITY (8–12 min)", [
            ("•", "What's prompting you to explore new opportunities right now?"),
            ("•", "What would your ideal next role look like?"),
            ("•", "What's your current notice period?"),
            ("•", "When would you be available to start?"),
        ]),
        ("COMPENSATION (12–15 min)", [
            ("•", "What is your current base salary / total compensation?"),
            ("•", "What are your compensation expectations for your next role?"),
            ("•", "Are you interviewing elsewhere right now? If so, at what stage?"),
        ]),
        ("ROLE OVERVIEW & INTEREST (15–18 min)", [
            "Present a 60-second overview of the opportunity without naming the client yet:",
            "'I'm working with a [size] [industry] company on a [role] position. It's [remote/hybrid/on-site] in [location], paying $[range] base + [benefits]. The team is [brief description].'",
            ("•", "Does that sound like the type of role you'd be interested in?"),
            ("•", "What aspects appeal to you most? Any concerns?"),
        ]),
        ("CLOSE (18–20 min)", [
            "'Based on this conversation, I think you could be a strong fit. I'd like to submit your profile to my client. To do that, I'll need to send you a brief summary to confirm accuracy. Is that okay?'",
            "Next: 'I'll be in touch within [2] business days with next steps. Can I text you updates as well as email?'",
        ]),
    ])

doc("04_CANDIDATE_MANAGEMENT/Interview_Preparation_Guide.docx",
    "Interview Preparation Guide",
    "Recruiting Agency Operating System | Candidate Management",
    [
        ("HOW TO USE THIS GUIDE", [
            "Send this guide to candidates before their client interview. Customize [brackets] with role and company-specific details.",
        ]),
        ("BEFORE THE INTERVIEW", [
            ("•", "Research [Company]: Visit their website, LinkedIn, Glassdoor, and recent news"),
            ("•", "Study the job description and match your experience to each requirement"),
            ("•", "Prepare 3–5 STAR stories (Situation, Task, Action, Result) for behavioral questions"),
            ("•", "Prepare 5 thoughtful questions to ask the interviewer"),
            ("•", "Confirm location, format (video/phone/in-person), and interviewer name"),
            ("•", "Plan to arrive / log on 5–10 minutes early"),
        ]),
        ("COMMON INTERVIEW QUESTIONS WITH TIPS", [
            ("•", "'Tell me about yourself.' → Give a 90-second professional story: current role → relevant experience → why this opportunity excites you."),
            ("•", "'Why are you leaving your current job?' → Keep it positive; focus on growth, opportunity, and fit — not negatives."),
            ("•", "'Tell me about a challenge you faced and how you handled it.' → Use a STAR story with a specific, measurable outcome."),
            ("•", "'Where do you see yourself in 5 years?' → Show ambition aligned with company trajectory."),
            ("•", "'What are your salary expectations?' → Reference the range discussed with your recruiter. Confirm current market before the interview."),
        ]),
        ("QUESTIONS TO ASK THE INTERVIEWER", [
            ("•", "What does success look like in the first 90 days for this role?"),
            ("•", "What are the biggest challenges the team is facing right now?"),
            ("•", "Can you describe the management style of the person I'd report to?"),
            ("•", "What do people in this role typically move on to?"),
            ("•", "What do you enjoy most about working at [Company]?"),
        ]),
        ("AFTER THE INTERVIEW", [
            ("•", "Send a thank-you email within 24 hours to each interviewer"),
            ("•", "Call your recruiter immediately with feedback and interest level"),
            ("•", "Rate your interest on a scale of 1–10 and share any concerns"),
        ]),
    ])

doc("04_CANDIDATE_MANAGEMENT/Candidate_Assessment_Framework.docx",
    "Candidate Assessment Framework",
    "Recruiting Agency Operating System | Candidate Management",
    [
        ("SCORING MODEL", [
            "Score each candidate on the following dimensions using a 1–5 scale. Total score out of 40 determines recommendation tier.",
        ]),
        ("DIMENSION 1 — TECHNICAL SKILLS (1–5)", [
            ("•", "5: Exceeds all technical requirements"),
            ("•", "4: Meets all requirements, exceeds some"),
            ("•", "3: Meets core requirements, minor gaps"),
            ("•", "2: Meets some requirements, notable gaps"),
            ("•", "1: Does not meet minimum requirements"),
        ]),
        ("DIMENSION 2 — EXPERIENCE LEVEL (1–5)", [
            ("•", "Years in relevant role, industry, and company size/stage"),
            ("•", "5 = 120%+ match to brief; 3 = ~80% match; 1 = below 50%"),
        ]),
        ("DIMENSION 3 — CULTURE FIT (1–5)", [
            ("•", "Assess: work style, communication, values alignment, energy"),
            ("•", "Ask: 'Describe your ideal work environment' / 'Tell me about a manager you thrived under'"),
        ]),
        ("DIMENSION 4 — MOTIVATION & COMMITMENT (1–5)", [
            ("•", "5: Strong reasons to move, excited about this specific role"),
            ("•", "3: Open to looking, moderate interest"),
            ("•", "1: Passive / just testing the market, low urgency"),
        ]),
        ("DIMENSION 5 — COMPENSATION ALIGNMENT (1–5)", [
            ("•", "5: Expectations comfortably within budget"),
            ("•", "3: At the top of range; possible but requires flexibility"),
            ("•", "1: Significantly above budget"),
        ]),
        ("DIMENSION 6 — AVAILABILITY & LOGISTICS (1–5)", [
            ("•", "Start date, location, remote requirement, right to work"),
        ]),
        ("DIMENSION 7 — INTERVIEW PERFORMANCE (1–5)", [
            ("•", "Communication clarity, professionalism, preparation, quality of examples"),
        ]),
        ("DIMENSION 8 — REFERENCES / REPUTATION (1–5)", [
            ("•", "Quality of references, LinkedIn recommendations, portfolio/samples"),
        ]),
        ("SCORING GUIDE", [
            ("•", "35–40: A-player — Submit immediately with strong recommendation"),
            ("•", "28–34: Strong candidate — Submit with notes on any gaps"),
            ("•", "20–27: Consider — Only if pipeline is thin; flag concerns"),
            ("•", "Below 20: Do not submit"),
        ]),
    ])

doc("04_CANDIDATE_MANAGEMENT/Candidate_Communication_Templates.docx",
    "Candidate Communication Templates",
    "Recruiting Agency Operating System | Candidate Management",
    [
        ("PROFILE SUBMITTED", [
            "Subject: Your Profile Has Been Submitted — [Role] at [Company]",
            "Hi [Name], I've submitted your profile to [Company] for the [Role] position. They typically respond within [3–5] business days. I'll update you as soon as I hear back. Any questions in the meantime, I'm here.",
        ]),
        ("INTERVIEW CONFIRMED", [
            "Subject: Interview Confirmed — [Role] at [Company]",
            "Hi [Name], great news — [Company] would like to interview you! Here are the details:\n• Date/Time: [Date] at [Time]\n• Format: [Video/Phone/In-Person]\n• Interviewer: [Name, Title]\n• Location/Link: [Details]\nI'll send you an interview prep guide shortly. Let me know if you have questions.",
        ]),
        ("POST-INTERVIEW FEEDBACK REQUEST", [
            "Subject: How Did It Go? — [Company] Interview",
            "Hi [Name], I hope the interview went well! Can you share:\n1. Your overall impression of the role and company\n2. Your interest level (1–10)\n3. Anything you felt uncertain about\nThe client is looking for feedback this week — I'll keep you posted.",
        ]),
        ("OFFER EXTENDED", [
            "Subject: Exciting Update — Offer for [Role] at [Company]",
            "Hi [Name], I have exciting news — [Company] has extended an offer. Here are the details:\n• Base Salary: $[Amount]\n• Bonus: [Details]\n• Benefits: [Details]\n• Start Date: [Date]\nI'd like to walk you through this with you on a call. Are you available [time options]?",
        ]),
        ("CANDIDATE NOT SELECTED", [
            "Subject: Update on [Role] at [Company]",
            "Hi [Name], I received an update from [Company] — they've decided to move forward with another candidate. I know this isn't the news you were hoping for.\nTheir feedback: [Specific feedback if shared].\nI have [X] other searches that may be a fit for your profile. Can we reconnect this week to discuss?",
        ]),
        ("PLACEMENT CONGRATULATIONS", [
            "Subject: Congratulations on Your New Role!",
            "Hi [Name], congratulations — you're starting at [Company] on [Date]! This is a fantastic opportunity and I'm excited for you.\nA few reminders:\n• Contact [HR Name] to complete onboarding paperwork\n• Let me know how your first week goes\n• I'll check in at the [30]-day mark\nWishing you every success in your new role.",
        ]),
    ])

doc("04_CANDIDATE_MANAGEMENT/Reference_Check_Script.docx",
    "Reference Check Script",
    "Recruiting Agency Operating System | Candidate Management",
    [
        ("OPENING", [
            "'Hi [Reference Name], this is [Your Name] from [Agency]. [Candidate] gave your name as a professional reference. Do you have about 10 minutes?'",
        ]),
        ("RELATIONSHIP VERIFICATION", [
            ("•", "How long have you known [Candidate] and in what capacity?"),
            ("•", "Did you directly manage [Candidate]? For how long?"),
        ]),
        ("PERFORMANCE QUESTIONS", [
            ("•", "How would you describe [Candidate's] overall performance and contribution to the team?"),
            ("•", "What were [Candidate's] strongest skills?"),
            ("•", "What areas did [Candidate] most need to develop or improve?"),
            ("•", "Can you give me a specific example of a challenge [Candidate] handled well?"),
            ("•", "How did [Candidate] work under pressure or tight deadlines?"),
        ]),
        ("CULTURE & COLLABORATION", [
            ("•", "How did [Candidate] interact with colleagues, leadership, and clients?"),
            ("•", "How did [Candidate] handle conflict or disagreement?"),
            ("•", "Describe [Candidate's] communication style."),
        ]),
        ("REHIRE QUESTION", [
            ("•", "'Would you rehire [Candidate] if given the opportunity? Why or why not?'"),
            "(This is the single most telling question — hesitation or a 'no' is a red flag.)",
        ]),
        ("CLOSING", [
            "'Is there anything else you think I should know about [Candidate] that would help me assess their fit for a [role title] position?'",
            "'Thank you so much for your time. Your insights are very helpful.'",
        ]),
        ("RED FLAGS TO LISTEN FOR", [
            ("•", "Overly generic or vague answers"),
            ("•", "Long pauses before answering"),
            ("•", "Reluctance to give specific examples"),
            ("•", "'No' or hesitation on rehire question"),
            ("•", "Mentions of interpersonal issues or poor performance without being asked"),
        ]),
    ])

print("✓ 04_CANDIDATE_MANAGEMENT DOCX complete")

# ── 05_CLIENT_MANAGEMENT ──────────────────────────────────────────────────────
doc("05_CLIENT_MANAGEMENT/Candidate_Submittal_Template.docx",
    "Candidate Submittal Template",
    "Recruiting Agency Operating System | Client Management",
    [
        ("CANDIDATE SUBMITTAL FORMAT", [
            "Use this format for each candidate profile you submit. Include one profile per page or section.",
        ]),
        ("CANDIDATE PROFILE TEMPLATE", [
            "CANDIDATE: [Full Name]",
            "CURRENT ROLE: [Title] at [Company] ([X] years)",
            "EDUCATION: [Degree], [Institution]",
            "LOCATION: [City, State] | [Remote/Relocation preference]",
            "AVAILABILITY: [Date] | Notice period: [X weeks]",
            "COMPENSATION: Current $[X] | Seeking $[X]–$[X]",
            "",
            "RELEVANT EXPERIENCE SUMMARY:",
            "3–4 sentences highlighting the most relevant experience for this specific role.",
            "",
            "KEY QUALIFICATIONS:",
            ("•", "[Requirement from job order]: [Candidate evidence]"),
            ("•", "[Requirement from job order]: [Candidate evidence]"),
            ("•", "[Requirement from job order]: [Candidate evidence]"),
            "",
            "RECRUITER'S ASSESSMENT:",
            "1–2 sentences on overall fit, any notable strengths or considerations.",
            "",
            "INTEREST LEVEL: [X]/10 — [Brief reason]",
        ]),
        ("COVER EMAIL TEMPLATE", [
            "Subject: [X] Candidates for [Role] — [Company Name]",
            "Hi [Name],",
            "Please find [X] candidate profiles for the [Role] position. Each has been screened against your criteria and is available within your budget.",
            "My top recommendation is [Candidate Name] because [1 sentence reason].",
            "Please let me know by [date] which candidates you'd like to interview, and I'll schedule within 24 hours.",
            "Best,\n[Your Name]",
        ]),
    ])

doc("05_CLIENT_MANAGEMENT/Weekly_Client_Update_Template.docx",
    "Weekly Client Update Template",
    "Recruiting Agency Operating System | Client Management",
    [
        ("WEEKLY SEARCH UPDATE EMAIL", [
            "Subject: Weekly Search Update — [Role] | [Company] | Week [X]",
            "Hi [Name],",
            "Here's your weekly update for the [Role] search:",
        ]),
        ("PIPELINE METRICS", [
            ("•", "Total candidates sourced this week: [X]"),
            ("•", "Phone screens completed: [X]"),
            ("•", "Qualified candidates identified: [X]"),
            ("•", "Profiles submitted to date: [X]"),
            ("•", "Active in interview process: [X]"),
            ("•", "Offers pending: [X]"),
        ]),
        ("HIGHLIGHTS THIS WEEK", [
            "[2–3 sentences on notable activity, strong candidates, or progress made]",
        ]),
        ("NEXT WEEK'S FOCUS", [
            ("•", "[Specific sourcing action]"),
            ("•", "[Scheduled interviews or calls]"),
            ("•", "[Any adjustments to search strategy]"),
        ]),
        ("ITEMS NEEDED FROM YOU", [
            ("•", "Feedback on submitted profiles by [date]"),
            ("•", "Interview availability for approved candidates"),
            ("•", "[Any other action items]"),
        ]),
        ("SEARCH STATUS", [
            "Overall status: [ ] On Track  [ ] Adjusting Approach  [ ] Needs Discussion",
            "Best,\n[Your Name] | [Agency] | [Phone]",
        ]),
    ])

doc("05_CLIENT_MANAGEMENT/Client_Feedback_Collection.docx",
    "Client Feedback Collection",
    "Recruiting Agency Operating System | Client Management",
    [
        ("POST-INTERVIEW FEEDBACK REQUEST", [
            "Subject: Interview Feedback — [Candidate Name] for [Role]",
            "Hi [Name], following up on [Candidate's] interview [yesterday/on Date]. Could you share:",
            ("•", "Overall impression (1–10)"),
            ("•", "Strongest qualities observed"),
            ("•", "Any concerns or gaps"),
            ("•", "Decision: [ ] Move forward  [ ] Pass  [ ] Pending"),
            "This helps me refine the search and find even better matches. Takes 2 minutes — happy to call instead if easier.",
        ]),
        ("POST-PLACEMENT FEEDBACK (30-Day Check-In)", [
            "Subject: 30-Day Check-In — [Candidate Name] at [Company]",
            "Hi [Name], it's been 30 days since [Candidate] started. Quick check-in:",
            ("•", "How is [Candidate] settling in? (1–10)"),
            ("•", "Meeting expectations so far?"),
            ("•", "Any concerns or coaching areas?"),
            ("•", "Anything we should know for future searches?"),
            "Your feedback helps us continuously improve. Thank you!",
        ]),
        ("CANDIDATE PROFILE FEEDBACK", [
            "Subject: Profile Feedback Needed — [Role] Candidates",
            "Hi [Name], I sent [X] profiles on [Date]. Quick feedback on each would help me narrow the search:",
            ("•", "[Candidate 1]: [ ] Yes — interview  [ ] No — because: ___"),
            ("•", "[Candidate 2]: [ ] Yes — interview  [ ] No — because: ___"),
            ("•", "[Candidate 3]: [ ] Yes — interview  [ ] No — because: ___"),
            "Any theme in what's not fitting will help me find the right person faster.",
        ]),
        ("ANNUAL RELATIONSHIP REVIEW", [
            "Once a year, schedule a relationship review call with key clients.",
            ("•", "How satisfied are you with our service overall? (1–10)"),
            ("•", "What did we do well this year?"),
            ("•", "What would you like to see us improve?"),
            ("•", "Are there other roles or departments we could support?"),
            ("•", "Would you feel comfortable recommending us to a colleague?"),
        ]),
    ])

doc("05_CLIENT_MANAGEMENT/Difficult_Conversation_Scripts.docx",
    "Difficult Conversation Scripts",
    "Recruiting Agency Operating System | Client Management",
    [
        ("SCENARIO: CANDIDATE DECLINED OFFER", [
            "'[Name], I have some disappointing news — [Candidate] has decided to decline the offer. I know that's frustrating. They cited [reason]. Here's what I'm doing next: [specific action]. I expect to have new profiles to you by [date]. I'm sorry for the setback.'",
        ]),
        ("SCENARIO: SEARCH IS TAKING LONGER THAN EXPECTED", [
            "'[Name], I want to be transparent — we're at [week X] and haven't yet found the right match. Here's why: [honest assessment of market/criteria]. I'd like to discuss [salary adjustment / relaxed criteria / expanded geography]. Can we talk this week?'",
        ]),
        ("SCENARIO: CLIENT KEEPS REJECTING CANDIDATES WITHOUT CLEAR FEEDBACK", [
            "'[Name], I want to make sure we're aligned. We've submitted [X] candidates and none have moved forward. To find the right person faster, could you share specifically what's missing? Even a few words would help me recalibrate the search.'",
        ]),
        ("SCENARIO: CANDIDATE ACCEPTED COUNTER-OFFER FROM CURRENT EMPLOYER", [
            "'[Name], [Candidate] accepted a counter-offer from their current employer. This is relatively common, especially at senior levels. I had a direct conversation with them and [what you learned]. Here's what I'd suggest we do next...'",
        ]),
        ("SCENARIO: CLIENT WANTS TO REDUCE FEE", [
            "'I understand budget is a consideration. Our fee reflects the depth of search and guarantee we provide. What I can offer is [alternative: payment plan / milestone-based / retained structure]. What I can't do is reduce the fee and maintain the same service level. Can we find a structure that works for both of us?'",
        ]),
        ("SCENARIO: PLACED CANDIDATE IS UNDERPERFORMING", [
            "'[Name], I appreciate you letting me know. I take this seriously. I'd like to understand more about the specific performance gaps so I can assess next steps. Is [Candidate] still within the guarantee period? I want to make this right.'",
        ]),
    ])

print("✓ 05_CLIENT_MANAGEMENT DOCX complete")

# ── 06_COMPLIANCE_LEGAL ───────────────────────────────────────────────────────
doc("06_COMPLIANCE_LEGAL/Recruiting_Service_Agreement.docx",
    "Recruiting Service Agreement Template",
    "Recruiting Agency Operating System | Compliance & Legal",
    [
        ("PARTIES", [
            "This Recruiting Service Agreement ('Agreement') is entered into as of [Date] between [Agency Name], a [State] [entity type] ('Agency'), and [Client Company Name] ('Client').",
        ]),
        ("SERVICES", [
            "Agency will provide candidate sourcing, screening, and placement services for the position(s) described in a Job Order form completed by Client. Each Job Order is incorporated into this Agreement.",
        ]),
        ("FEES", [
            ("•", "Contingency Fee: [X]% of the placed candidate's annualized first-year base salary, due within [30] days of candidate's start date."),
            ("•", "Retained Fee: [X]% paid as follows: [1/3] upon engagement, [1/3] upon shortlist delivery, [1/3] upon start date."),
            ("•", "All fees are exclusive of applicable taxes."),
        ]),
        ("GUARANTEE", [
            "If a placed candidate voluntarily resigns or is terminated for performance within [90] days of start date, Agency will conduct one replacement search at no additional fee. Guarantee is void if: (a) Client terminates the candidate's employment for reasons unrelated to performance; (b) the role is eliminated; (c) Client fails to pay Agency fees timely.",
        ]),
        ("CLIENT OBLIGATIONS", [
            ("•", "Client will provide accurate job descriptions and timely interview scheduling."),
            ("•", "Client will not hire any candidate introduced by Agency for a period of [12] months without paying Agency's fee."),
            ("•", "Client will notify Agency within [5] business days of a placement start date."),
        ]),
        ("CONFIDENTIALITY", [
            "Both parties agree to keep confidential all non-public information shared during the engagement, including candidate information.",
        ]),
        ("LIMITATION OF LIABILITY", [
            "Agency's liability shall not exceed the fees paid by Client in the [3] months preceding any claim. Agency is not liable for consequential, indirect, or punitive damages.",
        ]),
        ("GOVERNING LAW", [
            "This Agreement is governed by the laws of [State]. Disputes shall be resolved by the courts of [State].",
        ]),
        ("SIGNATURES", [
            "Agency: _________________________ Date: _________",
            "Client: _________________________ Date: _________",
        ]),
    ])

doc("06_COMPLIANCE_LEGAL/Anti_Discrimination_Policy.docx",
    "Anti-Discrimination Policy",
    "Recruiting Agency Operating System | Compliance & Legal",
    [
        ("POLICY STATEMENT", [
            "[Agency Name] is committed to equal opportunity in all recruitment activities. We do not discriminate based on race, color, religion, sex, national origin, age, disability, genetic information, sexual orientation, gender identity, veteran status, or any other characteristic protected by federal, state, or local law.",
        ]),
        ("APPLICABLE LAWS", [
            ("•", "Title VII of the Civil Rights Act of 1964"),
            ("•", "Age Discrimination in Employment Act (ADEA)"),
            ("•", "Americans with Disabilities Act (ADA)"),
            ("•", "Genetic Information Nondiscrimination Act (GINA)"),
            ("•", "Applicable state and local fair employment laws"),
        ]),
        ("RECRUITER CONDUCT", [
            ("•", "Do not ask candidates about age, marital status, religion, national origin, pregnancy, or disability"),
            ("•", "Evaluate candidates solely on skills, experience, and qualifications relevant to the role"),
            ("•", "Document all candidate decisions with objective, job-related criteria"),
            ("•", "Do not accept or act on discriminatory client requests"),
        ]),
        ("PROHIBITED QUESTIONS", [
            ("•", "Do not ask: 'How old are you?' 'Are you married?' 'Do you have children?' 'What country are you from?' 'Do you have any disabilities?' 'What is your religion?'"),
            ("•", "Do ask (if job-relevant): 'Are you authorized to work in the US?' 'Can you perform the essential functions of this role?'"),
        ]),
        ("HANDLING DISCRIMINATORY CLIENT REQUESTS", [
            "If a client requests candidates of a specific age, gender, religion, national origin, or other protected class, inform the client that such requirements are unlawful. If the client insists, terminate the search and document the refusal.",
        ]),
        ("VIOLATIONS", [
            "Violations of this policy by Agency staff may result in disciplinary action up to and including termination. Violations by clients will result in termination of the service agreement.",
        ]),
    ])

doc("06_COMPLIANCE_LEGAL/EEOC_Compliance_Checklist.docx",
    "EEOC Compliance Checklist",
    "Recruiting Agency Operating System | Compliance & Legal",
    [
        ("JOB POSTING COMPLIANCE", [
            ("•", "[ ] Job description based on objective, job-related requirements only"),
            ("•", "[ ] No age or experience minimums that could imply age discrimination"),
            ("•", "[ ] 'Equal Opportunity Employer' statement included"),
            ("•", "[ ] No gender-coded language (use inclusive terms)"),
        ]),
        ("SCREENING COMPLIANCE", [
            ("•", "[ ] All candidates for same role screened on same criteria"),
            ("•", "[ ] Interview questions reviewed and approved (no prohibited questions)"),
            ("•", "[ ] Criminal background checks comply with 'ban the box' laws in applicable states"),
            ("•", "[ ] Background check consent obtained before running any check"),
        ]),
        ("INTERVIEW COMPLIANCE", [
            ("•", "[ ] Structured interviews used (same questions for all candidates)"),
            ("•", "[ ] Interview notes focus on job-related observations only"),
            ("•", "[ ] No notes on physical appearance, accent, or personal characteristics"),
            ("•", "[ ] Reasonable accommodations offered if candidate requests"),
        ]),
        ("RECORD KEEPING", [
            ("•", "[ ] Candidate applications and resumes retained for minimum [1–2] years"),
            ("•", "[ ] Interview notes and scoring sheets retained"),
            ("•", "[ ] Reason for rejection documented in objective, job-related terms"),
            ("•", "[ ] Adverse action notices sent if credit/background check results in rejection"),
        ]),
        ("ANNUAL REVIEW", [
            ("•", "[ ] Placement data reviewed for disparate impact patterns"),
            ("•", "[ ] Team trained on updated EEOC guidelines"),
            ("•", "[ ] Client agreements reviewed for discriminatory language"),
        ]),
    ])

doc("06_COMPLIANCE_LEGAL/Record_Retention_Policy.docx",
    "Record Retention Policy",
    "Recruiting Agency Operating System | Compliance & Legal",
    [
        ("PURPOSE", [
            "This policy establishes minimum record retention requirements for [Agency Name] to comply with applicable employment, privacy, and business laws.",
        ]),
        ("RETENTION SCHEDULE", [
            ("•", "Resumes / Applications: 1–2 years from receipt"),
            ("•", "Interview notes and assessments: 1–2 years from final decision"),
            ("•", "Background check records: As required by FCRA (up to 5 years)"),
            ("•", "Placement records (offer letters, contracts): 7 years after placement ends"),
            ("•", "Invoices and payment records: 7 years"),
            ("•", "Client service agreements: Duration of relationship + 7 years"),
            ("•", "EEOC compliance records: 1–2 years minimum"),
            ("•", "Payroll / contractor payment records: 3–7 years"),
        ]),
        ("STORAGE REQUIREMENTS", [
            ("•", "Electronic records: Stored in secure, access-controlled systems with regular backups"),
            ("•", "Physical records: Locked storage; access limited to authorized staff"),
            ("•", "Candidate data: Encrypted at rest and in transit"),
        ]),
        ("DISPOSAL", [
            ("•", "Paper records: Shredded by certified provider"),
            ("•", "Electronic records: Permanently deleted or overwritten using secure methods"),
            ("•", "Document disposal with date and method recorded"),
        ]),
        ("DATA SUBJECT RIGHTS", [
            "Candidates may request access to, correction of, or deletion of their personal data. Respond to such requests within [30] days. Consult applicable privacy laws (GDPR, CCPA) before deleting records within retention periods.",
        ]),
    ])

print("✓ 06_COMPLIANCE_LEGAL DOCX complete")

# ── 07_PLACEMENT_PROCESS ──────────────────────────────────────────────────────
doc("07_PLACEMENT_PROCESS/Offer_Management_SOP.docx",
    "Offer Management SOP",
    "Recruiting Agency Operating System | Placement Process",
    [
        ("STEP 1 — VERBAL OFFER FROM CLIENT", [
            ("•", "Receive verbal offer details: base salary, bonus, benefits, start date, title"),
            ("•", "Confirm all details in writing with client before presenting to candidate"),
            ("•", "Assess: Is offer within candidate's stated expectations?"),
        ]),
        ("STEP 2 — PRESENT OFFER TO CANDIDATE", [
            "'[Name], I have great news — [Company] has extended an offer. I'd like to walk you through it now.'",
            ("•", "Present all details clearly: base, bonus, benefits, PTO, title, start date"),
            ("•", "Gauge initial reaction: 'What's your initial feeling?'"),
            ("•", "Do NOT pressure; give them time to process"),
        ]),
        ("STEP 3 — HANDLE HESITATION OR COUNTER", [
            "If candidate has concerns: 'What specifically would need to change for you to feel great about this offer?'",
            "If counter is reasonable: Present to client as 'candidate is very excited but has one question about [X].'",
            "If counter is unreasonable: 'I want to be honest with you — I don't think the client has room on [X]. Is this truly a deal-breaker, or could you move forward if everything else is in order?'",
        ]),
        ("STEP 4 — ACCEPTANCE CONFIRMED", [
            ("•", "Candidate confirms verbally → immediately notify client"),
            ("•", "Request formal written offer letter sent within [24–48 hours]"),
            ("•", "Advise candidate on how to resign professionally"),
            ("•", "Ask about counter-offer risk: 'When you resign, your employer may counter. How will you handle that?'"),
        ]),
        ("STEP 5 — START DATE MANAGEMENT", [
            ("•", "Confirm written acceptance received by client"),
            ("•", "Note start date in CRM and set guarantee clock"),
            ("•", "Send congratulations email to candidate"),
            ("•", "Send handoff summary to client HR"),
            ("•", "Schedule 30-day check-in with both candidate and client"),
        ]),
    ])

doc("07_PLACEMENT_PROCESS/Salary_Negotiation_Scripts.docx",
    "Salary Negotiation Scripts",
    "Recruiting Agency Operating System | Placement Process",
    [
        ("UNDERSTANDING CANDIDATE'S POSITION", [
            ("•", "'What would it take for this to be an easy yes for you?'"),
            ("•", "'Is this about base salary, or are there other components that matter most to you?'"),
            ("•", "'If the base can't move, what else would make this feel right?'"),
        ]),
        ("PRESENTING A COUNTER TO THE CLIENT", [
            "'[Client Name], [Candidate] is very excited about the role and [Company]. They have one request: could you bring the base to $[X]? Given [their current comp / competing offer / seniority], I think this is reasonable. Is that something you can do?'",
            "If client resists: 'I understand. Could you offer anything else — a signing bonus, extra PTO, earlier review date? That might close the gap without affecting base salary.'",
        ]),
        ("COUNTER-OFFER PREVENTION SCRIPT (Use pre-close)", [
            "Before candidate resigns: 'I need to ask — if your current employer makes a counter-offer when you resign, what will you do?'",
            "If they're unsure: 'In my experience, candidates who accept counter-offers are usually gone within 6 months. The same issues that made them look for a new role are still there — the counter buys time. If you were happy enough to stay for more money, you'd have asked for it already. Does that resonate?'",
        ]),
        ("HANDLING 'I GOT A COMPETING OFFER'", [
            "'Tell me about it — what's the offer, and how does it compare to this one?'",
            "If other offer is higher: 'What does [Company] offer that the other doesn't? Is it worth the difference to you? Let me talk to my client and see what's possible.'",
            "If candidate prefers this role: 'Then let's make the number work. What's the minimum you need to choose this role?'",
        ]),
    ])

doc("07_PLACEMENT_PROCESS/Onboarding_Handoff_Checklist.docx",
    "Onboarding Handoff Checklist",
    "Recruiting Agency Operating System | Placement Process",
    [
        ("FOR CANDIDATE — AFTER ACCEPTANCE", [
            ("•", "[ ] Resignation guidance provided (script if needed)"),
            ("•", "[ ] Start date confirmed and on calendar"),
            ("•", "[ ] Background check / drug screen initiated if required"),
            ("•", "[ ] Offer letter reviewed and signed"),
            ("•", "[ ] Candidate has hiring manager contact for day 1 questions"),
            ("•", "[ ] Counter-offer strategy discussed"),
        ]),
        ("FOR CLIENT — HANDOFF EMAIL", [
            "Subject: Placement Confirmed — [Candidate] Starting [Date]",
            "Hi [Name], delighted to confirm [Candidate] has accepted and will start [Date]. Summary:\n• Start Date: [Date]\n• Background check: [Status]\n• Point of contact for candidate: [HR Name]\n• Guarantee period: [90] days from start date\nPlease let me know if any issues arise. I'll check in at the 30-day mark.",
        ]),
        ("30-DAY CHECK-IN AGENDA", [
            ("•", "Candidate: 'How's the role going? Is it what you expected? Any concerns?'"),
            ("•", "Client: 'How is [Candidate] settling in? Meeting expectations? Any coaching needed?'"),
            ("•", "Document feedback in CRM"),
            ("•", "Flag any performance concerns immediately"),
        ]),
    ])

doc("07_PLACEMENT_PROCESS/Post_Placement_Follow_Up.docx",
    "Post-Placement Follow-Up",
    "Recruiting Agency Operating System | Placement Process",
    [
        ("30-DAY CANDIDATE FOLLOW-UP", [
            "'Hi [Name], it's been a month since you started at [Company]. How is it going? Is the role what you expected? Any surprises — good or bad? I'm here if you ever need anything.'",
        ]),
        ("30-DAY CLIENT FOLLOW-UP", [
            "'Hi [Name], quick check-in on [Candidate] — how are they settling in? Any feedback at this stage? I want to make sure the placement is meeting your expectations.'",
        ]),
        ("90-DAY GUARANTEE EXPIRATION NOTICE", [
            "'Hi [Name], [Candidate's] 90-day guarantee period is ending on [Date]. I trust everything is going well! This is also a great time to discuss any upcoming roles we could help you fill.'",
        ]),
        ("6-MONTH RELATIONSHIP TOUCH", [
            "Candidate: 'Hi [Name], hard to believe it's been 6 months at [Company]! Hope things are going well. If you ever want to connect — or know anyone looking for their next opportunity — I'm always happy to help.'",
            "Client: 'Hi [Name], just thinking of [Company] and wanted to check in. Any upcoming hiring plans for [Q3/Q4]? I'd love to be your first call.'",
        ]),
        ("ANNUAL ANNIVERSARY", [
            "Candidate: 'Hi [Name], one year at [Company]! Hope it's been a great one. If you have colleagues who are open to new opportunities, I'd appreciate an introduction.'",
            "Client: 'Hi [Name], can't believe it's been a year since we placed [Candidate]. Hope they're still delivering. Would love to connect and discuss your team's plans for the year ahead.'",
        ]),
    ])

print("✓ 07_PLACEMENT_PROCESS DOCX complete")

# ── XLSX FILES ────────────────────────────────────────────────────────────────

# 1. Business Development CRM
wb = Workbook()
ws = wb.active; ws.title = "BD Pipeline"
ws.column_dimensions['A'].width = 25
ws.column_dimensions['B'].width = 20
ws.column_dimensions['C'].width = 15
ws.column_dimensions['D'].width = 20
ws.column_dimensions['E'].width = 15
ws.column_dimensions['F'].width = 30
ws.column_dimensions['G'].width = 20
ws.column_dimensions['H'].width = 20

cols = list(range(1,9))
hrow(ws,1,cols,["Company","Contact Name","Title","Email","Stage","Last Activity","Next Action","Est. Fee"],NAV,WHT)
stages = [
    ("Acme Corp","Sarah Johnson","VP HR","sarah@acme.com","Discovery Call","2024-01-10","Send proposal","$18,000"),
    ("Beta Inc","Mike Chen","CEO","mike@beta.com","Proposal Sent","2024-01-08","Follow up Fri","$24,000"),
    ("Gamma Co","Lisa Park","HR Director","lisa@gamma.com","Agreement","2024-01-05","Send agreement","$16,000"),
    ("Delta LLC","Tom Rodriguez","COO","tom@delta.com","Cold Outreach","2024-01-12","Follow up Day 3","$20,000"),
    ("Echo Group","Amy White","Founder","amy@echo.com","Negotiation","2024-01-03","Confirm fee","$15,000"),
]
for i, row in enumerate(stages, 2):
    bg = LGR if i % 2 == 0 else WHT
    drow(ws, i, cols, list(row), bg)

ws2 = wb.create_sheet("Stage Legend")
hrow(ws2,1,[1,2],["Stage","Description"],ACC,WHT)
legend = [
    ("Cold Outreach","Initial contact not yet made"),
    ("Contacted","First touch sent — awaiting response"),
    ("Discovery Call","Call scheduled or completed"),
    ("Proposal Sent","Written proposal delivered"),
    ("Negotiation","Terms being discussed"),
    ("Agreement","Service agreement sent/pending"),
    ("Active Search","Currently filling a role"),
    ("Closed Won","Placement made, fee invoiced"),
    ("Closed Lost","Did not proceed"),
    ("Nurture","Long-term follow-up mode"),
]
for i, row in enumerate(legend, 2):
    bg = LGR if i % 2 == 0 else WHT
    drow(ws2, i, [1,2], list(row), bg)

wb.save(BASE + "01_BUSINESS_DEVELOPMENT/Business_Development_CRM.xlsx")
print("  ✓ 01_BUSINESS_DEVELOPMENT/Business_Development_CRM.xlsx")

# 2. Client Onboarding Tracker
wb2 = Workbook()
ws = wb2.active; ws.title = "Onboarding Tracker"
ws.column_dimensions['A'].width = 25
ws.column_dimensions['B'].width = 20
ws.column_dimensions['C'].width = 20
ws.column_dimensions['D'].width = 15
ws.column_dimensions['E'].width = 15
ws.column_dimensions['F'].width = 20
ws.column_dimensions['G'].width = 20

cols = list(range(1,8))
hrow(ws,1,cols,["Client Company","Role","Agreement Date","Kickoff Date","First Profiles","Status","Recruiter"],NAV,WHT)
data = [
    ("Acme Corp","VP of Sales","Jan 5","Jan 7","Jan 12","Active Search","[Recruiter A]"),
    ("Beta Inc","Sr. Engineer","Jan 3","Jan 4","Jan 9","Interviewing","[Recruiter B]"),
    ("Gamma Co","Marketing Mgr","Dec 28","Dec 30","Jan 4","Offer Stage","[Recruiter A]"),
    ("Delta LLC","Operations Dir","Jan 10","Jan 12","Jan 17","Awaiting Kickoff","[Recruiter C]"),
]
for i, row in enumerate(data, 2):
    drow(ws, i, cols, list(row), LGR if i%2==0 else WHT)

ws2 = wb2.create_sheet("Onboarding Checklist")
hrow(ws2,1,[1,2,3],["Step","Action","Status"],ACC,WHT)
steps = [
    ("1","Agreement signed","✓ Complete"),
    ("2","Welcome email sent","✓ Complete"),
    ("3","Job order intake form received","✓ Complete"),
    ("4","Client research completed","✓ Complete"),
    ("5","Kickoff call scheduled","✓ Complete"),
    ("6","Kickoff call completed","✓ Complete"),
    ("7","Post-kickoff summary sent","✓ Complete"),
    ("8","Sourcing launched","In Progress"),
    ("9","First profiles delivered","Pending"),
    ("10","Candidate feedback received","Pending"),
    ("11","Interviews scheduled","Pending"),
    ("12","Offer stage","Pending"),
    ("13","Placement confirmed","Pending"),
    ("14","30-day check-in scheduled","Pending"),
]
for i, row in enumerate(steps, 2):
    drow(ws2, i, [1,2,3], list(row), LGR if i%2==0 else WHT)

wb2.save(BASE + "02_CLIENT_ONBOARDING/Client_Onboarding_Tracker.xlsx")
print("  ✓ 02_CLIENT_ONBOARDING/Client_Onboarding_Tracker.xlsx")

# 3. Candidate Pipeline Tracker
wb3 = Workbook()
ws = wb3.active; ws.title = "Active Pipeline"
ws.column_dimensions['A'].width = 25
ws.column_dimensions['B'].width = 20
ws.column_dimensions['C'].width = 20
ws.column_dimensions['D'].width = 15
ws.column_dimensions['E'].width = 15
ws.column_dimensions['F'].width = 15
ws.column_dimensions['G'].width = 20
ws.column_dimensions['H'].width = 15

cols = list(range(1,9))
hrow(ws,1,cols,["Candidate Name","Current Role","Target Role","Salary Req","Availability","Stage","Client","Score/10"],NAV,WHT)
cands = [
    ("Alex Turner","Sr. AE at TechCo","VP Sales","$140K","2 weeks","Submitted","Acme Corp","8"),
    ("Maria Santos","Eng Manager","Sr. Engineer","$160K","1 month","Phone Screen","Beta Inc","7"),
    ("James Liu","Mktg Director","Marketing Mgr","$120K","Immediate","Offer","Gamma Co","9"),
    ("Priya Patel","Ops Lead","Operations Dir","$130K","3 weeks","Interview R2","Delta LLC","8"),
    ("Chris Evans","Sales Mgr","VP Sales","$130K","2 weeks","Screening","Acme Corp","6"),
]
for i, row in enumerate(cands, 2):
    drow(ws, i, cols, list(row), LGR if i%2==0 else WHT)

wb3.save(BASE + "04_CANDIDATE_MANAGEMENT/Candidate_Pipeline_Tracker.xlsx")
print("  ✓ 04_CANDIDATE_MANAGEMENT/Candidate_Pipeline_Tracker.xlsx")

# 4. Client Activity Tracker
wb4 = Workbook()
ws = wb4.active; ws.title = "Client Activity"
ws.column_dimensions['A'].width = 25
ws.column_dimensions['B'].width = 20
ws.column_dimensions['C'].width = 15
ws.column_dimensions['D'].width = 20
ws.column_dimensions['E'].width = 25
ws.column_dimensions['F'].width = 20

cols = list(range(1,7))
hrow(ws,1,cols,["Client","Active Roles","Placed YTD","Total Fees YTD","Last Touch","Next Action"],NAV,WHT)
clients = [
    ("Acme Corp","2","3","$54,000","Jan 10","Send weekly update"),
    ("Beta Inc","1","1","$18,000","Jan 9","Schedule interview"),
    ("Gamma Co","1","5","$90,000","Jan 8","Offer call"),
    ("Delta LLC","1","0","$0","Jan 10","Kickoff call"),
    ("Echo Group","0","2","$32,000","Dec 20","Q1 check-in"),
]
for i, row in enumerate(clients, 2):
    drow(ws, i, cols, list(row), LGR if i%2==0 else WHT)

wb4.save(BASE + "05_CLIENT_MANAGEMENT/Client_Activity_Tracker.xlsx")
print("  ✓ 05_CLIENT_MANAGEMENT/Client_Activity_Tracker.xlsx")

print("PART 2 DONE")
