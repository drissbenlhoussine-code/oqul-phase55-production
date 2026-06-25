import { brand, pageLayout } from '../brand.mjs';

export const readMeFirst = {
  filename: '02_Read_Me_First.pdf',
  outputDir: '00_START_HERE',
  html: pageLayout({
    title: 'Read Me First',
    docLabel: 'Read Me First',
    pageNum: '2',
    content: `
    <h1 class="section-title">Read Me First</h1>
    <p style="color:${brand.textSecondary}; font-size:10.5pt; margin-bottom:18px;">Before opening any other file, read this document completely. It will save you hours of confusion and ensure you get maximum value from your purchase immediately.</p>

    <div class="callout callout-warning">
      <span class="callout-icon">⚠️</span>
      <div class="callout-content">
        <div class="callout-title">Important: Read This Before Installation</div>
        <p class="callout-body">OQUL EdTech OS is a full-stack production application, not a simple template. It requires a proper development environment. Please complete this document before attempting installation.</p>
      </div>
    </div>

    <div class="section-break"><h2>What Is OQUL?</h2></div>

    <p>OQUL (عقل — Arabic for <em>mind/intellect</em>) is a complete AI-powered educational platform originally built for Moroccan K–12 students. It features an intelligent AI tutor named <strong>Leila</strong>, adaptive learning paths, a full curriculum registry aligned to official educational standards, and a parent monitoring portal.</p>

    <p>As a commercial product, OQUL gives you a <strong>fully-built, production-tested SaaS foundation</strong> that you can deploy, customize, and operate as your own educational business.</p>

    <div class="section-break"><h2>System Requirements</h2></div>

    <table>
      <thead><tr><th>Requirement</th><th>Minimum</th><th>Recommended</th></tr></thead>
      <tbody>
        <tr><td><strong>Node.js</strong></td><td>v20.0+</td><td>v20 LTS</td></tr>
        <tr><td><strong>PostgreSQL</strong></td><td>v14+</td><td>v16</td></tr>
        <tr><td><strong>Redis</strong></td><td>v7+</td><td>v7.2</td></tr>
        <tr><td><strong>RAM</strong></td><td>4 GB</td><td>8 GB+</td></tr>
        <tr><td><strong>Storage</strong></td><td>10 GB</td><td>50 GB+</td></tr>
        <tr><td><strong>OS</strong></td><td>Ubuntu 22.04+</td><td>Ubuntu 22.04 LTS</td></tr>
        <tr><td><strong>Docker</strong></td><td>v24+</td><td>Docker Desktop latest</td></tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Required API Keys</h2></div>

    <div class="card-grid">
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Groq API <span class="badge badge-blue">Required</span></div>
        <p style="font-size:9pt">Powers the Leila AI tutor with ultra-fast LLM inference. Free tier available at console.groq.com</p>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">SMTP Service <span class="badge badge-yellow">Optional</span></div>
        <p style="font-size:9pt">For email verification and password resets. Works with Resend, SendGrid, or any SMTP provider.</p>
      </div>
    </div>

    <div class="section-break"><h2>Folder Structure Overview</h2></div>

    <table>
      <thead><tr><th>Folder</th><th>Contents</th></tr></thead>
      <tbody>
        <tr><td><strong>00_START_HERE</strong></td><td>Cover, Welcome, this document, and Folder Guide</td></tr>
        <tr><td><strong>01_INSTALLATION</strong></td><td>Step-by-step setup guide and Quick Start</td></tr>
        <tr><td><strong>02_DOCUMENTATION</strong></td><td>Business Overview, Architecture, SOP Library</td></tr>
        <tr><td><strong>03_TEMPLATES</strong></td><td>Notion, Google Sheets, Canva, Word templates</td></tr>
        <tr><td><strong>04_LEGAL</strong></td><td>License and Terms of Use</td></tr>
        <tr><td><strong>05_SUPPORT</strong></td><td>FAQ and Support Guide</td></tr>
        <tr><td><strong>06_META</strong></td><td>Version History, Changelog, Asset Manifest, Roadmap</td></tr>
        <tr><td><strong>source/</strong></td><td>Complete application source code</td></tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Technology Stack at a Glance</h2></div>

    <div class="three-col">
      <div class="card no-break" style="padding:12px 14px">
        <div style="font-weight:700; font-size:9pt; color:${brand.primary}; margin-bottom:6px">Frontend</div>
        <ul class="feature-list">
          <li>Next.js 15.5</li>
          <li>React 19</li>
          <li>TypeScript</li>
          <li>Tailwind CSS</li>
          <li>Radix UI</li>
        </ul>
      </div>
      <div class="card no-break" style="padding:12px 14px">
        <div style="font-weight:700; font-size:9pt; color:${brand.primary}; margin-bottom:6px">Backend</div>
        <ul class="feature-list">
          <li>Node.js 20+</li>
          <li>PostgreSQL</li>
          <li>Redis + BullMQ</li>
          <li>Drizzle ORM</li>
          <li>Groq AI API</li>
        </ul>
      </div>
      <div class="card no-break" style="padding:12px 14px">
        <div style="font-weight:700; font-size:9pt; color:${brand.primary}; margin-bottom:6px">DevOps</div>
        <ul class="feature-list">
          <li>Docker Compose</li>
          <li>GitHub Actions</li>
          <li>Prometheus</li>
          <li>Grafana</li>
          <li>K6 Load Tests</li>
        </ul>
      </div>
    </div>

    <div class="section-break"><h2>Key Concepts to Understand</h2></div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Leila — The AI Tutor</div>
      <p style="font-size:9pt">Leila is the core AI personality of the platform. She communicates in Arabic, French, and Moroccan Darija dialect. She adapts her teaching style based on the student's confidence level, pace, and learning history. Leila's persona is defined in <code>src/server/ai/personas/</code>.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Adaptive Learning Engine</div>
      <p style="font-size:9pt">The platform continuously adjusts difficulty, pacing, and content based on student performance. This is powered by a knowledge tracing algorithm in <code>src/server/adaptive/</code> and a confidence engine in <code>src/server/confidence-engine/</code>.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Curriculum Registry</div>
      <p style="font-size:9pt">All curriculum data lives in <code>curriculum-registry/</code> as structured JSON files. These map to official Moroccan educational standards and are seeded into the database on first run via scripts in <code>scripts/</code>.</p>
    </div>

    <div class="callout callout-success">
      <span class="callout-icon">🚀</span>
      <div class="callout-content">
        <div class="callout-title">Ready to Install?</div>
        <p class="callout-body">Once you have Node.js 20+, PostgreSQL, Redis, and your Groq API key ready, open <strong>01_INSTALLATION/Installation_Guide.pdf</strong> for the complete step-by-step walkthrough.</p>
      </div>
    </div>
    `,
  }),
};
