import { brand, pageLayout } from '../brand.mjs';

export const quickStart = {
  filename: '05_Quick_Start_Guide.pdf',
  outputDir: '01_INSTALLATION',
  html: pageLayout({
    title: 'Quick Start Guide',
    docLabel: 'Quick Start Guide',
    pageNum: '5',
    content: `
    <h1 class="section-title">Quick Start Guide</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:16px;">For experienced developers. Get OQUL running in <strong>under 15 minutes</strong>. Assumes Node.js 20+, PostgreSQL, Redis, and a Groq API key are already available.</p>

    <div class="callout callout-warning">
      <span class="callout-icon">⚡</span>
      <div class="callout-content">
        <div class="callout-title">This is the fast-track guide</div>
        <p class="callout-body">If you encounter any issues, switch to the full <strong>Installation_Guide.pdf</strong> which covers every step in detail including troubleshooting.</p>
      </div>
    </div>

    <div class="section-break"><h2>5-Command Setup</h2></div>

    <div class="code-block" style="font-size:9pt">
<span class="comment"># 1. Install dependencies</span><br>
<span class="cmd">npm install</span><br><br>
<span class="comment"># 2. Configure environment (fill in your values)</span><br>
<span class="cmd">cp</span> .env.example .env.local<br><br>
<span class="comment"># 3. Start services + run migrations</span><br>
<span class="cmd">docker compose</span> -f docker-compose.runtime.yml up -d<br>
<span class="cmd">npx drizzle-kit</span> migrate<br><br>
<span class="comment"># 4. Seed curriculum data</span><br>
<span class="cmd">node</span> scripts/seed-full-curriculum.mjs<br><br>
<span class="comment"># 5. Launch</span><br>
<span class="cmd">npm run dev</span>
    </div>

    <div class="section-break"><h2>Minimum .env.local</h2></div>

    <div class="code-block" style="font-size:8.5pt">
<span class="comment"># Database</span><br>
<span class="str">DATABASE_URL</span>=postgresql://postgres:password@localhost:5432/oqul<br><br>
<span class="comment"># Cache</span><br>
<span class="str">REDIS_URL</span>=redis://localhost:6379<br><br>
<span class="comment"># AI Tutor (get key at console.groq.com)</span><br>
<span class="str">GROQ_API_KEY</span>=gsk_your_groq_api_key_here<br><br>
<span class="comment"># Auth (generate with: openssl rand -hex 32)</span><br>
<span class="str">JWT_SECRET</span>=your_64_char_random_secret_here<br><br>
<span class="comment"># App URL</span><br>
<span class="str">NEXTAUTH_URL</span>=http://localhost:3000
    </div>

    <div class="section-break"><h2>Verification Checklist</h2></div>

    <ul class="checklist">
      <li class="done">App loads at http://localhost:3000</li>
      <li class="done">Landing page renders correctly</li>
      <li class="done">Can register a new user account</li>
      <li class="done">Email verification sent (if SMTP configured)</li>
      <li class="done">Dashboard loads after login</li>
      <li class="done">Leila AI responds in chat</li>
      <li class="done">Curriculum content shows for Grade 1</li>
      <li class="done">Gamification XP points update on lesson completion</li>
      <li class="done">Parent portal accessible</li>
      <li class="done">Grafana dashboard shows metrics at http://localhost:3001</li>
    </ul>

    <div class="section-break"><h2>Useful Scripts</h2></div>

    <table>
      <thead><tr><th>Command</th><th>Purpose</th></tr></thead>
      <tbody>
        <tr><td><code>npm run dev</code></td><td>Start development server (hot reload)</td></tr>
        <tr><td><code>npm run build</code></td><td>Production build</td></tr>
        <tr><td><code>npm run start</code></td><td>Start production server</td></tr>
        <tr><td><code>npm run test</code></td><td>Run test suite</td></tr>
        <tr><td><code>npx drizzle-kit studio</code></td><td>Open database GUI</td></tr>
        <tr><td><code>node scripts/audit-curriculum-coverage.mjs</code></td><td>Audit curriculum completeness</td></tr>
        <tr><td><code>node scripts/check-user-email-exists.mjs</code></td><td>Check if user exists</td></tr>
      </tbody>
    </table>

    <div class="callout callout-success">
      <span class="callout-icon">🎉</span>
      <div class="callout-content">
        <div class="callout-title">You're live!</div>
        <p class="callout-body">Once the checklist above is green, you have a fully operational AI educational platform. Explore <strong>02_DOCUMENTATION/Business_Overview.pdf</strong> to understand the business model and how to monetize your deployment.</p>
      </div>
    </div>
    `,
  }),
};
