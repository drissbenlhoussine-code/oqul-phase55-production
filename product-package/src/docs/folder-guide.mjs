import { brand, pageLayout } from '../brand.mjs';

export const folderGuide = {
  filename: '04_Folder_Guide.pdf',
  outputDir: '00_START_HERE',
  html: pageLayout({
    title: 'Folder Guide',
    docLabel: 'Folder Guide',
    pageNum: '4',
    content: `
    <h1 class="section-title">Folder Guide</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:18px;">This guide maps every folder and file in the OQUL EdTech OS package. Use it as your navigation reference whenever you need to find something.</p>

    <div class="section-break"><h2>Top-Level Package Structure</h2></div>

    <div class="code-block" style="font-size:8pt; line-height:1.8">
<span style="color:#93C5FD">OQUL-EdTech-OS-v1.0/</span><br>
├── <span style="color:${brand.accent}">00_START_HERE/</span>          <span style="color:#64748B">← Begin here</span><br>
├── <span style="color:${brand.accent}">01_INSTALLATION/</span>        <span style="color:#64748B">← Setup guides</span><br>
├── <span style="color:${brand.accent}">02_DOCUMENTATION/</span>       <span style="color:#64748B">← Business docs</span><br>
├── <span style="color:${brand.accent}">03_TEMPLATES/</span>           <span style="color:#64748B">← All templates</span><br>
├── <span style="color:${brand.accent}">04_LEGAL/</span>               <span style="color:#64748B">← License & terms</span><br>
├── <span style="color:${brand.accent}">05_SUPPORT/</span>             <span style="color:#64748B">← FAQ & help</span><br>
├── <span style="color:${brand.accent}">06_META/</span>                <span style="color:#64748B">← Versions & roadmap</span><br>
└── <span style="color:#93C5FD">source/</span>                  <span style="color:#64748B">← Full source code</span>
    </div>

    <div class="section-break"><h2>00_START_HERE</h2></div>
    <div class="card">
      <p style="font-size:9pt; color:${brand.textSecondary}; margin-bottom:10px">The most important folder. Read all files in this folder before anything else.</p>
      <table style="margin:0">
        <tr><th>File</th><th>Purpose</th></tr>
        <tr><td>00_Cover.pdf</td><td>Product overview and visual identity</td></tr>
        <tr><td>01_Welcome.pdf</td><td>What's included and first steps</td></tr>
        <tr><td>02_Read_Me_First.pdf</td><td>Essential context before installation</td></tr>
        <tr><td>04_Folder_Guide.pdf</td><td>This document — package navigation</td></tr>
      </table>
    </div>

    <div class="section-break"><h2>01_INSTALLATION</h2></div>
    <div class="card">
      <p style="font-size:9pt; color:${brand.textSecondary}; margin-bottom:10px">Step-by-step setup and launch guides.</p>
      <table style="margin:0">
        <tr><th>File</th><th>Purpose</th></tr>
        <tr><td>03_Installation_Guide.pdf</td><td>Full environment setup (30–60 min)</td></tr>
        <tr><td>05_Quick_Start_Guide.pdf</td><td>Fast-track for experienced developers</td></tr>
      </table>
    </div>

    <div class="section-break"><h2>02_DOCUMENTATION</h2></div>
    <div class="card">
      <p style="font-size:9pt; color:${brand.textSecondary}; margin-bottom:10px">Business and technical documentation for operating the platform.</p>
      <table style="margin:0">
        <tr><th>File</th><th>Purpose</th></tr>
        <tr><td>Business_Overview.pdf</td><td>Platform capabilities and business model</td></tr>
        <tr><td>Architecture_Guide.pdf</td><td>Technical architecture deep-dive</td></tr>
        <tr><td>SOP_Library.pdf</td><td>40+ standard operating procedures</td></tr>
        <tr><td>Curriculum_Guide.pdf</td><td>K–12 curriculum structure and management</td></tr>
        <tr><td>AI_Tutor_Guide.pdf</td><td>Leila system documentation</td></tr>
        <tr><td>Subscription_Strategy.pdf</td><td>Monetization and pricing strategy</td></tr>
        <tr><td>90_Day_Growth_Plan.pdf</td><td>Launch to first 100 users plan</td></tr>
      </table>
    </div>

    <div class="section-break"><h2>03_TEMPLATES</h2></div>
    <div class="card">
      <table style="margin:0">
        <tr><th>Sub-Folder</th><th>Contents</th></tr>
        <tr><td>Notion/</td><td>Notion workspace export + setup guide</td></tr>
        <tr><td>Google_Sheets/</td><td>KPI dashboard, revenue tracker, analytics</td></tr>
        <tr><td>Canva/</td><td>12 design template links + instructions</td></tr>
        <tr><td>Word_Documents/</td><td>Proposal, contract, onboarding DOCX files</td></tr>
      </table>
    </div>

    <div class="section-break"><h2>Source Code Structure</h2></div>

    <div class="code-block" style="font-size:7.5pt; line-height:1.9">
<span style="color:#93C5FD">source/</span><br>
├── <span style="color:${brand.accent}">src/</span><br>
│   ├── <span style="color:#FCD34D">app/</span>            <span style="color:#64748B">← Next.js pages (auth, dashboard, API routes)</span><br>
│   ├── <span style="color:#FCD34D">components/</span>    <span style="color:#64748B">← Reusable React components</span><br>
│   ├── <span style="color:#FCD34D">features/</span>      <span style="color:#64748B">← Feature modules (ai-tutor, gamification, etc.)</span><br>
│   ├── <span style="color:#FCD34D">server/</span>        <span style="color:#64748B">← Backend business logic (47 subdirectories)</span><br>
│   ├── <span style="color:#FCD34D">db/</span>            <span style="color:#64748B">← Drizzle ORM schema</span><br>
│   ├── <span style="color:#FCD34D">lib/</span>           <span style="color:#64748B">← Shared utilities, state, validators</span><br>
│   └── <span style="color:#FCD34D">types/</span>         <span style="color:#64748B">← TypeScript type definitions</span><br>
├── <span style="color:${brand.accent}">curriculum-registry/</span>   <span style="color:#64748B">← JSON curriculum data (K–12)</span><br>
├── <span style="color:${brand.accent}">db/</span><br>
│   └── <span style="color:#FCD34D">migrations/</span>    <span style="color:#64748B">← 17 SQL migration files</span><br>
├── <span style="color:${brand.accent}">scripts/</span>               <span style="color:#64748B">← 50+ seeding and utility scripts</span><br>
├── <span style="color:${brand.accent}">infra/</span>                 <span style="color:#64748B">← Docker + Prometheus + Grafana configs</span><br>
├── <span style="color:${brand.accent}">load-tests/</span>            <span style="color:#64748B">← K6 performance test suites</span><br>
├── <span style="color:${brand.accent}">docs/</span>                  <span style="color:#64748B">← 50+ architecture markdown docs</span><br>
└── <span style="color:#FCD34D">.github/workflows/</span>    <span style="color:#64748B">← CI/CD pipeline configuration</span>
    </div>

    <div class="callout callout-tip">
      <span class="callout-icon">💡</span>
      <div class="callout-content">
        <div class="callout-title">Naming Conventions</div>
        <p class="callout-body">All PDF files are numbered with a 2-digit prefix (e.g., <code>03_</code>) indicating reading order. Numbered files should be read in sequence when setting up for the first time.</p>
      </div>
    </div>
    `,
  }),
};
