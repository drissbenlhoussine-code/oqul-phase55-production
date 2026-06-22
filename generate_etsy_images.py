#!/usr/bin/env python3
"""
Generate 7 professional Etsy listing images for each of 15 products.
Style: Premium digital product listings inspired by reference images.
Output: 2000x2000 px PNG files, organized per product.
"""

import os, math
from PIL import Image, ImageDraw, ImageFont

W, H = 2000, 2000
OUT = "/home/user/oqul-phase55-production/etsy-images/"
os.makedirs(OUT, exist_ok=True)

# ─── FONTS ───────────────────────────────────────────────────────────────────
SERIF_B = "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf"
SERIF_R = "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"
SANS_B  = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_R  = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
DEJA_B  = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
DEJA_R  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(path, sz):
    try: return ImageFont.truetype(path, sz)
    except: return ImageFont.load_default()

# ─── COLOR UTILS ─────────────────────────────────────────────────────────────
def h2r(h):
    h=h.lstrip('#')
    return tuple(int(h[i:i+2],16) for i in (0,2,4))

def lighten(h, t=0.88):
    r,g,b=h2r(h)
    return (int(r+(255-r)*t), int(g+(255-g)*t), int(b+(255-b)*t))

def darken(h, t=0.6):
    r,g,b=h2r(h)
    return (int(r*t), int(g*t), int(b*t))

def mix(c1,c2,t=0.5):
    r1,g1,b1=(h2r(c1) if isinstance(c1,str) else c1)
    r2,g2,b2=(h2r(c2) if isinstance(c2,str) else c2)
    return (int(r1+(r2-r1)*t),int(g1+(g2-g1)*t),int(b1+(b2-b1)*t))

# ─── DRAW UTILS ──────────────────────────────────────────────────────────────
def rr(draw, xy, radius, fill, outline=None, ow=0):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=ow)

def circ(draw, cx, cy, r, fill, outline=None, ow=2):
    draw.ellipse([cx-r,cy-r,cx+r,cy+r], fill=fill, outline=outline, width=ow)

def txt(draw, text, x, y, font, fill, anchor="lt"):
    draw.text((x,y), text, font=font, fill=fill, anchor=anchor)

def txt_c(draw, text, cx, y, font, fill):
    bb = draw.textbbox((0,0), text, font=font)
    tw = bb[2]-bb[0]
    draw.text((cx-tw//2, y), text, font=font, fill=fill)

def txt_block(draw, text, x, y, max_w, font, fill, lh=None):
    if lh is None:
        bb=draw.textbbox((0,0),"Ag",font=font); lh=int((bb[3]-bb[1])*1.45)
    words=text.split(); line=""; cy=y
    for w in words:
        test=(line+" "+w).strip()
        bb=draw.textbbox((0,0),test,font=font)
        if (bb[2]-bb[0])>max_w and line:
            draw.text((x,cy),line,font=font,fill=fill); cy+=lh; line=w
        else: line=test
    if line: draw.text((x,cy),line,font=font,fill=fill); cy+=lh
    return cy

def txt_block_c(draw, text, cx, y, max_w, font, fill, lh=None):
    if lh is None:
        bb=draw.textbbox((0,0),"Ag",font=font); lh=int((bb[3]-bb[1])*1.45)
    words=text.split(); line=""; cy=y; lines=[]
    for w in words:
        test=(line+" "+w).strip()
        bb=draw.textbbox((0,0),test,font=font)
        if (bb[2]-bb[0])>max_w and line:
            lines.append(line); line=w
        else: line=test
    if line: lines.append(line)
    for l in lines:
        bb=draw.textbbox((0,0),l,font=font); tw=bb[2]-bb[0]
        draw.text((cx-tw//2,cy),l,font=font,fill=fill); cy+=lh
    return cy

def divider(draw, cx, y, w, col, sym="◆"):
    half=(w-60)//2
    draw.line([(cx-half//2-40,y+12),(cx-60,y+12)],fill=col,width=3)
    txt_c(draw,sym,cx,y,F(SERIF_R,28),col)
    draw.line([(cx+60,y+12),(cx+half//2+40,y+12)],fill=col,width=3)

def num_badge(draw, x, y, n, bg, fg="#FFFFFF", sz=44):
    circ(draw, x, y, sz//2+6, bg)
    txt_c(draw, str(n).zfill(2), x, y-sz//2+6, F(SANS_B,sz), fg)

def check_item(draw, x, y, text, font, col_check, col_text, icon="✓"):
    circ(draw, x+18, y+18, 18, col_check)
    txt(draw, icon, x+6, y+4, F(SANS_B,20), "#FFFFFF")
    txt_block(draw, text, x+48, y+2, 820, font, col_text)

def cross_item(draw, x, y, text, font, col_cross="#CC3333", col_text="#444444"):
    circ(draw, x+18, y+18, 18, col_cross)
    txt(draw, "✗", x+7, y+4, F(SANS_B,20), "#FFFFFF")
    txt_block(draw, text, x+48, y+2, 740, font, col_text)

def gradient_bg(size, c1, c2, vertical=True):
    img=Image.new("RGB",size)
    draw=ImageDraw.Draw(img)
    w,h=size
    r1,g1,b1=h2r(c1) if isinstance(c1,str) else c1
    r2,g2,b2=h2r(c2) if isinstance(c2,str) else c2
    n=h if vertical else w
    for i in range(n):
        t=i/n
        rc=int(r1+(r2-r1)*t); gc=int(g1+(g2-g1)*t); bc=int(b1+(b2-b1)*t)
        if vertical: draw.line([(0,i),(w,i)],fill=(rc,gc,bc))
        else: draw.line([(i,0),(i,h)],fill=(rc,gc,bc))
    return img

# ─── PRODUCT DATA ────────────────────────────────────────────────────────────
PRODUCTS = [
{
 "id":"01","name":"MORTGAGE BROKER","line2":"OPERATING SYSTEM",
 "audience":"Mortgage Brokers & Loan Officers",
 "tagline":"The complete system to attract clients, manage loans & scale your brokerage",
 "files":"60+","price":"$49",
 "pri":"#0A2342","acc":"#C9A84C","bg":"#F5F2EA","txt":"#0A2342",
 "contents":[
  ("Business Plan Template","Revenue projections & 90-day launch plan"),
  ("Loan Pipeline Tracker","Excel CRM: application to closing stage"),
  ("Pre-Approval Checklist","20-step document collection system"),
  ("Client Onboarding Workflow","Welcome packet & intake process"),
  ("Referral Partner System","Track realtors, CPAs & attorneys"),
  ("Rate Quote Email Templates","10 professional email scripts"),
  ("Realtor Outreach Scripts","Cold + warm outreach email sequences"),
  ("Compliance Checklist","RESPA, TILA, & disclosure requirements"),
  ("Notion CRM Databases","3 importable CSV databases"),
  ("Agency Pitch Deck","PowerPoint presentation for partners"),
 ],
 "pillars":[
  ("ATTRACT","Get qualified mortgage leads with proven outreach scripts and referral systems"),
  ("CONSULT","Convert inquiries into pre-approvals with a professional consultation framework"),
  ("PROCESS","Move loans from application to closing with organized checklists and workflows"),
  ("RETAIN","Build a referral engine with past clients, realtors, and financial partners"),
  ("SCALE","Grow your brokerage with systems that work without you in every deal"),
 ],
 "before":["Losing leads in your email inbox","No system for tracking loan stages","Inconsistent client follow-up","No referral partner strategy","Working 60+ hours with no leverage"],
 "after":["Organized pipeline from lead to closed loan","Stage-by-stage loan tracker with alerts","Professional templates for every touchpoint","Referral system that generates leads on autopilot","A scalable business that runs on systems"],
 "benefits":["Save 10+ hours per week on admin","Never lose a mortgage lead again","Professional client experience from day 1","Built-in referral and follow-up system","Works for solo brokers or full teams","60+ files ready to use immediately","No experience needed -- just customize"],
},
{
 "id":"02","name":"RECRUITING AGENCY","line2":"OPERATING SYSTEM",
 "audience":"Independent Recruiters & Agency Founders",
 "tagline":"The complete system to source candidates, win clients & close placements faster",
 "files":"70+","price":"$49",
 "pri":"#2D1B69","acc":"#FF6B35","bg":"#F7F5FF","txt":"#1A1040",
 "contents":[
  ("Business Plan Template","Fee structure, revenue model & launch roadmap"),
  ("Candidate Pipeline Tracker","8-stage sourcing to placement CRM"),
  ("Job Order Management","Client intake & position specification system"),
  ("Client Service Agreement","Professional placement contract template"),
  ("Placement Fee Invoice","Contingency & retained fee invoice templates"),
  ("LinkedIn Sourcing Playbook","Boolean search strings & InMail scripts"),
  ("Candidate Scorecard","Assessment framework for every placement"),
  ("Interview Templates","Scheduling, prep & feedback system"),
  ("Cold Outreach Scripts","Email sequences for clients & candidates"),
  ("Agency Pitch Deck","PowerPoint presentation for new clients"),
 ],
 "pillars":[
  ("SOURCE","Find top candidates with LinkedIn Boolean search strings and sourcing playbook"),
  ("ENGAGE","Build candidate pipelines with proven outreach scripts and InMail templates"),
  ("MATCH","Score and present candidates with professional scorecards and profiles"),
  ("PLACE","Close placements faster with contracts, invoices and delivery systems"),
  ("GROW","Scale your desk revenue with client outreach and referral partner systems"),
 ],
 "before":["Tracking candidates in spreadsheets & emails","No system for managing job orders","No professional contract or invoice templates","Struggling to win corporate clients","Revenue unpredictable month to month"],
 "after":["8-stage pipeline from sourcing to placed","Organized job order and client system","Professional contracts and invoices ready to send","Pitch deck to win corporate accounts","Consistent placements with a proven process"],
 "benefits":["70+ files covering every part of your desk","Source 3x faster with Boolean search strings","Professional candidate scorecards and profiles","Win more clients with the included pitch deck","Invoice and contract templates ready to send","Works for all niches: tech, finance, healthcare","No agency experience required"],
},
{
 "id":"03","name":"BOOKKEEPING BUSINESS","line2":"OPERATING SYSTEM",
 "audience":"Freelance Bookkeepers & Accounting Professionals",
 "tagline":"The complete system to launch, fill your client roster & run a profitable bookkeeping firm",
 "files":"65+","price":"$49",
 "pri":"#1A4D2E","acc":"#D4AC0D","bg":"#F5FAF5","txt":"#1A4D2E",
 "contents":[
  ("Business Plan Template","Niche selection, revenue goals & roadmap"),
  ("Service Menu (15+ services)","Pricing guidance for every service tier"),
  ("Client Pricing Calculator","Excel model for packages and hourly rates"),
  ("Bookkeeping Service Agreement","Full legal contract template"),
  ("Client Onboarding Checklist","Welcome packet & intake workflow"),
  ("Monthly Bookkeeping SOP","Step-by-step month-end workflow"),
  ("Chart of Accounts Template","24 standard accounts pre-built"),
  ("Client Outreach Email Templates","LinkedIn & email cold outreach scripts"),
  ("Notion CRM Databases","Client tracker, task log & income tracker"),
  ("52-Week Content Calendar","Social media plan for the full year"),
 ],
 "pillars":[
  ("POSITION","Choose the right niche and service package to stand out in a crowded market"),
  ("ATTRACT","Get bookkeeping clients with proven outreach scripts and referral systems"),
  ("ONBOARD","Deliver a professional first impression with a structured onboarding workflow"),
  ("DELIVER","Run clean books for every client with SOPs and monthly checklists"),
  ("GROW","Raise your rates and expand your roster with data-driven business systems"),
 ],
 "before":["Charging too little for your bookkeeping skills","No contract or onboarding system","Working informally without clear processes","Struggling to find consistent clients","Doing client work without a structured SOP"],
 "after":["Professional pricing with clear service packages","Service agreement and onboarding workflow ready","Step-by-step monthly bookkeeping SOP","Outreach scripts to land new clients","A business that runs with consistent systems"],
 "benefits":["65+ files for every part of your business","Service agreement protects you legally","Month-end SOP so nothing gets missed","52-week social media calendar included","Notion CRM for all your clients","Works for QBO, Xero, and Wave users","From setup to 5-client roster in 30 days"],
},
{
 "id":"04","name":"REAL ESTATE AGENT","line2":"OPERATING SYSTEM",
 "audience":"Real Estate Agents & Realtors",
 "tagline":"The complete system to generate leads, win listings & close more transactions",
 "files":"70+","price":"$49",
 "pri":"#2C3E50","acc":"#E67E22","bg":"#FDF9F5","txt":"#2C3E50",
 "contents":[
  ("Business Plan & GCI Calculator","Annual goal setting with income projections"),
  ("Lead Tracking CRM","Excel: source, stage, follow-up date"),
  ("Buyer Consultation Framework","Discovery script & needs analysis"),
  ("Listing Presentation Deck","PowerPoint template to win listings"),
  ("Open House Sign-In & Follow-Up","System for capturing & nurturing leads"),
  ("Buyer & Seller Guides","Professional client handout templates"),
  ("30-Step Closing Checklist","Transaction coordinator workflow"),
  ("10 Email & Text Scripts","Follow-up sequences for every scenario"),
  ("52-Week Social Media Calendar","Content plan for the full year"),
  ("Referral & Past Client System","Re-engagement templates and tracker"),
 ],
 "pillars":[
  ("GENERATE","Build a consistent lead pipeline with sphere, farming, and digital strategies"),
  ("CONSULT","Win more listings with a professional buyer and seller consultation framework"),
  ("MARKET","Showcase listings with a presentation deck that closes more appointments"),
  ("TRANSACT","Close cleanly with a 30-step transaction coordinator checklist"),
  ("RETAIN","Turn past clients into referral machines with a re-engagement system"),
 ],
 "before":["Following up inconsistently with leads","Losing listing appointments to competitors","No system for managing transactions","Spending hours creating marketing content","Relying only on luck for referrals"],
 "after":["Organized lead CRM with source and stage tracking","Listing presentation that consistently wins business","30-step closing checklist from contract to keys","52 weeks of social media content planned out","Referral system that generates consistent introductions"],
 "benefits":["70+ files to run your entire real estate business","GCI calculator to hit your income goals","Professional listing presentation included","Works for buyer agents, listing agents & teams","Email scripts for every follow-up scenario","Past client re-engagement system to generate referrals","Customizable for any market or brokerage"],
},
{
 "id":"05","name":"INSURANCE AGENCY","line2":"OPERATING SYSTEM",
 "audience":"Independent Insurance Agents & Agency Owners",
 "tagline":"The complete system to grow your agency, retain clients & maximize policy revenue",
 "files":"60+","price":"$49",
 "pri":"#1B2A4A","acc":"#2980B9","bg":"#F0F4FA","txt":"#1B2A4A",
 "contents":[
  ("Agency Business Plan","Commission projections & 90-day launch"),
  ("Client CRM Tracker","Policy type, renewal date, premium status"),
  ("Policy Renewal Tracker","Never miss a renewal opportunity again"),
  ("Sales Pipeline System","Prospect to bound policy tracker"),
  ("Referral Partner System","Attorneys, CPAs & realtor partners"),
  ("Client Needs Analysis","Questionnaire to uncover coverage gaps"),
  ("Quote Follow-Up Sequences","5 email templates for every lead"),
  ("Claims Support Workflow","Guide clients through claims professionally"),
  ("Annual Policy Review Checklist","Strengthen retention and upsell"),
  ("Agency Pitch Deck","Presentation for referral partner meetings"),
 ],
 "pillars":[
  ("PROSPECT","Build a consistent pipeline with referral partner systems and cold outreach"),
  ("QUOTE","Convert more prospects with a professional needs analysis and quote workflow"),
  ("BIND","Win more policies with follow-up sequences that close at every stage"),
  ("RETAIN","Keep clients long-term with annual reviews, claims support and check-ins"),
  ("GROW","Cross-sell and upsell existing clients to maximize revenue per household"),
 ],
 "before":["Missing policy renewals and losing clients","No system for tracking leads and quotes","No referral partner strategy","Inconsistent follow-up with prospects","Revenue tied to new business only"],
 "after":["Policy renewal tracker so no client slips away","Pipeline from first contact to bound policy","Referral system with attorneys, CPAs & realtors","5-email follow-up sequence that converts","Cross-sell checklist to grow revenue per client"],
 "benefits":["60+ files for every part of your agency","Never miss a renewal with our tracker","Referral system generates warm introductions","Quote follow-up sequences close more policies","Works for P&C, life, health, or multi-line","Client CRM tracks every policy in one place","Professional pitch deck for partner meetings"],
},
{
 "id":"06","name":"AI SOCIAL MEDIA","line2":"AGENCY OS",
 "audience":"SMMA Founders & Social Media Freelancers",
 "tagline":"The complete system to launch your SMMA, sign clients & deliver results with AI",
 "files":"80+","price":"$39",
 "pri":"#1A0533","acc":"#FF006E","bg":"#FAF0FF","txt":"#1A0533",
 "contents":[
  ("Business Plan & Pricing Tiers","Revenue model & 90-day launch roadmap"),
  ("Complete Service Menu","30+ SMMA services with pricing guidance"),
  ("Client Proposal Template","Word doc to pitch & win retainer clients"),
  ("Social Media Contract","Full service agreement template"),
  ("Client Onboarding System","Welcome packet & intake questionnaire"),
  ("90-Day Content Calendar","Multi-platform content planning template"),
  ("AI Content Creation Workflow","ChatGPT + Canva system for every client"),
  ("Monthly Reporting Template","Client-ready performance report"),
  ("Cold Outreach Email Sequences","5-email flow to book discovery calls"),
  ("Notion Agency Databases","Client CRM, content tracker & revenue log"),
 ],
 "pillars":[
  ("LAUNCH","Set up your SMMA with a professional business plan, pricing, and positioning"),
  ("ATTRACT","Book discovery calls with cold email sequences and DM outreach scripts"),
  ("CLOSE","Win retainer clients with a pitch deck, proposal template, and contract"),
  ("DELIVER","Use AI workflows to create content 10x faster for every client"),
  ("RETAIN","Send monthly reports that prove ROI and keep clients for 12+ months"),
 ],
 "before":["No clear offer or pricing for your services","Struggling to book discovery calls","Losing pitches to more professional agencies","Spending 10+ hours per client on content","Clients leaving because they don't see results"],
 "after":["Clear service packages with proven pricing","Outreach system that books calls consistently","Pitch deck and proposal that wins retainers","AI workflow that cuts content creation to 2 hours","Monthly report that proves value and retains clients"],
 "benefits":["80+ files to run your entire SMMA","AI content workflow saves 8+ hours per client","Cold outreach sequences included","Professional contracts protect you legally","Notion CRM for all client management","Works for Instagram, TikTok, LinkedIn & more","Launch your SMMA in 30 days or less"],
},
{
 "id":"07","name":"BOOKKEEPER PRACTICE","line2":"LAUNCH SYSTEM",
 "audience":"New Bookkeepers Launching Their First Practice",
 "tagline":"Everything you need to land your first bookkeeping clients and build a real business",
 "files":"50+","price":"$39",
 "pri":"#006D6D","acc":"#FF6B6B","bg":"#F0FAFA","txt":"#003D3D",
 "contents":[
  ("12-Month Business Plan","Milestones, revenue goals & niche selection"),
  ("Service Package Calculator","Tiered pricing for 4 service packages"),
  ("Bookkeeping Service Agreement","Legal contract template (Word)"),
  ("Client Database Tracker","8 clients pre-filled with full data"),
  ("Month-End Closing Checklist","15 task checklist for every client"),
  ("Chart of Accounts Template","24 standard accounts ready to use"),
  ("Tax Planning Guide","Client handout to retain them year-round"),
  ("LinkedIn + Email Outreach Scripts","Cold outreach to land first clients"),
  ("52-Week Content Calendar","CSV, importable to Notion"),
  ("Services Overview Pitch Deck","Professional PowerPoint presentation"),
 ],
 "pillars":[
  ("POSITION","Pick a profitable niche and build a service package that stands out"),
  ("ATTRACT","Get your first bookkeeping clients with outreach scripts and cold email"),
  ("ONBOARD","Deliver a 5-star first impression with a professional onboarding workflow"),
  ("DELIVER","Run clean monthly books with the step-by-step closing checklist"),
  ("RETAIN","Keep clients year-round with tax planning support and proactive reviews"),
 ],
 "before":["No idea what to charge for bookkeeping","Taking on any client without a contract","Starting fresh without a clear process","Too scared to reach out to potential clients","Doing bookkeeping without monthly checklists"],
 "after":["4-tier pricing packages with clear positioning","Professional service agreement for every client","Structured onboarding that impresses from day 1","Outreach scripts to land first 3 clients in 30 days","Month-end checklist so nothing ever gets missed"],
 "benefits":["50+ files to launch your practice","Legal contract protects you from day 1","Pricing calculator ends the guesswork","Outreach scripts land first clients fast","Month-end SOP for consistent delivery","Works with QBO, Xero and Wave","Land your first client in 30 days"],
},
{
 "id":"08","name":"STAFFING AGENCY","line2":"OPERATING SYSTEM",
 "audience":"Independent Recruiters & Staffing Agency Founders",
 "tagline":"The complete system to build a staffing agency, source candidates & close placements",
 "files":"60+","price":"$49",
 "pri":"#0D1B2A","acc":"#C9A84C","bg":"#F5F3EA","txt":"#0D1B2A",
 "contents":[
  ("Agency Business Plan","Fee structure, revenue model & 90-day plan"),
  ("Staffing Fee Calculator","Placement fees by salary level (Excel)"),
  ("Candidate Pipeline (8 stages)","Sourcing to placement CRM tracker"),
  ("Candidate Scorecard","Assessment framework for every role"),
  ("LinkedIn Sourcing Playbook","Boolean search strings for any niche"),
  ("Client Service Agreement","Full staffing contract (Word)"),
  ("Job Order Intake Template","Position specification & client intake"),
  ("Recruiter Scripts Vault","Client & candidate call scripts"),
  ("Compliance Checklist","EEOC, FLSA & background check guide"),
  ("Agency Pitch Deck","PowerPoint for new client presentations"),
 ],
 "pillars":[
  ("SOURCE","Find top candidates with LinkedIn Boolean search strings and sourcing playbook"),
  ("QUALIFY","Score every candidate with professional scorecards and assessment tools"),
  ("PRESENT","Win client confidence with formatted candidate profiles and presentations"),
  ("PLACE","Close placements faster with compliant contracts and structured processes"),
  ("INVOICE","Bill professionally with fee calculators and payment terms templates"),
 ],
 "before":["No system for tracking candidates across roles","No contract or legal protection","Guessing on staffing fees and margins","Losing placements to more organized competitors","Tracking everything in email and spreadsheets"],
 "after":["8-stage pipeline from sourcing to placed and billed","Professional contracts protect every placement","Fee calculator for contingency and retained work","Pitch deck and candidate profiles that win accounts","Organized system for every role and every client"],
 "benefits":["60+ files for every part of your desk","Boolean search strings for sourcing any role","Compliance checklist protects your agency","Candidate scorecard for consistent quality","Professional pitch deck wins corporate clients","Works for direct hire, contract & temp staffing","Launch your staffing agency in 60 days"],
},
{
 "id":"09","name":"AI AUTOMATION AGENCY","line2":"STARTER KIT",
 "audience":"Automation Entrepreneurs & Tech-Savvy Freelancers",
 "tagline":"30 automation blueprints, client system & full business kit to launch your agency",
 "files":"55+","price":"$39",
 "pri":"#0B0C2A","acc":"#7C3AED","bg":"#F3F0FF","txt":"#0B0C2A",
 "contents":[
  ("Agency Business Plan","Positioning, pricing tiers & revenue model"),
  ("30 Automation Blueprints","9 industries: lead gen, email, e-commerce..."),
  ("Financial Model & Pricing","Excel calculator for service packages"),
  ("Lead Pipeline Tracker","Outreach to signed client CRM"),
  ("5-Phase Delivery SOP","Step-by-step client delivery workflow"),
  ("Automation Proposal Template","Word proposal to win new clients"),
  ("Complete Service Menu","30+ automation services with pricing"),
  ("AI Tools Directory","20 essential tools with pricing & use cases"),
  ("Cold Outreach Email Templates","Scripts to book discovery calls"),
  ("Notion Agency Workspace","3 importable CSV databases"),
 ],
 "pillars":[
  ("POSITION","Define your automation niche and service packages for maximum profitability"),
  ("ATTRACT","Book discovery calls with cold outreach scripts tailored to automation buyers"),
  ("CLOSE","Win clients with a professional proposal and 30 ready-to-sell blueprints"),
  ("DELIVER","Execute client projects with the 5-phase delivery SOP and blueprint library"),
  ("SCALE","Build recurring revenue with retainer packages and a growing client roster"),
 ],
 "before":["No idea which automations to sell to businesses","Struggling to explain automation value to clients","No proposal or contract for automation projects","Delivering projects inconsistently with no SOP","Charging one-off fees instead of building retainers"],
 "after":["30 proven blueprints across 9 industries ready to sell","Pitch deck and proposal that explain ROI clearly","Professional contract and delivery workflow","5-phase SOP from kickoff to client handoff","Retainer package framework for recurring income"],
 "benefits":["30 blueprints = 30 ready-to-sell services","No coding required -- just configure the tools","5-phase delivery SOP for consistent results","AI tools directory saves 20+ hours of research","Financial model with pricing built in","Works with Make.com, Zapier & n8n","Launch your automation agency in 60 days"],
},
{
 "id":"10","name":"VIRTUAL ASSISTANT","line2":"BUSINESS OS",
 "audience":"Freelance VAs & Online Business Managers",
 "tagline":"The complete system to launch your VA business, sign clients & scale to $5k months",
 "files":"60+","price":"$34",
 "pri":"#2D3748","acc":"#38A169","bg":"#F5FAF7","txt":"#1A202C",
 "contents":[
  ("Business Plan (3 niches)","Admin VA, Social VA, Executive VA plans"),
  ("Tiered Pricing Calculator","4 service packages with Excel model"),
  ("VA Service Agreement + NDA","Full legal contract template"),
  ("80-Service Menu","Complete menu with descriptions and rates"),
  ("LinkedIn & Facebook Scripts","Cold outreach email + DM templates"),
  ("Discovery Call Framework","Script to close clients on calls"),
  ("SOPs for 20 VA Tasks","Step-by-step for every common task"),
  ("Tech Stack Guide","20 essential tools with tutorials"),
  ("Notion CRM Databases","Client tracker, task log & income log"),
  ("52 Client Email Templates","CSV, covers every communication type"),
 ],
 "pillars":[
  ("POSITION","Choose your VA niche and service packages to stand out and charge premium rates"),
  ("ATTRACT","Land your first VA clients with LinkedIn and Facebook outreach scripts"),
  ("CLOSE","Convert discovery calls into retainer clients with a proven call framework"),
  ("DELIVER","Complete every task professionally with 20 SOPs for the most common VA work"),
  ("SCALE","Raise your rates, hire subcontractors, and grow to an OBM business"),
 ],
 "before":["No idea what services to offer as a VA","Charging hourly instead of package pricing","Taking on clients without a contract","Delivering work without any SOPs or systems","Struggling to find consistent clients"],
 "after":["Clear niche with 4 professional service packages","Package pricing that earns more per client","Legal contract and NDA for every engagement","20 SOPs for consistent professional delivery","Outreach system that generates consistent leads"],
 "benefits":["60+ files to run your entire VA business","80-service menu covers every possible offering","20 SOPs so you never miss a step","52 email templates for every situation","Legal contract protects you from day 1","Works for admin, social, executive, or OBM","Scale from $1k to $5k months in 90 days"],
},
{
 "id":"11","name":"AIRBNB CO-HOST","line2":"MANAGEMENT SYSTEM",
 "audience":"Airbnb Co-Hosts & Short-Term Rental Managers",
 "tagline":"The complete system to sign property owners, manage listings & deliver 5-star stays",
 "files":"50+","price":"$34",
 "pri":"#FF5A5F","acc":"#00A699","bg":"#FFF5F5","txt":"#2D1515",
 "contents":[
  ("Co-Host Pitch Deck","PowerPoint to sign new property owners"),
  ("Portfolio & Booking Tracker","5 properties, Excel CRM"),
  ("Co-Host Agreement Template","Full management contract (Word)"),
  ("Co-Host Fee Structure Guide","Typical commission rates and packages"),
  ("Guest Message Templates","7 templates for every guest situation"),
  ("Turnover Cleaning Checklist","Kitchen, bathrooms, bedrooms & final"),
  ("Revenue Dashboard","Dynamic pricing guide & income tracker"),
  ("Maintenance Request Tracker","Log and follow up on property issues"),
  ("House Rules Template","Professional house rules for all properties"),
  ("Notion Workspace Databases","Property, booking & maintenance CSVs"),
 ],
 "pillars":[
  ("PITCH","Win property owner trust with a professional co-host pitch deck and agreement"),
  ("ONBOARD","Set up every property for success with a structured listing optimization system"),
  ("COMMUNICATE","Deliver 5-star guest experiences with 7 message templates for every scenario"),
  ("OPERATE","Run turnover and maintenance like clockwork with checklists and trackers"),
  ("GROW","Add more properties and raise your co-host fee with a proven track record"),
 ],
 "before":["No professional agreement with property owners","Managing guests with ad-hoc messages","Turnover cleaning with no standard checklist","No system for tracking revenue per property","Struggling to sign new property owners"],
 "after":["Professional co-host agreement for every owner","7 guest message templates for every scenario","Turnover checklist so every stay is 5-star ready","Revenue dashboard per property and overall","Pitch deck to sign 1 new property per month"],
 "benefits":["50+ files to run your co-host business","Guest message templates = 5-star reviews","Turnover checklist eliminates bad check-ins","Revenue tracker per property and overall","Co-host agreement protects you legally","Works for 1 or 20 properties","Sign your first property in 30 days"],
},
{
 "id":"12","name":"NOTION CLIENT PORTAL","line2":"FOR AGENCIES",
 "audience":"Agency Owners, Freelancers & Consultants",
 "tagline":"A professional Notion workspace for client management, project delivery & agency growth",
 "files":"45+","price":"$29",
 "pri":"#191919","acc":"#6366F1","bg":"#F5F5FF","txt":"#191919",
 "contents":[
  ("Client Master Database","Full client CRM importable to Notion"),
  ("Project Tracker","Sprint-based project management CSV"),
  ("Content Calendar Database","Editorial planning and scheduling CSV"),
  ("Invoice & Payments Log","Revenue and billing tracker CSV"),
  ("Analytics Report Log","Campaign metrics database CSV"),
  ("Client Onboarding Workbook","Word document for new client setup"),
  ("Monthly Report Template","Professional report for every client"),
  ("Agency-Client Communication SOP","Response time and protocol guide"),
  ("Agency KPI Dashboard","Excel tracker: revenue, utilization, projects"),
  ("Notion Setup Guide","Step-by-step Markdown setup instructions"),
 ],
 "pillars":[
  ("ORGANIZE","Set up your entire agency in Notion in under 2 hours with the setup guide"),
  ("TRACK","Manage clients, projects, invoices and content in one connected workspace"),
  ("REPORT","Send professional monthly reports that showcase your value to every client"),
  ("COMMUNICATE","Set clear expectations with an agency-client communication SOP"),
  ("SCALE","Add team members, new clients and new services without losing visibility"),
 ],
 "before":["Managing clients across email, Slack & spreadsheets","No central place to track all active projects","Spending hours building monthly client reports","No clear system for new client onboarding","Team members not knowing what to work on next"],
 "after":["One Notion workspace for every client and project","Real-time project status visible in one dashboard","30-minute monthly report with the included template","Structured onboarding for every new client","Team clarity with organized sprint boards and tasks"],
 "benefits":["5 Notion databases importable in minutes","Setup guide gets you live in under 2 hours","Monthly report template saves 2 hours per client","Works for 1 or 50 clients","Covers client, project, invoice, content & analytics","Fully customizable to your agency workflow","One-time purchase, use forever"],
},
{
 "id":"13","name":"UGC CREATOR","line2":"BRAND DEAL KIT",
 "audience":"UGC Creators & Content Creator Entrepreneurs",
 "tagline":"Everything you need to land brand deals, charge premium rates & run a creator business",
 "files":"50+","price":"$24",
 "pri":"#1A1A2E","acc":"#E94560","bg":"#FFF0F3","txt":"#1A1A2E",
 "contents":[
  ("UGC Rate Card & Calculator","Pricing for every content type + deal value calc"),
  ("Media Kit Creation Guide","Build a 2-page kit that wins brand deals"),
  ("Brand Pitch Playbook","10+ email templates + DM scripts"),
  ("UGC Service Agreement","Full contract template (Word)"),
  ("Content Brief Template","Send to every brand before filming"),
  ("50 Scroll-Stop Hooks","Proven UGC hooks that drive views"),
  ("5-Step Production Workflow","Brief to delivery in 5 structured steps"),
  ("Content Performance Dashboard","Excel: hook rate, CTR, ROAS tracker"),
  ("Negotiation Scripts","Word-for-word scripts for every objection"),
  ("Notion Creator Databases","Brand tracker, content library, income log"),
 ],
 "pillars":[
  ("BRAND","Define your UGC niche, USP and portfolio to attract premium brand partnerships"),
  ("PITCH","Land brand deals with email templates and DM scripts that get replies"),
  ("NEGOTIATE","Use word-for-word scripts to get paid what your content is worth"),
  ("CREATE","Produce scroll-stopping UGC with 50 hooks and a 5-step production system"),
  ("TRACK","Prove ROI to brands with performance dashboards that justify re-booking"),
 ],
 "before":["No idea what to charge for UGC content","Brands offering gifting instead of paying","No professional contract for brand deals","Creating content without a structured process","No data to show brands after delivery"],
 "after":["Rate card with pricing for every content type","Scripts to redirect brands from gifting to paying","Service agreement for every paid collaboration","5-step production system from brief to delivery","Performance dashboard that justifies your rates"],
 "benefits":["50+ files to run your creator business","50 proven UGC hooks to stop the scroll","Rate card ends the guessing on pricing","Negotiation scripts handle every objection","Contract protects you on every deal","Analytics dashboard proves your value","Land your first paid brand deal in 30 days"],
},
{
 "id":"14","name":"CREATOR SPONSORSHIP","line2":"TRACKER",
 "audience":"YouTube, Instagram & TikTok Creators",
 "tagline":"Track every brand deal, manage your income & grow your sponsorship revenue",
 "files":"50+","price":"$19",
 "pri":"#0F2940","acc":"#FF6B35","bg":"#FFF8F3","txt":"#0F2940",
 "contents":[
  ("Master Sponsorship Tracker","Excel: 10 deal fields, 10 sample deals"),
  ("Brand Deal Pipeline","8-stage deal management system"),
  ("Income & Tax Tracker","Monthly income + quarterly tax estimates"),
  ("Sponsored Content Calendar","Monthly + annual planning (Excel + CSV)"),
  ("Brand Pitch System","Templates for YouTube, Instagram & TikTok"),
  ("Channel Analytics Dashboard","Subscribers, views, CTR & engagement"),
  ("Video Performance Tracker","Views, conversions, sponsor revenue"),
  ("Sponsorship Agreement Template","Full contract template (Word)"),
  ("Platform Playbooks (x3)","YouTube, Instagram & TikTok guides"),
  ("Sponsorship Rate Guide","Rates by platform and follower tier"),
 ],
 "pillars":[
  ("TRACK","Manage every brand deal in one master spreadsheet from pitch to paid"),
  ("PITCH","Land sponsorships on YouTube, Instagram and TikTok with platform-specific scripts"),
  ("NEGOTIATE","Use the rate guide and negotiation framework to get paid what you're worth"),
  ("DELIVER","Create sponsor-compliant content with integration scripts and disclosure guides"),
  ("ANALYZE","Show brands your performance data to justify re-booking and rate increases"),
 ],
 "before":["Managing brand deals in your email inbox","No idea what to charge per platform","No professional contract for sponsorships","Missing payment deadlines and follow-ups","No data to prove your content performance"],
 "after":["All 10+ deals tracked in one dashboard","Rate guide for YouTube, Instagram and TikTok","Professional sponsorship contract included","Pipeline tracker with follow-up reminders","Analytics dashboard to prove and grow your rates"],
 "benefits":["50+ files for your sponsorship business","Works for YouTube, Instagram & TikTok","Rate guide covers every follower tier","Contract template protects every deal","Income tracker with quarterly tax estimates","Platform playbooks for YouTube, IG & TikTok","Organize all your brand deals in one place"],
},
{
 "id":"15","name":"ETSY AI SEO","line2":"LISTING SYSTEM",
 "audience":"Etsy Sellers in Every Niche",
 "tagline":"Get found in Etsy search with optimized titles, tag vaults & AI prompts for every listing",
 "files":"60+","price":"$19",
 "pri":"#F56400","acc":"#1A1A2E","bg":"#FFF9F5","txt":"#1A1A2E",
 "contents":[
  ("Etsy SEO Masterclass","How Etsy search ranking actually works"),
  ("5-Source Keyword Research Method","Autocomplete, eRank, competitors + more"),
  ("200+ Title Formula Templates","By category: digital, jewelry, decor, gifts"),
  ("3 Description Templates","Digital, physical & custom products"),
  ("13-Tag Framework + 6 Tag Sets","Pre-built tag sets for 6 popular niches"),
  ("6 AI Prompts for ChatGPT & Claude","Title, tags, description, keyword research"),
  ("Shop Optimization Guide","Beyond listings: sections, About, title"),
  ("Analytics Tracker","Views, conversion & revenue by listing"),
  ("300+ Niche Keywords (3 packs)","Digital, gifts & home decor packs"),
  ("30-Point SEO Audit Checklist","Audit every listing for maximum visibility"),
 ],
 "pillars":[
  ("RESEARCH","Find the exact keywords buyers type using the 5-source keyword research system"),
  ("TITLE","Front-load your primary keyword with proven title formulas that rank and convert"),
  ("TAGS","Use all 13 tags strategically with the 13-tag framework and ready-to-use tag sets"),
  ("DESCRIBE","Write descriptions that rank and convert with the 3 professional templates"),
  ("OPTIMIZE","Run the 30-point audit checklist on every listing for maximum search visibility"),
 ],
 "before":["Listings getting no views from Etsy search","Random tags that don't match buyer searches","Titles that describe the product, not the buyer","No system for updating seasonal keywords","Guessing at what keywords actually rank"],
 "after":["Listings optimized for the exact phrases buyers type","13-tag framework fills all tags with strategic phrases","Title formulas that front-load the right keywords","Seasonal keyword update checklist by quarter","AI prompts that write full listings in under 5 minutes"],
 "benefits":["60+ files covering every Etsy SEO factor","6 AI prompts write full listings in minutes","300+ validated keywords across 3 niches","Works for digital, physical & custom products","30-point audit so no listing gets left behind","Tag vault for 6 popular niches ready to copy","Beginner-friendly -- no SEO experience needed"],
},
]  # end PRODUCTS

# ─── SLIDE 1: HERO COVER ─────────────────────────────────────────────────────
def slide1(p):
    pri=p["pri"]; acc=p["acc"]
    bg_col=lighten(pri, 0.94)
    img=Image.new("RGB",(W,H),bg_col)
    draw=ImageDraw.Draw(img)

    # Top accent bar
    draw.rectangle([0,0,W,22], fill=h2r(acc))
    # Bottom accent bar
    draw.rectangle([0,H-22,W,H], fill=h2r(acc))

    # Left thick color stripe
    draw.rectangle([0,22,12,H-22], fill=h2r(pri))

    # "THE COMPLETE" label
    txt_c(draw,"◆  THE COMPLETE  ◆",W//2,70,F(SANS_B,38),h2r(acc))

    # Product name - large serif
    name_y=150
    txt_c(draw,p["name"],W//2,name_y,F(SERIF_B,120),h2r(pri))
    bb=draw.textbbox((0,0),p["name"],font=F(SERIF_B,120))
    name_h=bb[3]-bb[1]
    line2_y=name_y+name_h+10
    txt_c(draw,p["line2"],W//2,line2_y,F(SERIF_B,90),h2r(acc))
    bb2=draw.textbbox((0,0),p["line2"],font=F(SERIF_B,90))
    line2_h=bb2[3]-bb2[1]

    # Divider
    div_y=line2_y+line2_h+30
    divider(draw,W//2,div_y,500,h2r(pri))

    # Tagline
    tag_y=div_y+55
    txt_block_c(draw,p["tagline"],W//2,tag_y,1400,F(SANS_R,44),h2r(pri),lh=60)

    # Contents in 2 columns
    col_y=tag_y+160
    items=p["contents"]
    left_items=items[:5]; right_items=items[5:]
    lx=130; rx=W//2+60
    dot_col=h2r(acc)

    for i,(title,desc) in enumerate(left_items):
        cy=col_y+i*115
        circ(draw,lx+20,cy+24,20,dot_col)
        txt(draw,str(i+1).zfill(2),lx+7,cy+10,F(SANS_B,24),"#FFFFFF")
        txt(draw,title,lx+55,cy+8,F(SANS_B,36),h2r(pri))
        txt(draw,desc,lx+55,cy+52,F(SANS_R,30),(80,80,90))

    for i,(title,desc) in enumerate(right_items):
        cy=col_y+i*115
        circ(draw,rx+20,cy+24,20,dot_col)
        txt(draw,str(i+6).zfill(2),rx+7,cy+10,F(SANS_B,24),"#FFFFFF")
        txt(draw,title,rx+55,cy+8,F(SANS_B,36),h2r(pri))
        txt(draw,desc,rx+55,cy+52,F(SANS_R,30),(80,80,90))

    # Files badge (top right)
    rr(draw,[W-260,60,W-40,200],20,h2r(acc))
    txt_c(draw,p["files"],W-150,72,F(SERIF_B,72),"#FFFFFF")
    txt_c(draw,"FILES",W-150,152,F(SANS_B,32),"#FFFFFF")

    # Bottom row of badges
    badge_y=H-110
    badges=[("INSTANT","DOWNLOAD"),("LIFETIME","ACCESS"),("DONE-FOR-YOU","TEMPLATES"),("FULLY","CUSTOMIZABLE")]
    bw=420; gap=20; total=len(badges)*bw+(len(badges)-1)*gap
    bx=(W-total)//2
    for label1,label2 in badges:
        rr(draw,[bx,badge_y,bx+bw,badge_y+80],16,h2r(pri))
        txt_c(draw,f"{label1} {label2}",bx+bw//2,badge_y+22,F(SANS_B,28),"#FFFFFF")
        bx+=bw+gap

    # Number badge
    rr(draw,[40,H-120,130,H-35],10,h2r(acc))
    txt_c(draw,"01",85,H-110,F(SANS_B,56),"#FFFFFF")

    return img

# ─── SLIDE 2: WHAT'S INSIDE ──────────────────────────────────────────────────
def slide2(p):
    pri=p["pri"]; acc=p["acc"]
    img=Image.new("RGB",(W,H),"#FFFFFF")
    draw=ImageDraw.Draw(img)

    # Top bar
    draw.rectangle([0,0,W,130],fill=h2r(pri))
    txt_c(draw,"02",W//2,10,F(SANS_B,100),h2r(acc))
    txt(draw,"WHAT'S INSIDE?",60,25,F(SERIF_B,80),"#FFFFFF")

    # Subtitle
    txt_c(draw,f"{len(p['contents'])} Professional Resources",W//2,145,F(SANS_B,50),h2r(acc))
    txt_c(draw,f"To {p['tagline'].split('&')[0].strip().lower().replace('the complete system to ','')}",W//2,205,F(SANS_R,36),(60,60,70),)

    # Left panel - product card
    lx=50; ly=270; lw=580; lh=1100
    rr(draw,[lx,ly,lx+lw,ly+lh],24,h2r(pri))
    txt_c(draw,p["name"],lx+lw//2,ly+50,F(SERIF_B,52),"#FFFFFF")
    txt_c(draw,p["line2"],lx+lw//2,ly+120,F(SANS_B,38),h2r(acc))
    # Decorative lines in card
    for i in range(5):
        y=ly+210+i*80
        rr(draw,[lx+40,y,lx+lw-40,y+12],6,(255,255,255,60))
    txt_c(draw,p["files"],lx+lw//2,ly+680,F(SERIF_B,130),h2r(acc))
    txt_c(draw,"FILES INCLUDED",lx+lw//2,ly+830,F(SANS_B,36),"#FFFFFF")
    txt_c(draw,p["audience"],lx+lw//2,ly+920,F(SANS_R,30),(200,210,230))
    # Instant download badge in card
    rr(draw,[lx+80,ly+1000,lx+lw-80,ly+1070],20,h2r(acc))
    txt_c(draw,"INSTANT DOWNLOAD",lx+lw//2,ly+1018,F(SANS_B,30),"#FFFFFF")

    # Right side - numbered items
    rx=680
    for i,(title,desc) in enumerate(p["contents"]):
        row=i; col=0 if i<5 else 1
        if col==1: row=i-5
        x=rx+col*620
        y=270+row*210
        # Number circle
        circ(draw,x+30,y+36,30,h2r(acc))
        txt_c(draw,str(i+1).zfill(2),x+30,y+14,F(SANS_B,30),"#FFFFFF")
        # Content
        txt(draw,title,x+74,y+10,F(SANS_B,40),h2r(pri))
        txt_block(draw,desc,x+74,y+58,560,F(SANS_R,30),(80,90,100),lh=38)
        # Divider line
        draw.line([(x+74,y+180),(x+600,y+180)],fill=(220,225,235),width=2)

    # Bottom bar
    draw.rectangle([0,H-90,W,H],fill=h2r(pri))
    txt_c(draw,f"{len(p['contents'])} HIGH-QUALITY RESOURCES  |  FULLY CUSTOMIZABLE  |  EDIT & USE TODAY!",W//2,H-72,F(SANS_B,34),"#FFFFFF")

    return img

# ─── SLIDE 3: CONTENT PREVIEW ────────────────────────────────────────────────
def slide3(p):
    pri=p["pri"]; acc=p["acc"]
    bg=lighten(pri,0.96)
    img=Image.new("RGB",(W,H),bg)
    draw=ImageDraw.Draw(img)

    # Header
    draw.rectangle([0,0,W,140],fill=h2r(pri))
    txt(draw,"03",50,10,F(SANS_B,110),h2r(acc))
    txt_c(draw,"CONTENT PREVIEW",W//2,25,F(SERIF_B,80),"#FFFFFF")
    txt_c(draw,"High-Quality, Ready-to-Use Files Included in Your Kit",W//2,152,F(SANS_R,40),(60,65,80))

    # File type indicator strip
    types=["DOCX","XLSX","CSV","PPTX","PDF","MD"]
    type_colors=["#2B5BA8","#1D6A2E","#0D8A6A","#C9540A","#C0392B","#4A4A4A"]
    tx=80
    for t,tc in zip(types,type_colors):
        rr(draw,[tx,200,tx+200,250],8,h2r(tc))
        txt_c(draw,t,tx+100,210,F(SANS_B,36),"#FFFFFF")
        tx+=220

    # Content preview cards in 2x3 grid
    items=p["contents"][:6]
    cols=2; rows=3
    cw=860; ch=330; gap=40
    total_w=cols*cw+(cols-1)*gap
    sx=(W-total_w)//2

    file_icons=["📊","📋","📄","📈","📝","🗂"]
    file_ext=["XLSX","DOCX","PDF","XLSX","DOCX","CSV"]
    ext_colors=["#1D6A2E","#2B5BA8","#C0392B","#1D6A2E","#2B5BA8","#0D8A6A"]

    for i,((title,desc),icon,ext,ec) in enumerate(zip(items,file_icons,file_ext,ext_colors)):
        col=i%cols; row=i//cols
        x=sx+col*(cw+gap); y=290+row*(ch+gap)
        rr(draw,[x,y,x+cw,y+ch],20,"#FFFFFF")
        # Color left strip
        rr(draw,[x,y,x+16,y+ch],8,h2r(acc))
        # File type badge
        rr(draw,[x+30,y+20,x+150,y+66],10,h2r(ec))
        txt_c(draw,ext,x+90,y+26,F(SANS_B,34),"#FFFFFF")
        # Title and description
        txt(draw,title,x+170,y+22,F(SANS_B,38),h2r(pri))
        txt_block(draw,desc,x+30,y+85,cw-60,F(SANS_R,32),(70,80,95),lh=44)
        # Bottom detail line
        draw.line([(x+30,y+ch-50),(x+cw-30,y+ch-50)],fill=lighten(pri,0.75),width=2)
        txt(draw,"Included in your download",x+30,y+ch-42,F(SANS_R,26),h2r(acc))

    # Bottom
    draw.rectangle([0,H-80,W,H],fill=h2r(acc))
    txt_c(draw,f"EVERYTHING YOU NEED TO START IMMEDIATELY  |  {p['files']} FILES  |  {p['price']} ONE-TIME",W//2,H-64,F(SANS_B,34),"#FFFFFF")

    return img

# ─── SLIDE 4: THE SYSTEM ─────────────────────────────────────────────────────
def slide4(p):
    pri=p["pri"]; acc=p["acc"]
    img=gradient_bg((W,H), pri, darken(pri,0.75))
    draw=ImageDraw.Draw(img)

    # Decorative top
    draw.rectangle([0,0,W,14],fill=h2r(acc))

    # Header
    txt_c(draw,"04",W//2,30,F(SANS_B,90),(*h2r(acc),40))
    txt_c(draw,f"COMPLETE {p['name']}",W//2,50,F(SERIF_B,72),"#FFFFFF")
    txt_c(draw,f"SYSTEM FOR {p['audience'].upper()}",W//2,138,F(SERIF_B,50),h2r(acc))

    divider(draw,W//2,210,600,h2r(acc),"◆")

    subtitle=f"A Proven {len(p['pillars'])}-Step System to {p['tagline'].replace('The complete system to','').strip()}"
    txt_block_c(draw,subtitle,W//2,260,1500,F(SANS_R,36),(230,235,245),lh=50)

    # Pillars
    py=380; ph=210; gap=22
    for i,(pillar,desc) in enumerate(p["pillars"]):
        y=py+i*(ph+gap)
        # Background card
        rr(draw,[60,y,W-60,y+ph],18,(255,255,255,18))
        # Number badge
        rr(draw,[60,y,160,y+ph],18,h2r(acc))
        txt_c(draw,str(i+1).zfill(2),110,y+75,F(SERIF_B,66),"#FFFFFF")
        # Pillar title
        txt(draw,pillar,195,y+24,F(SERIF_B,60),"#FFFFFF")
        # Description
        txt_block(draw,desc,195,y+100,1400,F(SANS_R,36),(200,210,225),lh=48)
        # Checkmark items preview
        for j in range(3):
            if j<len(p["benefits"]):
                txt(draw,f"  ✓  {p['benefits'][j][:55]}",195+j*530,y+ph-50,F(SANS_R,26),h2r(acc))

    # Bottom
    draw.rectangle([0,H-80,W,H],fill=h2r(acc))
    txt_c(draw,"ONE COMPLETE SYSTEM. INSTANT DOWNLOAD. USE FOREVER.",W//2,H-64,F(SANS_B,36),"#FFFFFF")

    return img

# ─── SLIDE 5: BENEFITS ───────────────────────────────────────────────────────
def slide5(p):
    pri=p["pri"]; acc=p["acc"]
    img=Image.new("RGB",(W,H),"#FFFFFF")
    draw=ImageDraw.Draw(img)

    # Header
    draw.rectangle([0,0,W,130],fill=h2r(pri))
    txt(draw,"05",40,10,F(SANS_B,100),h2r(acc))
    txt_c(draw,"EVERYTHING YOU NEED",W//2,18,F(SERIF_B,68),"#FFFFFF")
    txt_c(draw,"TO SAVE TIME & GROW FAST",W//2,94,F(SERIF_B,56),h2r(acc))

    # Left column - benefits checklist
    benefits=p["benefits"]
    bx=60; by=160; bl_w=1180
    for i,b in enumerate(benefits):
        y=by+i*115
        rr(draw,[bx,y+4,bx+bl_w,y+94],16,lighten(pri,0.94))
        circ(draw,bx+44,y+48,30,h2r(acc))
        txt(draw,"✓",bx+30,y+28,F(SANS_B,32),"#FFFFFF")
        txt(draw,b,bx+96,y+16,F(SANS_B,40),h2r(pri))
        draw.line([(bx+96,y+66),(bx+bl_w-30,y+66)],fill=lighten(pri,0.80),width=2)

    # Right panel - price & guarantee
    rx=1280; ry=160; rpw=650; rph=760
    rr(draw,[rx,ry,rx+rpw,ry+rph],30,h2r(pri))
    txt_c(draw,"ONLY",rx+rpw//2,ry+50,F(SANS_B,44),"#FFFFFF")
    txt_c(draw,p["price"],rx+rpw//2,ry+110,F(SERIF_B,130),h2r(acc))
    txt_c(draw,"ONE-TIME PAYMENT",rx+rpw//2,ry+260,F(SANS_B,36),(200,210,225))
    divider(draw,rx+rpw//2,ry+320,500,h2r(acc))
    txt_c(draw,p["files"]+" FILES",rx+rpw//2,ry+380,F(SANS_B,44),"#FFFFFF")
    txt_c(draw,"INCLUDED",rx+rpw//2,ry+440,F(SANS_R,36),(200,210,225))
    rr(draw,[rx+60,ry+520,rx+rpw-60,ry+600],20,h2r(acc))
    txt_c(draw,"INSTANT DOWNLOAD",rx+rpw//2,ry+538,F(SANS_B,38),"#FFFFFF")
    txt_c(draw,"Use forever  |  Lifetime access",rx+rpw//2,ry+630,F(SANS_R,32),(200,210,225))
    txt_c(draw,"30-day satisfaction guarantee",rx+rpw//2,ry+680,F(SANS_R,30),(180,190,210))

    # Bottom badges
    badge_y=H-110
    badges=["INSTANT DOWNLOAD","LIFETIME ACCESS","USE FOREVER","EDIT FREELY"]
    bw=430; gap=22; total=len(badges)*bw+(len(badges)-1)*gap
    bx2=(W-total)//2
    for b in badges:
        rr(draw,[bx2,badge_y,bx2+bw,badge_y+80],16,h2r(acc))
        txt_c(draw,b,bx2+bw//2,badge_y+22,F(SANS_B,30),"#FFFFFF")
        bx2+=bw+gap

    return img

# ─── SLIDE 6: BEFORE / AFTER ─────────────────────────────────────────────────
def slide6(p):
    pri=p["pri"]; acc=p["acc"]
    img=Image.new("RGB",(W,H),"#FFFFFF")
    draw=ImageDraw.Draw(img)

    # Header
    draw.rectangle([0,0,W,140],fill=h2r(pri))
    txt(draw,"06",40,10,F(SANS_B,110),h2r(acc))
    ba_title=f"FROM STRUGGLE  →  TO SYSTEM"
    txt_c(draw,ba_title,W//2,28,F(SERIF_B,68),"#FFFFFF")
    txt_c(draw,"See the difference a proven system makes",W//2,105,F(SANS_R,40),(200,215,230))

    # Before column
    col_w=840; pad=60
    lx=pad; rx=W//2+pad; col_h=H-310
    rr(draw,[lx,170,lx+col_w,170+col_h],24,lighten("#CC3333",0.93))
    draw.rectangle([lx,170,lx+col_w,250],fill=h2r("#CC3333"))
    txt_c(draw,"BEFORE",lx+col_w//2,178,F(SERIF_B,58),"#FFFFFF")
    txt_c(draw,"Without this system",lx+col_w//2,242,F(SANS_R,30),(100,30,30))

    for i,b in enumerate(p["before"]):
        y=290+i*150
        rr(draw,[lx+30,y,lx+col_w-30,y+120],16,(255,255,255))
        circ(draw,lx+66,y+60,26,h2r("#CC3333"))
        txt(draw,"✗",lx+53,y+38,F(SANS_B,28),"#FFFFFF")
        txt_block(draw,b,lx+106,y+18,680,F(SANS_R,36),(80,30,30),lh=46)

    # After column
    rr(draw,[rx,170,rx+col_w,170+col_h],24,lighten(acc,0.93))
    draw.rectangle([rx,170,rx+col_w,250],fill=h2r(acc))
    txt_c(draw,"AFTER",rx+col_w//2,178,F(SERIF_B,58),"#FFFFFF")
    txt_c(draw,"With this system",rx+col_w//2,242,F(SANS_R,30),(40,60,40))

    for i,a in enumerate(p["after"]):
        y=290+i*150
        rr(draw,[rx+30,y,rx+col_w-30,y+120],16,(255,255,255))
        circ(draw,rx+66,y+60,26,h2r(acc))
        txt(draw,"✓",rx+53,y+38,F(SANS_B,28),"#FFFFFF")
        txt_block(draw,a,rx+106,y+18,680,F(SANS_R,36),(20,50,20) if acc!="#C9A84C" else (50,40,10),lh=46)

    # Bottom
    draw.rectangle([0,H-80,W,H],fill=h2r(pri))
    txt_c(draw,f"GET THE SYSTEM  |  {p['files']} FILES  |  {p['price']}  |  INSTANT DOWNLOAD",W//2,H-64,F(SANS_B,34),"#FFFFFF")

    return img

# ─── SLIDE 7: EASY TO USE ────────────────────────────────────────────────────
def slide7(p):
    pri=p["pri"]; acc=p["acc"]
    bg=lighten(pri,0.95)
    img=Image.new("RGB",(W,H),bg)
    draw=ImageDraw.Draw(img)

    draw.rectangle([0,0,W,14],fill=h2r(acc))
    draw.rectangle([0,H-14,W,H],fill=h2r(acc))

    # Header
    txt_c(draw,"07",W//2,20,F(SANS_B,90),(*h2r(pri),25))
    txt_c(draw,"BEAUTIFULLY ORGANIZED",W//2,60,F(SERIF_B,78),h2r(pri))
    txt_c(draw,"& EASY TO USE",W//2,152,F(SERIF_B,70),h2r(acc))
    txt_c(draw,"Access Your Entire Kit on Any Device",W//2,242,F(SANS_R,44),(70,80,95))
    draw.line([(100,300),(W-100,300)],fill=lighten(pri,0.75),width=3)

    # Left panel - feature list
    lx=60; ly=330; fw=860
    features=[
        ("FULLY CUSTOMIZABLE","Edit everything in Word, Excel & Canva to match your brand"),
        ("INSTANT ACCESS","Download right away and start using today -- no waiting"),
        ("ORGANIZED & EASY","Everything is labeled, sorted and ready to go"),
        ("WORKS ON ANY DEVICE","Open on your laptop, tablet or phone with no issues"),
        ("PROFESSIONAL QUALITY","Designed to the standard of a premium business resource"),
    ]
    for i,(ftitle,fdesc) in enumerate(features):
        y=ly+i*230
        rr(draw,[lx,y,lx+fw,y+200],20,"#FFFFFF")
        rr(draw,[lx,y,lx+fw,y+200],20,None,h2r(acc),2)
        circ(draw,lx+50,y+100,34,h2r(acc))
        txt(draw,"✓",lx+36,y+78,F(SANS_B,34),"#FFFFFF")
        txt(draw,ftitle,lx+100,y+28,F(SANS_B,40),h2r(pri))
        txt_block(draw,fdesc,lx+100,y+82,700,F(SANS_R,32),(70,80,95),lh=42)

    # Right panel - device mockup illustration
    rx=1000; ry=330; rpw=920; rph=1090
    rr(draw,[rx,ry,rx+rpw,ry+rph],30,"#FFFFFF")
    rr(draw,[rx,ry,rx+rpw,ry+rph],30,None,h2r(pri),3)
    # Laptop illustration
    rr(draw,[rx+60,ry+50,rx+rpw-60,ry+580],20,h2r(pri))
    rr(draw,[rx+80,ry+70,rx+rpw-80,ry+560],12,lighten(pri,0.85))
    txt_c(draw,p["name"],rx+rpw//2,ry+180,F(SANS_B,44),h2r(pri))
    txt_c(draw,p["line2"],rx+rpw//2,ry+240,F(SANS_R,34),h2r(acc))
    txt_c(draw,p["files"]+" FILES",rx+rpw//2,ry+340,F(SERIF_B,80),h2r(acc))
    txt_c(draw,"INCLUDED",rx+rpw//2,ry+440,F(SANS_B,36),h2r(pri))
    # Laptop base
    rr(draw,[rx+20,ry+585,rx+rpw-20,ry+620],8,h2r(pri))
    # Tablet illustration
    rr(draw,[rx+60,ry+650,rx+420,ry+970],16,h2r(pri))
    rr(draw,[rx+74,ry+664,rx+406,ry+956],10,lighten(pri,0.85))
    txt_c(draw,p["name"],rx+240,ry+760,F(SANS_B,30),h2r(pri))
    txt_c(draw,p["files"],rx+240,ry+830,F(SERIF_B,54),h2r(acc))
    # Phone illustration
    rr(draw,[rx+460,ry+700,rx+680,ry+970],22,h2r(pri))
    rr(draw,[rx+472,ry+712,rx+668,ry+958],14,lighten(pri,0.85))
    txt_c(draw,p["line2"],rx+570,ry+810,F(SANS_B,24),h2r(pri))
    txt_c(draw,p["price"],rx+570,ry+856,F(SERIF_B,40),h2r(acc))

    # Format badges row
    formats=[("WORD","#2B5BA8"),("EXCEL","#1D6A2E"),("CSV","#0D8A6A"),("PPT","#C9540A"),("PDF","#C0392B")]
    fw2=150; fg=18; ftotal=len(formats)*fw2+(len(formats)-1)*fg
    fx=(rx+(rpw-ftotal)//2)
    fy=ry+rph-100
    for fname,fcolor in formats:
        rr(draw,[fx,fy,fx+fw2,fy+72],14,h2r(fcolor))
        txt_c(draw,fname,fx+fw2//2,fy+18,F(SANS_B,30),"#FFFFFF")
        fx+=fw2+fg

    # Instant download badge
    rr(draw,[rx+200,ry+rph-175,rx+rpw-200,ry+rph-110],22,h2r(acc))
    txt_c(draw,"INSTANT DOWNLOAD",rx+rpw//2,ry+rph-166,F(SANS_B,38),"#FFFFFF")

    # Bottom tagline
    draw.rectangle([0,H-80,W,H],fill=h2r(pri))
    txt_c(draw,f"YOUR COMPLETE {p['name']} KIT -- READY WHEN YOU ARE",W//2,H-65,F(SANS_B,38),"#FFFFFF")

    return img

# ─── MAIN RUNNER ─────────────────────────────────────────────────────────────
slide_funcs=[slide1,slide2,slide3,slide4,slide5,slide6,slide7]
slide_names=["01_Cover","02_WhatsInside","03_ContentPreview","04_TheSystem","05_Benefits","06_BeforeAfter","07_EasyToUse"]

total=0
for p in PRODUCTS:
    folder=OUT+p["id"]+"_"+p["name"].replace(" ","_")+"/"
    os.makedirs(folder,exist_ok=True)
    for fn,fname in zip(slide_funcs,slide_names):
        try:
            img=fn(p)
            path=folder+fname+".png"
            img.save(path,quality=95)
            total+=1
            print(f"  {p['id']} {fname}")
        except Exception as e:
            print(f"  ERROR {p['id']} {fname}: {e}")

print(f"\nDone: {total} images generated in {OUT}")
