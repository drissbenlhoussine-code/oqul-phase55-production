import { ReactNode } from "react";

type StatCardProps = {
  icon: ReactNode;
  label: string;
  value: string | number;
  helper?: string;
};

export function StatCard({ icon, label, value, helper }: StatCardProps) {
  return (
    <div className="rounded-[2rem] border border-white/70 bg-white/90 p-5 shadow-soft backdrop-blur">
      <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-2xl bg-brand-100 text-brand-700">
        {icon}
      </div>
      <p className="text-sm text-slate-500">{label}</p>
      <strong className="mt-1 block text-3xl font-black text-slate-950">{value}</strong>
      {helper && <p className="mt-2 text-xs text-slate-400">{helper}</p>}
    </div>
  );
}
