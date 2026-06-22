from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = "/usr/share/fonts/truetype/liberation"
W, H = 2700, 2025
OUT = "/home/user/oqul-phase55-production/airbnb-host-kit/4_ETSY_IMAGES"

DARK   = "#0A1929"
MAIN   = "#1B4F72"
ACCENT = "#2E86C1"
LIGHT  = "#AED6F1"
CREAM  = "#EAF4FB"
GOLD   = "#F0B429"
RED    = "#E74C3C"

def fnt(n, s):
    f = {"sb":"LiberationSerif-Bold.ttf","sr":"LiberationSerif-Regular.ttf",
         "ab":"LiberationSans-Bold.ttf","ar":"LiberationSans-Regular.ttf"}
    return ImageFont.truetype(os.path.join(FONT_DIR, f[n]), s)

def rgb(h):
    if isinstance(h, tuple): return h
    h = h.lstrip("#")
    return tuple(int(h[i:i+2],16) for i in (0,2,4))

def bar(img, y, h, col):
    c = rgb(col)
    ImageDraw.Draw(img).rectangle([(0,y),(W,y+h)], fill=c)

def cx(draw, text, y, f, col, w=W, ox=0):
    c = rgb(col)
    bb = draw.textbbox((0,0), text, font=f)
    x = ox + (w-(bb[2]-bb[0]))//2
    draw.text((x,y), text, font=f, fill=c)

def lx(draw, text, x, y, f, col):
    c = rgb(col)
    draw.text((x,y), text, font=f, fill=c)

def text_h(draw, text, f):
    bb = draw.textbbox((0,0), text, font=f)
    return bb[3] - bb[1]

def text_w(draw, text, f):
    bb = draw.textbbox((0,0), text, font=f)
    return bb[2] - bb[0]

os.makedirs(OUT, exist_ok=True)

# ── 01_hero.jpg ──────────────────────────────────────────────────
img = Image.new("RGB", (W, H), rgb(DARK))
d = ImageDraw.Draw(img)

# Subtle horizontal lines every 80px
for y in range(0, H, 80):
    d.line([(0, y), (W, y)], fill=rgb("#0D2137"), width=1)

# Border bars
d.rectangle([(0,0),(W,12)], fill=rgb(MAIN))
d.rectangle([(0,H-12),(W,H)], fill=rgb(MAIN))
d.rectangle([(0,0),(12,H)], fill=rgb(MAIN))
d.rectangle([(W-12,0),(W,H)], fill=rgb(MAIN))

# Title
f_title = fnt("sb", 130)
cx(d, "AIRBNB HOST KIT", 320, f_title, GOLD)

# Subtitle
f_sub = fnt("ar", 72)
cx(d, "The Complete Hosting Business System", 490, f_sub, CREAM)

# Divider line
d.rectangle([(300, 610), (W-300, 616)], fill=rgb(MAIN))

# Tagline
f_tag = fnt("ar", 54)
cx(d, "10 Professional Templates  •  Instant Digital Download", 640, f_tag, LIGHT)

# 6 template boxes
labels = ["Guest Scripts", "House Rules", "Review System", "Pricing Guide", "Caption Bank", "Host Systems"]
box_w, box_h = 380, 90
total_w = 6 * box_w + 5 * 20
start_x = (W - total_w) // 2
box_y = 800
f_box = fnt("ab", 38)
for i, label in enumerate(labels):
    bx = start_x + i * (box_w + 20)
    d.rectangle([(bx, box_y), (bx+box_w, box_y+box_h)], fill=rgb(MAIN))
    lw = text_w(d, label, f_box)
    lh = text_h(d, label, f_box)
    d.text((bx + (box_w-lw)//2, box_y + (box_h-lh)//2), label, font=f_box, fill=rgb(CREAM))

img.save(os.path.join(OUT, "01_hero.jpg"), "JPEG", quality=95)
print("01_hero.jpg done")

# ── 02_whats_inside.jpg ──────────────────────────────────────────
img = Image.new("RGB", (W, H), rgb(DARK))
d = ImageDraw.Draw(img)

# Header bar
d.rectangle([(0,0),(W,180)], fill=rgb(MAIN))
f_hdr = fnt("ab", 90)
cx(d, "WHAT'S INSIDE", 30, f_hdr, CREAM)

templates = [
    "365 Airbnb & Hosting Captions",
    "Guest Message Scripts & Templates",
    "House Rules & Welcome Guide Templates",
    "Check-In & Check-Out Instructions",
    "Review Request & Response System",
    "Listing Description Templates",
    "Social Media Ad Copy (10 ads)",
    "Hashtag Bank (200 hashtags)",
    "30-Day Content Calendar",
    "Airbnb Host Business Systems Guide",
]

f_num = fnt("ab", 44)
f_item = fnt("ar", 44)

col_x = [120, 1400]
start_y = 240
row_h = 160

for i, tmpl in enumerate(templates):
    col = i % 2
    row = i // 2
    x = col_x[col]
    y = start_y + row * row_h

    # Gold number badge
    badge_size = 70
    d.rectangle([(x, y+5), (x+badge_size, y+5+badge_size)], fill=rgb(GOLD))
    num_str = str(i+1)
    nw = text_w(d, num_str, f_num)
    nh = text_h(d, num_str, f_num)
    d.text((x+(badge_size-nw)//2, y+5+(badge_size-nh)//2), num_str, font=f_num, fill=rgb(DARK))

    d.text((x+badge_size+20, y+10), tmpl, font=f_item, fill=rgb(CREAM))

# Bottom gold bar
d.rectangle([(0, H-90),(W, H)], fill=rgb(GOLD))
f_bot = fnt("ab", 48)
cx(d, "Instant Download  •  Open in Google Docs or Notion  •  Start Using Today", H-78, f_bot, DARK)

img.save(os.path.join(OUT, "02_whats_inside.jpg"), "JPEG", quality=95)
print("02_whats_inside.jpg done")

# ── 03_content_preview.jpg ───────────────────────────────────────
img = Image.new("RGB", (W, H), rgb(DARK))
d = ImageDraw.Draw(img)

f_t = fnt("sb", 110)
cx(d, "365 CAPTIONS INCLUDED", 40, f_t, GOLD)
f_s = fnt("ar", 60)
cx(d, "A full year of Airbnb & hosting content", 175, f_s, CREAM)

captions = [
    "Five stars starts before they arrive. Every detail\nin this listing was chosen with your stay in mind.",
    "Checked the keypad, restocked the essentials,\nand left a handwritten note. This is a business.",
    "The best review I ever received said:\n'It felt like someone actually thought about us.'",
    "Your booking is confirmed. Here's what to expect:\nseamless check-in, a spotless space, everything ready.",
    "Running an Airbnb means running a business.\nThese are the systems that keep mine at Superhost level.",
    "Poll: what matters most as a guest?\nLocation | Cleanliness | Communication | Comfort",
]

card_w, card_h = 820, 340
gap = 40
cols = 3
total_card_w = cols * card_w + (cols-1) * gap
sx = (W - total_card_w) // 2
sy = 310
f_cap = fnt("ar", 36)

for i, cap in enumerate(captions):
    col = i % cols
    row = i // cols
    cx_ = sx + col * (card_w + gap)
    cy_ = sy + row * (card_h + gap)

    # Card background
    d.rectangle([(cx_, cy_), (cx_+card_w, cy_+card_h)], fill=rgb(MAIN))
    d.rectangle([(cx_, cy_), (cx_+card_w, cy_+card_h)], outline=rgb(ACCENT), width=3)

    # Text inside card
    lines = cap.split("\n")
    ty = cy_ + 30
    for line in lines:
        lw = text_w(d, line, f_cap)
        tx = cx_ + (card_w - lw) // 2
        d.text((tx, ty), line, font=f_cap, fill=rgb(CREAM))
        ty += text_h(d, line, f_cap) + 12

img.save(os.path.join(OUT, "03_content_preview.jpg"), "JPEG", quality=95)
print("03_content_preview.jpg done")

# ── 04_system_feature.jpg ────────────────────────────────────────
img = Image.new("RGB", (W, H), rgb(DARK))
d = ImageDraw.Draw(img)

f_t = fnt("sb", 100)
cx(d, "COMPLETE GUEST COMMUNICATION SYSTEM", 60, f_t, GOLD)
f_s = fnt("ar", 56)
cx(d, "Every message, from booking to review — done for you", 195, f_s, CREAM)

steps = ["BOOKING\nCONFIRMED", "PRE-ARRIVAL\nMESSAGE", "CHECK-IN\nINSTRUCTIONS", "MID-STAY\nCHECK-IN", "REVIEW\nREQUEST"]
step_w, step_h = 430, 180
arrow_w = 60
total = len(steps) * step_w + (len(steps)-1) * arrow_w
sx = (W - total) // 2
sy = 380

f_step = fnt("ab", 42)
for i, step in enumerate(steps):
    bx = sx + i * (step_w + arrow_w)
    d.rectangle([(bx, sy), (bx+step_w, sy+step_h)], fill=rgb(MAIN))
    lines = step.split("\n")
    ty = sy + (step_h - len(lines)*(text_h(d, lines[0], f_step)+8)) // 2
    for line in lines:
        lw = text_w(d, line, f_step)
        d.text((bx+(step_w-lw)//2, ty), line, font=f_step, fill=rgb(CREAM))
        ty += text_h(d, line, f_step) + 8

    if i < len(steps)-1:
        ax = bx + step_w
        ay = sy + step_h // 2
        d.line([(ax, ay), (ax+arrow_w-10, ay)], fill=rgb(GOLD), width=6)
        # Arrow head
        d.polygon([(ax+arrow_w-10, ay-15), (ax+arrow_w, ay), (ax+arrow_w-10, ay+15)], fill=rgb(GOLD))

# 3 feature highlights
features = ["50+ Message\nTemplates", "Review Response\nScripts", "Superhost-Level\nSystem"]
feat_w = 700
feat_sx = (W - 3*feat_w - 2*80) // 2
feat_y = 660
f_feat = fnt("ab", 52)
for i, feat in enumerate(features):
    fx = feat_sx + i * (feat_w + 80)
    d.rectangle([(fx, feat_y), (fx+feat_w, feat_y+160)], fill=rgb(ACCENT))
    lines = feat.split("\n")
    ty = feat_y + (160 - len(lines)*(text_h(d, lines[0], f_feat)+8))//2
    for line in lines:
        lw = text_w(d, line, f_feat)
        d.text((fx+(feat_w-lw)//2, ty), line, font=f_feat, fill=rgb(CREAM))
        ty += text_h(d, line, f_feat) + 8

img.save(os.path.join(OUT, "04_system_feature.jpg"), "JPEG", quality=95)
print("04_system_feature.jpg done")

# ── 05_value_anchor.jpg ──────────────────────────────────────────
img = Image.new("RGB", (W, H), rgb(DARK))
d = ImageDraw.Draw(img)

# Right half lighter
d.rectangle([(W//2, 0), (W, H)], fill=rgb(MAIN))

# Gold center divider
d.rectangle([(W//2-4, 0), (W//2+4, H-120)], fill=rgb(GOLD))

f_hdr = fnt("ab", 72)
f_item = fnt("ar", 48)

# LEFT: WITHOUT
cx(d, "WITHOUT THIS KIT", 60, f_hdr, RED, w=W//2)
struggles = [
    "Rewriting guest messages every booking",
    "Inconsistent check-in instructions",
    "No system for getting 5-star reviews",
    "Generic listing description",
    "Starting from scratch every time",
]
ty = 200
for s in struggles:
    d.text((80, ty), "X", font=fnt("ab", 56), fill=rgb(RED))
    d.text((160, ty+4), s, font=f_item, fill=rgb(CREAM))
    ty += 120

# RIGHT: WITH
cx(d, "WITH THIS KIT", 60, f_hdr, GOLD, w=W//2, ox=W//2)
solutions = [
    "50+ done-for-you guest message templates",
    "Professional check-in & house rules guides",
    "Proven review request system",
    "Listing description framework",
    "Complete hosting business system",
]
ty = 200
for s in solutions:
    d.text((W//2+60, ty), "✓", font=fnt("ab", 56), fill=rgb(GOLD))
    d.text((W//2+140, ty+4), s, font=f_item, fill=rgb(CREAM))
    ty += 120

# Bottom bar
d.rectangle([(0, H-120), (W, H)], fill=rgb(DARK))
f_bot = fnt("ab", 80)
cx(d, "10 Templates  •  $19  •  Instant Download", H-112, f_bot, GOLD)

img.save(os.path.join(OUT, "05_value_anchor.jpg"), "JPEG", quality=95)
print("05_value_anchor.jpg done")

# ── 06_before_after.jpg ──────────────────────────────────────────
img = Image.new("RGB", (W, H), rgb(DARK))
d = ImageDraw.Draw(img)

# Top banner
d.rectangle([(0,0),(W,140)], fill=rgb(MAIN))
f_banner = fnt("ab", 90)
cx(d, "THE DIFFERENCE SYSTEMS MAKE", 18, f_banner, CREAM)

panel_w = W//2 - 40
panel_x = [30, W//2+10]
panel_y = 160
panel_h = H - 280

# LEFT panel
d.rectangle([(panel_x[0], panel_y), (panel_x[0]+panel_w, panel_y+panel_h)], fill=rgb("#0D2137"))
d.rectangle([(panel_x[0], panel_y), (panel_x[0]+panel_w, panel_y+16)], fill=rgb(RED))

f_label = fnt("ab", 72)
d.text((panel_x[0]+40, panel_y+40), "BEFORE", font=f_label, fill=rgb(RED))

before_lines = [
    "Hosting on vibes and hoping",
    "for good reviews.",
    "",
    "Rewriting every message.",
    "No consistent process.",
    "",
    "Wondering why 5-star hosts",
    "seem to have it all figured out.",
]
f_txt = fnt("ar", 50)
ty = panel_y + 150
for line in before_lines:
    if line:
        d.text((panel_x[0]+40, ty), line, font=f_txt, fill=rgb(CREAM))
    ty += 72

# RIGHT panel
d.rectangle([(panel_x[1], panel_y), (panel_x[1]+panel_w, panel_y+panel_h)], fill=rgb(MAIN))
d.rectangle([(panel_x[1], panel_y), (panel_x[1]+panel_w, panel_y+16)], fill=rgb(GOLD))

d.text((panel_x[1]+40, panel_y+40), "AFTER", font=f_label, fill=rgb(GOLD))

after_lines = [
    "Every guest touchpoint",
    "is handled.",
    "",
    "Professional messages",
    "sent in seconds.",
    "",
    "Superhost-level systems —",
    "without the guesswork.",
]
ty = panel_y + 150
for line in after_lines:
    if line:
        d.text((panel_x[1]+40, ty), line, font=f_txt, fill=rgb(CREAM))
    ty += 72

# Bottom
d.rectangle([(0, H-120),(W,H)], fill=rgb(DARK))
f_bot = fnt("ar", 60)
cx(d, "Get there today. Instant download.", H-100, f_bot, CREAM)

img.save(os.path.join(OUT, "06_before_after.jpg"), "JPEG", quality=95)
print("06_before_after.jpg done")

# ── 07_mockup.jpg ────────────────────────────────────────────────
img = Image.new("RGB", (W, H), rgb(DARK))
d = ImageDraw.Draw(img)

# Subtle grid pattern
for y in range(0, H, 60):
    d.line([(0,y),(W,y)], fill=rgb("#0D1F2E"), width=1)
for x in range(0, W, 60):
    d.line([(x,0),(x,H)], fill=rgb("#0D1F2E"), width=1)

# Laptop base/keyboard
base_x1, base_y1 = 600, 1400
base_x2, base_y2 = 2100, 1680
d.rectangle([(base_x1, base_y1), (base_x2, base_y2)], fill=rgb("#1A1A2A"))
# Keyboard row suggestion
for row in range(3):
    for col in range(12):
        kx = base_x1 + 80 + col*115
        ky = base_y1 + 30 + row*75
        d.rectangle([(kx,ky),(kx+100,ky+60)], fill=rgb("#222235"), outline=rgb("#2A2A45"), width=1)

# Laptop screen area
scr_x1, scr_y1 = 550, 360
scr_x2, scr_y2 = 2150, 1380
d.rectangle([(scr_x1-10, scr_y1-10), (scr_x2+10, scr_y2+10)], fill=rgb("#0D0D1A"))
d.rectangle([(scr_x1-10, scr_y1-10), (scr_x2+10, scr_y2+10)], outline=rgb(MAIN), width=6)

# Screen content area (lighter dark)
d.rectangle([(scr_x1, scr_y1), (scr_x2, scr_y2)], fill=rgb("#0F1B2A"))

# Google Docs-like header bar on screen
d.rectangle([(scr_x1, scr_y1), (scr_x2, scr_y1+60)], fill=rgb("#1E3A5A"))
# Dots
for i, c in enumerate(["#E74C3C","#F0B429","#2ECC71"]):
    d.ellipse([(scr_x1+20+i*40, scr_y1+18),(scr_x1+46+i*40, scr_y1+44)], fill=rgb(c))

# Document content on screen
doc_x = scr_x1 + 80
doc_y = scr_y1 + 100

f_doc_title = fnt("ab", 52)
d.text((doc_x, doc_y), "Guest Welcome Message", font=f_doc_title, fill=rgb(GOLD))
doc_y += 80

d.line([(doc_x, doc_y),(scr_x2-80, doc_y)], fill=rgb(ACCENT), width=2)
doc_y += 20

f_doc_line = fnt("ar", 38)
doc_lines = [
    "Hi [Guest Name], welcome to [Property Name]!",
    "We're so excited to host you. Here's everything you need",
    "to know for a smooth and enjoyable stay:",
    "",
    "CHECK-IN: The door code is [CODE]. You can check in",
    "anytime after 3 PM. The lockbox is located [LOCATION].",
    "",
    "WIFI: Network: [NETWORK NAME] | Password: [PASSWORD]",
    "",
    "Feel free to message me anytime if you need anything.",
    "Enjoy your stay!",
]
for line in doc_lines:
    if line:
        # Vary line colors for visual interest
        col = CREAM if not line.startswith(("CHECK", "WIFI")) else LIGHT
        d.text((doc_x, doc_y), line, font=f_doc_line, fill=rgb(col))
    doc_y += 58

# Below laptop text
f_sub = fnt("ar", 54)
cx(d, "Opens instantly in Google Docs, Notion, or Word", 1720, f_sub, CREAM)

f_wm = fnt("ab", 44)
cx(d, "AIRBNB HOST KIT", 1820, f_wm, MAIN)

img.save(os.path.join(OUT, "07_mockup.jpg"), "JPEG", quality=95)
print("07_mockup.jpg done")

print("DONE")
