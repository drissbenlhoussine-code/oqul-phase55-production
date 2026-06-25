import { brand, pageLayout } from '../brand.mjs';

export const faq = {
  filename: 'FAQ.pdf',
  outputDir: '05_SUPPORT',
  html: pageLayout({
    title: 'FAQ',
    docLabel: 'Frequently Asked Questions',
    pageNum: '8',
    content: `
    <h1 class="section-title">Frequently Asked Questions</h1>
    <p style="color:${brand.textSecondary}; font-size:10pt; margin-bottom:20px;">Answers to the most common questions about OQUL EdTech OS — from installation to customization to scaling.</p>

    <div class="section-break"><h2>General Questions</h2></div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: What exactly is OQUL EdTech OS?</div>
      <p style="font-size:9.5pt">OQUL EdTech OS is a complete, production-ready AI educational platform and business system. It includes full source code (Next.js + Node.js), a complete K–12 curriculum registry, an AI tutor named Leila, adaptive learning algorithms, business operation templates, and everything needed to run an educational technology business.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: Do I need to know how to code to use this?</div>
      <p style="font-size:9.5pt">Basic familiarity with Node.js and web hosting is needed to deploy the platform. However, the business templates (Notion, Google Sheets, Canva) can be used independently of the technical platform. The documentation and SOPs are valuable for any educational entrepreneur, regardless of technical background.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: Can I use this for a country other than Morocco?</div>
      <p style="font-size:9.5pt">Yes. The curriculum registry is designed to be extended. The core platform (AI tutor, adaptive learning, user management) works for any educational context. You would need to replace or extend the Moroccan curriculum data with your own country's curriculum, and update Leila's language settings if you need a different language than Arabic/French/Darija.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: What language is the AI tutor (Leila) in?</div>
      <p style="font-size:9.5pt">Leila communicates in Arabic (Modern Standard Arabic), French, and Moroccan Darija (dialect). The language model used is accessed via Groq API. You can customize Leila's persona, language, and personality in <code>src/server/ai/personas/</code>.</p>
    </div>

    <div class="section-break"><h2>Technical Questions</h2></div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: What happens if my Groq API rate limit is hit?</div>
      <p style="font-size:9.5pt">The platform has a built-in reliability layer in <code>src/server/ai/reliability/</code> that handles rate limits gracefully — it queues requests, retries with exponential backoff, and displays appropriate user-facing messages. Groq's free tier supports development; upgrade to a paid plan for production traffic.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: Can I swap out Groq for OpenAI or another provider?</div>
      <p style="font-size:9.5pt">Yes. The AI provider is abstracted in <code>src/server/ai/providers/</code>. You can add an OpenAI or Anthropic provider by implementing the provider interface. The core platform doesn't depend on any specific AI provider — it uses the abstraction layer.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: How do I add new curriculum content?</div>
      <p style="font-size:9.5pt">Add new entries to the JSON files in <code>curriculum-registry/</code> following the existing schema, then run the appropriate seed script in <code>scripts/</code>. For bulk content generation, use the scripts in <code>scripts/lib/ai-lesson-enhancer.mjs</code> which uses AI to generate lesson content at scale.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: The migrations fail — what should I do?</div>
      <p style="font-size:9.5pt">First, verify your <code>DATABASE_URL</code> is correct and PostgreSQL is running. Then check that you're running the latest version of Drizzle Kit: <code>npx drizzle-kit --version</code>. If migrations still fail, check <code>db/migrations/</code> for the failing migration file and review the SQL manually. Most failures are due to permission issues with the database user.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: How do I enable Redis Sentinel for high availability?</div>
      <p style="font-size:9.5pt">Use the provided configuration at <code>infra/failover/docker-compose.redis-sentinel.yml</code> and <code>infra/failover/sentinel.conf</code>. This sets up Redis Sentinel with automatic failover. Update your <code>REDIS_URL</code> to use the Sentinel connection string format.</p>
    </div>

    <div class="section-break"><h2>Business & Commercial Questions</h2></div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: How many students can the platform support?</div>
      <p style="font-size:9.5pt">The platform has been load-tested (see <code>load-tests/</code>) to handle significant concurrent users. On a standard VPS with 4 CPUs and 8 GB RAM, you can support hundreds of concurrent active students. For thousands of concurrent students, scale horizontally using Docker Swarm or Kubernetes with the provided configurations.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: Can I white-label this and sell it under my brand?</div>
      <p style="font-size:9.5pt">Yes. Your license permits you to rebrand and deploy OQUL under your own business name and identity. You cannot, however, resell the source code or templates to third parties. See <strong>04_LEGAL/License.pdf</strong> for the complete terms.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: What's the recommended pricing model for my platform?</div>
      <p style="font-size:9.5pt">The included <strong>Subscription Strategy document</strong> in <code>02_DOCUMENTATION/</code> covers this in detail. The recommended model is a freemium tier (5 lessons/month free) + a student subscription (€9–19/month) + a family plan (€25–35/month for 3 students). This is based on the original business model in <code>docs/SUBSCRIPTION_STRATEGY.md</code>.</p>
    </div>

    <div class="card no-break">
      <div class="section-subtitle" style="margin-top:0">Q: Are there marketing templates included?</div>
      <p style="font-size:9.5pt">Yes. The <strong>03_TEMPLATES</strong> folder includes Canva templates for social media, client proposals, welcome packets, and monthly reports. The <strong>02_DOCUMENTATION</strong> folder includes the 90-Day Growth Plan which covers content strategy, launch sequence, and acquisition channels.</p>
    </div>

    <div class="section-break"><h2>Still Need Help?</h2></div>

    <div class="callout callout-info">
      <span class="callout-icon">📬</span>
      <div class="callout-content">
        <div class="callout-title">Contact Support</div>
        <p class="callout-body">If your question isn't answered here, open <strong>05_SUPPORT/Support_Guide.pdf</strong> for detailed support options, documentation links, and community resources.</p>
      </div>
    </div>
    `,
  }),
};
