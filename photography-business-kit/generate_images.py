from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = "/usr/share/fonts/truetype/liberation"
W, H = 2700, 2025
OUT_DIR = "/home/user/oqul-phase55-production/photography-business-kit/4_ETSY_IMAGES"

# Colors
DARK   = "#1C1008"
MAIN   = "#3D2314"
ACCENT = "#7B4A2D"
LIGHT  = "#D4A574"
CREAM  = "#FDF6EC"
GOLD   = "#C8941A"

def fnt(n, s):
    f = {"sb":"LiberationSerif-Bold.ttf","sr":"LiberationSerif-Regular.ttf",
         "ab":"LiberationSans-Bold.ttf","ar":"LiberationSans-Regular.ttf"}
    return ImageFont.truetype(os.path.join(FONT_DIR, f[n]), s)

def rgb(h):
    if isinstance(h, tuple): return h
    h = h.lstrip("#")
    return tuple(int(h[i:i+2],16) for i in (0,2,4))

def cx(draw, text, y, f, col, w=W):
    c = rgb(col)
    bb = draw.textbbox((0,0), text, font=f)
    x = (w-(bb[2]-bb[0]))//2
    draw.text((x,y), text, font=f, fill=c)

def lx(draw, text, x, y, f, col):
    draw.text((x,y), text, font=f, fill=rgb(col))

def wrap_text(draw, text, font, max_width):
    """Wrap text to fit within max_width, returns list of lines."""
    words = text.split()
    lines = []
    current = []
    for word in words:
        test = ' '.join(current + [word])
        bb = draw.textbbox((0,0), test, font=font)
        if bb[2]-bb[0] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(' '.join(current))
            current = [word]
    if current:
        lines.append(' '.join(current))
    return lines

def draw_border(draw, thick=12, col=GOLD):
    c = rgb(col)
    draw.rectangle([0, 0, W-1, thick-1], fill=c)
    draw.rectangle([0, H-thick, W-1, H-1], fill=c)
    draw.rectangle([0, 0, thick-1, H-1], fill=c)
    draw.rectangle([W-thick, 0, W-1, H-1], fill=c)

def save(img, name):
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, name)
    img.save(path, "JPEG", quality=95)
    print(f"  Saved: {path}")

# ─────────────────────────────────────────────
# 01_hero.jpg
# ─────────────────────────────────────────────
def gen_01():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Subtle texture via gradient-like bands
    for i in range(0, H, 4):
        alpha = int(8 * (i / H))
        band_col = tuple(min(255, c+alpha) for c in rgb(DARK))
        d.rectangle([0, i, W, i+3], fill=band_col)

    draw_border(d)

    # Top ornamental line
    d.rectangle([80, 55, W-80, 57], fill=rgb(GOLD))

    # Main title
    f_title = fnt("sb", 110)
    cx(d, "PHOTOGRAPHY BUSINESS KIT", 130, f_title, GOLD)

    # Decorative divider
    d.rectangle([200, 270, W-200, 274], fill=rgb(GOLD))
    d.rectangle([200, 279, W-200, 280], fill=rgb(ACCENT))

    # Subtitle
    f_sub = fnt("sr", 64)
    cx(d, "The Complete Photography Business System", 310, f_sub, CREAM)

    # Secondary divider
    d.rectangle([300, 415, W-300, 418], fill=rgb(ACCENT))

    # Feature line
    f_feat = fnt("ar", 52)
    cx(d, "10 Professional Templates  •  Instant Digital Download", 455, f_feat, LIGHT)

    # Section label
    f_label = fnt("ab", 38)
    cx(d, "WHAT'S INCLUDED", 560, f_label, GOLD)

    # 6 Preview boxes
    box_labels = ["365 Captions", "Client Scripts", "Contracts",
                  "Pricing Guide", "Ad Copy", "Business Guide"]
    box_w = 370
    box_h = 230
    cols = 6
    total_w = cols * box_w + (cols-1) * 30
    start_x = (W - total_w) // 2
    box_y = 630

    for i, label in enumerate(box_labels):
        bx = start_x + i * (box_w + 30)
        # Box background
        d.rectangle([bx, box_y, bx+box_w, box_y+box_h], fill=rgb(MAIN))
        # Gold accent top bar
        d.rectangle([bx, box_y, bx+box_w, box_y+6], fill=rgb(GOLD))
        # Gold border
        d.rectangle([bx, box_y, bx+box_w, box_y+box_h], outline=rgb(GOLD), width=2)
        # Number
        f_num = fnt("sb", 42)
        num_str = f"0{i+1}"
        bb = d.textbbox((0,0), num_str, font=f_num)
        nx = bx + (box_w - (bb[2]-bb[0])) // 2
        d.text((nx, box_y+20), num_str, font=f_num, fill=rgb(GOLD))
        # Label — wrap if needed
        f_box = fnt("ab", 34)
        lines = wrap_text(d, label, f_box, box_w - 20)
        ly = box_y + 80
        for line in lines:
            bb2 = d.textbbox((0,0), line, font=f_box)
            lx2 = bx + (box_w - (bb2[2]-bb2[0])) // 2
            d.text((lx2, ly), line, font=f_box, fill=rgb(CREAM))
            ly += 45

    # Bottom ornamental area
    d.rectangle([80, 920, W-80, 924], fill=rgb(GOLD))

    # Bottom tagline
    f_tag = fnt("sr", 46)
    cx(d, "Built for photographers ready to run a real business.", 960, f_tag, LIGHT)

    f_small = fnt("ar", 36)
    cx(d, "Editable  •  Printable  •  Instantly Usable", 1040, f_small, ACCENT)

    # Bottom border line
    d.rectangle([80, H-80, W-80, H-77], fill=rgb(GOLD))

    save(img, "01_hero.jpg")

# ─────────────────────────────────────────────
# 02_whats_inside.jpg
# ─────────────────────────────────────────────
def gen_02():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Header bar
    d.rectangle([0, 0, W, 185], fill=rgb(MAIN))
    d.rectangle([0, 183, W, 188], fill=rgb(GOLD))
    f_hdr = fnt("ab", 90)
    cx(d, "WHAT'S INSIDE", 42, f_hdr, GOLD)

    # Subtitle
    f_sub = fnt("sr", 44)
    cx(d, "Photography Business Kit  —  10 Professional Templates", 210, f_sub, LIGHT)

    templates = [
        "365 Photography Captions",
        "Client Inquiry & Booking Scripts",
        "Photography Contract Language & Clauses",
        "Pricing Guide & Package Templates",
        "Session Prep & Client Education Guides",
        "Gallery Delivery & Follow-Up Scripts",
        "Social Media Ad Copy (10 Ads)",
        "Hashtag Bank (200 Hashtags)",
        "30-Day Content Calendar",
        "Photography Business Systems Guide",
    ]

    col_count = 2
    items_per_col = 5
    col_w = 1200
    start_y = 290
    row_h = 145
    pad_x = 80
    col_gap = 80

    col_starts = [pad_x, pad_x + col_w + col_gap]

    f_num = fnt("sb", 46)
    f_item = fnt("ar", 40)
    f_item_b = fnt("ab", 40)

    for i, tmpl in enumerate(templates):
        col = i // items_per_col
        row = i % items_per_col
        bx = col_starts[col]
        by = start_y + row * row_h

        # Badge background
        badge_r = 36
        d.ellipse([bx, by+4, bx+badge_r*2, by+4+badge_r*2], fill=rgb(GOLD))
        # Number
        num_str = str(i+1)
        bb = d.textbbox((0,0), num_str, font=f_num)
        nx = bx + badge_r - (bb[2]-bb[0])//2
        ny = by + 4 + badge_r - (bb[3]-bb[1])//2
        d.text((nx, ny), num_str, font=f_num, fill=rgb(DARK))

        # Card background
        card_x = bx + badge_r*2 + 18
        card_y = by - 4
        card_h = row_h - 14
        card_end_x = col_starts[col] + col_w - 10
        d.rectangle([card_x, card_y, card_end_x, card_y+card_h], fill=rgb(MAIN))
        d.rectangle([card_x, card_y, card_end_x, card_y+card_h], outline=rgb(ACCENT), width=1)

        # Template text
        max_w = card_end_x - card_x - 30
        lines = wrap_text(d, tmpl, f_item_b, max_w)
        ty = card_y + (card_h - len(lines)*46)//2
        for line in lines:
            d.text((card_x+18, ty), line, font=f_item_b, fill=rgb(CREAM))
            ty += 46

    # Divider
    d.rectangle([80, H-130, W-80, H-127], fill=rgb(GOLD))

    # Bottom bar
    d.rectangle([0, H-120, W, H], fill=rgb(GOLD))
    f_bot = fnt("ab", 52)
    cx(d, "Instant Download  •  Open in Google Docs  •  Start Today", H-95, f_bot, DARK)

    save(img, "02_whats_inside.jpg")

# ─────────────────────────────────────────────
# 03_content_preview.jpg
# ─────────────────────────────────────────────
def gen_03():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    draw_border(d, 10)

    # Header
    f_hdr = fnt("sb", 100)
    cx(d, "365 PHOTOGRAPHY CAPTIONS", 55, f_hdr, GOLD)

    # Subtitle
    f_sub = fnt("sr", 46)
    cx(d, "Ready-to-post captions for every shoot, every season, every vibe.", 195, f_sub, LIGHT)

    d.rectangle([150, 270, W-150, 274], fill=rgb(GOLD))

    captions = [
        ("01", "Golden hour did exactly what golden hour does.\nGallery delivery in 3 days."),
        ("02", "Behind the shot: the 20-minute wait for the light\nto hit right, the one frame that made it worth it."),
        ("03", "Your wedding day will fly by.\nThe photos are what slow it back down."),
        ("04", "New inquiry form is in the bio.\nBooking portrait sessions through October."),
        ("05", "When couples say 'we're not photogenic' —\nthat's not a person problem. That's a photographer problem."),
        ("06", "Poll: what matters most in a photographer?\nStyle | Personality | Price | Turnaround"),
    ]

    card_w = 1200
    card_h = 270
    gap_x = 60
    gap_y = 36
    start_x = (W - (2*card_w + gap_x)) // 2
    start_y = 310

    f_num = fnt("sb", 44)
    f_cap = fnt("sr", 36)
    f_label = fnt("ab", 28)

    for i, (num, caption) in enumerate(captions):
        col = i % 2
        row = i // 2
        cx2 = start_x + col*(card_w + gap_x)
        cy2 = start_y + row*(card_h + gap_y)

        # Card
        d.rectangle([cx2, cy2, cx2+card_w, cy2+card_h], fill=rgb(MAIN))
        d.rectangle([cx2, cy2, cx2+card_w, cy2+card_h], outline=rgb(ACCENT), width=2)
        # Gold left accent bar
        d.rectangle([cx2, cy2, cx2+8, cy2+card_h], fill=rgb(GOLD))
        # Number badge
        d.ellipse([cx2+20, cy2+16, cx2+80, cy2+76], fill=rgb(GOLD))
        bb = d.textbbox((0,0), num, font=f_num)
        nx = cx2+20 + (60-(bb[2]-bb[0]))//2
        ny = cy2+16 + (60-(bb[3]-bb[1]))//2
        d.text((nx, ny), num, font=f_num, fill=rgb(DARK))

        # Caption text
        lines = caption.split('\n')
        ty = cy2 + 22
        for line in lines:
            wrapped = wrap_text(d, line, f_cap, card_w - 110)
            for wl in wrapped:
                d.text((cx2+95, ty), wl, font=f_cap, fill=rgb(CREAM))
                ty += 46

    # Bottom
    d.rectangle([150, H-100, W-150, H-96], fill=rgb(GOLD))
    f_bot = fnt("ab", 40)
    cx(d, "+ 359 more captions included  •  All niches covered  •  Post with confidence", H-82, f_bot, LIGHT)

    save(img, "03_content_preview.jpg")

# ─────────────────────────────────────────────
# 04_system_feature.jpg
# ─────────────────────────────────────────────
def gen_04():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    draw_border(d, 10)

    # Title
    f_title = fnt("sb", 90)
    cx(d, "COMPLETE CLIENT BOOKING SYSTEM", 70, f_title, GOLD)

    f_sub = fnt("sr", 48)
    cx(d, "Every touchpoint. Every script. Every template — done for you.", 200, f_sub, LIGHT)

    d.rectangle([150, 285, W-150, 289], fill=rgb(GOLD))

    # Flow diagram
    flow_steps = ["INQUIRY", "QUOTE", "CONTRACT", "SESSION\nPREP", "GALLERY", "REVIEW"]
    step_w = 340
    step_h = 200
    step_gap = 50
    arrow_w = 40
    total = len(flow_steps) * step_w + (len(flow_steps)-1) * (step_gap + arrow_w)
    fx = (W - total) // 2
    fy = 330

    f_step = fnt("ab", 38)
    f_arrow = fnt("ab", 52)

    for i, step in enumerate(flow_steps):
        sx = fx + i * (step_w + step_gap + arrow_w)
        # Box
        d.rectangle([sx, fy, sx+step_w, fy+step_h], fill=rgb(MAIN))
        d.rectangle([sx, fy, sx+step_w, fy+step_h], outline=rgb(GOLD), width=3)
        d.rectangle([sx, fy, sx+step_w, fy+8], fill=rgb(GOLD))

        # Step number
        f_sn = fnt("sb", 34)
        sn = f"{i+1:02d}"
        d.text((sx+14, fy+16), sn, font=f_sn, fill=rgb(GOLD))

        # Step label
        lines = step.split('\n')
        total_h = len(lines) * 46
        ty = fy + (step_h - total_h) // 2 + 10
        for line in lines:
            bb = d.textbbox((0,0), line, font=f_step)
            lx2 = sx + (step_w - (bb[2]-bb[0])) // 2
            d.text((lx2, ty), line, font=f_step, fill=rgb(CREAM))
            ty += 48

        # Arrow between boxes
        if i < len(flow_steps) - 1:
            ax = sx + step_w + 8
            ay = fy + step_h//2 - 18
            d.text((ax, ay), "›", font=f_arrow, fill=rgb(GOLD))

    # Connection line below flow
    line_y = fy + step_h + 40
    d.rectangle([fx, line_y, fx+total, line_y+3], fill=rgb(ACCENT))

    # 3 highlight cards
    highlights = [
        ("INQUIRY\nSCRIPTS", "Word-for-word responses\nto new leads & inquiries"),
        ("CONTRACT\nTEMPLATES", "Professional language\nthat protects your business"),
        ("REVIEW\nSYSTEM", "Follow-up scripts that\nturn clients into referrals"),
    ]

    card_w2 = 740
    card_h2 = 310
    card_gap = 90
    hx = (W - (3*card_w2 + 2*card_gap)) // 2
    hy = line_y + 50

    f_hcard = fnt("ab", 42)
    f_hbody = fnt("ar", 36)

    for i, (title, body) in enumerate(highlights):
        cx3 = hx + i*(card_w2+card_gap)
        d.rectangle([cx3, hy, cx3+card_w2, hy+card_h2], fill=rgb(MAIN))
        d.rectangle([cx3, hy, cx3+card_w2, hy+card_h2], outline=rgb(GOLD), width=2)
        d.rectangle([cx3, hy, cx3+card_w2, hy+10], fill=rgb(GOLD))

        # Title
        t_lines = title.split('\n')
        ty = hy + 30
        for tl in t_lines:
            bb = d.textbbox((0,0), tl, font=f_hcard)
            tx = cx3 + (card_w2 - (bb[2]-bb[0])) // 2
            d.text((tx, ty), tl, font=f_hcard, fill=rgb(GOLD))
            ty += 48

        # Body
        b_lines = body.split('\n')
        ty2 = ty + 16
        for bl in b_lines:
            wrapped = wrap_text(d, bl, f_hbody, card_w2-40)
            for wl in wrapped:
                bb = d.textbbox((0,0), wl, font=f_hbody)
                lx2 = cx3 + (card_w2 - (bb[2]-bb[0])) // 2
                d.text((lx2, ty2), wl, font=f_hbody, fill=rgb(CREAM))
                ty2 += 44

    # Bottom
    d.rectangle([0, H-110, W, H], fill=rgb(MAIN))
    d.rectangle([0, H-112, W, H-109], fill=rgb(GOLD))
    f_bot = fnt("ab", 46)
    cx(d, "Scripts  •  Templates  •  Systems  •  All In One Kit", H-88, f_bot, GOLD)

    save(img, "04_system_feature.jpg")

# ─────────────────────────────────────────────
# 05_value_anchor.jpg
# ─────────────────────────────────────────────
def gen_05():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Left panel (WITHOUT)
    d.rectangle([0, 0, W//2, H], fill=rgb(MAIN))
    # Right panel (WITH)
    d.rectangle([W//2, 0, W, H], fill=rgb(DARK))
    # Center divider
    d.rectangle([W//2-3, 0, W//2+3, H], fill=rgb(GOLD))

    draw_border(d, 10)

    # WITHOUT header
    f_hdr = fnt("ab", 72)
    cx(d, "WITHOUT", 55, f_hdr, LIGHT, w=W//2)
    d.rectangle([80, 148, W//2-80, 152], fill=rgb(ACCENT))

    # WITH header
    cx_right = W//2
    f_hdr_gold = fnt("ab", 72)
    bb = d.textbbox((0,0), "WITH THE KIT", font=f_hdr_gold)
    rx = cx_right + (W//2 - (bb[2]-bb[0])) // 2
    d.text((rx, 55), "WITH THE KIT", font=f_hdr_gold, fill=rgb(GOLD))
    d.rectangle([W//2+80, 148, W-80, 152], fill=rgb(GOLD))

    struggles = [
        "Starting from scratch every time",
        "Unsure what to say to leads",
        "No consistent client process",
        "Contracts from the internet (yikes)",
        "Posting whatever feels okay",
        "Guessing on pricing & packages",
        "Losing clients to silence",
    ]
    solutions = [
        "Done-for-you templates, ready now",
        "Word-for-word inquiry scripts",
        "Full booking system in place",
        "Professional contract language",
        "365 captions + content calendar",
        "Complete pricing guide & packages",
        "Follow-up system that books jobs",
    ]

    f_x_icon = fnt("ab", 44)
    f_check_icon = fnt("ab", 44)
    f_item = fnt("ar", 38)

    item_start_y = 190
    item_gap = 100

    for i, (s, sol) in enumerate(zip(struggles, solutions)):
        iy = item_start_y + i * item_gap

        # Left (WITHOUT) — ✗
        d.text((90, iy), "✗", font=f_x_icon, fill=rgb(ACCENT))
        wrapped = wrap_text(d, s, f_item, W//2 - 180)
        ty = iy + 4
        for wl in wrapped:
            d.text((148, ty), wl, font=f_item, fill=rgb(CREAM))
            ty += 42

        # Right (WITH) — ✓
        d.text((W//2 + 30, iy), "✓", font=f_check_icon, fill=rgb(GOLD))
        wrapped2 = wrap_text(d, sol, f_item, W//2 - 180)
        ty2 = iy + 4
        for wl in wrapped2:
            d.text((W//2 + 90, ty2), wl, font=f_item, fill=rgb(CREAM))
            ty2 += 42

    # Bottom gold bar
    d.rectangle([0, H-155, W, H], fill=rgb(GOLD))
    d.rectangle([0, H-157, W, H-154], fill=rgb(DARK))
    f_price = fnt("sb", 80)
    cx(d, "10 Templates  •  $24  •  Instant Download", H-135, f_price, DARK)

    save(img, "05_value_anchor.jpg")

# ─────────────────────────────────────────────
# 06_before_after.jpg
# ─────────────────────────────────────────────
def gen_06():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Top banner
    banner_h = 180
    d.rectangle([0, 0, W, banner_h], fill=rgb(MAIN))
    d.rectangle([0, banner_h-6, W, banner_h], fill=rgb(GOLD))

    f_banner = fnt("ab", 68)
    cx(d, "FROM SHOOTING ON VIBES TO RUNNING A BUSINESS", 48, f_banner, GOLD)

    # Subtitle
    f_sub = fnt("sr", 44)
    cx(d, "Here's what changes when you have the right systems in place.", banner_h+24, f_sub, LIGHT)

    d.rectangle([150, banner_h+94, W-150, banner_h+98], fill=rgb(ACCENT))

    # Two panels
    panel_top = banner_h + 120
    panel_h = H - panel_top - 170
    panel_w = (W - 120) // 2
    panel_gap = 60
    left_x = 60
    right_x = left_x + panel_w + panel_gap

    # BEFORE panel
    d.rectangle([left_x, panel_top, left_x+panel_w, panel_top+panel_h], fill=rgb(MAIN))
    d.rectangle([left_x, panel_top, left_x+panel_w, panel_top+panel_h], outline=rgb(ACCENT), width=2)
    d.rectangle([left_x, panel_top, left_x+panel_w, panel_top+50], fill=rgb(ACCENT))
    f_ph = fnt("ab", 46)
    bb = d.textbbox((0,0), "BEFORE", font=f_ph)
    bx2 = left_x + (panel_w - (bb[2]-bb[0])) // 2
    d.text((bx2, panel_top+6), "BEFORE", font=f_ph, fill=rgb(DARK))

    before_items = [
        "Spending hours writing captions",
        "Forgetting to follow up with leads",
        "Sending sloppy first impressions",
        "No contract = no protection",
        "Pricing based on gut feelings",
        "Content calendar = your brain",
        "Every booking feels improvised",
    ]

    f_bi = fnt("ar", 38)
    f_x = fnt("ab", 44)
    biy = panel_top + 72
    for item in before_items:
        d.text((left_x+24, biy), "✗", font=f_x, fill=rgb(LIGHT))
        wrapped = wrap_text(d, item, f_bi, panel_w - 90)
        ty = biy + 4
        for wl in wrapped:
            d.text((left_x+78, ty), wl, font=f_bi, fill=rgb(CREAM))
            ty += 40
        biy = ty + 14

    # AFTER panel
    d.rectangle([right_x, panel_top, right_x+panel_w, panel_top+panel_h], fill=rgb(DARK))
    d.rectangle([right_x, panel_top, right_x+panel_w, panel_top+panel_h], outline=rgb(GOLD), width=2)
    d.rectangle([right_x, panel_top, right_x+panel_w, panel_top+50], fill=rgb(GOLD))
    bb2 = d.textbbox((0,0), "AFTER", font=f_ph)
    ax2 = right_x + (panel_w - (bb2[2]-bb2[0])) // 2
    d.text((ax2, panel_top+6), "AFTER", font=f_ph, fill=rgb(DARK))

    after_items = [
        "365 captions ready in seconds",
        "Follow-up scripts that close jobs",
        "Professional inquiry responses",
        "Contract templates that protect you",
        "Pricing guide with full packages",
        "30-day content calendar done",
        "Every booking runs on a system",
    ]

    f_check = fnt("ab", 44)
    aiy = panel_top + 72
    for item in after_items:
        d.text((right_x+24, aiy), "✓", font=f_check, fill=rgb(GOLD))
        wrapped = wrap_text(d, item, f_bi, panel_w - 90)
        ty = aiy + 4
        for wl in wrapped:
            d.text((right_x+78, ty), wl, font=f_bi, fill=rgb(CREAM))
            ty += 40
        aiy = ty + 14

    # Bottom
    d.rectangle([0, H-155, W, H], fill=rgb(GOLD))
    d.rectangle([0, H-157, W, H-154], fill=rgb(DARK))
    f_bot = fnt("sb", 58)
    cx(d, "Photography Business Kit  —  $24  •  Instant Download", H-132, f_bot, DARK)

    save(img, "06_before_after.jpg")

# ─────────────────────────────────────────────
# 07_mockup.jpg
# ─────────────────────────────────────────────
def gen_07():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Subtle grid background
    grid_col = tuple(min(255, c+12) for c in rgb(DARK))
    for gx in range(0, W, 80):
        d.line([(gx, 0), (gx, H)], fill=grid_col, width=1)
    for gy in range(0, H, 80):
        d.line([(0, gy), (W, gy)], fill=grid_col, width=1)

    draw_border(d, 10)

    # Top title
    f_top = fnt("sb", 60)
    cx(d, "PHOTOGRAPHY BUSINESS KIT", 40, f_top, GOLD)

    d.rectangle([200, 120, W-200, 124], fill=rgb(GOLD))

    # Laptop body
    laptop_x = 380
    laptop_y = 155
    laptop_w = W - 760
    laptop_h = int(laptop_w * 0.625)
    laptop_bot_y = laptop_y + laptop_h

    # Laptop base (bottom)
    base_h = 60
    base_y = laptop_bot_y + 18
    base_x = laptop_x - 80
    base_w = laptop_w + 160
    # Base shadow
    d.rectangle([base_x+10, base_y+10, base_x+base_w+10, base_y+base_h+10],
                fill=tuple(max(0,c-10) for c in rgb(DARK)))
    # Base
    d.rectangle([base_x, base_y, base_x+base_w, base_y+base_h], fill=rgb(ACCENT))
    d.rectangle([base_x, base_y, base_x+base_w, base_y+base_h], outline=rgb(GOLD), width=2)
    # Hinge detail
    hinge_x = base_x + base_w//2 - 80
    d.rectangle([hinge_x, base_y-4, hinge_x+160, base_y+14], fill=rgb(MAIN))
    d.rectangle([hinge_x, base_y-4, hinge_x+160, base_y+14], outline=rgb(GOLD), width=1)

    # Laptop screen outer
    d.rectangle([laptop_x-8, laptop_y-8, laptop_x+laptop_w+8, laptop_bot_y+8],
                fill=rgb(ACCENT))
    # Gold border
    d.rectangle([laptop_x-8, laptop_y-8, laptop_x+laptop_w+8, laptop_bot_y+8],
                outline=rgb(GOLD), width=6)
    # Screen inner (dark bezel)
    bezel = 22
    screen_x = laptop_x + bezel
    screen_y = laptop_y + bezel
    screen_w = laptop_w - 2*bezel
    screen_h = laptop_h - 2*bezel
    d.rectangle([screen_x, screen_y, screen_x+screen_w, screen_y+screen_h],
                fill=rgb(MAIN))

    # Screen content
    # Header bar on screen
    header_y = screen_y + 40
    header_h = 70
    d.rectangle([screen_x+20, header_y, screen_x+screen_w-20, header_y+header_h],
                fill=rgb(DARK))
    d.rectangle([screen_x+20, header_y, screen_x+screen_w-20, header_y+6],
                fill=rgb(GOLD))
    f_screen_h = fnt("ab", 42)
    cx(d, "Photography Contract Template", header_y+16, f_screen_h, GOLD,
       w=screen_x + screen_w - screen_x)
    # Offset for centered-in-screen
    bb = d.textbbox((0,0), "Photography Contract Template", font=f_screen_h)
    tx = screen_x + (screen_w - (bb[2]-bb[0])) // 2
    d.text((tx, header_y+16), "Photography Contract Template", font=f_screen_h, fill=rgb(GOLD))

    # Simulated text lines
    line_x = screen_x + 40
    line_y_start = header_y + header_h + 30
    line_widths = [screen_w-100, screen_w-200, screen_w-80, screen_w-240,
                   screen_w-120, screen_w-180, screen_w-90, screen_w-210,
                   screen_w-140, screen_w-160]
    line_cols = [CREAM, LIGHT, CREAM, LIGHT, CREAM, LIGHT, CREAM, LIGHT, CREAM, LIGHT]
    for j, (lw, lc) in enumerate(zip(line_widths, line_cols)):
        ly2 = line_y_start + j*42
        if ly2 + 14 > screen_y + screen_h - 30:
            break
        alpha = max(60, 200 - j*14)
        col = rgb(lc)
        # Vary line lengths for realism
        if j % 3 == 2:
            lw = int(lw * 0.5)
        d.rectangle([line_x, ly2, line_x+lw, ly2+14], fill=col)

    # Google Docs logo hint (colored dots)
    dot_y = screen_y + screen_h - 52
    dot_x = screen_x + screen_w//2 - 48
    dot_colors = [(rgb("#4285F4")), rgb("#34A853"), rgb("#FBBC04"), rgb("#EA4335")]
    for di, dc in enumerate(dot_colors):
        d.ellipse([dot_x+di*28, dot_y, dot_x+di*28+20, dot_y+20], fill=dc)

    # Below laptop caption
    caption_y = base_y + base_h + 50
    f_cap = fnt("sr", 54)
    cx(d, "Opens instantly in Google Docs, Notion, or Word", caption_y, f_cap, CREAM)

    f_cap2 = fnt("ar", 40)
    cx(d, "Edit, customize, and use immediately — no design skills needed.", caption_y+72, f_cap2, LIGHT)

    # Bottom
    d.rectangle([100, H-120, W-100, H-116], fill=rgb(GOLD))
    f_bot = fnt("ab", 44)
    cx(d, "PHOTOGRAPHY BUSINESS KIT  •  10 TEMPLATES  •  INSTANT DOWNLOAD", H-100, f_bot, GOLD)

    save(img, "07_mockup.jpg")


# ─────────────────────────────────────────────
# RUN ALL
# ─────────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Generating Photography Business Kit Etsy images...")
    gen_01(); print("  01/07 Hero")
    gen_02(); print("  02/07 What's Inside")
    gen_03(); print("  03/07 Caption Preview")
    gen_04(); print("  04/07 System Feature")
    gen_05(); print("  05/07 Value Anchor")
    gen_06(); print("  06/07 Before/After")
    gen_07(); print("  07/07 Mockup")
    print("\nAll 7 images generated successfully.")
