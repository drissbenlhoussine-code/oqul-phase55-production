import { brand, pageLayout } from '../brand.mjs';

export const supportGuide = {
  filename: 'Support_Guide.pdf',
  outputDir: '05_SUPPORT',
  html: pageLayout({
    title: 'Support Guide',
    docLabel: 'Support Guide',
    pageNum: '7',
    content: `
    <h1 class="section-title">Support Guide</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:18px;">Everything you need to get help, report issues, and make the most of OQUL EdTech OS.</p>

    <div class="callout callout-success">
      <span class="callout-icon">✅</span>
      <div class="callout-content">
        <div class="callout-title">Start with Self-Service</div>
        <p class="callout-body">Before contacting support, check the FAQ.pdf in this folder. 80% of common questions are answered there. The documentation in 02_DOCUMENTATION also covers most technical topics in depth.</p>
      </div>
    </div>

    <div class="section-break"><h2>Support Tiers</h2></div>

    <div class="card-grid">
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0; color:${brand.accent}">Self-Service (Instant)</div>
        <ul class="feature-list">
          <li>FAQ.pdf — 20 common questions answered</li>
          <li>Installation Guide.pdf — step-by-step setup</li>
          <li>docs/ folder — 50+ technical markdown docs</li>
          <li>Code comments in src/server/ directories</li>
          <li>Architecture Decision Records (docs/adr/)</li>
        </ul>
        <div style="margin-top:10px; font-size:8.5pt; color:${brand.textSecondary}">Response: Immediate</div>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0; color:${brand.primary}">Purchase Support (Included)</div>
        <ul class="feature-list">
          <li>Contact seller via Etsy messaging</li>
          <li>Installation assistance</li>
          <li>Configuration questions</li>
          <li>Bug reports for product defects</li>
          <li>Clarification on documentation</li>
        </ul>
        <div style="margin-top:10px; font-size:8.5pt; color:${brand.textSecondary}">Response: 24–48 hours</div>
      </div>
    </div>

    <div class="section-break"><h2>Before Contacting Support</h2></div>

    <ol class="steps">
      <li>
        <strong>Check the FAQ first</strong>
        Open FAQ.pdf in this folder. Your question is likely answered there.
      </li>
      <li>
        <strong>Review the Installation Guide</strong>
        Most issues relate to environment setup. Re-read the relevant section in Installation_Guide.pdf.
      </li>
      <li>
        <strong>Check the docs/ folder</strong>
        The source code comes with 50+ technical documentation files. For any architecture question, check <code>docs/ARCHITECTURE_RULES.md</code> or the relevant PHASE document.
      </li>
      <li>
        <strong>Collect error information</strong>
        Before reaching out, gather: the exact error message, which step failed, your Node.js version (<code>node -v</code>), and what you've already tried.
      </li>
    </ol>

    <div class="section-break"><h2>Troubleshooting Quick Reference</h2></div>

    <table>
      <thead><tr><th>Problem</th><th>First Check</th><th>Solution</th></tr></thead>
      <tbody>
        <tr>
          <td>App won't start</td>
          <td>Check .env.local exists</td>
          <td>Copy .env.example to .env.local and fill all Required fields</td>
        </tr>
        <tr>
          <td>Database connection error</td>
          <td>Is PostgreSQL running?</td>
          <td>Run <code>docker compose up -d</code> to start services</td>
        </tr>
        <tr>
          <td>Leila AI not responding</td>
          <td>Check GROQ_API_KEY</td>
          <td>Verify key at console.groq.com, check rate limit status</td>
        </tr>
        <tr>
          <td>Migrations fail</td>
          <td>Database credentials correct?</td>
          <td>Check DATABASE_URL format: postgresql://user:pass@host:5432/db</td>
        </tr>
        <tr>
          <td>No curriculum content</td>
          <td>Did you run seed scripts?</td>
          <td>Run <code>node scripts/seed-full-curriculum.mjs</code></td>
        </tr>
        <tr>
          <td>Redis errors in logs</td>
          <td>Is Redis running?</td>
          <td>Check <code>docker compose ps</code> for Redis container status</td>
        </tr>
        <tr>
          <td>Email not sending</td>
          <td>SMTP credentials set?</td>
          <td>Check SMTP_HOST, SMTP_USER, SMTP_PASS in .env.local</td>
        </tr>
        <tr>
          <td>TypeScript errors</td>
          <td>Node modules installed?</td>
          <td>Run <code>npm install</code> then <code>npm run build</code> to check</td>
        </tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Key Technical Resources</h2></div>

    <div class="card-grid">
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Architecture Docs</div>
        <ul class="feature-list">
          <li><code>docs/ARCHITECTURE_RULES.md</code></li>
          <li><code>docs/FINAL_ARCHITECTURE.md</code></li>
          <li><code>docs/adr/</code> — Decision records</li>
          <li><code>FINAL_BUILD_REPORT.md</code></li>
        </ul>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Phase Documentation</div>
        <ul class="feature-list">
          <li><code>docs/PHASE55_*.md</code> — Current version</li>
          <li><code>docs/PHASE54_*.md</code> — Curriculum align</li>
          <li><code>docs/ROADMAP.md</code> — Future plans</li>
          <li><code>docs/LAUNCH_READINESS_*.md</code></li>
        </ul>
      </div>
    </div>

    <div class="section-break"><h2>External Documentation</h2></div>

    <table>
      <thead><tr><th>Resource</th><th>For</th></tr></thead>
      <tbody>
        <tr><td>nextjs.org/docs</td><td>Next.js App Router documentation</td></tr>
        <tr><td>orm.drizzle.team</td><td>Drizzle ORM schema and migration docs</td></tr>
        <tr><td>console.groq.com</td><td>Groq API key management and rate limits</td></tr>
        <tr><td>redis.io/docs</td><td>Redis configuration and commands</td></tr>
        <tr><td>bullmq.io</td><td>BullMQ job queue documentation</td></tr>
        <tr><td>k6.io/docs</td><td>K6 load testing documentation</td></tr>
      </tbody>
    </table>

    <div class="callout callout-tip">
      <span class="callout-icon">💡</span>
      <div class="callout-content">
        <div class="callout-title">Pro Tip: Read the Phase Docs</div>
        <p class="callout-body">The <code>docs/</code> folder contains detailed documentation written during development. Each PHASE document explains WHY decisions were made, not just what was built. This context is invaluable when customizing the platform.</p>
      </div>
    </div>
    `,
  }),
};
