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

---

DEVICE MOCKUP REQUIREMENTS:
Draw all devices with PIL polygons and rectangles — no image imports.

MacBook Pro: Lid (rounded rect, Space Gray) · Bezel (darker inner frame) · Screen area · Notch (top center) · Camera dot · Hinge line · Keyboard base with key rows · Trackpad groove · Screen glow (radial cyan blur behind device)

iPad Pro (landscape): Frame (rounded rect) · Thin bezel · Screen area · Camera dot (right edge center) · Home indicator bar (bottom center)

iPhone: Frame (heavily rounded rect) · Dynamic Island (pill, top center) · Screen area (rounded) · Side buttons (power right, volume left) · Home indicator bar

---

UI INSIDE MOCKUPS — MANDATORY:
Every screen must look like real SaaS software. Include:
Dark sidebar with icon nav · Top bar with title and avatar · KPI cards with top accent lines and metrics · Bar or area chart with labeled axes · Table or booking list with real data rows · Status badges (colored dots) · Sheet tabs (for spreadsheet images)

---

ABSOLUTE VISUAL RULES:
- No flat screenshots
- No Canva-style layouts
- No empty interfaces
- No placeholder blocks
- No lorem ipsum in any UI element
- Every image communicates one idea in under 5 seconds
- Composition: 60% product mockup · 25% headline/messaging · 15% supporting details
- Maximum per image: 1 headline · 1 subtitle · 5 feature items
- Every device must have a soft radial glow emitting from the screen
- Every card must have a drop shadow (GaussianBlur, offset 14–18px, 60–70% opacity)

---

IMAGE SEQUENCE — BUILD ALL 10:

**01 — Hero (Attention)**
MacBook Pro (center-left) showing the main dashboard of [PRODUCT NAME]. Radial teal glow behind screen. Top-right: bold headline "[PRODUCT NAME] System" in Roboto Black 108px, teal accent on last word. Right side: 3 floating stat cards with key result metrics (specific to [PRODUCT NAME]). Bottom bar: 4 product highlights in slate text.

**02 — Problem Solved**
No device. Full-width two-column layout. Left card (dark crimson tint): "WITHOUT THIS" header, 7 pain points in red text with ✗ marks. Right card (dark navy): "WITH [PRODUCT NAME]" header in teal, 7 solutions in white with ✓ marks. Bold headline above: "Stop Guessing. Start [relevant verb for product type]."

**03 — Everything Included**
No device. 3×3 grid of dark glass cards. Each card: emoji icon + bold asset title + one-line description + teal left accent bar. Cards slightly staggered in depth via shadow intensity. Headline: "Everything Included." Subtitle: exact count of assets + "One Complete System."

**04 — Dashboard**
Large MacBook (centered, wider than image 01, sw=1700). Show the spreadsheet or workspace dashboard of [PRODUCT NAME]. Sheet tabs visible at bottom. KPI cards at top with real metric names for [PRODUCT NAME]. Prominent bar chart. Headline top-left: "Your entire operation, on one dashboard." Badge bottom-right: number of sheets/pages + "formula-driven."

**05 — Workflow**
iPhone (center) showing a key workflow from [PRODUCT NAME]: message thread, checklist, or process view. Real content in the phone UI, specific to [PRODUCT NAME]. Left side: headline "One system. Zero chaos." + 3 benefit lines. Right side: 3 floating stat cards.

**06 — Templates**
MacBook (left-center) showing the main template document of [PRODUCT NAME]. Right side: vertical list of 10 template names with teal ✓ checkmarks. Headline top-right: exact count + "Done-for-You Templates." Subtitle: "Copy. Paste. Personalize. Done."

**07 — Customer Experience**
iPad Pro landscape showing the client-facing or user-facing asset of [PRODUCT NAME] (manual, portal, guide). Floating glass card bottom-left: 5 gold stars + real review quote relevant to [PRODUCT NAME] type + "Verified Buyer." Headline: "Deliver a premium experience every time."

**08 — Results**
Area chart with glow fill (left panel, inside dark card). Chart shows upward trend with 8 data points, months labeled, last point value highlighted in amber. Right: 4 stat cards with key outcome metrics specific to [PRODUCT NAME] (rating, revenue, efficiency, time saved). Headline: "The numbers don't lie."

**09 — Who It's For**
3 audience profile cards (full height, side by side). Each: colored top strip + emoji + audience title in Black 48px + one-sentence description + divider line + 4 bullet points specific to that audience segment. Bottom of each card: a short quote or outcome statement. Headline: "Built for ambitious professionals."

**10 — Purchase Confidence (CTA)**
Left panel: dark card listing every asset with individual €price values. Strikethrough total. Bottom: "Today:" + bold price. Right: large price card with "TODAY ONLY" amber label + big price in Roboto Black 130px + "One-time payment" + "Lifetime access." Below: full-width teal CTA button "Get Instant Access →" in Roboto Black 36px. Below button: 4 trust badge cards (Instant Download · Lifetime Access · No Subscription · [product-specific badge]).

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
- Script must run without errors from python3 airbnb_images_v2.py
- Include all helper functions, all 10 image functions, and the main execution block

Output: **SCRIPT COMPLETE** on the final line.
