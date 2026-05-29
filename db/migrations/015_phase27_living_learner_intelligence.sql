CREATE TABLE IF NOT EXISTS learner_memory_snapshots (
  snapshot_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  memory_type TEXT NOT NULL,
  summary TEXT NOT NULL,
  signals JSONB NOT NULL DEFAULT '{}'::jsonb,
  confidence_score NUMERIC(5,2) NOT NULL DEFAULT 50,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS learner_emotional_trends (
  trend_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  emotion TEXT NOT NULL,
  intensity NUMERIC(5,2) NOT NULL DEFAULT 0,
  source TEXT NOT NULL DEFAULT 'learning-session',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS cognitive_pacing_recommendations (
  recommendation_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  skill_id TEXT,
  recommended_pace TEXT NOT NULL,
  reason TEXT NOT NULL,
  max_session_minutes INTEGER NOT NULL DEFAULT 12,
  challenge_level TEXT NOT NULL DEFAULT 'normal',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS learning_recovery_paths (
  path_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  target_skill_id TEXT NOT NULL,
  prerequisite_skill_ids JSONB NOT NULL DEFAULT '[]'::jsonb,
  recovery_steps JSONB NOT NULL DEFAULT '[]'::jsonb,
  status TEXT NOT NULL DEFAULT 'active',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  completed_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS leila_relationship_events (
  event_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  event_type TEXT NOT NULL,
  message TEXT NOT NULL,
  tone TEXT NOT NULL DEFAULT 'warm',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS learner_memory_student_created_idx
  ON learner_memory_snapshots(student_id, created_at DESC);

CREATE INDEX IF NOT EXISTS learner_emotional_trends_student_created_idx
  ON learner_emotional_trends(student_id, created_at DESC);

CREATE INDEX IF NOT EXISTS learning_recovery_paths_student_status_idx
  ON learning_recovery_paths(student_id, status);
