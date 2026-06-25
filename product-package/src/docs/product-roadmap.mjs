import { brand, pageLayout } from '../brand.mjs';

export const productRoadmap = {
  filename: 'Product_Roadmap.pdf',
  outputDir: '06_META',
  html: pageLayout({
    title: 'Product Roadmap',
    docLabel: 'Product Roadmap',
    pageNum: '13',
    content: `
    <h1 class="section-title">Product Roadmap</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:18px;">The OQUL EdTech OS roadmap — what's built, what's coming, and the long-term vision for the platform.</p>

    <div class="highlight-block">
      <h3>Vision: The Operating System for Education</h3>
      <p>OQUL aims to be the foundational infrastructure layer for AI-powered education — as essential to EdTech businesses as AWS is to cloud businesses. Every student deserves a personalized, adaptive learning experience powered by AI.</p>
    </div>

    <div class="section-break"><h2>Current State — v1.0 (Phase 55)</h2></div>

    <div class="card-grid">
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Shipped ✅</div>
        <ul class="checklist">
          <li class="done">AI tutor (Leila) with Darija support</li>
          <li class="done">Adaptive learning engine</li>
          <li class="done">Full K–12 curriculum (12 grade levels)</li>
          <li class="done">Official exam alignment</li>
          <li class="done">Parent monitoring portal</li>
          <li class="done">Gamification (XP, badges, streaks)</li>
          <li class="done">Daily challenges</li>
          <li class="done">Knowledge tracing</li>
          <li class="done">Email verification</li>
          <li class="done">Production observability stack</li>
        </ul>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Platform Stats</div>
        <table style="margin:0">
          <tr><td>Grade Levels</td><td><strong>12</strong></td></tr>
          <tr><td>Source Files</td><td><strong>461</strong></td></tr>
          <tr><td>API Endpoints</td><td><strong>50+</strong></td></tr>
          <tr><td>DB Migrations</td><td><strong>17</strong></td></tr>
          <tr><td>Seed Scripts</td><td><strong>50+</strong></td></tr>
          <tr><td>Load Test Suites</td><td><strong>5</strong></td></tr>
          <tr><td>Build Phases</td><td><strong>55</strong></td></tr>
        </table>
      </div>
    </div>

    <div class="section-break"><h2>Phase 56 — Content Factory</h2></div>

    <div class="tag-row">
      <span class="tag">Q2 2026</span>
      <span class="tag">Planned</span>
      <span class="tag">Content Generation</span>
    </div>

    <div class="card">
      <p style="font-size:9.5pt; margin-bottom:12px">Automated AI content generation pipeline to scale curriculum coverage beyond the current hand-crafted lessons. Full specification available in <code>docs/phase-58-content-factory/</code>.</p>
      <ul class="feature-list">
        <li>AI-powered lesson generator with quality gates</li>
        <li>2BAC Mathematics full content automation</li>
        <li>Batch content generation with human review workflow</li>
        <li>Quality scoring system for generated content</li>
        <li>Content versioning and rollback capabilities</li>
        <li>Pilot batch: 50 lessons per subject, validated by educators</li>
      </ul>
    </div>

    <div class="section-break"><h2>Phase 57 — Multi-Language Expansion</h2></div>

    <div class="tag-row">
      <span class="tag">Q3 2026</span>
      <span class="tag">Planned</span>
      <span class="tag">Internationalization</span>
    </div>

    <div class="card">
      <ul class="feature-list">
        <li>Full internationalization (i18n) framework implementation</li>
        <li>French-first curriculum variant for Francophone Africa</li>
        <li>English curriculum module for international schools</li>
        <li>Leila persona localization (name, dialect, cultural context)</li>
        <li>Right-to-left (RTL) layout refinements for Arabic</li>
      </ul>
    </div>

    <div class="section-break"><h2>Phase 58 — B2B School Licensing</h2></div>

    <div class="tag-row">
      <span class="tag">Q4 2026</span>
      <span class="tag">Planned</span>
      <span class="tag">Enterprise</span>
    </div>

    <div class="card">
      <ul class="feature-list">
        <li>School/institution licensing module</li>
        <li>Bulk student enrollment via CSV/API</li>
        <li>School administrator dashboard</li>
        <li>Teacher performance analytics</li>
        <li>Classroom management interface</li>
        <li>API for integration with existing school ERP systems</li>
        <li>White-label SDK for school-branded apps</li>
      </ul>
    </div>

    <div class="section-break"><h2>Long-Term Vision (2027+)</h2></div>

    <div class="timeline">
      <div class="timeline-item no-break">
        <div class="timeline-dot">A</div>
        <div class="timeline-content">
          <div class="timeline-title">AI Tutor Marketplace</div>
          <div class="timeline-desc">Allow educators to create and sell custom AI tutor personas and curriculum packs within the OQUL ecosystem.</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">B</div>
        <div class="timeline-content">
          <div class="timeline-title">Mobile Applications</div>
          <div class="timeline-desc">Native iOS and Android apps with offline lesson access, push notification reminders, and mobile-optimized adaptive experiences.</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">C</div>
        <div class="timeline-content">
          <div class="timeline-title">Regional Expansion API</div>
          <div class="timeline-desc">Open API for third-party curriculum providers to plug their content into the OQUL adaptive learning engine.</div>
        </div>
      </div>
      <div class="timeline-item no-break">
        <div class="timeline-dot">D</div>
        <div class="timeline-content">
          <div class="timeline-title">OQUL Cloud</div>
          <div class="timeline-desc">Managed hosting option — deploy OQUL with zero infrastructure management. Focus on content and business, not servers.</div>
        </div>
      </div>
    </div>

    <div class="callout callout-tip">
      <span class="callout-icon">🔔</span>
      <div class="callout-content">
        <div class="callout-title">Stay Updated</div>
        <p class="callout-body">Major releases are delivered as new product versions. This roadmap reflects the development direction as of v1.0 release. Priorities may shift based on community needs and market feedback.</p>
      </div>
    </div>
    `,
  }),
};
