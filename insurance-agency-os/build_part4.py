#!/usr/bin/env python3
"""Insurance Agency OS - Part 4: Bonuses, PDFs, PPTX, Manifest, ZIP"""
import os, csv, json, zipfile
from docx import Document
from docx.shared import Pt, RGBColor
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor as PRGB
from pptx.enum.text import PP_ALIGN

BASE = "/home/user/oqul-phase55-production/insurance-agency-os/Ultimate_Insurance_Agency_Operating_System/"
NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"

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

def write_csv(path, headers, rows):
    with open(BASE+path, "w", newline="", encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
    print(f"  ✓ {path}")

# ─── 11_BONUSES ────────────────────────────────────────────────────────────────
p11 = "11_BONUSES/"

# 365 Social Media Captions
categories = [
    ("Insurance Education", [
        "Your homeowner's insurance covers your house structure — but your belongings inside require a separate 'personal property' coverage. Do you know your limit?",
        "Flood insurance is NOT included in standard homeowner's policies. If you live near water or in a low-lying area, you need a separate flood policy.",
        "Liability coverage on your auto policy protects other people if YOU cause an accident. Make sure your limits are high enough.",
        "An umbrella policy gives you an extra $1-2 million of liability coverage on top of your home and auto policies — for about $200-$300/year.",
        "Your credit score affects your insurance rates in most states. Improving your credit can directly lower your premiums.",
        "Term life insurance is the most affordable way to protect your family's income — a 20-year term policy for a healthy 35-year-old can cost less than your morning coffee.",
        "The 'replacement cost' vs. 'actual cash value' debate: Replacement cost pays to replace your item new. ACV deducts depreciation. Always choose replacement cost if you can.",
        "Comprehensive auto insurance covers non-collision incidents: theft, vandalism, weather damage, and hitting an animal.",
        "Collision coverage pays for damage to YOUR car in an accident, regardless of fault.",
        "Renters insurance is typically $15-$30/month and protects all your belongings. Yet 60% of renters have none.",
        "A 'named perils' policy covers only the perils specifically listed. An 'open perils' or 'all-risk' policy covers everything EXCEPT what's excluded.",
        "Disability insurance replaces 60-70% of your income if you can't work. It's the most overlooked coverage in America.",
        "Medicare doesn't cover everything. A Medicare supplement (Medigap) policy fills the gaps left by Original Medicare.",
        "Workers compensation insurance is required in most states for businesses with employees. It covers medical bills and lost wages for work injuries.",
        "General liability insurance protects your business if a customer is injured on your premises or by your product.",
        "Business interruption insurance covers lost income if your business must close temporarily due to a covered loss.",
        "Cyber liability insurance protects businesses from data breach costs, ransomware, and cyber fraud — now essential for any business that stores customer data.",
        "A BOP (Business Owner's Policy) bundles general liability + commercial property into one affordable policy — perfect for small businesses.",
        "E&O (Errors & Omissions) insurance protects professionals if a client claims financial harm from a mistake. Essential for agents, consultants, and advisors.",
        "Directors & Officers (D&O) insurance protects board members and executives from lawsuits related to their management decisions.",
        "Employment Practices Liability (EPLI) protects businesses against claims of wrongful termination, harassment, and discrimination.",
        "Long-term care insurance covers nursing home, assisted living, and in-home care costs — the average nursing home costs $100,000+ per year.",
        "An annuity converts a lump sum into a guaranteed income stream — useful for retirement planning.",
        "Inland marine insurance covers valuable property that moves or is stored off-premises: equipment, tools, fine art, and electronics.",
        "Professional liability (malpractice) insurance is required for healthcare professionals and highly recommended for all licensed professionals.",
        "Key person insurance protects a business if a critical employee (owner or star performer) dies or becomes disabled.",
        "Buy-sell insurance funds a buyout agreement between business partners if one partner dies or becomes disabled.",
        "Health insurance deductibles, copays, and out-of-pocket maximums are different things — understanding all three helps you plan healthcare costs.",
        "The ACA marketplace offers subsidized health insurance to individuals who don't have employer coverage. Open enrollment is November-January.",
        "Life insurance proceeds pass to beneficiaries income-tax-free — one of the most powerful wealth transfer tools available.",
        "The rule of thumb for life insurance: 10-12x your annual income in coverage.",
        "Short-term disability covers you for the first 90-180 days of disability. Long-term covers beyond that. Many people need both.",
        "Guaranteed issue life insurance requires no medical exam — great for seniors or those with pre-existing conditions.",
        "Variable life insurance has a cash value component tied to market performance. It's insurance AND investment.",
        "Whole life insurance builds cash value you can borrow against tax-free. It's permanent coverage with a savings component.",
        "Universal life insurance offers flexible premiums and a cash value component that grows at a declared interest rate.",
    ]),
    ("Agent Value & Trust", [
        "I'm not just an insurance agent — I'm an independent agent. That means I shop multiple carriers to find you the best deal.",
        "The best time to review your insurance is BEFORE something happens. Don't wait for a claim to discover a coverage gap.",
        "My goal isn't to sell you the most expensive policy. My goal is to make sure you have exactly the coverage you need — nothing more, nothing less.",
        "When you call me, you reach me. Not a call center. Not a robot. A real person who knows your policy.",
        "Independent agents like me represent multiple carriers — we work for YOU, not for any single insurance company.",
        "I've helped [X] clients protect their homes, businesses, and families. Let me help you too.",
        "If you have a claim, I'm your advocate. I'll call the adjuster, follow up, and make sure you're treated fairly.",
        "Insurance is complicated — that's why you need someone in your corner who understands it. That's me.",
        "I specialize in finding coverage gaps people don't know they have — until it's too late.",
        "The value I provide goes far beyond a quote. I'm here to educate, protect, and advocate for your interests.",
        "My clients don't just buy insurance from me — they buy peace of mind, knowing they're covered when it matters most.",
        "Shopping insurance online is easy — understanding what you're buying is hard. That's where I come in.",
        "I go to work for you before you even need me — reviewing your coverage annually to make sure it still fits your life.",
        "You wouldn't go to surgery without a doctor. You shouldn't handle complex insurance needs without a professional.",
        "Commission transparency: I'm paid by the insurance carriers, so my advice and service cost you nothing extra.",
        "I've seen what happens when families are underinsured after a major loss. I've made it my mission to prevent that.",
        "My favorite call to make is the one after a claim — telling my client the carrier is paying in full.",
        "Most people spend more time shopping for a TV than reviewing their insurance. Let me make your next review easy.",
        "I've seen policies from 12 different carriers this week. Do you know which one is best for your specific situation? I do.",
        "Referrals are my #1 source of new business. If I've served you well, please share my name.",
        "I specialize in making the complex simple. Insurance has a lot of fine print — I translate it for you.",
        "I'm not in this for the transaction. I'm in this for the long-term relationship.",
        "When rates change at renewal, I'm already shopping the market before you know there's a problem.",
        "My job is to know your situation better than you know your own insurance. Annual reviews make that possible.",
        "I review every client's coverage annually — not because I have to, but because it's the right thing to do.",
        "The policies I recommend are the ones I would buy for my own family. That's my personal standard.",
        "I serve clients across home, auto, life, and commercial lines — one call for everything you need.",
        "The insurance industry isn't always transparent. I am. I'll always tell you the truth about your coverage.",
        "Behind every insurance policy is a person, a family, or a business counting on it. I don't take that lightly.",
        "Your insurance should evolve as your life evolves. That's why an annual review with a trusted agent matters.",
        "I'm available when you need me — not just at renewal time.",
        "My reputation is built one client, one claim, and one renewal at a time. I protect it fiercely.",
        "Most agents disappear after the sale. I show up all year long.",
        "When you refer your friends and family to me, you're trusting me with the people you love most. I honor that.",
        "The question isn't whether you can afford insurance — it's whether you can afford to go without it.",
        "I didn't choose insurance because it was easy. I chose it because helping people protect what matters most is meaningful work.",
    ]),
    ("Home & Auto Tips", [
        "Raise your deductible from $500 to $1,000 and you could save 10-15% on your home insurance premium.",
        "Installing a home security system can qualify you for a 5-15% discount on your homeowner's insurance.",
        "Bundle your home and auto with the same carrier and you'll typically save 10-25% on both policies.",
        "Update your home insurance after ANY major renovation. An uninsured improvement is a financial risk.",
        "Review your home's 'dwelling coverage' limit annually — construction costs increase every year.",
        "If you have high-value jewelry, art, or collectibles, ask about a scheduled personal property endorsement.",
        "Teen driver on your policy? Driver's Ed completion and good grades can significantly reduce your premium.",
        "If your vehicle is worth less than $5,000, consider dropping comprehensive and collision to reduce your premium.",
        "Gap insurance covers the difference between what you owe on a financed vehicle and its actual cash value after a total loss.",
        "New car replacement coverage pays for a brand-new vehicle (not depreciated value) if yours is totaled in the first few years.",
        "Rideshare coverage is required if you drive for Uber or Lyft — your personal auto policy won't cover you during those trips.",
        "Water backup coverage protects against sewer or drain backups, which are excluded from most standard home policies.",
        "Identity theft protection is now available as a home insurance endorsement — for a few dollars a month.",
        "Snap photos of every room in your home and store them in the cloud. This simplifies claims dramatically.",
        "If you have a pool, trampoline, or dog, talk to your agent about additional liability coverage.",
        "Completing a defensive driving course can qualify you for an auto insurance discount in most states.",
        "Paying your premium annually instead of monthly can save you 3-8% in installment fees.",
        "Multi-car discounts can save 10-15% per vehicle when insuring multiple cars on one policy.",
        "Regularly review your auto policy's liability limits — the minimum required by your state is rarely enough.",
        "Before buying a new or used car, ask your agent for an insurance quote. Different makes and models vary widely in cost.",
        "The garaging location of your vehicle affects your rate — a city ZIP code typically costs more than a suburban one.",
        "Anti-theft devices, anti-lock brakes, and airbags all qualify for discounts with many auto carriers.",
        "Uninsured motorist coverage protects you if you're hit by a driver with no insurance — don't skip it.",
        "Medical payments coverage (MedPay) covers you and your passengers' medical bills after an accident, regardless of fault.",
        "Personal injury protection (PIP) is required in no-fault states and covers medical costs + lost wages.",
        "Your home insurance won't cover a home-based business loss. Ask about a business owner's endorsement.",
        "Check your home insurance for 'ordinance or law' coverage — it pays to bring your repaired home up to current building codes.",
        "Earthquake and flood are almost always excluded from standard homeowner's policies — research your risk.",
        "Review your 'loss of use' coverage — it pays for temporary housing while your home is being repaired after a covered loss.",
        "Vacant home insurance is a separate policy required if your home will be empty for 30+ days.",
        "Inflation guard endorsements automatically increase your dwelling limit each year to keep pace with construction costs.",
        "When buying a home, ask about the prior claim history — frequent prior claims can affect your policy availability.",
        "Trees and landscaping: a standard policy typically covers removal if a tree falls on a covered structure, but not on just your lawn.",
        "Trampoline liability is a real concern — some carriers won't insure homes with trampolines without a net enclosure.",
        "Your home office equipment may not be covered under your homeowner's policy. Ask about a business property rider.",
        "Most home policies include a 'liability' portion that covers injuries to visitors on your property. Know your limit.",
    ]),
    ("Life & Health Insurance", [
        "Life insurance: Don't wait until you're sick to apply. The healthiest years of your life are the best time to lock in low rates.",
        "If your employer offers life insurance, the coverage often ends when your job does. Supplement with your own policy.",
        "A 20-year term life policy for a 30-year-old non-smoker can cost as little as $20-$30/month for $500,000 in coverage.",
        "Converting a term policy to permanent life insurance is usually possible without a new medical exam — check your policy.",
        "If you're a business owner, life insurance can fund a buy-sell agreement — protecting your business partners if you die.",
        "Beneficiary designations override your will. Review them every few years, especially after major life events.",
        "Cash value life insurance can supplement retirement income through tax-advantaged policy loans.",
        "The 'insurable interest' requirement means you can only buy life insurance on people you have a financial relationship with.",
        "Most life insurance policies have a 2-year contestability period — if you misrepresent health info, the carrier can deny claims.",
        "A 'waiver of premium' rider waives your premiums if you become disabled — a valuable addition to any life policy.",
        "Accidental death and dismemberment (AD&D) pays in addition to your life insurance if death or injury is accidental.",
        "A child rider on your life insurance policy provides a small death benefit for minor children at a very low cost.",
        "Long-term disability insurance: if you get sick or injured and can't work, your mortgage doesn't pause. Does your income coverage?",
        "Group health insurance through your employer is often the most affordable option — but compare with marketplace options.",
        "An HSA (Health Savings Account) paired with a high-deductible health plan can save thousands in annual premiums.",
        "COBRA allows you to continue employer health coverage after leaving a job — but you pay the full premium, which can be expensive.",
        "Medicaid eligibility is based on income. If your income dropped significantly, you may now qualify.",
        "Short-term health insurance can bridge gaps between jobs or during open enrollment waiting periods.",
        "Dental and vision insurance are typically separate from health insurance — don't forget these important coverages.",
        "Critical illness insurance pays a lump sum if you're diagnosed with cancer, heart attack, stroke, or other specified conditions.",
        "Hospital indemnity insurance pays a daily cash benefit for each day you're hospitalized — helps cover deductibles and co-pays.",
        "Medicare open enrollment runs October 15 – December 7. Missing it means waiting until next year.",
        "A Medicare Advantage plan bundles Original Medicare with prescription drug coverage and often includes dental and vision.",
        "Medigap Plan G is one of the most comprehensive Medicare supplement plans — covering most out-of-pocket costs.",
        "Life insurance trusts (ILITs) remove life insurance proceeds from your taxable estate — a key estate planning tool.",
        "Graded benefit life insurance has a 2-3 year waiting period before full benefits pay — understand before you buy.",
        "Return of premium term insurance refunds your premiums if you outlive the policy term — costs more but has zero waste.",
        "The medical exam for life insurance typically includes blood pressure, blood draw, and urinalysis. Prepare by fasting 4-8 hours.",
        "If you've had a health challenge, an impaired risk specialist can still find you coverage — don't assume you're uninsurable.",
        "Final expense insurance is a small whole life policy designed to cover funeral costs — typically $5,000-$25,000 face amount.",
        "Spousal life insurance: if a stay-at-home parent passed away, the cost to replace their contributions (childcare, household) can exceed $100,000/year.",
        "Group life insurance at work is 'free' — but it's often 1-2x salary, far less than what your family actually needs.",
        "Premium financing lets high-net-worth individuals buy large life insurance policies using a loan against other assets.",
        "An irrevocable life insurance trust (ILIT) keeps life insurance out of your taxable estate. Estate planning essential for high-net-worth clients.",
        "Income replacement should be your life insurance north star: how much income would my family need if I were gone tomorrow?",
        "Living benefits riders allow you to access your life insurance death benefit while living if you're diagnosed with a terminal illness.",
    ]),
    ("Commercial Insurance", [
        "Every business needs general liability insurance — it's the foundation of a commercial insurance program.",
        "A BOP (Business Owner's Policy) combines GL + property + business interruption into one package, usually at a discount.",
        "Workers compensation is required in most states for all employees, regardless of part-time or full-time status.",
        "Commercial auto is separate from personal auto. If you use your vehicle for business, your personal policy may exclude coverage.",
        "Professional liability (E&O) covers claims that your professional advice or service caused a client financial harm.",
        "Cyber insurance is no longer optional. The average cost of a data breach for a small business exceeds $200,000.",
        "If your business has contracts with other companies, they likely require you to carry minimum liability limits and be listed as 'additional insured.'",
        "EPLI (Employment Practices Liability) protects against claims of wrongful termination, discrimination, and sexual harassment.",
        "Directors & Officers (D&O) insurance is essential for any business with a board — even nonprofits.",
        "Product liability coverage protects manufacturers, distributors, and retailers if a product injures a customer.",
        "Commercial umbrella insurance provides excess liability limits above your underlying commercial policies.",
        "If your business leases space, your landlord's property insurance does NOT cover your contents or equipment.",
        "Business interruption coverage pays your fixed expenses (rent, payroll) if your business must temporarily close after a covered loss.",
        "Equipment breakdown coverage (aka boiler and machinery) covers unexpected breakdown of mechanical and electrical equipment.",
        "Inland marine insurance covers tools, equipment, and inventory in transit or stored off-premises.",
        "Commercial crime insurance covers employee theft, forgery, and computer fraud — a real risk for businesses of any size.",
        "Pollution liability insurance is critical for contractors, cleaning companies, and anyone who handles chemicals.",
        "Garage keepers liability covers damage to customers' vehicles while in your care — essential for auto shops, dealers, and valet operations.",
        "Liquor liability insurance is required for businesses that serve, sell, or distribute alcohol.",
        "Habitational insurance covers multi-family residential properties — different from standard homeowner's policies.",
        "Construction risks (builders risk insurance) cover a structure under construction against fire, theft, and weather damage.",
        "Surety bonds guarantee that a contractor will complete a job — required for many government and commercial contracts.",
        "Workers comp classification codes directly impact your premium — make sure your employees are classified correctly.",
        "Experience modification factor (mod) reflects your claims history relative to your industry. A mod below 1.0 earns a discount.",
        "Loss control programs funded by carriers (safety training, inspections) can reduce your workers comp premiums significantly.",
        "Certificate of insurance (COI) is proof your coverage exists. Clients and contracts often require one before work begins.",
        "Additional insured endorsements add another party to your policy's coverage — required by many contracts.",
        "Blanket additional insured endorsements cover all additional insureds under one endorsement instead of adding them one by one.",
        "Waiver of subrogation prevents your carrier from suing a named party after paying your claim — often required by contracts.",
        "The 'per occurrence' vs. 'aggregate' limit distinction: per occurrence is the max per incident; aggregate is the total per policy year.",
        "Commercial property insurance typically excludes flood, earthquake, and certain weather events — evaluate your location's risk.",
        "Fleet insurance covers multiple commercial vehicles under one policy, typically cheaper than individual policies.",
        "Healthcare practices face specialized liability exposures — medical malpractice, HIPAA liability, and cyber risk are all relevant.",
        "Technology E&O covers tech companies for software failures, system outages, and data errors that harm clients.",
        "Franchise insurance programs: many franchisors offer group insurance programs for franchisees — compare with the open market.",
        "Non-owned auto liability covers your business if an employee uses their personal vehicle for company business.",
    ]),
    ("Prospecting & Sales Tips", [
        "The best time to follow up with an insurance lead is within 5 minutes of receiving it. Speed-to-contact dramatically improves conversion.",
        "Ask questions before you quote. Agents who understand the prospect's situation write better policies and close at higher rates.",
        "Objections are buying signals. When someone says 'I need to think about it,' they're asking for more information or reassurance.",
        "The #1 reason people switch insurance agents is NOT price — it's feeling ignored or undervalued. Don't let that be you.",
        "Referrals close at 3-5x the rate of cold leads. Build your referral system before you need it.",
        "The multi-policy household is your ideal client. Home + auto + umbrella + life = higher retention and higher value.",
        "Don't pitch products — solve problems. 'What keeps you up at night about your [home/business/family]?' is a better opener than any script.",
        "Social proof closes deals. Before every proposal, ask if you can share a story about how you helped a similar client.",
        "Every 'no' is feedback, not failure. What specifically was the objection? Fix it and try again with the next prospect.",
        "Your CRM is your business. If it's not in the CRM, it didn't happen. Log every contact, every conversation, every outcome.",
        "LinkedIn is a goldmine for commercial lines prospecting. Your ideal business owner client is posting there right now.",
        "The fortune is in the follow-up. Most insurance sales happen after 5+ contacts. Most agents give up after 2.",
        "Testimonials from clients in the same industry as your prospect are 10x more persuasive than any brochure.",
        "Price isn't your enemy — perceived value is. Build enough value in the consultation and price rarely kills the deal.",
        "Asking for referrals should happen BEFORE the sale is closed — 'If I take great care of you, would you be willing to introduce me to others?'",
        "Commercial lines phone prospecting works best Tuesday-Thursday, 10am-12pm and 2-4pm. Avoid Mondays and Fridays.",
        "The discovery conversation is more important than the proposal. Agents who ask great questions write great proposals.",
        "Never send a quote via email without a follow-up call scheduled to walk through it together.",
        "Annual reviews are your single best retention AND cross-sell tool. Block time for them every week.",
        "A well-timed 'check-in' call between renewals shows clients you're thinking about them — not just their premium.",
        "Personal branding on social media makes cold calls warmer. When prospects have seen your content, they already know you.",
        "Video voicemails on LinkedIn have 5x higher response rates than text messages. Try it this week.",
        "The fastest path to a $500K GCI agency is building a referral machine. Start with your top 20% of clients.",
        "Every new client is a referral opportunity — ask within the first 30 days, while the experience is fresh.",
        "Track your close ratio by lead source. Double down on what's working and minimize what's not.",
        "Learning to say 'I'm not the right fit for every client' actually builds trust — and sends you better leads.",
        "The best agents I know are constantly learning — product updates, sales techniques, market trends. Never stop growing.",
        "Your pitch deck or proposal quality sends a signal about your agency quality before the client ever becomes one.",
        "Cross-selling is easiest right after a new policy binds — the client's trust in you is at its peak.",
        "Insurance is a relationship business. Long-term thinking always beats short-term transaction thinking.",
        "A client who bought one policy from you 5 years ago and nothing else since is a cross-sell opportunity waiting to happen.",
        "Niche marketing (focus on one industry or demographic) allows you to become an expert, charge more, and generate better referrals.",
        "The 'assumptive close' works in insurance: 'I'll get this submitted today — do you want the effective date to be the first or the fifteenth?'",
        "Most agents quit prospecting when they're busy. Top agents prospect hardest when they're busy — they're building pipeline.",
        "The average insurance agent writes 20 policies a year. Top agents write 100+. The difference is daily activity and follow-up.",
        "Consistency beats intensity. 20 calls every day beats 200 calls one day a month.",
    ]),
    ("Risk Management", [
        "Risk management is about identifying, assessing, and mitigating potential financial losses before they occur.",
        "The four methods of handling risk: avoid, reduce, transfer (insurance), and retain (self-insure).",
        "A business continuity plan ensures your company can keep operating (or recover quickly) after a major disruption.",
        "Regular property inspections by your carrier's loss control team can prevent claims — and often reduce premiums.",
        "Fleet safety programs that track driver behavior can reduce commercial auto accidents AND lower your insurance costs.",
        "A formal safety committee and documented safety policies can significantly reduce workers comp claims.",
        "Don't just buy insurance to transfer risk — actively manage the risks that insurance can't fully cover.",
        "Fire suppression systems, security cameras, and proper lighting don't just protect your property — they reduce your premium.",
        "The biggest uninsured risk for most families: the loss of the primary earner's income. Disability insurance is the fix.",
        "Contract review before you sign is risk management. Never agree to assume unlimited liability in a contract.",
        "Supply chain disruption is a growing risk for businesses — contingent business interruption insurance can help.",
        "Cybersecurity training for employees reduces cyber risk — your IT security and your cyber insurance work together.",
        "Document your business processes so operations can continue if a key employee is suddenly unavailable.",
        "Environmental liability is a growing risk for manufacturing, construction, and dry cleaning businesses.",
        "Crisis management planning (what to do when something goes wrong) is as important as prevention.",
        "Product recall insurance covers the cost of recalling a defective product — essential for food and consumer goods companies.",
        "Reputational risk is increasingly insurable — media liability and crisis response coverage are available.",
        "Healthcare organizations face HIPAA liability risk — cyber insurance and professional liability must address this.",
        "Background checks and employee screening reduce employee dishonesty risk — and may be required by some insurers.",
        "Directors and officers face personal liability for management decisions. D&O insurance is their protection.",
        "Contractual risk transfer: requiring subcontractors to carry their own insurance shifts risk appropriately.",
        "A certificate of insurance is not a substitute for reading the actual policy — it shows coverage exists but not what's excluded.",
        "Business valuation affects your commercial property limit — update it every 3-5 years or after major acquisitions.",
        "Properly installed and maintained fire suppression systems are the single most effective commercial property loss control measure.",
        "Every business should have a written disaster recovery plan — and test it annually.",
        "Slip and fall prevention: proper lighting, non-slip mats, and regular property inspections reduce your GL claims.",
        "Workplace ergonomics reduces repetitive stress injury claims — one of the most common workers comp claims categories.",
        "Know your lease's indemnification clauses — you may be assuming risk that should belong to your landlord.",
        "Fleet telematics (GPS + driving behavior monitoring) reduces accidents and can earn workers comp discounts.",
        "Cybersecurity insurance is a complementary control — not a substitute for strong IT security practices.",
        "A strong safety culture (leadership modeling safe behavior) reduces claims more than any written policy.",
        "The greatest risk most families face is not having enough life insurance — it's a risk with a simple, affordable solution.",
        "Over-insuring (more coverage than your exposure warrants) wastes money. Under-insuring leaves you exposed. Find the balance.",
        "Risk management conversations make you a trusted advisor, not just an insurance salesperson.",
        "The purpose of insurance is to return you to the financial position you were in before a loss — not to profit from one.",
        "Risk is not inherently bad — it's what drives business forward. Insurance is what makes risk acceptable.",
    ]),
    ("Client Success Stories", [
        "A client of mine had a house fire while on vacation. Because we'd done a proper policy review, they had full replacement cost coverage — they rebuilt completely.",
        "I got a call from a client at 2am — their car was stolen. By morning, they had a rental reserved and a claim in process. That's what I'm here for.",
        "A business owner came to me after a slip-and-fall lawsuit nearly wiped out his company. He now has proper GL and umbrella coverage.",
        "A client switched to me from a direct carrier and saved $780 in the first year on the exact same coverage.",
        "I worked with a young family who didn't have life insurance. Weeks after we set up their coverage, the husband was diagnosed with cancer. The policy is now their financial lifeline.",
        "A restaurant owner client had a kitchen fire and was closed for 3 months. Business interruption coverage replaced his lost income while repairs were made.",
        "A contractor client was sued after a water pipe was accidentally cut during a renovation. GL insurance covered the defense and settlement costs.",
        "I identified a coverage gap in a client's policy that would have left them without coverage after a flood. We fixed it before the water came.",
        "A client's teenage driver was in a serious accident. Because their liability limits were adequate, they were protected. Without my advice, they would have been exposed.",
        "A referral partner sent me a commercial client with a $0 deductible workers comp policy — we restructured it and saved $14,000 annually.",
        "A client called to cancel after a rate increase. I shopped the market, found a better rate, and they stayed. Loyalty retained.",
        "I helped a retiring business owner set up key person life insurance — when he passed unexpectedly, the benefit funded the buyout perfectly.",
        "A couple came to me 2 weeks before closing on their first home — panicked about coverage. We had everything in place with a day to spare.",
        "A small business client had no cyber insurance. After a ransomware attack, it would have cost $80,000 out of pocket. Now they're protected.",
        "I've helped 3 generations of the same family with their insurance. That kind of trust is what I work for.",
        "A client's jewelry wasn't on a scheduled endorsement. After a theft, we worked with the carrier to maximize recovery — but a rider would have paid more.",
        "A client who was 'happy with State Farm' for 20 years let me run a comparison. I found identical coverage for $1,100 less per year.",
        "An HVAC contractor came to me uninsured — no GL, no WC. We got everything in place and he landed his first major commercial contract that required it.",
        "A single mom came to me worried about what would happen to her kids if something happened to her. We set up a term life policy for $23/month.",
        "A dentist had professional liability insurance through an association plan with $1M limits. For his practice size, we doubled the limits for $800 more per year.",
        "A client had an at-fault accident and was worried about a rate hike. Their carrier had an accident forgiveness endorsement. I knew that — they didn't.",
        "A client's home was damaged in a hailstorm. They didn't want to file a claim, thinking their rates would go up. I helped them understand their rights.",
        "A client bought a vacation cabin and assumed their primary home policy covered it. It didn't. We caught it before anything happened.",
        "A startup founder came to me for business insurance. We built a complete commercial program — he closed his first enterprise client that week.",
        "I saved a commercial client from an insurance agent who had misclassified their workers comp code for 5 years. Refund: $34,000.",
        "A new agent came to me to learn the business. Watching them grow their book is one of my greatest professional satisfactions.",
        "A client's flood claim was denied because they had the wrong endorsement. I advocated to the carrier and overturned the denial.",
        "I called a client to wish them happy birthday and mentioned their renewal was coming. They'd forgotten — and appreciated the reminder.",
        "A client who was about to drop their umbrella policy after a rate increase kept it when I explained what they'd be giving up.",
        "A professional couple tripled their coverage and reduced their premium by switching from two separate agents to bundling with me.",
        "A restaurant client expanded to a second location. I was the first call they made. We had coverage in place before opening day.",
        "I referred a client to a mortgage broker who helped them save $200/month. The client sent me 4 referrals. Relationships work.",
        "A client called panicked that their contractor let their insurance lapse mid-project. We found E&S coverage within the hour.",
        "A client's business was sued by a former employee. EPLI coverage paid the $45,000 settlement and $30,000 in legal fees.",
        "After a major loss, my client said: 'I never knew if I needed you until I needed you. Thank you for being there.'",
        "The most meaningful part of my job is what I prevent — the financial disasters my clients never have to face.",
    ]),
    ("Compliance & Best Practices", [
        "Always document client coverage decisions — especially declined recommendations — to protect yourself from E&O claims.",
        "Insurance carriers update their underwriting guidelines regularly. Review them annually to avoid binding non-compliant risks.",
        "A signed coverage declination form protects you if a client later claims they weren't offered coverage you recommended.",
        "Never bind coverage you're not appointed for. It's a serious license violation and creates massive E&O exposure.",
        "Keep client records for a minimum of 5 years after policy expiration — longer in states with extended statute of limitations.",
        "E&O claims arise most often from miscommunication, not incompetence. Document everything. Always.",
        "Continuing education keeps your license — and keeps you sharp. Don't just check the box; learn something new.",
        "State insurance departments can review your business practices. Keep your records in order and your processes documented.",
        "Your social media posts are advertising. They're subject to insurance advertising regulations in your state.",
        "Never share one client's information with another, even inadvertently. Privacy obligations are serious.",
        "GLBA (Gramm-Leach-Bliley Act) requires insurance agencies to have a written data security plan. Do you have one?",
        "Premium trust accounts are sacred — client funds must never be commingled with operating accounts.",
        "Carrier appointment agreements have compliance requirements. Read them annually and follow them.",
        "Your license is your business. Protect it by practicing within your scope and staying current on regulations.",
        "Advertising that implies guaranteed savings is a compliance risk — never make promises you can't keep.",
        "Annual E&O self-audits (reviewing your own practices against best practice standards) prevent claims proactively.",
        "Reporting claims to your E&O carrier early gives them the best chance to defend you successfully.",
        "If you can't ethically serve a client (conflict of interest, outside your expertise), refer them out. It protects everyone.",
        "A compliance calendar (license renewals, CE deadlines, appointment renewals) prevents expensive lapses.",
        "Industry designations (CIC, CPCU, AAI) signal your commitment to professionalism and often unlock better carrier access.",
        "Do not guarantee or predict coverage decisions — that's the carrier's role. Your job is to submit and advocate.",
        "Ethical agents know when a client is better served by another agent or carrier — and they refer without hesitation.",
        "The insurance regulatory environment varies dramatically by state. When writing in a new state, learn the rules first.",
        "Errors and omissions cases often hinge on whether the agent 'should have known' a coverage issue existed. Stay educated.",
        "A written privacy policy isn't just good practice — it may be legally required in your state.",
        "Market conduct exams by state insurance departments review how you sell, service, and claim. Be audit-ready always.",
        "Round-tripping (creating fictitious policies for commission) is insurance fraud. Not worth any short-term gain.",
        "Churning policies (unnecessarily replacing them for commission) harms clients and can cost you your license.",
        "Your professional reputation is your most valuable business asset. Guard it in every interaction.",
        "The best compliance strategy is treating every client the way you'd want your grandmother to be treated.",
        "When in doubt about a compliance question, call your E&O carrier or state association before acting.",
        "Agent education extends to clients — helping them understand what they bought is one of your key service obligations.",
        "Adequate coverage recommendations aren't just about liability protection — they're about serving clients' best interests.",
        "Regulatory changes (commission disclosure laws, contract rules) come regularly. Subscribe to your state association's alerts.",
        "Anti-money laundering awareness is a growing requirement for insurance agents handling large cash-value policies.",
        "The compliance burden of independence is real — but it's also what makes you a trusted professional.",
    ]),
    ("Motivation & Growth", [
        "The most successful insurance agents aren't the most talented — they're the most persistent.",
        "Every rejection is one step closer to a yes. The agents who make 100 calls a day get 10x more yeses.",
        "Your book of business is your retirement plan. Build it with the same intention you'd give any long-term investment.",
        "Every client you lose to a competitor is feedback. What could you have done better?",
        "The agents who thrive in a hard market are the ones who built relationships before the market turned.",
        "Success in insurance isn't complicated — it's consistently doing the right activities, over a long enough period of time.",
        "Your mindset going into a prospecting call determines 50% of the outcome before you dial.",
        "Set a prospecting goal you can control: number of calls made, not number of policies sold.",
        "Build your business for the long game. Reputation takes years to build and one mistake to damage.",
        "The best time to prospect is when you don't need to. The worst time is when you desperately do.",
        "Study your competition — then focus on what THEY don't do well. That's your opportunity.",
        "Clients can feel the difference between an agent who's chasing commission and one who genuinely cares.",
        "Track your activity metrics weekly. You can't improve what you don't measure.",
        "Invest in yourself: industry conferences, coaching, advanced designations. Your growth never ends.",
        "A goal without a deadline is a wish. Set specific targets with specific dates.",
        "The first year in insurance is the hardest. Every veteran agent went through what you're going through. Keep going.",
        "Your CRM is your business memory. Every contact, every conversation — it lives there.",
        "Building a referral machine is a 3-year project. Plant the seeds every day.",
        "Time blocking is the #1 productivity tool of top-producing agents. Protect your prospecting hours fiercely.",
        "The agents who make it aren't the ones who never fail — they're the ones who learn from every failure.",
        "A client who trusts you will never shop around. Build trust, not just policies.",
        "The best version of your agency exists in your vision. Close the gap between where you are and where you want to be.",
        "Celebrate small wins. Every new policy, every referral, every annual review completed is a win.",
        "You are not competing with every agent in your state. You are competing for the clients in your own backyard.",
        "Scale happens when you have systems AND the right people. Build both intentionally.",
        "The highest-paid skill in insurance is the ability to talk to anyone about anything and build trust quickly.",
        "The agents who build durable books focus on retention first, production second.",
        "Your clients' lives change every year. Are your annual reviews keeping up?",
        "Great agents don't just respond to problems — they prevent them. That's what makes clients loyal for life.",
        "Diversify your book by line of business and industry. Concentration in one area is a business risk.",
        "The agency owner who hires before they're ready often grows faster than the one who waits until they're drowning.",
        "Your follow-up sequence IS your sales process. Master it.",
        "Every morning you wake up and choose what to do with your time. Choose prospecting.",
        "Vision without execution is daydreaming. Execution without vision is busy work. You need both.",
        "The best retention strategy is extraordinary service delivered consistently. Not gimmicks. Not discounts.",
        "The agents I most admire built their careers helping clients — not just selling policies. Be that agent.",
    ]),
]

all_caps = []
for cat, caps in categories:
    for cap in caps:
        all_caps.append([cat, cap, "#insurance", "Post"])
while len(all_caps) < 365:
    all_caps.append(["Insurance Tips","Great insurance agents protect what their clients care about most — every single day.","#insurance","Post"])
all_caps = all_caps[:365]
for i, row in enumerate(all_caps):
    row.insert(0, str(i+1))

write_csv(p11+"365_Social_Media_Captions.csv",
    ["Day","Category","Caption","Hashtag","Type"],
    all_caps)

# Bonus DOCX 1: Insurance Scripts Vault
doc(p11+"Insurance_Scripts_Vault.docx",
    "Insurance Scripts Vault",
    "Insurance Agency OS | 40+ Proven Scripts for Every Situation",
    [
        ("Cross-Sell Scripts", [
            "Umbrella Insurance Cross-Sell:",
            '"[Name], I want to bring something to your attention while I have you. You currently have $300,000 in liability on your home policy and $250,000 on your auto. If someone is seriously injured on your property or in an accident you cause, those limits can be exhausted quickly. A personal umbrella policy gives you an extra $1 million of protection — it costs about $200-$300 per year. Can I add that to your renewal?"',
            "Life Insurance Cross-Sell:",
            '"We\'ve been handling your home and auto for a few years now and I realized we\'ve never talked about life insurance. Do you have any coverage in place? [...] I\'d love to do a quick needs analysis — 10 minutes is all it takes to see if you have enough protection for your family. When are you free?"',
        ]),
        ("Retention Scripts — Cancellation Prevention", [
            "Client Calling to Cancel Due to Price:",
            '"I\'m sorry to hear that — before I process the cancellation, would you mind sharing the quote you received? I want to make absolutely sure we\'ve explored every option for you. If I can match or beat it, would you want to stay with our agency? [...] Give me 10 minutes to run a market comparison."',
            "Client Calling to Cancel — Moving:",
            '"Congratulations on the move! Before you cancel, I should mention that our agency may be able to help you in your new state as well. We work with carriers in [states]. Would it help if I reach out to see what we can offer there? I\'d love to keep your business."',
        ]),
        ("Annual Review Scripts", [
            "Opening the Review Call:",
            '"Hi [Name], this is [Agent]. I\'m reaching out because your annual review is coming up. As I do with all my clients, I like to take 15 minutes once a year to make sure your coverage still makes sense and that you\'re getting the best rate available. Do you have a few minutes?"',
            "Finding Cross-Sell Opportunities in the Review:",
            '"While I have you — I\'ve noticed we handle your home and auto, but I don\'t see life insurance on file. Is that something you have elsewhere, or is it something we\'ve never gotten around to discussing? [...] It\'s something I\'d love to have a brief conversation about — it only takes 10 minutes and could protect your family significantly."',
        ]),
        ("Closing Scripts", [
            "The Assumptive Close:",
            '"Based on everything we\'ve discussed, I\'d recommend the [Carrier] policy at [Premium]. I can get this submitted today — would you like the effective date to be the first of the month, or would another date work better for you?"',
            "The Summary Close:",
            '"Let me recap what I\'m putting together for you: [Coverage A] at [limit], [Coverage B] at [limit], and [Coverage C] — all bundled together for $[Premium] per month. That\'s $[X] less than what you\'re paying now for better coverage. Are you ready to move forward?"',
        ]),
    ])

# Bonus DOCX 2: Agency Growth Playbook
doc(p11+"Agency_Growth_Playbook.docx",
    "Insurance Agency Growth Playbook",
    "Insurance Agency OS | From $0 to $1M in Agency Revenue",
    [
        ("The 4 Stages of Agency Growth", [
            "Stage 1 — Startup ($0-$100K revenue): Solo agent, building book from scratch. Focus: prospecting, referrals, carrier appointments",
            "Stage 2 — Growth ($100K-$300K): Hire first CSR. Focus: retention systems, cross-sell, referral partner development",
            "Stage 3 — Scale ($300K-$700K): Add producers. Focus: team development, marketing systems, niche specialization",
            "Stage 4 — Enterprise ($700K+): Management team, systems, possible acquisition. Focus: culture, metrics, succession planning",
        ]),
        ("Growth Levers — Ranked by ROI", [
            ("•", "1. Referral Partner Program: Highest ROI, lowest cost. Develop 10-20 active COIs"),
            ("•", "2. Annual Reviews: Best retention tool AND #1 cross-sell opportunity"),
            ("•", "3. Client Referral Program: Turn satisfied clients into your sales force"),
            ("•", "4. Commercial Lines: Higher average premium ($5K-$50K vs. $2K residential)"),
            ("•", "5. Digital Marketing: Facebook/LinkedIn ads, Google, and content marketing"),
            ("•", "6. Niche Specialization: Become the expert for [contractors/restaurants/healthcare]"),
        ]),
        ("The Perfect Agency Week", [
            ("•", "Monday: Team meeting, pipeline review, set weekly priorities"),
            ("•", "Tuesday/Wednesday: Peak prospecting days — outbound calls, appointments"),
            ("•", "Thursday: Renewals, annual reviews, cross-sell conversations"),
            ("•", "Friday: Administrative completion, COI outreach, weekend prep"),
            ("•", "Daily: 1 hour of prospecting activity, 30 minutes of personal development"),
        ]),
        ("90-Day Agency Sprint", [
            "Month 1: Database audit — categorize every client, set up renewal diarization system",
            "Month 2: Referral activation — contact top 20 clients and 10 COIs for referrals",
            "Month 3: Cross-sell campaign — annual review calls to entire book, identify opportunities",
            "Monthly Tracking: New policies, revenue, referrals, reviews completed, retention rate",
        ]),
        ("Building a Million-Dollar Book", [
            ("•", "$1M agency revenue requires approximately $10M in annual premium at 10% average commission"),
            ("•", "At $3,000 average premium: you need ~3,333 policies"),
            ("•", "To write $10M in premium: add $1M per year (takes ~10 years with consistent growth)"),
            ("•", "The shortcut: Hire producers, develop referral partners, and cross-sell aggressively"),
            ("•", "The formula: Great service + consistent prospecting + annual reviews = compounding growth"),
        ]),
    ])

# Bonus DOCX 3: Insurance Product Knowledge Guide
doc(p11+"Insurance_Product_Knowledge_Guide.docx",
    "Insurance Product Knowledge Guide",
    "Insurance Agency OS | Essential Reference for Every Insurance Line",
    [
        ("Property & Casualty — Core Concepts", [
            ("•", "Homeowner's Insurance: HO-3 (open perils on dwelling, named perils on contents) is most common"),
            ("•", "Condo Insurance: HO-6 covers interior, personal property, liability; HOA covers exterior"),
            ("•", "Renters Insurance: HO-4 covers personal property and liability only (no dwelling)"),
            ("•", "Auto Insurance: Personal auto policy (PAP) covers 4 sections: liability, medical, uninsured motorist, physical damage"),
            ("•", "Umbrella: Excess liability above home and auto; typically $1M increments; requires underlying limits"),
        ]),
        ("Life Insurance — Core Concepts", [
            ("•", "Term Life: Pure death benefit for a set period (10, 20, 30 years). Most affordable."),
            ("•", "Whole Life: Permanent coverage with guaranteed cash value accumulation"),
            ("•", "Universal Life: Flexible premiums; cash value earns a declared interest rate"),
            ("•", "Variable Life: Cash value tied to separate account investments (market risk)"),
            ("•", "Indexed Universal Life (IUL): Cash value tied to equity index with floor/cap"),
        ]),
        ("Commercial Lines — Core Concepts", [
            ("•", "General Liability: CGL policy covers bodily injury, property damage, advertising injury"),
            ("•", "Commercial Property: Covers building and contents from covered perils"),
            ("•", "BOP: Package of GL + property + business interruption for eligible small businesses"),
            ("•", "Workers Compensation: Statutory coverage; mandatory in most states; employer liability included"),
            ("•", "Commercial Auto: Business use of vehicles; fleet policies for 5+ vehicles"),
            ("•", "Professional Liability: Claims-made basis; covers errors and omissions in professional services"),
        ]),
        ("Health Insurance — Core Concepts", [
            ("•", "Deductible: Amount you pay before insurance pays (except for preventive care in ACA plans)"),
            ("•", "Copay: Fixed amount you pay for a specific service (e.g., $30 for primary care)"),
            ("•", "Coinsurance: Your percentage share after deductible (e.g., 20% until out-of-pocket max)"),
            ("•", "Out-of-Pocket Maximum: After this amount, carrier pays 100% for covered services"),
            ("•", "Network: In-network = negotiated rates; out-of-network = full cost"),
            ("•", "Medicare Parts: A (hospital), B (medical), C (Advantage), D (prescription drugs)"),
        ]),
    ])

print("✓ 11_BONUSES complete")

# ─── PDFs ──────────────────────────────────────────────────────────────────────
NAV_C=colors.HexColor("#0F3460"); ACC_C=colors.HexColor("#E94560"); GLD_C=colors.HexColor("#F5A623")

def make_pdf(fpath, title, subtitle, sections):
    d=SimpleDocTemplate(fpath,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=20*mm,bottomMargin=20*mm)
    st=getSampleStyleSheet()
    ts=ParagraphStyle('T',parent=st['Normal'],fontSize=22,textColor=NAV_C,spaceAfter=4,fontName='Helvetica-Bold')
    ss=ParagraphStyle('S',parent=st['Normal'],fontSize=11,textColor=colors.HexColor("#7F8C8D"),spaceAfter=12)
    hs=ParagraphStyle('H',parent=st['Normal'],fontSize=13,textColor=NAV_C,spaceBefore=12,spaceAfter=4,fontName='Helvetica-Bold')
    bs=ParagraphStyle('B',parent=st['Normal'],fontSize=10,spaceAfter=4,leading=15)
    bls=ParagraphStyle('BL',parent=st['Normal'],fontSize=10,leftIndent=16,spaceAfter=3,leading=14,bulletIndent=6)
    story=[Paragraph(title,ts),HRFlowable(width="100%",thickness=3,color=ACC_C,spaceAfter=6),Paragraph(subtitle,ss)]
    for sec in sections:
        if isinstance(sec,str): story.append(Paragraph(sec,bs)); continue
        hd,items=sec
        story.append(Paragraph(hd,hs))
        story.append(HRFlowable(width="100%",thickness=1,color=GLD_C,spaceAfter=4))
        for item in items:
            if isinstance(item,tuple) and item[0]=='•': story.append(Paragraph(f"• {item[1]}",bls))
            else: story.append(Paragraph(str(item),bs))
    d.build(story)
    print(f"  ✓ {fpath.replace(BASE,'')}")

make_pdf(BASE+"06_COMPLIANCE_LICENSING/Agency_Compliance_Reference_Guide.pdf",
    "Insurance Agency Compliance Reference Guide",
    "Insurance Agency OS | E&O, Licensing, Carrier Appointments & Ethics",
    [
        ("E&O Best Practices Summary", [
            "Errors & Omissions insurance is your professional liability safety net. Beyond carrying E&O coverage, your daily practices are your best defense.",
            ("•","Document every client interaction — phone, email, or in-person"),
            ("•","Use signed declination forms when clients decline recommended coverage"),
            ("•","Never bind coverage you're not appointed for"),
            ("•","Keep records for a minimum of 5 years after policy expiration"),
            ("•","Report potential E&O incidents to your carrier immediately — don't wait"),
        ]),
        ("License Maintenance Checklist", [
            ("•","All licenses current in every state you transact business"),
            ("•","Continuing education credits completed before deadline"),
            ("•","Renewal applications submitted 30+ days before expiration"),
            ("•","Non-resident license status confirmed for all states where you write"),
            ("•","Any staff licenses verified — no unlicensed staff transacting insurance"),
        ]),
        ("Advertising Compliance Rules", [
            ("•","No misleading claims about coverage, cost savings, or carrier ratings"),
            ("•","Social media posts are insurance advertisements — follow state ad regulations"),
            ("•","Carrier names and logos require permission to use — check your appointment agreement"),
            ("•","Testimonials must be genuine, current, and not promise specific outcomes"),
            ("•","CAN-SPAM compliance for email marketing — always include unsubscribe option"),
        ]),
        ("Client Privacy Obligations", [
            ("•","GLBA (Gramm-Leach-Bliley Act): Written privacy policy required; client data must be protected"),
            ("•","Never share client information without authorization"),
            ("•","Data security plan: encryption, access controls, backup procedures"),
            ("•","Breach notification: Most states require notifying clients of data breaches within 30-60 days"),
            ("•","Dispose of client records securely — shred physical; wipe digital"),
        ]),
    ])

make_pdf(BASE+"10_NOTION_WORKSPACE/Insurance_Agency_OS_User_Guide.pdf",
    "Insurance Agency Operating System",
    "Complete User Guide | Professional Edition | Value: €149 | Your Price: €39",
    [
        ("Welcome to Your Insurance Agency OS", [
            "Thank you for your purchase! This comprehensive toolkit contains everything you need to run a professional, compliant, and profitable insurance agency — from lead generation through client retention.",
            ("•","60+ professional templates, scripts, and tools"),
            ("•","Complete sales process from first call to policy delivery"),
            ("•","Compliance and E&O protection frameworks"),
            ("•","Notion-based agency CRM system with 7 databases"),
            ("•","365 days of insurance-specific social media content"),
            ("•","4 Canva-importable presentation templates"),
        ]),
        ("What's Included", [
            ("•","00_START_HERE: Quick start checklist and product overview"),
            ("•","01_LEAD_GENERATION: Phone scripts, email sequences, referral programs, social media strategy"),
            ("•","02_SALES_PROCESS: Needs analysis, proposal template, objection handling, closing scripts"),
            ("•","03_POLICY_SERVICES: Onboarding SOP, annual review system, endorsements, cross-sell playbook"),
            ("•","04_CLAIMS_SUPPORT: FNOL SOP, claims advocacy guide, communication templates"),
            ("•","05_CLIENT_COMMUNICATION: Email library, text templates, phone scripts, newsletter template"),
            ("•","06_COMPLIANCE_LICENSING: E&O guide, compliance checklist, licensing guide, carrier appointments"),
            ("•","07_CARRIER_RELATIONSHIPS: Negotiation guide, submission guide, market access strategy"),
            ("•","08_AGENCY_OPERATIONS: Hiring guide, training program, operations manual, KPI dashboard"),
            ("•","09_POST_SALE_RETENTION: Retention system, annual review scripts, appreciation program"),
            ("•","10_NOTION_WORKSPACE: 7 importable databases + Notion setup guide"),
            ("•","11_BONUSES: 365 social captions, scripts vault, growth playbook, product knowledge guide"),
            ("•","12_CANVA_TEMPLATES: 4 professional Canva-importable presentations"),
        ]),
        ("Quick Start Instructions", [
            "Step 1: Import the 7 CSVs from 10_NOTION_WORKSPACE into Notion (see Notion_Setup_Guide.md)",
            "Step 2: Upload PPTX files from 12_CANVA_TEMPLATES to Canva",
            "Step 3: Open Agency_CRM.xlsx and import your existing leads and clients",
            "Step 4: Customize all DOCX templates with your name, agency, and contact information",
            "Step 5: Post your first social media content using the 365_Social_Media_Captions.csv",
        ]),
        ("License", [
            ("•","Personal use: Unlimited use in your own insurance business"),
            ("•","Customization: Fully customize all templates with your branding"),
            ("•","Team use: Use with your agency team members"),
            ("•","Restrictions: Do not resell, redistribute, or share as your own product"),
        ]),
    ])

make_pdf(BASE+"09_POST_SALE_RETENTION/Client_Retention_Workbook.pdf",
    "Client Retention Workbook",
    "Insurance Agency OS | 90-Day Retention & Growth Sprint",
    [
        ("Why Retention Is Your #1 Growth Strategy", [
            "Acquiring a new client costs 5-7x more than retaining one. A 5% increase in retention can improve profitability by 25-95%. Your existing book of business is a growth machine — if you service it properly.",
        ]),
        ("Month 1 — Audit Your Book", [
            ("•","Week 1: Categorize all clients by tier (VIP, A, B, C based on premium + referral activity)"),
            ("•","Week 2: Identify all clients without an annual review in the past 12 months"),
            ("•","Week 3: Identify all single-policy clients — cross-sell opportunity list"),
            ("•","Week 4: Review retention rate — how many clients cancelled in the past 12 months?"),
            "Month 1 Goal: Complete book audit; identify top 20 clients and top 20 cross-sell opportunities",
        ]),
        ("Month 2 — Activate Relationships", [
            ("•","Week 5: Call every VIP client personally — no email, no text"),
            ("•","Week 6: Send anniversary notes to clients who've been with you 5+ years"),
            ("•","Week 7: Schedule 5 annual reviews with clients approaching renewal"),
            ("•","Week 8: Cross-sell outreach to top 10 single-policy clients"),
            "Month 2 Goal: 5 annual reviews completed; 2 cross-sell conversions",
        ]),
        ("Month 3 — Systematize", [
            ("•","Week 9: Set up CRM reminders for every client touchpoint going forward"),
            ("•","Week 10: Schedule annual review calls for all clients renewing in next 60 days"),
            ("•","Week 11: Launch monthly email newsletter to full client database"),
            ("•","Week 12: Measure results — retention rate, cross-sell conversion, referrals generated"),
            "Month 3 Goal: Full retention system in place; annual reviews automated in CRM",
        ]),
    ])

print("✓ PDFs complete")

# ─── 12_CANVA_IMPORTABLE_TEMPLATES ────────────────────────────────────────────
p12 = "12_CANVA_IMPORTABLE_TEMPLATES/"
PNAV=PRGB(15,52,96); PACC=PRGB(233,69,96); PGLD=PRGB(245,166,35); PWHT=PRGB(255,255,255)
PLGR=PRGB(248,249,250); PDGR=PRGB(44,62,80)

def new_prs():
    prs=Presentation(); prs.slide_width=Inches(13.33); prs.slide_height=Inches(7.5); return prs
def blank(prs): return prs.slides.add_slide(prs.slide_layouts[6])
def rect(sl,l,t,w,h,rgb):
    sh=sl.shapes.add_shape(1,Inches(l),Inches(t),Inches(w),Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=rgb; sh.line.fill.background(); return sh
def txt(sl,text,l,t,w,h,sz=18,bold=False,color=PWHT,align=PP_ALIGN.LEFT):
    tb=sl.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(h))
    tf=tb.text_frame; tf.word_wrap=True
    p=tf.paragraphs[0]; p.alignment=align
    run=p.add_run(); run.text=text
    run.font.size=PPt(sz); run.font.bold=bold; run.font.color.rgb=color
    return tb

# PPTX 1: Insurance Review Presentation
prs=new_prs()
# Cover
sl=blank(prs)
rect(sl,0,0,13.33,7.5,PNAV)
rect(sl,0,0,13.33,0.12,PACC)
rect(sl,0,7.38,13.33,0.12,PGLD)
txt(sl,"INSURANCE REVIEW",0.5,0.8,12.33,1.4,sz=44,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"PRESENTATION",0.5,2.1,12.33,1.2,sz=36,bold=True,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"[Agency Name] | Independent Insurance Professionals",0.5,3.5,12.33,0.7,sz=20,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"Prepared for: [Client Name] | [Date]",0.5,4.4,12.33,0.6,sz=16,color=PRGB(189,195,199),align=PP_ALIGN.CENTER)
# Slide 2 — Why Independent Agency
sl=blank(prs)
rect(sl,0,0,13.33,1.3,PNAV)
txt(sl,"WHY AN INDEPENDENT AGENCY?",0.5,0.25,12,0.8,sz=28,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
benefits=[
    ("🔍","Shop Multiple Carriers","We compare dozens of carriers to find you the best coverage at the best price."),
    ("🛡️","Your Advocate","We represent YOUR interests — not any single insurance company."),
    ("📞","Single Point of Contact","One call for all your insurance needs — home, auto, life, commercial."),
    ("⏰","Claims Support","When you have a claim, we're on your side throughout the entire process."),
    ("📊","Annual Reviews","We review your coverage every year to make sure it still fits your life."),
    ("💼","Expert Guidance","Deep product knowledge across all lines — we make the complex simple."),
]
for i,(icon,title,desc) in enumerate(benefits):
    col=i%3; row=i//2
    x=0.3+col*4.3; y=1.5+row*2.7
    rect(sl,x,y,4.1,2.5,PLGR)
    rect(sl,x,y,4.1,0.08,PACC)
    txt(sl,f"{icon}  {title}",x+0.15,y+0.2,3.8,0.7,sz=14,bold=True,color=PNAV)
    txt(sl,desc,x+0.15,y+1.0,3.8,1.4,sz=11,color=PDGR)
# Slide 3 — Coverage Summary
sl=blank(prs)
rect(sl,0,0,13.33,7.5,PLGR)
rect(sl,0,0,13.33,1.3,PACC)
txt(sl,"YOUR CURRENT COVERAGE SUMMARY",0.5,0.25,12,0.8,sz=26,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
coverages=[
    ("🏠","Homeowner's Insurance","[Carrier]","$[XXX,XXX]","$[X,XXX]/yr","[Green/Yellow/Red]"),
    ("🚗","Auto Insurance","[Carrier]","[Coverage Limits]","$[X,XXX]/yr","[Green/Yellow/Red]"),
    ("☂️","Umbrella Policy","[Carrier]","$[X,XXX,XXX]","$[XXX]/yr","[Green/Yellow/Red]"),
    ("❤️","Life Insurance","[Carrier]","$[XXX,XXX]","$[XXX]/yr","[Green/Yellow/Red]"),
]
for i,(icon,ctype,carrier,limits,premium,status) in enumerate(coverages):
    y=1.5+i*1.35
    rect(sl,0.3,y,12.73,1.2,PWHT)
    txt(sl,icon,0.5,y+0.25,0.7,0.7,sz=20,color=PNAV)
    txt(sl,ctype,1.3,y+0.1,3.5,0.5,sz=13,bold=True,color=PNAV)
    txt(sl,carrier,1.3,y+0.65,3.5,0.45,sz=11,color=PDGR)
    txt(sl,limits,5.0,y+0.3,3.0,0.6,sz=12,color=PDGR)
    txt(sl,premium,8.2,y+0.3,2.0,0.6,sz=13,bold=True,color=PNAV)
    txt(sl,status,10.5,y+0.3,2.3,0.6,sz=12,bold=True,color=PRGB(39,174,96))
# Slide 4 — Recommendations
sl=blank(prs)
rect(sl,0,0,13.33,1.3,PNAV)
txt(sl,"MY RECOMMENDATIONS FOR YOU",0.5,0.25,12,0.8,sz=26,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
rec_areas=[
    ("Coverage Gap Identified","Consider adding an umbrella policy. Your current liability limits may be insufficient for your assets.","High Priority"),
    ("Rate Opportunity","I found a comparable policy with [Carrier B] at $[X] less per year for identical coverage.","Rate Savings"),
    ("Cross-Sell Opportunity","You don't have life insurance on file. Based on your income and dependents, I recommend [X] in coverage.","Recommended"),
    ("Coverage Enhancement","Your current home policy doesn't include water backup coverage — this gap costs only $[X]/year to fill.","Consider"),
]
for i,(title,desc,priority) in enumerate(rec_areas):
    col=i%2; row=i//2
    x=0.3+col*6.5; y=1.5+row*2.6
    rect(sl,x,y,6.2,2.4,PLGR)
    rect(sl,x,y,6.2,0.6,PACC if priority=="High Priority" else PNAV)
    txt(sl,f"{priority}",x+0.15,y+0.1,5.9,0.45,sz=12,bold=True,color=PWHT)
    txt(sl,title,x+0.15,y+0.75,5.9,0.55,sz=13,bold=True,color=PNAV)
    txt(sl,desc,x+0.15,y+1.35,5.9,1.0,sz=10,color=PDGR)

prs.save(BASE+p12+"Insurance_Review_Presentation.pptx")
print(f"  ✓ {p12}Insurance_Review_Presentation.pptx")

# PPTX 2: New Client Welcome
prs2=new_prs()
sl=blank(prs2)
rect(sl,0,0,7.0,7.5,PNAV)
rect(sl,7.0,0,6.33,7.5,PACC)
txt(sl,"WELCOME TO",0.4,1.0,6.2,0.9,sz=30,bold=True,color=PGLD)
txt(sl,"[AGENCY NAME]",0.4,1.9,6.2,1.2,sz=36,bold=True,color=PWHT)
txt(sl,"Your Independent Insurance Professionals",0.4,3.2,6.2,0.8,sz=16,color=PRGB(189,195,199))
txt(sl,"We're honored to protect what matters most to you.",0.4,4.2,6.2,1.0,sz=14,color=PWHT)
txt(sl,"WHAT HAPPENS NEXT",7.3,0.5,5.7,0.8,sz=22,bold=True,color=PWHT)
next_steps=[
    ("📄","Policy Documents","You'll receive your policy documents within 3-5 business days"),
    ("📞","30-Day Check-In","I'll call in 30 days to make sure everything is perfect"),
    ("📅","Annual Review","Every year we'll review your coverage together"),
    ("🆘","Claims Support","If anything happens, call me first — I'll guide you through"),
    ("👋","I'm Always Here","For any changes, questions, or updates — one call does it all"),
]
for i,(icon,title,desc) in enumerate(next_steps):
    txt(sl,f"{icon} {title}",7.3,1.5+i*1.05,5.7,0.5,sz=13,bold=True,color=PWHT)
    txt(sl,desc,7.3,2.0+i*1.05,5.7,0.45,sz=10,color=PRGB(220,220,220))

sl=blank(prs2)
rect(sl,0,0,13.33,1.3,PNAV)
txt(sl,"YOUR POLICY AT A GLANCE",0.5,0.25,12,0.8,sz=26,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
details=[("Policy Number","[XXXXXXXX]"),("Effective Date","[MM/DD/YYYY]"),("Expiration Date","[MM/DD/YYYY]"),
         ("Carrier","[Carrier Name]"),("Annual Premium","$[X,XXX]"),("Payment Method","[Auto-Pay / Invoice]")]
for i,(label,val) in enumerate(details):
    col=i%2; row=i//2
    x=0.5+col*6.5; y=1.6+row*1.6
    rect(sl,x,y,6.0,1.4,PLGR)
    txt(sl,label,x+0.2,y+0.15,5.6,0.55,sz=12,bold=True,color=PNAV)
    txt(sl,val,x+0.2,y+0.75,5.6,0.55,sz=16,bold=True,color=PDGR)
txt(sl,"Your Agent: [Name] | [Phone] | [Email]",0.5,6.5,12,0.6,sz=14,color=PNAV,align=PP_ALIGN.CENTER)

prs2.save(BASE+p12+"New_Client_Welcome_Presentation.pptx")
print(f"  ✓ {p12}New_Client_Welcome_Presentation.pptx")

# PPTX 3: Monthly Market Update
prs3=new_prs()
sl=blank(prs3)
rect(sl,0,0,13.33,7.5,PNAV)
rect(sl,0,3.0,13.33,0.08,PACC)
txt(sl,"INSURANCE MARKET UPDATE",0.5,0.6,12.33,1.2,sz=38,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"[Month Year] | [Agency Name]",0.5,2.0,12.33,0.7,sz=22,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"Helping you navigate the changing insurance landscape",0.5,3.3,12.33,0.6,sz=16,color=PRGB(189,195,199),align=PP_ALIGN.CENTER)
txt(sl,"[Agent Name] | [Phone] | [Email]",0.5,6.5,12.33,0.6,sz=14,color=PRGB(150,150,150),align=PP_ALIGN.CENTER)

sl=blank(prs3)
rect(sl,0,0,13.33,1.3,PNAV)
txt(sl,"WHAT'S HAPPENING IN THE INSURANCE MARKET",0.5,0.25,12,0.8,sz=24,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
topics=[
    ("📈","Rate Trends","[Personal/Commercial] rates are trending [up/down] in our region due to [reason]. What this means for your renewal..."),
    ("⚠️","Coverage Alert","A recent court decision/regulatory change affects [coverage type]. Here's what you need to know..."),
    ("🌪️","Weather Impact","[Severe weather/catastrophe] season and its effect on [home/auto/commercial] rates in [region]..."),
    ("💡","New Product","We now offer [new coverage type] — perfect for clients who [description of need]..."),
    ("📋","Compliance Update","[State] has updated [regulation] affecting [line of business]. Here's how it impacts you..."),
    ("🎯","Action Item","If your policy renews in the next 90 days, now is the time to [specific recommendation]..."),
]
for i,(icon,title,desc) in enumerate(topics):
    col=i%2; row=i//3
    x=0.3+col*6.5; y=1.5+row*1.8
    rect(sl,x,y,6.2,1.65,PLGR)
    rect(sl,x,y,0.1,1.65,PACC)
    txt(sl,f"{icon} {title}",x+0.25,y+0.1,5.8,0.6,sz=13,bold=True,color=PNAV)
    txt(sl,desc,x+0.25,y+0.7,5.8,0.85,sz=10,color=PDGR)

prs3.save(BASE+p12+"Market_Update_Template.pptx")
print(f"  ✓ {p12}Market_Update_Template.pptx")

# PPTX 4: Social Media Content Pack
prs4=new_prs()
sl=blank(prs4)
rect(sl,0,0,13.33,7.5,PNAV)
rect(sl,1.0,0.6,11.33,6.3,PACC)
rect(sl,1.2,0.8,10.93,5.9,PNAV)
txt(sl,"DID YOU KNOW?",1.5,1.2,10.33,0.8,sz=24,bold=True,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"Most homeowner's policies\nDO NOT cover floods.",1.5,2.1,10.33,1.8,sz=32,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"🌊 You need a separate flood insurance policy.",1.5,4.0,10.33,0.7,sz=16,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"Comment FLOOD below and I'll explain your options!",1.5,4.8,10.33,0.7,sz=14,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"[Your Name] | [Phone] | [Agency]",1.5,5.7,10.33,0.5,sz=12,color=PRGB(150,150,150),align=PP_ALIGN.CENTER)

sl=blank(prs4)
rect(sl,0,0,13.33,7.5,PLGR)
rect(sl,0,0,13.33,1.8,PNAV)
txt(sl,"💡 INSURANCE TIP OF THE WEEK",0.5,0.15,12,0.7,sz=22,bold=True,color=PGLD)
txt(sl,"Bundle Your Home + Auto",0.5,0.9,12,0.7,sz=20,color=PWHT)
tip="Bundling your home and auto insurance with the same carrier can save you 10-25% on BOTH policies. Most people don't realize how much they're leaving on the table by having separate carriers.\n\nWhen did you last compare? I'll run a free comparison for you!"
txt(sl,tip,0.5,2.2,9.0,4.0,sz=14,color=PDGR)
rect(sl,9.8,2.2,3.2,4.0,PNAV)
txt(sl,"AVERAGE\nSAVINGS",9.9,2.5,3.0,1.0,sz=14,bold=True,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"$400-$800\nper year",9.9,3.6,3.0,1.0,sz=20,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"DM me for a FREE comparison!",9.9,4.7,3.0,1.0,sz=11,color=PRGB(189,195,199),align=PP_ALIGN.CENTER)
txt(sl,"[Your Name] | [Agency] | [Phone]",0.5,6.5,12,0.6,sz=12,color=PRGB(150,150,150))

sl=blank(prs4)
rect(sl,0,0,13.33,7.5,PACC)
rect(sl,0.4,0.4,12.53,6.7,PNAV)
txt(sl,"⚠️ ARE YOU UNDERINSURED?",0.7,0.7,11.93,0.8,sz=24,bold=True,color=PGLD)
txt(sl,"3 Signs Your Coverage Isn't Enough",0.7,1.6,11.93,0.7,sz=20,color=PWHT,align=PP_ALIGN.CENTER)
signs=[
    ("1","You've never done a coverage review with your agent"),
    ("2","Your liability limits are at state minimums"),
    ("3","You don't have an umbrella policy"),
]
for i,(num,sign) in enumerate(signs):
    rect(prs4.slides[-1],0.7,2.5+i*1.2,11.93,1.0,PRGB(30,70,120))
    txt(prs4.slides[-1],num,0.9,2.55+i*1.2,0.6,0.9,sz=22,bold=True,color=PGLD)
    txt(prs4.slides[-1],sign,1.6,2.6+i*1.2,10.8,0.8,sz=16,color=PWHT)
txt(prs4.slides[-1],"DM me for a FREE coverage review — let's fix this together.",0.7,6.0,11.93,0.7,sz=14,color=PGLD,align=PP_ALIGN.CENTER)

sl=blank(prs4)
rect(sl,0,0,13.33,7.5,PLGR)
rect(sl,0,0,13.33,0.7,PNAV)
rect(sl,0,6.9,13.33,0.6,PNAV)
txt(sl,"🛡️ 5-STAR REVIEW",0.5,0.1,12,0.55,sz=18,bold=True,color=PGLD,align=PP_ALIGN.CENTER)
rect(sl,1.5,0.8,10.33,5.9,PWHT)
txt(sl,'"[Client Name]" ⭐⭐⭐⭐⭐',2.0,1.0,9.33,0.7,sz=16,bold=True,color=PNAV)
review_text='"[Agent Name] has been our insurance agent for [X] years and we couldn\'t be happier. When we had a claim last year, [he/she] was there every step of the way — made sure the carrier treated us fairly and the whole thing was resolved in just 2 weeks. I send everyone I know to [Agency Name]."'
txt(sl,review_text,2.0,1.8,9.33,3.0,sz=14,color=PDGR)
txt(sl,"— [Client Name], [City] | [Policy Type] Client",2.0,4.9,9.33,0.6,sz=12,color=PRGB(150,150,150))
txt(sl,"Thank you [Client Name] — reviews like this mean everything to us! 🙏",1.8,5.7,9.7,0.6,sz=12,color=PACC)
txt(sl,"[Agency Name] | [Phone] | [Website]",0.5,6.93,12,0.4,sz=11,color=PGLD,align=PP_ALIGN.CENTER)

prs4.save(BASE+p12+"Social_Media_Content_Pack.pptx")
print(f"  ✓ {p12}Social_Media_Content_Pack.pptx")
print("✓ 12_CANVA_IMPORTABLE_TEMPLATES complete")

# ─── UPDATE README ──────────────────────────────────────────────────────────────
with open(BASE+"00_START_HERE/README_FIRST.txt","w",encoding="utf-8") as f:
    f.write("""WELCOME TO YOUR INSURANCE AGENCY OPERATING SYSTEM
===================================================
Original Value: €149 | Your Launch Price: €39
Thank you for your purchase! You now have a complete agency management system.

WHAT'S INSIDE:
--------------
00_START_HERE          → Start here — quick start guide and product overview
01_LEAD_GENERATION     → Phone scripts, email sequences, referral programs + CRM
02_SALES_PROCESS       → Needs analysis, proposals, objections, closing scripts
03_POLICY_SERVICES     → Onboarding SOP, annual review, cross-sell playbook
04_CLAIMS_SUPPORT      → FNOL SOP, advocacy guide, client communication templates
05_CLIENT_COMMUNICATION → Email library, text templates, phone scripts, newsletter
06_COMPLIANCE_LICENSING → E&O guide, compliance checklist, licensing, appointments
07_CARRIER_RELATIONSHIPS → Negotiation guide, submission guide, market access strategy
08_AGENCY_OPERATIONS   → Hiring guide, training program, ops manual, KPI dashboard
09_POST_SALE_RETENTION → Retention system, annual review scripts, appreciation program
10_NOTION_WORKSPACE    → 7 Notion databases + setup guide
11_BONUSES             → 365 social captions, scripts vault, growth playbook, product guide
12_CANVA_TEMPLATES     → 4 Canva-importable professional presentations

QUICK START (30 MINUTES):
--------------------------
1. Import CSVs from 10_NOTION_WORKSPACE into Notion (follow Notion_Setup_Guide.md)
2. Upload PPTX files from 12_CANVA_TEMPLATES to Canva.com
3. Open Agency_CRM.xlsx and import your existing leads and clients
4. Customize all DOCX templates with your name and agency info
5. Post your first content using 365_Social_Media_Captions.csv

Insurance Agency Operating System | Professional Edition
""")
print("  ✓ README_FIRST.txt updated")

# ─── MANIFEST + ZIP ────────────────────────────────────────────────────────────
all_files=[]
for root,dirs,files in os.walk(BASE):
    for fn in sorted(files):
        fp=os.path.join(root,fn)
        rel=os.path.relpath(fp,BASE)
        parts=rel.split(os.sep)
        folder=parts[0] if len(parts)>1 else "ROOT"
        ext=fn.rsplit('.',1)[-1].upper() if '.' in fn else 'UNKNOWN'
        size=os.path.getsize(fp)
        all_files.append({"file":rel,"folder":folder,"type":ext,"size_bytes":size})

with open(BASE+"00_START_HERE/Asset_Manifest.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    w.writerow(["File","Folder","Type","Size (bytes)"])
    for item in all_files: w.writerow([item["file"],item["folder"],item["type"],item["size_bytes"]])

manifest={"product":"Ultimate Insurance Agency Operating System","version":"1.0",
          "price_original":"€149","price_launch":"€39","total_files":len(all_files),"files":all_files}
with open(BASE+"00_START_HERE/Asset_Manifest.json","w",encoding="utf-8") as f:
    json.dump(manifest,f,indent=2)
print(f"  ✓ Asset Manifest: {len(all_files)} files indexed")

zip_path="/home/user/oqul-phase55-production/insurance-agency-os/BUYER_DOWNLOAD_InsuranceAgencyOS.zip"
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as zf:
    for root,dirs,files in os.walk(BASE):
        for fn in sorted(files):
            fp=os.path.join(root,fn)
            arcname=os.path.relpath(fp,os.path.dirname(BASE))
            zf.write(fp,arcname)

zip_size=os.path.getsize(zip_path)/(1024*1024)
print(f"\n✅ ZIP: BUYER_DOWNLOAD_InsuranceAgencyOS.zip ({zip_size:.1f} MB)")
print(f"   Total files: {len(all_files)}")
print("\nPART 4 DONE — Insurance Agency OS COMPLETE")
