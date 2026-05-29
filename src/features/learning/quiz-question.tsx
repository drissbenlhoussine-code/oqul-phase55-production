"use client";

import { useState } from "react";
import { CheckCircle, XCircle } from "lucide-react";
import { cn } from "@/lib/cn";

interface QuizQuestionProps {
  index:         number;
  exercise: {
    id:            string;
    type:          string;
    question:      string;
    options?:      string[];
    correctAnswer: string;
    explanation?:  string | null;
    points:        number;
  };
  submitted:     boolean;
  value:         string;
  onChange:      (val: string) => void;
}

export function QuizQuestion({ index, exercise, submitted, value, onChange }: QuizQuestionProps) {
  const [localAns, setLocalAns] = useState(value);

  const isCorrect = submitted && localAns.trim().toLowerCase() === exercise.correctAnswer.trim().toLowerCase();
  const isWrong   = submitted && localAns && !isCorrect;

  function pick(opt: string) {
    if (submitted) return;
    setLocalAns(opt);
    onChange(opt);
  }

  return (
    <div className={cn(
      "rounded-2xl border-2 p-5 space-y-4 transition-all duration-300",
      submitted && isCorrect ? "border-emerald-300 bg-emerald-50" :
      submitted && isWrong   ? "border-red-200 bg-red-50" :
      localAns               ? "border-primary/30 bg-card" :
                               "border-border bg-card"
    )}>
      {/* Question header */}
      <div className="flex items-start gap-3">
        <span className={cn(
          "w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0 mt-0.5 transition-colors",
          submitted && isCorrect ? "bg-emerald-500 text-white" :
          submitted && isWrong   ? "bg-red-400 text-white" :
                                   "bg-primary text-white"
        )}>
          {submitted ? (isCorrect ? "✓" : "✗") : index + 1}
        </span>
        <div className="flex-1">
          <p className="font-medium text-sm leading-relaxed">{exercise.question}</p>
          <span className="text-xs text-muted-foreground">{exercise.points} نقطة</span>
        </div>
      </div>

      {/* MCQ / True-False options */}
      {(exercise.type === "mcq" || exercise.type === "true_false") && exercise.options && (
        <div className="grid gap-2 pr-11">
          {exercise.options.map((opt) => {
            const isSelected  = localAns === opt;
            const isThisRight = submitted && opt === exercise.correctAnswer;
            const isThisWrong = submitted && isSelected && opt !== exercise.correctAnswer;

            return (
              <button
                key={opt}
                onClick={() => pick(opt)}
                disabled={submitted}
                className={cn(
                  "p-3 rounded-xl text-sm text-right font-medium transition-all border-2",
                  isThisRight  ? "bg-emerald-100 border-emerald-400 text-emerald-800" :
                  isThisWrong  ? "bg-red-100 border-red-400 text-red-800" :
                  isSelected   ? "bg-primary/10 border-primary text-primary" :
                                 "bg-secondary border-transparent hover:border-border disabled:cursor-default"
                )}
              >
                <span className="flex items-center justify-between gap-2">
                  {opt}
                  {isThisRight && <CheckCircle className="w-4 h-4 text-emerald-600 flex-shrink-0" />}
                  {isThisWrong && <XCircle className="w-4 h-4 text-red-500 flex-shrink-0" />}
                </span>
              </button>
            );
          })}
        </div>
      )}

      {/* Fill blank */}
      {exercise.type === "fill_blank" && (
        <div className="pr-11">
          <input
            disabled={submitted}
            value={localAns}
            onChange={(e) => { setLocalAns(e.target.value); onChange(e.target.value); }}
            placeholder="اكتب إجابتك هنا..."
            className={cn(
              "w-full p-3 rounded-xl border-2 bg-background text-sm focus:outline-none transition-colors",
              submitted && isCorrect ? "border-emerald-400 bg-emerald-50" :
              submitted && isWrong   ? "border-red-400 bg-red-50" :
                                       "border-border focus:border-primary"
            )}
          />
        </div>
      )}

      {/* Post-submit explanation */}
      {submitted && (
        <div className={cn(
          "pr-11 text-sm rounded-xl p-3 border",
          isCorrect
            ? "bg-emerald-100 border-emerald-200 text-emerald-800"
            : "bg-amber-50 border-amber-200 text-amber-800"
        )}>
          {isCorrect ? (
            <p className="font-medium">✅ ممتاز! {exercise.explanation ?? "إجابة صحيحة"}</p>
          ) : (
            <div className="space-y-1">
              <p className="font-semibold">الجواب الصح: <span className="text-emerald-700">{exercise.correctAnswer}</span></p>
              {exercise.explanation && <p className="text-xs opacity-80">{exercise.explanation}</p>}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
