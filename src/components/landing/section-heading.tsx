import { cn } from "@/lib/cn";

interface SectionHeadingProps {
  eyebrow: string;
  title: string;
  description: string;
  className?: string;
}

export function SectionHeading({ eyebrow, title, description, className }: SectionHeadingProps) {
  return (
    <div className={cn("mx-auto max-w-3xl text-center", className)}>
      <span className="inline-flex rounded-full bg-primary/10 px-5 py-2 text-sm font-extrabold text-primary">
        {eyebrow}
      </span>
      <h2 className="mt-5 text-4xl font-black leading-tight tracking-tight text-foreground md:text-6xl">
        {title}
      </h2>
      <p className="mt-5 text-lg leading-9 text-muted-foreground md:text-xl">{description}</p>
    </div>
  );
}
