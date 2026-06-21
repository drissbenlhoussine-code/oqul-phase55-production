#!/usr/bin/env python3
"""Real Estate Agent OS - Part 3: Folders 08-10"""
import os, csv
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

BASE = "/home/user/oqul-phase55-production/real-estate-agent-os/Ultimate_Real_Estate_Agent_Operating_System/"
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

def write_csv(path, headers, rows):
    with open(BASE+path, "w", newline="", encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
    print(f"  ✓ {path}")

# ─── 08_POST_CLOSING_RETENTION ────────────────────────────────────────────────
p08 = "08_POST_CLOSING_RETENTION/"

doc(p08+"Post_Closing_Follow_Up_System.docx",
    "Post-Closing Follow-Up System",
    "Real Estate Agent OS | Client Retention & Referral Generation",
    [
        ("Post-Closing Communication Strategy", [
            ("•", "Day 1 – Send personalized thank-you card and closing gift"),
            ("•", "Day 3 – Call to confirm move-in went smoothly and everything is settling"),
            ("•", "Day 7 – Email with list of recommended local vendors: plumbers, electricians, painters"),
            ("•", "Day 30 – Check-in call: ask how they are loving the new home"),
            ("•", "Day 90 – Mail a quarterly neighborhood market update report"),
            ("•", "Day 180 – Send mid-year home valuation report with personalized note"),
        ]),
        ("Annual Client Retention Calendar", [
            ("•", "January: New Year card + annual home valuation report"),
            ("•", "February: Valentine's Day card with a local restaurant recommendation"),
            ("•", "March: Spring maintenance checklist email"),
            ("•", "April: Property tax reminder and appeal deadline notice"),
            ("•", "May: Home appreciation update + market conditions summary"),
            ("•", "June: Summer entertainment tips and home improvement ideas"),
            ("•", "July: Fourth of July card + mid-year market report"),
            ("•", "August: Back-to-school neighborhood guide (for families)"),
            ("•", "September: Fall maintenance checklist"),
            ("•", "October: Halloween card + home equity update"),
            ("•", "November: Thanksgiving card + gratitude message"),
            ("•", "December: Holiday card + year-in-review market summary"),
        ]),
        ("Client Appreciation Events", [
            "Host 2–3 client appreciation events annually to stay top-of-mind and generate referrals.",
            ("•", "Spring Event: Easter egg hunt or spring picnic at a local park"),
            ("•", "Summer Event: Outdoor movie night or BBQ cookout"),
            ("•", "Holiday Event: Annual holiday party (December) with food, drinks, and giveaways"),
            ("•", "Invite past clients, sphere of influence, and their families"),
            ("•", "Budget: $20–$50 per attendee; aim for 50–100 guests"),
        ]),
        ("Referral Request Scripts", [
            "Use these scripts at the 30-day and 6-month touchpoints to ask for referrals naturally:",
            '"[Client Name], I\'m so glad the move went smoothly! I wanted to let you know that my business grows almost entirely through referrals from wonderful clients like you. If anyone in your life is thinking about buying or selling, I would be honored if you\'d pass my name along."',
            '"[Client Name], it\'s been 6 months since we closed on your home and I hope you\'re loving every moment! I love staying in touch with my clients and making sure you have everything you need. And if you ever hear of anyone who needs a great real estate agent, please think of me!"',
        ]),
        ("Post-Closing Gift Ideas", [
            ("•", "Personalized cutting board or door mat with new address"),
            ("•", "Local restaurant gift cards or grocery store gift card"),
            ("•", "Professional cleaning service for the new home"),
            ("•", "Custom neighborhood map framed print"),
            ("•", "Smart home starter kit (smart thermostat or doorbell camera)"),
            ("•", "Wine or champagne with personalized closing label"),
            ("•", "Home warranty policy contribution"),
        ]),
        ("Milestone Anniversary Program", [
            ("•", "1-Year Anniversary: Send a '1 Year in Your New Home' card with a home value update"),
            ("•", "2-Year Anniversary: Call to check in on any real estate needs or changes in life"),
            ("•", "3-Year Anniversary: Mail a market appreciation report showing equity growth"),
            ("•", "5-Year Anniversary: Invite to a VIP client appreciation dinner"),
            ("•", "Automate milestone dates in your CRM to never miss an anniversary"),
        ]),
    ])

doc(p08+"Sphere_Of_Influence_Nurture_Plan.docx",
    "Sphere of Influence (SOI) Nurture Plan",
    "Real Estate Agent OS | Relationship Marketing & Referral System",
    [
        ("Understanding Your Sphere of Influence", [
            "Your Sphere of Influence (SOI) is the most powerful lead source available to a real estate agent. Research shows that 64% of sellers and 41% of buyers choose an agent they already know or who was referred to them.",
            ("•", "SOI includes: family, friends, past clients, neighbors, coworkers, business contacts"),
            ("•", "Goal: Stay top-of-mind so you are the first person they call or refer"),
            ("•", "Rule of 33: Contact your top 33 SOI members at least once per month"),
            ("•", "Expand SOI by 50–100 new people per year through networking and community involvement"),
        ]),
        ("SOI Segmentation", [
            "Divide your SOI into tiers based on relationship strength and referral potential:",
            ("•", "Tier 1 — Champions (top 33): Monthly personal contact (calls, coffees, events)"),
            ("•", "Tier 2 — Advocates (next 100): Bi-monthly contact (email, social media, cards)"),
            ("•", "Tier 3 — Prospects (remaining): Quarterly touchpoint (newsletter, market update)"),
        ]),
        ("Monthly SOI Contact System", [
            ("•", "Week 1: Personal phone call to 5–8 Tier 1 contacts"),
            ("•", "Week 2: Handwritten note cards to 5 contacts with a personalized message"),
            ("•", "Week 3: Send market update email to full database"),
            ("•", "Week 4: Social media engagement — comment, like, and share SOI posts"),
        ]),
        ("SOI Conversation Scripts", [
            "Catching Up Call:",
            '"Hey [Name], it\'s [Your Name]! I was just thinking about you and wanted to call and check in. How\'s everything going with [family/work/recent event]?"',
            '"Things are going great on my end — I\'ve been busy helping families find amazing homes. Speaking of which, do you know anyone who might be thinking about making a move this year?"',
            "Referral Introduction Call:",
            '"Hi [Name], I heard through [mutual contact] that you might be thinking about selling your home. I\'d love to get together for 20 minutes and share what the market is doing in your neighborhood. When would work for you?"',
        ]),
        ("SOI Database Management", [
            ("•", "Record every SOI contact in your CRM with date, notes, and next follow-up"),
            ("•", "Update contact details annually — phone, email, address, life events"),
            ("•", "Track referrals received from each SOI member and send thank-you gifts"),
            ("•", "Remove disengaged contacts after 3 years of no response"),
        ]),
    ])

doc(p08+"Client_Reviews_Testimonials_System.docx",
    "Client Reviews & Testimonials System",
    "Real Estate Agent OS | Reputation Management & Social Proof",
    [
        ("Why Reviews Matter", [
            ("•", "84% of consumers trust online reviews as much as personal recommendations"),
            ("•", "Agents with 20+ Google reviews receive 70% more inquiries than those with fewer"),
            ("•", "Reviews on Zillow, Realtor.com, and Google directly impact lead volume"),
            ("•", "Goal: Collect a review after every closed transaction within 7 days of closing"),
        ]),
        ("Review Request Process", [
            "Step 1 — Closing Day: Mention reviews in person: 'I'm going to send you a quick link — if you'd be willing to share your experience, it would mean the world to me.'",
            "Step 2 — Day 1 After Closing: Send review request email with direct links to Google, Zillow, and Realtor.com.",
            "Step 3 — Day 7 Follow-Up: Text reminder if no review received: 'Hey [Name], just a gentle reminder on that review — it takes less than 2 minutes and helps me so much!'",
            "Step 4 — Save and Repurpose: Screenshot all reviews for social media, website, and listing presentations.",
        ]),
        ("Review Request Email Template", [
            '"Subject: A Quick Favor, [Name]?"',
            '"Hi [Name],",',
            '"Congratulations again on your [purchase/sale]! It was truly an honor to work with you and help you [achieve goal].",',
            '"If you have 2 minutes, I would be so grateful if you could share your experience online. Reviews from wonderful clients like you are what help me continue helping other families.",',
            '"Here are the links:",',
            '"Google Review: [Your Google Review Link]",',
            '"Zillow Review: [Your Zillow Profile Link]",',
            '"Thank you so much — your support means everything to me!",',
            '"Warmly, [Your Name]"',
        ]),
        ("Testimonial Collection for Marketing", [
            ("•", "Ask 3 specific questions for a detailed testimonial: What was your biggest challenge? How did I help? Would you recommend me?"),
            ("•", "Use testimonial quotes in listing presentations, website, and social media graphics"),
            ("•", "Create video testimonials: Short 30–60 second phone videos from happy clients"),
            ("•", "Feature testimonials in email newsletters with client permission"),
        ]),
        ("Review Platforms Priority", [
            ("•", "Google My Business (highest priority — affects local SEO)"),
            ("•", "Zillow (buyer/seller leads browse agent profiles here)"),
            ("•", "Realtor.com (secondary platform for additional credibility)"),
            ("•", "Facebook (community trust and social proof)"),
            ("•", "Yelp (additional local business credibility)"),
        ]),
    ])

print("✓ 08_POST_CLOSING_RETENTION complete")

# ─── 09_BUSINESS_OPERATIONS ───────────────────────────────────────────────────
p09 = "09_BUSINESS_OPERATIONS/"

doc(p09+"Annual_Business_Plan.docx",
    "Annual Business Plan Template",
    "Real Estate Agent OS | Business Planning & Goal Setting",
    [
        ("Annual Vision Statement", [
            "Fill in your vision for the coming year:",
            "My vision for [Year]: I will [production goal] while serving [X] clients with exceptional experience, building [specific milestone], and achieving [personal goal].",
        ]),
        ("Production Goals", [
            ("•", "Annual GCI Target: $___________"),
            ("•", "Number of Transactions: ___________"),
            ("•", "Average Sales Price: $___________"),
            ("•", "Buyer Transactions: ___________"),
            ("•", "Seller Transactions: ___________"),
            ("•", "Referral Transactions: ___________"),
            ("•", "New Construction/Investor Transactions: ___________"),
        ]),
        ("Lead Generation Targets", [
            ("•", "SOI Contacts (database size): ___________"),
            ("•", "New Contacts Added This Year: ___________"),
            ("•", "Open Houses Hosted: ___________"),
            ("•", "Online Leads Generated: ___________"),
            ("•", "Referral Partners Developed: ___________"),
        ]),
        ("Marketing Budget Allocation", [
            ("•", "Social Media Advertising: $___________/month"),
            ("•", "Direct Mail Campaigns: $___________/quarter"),
            ("•", "Client Events: $___________/year"),
            ("•", "Photography & Video: $___________/year"),
            ("•", "CRM & Technology: $___________/year"),
            ("•", "Professional Development: $___________/year"),
        ]),
        ("Quarterly Milestones", [
            ("•", "Q1 (Jan–Mar): [Goal + KPI]"),
            ("•", "Q2 (Apr–Jun): [Goal + KPI]"),
            ("•", "Q3 (Jul–Sep): [Goal + KPI]"),
            ("•", "Q4 (Oct–Dec): [Goal + KPI]"),
        ]),
        ("Personal Development Plan", [
            ("•", "Designations to Earn: ___________"),
            ("•", "Books to Read: ___________"),
            ("•", "Conferences to Attend: ___________"),
            ("•", "Coaching or Mentorship: ___________"),
            ("•", "Health & Wellness Goals: ___________"),
        ]),
    ])

doc(p09+"Weekly_Agent_Schedule_Template.docx",
    "Weekly Agent Schedule Template",
    "Real Estate Agent OS | Time Blocking & Productivity System",
    [
        ("Time Blocking Philosophy", [
            "Successful real estate agents protect their time by blocking specific hours for income-producing activities. Without a schedule, reactive tasks (emails, calls, problems) will consume your entire day.",
        ]),
        ("Model Week Schedule", [
            ("•", "Monday: 8–9am Admin + email; 9–11am Prospecting calls (SOI + follow-up); 11am–12pm CRM updates; 1–3pm Buyer showings; 3–5pm Listing appointments; 5–6pm Admin wrap-up"),
            ("•", "Tuesday: 8–9am Social media content creation; 9–11am Lead follow-up; 11am–12pm Market research; 1–5pm Buyer appointments; 5–6pm Contract review"),
            ("•", "Wednesday: 8–9am Admin; 9–11am Prospecting calls; 11am–12pm CRM; 1–3pm Listing activities (photos, staging consult); 3–6pm Office admin"),
            ("•", "Thursday: 8–9am Business planning; 9–11am Lead follow-up; 11am–1pm Networking lunch; 1–4pm Buyer showings; 4–6pm Offer writing"),
            ("•", "Friday: 8–9am Weekly review; 9–11am Prospecting; 11am–12pm Training or podcast; 1–4pm Open house prep; 4–5pm Team/broker check-in"),
            ("•", "Saturday: 10am–4pm Open house (2 hours each location); 4–5pm Follow-up new leads"),
            ("•", "Sunday: Personal day — protect family time"),
        ]),
        ("Income-Producing Activities (IPAs)", [
            "Block a minimum of 3 hours daily for these activities — they directly produce income:",
            ("•", "Prospecting calls to SOI and leads"),
            ("•", "Listing appointments and buyer consultations"),
            ("•", "Writing and negotiating offers"),
            ("•", "Hosting open houses"),
            ("•", "Networking with referral partners"),
        ]),
        ("Daily Habits for High Performers", [
            ("•", "Morning: Review daily schedule and top 3 priorities before email"),
            ("•", "Prospecting block: No interruptions — phone calls only"),
            ("•", "EOD review: Log all contacts and update CRM before shutting down"),
            ("•", "Weekly planning: Every Friday — set next week's schedule and goals"),
        ]),
        ("Weekly Metrics Tracking", [
            ("•", "Calls Made: ___"),
            ("•", "Contacts Reached: ___"),
            ("•", "Appointments Set: ___"),
            ("•", "Appointments Held: ___"),
            ("•", "Offers Written: ___"),
            ("•", "Closings This Week: ___"),
        ]),
    ])

doc(p09+"Commission_Tracking_System.docx",
    "Commission Tracking System",
    "Real Estate Agent OS | Financial Management & Income Planning",
    [
        ("Commission Structure Overview", [
            ("•", "Buyer Agent Commission: Typically 2–3% of purchase price (negotiated)"),
            ("•", "Listing Agent Commission: Typically 2–3% of purchase price"),
            ("•", "Total Commission: 5–6% split between buyer and listing agent"),
            ("•", "Brokerage Split: Your commission is further split with your brokerage per your agreement"),
            ("•", "Track gross commission, brokerage split, and net commission separately"),
        ]),
        ("Commission Calculation Examples", [
            ("•", "$300,000 sale at 6% total = $18,000 gross commission"),
            ("•", "Your side (3%) = $9,000 gross"),
            ("•", "Brokerage split (80/20) = $7,200 net to you"),
            ("•", "After taxes (25% self-employed) = $5,400 take-home"),
            ("•", "Track all expenses against commission to understand true profitability"),
        ]),
        ("Monthly Income Projection System", [
            "Use this formula to project monthly income:",
            ("•", "Pipeline Value = Sum of all active transaction expected commissions"),
            ("•", "Close Rate = Historical percentage of pipeline that closes"),
            ("•", "Projected Monthly Income = Pipeline Value × Close Rate"),
            ("•", "Example: $80,000 pipeline × 75% close rate = $60,000 projected"),
        ]),
        ("Business Expense Categories", [
            ("•", "Marketing & Advertising: Social media ads, direct mail, print materials"),
            ("•", "Technology: CRM, MLS fees, transaction management software"),
            ("•", "Professional Development: Continuing education, coaching, conferences"),
            ("•", "Vehicle: Mileage at IRS rate ($0.67/mile in 2024), gas, maintenance"),
            ("•", "Office & Admin: Supplies, virtual assistant, phone"),
            ("•", "Client Gifts & Entertainment: Closing gifts, client events, meals"),
        ]),
        ("Quarterly Tax Planning", [
            ("•", "Set aside 25–30% of net commission for federal + state taxes"),
            ("•", "Pay estimated quarterly taxes: April 15, June 15, September 15, January 15"),
            ("•", "Track deductible business expenses throughout the year"),
            ("•", "Meet with CPA quarterly to review P&L and adjust tax strategy"),
            ("•", "Consider S-Corp election when annual net income exceeds $40,000"),
        ]),
    ])

# XLSX - Business Operations Dashboard
wb = Workbook()

# Sheet 1: Annual Business Plan Tracker
ws1 = wb.active; ws1.title = "Annual Business Plan"
ws1.column_dimensions['A'].width = 28
ws1.column_dimensions['B'].width = 16
ws1.column_dimensions['C'].width = 16
ws1.column_dimensions['D'].width = 16
ws1.column_dimensions['E'].width = 28

hrow(ws1,1,[1,2,3,4,5],["Category","Q1 Goal","Q2 Goal","Q3 Goal","Q4 Goal"],NAV)
plan_rows = [
    ("GCI Target","$25,000","$35,000","$40,000","$30,000"),
    ("Transactions","4","6","7","5"),
    ("Buyer Transactions","2","3","4","3"),
    ("Seller Transactions","2","3","3","2"),
    ("New Listings","2","3","3","2"),
    ("SOI Contacts Added","30","30","30","30"),
    ("Open Houses Hosted","6","8","8","6"),
    ("Listing Appointments","4","6","6","4"),
    ("Buyer Consultations","5","7","8","6"),
    ("Referrals Received","3","4","5","4"),
    ("Online Leads","20","25","30","20"),
    ("Marketing Spend","$2,000","$3,000","$3,000","$2,000"),
]
for i, row in enumerate(plan_rows):
    bg = LGR if i%2==0 else WHT
    drow(ws1,i+2,[1,2,3,4,5],list(row),bg)

# Sheet 2: Commission Tracker
ws2 = wb.create_sheet("Commission Tracker")
ws2.column_dimensions['A'].width = 18
ws2.column_dimensions['B'].width = 30
ws2.column_dimensions['C'].width = 14
ws2.column_dimensions['D'].width = 14
ws2.column_dimensions['E'].width = 14
ws2.column_dimensions['F'].width = 14
ws2.column_dimensions['G'].width = 18
ws2.column_dimensions['H'].width = 16

hrow(ws2,1,[1,2,3,4,5,6,7,8],
     ["Close Date","Property Address","Sale Price","Gross Comm %","Gross Comm $","Brokerage Split","Net Commission","Status"],
     NAV)
comm_data = [
    ("2024-01-15","123 Oak Street, Springfield","$285,000","3.0%","$8,550","20%","$6,840","Paid"),
    ("2024-01-28","456 Maple Ave, Riverside","$412,000","2.5%","$10,300","20%","$8,240","Paid"),
    ("2024-02-10","789 Pine Road, Lakewood","$365,000","3.0%","$10,950","20%","$8,760","Paid"),
    ("2024-02-22","321 Elm Drive, Hillside","$525,000","2.5%","$13,125","20%","$10,500","Paid"),
    ("2024-03-08","654 Birch Blvd, Greenview","$198,000","3.0%","$5,940","20%","$4,752","Paid"),
    ("2024-03-20","987 Cedar Lane, Westport","$620,000","2.5%","$15,500","20%","$12,400","Pending"),
    ("2024-04-05","147 Willow Way, Eastside","$445,000","3.0%","$13,350","20%","$10,680","Pending"),
    ("2024-04-18","258 Ash Court, Northview","$310,000","3.0%","$9,300","20%","$7,440","Pipeline"),
]
for i, row in enumerate(comm_data):
    bg = LGR if i%2==0 else WHT
    drow(ws2,i+2,[1,2,3,4,5,6,7,8],list(row),bg)

# Sheet 3: Weekly Activity Tracker
ws3 = wb.create_sheet("Weekly Activity")
ws3.column_dimensions['A'].width = 18
ws3.column_dimensions['B'].width = 14
ws3.column_dimensions['C'].width = 14
ws3.column_dimensions['D'].width = 14
ws3.column_dimensions['E'].width = 16
ws3.column_dimensions['F'].width = 16
ws3.column_dimensions['G'].width = 14
ws3.column_dimensions['H'].width = 14

hrow(ws3,1,[1,2,3,4,5,6,7,8],
     ["Week Of","Calls Made","Contacts Reached","Appts Set","Appts Held","Offers Written","Closings","Weekly GCI"],
     NAV)
activity_data = [
    ("Jan 1-7","42","18","5","4","2","1","$6,840"),
    ("Jan 8-14","38","15","4","3","1","1","$8,240"),
    ("Jan 15-21","45","21","6","5","3","0","$0"),
    ("Jan 22-28","41","17","4","4","2","2","$19,260"),
    ("Feb 1-7","39","16","5","3","1","0","$0"),
    ("Feb 8-14","47","22","7","6","3","1","$8,760"),
    ("Feb 15-21","43","19","5","5","2","1","$10,500"),
    ("Feb 22-28","36","14","3","3","1","0","$0"),
]
for i, row in enumerate(activity_data):
    bg = LGR if i%2==0 else WHT
    drow(ws3,i+2,[1,2,3,4,5,6,7,8],list(row),bg)

wb.save(BASE + p09 + "Business_Operations_Dashboard.xlsx")
print(f"  ✓ {p09}Business_Operations_Dashboard.xlsx")
print("✓ 09_BUSINESS_OPERATIONS complete")

# ─── 10_NOTION_WORKSPACE ──────────────────────────────────────────────────────
p10 = "10_NOTION_WORKSPACE/"

# CSV 1: Lead Tracker
write_csv(p10+"Lead_Tracker.csv",
    ["Lead ID","Full Name","Phone","Email","Source","Status","Type","Budget","Timeline","Neighborhood","Last Contact","Next Follow Up","Notes","Agent"],
    [
        ["L001","Michael Johnson","(555) 234-5678","mjohnson@email.com","Zillow","Hot","Buyer","$350,000-$450,000","2-3 months","Westside","2024-01-10","2024-01-17","Pre-approved, motivated","Sarah Mitchell"],
        ["L002","Jennifer Davis","(555) 345-6789","jdavis@email.com","Referral","Warm","Seller","$425,000","3-4 months","Northview","2024-01-11","2024-01-18","Home needs minor updates","Sarah Mitchell"],
        ["L003","Robert Martinez","(555) 456-7890","rmartinez@email.com","Open House","Hot","Buyer","$280,000-$320,000","1-2 months","Eastside","2024-01-12","2024-01-15","First-time buyer, needs guidance","Sarah Mitchell"],
        ["L004","Amanda Wilson","(555) 567-8901","awilson@email.com","Social Media","Warm","Buyer","$500,000+","4-6 months","Luxury District","2024-01-13","2024-01-20","Looking for executive home","Sarah Mitchell"],
        ["L005","James Thompson","(555) 678-9012","jthompson@email.com","SOI","Hot","Seller","$695,000","Immediate","Premium Heights","2024-01-14","2024-01-16","Divorce situation, urgent","Sarah Mitchell"],
        ["L006","Lisa Anderson","(555) 789-0123","landerson@email.com","Website","Cold","Buyer","$200,000-$250,000","6+ months","Affordable Acres","2024-01-15","2024-02-15","Just browsing, not ready yet","Sarah Mitchell"],
        ["L007","David Garcia","(555) 890-1234","dgarcia@email.com","Zillow","Warm","Buyer/Seller","$380,000","2-3 months","Midtown","2024-01-16","2024-01-23","Moving up, selling first","Sarah Mitchell"],
        ["L008","Nancy Rodriguez","(555) 901-2345","nrodriguez@email.com","Referral","Hot","Seller","$520,000","1 month","Lakeview","2024-01-17","2024-01-19","Ready to list next week","Sarah Mitchell"],
    ])

# CSV 2: Active Clients
write_csv(p10+"Active_Clients.csv",
    ["Client ID","Full Name","Phone","Email","Type","Status","Property Address","Price","Contract Date","Close Date","Lender","Notes"],
    [
        ["C001","Thomas Brown","(555) 112-2334","tbrown@email.com","Buyer","Under Contract","456 Maple Ave, Riverside","$412,000","2024-01-15","2024-02-15","First National Bank","20% down, conventional loan"],
        ["C002","Patricia Lee","(555) 223-3445","plee@email.com","Seller","Active Listing","789 Pine Road, Lakewood","$365,000","2024-01-10","","N/A","Listed 1/10, 3 showings scheduled"],
        ["C003","Christopher Harris","(555) 334-4556","charris@email.com","Buyer","Active Search","","$290,000-$350,000","","","Riverside Credit Union","Need 3BR, 2BA, fenced yard"],
        ["C004","Barbara Clark","(555) 445-5667","bclark@email.com","Seller","Under Contract","321 Elm Drive, Hillside","$525,000","2024-01-20","2024-02-28","","Cash offer, quick close"],
        ["C005","Kevin Lewis","(555) 556-6778","klewis@email.com","Buyer","Offer Pending","147 Willow Way","$445,000","","","Summit Mortgage","Offer submitted, waiting on response"],
        ["C006","Margaret Walker","(555) 667-7889","mwalker@email.com","Seller","Pre-Listing","987 Cedar Lane, Westport","$620,000","","","N/A","Pre-listing prep, staging consult 1/25"],
    ])

# CSV 3: Listing Inventory
write_csv(p10+"Listing_Inventory.csv",
    ["MLS #","Address","Beds","Baths","Sq Ft","List Price","Days on Market","Status","List Date","Open House","Showings","Offers","Price Reduction","Notes"],
    [
        ["MLS-2401","789 Pine Road, Lakewood","3","2","1,850","$365,000","11","Active","2024-01-10","Jan 20, 1-4pm","8","1","None","Great condition, motivated seller"],
        ["MLS-2402","987 Cedar Lane, Westport","5","3.5","3,200","$620,000","1","Active","2024-01-20","Jan 27, 2-5pm","3","0","None","Luxury finishes throughout"],
        ["MLS-2403","147 Willow Way, Eastside","4","2.5","2,100","$445,000","22","Pending","2024-01-01","None","15","3","$20,000 reduction","Multiple offers received"],
        ["MLS-2404","654 Birch Blvd, Greenview","2","1","980","$198,000","45","Active","2023-12-07","Feb 3, 1-4pm","12","1","$5,000 reduction","Investment property potential"],
        ["MLS-2405","321 Elm Drive, Hillside","4","3","2,650","$525,000","6","Under Contract","2024-01-17","None","9","2","None","Cash offer, inspections done"],
    ])

# CSV 4: Transaction Pipeline
write_csv(p10+"Transaction_Pipeline.csv",
    ["Transaction ID","Property","Client","Type","Status","Contract Price","Commission","Close Date","Lender","Title Company","Inspector","Days to Close","Notes"],
    [
        ["TXN-001","456 Maple Ave","Thomas Brown","Buyer","Active","$412,000","$10,300","2024-02-15","First National Bank","Premier Title","HomeCheck Pro","21","Appraisal ordered"],
        ["TXN-002","321 Elm Drive","Barbara Clark","Seller","Inspections","$525,000","$13,125","2024-02-28","Cash","Lakeside Title","Done","28","Inspection repair list negotiation"],
        ["TXN-003","147 Willow Way","Kevin Lewis","Buyer","Offer Pending","$445,000","$13,350","Projected 2/28","Summit Mortgage","TBD","TBD","35","Waiting seller response"],
        ["TXN-004","987 Cedar Lane","Margaret Walker","Seller","Pre-Listing","$620,000","$15,500","Projected 3/15","N/A","TBD","TBD","55","Staging in progress"],
    ])

# CSV 5: Referral Partner Database
write_csv(p10+"Referral_Partner_Database.csv",
    ["Partner ID","Name","Company","Type","Phone","Email","Referrals Sent","Referrals Received","Last Contact","Relationship Status","Notes"],
    [
        ["RP001","Alex Chen","First National Bank","Mortgage Lender","(555) 111-2222","achen@fnb.com","8","5","2024-01-12","Strong","Monthly lunch meetings"],
        ["RP002","Maria Santos","Premier Title Co","Title Company","(555) 222-3333","msantos@premiertitle.com","12","3","2024-01-08","Strong","Fast closings, reliable"],
        ["RP003","Brian Foster","HomeCheck Pro","Home Inspector","(555) 333-4444","bfoster@homecheckpro.com","15","6","2024-01-15","Strong","48hr report turnaround"],
        ["RP004","Nicole Park","Riverside Credit Union","Mortgage Lender","(555) 444-5555","npark@rcu.com","4","2","2024-01-05","Developing","Good FHA loan specialist"],
        ["RP005","Carlos Rivera","Rivera Law Group","Real Estate Attorney","(555) 555-6666","crivera@riveralaw.com","6","1","2023-12-20","Warm","Handles complex transactions"],
        ["RP006","Ashley Moore","Stageworthy Interiors","Home Stager","(555) 666-7777","amoore@stageworthy.com","10","4","2024-01-10","Strong","Makes listings sell faster"],
        ["RP007","Daniel Kim","Snap & Sell Photography","Photographer","(555) 777-8888","dkim@snapsell.com","20","8","2024-01-14","Strong","2hr turnaround, drone available"],
        ["RP008","Stephanie Wells","Clean Sweep Co","Cleaning Service","(555) 888-9999","swells@cleansweep.com","5","2","2023-12-15","Warm","Pre-listing cleaning specialist"],
    ])

# CSV 6: Open House Tracker
write_csv(p10+"Open_House_Tracker.csv",
    ["Date","Property Address","Time","Visitors","Contacts Collected","Follow Up Sent","Leads Generated","Notes"],
    [
        ["2024-01-13","789 Pine Road, Lakewood","1pm-4pm","23","18","Yes","4","Beautiful weather, great turnout"],
        ["2024-01-14","654 Birch Blvd, Greenview","2pm-5pm","14","11","Yes","2","Investor interest was high"],
        ["2024-01-20","789 Pine Road, Lakewood","1pm-4pm","19","16","Yes","3","Multiple repeat visitors"],
        ["2024-01-21","987 Cedar Lane, Westport","2pm-5pm","31","25","Yes","7","Luxury market event, wine and cheese"],
        ["2024-01-27","654 Birch Blvd, Greenview","1pm-4pm","11","9","Yes","1","Slower day, cold weather"],
        ["2024-01-28","987 Cedar Lane, Westport","2pm-5pm","27","22","Yes","5","Best open house of month"],
    ])

# CSV 7: Showing Feedback Log
write_csv(p10+"Showing_Feedback_Log.csv",
    ["Date","Property","Showing Agent","Buyer Feedback","Price Feedback","Condition","Likelihood to Offer","Notes"],
    [
        ["2024-01-11","789 Pine Road","Agent Brown","Loved the kitchen, small master bath","Fair","Good","Medium","May write offer after seeing 2 more"],
        ["2024-01-12","789 Pine Road","Agent Jones","Perfect size and location","Good","Excellent","High","Writing offer this weekend"],
        ["2024-01-13","654 Birch Blvd","Agent Garcia","Good investment bones","Fair","Needs work","Low","Looking for move-in ready"],
        ["2024-01-14","987 Cedar Lane","Agent Patel","Spectacular home, love everything","High","Excellent","High","Client pre-approved to $700k"],
        ["2024-01-15","789 Pine Road","Agent Williams","Too close to the highway","Not sure","Good","Low","Will not be writing offer"],
        ["2024-01-16","321 Elm Drive","Agent Chen","Best backyard they've seen","Good","Very Good","High","Offer coming Monday"],
    ])

# Markdown Setup Guide
md_content = """# Real Estate Agent OS — Notion Workspace Setup Guide

## Overview
This guide walks you through setting up your complete Notion workspace using the CSV database files included in this folder. Once imported, you'll have a professional CRM and transaction management system running in under 30 minutes.

## Files Included
| File | Notion Database | Purpose |
|------|----------------|---------|
| Lead_Tracker.csv | Lead Tracker | Manage all incoming leads |
| Active_Clients.csv | Active Clients | Track current buyer/seller clients |
| Listing_Inventory.csv | Listing Inventory | Monitor your active listings |
| Transaction_Pipeline.csv | Transaction Pipeline | Track deals from contract to close |
| Referral_Partner_Database.csv | Referral Partners | Manage your partner network |
| Open_House_Tracker.csv | Open Houses | Log open house events and leads |
| Showing_Feedback_Log.csv | Showing Feedback | Collect and review buyer feedback |

## Step-by-Step Import Instructions

### Step 1 — Create Your Workspace
1. Open Notion and create a new page titled "Real Estate Agent OS"
2. Add an emoji icon: 🏡
3. Set a cover photo (use a professional real estate image)

### Step 2 — Import Each Database
For each CSV file:
1. Click **+ New Page** inside your Real Estate Agent OS page
2. Select **Import** → **CSV**
3. Upload the CSV file
4. Click **Import**
5. Notion creates a Table database automatically

### Step 3 — Set Up Views
For your Lead Tracker database, add these views:
- **Table View** (default) — full data grid
- **Board View** — group by Status (Hot/Warm/Cold)
- **Calendar View** — group by Next Follow Up date
- **Gallery View** — visual contact cards

For your Transaction Pipeline:
- **Table View** — full pipeline view
- **Board View** — group by Status (Active/Pending/Closed)
- **Calendar View** — group by Close Date

### Step 4 — Link Your Databases
Connect related databases using Relation properties:
1. In **Active Clients**, add a Relation to **Transaction Pipeline**
2. In **Lead Tracker**, add a Relation to **Active Clients**
3. In **Transaction Pipeline**, add a Relation to **Referral Partner Database**

### Step 5 — Set Up Filters and Sorts
**Lead Tracker — Hot Leads View:**
- Filter: Status = Hot
- Sort: Next Follow Up (ascending)

**Transaction Pipeline — This Month's Closings:**
- Filter: Close Date = This Month
- Sort: Close Date (ascending)

## Recommended Notion Templates to Add

### Daily Agent Dashboard
Create a new page with:
- 📊 Today's appointments (linked from Active Clients)
- 🔥 Hot leads to call (linked from Lead Tracker)
- 📋 Tasks due today
- 💰 Weekly GCI tracker

### Weekly Review Template
```
## Week of [Date]

### Wins This Week
-

### Challenges
-

### Metrics
- Calls Made:
- Appointments:
- Offers Written:
- Closings:

### Top 3 Priorities Next Week
1.
2.
3.
```

## Tips for Using This System
- Update your Lead Tracker every day before you end work
- Move leads to Active Clients the moment you have a signed agreement
- Log all showing feedback within 24 hours while it's fresh
- Review your Transaction Pipeline every Monday morning

---
*Real Estate Agent Operating System | Professional Edition*
*Original Price: €149 | Your Price: €39*
"""
with open(BASE + p10 + "Notion_Workspace_Setup_Guide.md", "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"  ✓ {p10}Notion_Workspace_Setup_Guide.md")
print("✓ 10_NOTION_WORKSPACE complete")

print("\nPART 3 DONE")
