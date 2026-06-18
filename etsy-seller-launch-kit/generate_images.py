from PIL import Image, ImageDraw, ImageFont
import os, textwrap

FONT_DIR = "/usr/share/fonts/truetype/liberation"
W, H = 2700, 2025
OUT_DIR = "/home/user/oqul-phase55-production/etsy-seller-launch-kit/4_ETSY_IMAGES"

DARK   = "#1A0800"
MAIN   = "#7D2E00"
ACCENT = "#E8650A"
LIGHT  = "#F5A623"
CREAM  = "#FFF8F0"
GOLD   = "#F5A623"

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

def save(img, name):
    path = os.path.join(OUT_DIR, name)
    img.save(path, "JPEG", quality=95)
    print(f"  Saved: {name}")

def wrap_text(draw, text, x, y, font, col, max_width, line_spacing=10):
    """Wrap text to fit within max_width pixels."""
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        bb = draw.textbbox((0,0), test_line, font=font)
        if bb[2]-bb[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    for line in lines:
        draw.text((x, y), line, font=font, fill=rgb(col))
        bb = draw.textbbox((0,0), line, font=font)
        y += (bb[3]-bb[1]) + line_spacing
    return y

# ─────────────────────────────────────────────────────────────
# 01_hero.jpg
# ─────────────────────────────────────────────────────────────
def make_01():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Border bars 12px ACCENT
    bar = 12
    d.rectangle([0, 0, W, bar], fill=rgb(ACCENT))
    d.rectangle([0, H-bar, W, H], fill=rgb(ACCENT))
    d.rectangle([0, 0, bar, H], fill=rgb(ACCENT))
    d.rectangle([W-bar, 0, W, H], fill=rgb(ACCENT))

    # Decorative top stripe
    d.rectangle([0, bar, W, bar+4], fill=rgb(MAIN))

    # Title
    f_title = fnt("sb", 118)
    cy = 180
    cx(d, "ETSY SELLER LAUNCH KIT", cy, f_title, LIGHT)

    # Subtitle
    f_sub = fnt("sr", 68)
    cy += 165
    cx(d, "The Complete Etsy Business System", cy, f_sub, CREAM)

    # Divider
    cy += 110
    margin = 200
    d.rectangle([margin, cy, W-margin, cy+4], fill=rgb(ACCENT))

    # Feature line
    cy += 30
    f_feat = fnt("ab", 52)
    cx(d, "10 Professional Templates  •  Instant Digital Download", cy, f_feat, LIGHT)

    # Template preview boxes
    cy += 130
    labels = ["365 Captions", "Shop SEO", "Listing Templates", "Ad Copy", "Review System", "Business Guide"]
    n = len(labels)
    pad = 40
    box_w = (W - 2*pad - (n-1)*30) // n
    box_h = 200
    f_box = fnt("ab", 38)
    for i, lbl in enumerate(labels):
        bx = pad + i*(box_w+30)
        # Box with MAIN bg and ACCENT border
        d.rectangle([bx, cy, bx+box_w, cy+box_h], fill=rgb(MAIN))
        d.rectangle([bx, cy, bx+box_w, cy+4], fill=rgb(ACCENT))
        d.rectangle([bx, cy+box_h-4, bx+box_w, cy+box_h], fill=rgb(ACCENT))
        # Center text in box
        bb = d.textbbox((0,0), lbl, font=f_box)
        tx = bx + (box_w - (bb[2]-bb[0]))//2
        ty = cy + (box_h - (bb[3]-bb[1]))//2
        d.text((tx, ty), lbl, font=f_box, fill=rgb(CREAM))

    # Decorative bottom label
    cy += box_h + 60
    f_small = fnt("ar", 42)
    cx(d, "✦  Professional  •  Complete  •  Ready to Use  ✦", cy, f_small, ACCENT)

    # Bottom branding strip
    d.rectangle([0, H-110, W, H-bar], fill=rgb(MAIN))
    f_brand = fnt("ab", 44)
    cx(d, "INSTANT DIGITAL DOWNLOAD", H-88, f_brand, CREAM)

    save(img, "01_hero.jpg")


# ─────────────────────────────────────────────────────────────
# 02_whats_inside.jpg
# ─────────────────────────────────────────────────────────────
def make_02():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Header bar
    d.rectangle([0, 0, W, 180], fill=rgb(ACCENT))
    f_hdr = fnt("ab", 90)
    cx(d, "WHAT'S INSIDE", 38, f_hdr, DARK)

    # Decorative stripe under header
    d.rectangle([0, 180, W, 188], fill=rgb(LIGHT))

    templates = [
        (1, "365 Etsy Seller Captions"),
        (2, "Shop SEO & Listing Description Templates"),
        (3, "Customer Message Scripts"),
        (4, "Review Request & Response System"),
        (5, "Social Media Ad Copy (10 ads)"),
        (6, "Pricing & Packaging Guide"),
        (7, "Hashtag Bank (200 hashtags)"),
        (8, "30-Day Content Calendar"),
        (9, "Launch & Relaunch Promotion Templates"),
        (10,"Etsy Business Systems Guide"),
    ]

    f_num = fnt("ab", 48)
    f_item = fnt("sr", 52)
    col1 = templates[:5]
    col2 = templates[5:]
    col_x = [100, W//2 + 50]
    start_y = 240
    row_h = 130

    for col_idx, col_items in enumerate([col1, col2]):
        cx_pos = col_x[col_idx]
        for row_idx, (num, name) in enumerate(col_items):
            y = start_y + row_idx * row_h
            # Number badge
            badge_r = 32
            badge_cx = cx_pos + badge_r
            badge_cy = y + badge_r
            d.ellipse([badge_cx-badge_r, badge_cy-badge_r, badge_cx+badge_r, badge_cy+badge_r],
                      fill=rgb(LIGHT))
            num_str = str(num)
            bb = d.textbbox((0,0), num_str, font=f_num)
            nx = badge_cx - (bb[2]-bb[0])//2
            ny = badge_cy - (bb[3]-bb[1])//2
            d.text((nx, ny), num_str, font=f_num, fill=rgb(DARK))
            # Item text
            d.text((cx_pos + badge_r*2 + 20, y + 8), name, font=f_item, fill=rgb(CREAM))

            # Subtle divider
            if row_idx < len(col_items)-1:
                dy = y + row_h - 12
                d.rectangle([cx_pos, dy, cx_pos + (W//2 - 120), dy+1], fill=rgb(MAIN))

    # Vertical divider between columns
    mid = W//2 + 10
    d.rectangle([mid, 230, mid+2, H-120], fill=rgb(MAIN))

    # Bottom bar
    d.rectangle([0, H-120, W, H], fill=rgb(DARK))
    d.rectangle([0, H-120, W, H-116], fill=rgb(ACCENT))
    f_bot = fnt("ab", 52)
    cx(d, "Instant Download  •  Google Docs & Notion Compatible", H-96, f_bot, CREAM)

    save(img, "02_whats_inside.jpg")


# ─────────────────────────────────────────────────────────────
# 03_content_preview.jpg
# ─────────────────────────────────────────────────────────────
def make_03():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Decorative top bar
    d.rectangle([0, 0, W, 8], fill=rgb(ACCENT))

    # Header
    f_title = fnt("sb", 108)
    cx(d, "365 ETSY CAPTIONS INCLUDED", 40, f_title, LIGHT)

    f_sub = fnt("sr", 58)
    cx(d, "A full year of content for Etsy sellers", 178, f_sub, CREAM)

    # Divider
    d.rectangle([180, 268, W-180, 272], fill=rgb(ACCENT))

    captions = [
        "New listing is live. Handmade with intention,\nshipped with care. Link in bio.",
        "Behind the scenes: the cutting, the packaging,\nthe tiny details that make this worth every penny.",
        "Your order is being packed right now.\nHere's what goes into every single one.",
        "5-star review from yesterday: 'Better than the\nphotos. Will be back.' This is why I do it.",
        "Shop update: restock happening this Friday\nat 6pm EST. Set your reminder.",
        "Poll: do you prefer natural or bold\npackaging? Natural | Bold",
    ]

    f_cap = fnt("sr", 40)
    f_num = fnt("ab", 38)
    f_tag = fnt("ar", 32)

    # 6 cards in 2 rows of 3
    card_margin = 60
    card_pad = 30
    cols = 3
    rows = 2
    card_w = (W - (cols+1)*card_margin) // cols
    card_h = (H - 320 - (rows+1)*card_margin) // rows

    for i, caption in enumerate(captions):
        col = i % cols
        row = i // cols
        cx_pos = card_margin + col*(card_w + card_margin)
        cy_pos = 310 + card_margin + row*(card_h + card_margin)

        # Card background
        d.rectangle([cx_pos, cy_pos, cx_pos+card_w, cy_pos+card_h],
                    fill=rgb(MAIN))
        # Top accent stripe
        d.rectangle([cx_pos, cy_pos, cx_pos+card_w, cy_pos+8], fill=rgb(ACCENT))
        # Number badge
        badge_str = f"#{i+1:03d}"
        d.text((cx_pos+16, cy_pos+20), badge_str, font=f_num, fill=rgb(LIGHT))

        # Caption text with wrapping
        lines = caption.split('\n')
        ty = cy_pos + 80
        for line in lines:
            d.text((cx_pos+card_pad, ty), line, font=f_cap, fill=rgb(CREAM))
            bb = d.textbbox((0,0), line, font=f_cap)
            ty += (bb[3]-bb[1]) + 8

        # Tag line at bottom
        tag = "#etsyshop #handmade"
        d.text((cx_pos+card_pad, cy_pos+card_h-50), tag, font=f_tag, fill=rgb(ACCENT))

    # Bottom strip
    d.rectangle([0, H-8, W, H], fill=rgb(ACCENT))

    save(img, "03_content_preview.jpg")


# ─────────────────────────────────────────────────────────────
# 04_system_feature.jpg
# ─────────────────────────────────────────────────────────────
def make_04():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Decorative top element
    d.rectangle([0, 0, W, 12], fill=rgb(ACCENT))
    d.rectangle([0, 12, W, 16], fill=rgb(LIGHT))

    # Title
    f_title = fnt("sb", 98)
    cx(d, "COMPLETE LISTING & SEO SYSTEM", 70, f_title, LIGHT)

    f_sub = fnt("sr", 56)
    cx(d, "Write listings that rank and convert", 198, f_sub, CREAM)

    # Divider
    d.rectangle([200, 290, W-200, 294], fill=rgb(ACCENT))

    # Flow diagram
    steps = ["RESEARCH\nKEYWORDS", "WRITE\nTITLE", "CRAFT\nDESCRIPTION", "ADD\nTAGS", "OPTIMIZE\nPHOTOS"]
    n = len(steps)
    step_w = 300
    step_h = 220
    total_w = n * step_w + (n-1)*80  # arrows between
    start_x = (W - total_w) // 2
    step_y = 340
    f_step = fnt("ab", 40)
    f_arrow = fnt("ab", 60)

    for i, step in enumerate(steps):
        sx = start_x + i*(step_w + 80)
        # Step box
        d.rectangle([sx, step_y, sx+step_w, step_y+step_h], fill=rgb(MAIN))
        d.rectangle([sx, step_y, sx+step_w, step_y+8], fill=rgb(ACCENT))
        d.rectangle([sx, step_y+step_h-8, sx+step_w, step_y+step_h], fill=rgb(ACCENT))
        # Step number circle
        circ_r = 28
        d.ellipse([sx+step_w//2-circ_r, step_y+18, sx+step_w//2+circ_r, step_y+18+circ_r*2],
                  fill=rgb(ACCENT))
        sn = str(i+1)
        bb = d.textbbox((0,0), sn, font=fnt("ab",36))
        d.text((sx+step_w//2-(bb[2]-bb[0])//2, step_y+22), sn, font=fnt("ab",36), fill=rgb(DARK))
        # Step text (2 lines)
        lines = step.split('\n')
        ty = step_y + 90
        for line in lines:
            bb = d.textbbox((0,0), line, font=f_step)
            tx = sx + (step_w - (bb[2]-bb[0]))//2
            d.text((tx, ty), line, font=f_step, fill=rgb(CREAM))
            ty += (bb[3]-bb[1]) + 8
        # Arrow (not after last)
        if i < n-1:
            ax = sx + step_w + 10
            ay = step_y + step_h//2 - 20
            d.polygon([(ax, ay+20), (ax+60, ay+20), (ax+60, ay+8), (ax+80, ay+30),
                       (ax+60, ay+52), (ax+60, ay+40), (ax, ay+40)], fill=rgb(ACCENT))

    # 3 Feature highlight cards
    feat_y = step_y + step_h + 100
    feats = [
        ("Listing Title\nTemplates", "Fill-in-the-blank title\nformats for any product"),
        ("Tag Strategy\nGuide", "13 tags that drive\norganic Etsy traffic"),
        ("Description\nFrameworks", "Proven structures that\nturn browsers into buyers"),
    ]
    feat_cols = 3
    feat_margin = 80
    feat_w = (W - (feat_cols+1)*feat_margin) // feat_cols
    feat_h = H - feat_y - 100
    f_fh = fnt("ab", 52)
    f_fd = fnt("sr", 42)

    for i, (title, desc) in enumerate(feats):
        fx = feat_margin + i*(feat_w + feat_margin)
        # Card
        d.rectangle([fx, feat_y, fx+feat_w, feat_y+feat_h], fill=rgb(MAIN))
        d.rectangle([fx, feat_y, fx+feat_w, feat_y+10], fill=rgb(LIGHT))
        # Title
        lines = title.split('\n')
        ty = feat_y + 40
        for line in lines:
            bb = d.textbbox((0,0), line, font=f_fh)
            tx = fx + (feat_w - (bb[2]-bb[0]))//2
            d.text((tx, ty), line, font=f_fh, fill=rgb(LIGHT))
            ty += (bb[3]-bb[1]) + 6
        # Desc
        ty += 20
        lines2 = desc.split('\n')
        for line in lines2:
            bb = d.textbbox((0,0), line, font=f_fd)
            tx = fx + (feat_w - (bb[2]-bb[0]))//2
            d.text((tx, ty), line, font=f_fd, fill=rgb(CREAM))
            ty += (bb[3]-bb[1]) + 8

    save(img, "04_system_feature.jpg")


# ─────────────────────────────────────────────────────────────
# 05_value_anchor.jpg
# ─────────────────────────────────────────────────────────────
def make_05():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Left panel DARK (already bg), Right panel MAIN
    mid = W // 2
    d.rectangle([mid, 0, W, H-130], fill=rgb(MAIN))

    # Top banner
    d.rectangle([0, 0, W, 130], fill=rgb(ACCENT))
    d.rectangle([0, 130, W, 138], fill=rgb(LIGHT))

    f_hdr = fnt("ab", 72)
    cx(d, "WITHOUT vs WITH THE KIT", 30, f_hdr, DARK)

    # LEFT header
    f_side = fnt("ab", 62)
    cx_left = mid // 2
    d.text((cx_left - d.textbbox((0,0),"WITHOUT THIS KIT",font=f_side)[2]//2, 160),
           "WITHOUT THIS KIT", font=f_side, fill=rgb(LIGHT))
    # center in left panel
    bb = d.textbbox((0,0), "WITHOUT THIS KIT", font=f_side)
    tx = (mid - (bb[2]-bb[0]))//2
    d.text((tx, 162), "WITHOUT THIS KIT", font=f_side, fill=rgb(ACCENT))

    # RIGHT header
    bb2 = d.textbbox((0,0), "WITH THIS KIT", font=f_side)
    tx2 = mid + (mid - (bb2[2]-bb2[0]))//2
    d.text((tx2, 162), "WITH THIS KIT", font=f_side, fill=rgb(LIGHT))

    struggles = [
        "Guessing which keywords to use",
        "Generic listing descriptions",
        "No system for getting reviews",
        "Posting randomly with no strategy",
        "Restarting from scratch each listing",
    ]
    solutions = [
        "Proven SEO-optimized listing templates",
        "Professional description frameworks",
        "Complete review request system",
        "30-day content calendar",
        "Done-for-you caption bank",
    ]

    f_item = fnt("sr", 48)
    f_mark = fnt("ab", 56)
    item_start_y = 280
    item_spacing = 120

    for i, (struggle, solution) in enumerate(zip(struggles, solutions)):
        iy = item_start_y + i * item_spacing

        # Left — struggle with X
        lx_icon = 80
        d.text((lx_icon, iy), "✗", font=f_mark, fill=rgb(ACCENT))
        # Wrap if needed
        wrap_text(d, struggle, lx_icon+70, iy+4, f_item, CREAM, mid-lx_icon-90, 4)

        # Divider row
        d.rectangle([60, iy+item_spacing-10, mid-60, iy+item_spacing-9], fill=rgb(MAIN))

        # Right — solution with checkmark
        rx_icon = mid + 80
        d.text((rx_icon, iy), "✓", font=f_mark, fill=rgb(LIGHT))
        wrap_text(d, solution, rx_icon+70, iy+4, f_item, CREAM, mid-rx_icon-90+mid, 4)
        d.rectangle([mid+60, iy+item_spacing-10, W-60, iy+item_spacing-9], fill=rgb(ACCENT))

    # Vertical divider
    d.rectangle([mid-3, 140, mid+3, H-130], fill=rgb(ACCENT))

    # Bottom bar
    d.rectangle([0, H-130, W, H], fill=rgb(DARK))
    d.rectangle([0, H-130, W, H-124], fill=rgb(ACCENT))
    f_price = fnt("ab", 78)
    cx(d, "10 Templates  •  $17  •  Instant Download", H-114, f_price, LIGHT)

    save(img, "05_value_anchor.jpg")


# ─────────────────────────────────────────────────────────────
# 06_before_after.jpg
# ─────────────────────────────────────────────────────────────
def make_06():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Top banner ACCENT
    d.rectangle([0, 0, W, 160], fill=rgb(ACCENT))
    f_banner = fnt("ab", 88)
    cx(d, "FROM INVISIBLE TO CONVERTING", 32, f_banner, DARK)
    d.rectangle([0, 160, W, 168], fill=rgb(LIGHT))

    # Two panels
    panel_y = 190
    panel_h = H - panel_y - 140
    mid = W // 2 - 10
    pad = 40

    # LEFT panel (DARK bg, already set)
    # Slight lighter bg for contrast
    d.rectangle([pad, panel_y, mid, panel_y+panel_h], fill=rgb("#200A00"))
    d.rectangle([pad, panel_y, mid, panel_y+8], fill=rgb(ACCENT))
    # LEFT title
    f_ptitle = fnt("ab", 64)
    cx_left_mid = (pad + mid) // 2
    bb = d.textbbox((0,0), "BEFORE", font=f_ptitle)
    d.text(((mid+pad-(bb[2]-bb[0]))//2, panel_y+24), "BEFORE", font=f_ptitle, fill=rgb(ACCENT))

    # RIGHT panel
    d.rectangle([mid+20, panel_y, W-pad, panel_y+panel_h], fill=rgb(MAIN))
    d.rectangle([mid+20, panel_y, W-pad, panel_y+8], fill=rgb(LIGHT))
    bb2 = d.textbbox((0,0), "AFTER", font=f_ptitle)
    d.text(((W-pad+mid+20-(bb2[2]-bb2[0]))//2, panel_y+24), "AFTER", font=f_ptitle, fill=rgb(LIGHT))

    before_items = [
        "No keyword strategy",
        "Generic copy-paste descriptions",
        "Zero review follow-up",
        "Random posting, no plan",
    ]
    after_items = [
        "SEO-optimized titles & tags",
        "Proven description frameworks",
        "Automated review system",
        "30-day content calendar",
    ]

    f_item = fnt("sr", 52)
    f_mark = fnt("ab", 60)
    item_start = panel_y + 110
    spacing = 140

    for i, (b, a) in enumerate(zip(before_items, after_items)):
        iy = item_start + i * spacing

        # Before item
        bx = pad + 30
        d.text((bx, iy), "✗", font=f_mark, fill=rgb(ACCENT))
        d.text((bx+65, iy+4), b, font=f_item, fill=rgb(CREAM))

        # After item
        ax = mid + 50
        d.text((ax, iy), "✓", font=f_mark, fill=rgb(LIGHT))
        d.text((ax+65, iy+4), a, font=f_item, fill=rgb(CREAM))

        # subtle dividers
        if i < len(before_items)-1:
            dly = iy + spacing - 20
            d.rectangle([pad+20, dly, mid-20, dly+1], fill=rgb(MAIN))
            d.rectangle([mid+40, dly, W-pad-20, dly+1], fill=rgb(ACCENT))

    # Bottom bar
    d.rectangle([0, H-140, W, H], fill=rgb(DARK))
    d.rectangle([0, H-140, W, H-134], fill=rgb(LIGHT))
    f_bot = fnt("ab", 56)
    cx(d, "Etsy Seller Launch Kit  •  10 Templates  •  Instant Download", H-116, f_bot, CREAM)

    save(img, "06_before_after.jpg")


# ─────────────────────────────────────────────────────────────
# 07_mockup.jpg
# ─────────────────────────────────────────────────────────────
def make_07():
    img = Image.new("RGB", (W, H), rgb(DARK))
    d = ImageDraw.Draw(img)

    # Subtle grid pattern
    grid_col = rgb("#220B00")
    for gx in range(0, W, 80):
        d.line([(gx, 0), (gx, H)], fill=grid_col, width=1)
    for gy in range(0, H, 80):
        d.line([(0, gy), (W, gy)], fill=grid_col, width=1)

    # Laptop base dimensions
    laptop_w = 1800
    laptop_h = 1100
    laptop_x = (W - laptop_w) // 2
    laptop_y = 80

    # Laptop body (outer shell)
    body_margin = 40
    d.rectangle([laptop_x, laptop_y, laptop_x+laptop_w, laptop_y+laptop_h],
                fill=rgb("#2A1000"))
    # Outer border
    d.rectangle([laptop_x, laptop_y, laptop_x+laptop_w, laptop_y+laptop_h],
                outline=rgb(MAIN), width=8)

    # Screen bezel
    bezel = 60
    screen_x = laptop_x + bezel
    screen_y = laptop_y + bezel
    screen_w = laptop_w - 2*bezel
    screen_h = laptop_h - bezel - 120  # leave base at bottom

    d.rectangle([screen_x, screen_y, screen_x+screen_w, screen_y+screen_h],
                fill=rgb("#0D0400"))
    # Screen border (ACCENT)
    d.rectangle([screen_x, screen_y, screen_x+screen_w, screen_y+screen_h],
                outline=rgb(ACCENT), width=6)

    # Laptop base/keyboard area
    base_y = screen_y + screen_h
    d.rectangle([laptop_x, base_y, laptop_x+laptop_w, laptop_y+laptop_h],
                fill=rgb("#1A0800"))
    # Keyboard hint
    f_kb = fnt("ar", 28)
    d.text((laptop_x + laptop_w//2 - 60, base_y + 40), "▬ ▬ ▬", font=f_kb, fill=rgb(MAIN))

    # Trackpad
    tp_w, tp_h = 280, 160
    tp_x = laptop_x + (laptop_w - tp_w)//2
    tp_y = base_y + 60
    d.rectangle([tp_x, tp_y, tp_x+tp_w, tp_y+tp_h], fill=rgb(MAIN), outline=rgb(MAIN), width=2)

    # Laptop hinge
    hinge_y = base_y
    d.rectangle([laptop_x+100, hinge_y-4, laptop_x+laptop_w-100, hinge_y+4], fill=rgb(ACCENT))

    # Screen content
    content_pad = 60
    content_x = screen_x + content_pad
    content_y_start = screen_y + 50

    # Browser bar simulation
    bar_h = 50
    d.rectangle([screen_x, screen_y, screen_x+screen_w, screen_y+bar_h], fill=rgb("#160600"))
    d.ellipse([screen_x+20, screen_y+15, screen_x+40, screen_y+35], fill=rgb(ACCENT))
    d.ellipse([screen_x+50, screen_y+15, screen_x+70, screen_y+35], fill=rgb(LIGHT))
    d.ellipse([screen_x+80, screen_y+15, screen_x+100, screen_y+35], fill=rgb(MAIN))

    # URL bar
    d.rectangle([screen_x+120, screen_y+12, screen_x+screen_w-20, screen_y+bar_h-12],
                fill=rgb("#0D0400"), outline=rgb(MAIN), width=1)
    f_url = fnt("ar", 24)
    d.text((screen_x+130, screen_y+17), "docs.google.com/document/etsy-listing-template", font=f_url, fill=rgb(ACCENT))

    # Document content on screen
    doc_y = screen_y + bar_h + 30
    # Doc title
    f_doc_title = fnt("sb", 52)
    doc_title = "Etsy Listing Description Template"
    bb = d.textbbox((0,0), doc_title, font=f_doc_title)
    doc_x = screen_x + (screen_w - (bb[2]-bb[0]))//2
    d.text((doc_x, doc_y), doc_title, font=f_doc_title, fill=rgb(LIGHT))

    # Divider under doc title
    doc_y += 72
    d.rectangle([screen_x+40, doc_y, screen_x+screen_w-40, doc_y+2], fill=rgb(ACCENT))
    doc_y += 20

    # Simulated text lines
    f_line = fnt("ar", 32)
    f_bold_line = fnt("ab", 34)
    sim_lines = [
        ("ab", "PRODUCT TITLE FORMULA:", ACCENT),
        ("ar", "[Keyword 1] + [Keyword 2] + [Product Type] for [Audience]", CREAM),
        ("", "", ""),
        ("ab", "OPENING HOOK:", ACCENT),
        ("ar", "Looking for [product benefit]? This handmade [product] is designed...", CREAM),
        ("", "", ""),
        ("ab", "KEY FEATURES:", ACCENT),
        ("ar", "• Made from: ________________________________", CREAM),
        ("ar", "• Perfect for: _______________________________", CREAM),
        ("ar", "• Ships in: __________________________________", CREAM),
        ("", "", ""),
        ("ab", "CALL TO ACTION:", ACCENT),
        ("ar", "Add to your cart today and receive [bonus/guarantee].", CREAM),
    ]

    line_y = doc_y + 10
    for ftype, text, col in sim_lines:
        if ftype == "":
            line_y += 18
            continue
        f_use = fnt("ab", 34) if ftype == "ab" else fnt("ar", 32)
        d.text((screen_x+60, line_y), text, font=f_use, fill=rgb(col))
        bb = d.textbbox((0,0), text, font=f_use)
        line_y += (bb[3]-bb[1]) + 8
        if line_y > screen_y + screen_h - 30:
            break

    # Below laptop text
    below_y = laptop_y + laptop_h + 60
    f_below = fnt("sr", 54)
    cx(d, "Opens instantly in Google Docs, Notion, or Word", below_y, f_below, CREAM)

    # Watermark at bottom
    below_y += 90
    d.rectangle([0, below_y, W, below_y+4], fill=rgb(ACCENT))
    f_wm = fnt("ab", 44)
    cx(d, "ETSY SELLER LAUNCH KIT", below_y+18, f_wm, ACCENT)

    save(img, "07_mockup.jpg")


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Generating images...")
    make_01()
    make_02()
    make_03()
    make_04()
    make_05()
    make_06()
    make_07()
    print("All 7 images generated successfully.")
