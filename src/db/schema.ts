import { relations, sql } from "drizzle-orm";
import { boolean, index, integer, jsonb, pgEnum, pgTable, text, timestamp, uniqueIndex, uuid, varchar, real, decimal } from "drizzle-orm/pg-core";

// ─── Enums ───────────────────────────────────────────────────────────────────
export const userRoleEnum         = pgEnum("user_role", ["user", "admin"]);
export const planEnum             = pgEnum("plan", ["free", "basic", "advanced", "family", "school"]);
export const subscriptionStatus   = pgEnum("subscription_status", ["trialing", "active", "past_due", "cancelled", "expired"]);
export const cycleEnum            = pgEnum("cycle", ["primary", "middle", "high"]);
export const difficultyEnum       = pgEnum("difficulty", ["easy", "medium", "hard"]);
export const lessonProgressStatus = pgEnum("lesson_progress_status", ["not_started", "in_progress", "completed", "needs_review"]);
export const exerciseTypeEnum     = pgEnum("exercise_type", ["mcq", "true_false", "fill_blank", "short_answer"]);
export const messageRoleEnum      = pgEnum("message_role", ["system", "user", "assistant"]);
export const quotaFeatureEnum     = pgEnum("quota_feature", ["leila_text", "leila_voice", "quiz", "lesson"]);

// ─── Users ───────────────────────────────────────────────────────────────────
export const users = pgTable("users", {
  id:           uuid("id").primaryKey().defaultRandom(),
  fullName:     varchar("full_name", { length: 160 }).notNull(),
  email:        varchar("email", { length: 255 }).notNull(),
  passwordHash: text("password_hash").notNull(),
  role:         userRoleEnum("role").notNull().default("user"),
  plan:         planEnum("plan").notNull().default("free"),
  locale:       varchar("locale", { length: 16 }).notNull().default("ar-MA"),
  trialEndsAt:  timestamp("trial_ends_at", { withTimezone: true }),
  

  // Launch safety — email verification & password reset
  emailVerified: boolean("email_verified").notNull().default(false),
  emailVerificationToken: text("email_verification_token"),
  emailVerificationSentAt: timestamp("email_verification_sent_at", { withTimezone: true }),
  passwordResetToken: text("password_reset_token"),
  passwordResetExpiresAt: timestamp("password_reset_expires_at", { withTimezone: true }),
  termsAcceptedAt: timestamp("terms_accepted_at", { withTimezone: true }),
createdAt:    timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
  updatedAt:    timestamp("updated_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  emailUnique: uniqueIndex("users_email_unique").on(t.email),
}));

// ─── Children ────────────────────────────────────────────────────────────────
export const children = pgTable("children", {
  id:        uuid("id").primaryKey().defaultRandom(),
  userId:    uuid("user_id").notNull().references(() => users.id, { onDelete: "cascade" }),
  name:      varchar("name", { length: 120 }).notNull(),
  gradeId:   uuid("grade_id").references(() => grades.id),
  avatarUrl: varchar("avatar_url", { length: 500 }),
  xp:        integer("xp").notNull().default(0),
  streak:    integer("streak").notNull().default(0),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  userIdx: index("children_user_idx").on(t.userId),
}));

// ─── Curriculum ───────────────────────────────────────────────────────────────
export const cycles = pgTable("cycles", {
  id:          uuid("id").primaryKey().defaultRandom(),
  slug:        cycleEnum("slug").notNull(),
  titleAr:     varchar("title_ar", { length: 120 }).notNull(),
  titleFr:     varchar("title_fr", { length: 120 }),
  orderIndex:  integer("order_index").notNull().default(0),
  isActive:    boolean("is_active").notNull().default(true),
}, (t) => ({
  slugUnique: uniqueIndex("cycles_slug_unique").on(t.slug),
}));

export const grades = pgTable("grades", {
  id:         uuid("id").primaryKey().defaultRandom(),
  cycleId:    uuid("cycle_id").notNull().references(() => cycles.id, { onDelete: "cascade" }),
  slug:       varchar("slug", { length: 80 }).notNull(),
  titleAr:    varchar("title_ar", { length: 140 }).notNull(),
  titleFr:    varchar("title_fr", { length: 140 }),
  orderIndex: integer("order_index").notNull().default(0),
  ageMin:     integer("age_min"),
  ageMax:     integer("age_max"),
  color:      varchar("color", { length: 32 }).default("#059669"),
  isActive:   boolean("is_active").notNull().default(true),
}, (t) => ({
  slugUnique: uniqueIndex("grades_slug_unique").on(t.slug),
  cycleIdx:   index("grades_cycle_idx").on(t.cycleId),
}));

export const subjects = pgTable("subjects", {
  id:         uuid("id").primaryKey().defaultRandom(),
  gradeId:    uuid("grade_id").notNull().references(() => grades.id, { onDelete: "cascade" }),
  slug:       varchar("slug", { length: 100 }).notNull(),
  titleAr:    varchar("title_ar", { length: 160 }).notNull(),
  titleFr:    varchar("title_fr", { length: 160 }),
  icon:       varchar("icon", { length: 64 }).default("BookOpen"),
  color:      varchar("color", { length: 32 }).default("#7C3AED"),
  orderIndex: integer("order_index").notNull().default(0),
  isActive:   boolean("is_active").notNull().default(true),
}, (t) => ({
  gradeSlugUnique: uniqueIndex("subjects_grade_slug_unique").on(t.gradeId, t.slug),
  gradeIdx:        index("subjects_grade_idx").on(t.gradeId),
}));

export const units = pgTable("units", {
  id:          uuid("id").primaryKey().defaultRandom(),
  subjectId:   uuid("subject_id").notNull().references(() => subjects.id, { onDelete: "cascade" }),
  slug:        varchar("slug", { length: 120 }).notNull(),
  titleAr:     varchar("title_ar", { length: 180 }).notNull(),
  orderIndex:  integer("order_index").notNull().default(0),
  isPublished: boolean("is_published").notNull().default(true),
}, (t) => ({
  subjectSlugUnique: uniqueIndex("units_subject_slug_unique").on(t.subjectId, t.slug),
  subjectIdx:        index("units_subject_idx").on(t.subjectId),
}));

export const lessons = pgTable("lessons", {
  id:                        uuid("id").primaryKey().defaultRandom(),
  unitId:                    uuid("unit_id").notNull().references(() => units.id, { onDelete: "cascade" }),
  slug:                      varchar("slug", { length: 140 }).notNull(),
  titleAr:                   varchar("title_ar", { length: 220 }).notNull(),
  objectives:                jsonb("objectives").$type<string[]>().notNull().default(sql`'[]'::jsonb`),
  estimatedDurationMinutes:  integer("estimated_duration_minutes").notNull().default(20),
  difficulty:                difficultyEnum("difficulty").notNull().default("easy"),
  orderIndex:                integer("order_index").notNull().default(0),
  isPublished:               boolean("is_published").notNull().default(true),
}, (t) => ({
  unitSlugUnique: uniqueIndex("lessons_unit_slug_unique").on(t.unitId, t.slug),
  unitIdx:        index("lessons_unit_idx").on(t.unitId),
}));

export const lessonContents = pgTable("lesson_contents", {
  id:          uuid("id").primaryKey().defaultRandom(),
  lessonId:    uuid("lesson_id").notNull().references(() => lessons.id, { onDelete: "cascade" }).unique(),
  explanation: text("explanation").notNull(),
  vocabulary:  jsonb("vocabulary").$type<{ word: string; definition: string }[]>().default(sql`'[]'::jsonb`),
  examples:    jsonb("examples").$type<{ text: string; note?: string }[]>().default(sql`'[]'::jsonb`),
  summary:     text("summary"),
});

export const exercises = pgTable("exercises", {
  id:            uuid("id").primaryKey().defaultRandom(),
  lessonId:      uuid("lesson_id").notNull().references(() => lessons.id, { onDelete: "cascade" }),
  type:          exerciseTypeEnum("type").notNull(),
  question:      text("question").notNull(),
  options:       jsonb("options").$type<string[]>(),
  correctAnswer: text("correct_answer").notNull(),
  explanation:   text("explanation"),
  orderIndex:    integer("order_index").notNull().default(0),
  points:        integer("points").notNull().default(10),
}, (t) => ({
  lessonIdx: index("exercises_lesson_idx").on(t.lessonId),
}));

// ─── Progress ────────────────────────────────────────────────────────────────
export const lessonProgress = pgTable("lesson_progress", {
  id:             uuid("id").primaryKey().defaultRandom(),
  childId:        uuid("child_id").notNull().references(() => children.id, { onDelete: "cascade" }),
  lessonId:       uuid("lesson_id").notNull().references(() => lessons.id, { onDelete: "cascade" }),
  status:         lessonProgressStatus("status").notNull().default("not_started"),
  score:          real("score"),
  timeSpentSecs:  integer("time_spent_secs").notNull().default(0),
  completedAt:    timestamp("completed_at", { withTimezone: true }),
  updatedAt:      timestamp("updated_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  childLessonUnique: uniqueIndex("lesson_progress_child_lesson_unique").on(t.childId, t.lessonId),
  childIdx:          index("lesson_progress_child_idx").on(t.childId),
}));

export const quizAttempts = pgTable("quiz_attempts", {
  id:          uuid("id").primaryKey().defaultRandom(),
  childId:     uuid("child_id").notNull().references(() => children.id, { onDelete: "cascade" }),
  lessonId:    uuid("lesson_id").notNull().references(() => lessons.id, { onDelete: "cascade" }),
  score:       real("score").notNull(),
  totalPoints: integer("total_points").notNull(),
  earnedPoints: integer("earned_points").notNull(),
  answers:     jsonb("answers").$type<Record<string, string>>().notNull().default(sql`'{}'::jsonb`),
  completedAt: timestamp("completed_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  childIdx:  index("quiz_attempts_child_idx").on(t.childId),
  lessonIdx: index("quiz_attempts_lesson_idx").on(t.lessonId),
}));

export const weakPoints = pgTable("weak_points", {
  id:         uuid("id").primaryKey().defaultRandom(),
  childId:    uuid("child_id").notNull().references(() => children.id, { onDelete: "cascade" }),
  subjectId:  uuid("subject_id").notNull().references(() => subjects.id, { onDelete: "cascade" }),
  topic:      varchar("topic", { length: 200 }).notNull(),
  severity:   integer("severity").notNull().default(1),
  updatedAt:  timestamp("updated_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  childIdx: index("weak_points_child_idx").on(t.childId),
}));

// ─── AI Chat ─────────────────────────────────────────────────────────────────
export const chatSessions = pgTable("chat_sessions", {
  id:        uuid("id").primaryKey().defaultRandom(),
  childId:   uuid("child_id").notNull().references(() => children.id, { onDelete: "cascade" }),
  lessonId:  uuid("lesson_id").references(() => lessons.id),
  title:     varchar("title", { length: 200 }),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
  updatedAt: timestamp("updated_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  childIdx: index("chat_sessions_child_idx").on(t.childId),
}));

export const chatMessages = pgTable("chat_messages", {
  id:        uuid("id").primaryKey().defaultRandom(),
  sessionId: uuid("session_id").notNull().references(() => chatSessions.id, { onDelete: "cascade" }),
  role:      messageRoleEnum("role").notNull(),
  content:   text("content").notNull(),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  sessionIdx: index("chat_messages_session_idx").on(t.sessionId),
}));

// ─── Usage & Quota ────────────────────────────────────────────────────────────
export const aiUsageEvents = pgTable("ai_usage_events", {
  id:        uuid("id").primaryKey().defaultRandom(),
  userId:    uuid("user_id").notNull().references(() => users.id, { onDelete: "cascade" }),
  feature:   quotaFeatureEnum("feature").notNull(),
  tokens:    integer("tokens").notNull().default(0),
  provider:  varchar("provider", { length: 64 }).notNull().default("groq"),
  model:     varchar("model", { length: 100 }),
  success:   boolean("success").notNull().default(true),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  userIdx:  index("ai_usage_user_idx").on(t.userId),
  dateIdx:  index("ai_usage_date_idx").on(t.createdAt),
}));

// ─── Relations ────────────────────────────────────────────────────────────────
export const usersRelations = relations(users, ({ many }) => ({
  children: many(children),
  aiUsage:  many(aiUsageEvents),
}));

export const childrenRelations = relations(children, ({ one, many }) => ({
  user:          one(users, { fields: [children.userId], references: [users.id] }),
  grade:         one(grades, { fields: [children.gradeId], references: [grades.id] }),
  progress:      many(lessonProgress),
  quizAttempts:  many(quizAttempts),
  weakPoints:    many(weakPoints),
  chatSessions:  many(chatSessions),
}));

export const cyclesRelations    = relations(cycles,   ({ many }) => ({ grades:   many(grades)   }));
export const gradesRelations    = relations(grades,   ({ one, many }) => ({ cycle: one(cycles, { fields: [grades.cycleId], references: [cycles.id] }), subjects: many(subjects), children: many(children) }));
export const subjectsRelations  = relations(subjects, ({ one, many }) => ({ grade: one(grades, { fields: [subjects.gradeId], references: [grades.id] }), units: many(units), weakPoints: many(weakPoints) }));
export const unitsRelations     = relations(units,    ({ one, many }) => ({ subject: one(subjects, { fields: [units.subjectId], references: [subjects.id] }), lessons: many(lessons) }));
export const lessonsRelations   = relations(lessons,  ({ one, many }) => ({
  unit: one(units, { fields: [lessons.unitId], references: [units.id] }),
  content: one(lessonContents, { fields: [lessons.id], references: [lessonContents.lessonId] }),
  exercises: many(exercises),
  progress: many(lessonProgress),
  quizAttempts: many(quizAttempts),
  chatSessions: many(chatSessions),
}));
export const lessonContentsRelations = relations(lessonContents, ({ one }) => ({ lesson: one(lessons, { fields: [lessonContents.lessonId], references: [lessons.id] }) }));
export const exercisesRelations = relations(exercises, ({ one }) => ({ lesson: one(lessons, { fields: [exercises.lessonId], references: [lessons.id] }) }));
export const lessonProgressRelations = relations(lessonProgress, ({ one }) => ({
  child: one(children, { fields: [lessonProgress.childId], references: [children.id] }),
  lesson: one(lessons, { fields: [lessonProgress.lessonId], references: [lessons.id] }),
}));
export const quizAttemptsRelations = relations(quizAttempts, ({ one }) => ({
  child: one(children, { fields: [quizAttempts.childId], references: [children.id] }),
  lesson: one(lessons, { fields: [quizAttempts.lessonId], references: [lessons.id] }),
}));
export const aiUsageEventsRelations = relations(aiUsageEvents, ({ one }) => ({
  user: one(users, { fields: [aiUsageEvents.userId], references: [users.id] }),
}));

export const weakPointsRelations = relations(weakPoints, ({ one }) => ({
  child: one(children, { fields: [weakPoints.childId], references: [children.id] }),
  subject: one(subjects, { fields: [weakPoints.subjectId], references: [subjects.id] }),
}));
export const chatSessionsRelations = relations(chatSessions, ({ one, many }) => ({ child: one(children, { fields: [chatSessions.childId], references: [children.id] }), lesson: one(lessons, { fields: [chatSessions.lessonId], references: [lessons.id] }), messages: many(chatMessages) }));
export const chatMessagesRelations = relations(chatMessages, ({ one }) => ({ session: one(chatSessions, { fields: [chatMessages.sessionId], references: [chatSessions.id] }) }));

// ─── Gamification ─────────────────────────────────────────────────────────────
export const badges = pgTable("badges", {
  id:          uuid("id").primaryKey().defaultRandom(),
  slug:        varchar("slug", { length: 80 }).notNull().unique(),
  titleAr:     varchar("title_ar", { length: 120 }).notNull(),
  description: varchar("description", { length: 300 }),
  icon:        varchar("icon", { length: 10 }).notNull().default("🏅"),
  xpReward:    integer("xp_reward").notNull().default(50),
  condition:   varchar("condition", { length: 200 }),
});

export const childBadges = pgTable("child_badges", {
  id:         uuid("id").primaryKey().defaultRandom(),
  childId:    uuid("child_id").notNull().references(() => children.id, { onDelete: "cascade" }),
  badgeId:    uuid("badge_id").notNull().references(() => badges.id, { onDelete: "cascade" }),
  earnedAt:   timestamp("earned_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  childBadgeUnique: uniqueIndex("child_badge_unique").on(t.childId, t.badgeId),
  childIdx:         index("child_badges_child_idx").on(t.childId),
}));

export const badgesRelations    = relations(badges,      ({ many }) => ({ childBadges: many(childBadges) }));
export const childBadgesRelations = relations(childBadges, ({ one }) => ({
  child: one(children, { fields: [childBadges.childId], references: [children.id] }),
  badge: one(badges,   { fields: [childBadges.badgeId], references: [badges.id] }),
}));

// ─── Streak events (for daily tracking) ──────────────────────────────────────
export const streakEvents = pgTable("streak_events", {
  id:        uuid("id").primaryKey().defaultRandom(),
  childId:   uuid("child_id").notNull().references(() => children.id, { onDelete: "cascade" }),
  date:      varchar("date", { length: 10 }).notNull(), // YYYY-MM-DD
  xpEarned:  integer("xp_earned").notNull().default(0),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  childDateUnique: uniqueIndex("streak_events_child_date_unique").on(t.childId, t.date),
  childIdx:        index("streak_events_child_idx").on(t.childId),
}));

export const streakEventsRelations = relations(streakEvents, ({ one }) => ({
  child: one(children, { fields: [streakEvents.childId], references: [children.id] }),
}));

// ─── Auth Sessions & Refresh Token Rotation ───────────────────────────────────
export const authSessions = pgTable("auth_sessions", {
  id:           uuid("id").primaryKey().defaultRandom(),
  userId:       uuid("user_id").notNull().references(() => users.id, { onDelete: "cascade" }),
  // Refresh token family — all tokens in a rotation chain share this ID
  // Detecting a reuse of a revoked token from the same family = token theft
  familyId:     uuid("family_id").notNull().defaultRandom(),
  // Hash of the current valid refresh token (SHA-256)
  tokenHash:    varchar("token_hash", { length: 64 }).notNull(),
  // Tracks which device/browser this session belongs to
  userAgent:    varchar("user_agent", { length: 512 }),
  ipAddress:    varchar("ip_address", { length: 64 }),
  // Rotation tracking
  rotationCount: integer("rotation_count").notNull().default(0),
  isRevoked:    boolean("is_revoked").notNull().default(false),
  expiresAt:    timestamp("expires_at", { withTimezone: true }).notNull(),
  createdAt:    timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
  lastUsedAt:   timestamp("last_used_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  userIdx:      index("auth_sessions_user_idx").on(t.userId),
  familyIdx:    index("auth_sessions_family_idx").on(t.familyId),
  tokenHashIdx: index("auth_sessions_token_hash_idx").on(t.tokenHash),
}));

export const authSessionsRelations = relations(authSessions, ({ one }) => ({
  user: one(users, { fields: [authSessions.userId], references: [users.id] }),
}));

// ─── Phase 27: Living Learner Intelligence ─────────────────────────────────

export const studentLearningProfiles = pgTable("student_learning_profiles", {
  studentId:         varchar("student_id").primaryKey(),
  grade:             integer("grade").notNull(),
  preferredLanguage: varchar("preferred_language", { length: 20 }).notNull().default("ar-MA"),
  focusMinutes:      integer("focus_minutes").notNull().default(12),
  confidenceScore:   decimal("confidence_score", { precision: 5, scale: 2 }).notNull().default("50"),
  frustrationScore:  decimal("frustration_score", { precision: 5, scale: 2 }).notNull().default("0"),
  curiosityScore:    decimal("curiosity_score", { precision: 5, scale: 2 }).notNull().default("50"),
  lastActiveAt:      timestamp("last_active_at", { withTimezone: true }),
  createdAt:         timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
  updatedAt:         timestamp("updated_at", { withTimezone: true }).defaultNow().notNull(),
});

export const learnerMemorySnapshots = pgTable("learner_memory_snapshots", {
  snapshotId:      varchar("snapshot_id").primaryKey(),
  studentId:       varchar("student_id").notNull(),
  memoryType:      varchar("memory_type").notNull(),
  summary:         text("summary").notNull(),
  signals:         jsonb("signals").notNull().default({}),
  confidenceScore: decimal("confidence_score", { precision: 5, scale: 2 }).notNull().default("50"),
  createdAt:       timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
}, (t) => ({
  studentCreatedIdx: index("learner_memory_student_created_idx").on(t.studentId, t.createdAt),
}));

export const learnerEmotionalTrends = pgTable("learner_emotional_trends", {
  trendId:   varchar("trend_id").primaryKey(),
  studentId: varchar("student_id").notNull(),
  emotion:   varchar("emotion").notNull(),
  intensity: decimal("intensity", { precision: 5, scale: 2 }).notNull().default("0"),
  source:    varchar("source").notNull().default("learning-session"),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
});

export const leilaRelationshipEvents = pgTable("leila_relationship_events", {
  eventId:   varchar("event_id").primaryKey(),
  studentId: varchar("student_id").notNull(),
  eventType: varchar("event_type").notNull(),
  message:   text("message").notNull(),
  tone:      varchar("tone").notNull().default("warm"),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
});
