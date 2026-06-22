#!/usr/bin/env python3
"""AI SMMA OS - Part 3: Folders 07,08,09,10 + KPI_ROI_Dashboard.xlsx + Agency_Revenue_Tracker.xlsx + Notion CSVs"""
import os, csv
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment

BASE = "/home/user/oqul-phase55-production/ai-smma-os/Ultimate_AI_SMMA_Operating_System/"
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

# ─── 07_CLIENT_REPORTING ───────────────────────────────────────────────────────
p07 = "07_CLIENT_REPORTING/"

doc(p07+"Monthly_Report_Guide.docx",
    "Monthly Report Guide — How to Present Results That Retain Clients",
    "Ultimate AI SMMA OS | What to Include, How to Frame Wins, Handle Challenges, Plan Next Month",
    [
        ("Why Monthly Reports Are a Retention Tool, Not Just a Deliverable", [
            "The monthly report is not a formality — it is the most important touchpoint in your client relationship. Clients who feel informed stay. Clients who feel uncertain churn. A well-crafted monthly report builds confidence, demonstrates expertise, and creates the conversation that leads to upsells and long-term retention. Think of your report not as a document — but as a monthly meeting with your most important asset: a paying client.",
        ]),
        ("The 8 Components of an Outstanding Monthly Report", [
            "Component 1 — Executive Summary (1 paragraph):",
            ("•", "Top 3 achievements of the month, framed in business terms (not just vanity metrics)"),
            ("•", "Key challenge encountered and how you addressed it"),
            ("•", "One clear headline number (e.g., '47% increase in profile visits this month')"),
            "Component 2 — KPI Dashboard Summary:",
            ("•", "All agreed KPIs shown month-over-month with directional arrow (↑ ↓ →)"),
            ("•", "Color coding: Green for above target, Amber for on track, Red for below target"),
            ("•", "Include: Followers, Follower Growth %, Engagement Rate, Reach, Impressions, Website Clicks, Leads Generated"),
            "Component 3 — Platform Performance Breakdown:",
            ("•", "Each platform gets its own section with key metrics and observations"),
            ("•", "Highlight top-performing content from each platform with thumbnail and stats"),
            "Component 4 — Content Performance Highlights:",
            ("•", "Top 3 posts by engagement, reach, and saves — with explanations for WHY they worked"),
            ("•", "Lowest performing post and what we learned from it"),
            "Component 5 — Community Management Summary:",
            ("•", "Comments responded to, average response time, notable DM conversations"),
            ("•", "Any emerging themes in audience questions or feedback"),
            "Component 6 — Paid Advertising Results (if applicable):",
            ("•", "Spend, impressions, clicks, CTR, conversions, CPA, ROAS for each active campaign"),
            "Component 7 — Challenges and What We Did About Them:",
            ("•", "Never hide challenges — address them proactively with your solution"),
            ("•", "Frame: 'We noticed X. We believe it happened because Y. Here's what we're testing next.'"),
            "Component 8 — Next Month Strategy Preview:",
            ("•", "Content themes for next month"),
            ("•", "Any tactical changes based on this month's learnings"),
            ("•", "Any additional opportunities you want to discuss"),
        ]),
        ("How to Present Wins Without Overclaiming", [
            ("•", "Always tie metrics back to business outcomes: not 'we got 500 new followers' but 'our profile visits increased 78% — that's 500 new people who discovered [Business Name] this month'"),
            ("•", "Use comparisons: month-over-month, quarter-over-quarter, or vs. campaign benchmark"),
            ("•", "Attribution language: 'We believe the increase in website clicks is driven by the [specific content type] we introduced this month'"),
            ("•", "Be specific on top posts: 'The Tuesday reel about [topic] reached [X] non-followers — the highest discovery reach we've had in 3 months'"),
        ]),
        ("How to Handle a Bad Month", [
            "Every month won't be a home run. How you handle low-performance months defines your agency's trustworthiness.",
            ("•", "Never skip a bad month report or bury the data"),
            ("•", "Address it early in the report — not buried on page 8"),
            "Script for discussing a down month on a call:",
            '"I want to address the engagement drop head-on. This month we saw a [X]% decrease in [metric]. Based on our analysis, we believe this was driven by [algorithm update / seasonal trend / testing new format]. Here\'s exactly what we\'re changing next month and why we\'re confident it will improve."',
        ]),
        ("Report Delivery Best Practices", [
            ("•", "Delivery format: PDF is professional and prevents editing; use Google Slides for interactive presentations"),
            ("•", "Timing: Delivered within the first 5 business days of the following month"),
            ("•", "Presentation: Walk the client through the report on a call — never just email and hope they read it"),
            ("•", "Length: 8-12 pages for a well-designed PDF; comprehensive without being overwhelming"),
            ("•", "Frequency: Monthly minimum; weekly updates (via email or Loom video) for Elite clients"),
        ]),
    ])

doc(p07+"Weekly_Update_Script.docx",
    "Weekly Update Script — 15-Minute Call + Email Alternative",
    "Ultimate AI SMMA OS | Client Communication Between Monthly Reports",
    [
        ("Why Weekly Updates Matter", [
            "Elite and Pro clients expect to hear from you more than once a month. Weekly updates build the 'always on top of it' perception that justifies premium retainer pricing. They also give you the opportunity to identify and address any concerns before they become churn risks. This script covers both the 15-minute call format and the email-only alternative for clients who prefer less contact.",
        ]),
        ("15-Minute Weekly Call Structure", [
            "Part 1 — This Week's Highlights (3-4 Minutes):",
            '"Hi [Name], good to connect! Here are the highlights from this week: [Top 2-3 performance points]. The standout was [best piece of content or metric] — here\'s why I think that worked particularly well: [brief explanation]."',
            "Part 2 — What We're Watching (2-3 Minutes):",
            '"A couple of things on my radar for the coming week: [trend or platform change relevant to their niche]. We\'re planning to test [specific approach] to capitalize on it. I also want to flag [one challenge] — it\'s not a problem yet but I\'m watching it closely."',
            "Part 3 — What\'s Coming Next Week (3-4 Minutes):",
            '"Next week we have [content scheduled]. The main focus is [strategic objective for the week]. I'll send the content for your approval by [date] — as usual, please review within 48 hours so we can stay on schedule."',
            "Part 4 — Any Questions from the Client (3-4 Minutes):",
            '"Before we wrap up — do you have any upcoming events, promotions, or news we should know about for next week's content? And any questions on anything we covered today?"',
        ]),
        ("Weekly Email Update Template", [
            "Subject: [Client Name] — Weekly Social Media Update [Week of DD/MM]",
            "Hi [Name],",
            "Here's your quick social media update for the week:",
            "THIS WEEK'S HIGHLIGHTS:",
            "• [Platform]: [Metric] — [brief insight]",
            "• Best performing post: [Description] — [Key stat]",
            "• [Any community management highlights]",
            "WHAT WE'RE TRACKING:",
            "• [One trend or challenge with brief explanation]",
            "NEXT WEEK:",
            "• Content calendar for [dates] coming for your approval by [date]",
            "• [Any upcoming content or strategic focus]",
            "Anything on your end we should know about for next week's content? Promotions, events, news?",
            "[Your Name]",
        ]),
        ("Weekly Update Frequency by Package", [
            ("•", "Starter Package: Email update only, 2x per month (every 2 weeks)"),
            ("•", "Growth Package: Weekly email update, monthly call"),
            ("•", "Pro Package: Weekly email + bi-weekly 15-minute call"),
            ("•", "Elite Package: Weekly email + weekly 15-minute call + monthly strategy session"),
        ]),
    ])

doc(p07+"Reporting_SOP.docx",
    "Reporting SOP — Data Collection, Tool Integration, and Report Delivery",
    "Ultimate AI SMMA OS | End-to-End Reporting Process for SMMA Agencies",
    [
        ("Why a Reporting SOP Saves Hours Every Month", [
            "Without a documented reporting process, compiling each monthly report is a 4-6 hour task. With a standardized SOP, it takes 60-90 minutes. This SOP defines exactly what data to collect, where to find it, how to enter it, and how to deliver the final report. Run this process in the first 3 business days of every month.",
        ]),
        ("Step 1 — Data Collection (Day 1 of Reporting Cycle)", [
            "Instagram Data (via Instagram Insights or Meta Business Suite):",
            ("•", "Account Insights > Overview: Total Reach, Impressions, Profile Visits, Follower Count, Net Follower Change"),
            ("•", "Content Performance: Sort by engagement — capture Top 3 posts (screenshot + export stats)"),
            ("•", "Audience Insights: Top locations, age/gender breakdown (for audience alignment reporting)"),
            "Facebook Data (via Meta Business Suite):",
            ("•", "Page Summary: Reach, Impressions, Engagement, Follower Change"),
            ("•", "Content: Post-by-post performance for the reporting month"),
            "LinkedIn Data (via LinkedIn Analytics):",
            ("•", "Visitors: Unique visitors, page views, follower change"),
            ("•", "Content: Impressions, clicks, reactions, CTR for each post"),
            "TikTok Data (via TikTok Analytics):",
            ("•", "Overview: Views, Followers, Profile Views, Likes"),
            ("•", "Content: View count, average watch time, shares for each video"),
            "Website Data (via Google Analytics 4):",
            ("•", "Traffic from social media (Source/Medium report)"),
            ("•", "Conversions attributed to social media"),
        ]),
        ("Step 2 — Data Entry (Day 1-2)", [
            ("•", "Enter all data into KPI_ROI_Dashboard.xlsx for the relevant client and month"),
            ("•", "Calculate month-over-month change for each metric"),
            ("•", "Identify top 3 posts by each metric category (engagement, reach, saves)"),
            ("•", "Calculate ROI if client has provided revenue or lead data"),
        ]),
        ("Step 3 — Report Creation (Day 2-3)", [
            ("•", "Open Monthly_Client_Report.pptx template in Canva or PowerPoint"),
            ("•", "Update all metrics from the KPI dashboard"),
            ("•", "Insert top post screenshots with caption and stats"),
            ("•", "Write executive summary using Monthly_Report_Guide.docx structure"),
            ("•", "Write next month preview based on approved content calendar"),
            ("•", "Internal review: Check all numbers match source data, no typos"),
        ]),
        ("Step 4 — Report Delivery (Day 3-5)", [
            ("•", "Export as PDF for email delivery"),
            ("•", "Email report with subject: '[Client Name] — [Month] Social Media Performance Report'"),
            ("•", "Send calendar invite for report walkthrough call (30 minutes)"),
            ("•", "On the call: Walk through each section, ask if they have questions, confirm next month priorities"),
        ]),
        ("Reporting Tools and Integrations", [
            ("•", "Social Media Analytics: Native platform insights (free) or Sprout Social / Hootsuite Analytics (paid)"),
            ("•", "Reporting Templates: Monthly_Client_Report.pptx (this kit) + KPI_ROI_Dashboard.xlsx"),
            ("•", "Screen Recording: Loom for video walkthroughs if no call scheduled"),
            ("•", "PDF Creation: Canva Pro, Adobe Acrobat, or export from Google Slides"),
            ("•", "Report Storage: Share via Google Drive or Dropbox — client keeps their own reporting history"),
        ]),
    ])

# KPI_ROI_Dashboard XLSX
wb = Workbook()
ws1 = wb.active
ws1.title = "KPI Tracker"
kpi_headers = ["Client","Month","Followers","Follower Growth %","Avg Engagement Rate",
               "Total Reach","Impressions","Website Clicks","Leads Generated",
               "Revenue Attributed (€)","Target Met?","Agency Notes"]
ws1.append(kpi_headers)
for cell in ws1[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=10)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

kpi_data = [
    ["Bella Vita Restaurant","January 2025","4,892","8.2%","3.4%","28,400","94,200","342","18","3,200","YES","Strong month — Reel on pasta recipe went viral in local area"],
    ["Bella Vita Restaurant","February 2025","5,340","9.2%","3.8%","34,100","112,000","428","24","4,100","YES","Valentine's campaign very successful, best engagement month yet"],
    ["FitLife Coaching","January 2025","8,220","5.1%","4.2%","42,800","135,000","891","31","8,500","YES","January always strong for fitness — challenge campaign worked well"],
    ["Luxe Aesthetics Clinic","January 2025","2,890","3.4%","5.8%","18,200","56,400","218","9","6,300","YES","Highest engagement rate in niche — storytelling content driving leads"],
    ["TechFlow SaaS","January 2025","1,240","2.1%","3.1%","12,400","38,200","1,240","42","22,000","YES","LinkedIn driving most B2B leads — 42 MQL from social in January"],
    ["Green Harvest Ecom","January 2025","11,820","6.8%","2.9%","58,400","198,000","2,840","68","14,200","YES","TikTok driving highest traffic — UGC campaign performed above expectations"],
]
for i, row in enumerate(kpi_data):
    ws1.append(row)
    for cell in ws1[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",22),("B",16),("C",12),("D",18),("E",20),("F",14),("G",14),("H",16),("I",18),("J",22),("K",14),("L",38)]:
    ws1.column_dimensions[col].width = w

# ROI Calculator Sheet
ws2 = wb.create_sheet("ROI Calculator")
ws2.append(["SMMA ROI Calculator — Show Clients Their Return"])
ws2["A1"].font = Font(bold=True, size=14, color=NAV)
ws2.append([""])
ws2.append(["CLIENT ROI INPUTS","Value"])
for cell in ws2[3]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center")

roi_inputs = [
    ["Monthly Retainer Paid to Agency (€)","1500"],
    ["Leads Generated from Social Media (this month)","18"],
    ["Client's Average Close Rate (%)","25%"],
    ["Client's Average Sale Value (€)","450"],
    ["Number of New Clients Closed from Social Leads","4"],
    ["Total Revenue from Social Leads (€)","=B7*B8"],
    ["",""],
    ["ROI OUTPUTS","Calculation"],
    ["Gross Revenue from Social Media (€)","=B9"],
    ["Agency Fee (€)","=B4"],
    ["Net Profit from Social Leads (€)","=B12-B13"],
    ["Return on Investment (%)","=(B12-B13)/B13*100"],
    ["For every €1 spent on agency, client earned (€)","=B12/B13"],
    ["Annual Projection at this rate (€)","=B12*12"],
    ["Annual Agency Spend (€)","=B13*12"],
    ["Annual Net ROI (€)","=B16-B17"],
]
for i, row in enumerate(roi_inputs):
    ws2.append(row)
    if row[0] in ["ROI OUTPUTS"]:
        for cell in ws2[i+4]:
            cell.fill = PatternFill("solid", fgColor=NAV)
            cell.font = Font(bold=True, color=WHT)
    elif "€" in row[0] or "%" in row[0] or row[0].startswith("For") or row[0].startswith("Annual") or row[0].startswith("Return") or row[0].startswith("Net") or row[0].startswith("Gross"):
        for cell in ws2[i+4]:
            cell.fill = PatternFill("solid", fgColor="E8F5E9")
            cell.font = Font(bold=True, color="27AE60")
    elif row[0]:
        for cell in ws2[i+4]:
            cell.fill = PatternFill("solid", fgColor=LGR)

for col, w in [("A",45),("B",20)]:
    ws2.column_dimensions[col].width = w

# Client Performance Sheet
ws3 = wb.create_sheet("Client Performance")
cp_headers = ["Client","Package","MRR (€)","Jan Followers","Jan Engagement%","Jan Leads",
              "Feb Followers","Feb Engagement%","Feb Leads","Trend","3-Month Target","On Track?"]
ws3.append(cp_headers)
for cell in ws3[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=10)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

cp_data = [
    ["Bella Vita Restaurant","Growth","1500","4,892","3.4%","18","5,340","3.8%","24","↑ Improving","6,000 followers, 4% eng, 30 leads","YES"],
    ["FitLife Coaching","Pro","3000","8,220","4.2%","31","8,890","4.6%","38","↑ Improving","10,000 followers, 5% eng, 50 leads","YES"],
    ["Luxe Aesthetics Clinic","Elite","5000","2,890","5.8%","9","3,100","6.1%","11","↑ Improving","4,000 followers, 6%+ eng, 15 leads","YES"],
    ["TechFlow SaaS","Pro","3000","1,240","3.1%","42","1,380","3.4%","48","↑ Improving","2,000 followers, 4% eng, 60 MQL","YES"],
    ["Green Harvest Ecom","Elite","5000","11,820","2.9%","68","12,400","3.1%","74","↑ Improving","15,000 followers, 3.5% eng, 100 leads","YES"],
    ["Bloom Wedding Co.","Starter","500","1,820","2.1%","4","1,940","2.2%","5","→ Steady","2,500 followers, 3% eng, 8 leads","BORDERLINE"],
]
for i, row in enumerate(cp_data):
    ws3.append(row)
    for cell in ws3[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(horizontal="center", wrap_text=True)

for col, w in [("A",22),("B",12),("C",10),("D",14),("E",16),("F",12),("G",14),("H",16),("I",12),("J",14),("K",35),("L",12)]:
    ws3.column_dimensions[col].width = w

wb.save(BASE + p07 + "KPI_ROI_Dashboard.xlsx")
print(f"  ✓ {p07}KPI_ROI_Dashboard.xlsx")
print("✓ 07_CLIENT_REPORTING complete")

# ─── 08_AI_TOOLS_STACK ─────────────────────────────────────────────────────────
p08 = "08_AI_TOOLS_STACK/"

doc(p08+"AI_Tools_Guide_for_SMMA.docx",
    "AI Tools Guide for SMMA — Complete Stack Overview",
    "Ultimate AI SMMA OS | ChatGPT, Claude, Midjourney, Canva AI, and More",
    [
        ("The AI-Powered SMMA: Your Competitive Advantage", [
            "AI tools have fundamentally changed what's possible for a solo operator or small agency. Tasks that once required a team of 5 — content ideation, caption writing, graphic design, video editing, email writing — can now be done by one person with the right AI stack. This guide covers every essential AI tool for SMMA owners, including specific use cases, pricing, and how to integrate them into your workflow.",
        ]),
        ("ChatGPT (GPT-4 / GPT-4o)", [
            "Best For: Caption writing, content ideation, strategy planning, email templates, objection handling responses",
            "Pricing: Free (GPT-3.5) | $20/month for Plus (GPT-4) | $25/month for Team",
            "SMMA Use Cases:",
            ("•", "Monthly content calendar generation (use CI-1 prompt from AI_Prompt_Library.docx)"),
            ("•", "Caption writing using AIDA, PAS, and storytelling frameworks"),
            ("•", "Client proposal drafts (then customize manually)"),
            ("•", "Discovery call preparation — generate questions based on client niche"),
            ("•", "Monthly report executive summaries"),
            "Power Tip: Create custom GPTs for your most common client niches. A 'Restaurant Social Media GPT' with your client's menu, voice guide, and posting rules saves hours of prompting every month.",
        ]),
        ("Claude (Anthropic)", [
            "Best For: Long-form content, nuanced writing, contracts, SOPs, complex strategy documents",
            "Pricing: Free (Claude.ai) | $20/month for Pro | API pricing for integration",
            "SMMA Use Cases:",
            ("•", "Writing and reviewing contract templates and SOPs"),
            ("•", "Long-form LinkedIn articles and thought leadership pieces"),
            ("•", "Nuanced client communication (sensitive situations, complaint responses)"),
            ("•", "Research and competitor analysis summaries"),
            ("•", "Complex content strategy documents"),
            "Power Tip: Claude excels at maintaining a consistent brand voice over a long document. Paste your client's brand voice guide at the top of your prompt and every piece of content will feel on-brand.",
        ]),
        ("Midjourney / DALL-E 3 / Adobe Firefly", [
            "Best For: Custom social media graphics, concept images, product mockups, lifestyle visuals",
            "Pricing: Midjourney from $10/month | DALL-E via ChatGPT Plus | Firefly via Adobe Creative Cloud",
            "SMMA Use Cases:",
            ("•", "Custom lifestyle imagery when clients don't have photography budgets"),
            ("•", "Concept visualization for content pitches to clients"),
            ("•", "Unique graphic elements for branded content"),
            ("•", "Ad creative concepting"),
            "Power Tip: Generate 10 variations of a concept image and let the client pick their favorite — this removes the 'I don't know what I want' problem from creative briefing.",
        ]),
        ("Canva AI (Magic Studio)", [
            "Best For: Professional social media graphics, carousels, presentations, video clips",
            "Pricing: Free | Canva Pro $15/month (recommended for agencies)",
            "SMMA Use Cases:",
            ("•", "All platform-sized social media graphics — templates save hours per month"),
            ("•", "Magic Write for caption suggestions within Canva"),
            ("•", "Magic Design: Upload an image and get 8 design options instantly"),
            ("•", "Brand Kit: Store client colors, fonts, and logos for instant on-brand creation"),
            ("•", "Video editing: Simple Reels/TikTok videos with text, music, and transitions"),
            "Power Tip: Create a separate Canva workspace per client. Within each workspace, set up the brand kit so any designer or freelancer immediately has the correct brand assets.",
        ]),
        ("Kling AI / Runway ML / Pika Labs (Video AI)", [
            "Best For: AI-generated video clips, video enhancement, text-to-video content for Reels and TikTok",
            "Pricing: Kling from $8/month | Runway from $15/month | Pika free beta",
            "SMMA Use Cases:",
            ("•", "Generate B-roll footage for Reels when clients don't have video content"),
            ("•", "Create animated versions of static product images for ads"),
            ("•", "Video enhancement and stabilization for client-provided footage"),
            "Power Tip: Use AI video for background B-roll while the client's voiceover or on-camera footage plays in the foreground — adds production value without a budget.",
        ]),
        ("ElevenLabs (AI Voice)", [
            "Best For: Voiceovers for Reels, TikToks, YouTube Shorts, and ad video",
            "Pricing: Free (limited) | $5-$22/month for Starter/Creator",
            "SMMA Use Cases:",
            ("•", "Add professional voiceovers to Reels without the client needing to record"),
            ("•", "Create consistent voice branding for clients who don't want to be on camera"),
            ("•", "Narrate case study or explainer videos"),
            "Power Tip: Clone a client's voice (with permission) using ElevenLabs Voice Cloning — they speak for 3 minutes, and you can generate voiceovers in their voice for months.",
        ]),
        ("Copy.ai / Jasper (Specialized AI Writing)", [
            "Best For: Rapid content variation generation, A/B testing ad copy, email marketing sequences",
            "Pricing: Copy.ai from $36/month | Jasper from $49/month",
            "SMMA Use Cases:",
            ("•", "Generate 10 versions of the same headline for A/B testing"),
            ("•", "Build email marketing sequences for clients who also want email newsletters"),
            ("•", "Create multiple variations of ad copy for campaign testing"),
            "Power Tip: Use Copy.ai's workflow templates to create end-to-end content briefs — they have specific templates for social media captions, email sequences, and ad copy that are faster than writing prompts from scratch.",
        ]),
    ])

doc(p08+"ChatGPT_Workflow_SOPs.docx",
    "ChatGPT Workflow SOPs — 10 Complete SMMA Workflows",
    "Ultimate AI SMMA OS | Step-by-Step ChatGPT Processes for Every Agency Task",
    [
        ("How to Use These Workflow SOPs", [
            "Each workflow is a documented process that combines multiple ChatGPT prompts into a complete end-to-end task. Follow each workflow in order. The output of one prompt often feeds into the next. These workflows are designed to take a task that normally requires 2-3 hours and compress it into 30-45 minutes without sacrificing quality.",
        ]),
        ("Workflow 1 — Monthly Content Planning (45 Minutes)", [
            "What This Produces: A complete 30-day content calendar with topics, hooks, and CTA for all client platforms",
            "Step 1 — Client Context Prompt:",
            '"I run a social media agency managing [CLIENT NAME], a [NICHE] business targeting [AUDIENCE DESCRIPTION]. Their 5 content pillars are: [LIST PILLARS]. This month\'s theme is [THEME]. They post on [PLATFORMS] at a frequency of [FREQUENCY]. Please remember this context for all prompts in this session."',
            "Step 2 — Calendar Framework:",
            '"Based on the client context, create a 30-day content calendar for [MONTH]. For each day with a post, provide: Date | Platform | Post Type | Topic/Hook | Primary Pillar. Use a table format. Ensure variety in post types and platforms."',
            "Step 3 — Hook Refinement:",
            '"For the 5 Reel/TikTok entries in the calendar, generate 3 alternative hooks for each. I will choose the best one for each video."',
            "Step 4 — Caption Draft:",
            '"Write full captions for the first 8 posts in the calendar. For each: hook, body (3-4 paragraphs), CTA. Use the brand voice: [VOICE]. Hashtag placeholder: [HASHTAGS]."',
            "Output: Export conversation as PDF, save as [CLIENT]_Content_Plan_[MONTH].pdf",
        ]),
        ("Workflow 2 — Caption Writing Batch (30 Minutes)", [
            "What This Produces: 10 complete captions for a client's content batch",
            "Step 1 — Set Context: [Client name, niche, brand voice, target audience]",
            "Step 2 — Format Prompts: Request AIDA, PAS, and Story-format captions (3-4 each)",
            "Step 3 — Hook Testing: For each caption, ask for 3 alternative hooks. Rate them 1-10.",
            "Step 4 — CTA Variation: Generate 5 different CTA options for this content batch.",
            "Step 5 — Final Polish: 'Review all 10 captions and flag any that feel off-brand or that repeat themselves.'",
        ]),
        ("Workflow 3 — Discovery Call Preparation (20 Minutes)", [
            "What This Produces: Custom discovery call questions and pitch points for a specific prospect",
            "Step 1 — Prospect Research Prompt:",
            '"I have a discovery call with [PROSPECT BUSINESS], a [NICHE] business in [LOCATION]. Their social media currently shows: [describe what you observed — follower count, content type, engagement]. Their website suggests: [brief observation]. Please help me prepare."',
            "Step 2 — Pain Point Questions:",
            '"Generate 10 discovery questions specific to this prospect that will reveal their biggest social media challenges. Questions should be open-ended and build toward revealing that they need our services."',
            "Step 3 — Custom Value Props:",
            '"Based on what you know about this prospect, what 3 specific value propositions should I emphasize in my pitch? Give me the exact language to use."',
            "Step 4 — Objection Anticipation:",
            '"Based on this type of business, what are the 3 most likely objections I\'ll face? Give me a response to each."',
        ]),
        ("Workflow 4 — Monthly Report Writing (40 Minutes)", [
            "What This Produces: Complete executive summary and narrative for monthly client report",
            "Step 1 — Metrics Input: Paste all your performance metrics for the month",
            "Step 2 — Executive Summary: 'Write a 3-paragraph executive summary for our monthly social media report. Month: [MONTH]. Metrics: [PASTE]. Client goal: [GOAL]. Tone: confident and forward-looking.'",
            "Step 3 — Performance Narrative: 'Explain why [TOP POST] performed so well in plain language the client can understand.'",
            "Step 4 — Challenge Framing: 'Frame this challenge professionally: [DESCRIBE UNDERPERFORMANCE]. Explain why it happened and what we're doing differently next month.'",
            "Step 5 — Next Month Preview: 'Write a compelling 1-page preview of next month's strategy including content themes, key tactical changes, and expected outcomes.'",
        ]),
        ("Workflow 5 — Client Email Writing (15 Minutes)", [
            "What This Produces: Professional client emails for any situation",
            "Prompt A — Proposal Follow-Up: 'Write a follow-up email to [CLIENT] who received our proposal 3 days ago and hasn't responded. [Context]. Keep under 100 words. Be warm, not pushy.'",
            "Prompt B — Contract Renewal: 'Write a contract renewal email for [CLIENT] whose 6-month contract ends in 30 days. Include: acknowledgment of results achieved, proposal for renewal, any new additions, and an invitation to discuss. Tone: confident and grateful.'",
            "Prompt C — Bad News Delivery: 'Help me write a professional email telling [CLIENT] that their [engagement/reach/results] was lower than expected this month. Be honest, explain what we believe caused it, and clearly outline our plan to improve.'",
        ]),
        ("Workflow 6 — Ad Copy Creation (30 Minutes)", [
            "What This Produces: 5 complete Facebook/Instagram ad copy sets ready for testing",
            "Step 1: Set up ad context — product/service, audience, objective, unique selling point",
            "Step 2: Generate 5 headlines (max 40 characters each) targeting 5 different emotional angles",
            "Step 3: Write primary text for the top 3 headlines (hook + body + CTA, max 125 words each)",
            "Step 4: Create 3 retargeting versions (for people who visited but didn't convert)",
            "Step 5: Generate 5 short CTA button text options and rank them for expected CTR",
        ]),
        ("Workflow 7 — Hashtag Research (20 Minutes)", [
            "What This Produces: A 50-hashtag bank for a specific niche, organized by tier",
            "Prompt: 'I need a hashtag bank for [CLIENT NICHE] content on Instagram. Create 50 hashtags organized into 4 tiers: 5 Mega (1M+ posts), 15 Macro (100K-1M), 20 Mid-range (10K-100K), 10 Niche (under 10K). For each hashtag, give the approximate post count and a note on its best use. Present in a table: Hashtag | Tier | Est. Posts | Best For.'",
        ]),
        ("Workflow 8 — Onboarding Questionnaire Analysis (20 Minutes)", [
            "What This Produces: A strategy brief based on a completed client questionnaire",
            "Step 1: Paste the completed questionnaire responses",
            "Prompt: 'Based on this questionnaire, create: (1) A 5-word brand voice summary, (2) 5 content pillars with 1-sentence descriptions, (3) Top 3 platform recommendations with rationale, (4) 3 content formats to prioritize, (5) 3 specific campaign ideas for Month 1.'",
        ]),
        ("Workflow 9 — Team Briefing Creation (15 Minutes)", [
            "What This Produces: A complete brief for a freelancer designer or video editor",
            "Prompt: 'Create a content brief for a freelance Canva designer working on [CLIENT NAME]. Brand info: [paste from questionnaire]. This month's batch: [list post types and topics]. Include: brand guidelines summary, dos and don'ts, platform specs for each post type, content references or style examples to follow, revision process and deadline.'",
        ]),
        ("Workflow 10 — Crisis Response Planning (10 Minutes)", [
            "What This Produces: A ready-to-use crisis response script",
            "Prompt: 'My client [CLIENT NAME] is facing this social media situation: [DESCRIBE CRISIS]. Help me: (1) Write an immediate public response (under 3 sentences — acknowledge, empathize, redirect to DM), (2) Write a detailed DM response for the affected party, (3) Suggest whether to pause content (yes/no and why), (4) Draft a 24-hour follow-up post to restore positive sentiment.'",
        ]),
    ])

doc(p08+"AI_Content_Production_SOP.docx",
    "AI Content Production SOP — Human + AI Hybrid Workflow",
    "Ultimate AI SMMA OS | 5x Your Content Output Without Sacrificing Quality",
    [
        ("The AI Content Production Philosophy", [
            "AI does not replace your agency's value — it amplifies it. The value you bring is strategy, client relationships, quality control, and brand understanding. AI handles the time-consuming production work: first drafts, variations, research, and formatting. This hybrid model allows a one-person agency to serve 8-12 clients simultaneously, or a small team to serve 25+.",
        ]),
        ("The 3-Layer Human-AI Hybrid Model", [
            "Layer 1 — AI-Led (80% of time savings):",
            ("•", "First draft captions using AI_Prompt_Library.docx prompts"),
            ("•", "Content ideas and hook variations"),
            ("•", "Email drafts and report sections"),
            ("•", "Research and competitor analysis"),
            "Layer 2 — Human Refinement (15% of time):",
            ("•", "Edit AI output for brand voice accuracy"),
            ("•", "Add specific client details, product names, offers, local references"),
            ("•", "Remove anything that sounds generic or off-brand"),
            ("•", "Ensure cultural sensitivity and tone appropriateness"),
            "Layer 3 — Human Strategy (5% of time):",
            ("•", "Direction-setting and strategic decisions"),
            ("•", "Client relationship management"),
            ("•", "Quality approval before delivery"),
            ("•", "Creative direction for high-impact content"),
        ]),
        ("Monthly Content Production Schedule", [
            "Day 1-2: Content brief creation (human) + AI ideation session",
            "Day 3-4: AI caption drafting using AI_Prompt_Library.docx (30-45 min per client)",
            "Day 4-5: Human editing pass — refine, personalize, quality check",
            "Day 5-6: Design phase in Canva — use templates + AI Magic Design where applicable",
            "Day 7-8: Internal review against quality checklist",
            "Day 8-10: Client review",
            "Day 11-12: Revisions and final approval",
            "Day 12-15: Scheduling",
        ]),
        ("AI Tool Stack by Task", [
            ("•", "Caption Writing: ChatGPT / Claude — use AI_Prompt_Library.docx prompts"),
            ("•", "Content Ideas: ChatGPT (broader brainstorming) or Claude (more nuanced industry content)"),
            ("•", "Graphic Design: Canva Pro with AI tools (Magic Design, Magic Write, background remover)"),
            ("•", "Image Generation: Midjourney or DALL-E 3 for custom visuals when photography unavailable"),
            ("•", "Video Content: Kling AI / Runway for B-roll, ElevenLabs for voiceover"),
            ("•", "Email Writing: ChatGPT with your custom client context template"),
            ("•", "Report Writing: ChatGPT / Claude for executive summaries and narrative sections"),
        ]),
        ("Quality Assurance in AI-Assisted Production", [
            "The most common mistake with AI content: sending it directly to clients without editing. AI output is always a starting point, never a final product. These quality checks must happen before every client delivery:",
            ("•", "Brand Voice Check: Does every caption sound like THIS client? Not a generic brand?"),
            ("•", "Factual Accuracy: Are all statistics, product details, and claims accurate?"),
            ("•", "Tone Consistency: Is the tone consistent across all posts in the batch?"),
            ("•", "Human Feel: Does any caption read as obviously AI-generated? (Remove clichés, add specificity)"),
            ("•", "CTA Quality: Is the call-to-action specific and compelling, not generic ('link in bio' alone is not enough)"),
        ]),
    ])

doc(p08+"Midjourney_Prompt_Pack.docx",
    "Midjourney Prompt Pack — 60 Social Media Image Prompts",
    "Ultimate AI SMMA OS | Professional AI Image Prompts Organized by Niche and Style",
    [
        ("How to Use Midjourney for SMMA Clients", [
            "Midjourney generates stunning images from text prompts. For SMMA agencies, it solves the #1 content problem: most clients don't have enough photography to post consistently. These 60 prompts are organized by niche and style. Always add your client's brand colors or style description to the prompt for better results.",
            "Basic Structure: [Subject] + [Setting/Context] + [Mood/Lighting] + [Style] + [Technical specs]",
            "Always add: --ar 1:1 (for Instagram) or --ar 9:16 (for Stories/Reels/TikTok) or --ar 4:5 (for portrait feed posts)",
        ]),
        ("Restaurant and Food & Beverage Prompts", [
            "MJ-01: 'A perfectly styled bowl of pasta with fresh basil, rustic wooden table, warm golden hour lighting, shallow depth of field, food photography style, professional DSLR, --ar 1:1 --style raw'",
            "MJ-02: 'Modern restaurant interior with soft ambient lighting, empty tables set for dinner service, warm and inviting atmosphere, architectural photography, --ar 4:5'",
            "MJ-03: 'Chef hands plating a sophisticated dish in a professional kitchen, motion blur on hands, documentary photography style, editorial, --ar 4:5'",
            "MJ-04: 'Artisan coffee latte art in a white ceramic cup, marble background, minimalist food photography, top-down flat lay, --ar 1:1'",
            "MJ-05: 'Family dining at an outdoor restaurant patio, golden hour, candid lifestyle photography, warm colors, genuine smiles, no posed look, --ar 4:5'",
            "MJ-06: 'Ingredients laid out on a stone countertop for meal preparation, hero ingredients highlighted, editorial food photography, natural daylight, --ar 1:1'",
            "MJ-07: 'Street food vendor at a night market, vibrant neon lights reflecting on wet pavement, documentary street photography, cinematic, --ar 9:16'",
            "MJ-08: 'Close-up of a stack of handcrafted chocolate truffles with cocoa powder dusting, studio lighting, luxury confectionery product photography, --ar 1:1'",
        ]),
        ("Fitness and Wellness Prompts", [
            "MJ-09: 'Athletic woman doing yoga at sunrise on a rooftop, city skyline behind, soft morning light, inspirational lifestyle photography, --ar 4:5'",
            "MJ-10: 'Personal trainer coaching a client in a modern gym, motivating gesture, both smiling, authentic candid feel, warm tone, --ar 4:5'",
            "MJ-11: 'Healthy meal prep containers arranged in rainbow of colors, clean white marble counter, minimal flat lay, nutrition photography, --ar 1:1'",
            "MJ-12: 'Runner in motion on an urban trail at dawn, motion blur on legs, golden light breaking through trees, sports photography, --ar 9:16'",
            "MJ-13: 'Before and after style split image concept for fitness transformation, left: dark moody starting point, right: bright energetic transformation, --ar 1:1'",
            "MJ-14: 'Meditation space with candles, plants, yoga mat, and morning light through window, mindfulness aesthetic, clean and minimal, --ar 4:5'",
        ]),
        ("Business Coaching and Consulting Prompts", [
            "MJ-15: 'Professional woman in modern office, confident posture, looking at camera, soft window light, editorial business portrait, clean background, --ar 4:5'",
            "MJ-16: 'Overhead view of a strategy planning session, notebooks, coffee, and laptop on clean desk, productive aesthetic, flat lay, --ar 1:1'",
            "MJ-17: 'Split scene graphic concept: left side shows stress and chaos of old way, right side shows calm success of new way, illustrative graphic style, --ar 1:1'",
            "MJ-18: 'Team collaboration in a bright modern co-working space, diverse group of professionals, candid working moment, natural light, --ar 4:5'",
            "MJ-19: 'Abstract representation of growth — an upward trending graph made of growing green plants, conceptual art style, business metaphor, --ar 1:1'",
            "MJ-20: 'Close up of hands writing in a premium leather journal, blurred laptop in background, entrepreneurial aesthetic, warm film photography, --ar 4:5'",
        ]),
        ("Real Estate Prompts", [
            "MJ-21: 'Luxury modern home exterior at dusk with interior lights glowing, architecture photography, dramatic sky, wide angle lens, --ar 4:5'",
            "MJ-22: 'Real estate agent shaking hands with a happy couple in front of a newly purchased home, celebratory moment, candid photography, --ar 4:5'",
            "MJ-23: 'Minimalist interior living room with natural light, designer furniture, neutral tones, architectural photography, aspirational lifestyle, --ar 1:1'",
            "MJ-24: 'Aerial drone view of a beautiful residential neighborhood at golden hour, birds-eye perspective, lifestyle real estate, --ar 1:1'",
            "MJ-25: 'Modern kitchen with marble countertops, pendant lighting, and a view of the garden, real estate photography, bright and airy, --ar 4:5'",
        ]),
        ("E-Commerce and Product Prompts", [
            "MJ-26: 'Luxury skincare product on a white marble surface with fresh flowers, product photography, soft diffused light, lifestyle beauty, --ar 1:1'",
            "MJ-27: 'Fashion flat lay: curated outfit on white linen background, pastel accessories arranged aesthetically, editorial style photography, --ar 1:1'",
            "MJ-28: 'Person holding a product package while in a sunlit kitchen, lifestyle product photography, authentic moment, warm filter, --ar 4:5'",
            "MJ-29: 'Multiple product variations arranged in a gradient color pattern, product showcase, clean white background, commercial photography, --ar 1:1'",
            "MJ-30: 'Unboxing moment: hands opening a beautifully packaged box, tissue paper, branded card, premium unboxing experience photography, --ar 4:5'",
        ]),
        ("Abstract and Conceptual Designs for Any Niche", [
            "MJ-31: 'Geometric gradient background in [CLIENT BRAND COLORS], modern and minimal, suitable for text overlay, professional branded graphic, --ar 1:1'",
            "MJ-32: 'Abstract wave pattern in navy blue and gold, premium brand texture, suitable as social media graphic background, --ar 4:5'",
            "MJ-33: 'Split-tone gradient from dark navy to warm gold, professional brand aesthetic, text-overlay ready, clean and modern, --ar 1:1'",
            "MJ-34: 'Bokeh light background in warm tones, shallow depth of field, ideal for motivational quote graphic overlay, --ar 4:5'",
            "MJ-35: 'Dark textured background with subtle gold grain, luxury brand aesthetic, premium feel, text-overlay ready, --ar 1:1'",
        ]),
        ("Prompt Engineering Tips for Better Results", [
            ("•", "Lighting: 'golden hour', 'soft diffused light', 'dramatic side lighting', 'editorial lighting' — specific lighting dramatically improves quality"),
            ("•", "Photography Style: 'documentary', 'editorial', 'lifestyle photography', 'product photography' — tells Midjourney the genre"),
            ("•", "Brand Colors: 'in the color palette of [hex] and [hex]' — works in v6+"),
            ("•", "Mood: 'warm and inviting', 'professional and clean', 'vibrant and energetic' — sets the emotional tone"),
            ("•", "Negative Prompts: Use --no [unwanted elements] — e.g., '--no people, watermarks, text, logos'"),
            ("•", "Variations: After getting a good image, use V1-V4 to generate variations before U-ing (upscaling)"),
        ]),
    ])

print("✓ 08_AI_TOOLS_STACK complete")

# ─── 09_BUSINESS_OPERATIONS ────────────────────────────────────────────────────
p09 = "09_BUSINESS_OPERATIONS/"

doc(p09+"Annual_Business_Plan.docx",
    "Annual Business Plan — SMMA Agency",
    "Ultimate AI SMMA OS | Revenue Goals, Client Targets, Hiring Plan, and Quarterly Milestones",
    [
        ("Executive Summary — Your Agency Vision", [
            "Fill in this section with your specific agency vision. This document is your annual roadmap — return to it monthly to check your progress and quarterly to update projections.",
            "[FILL IN] Agency Name: _______________",
            "[FILL IN] Year: _______________",
            "[FILL IN] Annual Revenue Target: €_______________",
            "[FILL IN] Target Number of Active Clients: _______________",
            "[FILL IN] Target Average Retainer: €_______________/month",
            "[FILL IN] Primary Niche(s): _______________",
        ]),
        ("Revenue Projections and Client Targets", [
            "Revenue Model (fill in based on your pricing tiers):",
            "[FILL IN] Starter Clients (€500/mo): ___ clients = €___/month",
            "[FILL IN] Growth Clients (€1,500/mo): ___ clients = €___/month",
            "[FILL IN] Pro Clients (€3,000/mo): ___ clients = €___/month",
            "[FILL IN] Elite Clients (€5,000/mo): ___ clients = €___/month",
            "[FILL IN] Total Target MRR: €___/month",
            "[FILL IN] Annual Revenue Target: €___/year",
            "Example Model (10 active clients at mixed packages):",
            ("•", "2 Starter clients @ €500 = €1,000/month"),
            ("•", "3 Growth clients @ €1,500 = €4,500/month"),
            ("•", "3 Pro clients @ €3,000 = €9,000/month"),
            ("•", "2 Elite clients @ €5,000 = €10,000/month"),
            ("•", "Total: €24,500 MRR = €294,000/year"),
        ]),
        ("Q1 Milestones (January-March)", [
            "Q1 Focus: Foundation and First Clients",
            ("•", "Month 1: Complete agency setup — brand, contracts, systems, CRM"),
            ("•", "Month 1: Launch outreach to first 50 prospects (20 DMs + 20 emails + 10 LinkedIn)"),
            ("•", "Month 2: Close first 2 paying clients"),
            ("•", "Month 2: Deliver first content batch, establish reporting rhythm"),
            ("•", "Month 3: Close 2 more clients (total 4)"),
            ("•", "Month 3: Establish referral network — identify 3 potential referral partners"),
            "[FILL IN] Q1 Revenue Target: €___/month by March 31",
            "[FILL IN] Q1 Client Target: ___ active clients by March 31",
        ]),
        ("Q2 Milestones (April-June)", [
            "Q2 Focus: Systematize and Scale to 8 Clients",
            ("•", "Month 4: Hire first freelancer (content creator or designer)"),
            ("•", "Month 4: Systematize content production with AI workflow"),
            ("•", "Month 5: Close 2 more clients — now 6 active"),
            ("•", "Month 5: Launch first client upsell campaign (upgrade 2 Starter clients to Growth)"),
            ("•", "Month 6: Close 2 more clients — now 8 active"),
            ("•", "Month 6: Quarterly review — identify top 2 performing clients and build case studies"),
            "[FILL IN] Q2 Revenue Target: €___/month by June 30",
        ]),
        ("Q3 Milestones (July-September)", [
            "Q3 Focus: Optimize, Retain, and Build to €15K MRR",
            ("•", "Month 7: Full retention audit — review all clients, proactively address any at-risk accounts"),
            ("•", "Month 8: Publish first case study and launch referral program"),
            ("•", "Month 8: Target 2 Enterprise or Elite inquiries through case study-driven outreach"),
            ("•", "Month 9: Close 1 Elite/Pro client — highest-value acquisition of year"),
            "[FILL IN] Q3 Revenue Target: €___/month by September 30",
        ]),
        ("Q4 Milestones (October-December)", [
            "Q4 Focus: End-of-Year Push and 2026 Planning",
            ("•", "Month 10: Prepare Q4 campaign packages for all clients (Black Friday, Christmas, year-end)"),
            ("•", "Month 11: Black Friday — sell new annual packages with discount to interested prospects"),
            ("•", "Month 12: Annual review calls with all current clients — confirm renewals for 2026"),
            ("•", "Month 12: Begin 2026 planning — update this business plan, set new targets"),
            "[FILL IN] Q4 Revenue Target: €___/month by December 31",
            "[FILL IN] 2026 Annual Target: €___",
        ]),
        ("Marketing Budget Allocation", [
            "Recommended annual marketing budget (scale with revenue — target 10-15% of revenue):",
            ("•", "Own Agency Social Media (time cost): 3-5 hours/week personal content"),
            ("•", "Paid Outreach Tools (LinkedIn Sales Navigator, email tools): €100-300/month"),
            ("•", "Networking events and meetups: €100-200/month"),
            ("•", "Content creation for own agency: €200-500/month (freelancers + tools)"),
            ("•", "Paid social ads for own agency: €300-800/month (once first 5 clients are secured)"),
        ]),
    ])

doc(p09+"Client_Churn_Prevention_System.docx",
    "Client Churn Prevention System",
    "Ultimate AI SMMA OS | Early Warning Signs, Retention Scripts, and Win-Back Strategies",
    [
        ("Why Client Churn Is Your Agency's Biggest Threat", [
            "Acquiring a new SMMA client costs 5-7x more than retaining one. A single churn at €3,000/month = €36,000 in annualized lost revenue. More importantly, the emotional and operational disruption of losing a client — and having to replace them — derails your growth momentum. The agencies that scale fastest have the best retention systems, not the best sales systems.",
        ]),
        ("The 5 Early Warning Signs of Churn", [
            "Sign 1 — Decreased Communication:",
            ("•", "Client responds to messages much slower than usual"),
            ("•", "Client stops joining review calls or consistently reschedules"),
            ("•", "Client stops leaving comments on the content calendar"),
            "Sign 2 — Increased Criticism:",
            ("•", "Client requests revisions more frequently than usual"),
            ("•", "Quality complaints about content that was previously fine"),
            ("•", "Questioning the strategy or specific decisions more than before"),
            "Sign 3 — Budget Conversations:",
            ("•", "Client mentions cash flow, budget reviews, or cutting costs unprompted"),
            ("•", "Client asks about pausing, reducing scope, or switching to a lower package"),
            "Sign 4 — Reduced Enthusiasm:",
            ("•", "Client stops sharing content to their own Stories or engaging with their own posts"),
            ("•", "No longer mentions business wins, launches, or exciting news"),
            ("•", "Stopped introducing you to other business owners"),
            "Sign 5 — Competitive Shopping Signals:",
            ("•", "Client mentions speaking with other agencies"),
            ("•", "Client suddenly asks detailed questions about pricing or scope justification"),
        ]),
        ("Churn Prevention Response Protocol", [
            "When you notice 2+ warning signs, activate the Retention Protocol immediately — do not wait.",
            "Step 1 — Proactive Call (within 48 hours of spotting warning signs):",
            '"Hi [Name], I wanted to reach out personally — I\'ve been thinking about [Business Name] this week and wanted to check in on how you\'re feeling about our work together. Are there any areas where you feel we could be doing better or things you\'d like us to focus on differently?"',
            "Step 2 — Value Reminder:",
            '"While I have you — I pulled together this month\'s highlights [share specific wins] and I want to make sure you\'re seeing the full picture. [X] new followers, [Y] leads, [Z] website clicks — and this all happened in a competitive month for [niche]."',
            "Step 3 — Problem Solving:",
            '"If there\'s a specific frustration or expectation gap, I want to address it directly. I\'d rather have this honest conversation now than have you feel unhappy for another month. What would need to change for you to feel fully confident in our work together?"',
        ]),
        ("Retention Scripts for Common Churn Reasons", [
            "If client wants to cancel due to budget:",
            '"I completely understand — let\'s see if there\'s a way to make this work. Could we discuss a reduced scope version at €[LOWER PRICE]? It means [specific reduction in deliverables], but we keep the most important things running. I\'d hate for you to lose the momentum we\'ve built."',
            "If client is unhappy with results:",
            '"I take full responsibility for the results gap — let me be transparent about what I think is happening. [Honest diagnosis]. Here is exactly what I\'m proposing to change in the next 30 days, with specific targets I\'m committing to. Can we give this 30-day sprint a chance before making a final decision?"',
            "If client found another agency:",
            '"I appreciate you being direct with me. Could I ask what they\'re offering that feels different from what we do? I ask not to compete but to understand. [Listen] Based on what you\'ve described, I think we could match or improve on that if we adjusted [specific element]. Would you be open to staying and testing that first?"',
        ]),
        ("Win-Back Strategy for Lost Clients", [
            "Not every client can be retained. But lost clients are not lost forever. A structured win-back campaign can recover 20-30% of churned clients within 6-12 months.",
            ("•", "Month 1 after churn: Send a gracious exit email — no pressure, thank them for the partnership"),
            ("•", "Month 3: Send a genuine value share — a case study or tip relevant to their niche"),
            ("•", "Month 6: Check in with a specific observation about their current social media"),
            ("•", "Month 9-12: Share a 'what's changed at our agency' message highlighting improvements"),
            "Win-Back Email (Month 6):",
            '"Hi [Name], it\'s been a while! I came across [Business Name]\'s Instagram this week and noticed [specific observation]. I had a quick idea that I thought might be useful for you — [share 1 specific tip]. No agenda, just wanted to share it. Hope [business] is going well! [Your Name]"',
        ]),
    ])

doc(p09+"Team_and_Freelancer_Management.docx",
    "Team and Freelancer Management Guide",
    "Ultimate AI SMMA OS | Hiring, Briefing, Managing, and Paying Contractors",
    [
        ("When to Hire Your First Team Member", [
            "The question is not 'Can I afford to hire?' — it is 'Can I afford NOT to hire?' The typical trigger point for your first hire is when you consistently work more than 50 hours per week and are turning down new clients due to capacity. At that point, a €1,500-2,000/month freelancer can unlock €5,000-10,000 in additional monthly revenue.",
            ("•", "Your first hire should solve your biggest time bottleneck"),
            ("•", "Common first hires: Content Creator / Social Media Manager, Graphic Designer, Video Editor"),
            ("•", "Never hire for a role you don't understand yourself — you won't know if the work is good"),
        ]),
        ("Where to Find Quality SMMA Freelancers", [
            ("•", "Contra: Commission-free, U.S.-based creatives, strong for designers and writers"),
            ("•", "Upwork: Largest global freelance platform, excellent for vetting with portfolio reviews"),
            ("•", "LinkedIn: Direct outreach to junior social media managers and content creators"),
            ("•", "Fiverr Pro: Higher-tier verified freelancers for specific skills"),
            ("•", "Facebook Groups: 'SMMA Freelancers', 'Social Media Jobs' groups"),
            ("•", "Your network: Former colleagues, course community members, agency alumni"),
        ]),
        ("The Freelancer Interview Process", [
            "Step 1 — Portfolio Review: Ask for 5 examples of their best social media content. Judge on: quality, variety, relevance to your clients' niche",
            "Step 2 — Test Project: Pay for a small test task — 1 caption + 1 graphic for a fictional client brief. This tests quality, process, and communication",
            "Step 3 — Interview Questions:",
            ("•", "'Walk me through your process from receiving a brief to delivering the final content.'"),
            ("•", "'How do you handle feedback and revisions?'"),
            ("•", "'What social media tools are you proficient in?'"),
            ("•", "'What niche content have you produced before?'"),
            ("•", "'How many clients are you currently serving, and what's your typical turnaround time?'"),
        ]),
        ("Briefing Freelancers Effectively", [
            "Every freelancer must be briefed using the client's Brand Discovery Questionnaire and Visual Content Brief Template. Never rely on verbal instructions for creative work.",
            "The 5 elements of a great creative brief:",
            ("•", "Client Context: Who the client is, what they do, who they serve"),
            ("•", "Brand Identity: Colors, fonts, logo, visual style, dos and don'ts"),
            ("•", "Task Specifics: Exact deliverables, dimensions, format, deadline"),
            ("•", "Examples: 3-5 example posts or accounts for reference — 'like this but for [client]'"),
            ("•", "Revision Process: How to submit work, how many rounds of revisions are included, how to communicate questions"),
        ]),
        ("Managing Freelancers Without Micromanaging", [
            ("•", "Daily: Check in via Slack/WhatsApp group — 'How's [task] coming along?'"),
            ("•", "Weekly: Monday kickoff (set week's priorities), Friday review (review all delivered work)"),
            ("•", "Monthly: Payment cycle + brief performance review — what's working, what to improve"),
            ("•", "Feedback Formula: 'Great job on [specific thing]. For next time, let's [specific improvement]. Here's an example: [reference].'"),
            ("•", "Never: Micro-manage the process. Agree on outputs and deadlines, not methods."),
        ]),
        ("Freelancer Payment Best Practices", [
            ("•", "Always have a signed agreement before the first project — use a simplified version of your client contract"),
            ("•", "Payment terms: Net 5 or Net 7 (pay within 5-7 days of invoice submission)"),
            ("•", "Never pay in advance for a new freelancer — pay upon delivery of approved work"),
            ("•", "Use Revolut Business, Wise, or PayPal Business for international payments"),
            ("•", "Track all freelancer invoices in Invoice_Log.csv in Notion"),
            ("•", "Keep records for tax purposes — freelancer payments are business expenses"),
        ]),
    ])

# Agency Revenue Tracker XLSX
wb2 = Workbook()
ws1 = wb2.active
ws1.title = "Monthly P&L"
pl_headers = ["Month","Client 1","Client 2","Client 3","Client 4","Client 5",
              "Client 6","Client 7","Client 8","Total Income (€)",
              "Tools/Software (€)","Freelancers (€)","Ads (€)","Education (€)",
              "Other Expenses (€)","Total Expenses (€)","Net Profit (€)","Margin %"]
ws1.append(pl_headers)
for cell in ws1[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=10)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

pl_data = [
    ["January 2025","500","1500","0","0","0","0","0","0","=SUM(B2:I2)","128","300","0","49","75","=SUM(K2:O2)","=J2-P2","=Q2/J2"],
    ["February 2025","500","1500","1500","0","0","0","0","0","=SUM(B3:I3)","128","500","0","49","75","=SUM(K3:O3)","=J3-P3","=Q3/J3"],
    ["March 2025","500","1500","1500","3000","0","0","0","0","=SUM(B4:I4)","128","800","0","49","75","=SUM(K4:O4)","=J4-P4","=Q4/J4"],
    ["April 2025","500","1500","1500","3000","3000","0","0","0","=SUM(B5:I5)","128","1200","200","49","75","=SUM(K5:O5)","=J5-P5","=Q5/J5"],
    ["May 2025","500","1500","1500","3000","3000","3000","0","0","=SUM(B6:I6)","128","1800","200","49","75","=SUM(K6:O6)","=J6-P6","=Q6/J6"],
    ["June 2025","500","1500","1500","3000","3000","3000","5000","0","=SUM(B7:I7)","128","2500","500","49","100","=SUM(K7:O7)","=J7-P7","=Q7/J7"],
    ["July 2025","500","1500","1500","3000","3000","3000","5000","5000","=SUM(B8:I8)","128","3200","500","49","100","=SUM(K8:O8)","=J8-P8","=Q8/J8"],
    ["August 2025","0","1500","1500","3000","3000","3000","5000","5000","=SUM(B9:I9)","128","3200","500","49","100","=SUM(K9:O9)","=J9-P9","=Q9/J9"],
]
for i, row in enumerate(pl_data):
    ws1.append(row)
    for cell in ws1[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(horizontal="center")

for col, w in [("A",16),("B",12),("C",12),("D",12),("E",12),("F",12),("G",12),("H",12),("I",12),("J",16),("K",18),("L",16),("M",12),("N",14),("O",16),("P",18),("Q",16),("R",12)]:
    ws1.column_dimensions[col].width = w

# MRR Dashboard Sheet
ws2 = wb2.create_sheet("MRR Dashboard")
mrr_headers = ["Client Name","Package","MRR (€)","Contract Start","Contract End","Renewal Date","Status","Churn Risk","Notes"]
ws2.append(mrr_headers)
for cell in ws2[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

mrr_data = [
    ["Bella Vita Restaurant","Growth","1500","2025-01-01","2025-03-31","2025-04-01","Active - Renewed","LOW","Excellent client, already renewed for Q2"],
    ["FitLife Coaching","Pro","3000","2025-01-15","2025-07-15","2025-07-15","Active","LOW","Growing fast — upsell to Elite in Q3"],
    ["Luxe Aesthetics Clinic","Elite","5000","2024-11-01","2025-04-30","2025-05-01","Active","LOW","Strong results, refers clients regularly"],
    ["TechFlow SaaS","Pro","3000","2025-02-01","2025-07-31","2025-08-01","Active","MEDIUM","Decision maker changed — new contact relationship needed"],
    ["Green Harvest Ecom","Elite","5000","2024-10-15","2025-04-15","2025-04-15","Active — Renewing","LOW","Best performing client — TikTok strategy killing it"],
    ["Bloom Wedding Co.","Starter","500","2025-01-01","2025-03-31","2025-04-01","Trial ending","HIGH","Results below expectations — intervention call needed"],
    ["Kairos Real Estate","Growth","1500","2025-03-01","2025-08-31","2025-09-01","Active","LOW","New client, Month 1 onboarding complete"],
    ["Mindset Academy","Growth","1500","2025-02-15","2025-08-15","2025-08-15","Active","LOW","Strong engagement results"],
]
for i, row in enumerate(mrr_data):
    ws2.append(row)
    for cell in ws2[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

ws2.append([""])
ws2.append(["TOTAL ACTIVE MRR","","=SUM(C2:C9)"])
ws2["A10"].font = Font(bold=True)
ws2["C10"].font = Font(bold=True, color=NAV)

for col, w in [("A",22),("B",12),("C",12),("D",15),("E",15),("F",14),("G",22),("H",14),("I",38)]:
    ws2.column_dimensions[col].width = w

# Expense Tracker Sheet
ws3 = wb2.create_sheet("Expense Tracker")
exp_headers = ["Date","Category","Description","Amount (€)","Recurring?","Frequency","Annual Cost (€)","Notes"]
ws3.append(exp_headers)
for cell in ws3[1]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

exp_data = [
    ["2025-01-01","Tools/Software","Canva Pro","15","YES","Monthly","180","Essential — design tool for all clients"],
    ["2025-01-01","Tools/Software","ChatGPT Plus","20","YES","Monthly","240","Primary AI tool for content and strategy"],
    ["2025-01-01","Tools/Software","Buffer (Essentials)","18","YES","Monthly","216","Social media scheduling across all clients"],
    ["2025-01-01","Tools/Software","Later Pro","25","YES","Monthly","300","Instagram scheduling + link in bio"],
    ["2025-01-01","Tools/Software","Claude Pro","20","YES","Monthly","240","AI writing for contracts, SOPs, long-form"],
    ["2025-01-01","Tools/Software","Google Workspace","12","YES","Monthly","144","Email, Drive, Docs, Sheets"],
    ["2025-01-01","Tools/Software","Notion Plus","10","YES","Monthly","120","Project management and client databases"],
    ["2025-01-15","Freelancers","Content Creator - Part time","600","NO","Monthly","7200","20hr/month for 3 clients"],
    ["2025-01-15","Freelancers","Graphic Designer","400","NO","Monthly","4800","15hr/month for 4 clients"],
    ["2025-02-01","Ads","Agency own LinkedIn ads","150","YES","Monthly","1800","Lead generation for agency growth"],
    ["2025-01-01","Education","SMMA course renewal","49","YES","Monthly","588","Ongoing education and community"],
    ["2025-01-01","Other","Domain + hosting","12","YES","Monthly","144","Agency website"],
    ["2025-01-01","Other","Accounting software","25","YES","Monthly","300","QuickBooks / FreshBooks"],
]
for i, row in enumerate(exp_data):
    ws3.append(row)
    for cell in ws3[i+2]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(wrap_text=True, vertical="top")

for col, w in [("A",14),("B",18),("C",35),("D",14),("E",12),("F",14),("G",16),("H",35)]:
    ws3.column_dimensions[col].width = w

# Revenue Projections Sheet
ws4 = wb2.create_sheet("Revenue Projections")
ws4.append(["12-MONTH REVENUE PROJECTION — [YEAR]"])
ws4["A1"].font = Font(bold=True, size=14, color=NAV)
ws4.append([""])
rp_headers = ["Month","New Clients Added","Churned Clients","Total Active Clients",
              "Projected MRR (€)","Projected Expenses (€)","Net Profit (€)","Cumulative Revenue (€)"]
ws4.append(rp_headers)
for cell in ws4[3]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT, size=11)
    cell.alignment = Alignment(horizontal="center", wrap_text=True)

rp_data = [
    ["January","2","0","2","2000","800","1200","2000"],
    ["February","2","0","4","5000","1200","3800","7000"],
    ["March","2","0","6","9500","2000","7500","16500"],
    ["April","2","0","8","13500","3000","10500","30000"],
    ["May","1","1","8","14500","3200","11300","44500"],
    ["June","2","0","10","18000","4000","14000","62500"],
    ["July","1","0","11","21000","4500","16500","83500"],
    ["August","1","1","11","20000","4200","15800","103500"],
    ["September","2","0","13","24500","5000","19500","128000"],
    ["October","1","0","14","26000","5200","20800","154000"],
    ["November","2","1","15","28500","5500","23000","182500"],
    ["December","1","0","16","30000","5800","24200","212500"],
]
for i, row in enumerate(rp_data):
    ws4.append(row)
    for cell in ws4[i+4]:
        cell.fill = PatternFill("solid", fgColor=LGR) if i % 2 == 0 else PatternFill("solid", fgColor=WHT)
        cell.alignment = Alignment(horizontal="center")

ws4.append(["FULL YEAR TOTALS","=SUM(B4:B15)","=SUM(C4:C15)","","","=SUM(F4:F15)","=SUM(G4:G15)","=H15"])
for cell in ws4[16]:
    cell.fill = PatternFill("solid", fgColor=NAV)
    cell.font = Font(bold=True, color=WHT)
    cell.alignment = Alignment(horizontal="center")

for col, w in [("A",16),("B",18),("C",18),("D",20),("E",20),("F",22),("G",18),("H",22)]:
    ws4.column_dimensions[col].width = w

wb2.save(BASE + p09 + "Agency_Revenue_Tracker.xlsx")
print(f"  ✓ {p09}Agency_Revenue_Tracker.xlsx")
print("✓ 09_BUSINESS_OPERATIONS complete")

# ─── 10_NOTION_WORKSPACE ───────────────────────────────────────────────────────
p10 = "10_NOTION_WORKSPACE/"

write_csv(p10+"Client_Database.csv",
    ["Client ID","Business Name","Owner Name","Email","Phone","Package","Monthly Retainer (€)",
     "Contract Start","Contract End","Platforms Managed","Status","Notes"],
    [
        ["CLI-001","Bella Vita Restaurant","Marco Rossi","marco@bellavita.com","+353 87 123 4567","Growth","1500","2025-01-01","2025-03-31","Instagram, Facebook","Active","Best performing client — excellent content engagement"],
        ["CLI-002","FitLife Coaching","Sarah Chen","sarah@fitlifecoaching.com","+44 7700 900123","Pro","3000","2025-01-15","2025-07-15","Instagram, TikTok, LinkedIn","Active","Fitness coach with 8K followers — growing fast"],
        ["CLI-003","Luxe Aesthetics Clinic","Dr. Anna Müller","anna@luxeaesthetics.com","+49 151 12345678","Elite","5000","2024-11-01","2025-04-30","Instagram, Facebook, LinkedIn","Active","Medical aesthetic clinic — high-value content, referral source"],
        ["CLI-004","TechFlow SaaS","James Wilson","james@techflowsaas.com","+1 415 555 0192","Pro","3000","2025-02-01","2025-07-31","LinkedIn, Twitter/X","Active","B2B SaaS — LinkedIn driving strong MQL volume"],
        ["CLI-005","Green Harvest Ecom","Priya Patel","priya@greenharvestecom.com","+91 98765 43210","Elite","5000","2024-10-15","2025-04-15","Instagram, TikTok, Pinterest","Active","Sustainable e-commerce brand — TikTok is primary growth channel"],
        ["CLI-006","Bloom Wedding Co.","Emma Wright","emma@bloomweddingco.com","+353 86 987 6543","Starter","500","2025-01-01","2025-03-31","Instagram","Trial","First client — results below target, intervention in progress"],
    ])

write_csv(p10+"Lead_Tracker.csv",
    ["Lead ID","Business Name","Owner","Platform","Status","Source","Package Interest",
     "Est Monthly Value (€)","Last Contact","Next Action","Notes"],
    [
        ["LD-001","Bella Vita Restaurant","Marco Rossi","Instagram","CLOSED","Cold DM","Growth","1500","2024-12-28","Onboarding complete","Closed Jan 1 — first paid client"],
        ["LD-002","FitLife Coaching","Sarah Chen","LinkedIn","CLOSED","Cold Email","Pro","3000","2025-01-03","Onboarding complete","Closed Jan 15 — referred by Marco"],
        ["LD-003","City Cycles Dublin","Tom Murphy","Instagram","Discovery Call Booked","Cold DM","Growth","1500","2025-01-20","Call 2025-01-25 at 3pm","Bike shop owner, 2K IG followers, wants more bookings"],
        ["LD-004","Clarity Legal Services","Helena Kovač","LinkedIn","Proposal Sent","LinkedIn Outreach","Pro","3000","2025-01-18","Follow up Jan 24","Law firm — proposal sent, budget approved in principle"],
        ["LD-005","Nomad Coffee Co.","Ryan Davies","Instagram","Contacted","Cold DM","Starter","500","2025-01-19","Follow up Day 3","Independent coffee shop, very active on Instagram"],
        ["LD-006","Summit Fitness","Ali Hassan","Instagram","Not Interested","Cold DM","Growth","1500","2025-01-10","Archive Q2","Managing in-house, team of 3 — revisit in April"],
        ["LD-007","Prestige Property Group","Fiona Clarke","LinkedIn","Negotiating","Referral","Elite","5000","2025-01-21","Contract review call Friday","Referred by CLI-003 — real estate group with 5 agents"],
        ["LD-008","MindFlow Coaching","Keiran Doyle","Instagram","New Lead","Instagram Search","Growth","1500","2025-01-22","Send DM today","Life coach with 12K followers, inconsistent posting"],
    ])

write_csv(p10+"Content_Pipeline.csv",
    ["Content ID","Client","Platform","Content Type","Topic","Caption Status","Design Status",
     "Approval Status","Scheduled Date","Published","Engagement Notes"],
    [
        ["CON-001","Bella Vita Restaurant","Instagram","Reel","Kitchen prep: Sunday pasta secret","DONE","DONE","APPROVED","2025-01-27 10:00","YES","1,240 views, 89 likes, 12 comments — best ever reel"],
        ["CON-002","Bella Vita Restaurant","Facebook","Static Post","Valentine's Day booking announcement","DONE","DONE","APPROVED","2025-02-10 09:00","YES","52 reactions, 18 comments, 8 bookings tracked"],
        ["CON-003","FitLife Coaching","Instagram","Carousel","5 myths about weight loss","DONE","DONE","APPROVED","2025-01-28 08:00","YES","342 saves, 28 shares — highest save rate this month"],
        ["CON-004","FitLife Coaching","TikTok","TikTok Video","Morning routine of a PT (BTS)","DONE","IN EDITING","NOT SENT","2025-02-03","NO","Waiting on client video file"],
        ["CON-005","Luxe Aesthetics Clinic","Instagram","Static Post","Client result: skin transformation","DONE","DONE","APPROVED","2025-01-29 12:00","YES","189 likes, 24 DM inquiries — best lead gen post"],
        ["CON-006","TechFlow SaaS","LinkedIn","Text Post","Opinion: Why SaaS companies need social media in 2025","DONE","N/A — Text","APPROVED","2025-01-30 08:00","YES","1,840 impressions, 67 reactions, 23 comments"],
        ["CON-007","Green Harvest Ecom","TikTok","TikTok Video","Packaging unboxing ASMR","IN PROGRESS","IN EDITING","NOT SENT","2025-02-04","NO","Trending audio selected — editing by end of week"],
        ["CON-008","Bloom Wedding Co.","Instagram","Static Post","Spring wedding season announcement","DONE","DONE","APPROVED","2025-01-31 10:00","YES","34 likes, 2 comments — below target, strategy adjustment needed"],
    ])

write_csv(p10+"Campaign_Tracker.csv",
    ["Campaign ID","Client","Campaign Name","Platform","Ad Budget (€)","Start Date","End Date",
     "Impressions","Clicks","CTR","Conversions","CPA (€)","ROAS","Status"],
    [
        ["CAM-001","Bella Vita Restaurant","Valentine's Day Bookings","Meta (FB+IG)","500","2025-02-01","2025-02-14","84,200","1,840","2.18%","42","11.90","3.2x","COMPLETED — Highly profitable"],
        ["CAM-002","FitLife Coaching","January New Year Challenge","Instagram","300","2025-01-02","2025-01-31","42,100","980","2.33%","28","10.71","4.1x","COMPLETED — Excellent ROAS for coaching"],
        ["CAM-003","Luxe Aesthetics Clinic","Botox Spring Promo","Meta (FB+IG)","1000","2025-03-01","2025-03-31","128,400","2,840","2.21%","19","52.63","8.4x","ACTIVE — Tracking above target"],
        ["CAM-004","TechFlow SaaS","Q1 Lead Gen — LinkedIn","LinkedIn","800","2025-01-15","2025-03-31","18,200","640","3.52%","34","23.53","5.2x","ACTIVE — Strong LinkedIn CTR"],
        ["CAM-005","Green Harvest Ecom","Spring Collection Launch","TikTok + IG","1500","2025-03-15","2025-04-15","0","0","0","0","0","0","UPCOMING — Creative in preparation"],
        ["CAM-006","Bloom Wedding Co.","Bridal Season Awareness","Instagram","200","2025-02-15","2025-03-31","8,400","220","2.62%","3","66.67","1.8x","ACTIVE — Below target, creative being tested"],
    ])

write_csv(p10+"Team_Tasks.csv",
    ["Task ID","Assigned To","Client","Task Description","Priority","Status","Due Date","Est Hours","Notes"],
    [
        ["TSK-001","[Your Name]","Bella Vita Restaurant","February content calendar creation and caption writing","HIGH","IN PROGRESS","2025-01-22","4","Need client's Valentine's promo details before completion"],
        ["TSK-002","[Designer Name]","FitLife Coaching","Design 8 carousel slides for weight loss myths post","HIGH","DONE","2025-01-20","3","Delivered and approved by client Jan 20"],
        ["TSK-003","[Video Editor]","Green Harvest Ecom","Edit unboxing TikTok — add trending audio and text overlays","HIGH","IN PROGRESS","2025-01-24","2","Audio selected: [TRACK NAME] — client approved"],
        ["TSK-004","[Your Name]","ALL CLIENTS","Monthly reporting — collect January analytics data from all platforms","MEDIUM","NOT STARTED","2025-02-03","6","Use Reporting_SOP.docx — start Feb 1"],
        ["TSK-005","[Content Creator]","Luxe Aesthetics Clinic","Write captions for March botox campaign ad copy (4 variations)","HIGH","DONE","2025-01-23","2","Approved — sent to ads manager"],
        ["TSK-006","[Your Name]","TechFlow SaaS","Monthly strategy call prep — pull January LinkedIn analytics","MEDIUM","NOT STARTED","2025-01-28","1","Call scheduled Jan 30 at 2pm"],
        ["TSK-007","[Designer Name]","Bloom Wedding Co.","Redesign static post template — engagement too low","HIGH","IN PROGRESS","2025-01-25","2","Testing new style: lighter background, larger font"],
        ["TSK-008","[Your Name]","Prospect - Clarity Legal","Prepare custom proposal for legal services niche","HIGH","IN PROGRESS","2025-01-23","3","Use Agency_Proposal_Template.pptx — present Jan 25"],
    ])

write_csv(p10+"Invoice_Log.csv",
    ["Invoice #","Client","Service Month","Amount (€)","Date Issued","Due Date","Status","Payment Method","Notes"],
    [
        ["INV-2025-001","Bella Vita Restaurant","January 2025","1500","2025-01-01","2025-01-08","PAID","Stripe","Paid Jan 6 — auto-charge set up"],
        ["INV-2025-002","FitLife Coaching","January 2025","3000","2025-01-15","2025-01-22","PAID","Bank Transfer","Paid Jan 19"],
        ["INV-2025-003","Luxe Aesthetics Clinic","January 2025","5000","2025-01-01","2025-01-08","PAID","Bank Transfer","Paid Jan 5 — early payment"],
        ["INV-2025-004","TechFlow SaaS","February 2025","3000","2025-02-01","2025-02-08","PAID","Stripe","Auto-charge successful"],
        ["INV-2025-005","Green Harvest Ecom","February 2025","5000","2025-02-01","2025-02-08","PAID","Bank Transfer","Paid Feb 6"],
        ["INV-2025-006","Bloom Wedding Co.","February 2025","500","2025-02-01","2025-02-08","OVERDUE","Stripe","Card declined — follow up required"],
        ["INV-2025-007","Kairos Real Estate","March 2025","1500","2025-03-01","2025-03-08","PENDING","Bank Transfer","New client — first invoice sent"],
        ["INV-2025-008","Mindset Academy","March 2025","1500","2025-03-01","2025-03-08","PENDING","Stripe","Auto-charge set up — pending first charge"],
    ])

write_csv(p10+"Analytics_Report.csv",
    ["Report Date","Client","Platform","Followers","New Followers","Engagement Rate",
     "Total Reach","Impressions","Clicks","Top Post","Notes"],
    [
        ["2025-01-31","Bella Vita Restaurant","Instagram","4892","382","3.4%","28400","94200","342","Sunday Pasta Reel — 1,240 views, 89 likes","Best month yet — Reel drove 78% of reach"],
        ["2025-01-31","FitLife Coaching","Instagram","8220","420","4.2%","42800","135000","891","Weight Loss Myths Carousel — 342 saves","January fitness content peak — maintain momentum"],
        ["2025-01-31","Luxe Aesthetics Clinic","Instagram","2890","94","5.8%","18200","56400","218","Skin transformation before/after — 24 DM inquiries","Highest quality leads month — 9 clinic bookings attributed"],
        ["2025-01-31","TechFlow SaaS","LinkedIn","1240","80","3.1%","12400","38200","1240","2025 SaaS Social Media Opinion post — 23 comments","LinkedIn performing strongly — 42 MQL generated"],
        ["2025-01-31","Green Harvest Ecom","TikTok","11820","880","2.9%","58400","198000","2840","Packaging unboxing ASMR — 12,400 views","TikTok growth is primary channel — IG still growing but slower"],
        ["2025-01-31","Bloom Wedding Co.","Instagram","1820","120","2.1%","8400","24200","84","Spring announcement post — 34 likes","Below average engagement — content strategy review needed"],
    ])

write_csv(p10+"Brand_Asset_Library.csv",
    ["Asset ID","Client","Asset Type","File Name","Version","Status","Approved By","Date","Notes"],
    [
        ["AST-001","Bella Vita Restaurant","Logo (Primary)","bellavita_logo_primary_v2.svg","v2","ACTIVE","Marco Rossi","2025-01-05","High-res SVG — use for all print and digital"],
        ["AST-002","Bella Vita Restaurant","Brand Colors","bellavita_brand_colors.pdf","v1","ACTIVE","Marco Rossi","2025-01-05","Primary: #8B0000, Secondary: #F5F0E8, Accent: #D4AF37"],
        ["AST-003","FitLife Coaching","Logo (Horizontal)","fitlife_logo_horizontal_v1.png","v1","ACTIVE","Sarah Chen","2025-01-18","PNG with transparent background — horizontal version"],
        ["AST-004","FitLife Coaching","Profile Photo Set","fitlife_profile_photos_jan2025.zip","v1","ACTIVE","Sarah Chen","2025-01-18","12 professional photos for Q1 content use"],
        ["AST-005","Luxe Aesthetics Clinic","Logo Set (All Versions)","luxe_logo_full_set_v3.zip","v3","ACTIVE","Dr. Anna Müller","2024-11-10","Full logo set: primary, white, dark, icon-only"],
        ["AST-006","TechFlow SaaS","Brand Guidelines PDF","techflow_brand_guidelines_v2.pdf","v2","ACTIVE","James Wilson","2025-02-05","Complete brand guide: colors, fonts, logo usage, imagery style"],
    ])

# Notion Setup Guide (Markdown)
with open(BASE + p10 + "Notion_Setup_Guide.md", "w", encoding="utf-8") as f:
    f.write("""# Notion Setup Guide — AI SMMA Operating System

## Welcome to Your SMMA Notion Workspace

This guide walks you through setting up your complete Notion workspace using the 8 CSV databases included in this folder. Follow the steps exactly in this order for the best result.

---

## Step 1: Import the 8 CSV Databases

For **each** CSV file in this folder, follow these steps:

1. Open Notion (notion.so)
2. In your sidebar, click **+ New Page**
3. Name the page the same as the CSV file (e.g., "Client Database")
4. Click into the page and type `/table` → Select **Table — Full Page**
5. In the empty table, click the **three dots (...)** in the top right
6. Select **Import → CSV**
7. Upload the corresponding CSV file
8. Notion will create columns matching the CSV headers automatically

**Repeat for all 8 files:**
- `Client_Database.csv`
- `Lead_Tracker.csv`
- `Content_Pipeline.csv`
- `Campaign_Tracker.csv`
- `Team_Tasks.csv`
- `Invoice_Log.csv`
- `Analytics_Report.csv`
- `Brand_Asset_Library.csv`

---

## Step 2: Set Up Recommended Views for Each Database

### Client Database — Recommended Views
- **All Clients (Default)** — Grid view, all columns visible
- **Active Clients** — Filter: Status = "Active"
- **By Package** — Group by: Package
- **Renewal Calendar** — Calendar view, date: Contract End

### Lead Tracker — Recommended Views
- **Lead Pipeline (Kanban)** — Board view, grouped by: Status (stages: New Lead → Contacted → Discovery Call Booked → Proposal Sent → Negotiating → Closed / Not Interested)
- **Hot Leads** — Filter: Status = "Discovery Call Booked" OR "Negotiating"
- **Follow-Up Today** — Filter: Next Action date = Today or Earlier

### Content Pipeline — Recommended Views
- **By Client (Kanban)** — Board view, grouped by: Client
- **Approval Queue** — Filter: Approval Status = "NOT SENT" AND Caption Status = "DONE"
- **Publishing Calendar** — Calendar view, date: Scheduled Date

### Team Tasks — Recommended Views
- **My Tasks** — Filter: Assigned To = [Your Name]
- **Due This Week** — Filter: Due Date = This Week
- **By Priority (Board)** — Board view, grouped by: Priority (HIGH → MEDIUM → LOW)

### Invoice Log — Recommended Views
- **Overdue Invoices** — Filter: Status = "OVERDUE"
- **This Month** — Filter: Date Issued = This Month
- **By Client** — Group by: Client

---

## Step 3: Link Databases Together (Relations)

Connect your databases for a powerful CRM system:

1. **Content Pipeline → Client Database**: In Content Pipeline, add a **Relation** property called "Client Link". Point it to the Client Database. Now each piece of content is linked to the client.

2. **Team Tasks → Content Pipeline**: In Team Tasks, add a **Relation** property called "Related Content". Link to Content Pipeline. Now tasks are linked to specific content pieces.

3. **Invoice Log → Client Database**: In Invoice Log, add a **Relation** to Client Database. Now invoices are linked to client profiles.

4. **Analytics Report → Client Database**: Link analytics to the corresponding client.

---

## Step 4: Create Your Daily Dashboard

Create a new Notion page called **"SMMA Daily Dashboard"** and add these linked database views:

1. **Team Tasks Due Today** — Filter from Team Tasks: Due Date = Today
2. **Content Awaiting Approval** — Filter from Content Pipeline: Approval Status = NOT SENT
3. **Overdue Invoices** — Filter from Invoice Log: Status = OVERDUE
4. **Hot Leads** — Filter from Lead Tracker: Status = Negotiating or Discovery Call Booked
5. **This Month's Revenue** — Gallery view of Invoice Log for current month

This dashboard gives you an instant overview of your business every morning.

---

## Step 5: Set Up Recurring Templates (Notion Templates)

For your most common tasks, create Notion Templates:

**Monthly Content Calendar Template:**
- Create a new page in your Content Pipeline section
- Add all your standard column properties
- Save as a template by clicking "New Template" in your database

**Monthly Report Template:**
- Create a page with sections: Executive Summary, KPIs, Platform Performance, Content Highlights, Next Month Plan
- Save as template for quick monthly report creation

---

## Step 6: Invite Team Members

If you have freelancers or team members:

1. Click **Share** in the top right of your workspace page
2. Enter their email address
3. Set permissions: **Can Edit** for full access, **Can View** for read-only
4. Assign them to tasks in Team_Tasks database

---

## Recommended Notion Integrations

- **Zapier / Make (formerly Integromat)**: Automate task creation when new leads are added
- **Slack Integration**: Get Notion task reminders in Slack
- **Google Calendar Sync**: Sync content calendar with your Google Calendar
- **Notion AI**: Available in Notion Pro — use it to summarize client notes and draft content briefs

---

## Need Help?

If you have any questions about the Notion setup, refer to the **AI_SMMA_OS_Complete_User_Guide.pdf** in this folder for a full walkthrough with screenshots.

---

*Ultimate AI SMMA Operating System | Notion Workspace Setup Guide v1.0*
""")
print(f"  ✓ {p10}Notion_Setup_Guide.md")
print("✓ 10_NOTION_WORKSPACE complete")
print("\nPART 3 DONE")
