import { brand, pageLayout } from '../brand.mjs';

export const businessOverview = {
  filename: 'Business_Overview.pdf',
  outputDir: '02_DOCUMENTATION',
  html: pageLayout({
    title: 'Business Overview',
    docLabel: 'Business Overview',
    pageNum: '6',
    content: `
    <h1 class="section-title">Business Overview</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:18px;">A complete overview of the OQUL EdTech OS business model, market positioning, revenue strategy, and operational framework.</p>

    <div class="section-break"><h2>The Opportunity</h2></div>

    <div class="card-grid">
      <div class="kpi-card no-break">
        <div class="kpi-value">€2.6B</div>
        <div class="kpi-label">MENA EdTech Market 2025</div>
        <div class="kpi-trend">↑ 18% YoY growth</div>
      </div>
      <div class="kpi-card no-break">
        <div class="kpi-value">37M</div>
        <div class="kpi-label">Students K–12 in Morocco</div>
        <div class="kpi-trend">Target: 1% = 370,000 users</div>
      </div>
      <div class="kpi-card no-break">
        <div class="kpi-value">87%</div>
        <div class="kpi-label">Mobile Internet Penetration</div>
        <div class="kpi-trend">Digital-first generation</div>
      </div>
    </div>

    <div class="section-break"><h2>What OQUL Is</h2></div>

    <p>OQUL (عقل — "mind") is an AI-powered adaptive learning platform for K–12 students. At its core is <strong>Leila</strong>, an AI tutor that teaches in Arabic, French, and Moroccan Darija dialect — creating a culturally authentic learning experience that traditional platforms cannot match.</p>

    <p>Unlike generic AI tools, OQUL is purpose-built for the Moroccan curriculum, aligned to official Ministry of Education standards, and designed to adapt to each student's individual pace and learning style.</p>

    <div class="section-break"><h2>Core Value Propositions</h2></div>

    <div class="three-col">
      <div class="card no-break" style="padding:14px">
        <div style="font-size:18px; margin-bottom:8px">🧠</div>
        <div style="font-weight:700; font-size:10pt; margin-bottom:6px">Adaptive Intelligence</div>
        <p style="font-size:8.5pt; color:${brand.textSecondary}; margin:0">Every student gets a personalized learning path. Difficulty, pace, and content adapt in real-time based on performance data.</p>
      </div>
      <div class="card no-break" style="padding:14px">
        <div style="font-size:18px; margin-bottom:8px">🌍</div>
        <div style="font-weight:700; font-size:10pt; margin-bottom:6px">Cultural Authenticity</div>
        <p style="font-size:8.5pt; color:${brand.textSecondary}; margin:0">Leila speaks in Darija. Curriculum follows official standards. Content reflects Moroccan cultural context — not translated Western content.</p>
      </div>
      <div class="card no-break" style="padding:14px">
        <div style="font-size:18px; margin-bottom:8px">📊</div>
        <div style="font-weight:700; font-size:10pt; margin-bottom:6px">Parent Transparency</div>
        <p style="font-size:8.5pt; color:${brand.textSecondary}; margin:0">Parents see exactly what their child is learning, their strengths, gaps, and progress — in real time. Builds trust and retention.</p>
      </div>
    </div>

    <div class="section-break"><h2>Revenue Model</h2></div>

    <table>
      <thead><tr><th>Tier</th><th>Price</th><th>Features</th><th>Target</th></tr></thead>
      <tbody>
        <tr>
          <td><span class="badge badge-gray">Free</span></td>
          <td>€0/month</td>
          <td>5 lessons/month, basic progress tracking</td>
          <td>Top-of-funnel acquisition</td>
        </tr>
        <tr>
          <td><span class="badge badge-blue">Student</span></td>
          <td>€9–19/month</td>
          <td>Unlimited lessons, all subjects, Leila AI, progress reports</td>
          <td>Core revenue base</td>
        </tr>
        <tr>
          <td><span class="badge badge-green">Family</span></td>
          <td>€25–35/month</td>
          <td>3 student accounts, parent dashboard, priority support</td>
          <td>High-LTV families</td>
        </tr>
        <tr>
          <td><span class="badge badge-yellow">School</span></td>
          <td>Custom pricing</td>
          <td>Bulk students, admin dashboard, teacher analytics, SLA</td>
          <td>B2B enterprise</td>
        </tr>
      </tbody>
    </table>

    <div class="section-break"><h2>Unit Economics</h2></div>

    <div class="card-grid">
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Student Tier Projection</div>
        <table style="margin:0; font-size:8.5pt">
          <tr><td>Monthly subscribers</td><td><strong>1,000</strong></td></tr>
          <tr><td>Average price</td><td><strong>€14/month</strong></td></tr>
          <tr><td>Monthly Revenue</td><td><strong>€14,000</strong></td></tr>
          <tr><td>Groq API cost</td><td><strong>~€800</strong></td></tr>
          <tr><td>Server costs</td><td><strong>~€300</strong></td></tr>
          <tr><td><strong>Net Monthly</strong></td><td><strong style="color:${brand.accent}">~€12,900</strong></td></tr>
        </table>
      </div>
      <div class="card no-break">
        <div class="section-subtitle" style="margin-top:0">Scale Scenario (5K users)</div>
        <table style="margin:0; font-size:8.5pt">
          <tr><td>Monthly subscribers</td><td><strong>5,000</strong></td></tr>
          <tr><td>Average price</td><td><strong>€14/month</strong></td></tr>
          <tr><td>Monthly Revenue</td><td><strong>€70,000</strong></td></tr>
          <tr><td>Groq API cost</td><td><strong>~€4,000</strong></td></tr>
          <tr><td>Server costs</td><td><strong>~€1,200</strong></td></tr>
          <tr><td><strong>Net Monthly</strong></td><td><strong style="color:${brand.accent}">~€64,800</strong></td></tr>
        </table>
      </div>
    </div>

    <div class="section-break"><h2>Competitive Advantages</h2></div>

    <div class="card">
      <table style="margin:0">
        <thead><tr><th>Feature</th><th>OQUL</th><th>Generic Tutoring Apps</th><th>YouTube/Khan</th></tr></thead>
        <tbody>
          <tr><td>Arabic/Darija AI tutor</td><td><span class="badge badge-green">✓ Native</span></td><td><span class="badge badge-red">✗ None</span></td><td><span class="badge badge-red">✗ None</span></td></tr>
          <tr><td>Moroccan curriculum</td><td><span class="badge badge-green">✓ Full K–12</span></td><td><span class="badge badge-yellow">Partial</span></td><td><span class="badge badge-red">✗ None</span></td></tr>
          <tr><td>Adaptive learning</td><td><span class="badge badge-green">✓ Real-time</span></td><td><span class="badge badge-yellow">Basic</span></td><td><span class="badge badge-red">✗ None</span></td></tr>
          <tr><td>Parent portal</td><td><span class="badge badge-green">✓ Full</span></td><td><span class="badge badge-yellow">Limited</span></td><td><span class="badge badge-red">✗ None</span></td></tr>
          <tr><td>Exam alignment</td><td><span class="badge badge-green">✓ Official</span></td><td><span class="badge badge-red">✗ None</span></td><td><span class="badge badge-red">✗ None</span></td></tr>
        </tbody>
      </table>
    </div>

    <div class="callout callout-success">
      <span class="callout-icon">📈</span>
      <div class="callout-content">
        <div class="callout-title">Next: 90-Day Growth Plan</div>
        <p class="callout-body">See <strong>90_Day_Growth_Plan.pdf</strong> in this folder for the step-by-step launch strategy to acquire your first 100 paying subscribers.</p>
      </div>
    </div>
    `,
  }),
};
