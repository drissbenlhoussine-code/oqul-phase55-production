import { brand, pageLayout } from '../brand.mjs';

export const changelog = {
  filename: 'Changelog.pdf',
  outputDir: '06_META',
  html: pageLayout({
    title: 'Changelog',
    docLabel: 'Changelog',
    pageNum: '11',
    content: `
    <h1 class="section-title">Changelog</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:16px;">Detailed log of all significant changes, additions, and fixes across all phases of OQUL EdTech OS development.</p>

    <div class="section-break"><h2>v1.0.0 — Initial Commercial Release</h2></div>
    <div class="card">
      <div style="display:flex; align-items:center; gap:8px; margin-bottom:10px">
        <span class="badge badge-green">Latest</span>
        <span style="font-size:8.5pt; color:${brand.textSecondary}">January 2026</span>
      </div>

      <div class="section-subtitle" style="margin-top:0">New Features</div>
      <ul class="feature-list">
        <li>Phase 55 Adaptive AI Learning Platform module shipped</li>
        <li>Complete K–12 curriculum registry (Grades 1–12)</li>
        <li>Official alignment to Moroccan Ministry of Education standards</li>
        <li>Competency matrix for all assessed subjects</li>
        <li>Parent portal with real-time progress monitoring</li>
        <li>Email verification flow with SMTP integration</li>
        <li>Full observability stack (Prometheus + Grafana + Sentry)</li>
        <li>Redis Sentinel high-availability configuration</li>
        <li>K6 load testing suites for all core paths</li>
        <li>Product package with premium documentation</li>
      </ul>

      <div class="section-subtitle">Improvements</div>
      <ul class="feature-list">
        <li>Leila AI persona enhanced with Darija dialect support</li>
        <li>Adaptive learning paths refined with Bayesian knowledge tracing</li>
        <li>Gamification system: XP, streaks, badges, and adventure map</li>
        <li>Deep content enhancer for weak curriculum lessons</li>
        <li>Cognitive pacing algorithm improved for primary school students</li>
        <li>Daily challenge system with difficulty calibration</li>
        <li>BullMQ job queue optimized for AI request handling</li>
      </ul>

      <div class="section-subtitle">Bug Fixes</div>
      <ul class="feature-list">
        <li>Password reset email flow stabilized (FIXES.md references)</li>
        <li>Auth cookie handling on mobile browsers resolved</li>
        <li>Streaming response interruption on network loss handled</li>
        <li>Race condition in adaptive learning state updates resolved</li>
        <li>Redis connection pool leak under sustained load fixed</li>
      </ul>
    </div>

    <div class="section-break"><h2>Development Phase Highlights</h2></div>

    <table>
      <thead><tr><th>Phase</th><th>Key Change</th><th>Type</th></tr></thead>
      <tbody>
        <tr><td>Phase 55</td><td>Adaptive AI platform — full production release</td><td><span class="badge badge-green">Feature</span></td></tr>
        <tr><td>Phase 54</td><td>Official curriculum alignment + competency matrix</td><td><span class="badge badge-blue">Data</span></td></tr>
        <tr><td>Phase 53</td><td>Full secondary school curriculum (TC/1BAC/2BAC)</td><td><span class="badge badge-blue">Data</span></td></tr>
        <tr><td>Phase 52</td><td>Full primary school curriculum (Grades 1–6)</td><td><span class="badge badge-blue">Data</span></td></tr>
        <tr><td>Phase 51</td><td>Full middle school curriculum (Grades 7–9)</td><td><span class="badge badge-blue">Data</span></td></tr>
        <tr><td>Phase 50</td><td>Deep content enhancement system + curriculum mapping</td><td><span class="badge badge-green">Feature</span></td></tr>
        <tr><td>Phase 42</td><td>Middle school intelligence engine</td><td><span class="badge badge-green">Feature</span></td></tr>
        <tr><td>Phase 40</td><td>Gamification + adventure map + daily challenges</td><td><span class="badge badge-green">Feature</span></td></tr>
        <tr><td>Phase 38</td><td>Security hardening + child safety compliance</td><td><span class="badge badge-yellow">Security</span></td></tr>
        <tr><td>Phase 29</td><td>Knowledge tracing + Bayesian learning algorithms</td><td><span class="badge badge-green">Feature</span></td></tr>
        <tr><td>Phase 28</td><td>Emotional memory + human learning experience</td><td><span class="badge badge-green">Feature</span></td></tr>
        <tr><td>Phase 27</td><td>Living learner intelligence + confidence scoring</td><td><span class="badge badge-green">Feature</span></td></tr>
        <tr><td>Phase 14</td><td>Living learning system — first adaptive migration</td><td><span class="badge badge-green">Feature</span></td></tr>
        <tr><td>Phase 8</td><td>Real-time AI streaming production hardening</td><td><span class="badge badge-yellow">Perf</span></td></tr>
        <tr><td>Phase 5</td><td>Product API contracts defined (ADR-005)</td><td><span class="badge badge-gray">Arch</span></td></tr>
        <tr><td>Phase 2</td><td>JWT authentication + session management</td><td><span class="badge badge-yellow">Security</span></td></tr>
        <tr><td>Phase 1</td><td>PostgreSQL database architecture + Drizzle ORM</td><td><span class="badge badge-gray">Arch</span></td></tr>
        <tr><td>Phase 0</td><td>Foundation: environment, architecture decisions</td><td><span class="badge badge-gray">Arch</span></td></tr>
      </tbody>
    </table>

    <div class="callout callout-tip">
      <span class="callout-icon">📌</span>
      <div class="callout-content">
        <div class="callout-title">Staying Up to Date</div>
        <p class="callout-body">Future updates to this product will be delivered as new downloads. Check your purchase receipt for update notification instructions. Major new phases (56+) will be announced separately.</p>
      </div>
    </div>
    `,
  }),
};
