#!/usr/bin/env node
/**
 * OQUL EdTech OS — Premium Product Package Generator
 * Generates all PDF files using Playwright (Chromium pre-installed)
 */
import { chromium } from 'playwright';
import { mkdir, writeFile, readFile } from 'fs/promises';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { existsSync } from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const OUTPUT_DIR = join(__dirname, 'output');

// Import all document modules
import { cover } from './src/docs/cover.mjs';
import { welcome } from './src/docs/welcome.mjs';
import { readMeFirst } from './src/docs/read-me-first.mjs';
import { installationGuide } from './src/docs/installation-guide.mjs';
import { folderGuide } from './src/docs/folder-guide.mjs';
import { quickStart } from './src/docs/quick-start.mjs';
import { businessOverview } from './src/docs/business-overview.mjs';
import { faq } from './src/docs/faq.mjs';
import { license } from './src/docs/license.mjs';
import { supportGuide } from './src/docs/support-guide.mjs';
import { versionHistory } from './src/docs/version-history.mjs';
import { changelog } from './src/docs/changelog.mjs';
import { assetManifest } from './src/docs/asset-manifest.mjs';
import { productRoadmap } from './src/docs/product-roadmap.mjs';

const DOCS = [
  cover,
  welcome,
  readMeFirst,
  installationGuide,
  folderGuide,
  quickStart,
  businessOverview,
  faq,
  license,
  supportGuide,
  versionHistory,
  changelog,
  assetManifest,
  productRoadmap,
];

// Additional output folders
const FOLDER_STRUCTURE = [
  '00_START_HERE',
  '01_INSTALLATION',
  '02_DOCUMENTATION',
  '03_TEMPLATES/Word_Documents',
  '03_TEMPLATES/Google_Sheets',
  '03_TEMPLATES/Canva',
  '03_TEMPLATES/Notion',
  '04_LEGAL',
  '05_SUPPORT',
  '06_META',
];

async function ensureDir(dir) {
  if (!existsSync(dir)) {
    await mkdir(dir, { recursive: true });
  }
}

async function generatePDF(page, doc, outputPath) {
  await page.setContent(doc.html, {
    waitUntil: 'networkidle',
    timeout: 30000,
  });

  // Wait for fonts to load
  await page.waitForTimeout(1500);

  await page.pdf({
    path: outputPath,
    format: 'A4',
    printBackground: true,
    margin: { top: '0mm', right: '0mm', bottom: '0mm', left: '0mm' },
  });
}

async function createGoogleSheetsTemplates(outputDir) {
  const sheetsDir = join(outputDir, '03_TEMPLATES', 'Google_Sheets');

  // KPI Dashboard CSV
  const kpiCSV = `KPI Dashboard — OQUL EdTech OS,,,,
Last Updated:,=TODAY(),,Sheet by OQUL v1.0,
,,,,
MONTHLY OVERVIEW,,,,
Metric,Current Month,Previous Month,Change (%),Status
Total Active Students,0,0,=IF(B6=0,0,(B6-C6)/MAX(C6,1)*100),=IF(E6>=0,"↑ Growth","↓ Decline")
New Registrations (Month),0,0,=IF(B7=0,0,(B7-C7)/MAX(C7,1)*100),=IF(E7>=0,"↑ Growth","↓ Decline")
Paid Subscribers,0,0,=IF(B8=0,0,(B8-C8)/MAX(C8,1)*100),=IF(E8>=0,"↑ Growth","↓ Decline")
Monthly Revenue (€),0,0,=IF(B9=0,0,(B9-C9)/MAX(C9,1)*100),=IF(E9>=0,"↑ Growth","↓ Decline")
Churn Rate (%),0,0,=IF(B10=0,0,(B10-C10)/MAX(C10,1)*100),=IF(E10<=0,"↑ Improved","↓ Worsened")
AI Sessions (Leila),0,0,=IF(B11=0,0,(B11-C11)/MAX(C11,1)*100),=IF(E11>=0,"↑ Growth","↓ Decline")
Avg Session Duration (min),0,0,=IF(B12=0,0,(B12-C12)/MAX(C12,1)*100),=IF(E12>=0,"↑ Growth","↓ Decline")
Lessons Completed,0,0,=IF(B13=0,0,(B13-C13)/MAX(C13,1)*100),=IF(E13>=0,"↑ Growth","↓ Decline")
,,,,
REVENUE BREAKDOWN,,,,
Tier,Subscribers,Price (€),Revenue (€),% of Total
Free,0,0,=B17*C17,=IF(SUM(D17:D20)=0,0,D17/SUM(D17:D20)*100)
Student (Individual),0,14,=B18*C18,=IF(SUM(D17:D20)=0,0,D18/SUM(D17:D20)*100)
Family Plan,0,29,=B19*C19,=IF(SUM(D17:D20)=0,0,D19/SUM(D17:D20)*100)
School License,0,0,=B20*C20,=IF(SUM(D17:D20)=0,0,D20/SUM(D17:D20)*100)
TOTAL,=SUM(B17:B20),,=SUM(D17:D20),100%
,,,,
COST TRACKING,,,,
Cost Center,Monthly (€),Annual Est. (€),Notes,
Server / Hosting,0,=B24*12,VPS or cloud hosting,
Groq API,0,=B25*12,AI inference costs,
Email Service,0,=B26*12,SMTP provider,
Domain & SSL,0,=B27*12,Annual cost / 12,
Marketing,0,=B28*12,Ads content tools,
TOTAL COSTS,=SUM(B24:B28),=SUM(C24:C28),,
,,,,
NET MONTHLY,=D21-B29,,,`;

  await writeFile(join(sheetsDir, 'KPI_Dashboard.csv'), kpiCSV);

  // Revenue Tracker CSV
  const revenueCSV = `Revenue Tracker — OQUL EdTech OS v1.0,,,,,
,,,,,,
ANNUAL REVENUE TRACKER,,,,,
Month,New Students,Active Students,Revenue (€),Expenses (€),Net Profit (€)
January 2026,0,0,0,0,=D4-E4
February 2026,0,=C4+B5,0,0,=D5-E5
March 2026,0,=C5+B6,0,0,=D6-E6
April 2026,0,=C6+B7,0,0,=D7-E7
May 2026,0,=C7+B8,0,0,=D8-E8
June 2026,0,=C8+B9,0,0,=D9-E9
July 2026,0,=C9+B10,0,0,=D10-E10
August 2026,0,=C10+B11,0,0,=D11-E11
September 2026,0,=C11+B12,0,0,=D12-E12
October 2026,0,=C12+B13,0,0,=D13-E13
November 2026,0,=C13+B14,0,0,=D14-E14
December 2026,0,=C14+B15,0,0,=D15-E15
TOTALS,=SUM(B4:B15),=AVERAGE(C4:C15),=SUM(D4:D15),=SUM(E4:E15),=SUM(F4:F15)`;

  await writeFile(join(sheetsDir, 'Revenue_Tracker.csv'), revenueCSV);

  // Student Analytics CSV
  const analyticsCSV = `Student Analytics — OQUL EdTech OS v1.0,,,,
,,,,
STUDENT PERFORMANCE TRACKER,,,,
Student ID,Name,Grade Level,Lessons Completed,Avg Score (%),Streak (Days),Last Active,Status
S001,,Grade 1,0,0,0,,Active
S002,,Grade 1,0,0,0,,Active
S003,,Grade 2,0,0,0,,Active
,,,,
SUBJECT PERFORMANCE,,,,
Subject,Students,Avg Score,Completion Rate,Trend
Arabic Language,0,0,0%,—
Mathematics,0,0,0%,—
French,0,0,0%,—
Science,0,0,0%,—
,,,,
ENGAGEMENT METRICS,,,,
Metric,Week 1,Week 2,Week 3,Week 4,Monthly Avg
Daily Active Users,0,0,0,0,=AVERAGE(B18:E18)
Sessions per User,0,0,0,0,=AVERAGE(B19:E19)
Avg Session Length (min),0,0,0,0,=AVERAGE(B20:E20)
Lessons Completed,0,0,0,0,=AVERAGE(B21:E21)`;

  await writeFile(join(sheetsDir, 'Student_Analytics.csv'), analyticsCSV);

  // Google Sheets setup guide
  const setupGuide = `GOOGLE SHEETS SETUP GUIDE
OQUL EdTech OS v1.0

HOW TO IMPORT CSV FILES INTO GOOGLE SHEETS
==========================================

1. Open Google Drive (drive.google.com)
2. Click "+ New" → "File upload"
3. Upload the CSV file (e.g., KPI_Dashboard.csv)
4. Right-click the uploaded file → "Open with Google Sheets"
5. Google Sheets will convert the CSV and preserve formulas

ENABLING FORMULAS
================
After import, verify formulas are active:
- Click any cell containing "=SUM" or "=IF"
- Press F2 to edit, then Enter to confirm
- If formulas show as text, go to Format → Number → Automatic

RECOMMENDED FORMATTING
======================
- Freeze Row 1: View → Freeze → 1 row
- Add header background: select Row 1, fill with #2563EB, text color white
- Column widths: expand all columns for readability (double-click column borders)
- Enable alternating colors: Format → Alternating colors

SHARING WITH YOUR TEAM
=======================
- Click "Share" in top-right
- Add team member emails
- Set permission: "Viewer" for dashboards, "Editor" for trackers
- Always keep one "master" copy that only you can edit

CONNECTING TO OQUL DATA
========================
For advanced users: use Google Sheets' IMPORTDATA function or Google Apps Script
to automatically pull data from your OQUL PostgreSQL database via an API endpoint.
The platform exposes analytics data at: /api/analytics/export (requires auth token)
`;

  await writeFile(join(sheetsDir, 'Google_Sheets_Setup_Guide.txt'), setupGuide);
}

async function createWordTemplates(outputDir) {
  const wordDir = join(outputDir, '03_TEMPLATES', 'Word_Documents');

  // Create RTF files (compatible with Word) for each template
  const proposalRTF = createRTFDocument('Client Proposal Template', `
OQUL PLATFORM PARTNERSHIP PROPOSAL

Prepared for: [Client School / Organization Name]
Prepared by: [Your Name / Company]
Date: [Date]

═══════════════════════════════════════════════════

EXECUTIVE SUMMARY
─────────────────
We propose a partnership to deploy OQUL — an AI-powered adaptive learning platform — for [Client Name]'s students. This platform provides personalized AI tutoring, tracks progress in real-time, and aligns to the official curriculum.

THE CHALLENGE
─────────────
[Client Name] students face challenges including:
• [Challenge 1 — e.g., limited personalized tutoring support]
• [Challenge 2 — e.g., difficulty preparing for national exams]
• [Challenge 3 — e.g., no real-time visibility for parents and teachers]

OUR SOLUTION
────────────
OQUL EdTech OS provides:
✓ AI tutor (Leila) available 24/7 in Arabic, French, and Darija
✓ Adaptive learning paths personalized to each student
✓ Full K–12 curriculum aligned to Ministry of Education standards
✓ Parent dashboard with real-time progress monitoring
✓ Gamification system to maintain student engagement

INVESTMENT
──────────
[Tier Name]: [Price per student per month]
Minimum commitment: [X] students
Contract term: [12 months / 6 months]
Total investment: [Calculate]

NEXT STEPS
──────────
1. Sign this proposal to initiate onboarding
2. Complete student enrollment via bulk CSV upload
3. Admin training session (2 hours)
4. Go-live within 5 business days

═══════════════════════════════════════════════════
Signature: _______________________  Date: __________
`);

  await writeFile(join(wordDir, 'Client_Proposal_Template.rtf'), proposalRTF);

  const contractRTF = createRTFDocument('Service Contract Template', `
SERVICE AGREEMENT

This Service Agreement ("Agreement") is entered into as of [Date] between:

Service Provider: [Your Company Name], ("Provider")
Client: [Client Name], ("Client")

SERVICES
────────
Provider agrees to provide the following services:
• Access to OQUL EdTech OS platform for [Number] student accounts
• AI tutoring sessions via Leila AI tutor
• Parent monitoring portal access
• Platform maintenance and uptime (99% SLA)
• Monthly progress reports
• Email support during business hours

PAYMENT TERMS
─────────────
• Subscription fee: [€X] per student per month
• Billing cycle: Monthly, due on the 1st of each month
• Payment method: Bank transfer / Credit card
• Late payment: 1.5% monthly interest after 15 days

TERM & TERMINATION
──────────────────
• Term: [Start Date] to [End Date] (12 months)
• Either party may terminate with 30 days written notice
• No refunds for partial months upon termination

CONFIDENTIALITY
───────────────
Both parties agree to maintain confidentiality of all student data in compliance with applicable privacy laws, including GDPR where applicable.

LIMITATION OF LIABILITY
───────────────────────
Provider's liability is limited to the amount paid in the preceding 3 months.

SIGNATURES
──────────
Provider: ________________________  Date: ____________
Client:   ________________________  Date: ____________
`);

  await writeFile(join(wordDir, 'Service_Contract_Template.rtf'), contractRTF);

  const onboardingRTF = createRTFDocument('Student Onboarding Pack', `
WELCOME TO OQUL!
Your AI-Powered Learning Journey Starts Here

Dear [Student Name],

Welcome to OQUL — your personal AI learning companion. This pack contains everything you need to get started on your educational journey.

YOUR ACCOUNT DETAILS
────────────────────
Email: [student@email.com]
Temporary Password: [provided by admin]
Platform URL: [your-platform.com]

MEET LEILA — YOUR AI TUTOR
───────────────────────────
Leila is your AI study companion. She:
✓ Teaches in Arabic, French, and Darija
✓ Adapts to YOUR pace and style
✓ Is available 24/7 — no waiting
✓ Remembers what you've learned
✓ Celebrates your progress

YOUR FIRST WEEK CHECKLIST
──────────────────────────
□ Log in and complete your profile
□ Take the placement assessment (10 minutes)
□ Complete your first lesson with Leila
□ Set your daily study goal
□ Share your parent's email for progress reports
□ Join your first daily challenge

EARN REWARDS
────────────
• Complete lessons → Earn XP points
• Study 3 days in a row → Unlock a streak badge
• Score 90%+ → Earn a gold star
• Reach Level 5 → Unlock special achievements

STUDY TIPS FROM LEILA
─────────────────────
"Start with 15 minutes a day. Consistency is more important than long sessions.
Ask me anything you don't understand — I'll explain it in a way that makes sense to you!"

PARENT INFORMATION
──────────────────
Your parent/guardian can monitor your progress at:
[your-platform.com/parent]
They'll receive weekly progress emails automatically.

Questions? Ask Leila! She's available in the chat anytime you're logged in.

بالتوفيق! — Good luck! — Bonne chance!
`);

  await writeFile(join(wordDir, 'Student_Onboarding_Pack.rtf'), onboardingRTF);
}

function createRTFDocument(title, content) {
  const escapedContent = content
    .replace(/\\/g, '\\\\')
    .replace(/\{/g, '\\{')
    .replace(/\}/g, '\\}')
    .split('\n')
    .join('\\par\n');

  return `{\\rtf1\\ansi\\deff0
{\\fonttbl{\\f0 Arial;}{\\f1 Courier New;}}
{\\colortbl;\\red37\\green99\\blue235;\\red15\\green23\\blue42;\\red16\\green185\\blue129;}
\\f0\\fs24
{\\b\\fs36\\cf2 ${title.replace(/[{}\\]/g, '')}\\par}
\\par
${escapedContent}
}`;
}

async function createNotionTemplates(outputDir) {
  const notionDir = join(outputDir, '03_TEMPLATES', 'Notion');

  const notionGuide = `NOTION WORKSPACE SETUP GUIDE
OQUL EdTech OS v1.0
=====================================

HOW TO SET UP YOUR OQUL NOTION WORKSPACE
=========================================

STEP 1: DUPLICATE THE TEMPLATE
--------------------------------
1. Open the Notion template link provided with your purchase
2. Click "Duplicate" in the top-right corner
3. Select your Notion workspace
4. The template will copy to your workspace

STEP 2: WORKSPACE MODULES
--------------------------
Your OQUL Notion workspace includes these pages:

📋 OQUL OPERATIONS HUB (Main Dashboard)
  └─ Navigation to all other sections
  └─ Quick Stats overview
  └─ This week's priorities

👥 STUDENT CRM DATABASE
  └─ Student Name, Email, Grade Level
  └─ Subscription Tier, Join Date
  └─ Last Active, Total Lessons, Progress Score
  └─ Parent Contact, Notes
  └─ Views: All Students | Active | At-Risk | Premium

📅 CONTENT CALENDAR
  └─ Monthly content planning
  └─ Social media posts, emails, webinars
  └─ Status: Draft | Scheduled | Published
  └─ Views: Calendar | Board | Table

📚 SOP LIBRARY DATABASE
  └─ 40+ Standard Operating Procedures
  └─ Category: Operations | Marketing | Finance | HR | Technical
  └─ Owner, Last Updated, Version
  └─ Linked to: Team Handbook

👔 TEAM MANAGEMENT
  └─ Staff & tutor roster
  └─ Role, Department, Start Date
  └─ Performance metrics
  └─ Leave tracker
  └─ Linked to: SOPs

💰 FINANCE DASHBOARD
  └─ Monthly revenue tracking
  └─ Expense categories
  └─ Student tier breakdown
  └─ Profit/Loss summary
  └─ Linked charts (import from Google Sheets)

📈 90-DAY GROWTH TRACKER
  └─ Week-by-week milestones
  └─ Acquisition goals
  └─ Revenue targets
  └─ Progress: Not Started | In Progress | Done | Blocked

STEP 3: CUSTOMIZE YOUR WORKSPACE
----------------------------------
After duplicating:
1. Replace [Your Company Name] in the cover pages
2. Update brand colors in Gallery covers (use #2563EB for primary)
3. Add your team members to the Team database
4. Import your first students into the CRM
5. Customize SOP categories to match your workflow

STEP 4: CONNECT DATABASES
---------------------------
The template uses Notion Relations to connect:
- Students ↔ Content Calendar (which content students see)
- SOPs ↔ Team (who owns each procedure)
- Finance ↔ Students (revenue attribution)

NOTION PRO TIPS
---------------
• Use /template buttons to create recurring content
• Filter database views by status for daily focus
• Use @-mentions to link pages and databases
• Export to PDF for professional client reports
• Enable Notion AI for summarizing student progress notes

TEMPLATE LINK
-------------
[Your Notion template link is provided in your purchase confirmation email]
`;

  await writeFile(join(notionDir, 'Notion_Workspace_Guide.txt'), notionGuide);

  const sopDatabase = `OQUL SOP LIBRARY — NOTION DATABASE EXPORT
==========================================
Use this to populate your Notion SOP Library database.

SOP-001 | Student Onboarding Process | Operations | Active
Standard procedure for onboarding new students: account creation, placement assessment, first session, parent notification.

SOP-002 | Monthly Billing Cycle | Finance | Active
Process for collecting subscription payments, handling failed payments, and generating receipts.

SOP-003 | Parent Communication Protocol | Operations | Active
When and how to communicate with parents: weekly reports, concern escalation, celebration milestones.

SOP-004 | AI Tutor Performance Review | Technical | Active
Monthly review of Leila AI response quality, accuracy checking, and prompt optimization.

SOP-005 | New Curriculum Content Addition | Technical | Active
Process for adding new lessons to the curriculum registry, QA checking, and deployment.

SOP-006 | Student At-Risk Identification | Operations | Active
How to identify students with declining engagement, intervention steps, and escalation protocol.

SOP-007 | Subscription Cancellation Handling | Finance | Active
Steps to handle cancellation requests: save attempt, exit survey, account suspension, data retention.

SOP-008 | Platform Incident Response | Technical | Active
Emergency response procedure when platform experiences downtime or critical bugs.

SOP-009 | Social Media Content Creation | Marketing | Active
Weekly content creation workflow for Instagram, LinkedIn, and TikTok educational posts.

SOP-010 | B2B School Partnership Outreach | Marketing | Active
Step-by-step process for prospecting, contacting, pitching, and closing school partnerships.

SOP-011 | Tutor/Content Creator Hiring | HR | Active
Job posting, screening, interview, trial project, and onboarding process for new team members.

SOP-012 | Monthly Financial Close | Finance | Active
End-of-month process for reconciling revenue, categorizing expenses, and generating P&L report.

SOP-013 | Student Feedback Collection | Operations | Active
How to collect NPS scores, session feedback, and feature requests from students and parents.

SOP-014 | AI Prompt Library Update | Technical | Active
Process for adding, testing, and deploying new prompts for Leila's teaching scenarios.

SOP-015 | Platform Security Audit | Technical | Active
Quarterly security review checklist: dependency updates, access review, log audit, pen test.
`;

  await writeFile(join(notionDir, 'SOP_Library_Database.txt'), sopDatabase);
}

async function createCanvaGuide(outputDir) {
  const canvaDir = join(outputDir, '03_TEMPLATES', 'Canva');

  const canvaGuide = `CANVA TEMPLATES GUIDE
OQUL EdTech OS v1.0
==============================================

YOUR 12 CANVA TEMPLATES
========================

Template links are provided in your purchase confirmation email.
Each template is fully editable in Canva (free account works for most features).

1. CLIENT PROPOSAL DECK (16:9 Presentation — 20 slides)
   Purpose: Present OQUL to schools, parents, investors
   Key slides: Problem, Solution, Curriculum overview, Pricing, Next steps
   Colors: Navy (#0F172A) + Blue (#2563EB) on white
   How to use: Duplicate → Replace [Company Name] → Add your logo

2. WELCOME PACKET (A4 Document — 6 pages)
   Purpose: First document new students/parents receive
   Key sections: Welcome, Platform overview, How-to guide, Contact
   Colors: Clean white with blue accents
   How to use: Download as PDF after customizing

3. MONTHLY PROGRESS REPORT (A4 Document — 4 pages)
   Purpose: Monthly student progress report for parents
   Key sections: Stats summary, Subject breakdown, Achievements, Goals
   Colors: Professional white/gray with green accents
   How to use: Customize stats monthly, download PDF, email to parents

4. BUSINESS PRESENTATION (16:9 — 30 slides)
   Purpose: Investor/partner pitches
   Key slides: Market size, Product demo, Team, Financials, Ask
   Colors: Dark navy theme, premium feel
   How to use: Full pitch deck, customize financial slides with your data

5. CASE STUDY (A4 — 2 pages)
   Purpose: Showcase student success stories
   Key sections: Student background, Challenge, Solution, Results
   Colors: Light background, photo-friendly layout
   How to use: One per featured student, collect testimonials

6. LEAD MAGNET (A4 PDF — 8 pages)
   Purpose: Free resource to grow email list
   Title: "5 Ways AI is Transforming Education in Morocco"
   Colors: Bold brand colors, attention-grabbing
   How to use: Download → Share via landing page / social media

7. INSTAGRAM CAROUSEL (1:1 Square — 7 slides)
   Purpose: Educational content for Instagram
   Topics: Study tips, AI facts, Curriculum insights, Student wins
   Colors: Vibrant brand colors, thumb-stopping design
   How to use: Post 1 carousel per week for organic growth

8. LINKEDIN CAROUSEL (4:5 Portrait — 8 slides)
   Purpose: Thought leadership content for LinkedIn
   Topics: EdTech insights, Parent tips, Platform features
   Colors: Professional dark theme
   How to use: Target parents, teachers, school administrators

9. INVOICE TEMPLATE (A4 — 1 page)
   Purpose: Professional invoice for subscription payments
   Key fields: Client name, subscription tier, amount, bank details
   Colors: Clean minimal with brand accents
   How to use: Customize per client, download PDF

10. CERTIFICATE OF COMPLETION (Landscape A4 — 1 page)
    Purpose: Reward students who complete a curriculum module
    Key elements: Student name, module completed, date, signature line
    Colors: Gold and navy, premium feel
    How to use: Award monthly to motivate continued learning

11. BUSINESS REPORT (A4 — 8 pages)
    Purpose: Annual/quarterly business performance report
    Key sections: YoY growth, Revenue breakdown, Product updates, Goals
    Colors: Executive dark navy theme
    How to use: Annual investor update or internal review

12. BRAND BOARD (Square — 1 page)
    Purpose: Quick reference for OQUL brand identity
    Shows: Logo, colors, fonts, icons, usage examples
    Colors: All brand colors shown
    How to use: Share with freelancers/agencies for consistency

BRAND COLORS FOR CANVA
=======================
Primary Blue:    #2563EB
Secondary Dark:  #0F172A
Accent Green:    #10B981
Background:      #F8FAFC
White:           #FFFFFF
Border Gray:     #E5E7EB

FONTS IN CANVA
==============
Headings: Poppins Bold / Poppins ExtraBold
Body:     Inter Regular / Inter Medium
Numbers:  Inter SemiBold

HOW TO APPLY BRAND COLORS
==========================
1. Select any element in Canva
2. Click the color swatch
3. Click "+" to add a new color
4. Paste the hex code (e.g., 2563EB)
5. Click "Add to brand kit" to save for future use

CANVA PRO VS FREE
=================
Free Canva: Access to templates, basic editing, PNG/PDF export
Canva Pro: Brand kits, Magic Resize (resize for all platforms at once),
           Background remover, Team collaboration, Unlimited storage

Recommendation: Start with free, upgrade to Pro when you have 3+ team members.
`;

  await writeFile(join(canvaDir, 'Canva_Templates_Guide.txt'), canvaGuide);
}

async function generateAllPDFs() {
  console.log('\n🚀 OQUL EdTech OS — Premium Product Package Generator\n');
  console.log('═'.repeat(55));

  // Create all output directories
  console.log('\n📁 Creating folder structure...');
  for (const folder of FOLDER_STRUCTURE) {
    await ensureDir(join(OUTPUT_DIR, folder));
  }
  console.log('   ✓ All folders created\n');

  // Generate PDFs
  console.log('📄 Launching Chromium for PDF generation...');
  const browser = await chromium.launch({
    executablePath: process.env.PLAYWRIGHT_BROWSERS_PATH
      ? `${process.env.PLAYWRIGHT_BROWSERS_PATH}/chromium`
      : undefined,
  });

  const context = await browser.newContext();
  const page = await context.newPage();

  console.log('   ✓ Browser ready\n');
  console.log('🖨️  Generating PDFs...\n');

  const results = [];

  for (const doc of DOCS) {
    const docOutputDir = join(OUTPUT_DIR, doc.outputDir);
    await ensureDir(docOutputDir);
    const outputPath = join(docOutputDir, doc.filename);

    process.stdout.write(`   → ${doc.filename.padEnd(40)} `);

    try {
      await generatePDF(page, doc, outputPath);
      console.log('✅ Done');
      results.push({ file: doc.filename, status: 'success', path: outputPath });
    } catch (err) {
      console.log(`❌ Failed: ${err.message}`);
      results.push({ file: doc.filename, status: 'failed', error: err.message });
    }
  }

  await browser.close();
  console.log('\n📊 Creating Google Sheets templates...');
  await createGoogleSheetsTemplates(OUTPUT_DIR);
  console.log('   ✓ KPI_Dashboard.csv created');
  console.log('   ✓ Revenue_Tracker.csv created');
  console.log('   ✓ Student_Analytics.csv created');

  console.log('\n📝 Creating Word document templates...');
  await createWordTemplates(OUTPUT_DIR);
  console.log('   ✓ Client_Proposal_Template.rtf created');
  console.log('   ✓ Service_Contract_Template.rtf created');
  console.log('   ✓ Student_Onboarding_Pack.rtf created');

  console.log('\n🗂️  Creating Notion workspace templates...');
  await createNotionTemplates(OUTPUT_DIR);
  console.log('   ✓ Notion_Workspace_Guide.txt created');
  console.log('   ✓ SOP_Library_Database.txt created');

  console.log('\n🎨 Creating Canva templates guide...');
  await createCanvaGuide(OUTPUT_DIR);
  console.log('   ✓ Canva_Templates_Guide.txt created');

  // Print summary
  const succeeded = results.filter(r => r.status === 'success').length;
  const failed = results.filter(r => r.status === 'failed').length;

  console.log('\n' + '═'.repeat(55));
  console.log(`\n✅ Generation Complete!\n`);
  console.log(`   PDFs generated:  ${succeeded}/${DOCS.length}`);
  if (failed > 0) {
    console.log(`   ⚠️  Failed:        ${failed}`);
    results.filter(r => r.status === 'failed').forEach(r => {
      console.log(`      - ${r.file}: ${r.error}`);
    });
  }
  console.log(`\n   📦 Output: ${OUTPUT_DIR}`);
  console.log('\n' + '═'.repeat(55) + '\n');
}

generateAllPDFs().catch(err => {
  console.error('\n❌ Generator failed:', err);
  process.exit(1);
});
