CREATE TABLE IF NOT EXISTS leila_emotional_memory (
  memory_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL UNIQUE,
  preferred_examples JSONB NOT NULL DEFAULT '[]'::jsonb,
  motivation_style TEXT NOT NULL DEFAULT 'encouragement',
  frustration_triggers JSONB NOT NULL DEFAULT '[]'::jsonb,
  learning_notes JSONB NOT NULL DEFAULT '[]'::jsonb,
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS daily_learning_challenges (
  challenge_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  challenge_date DATE NOT NULL DEFAULT CURRENT_DATE,
  skill_id TEXT,
  subject TEXT NOT NULL,
  prompt TEXT NOT NULL,
  difficulty TEXT NOT NULL DEFAULT 'easy',
  estimated_minutes INTEGER NOT NULL DEFAULT 5,
  reward_points INTEGER NOT NULL DEFAULT 10,
  completed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(student_id, challenge_date)
);

CREATE TABLE IF NOT EXISTS leila_session_notes (
  note_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  lesson_id TEXT,
  note TEXT NOT NULL,
  tone TEXT NOT NULL DEFAULT 'warm',
  parent_visible BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS parent_learning_journal_entries (
  entry_id TEXT PRIMARY KEY,
  student_id TEXT NOT NULL,
  journal_date DATE NOT NULL DEFAULT CURRENT_DATE,
  learned_today JSONB NOT NULL DEFAULT '[]'::jsonb,
  struggled_with JSONB NOT NULL DEFAULT '[]'::jsonb,
  leila_suggestion TEXT NOT NULL,
  emotional_state TEXT NOT NULL DEFAULT 'stable',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
