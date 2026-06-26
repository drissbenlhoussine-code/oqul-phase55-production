PRODUCT NAME: [REPLACE THIS WITH YOUR PRODUCT NAME]

You are a senior product designer and Python developer. Write a complete, runnable Python PIL image generation script that produces 10 premium Etsy listing images for [PRODUCT NAME].

If the script is long, continue automatically without stopping until every image function is complete and the main execution block is written.

---

DESIGN STANDARD — MANDATORY:
Reference quality: Apple, Stripe, Linear, Notion, Framer, Arc Browser, Raycast
The customer must immediately think: "This looks like a €100–€200 product."

Background: Deep dark gradient (near-black #06080E to deep navy #0F1630)
Accent palette: Teal (0,200,182) · Amber (251,191,36) · Cyan (14,165,233) · White (255,255,255)
Muted text: Slate (148,163,184) · Dim slate (100,116,139)
Cards: Dark navy panel (18,27,58) with 1px white 11% opacity border
Device frame: Space Gray (44,46,52)
Texture: Dot grid overlay, 80px spacing, 10% opacity white dots

COMPOSITION PRINCIPLES — APPLY TO EVERY IMAGE:
- Rule of thirds: place the dominant subject at a grid intersection, not dead center (except Image 10 CTA)
- Negative space: at least 20% of the canvas must be intentionally empty to create breathing room
- Depth: minimum 3 layers — background glow · mid-ground device · foreground cards or text
- Eye tracking: design so the eye moves Device → Headline → Key Metric → CTA or Key Stat
- Contrast: the single most important element must be visually dominant — at least 40% brighter than surrounding elements
- Visual weight: left side anchors the device; right side anchors the message — or reverse intentionally

---

DEVICE MOCKUP REQUIREMENTS:
Draw all devices with PIL polygons and rectangles — no image imports.

MacBook Pro: Lid (rounded rect, Space Gray) · Bezel (darker inner frame) · Screen area · Notch (top center) · Camera dot · Hinge line · Keyboard base with key rows · Trackpad groove · Screen glow (radial cyan blur behind device) · Top-edge highlight: 2px lighter-gray line to simulate studio overhead lighting.

iPad Pro (landscape): Frame (rounded rect) · Thin bezel · Screen area · Camera dot (right edge center) · Home indicator bar (bottom center)

iPhone: Frame (heavily rounded rect) · Dynamic Island (pill, top center) · Screen area (rounded) · Side buttons (power right, volume left) · Home indicator bar

All devices: Cast a soft directional shadow angled 15° from vertical. Glow radius must be proportional to screen size (minimum: screen_height ÷ 2).

---

UI INSIDE MOCKUPS — MANDATORY:
Every screen must look like real SaaS software. Include:
Dark sidebar with icon nav · Top bar with title and avatar · KPI cards with top accent lines and real metrics · Bar or area chart with labeled axes · Table or booking list with real data rows · Status badges · Sheet tabs (for spreadsheet images)
All data inside the UI must be specific to [PRODUCT NAME]. Zero generic placeholders. Zero "Sample Data". Zero "John Doe."

---

ABSOLUTE VISUAL RULES:
- No flat screenshots
- No Canva-style layouts
- No presentation-slide appearance (text block on a colored rectangle = rejected)
- No empty interfaces
- No placeholder blocks
- No lorem ipsum in any UI element
- No symmetrical center-aligned layouts unless intentionally balanced (Image 10 only)
- Every image communicates one idea in under 3 seconds
- Composition: 60% product mockup · 25% headline/messaging · 15% supporting details
- Maximum per image: 1 headline · 1 subtitle · 5 feature items
- Every device must have a soft radial glow emitting from the screen
- Every card must have a drop shadow (GaussianBlur, offset 14–18px, 60–70% opacity)
- Visual flow must be intentional: eye enters at brightest element, exits at CTA or key stat

---

IMAGE SEQUENCE — BUILD ALL 10:

**01 — Hero (Attention)**
MacBook Pro positioned left of center (rule-of-thirds left anchor). Radial teal glow behind screen. Top-right: headline "[PRODUCT NAME] System" in Roboto Black 108px, teal accent on last word. Right side: 3 floating stat cards with key result metrics (specific to [PRODUCT NAME]). Bottom bar: 4 product highlights in slate text. Eye path: laptop → headline → stat cards.

**02 — Problem Solved**
No device. Full-width two-column layout. Left card (dark crimson tint): "WITHOUT THIS" header · 7 pain points in red with ✗. Right card (dark navy): "WITH [PRODUCT NAME]" header in teal · 7 solutions in white with ✓. Bold headline above. Visual weight must lean right — the solution side is brighter and heavier than the problem side.

**03 — Everything Included**
No device. 3×3 grid of dark glass cards. Each card: emoji icon + bold asset title + one-line description + teal left accent bar. Cards staggered in shadow depth (far = lighter shadow, near = heavier) to create subtle 3D grid. Headline: "Everything Included." Subtitle: exact asset count + "One Complete System."

**04 — Dashboard**
Large MacBook (centered, wider than Image 01, sw=1700). Core spreadsheet or workspace of [PRODUCT NAME]. Sheet tabs at bottom. KPI cards at top with real metric names. Prominent bar chart. Headline top-left: "Your entire operation, on one dashboard." Badge bottom-right: sheet count + "formula-driven." Device fills the frame — this is a product-dominance image.

**05 — Workflow**
iPhone positioned slightly right of center. Left: headline + 3 benefit lines anchored left. Right: 3 floating stat cards. Real workflow content inside phone (message thread, checklist, or process view) specific to [PRODUCT NAME]. Eye path: left headline → phone screen → right stats.

**06 — Templates**
MacBook left-center. Right side: vertical list of 10 template names with teal ✓ checkmarks. Headline top-right: exact template count + "Done-for-You Templates." Subtitle: "Copy. Paste. Personalize. Done." Strong negative space above and below the device.

**07 — Customer Experience**
iPad Pro landscape. Floating glass card bottom-left: 5 gold stars + real review quote (specific to [PRODUCT NAME] buyer type) + "Verified Buyer." Headline top-right with strong contrast. Eye path: iPad content → review card → headline.

**08 — Results**
Area chart with glow fill (left panel, 55% width, inside dark card). Upward trend, 8 labeled data points, last value highlighted in amber. Right 45%: 4 stat cards stacked with key outcome metrics specific to [PRODUCT NAME]. Headline: "The numbers don't lie." The chart must visually dominate — credibility image, not marketing image.

**09 — Who It's For**
3 audience profile cards equal width, full height. Each: colored top strip + emoji + audience title Black 48px + one-sentence description + divider + 4 audience-specific bullet points + bottom outcome quote. Headline centered above all 3. Cards cast different shadow depths for 3D depth feel.

**10 — Purchase Confidence (CTA)**
Left panel: value stack — every asset listed with individual €price · strikethrough total retail value · today's price bold and prominent. Right: large price card ("TODAY ONLY" amber label · price in Roboto Black 130px · "One-time payment" · "Lifetime access"). Full-width teal CTA button: "Get Instant Access →" in Roboto Black 36px. Below: 4 trust badge cards. This image must feel like a premium landing page, not a slide. Intentionally center-balanced.

---

VISUAL QA — RUN AFTER ALL 10 IMAGE FUNCTIONS ARE WRITTEN:
Before outputting SCRIPT COMPLETE, verify:
[ ] No image has its dominant subject dead center (except Image 10)
[ ] Negative space ≥ 20% on every canvas
[ ] Every device has a visible proportional screen glow
[ ] All UI content is product-specific — zero generic placeholders
[ ] No image resembles a presentation slide or Canva template
[ ] Visual flow is intentional in every image
[ ] Drop shadows present on all floating cards
[ ] Every image passes the 3-second test: one idea, immediately clear

Fix any failure before outputting SCRIPT COMPLETE.

---

TECHNICAL REQUIREMENTS:
- Output path: ./output/etsy-images-v2/
- Dimensions: 2700 × 1800 px per image
- Format: JPEG, quality=96
- Fonts: Roboto family from /usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/ (Black, Bold, Medium, Regular, Light)
- All d.text() calls must use fill= and font= as explicit keyword arguments
- Drop shadows: GaussianBlur on RGBA layer, alpha_composite to merge
- Glow effects: concentric ellipses on RGBA layer, GaussianBlur, alpha_composite
- Glass cards: RGBA layer with white at 20–25 alpha, 1px white border at 55 alpha
- No radius list arguments in rounded_rectangle — use single integer radius only
- Script must run without errors from python3 [script_name].py
- Include all helper functions, all 10 image functions, and the main execution block

Output: **SCRIPT COMPLETE** on the final line.
