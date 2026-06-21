"""Real Estate Agent OS — Part 2: folders 04–07 + XLSX"""
import os
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/real-estate-agent-os/Ultimate_Real_Estate_Agent_Operating_System/"
NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"

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

# ── 04_NEGOTIATION ────────────────────────────────────────────────────────────
doc("04_NEGOTIATION/Offer_Negotiation_Scripts.docx",
    "Offer Negotiation Scripts",
    "Real Estate Agent Operating System | Negotiation",
    [
        ("NEGOTIATING FOR BUYERS", [
            "After receiving a counter-offer, always present it neutrally first, then give your recommendation.",
            ("•", "Presenting a counter: 'They came back at $[X] with [terms]. Here's my read: [assessment]. I recommend [specific action] because [reason].'"),
            ("•", "If seller won't budge on price: 'What if we ask them to cover $[X] in closing costs / leave the appliances / fix [specific item]? That has the same net effect for you without changing the purchase price.'"),
            ("•", "Anchoring: Present an offer below your buyer's ceiling. 'Let's start at $[X] — it's lower than we'll settle for, but it anchors the negotiation and gives us room.'"),
        ]),
        ("NEGOTIATING FOR SELLERS", [
            ("•", "If offer is low: 'The offer is at $[X]. My recommendation is we counter at $[X] — close but not at asking — to signal we're engaged without giving up position.'"),
            ("•", "Multiple offer scenario: 'We have [X] offers. Let's call for highest and best by [date]. This creates urgency and often improves all offers.'"),
            ("•", "If buyer asks for repairs after inspection: 'The buyer is asking for $[X] in credits or repairs. Here's how I assess the inspection items: [major vs. cosmetic]. I recommend [counter / concede / refuse specific items] because [reason].'"),
        ]),
        ("NEGOTIATION PRINCIPLES", [
            ("•", "Never reveal your client's bottom line or deadline — this is the most common negotiation mistake"),
            ("•", "Always respond in writing — even to verbal counters, confirm in email"),
            ("•", "Speed matters: buyers who wait feel less certain; don't let offers sit"),
            ("•", "Find the seller's real motivation — sometimes it's not price (date, certainty, condition)"),
            ("•", "Use 'if/then' trades: 'If you'll come down to $[X], we'll waive the inspection contingency'"),
        ]),
        ("DIFFICULT NEGOTIATIONS", [
            ("•", "Impasse on price: 'Both parties are [X] apart. What if we split the difference at $[X]?'"),
            ("•", "Unrealistic buyer expectations: 'I need to be honest with you — an offer at $[X] in this market has very little chance of being accepted. Here's the data: [comps]. An offer at $[X] is competitive and still saves you $[X] from list price.'"),
            ("•", "Emotional seller: 'I understand how much this home means to you. I want to get you the best outcome, and sometimes that means accepting an offer that feels lower than you'd like but is the best the market will bear right now.'"),
        ]),
    ])

doc("04_NEGOTIATION/Multiple_Offer_Guide.docx",
    "Multiple Offer Guide",
    "Real Estate Agent Operating System | Negotiation",
    [
        ("FOR SELLERS — MANAGING MULTIPLE OFFERS", [
            "When multiple offers arrive, inform all buyers' agents promptly and follow your state's disclosure laws.",
            ("•", "Call for highest and best: Set a clear deadline (24–48 hours). Instruct each buyer to submit their best and final offer. This maximizes seller net proceeds and reduces drawn-out negotiation."),
            ("•", "What to evaluate beyond price: Financing type (cash > conventional > FHA), earnest money amount, contingency terms, closing date flexibility, escalation clause ceiling"),
            ("•", "Disclose multiple offers: Tell each buyer's agent there are competing offers. You are required to disclose this in most states."),
        ]),
        ("HOW TO EVALUATE MULTIPLE OFFERS (Scoring Sheet)", [
            ("•", "Price: $[amount] — net to seller after concessions"),
            ("•", "Financing: [ ] Cash  [ ] Conventional  [ ] FHA  [ ] VA"),
            ("•", "Earnest money: $[X]"),
            ("•", "Inspection contingency: [ ] Yes  [ ] No  [ ] Modified"),
            ("•", "Financing contingency: [ ] Yes  [ ] No"),
            ("•", "Appraisal contingency: [ ] Yes  [ ] No  [ ] Waived with gap coverage"),
            ("•", "Proposed closing date: [Date]"),
            ("•", "Other terms: [Inclusions, requests, escalation clause]"),
            ("•", "Overall strength: Strong / Moderate / Weak"),
        ]),
        ("FOR BUYERS — WINNING IN A MULTIPLE OFFER SITUATION", [
            ("•", "Come in strong: Offering below list price when there are multiple offers almost never works"),
            ("•", "Escalation clause: 'Buyer will beat any bona fide offer by $[X] up to a maximum of $[X]'"),
            ("•", "Limit contingencies where possible — but never waive financing/inspection blindly"),
            ("•", "Write a personal letter (check state fair housing rules first)"),
            ("•", "Use a local or known lender — listing agents know which lenders close on time"),
            ("•", "Match the seller's preferred closing date"),
            ("•", "Offer more earnest money — shows commitment and differentiation"),
        ]),
        ("CASH OFFER CONSIDERATIONS", [
            ("•", "Cash offers are often more competitive but not always necessary to win"),
            ("•", "If buyer has significant assets, some lenders offer 'cash-like' products (buy now, mortgage later)"),
            ("•", "Help buyer understand their true competition — in some markets conventional loans are accepted freely"),
        ]),
    ])

doc("04_NEGOTIATION/Counter_Offer_SOP.docx",
    "Counter-Offer SOP",
    "Real Estate Agent Operating System | Negotiation",
    [
        ("WHEN YOU RECEIVE AN OFFER", [
            ("•", "Call your client immediately (do not text or email first)"),
            ("•", "Walk through all terms: price, earnest money, contingencies, closing date, inclusions"),
            ("•", "Give your professional recommendation"),
            ("•", "Allow client to process — but set a reasonable decision timeline"),
        ]),
        ("COUNTER-OFFER STRATEGY", [
            "Counter-offer options:",
            ("•", "Accept as written — if terms are acceptable"),
            ("•", "Counter on price only — simplest; keeps other terms clean"),
            ("•", "Counter on multiple terms — address all concerns in one counter"),
            ("•", "Reject and request new offer — rarely recommended; cuts off negotiation"),
        ]),
        ("COUNTER-OFFER WRITING TIPS", [
            ("•", "Be specific: counter with exact numbers, not ranges"),
            ("•", "Set a short acceptance deadline: 24 hours is standard"),
            ("•", "Address one thing at a time when possible — minimizes points of friction"),
            ("•", "In writing: all counters must be in writing via your state's approved forms"),
        ]),
        ("PRESENTING A COUNTER TO YOUR CLIENT", [
            "'They countered at $[X] with [changes to terms]. Here's my analysis: [brief assessment]. My recommendation is [accept / counter at $[X] / reject for these reasons]. What are your thoughts?'",
        ]),
        ("WHAT TO DOCUMENT", [
            ("•", "Date and time of every offer, counter, and acceptance"),
            ("•", "All verbal conversations summarized in email immediately after"),
            ("•", "All written documents signed and in the transaction file"),
            ("•", "Disposition of every offer — whether accepted, countered, or rejected"),
        ]),
    ])

doc("04_NEGOTIATION/Inspection_Negotiation_Scripts.docx",
    "Inspection Negotiation Scripts",
    "Real Estate Agent Operating System | Negotiation",
    [
        ("UNDERSTANDING INSPECTION REQUESTS", [
            "After a home inspection, buyers typically request repairs, credits, or price reductions. Your job is to assess the legitimacy of each item and negotiate effectively for your client.",
        ]),
        ("CATEGORIZING INSPECTION ITEMS", [
            ("•", "Safety and structural: Roof failure, foundation issues, electrical hazards, HVAC failure — major items; legitimate to negotiate"),
            ("•", "Code violations: Items that were legal when built but require update — negotiate based on cost and significance"),
            ("•", "Deferred maintenance: Worn caulk, minor paint peeling, dated systems still functional — low priority; sellers often push back"),
            ("•", "Cosmetic: Scratched floors, outdated fixtures, normal wear — generally not negotiable"),
        ]),
        ("FOR BUYERS — REQUESTING REPAIRS/CREDIT", [
            "Script to buyer: 'The inspection found [X] items. I recommend we focus our request on [major items] and leave [minor items] alone. Asking for everything reduces your credibility and may put the deal at risk.'",
            "Request letter to seller: 'Following the inspection at [Address], buyer requests: (1) [Major item — specific repair or credit]; (2) [Major item]. Buyer is willing to accept a credit of $[X] in lieu of repairs. Buyer is not requesting repairs for minor maintenance items noted in the report.'",
        ]),
        ("FOR SELLERS — RESPONDING TO REPAIR REQUESTS", [
            "Script to seller: 'The buyer is asking for $[X] in repairs. Looking at the list: [Item A] is legitimate and I'd recommend addressing it. [Item B] is cosmetic and I recommend we decline. [Item C] we could offer a small credit instead of a repair — that's cleaner.'",
            ("•", "Counter with a credit: Often cleaner than making repairs — seller controls less; buyer chooses their own contractor"),
            ("•", "Decline selectively: 'Seller declines items [X, Y] as cosmetic/deferred maintenance but agrees to provide a $[X] closing credit for [specific item].'"),
        ]),
        ("WHEN NEGOTIATIONS BREAK DOWN", [
            "If buyer threatens to walk over inspection:",
            "'[Name], let's step back. Buying a perfect home isn't realistic — all homes have inspection findings. The question is whether the findings change the fundamental value of this home. The items the seller is declining to address are [assessed value]. Is this worth walking away from a home you love?'",
        ]),
    ])

print("✓ 04_NEGOTIATION complete")

# ── 05_TRANSACTION_MANAGEMENT ─────────────────────────────────────────────────
doc("05_TRANSACTION_MANAGEMENT/Contract_To_Close_SOP.docx",
    "Contract to Close SOP",
    "Real Estate Agent Operating System | Transaction Management",
    [
        ("DAY 1 — EXECUTED CONTRACT", [
            ("•", "[ ] Collect signed contract from all parties and send to all — buyer, seller, lender, title"),
            ("•", "[ ] Collect earnest money and deliver to escrow per contract terms"),
            ("•", "[ ] Create transaction file (digital and/or physical)"),
            ("•", "[ ] Log all key dates: inspection deadline, financing contingency, appraisal, closing"),
            ("•", "[ ] Introduce buyer to lender and title company if not already connected"),
            ("•", "[ ] Email both parties with a timeline summary"),
        ]),
        ("DAYS 1–7 — INSPECTION PERIOD", [
            ("•", "[ ] Schedule home inspection immediately (licensed inspector)"),
            ("•", "[ ] Attend inspection or instruct buyer to attend"),
            ("•", "[ ] Receive inspection report; review all items"),
            ("•", "[ ] Negotiate inspection items per contract and state law"),
            ("•", "[ ] Complete and sign inspection response before deadline"),
        ]),
        ("DAYS 7–21 — FINANCING AND APPRAISAL", [
            ("•", "[ ] Confirm buyer submitted full loan application to lender"),
            ("•", "[ ] Confirm appraisal ordered by lender"),
            ("•", "[ ] Receive appraisal — if at value, proceed; if low, see appraisal gap options"),
            ("•", "[ ] Receive conditional loan approval (CLC)"),
            ("•", "[ ] Clear all lender conditions: title, survey, HOA docs, etc."),
        ]),
        ("DAYS 21–30 — CLEAR TO CLOSE", [
            ("•", "[ ] Receive Clear to Close (CTC) from lender"),
            ("•", "[ ] Confirm closing date, time, and location with title"),
            ("•", "[ ] Schedule final walkthrough 24 hours before closing"),
            ("•", "[ ] Confirm buyer's closing funds wired to escrow (verify wire instructions by phone)"),
        ]),
        ("CLOSING DAY", [
            ("•", "[ ] Complete final walkthrough — note any issues"),
            ("•", "[ ] Attend closing or confirm parties prepared"),
            ("•", "[ ] All parties sign documents with title/escrow officer"),
            ("•", "[ ] Confirm funds received and disbursed"),
            ("•", "[ ] Keys transferred to buyer"),
            ("•", "[ ] Send congratulations message to clients"),
            ("•", "[ ] Request review and referral"),
        ]),
    ])

doc("05_TRANSACTION_MANAGEMENT/Transaction_Checklist.docx",
    "Transaction Checklist",
    "Real Estate Agent Operating System | Transaction Management",
    [
        ("CONTRACT DOCUMENTS", [
            ("•", "[ ] Purchase agreement — fully executed by all parties"),
            ("•", "[ ] All addenda and counteroffers — signed"),
            ("•", "[ ] Earnest money receipt from escrow"),
            ("•", "[ ] Buyer representation agreement (if buyer)"),
            ("•", "[ ] Listing agreement (if seller)"),
        ]),
        ("INSPECTION DOCUMENTS", [
            ("•", "[ ] Inspection report"),
            ("•", "[ ] Inspection response / repair agreement"),
            ("•", "[ ] Receipts for any agreed repairs"),
        ]),
        ("FINANCING DOCUMENTS", [
            ("•", "[ ] Loan estimate"),
            ("•", "[ ] Appraisal report"),
            ("•", "[ ] Conditional loan approval"),
            ("•", "[ ] Clear to close letter"),
            ("•", "[ ] Closing disclosure (3 days before closing)"),
        ]),
        ("TITLE AND CLOSING DOCUMENTS", [
            ("•", "[ ] Preliminary title report"),
            ("•", "[ ] HOA documents (if applicable)"),
            ("•", "[ ] Survey (if required)"),
            ("•", "[ ] Final walkthrough report"),
            ("•", "[ ] Settlement statement / HUD-1"),
            ("•", "[ ] Deed of trust / mortgage documents"),
        ]),
        ("POST-CLOSING", [
            ("•", "[ ] Copy of deed provided to buyer"),
            ("•", "[ ] Keys and garage openers delivered"),
            ("•", "[ ] Commission disbursement confirmed"),
            ("•", "[ ] Add to past client database for follow-up"),
            ("•", "[ ] Request Google/Zillow review within 48 hours"),
        ]),
    ])

doc("05_TRANSACTION_MANAGEMENT/Appraisal_Management_SOP.docx",
    "Appraisal Management SOP",
    "Real Estate Agent Operating System | Transaction Management",
    [
        ("BEFORE THE APPRAISAL", [
            ("•", "Prepare a packet for the appraiser: subject property details, your CMA, list of upgrades"),
            ("•", "If listing agent: provide a list of recent upgrades (kitchen remodel, roof, HVAC) with dates and costs"),
            ("•", "Ensure the home is clean and accessible for the appraiser"),
            ("•", "Be present at the appraisal (or send a representative) to answer questions"),
        ]),
        ("WHEN THE APPRAISAL COMES IN AT VALUE", [
            "Notify both parties immediately. Confirm lender received the report. Move to next step (financing conditions).",
        ]),
        ("WHEN THE APPRAISAL COMES IN LOW", [
            "A low appraisal means the home appraised below the agreed purchase price. Options:",
            ("•", "Option 1 — Renegotiate price: Seller reduces to appraised value. Most common resolution."),
            ("•", "Option 2 — Buyer pays the gap: Buyer pays the difference between appraised value and purchase price out of pocket ('appraisal gap coverage')."),
            ("•", "Option 3 — Split the difference: Seller reduces price partway; buyer covers the remainder."),
            ("•", "Option 4 — Dispute the appraisal: Request a reconsideration of value with your CMA and additional comps. Must be submitted through lender within their timeline."),
            ("•", "Option 5 — Cancel: If buyer has an appraisal contingency, they may exit without penalty."),
        ]),
        ("APPRAISAL DISPUTE PROCESS", [
            "1. Review the appraisal report — identify any errors (square footage, room count, outdated comps)",
            "2. Gather 3–5 recent comps the appraiser missed or underweighted",
            "3. Write a formal reconsideration request through the lender",
            "4. Allow 5–10 business days for appraiser to respond",
            "Note: Only factual errors and additional market data can be submitted — not an argument about opinion.",
        ]),
    ])

doc("05_TRANSACTION_MANAGEMENT/Closing_Day_Checklist.docx",
    "Closing Day Checklist",
    "Real Estate Agent Operating System | Transaction Management",
    [
        ("FOR BUYERS — CLOSING DAY PREPARATION", [
            ("•", "[ ] Government-issued photo ID (two forms often required)"),
            ("•", "[ ] Certified funds / wire confirmation (verify wire instructions by phone with title company)"),
            ("•", "[ ] Cashier's check if required (confirm exact amount from closing disclosure)"),
            ("•", "[ ] Copies of all required insurance (homeowners, flood if required)"),
            ("•", "[ ] Final walkthrough completed and satisfactory"),
            ("•", "[ ] Any outstanding items from lender submitted"),
        ]),
        ("FINAL WALKTHROUGH CHECKLIST", [
            ("•", "[ ] All agreed repairs completed — obtain receipts"),
            ("•", "[ ] All personal property included in sale is present"),
            ("•", "[ ] All personal property excluded from sale is removed"),
            ("•", "[ ] All appliances in working order"),
            ("•", "[ ] No new damage since last viewing"),
            ("•", "[ ] Keys, garage openers, mailbox keys available for transfer"),
        ]),
        ("AT THE CLOSING TABLE", [
            "1. Review the closing disclosure with your client before signing — confirm all numbers match what was expected",
            "2. Sign all documents with the title/escrow officer",
            "3. Confirm funding (lender wires funds to escrow)",
            "4. Deed is recorded — keys are transferred",
        ]),
        ("POST-CLOSING AGENT ACTIONS", [
            ("•", "Text/call client: 'Congratulations! You officially own [Address]! Here's what to do in your first week: [change locks, update address, schedule any movers]'"),
            ("•", "Send handwritten congratulations card within 48 hours"),
            ("•", "Request review: 'If you've been happy with my service, a Google or Zillow review means the world to me. Here's the link: [link]'"),
            ("•", "Add to past client CRM — set 1-year follow-up reminder"),
        ]),
    ])

print("✓ 05_TRANSACTION_MANAGEMENT complete")

# ── 06_CLIENT_COMMUNICATION ───────────────────────────────────────────────────
doc("06_CLIENT_COMMUNICATION/Email_Templates.docx",
    "Email Templates",
    "Real Estate Agent Operating System | Client Communication",
    [
        ("NEW BUYER LEAD — FIRST RESPONSE", [
            "Subject: Re: [Property or Area They Inquired About]",
            "Hi [Name], thanks for reaching out! I specialize in [Area/Neighborhood] and would love to help you find the right home.",
            "A few quick questions so I can be most helpful:",
            ("•", "What's your timeline for moving?"),
            ("•", "Have you been pre-approved for a mortgage?"),
            ("•", "What areas or price range are you focused on?"),
            "Happy to set up a buyer consultation — it's free and no commitment. Here's my calendar: [link]. Look forward to connecting!",
        ]),
        ("POST-LISTING APPOINTMENT (Did Not Sign)", [
            "Subject: Great Meeting You — [Address]",
            "Hi [Name], it was a pleasure meeting you and learning about [Property]. I want you to feel 100% confident in whoever you choose to list with.",
            "Attached is the CMA we discussed. If you have any questions or want to talk through your options further, I'm always available. I hope to earn your business.",
        ]),
        ("OFFER ACCEPTED — BUYER", [
            "Subject: CONGRATULATIONS — Offer Accepted on [Address]!",
            "Hi [Name], thrilling news — the seller has accepted your offer on [Address]! Here's what happens next:",
            ("•", "Earnest money due by: [Date]"),
            ("•", "Home inspection: Schedule immediately — I recommend [Inspector Name]"),
            ("•", "Financing contingency deadline: [Date]"),
            ("•", "Closing date: [Date]"),
            "I'll be with you every step of the way. Let's celebrate this milestone — more details to come!",
        ]),
        ("LISTING ACTIVITY UPDATE", [
            "Subject: Weekly Update — [Address] | Week [X] Active",
            "Hi [Name], here's your update for this week:",
            ("•", "Showings: [X] this week | [X] total"),
            ("•", "Open house visitors: [X]"),
            ("•", "Online views (Zillow): [X] | Average time on listing: [X] minutes"),
            ("•", "Agent feedback: [Summary]",),
            "My assessment: [2–3 sentences]. Questions? Call me anytime.",
        ]),
        ("REFERRAL THANK YOU", [
            "Subject: Thank You for the Referral — Means More Than You Know",
            "Hi [Name], I heard that [Client] reached out to me because of your recommendation. That truly means the world.",
            "Referrals are the foundation of my business, and knowing you trusted me enough to recommend me to someone you care about is the greatest compliment.",
            "I'll make sure [Client] is taken great care of. If there's ever anything I can do for you, please don't hesitate to reach out.",
        ]),
    ])

doc("06_CLIENT_COMMUNICATION/Text_Templates.docx",
    "Text Message Templates",
    "Real Estate Agent Operating System | Client Communication",
    [
        ("NEW LEAD — IMMEDIATE RESPONSE", [
            ("•", "'Hi [Name], this is [Your Name] from [Brokerage]. I saw you were interested in [Address / Area]. Happy to help — are you available for a quick call?'"),
        ]),
        ("SHOWING CONFIRMATION", [
            ("•", "'Hi [Name], just confirming your showings tomorrow: [Time] — [Address 1] and [Time] — [Address 2]. See you then! Any questions before we go?'"),
        ]),
        ("POST-SHOWING CHECK-IN", [
            ("•", "'Hi [Name], how did you feel about [Address] today? Still thinking about it, or should I keep looking?'"),
        ]),
        ("OFFER SUBMISSION", [
            ("•", "'Hi [Name], offer has been submitted on [Address] at $[X]. The seller's agent expects a response by [time]. I'll update you the moment I hear back!'"),
        ]),
        ("OFFER ACCEPTED", [
            ("•", "'[Name] — YOUR OFFER WAS ACCEPTED! Calling you now. So excited for you!'"),
        ]),
        ("INSPECTION REMINDER", [
            ("•", "'Hi [Name], quick reminder — your inspection is scheduled for [Date] at [Time] at [Address]. Please plan to be there for the last 30 minutes. Your inspector will explain everything!'"),
        ]),
        ("CLOSING COUNTDOWN", [
            ("•", "'Hi [Name], 3 days until closing! Reminder to confirm your wire transfer. Don't forget to verify the wiring instructions by calling the title company directly before sending. See you [Date]!'"),
        ]),
        ("POST-CLOSING", [
            ("•", "'Congratulations, [Name]! You're officially a homeowner! So honored to have been part of this. Welcome home!'"),
        ]),
        ("SOI MARKET CHECK-IN", [
            ("•", "'Hi [Name], just thinking of you! The [Area] market has been [active / shifting / strong] lately. If you ever want to know what your home is worth or what's happening in the neighborhood, I'm always here. Hope all is well!'"),
        ]),
    ])

doc("06_CLIENT_COMMUNICATION/Weekly_Update_Scripts.docx",
    "Weekly Update Scripts",
    "Real Estate Agent Operating System | Client Communication",
    [
        ("BUYER WEEKLY CHECK-IN", [
            "'Hi [Name], quick update on your search. New listings this week in your criteria: [X homes]. I'm watching [specific property] closely — it just had a price drop and could be worth a look. Your MLS alerts are active and I'll flag anything that stands out. Any changes to your must-haves or timeline?'",
        ]),
        ("SELLER WEEKLY ACTIVITY REPORT CALL", [
            "Opening: 'Hi [Name], calling with your weekly update on [Address].'",
            ("•", "Showings: [X] showings this week; [X] total to date"),
            ("•", "Feedback: 'The feedback I've been hearing is [summary]. The most common theme is [price/condition/location].'"),
            ("•", "Market activity: '[X] similar homes listed / sold in your price range this week.'"),
            ("•", "Online metrics: [Views on Zillow, saves, inquiries]"),
            "Close: 'Based on all of this, I want to share my recommendation: [continue / adjust price / enhance marketing]. What are your thoughts?'",
        ]),
        ("TRANSACTION WEEKLY UPDATE", [
            "'Hi [Name], checking in with a transaction update. We're on track for your [date] closing. Here's where things stand:'",
            ("•", "Inspection: [Status]"),
            ("•", "Lender: [Status — appraisal, conditions, CTC expected by date]"),
            ("•", "Title: [Status]"),
            ("•", "Next deadline: [Date and action required]"),
            "No action needed from you right now — I'll reach out the moment anything changes.",
        ]),
    ])

doc("06_CLIENT_COMMUNICATION/Difficult_Conversation_Scripts.docx",
    "Difficult Conversation Scripts",
    "Real Estate Agent Operating System | Client Communication",
    [
        ("SCENARIO: CLIENT WANTS TO SIGNIFICANTLY OVERPRICE THE LISTING", [
            "'[Name], I respect that you have a number in mind, and I want to get you as much as possible. But I'd be doing you a disservice if I didn't share this: homes priced above market sit longer, see more price reductions, and ultimately sell for less than homes priced correctly from day one. I've seen it many times. My recommendation is $[X]. Can I show you the data behind that?'",
        ]),
        ("SCENARIO: BUYER WANTS TO OFFER FAR BELOW ASKING IN A HOT MARKET", [
            "'I hear you — you want the best deal possible. Let me be honest about what's happening in this market: homes like this are [selling in X days / receiving multiple offers]. An offer at $[X] has a [very low] chance of being accepted. It might also signal to the seller that you're not a serious buyer. My recommendation is $[X] — still below asking, but competitive. What do you think?'",
        ]),
        ("SCENARIO: CLIENT IS UNHAPPY ABOUT HOW THE TRANSACTION IS GOING", [
            "'[Name], I hear you, and I'm taking your concerns seriously. Let me address each one: [specific response]. Here's what I'm doing right now to move this forward: [actions]. I appreciate your patience — I know this process is stressful, and my job is to protect your interests every step of the way.'",
        ]),
        ("SCENARIO: CLIENT WANTS TO CANCEL THE TRANSACTION", [
            "'Before we go down that path, let's make sure we understand what happens. [If buyer]: You may lose your earnest money of $[X]. [If seller]: You may be subject to specific performance or damages. Let's talk through what's driving this and whether there's a way to resolve it first. What's the core issue?'",
        ]),
        ("SCENARIO: DEAL IS FALLING APART AT THE LAST MINUTE", [
            "'[Name], I want to be completely transparent: we're facing a serious challenge. [Explain issue]. Here are the options as I see them: [Option A / Option B / Option C]. My recommendation is [option] because [reason]. Whatever you decide, I'm with you. What do you want to do?'",
        ]),
    ])

print("✓ 06_CLIENT_COMMUNICATION complete")

# ── 07_COMPLIANCE_LEGAL ───────────────────────────────────────────────────────
doc("07_COMPLIANCE_LEGAL/Fair_Housing_Compliance_Guide.docx",
    "Fair Housing Compliance Guide",
    "Real Estate Agent Operating System | Compliance & Legal",
    [
        ("THE FAIR HOUSING ACT", [
            "The Fair Housing Act prohibits discrimination in the sale, rental, or financing of housing based on:",
            ("•", "Race"), ("•", "Color"), ("•", "National origin"), ("•", "Religion"),
            ("•", "Sex"), ("•", "Familial status (families with children under 18)"),
            ("•", "Disability"),
            "Many states and localities add additional protected classes (marital status, sexual orientation, gender identity, source of income). Know your state's laws.",
        ]),
        ("WHAT AGENTS MUST NEVER DO", [
            ("•", "Steer buyers toward or away from neighborhoods based on protected characteristics"),
            ("•", "Describe neighborhoods using coded or discriminatory language"),
            ("•", "Treat clients differently in providing information, access, or service based on protected class"),
            ("•", "Refuse to show homes or accept offers based on buyer's protected characteristics"),
            ("•", "Advertise properties with language that implies preference or limitation by protected class"),
        ]),
        ("WHAT SELLERS CANNOT INSTRUCT YOU TO DO", [
            "Sellers may not direct you to reject buyers based on any protected class. If a seller gives instructions that violate the Fair Housing Act, you must refuse and document the refusal. If they persist, you should consider withdrawing from the listing.",
        ]),
        ("MARKETING AND ADVERTISING", [
            ("•", "Never use: 'ideal for couples,' 'quiet neighborhood' (code for no children), 'walking distance to church/synagogue/mosque'"),
            ("•", "Always use: 'open to all buyers,' neutral language describing property features"),
            ("•", "Include the Equal Housing Opportunity logo in all advertising"),
        ]),
        ("BUYER LETTERS / PERSONAL NOTES", [
            "Personal letters from buyers to sellers are legal in most states, but must be offered equally to all buyers and not encourage sellers to discriminate. Use caution and follow your brokerage policy. Some agents and sellers now refuse to accept or read personal letters.",
        ]),
        ("DOCUMENTATION", [
            ("•", "Keep records of all offers presented to sellers"),
            ("•", "Document all buyer showings and properties shown"),
            ("•", "Save all advertising materials"),
            ("•", "Document any seller instructions that you refused"),
        ]),
    ])

doc("07_COMPLIANCE_LEGAL/Disclosure_Requirements_Guide.docx",
    "Disclosure Requirements Guide",
    "Real Estate Agent Operating System | Compliance & Legal",
    [
        ("IMPORTANT NOTICE", [
            "Disclosure requirements vary significantly by state. This guide provides a general framework. Always follow your state's specific disclosure laws and your brokerage's requirements. Consult a licensed attorney when in doubt.",
        ]),
        ("SELLER DISCLOSURE REQUIREMENTS (General)", [
            ("•", "Material defects: Known conditions that would affect a buyer's decision or the property value"),
            ("•", "Prior repairs: Major repairs made to the property (roof, foundation, plumbing, electrical)"),
            ("•", "Water damage or mold: Known history of leaks, water intrusion, or mold remediation"),
            ("•", "HOA: All association rules, fees, special assessments, and pending litigation"),
            ("•", "Environmental hazards: Lead paint (pre-1978 homes federal requirement), asbestos, radon, underground storage tanks"),
            ("•", "Death on property: Some states require disclosure; others do not — know your state's law"),
        ]),
        ("AGENT DISCLOSURE OBLIGATIONS", [
            ("•", "Agency relationship: Disclose who you represent in writing (buyer, seller, dual agent, transaction broker)"),
            ("•", "Conflict of interest: Disclose if you have any personal or financial interest in the property"),
            ("•", "Known defects: If you become aware of material defects, you must disclose even if the seller hasn't"),
        ]),
        ("LEAD-BASED PAINT DISCLOSURE", [
            "Required by federal law for homes built before 1978:",
            ("•", "Sellers must disclose known lead paint hazards"),
            ("•", "Buyers must receive the EPA pamphlet 'Protect Your Family from Lead in Your Home'"),
            ("•", "Buyers have a 10-day period to conduct lead paint inspection"),
            ("•", "Disclosure must be completed before contract is signed"),
        ]),
        ("DUAL AGENCY", [
            "Dual agency occurs when one agent represents both buyer and seller. In states where allowed, it must be disclosed in writing to both parties. Limitations include inability to advocate fully for either party. Some agents and brokerages avoid dual agency entirely.",
        ]),
    ])

doc("07_COMPLIANCE_LEGAL/Agency_Relationship_Guide.docx",
    "Agency Relationship Guide",
    "Real Estate Agent Operating System | Compliance & Legal",
    [
        ("TYPES OF AGENCY RELATIONSHIPS", [
            ("•", "Buyer's Agent: Represents the buyer exclusively; fiduciary duty to buyer"),
            ("•", "Seller's Agent / Listing Agent: Represents the seller exclusively; fiduciary duty to seller"),
            ("•", "Dual Agent: Represents both buyer and seller in the same transaction (where legally permitted)"),
            ("•", "Transaction Broker / Facilitator: Assists both parties without full fiduciary duty to either (state-specific)"),
        ]),
        ("FIDUCIARY DUTIES TO YOUR CLIENT", [
            ("•", "Loyalty: Put client's interests above all others, including your own commission"),
            ("•", "Confidentiality: Do not share client's motivations, price ceiling, or deadline"),
            ("•", "Disclosure: Share all material information that affects client's decision"),
            ("•", "Obedience: Follow client's legal instructions"),
            ("•", "Reasonable Care: Apply professional skill and knowledge"),
            ("•", "Accounting: Properly handle all funds"),
        ]),
        ("AGENCY DISCLOSURE REQUIREMENTS", [
            ("•", "Most states require written agency disclosure before substantive discussions"),
            ("•", "Provide the state-required agency disclosure form at first meeting"),
            ("•", "Explain clearly who you represent and what your duties are"),
            ("•", "Get signed acknowledgment"),
        ]),
        ("DUAL AGENCY RISKS", [
            "Dual agency creates inherent conflict. As a dual agent, you cannot:",
            ("•", "Advise either party on negotiation tactics against the other"),
            ("•", "Share confidential information of one party with the other"),
            "If you take on dual agency: disclose immediately, get written consent from both parties, and document everything.",
        ]),
    ])

doc("07_COMPLIANCE_LEGAL/Record_Keeping_Policy.docx",
    "Record Keeping Policy",
    "Real Estate Agent Operating System | Compliance & Legal",
    [
        ("REQUIRED RETENTION PERIODS", [
            ("•", "Transaction files (contracts, disclosures, all related docs): 3–7 years (check your state — most require 5 years minimum)"),
            ("•", "Trust account records: 3–5 years"),
            ("•", "Advertising and marketing materials: 3 years"),
            ("•", "Agency disclosure acknowledgments: Life of transaction + 3 years minimum"),
            ("•", "Lead paint disclosures: 3 years after sale"),
        ]),
        ("WHAT TO KEEP IN EVERY TRANSACTION FILE", [
            ("•", "Listing agreement or buyer representation agreement"),
            ("•", "All offers, counteroffers, and addenda"),
            ("•", "Executed purchase agreement"),
            ("•", "Agency disclosures — signed by all parties"),
            ("•", "Inspection reports and responses"),
            ("•", "Lead paint disclosure (if pre-1978 home)"),
            ("•", "Appraisal report"),
            ("•", "Closing settlement statement"),
            ("•", "All written communications with parties"),
        ]),
        ("DIGITAL RECORD KEEPING", [
            ("•", "Organize by address and transaction year: [Year]/[Address]/[Folder structure]"),
            ("•", "Use cloud storage with automatic backup"),
            ("•", "Store signed documents as PDFs — never only as unsigned drafts"),
            ("•", "Confirm your brokerage record-keeping requirements — most brokers maintain master files"),
        ]),
        ("UPON LEAVING A BROKERAGE", [
            "When changing brokerages, all transaction files typically remain with the brokerage. Ensure you have personal copies of your own business records and client contact information (check your state's rules on this).",
        ]),
    ])

print("✓ 07_COMPLIANCE_LEGAL complete")

# ── XLSX FILES ────────────────────────────────────────────────────────────────
# 1. Lead Generation CRM
wb=Workbook()
ws=wb.active; ws.title="Lead Pipeline"
for col,w in zip("ABCDEFGHI",[25,20,15,15,20,20,15,15,25]):
    ws.column_dimensions[col].width=w
hrow(ws,1,list(range(1,10)),["Name","Email","Phone","Source","Status","Area Interest","Price Range","Timeline","Last Touch"])
rows=[
    ("Sarah Mitchell","sarah@email.com","555-0201","Open House","Hot","[Neighborhood A]","$400-500K","0-3 months","Jan 10"),
    ("Tom & Lisa Park","tpark@email.com","555-0202","Zillow","Warm","[Neighborhood B]","$550-700K","3-6 months","Jan 8"),
    ("Carlos Rivera","crivera@email.com","555-0203","Referral","Hot","[Neighborhood A]","$300-400K","Immediate","Jan 12"),
    ("Jennifer Watts","jwatts@email.com","555-0204","SOI","Cold","[Neighborhood C]","$500-650K","6-12 months","Dec 20"),
    ("James Chen","jchen@email.com","555-0205","Facebook Ad","Warm","[Neighborhood B]","$350-450K","3-6 months","Jan 9"),
]
for i,r in enumerate(rows,2):
    drow(ws,i,list(range(1,10)),list(r),LGR if i%2==0 else WHT)
ws2=wb.create_sheet("Status Legend")
hrow(ws2,1,[1,2],["Status","Description"],ACC,WHT)
for i,r in enumerate([("Hot","Pre-approved, actively looking, 0-60 days"),
    ("Warm","Engaged, looking but not urgent, 60-180 days"),
    ("Cold","Early stage, 6-12+ months or uncertain"),
    ("Nurture","Long-term follow-up — annual or semi-annual"),
    ("Active Buyer","Currently showing/writing offers"),("Under Contract","Deal in progress"),
    ("Closed","Transaction complete"),("Dead","No longer interested")],2):
    drow(ws2,i,[1,2],list(r),LGR if i%2==0 else WHT)
wb.save(BASE+"01_LEAD_GENERATION/Lead_Generation_CRM.xlsx")
print("  ✓ 01_LEAD_GENERATION/Lead_Generation_CRM.xlsx")

# 2. Buyer Pipeline Tracker
wb2=Workbook()
ws=wb2.active; ws.title="Buyer Pipeline"
for col,w in zip("ABCDEFGH",[25,15,20,15,20,15,15,25]):
    ws.column_dimensions[col].width=w
hrow(ws,1,list(range(1,9)),["Buyer Name","Pre-Approved","Lender","Budget","Search Area","Status","Homes Shown","Notes"])
for i,r in enumerate([
    ("Sarah Mitchell","Yes","[Lender]","$450K","[Area A]","Actively Showing","8","Has offer in mind on 123 Main"),
    ("Tom & Lisa Park","Yes","[Lender]","$650K","[Area B]","Buyer Consult Done","3","Looking for 4BR with yard"),
    ("Carlos Rivera","In Process","[Lender]","$380K","[Area A]","Pre-Approval Pending","0","Strong motivation"),
],2):
    drow(ws,i,list(range(1,9)),list(r),LGR if i%2==0 else WHT)
wb2.save(BASE+"02_BUYER_SERVICES/Buyer_Pipeline_Tracker.xlsx")
print("  ✓ 02_BUYER_SERVICES/Buyer_Pipeline_Tracker.xlsx")

# 3. Listing Pipeline Tracker
wb3=Workbook()
ws=wb3.active; ws.title="Listing Pipeline"
for col,w in zip("ABCDEFGHI",[25,20,12,12,12,15,12,15,25]):
    ws.column_dimensions[col].width=w
hrow(ws,1,list(range(1,10)),["Address","Seller Name","List Price","DOM","Showings","Status","Open Houses","Offers","Notes"])
for i,r in enumerate([
    ("456 Oak Ave","Johnson Family","$525,000","14","12","Active","2","1 received","Counter in progress"),
    ("789 Pine St","Rodriguez","$389,000","5","6","Active","1","None","Strong activity week 1"),
    ("321 Elm Dr","Williams","$695,000","28","9","Price Reduction","3","None","Reduced $20K Jan 10"),
    ("100 Maple Ct","Chen","$0","0","0","Pre-Listing","0","None","Listing appt Jan 20"),
],2):
    drow(ws,i,list(range(1,10)),list(r),LGR if i%2==0 else WHT)
wb3.save(BASE+"03_SELLER_SERVICES/Listing_Pipeline_Tracker.xlsx")
print("  ✓ 03_SELLER_SERVICES/Listing_Pipeline_Tracker.xlsx")

print("PART 2 DONE")
