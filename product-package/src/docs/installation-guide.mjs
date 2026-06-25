import { brand, pageLayout } from '../brand.mjs';

export const installationGuide = {
  filename: '03_Installation_Guide.pdf',
  outputDir: '01_INSTALLATION',
  html: pageLayout({
    title: 'Installation Guide',
    docLabel: 'Installation Guide',
    pageNum: '3',
    content: `
    <h1 class="section-title">Installation Guide</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:18px;">Complete step-by-step guide to deploying OQUL EdTech OS from source to production. Estimated time: <strong>30–60 minutes</strong>.</p>

    <div class="callout callout-info">
      <span class="callout-icon">ℹ️</span>
      <div class="callout-content">
        <div class="callout-title">Prerequisites Checklist</div>
        <p class="callout-body">Before starting, ensure you have: Node.js 20+, Git, Docker Desktop, a Groq API key (free at console.groq.com), and PostgreSQL credentials.</p>
      </div>
    </div>

    <div class="section-break"><h2>Phase 1 — Environment Setup</h2></div>

    <ol class="steps">
      <li>
        <strong>Clone the Repository</strong>
        <div class="code-block">
          <span class="comment"># Clone OQUL to your local machine</span><br>
          <span class="cmd">git clone</span> <span class="str">https://github.com/your-org/oqul-platform.git</span><br>
          <span class="cmd">cd</span> oqul-platform
        </div>
      </li>
      <li>
        <strong>Install Dependencies</strong>
        <div class="code-block">
          <span class="comment"># Install all Node.js packages</span><br>
          <span class="cmd">npm install</span>
        </div>
      </li>
      <li>
        <strong>Configure Environment Variables</strong>
        <div class="code-block">
          <span class="comment"># Copy the example environment file</span><br>
          <span class="cmd">cp</span> .env.example .env.local<br><br>
          <span class="comment"># Edit with your values</span><br>
          <span class="cmd">nano</span> .env.local
        </div>
      </li>
    </ol>

    <div class="section-break"><h2>Environment Variables Reference</h2></div>

    <table>
      <thead><tr><th>Variable</th><th>Description</th><th>Required</th></tr></thead>
      <tbody>
        <tr><td><code>DATABASE_URL</code></td><td>PostgreSQL connection string</td><td><span class="badge badge-red">Required</span></td></tr>
        <tr><td><code>REDIS_URL</code></td><td>Redis connection string</td><td><span class="badge badge-red">Required</span></td></tr>
        <tr><td><code>GROQ_API_KEY</code></td><td>Groq AI API key for Leila tutor</td><td><span class="badge badge-red">Required</span></td></tr>
        <tr><td><code>JWT_SECRET</code></td><td>Secret for JWT token signing (32+ chars)</td><td><span class="badge badge-red">Required</span></td></tr>
        <tr><td><code>NEXTAUTH_URL</code></td><td>Your application URL</td><td><span class="badge badge-red">Required</span></td></tr>
        <tr><td><code>SMTP_HOST</code></td><td>Email server hostname</td><td><span class="badge badge-yellow">Optional</span></td></tr>
        <tr><td><code>SMTP_USER</code></td><td>Email server username</td><td><span class="badge badge-yellow">Optional</span></td></tr>
        <tr><td><code>SMTP_PASS</code></td><td>Email server password</td><td><span class="badge badge-yellow">Optional</span></td></tr>
        <tr><td><code>SENTRY_DSN</code></td><td>Sentry error tracking DSN</td><td><span class="badge badge-gray">Optional</span></td></tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Phase 2 — Database Setup</h2></div>

    <ol class="steps">
      <li>
        <strong>Start PostgreSQL and Redis via Docker</strong>
        <div class="code-block">
          <span class="comment"># Launch all required services</span><br>
          <span class="cmd">docker compose</span> -f docker-compose.runtime.yml up -d<br><br>
          <span class="comment"># Verify services are running</span><br>
          <span class="cmd">docker compose</span> ps
        </div>
      </li>
      <li>
        <strong>Run Database Migrations</strong>
        <div class="code-block">
          <span class="comment"># Apply all schema migrations</span><br>
          <span class="cmd">npx drizzle-kit</span> migrate<br><br>
          <span class="comment"># Expected: 17 migrations applied</span>
        </div>
      </li>
      <li>
        <strong>Seed the Curriculum Data</strong>
        <div class="code-block">
          <span class="comment"># Seed full K-12 curriculum (takes ~5 minutes)</span><br>
          <span class="cmd">node</span> scripts/seed-full-curriculum.mjs<br><br>
          <span class="comment"># Seed primary school specifically</span><br>
          <span class="cmd">node</span> scripts/seed-phase52-primary.mjs<br><br>
          <span class="comment"># Seed secondary school (2BAC/1BAC/TC)</span><br>
          <span class="cmd">node</span> scripts/seed-phase53-full-secondary-school.mjs
        </div>
      </li>
    </ol>

    <div class="section-break"><h2>Phase 3 — Launch Application</h2></div>

    <ol class="steps">
      <li>
        <strong>Start Development Server</strong>
        <div class="code-block">
          <span class="cmd">npm run dev</span><br><br>
          <span class="comment"># App available at http://localhost:3000</span>
        </div>
      </li>
      <li>
        <strong>Verify Installation</strong>
        <p style="font-size:9pt; margin-top:6px; margin-bottom:8px">Open your browser and navigate to <code>http://localhost:3000</code>. You should see the OQUL landing page. Register a student account and verify the AI tutor Leila responds.</p>
      </li>
      <li>
        <strong>Run Test Suite</strong>
        <div class="code-block">
          <span class="comment"># Run all unit and integration tests</span><br>
          <span class="cmd">npm run test</span><br><br>
          <span class="comment"># Expected: All tests pass</span>
        </div>
      </li>
    </ol>

    <div class="section-break"><h2>Production Deployment Checklist</h2></div>

    <ul class="checklist">
      <li>All environment variables set in production .env</li>
      <li>DATABASE_URL points to production PostgreSQL instance</li>
      <li>REDIS_URL points to production Redis (with Sentinel for HA)</li>
      <li>GROQ_API_KEY validated and rate limits understood</li>
      <li>JWT_SECRET is cryptographically random (32+ characters)</li>
      <li>NEXTAUTH_URL set to your production domain (https://)</li>
      <li>All database migrations applied: <code>npx drizzle-kit migrate</code></li>
      <li>Full curriculum seeded via seed scripts</li>
      <li>Prometheus + Grafana monitoring configured</li>
      <li>Sentry DSN configured for error tracking</li>
      <li>Email SMTP service configured for user verification</li>
      <li>SSL/TLS certificate configured (via nginx or Caddy)</li>
      <li>Load tests run: <code>k6 run load-tests/ai-runtime-k6.js</code></li>
      <li>GitHub Actions CI pipeline green</li>
    </ul>

    <div class="callout callout-success">
      <span class="callout-icon">✅</span>
      <div class="callout-content">
        <div class="callout-title">Need help? Check FAQ.pdf first</div>
        <p class="callout-body">The most common installation issues are covered in <strong>05_SUPPORT/FAQ.pdf</strong>. If your issue is not covered there, consult <strong>05_SUPPORT/Support_Guide.pdf</strong> for how to get assistance.</p>
      </div>
    </div>

    <div class="section-break"><h2>Architecture Quick Reference</h2></div>

    <div class="card-grid">
      <div class="card">
        <div class="section-subtitle" style="margin-top:0">Port Reference</div>
        <table style="margin:0">
          <tr><td><strong>3000</strong></td><td>Next.js Application</td></tr>
          <tr><td><strong>5432</strong></td><td>PostgreSQL</td></tr>
          <tr><td><strong>6379</strong></td><td>Redis</td></tr>
          <tr><td><strong>9090</strong></td><td>Prometheus</td></tr>
          <tr><td><strong>3001</strong></td><td>Grafana</td></tr>
        </table>
      </div>
      <div class="card">
        <div class="section-subtitle" style="margin-top:0">Key Directories</div>
        <table style="margin:0">
          <tr><td><code>src/app/</code></td><td>Next.js pages & routes</td></tr>
          <tr><td><code>src/server/</code></td><td>Business logic</td></tr>
          <tr><td><code>src/features/</code></td><td>Feature modules</td></tr>
          <tr><td><code>curriculum-registry/</code></td><td>Curriculum JSON</td></tr>
          <tr><td><code>scripts/</code></td><td>Seed & setup tools</td></tr>
        </table>
      </div>
    </div>
    `,
  }),
};
