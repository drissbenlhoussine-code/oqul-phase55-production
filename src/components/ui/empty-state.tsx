import { ReactNode } from "react";

type EmptyStateProps = {
  title: string;
  description?: string;
  icon?: ReactNode;
  action?: ReactNode;
};

export function EmptyState({ title, description, icon, action }: EmptyStateProps) {
  return (
    <section className="rounded-3xl border border-dashed border-slate-300 bg-white/70 p-8 text-center shadow-sm backdrop-blur dark:border-slate-700 dark:bg-slate-900/60">
      {icon ? <div className="mb-4 flex justify-center">{icon}</div> : null}
      <h3 className="text-xl font-bold text-slate-900 dark:text-white">{title}</h3>
      {description ? (
        <p className="mx-auto mt-2 max-w-md text-sm leading-7 text-slate-600 dark:text-slate-300">
          {description}
        </p>
      ) : null}
      {action ? <div className="mt-5">{action}</div> : null}
    </section>
  );
}
