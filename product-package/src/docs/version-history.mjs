import { brand, pageLayout } from '../brand.mjs';

export const versionHistory = {
  filename: 'Version_History.pdf',
  outputDir: '06_META',
  html: pageLayout({
    title: 'Version History',
    docLabel: 'Version History',
    pageNum: '10',
    content: `
    <h1 class="section-title">Version History</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:18px;">Complete development history of OQUL EdTech OS from foundation through Phase 55 production release.</p>

    <div class="icon-stat-row">
      <div class="icon-stat">
        <span class="stat-icon">🏗️</span>
        <div class="stat-val">55</div>
        <div class="stat-label">Build Phases</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">📅</span>
        <div class="stat-val">2024–26</div>
        <div class="stat-label">Development Period</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">🔄</span>
        <div class="stat-val">17</div>
        <div class="stat-label">DB Migrations</div>
      </div>
      <div class="icon-stat">
        <span class="stat-icon">📦</span>
        <div class="stat-val">v1.0</div>
        <div class="stat-label">Current Release</div>
      </div>
    </div>

    <div class="section-break"><h2>Release Timeline</h2></div>

    <div class="timeline">
      <div class="timeline-item no-break">
        <div class="timeline-dot">0</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 0 — Foundation</div>
          <div class="timeline-desc">Project architecture established. Database schema designed. Environment configuration standardized. Drizzle ORM selected over Prisma for performance.</div>
          <div class="timeline-date">Foundation · ADR-001 through ADR-004</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">1</div>
        <div class="timeline-content">
          <div class="timeline-title">Phases 1–3 — Core Infrastructure</div>
          <div class="timeline-desc">Database architecture finalized (PostgreSQL + Drizzle). Authentication system built (JWT + HTTP-only cookies). Application runtime established.</div>
          <div class="timeline-date">Infrastructure Layer</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">4</div>
        <div class="timeline-content">
          <div class="timeline-title">Phases 4–8 — Product APIs & Runtime</div>
          <div class="timeline-desc">Product API contracts defined. AI provider abstraction layer built. Real-time AI streaming via Groq API. Production hardening for AI reliability. Rate limiting implemented.</div>
          <div class="timeline-date">Product Runtime · ADR-005</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">14</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 14 — Living Learning System</div>
          <div class="timeline-desc">First adaptive learning migration. Student knowledge state tracking introduced. Redis caching layer for learning data.</div>
          <div class="timeline-date">Migration 014</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">27</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 27 — Living Learner Intelligence</div>
          <div class="timeline-desc">Learner memory system. Personalized learning paths. Confidence scoring engine. Student emotional state modeling.</div>
          <div class="timeline-date">Migration 015</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">28</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 28 — Human Learning Experience</div>
          <div class="timeline-desc">Emotional memory integration. Daily challenge system. Human-centered UX patterns. Leila persona deepened with empathy layers.</div>
          <div class="timeline-date">Migration 016 · Emotional Intelligence</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">29</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 29 — Adaptive Learning Intelligence</div>
          <div class="timeline-desc">Knowledge tracing algorithms. Bayesian knowledge estimation. Cognitive pacing system. Learning velocity measurement.</div>
          <div class="timeline-date">Adaptive ML Systems</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">38</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 38 — Stabilization & Security</div>
          <div class="timeline-desc">Security hardening. Rate limiting refinement. Error boundary improvements. Child safety compliance (COPPA-aligned checks).</div>
          <div class="timeline-date">Security & Compliance</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">40</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 40 — Learning Experience Core</div>
          <div class="timeline-desc">Core learning UX rebuilt. Gamification system (XP, streaks, badges). Adventure map journey system. Engagement mechanics.</div>
          <div class="timeline-date">UX & Gamification</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">42</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 42 — Middle School Intelligence</div>
          <div class="timeline-desc">Middle school curriculum engine. Grade 7–9 adaptive paths. Subject-specific AI tutor behaviors for Arabic and Mathematics.</div>
          <div class="timeline-date">Middle School Module</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">50</div>
        <div class="timeline-content">
          <div class="timeline-title">Phases 50–53 — Full Curriculum System</div>
          <div class="timeline-desc">Complete K–12 curriculum mapping. Primary school (Phases 52), middle school (Phase 51), secondary school (Phase 53, TC/1BAC/2BAC). Deep content enhancement system.</div>
          <div class="timeline-date">Complete Curriculum Registry</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">54</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 54 — Official Alignment & Exam Intelligence</div>
          <div class="timeline-desc">Alignment to official Moroccan Ministry of Education standards. Competency matrix for all subjects. Exam-ready assessment system.</div>
          <div class="timeline-date">Official Curriculum Alignment</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot" style="background:${brand.accent}">55</div>
        <div class="timeline-content">
          <div class="timeline-title">Phase 55 — Adaptive AI Learning Platform <span class="badge badge-green">Current</span></div>
          <div class="timeline-desc">Full adaptive AI platform. Phase 55 adaptive platform feature module. Production hardening complete. Load testing verified. Parent portal. Complete observability stack.</div>
          <div class="timeline-date">Production Release v1.0 · 2026</div>
        </div>
      </div>
    </div>

    <div class="callout callout-info">
      <span class="callout-icon">🗺️</span>
      <div class="callout-content">
        <div class="callout-title">What's Coming Next</div>
        <p class="callout-body">See <strong>06_META/Product_Roadmap.pdf</strong> for the Phase 56+ feature roadmap including content factory automation, multi-language support, and B2B school licensing.</p>
      </div>
    </div>
    `,
  }),
};
