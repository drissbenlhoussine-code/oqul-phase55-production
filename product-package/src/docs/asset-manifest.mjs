import { brand, pageLayout } from '../brand.mjs';

export const assetManifest = {
  filename: 'Asset_Manifest.pdf',
  outputDir: '06_META',
  html: pageLayout({
    title: 'Asset Manifest',
    docLabel: 'Asset Manifest',
    pageNum: '12',
    content: `
    <h1 class="section-title">Asset Manifest</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:16px;">Complete inventory of every file and resource included in OQUL EdTech OS v1.0. Use this to verify your download is complete.</p>

    <div class="icon-stat-row">
      <div class="icon-stat">
        <span class="stat-icon">📄</span>
        <div class="stat-val">12</div>
        <div class="stat-label">PDF Files</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">📝</span>
        <div class="stat-val">5</div>
        <div class="stat-label">DOCX Templates</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">📊</span>
        <div class="stat-val">3</div>
        <div class="stat-label">Spreadsheets</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">🎨</span>
        <div class="stat-val">12</div>
        <div class="stat-label">Canva Templates</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">🗂️</span>
        <div class="stat-val">461</div>
        <div class="stat-label">Source Files</div>
      </div>
    </div>

    <div class="section-break"><h2>PDF Documents</h2></div>
    <table>
      <thead><tr><th>#</th><th>Filename</th><th>Folder</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td>1</td><td>00_Cover.pdf</td><td>00_START_HERE</td><td>Product visual identity and overview</td></tr>
        <tr><td>2</td><td>01_Welcome.pdf</td><td>00_START_HERE</td><td>What's included and first steps</td></tr>
        <tr><td>3</td><td>02_Read_Me_First.pdf</td><td>00_START_HERE</td><td>Essential context and prerequisites</td></tr>
        <tr><td>4</td><td>04_Folder_Guide.pdf</td><td>00_START_HERE</td><td>Package navigation guide</td></tr>
        <tr><td>5</td><td>03_Installation_Guide.pdf</td><td>01_INSTALLATION</td><td>Full setup walkthrough</td></tr>
        <tr><td>6</td><td>05_Quick_Start_Guide.pdf</td><td>01_INSTALLATION</td><td>Fast-track installation</td></tr>
        <tr><td>7</td><td>FAQ.pdf</td><td>05_SUPPORT</td><td>Frequently asked questions</td></tr>
        <tr><td>8</td><td>Support_Guide.pdf</td><td>05_SUPPORT</td><td>How to get help</td></tr>
        <tr><td>9</td><td>License.pdf</td><td>04_LEGAL</td><td>End user license agreement</td></tr>
        <tr><td>10</td><td>Version_History.pdf</td><td>06_META</td><td>Complete development history</td></tr>
        <tr><td>11</td><td>Changelog.pdf</td><td>06_META</td><td>Detailed change log</td></tr>
        <tr><td>12</td><td>Asset_Manifest.pdf</td><td>06_META</td><td>This document</td></tr>
        <tr><td>13</td><td>Product_Roadmap.pdf</td><td>06_META</td><td>Future features and phases</td></tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Word Document Templates (DOCX)</h2></div>
    <table>
      <thead><tr><th>Filename</th><th>Folder</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td>Client_Proposal_Template.docx</td><td>03_TEMPLATES/Word_Documents</td><td>Professional proposal for school partnerships</td></tr>
        <tr><td>Service_Contract_Template.docx</td><td>03_TEMPLATES/Word_Documents</td><td>Service agreement template</td></tr>
        <tr><td>Student_Onboarding_Pack.docx</td><td>03_TEMPLATES/Word_Documents</td><td>New student welcome materials</td></tr>
        <tr><td>Team_Handbook.docx</td><td>03_TEMPLATES/Word_Documents</td><td>Staff and tutor handbook</td></tr>
        <tr><td>Monthly_Report_Template.docx</td><td>03_TEMPLATES/Word_Documents</td><td>Client-facing monthly progress report</td></tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Google Sheets / Spreadsheet Templates</h2></div>
    <table>
      <thead><tr><th>Filename</th><th>Folder</th><th>Description</th></tr></thead>
      <tbody>
        <tr><td>KPI_Dashboard.csv</td><td>03_TEMPLATES/Google_Sheets</td><td>Business KPI tracking dashboard</td></tr>
        <tr><td>Revenue_Tracker.csv</td><td>03_TEMPLATES/Google_Sheets</td><td>Monthly revenue and expense tracker</td></tr>
        <tr><td>Student_Analytics.csv</td><td>03_TEMPLATES/Google_Sheets</td><td>Student progress analytics template</td></tr>
        <tr><td>Google_Sheets_Setup_Guide.pdf</td><td>03_TEMPLATES/Google_Sheets</td><td>How to import and use the sheets</td></tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Canva Templates</h2></div>
    <table>
      <thead><tr><th>Template Name</th><th>Format</th><th>Purpose</th></tr></thead>
      <tbody>
        <tr><td>Client Proposal Deck</td><td>16:9 Presentation</td><td>School/parent sales presentations</td></tr>
        <tr><td>Welcome Packet</td><td>A4 Document</td><td>New student/parent onboarding</td></tr>
        <tr><td>Monthly Progress Report</td><td>A4 Document</td><td>Student performance reporting</td></tr>
        <tr><td>Business Presentation</td><td>16:9 Presentation</td><td>Investor/partner pitches</td></tr>
        <tr><td>Case Study</td><td>A4 Document</td><td>Student success stories</td></tr>
        <tr><td>Lead Magnet</td><td>A4 PDF</td><td>Free resource for lead generation</td></tr>
        <tr><td>Instagram Carousel</td><td>1:1 Social</td><td>Educational content for Instagram</td></tr>
        <tr><td>LinkedIn Carousel</td><td>4:5 Social</td><td>Professional content for LinkedIn</td></tr>
        <tr><td>Invoice Template</td><td>A4 Document</td><td>Branded invoice for services</td></tr>
        <tr><td>Certificate of Completion</td><td>Landscape A4</td><td>Student achievement certificates</td></tr>
        <tr><td>Business Report</td><td>A4 Document</td><td>Annual/quarterly business reporting</td></tr>
        <tr><td>Brand Board</td><td>Square</td><td>Platform brand identity reference</td></tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Notion Workspace Modules</h2></div>
    <table>
      <thead><tr><th>Module</th><th>Purpose</th></tr></thead>
      <tbody>
        <tr><td>OQUL Operations Hub</td><td>Master navigation workspace</td></tr>
        <tr><td>Student CRM</td><td>Track enrolled students and progress</td></tr>
        <tr><td>Content Calendar</td><td>Plan and schedule educational content</td></tr>
        <tr><td>SOP Database</td><td>All standard operating procedures</td></tr>
        <tr><td>Team Management</td><td>Staff, tutors, and HR management</td></tr>
        <tr><td>Finance Dashboard</td><td>Revenue, expenses, and projections</td></tr>
        <tr><td>90-Day Growth Tracker</td><td>Launch plan with milestone tracking</td></tr>
      </tbody>
    </table>

    <div class="callout callout-warning">
      <span class="callout-icon">⚠️</span>
      <div class="callout-content">
        <div class="callout-title">Missing a file?</div>
        <p class="callout-body">If any files listed above are missing from your download, re-download the product from your purchase confirmation. If the issue persists, see Support_Guide.pdf for contact options.</p>
      </div>
    </div>
    `,
  }),
};
