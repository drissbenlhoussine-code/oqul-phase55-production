type ProgressRingProps = {
  value: number;
  label: string;
};

export function ProgressRing({ value, label }: ProgressRingProps) {
  const safe = Math.max(0, Math.min(100, value));
  return (
    <div className="rounded-[2rem] bg-gradient-to-br from-brand-600 to-indigo-700 p-6 text-white shadow-glow">
      <div className="mx-auto grid h-32 w-32 place-items-center rounded-full border-[10px] border-white/20">
        <span className="text-3xl font-black">{safe}%</span>
      </div>
      <p className="mt-5 text-center text-lg font-bold">{label}</p>
    </div>
  );
}
