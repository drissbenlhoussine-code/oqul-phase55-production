// Brand constants for OQUL Premium Product Package
export const brand = {
  primary: '#2563EB',
  secondary: '#0F172A',
  accent: '#10B981',
  background: '#F8FAFC',
  white: '#FFFFFF',
  border: '#E5E7EB',
  textPrimary: '#0F172A',
  textSecondary: '#64748B',
  textMuted: '#94A3B8',
  danger: '#EF4444',
  warning: '#F59E0B',
  info: '#3B82F6',
};

export const productMeta = {
  name: 'OQUL EdTech OS',
  fullName: 'OQUL — Complete AI Educational Business System',
  version: 'v1.0',
  year: '2026',
  tagline: 'Build. Teach. Scale.',
  subtitle: 'The Ultimate AI-Powered Educational Platform Business Kit',
  price: '€149',
};

export const sharedCSS = `
  @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,600;0,700;0,800;1,400&family=Inter:wght@400;500;600&display=swap');

  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

  html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }

  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: ${brand.background};
    color: ${brand.textPrimary};
    font-size: 9.5pt;
    line-height: 1.65;
  }

  h1, h2, h3, h4, h5 {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    color: ${brand.secondary};
    line-height: 1.3;
  }

  .page {
    width: 210mm;
    min-height: 297mm;
    margin: 0 auto;
    background: ${brand.white};
    position: relative;
    padding: 20mm 18mm 22mm 18mm;
  }

  .page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 8px;
    border-bottom: 2px solid ${brand.primary};
    margin-bottom: 22px;
  }

  .page-header .logo {
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    font-size: 13pt;
    color: ${brand.primary};
    letter-spacing: -0.5px;
  }

  .page-header .doc-label {
    font-size: 8pt;
    color: ${brand.textSecondary};
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }

  .page-footer {
    position: fixed;
    bottom: 10mm;
    left: 18mm;
    right: 18mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid ${brand.border};
    padding-top: 6px;
  }

  .page-footer span {
    font-size: 7.5pt;
    color: ${brand.textMuted};
  }

  .page-footer .page-num {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 7.5pt;
    color: ${brand.textSecondary};
  }

  /* Section headings */
  .section-title {
    font-size: 16pt;
    font-weight: 800;
    color: ${brand.secondary};
    margin-bottom: 6px;
    margin-top: 28px;
  }
  .section-title:first-of-type { margin-top: 0; }

  .section-subtitle {
    font-size: 10.5pt;
    font-weight: 600;
    color: ${brand.primary};
    margin-top: 18px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .section-subtitle::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 16px;
    background: ${brand.primary};
    border-radius: 2px;
    flex-shrink: 0;
  }

  p { margin-bottom: 10px; color: ${brand.textPrimary}; }

  /* Cards */
  .card {
    background: ${brand.white};
    border: 1px solid ${brand.border};
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }

  .card-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 14px;
  }

  .card-grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-bottom: 14px;
  }

  .kpi-card {
    background: ${brand.white};
    border: 1px solid ${brand.border};
    border-radius: 10px;
    padding: 14px 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }

  .kpi-card .kpi-value {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 22pt;
    color: ${brand.primary};
    line-height: 1.1;
  }

  .kpi-card .kpi-label {
    font-size: 8pt;
    color: ${brand.textSecondary};
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-top: 4px;
  }

  .kpi-card .kpi-trend {
    font-size: 8pt;
    color: ${brand.accent};
    font-weight: 600;
    margin-top: 6px;
  }

  /* Callout boxes */
  .callout {
    border-radius: 8px;
    padding: 14px 16px;
    margin: 14px 0;
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .callout-icon {
    font-size: 16px;
    flex-shrink: 0;
    margin-top: 1px;
  }

  .callout-content { flex: 1; }
  .callout-title { font-weight: 600; font-size: 9.5pt; margin-bottom: 4px; }
  .callout-body { font-size: 9pt; line-height: 1.55; color: inherit; margin: 0; }

  .callout-tip { background: #EFF6FF; border-left: 4px solid ${brand.primary}; color: #1E40AF; }
  .callout-success { background: #ECFDF5; border-left: 4px solid ${brand.accent}; color: #065F46; }
  .callout-warning { background: #FFFBEB; border-left: 4px solid ${brand.warning}; color: #92400E; }
  .callout-danger { background: #FEF2F2; border-left: 4px solid ${brand.danger}; color: #991B1B; }
  .callout-info { background: #F0F9FF; border-left: 4px solid #0EA5E9; color: #0C4A6E; }

  /* Checklist */
  .checklist { list-style: none; margin: 10px 0; }
  .checklist li {
    padding: 5px 0 5px 28px;
    position: relative;
    font-size: 9.5pt;
    border-bottom: 1px solid ${brand.background};
  }
  .checklist li:last-child { border-bottom: none; }
  .checklist li::before {
    content: '☐';
    position: absolute;
    left: 4px;
    color: ${brand.primary};
    font-size: 12px;
  }
  .checklist li.done::before {
    content: '✓';
    color: ${brand.accent};
    font-weight: 700;
  }

  /* Numbered steps */
  .steps { list-style: none; margin: 12px 0; counter-reset: step-counter; }
  .steps li {
    counter-increment: step-counter;
    padding: 10px 10px 10px 48px;
    position: relative;
    margin-bottom: 8px;
    background: ${brand.background};
    border-radius: 8px;
    font-size: 9.5pt;
  }
  .steps li::before {
    content: counter(step-counter);
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    width: 22px;
    height: 22px;
    background: ${brand.primary};
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 8pt;
    line-height: 1;
  }
  .steps li strong { display: block; font-weight: 600; margin-bottom: 2px; }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 9pt;
  }

  th {
    background: ${brand.secondary};
    color: white;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    font-size: 8.5pt;
    padding: 9px 12px;
    text-align: left;
    letter-spacing: 0.3px;
  }

  td {
    padding: 8px 12px;
    border-bottom: 1px solid ${brand.border};
    vertical-align: top;
  }

  tr:nth-child(even) td { background: ${brand.background}; }
  tr:last-child td { border-bottom: none; }

  .badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 100px;
    font-size: 7.5pt;
    font-weight: 600;
    line-height: 1.6;
  }
  .badge-blue { background: #DBEAFE; color: #1D4ED8; }
  .badge-green { background: #D1FAE5; color: #065F46; }
  .badge-yellow { background: #FEF3C7; color: #92400E; }
  .badge-red { background: #FEE2E2; color: #991B1B; }
  .badge-gray { background: #F3F4F6; color: #374151; }

  /* Divider */
  .divider {
    height: 1px;
    background: ${brand.border};
    margin: 20px 0;
  }

  .divider-accent {
    height: 2px;
    background: linear-gradient(90deg, ${brand.primary}, ${brand.accent});
    margin: 20px 0;
    border-radius: 1px;
  }

  /* Highlight block */
  .highlight-block {
    background: ${brand.secondary};
    color: white;
    border-radius: 10px;
    padding: 18px 20px;
    margin: 14px 0;
  }
  .highlight-block h3 {
    color: white;
    font-size: 11pt;
    margin-bottom: 8px;
  }
  .highlight-block p { color: rgba(255,255,255,0.8); margin-bottom: 6px; }

  /* Tag row */
  .tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin: 10px 0; }
  .tag {
    background: #EFF6FF;
    color: ${brand.primary};
    border: 1px solid #BFDBFE;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 8pt;
    font-weight: 500;
  }

  /* Icon stat */
  .icon-stat-row {
    display: flex;
    gap: 12px;
    margin: 12px 0;
  }
  .icon-stat {
    flex: 1;
    background: ${brand.background};
    border-radius: 8px;
    padding: 12px 14px;
    text-align: center;
    border: 1px solid ${brand.border};
  }
  .icon-stat .stat-icon { font-size: 18px; display: block; margin-bottom: 4px; }
  .icon-stat .stat-val {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 14pt;
    color: ${brand.primary};
  }
  .icon-stat .stat-label { font-size: 8pt; color: ${brand.textSecondary}; margin-top: 2px; }

  /* Timeline */
  .timeline { margin: 14px 0; }
  .timeline-item {
    display: flex;
    gap: 14px;
    padding-bottom: 16px;
    position: relative;
  }
  .timeline-item:not(:last-child)::before {
    content: '';
    position: absolute;
    left: 16px;
    top: 30px;
    bottom: 0;
    width: 2px;
    background: ${brand.border};
  }
  .timeline-dot {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: ${brand.primary};
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 11px;
    font-weight: 700;
    font-family: 'Poppins', sans-serif;
  }
  .timeline-content { flex: 1; padding-top: 4px; }
  .timeline-title { font-weight: 600; font-size: 10pt; color: ${brand.secondary}; }
  .timeline-desc { font-size: 9pt; color: ${brand.textSecondary}; margin-top: 3px; }
  .timeline-date { font-size: 7.5pt; color: ${brand.textMuted}; font-weight: 500; margin-top: 2px; }

  /* Feature list */
  .feature-list { list-style: none; margin: 10px 0; }
  .feature-list li {
    padding: 5px 0 5px 22px;
    position: relative;
    font-size: 9.5pt;
    color: ${brand.textPrimary};
  }
  .feature-list li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: ${brand.primary};
    font-weight: 700;
  }

  /* Code block */
  .code-block {
    background: ${brand.secondary};
    color: #E2E8F0;
    border-radius: 8px;
    padding: 14px 16px;
    font-family: 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.7;
    margin: 12px 0;
    overflow: hidden;
  }
  .code-block .comment { color: #64748B; }
  .code-block .cmd { color: ${brand.accent}; }
  .code-block .str { color: #93C5FD; }

  /* Separator heading */
  .section-break {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 24px 0 16px;
  }
  .section-break h2 {
    font-size: 13pt;
    white-space: nowrap;
  }
  .section-break::after {
    content: '';
    flex: 1;
    height: 1px;
    background: ${brand.border};
  }

  /* Two-column layout */
  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }

  /* Print */
  @media print {
    .page { page-break-after: always; }
    .no-break { page-break-inside: avoid; }
  }
`;

export function pageLayout({ title, docLabel, version = productMeta.version, pageNum = '', content }) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${title} — ${productMeta.name}</title>
<style>${sharedCSS}</style>
</head>
<body>
<div class="page">
  <header class="page-header">
    <span class="logo">OQUL</span>
    <span class="doc-label">${docLabel} &nbsp;·&nbsp; ${productMeta.version}</span>
  </header>

  ${content}

  <footer class="page-footer">
    <span>${productMeta.fullName} &nbsp;·&nbsp; ${productMeta.year}</span>
    <span class="page-num">${pageNum}</span>
  </footer>
</div>
</body>
</html>`;
}
