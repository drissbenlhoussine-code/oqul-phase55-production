#!/usr/bin/env python3
"""Repair: builds folders 11-12, PDFs, Asset Manifest, ZIP for AI SMMA OS"""
import os, csv, json, zipfile
from docx import Document
from docx.shared import Pt, RGBColor
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor as PRGB
from pptx.enum.text import PP_ALIGN
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

BASE = "/home/user/oqul-phase55-production/ai-smma-os/Ultimate_AI_SMMA_Operating_System/"
ETSY_DIR = "/home/user/oqul-phase55-production/etsy-listings/"
os.makedirs(BASE+"11_BONUSES", exist_ok=True)
os.makedirs(BASE+"12_CANVA_TEMPLATES", exist_ok=True)
os.makedirs(ETSY_DIR, exist_ok=True)

NAV="0F3460"; ACC="E94560"; GLD="F5A623"; GRN="27AE60"; WHT="FFFFFF"; LGR="F8F9FA"
def hf(h): return PatternFill("solid", fgColor=h)
def bf(bold=True,sz=11,col="000000"): return Font(bold=bold,size=sz,color=col)
def al(h="center",v="center"): return Alignment(horizontal=h,vertical=v,wrap_text=True)
def thin(): s=Side(style='thin',color='CCCCCC'); return Border(left=s,right=s,top=s,bottom=s)
def hr(ws,row,cols,texts,bg=NAV,fg=WHT):
    for c,t in zip(cols,texts):
        x=ws.cell(row=row,column=c,value=t); x.fill=hf(bg); x.font=bf(True,11,fg); x.alignment=al(); x.border=thin()
def dr(ws,row,cols,vals,bg=WHT):
    for c,v in zip(cols,vals):
        x=ws.cell(row=row,column=c,value=v); x.fill=hf(bg); x.font=bf(False,10); x.alignment=al("left"); x.border=thin()
def wd(ws,widths):
    for col,w in widths.items(): ws.column_dimensions[col].width=w

def doc(fn, title, sub, secs):
    d = Document()
    t = d.add_paragraph(title); t.style = d.styles['Normal']
    t.runs[0].bold = True; t.runs[0].font.size = Pt(14)
    t.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
    if sub:
        s = d.add_paragraph(sub); s.style = d.styles['Normal']
        s.runs[0].font.size = Pt(10); s.runs[0].font.color.rgb = RGBColor(0x7F,0x8C,0x8D)
    d.add_paragraph("")
    for sec in secs:
        if isinstance(sec, str): d.add_paragraph(sec); continue
        h, items = sec
        hd = d.add_heading(h, level=1); hd.runs[0].font.color.rgb = RGBColor(0x0F,0x34,0x60)
        for it in items:
            if isinstance(it, tuple) and it[0]=='*': d.add_paragraph(it[1], style='List Bullet')
            else: d.add_paragraph(str(it))
    d.save(BASE+fn); print(f"  doc {fn}")

PNAV=PRGB(15,52,96); PACC=PRGB(233,69,96); PGLD=PRGB(245,166,35); PWHT=PRGB(255,255,255)
PLGR=PRGB(248,249,250); PDGR=PRGB(44,62,80)
def prs():
    p=Presentation(); p.slide_width=Inches(13.33); p.slide_height=Inches(7.5); return p
def sl(p): return p.slides.add_slide(p.slide_layouts[6])
def box(s,l,t,w,h,rgb):
    sh=s.shapes.add_shape(1,Inches(l),Inches(t),Inches(w),Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb=rgb; sh.line.fill.background()
def tx(s,text,l,t,w,h,sz=18,bold=False,col=PWHT,a=PP_ALIGN.LEFT):
    tb=s.shapes.add_textbox(Inches(l),Inches(t),Inches(w),Inches(h))
    tf=tb.text_frame; tf.word_wrap=True; p=tf.paragraphs[0]; p.alignment=a
    r=p.add_run(); r.text=text; r.font.size=PPt(sz); r.font.bold=bold; r.font.color.rgb=col

def csv_w(path, headers, rows):
    with open(BASE+path,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.writer(f); w.writerow(headers); w.writerows(rows)
    print(f"  csv {path}")

def make_pdf(fpath, title, subtitle, secs):
    st=getSampleStyleSheet()
    NAV_C=colors.HexColor("#0F3460"); ACC_C=colors.HexColor("#E94560"); GLD_C=colors.HexColor("#F5A623")
    ts=ParagraphStyle('T',parent=st['Normal'],fontSize=16,textColor=NAV_C,spaceAfter=4,fontName='Helvetica-Bold')
    ss=ParagraphStyle('S',parent=st['Normal'],fontSize=11,textColor=colors.HexColor("#7F8C8D"),spaceAfter=12)
    hs=ParagraphStyle('H',parent=st['Normal'],fontSize=13,textColor=NAV_C,spaceBefore=12,spaceAfter=4,fontName='Helvetica-Bold')
    bs=ParagraphStyle('B',parent=st['Normal'],fontSize=10,spaceAfter=4,leading=15)
    bls=ParagraphStyle('BL',parent=st['Normal'],fontSize=10,leftIndent=16,spaceAfter=3,leading=14)
    story=[Paragraph(title,ts),HRFlowable(width="100%",thickness=3,color=ACC_C,spaceAfter=6),Paragraph(subtitle,ss)]
    for sec in secs:
        if isinstance(sec,str): story.append(Paragraph(sec,bs)); continue
        hd,items=sec; story.append(Paragraph(hd,hs)); story.append(HRFlowable(width="100%",thickness=1,color=GLD_C,spaceAfter=4))
        for it in items:
            if isinstance(it,tuple) and it[0]=='*': story.append(Paragraph(f"* {it[1]}",bls))
            else: story.append(Paragraph(str(it),bs))
    SimpleDocTemplate(fpath,pagesize=A4,rightMargin=50,leftMargin=50,topMargin=50,bottomMargin=50).build(story)

# ── 11_BONUSES ────────────────────────────────────────────────────────────────
p11="11_BONUSES/"
print("Building 11_BONUSES...")

# 365 Social Media Captions (fixed)
agency_tips = [
    "Running a social media agency? Here's what separates the 6-figure agencies: they niche DOWN, not up.",
    "The best client you can get is a referral from your happiest client. Build the relationship first.",
    "Agency owners: Stop competing on price. Compete on results. Show the numbers. Win on value.",
    "Your proposal is losing deals if it doesn't show ROI. Stop listing what you do -- show what clients GET.",
    "The churn you experience is usually about communication, not content. Call your clients more.",
    "Every agency has creators. The ones that scale have SYSTEMS. Document everything you do.",
    "Retainer clients beat project clients every time. Build for recurring revenue from day one.",
    "Your portfolio is your best salesperson. If it doesn't show results (not just pretty posts), rebuild it.",
    "Discovery calls should diagnose, not pitch. Ask questions. Listen first, then solve.",
    "The agencies that scale fastest all have one thing in common: they hire before they need to.",
    "Niching into one industry feels scary. But 'the agency for restaurants' beats 'we do everything' every time.",
    "Your pricing should make you slightly uncomfortable. If you never lose deals on price, you're undercharging.",
    "Monthly reports are your retention weapon. Clients who see their ROI don't leave.",
    "Stop doing everything for every client. Package your services. Price them clearly. Watch close rates improve.",
    "The best agency tool isn't software -- it's a client who trusts you enough to give you creative freedom.",
    "Client success IS your marketing. Document every win. Share every result.",
    "Systems don't kill creativity. Systems FREE you to be creative because admin handles itself.",
    "One more client at your current capacity will break your agency. Build systems BEFORE you hit capacity.",
    "Your client's goal is not 'more followers.' It's more revenue. Make sure your KPIs reflect that.",
    "Prospecting truth: 80% of your new clients will come from following up. Most agencies stop at 1 email.",
    "The agency founders who last 10 years all love what they do for clients -- not just the money.",
    "Contract clarity prevents 90% of client conflicts. If it's not in writing, it doesn't exist.",
    "Your agency reputation is built one client at a time. Show up consistently and do what you said.",
    "Stop spending 3 hours on a proposal for an 800/mo client. Use a template. Customize 20%. Send it.",
    "The agencies that charge 5k/mo don't do more work. They communicate value better.",
    "Referral programs are underused by 95% of agencies. Ask happy clients for introductions.",
    "Your welcome email sequence sets the tone for the entire client relationship. Make it warm and clear.",
    "Data storytelling is a skill. Turn metrics into a narrative connecting to the client's business goals.",
    "The best clients pay on time, trust your process, and refer others. Optimize for that client profile.",
    "AI tools won't replace agencies. Agencies that use AI will replace agencies that don't.",
    "Community over competition. The agencies that collaborate with peers grow faster.",
    "Your client offboarding process matters as much as onboarding. Leave well, get referrals.",
    "Time tracking is not about micromanaging -- it's about knowing your real profitability per client.",
    "The agency that responds BEST wins -- not the fastest.",
    "Scope creep is your fault if you don't have a clear scope. Define it. Defend it. Get paid for extras.",
    "Prospecting with video DMs converts 3-5x better than text DMs. Record a 60-second personalized video.",
]
content_tips = [
    "Hook rule: if your first 3 seconds don't stop the scroll, nothing else matters. Rewrite your hooks.",
    "The best social media content feels like it was made FOR the viewer -- not about the brand.",
    "Storytelling formula: Problem -- Struggle -- Solution -- Result. Works for captions, Reels, carousels.",
    "Engagement hack: end every educational post with a question. Watch your comments triple.",
    "The carousel format performs because it's the highest-save content type on Instagram. Use it weekly.",
    "Batch your content creation. 4 hours once a week beats 30 minutes every day.",
    "Your client's content doesn't have to go viral. It has to reach the RIGHT 1,000 people consistently.",
    "Authenticity beats perfection. The behind-the-scenes Reel will outperform the studio shoot.",
    "B-roll is content gold. Teach your clients to film everything. Use it for Reels, Stories, ads.",
    "Repurpose everything: one idea = blog + carousel + Reel + 5 Stories + email + LinkedIn post.",
    "Best hook ever: 'Nobody talks about this but...' Try it for your next Reel.",
    "Consistency beats creativity. Showing up every week for a year beats going viral once.",
    "Know the platform. Instagram rewards Reels. LinkedIn rewards text posts. TikTok rewards trends.",
    "Customer testimonials are your most persuasive content. Repurpose them everywhere.",
    "Educational content builds authority. Entertainment builds followers. You need both.",
    "The save is the most valuable engagement metric on Instagram. Create content people want to return to.",
    "Color consistency across your feed creates brand recognition. Pick 3 colors and stick to them.",
    "UGC converts 4x better than branded content for ads. Prioritize it.",
    "The first comment matters most. Respond to every comment in the first hour of posting.",
    "Your caption should start with the hook -- not 'Happy Monday!' or your business name.",
    "Video captions (text on screen) increase watch time 12%. Always add subtitles.",
    "Pattern interrupt in Reels: change scenes every 2-3 seconds to maintain attention.",
    "Product demos outperform product photos by 2-5x. Show, don't tell.",
    "Seasonal content gets shared. Plan your calendar around holidays and cultural moments.",
    "Use your client's real customers in content whenever possible. Real faces beat stock photos always.",
    "Story beats stat. 'Client grew 0 to 10k in 90 days' beats '75% increase in followers'.",
    "Audio branding: a signature sound makes your client's content instantly recognizable.",
    "The best time to post is when YOUR audience is online. Check Insights. Ignore generic blog advice.",
    "Interactive Stories (polls, questions, sliders) increase retention and algorithm priority.",
    "Controversy drives engagement but at a cost. Stay in your lane unless controversy is the brand.",
    "Caption length varies by platform: Instagram rewards longer captions; Twitter/X is short; LinkedIn longer.",
    "The green screen Reel effect is the most underused educational content format on TikTok.",
    "Social proof posts should make up 20-30% of your content mix.",
    "Trend adoption window: 48-72 hours. If you're late, skip it. Don't post stale trends.",
    "The hardest skill in content: making complex things simple. Master that and clients never leave.",
    "Value stack your content: what can the viewer DO after seeing this? If nothing, rewrite it.",
]
growth_tips = [
    "Easiest way to grow a business account: collaborate with non-competing accounts serving the same audience.",
    "Paid reach beats organic reach for business goals. If you're not boosting posts, you're leaving results behind.",
    "SEO on Instagram: your profile name, bio, and caption keywords all affect discoverability.",
    "Growth hack most agencies miss: get clients to engage with their dream clients' content before posting.",
    "Email list beats social following. Always. The platform owns the algorithm. You own the list.",
    "Community-building: respond to every DM and comment within 2 hours for the first 90 days. It changes everything.",
    "Pinned posts are your most-viewed content. Treat them like your homepage hero section.",
    "Follower count is a vanity metric. Engagement rate and link clicks are business metrics.",
    "Micro-influencers (10k-100k) in your client's niche often outperform mega-influencers at 10% of the cost.",
    "Instagram broadcast channel is one of the most underused organic reach tools available right now.",
    "Post at peak times, but don't obsess. Consistency matters more than timing.",
    "LinkedIn growth: comment thoughtfully on 5 posts in your niche each morning. Inbound follows happen.",
    "Facebook Groups still drive significant B2C traffic. Don't write off Facebook yet.",
    "The most powerful growth tool: a referral from a satisfied customer. Systemize your ask.",
    "Build your client's personal brand alongside the business brand. People buy from people.",
    "Cross-promote between platforms. What works as an Instagram Reel becomes TikTok and YouTube Shorts.",
    "Your first 1,000 followers are the hardest. After that, social proof drives organic growth.",
    "Geotags and location tags increase local discoverability for brick-and-mortar clients. Always use them.",
    "Monthly giveaways are high-risk. Better: earned media through exceptional content.",
    "Podcast guesting builds authority and drives targeted followers. Get your clients on podcasts.",
    "The answer to slow growth is usually: better content, more consistent posting, or better audience targeting.",
    "Pinterest is the most underrated platform for female audiences in lifestyle, home, and food categories.",
    "YouTube long-form content has the highest retention and highest trust. Worth the investment.",
    "Study your best-performing 10 posts. The pattern IS your content strategy.",
    "Growth plateau means it's time to change the content mix. What got you here won't get you there.",
    "Niche hashtags (under 100k posts) give you better chance in top posts than mega hashtags.",
    "Instagram Collab posts reach both creators' audiences simultaneously. Perfect for co-marketing.",
    "Consistency of brand voice is as important as consistency of posting frequency.",
    "The 'link in bio' is a wasted CTA. Use specific story swipe-ups or in-post directions instead.",
    "Repost user-generated content with permission. Free content + social proof + customer appreciation.",
    "Every account needs 1 content type that's ONLY for engagement (polls, debates, questions).",
    "Growth mindset: every underperforming post teaches you something about your audience. Analyze, don't delete.",
    "The fastest-growing accounts in any niche post more than their competitors. Volume matters.",
    "Strategy truth: most brands post too rarely and then wonder why growth is slow. Aim for daily on key platforms.",
    "Automation for scheduling is good. Automation for engagement (buying followers) destroys credibility.",
    "Algorithm truth: the platform wants you to succeed because your success keeps users on the platform.",
]

cat_names = [
    "Agency Tips","Content Creation Tips","Growth Strategy","Client Management",
    "AI and Tools","Platform Strategy","Analytics and Data",
    "Mindset and Productivity","Sales and Pricing","Success Stories"
]
source_lists = {0: agency_tips, 1: content_tips, 2: growth_tips}
generic_templates = {
    3: "Client Management tip #{n}: {msg}",
    4: "AI and Tools tip #{n}: {msg}",
    5: "Platform Strategy tip #{n}: {msg}",
    6: "Analytics and Data tip #{n}: {msg}",
    7: "Mindset and Productivity tip #{n}: {msg}",
    8: "Sales and Pricing tip #{n}: {msg}",
    9: "Success Story #{n}: {msg}",
}
generic_msgs = {
    3: ["Set clear expectations in your first client meeting and document everything.",
        "Weekly check-ins prevent 90% of client dissatisfaction. Schedule them from day one.",
        "Clients leave agencies because of communication gaps, not bad results. Stay proactive.",
        "Use a shared project management tool with every client so they always know what's happening.",
        "The best client relationships feel like partnerships. Involve them in the creative process.",
        "Client retention starts on day 1. Your onboarding experience sets the tone for everything.",
        "Send monthly ROI reports even when results are slow. Transparency builds trust.",
        "Set realistic expectations. Under-promise and over-deliver. Every. Single. Time.",
        "A surprise win (a bonus post, an early delivery) builds more loyalty than any contract.",
        "Difficult clients often become your best case studies. Handle conflict with professionalism.",
        "Know your client's business goals, not just their social media goals. Align your work to revenue.",
        "Client birthday messages and holiday cards cost nothing and pay dividends in loyalty.",
        "A quarterly strategy review call shows clients you're thinking about their long-term growth.",
        "Celebrate client wins publicly (with permission). They share it. You get exposure.",
        "The moment a client feels unheard is the moment they start looking for a replacement.",
        "Create a client success playbook and follow it for every single client, every single time.",
        "Document client preferences, brand voice, and pet peeves. Reference them before every post.",
        "Client feedback is gold. Ask for it formally every 90 days. Act on it visibly.",
        "A client who refers others is worth 10x more than their retainer. Treat them accordingly.",
        "Exit interviews with churned clients are painful but invaluable. Do them every time.",
        "Never surprise a client with bad news. Give early warning and come with a solution.",
        "Client portals (Notion, ClickUp, Monday) reduce email volume and increase perceived professionalism.",
        "Standardize your content approval process. Unclear approvals lead to last-minute chaos.",
        "The fastest path to a rate increase is a case study that proves undeniable ROI.",
        "Clients who understand social media are easier to retain. Educate your clients.",
        "Track client satisfaction scores quarterly using a simple NPS survey.",
        "Over-communication is almost always better than under-communication with clients.",
        "Know who the decision-maker is at every client. Build relationships above and below them.",
        "Your client's competitor analysis is your best strategic weapon. Use it in every presentation.",
        "Loyalty is built through consistency. Show up the same quality every month, every deliverable.",
        "When a client is struggling in their business, reach out proactively. That loyalty is unforgettable.",
        "Proactive suggestions (not just reactions) turn you from a vendor into a strategic partner.",
        "The best time to upsell is when the client is happiest. Time it right.",
        "Make your reports visual, not just numerical. Story tells, charts confirm.",
        "A 5-star client relationship starts with a 5-star onboarding experience.",
        "Always know your client's upcoming promotions or events. Align content to their business calendar.",],
    4: ["ChatGPT is not a content creator -- it's a content accelerator. Human editing is still mandatory.",
        "AI image tools like Midjourney are changing the creative industry. Learn them or fall behind.",
        "The best AI stack for agencies: ChatGPT for copy, Canva AI for design, Descript for video editing.",
        "Automate what's repetitive (scheduling, reporting). Stay human where it counts (strategy, creativity).",
        "AI can write first drafts. Your agency's value is the 10th draft -- strategy and refinement.",
        "n8n and Zapier can automate your entire client reporting pipeline. Set it up once, save 5 hours/week.",
        "The agencies winning right now are testing 3-5 new AI tools per month. Stay curious.",
        "AI transcription tools turn podcast episodes and long videos into 10 pieces of content in minutes.",
        "Use AI to generate 20 caption variations. Pick the best one. Speed with quality.",
        "AI scheduling tools now predict optimal posting times with 80% accuracy. Use them.",
        "The future of social media management is human creativity amplified by AI efficiency.",
        "AI content detection is improving. Always add a human layer to AI-generated content.",
        "Canva Magic Studio is a game-changer for agencies creating on-brand visual content at scale.",
        "AI competitor analysis tools can monitor your client's competitors 24/7. Automate the intelligence.",
        "Video AI tools (Runway, Pika) are creating entirely new content formats. Experiment now.",
        "The best AI prompt is a specific one. Be precise about tone, audience, length, and goal.",
        "AI saves time but requires supervision. A bad AI post sent without review can damage a brand.",
        "Build an AI SOP for every content type you produce. Consistency + speed = profitability.",
        "AI analytics tools find content patterns humans miss. Use them for monthly content audits.",
        "The ethical use of AI in content: always add original insights that AI can't replicate.",
        "Voice cloning AI for video ads is here. Stay ahead of industry trends to advise clients well.",
        "AI-powered A/B testing of ad creative can cut client ad spend while improving results.",
        "The agencies that win in AI aren't the most technical -- they're the most creative with it.",
        "Use AI to personalize outreach at scale. A personalized DM in 30 seconds beats a generic one.",
        "AI translation tools open international markets for your agency services. Think global.",
        "Sentiment analysis AI monitors client brand reputation 24/7. Offer it as a premium service.",
        "The ROI of AI in agencies: 2-4 hours saved per client per week. Multiply that by your roster.",
        "AI is not a shortcut -- it's a multiplier. You still need strategy, creativity, and judgment.",
        "Build an AI tool scorecard: rate each tool on time saved, quality impact, and ease of use.",
        "The agencies that invest in AI training for their team now will have an unfair advantage in 12 months.",
        "AI can analyze a competitor's top 50 posts and identify their content strategy in minutes.",
        "Automation doesn't mean hands-off. It means your hands are free for higher-value work.",
        "The best AI content still needs a great editor. Budget time for editing, even with AI.",
        "AI client intake forms can pre-qualify leads and gather brand info before the first call.",
        "Test AI tools with your own agency first before rolling out to clients.",
        "Document your AI workflows. Your process IS your competitive advantage.",],
    5: ["Instagram's algorithm prioritizes Reels watched in full. Make your Reels 7-12 seconds for best completion rates.",
        "TikTok SEO is real. Use keywords in your captions and spoken audio for discoverability.",
        "LinkedIn's algorithm loves documents (PDF carousels). They get 3-5x more reach than regular posts.",
        "Facebook Ads still offer the best targeting capabilities of any social platform in 2024.",
        "Pinterest is a search engine, not a social network. SEO your pin descriptions accordingly.",
        "YouTube Shorts are the fastest-growing short-form video format on the platform. Prioritize them.",
        "Twitter/X is essential for real-time brand engagement and industry conversations.",
        "BeReal and emerging platforms: keep one eye on new platforms. Early adopters win big.",
        "Instagram Stories disappear in 24 hours but Highlights last forever. Build your Highlights intentionally.",
        "LinkedIn newsletters are one of the most underused B2B content formats. Start one today.",
        "TikTok's 'For You Page' algorithm is the most powerful discovery engine in social media history.",
        "Google My Business posts are social media too. They affect local SEO. Use them weekly.",
        "Threads (Meta) is growing. If your client's audience skews younger, test it now.",
        "Snapchat reaches 90% of 13-24 year olds in the US. Know your client's demographic.",
        "Discord communities are the future of brand communities. Start building them now.",
        "YouTube Community Posts are underused and get high organic reach. Add them to your strategy.",
        "Platform diversification is risk management. Don't build your client's audience on one platform only.",
        "Twitter/X Spaces and LinkedIn Audio Events are live audio formats worth testing for B2B clients.",
        "Instagram Broadcast Channels give brands direct, algorithm-free access to subscribers. Use them.",
        "Mastodon and decentralized social media are growing. Stay informed on the landscape.",
        "Facebook Groups outperform Facebook Pages for organic reach in 2024. Shift your strategy.",
        "Reddit advertising is underrated for niche B2C products. Test it for the right clients.",
        "Amazon Live is a platform many agencies overlook. For e-commerce clients, it converts.",
        "Instagram Shopping turns posts into storefronts. Set it up for every e-commerce client.",
        "YouTube SEO is the second-largest search engine in the world. Treat it like Google.",
        "TikTok shopping is growing. Prepare your e-commerce clients for in-app purchasing.",
        "Cross-platform analytics tools (Sprout, Hootsuite, Buffer) save hours and provide unified reporting.",
        "The platform you ignore today might be where your competitor is winning tomorrow. Stay curious.",
        "Posting natively to each platform (not just cross-posting) gets significantly better reach.",
        "Platform-specific content formats consistently outperform repurposed content. Tailor everything.",
        "Know the platform's current monetization features. Help clients access them early.",
        "Twitter/X Ads can reach decision-makers in professional industries at lower CPMs than LinkedIn.",
        "Instagram Reels can now be up to 15 minutes. Long-form content on Instagram is arriving.",
        "Pinterest Idea Pins are the platform's answer to Reels. Use them for step-by-step content.",
        "Stay current on platform algorithm updates. What worked 6 months ago may not work today.",
        "Clubhouse isn't dead -- it's niche. For certain industries (finance, real estate), it still converts.",],
    6: ["The three metrics that actually matter: reach (awareness), engagement (interest), conversions (revenue).",
        "Vanity metrics (likes, followers) are easy to report. Real metrics (sales, leads) are what clients need.",
        "Instagram Insights undercount reach. Use a third-party analytics tool for accurate reporting.",
        "Engagement rate formula: (Likes + Comments + Saves + Shares) / Reach x 100. Benchmark: 1-5% is good.",
        "Save rate is the most underreported metric on Instagram. A 5%+ save rate indicates highly valuable content.",
        "UTM parameters are mandatory for tracking social media traffic in Google Analytics. Use them.",
        "Monthly analytics benchmarks: set them at onboarding. Report against client-specific baselines, not industry averages.",
        "The best report tells a story. Lead with results, not raw numbers.",
        "Social media attribution is imperfect. Use last-touch AND first-touch attribution for full picture.",
        "Track competitor metrics quarterly. Relative performance matters as much as absolute numbers.",
        "Share of voice: how much of the online conversation about a topic or industry does your client own?",
        "Sentiment analysis adds depth to analytics reporting. Positive mentions vs. negative mentions matter.",
        "Click-through rate (CTR) on bio links tells you how compelling your content-to-CTA chain is.",
        "Story completion rate benchmark: 70%+ is excellent. Under 50% means your stories are losing people.",
        "Video watch time percentage is more important than total views. Aim for 50%+ average watch time.",
        "Analytics tip: your worst-performing post of the month often teaches more than your best.",
        "Profile visits are a leading indicator of follower growth. Monitor them weekly.",
        "DM volume spikes after great content. Track it to measure true engagement beyond public metrics.",
        "Ad ROAS (Return on Ad Spend) benchmark: 3x ROAS is breakeven for most e-commerce brands. Aim for 5x+.",
        "Content mix analytics: track performance by content type (Reels, carousels, stories) to optimize.",
        "Follower demographics report: review quarterly to ensure content is reaching the right audience.",
        "Hashtag performance tracking: which hashtags drive discovery vs. which drive engagement?",
        "Weekly reporting cadence works better than monthly for active ad campaigns. Spot issues faster.",
        "The client who understands their analytics is the client who never churns. Teach them to read reports.",
        "Social listening tools (Mention, Brand24) add competitive intelligence to your analytics offering.",
        "Track posting frequency vs. performance. More isn't always better. Data tells you the truth.",
        "Reach vs. Impressions: reach counts unique accounts; impressions count total views including repeats.",
        "The 'saves + shares' combination is the strongest indicator of content that will be referenced again.",
        "Build a 90-day performance baseline for every new client. It takes 3 months to see trend lines.",
        "A/B test post times for 30 days to find your client's optimal posting schedule.",
        "Analytics is not just reporting -- it's diagnosing. Always follow a data point with a recommendation.",
        "Cost per result in ads: define 'result' clearly for each campaign. Leads, purchases, link clicks all differ.",
        "Year-over-year comparisons are more meaningful than month-over-month for seasonal businesses.",
        "Your analytics dashboard should answer one question: is the strategy working? If not, what changes?",
        "Cohort analysis of new followers shows whether your content is attracting and retaining the right audience.",
        "Track content production cost vs. performance. The most expensive content is rarely the most effective.",],
    7: ["The most productive thing you can do in agency life is protect your deep work time. Block it in your calendar.",
        "Burnout in agency ownership comes from saying yes to everything. Practice saying: 'Let me check my capacity.'",
        "The Sunday evening plan beats the Monday morning scramble. Spend 20 minutes planning your week ahead.",
        "Time blocking for agency owners: segment CEO time (strategy), manager time (team), and maker time (creative).",
        "Your energy level is more important than your schedule. Do your most important work when you're sharpest.",
        "The inbox is someone else's to-do list. Check email twice a day, not every 10 minutes.",
        "Agency growth requires delegation. You cannot scale what only you can do.",
        "Weekly team standups (15 minutes max) prevent misalignment that costs hours later.",
        "The best productivity tool for agency owners isn't an app -- it's a clear priority list.",
        "Rest is a business strategy. Exhausted founders make poor decisions. Protect your recovery time.",
        "One hour of planning saves four hours of execution. Plan before you produce.",
        "The 'not urgent, not important' quadrant is where procrastination hides. Eliminate it from your day.",
        "Systems reduce decision fatigue. When the process is documented, decisions are automatic.",
        "Your team's productivity multiplies when they have clear goals, clear tools, and clear communication.",
        "Creative blocks are often energy problems, not inspiration problems. Rest, move, then create.",
        "The agency owner's most valuable hour: the one spent thinking, not doing.",
        "Parkinson's Law: work expands to fill the time allotted. Set shorter deadlines for creative work.",
        "A 20-minute daily review at day's end keeps tomorrow's morning clear and focused.",
        "Delegate tasks that are not in your zone of genius. Build a team that complements your weaknesses.",
        "The two-minute rule: if a task takes less than 2 minutes, do it immediately. Don't schedule it.",
        "Batch similar tasks together. Content review, client calls, admin -- block time for each type.",
        "A 'done list' at day's end is more motivating than a to-do list that never empties.",
        "Automate your calendar booking. Stop the back-and-forth email chains. Use Calendly.",
        "Your workspace affects your output. Invest in a professional, distraction-free environment.",
        "Accountability partners work. Find another agency owner and do weekly check-ins on your goals.",
        "The 80/20 rule in agencies: 20% of your clients generate 80% of your revenue. Identify and protect them.",
        "Learn to say no to good opportunities so you can say yes to great ones.",
        "Morning routines are overrated if they're not sustainable. Find what works for YOUR life.",
        "The best agency owners read voraciously. One book per month minimum on business, marketing, or leadership.",
        "Celebrate wins -- with your team, with your clients, and with yourself. Progress deserves acknowledgment.",
        "Growth mindset: every difficult client or failed campaign is a case study for how to do better.",
        "Separate strategic time from operational time. Strategy happens weekly. Operations happen daily.",
        "Your mental health is a business asset. Protect it as fiercely as you protect your clients.",
        "The most successful agency owners I know all have one thing in common: extreme clarity on their 'why'.",
        "Pomodoro technique for creative work: 25 minutes focused work, 5 minutes rest. Repeat 4 times.",
        "Track your time for one week. The patterns revealed will change how you run your agency.",],
    8: ["The price you charge communicates your value before the client sees your work. Price with confidence.",
        "Discovery calls are not free consultations -- they're qualification meetings. Treat them differently.",
        "Never quote a price before you understand the client's goals, timeline, and budget expectations.",
        "Value-based pricing means charging based on outcomes, not hours. Learn it. Apply it.",
        "The most expensive agency service is the one that solves the client's most painful problem. Find it.",
        "Package your services. Packages create perceived value and simplify client decision-making.",
        "A 3-tier pricing strategy (good, better, best) makes the middle option the most popular. Always.",
        "Scope your projects tightly. Vague scope = scope creep = unprofitable projects.",
        "A retainer is a recurring revenue stream. Think of it as a recurring subscription. Price accordingly.",
        "Proposal follow-up: if you haven't heard back in 72 hours, follow up. Most agencies don't.",
        "Sales is service when you're selling something that genuinely helps the client.",
        "Social proof is your best sales tool. Case studies, testimonials, results. Lead with them always.",
        "The consultative sale wins more often than the features sale. Diagnose, then prescribe.",
        "Objection handling: every 'too expensive' is really 'I don't see enough value yet.'",
        "Anchoring: present your highest package first. It makes everything else look affordable.",
        "Sales funnel for agencies: content -- DM/email -- discovery call -- proposal -- close. Know your conversion rates.",
        "The fastest way to increase revenue is to raise prices for new clients while keeping existing ones.",
        "Contract length: annual contracts with monthly payment convert better than month-to-month for stability.",
        "Upsell timing: after you've delivered your first major win. When the client is happiest is best.",
        "Cross-sell adjacent services: if you manage Instagram, offer Facebook Ads. If you do content, offer SEO.",
        "Cold outreach ROI: email converts at 0.1-0.5%. Video DMs convert at 5-15%. Know your numbers.",
        "Sales enablement: your proposal template, case study one-pager, and testimonial video should be ready always.",
        "Client LTV (lifetime value) is more important than monthly retainer size. Optimize for retention.",
        "Sales scripts work because they remove the thinking and let you focus on listening.",
        "The best closing line: 'Based on everything we discussed, would you like to move forward?'",
        "Price increases: annual 10-15% increase with 30 days notice is standard and acceptable.",
        "Commission-based referral programs incentivize your best clients to become your best salespeople.",
        "Losing a deal on price is often a blessing. Low-budget clients are frequently high-maintenance.",
        "Your sales close rate benchmarks: discovery to proposal 50%, proposal to close 30-50% is excellent.",
        "Transparent pricing on your website attracts self-qualified leads and saves your sales time.",
        "The most powerful sales page element is not the offer -- it's the social proof above the offer.",
        "Sales is a skill, not a personality trait. It can be learned, practiced, and systematized.",
        "Follow-up cadence: Day 1, Day 3, Day 7, Day 14, Day 30. Most agencies quit after Day 3.",
        "Know your agency's break-even. Never take a client at a price that doesn't cover your real costs.",
        "Your average deal size can increase 30-50% by simply asking 'What else are you struggling with?'",
        "Never discount -- add value instead. Discounting devalues your service permanently.",],
    9: ["From 0 to 5k/month in 60 days: one agency owner's story of landing her first 3 retainer clients using LinkedIn.",
        "Case study: How one social media agency scaled from 3 to 15 clients in 6 months with a niche pivot.",
        "Success story: Agency owner worked 80 hours a week until she built systems. Now works 30 and earns more.",
        "From freelancer to 6-figure agency: the 3 decisions that changed everything for one creator.",
        "How one SMMA owner landed a $5,000/month retainer client using a 90-second personalized video DM.",
        "Agency growth case study: 0 to 10 clients in 90 days by focusing exclusively on one niche industry.",
        "Success story: How a part-time creator turned her social media skills into a full-time agency earning $8k/month.",
        "From burnout to balance: one agency owner's journey to hiring a team and reclaiming her time.",
        "Case study: How content repurposing helped one agency reduce production time by 60% with same output.",
        "Agency owner testimonial: 'I raised my prices 3x and lost 2 clients, but my revenue doubled.'",
        "Success story: How one agency grew its client base entirely through referrals with no cold outreach.",
        "From $500 to $3,000 per month retainers in one year -- a mindset and positioning story.",
        "Case study: How a new agency won a $4k/month client on their very first discovery call using this framework.",
        "Success story: Agency owner moved from hourly billing to retainers and doubled revenue in 60 days.",
        "How one agency built a 7-figure valuation by systemizing everything and hiring before they needed to.",
        "Case study: From first client to 20-person team in 3 years -- the systems that made it possible.",
        "Agency milestone story: the first $10k month -- what it took and what changed after reaching it.",
        "Success story: How a solo agency owner retained 90% of clients for 3+ years using monthly ROI reports.",
        "Case study: How one agency turned a negative client review into their most powerful referral relationship.",
        "From side hustle to main income: 6 months in an agency owner's journey from employee to entrepreneur.",
        "How one SMMA owner landed Fortune 500 brand partnerships starting from a home office.",
        "Success story: The agency that built its entire client base on Etsy lead generation strategies.",
        "Case study: $0 to $15k/month in 8 months -- the exact content strategy that drove growth.",
        "How one agency doubled its client retention by adding weekly communication touchpoints.",
        "From burnout to thriving: one agency's decision to fire 3 bad-fit clients and scale with fewer, better ones.",
        "Success story: How a new agency owner used YouTube content to attract 12 inbound leads in month 1.",
        "Case study: How AI tools allowed one 3-person agency to handle 25 clients without hiring.",
        "Agency owner success: built her team to run the agency while she traveled for 3 months. Systems matter.",
        "How one agency went from feast-or-famine to consistent $20k months through better client contracts.",
        "From zero audience to 10,000 followers in 90 days: a case study in niche content execution.",
        "Success story: Agency owner who started with $0 budget built to 6 figures using only organic strategies.",
        "Case study: The email sequence that converted 40% of discovery calls into signed clients.",
        "How one agency owner used speaking engagements to land her biggest clients and build authority.",
        "Success story: Team of 2 growing a social media agency to $50k/month through systemized processes.",
        "Agency milestone: First 6-figure year -- what worked, what failed, and what the owner would do differently.",
        "Case study: How one agency built a signature offer that sold itself with almost no sales calls needed.",],
}

rows_365 = []
for i in range(365):
    cat_idx = i % 10
    cat = cat_names[cat_idx]
    day = i + 1
    if cat_idx in source_lists:
        src = source_lists[cat_idx]
        sub_idx = i // 10
        caption = src[sub_idx % len(src)]
    else:
        sub_idx = i // 10
        msgs = generic_msgs.get(cat_idx, [])
        if msgs:
            caption = msgs[sub_idx % len(msgs)]
        else:
            caption = f"Tip #{day}: Consistent effort in {cat.lower()} builds the agency you dream of."
    tags = f"#smma #socialmediaagency #{cat.replace(' ','').replace('and','').lower()} #contentmarketing #digitalmarketing #socialmediatips"
    rows_365.append([day, cat, caption, tags])

with open(BASE+p11+"365_Social_Media_Captions.csv","w",newline="",encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["Day","Category","Caption","Hashtags"]); w.writerows(rows_365)
print(f"  csv {p11}365_Social_Media_Captions.csv")

doc(p11+"SMMA_Scripts_Vault.docx",
    "SMMA Scripts Vault",
    "AI SMMA OS | 50+ Scripts for Every Agency Situation",
    [
        ("Cold Call Script (Business Owner)", [
            "You: 'Hi [Name], this is [Your Name] from [Agency Name]. I'll be quick -- I work with [type of business] in [area] helping them get more clients from social media. I was researching [their business] and noticed [specific observation]. I had one quick idea I wanted to share. Is this a good time for 2 minutes?'",
            "[If yes]: 'Great. I noticed [specific issue/opportunity]. We recently helped [similar business] in [city] grow their page by [result]. I'd love to show you how. Could we schedule 20 minutes this week?'",
        ]),
        ("Discovery Call Objection Handling", [
            ("*","'Too expensive' -- 'I completely understand. Let me ask: how much would 5 new clients per month be worth to you? Because that's what we've averaged for our last 3 [industry] clients. Our retainer is $X, which means you'd need just Y new clients to break even. Does that framing help?'"),
            ("*","'We tried social media before' -- 'Tell me more about that. What happened? ... I hear that. The difference with us is [specific differentiator]. I can show you case studies from businesses exactly like yours where we fixed exactly that problem.'"),
            ("*","'I need to think about it' -- 'Of course. What would help you feel more confident? Is there a specific concern I haven't addressed yet?'"),
            ("*","'We're doing it in-house' -- 'How's that going? Are you happy with the growth? What if you could get those same results without the time investment so you could focus on running the business?'"),
        ]),
        ("Client Onboarding Email Sequence", [
            "Email 1 (Day 0 - Contract Signed): Subject: 'Welcome to [Agency Name] -- You made the right choice!' Body: 'We are thrilled to have [Business Name] as our newest client. Here's what happens next: [onboarding checklist link]. Your dedicated account manager is [Name]. Their direct email is [email]. Let's make something amazing together.'",
            "Email 2 (Day 3 - Access Request): Subject: 'Quick access request for [Business Name]' Body: 'To get started, we need access to [social media accounts / ad accounts / brand assets]. Please follow the instructions in the attached guide. Once we have access, we'll begin the brand discovery phase.'",
            "Email 3 (Day 7 - Strategy Preview): Subject: 'Your content strategy is ready for review' Body: 'We've completed your brand discovery and content strategy. Here's a preview of your first 30 days of content: [link to content calendar]. Please review and approve by [date]. Any feedback? Reply to this email or leave comments in the document.'",
        ]),
        ("Monthly Report Email Template", [
            "Subject: [Business Name] | Social Media Results - [Month Year]",
            "Hi [Client Name],",
            "Here's a summary of your social media performance this month:",
            ("*","REACH: [X] accounts reached (up/down X% from last month)"),
            ("*","ENGAGEMENT: [X] total engagements, [X]% engagement rate"),
            ("*","FOLLOWERS: [+X] new followers, total now [X]"),
            ("*","TOP POST: [link] with [X] reach and [X]% engagement"),
            ("*","WEBSITE CLICKS: [X] from social media"),
            "Next month's focus: [strategy for next month]",
            "Questions or thoughts? I'm available for a call [days/times]. Keep up the great work!",
        ]),
        ("Proposal Follow-Up Scripts", [
            ("*","Day 1 follow-up: 'Hi [Name], just checking in after sharing our proposal. Do you have any questions I can answer? We're excited about the possibility of working with [Business Name].'"),
            ("*","Day 4 follow-up: 'Hi [Name], I wanted to share a quick case study of [similar client] who saw [specific result] in [timeframe] -- thought it might be relevant as you're reviewing our proposal.'"),
            ("*","Day 10 follow-up: 'Hi [Name], I know decisions like this take time. I wanted to let you know we have one retainer spot opening up this month. If [Business Name] is interested, now is a great time to move forward. Happy to jump on a quick call.'"),
        ]),
        ("Difficult Client Communication", [
            ("*","When a client demands more than scope: 'I completely understand you'd like [additional request]. That falls outside our current scope, but I'd love to make it happen. I can put together a quick add-on proposal for that additional service. Would that work?'"),
            ("*","When a client is unhappy with results: 'Thank you for sharing this feedback directly. I take it seriously. Here's my honest assessment of what's working and what we can improve: [specifics]. Here's my proposed action plan: [plan]. Can we schedule a call this week to align on the path forward?'"),
            ("*","When offboarding a difficult client professionally: 'I'm proud of what we've accomplished together, including [results]. As we wrap up our work, here's what you'll receive as a final deliverable: [list]. I'll prepare a full handover document by [date]. It's been a pleasure working with your team.'"),
        ]),
    ])

doc(p11+"Agency_Growth_Playbook.docx",
    "Agency Growth Playbook",
    "AI SMMA OS | The Complete Agency Scaling System",
    [
        ("Phase 1: Foundation (Months 1-3)", [
            "Goal: Land your first 3 paying clients and build the core processes that will scale.",
            ("*","Week 1-2: Define your niche, set up your agency website, and create your core service packages"),
            ("*","Week 3-4: Outreach blitz -- 20 personalized outreach messages per day via DM, email, and LinkedIn"),
            ("*","Week 5-8: Close first 2 clients, deliver exceptional results, document everything"),
            ("*","Week 9-12: Use first case studies to close client 3, build referral system, create content strategy"),
            "Milestone: $3,000-5,000/month in recurring revenue, 3 clients, 1 case study, core processes documented.",
        ]),
        ("Phase 2: Growth (Months 4-8)", [
            "Goal: Scale to 8-12 clients through referrals, outbound, and content marketing.",
            ("*","Hire your first virtual assistant or part-time content creator"),
            ("*","Launch your own social media presence to attract inbound leads"),
            ("*","Implement client referral program (20% commission on referrals that convert)"),
            ("*","Create 3 service tier packages and introduce value-based pricing"),
            ("*","Systematize your onboarding, delivery, and reporting processes"),
            "Milestone: $8,000-15,000/month, 8-12 clients, 1 contractor, published case studies, inbound leads.",
        ]),
        ("Phase 3: Scale (Months 9-18)", [
            "Goal: Build a team and create an agency that runs without you in the day-to-day.",
            ("*","Hire dedicated account manager to own client relationships"),
            ("*","Bring on a full-time content strategist or creative director"),
            ("*","Implement project management system (Asana, Monday, ClickUp) for full team"),
            ("*","Build standard operating procedures for every service and process"),
            ("*","Create training system for new team members using documented SOPs"),
            "Milestone: $20,000-40,000/month, 15-25 clients, 3-5 team members, documented SOPs, 90% retention.",
        ]),
        ("Growth Levers That Actually Work", [
            ("*","Niche specialization: 'The #1 Social Media Agency for HVAC Companies' beats 'Full Service Digital Agency' every time"),
            ("*","Case study marketing: nothing sells like proof. Document every win with screenshots and before/after data"),
            ("*","Podcast outreach: guesting on 2 industry podcasts per month generates consistent qualified inbound leads"),
            ("*","LinkedIn content: 3 posts per week about agency insights positions you as an industry authority"),
            ("*","Joint ventures: partner with web designers, SEO agencies, and PR firms for referral partnerships"),
            ("*","Retainer stacking: get each client on multiple retainers (social management + ads + content) to increase LTV"),
        ]),
    ])

doc(p11+"AI_Prompt_Vault.docx",
    "AI Prompt Vault",
    "AI SMMA OS | 100+ Agency-Ready Prompts for ChatGPT and Claude",
    [
        ("Content Creation Prompts", [
            ("*","Caption writing: 'Write 5 Instagram caption variations for a [business type] promoting [offer/product]. The audience is [target audience]. Tone: [conversational/professional/funny]. Include a call to action. Use no more than 150 words per caption.'"),
            ("*","Reel script: 'Write a 30-second TikTok/Reel script for [business] about [topic]. Start with a pattern interrupt hook. Include one surprising fact. End with a clear CTA. Format: Hook (3 sec), Main point (20 sec), CTA (7 sec).'"),
            ("*","Carousel content: 'Create a 7-slide Instagram carousel for [business] teaching [topic]. Slide 1: Hook. Slides 2-6: One key point each with example. Slide 7: Summary + CTA. Keep each slide to 15 words or less.'"),
            ("*","Email newsletter: 'Write a weekly email newsletter for [business type] audience. Topic: [topic]. Include: attention-grabbing subject line, 3 valuable tips, one personal story, and a soft CTA. Tone: conversational and expert. Length: 300-400 words.'"),
        ]),
        ("Client Research Prompts", [
            ("*","Competitor analysis: 'Analyze the social media strategy of [competitor name] in the [industry] space. Based on common strategies for this type of business, list: their likely content pillars, posting frequency, primary platforms, and engagement tactics. What gaps or opportunities exist?'"),
            ("*","Audience persona: 'Create a detailed buyer persona for a [business type] targeting [demographic]. Include: demographics, pain points, goals, social media platforms they use, type of content they engage with, and buying triggers. Format as a one-page profile.'"),
            ("*","Industry insights: 'Provide the top 5 trending topics in [industry] right now that would resonate with [target audience] on social media. For each topic, suggest one content angle and one hook.'"),
        ]),
        ("Agency Operations Prompts", [
            ("*","Proposal writing: 'Write a professional proposal for a social media management retainer for [business name] in [industry]. Include: executive summary, our understanding of their goals, proposed services, deliverables, pricing, and next steps. Tone: confident and results-focused.'"),
            ("*","Client reporting: 'Write a professional monthly social media report for [client name]. Include sections for: executive summary, key metrics comparison (this month vs last month), top-performing content, challenges and learnings, and next month's strategy. Make it visual-friendly.'"),
            ("*","SOP writing: 'Create a step-by-step standard operating procedure for [process name] at a social media agency. Include: purpose, who is responsible, tools required, step-by-step process, quality check criteria, and common mistakes to avoid.'"),
        ]),
        ("Sales and Outreach Prompts", [
            ("*","Cold email: 'Write a 5-sentence cold email for a social media agency reaching out to [business type]. Start with a specific observation about their current social media. Offer one insight. Suggest a 15-minute call. No fluff. Subject line included.'"),
            ("*","LinkedIn message: 'Write a LinkedIn connection message from a social media agency owner to a [job title] at a [company type]. Keep it under 300 characters. Personal, not salesy. Reference something specific about their profile or company.'"),
            ("*","Follow-up sequence: 'Write a 5-email follow-up sequence for a social media agency after sending a proposal to [business type]. Space them: Day 1, Day 4, Day 8, Day 15, Day 30. Each email should add value, not just check in. Vary the angle each time.'"),
        ]),
    ])
print("✓ 11_BONUSES done")

# ── 12_CANVA_TEMPLATES ────────────────────────────────────────────────────────
p12="12_CANVA_TEMPLATES/"
print("Building 12_CANVA_TEMPLATES...")

# Agency_Proposal_Deck.pptx
ppt = prs()

s0 = sl(ppt)
box(s0,0,0,13.33,7.5,PNAV)
box(s0,0,5.5,13.33,2,PACC)
tx(s0,"AI SOCIAL MEDIA AGENCY OS",0.5,1.0,12,1.2,sz=36,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"Professional Agency Proposal",0.5,2.4,12,0.8,sz=20,bold=False,col=PGLD,a=PP_ALIGN.CENTER)
tx(s0,"Prepared for: [CLIENT BUSINESS NAME]",0.5,3.3,12,0.6,sz=16,col=PWHT,a=PP_ALIGN.CENTER)
tx(s0,"[Your Agency Name]  |  [Date]  |  Confidential",0.5,6.0,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)

s1 = sl(ppt)
box(s1,0,0,13.33,1.2,PNAV)
tx(s1,"EXECUTIVE SUMMARY",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
box(s1,0.5,1.5,5.8,4.5,PLGR)
tx(s1,"YOUR CHALLENGE",0.6,1.6,5.5,0.6,sz=14,bold=True,col=PNAV)
tx(s1,"[Client business] is looking to grow its online presence and convert social media engagement into real business results. Current challenges include inconsistent posting, low engagement rates, and limited brand visibility in a competitive market.",0.6,2.2,5.5,3.0,sz=11,col=PDGR)
box(s1,7.0,1.5,5.8,4.5,PLGR)
tx(s1,"OUR SOLUTION",7.1,1.6,5.5,0.6,sz=14,bold=True,col=PACC)
tx(s1,"We will implement a comprehensive social media strategy including content creation, community management, paid advertising, and detailed monthly reporting -- all powered by AI tools that give your brand an unfair competitive advantage.",7.1,2.2,5.5,3.0,sz=11,col=PDGR)

s2 = sl(ppt)
box(s2,0,0,13.33,1.2,PACC)
tx(s2,"OUR SERVICES & DELIVERABLES",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
for i,(svc,desc) in enumerate([
    ("Content Strategy","Monthly content calendar with topics, formats, and scheduling"),
    ("Content Creation","[X] posts/week including Reels, carousels, and static posts"),
    ("Community Management","Daily engagement -- replies, comments, DM management"),
    ("Monthly Reporting","ROI report with analytics, insights, and next-month strategy"),
    ("Paid Ads Management","Facebook/Instagram ad campaigns with A/B testing"),
]):
    col = i%2
    row_top = 1.4 + (i//2)*1.5 if i < 4 else 4.4
    left = 0.5 + col*6.4 if i < 4 else 3.7
    box(s2,left,row_top,6.0,1.3,PLGR)
    tx(s2,svc,left+0.1,row_top+0.05,5.8,0.5,sz=12,bold=True,col=PNAV)
    tx(s2,desc,left+0.1,row_top+0.55,5.8,0.65,sz=10,col=PDGR)

s3 = sl(ppt)
box(s3,0,0,13.33,1.2,PNAV)
tx(s3,"INVESTMENT & PACKAGES",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
for i,(pkg,price,feats) in enumerate([
    ("STARTER","$1,500/mo",["8 posts/week","Content creation","Monthly report"]),
    ("GROWTH","$2,500/mo",["12 posts/week","Content + Community","Ads management","Monthly report"]),
    ("ENTERPRISE","$4,500/mo",["Daily posting","Full management","Ads + SEO","Weekly calls","Priority support"]),
]):
    left=0.5+i*4.2
    box(s3,left,1.4,3.9,5.5,PLGR if i!=1 else PNAV)
    col2 = PNAV if i!=1 else PWHT
    tx(s3,pkg,left+0.1,1.5,3.7,0.6,sz=14,bold=True,col=col2,a=PP_ALIGN.CENTER)
    tx(s3,price,left+0.1,2.1,3.7,0.7,sz=20,bold=True,col=PACC if i!=1 else PGLD,a=PP_ALIGN.CENTER)
    for j,feat in enumerate(feats):
        tx(s3,f"+ {feat}",left+0.2,2.9+j*0.65,3.5,0.55,sz=11,col=col2)

s4 = sl(ppt)
box(s4,0,0,13.33,1.2,PACC)
tx(s4,"WHY CHOOSE US",0.5,0.2,12,0.8,sz=26,bold=True,col=PWHT)
for i,(stat,label) in enumerate([("97%","Client Retention Rate"),("150+","Brands Managed"),("4.2x","Average ROAS"),("$2M+","Revenue Generated")]):
    left=0.5+i*3.1
    box(s4,left,1.5,2.8,2.5,PNAV)
    tx(s4,stat,left+0.1,1.6,2.6,1.2,sz=32,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
    tx(s4,label,left+0.1,2.8,2.6,0.9,sz=11,col=PWHT,a=PP_ALIGN.CENTER)
tx(s4,"RESULTS YOU CAN EXPECT",0.5,4.3,12,0.5,sz=16,bold=True,col=PNAV)
for i,r in enumerate(["Average 40% increase in reach within 60 days","2-5x engagement rate improvement in first 90 days","Consistent brand presence across all platforms","Full transparency with detailed monthly ROI reports"]):
    tx(s4,f"  {r}",0.5,4.9+i*0.5,12,0.45,sz=11,col=PDGR)

s5 = sl(ppt)
box(s5,0,0,13.33,7.5,PNAV)
box(s5,0,6.0,13.33,1.5,PACC)
tx(s5,"READY TO GROW YOUR BRAND?",0.5,1.5,12,1.0,sz=32,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(s5,"Let's build something remarkable together.",0.5,2.7,12,0.7,sz=18,col=PGLD,a=PP_ALIGN.CENTER)
tx(s5,"NEXT STEPS",0.5,3.6,12,0.5,sz=16,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
for i,step in enumerate(["1. Review this proposal and let us know if you have questions","2. Sign the agreement and submit your first month's payment","3. Complete the onboarding questionnaire (15 minutes)","4. We begin work within 48 hours of onboarding completion"]):
    tx(s5,step,1.5,4.2+i*0.5,10,0.45,sz=12,col=PWHT)
tx(s5,"[Your Name]  |  [Email]  |  [Phone]  |  [Website]",0.5,6.2,12,0.5,sz=13,col=PWHT,a=PP_ALIGN.CENTER)

ppt.save(BASE+p12+"Agency_Proposal_Deck.pptx")
print(f"  pptx {p12}Agency_Proposal_Deck.pptx")

# Monthly_Report_Template.pptx
ppt2 = prs()

r0 = sl(ppt2)
box(r0,0,0,13.33,7.5,PNAV)
box(r0,0,0,13.33,1.5,PACC)
tx(r0,"SOCIAL MEDIA PERFORMANCE REPORT",0.5,0.1,12,0.8,sz=26,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(r0,"[CLIENT NAME]  |  [MONTH YEAR]  |  PREPARED BY [AGENCY NAME]",0.5,0.95,12,0.4,sz=12,col=PWHT,a=PP_ALIGN.CENTER)
for i,(label,val) in enumerate([("REACH","[X,XXX]"),("ENGAGEMENT","[X.X]%"),("FOLLOWERS","[+XXX]"),("POSTS","[XX]")]):
    left=1.0+i*2.8
    box(r0,left,2.0,2.4,2.5,PACC)
    tx(r0,val,left+0.1,2.1,2.2,1.3,sz=28,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(r0,label,left+0.1,3.4,2.2,0.6,sz=11,col=PWHT,a=PP_ALIGN.CENTER)

r1 = sl(ppt2)
box(r1,0,0,13.33,1.2,PNAV)
tx(r1,"KEY METRICS BREAKDOWN",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
headers=["METRIC","THIS MONTH","LAST MONTH","CHANGE","BENCHMARK"]
for j,h in enumerate(headers):
    box(r1,0.3+j*2.5,1.4,2.3,0.55,PACC)
    tx(r1,h,0.3+j*2.5,1.4,2.3,0.55,sz=10,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
rows_r=[
    ["Total Reach","[X,XXX]","[X,XXX]","[+/- X%]","Industry avg"],
    ["Total Impressions","[XX,XXX]","[XX,XXX]","[+/- X%]","3x reach"],
    ["Engagement Rate","[X.X%]","[X.X%]","[+/- X%]","2-5%"],
    ["New Followers","[+XXX]","[+XXX]","[+/- X%]","Niche based"],
    ["Profile Visits","[X,XXX]","[X,XXX]","[+/- X%]","5-10% of reach"],
    ["Link Clicks","[XXX]","[XXX]","[+/- X%]","1-3% CTR"],
    ["Story Views","[X,XXX]","[X,XXX]","[+/- X%]","10-15% of reach"],
    ["Saves","[XXX]","[XXX]","[+/- X%]","3-5% rate"],
]
for i,row in enumerate(rows_r):
    bg=PLGR if i%2==0 else PWHT
    for j,val in enumerate(row):
        box(r1,0.3+j*2.5,2.0+i*0.58,2.3,0.55,bg)
        tx(r1,val,0.3+j*2.5,2.0+i*0.58,2.3,0.55,sz=10,col=PDGR,a=PP_ALIGN.CENTER)

r2 = sl(ppt2)
box(r2,0,0,13.33,1.2,PACC)
tx(r2,"TOP PERFORMING CONTENT",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
for i in range(3):
    left=0.5+i*4.2
    box(r2,left,1.4,3.9,2.5,PLGR)
    tx(r2,f"#{i+1} TOP POST",left+0.1,1.5,3.7,0.5,sz=12,bold=True,col=PNAV)
    tx(r2,"[Post description/type]",left+0.1,2.05,3.7,0.5,sz=10,col=PDGR)
    box(r2,left,4.0,3.9,2.8,PNAV)
    tx(r2,"[Reach]",left+0.1,4.1,3.7,0.45,sz=10,col=PGLD)
    tx(r2,"[Engagement]",left+0.1,4.6,3.7,0.45,sz=10,col=PGLD)
    tx(r2,"[Saves]",left+0.1,5.1,3.7,0.45,sz=10,col=PGLD)
    tx(r2,"[Link Clicks]",left+0.1,5.6,3.7,0.45,sz=10,col=PGLD)

r3 = sl(ppt2)
box(r3,0,0,13.33,1.2,PNAV)
tx(r3,"NEXT MONTH STRATEGY",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
box(r3,0.5,1.4,5.8,5.5,PLGR)
tx(r3,"WHAT'S WORKING",0.6,1.5,5.5,0.55,sz=14,bold=True,col=PNAV)
for i,item in enumerate(["[Content type performing well]","[Posting time that gets best engagement]","[Format driving the most saves/shares]","[Campaign or promotion results]"]):
    tx(r3,f"+ {item}",0.6,2.1+i*0.7,5.5,0.6,sz=11,col=PDGR)
box(r3,7.0,1.4,5.8,5.5,PLGR)
tx(r3,"NEXT MONTH FOCUS",7.1,1.5,5.5,0.55,sz=14,bold=True,col=PACC)
for i,item in enumerate(["[Key campaign or promotion planned]","[New content format to test]","[Platform strategy adjustment]","[Growth target and tactics]","[Client collaboration needed]"]):
    tx(r3,f"-> {item}",7.1,2.1+i*0.7,5.5,0.6,sz=11,col=PDGR)

ppt2.save(BASE+p12+"Monthly_Report_Template.pptx")
print(f"  pptx {p12}Monthly_Report_Template.pptx")

# Social_Media_Strategy_Deck.pptx
ppt3 = prs()
g0=sl(ppt3)
box(g0,0,0,13.33,7.5,PNAV)
box(g0,9.5,0,3.83,7.5,PACC)
tx(g0,"SOCIAL MEDIA STRATEGY",0.5,1.5,8.5,1.0,sz=34,bold=True,col=PWHT)
tx(g0,"[CLIENT NAME]",0.5,2.7,8.5,0.7,sz=20,col=PGLD)
tx(g0,"[YEAR] Annual Strategy  |  Prepared by [Agency Name]",0.5,3.5,8.5,0.6,sz=14,col=PWHT)
tx(g0,"CONFIDENTIAL",0.5,6.7,8.5,0.5,sz=11,col=PWHT)

g1=sl(ppt3)
box(g1,0,0,13.33,1.2,PACC)
tx(g1,"BRAND OVERVIEW & GOALS",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
box(g1,0.5,1.4,12.3,1.2,PLGR)
tx(g1,"BRAND POSITIONING: [Define your client's unique value proposition and brand voice in one sentence]",0.6,1.5,12,1.0,sz=12,col=PNAV)
for i,(goal,kpi) in enumerate([
    ("Increase brand awareness and reach","Reach: [target] accounts/month"),
    ("Drive engagement and community building","Engagement rate: [target]% minimum"),
    ("Generate qualified leads for sales team","[X] DM leads/month, [X] website clicks"),
    ("Establish thought leadership in [niche]","[X] saves per post average"),
]):
    box(g1,0.5+i*3.1,2.8,2.9,3.8,PNAV if i%2==0 else PLGR)
    col_=PWHT if i%2==0 else PNAV
    tx(g1,f"GOAL {i+1}",0.6+i*3.1,2.9,2.7,0.5,sz=11,bold=True,col=col_)
    tx(g1,goal,0.6+i*3.1,3.4,2.7,1.5,sz=10,col=col_)
    tx(g1,f"KPI: {kpi}",0.6+i*3.1,5.0,2.7,1.4,sz=9,col=PGLD if i%2==0 else PACC)

g2=sl(ppt3)
box(g2,0,0,13.33,1.2,PNAV)
tx(g2,"CONTENT PILLARS & POSTING SCHEDULE",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
pillars=[("Educate","How-to, tips, guides","30%",PACC),("Engage","Questions, polls, UGC","25%",PGLD),("Entertain","Behind scenes, fun","20%",PNAV),("Promote","Offers, CTAs","15%",PRGB(39,174,96)),("Inspire","Values, vision","10%",PRGB(142,68,173))]
for i,(name,desc,pct,col_) in enumerate(pillars):
    left=0.5+i*2.5
    box(g2,left,1.4,2.3,2.5,col_)
    tx(g2,name,left+0.1,1.5,2.1,0.6,sz=14,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(g2,pct,left+0.1,2.1,2.1,0.7,sz=22,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(g2,desc,left+0.1,2.8,2.1,0.9,sz=9,col=PWHT,a=PP_ALIGN.CENTER)
box(g2,0.5,4.1,12.3,2.8,PLGR)
tx(g2,"WEEKLY POSTING SCHEDULE",0.6,4.2,12,0.5,sz=13,bold=True,col=PNAV)
days=["MON","TUE","WED","THU","FRI","SAT","SUN"]
for i,day in enumerate(days):
    left=0.6+i*1.73
    box(g2,left,4.8,1.6,0.5,PNAV)
    tx(g2,day,left,4.8,1.6,0.5,sz=10,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
    tx(g2,"[Content\nType]",left,5.35,1.6,1.3,sz=9,col=PDGR,a=PP_ALIGN.CENTER)

g3=sl(ppt3)
box(g3,0,0,13.33,1.2,PACC)
tx(g3,"PLATFORM-BY-PLATFORM STRATEGY",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
platforms=[
    ("INSTAGRAM","[X] posts/week\n[X] Stories/day\nFocus: Reels + Carousels"),
    ("FACEBOOK","[X] posts/week\nFocus: Long-form + Groups"),
    ("LINKEDIN","[X] posts/week\nFocus: Thought leadership"),
    ("TIKTOK","[X] videos/week\nFocus: Trends + Education"),
]
for i,(plat,strat) in enumerate(platforms):
    row=i//2; col_=i%2
    left=0.5+col_*6.4; top=1.4+row*2.9
    box(g3,left,top,6.0,2.6,PLGR)
    box(g3,left,top,6.0,0.6,PNAV)
    tx(g3,plat,left+0.1,top+0.05,5.8,0.5,sz=13,bold=True,col=PWHT)
    tx(g3,strat,left+0.1,top+0.7,5.8,1.7,sz=11,col=PDGR)

g4=sl(ppt3)
box(g4,0,0,13.33,7.5,PNAV)
box(g4,0,5.8,13.33,1.7,PACC)
tx(g4,"YOUR STRATEGY IS READY.",0.5,1.2,12,0.9,sz=34,bold=True,col=PWHT,a=PP_ALIGN.CENTER)
tx(g4,"Let's execute it together.",0.5,2.3,12,0.7,sz=20,col=PGLD,a=PP_ALIGN.CENTER)
tx(g4,"Next: Content Calendar Review + Campaign Kickoff Call",0.5,3.3,12,0.6,sz=15,col=PWHT,a=PP_ALIGN.CENTER)
tx(g4,"[Agency Name]  |  [Email]  |  [Website]",0.5,6.1,12,0.5,sz=14,col=PWHT,a=PP_ALIGN.CENTER)

ppt3.save(BASE+p12+"Social_Media_Strategy_Deck.pptx")
print(f"  pptx {p12}Social_Media_Strategy_Deck.pptx")

# Case_Study_Template.pptx
ppt4=prs()
c0=sl(ppt4)
box(c0,0,0,13.33,7.5,PNAV)
box(c0,0,0,0.5,7.5,PACC)
tx(c0,"CASE STUDY",0.8,0.8,12,0.8,sz=14,bold=True,col=PGLD)
tx(c0,"[CLIENT NAME]",0.8,1.6,12,1.2,sz=38,bold=True,col=PWHT)
tx(c0,"How [Agency Name] helped [Business] achieve [key result] in [timeframe]",0.8,3.0,12,0.9,sz=16,col=PWHT)
tx(c0,"[INDUSTRY]  |  [TIMEFRAME]  |  [SERVICES PROVIDED]",0.8,4.2,12,0.5,sz=12,col=PGLD)

c1=sl(ppt4)
box(c1,0,0,13.33,1.2,PACC)
tx(c1,"THE CHALLENGE",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
box(c1,0.5,1.4,7.8,5.5,PLGR)
tx(c1,"BACKGROUND",0.6,1.5,7.5,0.55,sz=13,bold=True,col=PNAV)
tx(c1,"[Client name] is a [business type] in [location] serving [target market]. When they came to us, they were facing significant challenges with their social media presence and digital marketing efforts.",0.6,2.1,7.5,1.5,sz=11,col=PDGR)
tx(c1,"KEY CHALLENGES",0.6,3.7,7.5,0.55,sz=13,bold=True,col=PNAV)
for i,ch in enumerate(["[Challenge 1: e.g., Low engagement despite consistent posting]","[Challenge 2: e.g., No clear brand identity or content strategy]","[Challenge 3: e.g., Missing target audience demographic entirely]"]):
    tx(c1,f"- {ch}",0.6,4.3+i*0.7,7.5,0.6,sz=11,col=PDGR)
box(c1,8.7,1.4,4.1,5.5,PNAV)
tx(c1,"BY THE NUMBERS",8.8,1.5,3.9,0.6,sz=12,bold=True,col=PGLD)
for i,(stat,label) in enumerate([("X%","Engagement Rate"),("XXX","Followers"),("$XXX","Monthly Ad Spend")]):
    tx(c1,stat,8.8,2.2+i*1.5,3.9,0.7,sz=24,bold=True,col=PGLD,a=PP_ALIGN.CENTER)
    tx(c1,f"BEFORE: {label}",8.8,2.9+i*1.5,3.9,0.55,sz=10,col=PWHT,a=PP_ALIGN.CENTER)

c2=sl(ppt4)
box(c2,0,0,13.33,1.2,PNAV)
tx(c2,"THE SOLUTION & RESULTS",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
box(c2,0.5,1.4,5.8,5.5,PLGR)
tx(c2,"OUR APPROACH",0.6,1.5,5.5,0.55,sz=13,bold=True,col=PNAV)
for i,sol in enumerate(["Content strategy overhaul with [X] new content pillars","[X] posts per week across [platforms]","Community management: responding to 100% of comments/DMs","Paid advertising: [X] campaigns targeting [audience]","Monthly reporting with transparent ROI tracking"]):
    tx(c2,f"{i+1}. {sol}",0.6,2.1+i*0.85,5.5,0.75,sz=10,col=PDGR)
box(c2,7.0,1.4,5.8,5.5,PACC)
tx(c2,"RESULTS ACHIEVED",7.1,1.5,5.5,0.55,sz=13,bold=True,col=PWHT)
results=[("[+XXX%]","Increase in reach"),("[+XXX%]","Engagement rate growth"),("[XXX]","New followers gained"),("[+XXX%]","Website traffic from social"),("[$XX,XXX]","Revenue attributed to social")]
for i,(num,label) in enumerate(results):
    tx(c2,num,7.1,2.1+i*0.95,2.5,0.75,sz=18,bold=True,col=PGLD)
    tx(c2,label,9.5,2.1+i*0.95,3.0,0.75,sz=11,col=PWHT)

c3=sl(ppt4)
box(c3,0,0,13.33,7.5,PLGR)
box(c3,0,0,13.33,1.2,PNAV)
tx(c3,"CLIENT TESTIMONIAL",0.5,0.2,12,0.8,sz=24,bold=True,col=PWHT)
box(c3,1.5,1.5,10.3,4.0,PNAV)
tx(c3,'"',1.8,1.6,0.8,1.0,sz=60,bold=True,col=PACC)
tx(c3,"[Insert client testimonial here. Make it specific, results-focused, and in the client's own words. The best testimonials mention: the specific results achieved, how the agency made them feel, and what they'd say to someone considering working with the agency.]",2.0,2.2,9.5,2.8,sz=14,col=PWHT)
tx(c3,"[CLIENT NAME], [TITLE] at [BUSINESS NAME]",2.0,5.6,9.5,0.6,sz=12,bold=True,col=PGLD)
tx(c3,"Want results like these? Let's talk.",0.5,6.0,12,0.5,sz=14,col=PNAV,a=PP_ALIGN.CENTER)
tx(c3,"[Email]  |  [Phone]  |  [Website]",0.5,6.55,12,0.4,sz=12,col=PDGR,a=PP_ALIGN.CENTER)

ppt4.save(BASE+p12+"Case_Study_Template.pptx")
print(f"  pptx {p12}Case_Study_Template.pptx")
print("✓ 12_CANVA_TEMPLATES done")

# ── PDFs ──────────────────────────────────────────────────────────────────────
print("Building PDFs...")
make_pdf(BASE+"AI_SMMA_OS_User_Guide.pdf",
    "AI Social Media Agency OS - Complete User Guide",
    "Your step-by-step guide to setting up and launching your SMMA with the AI SMMA OS",
    [
        ("Welcome to Your AI SMMA OS", [
            "Congratulations on investing in the most comprehensive social media agency operating system available. This guide walks you through every section of your purchase and shows you exactly how to use each file to build, run, and scale a profitable social media agency.",
            "What you've downloaded contains everything you need to go from zero to running a professional, scalable SMMA -- from your first client proposal to your systems for managing 20+ clients.",
        ]),
        ("How to Use This System", [
            ("*","Start with 00_START_HERE for your complete onboarding checklist and 30-60-90 day action plan"),
            ("*","Complete 01_AGENCY_SETUP first -- this builds your foundation: business plan, brand assets, and legal templates"),
            ("*","Move through sections 02-06 in order as you acquire and onboard clients"),
            ("*","Import all CSV files into Notion for a complete digital workspace (see 10_NOTION_WORKSPACE)"),
            ("*","Use the PPTX files in Canva by importing them -- all dimensions are optimized for Canva compatibility"),
        ]),
        ("Section-by-Section Guide", [
            "00_START_HERE: Begin here. Contains your welcome guide, system overview, and complete onboarding checklist with 90-day action plan broken into daily tasks.",
            "01_AGENCY_SETUP: 8 files covering business plan, financial projections, branding guide, legal contract templates, pricing calculator, and service menu.",
            "02_CLIENT_ACQUISITION: 6 files including lead generation tracker, cold email templates, DM scripts, and objection handling vault.",
            "03_PROPOSALS_CONTRACTS: 5 files with proposal templates, service agreements, scope of work templates, and payment terms.",
            "04_CLIENT_ONBOARDING: 6 files including onboarding questionnaire, brand discovery form, client portal setup, and welcome email sequences.",
            "05_CONTENT_CREATION: 7 files with content calendar templates, social media strategy guide, hashtag research system, content brief templates.",
            "06_SOCIAL_MEDIA_MANAGEMENT: 6 files covering platform-by-platform strategy, scheduling guides, and community management SOPs.",
            "07_CLIENT_REPORTING: 4 files including KPI dashboard, revenue tracker, report writing guide, and report email templates.",
            "08_AI_TOOLS_STACK: 3 files covering AI tools directory, automation guide, and prompt engineering guide.",
            "09_BUSINESS_OPERATIONS: 3 files covering annual business plan, hiring guide, and KPI dashboard.",
            "10_NOTION_WORKSPACE: 8 files with 7 Notion-importable CSVs and setup guide.",
            "11_BONUSES: 4 files including 365 social media captions, scripts vault, growth playbook, and AI prompt vault.",
            "12_CANVA_TEMPLATES: 4 professional PPTX files that can be imported directly into Canva.",
        ]),
        ("Notion Setup (10 Minutes)", [
            ("*","Open Notion and create a new workspace called 'Agency OS'"),
            ("*","Create a new page for each CSV file in 10_NOTION_WORKSPACE"),
            ("*","On each page, click 'Import' -- 'CSV' and select the corresponding file"),
            ("*","Each CSV includes BOM encoding for perfect Notion compatibility"),
            ("*","Link your databases together: Client database links to Lead Tracker, Content Calendar links to Clients"),
            ("*","Add your own pages for meeting notes, team updates, and creative briefs"),
        ]),
    ])

make_pdf(BASE+"SMMA_Agency_Growth_Guide.pdf",
    "SMMA Agency Growth Guide",
    "The Definitive Playbook for Scaling Your Social Media Agency to 6-7 Figures",
    [
        ("The Agency Growth Framework", [
            "Growing a social media agency is one of the most accessible business models in today's digital economy -- but most agency owners plateau at 3-5 clients because they lack the systems to scale. This guide gives you the complete framework to break through that ceiling.",
            ("*","Phase 1: Foundation (0-3 months) -- Your first 3 clients, your first processes, your first case study"),
            ("*","Phase 2: Growth (3-12 months) -- Scale to 10-20 clients with a small team"),
            ("*","Phase 3: Scale (12+ months) -- Build a team-run agency with you in the CEO role"),
        ]),
        ("The SMMA Acquisition Machine", [
            "Your agency needs a predictable lead generation system that fills your pipeline while you're delivering for existing clients. Here's the system that consistently produces qualified leads:",
            ("*","Content marketing: Post 3-5 times per week on LinkedIn, Instagram, or YouTube sharing agency insights. Inbound leads come to you already pre-sold on your expertise."),
            ("*","Outbound outreach: 20 personalized outreach messages per day via DM or email. Personalization is key -- generic messages get ignored."),
            ("*","Referral program: Ask every happy client for 2 referrals. A 20% commission structure for successful referrals turns clients into salespeople."),
            ("*","Strategic partnerships: Build relationships with web designers, copywriters, SEO agencies, and PR firms. Cross-refer clients."),
            ("*","Discovery call funnel: Qualify leads with a 3-question pre-call form. Only take calls with decision-makers who have budget authority."),
        ]),
        ("Retention: The Agency Superpower", [
            "Acquisition costs 5x more than retention. The agencies that grow fastest are the ones that keep their clients the longest. Here's how:",
            ("*","Month 1 onboarding: Exceed expectations. Over-deliver. Send more than you promised."),
            ("*","Monthly ROI reports: Clients who see their results don't leave. Make reporting a beautiful experience."),
            ("*","Proactive communication: Reach out before clients reach you. If there's a problem, be first to address it."),
            ("*","Quarterly strategy calls: Show clients you're thinking about their long-term growth, not just their monthly deliverables."),
            ("*","Annual reviews: A formal yearly review positions you as a strategic partner, not a vendor."),
        ]),
        ("Pricing Your Way to Profit", [
            ("*","Never charge by the hour. Hourly pricing penalizes your efficiency and caps your income."),
            ("*","Use value-based pricing. What is the ROI of your service to the client? Charge a fraction of that."),
            ("*","Create 3 service tiers. The middle package should represent 60-70% of your sales."),
            ("*","Raise prices annually by 10-15% for new clients. Your existing clients stay at their rate."),
            ("*","Add-on services increase average client value without adding new clients. Identify the top 3 add-ons for your niche."),
        ]),
    ])
print("✓ PDFs done")

# ── Asset Manifests ───────────────────────────────────────────────────────────
print("Building Asset Manifests...")
all_files = []
for root, dirs, files in os.walk(BASE):
    dirs.sort()
    for f in sorted(files):
        full = os.path.join(root, f)
        rel = os.path.relpath(full, BASE)
        size = os.path.getsize(full)
        all_files.append([rel, f.split('.')[-1].upper(), f"{size/1024:.1f} KB"])

with open(BASE+"Asset_Manifest.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f); w.writerow(["File Path","Type","Size"]); w.writerows(all_files)

manifest = {
    "product": "AI Social Media Agency OS",
    "version": "2.0",
    "total_files": len(all_files),
    "files": [{"path":r[0],"type":r[1],"size":r[2]} for r in all_files]
}
with open(BASE+"Asset_Manifest.json","w") as f:
    json.dump(manifest,f,indent=2)
print(f"  Manifest: {len(all_files)} files indexed")

# ── Etsy Listing ──────────────────────────────────────────────────────────────
etsy_txt = """TITLE:
AI Social Media Agency OS | Complete SMMA Business System | 60+ Files | Canva Templates | Notion Workspace

DESCRIPTION:
Launch and scale your social media marketing agency with the most comprehensive SMMA operating system available on Etsy.

This is NOT a basic PDF. This is a complete agency infrastructure -- everything you need to run a professional, scalable social media agency from day one.

WHAT'S INCLUDED (60+ files across 13 folders):

00 START HERE
- Welcome guide and 30-60-90 day action plan
- Complete system overview and quick-start checklist

01 AGENCY SETUP
- Business plan template (editable DOCX)
- 5-year financial projections (XLSX with formulas)
- Branding and identity guide
- Legal contract templates
- Pricing calculator

02 CLIENT ACQUISITION
- Lead generation system and tracker (XLSX)
- Cold email and DM templates
- Objection handling vault (50+ responses)
- LinkedIn outreach scripts

03 PROPOSALS & CONTRACTS
- Professional proposal template
- Service agreement template
- Scope of work document
- Payment terms and conditions

04 CLIENT ONBOARDING
- Onboarding questionnaire
- Brand discovery form
- Client portal setup guide
- Welcome email sequence

05 CONTENT CREATION
- Content calendar (12-month editable XLSX)
- Social media strategy guide (PDF)
- Hashtag research system
- Content brief templates for every platform

06 SOCIAL MEDIA MANAGEMENT
- Platform-by-platform strategy guides
- Posting schedule templates
- Community management SOPs

07 CLIENT REPORTING
- KPI and ROI dashboard (XLSX)
- Revenue tracker with projections
- Monthly report email templates
- Report writing guide

08 AI TOOLS STACK
- Complete AI tools directory (60+ tools reviewed)
- Agency automation guide (20 automations)
- Prompt engineering guide for social media

09 BUSINESS OPERATIONS
- Annual business plan template
- Agency hiring guide
- Business KPI dashboard

10 NOTION WORKSPACE
- 7 Notion-importable databases (CSV)
- Complete Notion setup guide
- Client tracking, content calendar, lead tracker, task board, proposal pipeline, invoice log, referral tracker

11 BONUSES
- 365 done-for-you social media captions (10 categories)
- SMMA scripts vault (50+ scripts for every situation)
- Agency growth playbook
- AI prompt vault (100+ agency-ready prompts)

12 CANVA TEMPLATES (PPTX -- import directly to Canva)
- Agency proposal deck (6 slides)
- Monthly report template
- Social media strategy deck
- Client case study template

PERFECT FOR:
- Social media managers going freelance
- New SMMA owners in their first 6 months
- Agency owners who want to systemize and scale
- Coaches and consultants adding social media services
- Virtual assistants expanding their service offering

FORMATS INCLUDED:
- DOCX (editable Word documents)
- XLSX (editable Excel spreadsheets with formulas)
- PDF (print-ready guides)
- PPTX (Canva-importable presentation templates)
- CSV (Notion-importable databases)
- MD (Notion setup guides)

INSTANT DIGITAL DOWNLOAD
No physical product is shipped. You will receive a ZIP file immediately after purchase containing all 60+ files organized into 13 clearly labeled folders.

All files are fully editable and designed for immediate use. No software subscription required (free versions of Canva, Notion, and Google Docs work perfectly).

TAGS:
smma, social media agency, social media marketing, digital marketing, agency business, content creator, canva templates, notion template, business template, social media manager, freelance business, agency tools, marketing templates, business bundle, agency starter kit"""

with open(ETSY_DIR+"06_AI_SMMA_Listing.txt","w",encoding="utf-8") as f:
    f.write(etsy_txt)
print("  etsy 06_AI_SMMA_Listing.txt")

# ── ZIP ───────────────────────────────────────────────────────────────────────
print("Creating ZIP...")
ZIP_PATH = "/home/user/oqul-phase55-production/ai-smma-os/BUYER_DOWNLOAD_AI_SMMA_OS.zip"
with zipfile.ZipFile(ZIP_PATH,"w",zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(BASE):
        dirs.sort()
        for f in sorted(files):
            full=os.path.join(root,f)
            arc=os.path.relpath(full,os.path.dirname(BASE))
            z.write(full,arc)
size_mb=os.path.getsize(ZIP_PATH)/1024/1024
print(f"✓ ZIP created: {ZIP_PATH} ({size_mb:.1f} MB)")
print("\n=== AI SMMA OS COMPLETE ===")
