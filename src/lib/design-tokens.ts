export const designTokens = {
  colors: {
    brand: {
      blue: "#3157F5",
      indigo: "#151B69",
      amber: "#F8A20D",
      orange: "#FF7A3D",
      mint: "#23D3B6",
      sand: "#FFF7E8"
    },
    semantic: {
      success: "#16A34A",
      warning: "#F59E0B",
      danger: "#EF4444",
      info: "#2563EB"
    }
  },
  spacing: {
    pageX: "clamp(1rem, 4vw, 2rem)",
    sectionY: "clamp(4rem, 8vw, 7rem)",
    cardPadding: "clamp(1rem, 3vw, 1.75rem)"
  },
  radius: {
    sm: "0.75rem",
    md: "1rem",
    lg: "1.5rem",
    xl: "2rem"
  },
  typography: {
    fontArabic: "var(--font-cairo)",
    h1: "clamp(2.5rem, 7vw, 5rem)",
    h2: "clamp(2rem, 5vw, 3.5rem)",
    body: "clamp(1rem, 2vw, 1.125rem)"
  },
  shadows: {
    soft: "0 20px 60px rgba(15, 23, 42, 0.10)",
    glow: "0 24px 80px rgba(49, 87, 245, 0.22)",
    amberGlow: "0 24px 80px rgba(248, 162, 13, 0.22)"
  }
} as const;

export type DesignTokens = typeof designTokens;
