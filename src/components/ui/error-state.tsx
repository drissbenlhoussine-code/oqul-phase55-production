type ErrorStateProps = {
  title?: string;
  description?: string;
  onRetry?: () => void;
};

export function ErrorState({
  title = "وقع خطأ غير متوقع",
  description = "حاول مرة أخرى أو ارجع لاحقًا.",
  onRetry,
}: ErrorStateProps) {
  return (
    <section className="rounded-3xl border border-red-200 bg-red-50 p-6 text-center text-red-900 dark:border-red-900/40 dark:bg-red-950/30 dark:text-red-100">
      <h3 className="text-lg font-bold">{title}</h3>
      <p className="mt-2 text-sm leading-7 opacity-80">{description}</p>
      {onRetry ? (
        <button
          onClick={onRetry}
          className="mt-4 rounded-full bg-red-600 px-5 py-2 text-sm font-semibold text-white"
        >
          إعادة المحاولة
        </button>
      ) : null}
    </section>
  );
}
