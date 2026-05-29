CREATE TABLE IF NOT EXISTS student_learning_profiles (
  student_id TEXT PRIMARY KEY,
  grade INTEGER NOT NULL,
  preferred_language TEXT NOT NULL DEFAULT 'ar-MA',
  focus_minutes INTEGER NOT NULL DEFAULT 12,
  confidence_score NUMERIC(5,2) NOT NULL DEFAULT 50,
  frustration_score NUMERIC(5,2) NOT NULL DEFAULT 0,
  curiosity_score NUMERIC(5,2) NOT NULL DEFAULT 50,
  last_active_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS learning_skills (
  skill_id TEXT PRIMARY KEY,
  grade INTEGER NOT NULL,
  subject TEXT NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  difficulty INTEGER NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS learning_skill_prerequisites (
  skill_id TEXT NOT NULL REFERENCES learning_skills(skill_id) ON DELETE CASCADE,
  prerequisite_skill_id TEXT NOT NULL REFERENCES learning_skills(skill_id) ON DELETE CASCADE,
  PRIMARY KEY (skill_id, prerequisite_skill_id)
);

CREATE TABLE IF NOT EXISTS student_skill_mastery (
  student_id TEXT NOT NULL,
  skill_id TEXT NOT NULL REFERENCES learning_skills(skill_id) ON DELETE CASCADE,
  mastery_score NUMERIC(5,2) NOT NULL DEFAULT 0,
  attempts INTEGER NOT NULL DEFAULT 0,
  correct_attempts INTEGER NOT NULL DEFAULT 0,
  last_practiced_at TIMESTAMPTZ,
  next_review_at TIMESTAMPTZ,
  confidence NUMERIC(5,2) NOT NULL DEFAULT 50,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  PRIMARY KEY (student_id, skill_id)
);

CREATE TABLE IF NOT EXISTS learning_events (
  event_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  lesson_id TEXT,
  skill_id TEXT,
  event_type TEXT NOT NULL,
  correct BOOLEAN,
  duration_seconds INTEGER,
  emotion TEXT,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS daily_learning_habits (
  student_id TEXT NOT NULL,
  learning_date DATE NOT NULL,
  minutes_learned INTEGER NOT NULL DEFAULT 0,
  lessons_completed INTEGER NOT NULL DEFAULT 0,
  streak_day INTEGER NOT NULL DEFAULT 0,
  reward_points INTEGER NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  PRIMARY KEY (student_id, learning_date)
);

CREATE TABLE IF NOT EXISTS parent_weekly_insights (
  insight_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  week_start DATE NOT NULL,
  summary TEXT NOT NULL,
  strengths JSONB NOT NULL DEFAULT '[]'::jsonb,
  weaknesses JSONB NOT NULL DEFAULT '[]'::jsonb,
  recommended_actions JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS student_skill_mastery_review_idx
  ON student_skill_mastery(student_id, next_review_at);

CREATE INDEX IF NOT EXISTS learning_events_student_created_idx
  ON learning_events(student_id, created_at DESC);
