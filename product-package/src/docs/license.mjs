import { brand, productMeta, pageLayout } from '../brand.mjs';

export const license = {
  filename: 'License.pdf',
  outputDir: '04_LEGAL',
  html: pageLayout({
    title: 'License',
    docLabel: 'End User License Agreement',
    pageNum: '9',
    content: `
    <h1 class="section-title">License Agreement</h1>
    <p style="color:${brand.textSecondary}; font-size:9.5pt; margin-bottom:16px;">OQUL EdTech OS — End User License Agreement (EULA) &nbsp;·&nbsp; Version 1.0 &nbsp;·&nbsp; Effective: January 2026</p>

    <div class="callout callout-info">
      <span class="callout-icon">📋</span>
      <div class="callout-content">
        <div class="callout-title">License Summary (Plain Language)</div>
        <p class="callout-body">You may use this product for one commercial business. You may customize it, deploy it, and earn revenue from it. You may NOT resell it, share it, or redistribute it. This summary is for convenience only — the full terms below are legally binding.</p>
      </div>
    </div>

    <div class="section-break"><h2>1. Grant of License</h2></div>
    <p>Upon purchase of OQUL EdTech OS ("the Product"), the purchaser ("Licensee") is granted a non-exclusive, non-transferable, perpetual license to use the Product for one (1) commercial business or project. This license is personal to the Licensee and cannot be assigned or transferred to any third party without prior written consent.</p>

    <div class="section-break"><h2>2. Permitted Uses</h2></div>
    <div class="card">
      <ul class="checklist">
        <li class="done">Deploy the platform as a commercial educational service</li>
        <li class="done">Customize and modify the source code for your own use</li>
        <li class="done">White-label and rebrand the product under your business name</li>
        <li class="done">Use the templates (Notion, Google Sheets, Canva, Word) for your business</li>
        <li class="done">Generate revenue from students using your deployed platform</li>
        <li class="done">Use the SOPs and business documentation to operate your business</li>
        <li class="done">Add new curriculum content to the curriculum registry</li>
        <li class="done">Integrate with additional third-party services and APIs</li>
      </ul>
    </div>

    <div class="section-break"><h2>3. Prohibited Uses</h2></div>
    <div class="card">
      <ul class="checklist">
        <li>Resell, sublicense, or redistribute the Product or its source code</li>
        <li>Share access to the Product files with individuals who have not purchased</li>
        <li>Use the Product to create a competing product for sale</li>
        <li>Remove or alter any license notices or attribution within the code</li>
        <li>Use the Leila AI persona name/identity commercially without modification</li>
        <li>Deploy the product for more than one distinct commercial entity</li>
        <li>Upload the source code to public repositories</li>
      </ul>
    </div>

    <div class="section-break"><h2>4. Intellectual Property</h2></div>
    <p>The Product, including all source code, documentation, templates, designs, and curriculum data, remains the intellectual property of the original creator. The Licensee's customizations and additions are owned by the Licensee. The Licensee does not acquire any ownership rights to the original Product through this license.</p>

    <div class="section-break"><h2>5. Third-Party Components</h2></div>
    <p>This Product incorporates open-source libraries including Next.js (MIT), React (MIT), Tailwind CSS (MIT), Drizzle ORM (Apache 2.0), and others listed in <code>package.json</code>. These components are subject to their own respective licenses. The Licensee is responsible for compliance with all third-party license terms. The Groq API integration requires a separate account and is subject to Groq's Terms of Service.</p>

    <div class="section-break"><h2>6. Disclaimer of Warranties</h2></div>
    <p>The Product is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. The creator does not warrant that the Product will be error-free, uninterrupted, or meet the Licensee's specific requirements.</p>

    <div class="section-break"><h2>7. Limitation of Liability</h2></div>
    <p>In no event shall the creator be liable for any indirect, incidental, special, exemplary, or consequential damages arising out of or in connection with the use of the Product, including but not limited to loss of revenue, data, or business opportunity, even if advised of the possibility of such damages. The creator's total liability shall not exceed the purchase price of the Product.</p>

    <div class="section-break"><h2>8. Updates and Support</h2></div>
    <p>This license covers the version of the Product purchased. Future major version updates (e.g., v2.0) may require a separate purchase or upgrade license. Bug fix releases within the same major version are provided at no additional cost to existing licensees where commercially reasonable. Support is provided as described in the Support Guide.</p>

    <div class="section-break"><h2>9. Governing Law</h2></div>
    <p>This Agreement shall be governed by and construed in accordance with applicable commercial law. Any disputes arising under this Agreement shall be subject to binding arbitration.</p>

    <div class="divider"></div>

    <div class="card" style="background:${brand.background}; border-color:${brand.border}">
      <div style="display:flex; justify-content:space-between; align-items:center">
        <div>
          <div style="font-weight:700; font-size:10pt">OQUL EdTech OS ${productMeta.version}</div>
          <div style="font-size:8.5pt; color:${brand.textSecondary}; margin-top:2px">License effective upon purchase</div>
        </div>
        <div style="text-align:right">
          <div style="font-size:8.5pt; color:${brand.textSecondary}">Issue Date: January 2026</div>
          <div style="font-size:8.5pt; color:${brand.textSecondary}">License Type: Commercial Single Entity</div>
        </div>
      </div>
    </div>
    `,
  }),
};
