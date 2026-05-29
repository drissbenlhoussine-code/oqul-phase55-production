/**
 * Landing Page (/) — Phase 34 Fix
 * Path: src/app/page.tsx
 *
 * Fix: Navbar and Footer were completely absent from the landing page.
 * Users had no way to navigate to /login or /register from the homepage.
 *
 * All section components (Hero, Features, etc.) unchanged.
 */
import { Navbar }         from "@/components/layout/navbar";
import { Footer }         from "@/components/layout/footer";
import { Hero }           from "@/components/landing/hero";
import { Features }       from "@/components/landing/features";
import { HowItWorks }     from "@/components/landing/how-it-works";
import { Testimonials }   from "@/components/landing/testimonials";
import { PricingSection } from "@/components/landing/pricing";
import { CTA }            from "@/components/landing/cta";

export default function LandingPage() {
  return (
    <>
      <Navbar />
      <main>
        <Hero />
        <Features />
        <HowItWorks />
        <Testimonials />
        <PricingSection />
        <CTA />
      </main>
      <Footer />
    </>
  );
}
