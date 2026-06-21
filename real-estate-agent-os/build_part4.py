#!/usr/bin/env python3
"""Real Estate Agent OS - Part 4: Bonuses, PDFs, PPTX, Manifest, ZIP"""
import os, csv, json, zipfile
from docx import Document
from docx.shared import Pt, RGBColor
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor as PRGB
from pptx.enum.text import PP_ALIGN

BASE = "/home/user/oqul-phase55-production/real-estate-agent-os/Ultimate_Real_Estate_Agent_Operating_System/"
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

# ─── 11_BONUSES ───────────────────────────────────────────────────────────────
p11 = "11_BONUSES/"

# 365 Social Media Captions
categories = [
    ("Buyer Tips", [
        "Your credit score is one of the most important factors in getting a great mortgage rate. Start improving it 6 months before you plan to buy.",
        "Get pre-approved BEFORE you start house hunting. It gives you a clear budget and makes your offer much more competitive.",
        "The difference between list price and sale price in today's market might surprise you. Ask your agent for recent comps before making an offer.",
        "First-time buyer tip: Budget for closing costs on top of your down payment — they typically run 2-5% of the purchase price.",
        "Don't make any large purchases or open new credit accounts while under contract. It can affect your mortgage approval.",
        "A home inspection is NOT optional. Spending $400-$600 upfront can save you from a $40,000 surprise after closing.",
        "Love at first sight is real in real estate — but always come back for a second showing before writing an offer.",
        "Buying a home is the single largest investment most people will ever make. Work with an agent who treats it that way.",
        "The neighborhood matters as much as the house. Visit at different times of day before making a decision.",
        "Your home should meet your needs for the next 5-7 years, not just today. Think about how your life might change.",
        "Bidding wars are stressful — but having the right agent in your corner makes all the difference.",
        "Always negotiate. Even in a seller's market, there's often room for closing cost credits or repairs.",
        "Square footage isn't everything. A well-designed 1,500 sq ft home can live larger than a poorly laid out 2,000 sq ft home.",
        "The school district matters even if you don't have kids — it affects resale value significantly.",
        "Fixer-uppers can be great opportunities, but always get a contractor's estimate before making an offer.",
        "HOA fees can add hundreds to your monthly housing costs. Always factor them into your budget.",
        "Your earnest money deposit shows the seller you're serious. In competitive markets, more EMD can win deals.",
        "Never skip the final walkthrough before closing. Make sure repairs were completed and the home is in agreed condition.",
        "Flood zones, flight paths, and traffic patterns — these are things photos don't show. Research the area thoroughly.",
        "Buying a home with more space than you need today gives you room to grow without moving in 3 years.",
        "The best time to buy a home is when you're financially ready and have found the right property — not when the market 'bottoms out.'",
        "Ask about utility costs before making an offer. A $400/month electric bill can break a budget.",
        "Title insurance protects you from ownership disputes and hidden liens. Never skip it — it's a one-time premium.",
        "When comparing homes, price per square foot helps you make apples-to-apples comparisons.",
        "Seller disclosures are your right as a buyer. Read every line — what's disclosed (and what's not) tells a story.",
        "New construction homes have negotiation room too — upgrades, lot premiums, and closing costs are all on the table.",
        "An adjustable-rate mortgage can save you money short-term — but understand the risks if rates rise.",
        "Your offer is more than price. Terms like close date, contingencies, and flexibility matter to sellers too.",
        "Moving into a home that's been lived in is a feature, not a bug — the landscaping is already established.",
        "Buying below your maximum budget gives you financial breathing room for life's unexpected expenses.",
        "Don't fall in love with a home until you've seen the inspection report. Knowledge is power.",
        "The right agent will tell you when NOT to buy a home — not just push you to close.",
        "Pre-approval letters expire. If your home search takes longer than 90 days, get a fresh one.",
        "Water in the basement is a major red flag. Always ask about water intrusion history.",
        "When rates drop 1%, your buying power increases by roughly 10%. Small rate changes = big impact.",
        "Buying in a growing neighborhood today can mean significant appreciation in 5-10 years.",
    ]),
    ("Seller Tips", [
        "Curb appeal is your home's first impression — fresh mulch, trimmed bushes, and a clean front door make a huge difference.",
        "Decluttering is the highest ROI prep you can do before listing. Buyers need to visualize their belongings, not yours.",
        "Professional photography is non-negotiable in today's market. 95% of buyers search online first.",
        "Pricing your home right from day 1 generates the most buyer activity — and the best offers.",
        "Every week your home sits on the market, buyers assume something is wrong with it. Strategic pricing prevents this.",
        "Neutral paint colors help buyers visualize their own furniture and style. Bold colors can actually cost you money.",
        "Small upgrades with big returns: fresh paint, new hardware, updated light fixtures, clean carpets.",
        "Staged homes sell 73% faster and for up to 10% more than unstaged homes. It's worth the investment.",
        "Be flexible with showings — the less accessible your home is, the fewer buyers will see it.",
        "Leaving during showings makes buyers more comfortable exploring and discussing the home honestly.",
        "The first 2 weeks on the market are when you get the most buyer activity. Use them wisely.",
        "Over-improving for your neighborhood can actually hurt your sale price — know the ceiling.",
        "Your agent should be marketing your home on Zillow, Realtor.com, social media, AND to their buyer database.",
        "A pre-listing inspection can eliminate buyer objections and speed up the closing process.",
        "Sellers who are too emotionally attached to their asking price often net less in the end.",
        "Repair the obvious things before listing — a leaky faucet or broken fixture screams deferred maintenance.",
        "Don't overprice hoping to negotiate down. Overpriced homes often sell below market when they finally reduce.",
        "Your listing photos are your home's first showing — invest in a professional photographer.",
        "Consider a pre-listing appraisal if your home has unique features that make comparisons difficult.",
        "Accept or counter offers quickly — losing momentum in negotiations costs money.",
        "Buyers will lowball if they sense desperation. Your agent's job is to present your home — and you — confidently.",
        "Deep cleaning your home before every showing is essential. Smell is the first thing buyers notice.",
        "Remove personal photos and memorabilia. Help buyers see themselves in the home, not you.",
        "Smart home upgrades (smart thermostat, video doorbell) are inexpensive and very attractive to buyers.",
        "Keep your pets and pet items out of sight during showings. Not everyone is a pet lover.",
        "Garage organization matters. Buyers judge storage by what they see — a tidy garage signals a well-maintained home.",
        "Know your mortgage payoff amount before listing so you can calculate your real net proceeds.",
        "Capital gains tax applies to profits over $250K (single) or $500K (married) on a primary residence sale.",
        "Seller closing costs typically run 8-10% of the sale price when you include commission, title, and transfer taxes.",
        "A great agent doesn't just list your home — they market it aggressively and negotiate on your behalf.",
        "Multiple offer situations are won or lost based on how your agent presents your home and reviews offers.",
        "Listing in spring and summer typically generates the most buyer activity — but great homes sell year-round.",
        "Be honest on disclosure forms. Hiding known defects can lead to lawsuits after closing.",
        "Your closing timeline is negotiable. A flexible close date can make your listing more attractive.",
        "Accepting the highest offer isn't always the best move — terms, contingencies, and buyer strength matter.",
        "A seller's market doesn't mean you can ignore presentation. Competition is always there.",
    ]),
    ("Market Insights", [
        "Mortgage rates and home prices don't always move together. Understanding both is key to timing your move.",
        "The real estate market is local — national headlines rarely reflect what's happening in your specific neighborhood.",
        "Inventory levels drive everything. Low supply = seller's market. High supply = buyer's market.",
        "Median days on market is one of the best indicators of whether it's a buyer's or seller's market right now.",
        "A buyer's market means more negotiating power — sellers are competing for fewer buyers.",
        "In a seller's market, homes often receive multiple offers within 48 hours of listing.",
        "Real estate appreciates over time. The 10-year average annual appreciation rate is 3-5% nationally.",
        "Seasonality affects real estate — spring is typically the busiest season for listings and sales.",
        "Interest rate changes of even 0.5% can significantly impact monthly mortgage payments.",
        "Price reductions are a signal — they indicate a home was overpriced or the market has shifted.",
        "New listing activity in your area tells you a lot about seller confidence in the current market.",
        "The absorption rate (how quickly inventory sells) tells you how many months of supply exist in the market.",
        "Cash buyers have a significant advantage in competitive markets — no financing contingency speeds things up.",
        "Real estate is the only investment where you can live in what you own while it appreciates.",
        "Foreclosures and distressed properties can offer value but also carry unknown risks — research thoroughly.",
        "Commercial and residential real estate markets don't always move in the same direction.",
        "Local employment growth and corporate relocations drive housing demand in a market.",
        "Zoning changes and new developments can dramatically impact property values — stay informed.",
        "Population migration patterns shape which markets are growing and which are cooling.",
        "The 'lock-in effect' — homeowners with low-rate mortgages reluctant to sell — is limiting inventory nationwide.",
        "New construction permits are a leading indicator of future housing supply in a market.",
        "Property taxes vary widely by location and can significantly impact total homeownership cost.",
        "Home affordability (income-to-price ratio) is the real measure of whether a market is accessible.",
        "Rising rents often push renters toward buying — understanding this helps predict buyer demand.",
        "Second-home and investment property markets follow slightly different rules than primary residence markets.",
        "Remote work has permanently changed where people want to live — suburban and rural markets are now thriving.",
        "Luxury market trends often predict where the broader market is headed 12-18 months later.",
        "Year-over-year price comparisons can be misleading — look at 5-year trends for a fuller picture.",
        "Real estate cycles: expansion, peak, contraction, trough — understanding where you are in the cycle is crucial.",
        "Transaction volume matters as much as price — a falling-volume market signals uncertainty ahead.",
        "First-time buyer programs and down payment assistance programs expand access to homeownership.",
        "The wealth gap between homeowners and renters continues to grow — homeownership builds long-term wealth.",
        "Bridge loans help sellers purchase before their current home sells — a solution in tight inventory markets.",
        "1031 exchanges allow investors to defer capital gains taxes by rolling proceeds into a new investment property.",
        "Market corrections happen — but homeowners who stay through cycles almost always come out ahead.",
        "The local job market is the single biggest driver of housing demand in any city or suburb.",
    ]),
    ("Agent Value & Trust", [
        "A great real estate agent saves you more than their commission — in time, stress, and negotiating power.",
        "I don't just open doors — I negotiate, strategize, and protect your interests through every step of the transaction.",
        "Real estate transactions involve dozens of deadlines, dozens of documents, and dozens of people. You need a professional managing it all.",
        "My job doesn't end at contract acceptance — I manage the entire transaction from contract to close.",
        "When you work with me, you're not just getting an agent — you're getting my entire network of lenders, inspectors, and contractors.",
        "I've helped [X] families buy and sell in this area. That experience pays dividends for every client I serve.",
        "The right agent tells you hard truths. I'll tell you when a home is overpriced, over-improved, or not the right fit.",
        "I work by referral — which means my reputation is everything. Your satisfaction is my business model.",
        "I answer my phone. I respond to texts. I show up on time. In a world of excuses, reliability is a superpower.",
        "My market knowledge is up to date every single day. When you ask me a question, you get a real answer — not a guess.",
        "Representation matters. Without an agent, you're negotiating against professionals who do this every day.",
        "I go to continuing education, industry events, and training consistently — so I can serve you at the highest level.",
        "The commission conversation is easy when you understand what I actually do for you. Let me walk you through it.",
        "My goal isn't to close one deal with you — it's to be your real estate advisor for life.",
        "I've seen the mistakes buyers and sellers make without representation. My job is to make sure you never make them.",
        "I specialize in this market. I know the streets, the schools, the trends, and the values — and I put that to work for you.",
        "Every transaction has problems. The difference is an experienced agent solves them before you even know they exist.",
        "I'm transparent about everything — fees, timelines, challenges, and realistic expectations. Always.",
        "My clients refer their friends and family to me — that tells you everything you need to know about my service.",
        "Buying or selling a home is one of the biggest decisions you'll ever make. Choose your agent carefully.",
        "I've been in this business long enough to know: the market changes, but the principles of exceptional service never do.",
        "The best time to interview agents is before you need one. If you're thinking about making a move, let's talk now.",
        "I don't do cookie-cutter marketing. Every listing I take gets a customized strategy based on the property and market.",
        "Technology has changed real estate marketing dramatically — and I've embraced every tool that serves my clients better.",
        "I treat every transaction as if it were my own home. That standard of care shows in every detail.",
        "Referrals are the greatest compliment I receive. If I've served you well, please pass my name along.",
        "My job is to make the complex simple. Real estate has a lot of moving parts — I keep them all organized for you.",
        "I've negotiated [X] transactions. That experience means I know when to push, when to hold, and when to walk away.",
        "A good agent brings you opportunities. A great agent brings you the right opportunities for your specific goals.",
        "I measure my success by one thing: did my client achieve their real estate goals? Everything else is secondary.",
        "The transaction is done at closing. The relationship is just beginning.",
        "Real estate is my passion, not just my profession. That makes a difference in the service you receive.",
        "I invest in professional photography, staging consultation, and video for every listing. Your home deserves it.",
        "Communication is the #1 thing clients say they want from their agent — and it's what I deliver, consistently.",
        "When you choose me, you choose someone who will fight for your best interests — every single day.",
        "The real estate market is always changing. I study it so you don't have to.",
    ]),
    ("Neighborhood & Community", [
        "The best neighborhoods are defined not just by the homes, but by the people, the amenities, and the community feel.",
        "Local parks, good schools, and walkable dining — these are the features that hold and grow property values over time.",
        "Supporting local businesses isn't just good citizenship — it builds the kind of community that makes neighborhoods desirable.",
        "Getting to know your neighbors before you buy is one of the smartest things you can do. Attend an open house event.",
        "Commute time affects quality of life more than almost any other factor in where you live. Consider it carefully.",
        "New restaurants, coffee shops, and boutiques moving into an area are often early signs of neighborhood appreciation.",
        "The best neighborhoods to invest in are the ones where people WANT to move — follow the development activity.",
        "School ratings don't tell the whole story — visit schools, talk to parents, and look at trend data over time.",
        "Walkability scores matter more than ever — people want to be able to walk to things they love.",
        "A neighborhood with strong community events — farmer's markets, festivals, block parties — is a neighborhood that holds value.",
        "Infrastructure investment (new roads, transit lines, parks) signals that an area is a priority for the city.",
        "Gentrifying neighborhoods offer opportunity — but come with considerations about community and displacement.",
        "Crime statistics are important but don't tell the whole story. Visit the neighborhood at different times and days.",
        "Noise levels from traffic, airports, or commercial activity significantly impact quality of life and resale value.",
        "Green space and parks within walking distance are a consistent driver of residential property values.",
        "A neighborhood with diverse age groups tends to be more stable and community-oriented over time.",
        "Before you buy, research the HOA's financial health — underfunded reserves lead to special assessments.",
        "Local economic drivers (major employers, universities, hospitals) make a neighborhood more recession-resistant.",
        "Flood zone status can affect both insurability and resale potential — always check FEMA flood maps.",
        "The fastest-appreciating neighborhoods are often those adjacent to already-desirable areas.",
        "Historic districts offer charm and often strict design standards that protect neighborhood character.",
        "New construction communities offer warranties and modern features but lack the mature trees and character of established neighborhoods.",
        "Mixed-use developments (live-work-play) are driving some of the most exciting neighborhood transformations.",
        "Public transit access is becoming increasingly important — especially for millennial buyers.",
        "Community gardens, dog parks, and bike trails are magnets for the buyers who will be your future neighbors.",
        "When you buy in a neighborhood, you're also investing in the schools, safety, and quality of life for your family.",
        "The neighborhood you choose today shapes your social life, your commute, and your children's education.",
        "Asking neighbors about the area gives you insights no Zillow listing can provide.",
        "A walkthrough of the neighborhood on a Saturday afternoon tells you more than any data sheet.",
        "The best neighborhoods balance convenience, character, safety, and community — find yours.",
        "Local property tax rates vary widely — understand what you'll pay annually before you decide.",
        "Older neighborhoods often have better construction quality — solid bones matter more than new finishes.",
        "Know what's planned for that empty lot next door before you buy. Future development can help OR hurt.",
        "Neighborhood Facebook groups and Nextdoor profiles give you a real sense of community dynamics.",
        "The neighborhood you buy in today could look very different in 10 years. Research what's coming.",
        "The best investment advice for real estate is timeless: location, location, location.",
    ]),
    ("Investment & Wealth", [
        "Real estate is one of the few investments where you can use leverage — borrow 80% to control 100% of an appreciating asset.",
        "A rental property that cash flows $500/month generates $6,000/year in passive income — in addition to equity growth.",
        "The BRRRR strategy: Buy, Rehab, Rent, Refinance, Repeat — a proven wealth-building framework for investors.",
        "House hacking means buying a small multi-family property, living in one unit, and having tenants pay your mortgage.",
        "1031 exchanges allow real estate investors to defer capital gains taxes indefinitely by rolling into new properties.",
        "The cap rate (Net Operating Income / Property Value) tells you how efficiently a rental property generates income.",
        "Real estate vs. stocks: real estate offers tax advantages, leverage, and a tangible asset — stocks offer liquidity.",
        "Appreciation + cash flow + debt paydown + tax benefits = four ways real estate builds wealth simultaneously.",
        "The best rental markets combine affordable prices, strong rental demand, and landlord-friendly laws.",
        "Short-term rentals (Airbnb) can generate 2-3x the monthly income of traditional long-term rentals — but require more management.",
        "Vacation rental markets are location-specific — research local occupancy rates and regulations before investing.",
        "Real estate syndications allow passive investors to participate in commercial deals without active management.",
        "REITs (Real Estate Investment Trusts) offer real estate exposure without the complexity of direct ownership.",
        "Depreciation allows rental property owners to deduct the 'wear and tear' on a property — a powerful tax shelter.",
        "Home equity is the largest store of wealth for most American families — protect and grow it strategically.",
        "A home equity line of credit (HELOC) can fund investment property down payments — using your primary residence as leverage.",
        "The price-to-rent ratio tells you whether it makes more sense to buy or rent in a given market.",
        "Cash-on-cash return measures the annual return on the actual cash you invested — aim for 8% or higher.",
        "Real estate investing requires patience — most wealth is built over 10+ years, not 10 months.",
        "Location selection is the most important decision in real estate investing. A great property in the wrong area underperforms.",
        "Rental property management takes time — factor in 5-10% management fees if you hire a property manager.",
        "Rent growth in your market is one of the strongest indicators of a healthy investment property market.",
        "Multi-family properties (duplexes, triplexes) qualify for residential financing — lower rates than commercial loans.",
        "Value-add investing means buying underperforming properties, improving them, and increasing rents — a classic wealth strategy.",
        "Tax-deferred retirement accounts (self-directed IRAs) can hold real estate investments — consult a tax advisor.",
        "Real estate pairs well with a stock portfolio — low correlation provides diversification and stability.",
        "The neighborhood life cycle (growth, stability, decline, revitalization) determines investment timing and risk.",
        "Due diligence on a rental property includes reviewing leases, utility costs, maintenance history, and local rental comps.",
        "A property manager earns their fee when they handle problem tenants, maintenance calls, and legal compliance for you.",
        "Never buy an investment property without running the numbers on worst-case scenarios — vacancies, repairs, rate hikes.",
        "Commercial real estate (retail, office, industrial) offers higher yields but requires more sophisticated analysis.",
        "Real estate crowdfunding platforms now allow investors to start with as little as $500.",
        "Land banking (buying raw land in the path of development) is a patient strategy with significant potential returns.",
        "Net lease properties (NNN) have tenants pay most expenses — passive income with minimal landlord responsibility.",
        "Real estate investing builds more millionaires than any other asset class. The time to start is now.",
        "Every property you buy is a business. Treat it like one: track income, expenses, and ROI meticulously.",
    ]),
    ("Home Improvement & Value", [
        "Kitchen remodels consistently deliver some of the highest ROI of any home improvement — up to 80% return.",
        "A fresh coat of neutral paint is the most cost-effective way to transform a space before selling.",
        "Bathroom updates don't have to be expensive — new fixtures, a new vanity, and fresh grout can make a dramatic difference.",
        "Landscaping and curb appeal improvements return $1.09 for every $1 spent — among the highest ROI of any project.",
        "Energy efficiency upgrades (new windows, insulation, HVAC) save money on utilities AND increase home value.",
        "Hardwood floors consistently rank as one of the most desirable home features — and they last forever.",
        "A finished basement can add 10-20% to a home's livable square footage and significantly boost value.",
        "Smart home technology (Nest thermostat, Ring doorbell, smart locks) is increasingly expected by buyers.",
        "New garage doors are one of the highest ROI exterior upgrades — often returning 90%+ of their cost.",
        "Replacing an aging roof before listing removes one of the biggest buyer objections and inspection concerns.",
        "Updated lighting transforms a home — remove builder-grade fixtures and replace with statement pieces.",
        "Decluttering and deep cleaning cost almost nothing but dramatically increase how a home shows.",
        "A clean, organized closet makes a storage-hungry buyer fall in love with your home.",
        "Granite and quartz countertops in the kitchen remain a top feature buyers are willing to pay a premium for.",
        "Stainless steel appliances are the minimum expectation in today's market — mismatched appliances hurt listings.",
        "Pressure washing driveways, decks, and siding is a $150 transformation that makes a home look brand new.",
        "Adding a deck or patio can return 60-80% of its cost and dramatically increases a home's usable living space.",
        "In-law suites and ADUs (accessory dwelling units) are in high demand — they add flexibility and rental income potential.",
        "Home offices are now a top priority for buyers — dedicate a clean, well-lit room as a dedicated workspace.",
        "Ceiling fans are a cost-effective upgrade that adds comfort, energy savings, and a finished look to any room.",
        "Replacing dated brass fixtures with brushed nickel or matte black instantly modernizes a home.",
        "A power-washed exterior, replaced shutters, and painted front door can add thousands in perceived value.",
        "Open floor plans remain highly desirable — if walls can be removed (non-load-bearing), it's worth considering.",
        "Window treatments are often overlooked but make a huge difference in how finished and luxurious a home feels.",
        "A fresh, well-maintained lawn with defined edges signals a well-cared-for property to buyers.",
        "Before any major renovation, research what buyers in your specific market are actually paying a premium for.",
        "Over-improving for your neighborhood ceiling means you'll never recoup the investment at sale.",
        "Focus improvement dollars on kitchens, bathrooms, curb appeal, and condition — these move the needle most.",
        "Converting unused attic space to a bedroom can dramatically increase both square footage and home value.",
        "Outdated popcorn ceilings are a buyer turnoff — removing them is relatively affordable and makes a big impact.",
        "Master suite additions consistently rank as one of the highest-return major renovation projects.",
        "Don't put expensive renovation money into a home you plan to sell in under 2 years — focus on staging instead.",
        "New interior doors, baseboards, and crown molding give a home a polished, custom-built feel buyers love.",
        "A well-designed mudroom or laundry room with built-in storage is now a top-requested feature.",
        "Concrete driveways and clean, modern landscaping dramatically improve that critical first-impression moment.",
        "The best renovations solve real problems — wet basements, small closets, outdated electrical. Fix what hurts.",
    ]),
    ("Mortgage & Finance", [
        "Your debt-to-income ratio (DTI) is one of the most critical factors lenders use to determine your loan amount.",
        "Conventional loans require as little as 3% down for first-time buyers. FHA loans start at 3.5%.",
        "VA loans offer eligible veterans zero down payment with no PMI — one of the best mortgage products available.",
        "PMI (Private Mortgage Insurance) is required when you put less than 20% down — it adds to your monthly payment.",
        "You can remove PMI once you reach 20% equity — either through payments or appreciation. Ask your lender how.",
        "A 30-year mortgage keeps monthly payments lower. A 15-year mortgage builds equity faster and saves on interest.",
        "Getting quotes from 3+ lenders when buying can save you thousands over the life of your loan.",
        "Mortgage points allow you to buy down your interest rate upfront — run the math to see if it makes sense.",
        "Fixed-rate mortgages provide payment certainty. Adjustable-rate mortgages can offer savings in the short term.",
        "Pre-qualification vs. pre-approval: pre-approval requires verified income/assets and carries much more weight with sellers.",
        "Your mortgage rate is determined by credit score, down payment %, loan type, property type, and market conditions.",
        "A 1% increase in interest rates reduces your buying power by roughly 10%. Stay on top of rate movements.",
        "Closing costs typically run 2-5% of the loan amount and include origination fees, title, appraisal, and escrow.",
        "Sellers can contribute toward buyer closing costs in the purchase negotiation — ask your agent about seller concessions.",
        "Mortgage pre-approvals typically expire in 60-90 days — don't let yours lapse during an extended home search.",
        "Rate locks protect you from rising rates while your loan is processing — ask your lender about lock periods.",
        "USDA loans offer zero down payment for eligible rural and suburban properties — a powerful option for qualifying buyers.",
        "Down payment assistance programs exist in almost every state — many buyers who qualify never know they exist.",
        "Your income stability matters to lenders — 2+ years of consistent employment in the same field strengthens your application.",
        "Self-employed buyers need 2 years of tax returns showing consistent income — start planning 2 years ahead.",
        "Student loan debt affects your DTI ratio — work with a lender who understands how to optimize your profile.",
        "Bank statements, pay stubs, and tax returns form the foundation of your mortgage application — keep them organized.",
        "Cash gifts from family for down payments are allowed — but you'll need a gift letter from the donor for your file.",
        "Refinancing when rates drop 0.75-1% or more can save significant money over the remaining loan term.",
        "A cash-out refinance lets you access home equity for renovations, investments, or debt payoff.",
        "Rate-and-term refinancing reduces your rate or loan term without extracting equity — simplest refinance type.",
        "Mortgage forbearance was a COVID-era tool — understand how it differs from deferment and what it means for credit.",
        "Biweekly mortgage payments result in one extra payment per year — shaving years off a 30-year mortgage.",
        "Making extra principal payments early in your loan dramatically reduces total interest paid over the life of the loan.",
        "Home equity grows from 3 sources: appreciation, mortgage paydown, and improvements. Track all three.",
        "FHA loans have more lenient credit requirements — good for buyers who don't quite qualify for conventional financing.",
        "The loan estimate (LE) shows all costs upfront — compare LEs from multiple lenders side by side.",
        "Jumbo loans (over conforming loan limits) require stronger credit and larger down payments than conventional loans.",
        "Your earnest money deposit is typically credited toward your down payment at closing — it's not an additional cost.",
        "Consider total cost of ownership: mortgage + taxes + insurance + HOA + maintenance = your real housing budget.",
        "The amortization schedule shows exactly how much of each payment goes to principal vs. interest — early payments are mostly interest.",
    ]),
    ("Open House Tips", [
        "Open houses are one of the most powerful lead generation tools in real estate — use them strategically.",
        "Arrive 30-45 minutes early to an open house to set up, air out the home, and turn on all lights.",
        "Having a guest sign-in sheet at every open house is non-negotiable — those names are your next clients.",
        "Offer water, coffee, and a light snack at open houses — people stay longer when they're comfortable.",
        "Feature sheets with photos, specs, and neighborhood highlights should be ready for every visitor.",
        "Follow up with every open house contact within 24 hours while you're still fresh in their mind.",
        "Ask open house visitors one key question: 'What are you looking for that you haven't found yet?' Then listen.",
        "The best open houses feel like an experience, not just a showing. Create an atmosphere buyers remember.",
        "Fresh flowers on the kitchen counter and a light, pleasant scent make open houses more inviting.",
        "Park your car away from the property to leave curb spots for visiting buyers.",
        "Know the neighborhood stats cold — days on market, recent sales, school ratings. Buyers will ask.",
        "Sunset open houses with strategic lighting create a warm, inviting ambiance that photos can't capture.",
        "Advertise your open house on Zillow, social media, Nextdoor, and with neighborhood directional signs.",
        "Host broker opens (for agent colleagues) before public opens to generate MLS-to-buyer connections.",
        "The goal of an open house isn't just to sell THAT home — it's to meet buyers who might need your help.",
        "Have your business card visible but not pushy. Your helpfulness is what makes buyers want to call you.",
        "Ask buyers what they liked AND didn't like — that feedback is gold for positioning the listing.",
        "Keep your phone away during the open house unless you're actively helping a buyer. Your full attention matters.",
        "If buyers linger, it's a buying signal. Engage them in conversation about what they love most.",
        "Know the home's utility costs, HOA details, and recent improvements before the open house.",
        "Have a buyer consultation brochure available for visitors who aren't tied to an agent yet.",
        "Identify the home's top 3 selling points and naturally mention them in conversation during the open house.",
        "Sunday afternoons are typically the best time for public open houses — maximize attendance.",
        "Follow up open house contacts with a personal note that references something specific from your conversation.",
        "Virtual open houses can expand your reach dramatically — broadcast live on Instagram or Facebook.",
        "Keep a sign-in sheet simple — first name, phone, email, and whether they're working with an agent.",
        "Dress professionally — you represent the property AND your personal brand at every open house.",
        "Have neighborhood comps printed and ready — buyers appreciate transparency about market value.",
        "Offer to send a video walkthrough to buyers who had to leave early — keep the connection alive.",
        "The best open house follow-up starts before the open house ends — take notes on each visitor.",
        "Themed open houses (wine and cheese for luxury, coffee and pastries for family homes) create memorable experiences.",
        "Place directional signs at every key turn within 1 mile of the property — visibility drives traffic.",
        "Have a pre-qualification partner (your lender) available by phone during open houses for interested buyers.",
        "The more questions a buyer asks during an open house, the more interested they are — answer every one enthusiastically.",
        "Track your open house ROI — total visitors, contacts collected, appointments set, and deals closed from open houses.",
        "Open houses work best as part of a comprehensive marketing strategy — not as your only marketing tactic.",
    ]),
    ("Mindset & Motivation", [
        "Real estate success is built on consistency, not inspiration. Show up every day — even when motivation is low.",
        "The agents who make it aren't the most talented — they're the most persistent.",
        "Every 'no' in real estate is just a redirect to the right 'yes.' Keep dialing.",
        "Your mindset is your most valuable asset in this business. Protect it fiercely.",
        "Success in real estate is 20% skill and 80% follow-through. Most agents know what to do — few actually do it.",
        "The moment you stop prospecting is the moment your pipeline starts drying up. Never stop the activity.",
        "Rejection is part of this business. The faster you make peace with it, the faster you grow.",
        "Your competition isn't other agents — it's the version of you that makes excuses.",
        "Time-blocking isn't just a productivity tool — it's a declaration that your goals matter.",
        "The agents who thrive in tough markets are the ones who stayed consistent when others pulled back.",
        "Every client you work with deserves your absolute best — not your average, and not your worst day.",
        "Success leaves clues — study the top agents in your market and model what they do.",
        "Your database is your business. Treat it like the asset it is.",
        "There's no 'perfect time' to build your business. Start now, improve as you go.",
        "Commission anxiety is a mindset issue. When you truly believe in your value, pricing conversations become easy.",
        "Discipline is choosing your future over your present comfort — every single day.",
        "The biggest difference between a $100K agent and a $500K agent is often just activity level and follow-up.",
        "Real estate rewards the brave — agents who make offers, start conversations, and take action win.",
        "A bad month is data, not a death sentence. Analyze, adjust, and attack next month.",
        "Never celebrate a deal closing — celebrate the next deal in your pipeline. Never stop moving forward.",
        "Your clients don't just want a transaction — they want to feel safe and cared for. Be that agent.",
        "Gratitude in this business is powerful — clients who feel appreciated become raving fans.",
        "The most successful agents are also the most humble — they know there's always more to learn.",
        "Energy is contagious. Show up to every appointment as if this is the most important meeting of your career.",
        "Your business will grow in proportion to your personal growth. Invest in both.",
        "The best time to make a business plan was last year. The second best time is today.",
        "Fear of failure is the enemy of most agents' success. Feel the fear and make the call anyway.",
        "Real estate is a relationship business disguised as a transaction business. Never forget that.",
        "The agents who build lasting careers treat every client as a long-term relationship, not a one-time sale.",
        "Burn the boats — go all in on your business and give yourself no option but to succeed.",
        "Your morning routine sets the tone for your production. Protect your first 90 minutes.",
        "The highest-paid real estate agents are the best at talking to people — not the best at the paperwork.",
        "Build your business for the long game. Reputation takes years to build and seconds to destroy.",
        "Track your numbers ruthlessly. What gets measured gets managed.",
        "Success isn't a secret — it's the result of doing the right activities, consistently, for long enough.",
        "You don't rise to the level of your goals — you fall to the level of your systems. Build better systems.",
    ]),
]

all_captions = []
for cat_name, captions in categories:
    for caption in captions:
        all_captions.append([cat_name, caption, "#realestate", "Post"])

# Pad to exactly 365
while len(all_captions) < 365:
    all_captions.append(["Real Estate Tips", "Success in real estate comes from serving clients with integrity, expertise, and consistency every single day.", "#realestate", "Post"])
all_captions = all_captions[:365]

for i, row in enumerate(all_captions):
    row.insert(0, str(i+1))

write_csv(p11+"365_Social_Media_Captions.csv",
    ["Day","Category","Caption","Hashtag","Type"],
    all_captions)

# Bonus DOCX files
doc(p11+"Real_Estate_Scripts_Vault.docx",
    "Real Estate Scripts Vault",
    "Real Estate Agent OS | 50+ Proven Scripts for Every Situation",
    [
        ("FSBO (For Sale By Owner) Scripts", [
            "Initial FSBO Contact Call:",
            '"Hi, I\'m calling about your home for sale. I noticed it\'s listed on Zillow — is it still available? [...] Great! I\'m a local real estate agent and I was wondering if you\'d be open to working with a buyer\'s agent if I brought a qualified buyer? [...] Would you be willing to meet for 15 minutes so I can share some information about how I help FSBOs get more money for their home?"',
            "FSBO Objection — 'I don\'t want to pay a commission':",
            '"I completely understand — that\'s why most people try to sell on their own. But here\'s what I\'ve found: homes listed with an agent typically sell for 6-10% more than FSBOs, even after commission. So most sellers end up with more money in their pocket, not less. Would you like to see the numbers for your neighborhood?"',
        ]),
        ("Expired Listing Scripts", [
            "Initial Expired Contact:",
            '"Hi [Name], my name is [Agent] with [Brokerage]. I noticed your home was on the market and the listing expired — I was sorry to see it didn\'t sell. I\'ve had a lot of success with homes in your area that didn\'t sell with another agent, and I\'d love to stop by for 20 minutes to share what I would do differently. Would [Tuesday] or [Wednesday] work better for you?"',
            "Expired Objection — 'I\'m taking it off the market for now':",
            '"That makes complete sense. Sometimes a break from the market is the right move. Would it be okay if I stayed in touch and sent you a monthly market update? That way, when you\'re ready to give it another try, you\'ll have all the current data."',
        ]),
        ("Buyer Consultation Scripts", [
            "Opening a Buyer Consultation:",
            '"Thank you for coming in today. My goal for this meeting is simple: I want to understand exactly what you\'re looking for, share how my process works, and answer any questions you have. By the end, you\'ll know exactly how I can help you find and purchase the right home — often with less stress and better terms than going it alone. Does that sound good?"',
            "Asking for the Buyer Agency Agreement:",
            '"Before we start our search, I want to be fully committed to representing YOUR best interests — not the seller\'s. To do that, I ask that we sign a buyer representation agreement. This ensures I can give you 100% of my attention, negotiate hard for you, and put your interests first in every situation. Here\'s how it works..."',
        ]),
        ("Listing Appointment Scripts", [
            "Opening a Listing Presentation:",
            '"[Name], before I dive into what I do and how I\'d market your home, I\'d love to hear from you first. What\'s most important to you in this process? Is it the timeline, the price, making it as easy as possible, or something else? [...] Perfect. Everything I\'m about to share with you is designed with [their priority] in mind."',
            "Handling the Price Objection:",
            '"I understand wanting to price higher — every seller does, and it\'s completely natural. Here\'s what the data tells us: homes priced above market value spend more days on the market, go through price reductions, and often end up selling for less than if we\'d priced right from the start. I want to get you the most money possible — and the way to do that is to price it to generate multiple offers in the first 2 weeks. Let me show you why."',
        ]),
        ("Objection Handling Scripts", [
            "'We want to think about it' (seller after listing presentation):",
            '"Of course — this is a big decision and I want you to feel completely confident. What specifically would you like to think through? Is it the price? The marketing plan? Timing? If I can answer any questions right now, I want to make sure you have everything you need."',
            "'We\'re going to try it on our own first':",
            '"I completely respect that — and I\'d love to stay in touch. Would it be okay if I followed up with you in 30 days? In the meantime, I\'m going to send you my FSBO toolkit — tips that help sellers navigate the process. Even if you don\'t use me, I want you to be successful."',
            "'I want to interview 3 agents':",
            '"That\'s a smart approach and I encourage it. One thing I\'d suggest is asking each agent to show you their last 10 listings — days on market, list-to-sale price ratio, and marketing samples. Let the results speak for themselves. I\'m confident in what those numbers will show for my business."',
        ]),
        ("Referral Scripts", [
            "Asking for a Referral from Past Client:",
            '"[Name], working with you was truly one of my favorite transactions this year. As I\'m building my business, I rely almost entirely on referrals from wonderful clients like you. If anyone in your life — a friend, family member, coworker — ever mentions they\'re thinking about buying or selling, I would be so honored if you\'d pass my name along."',
            "Thank You After Receiving a Referral:",
            '"[Name], thank you so much for referring [Referral Name] to me. Referrals are the greatest compliment I can receive, and I promise to take exceptional care of them. I\'ll keep you posted on how things go — and when this transaction closes, I\'d love to take you to dinner as a thank you."',
        ]),
    ])

doc(p11+"Real_Estate_Marketing_Playbook.docx",
    "Real Estate Marketing Playbook",
    "Real Estate Agent OS | Personal Branding & Digital Marketing Strategy",
    [
        ("Your Personal Brand Foundation", [
            ("•", "Define your niche: first-time buyers, luxury, relocation, investors, or specific neighborhoods"),
            ("•", "Craft your Unique Value Proposition (UVP): What do you do better than anyone else in your market?"),
            ("•", "Professional headshot: Updated every 2 years, consistent across all platforms"),
            ("•", "Brand colors and logo: Consistent visual identity across all marketing materials"),
            ("•", "Professional bio: 150-word bio, 300-word bio, and 50-word social bio versions"),
        ]),
        ("Social Media Strategy", [
            ("•", "Instagram: Best for visual content — listings, behind-the-scenes, market updates, client celebrations"),
            ("•", "Facebook: Best for community engagement, local groups, event promotion, and paid advertising"),
            ("•", "LinkedIn: Best for professional networking, referral partners, and corporate relocation clients"),
            ("•", "YouTube: Best for long-form content — market updates, neighborhood tours, buyer/seller guides"),
            ("•", "TikTok: Best for reaching younger buyers with entertaining, educational short-form video"),
            ("•", "Posting frequency: Minimum 3x/week; ideal is daily for maximum algorithm reach"),
        ]),
        ("Content Pillars (5-3-2 Rule)", [
            "For every 10 pieces of content you post:",
            ("•", "5 pieces: Educational value (market tips, buyer/seller advice, community info)"),
            ("•", "3 pieces: Social proof (testimonials, success stories, client celebrations)"),
            ("•", "2 pieces: Personal brand (your story, your why, behind the scenes of your business)"),
        ]),
        ("Listing Marketing Checklist", [
            ("•", "Professional photography (including drone if above $400K)"),
            ("•", "Virtual tour or 3D Matterport walkthrough"),
            ("•", "Property highlight video for social media (60-90 seconds)"),
            ("•", "Professional listing description (250-400 words, SEO-optimized)"),
            ("•", "Just Listed postcard to 200-300 surrounding neighbors"),
            ("•", "Email blast to buyer database"),
            ("•", "Social media posts across all platforms"),
            ("•", "Paid advertising on Facebook/Instagram (minimum $150 per listing)"),
            ("•", "Open house promotion (Zillow, Nextdoor, social media, directional signs)"),
            ("•", "Broker open invitation to top buyer agents in the market"),
        ]),
        ("Email Marketing System", [
            ("•", "Monthly newsletter: Market update + local community news + featured listings"),
            ("•", "New listing alerts: Email buyer database within 24 hours of new listing"),
            ("•", "Market report: Quarterly email with neighborhood data and statistics"),
            ("•", "Holiday and milestone emails: Build personal connection with your database"),
            ("•", "Target open rate: 25%+ (industry average is 20%)"),
            ("•", "CRM tools: Mailchimp, Constant Contact, or your CRM's built-in email"),
        ]),
        ("Paid Advertising Strategy", [
            ("•", "Facebook/Instagram Ads: Best for listing promotion and buyer lead generation"),
            ("•", "Google Ads: Target buyers actively searching '[City] homes for sale'"),
            ("•", "Zillow Premier Agent: Pay-per-lead for buyers searching your ZIP codes"),
            ("•", "Realtor.com Advertising: Similar to Zillow but different audience"),
            ("•", "Monthly ad budget recommendation: 10% of target monthly GCI"),
            ("•", "Track cost per lead and cost per closing for every ad channel"),
        ]),
        ("Video Marketing", [
            ("•", "Neighborhood tour videos (2-4 minutes): Walk through the neighborhood, show local hotspots"),
            ("•", "Market update videos (1-2 minutes): Monthly, shot on your phone is fine"),
            ("•", "Listing walkthrough videos (1-2 minutes): Professional feel, highlight best features"),
            ("•", "Client testimonial videos (30-60 seconds): Phone recordings are authentic and relatable"),
            ("•", "Educational videos: Buyer and seller tip series (your own 'YouTube channel' content)"),
        ]),
    ])

doc(p11+"Top_Producer_Success_System.docx",
    "Top Producer Success System",
    "Real Estate Agent OS | Habits, Routines, and Systems of $500K+ Agents",
    [
        ("The Top Producer Mindset", [
            "Top producers in real estate share a common set of beliefs and habits that drive their results. This system distills those habits into a practical daily, weekly, and monthly framework you can implement immediately.",
            ("•", "They treat real estate as a business, not a job"),
            ("•", "They invest in themselves, their systems, and their team"),
            ("•", "They prospect relentlessly — even when they have a full pipeline"),
            ("•", "They follow up consistently — the majority of deals come after the 5th contact"),
            ("•", "They know their numbers cold: conversion rates, cost per lead, GCI per transaction"),
        ]),
        ("Daily Non-Negotiables (The Power Hour)", [
            "Block 1 hour every morning — before email, before social media — for these activities:",
            ("•", "15 minutes: Review yesterday's results and set today's 3 priorities"),
            ("•", "30 minutes: Prospecting calls (SOI follow-up, new leads, expired/FSBOs)"),
            ("•", "15 minutes: Personal development (book, podcast, or industry article)"),
        ]),
        ("Weekly Success Rituals", [
            ("•", "Monday: Weekly planning — set appointments, review pipeline, contact Tier 1 SOI"),
            ("•", "Tuesday/Wednesday: Peak prospecting days — maximum calls and new conversations"),
            ("•", "Thursday: Appointments and follow-ups — convert leads to signed clients"),
            ("•", "Friday: Administrative wrap-up, review week's numbers, plan next week"),
            ("•", "Saturday: Open houses, buyer showings, community involvement"),
        ]),
        ("Monthly Business Review", [
            "Review these metrics on the first Monday of every month:",
            ("•", "Total GCI vs. goal"),
            ("•", "Number of active buyers and sellers"),
            ("•", "Pipeline value and projected closings"),
            ("•", "Lead source breakdown (where are deals coming from?)"),
            ("•", "Marketing ROI by channel"),
            ("•", "SOI database size and contact rate"),
            ("•", "Referrals given vs. received"),
        ]),
        ("Systems That Scale Your Business", [
            ("•", "CRM: Your business lives in your CRM. Use it daily, log everything, automate follow-ups"),
            ("•", "Transaction Management: Dotloop, DocuSign, or your brokerage's system — use it religiously"),
            ("•", "Email Marketing: Automate monthly market updates and holiday touchpoints"),
            ("•", "Social Media Scheduling: Batch-create content and schedule 2 weeks ahead"),
            ("•", "Virtual Assistant: Hire a VA for 10-15 hours/week once you hit 20+ transactions/year"),
            ("•", "Team Building: Add a buyer's agent when your business exceeds your capacity"),
        ]),
        ("Income Goals by Production Level", [
            ("•", "Level 1 — $100K GCI: 12-15 transactions, strong SOI system, 1 open house/week"),
            ("•", "Level 2 — $250K GCI: 25-35 transactions, consistent lead gen, 2 marketing channels"),
            ("•", "Level 3 — $500K GCI: 50+ transactions, leverage (team/VA), multiple lead channels"),
            ("•", "Level 4 — $1M+ GCI: Team model, listing-focused, strong personal brand + referral machine"),
        ]),
    ])

print("✓ 11_BONUSES complete")

# ─── PDFs ─────────────────────────────────────────────────────────────────────
NAV_RGB = colors.HexColor("#0F3460")
ACC_RGB = colors.HexColor("#E94560")
GLD_RGB = colors.HexColor("#F5A623")

def make_pdf(filepath, title, subtitle, sections):
    doc_pdf = SimpleDocTemplate(filepath, pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('Title', parent=styles['Normal'],
        fontSize=22, textColor=NAV_RGB, spaceAfter=4, fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('Sub', parent=styles['Normal'],
        fontSize=11, textColor=colors.HexColor("#7F8C8D"), spaceAfter=12)
    h_style = ParagraphStyle('H', parent=styles['Normal'],
        fontSize=13, textColor=NAV_RGB, spaceBefore=12, spaceAfter=4, fontName='Helvetica-Bold')
    body_style = ParagraphStyle('Body', parent=styles['Normal'],
        fontSize=10, spaceAfter=4, leading=15)
    bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'],
        fontSize=10, leftIndent=16, spaceAfter=3, leading=14, bulletIndent=6)
    story = []
    story.append(Paragraph(title, title_style))
    story.append(HRFlowable(width="100%", thickness=3, color=ACC_RGB, spaceAfter=6))
    story.append(Paragraph(subtitle, subtitle_style))
    for section in sections:
        if isinstance(section, str):
            story.append(Paragraph(section, body_style)); continue
        heading, items = section
        story.append(Paragraph(heading, h_style))
        story.append(HRFlowable(width="100%", thickness=1, color=GLD_RGB, spaceAfter=4))
        for item in items:
            if isinstance(item, tuple) and item[0] == '•':
                story.append(Paragraph(f"• {item[1]}", bullet_style))
            else:
                story.append(Paragraph(str(item), body_style))
    doc_pdf.build(story)
    print(f"  ✓ {filepath.replace(BASE,'')}")

make_pdf(BASE+"07_COMPLIANCE_LEGAL/Real_Estate_Compliance_Guide.pdf",
    "Real Estate Compliance & Legal Guide",
    "Real Estate Agent OS | Fair Housing, Agency, Disclosure & Ethics",
    [
        ("Fair Housing Act Overview", [
            "The Fair Housing Act prohibits discrimination in the sale, rental, and financing of housing based on race, color, national origin, religion, sex, familial status, and disability. Many states add additional protected classes.",
            ("•", "Never steer clients toward or away from neighborhoods based on demographic composition"),
            ("•", "Use consistent selection criteria when presenting properties to all clients"),
            ("•", "Avoid any language in listings that indicates a preference for a particular class"),
            ("•", "Reasonable accommodations must be provided for clients with disabilities"),
        ]),
        ("Agency Relationships", [
            ("•", "Seller's Agent (Listing Agent): Fiduciary duty to the seller — confidentiality, disclosure, loyalty, obedience, reasonable care"),
            ("•", "Buyer's Agent: Fiduciary duty to the buyer — same duties applied to buyer's interests"),
            ("•", "Dual Agency: Representing both buyer and seller in the same transaction — legal in most states with written consent, but creates conflict of interest"),
            ("•", "Transaction Broker: Non-fiduciary, facilitates the transaction without representing either party's interests"),
            ("•", "Always disclose your agency relationship in writing at first substantive contact"),
        ]),
        ("Mandatory Disclosures", [
            ("•", "Seller disclosure: Known material defects — structural, environmental, legal, or physical issues"),
            ("•", "Lead paint disclosure: Required for homes built before 1978"),
            ("•", "Natural hazard disclosures: Flood zones, fire zones, earthquake zones (state-specific)"),
            ("•", "HOA documents: CC&Rs, bylaws, financials, meeting minutes"),
            ("•", "Death and stigma disclosures: Varies by state — research your state's requirements"),
        ]),
        ("Record Keeping Requirements", [
            ("•", "Federal law requires retention of transaction records for a minimum of 3 years"),
            ("•", "Most state licensing boards require 3-5 years of transaction file retention"),
            ("•", "Required records: Contract, listing agreement, disclosures, correspondence, amendments, closing docs"),
            ("•", "Electronic storage is acceptable — ensure files are backed up and accessible"),
            ("•", "Your brokerage may have additional record retention requirements — know your brokerage policy"),
        ]),
        ("Code of Ethics Highlights", [
            ("•", "Article 1: Protect and promote the interests of your client"),
            ("•", "Article 3: Cooperate with other brokers except when cooperation is not in the client's best interest"),
            ("•", "Article 11: Only provide services within your area of competence"),
            ("•", "Article 12: Be honest and truthful in all real estate communications"),
            ("•", "Article 15: Do not make false or misleading statements about other real estate professionals"),
        ]),
    ])

make_pdf(BASE+"10_NOTION_WORKSPACE/Real_Estate_Agent_OS_User_Guide.pdf",
    "Real Estate Agent Operating System",
    "Complete User Guide | Professional Edition | Value: €149 | Your Price: €39",
    [
        ("Welcome to Your Real Estate Agent OS", [
            "Congratulations on investing in the most comprehensive real estate agent operating system on the market. This toolkit contains everything you need to run a professional, organized, and profitable real estate business — built from the ground up with real-world agent best practices.",
            ("•", "60+ professional templates, tools, and systems"),
            ("•", "Complete lead generation, client management, and transaction workflows"),
            ("•", "Canva-ready presentation templates"),
            ("•", "Google Sheets-based CRM and tracking tools"),
            ("•", "Notion-importable database system"),
            ("•", "365 days of social media content"),
        ]),
        ("What's Included", [
            ("•", "00_START_HERE: Quick start guide and product overview"),
            ("•", "01_LEAD_GENERATION: Complete lead gen system with CRM tracker"),
            ("•", "02_BUYER_SERVICES: Buyer consultation, showing, and offer systems"),
            ("•", "03_SELLER_SERVICES: Listing presentation, pricing, and marketing tools"),
            ("•", "04_NEGOTIATION: Offer, counter-offer, and inspection scripts"),
            ("•", "05_TRANSACTION_MANAGEMENT: Contract-to-close checklists and SOPs"),
            ("•", "06_CLIENT_COMMUNICATION: Email, text, and update templates"),
            ("•", "07_COMPLIANCE_LEGAL: Fair housing, disclosure, and record-keeping guides"),
            ("•", "08_POST_CLOSING_RETENTION: Follow-up and referral systems"),
            ("•", "09_BUSINESS_OPERATIONS: Business plan, schedule, and commission tracker"),
            ("•", "10_NOTION_WORKSPACE: Complete Notion CRM setup with 7 databases"),
            ("•", "11_BONUSES: 365 captions, scripts vault, and marketing playbook"),
            ("•", "12_CANVA_IMPORTABLE_TEMPLATES: 4 professional presentation templates"),
        ]),
        ("Quick Start — First 30 Minutes", [
            "Step 1 (5 min): Read the README_FIRST.txt in the 00_START_HERE folder",
            "Step 2 (10 min): Import the Notion CSVs from 10_NOTION_WORKSPACE using the Setup Guide",
            "Step 3 (10 min): Open your Canva account and upload the PPTX files from 12_CANVA_IMPORTABLE_TEMPLATES",
            "Step 4 (5 min): Open Lead_Generation_CRM.xlsx and enter your first 10 contacts",
        ]),
        ("How to Use Canva Templates", [
            ("•", "Open Canva (free account works) and click 'Upload'"),
            ("•", "Select any of the 4 PPTX files from 12_CANVA_IMPORTABLE_TEMPLATES"),
            ("•", "Canva converts the file to an editable Canva design automatically"),
            ("•", "Customize colors, fonts, photos, and text to match your brand"),
            ("•", "Download as PDF or PowerPoint for professional presentations"),
        ]),
        ("License & Usage", [
            ("•", "Personal use: Unlimited use in your own real estate business"),
            ("•", "Client use: Use with unlimited clients and transactions"),
            ("•", "Customization: Fully customize all templates with your branding"),
            ("•", "Restrictions: Do not resell, share, or redistribute as your own product"),
            ("•", "Questions: Contact us through the Etsy shop for support"),
        ]),
    ])

make_pdf(BASE+"09_BUSINESS_OPERATIONS/Real_Estate_Business_Growth_Workbook.pdf",
    "Real Estate Business Growth Workbook",
    "Real Estate Agent OS | 90-Day Production Accelerator",
    [
        ("90-Day Business Sprint Overview", [
            "This workbook is your accountability partner for the next 90 days. Top-producing agents plan their business quarterly and track their results weekly. Complete this workbook at the beginning of each quarter and review it every Monday morning.",
        ]),
        ("Month 1 — Foundation", [
            ("•", "Week 1: Audit your database — clean it, categorize it, update contact info"),
            ("•", "Week 2: Contact every Tier 1 SOI contact personally — calls and handwritten notes"),
            ("•", "Week 3: Set up or clean up your CRM — all contacts entered, all follow-ups scheduled"),
            ("•", "Week 4: Host your first client appreciation event or community open house"),
            "Month 1 Goal: _____ new conversations | _____ appointments set | _____ GCI target",
        ]),
        ("Month 2 — Momentum", [
            ("•", "Week 5: Launch or improve your social media presence — post consistently"),
            ("•", "Week 6: Contact 5 referral partners — schedule coffees or lunches"),
            ("•", "Week 7: Host 2 open houses and follow up with every attendee within 24 hours"),
            ("•", "Week 8: Review results, double down on what's working, eliminate what's not"),
            "Month 2 Goal: _____ new conversations | _____ appointments set | _____ GCI target",
        ]),
        ("Month 3 — Acceleration", [
            ("•", "Week 9: Implement a paid advertising channel — Facebook ads or Zillow Premier Agent"),
            ("•", "Week 10: Ask 10 past clients for reviews on Google and Zillow"),
            ("•", "Week 11: Write a market update blog or video — post to all channels"),
            ("•", "Week 12: Quarterly review — did you hit your goals? What's the plan for next quarter?"),
            "Month 3 Goal: _____ new conversations | _____ appointments set | _____ GCI target",
        ]),
        ("90-Day Reflection Questions", [
            "Answer these honestly at the end of every 90-day sprint:",
            ("•", "What was my #1 lead source this quarter?"),
            ("•", "What activity produced the most appointments?"),
            ("•", "What am I avoiding that I know I should be doing?"),
            ("•", "Who are my top 5 referral partners and how am I nurturing those relationships?"),
            ("•", "If I kept doing exactly what I did this quarter for a full year, would I hit my annual goal?"),
        ]),
    ])

print("✓ PDFs complete")

# ─── 12_CANVA_IMPORTABLE_TEMPLATES ────────────────────────────────────────────
p12 = "12_CANVA_IMPORTABLE_TEMPLATES/"
PNAV=PRGB(15,52,96); PACC=PRGB(233,69,96); PGLD=PRGB(245,166,35); PWHT=PRGB(255,255,255)
PLGR=PRGB(248,249,250); PDGR=PRGB(44,62,80)

def new_prs():
    prs=Presentation(); prs.slide_width=Inches(13.33); prs.slide_height=Inches(7.5); return prs

def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])

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

# PPTX 1: Listing Presentation
prs = new_prs()
# Slide 1 — Cover
sl = blank(prs)
rect(sl,0,0,13.33,7.5,PNAV)
rect(sl,0,0,13.33,0.08,PACC)
rect(sl,0,7.42,13.33,0.08,PGLD)
txt(sl,"LISTING PRESENTATION",0.5,1.0,12,1.2,sz=40,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"Professional Real Estate Services",0.5,2.4,12,0.8,sz=20,bold=False,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"[Your Name] | [Your Brokerage] | [Phone Number]",0.5,3.3,12,0.6,sz=16,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"[Client Name] | [Property Address] | [Date]",0.5,4.0,12,0.6,sz=14,color=PRGB(189,195,199),align=PP_ALIGN.CENTER)
# Slide 2 — About Me
sl = blank(prs)
rect(sl,0,0,4.5,7.5,PNAV)
rect(sl,4.5,0,8.83,7.5,PLGR)
txt(sl,"ABOUT ME",0.3,0.4,3.9,0.8,sz=28,bold=True,color=PGLD)
txt(sl,"[Your Photo Here]",0.5,1.4,3.5,3.0,sz=16,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"[Your Name]",0.3,4.6,3.9,0.6,sz=18,bold=True,color=PWHT)
txt(sl,"[Your Title] | [Brokerage]",0.3,5.2,3.9,0.5,sz=13,color=PGLD)
txt(sl,"MY CREDENTIALS",5.0,0.5,7.8,0.6,sz=22,bold=True,color=PNAV)
creds = [
    ("● Years of Experience:", "[X] years serving this market"),
    ("● Homes Sold:", "[X] homes sold last year"),
    ("● Average Sale-to-List Ratio:", "[X]% — above market average"),
    ("● Average Days on Market:", "[X] days — below market average"),
    ("● Specialties:", "[Your Niche/Specialty]"),
    ("● Designations:", "[ABR, CRS, GRI, etc.]"),
    ("● Why I'm Different:", "Personalized service, aggressive marketing, proven results"),
]
for i,(label,val) in enumerate(creds):
    txt(sl,label,5.0,1.3+i*0.72,3.5,0.6,sz=11,bold=True,color=PDGR)
    txt(sl,val,8.2,1.3+i*0.72,4.5,0.6,sz=11,color=PDGR)
# Slide 3 — Marketing Plan
sl = blank(prs)
rect(sl,0,0,13.33,1.3,PNAV)
txt(sl,"MY MARKETING PLAN FOR YOUR HOME",0.5,0.25,12.3,0.8,sz=28,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
rect(sl,0,1.3,13.33,0.05,PGLD)
mktg = [
    ("📸","Professional Photography","HDR photos + drone + virtual tour"),
    ("🎥","Video Marketing","Property video + social media reels"),
    ("🌐","Online Exposure","Zillow, Realtor.com, MLS, 200+ sites"),
    ("📱","Social Media Ads","Facebook, Instagram, YouTube targeted ads"),
    ("📬","Direct Mail","Just Listed postcards to 300 neighbors"),
    ("🤝","Agent Network","Personal outreach to 200+ local buyer agents"),
]
for i,(emoji,title,desc) in enumerate(mktg):
    col = i % 3
    row = i // 3
    x = 0.4 + col * 4.3
    y = 1.6 + row * 2.6
    rect(sl,x,y,3.9,2.3,PWHT)
    txt(sl,emoji,x+1.6,y+0.15,0.8,0.7,sz=28,color=PNAV)
    txt(sl,title,x+0.1,y+0.85,3.7,0.6,sz=14,bold=True,color=PNAV,align=PP_ALIGN.CENTER)
    txt(sl,desc,x+0.1,y+1.45,3.7,0.7,sz=11,color=PDGR,align=PP_ALIGN.CENTER)
# Slide 4 — Pricing Strategy
sl = blank(prs)
rect(sl,0,0,13.33,7.5,PNAV)
rect(sl,0.3,0.3,12.73,6.9,PWHT)
txt(sl,"PRICING STRATEGY",0.5,0.6,12,0.8,sz=30,bold=True,color=PNAV,align=PP_ALIGN.CENTER)
rect(sl,0.3,1.4,12.73,0.05,PACC)
pricing = [
    ("PRICED TOO HIGH", "❌","• Extended days on market\n• Low showing activity\n• Eventual price reductions\n• Buyer perception: 'Something's wrong'\n• Final sale price often BELOW market","E94560"),
    ("PRICED RIGHT", "✅","• Strong showing activity\n• Buyer urgency and competition\n• Multiple offers possible\n• Fastest path to highest price\n• YOU WIN","27AE60"),
    ("PRICED TOO LOW", "⚠️","• Immediate activity and offers\n• Risk of leaving money on table\n• May signal urgency/desperation\n• Difficult to recover in negotiation","F5A623"),
]
for i,(title,icon,points,color_hex) in enumerate(pricing):
    x = 0.6 + i*4.2
    rect(sl,x,1.6,3.8,5.5,PRGB(*bytes.fromhex(color_hex)))
    txt(sl,icon,x+1.5,1.7,0.8,0.8,sz=24,color=PWHT)
    txt(sl,title,x+0.1,2.55,3.6,0.7,sz=14,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
    txt(sl,points,x+0.2,3.3,3.4,3.4,sz=10,color=PWHT)
# Slide 5 — Next Steps
sl = blank(prs)
rect(sl,0,0,13.33,7.5,PNAV)
rect(sl,0,0,13.33,0.1,PGLD)
txt(sl,"LET'S GET STARTED",0.5,0.5,12,1.0,sz=36,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"Here's what happens next:",0.5,1.7,12,0.6,sz=20,color=PGLD,align=PP_ALIGN.CENTER)
steps = [
    ("1","SIGN LISTING AGREEMENT","We agree on terms, commission, and timeline"),
    ("2","HOME PREP","Professional staging consultation + photography"),
    ("3","GO LIVE","List on MLS + launch full marketing campaign"),
    ("4","SHOW & NEGOTIATE","Manage showings + negotiate best offers"),
    ("5","CLOSE","Guide you through inspections, appraisal, closing"),
]
for i,(num,title,desc) in enumerate(steps):
    x = 0.4 + i*2.55
    rect(sl,x,2.5,2.3,0.7,PACC)
    txt(sl,num,x,2.5,2.3,0.7,sz=24,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
    txt(sl,title,x,3.3,2.3,0.7,sz=11,bold=True,color=PGLD,align=PP_ALIGN.CENTER)
    txt(sl,desc,x,4.1,2.3,1.5,sz=10,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"[Your Name] | [Phone] | [Email] | [Website]",0.5,6.3,12,0.6,sz=14,color=PRGB(189,195,199),align=PP_ALIGN.CENTER)

prs.save(BASE+p12+"Listing_Presentation_Template.pptx")
print(f"  ✓ {p12}Listing_Presentation_Template.pptx")

# PPTX 2: Buyer Consultation Presentation
prs2 = new_prs()
# Slide 1 — Cover
sl = blank(prs2)
rect(sl,0,0,6.5,7.5,PACC)
rect(sl,6.5,0,6.83,7.5,PNAV)
txt(sl,"BUYER\nCONSULTATION",0.4,1.2,5.7,3.0,sz=38,bold=True,color=PWHT)
txt(sl,"Your Complete Guide to\nBuying a Home With Confidence",0.4,4.0,5.7,1.5,sz=16,color=PWHT)
txt(sl,"[Your Name] | [Brokerage]",0.4,5.8,5.7,0.6,sz=14,color=PRGB(255,200,200))
txt(sl,"THE BUYING PROCESS",7.0,0.8,5.8,0.8,sz=22,bold=True,color=PGLD)
process_steps = ["1. Pre-Approval","2. Home Search","3. Make an Offer","4. Inspections","5. Appraisal","6. Final Walk-Through","7. CLOSING DAY!"]
for i,step in enumerate(process_steps):
    rect(sl,7.0,1.7+i*0.75,5.8,0.65,PRGB(30,70,120) if i<6 else PGLD)
    txt(sl,step,7.1,1.7+i*0.75,5.6,0.65,sz=13,bold=(i==6),color=PNAV if i==6 else PWHT)
# Slide 2 — Why Work With Me
sl = blank(prs2)
rect(sl,0,0,13.33,1.2,PNAV)
txt(sl,"WHY WORK WITH A BUYER'S AGENT?",0.5,0.2,12,0.8,sz=28,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
benefits = [
    ("🏠","NO COST TO YOU","In most transactions, the seller pays buyer agent commission"),
    ("🔍","MARKET EXPERTISE","Access to off-market deals and deep neighborhood knowledge"),
    ("💪","NEGOTIATION POWER","I've negotiated [X] transactions — I know how to win for you"),
    ("📋","TRANSACTION MANAGEMENT","I handle all the paperwork, deadlines, and coordination"),
    ("🤝","MY NETWORK","Access to trusted lenders, inspectors, and contractors"),
    ("🛡️","YOUR ADVOCATE","I put your interests first in every conversation and decision"),
]
for i,(icon,title,desc) in enumerate(benefits):
    col = i%3; row = i//3
    x = 0.4 + col*4.3; y = 1.5 + row*2.7
    rect(sl,x,y,4.0,2.5,PLGR)
    rect(sl,x,y,4.0,0.6,PNAV)
    txt(sl,f"{icon} {title}",x+0.1,y+0.1,3.8,0.5,sz=12,bold=True,color=PWHT)
    txt(sl,desc,x+0.1,y+0.7,3.8,1.6,sz=11,color=PDGR)
# Slide 3 — The Home Search Process
sl = blank(prs2)
rect(sl,0,0,13.33,7.5,PLGR)
rect(sl,0,0,13.33,1.3,PACC)
txt(sl,"THE HOME SEARCH PROCESS",0.5,0.25,12,0.8,sz=28,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
search_steps = [
    ("STEP 1\nPRE-APPROVAL","Get pre-approved first. Know your budget and show sellers you're serious."),
    ("STEP 2\nDEFINE CRITERIA","Location, size, price range, must-haves vs. nice-to-haves"),
    ("STEP 3\nSEARCH & TOUR","I'll send listings daily + schedule showings quickly"),
    ("STEP 4\nMAKE AN OFFER","I'll write a competitive offer to win the home you love"),
    ("STEP 5\nDUE DILIGENCE","Inspections, appraisal, title search — I coordinate all of it"),
    ("STEP 6\nCLOSING","Sign papers, get keys, celebrate your new home!"),
]
for i,(title,desc) in enumerate(search_steps):
    col = i%3; row = i//3
    x = 0.4 + col*4.3; y = 1.6 + row*2.7
    rect(sl,x,y,4.0,2.5,PWHT)
    rect(sl,x,y,4.0,1.0,PNAV)
    txt(sl,title,x+0.1,y+0.1,3.8,0.9,sz=12,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
    txt(sl,desc,x+0.1,y+1.1,3.8,1.3,sz=10,color=PDGR)
# Slide 4 — Buyer FAQ
sl = blank(prs2)
rect(sl,0,0,13.33,1.3,PNAV)
txt(sl,"FREQUENTLY ASKED BUYER QUESTIONS",0.5,0.25,12,0.8,sz=26,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
faqs = [
    ("How much do I need for a down payment?","As little as 3% conventional, 3.5% FHA, or 0% VA. We'll find the right loan for you."),
    ("How long does buying a home take?","30-60 days from accepted offer to closing. Home search varies by market."),
    ("Do I need a home inspection?","Absolutely yes. I'll recommend trusted inspectors who give thorough, fast reports."),
    ("What if the home doesn't appraise?","We negotiate with the seller, request a price reduction, or walk away — I protect you."),
    ("Can I back out if something goes wrong?","Yes — your contingencies (inspection, financing, appraisal) are exit protections."),
    ("What are closing costs?","Typically 2-5% of purchase price, covering loan fees, title, taxes, and escrow."),
]
for i,(q,a) in enumerate(faqs):
    col = i%2; row = i//2
    x = 0.4 + col*6.5; y = 1.5 + row*1.85
    rect(sl,x,y,6.2,1.75,PLGR)
    rect(sl,x,y,0.08,1.75,PACC)
    txt(sl,q,x+0.25,y+0.1,5.8,0.6,sz=11,bold=True,color=PNAV)
    txt(sl,a,x+0.25,y+0.7,5.8,0.9,sz=10,color=PDGR)

prs2.save(BASE+p12+"Buyer_Consultation_Presentation.pptx")
print(f"  ✓ {p12}Buyer_Consultation_Presentation.pptx")

# PPTX 3: Monthly Market Update
prs3 = new_prs()
sl = blank(prs3)
rect(sl,0,0,13.33,7.5,PNAV)
rect(sl,0,3.5,13.33,0.08,PACC)
txt(sl,"MONTHLY MARKET UPDATE",0.5,0.6,12,1.2,sz=38,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"[Month Year] | [City/Neighborhood]",0.5,2.0,12,0.8,sz=22,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"Prepared by [Your Name] | [Brokerage] | [Phone]",0.5,6.5,12,0.6,sz=14,color=PRGB(189,195,199),align=PP_ALIGN.CENTER)

sl = blank(prs3)
rect(sl,0,0,13.33,1.3,PNAV)
txt(sl,"KEY MARKET STATISTICS — [MONTH YEAR]",0.5,0.25,12,0.8,sz=26,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
stats = [
    ("$[XXX,XXX]","Median Sale Price","▲ [X]% vs last month"),
    ("[XX]","Average Days on Market","▼ [X] days vs last month"),
    ("[XXX]","Homes Sold","▲ [X]% vs same month last year"),
    ("[X.X]","Months of Inventory","[Seller's / Buyer's] Market"),
    ("[XX]%","List-to-Sale Ratio","Sellers receiving [above/below] asking"),
    ("$[XXX]","Price Per Square Foot","▲ [X]% year over year"),
]
for i,(val,label,change) in enumerate(stats):
    col = i%3; row = i//2
    x = 0.35 + col*4.3; y = 1.5 + row*2.7
    rect(sl,x,y,4.0,2.5,PLGR)
    rect(sl,x,y,4.0,0.08,PACC)
    txt(sl,val,x+0.1,y+0.2,3.8,1.0,sz=30,bold=True,color=PNAV,align=PP_ALIGN.CENTER)
    txt(sl,label,x+0.1,y+1.25,3.8,0.6,sz=13,bold=True,color=PDGR,align=PP_ALIGN.CENTER)
    txt(sl,change,x+0.1,y+1.9,3.8,0.5,sz=10,color=PRGB(100,100,100),align=PP_ALIGN.CENTER)

sl = blank(prs3)
rect(sl,0,0,13.33,1.3,PACC)
txt(sl,"WHAT THIS MEANS FOR YOU",0.5,0.25,12,0.8,sz=26,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
rect(sl,0.3,1.5,6.1,5.7,PLGR)
rect(sl,6.9,1.5,6.1,5.7,PLGR)
txt(sl,"🏡 IF YOU'RE SELLING",0.5,1.6,5.7,0.7,sz=18,bold=True,color=PNAV)
seller_points = ["• Market conditions favor [buyers/sellers]","• Your home could sell for $[XXX,XXX]","• Expected days on market: [XX] days","• Now is [a great/a challenging] time to list","• [Specific market insight for sellers]","• [Call to action: Schedule a free valuation]"]
for i,pt in enumerate(seller_points):
    txt(sl,pt,0.5,2.4+i*0.5,5.7,0.45,sz=11,color=PDGR)
txt(sl,"🔍 IF YOU'RE BUYING",7.1,1.6,5.7,0.7,sz=18,bold=True,color=PNAV)
buyer_points = ["• Competition level: [High/Moderate/Low]","• Average offers per home: [X]","• Homes going [above/below] asking price","• Expect to offer [X]% [above/below] list","• [Specific market insight for buyers]","• [Call to action: Get pre-approved today]"]
for i,pt in enumerate(buyer_points):
    txt(sl,pt,7.1,2.4+i*0.5,5.7,0.45,sz=11,color=PDGR)

prs3.save(BASE+p12+"Monthly_Market_Update_Template.pptx")
print(f"  ✓ {p12}Monthly_Market_Update_Template.pptx")

# PPTX 4: Social Media Content Pack
prs4 = new_prs()
# Post 1 — Market Stat
sl = blank(prs4)
rect(sl,0,0,13.33,7.5,PNAV)
rect(sl,1.5,0.8,10.33,5.9,PACC)
rect(sl,1.7,1.0,9.93,5.5,PNAV)
txt(sl,"DID YOU KNOW?",2.0,1.4,9.33,0.9,sz=26,bold=True,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"Homes in [City] are selling\nfor [X]% above asking price",2.0,2.4,9.33,1.8,sz=28,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"on average right now.",2.0,4.2,9.33,0.8,sz=22,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"📊 [Month Year] Market Update",2.0,5.1,9.33,0.6,sz=16,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"[Your Name] | [Phone] | [Brokerage]",2.0,5.8,9.33,0.5,sz=12,color=PRGB(189,195,199),align=PP_ALIGN.CENTER)
# Post 2 — Buyer Tip
sl = blank(prs4)
rect(sl,0,0,13.33,7.5,PLGR)
rect(sl,0,0,13.33,2.0,PNAV)
rect(sl,0,2.0,0.15,5.5,PACC)
txt(sl,"BUYER TIP OF THE WEEK",0.5,0.3,12,0.8,sz=28,bold=True,color=PWHT)
txt(sl,"#[Week Number]",0.5,1.2,12,0.6,sz=18,color=PGLD)
txt(sl,"GET PRE-APPROVED\nBEFORE YOU START SEARCHING",0.5,2.3,12,1.6,sz=28,bold=True,color=PNAV)
tip_text = "A pre-approval letter shows sellers you're a serious buyer and tells you exactly how much home you can afford. In today's competitive market, sellers won't even consider offers without one."
txt(sl,tip_text,0.5,4.1,9.5,2.0,sz=14,color=PDGR)
txt(sl,"Want to get pre-approved?\nI'll connect you with a trusted lender today!",10.0,4.1,3.1,2.0,sz=12,bold=True,color=PACC)
txt(sl,"[Your Name] | [Phone] | [Instagram Handle]",0.5,6.5,12,0.6,sz=12,color=PRGB(150,150,150))
# Post 3 — Seller Tip
sl = blank(prs4)
rect(sl,0,0,13.33,7.5,PACC)
rect(sl,0.4,0.4,12.53,6.7,PNAV)
txt(sl,"SELLER TIP",0.7,0.7,11.93,0.8,sz=22,bold=True,color=PGLD)
txt(sl,"THE #1 THING YOU CAN DO TO\nSELL YOUR HOME FASTER",0.7,1.6,11.93,1.6,sz=30,bold=True,color=PWHT,align=PP_ALIGN.CENTER)
rect(sl,1.5,3.4,10.33,0.08,PGLD)
txt(sl,"DECLUTTER AND DEEP CLEAN",0.7,3.6,11.93,0.8,sz=24,bold=True,color=PGLD,align=PP_ALIGN.CENTER)
txt(sl,"Buyers need to visualize themselves in your home.\nWhen your personal items dominate every room,\nthey can't picture their life there.",0.7,4.5,11.93,1.6,sz=14,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"Thinking about selling? Let's talk! 📞",0.7,6.1,11.93,0.6,sz=14,color=PGLD,align=PP_ALIGN.CENTER)
# Post 4 — Just Listed
sl = blank(prs4)
rect(sl,0,0,13.33,7.5,PLGR)
rect(sl,0,0,13.33,0.8,PNAV)
rect(sl,0,6.8,13.33,0.7,PNAV)
txt(sl,"⭐ JUST LISTED ⭐",0.5,0.1,12,0.6,sz=20,bold=True,color=PGLD,align=PP_ALIGN.CENTER)
rect(sl,0.4,0.9,5.5,5.7,PNAV)
txt(sl,"[PROPERTY\nPHOTO\nHERE]",0.4,0.9,5.5,5.7,sz=18,color=PWHT,align=PP_ALIGN.CENTER)
txt(sl,"[Street Address]",6.2,1.0,6.8,0.8,sz=24,bold=True,color=PNAV)
txt(sl,"[City, State ZIP]",6.2,1.85,6.8,0.6,sz=16,color=PDGR)
rect(sl,6.2,2.6,6.8,0.06,PACC)
details = [("🛏","[X] Bedrooms"),("🛁","[X] Bathrooms"),("📐","[X,XXX] Sq Ft"),("🚗","[X]-Car Garage"),("🌳","[Lot Size] Lot")]
for i,(icon,detail) in enumerate(details):
    txt(sl,f"{icon}  {detail}",6.2,2.8+i*0.55,6.8,0.5,sz=13,color=PDGR)
txt(sl,"$[XXX,XXX]",6.2,5.6,6.8,0.8,sz=30,bold=True,color=PACC)
txt(sl,"DM me for a private showing | [Your Phone] | [Your Name]",0.5,6.85,12,0.5,sz=13,color=PGLD,align=PP_ALIGN.CENTER)

prs4.save(BASE+p12+"Social_Media_Content_Pack.pptx")
print(f"  ✓ {p12}Social_Media_Content_Pack.pptx")
print("✓ 12_CANVA_IMPORTABLE_TEMPLATES complete")

# ─── UPDATE START HERE ─────────────────────────────────────────────────────────
with open(BASE+"00_START_HERE/README_FIRST.txt","w",encoding="utf-8") as f:
    f.write("""WELCOME TO YOUR REAL ESTATE AGENT OPERATING SYSTEM
====================================================
Original Value: €149 | Your Launch Price: €39
Thank you for your purchase! This toolkit contains everything you need to run
a professional, organized, and profitable real estate business.

WHAT'S INSIDE:
--------------
00_START_HERE          → You are here — read this first!
01_LEAD_GENERATION     → Cold outreach, SOI, open house, referral scripts + CRM
02_BUYER_SERVICES      → Buyer consultation, showing checklists, offer SOPs
03_SELLER_SERVICES     → Listing presentation, pricing strategy, marketing
04_NEGOTIATION         → Offer, counter-offer, inspection negotiation scripts
05_TRANSACTION_MGMT    → Contract to close SOPs and checklists
06_CLIENT_COMMUNICATION → Email, text, weekly update templates
07_COMPLIANCE_LEGAL    → Fair housing, disclosure, record-keeping guides
08_POST_CLOSING        → Follow-up system, SOI nurture, reviews
09_BUSINESS_OPERATIONS → Business plan, schedule, commission tracker
10_NOTION_WORKSPACE    → 7 Notion-importable databases + setup guide
11_BONUSES             → 365 social captions, scripts vault, marketing playbook
12_CANVA_TEMPLATES     → 4 Canva-importable PPTX presentations

QUICK START (30 MINUTES):
--------------------------
1. Import CSVs from 10_NOTION_WORKSPACE into Notion (see Setup Guide)
2. Upload PPTX files from 12_CANVA_TEMPLATES to Canva
3. Open Lead_Generation_CRM.xlsx and enter your first 10 contacts
4. Print or save the Quick_Start_Checklist.docx for your first week

Real Estate Agent Operating System | Professional Edition
""")
print("  ✓ 00_START_HERE/README_FIRST.txt updated")

# ─── ASSET MANIFEST + ZIP ─────────────────────────────────────────────────────
import os, json, zipfile

all_files = []
for root, dirs, files in os.walk(BASE):
    for fn in sorted(files):
        fp = os.path.join(root, fn)
        rel = os.path.relpath(fp, BASE)
        parts = rel.split(os.sep)
        folder = parts[0] if len(parts) > 1 else "ROOT"
        ext = fn.rsplit('.', 1)[-1].upper() if '.' in fn else 'UNKNOWN'
        size = os.path.getsize(fp)
        all_files.append({"file": rel, "folder": folder, "type": ext, "size_bytes": size})

# CSV manifest
with open(BASE+"00_START_HERE/Asset_Manifest.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["File", "Folder", "Type", "Size (bytes)"])
    for item in all_files:
        w.writerow([item["file"], item["folder"], item["type"], item["size_bytes"]])

# JSON manifest
manifest = {
    "product": "Ultimate Real Estate Agent Operating System",
    "version": "1.0",
    "price_original": "€149",
    "price_launch": "€39",
    "total_files": len(all_files),
    "files": all_files
}
with open(BASE+"00_START_HERE/Asset_Manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print(f"  ✓ Asset Manifest: {len(all_files)} files indexed")

# ZIP
zip_path = "/home/user/oqul-phase55-production/real-estate-agent-os/BUYER_DOWNLOAD_RealEstateAgentOS.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(BASE):
        for fn in sorted(files):
            fp = os.path.join(root, fn)
            arcname = os.path.relpath(fp, os.path.dirname(BASE))
            zf.write(fp, arcname)

zip_size = os.path.getsize(zip_path) / (1024*1024)
print(f"\n✅ ZIP created: BUYER_DOWNLOAD_RealEstateAgentOS.zip ({zip_size:.1f} MB)")
print(f"   Total files: {len(all_files)}")
print("\nPART 4 DONE — Real Estate Agent OS COMPLETE")
