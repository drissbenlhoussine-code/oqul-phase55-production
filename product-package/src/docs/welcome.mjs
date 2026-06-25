import { brand, productMeta, pageLayout } from '../brand.mjs';

export const welcome = {
  filename: '01_Welcome.pdf',
  outputDir: '00_START_HERE',
  html: pageLayout({
    title: 'Welcome',
    docLabel: 'Welcome Guide',
    pageNum: '1',
    content: `
    <h1 class="section-title">Welcome to OQUL EdTech OS 👋</h1>
    <p style="font-size:11pt; color:${brand.textSecondary}; margin-bottom:20px;">Thank you for investing in <strong>OQUL — the Complete AI Educational Business System</strong>. This is not just documentation — it is a full operating system for running a modern, AI-powered educational business.</p>

    <div class="highlight-block">
      <h3>What You Just Purchased</h3>
      <p>A production-ready, enterprise-grade educational platform with AI tutoring, adaptive learning, full K–12 curriculum, and complete business operations infrastructure — packaged for immediate deployment.</p>
    </div>

    <div class="section-break"><h2>What's Included</h2></div>

    <div class="card-grid">
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Platform Source Code</div>
        <ul class="feature-list">
          <li>Next.js 15 + React 19 frontend</li>
          <li>Node.js 20+ backend with Drizzle ORM</li>
          <li>461 TypeScript/TSX production files</li>
          <li>PostgreSQL + Redis infrastructure</li>
          <li>Prometheus + Grafana monitoring</li>
        </ul>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">AI Tutor System</div>
        <ul class="feature-list">
          <li>Leila AI tutor (Arabic + Darija)</li>
          <li>Groq API streaming integration</li>
          <li>Adaptive learning algorithms</li>
          <li>Knowledge tracing engine</li>
          <li>Confidence scoring system</li>
        </ul>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Curriculum Registry</div>
        <ul class="feature-list">
          <li>Complete K–12 curriculum (Grades 1–12)</li>
          <li>Primary school (6 levels)</li>
          <li>Middle school (3 levels)</li>
          <li>Secondary school (TC, 1BAC, 2BAC)</li>
          <li>Official exam alignment data</li>
        </ul>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Business Operations</div>
        <ul class="feature-list">
          <li>SOP Library (40+ procedures)</li>
          <li>Subscription strategy playbook</li>
          <li>Client portal templates</li>
          <li>Onboarding checklists</li>
          <li>90-Day growth plan</li>
        </ul>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Templates & Tools</div>
        <ul class="feature-list">
          <li>Notion workspace templates</li>
          <li>Google Sheets KPI dashboards</li>
          <li>Canva design templates (12 types)</li>
          <li>Word document templates</li>
          <li>Email & proposal templates</li>
        </ul>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Infrastructure & DevOps</div>
        <ul class="feature-list">
          <li>Docker Compose configurations</li>
          <li>Redis Sentinel (high availability)</li>
          <li>CI/CD GitHub Actions pipeline</li>
          <li>K6 load testing suites</li>
          <li>50+ deployment scripts</li>
        </ul>
      </div>
    </div>

    <div class="section-break"><h2>Package Statistics</h2></div>

    <div class="icon-stat-row">
      <div class="icon-stat">
        <span class="stat-icon">📁</span>
        <div class="stat-val">200+</div>
        <div class="stat-label">Total Files</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">🧩</span>
        <div class="stat-val">55</div>
        <div class="stat-label">Build Phases</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">🎓</span>
        <div class="stat-val">12</div>
        <div class="stat-label">Grade Levels</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">🤖</span>
        <div class="stat-val">1</div>
        <div class="stat-label">AI Tutor</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">⚡</span>
        <div class="stat-val">50+</div>
        <div class="stat-label">API Endpoints</div>
      </div>
    </div>

    <div class="section-break"><h2>Your First 3 Steps</h2></div>

    <ol class="steps">
      <li>
        <strong>Read "Read Me First" (00_START_HERE folder)</strong>
        Understand the product structure, what tools you need, and how everything connects before touching any files.
      </li>
      <li>
        <strong>Follow the Installation Guide (01_INSTALLATION folder)</strong>
        Set up your environment: Node.js 20+, PostgreSQL, Redis, and your Groq API key. The guide walks you through each step.
      </li>
      <li>
        <strong>Explore the Business Documentation (02_DOCUMENTATION folder)</strong>
        Review the Business Overview and SOP Library to understand how to position and operate this platform commercially.
      </li>
    </ol>

    <div class="callout callout-success">
      <span class="callout-icon">✅</span>
      <div class="callout-content">
        <div class="callout-title">You're fully supported</div>
        <p class="callout-body">Every component of this system has been professionally documented, tested under load, and is ready for production deployment. You are not starting from scratch — you are starting from finished.</p>
      </div>
    </div>

    <div class="callout callout-tip">
      <span class="callout-icon">💡</span>
      <div class="callout-content">
        <div class="callout-title">Pro Tip: Duplicate, Don't Delete</div>
        <p class="callout-body">When customizing Notion templates or Google Sheets dashboards, always duplicate the original first. Keep the originals as reference templates for future use.</p>
      </div>
    </div>

    <div class="section-break"><h2>License Summary</h2></div>
    <div class="card">
      <div class="tag-row">
        <span class="badge badge-green">✓ Commercial Use</span>
        <span class="badge badge-green">✓ One Business</span>
        <span class="badge badge-green">✓ Unlimited Students</span>
        <span class="badge badge-red">✗ Resale Prohibited</span>
        <span class="badge badge-red">✗ Redistribution Prohibited</span>
      </div>
      <p style="margin-top:10px; font-size:9pt; color:${brand.textSecondary}">Full license terms available in <strong>04_LEGAL/License.pdf</strong></p>
    </div>
    `,
  }),
};
