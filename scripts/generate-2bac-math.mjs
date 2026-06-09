/**
 * Phase 58A — 2BAC Mathematics Content Generator
 *
 * Generates 20 high-quality secondary math lessons for:
 *   النهايات | الاشتقاق | التكامل | الدوال | المتتاليات
 *
 * Run: node --env-file=.env.local scripts/generate-2bac-math.mjs
 * Or:  npx tsx scripts/generate-2bac-math.mjs
 */

import fs   from "node:fs";
import path from "node:path";

// ── Env loader ──────────────────────────────────────────────────────────────
function loadEnv(file) {
  const full = path.resolve(process.cwd(), file);
  if (!fs.existsSync(full)) return;
  for (const line of fs.readFileSync(full, "utf8").split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || !trimmed.includes("=")) continue;
    const [key, ...rest] = trimmed.split("=");
    if (!process.env[key]) process.env[key] = rest.join("=").trim().replace(/^['\"]|['\"]$/g, "");
  }
}
loadEnv(".env.local");
loadEnv(".env");

const DATABASE_URL = process.env.DATABASE_URL;
const GROQ_API_KEY = process.env.GROQ_API_KEY;
if (!DATABASE_URL) throw new Error("DATABASE_URL manquant");
if (!GROQ_API_KEY)  throw new Error("GROQ_API_KEY manquant");

// ── DB client ───────────────────────────────────────────────────────────────
const { default: postgres } = await import("postgres");
const sql = postgres(DATABASE_URL, { ssl: DATABASE_URL.includes("localhost") ? false : "require" });

// ── Groq client ─────────────────────────────────────────────────────────────
const { default: Groq } = await import("groq-sdk");
const groq = new Groq({ apiKey: GROQ_API_KEY });

// ── Lesson catalog: 5 topics × 4 lessons = 20 total ─────────────────────────
const TOPICS = [
  {
    unitSlug:  "limites",
    unitTitle: "النهايات (Limites)",
    order:     1,
    lessons: [
      {
        slug:  "definition-limite",
        title: "مفهوم النهاية وتعريفها",
        objectives: ["فهم تعريف النهاية", "حساب نهايات بسيطة بالاستبدال", "تمييز الحالات التي لا توجد فيها نهاية"],
        topic: `مفهوم النهاية وتعريفها — 2BAC رياضيات.
الشرح يجب أن يغطي: التعريف الرياضي الدقيق للنهاية (lim x→a f(x))، الاستبدال المباشر، حالة 0/0، والنهايات الجانبية.
أخطاء شائعة يجب ذكرها: الخلط بين f(a) وlim f(x)، نسيان التحقق من وجود النهاية الجانبية.`,
        order: 1,
      },
      {
        slug:  "calcul-limites",
        title: "تقنيات حساب النهايات",
        objectives: ["تطبيق قواعد النهايات", "رفع الإبهام بالتبسيط والتحليل", "حساب الأشكال المحتملة ∞/∞ و∞-∞"],
        topic: `تقنيات حساب النهايات — 2BAC رياضيات.
يغطي: قواعد العمليات على النهايات، رفع الإبهام بـ: التبسيط، التحليل بالمشترك الأكبر، الضرب بالعبارة المرافقة، والنهايات المرجعية الأساسية (sin(x)/x عند 0 وlim (1+1/n)^n).`,
        order: 2,
      },
      {
        slug:  "limites-infini",
        title: "النهايات عند اللانهاية والمقاربات",
        objectives: ["حساب نهايات الدوال عند ±∞", "تحديد المقاربات الأفقية والعمودية والمائلة", "رسم المخطط النهائي"],
        topic: `النهايات عند اللانهاية والمقاربات — 2BAC رياضيات.
يغطي: النهايات عند +∞ و-∞، تحديد الحدود المسيطرة في المقامات والبسطات، المقاربة الأفقية (y=L)، المقاربة العمودية (x=a)، المقاربة المائلة (y=ax+b).`,
        order: 3,
      },
      {
        slug:  "continuite",
        title: "الاستمرارية وعلاقتها بالنهايات",
        objectives: ["تعريف الدالة المستمرة", "فحص الاستمرارية عند نقطة", "تطبيق نظرية القيم الوسيطة (TVI)"],
        topic: `الاستمرارية وعلاقتها بالنهايات — 2BAC رياضيات.
يغطي: تعريف الاستمرارية، الاستمرارية على فترة، نظرية القيم الوسيطة TVI مع الدليل وتطبيقاتها في إثبات وجود حل لمعادلة على فترة.`,
        order: 4,
      },
    ],
  },
  {
    unitSlug:  "derivation",
    unitTitle: "الاشتقاق (Dérivation)",
    order:     2,
    lessons: [
      {
        slug:  "definition-derivee",
        title: "تعريف المشتق والتأويل الهندسي",
        objectives: ["تعريف المشتق بالنهاية", "حساب مشتق دالة من التعريف", "تأويل المشتق كميل المنحنى"],
        topic: `تعريف المشتق بالنهاية والتأويل الهندسي — 2BAC رياضيات.
يغطي: التعريف f'(a)=lim (f(a+h)-f(a))/h، الحساب من التعريف، المعنى الهندسي (ميل المماس)، معادلة المماس عند نقطة، التمييز بين الدالة والمشتق.`,
        order: 1,
      },
      {
        slug:  "regles-derivation",
        title: "قواعد الاشتقاق",
        objectives: ["تطبيق قواعد مشتق المجموع والجداء والخارج", "اشتقاق الدوال المركبة", "اشتقاق الدوال المثلثية واللوغاريتمية والأسية"],
        topic: `قواعد الاشتقاق الكاملة — 2BAC رياضيات.
يغطي: مشتق الثابت، الأسية (u^n)، الجذر، sin/cos، ln، exp، قاعدة الضرب، قاعدة الخارج، قاعدة السلسلة للدوال المركبة. مع جدول الاشتقاق الأساسي ملخصاً.`,
        order: 2,
      },
      {
        slug:  "etude-variation",
        title: "تطبيق المشتق — دراسة التغير والتطرف",
        objectives: ["استخدام المشتق لتحديد اتجاه تغير الدالة", "إيجاد القيم العظمى والصغرى", "رسم جدول التغيرات"],
        topic: `تطبيق المشتق في دراسة تغير الدالة — 2BAC رياضيات.
يغطي: علاقة إشارة f'(x) بالتزايد والتناقص، القيم الحرجة، القيم العظمى والصغرى المحلية، نقاط الانعطاف، رسم جدول التغيرات الكامل كما يُطلب في الباكالوريا.`,
        order: 3,
      },
      {
        slug:  "tangente-applications",
        title: "المعادلة التنجيلية والتطبيقات",
        objectives: ["كتابة معادلة المماس والقاطعة", "استخدام المشتق في المسائل المُموضَعة", "دراسة النمو والتراجع في الاقتصاد والفيزياء"],
        topic: `المعادلة التنجيلية ومسائل تطبيق المشتق — 2BAC رياضيات.
يغطي: معادلة المماس y=f(a)+f'(a)(x-a)، المعادلة الموازية والعمودية، التطبيقات في الميكانيك (السرعة والتسارع)، الاقتصاد (الكلفة الحدية)، تحسين القيم الخطية.`,
        order: 4,
      },
    ],
  },
  {
    unitSlug:  "integration",
    unitTitle: "التكامل (Intégration)",
    order:     3,
    lessons: [
      {
        slug:  "integrale-indefinie",
        title: "التكامل غير المحدود",
        objectives: ["فهم التكامل كمعكوس الاشتقاق", "حساب التكاملات الأساسية", "تطبيق قاعدة التكامل بالتعويض"],
        topic: `التكامل غير المحدود — 2BAC رياضيات.
يغطي: التعريف كـ primitive، جدول التكاملات الأساسية، خصائص التكامل (الخطية)، تكامل الدوال المركبة من النوع u'/u و u^n * u'، طريقة التعويض البسيطة.`,
        order: 1,
      },
      {
        slug:  "integrale-definie",
        title: "التكامل المحدود — نظرية التكامل الأساسية",
        objectives: ["حساب التكامل المحدود بنظرية نيوتن-لايبنيز", "خصائص التكامل المحدود", "تطبيق المتباينات على التكامل"],
        topic: `التكامل المحدود ونظرية نيوتن-لايبنيز — 2BAC رياضيات.
يغطي: التعريف ∫_a^b f(x)dx، نظرية التكامل الأساسية F(b)-F(a)، خصائص التكامل المحدود (الإضافية، الرأسية، الإزاحة)، متباينة الوسط التكاملي، تطبيق في الفيزياء.`,
        order: 2,
      },
      {
        slug:  "calcul-aires",
        title: "حساب المساحات بالتكامل",
        objectives: ["حساب مساحة المنطقة المحاطة بمنحنى والمحور السيني", "مساحة المنطقة بين منحنيين", "اختيار العلامة الصحيحة"],
        topic: `حساب المساحات بالتكامل — 2BAC رياضيات.
يغطي: مساحة المنطقة بين المنحنى ومحور السينات (مع مراعاة الإشارة)، مساحة المنطقة بين منحنيين، تحديد نقاط التقاطع أولاً، تجزئة الفترة حسب الإشارة. هذا من أكثر الدروس ظهوراً في باكالوريا.`,
        order: 3,
      },
      {
        slug:  "equations-differentielles",
        title: "المعادلات التفاضلية البسيطة",
        objectives: ["حل المعادلة y'=ay", "حل المعادلة y'=ay+b", "تطبيق الشروط الابتدائية"],
        topic: `المعادلات التفاضلية — 2BAC رياضيات.
يغطي: المعادلة y'=ay مع الحل العام Ce^(ax)، المعادلة y'=ay+b مع الحل الخاص والعام، تحديد الثابت C بالشرط الابتدائي، التطبيقات في النمو الأسي والتسوس النووي والتبريد.`,
        order: 4,
      },
    ],
  },
  {
    unitSlug:  "fonctions",
    unitTitle: "الدوال (Fonctions)",
    order:     4,
    lessons: [
      {
        slug:  "fonction-logarithme",
        title: "الدالة اللوغاريتمية",
        objectives: ["خصائص ln", "اشتقاق وتكامل اللوغاريتم", "دراسة دالة تتضمن ln"],
        topic: `الدالة اللوغاريتمية الطبيعية ln — 2BAC رياضيات.
يغطي: تعريف ln وخصائصها الأساسية (مجال، نهايات، مشتق)، قواعد اللوغاريتم (ln(ab)=lna+lnb وما يترتب عليها)، اشتقاق وتكامل ln(u), u'/u، دراسة كاملة لدالة من نوع f(x)=xlnx أو مشابهة.`,
        order: 1,
      },
      {
        slug:  "fonction-exponentielle",
        title: "الدالة الأسية",
        objectives: ["خصائص exp وe^x", "العلاقة بين exp وln", "دراسة دالة تتضمن e^x"],
        topic: `الدالة الأسية e^x — 2BAC رياضيات.
يغطي: تعريف exp كدالة عكسية لـ ln، الخصائص الأساسية (مجال، نهايات، مشتق، معادلة المماس الأصل)، خصائص e^x، تكامل e^x وأشكال الدوال المركبة e^(u)u'، دراسة كاملة لدالة من نوع f(x)=(ax+b)e^(cx).`,
        order: 2,
      },
      {
        slug:  "etude-complete-fonction",
        title: "منهجية الدراسة الكاملة لدالة",
        objectives: ["تنفيذ الدراسة الكاملة خطوة بخطوة", "رسم المنحنى مع المقاربات", "الإجابة المنهجية في الباكالوريا"],
        topic: `منهجية الدراسة الكاملة لدالة — 2BAC رياضيات.
هذا الدرس المنهجي يغطي بالترتيب: مجال التعريف، النهايات والمقاربات، المشتق ودراسة التغير، القيم الخاصة، جدول التغيرات، التقعر ونقاط الانعطاف، رسم المنحنى. مثال كامل على دالة كسرية ثم دالة تجمع ln وexp.`,
        order: 3,
      },
      {
        slug:  "convexite-inflexion",
        title: "التقعر ونقاط الانعطاف",
        objectives: ["تعريف التقعر نحو الأعلى والأسفل", "استخدام المشتق الثاني", "إيجاد نقاط الانعطاف وأثرها في الرسم"],
        topic: `التقعر ونقاط الانعطاف — 2BAC رياضيات.
يغطي: تعريف التقعر نحو الأعلى (convexe/concave vers le haut) ونحو الأسفل، العلاقة مع إشارة f''(x)، نقطة الانعطاف حيث تتغير إشارة f''، الرسم الصحيح للمنحنى مع التقعر. أخطاء شائعة في التمييز بين القيمة العظمى ونقطة الانعطاف.`,
        order: 4,
      },
    ],
  },
  {
    unitSlug:  "suites",
    unitTitle: "المتتاليات (Suites)",
    order:     5,
    lessons: [
      {
        slug:  "suites-arithmetiques",
        title: "المتتاليات الحسابية",
        objectives: ["تعريف المتتالية الحسابية والأساس", "حساب الحد العام والحد N-th", "مجموع حدود متتالية حسابية"],
        topic: `المتتاليات الحسابية (Suites arithmétiques) — 2BAC رياضيات.
يغطي: التعريف u_{n+1}=u_n+r، الحد العام u_n=u_0+nr، مجموع n حداً S_n=n(u_0+u_{n-1})/2، إثبات أن متتالية حسابية بطريقتين (التعريف أو التعريف الصريح)، التطبيقات في الفوائد البنكية البسيطة.`,
        order: 1,
      },
      {
        slug:  "suites-geometriques",
        title: "المتتاليات الهندسية",
        objectives: ["تعريف المتتالية الهندسية والأساس q", "الحد العام والمجموع", "التطبيق في الفوائد المركبة"],
        topic: `المتتاليات الهندسية (Suites géométriques) — 2BAC رياضيات.
يغطي: التعريف u_{n+1}=q*u_n، الحد العام u_n=u_0*q^n، مجموع n حداً S_n=u_0*(1-q^n)/(1-q) لـ q≠1، مجموع عدد لا نهائي من الحدود عندما |q|<1، التطبيق في الفوائد المركبة والتناقص الأسي. هذا درس مهم جداً في الباكالوريا.`,
        order: 2,
      },
      {
        slug:  "recurrence",
        title: "الاستدلال بالاستقراء الرياضي",
        objectives: ["منهجية إثبات الاستقراء", "تطبيقه على المتتاليات", "إثبات قابلية القسمة"],
        topic: `الاستقراء الرياضي (Récurrence) — 2BAC رياضيات.
يغطي: المنهجية الكاملة لإثبات الاستقراء: الخطوة الأولى (التحقق من n=0 أو n=1)، فرض الاستقراء، إثبات الانتقال. تطبيقات: إثبات صيغة الحد العام، إثبات متباينة، إثبات قابلية القسمة. أخطاء شائعة في الخطوة الانتقالية.`,
        order: 3,
      },
      {
        slug:  "suites-recurrentes",
        title: "المتتاليات المعرفة بالتكرار",
        objectives: ["دراسة الاتجاه والحد من المتتالية u_{n+1}=f(u_n)", "إيجاد الحد الثابت", "دراسة الاتجاه بالجداول"],
        topic: `المتتاليات المعرفة بالتكرار u_{n+1}=f(u_n) — 2BAC رياضيات.
يغطي: إيجاد الحد الثابت (حل f(x)=x)، ربط اتجاه المتتالية بإشارة u_{n+1}-u_n=f(u_n)-u_n، دراسة الاتجاه برسم بياني تكراري (escalier-toile d'araignée)، حالة الاتجاه المتغير، حساب الحد الأقصى بالاستقراء.`,
        order: 4,
      },
    ],
  },
];

// ── BAC-level generation prompt ─────────────────────────────────────────────
function buildPrompt(topicDescription) {
  return `أنت خبير تربوي متخصص في مناهج الثانوي المغربي — رياضيات الثانية باكالوريا (2BAC).

المطلوب: محتوى درس كامل لـ ${topicDescription}

الشروط الإلزامية للمحتوى:
1. اللغة: العربية الفصحى الأكاديمية مع المصطلحات الفرنسية بين قوسين
2. الأسلوب: خطوات منهجية مرقمة، كما تُكتب في فرض أو امتحان باكالوريا
3. الشرح يجب أن يتضمن قسم "## أخطاء شائعة" بشكل صريح (3 أخطاء على الأقل)
4. الشرح يجب أن ينتهي بقسم "## ملخص" مع القوانين الأساسية
5. الأمثلة: كل مثال بالحل الكامل خطوة بخطوة
6. التمارين: 3 إعدادية + 3 متوسطة + 2 بمستوى الباكالوريا = 8 تمارين

أجب بـ JSON صالح فقط — بدون markdown، بدون code fences، بدون أي نص خارج الـ JSON:

{
  "explanation": "شرح أكاديمي مفصل (600-900 كلمة) يشمل التعريفات والنظريات والخطوات والأخطاء الشائعة والملخص — اكتب ## أخطاء شائعة و## ملخص كعناوين فرعية صريحة",
  "vocabulary": [
    {"word": "المصطلح العربي (Terme français)", "definition": "تعريف دقيق مختصر"},
    ... (5-7 مصطلحات)
  ],
  "examples": [
    {"text": "مثال 1: [نص المسألة]\\n\\nالحل:\\n[خطوة 1]\\n[خطوة 2]\\n...\\nالجواب: [النتيجة]", "note": "ملاحظة أو خطأ شائع مرتبط"},
    ... (3-4 أمثلة متدرجة)
  ],
  "summary": "ملخص منهجي قصير: القوانين الأساسية + تنبيه باكالوريا (5-7 أسطر)",
  "exercises": [
    {
      "type": "mcq",
      "question": "نص السؤال الكامل",
      "options": ["الخيار أ", "الخيار ب", "الخيار ج", "الخيار د"],
      "correctAnswer": "الخيار الصحيح كاملاً",
      "explanation": "شرح لماذا هذا الجواب صحيح",
      "points": 10
    },
    {
      "type": "fill_blank",
      "question": "أكمل: ... = ___",
      "correctAnswer": "الجواب",
      "explanation": "التبرير",
      "points": 15
    },
    ... (8 تمارين إجمالاً)
  ]
}`;
}

// ── Quality check ───────────────────────────────────────────────────────────
function qaCheck(lesson, titleAr) {
  const issues = [];
  const exp = lesson.explanation ?? "";

  if (exp.length < 700)                                   issues.push("explanation_too_short");
  if (!exp.includes("أخطاء شائعة"))                      issues.push("missing_common_mistakes");
  if (!exp.includes("ملخص"))                             issues.push("missing_summary");
  if ((lesson.examples ?? []).length < 3)                 issues.push("not_enough_examples");
  if ((lesson.exercises ?? []).length < 6)                issues.push("not_enough_exercises");
  if (!lesson.summary || lesson.summary.length < 50)      issues.push("summary_too_short");
  if ((lesson.vocabulary ?? []).length < 4)               issues.push("not_enough_vocabulary");

  // Placeholder detection
  const placeholders = ["يحتاج مطابقة", "مثال بسيط", "جواب نموذجي مختصر", "درس أصلي من oqul"];
  if (placeholders.some((p) => exp.includes(p)))          issues.push("placeholder_text");

  const score  = Math.max(0, 100 - issues.length * 12);
  const status = score >= 85 ? "excellent" : score >= 70 ? "good" : score >= 50 ? "needs_review" : "weak";
  return { score, status, issues, titleAr };
}

// ── Groq call with retry ─────────────────────────────────────────────────────
async function generateWithRetry(topicDescription, maxRetries = 2) {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      const completion = await groq.chat.completions.create({
        model:       "llama-3.3-70b-versatile",
        messages:    [{ role: "user", content: buildPrompt(topicDescription) }],
        max_tokens:  3500,
        temperature: 0.35,
        stream:      false,
      });

      let text = completion.choices[0]?.message?.content ?? "{}";
      // Strip any accidental markdown fences
      text = text.replace(/^```(?:json)?\s*/m, "").replace(/\s*```$/m, "").trim();
      const parsed = JSON.parse(text);

      if (!parsed.explanation || !parsed.exercises) {
        throw new Error("Missing required fields in generated content");
      }
      return parsed;
    } catch (err) {
      if (attempt === maxRetries) throw err;
      console.log(`  ⚠ Attempt ${attempt + 1} failed, retrying in 3s...`);
      await new Promise((r) => setTimeout(r, 3000));
    }
  }
}

// ── DB upsert helpers ────────────────────────────────────────────────────────
async function getGradeId(slug) {
  const rows = await sql`select id from grades where slug = ${slug} limit 1`;
  if (!rows[0]) throw new Error(`Grade '${slug}' not found in DB — run npm run db:seed first`);
  return rows[0].id;
}

async function upsertSubject(gradeId, slug, titleAr) {
  const rows = await sql`
    insert into subjects (grade_id, slug, title_ar, icon, color, order_index, is_active)
    values (${gradeId}, ${slug}, ${titleAr}, 'Calculator', '#7c3aed', 1, true)
    on conflict (grade_id, slug) do update
      set title_ar = excluded.title_ar, is_active = true
    returning id
  `;
  return rows[0].id;
}

async function upsertUnit(subjectId, slug, titleAr, orderIndex) {
  const rows = await sql`
    insert into units (subject_id, slug, title_ar, order_index, is_published)
    values (${subjectId}, ${slug}, ${titleAr}, ${orderIndex}, true)
    on conflict (subject_id, slug) do update
      set title_ar = excluded.title_ar, order_index = excluded.order_index
    returning id
  `;
  return rows[0].id;
}

async function upsertLesson(unitId, slug, titleAr, objectives, orderIndex) {
  const rows = await sql`
    insert into lessons (unit_id, slug, title_ar, objectives, difficulty, estimated_duration_minutes, order_index, is_published)
    values (${unitId}, ${slug}, ${titleAr}, ${JSON.stringify(objectives)}::jsonb, 'hard', 40, ${orderIndex}, true)
    on conflict (unit_id, slug) do update
      set title_ar = excluded.title_ar, objectives = excluded.objectives,
          difficulty = 'hard', is_published = true
    returning id
  `;
  return rows[0].id;
}

async function upsertContent(lessonId, generated) {
  await sql`
    insert into lesson_contents (lesson_id, explanation, vocabulary, examples, summary)
    values (
      ${lessonId},
      ${generated.explanation},
      ${JSON.stringify(generated.vocabulary ?? [])}::jsonb,
      ${JSON.stringify((generated.examples ?? []).map((e) => ({ text: e.text, note: e.note ?? "" })))}::jsonb,
      ${generated.summary ?? ""}
    )
    on conflict (lesson_id) do update
      set explanation = excluded.explanation,
          vocabulary  = excluded.vocabulary,
          examples    = excluded.examples,
          summary     = excluded.summary
  `;
}

async function replaceExercises(lessonId, exercises) {
  await sql`delete from exercises where lesson_id = ${lessonId}`;
  if (!exercises?.length) return;
  for (let i = 0; i < exercises.length; i++) {
    const ex = exercises[i];
    const opts = ex.options ? JSON.stringify(ex.options) : null;
    await sql`
      insert into exercises (lesson_id, type, question, options, correct_answer, explanation, order_index, points)
      values (
        ${lessonId},
        ${ex.type ?? "mcq"},
        ${ex.question},
        ${opts ? sql`${opts}::jsonb` : null},
        ${ex.correctAnswer ?? ex.correct_answer ?? ""},
        ${ex.explanation ?? ""},
        ${i + 1},
        ${ex.points ?? 10}
      )
    `;
  }
}

// ── Main ─────────────────────────────────────────────────────────────────────
async function main() {
  console.log("\n🎓 Phase 58A — 2BAC Mathematics Content Generator");
  console.log("=".repeat(60));

  const gradeId    = await getGradeId("bac2");
  const subjectId  = await upsertSubject(gradeId, "advanced-math", "الرياضيات — ثانية باكالوريا");
  console.log(`✅ Grade bac2 found | Subject upserted`);

  const report = { generated: 0, saved: 0, failed: 0, qaResults: [], batches: [] };
  let batchIndex = 0;

  for (const topic of TOPICS) {
    console.log(`\n📐 وحدة: ${topic.unitTitle}`);
    const unitId = await upsertUnit(subjectId, topic.unitSlug, topic.unitTitle, topic.order);

    const batchResults = [];

    for (const lessonDef of topic.lessons) {
      process.stdout.write(`  ➜ ${lessonDef.title} ... `);

      try {
        const lessonId = await upsertLesson(unitId, lessonDef.slug, lessonDef.title, lessonDef.objectives, lessonDef.order);
        report.generated++;

        const generated = await generateWithRetry(lessonDef.topic);
        const qa = qaCheck(generated, lessonDef.title);

        await upsertContent(lessonId, generated);
        await replaceExercises(lessonId, generated.exercises);
        report.saved++;

        batchResults.push(qa);
        report.qaResults.push(qa);
        console.log(`✅ (QA: ${qa.score}/100 — ${qa.status})`);

        // Rate limit pause
        await new Promise((r) => setTimeout(r, 1500));

      } catch (err) {
        report.failed++;
        console.log(`❌ FAILED: ${err.message}`);
        batchResults.push({ score: 0, status: "failed", issues: [err.message], titleAr: lessonDef.title });
        report.qaResults.push({ score: 0, status: "failed", titleAr: lessonDef.title });
      }
    }

    // ── Batch QA report after each unit (4 lessons) ─────────────────────────
    batchIndex++;
    const batchAvg  = Math.round(batchResults.reduce((a, b) => a + b.score, 0) / batchResults.length);
    const batchPass = batchResults.filter((r) => r.score >= 70).length;
    report.batches.push({ unit: topic.unitTitle, avg: batchAvg, passed: batchPass, total: batchResults.length });

    console.log(`\n  📊 Batch ${batchIndex} QA: ${batchPass}/${batchResults.length} passed | avg ${batchAvg}/100`);
    if (batchPass < batchResults.length) {
      const failing = batchResults.filter((r) => r.score < 70);
      for (const f of failing) {
        console.log(`     ⚠ ${f.titleAr}: ${f.issues?.join(", ") ?? "failed"}`);
      }
    }
  }

  // ── Final report ───────────────────────────────────────────────────────────
  const avgQA    = Math.round(report.qaResults.reduce((a, b) => a + b.score, 0) / report.qaResults.length);
  const passing  = report.qaResults.filter((r) => r.score >= 70).length;

  console.log("\n" + "=".repeat(60));
  console.log("📋 FINAL REPORT — Phase 58A 2BAC Math");
  console.log("=".repeat(60));
  console.log(`✅ Generated:  ${report.generated}/20`);
  console.log(`💾 Saved to DB: ${report.saved}/20`);
  console.log(`❌ Failed:      ${report.failed}`);
  console.log(`📊 QA avg score: ${avgQA}/100`);
  console.log(`🎯 QA passing (≥70): ${passing}/${report.qaResults.length}`);
  console.log("\nPer-batch summary:");
  for (const b of report.batches) {
    const icon = b.passed === b.total ? "✅" : "⚠";
    console.log(`  ${icon} ${b.unit}: ${b.passed}/${b.total} passed | avg ${b.avg}/100`);
  }

  if (report.failed > 0) {
    console.log("\n⚠ Failed lessons (need manual review):");
    report.qaResults.filter((r) => r.score === 0).forEach((r) => console.log(`  - ${r.titleAr}`));
  }

  console.log("\n✅ Phase 58A complete. 2BAC math content is live in the DB.");
  console.log("=".repeat(60));

  // Save JSON report
  const reportPath = "reports/phase58a-2bac-math-report.json";
  fs.mkdirSync("reports", { recursive: true });
  fs.writeFileSync(reportPath, JSON.stringify({ ...report, avgQA, passing, timestamp: new Date().toISOString() }, null, 2));
  console.log(`📄 Detailed report saved to: ${reportPath}`);
}

main()
  .catch((err) => { console.error("\n❌ Script failed:", err); process.exitCode = 1; })
  .finally(async () => { await sql.end(); });
