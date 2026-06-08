import fs from "node:fs";
import path from "node:path";
import { neon, neonConfig, Pool as NeonPool } from "@neondatabase/serverless";
import { WebSocket } from "ws";
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });
dotenv.config({ path: ".env" });

export const DEFAULT_PLACEHOLDER_THRESHOLD = 75;

export function parseArgs(argv = process.argv.slice(2)) {
  const args = { _: [] };
  for (const arg of argv) {
    if (!arg.startsWith("--")) {
      args._.push(arg);
      continue;
    }
    const [key, ...rest] = arg.slice(2).split("=");
    args[key] = rest.length ? rest.join("=") : true;
  }
  return args;
}

export function requireDatabaseUrl() {
  if (!process.env.DATABASE_URL) {
    throw new Error("DATABASE_URL is required. Load it from .env.local, .env, or your shell.");
  }
  return process.env.DATABASE_URL;
}

function makeHttpClient(connectionString) {
  const sql = neon(connectionString);
  return {
    async query(text, params = []) {
      const rows = await sql.query(text, params);
      return { rows, rowCount: rows.length };
    },
    release() {},
  };
}

export async function withDb(fn, { useHttp = false } = {}) {
  if (useHttp) {
    const client = makeHttpClient(requireDatabaseUrl());
    return await fn(client);
  }
  // WebSocket pool — required for transactional writes (BEGIN/COMMIT/ROLLBACK)
  neonConfig.webSocketConstructor = WebSocket;
  const pool = new NeonPool({
    connectionString: requireDatabaseUrl(),
    connectionTimeoutMillis: 20_000,
    idleTimeoutMillis: 30_000,
    max: 1,
  });
  const client = await pool.connect();
  try {
    return await fn(client);
  } finally {
    client.release();
    await pool.end();
  }
}

export async function withReadDb(fn) {
  return withDb(fn, { useHttp: true });
}

export async function getColumns(client, tableName) {
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

export async function getSchemaInfo(client) {
  const tableNames = ["cycles", "grades", "subjects", "units", "lessons", "lesson_contents", "exercises"];
  const entries = await Promise.all(tableNames.map(async (name) => [name, await getColumns(client, name)]));
  return Object.fromEntries(entries);
}

export function pickColumn(columns, candidates, label) {
  const column = candidates.find((candidate) => columns.has(candidate));
  if (!column && label) throw new Error(`Unsupported schema: missing ${label} column.`);
  return column;
}

export function q(identifier) {
  return `"${String(identifier).replaceAll('"', '""')}"`;
}

function coalesce(alias, columns, fallback = "''") {
  const available = columns.map((column) => `${alias}.${q(column)}`);
  return `coalesce(${available.length ? available.join(", ") : fallback}, ${fallback})`;
}

function ilikeAny(columnSql, values, params) {
  const placeholders = values.map((value) => {
    params.push(value);
    return `$${params.length}`;
  });
  return `lower(${columnSql}) in (${placeholders.join(", ")})`;
}

function exactAnyAcross(alias, columns, values, params) {
  const predicates = [];
  for (const column of columns.filter(Boolean)) {
    predicates.push(ilikeAny(`lower(${alias}.${q(column)})`, values, params));
  }
  return `(${predicates.join(" or ")})`;
}

function likeAcross(alias, columns, value, params) {
  const predicates = [];
  for (const column of columns.filter(Boolean)) {
    params.push(`%${String(value).toLowerCase()}%`);
    predicates.push(`lower(${alias}.${q(column)}) like $${params.length}`);
  }
  return `(${predicates.join(" or ")})`;
}

export function lessonText(row) {
  return [
    row.lesson_title,
    row.unit_title,
    row.subject_title,
    row.grade_title,
    row.explanation,
    row.summary,
    JSON.stringify(row.objectives ?? []),
    JSON.stringify(row.vocabulary ?? []),
    JSON.stringify(row.examples ?? []),
  ]
    .filter(Boolean)
    .join("\n");
}

export function scoreLessonQuality(row) {
  const issues = [];
  const text = lessonText(row);
  const normalized = text.toLowerCase();
  const exerciseCount = Number(row.exercise_count ?? row.exercises?.length ?? 0);

  const placeholderMarkers = [
    "هذا درس في",
    "هذا درس تمهيدي",
    "درس أصلي من oqul مبني على عنوان المنهج فقط",
    "تمرين 1 سهل",
    "جواب نموذجي مختصر",
    "مثال مبسط حول",
    "يحتاج مطابقة",
    "placeholder",
    "generic",
    "Ø",
    "Ù",
  ];

  if (!String(row.explanation ?? "").trim()) issues.push("missing_content");
  if (String(row.explanation ?? "").trim().length < 900) issues.push("too_short");
  if (placeholderMarkers.some((marker) => normalized.includes(marker.toLowerCase()))) {
    issues.push("placeholder_text");
  }
  if (!/المغرب|مغربي|مغربية|المنهاج|الجذع المشترك|الفرض|الامتحان/.test(text)) {
    issues.push("missing_moroccan_context");
  }
  if (!/تعريف|مفهوم|نسمي|يرمز|قاعدة/.test(text)) issues.push("missing_definitions");
  if (!/مثال|خطوة|نحسب|الحل/.test(text)) issues.push("missing_worked_examples");
  if (!/تمرين|تطبيق|تدريب|أجب|احسب/.test(text)) issues.push("missing_guided_practice");
  if (exerciseCount < 3) issues.push("missing_exercises");
  if (!/الجواب|تصحيح|correct|answer|شرح/.test(text)) issues.push("missing_answers");
  if (!/خطأ|أخطاء|خلط|نسيان/.test(text)) issues.push("missing_common_mistakes");
  if (!/تلميح|العلاج|تصحيح|إعادة|remediation/.test(text)) issues.push("missing_remediation");
  if (!/فرض|امتحان|وضعية|استعداد/.test(text)) issues.push("missing_exam_prep");
  if (!/ملخص|خلاصة/.test(text)) issues.push("missing_summary");
  if (!/ليلى|Leila|leila/.test(text)) issues.push("missing_leila_instructions");

  const score = Math.max(0, Math.min(100, 100 - issues.length * 8));
  const status = score >= 90 ? "excellent" : score >= 75 ? "good" : score >= 50 ? "needs_review" : "weak";
  return { score, status, issues };
}

export function printLessonSummary(label, row) {
  const quality = scoreLessonQuality(row);
  console.log(`\n${label}`);
  console.table([
    {
      id: row.lesson_id ?? row.id,
      title: row.lesson_title ?? row.title_ar ?? row.title,
      grade: row.grade_slug ?? row.grade_title,
      subject: row.subject_slug ?? row.subject_title,
      unit: row.unit_slug ?? row.unit_title,
      contentChars: String(row.explanation ?? "").length,
      exercises: row.exercise_count ?? row.exercises?.length ?? 0,
      quality: quality.score,
      status: quality.status,
    },
  ]);
  if (quality.issues.length) console.log("Quality issues:", quality.issues.join(", "));
  console.log("Content preview:", String(row.explanation ?? "").replace(/\s+/g, " ").slice(0, 360));
}

export async function fetchLessons(client, filters = {}) {
  const schema = await getSchemaInfo(client);
  const lessonTitle = pickColumn(schema.lessons, ["title_ar", "title"], "lesson title");
  const lessonSlug = pickColumn(schema.lessons, ["slug"]);
  const objectives = pickColumn(schema.lessons, ["objectives"]);
  const unitTitle = pickColumn(schema.units, ["title_ar", "title", "name"], "unit title");
  const unitSlug = pickColumn(schema.units, ["slug"]);
  const subjectTitle = pickColumn(schema.subjects, ["title_ar", "title", "name"], "subject title");
  const subjectSlug = pickColumn(schema.subjects, ["slug", "code"]);
  const gradeTitle = pickColumn(schema.grades, ["title_ar", "title", "name"], "grade title");
  const gradeSlug = pickColumn(schema.grades, ["slug", "code"]);
  const cycleTitle = pickColumn(schema.cycles, ["title_ar", "title", "name"]);
  const cycleSlug = pickColumn(schema.cycles, ["slug", "code"]);
  const explanation = pickColumn(schema.lesson_contents, ["explanation", "content"]);
  const vocabulary = pickColumn(schema.lesson_contents, ["vocabulary"]);
  const examples = pickColumn(schema.lesson_contents, ["examples"]);
  const summary = pickColumn(schema.lesson_contents, ["summary"]);

  const where = [];
  const params = [];

  if (filters.lessonId) {
    params.push(filters.lessonId);
    where.push(`l.id = $${params.length}`);
  }
  if (filters.grade) {
    where.push(exactAnyAcross("g", [gradeSlug, gradeTitle], [String(filters.grade).toLowerCase()], params));
  }
  if (filters.subject) {
    const subjectValues = String(filters.subject)
      .split(",")
      .map((value) => value.trim().toLowerCase())
      .filter(Boolean);
    where.push(exactAnyAcross("s", [subjectSlug, subjectTitle], subjectValues, params));
  }
  if (filters.unit) {
    where.push(likeAcross("u", [unitSlug, unitTitle], filters.unit, params));
  }
  if (filters.title) {
    where.push(likeAcross("l", [lessonSlug, lessonTitle], filters.title, params));
  }

  const limit = Number(filters.limit ?? 500);
  params.push(limit);

  const result = await client.query(
    `
      select
        l.id as lesson_id,
        l.${q(lessonTitle)} as lesson_title,
        ${lessonSlug ? `l.${q(lessonSlug)}` : "null"} as lesson_slug,
        ${objectives ? `l.${q(objectives)}` : "'[]'::jsonb"} as objectives,
        l.unit_id,
        u.id as unit_id,
        u.${q(unitTitle)} as unit_title,
        ${unitSlug ? `u.${q(unitSlug)}` : "null"} as unit_slug,
        s.id as subject_id,
        s.${q(subjectTitle)} as subject_title,
        ${subjectSlug ? `s.${q(subjectSlug)}` : "null"} as subject_slug,
        g.id as grade_id,
        g.${q(gradeTitle)} as grade_title,
        ${gradeSlug ? `g.${q(gradeSlug)}` : "null"} as grade_slug,
        c.id as cycle_id,
        ${cycleTitle ? `c.${q(cycleTitle)}` : "null"} as cycle_title,
        ${cycleSlug ? `c.${q(cycleSlug)}` : "null"} as cycle_slug,
        lc.id as content_id,
        lc.${q(explanation)} as explanation,
        ${vocabulary ? `lc.${q(vocabulary)}` : "'[]'::jsonb"} as vocabulary,
        ${examples ? `lc.${q(examples)}` : "'[]'::jsonb"} as examples,
        ${summary ? `lc.${q(summary)}` : "null"} as summary,
        coalesce(ex.exercise_count, 0)::int as exercise_count
      from lessons l
      join units u on u.id = l.unit_id
      join subjects s on s.id = u.subject_id
      join grades g on g.id = s.grade_id
      left join cycles c on c.id = g.cycle_id
      left join lesson_contents lc on lc.lesson_id = l.id
      left join (
        select lesson_id, count(*) as exercise_count
        from exercises
        group by lesson_id
      ) ex on ex.lesson_id = l.id
      where ${where.length ? where.join("\n        and ") : "true"}
      order by g.order_index nulls last, s.order_index nulls last, u.order_index nulls last, l.order_index nulls last
      limit $${params.length}
    `,
    params
  );

  return result.rows;
}

export async function fetchLessonForViewer(client, lessonId) {
  const lessonRows = await fetchLessons(client, { lessonId, limit: 2 });
  const lesson = lessonRows[0];
  if (!lesson) return null;

  const exercises = await client.query(
    `
      select id, type, question, options, correct_answer as "correctAnswer", explanation, order_index as "orderIndex", points
      from exercises
      where lesson_id = $1
      order by order_index asc
    `,
    [lessonId]
  );

  return {
    id: lesson.lesson_id,
    titleAr: lesson.lesson_title,
    slug: lesson.lesson_slug,
    objectives: lesson.objectives ?? [],
    content: {
      id: lesson.content_id,
      explanation: lesson.explanation,
      vocabulary: lesson.vocabulary ?? [],
      examples: lesson.examples ?? [],
      summary: lesson.summary,
    },
    exercises: exercises.rows,
    unit: {
      id: lesson.unit_id,
      titleAr: lesson.unit_title,
      slug: lesson.unit_slug,
      subject: {
        id: lesson.subject_id,
        titleAr: lesson.subject_title,
        slug: lesson.subject_slug,
        grade: {
          id: lesson.grade_id,
          titleAr: lesson.grade_title,
          slug: lesson.grade_slug,
          cycle: { id: lesson.cycle_id, titleAr: lesson.cycle_title, slug: lesson.cycle_slug },
        },
      },
    },
  };
}

export function readJson(filePath) {
  return JSON.parse(fs.readFileSync(path.resolve(process.cwd(), filePath), "utf8"));
}

export function getPilotSourceLesson() {
  const filePath = "src/features/secondary/data/TC/advanced_math.json";
  const lessons = readJson(filePath);
  const lesson = lessons.find((item) => item.lessonId === "TC_advanced_math_10_1");
  if (!lesson) throw new Error(`Pilot lesson TC_advanced_math_10_1 not found in ${filePath}`);
  return { filePath, lesson };
}

export function buildDbPayloadFromEnhancedLesson(lesson) {
  const content = lesson.content ?? {};
  const definitions = Array.isArray(content.definitions)
    ? content.definitions.map((item) => `${item.term}: ${item.definition}`).join("\n")
    : "";
  const stepExample = content.stepByStepExample
    ? [
        `مثال محلول: ${content.stepByStepExample.prompt}`,
        ...(content.stepByStepExample.steps ?? []).map((step, index) => `${index + 1}. ${step}`),
        `الجواب: ${content.stepByStepExample.answer}`,
      ].join("\n")
    : "";
  const commonMistakes = Array.isArray(content.commonMistakes)
    ? content.commonMistakes.map((item) => `خطأ شائع: ${item.mistake}\nالتصحيح: ${item.correction}`).join("\n\n")
    : "";
  const hints = Array.isArray(content.hints) ? content.hints.map((hint) => `تلميح: ${hint}`).join("\n") : "";
  const correction = Array.isArray(content.correctionMethod)
    ? content.correctionMethod.map((step, index) => `${index + 1}. ${step}`).join("\n")
    : "";
  const leilaInstructions = Array.isArray(content.leilaInstructions)
    ? content.leilaInstructions.map((step) => `ليلى: ${step}`).join("\n")
    : "";

  const explanation = [
    lesson.description,
    content.explanation,
    definitions && `تعريفات أساسية:\n${definitions}`,
    stepExample,
    commonMistakes && `أخطاء شائعة وطريقة التصحيح:\n${commonMistakes}`,
    hints && `تلميحات موجهة:\n${hints}`,
    correction && `طريقة العلاج والتصحيح:\n${correction}`,
    "استعداد للفرض: اكتب مجموعة الإمكانات، حدد الحدث، احسب النسبة، ثم فسر هل الجواب بين 0 و1.",
    leilaInstructions && `تعليمات ليلى:\n${leilaInstructions}`,
  ]
    .filter(Boolean)
    .join("\n\n");

  return {
    title: lesson.title,
    objectives: lesson.objectives ?? [],
    explanation,
    vocabulary: content.vocabulary ?? [],
    examples: content.examples ?? [],
    summary: content.summary ?? lesson.description ?? "",
    exercises: (content.exercises ?? []).map((exercise, index) => ({
      type: "short_answer",
      question: exercise.question,
      correctAnswer: exercise.answer,
      explanation: exercise.hint ?? exercise.answer,
      points: (index + 1) * 10,
      orderIndex: index + 1,
    })),
  };
}

export async function updateLessonWithPayload(client, lessonId, payload, options = {}) {
  const schema = await getSchemaInfo(client);
  const lessonTitle = pickColumn(schema.lessons, ["title_ar", "title"], "lesson title");
  const objectives = pickColumn(schema.lessons, ["objectives"]);
  const explanation = pickColumn(schema.lesson_contents, ["explanation", "content"], "lesson content");
  const vocabulary = pickColumn(schema.lesson_contents, ["vocabulary"]);
  const examples = pickColumn(schema.lesson_contents, ["examples"]);
  const summary = pickColumn(schema.lesson_contents, ["summary"]);

  const counts = {
    lessons: 0,
    lessonContentsUpdated: 0,
    lessonContentsInserted: 0,
    exercisesDeleted: 0,
    exercisesInserted: 0,
  };

  await client.query("begin");
  try {
    const lessonSets = [`${q(lessonTitle)} = $1`];
    const lessonParams = [payload.title];
    if (objectives) {
      lessonSets.push(`${q(objectives)} = $${lessonParams.length + 1}::jsonb`);
      lessonParams.push(JSON.stringify(payload.objectives ?? []));
    }
    lessonParams.push(lessonId);
    const lessonUpdate = await client.query(
      `update lessons set ${lessonSets.join(", ")} where id = $${lessonParams.length}`,
      lessonParams
    );
    counts.lessons = lessonUpdate.rowCount ?? 0;
    if (counts.lessons !== 1) throw new Error(`Expected to update 1 lesson row, updated ${counts.lessons}.`);

    const contentRows = await client.query("select id from lesson_contents where lesson_id = $1", [lessonId]);
    if (contentRows.rows.length > 1) {
      throw new Error(`Safety abort: lesson ${lessonId} has multiple lesson_contents rows.`);
    }

    if (contentRows.rows.length === 1) {
      const sets = [`${q(explanation)} = $1`];
      const params = [payload.explanation];
      if (vocabulary) {
        sets.push(`${q(vocabulary)} = $${params.length + 1}::jsonb`);
        params.push(JSON.stringify(payload.vocabulary ?? []));
      }
      if (examples) {
        sets.push(`${q(examples)} = $${params.length + 1}::jsonb`);
        params.push(JSON.stringify(payload.examples ?? []));
      }
      if (summary) {
        sets.push(`${q(summary)} = $${params.length + 1}`);
        params.push(payload.summary ?? null);
      }
      params.push(lessonId);
      const contentUpdate = await client.query(
        `update lesson_contents set ${sets.join(", ")} where lesson_id = $${params.length}`,
        params
      );
      counts.lessonContentsUpdated = contentUpdate.rowCount ?? 0;
      if (counts.lessonContentsUpdated !== 1) {
        throw new Error(`Expected to update 1 lesson_contents row, updated ${counts.lessonContentsUpdated}.`);
      }
    } else {
      const columns = ["lesson_id", explanation];
      const values = ["$1", "$2"];
      const params = [lessonId, payload.explanation];
      if (vocabulary) {
        columns.push(vocabulary);
        values.push(`$${params.length + 1}::jsonb`);
        params.push(JSON.stringify(payload.vocabulary ?? []));
      }
      if (examples) {
        columns.push(examples);
        values.push(`$${params.length + 1}::jsonb`);
        params.push(JSON.stringify(payload.examples ?? []));
      }
      if (summary) {
        columns.push(summary);
        values.push(`$${params.length + 1}`);
        params.push(payload.summary ?? null);
      }
      const contentInsert = await client.query(
        `insert into lesson_contents (${columns.map(q).join(", ")}) values (${values.join(", ")})`,
        params
      );
      counts.lessonContentsInserted = contentInsert.rowCount ?? 0;
      if (counts.lessonContentsInserted !== 1) {
        throw new Error(`Expected to insert 1 lesson_contents row, inserted ${counts.lessonContentsInserted}.`);
      }
    }

    if (options.replaceExercises) {
      const deleted = await client.query("delete from exercises where lesson_id = $1", [lessonId]);
      counts.exercisesDeleted = deleted.rowCount ?? 0;
    }

    if (payload.exercises?.length) {
      for (const exercise of payload.exercises) {
        const inserted = await client.query(
          `
            insert into exercises (lesson_id, type, question, options, correct_answer, explanation, order_index, points)
            values ($1, $2, $3, $4::jsonb, $5, $6, $7, $8)
          `,
          [
            lessonId,
            exercise.type ?? "short_answer",
            exercise.question,
            exercise.options ? JSON.stringify(exercise.options) : null,
            exercise.correctAnswer,
            exercise.explanation ?? null,
            exercise.orderIndex ?? counts.exercisesInserted + 1,
            exercise.points ?? 10,
          ]
        );
        counts.exercisesInserted += inserted.rowCount ?? 0;
      }
      if (counts.exercisesInserted !== payload.exercises.length) {
        throw new Error(`Expected to insert ${payload.exercises.length} exercises, inserted ${counts.exercisesInserted}.`);
      }
    }

    await client.query("commit");
    return counts;
  } catch (error) {
    await client.query("rollback").catch(() => {});
    throw error;
  }
}
