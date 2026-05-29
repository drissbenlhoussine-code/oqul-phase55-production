import fs from "node:fs";
import path from "node:path";
import pg from "pg";
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });
dotenv.config({ path: ".env" });

const { Client } = pg;

const WRITE_SOURCE = process.argv.includes("--write-source");
const APPLY_DB = process.argv.includes("--apply-db");

const sourcePath = path.join(
  process.cwd(),
  "src",
  "features",
  "secondary",
  "data",
  "TC",
  "advanced_math.json"
);

const pilot = {
  lessonId: "TC_advanced_math_10_1",
  registryId: "TC-math-19-01",
  grade: "TC",
  gradeLabelAr: "الجذع المشترك",
  subject: "advanced_math",
  subjectLabelAr: "الرياضيات",
  unit: "probability",
  title: "الاحتمالات: مفاهيم أساسية",
  description:
    "مدخل منهجي إلى الاحتمالات في مستوى الجذع المشترك: تجربة عشوائية، مجموعة الإمكانات، حدث، وأول حساب لاحتمال حدث بسيط.",
  objectives: [
    "تمييز التجربة العشوائية عن التجربة الحتمية من خلال أمثلة مدرسية ومغربية قريبة.",
    "تحديد مجموعة الإمكانات وكتابة الأحداث باستعمال لغة رياضية دقيقة.",
    "حساب احتمال حدث بسيط في حالة تساوي الإمكانات باستعمال النسبة: عدد الحالات الملائمة على عدد الحالات الممكنة.",
    "تبرير الجواب والتحقق من أن الاحتمال عدد بين 0 و 1."
  ],
  prerequisites: [
    "الكسور والنسب المئوية.",
    "قراءة جداول بسيطة وتنظيم المعطيات.",
    "مفهوم المجموعة والانتماء إلى مجموعة.",
    "العد المنظم للحالات الممكنة."
  ],
  misconceptions: [
    "اعتبار الحدث الأكثر رغبة هو بالضرورة الأكثر احتمالا.",
    "نسيان عد جميع الحالات الممكنة قبل حساب الاحتمال.",
    "كتابة احتمال أكبر من 1 أو أصغر من 0 دون الانتباه إلى معنى الاحتمال.",
    "الخلط بين الحدث والنتيجة الواحدة داخل التجربة العشوائية."
  ],
  content: {
    explanation: [
      "في الاحتمالات ندرس وضعيات لا نعرف نتيجتها مسبقا، ولكن نستطيع وصف النتائج الممكنة وتنظيمها. نسمي هذه الوضعية تجربة عشوائية، مثل رمي قطعة نقدية، رمي نرد متوازن، أو اختيار بطاقة عشوائيا من علبة.",
      "مجموعة الإمكانات هي جميع النتائج الممكنة للتجربة. مثلا عند رمي نرد عادي مرة واحدة تكون مجموعة الإمكانات هي {1, 2, 3, 4, 5, 6}. الحدث هو جزء من هذه المجموعة، مثل الحصول على عدد زوجي: {2, 4, 6}.",
      "عندما تكون كل النتائج الممكنة لها نفس الحظ في الوقوع، نحسب احتمال حدث A بالقانون: P(A) = عدد الحالات الملائمة للحدث A / عدد الحالات الممكنة. لذلك فاحتمال الحصول على عدد زوجي عند رمي نرد متوازن هو 3/6 = 1/2.",
      "في ورقة الفرض لا يكفي إعطاء العدد النهائي فقط. نكتب التجربة، مجموعة الإمكانات، الحدث المطلوب، عدد الحالات الملائمة، ثم نحسب ونفسر النتيجة."
    ].join("\n\n"),
    definitions: [
      {
        term: "تجربة عشوائية",
        definition: "تجربة لا يمكن معرفة نتيجتها قبل إنجازها، رغم أننا نستطيع معرفة النتائج الممكنة."
      },
      {
        term: "مجموعة الإمكانات",
        definition: "مجموعة كل النتائج الممكنة لتجربة عشوائية، ويرمز لها غالبا ب Ω."
      },
      {
        term: "حدث",
        definition: "جزء من مجموعة الإمكانات؛ يتحقق الحدث إذا كانت النتيجة المحصل عليها تنتمي إليه."
      },
      {
        term: "احتمال حدث",
        definition: "عدد بين 0 و 1 يقيس حظ وقوع الحدث."
      }
    ],
    stepByStepExample: {
      prompt:
        "نرمي نردا متوازنا مرة واحدة. ما احتمال الحصول على عدد أكبر من 4؟",
      steps: [
        "نحدد مجموعة الإمكانات: Ω = {1, 2, 3, 4, 5, 6}.",
        "نحدد الحدث A: الحصول على عدد أكبر من 4، إذن A = {5, 6}.",
        "نعد الحالات الملائمة: عدد عناصر A هو 2.",
        "نعد الحالات الممكنة: عدد عناصر Ω هو 6.",
        "نحسب: P(A) = 2/6 = 1/3.",
        "نفسر: حظ الحصول على عدد أكبر من 4 هو ثلث المحاولات تقريبا إذا كررنا التجربة مرات كثيرة."
      ],
      answer: "P(A) = 1/3"
    },
    vocabulary: [
      { word: "Ω", definition: "رمز مجموعة الإمكانات في تجربة عشوائية." },
      { word: "حدث أكيد", definition: "حدث احتماله 1 لأنه يتحقق دائما." },
      { word: "حدث مستحيل", definition: "حدث احتماله 0 لأنه لا يمكن أن يتحقق." },
      { word: "حالات ملائمة", definition: "النتائج التي تجعل الحدث المطلوب يتحقق." }
    ],
    examples: [
      {
        text:
          "عند رمي قطعة نقدية متوازنة، مجموعة الإمكانات هي {صورة، كتابة}. احتمال الحصول على صورة هو 1/2.",
        note: "مثال تأسيسي لفهم تساوي الإمكانات."
      },
      {
        text:
          "في كيس توجد 3 كرات حمراء و2 زرقاء من نفس الحجم. احتمال سحب كرة زرقاء هو 2/5.",
        note: "نعد الحالات الملائمة أولا، ثم نقسم على مجموع الحالات."
      },
      {
        text:
          "إذا كان الحدث هو الحصول على عدد من 1 إلى 6 عند رمي نرد عادي، فهو حدث أكيد واحتماله 1.",
        note: "يساعد على تثبيت معنى الحدث الأكيد."
      }
    ],
    exercises: [
      {
        level: "easy",
        question:
          "نرمي قطعة نقدية متوازنة مرة واحدة. حدد مجموعة الإمكانات، ثم احسب احتمال الحصول على كتابة.",
        hint: "ابدأ بكتابة النتيجتين الممكنتين فقط.",
        answer: "Ω = {صورة، كتابة}، واحتمال الحصول على كتابة هو 1/2."
      },
      {
        level: "medium",
        question:
          "نرمي نردا متوازنا مرة واحدة. احسب احتمال الحصول على عدد فردي، ثم احتمال الحصول على عدد أصغر من 3.",
        hint: "اكتب الحدثين كمجموعتين فرعيتين من {1, 2, 3, 4, 5, 6}.",
        answer:
          "الأعداد الفردية {1, 3, 5} إذن الاحتمال 3/6 = 1/2. الأعداد الأصغر من 3 هي {1, 2} إذن الاحتمال 2/6 = 1/3."
      },
      {
        level: "hard",
        question:
          "في علبة 4 بطاقات مرقمة 1 و2 و3 و4. نسحب بطاقة واحدة عشوائيا. احسب احتمال سحب عدد يقبل القسمة على 2، ثم بين هل الحدث 'سحب عدد أكبر من 5' مستحيل أم لا.",
        hint: "استعمل معنى الحدث المستحيل: لا توجد أي حالة ملائمة.",
        answer:
          "الأعداد التي تقبل القسمة على 2 هي {2, 4}، إذن الاحتمال 2/4 = 1/2. الحدث 'عدد أكبر من 5' مستحيل لأن مجموعة الحالات الملائمة فارغة، واحتماله 0."
      }
    ],
    commonMistakes: [
      {
        mistake: "حساب الاحتمال قبل تحديد مجموعة الإمكانات.",
        correction:
          "نلزم المتعلم بكتابة Ω أولا، ثم الحدث A، ثم التعويض في القانون."
      },
      {
        mistake: "اعتبار احتمال حدث ما مساويا لعدد حالاته الملائمة فقط.",
        correction:
          "نذكر بأن الاحتمال نسبة: الحالات الملائمة مقسومة على جميع الحالات الممكنة."
      },
      {
        mistake: "عدم تبسيط الكسر أو عدم تفسيره.",
        correction:
          "بعد الحساب، نبسط الكسر إن أمكن ونضيف جملة تفسيرية قصيرة."
      }
    ],
    hints: [
      "ما هي كل النتائج الممكنة؟ لا تبدأ بالحساب قبل كتابتها.",
      "ما الحالات التي تحقق الحدث المطلوب فقط؟ ضع تحتها خطا.",
      "هل جوابك بين 0 و 1؟ إذا لم يكن كذلك فهناك خطأ في العد أو القسمة."
    ],
    correctionMethod: [
      "أطلب من المتعلم إعادة صياغة التجربة بكلماته.",
      "أجعله يكتب Ω ثم الحدث A في سطرين منفصلين.",
      "إذا أخطأ في العد، نستعمل جدولا صغيرا أو لائحة منظمة.",
      "إذا أعطى الجواب فقط، أطلب تبرير كل خطوة كما في الفرض.",
      "أختم بسؤال تحقق: هل الاحتمال قريب من 0 أم من 1؟ ولماذا؟"
    ],
    summary:
      "الاحتمال يقيس حظ وقوع حدث في تجربة عشوائية. في حالة تساوي الإمكانات نحسبه بقسمة عدد الحالات الملائمة على عدد الحالات الممكنة، ويجب دائما أن يكون بين 0 و 1.",
    leilaInstructions: [
      "ابدئي بسؤال قصير: ما النتائج الممكنة في هذه التجربة؟",
      "لا تعطي القانون مباشرة؛ اجعلي المتعلم يكتشف أن الاحتمال نسبة بين حالتين معدودتين.",
      "استعملي أمثلة مغربية بسيطة مثل نرد في لعبة، بطاقات في علبة، أو قرعة داخل القسم.",
      "إذا أخطأ المتعلم، أعطي تلميحا حول العد قبل التصحيح.",
      "اطلبي منه في النهاية تفسير معنى النتيجة بجملة عربية واضحة."
    ]
  },
  assessment: {
    quickCheck: 3,
    guidedExercises: 3,
    examStyleQuestions: 1,
    masteryThreshold: 80
  },
  leilaMode: {
    defaultLanguage: "formal_arabic",
    canSwitchTo: ["darija", "french", "english"],
    teachingStyle: "socratic_step_by_step",
    tone: "serious_motivating",
    instructions: [
      "ركزي على التمييز بين التجربة العشوائية والحدث.",
      "طالبي دائما بكتابة مجموعة الإمكانات قبل حساب الاحتمال.",
      "شجعي التلميذ على تفسير الكسر الناتج لا الاكتفاء بالحساب.",
      "استعملي الدارجة المغربية فقط للتشجيع أو إزالة التوتر، ثم عودي للمصطلح الرياضي الفصيح."
    ]
  }
};

function updateSourceJson() {
  const lessons = JSON.parse(fs.readFileSync(sourcePath, "utf8"));
  const index = lessons.findIndex((lesson) => lesson.lessonId === pilot.lessonId);

  if (index === -1) {
    throw new Error(`Pilot lesson not found in ${sourcePath}: ${pilot.lessonId}`);
  }

  lessons[index] = {
    ...lessons[index],
    title: pilot.title,
    description: pilot.description,
    objectives: pilot.objectives,
    prerequisites: pilot.prerequisites,
    misconceptions: pilot.misconceptions,
    content: pilot.content,
    assessment: pilot.assessment,
    leilaMode: pilot.leilaMode
  };

  fs.writeFileSync(sourcePath, `${JSON.stringify(lessons, null, 2)}\n`, "utf8");
}

async function getColumns(client, tableName) {
  const result = await client.query(
    `
    select column_name
    from information_schema.columns
    where table_schema = 'public'
      and table_name = $1
    `,
    [tableName]
  );
  return new Set(result.rows.map((row) => row.column_name));
}

function firstColumn(columns, candidates) {
  return candidates.find((candidate) => columns.has(candidate));
}

async function applyDatabasePatch() {
  if (!process.env.DATABASE_URL) {
    throw new Error("DATABASE_URL is required for --apply-db");
  }

  const client = new Client({ connectionString: process.env.DATABASE_URL });
  await client.connect();

  try {
    const lessonColumns = await getColumns(client, "lessons");
    const contentColumns = await getColumns(client, "lesson_contents");
    const exerciseColumns = await getColumns(client, "exercises");
    const gradeColumns = await getColumns(client, "grades");
    const subjectColumns = await getColumns(client, "subjects");
    const unitColumns = await getColumns(client, "units");

    const lessonTitleColumn = firstColumn(lessonColumns, ["title_ar", "title"]);
    const objectivesColumn = firstColumn(lessonColumns, ["objectives"]);
    const contentTextColumn = firstColumn(contentColumns, ["explanation", "content"]);
    const vocabularyColumn = firstColumn(contentColumns, ["vocabulary"]);
    const examplesColumn = firstColumn(contentColumns, ["examples"]);
    const summaryColumn = firstColumn(contentColumns, ["summary"]);

    if (!lessonTitleColumn || !contentTextColumn) {
      throw new Error("Unsupported curriculum schema for pilot enhancer");
    }

    const gradeCodeColumns = ["slug", "code"].filter((column) => gradeColumns.has(column));
    const subjectCodeColumns = ["slug", "code"].filter((column) => subjectColumns.has(column));
    const unitSlugColumn = firstColumn(unitColumns, ["slug"]);
    const unitTitleColumns = ["title_ar", "title"].filter((column) => unitColumns.has(column));
    const lessonSlugColumn = firstColumn(lessonColumns, ["slug"]);
    const lessonTitleColumns = ["title_ar", "title"].filter((column) => lessonColumns.has(column));

    const where = [];
    const params = [];

    if (gradeCodeColumns.length) {
      where.push(`lower(coalesce(${gradeCodeColumns.map((column) => `g.${column}`).join(", ")})) = 'tc'`);
    }

    if (subjectCodeColumns.length) {
      where.push(`lower(coalesce(${subjectCodeColumns.map((column) => `s.${column}`).join(", ")})) in ('math', 'advanced_math')`);
    }

    const unitPredicates = [];
    if (unitSlugColumn) unitPredicates.push(`lower(coalesce(u.${unitSlugColumn}, '')) = 'probability'`);
    for (const column of unitTitleColumns) {
      params.push("الاحتمالات");
      unitPredicates.push(`u.${column} = $${params.length}`);
    }
    if (unitPredicates.length) where.push(`(${unitPredicates.join(" or ")})`);

    const lessonPredicates = [];
    for (const column of lessonTitleColumns) {
      params.push(pilot.title);
      lessonPredicates.push(`l.${column} = $${params.length}`);
    }
    if (lessonSlugColumn) lessonPredicates.push(`lower(coalesce(l.${lessonSlugColumn}, '')) like '%probability%'`);
    if (lessonPredicates.length) where.push(`(${lessonPredicates.join(" or ")})`);

    const lessonResult = await client.query(
      `
      select l.id
      from lessons l
      join units u on u.id = l.unit_id
      join subjects s on s.id = u.subject_id
      join grades g on g.id = s.grade_id
      where ${where.length ? where.join("\n        and ") : "true"}
      order by l.order_index asc nulls last
      limit 1
      `,
      params
    );

    const lessonId = lessonResult.rows[0]?.id;
    if (!lessonId) {
      throw new Error("Pilot DB lesson not found: TC math probability");
    }

    await client.query("begin");

    const lessonUpdates = [`${lessonTitleColumn} = $1`];
    const lessonParams = [pilot.title];
    if (objectivesColumn) {
      lessonUpdates.push(`${objectivesColumn} = $2::jsonb`);
      lessonParams.push(JSON.stringify(pilot.objectives));
    }
    lessonParams.push(lessonId);
    await client.query(
      `update lessons set ${lessonUpdates.join(", ")} where id = $${lessonParams.length}`,
      lessonParams
    );

    const contentUpdates = [`${contentTextColumn} = $1`];
    const contentParams = [pilot.content.explanation];
    if (vocabularyColumn) {
      contentUpdates.push(`${vocabularyColumn} = $${contentParams.length + 1}::jsonb`);
      contentParams.push(JSON.stringify(pilot.content.vocabulary));
    }
    if (examplesColumn) {
      contentUpdates.push(`${examplesColumn} = $${contentParams.length + 1}::jsonb`);
      contentParams.push(JSON.stringify(pilot.content.examples));
    }
    if (summaryColumn) {
      contentUpdates.push(`${summaryColumn} = $${contentParams.length + 1}`);
      contentParams.push(pilot.content.summary);
    }

    const existingContent = await client.query(
      "select id from lesson_contents where lesson_id = $1 limit 1",
      [lessonId]
    );

    if (existingContent.rows[0]) {
      contentParams.push(lessonId);
      await client.query(
        `update lesson_contents set ${contentUpdates.join(", ")} where lesson_id = $${contentParams.length}`,
        contentParams
      );
    } else {
      const insertColumns = ["lesson_id", contentTextColumn];
      const insertValues = ["$1", "$2"];
      const insertParams = [lessonId, pilot.content.explanation];
      if (vocabularyColumn) {
        insertColumns.push(vocabularyColumn);
        insertValues.push(`$${insertParams.length + 1}::jsonb`);
        insertParams.push(JSON.stringify(pilot.content.vocabulary));
      }
      if (examplesColumn) {
        insertColumns.push(examplesColumn);
        insertValues.push(`$${insertParams.length + 1}::jsonb`);
        insertParams.push(JSON.stringify(pilot.content.examples));
      }
      if (summaryColumn) {
        insertColumns.push(summaryColumn);
        insertValues.push(`$${insertParams.length + 1}`);
        insertParams.push(pilot.content.summary);
      }
      await client.query(
        `insert into lesson_contents (${insertColumns.join(", ")}) values (${insertValues.join(", ")})`,
        insertParams
      );
    }

    const questionColumn = firstColumn(exerciseColumns, ["question"]);
    const answerColumn = firstColumn(exerciseColumns, ["correct_answer", "correctAnswer"]);
    const explanationColumn = firstColumn(exerciseColumns, ["explanation"]);
    const typeColumn = firstColumn(exerciseColumns, ["type"]);
    const orderColumn = firstColumn(exerciseColumns, ["order_index", "orderIndex"]);
    const pointsColumn = firstColumn(exerciseColumns, ["points"]);

    if (questionColumn && answerColumn && typeColumn) {
      for (const [index, exercise] of pilot.content.exercises.entries()) {
        const existing = await client.query(
          `select id from exercises where lesson_id = $1 and ${questionColumn} = $2 limit 1`,
          [lessonId, exercise.question]
        );
        if (existing.rows[0]) continue;

        const columns = ["lesson_id", questionColumn, answerColumn, typeColumn];
        const values = ["$1", "$2", "$3", "$4"];
        const params = [lessonId, exercise.question, exercise.answer, "short_answer"];

        if (explanationColumn) {
          columns.push(explanationColumn);
          values.push(`$${params.length + 1}`);
          params.push(exercise.hint);
        }
        if (orderColumn) {
          columns.push(orderColumn);
          values.push(`$${params.length + 1}`);
          params.push(index + 1);
        }
        if (pointsColumn) {
          columns.push(pointsColumn);
          values.push(`$${params.length + 1}`);
          params.push((index + 1) * 10);
        }

        await client.query(
          `insert into exercises (${columns.join(", ")}) values (${values.join(", ")})`,
          params
        );
      }
    }

    await client.query("commit");
    console.log(`Updated DB pilot lesson: ${lessonId}`);
  } catch (error) {
    await client.query("rollback").catch(() => {});
    throw error;
  } finally {
    await client.end();
  }
}

if (!WRITE_SOURCE && !APPLY_DB) {
  console.log("Dry run only. Use --write-source to update JSON and --apply-db to patch the database.");
  console.log({
    sourcePath,
    lessonId: pilot.lessonId,
    registryId: pilot.registryId,
    title: pilot.title,
    objectives: pilot.objectives.length,
    exercises: pilot.content.exercises.length
  });
}

if (WRITE_SOURCE) {
  updateSourceJson();
  console.log(`Updated source pilot lesson: ${sourcePath}`);
}

if (APPLY_DB) {
  await applyDatabasePatch();
}
