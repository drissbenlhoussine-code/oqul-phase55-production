import { brand, productMeta } from '../brand.mjs';

export const cover = {
  filename: '00_Cover.pdf',
  outputDir: '00_START_HERE',
  html: `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Cover — ${productMeta.name}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&family=Inter:wght@400;500;600&display=swap');
  *, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
  html { -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  body { font-family:'Inter',sans-serif; background:${brand.secondary}; width:210mm; min-height:297mm; overflow:hidden; }

  .cover {
    width: 210mm;
    height: 297mm;
    background: ${brand.secondary};
    position: relative;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  /* Background geometric shapes */
  .bg-circle-1 {
    position: absolute;
    width: 420px; height: 420px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(37,99,235,0.25) 0%, transparent 70%);
    top: -80px; right: -80px;
    pointer-events: none;
  }
  .bg-circle-2 {
    position: absolute;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(16,185,129,0.15) 0%, transparent 70%);
    bottom: 60px; left: -60px;
    pointer-events: none;
  }
  .bg-grid {
    position: absolute;
    inset: 0;
    background-image: linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 30px 30px;
  }

  /* Top bar */
  .top-bar {
    padding: 24px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 10;
  }
  .top-bar .logo {
    font-family: 'Poppins', sans-serif;
    font-weight: 900;
    font-size: 22pt;
    color: white;
    letter-spacing: -1px;
  }
  .top-bar .logo span { color: ${brand.primary}; }
  .top-bar .version-tag {
    background: rgba(37,99,235,0.2);
    border: 1px solid rgba(37,99,235,0.4);
    color: #93C5FD;
    padding: 5px 14px;
    border-radius: 100px;
    font-size: 9pt;
    font-weight: 500;
  }

  /* Main content */
  .cover-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 30px 20px 30px;
    position: relative;
    z-index: 10;
  }

  .product-category {
    font-size: 9pt;
    font-weight: 600;
    color: ${brand.accent};
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .product-category::before {
    content: '';
    display: inline-block;
    width: 24px;
    height: 2px;
    background: ${brand.accent};
  }

  .cover-title {
    font-family: 'Poppins', sans-serif;
    font-weight: 900;
    font-size: 42pt;
    color: white;
    line-height: 1.05;
    letter-spacing: -2px;
    margin-bottom: 10px;
  }
  .cover-title .highlight { color: ${brand.primary}; }

  .cover-subtitle {
    font-size: 13pt;
    color: rgba(255,255,255,0.6);
    font-weight: 400;
    margin-bottom: 36px;
    max-width: 420px;
    line-height: 1.5;
  }

  /* Feature pills */
  .feature-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 40px;
  }
  .pill {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 100px;
    padding: 6px 14px;
    font-size: 8.5pt;
    color: rgba(255,255,255,0.75);
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .pill-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: ${brand.accent};
    flex-shrink: 0;
  }

  /* Stats bar */
  .stats-bar {
    display: flex;
    gap: 0;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 32px;
  }
  .stat-item {
    flex: 1;
    padding: 14px 18px;
    border-right: 1px solid rgba(255,255,255,0.1);
  }
  .stat-item:last-child { border-right: none; }
  .stat-item .val {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 20pt;
    color: white;
    line-height: 1.1;
  }
  .stat-item .lbl {
    font-size: 8pt;
    color: rgba(255,255,255,0.45);
    margin-top: 3px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  /* CTA row */
  .cta-row {
    display: flex;
    align-items: center;
    gap: 18px;
  }
  .cta-primary {
    background: ${brand.primary};
    color: white;
    border-radius: 10px;
    padding: 12px 26px;
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 10.5pt;
  }
  .cta-secondary {
    color: rgba(255,255,255,0.6);
    font-size: 9.5pt;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .cta-secondary::before { content: '→'; color: ${brand.accent}; font-weight: 700; }

  /* Bottom bar */
  .bottom-bar {
    padding: 18px 30px;
    border-top: 1px solid rgba(255,255,255,0.08);
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 10;
  }
  .bottom-bar .tagline {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    font-size: 10pt;
    color: rgba(255,255,255,0.4);
    letter-spacing: 0.5px;
  }
  .bottom-bar .price {
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    font-size: 16pt;
    color: white;
  }
  .bottom-bar .price span { color: ${brand.accent}; }

  /* Accent line */
  .accent-line {
    position: absolute;
    bottom: 0;
    left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, ${brand.primary}, ${brand.accent}, ${brand.primary});
  }
</style>
</head>
<body>
<div class="cover">
  <div class="bg-circle-1"></div>
  <div class="bg-circle-2"></div>
  <div class="bg-grid"></div>

  <div class="top-bar">
    <span class="logo">OQ<span>U</span>L</span>
    <span class="version-tag">Version 1.0 — 2026</span>
  </div>

  <div class="cover-content">
    <div class="product-category">Complete EdTech Business System</div>

    <h1 class="cover-title">
      The <span class="highlight">AI-Powered</span><br>
      Educational<br>
      Business OS
    </h1>

    <p class="cover-subtitle">
      Everything you need to build, operate, and scale an AI-powered educational platform — from curriculum to clients, SOPs to scaling.
    </p>

    <div class="feature-pills">
      <div class="pill"><div class="pill-dot"></div>200+ Ready Assets</div>
      <div class="pill"><div class="pill-dot"></div>AI Tutor System</div>
      <div class="pill"><div class="pill-dot"></div>Adaptive Learning</div>
      <div class="pill"><div class="pill-dot"></div>Full Curriculum Registry</div>
      <div class="pill"><div class="pill-dot"></div>Business SOPs</div>
      <div class="pill"><div class="pill-dot"></div>Notion Workspace</div>
      <div class="pill"><div class="pill-dot"></div>Google Sheets Dashboards</div>
      <div class="pill"><div class="pill-dot"></div>Canva Templates</div>
    </div>

    <div class="stats-bar">
      <div class="stat-item">
        <div class="val">55+</div>
        <div class="lbl">Build Phases</div>
      </div>
      <div class="stat-item">
        <div class="val">461</div>
        <div class="lbl">Source Files</div>
      </div>
      <div class="stat-item">
        <div class="val">K–12</div>
        <div class="lbl">Curriculum</div>
      </div>
      <div class="stat-item">
        <div class="val">100%</div>
        <div class="lbl">Production Ready</div>
      </div>
    </div>

    <div class="cta-row">
      <div class="cta-primary">Start with Read Me First →</div>
      <div class="cta-secondary">Installation Guide included</div>
    </div>
  </div>

  <div class="bottom-bar">
    <span class="tagline">Build. Teach. Scale.</span>
    <span class="price">€<span>149</span></span>
    <div class="accent-line"></div>
  </div>
</div>
</body>
</html>`,
};
