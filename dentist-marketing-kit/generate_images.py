from PIL import Image, ImageDraw, ImageFont
import os, textwrap

FONT_DIR = "/usr/share/fonts/truetype/liberation"
W, H = 2700, 2025
OUT = "/home/user/oqul-phase55-production/dentist-marketing-kit/4_ETSY_IMAGES"

DARK   = "#04162B"
MAIN   = "#0B3D6B"
ACCENT = "#1565C0"
LIGHT  = "#90CAF9"
CREAM  = "#F0F8FF"
GOLD   = "#FFB300"
WHITE  = "#FFFFFF"
BLACK  = "#000000"

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

def draw_wrapped_text(draw, text, x, y, font, color, max_width, line_spacing=10):
    """Wrap text within max_width, return bottom y."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        bb = draw.textbbox((0,0), test, font=font)
        if bb[2]-bb[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    cy = y
    for line in lines:
        draw.text((x, cy), line, font=font, fill=rgb(color))
        bb = draw.textbbox((0,0), line, font=font)
        cy += (bb[3]-bb[1]) + line_spacing
    return cy

def cx_wrapped(draw, text, y, font, color, max_width, margin=0, line_spacing=8):
    """Center-wrapped text."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        bb = draw.textbbox((0,0), test, font=font)
        if bb[2]-bb[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    cy = y
    for line in lines:
        bb = draw.textbbox((0,0), line, font=font)
        lw = bb[2]-bb[0]
        x = margin + (max_width - lw) // 2
        draw.text((x, cy), line, font=font, fill=rgb(color))
        cy += (bb[3]-bb[1]) + line_spacing
    return cy

# ─────────────────────────────────────────────────────────────────────────────
# 01_hero.jpg
# ─────────────────────────────────────────────────────────────────────────────
def make_01():
    img = Image.new("RGB", (W, H), rgb(DARK))
    draw = ImageDraw.Draw(img)

    # Border bars 12px ACCENT
    bw = 12
    draw.rectangle([0, 0, W-1, bw-1], fill=rgb(ACCENT))
    draw.rectangle([0, H-bw, W-1, H-1], fill=rgb(ACCENT))
    draw.rectangle([0, 0, bw-1, H-1], fill=rgb(ACCENT))
    draw.rectangle([W-bw, 0, W-1, H-1], fill=rgb(ACCENT))

    # Large title
    f_title = fnt("sb", 120)
    cx(draw, "DENTIST MARKETING KIT", 130, f_title, GOLD)

    # Subtitle
    f_sub = fnt("ar", 64)
    cx(draw, "The Complete Dental Practice Marketing System", 290, f_sub, CREAM)

    # Divider line
    pad = 120
    draw.rectangle([pad, 395, W-pad, 403], fill=rgb(ACCENT))

    # Info line
    f_info = fnt("ar", 52)
    cx(draw, "10 Professional Templates  •  Instant Digital Download", 430, f_info, LIGHT)

    # 6 preview boxes
    labels = ["365 Captions", "Patient Scripts", "Review System", "Reactivation", "Ad Copy", "Practice Guide"]
    box_w = 370
    box_h = 160
    gap = 28
    total_w = 6 * box_w + 5 * gap
    start_x = (W - total_w) // 2
    box_y = 560

    for i, label in enumerate(labels):
        bx = start_x + i * (box_w + gap)
        # Box background
        draw.rounded_rectangle([bx, box_y, bx+box_w, box_y+box_h], radius=14, fill=rgb(MAIN))
        draw.rounded_rectangle([bx, box_y, bx+box_w, box_y+box_h], radius=14, outline=rgb(ACCENT), width=3)
        # Label
        f_lbl = fnt("ab", 38)
        bb = draw.textbbox((0,0), label, font=f_lbl)
        tx = bx + (box_w - (bb[2]-bb[0])) // 2
        ty = box_y + (box_h - (bb[3]-bb[1])) // 2
        draw.text((tx, ty), label, font=f_lbl, fill=rgb(CREAM))

    # Large decorative content area below boxes
    content_y = box_y + box_h + 50
    # Three column feature area
    col_w = (W - 2*pad - 2*40) // 3
    f_feat_title = fnt("ab", 42)
    f_feat_body = fnt("ar", 34)

    features = [
        ("DONE-FOR-YOU CONTENT", "365 ready-to-post dental captions for every platform and every topic"),
        ("PATIENT COMMUNICATION", "Scripts for inquiries, consultations, reminders, and reactivation"),
        ("GROWTH SYSTEMS", "Review requests, ad copy, hashtag bank, and local marketing playbook"),
    ]

    for i, (title, body) in enumerate(features):
        fx = pad + i * (col_w + 40)
        fy = content_y
        # Feature card
        draw.rounded_rectangle([fx, fy, fx+col_w, fy+280], radius=12, fill=rgb(MAIN))
        draw.rounded_rectangle([fx, fy, fx+col_w, fy+4], radius=0, fill=rgb(GOLD))
        # Gold top accent
        draw.rectangle([fx, fy, fx+col_w, fy+6], fill=rgb(GOLD))
        # Title
        bb = draw.textbbox((0,0), title, font=f_feat_title)
        tx = fx + (col_w - (bb[2]-bb[0])) // 2
        draw.text((tx, fy+24), title, font=f_feat_title, fill=rgb(GOLD))
        # Body wrapped
        draw_wrapped_text(draw, body, fx+20, fy+90, f_feat_body, CREAM, col_w-40, line_spacing=8)

    # Bottom branding strip
    strip_y = H - 110
    draw.rectangle([0, strip_y, W, H], fill=rgb(MAIN))
    f_brand = fnt("ab", 44)
    cx(draw, "⭐ INSTANT DOWNLOAD  •  GOOGLE DOCS & CANVA COMPATIBLE  •  DENTISTS WORLDWIDE", strip_y+30, f_brand, GOLD)

    img.save(os.path.join(OUT, "01_hero.jpg"), "JPEG", quality=95)
    print("01_hero.jpg done")

# ─────────────────────────────────────────────────────────────────────────────
# 02_whats_inside.jpg
# ─────────────────────────────────────────────────────────────────────────────
def make_02():
    img = Image.new("RGB", (W, H), rgb(DARK))
    draw = ImageDraw.Draw(img)

    # Header bar ACCENT 180px
    draw.rectangle([0, 0, W, 180], fill=rgb(ACCENT))
    f_hdr = fnt("ab", 90)
    cx(draw, "WHAT'S INSIDE", 30, f_hdr, DARK)

    templates = [
        "365 Dental Practice Captions",
        "Patient Inquiry & Consultation Scripts",
        "Appointment Reminder Templates",
        "Review Request & Response System",
        "Patient Reactivation Scripts",
        "Social Media Ad Copy (10 ads)",
        "Hashtag Bank (200 hashtags)",
        "30-Day Content Calendar",
        "Local Marketing Playbook",
        "Dental Practice Business Systems Guide",
    ]

    # 2 columns
    col_w = (W - 120) // 2
    pad = 60
    row_h = 130
    start_y = 210
    f_item = fnt("ab", 46)
    f_badge = fnt("ab", 36)

    for i, tmpl in enumerate(templates):
        col = i % 2
        row = i // 2
        x = pad + col * (col_w + 0)
        y = start_y + row * (row_h + 18)

        # Card background
        card_x2 = x + col_w - 40
        draw.rounded_rectangle([x, y, card_x2, y+row_h], radius=10, fill=rgb(MAIN))

        # Gold badge (number)
        badge_r = 34
        bx = x + 24 + badge_r
        by = y + row_h//2
        draw.ellipse([bx-badge_r, by-badge_r, bx+badge_r, by+badge_r], fill=rgb(GOLD))
        num_str = str(i+1)
        bb = draw.textbbox((0,0), num_str, font=f_badge)
        nx = bx - (bb[2]-bb[0])//2
        ny = by - (bb[3]-bb[1])//2
        draw.text((nx, ny), num_str, font=f_badge, fill=rgb(DARK))

        # Template name (wrap if needed)
        text_x = x + 24 + badge_r*2 + 20
        avail_w = card_x2 - text_x - 20
        bb2 = draw.textbbox((0,0), tmpl, font=f_item)
        if (bb2[2]-bb2[0]) <= avail_w:
            ty2 = y + (row_h - (bb2[3]-bb2[1])) // 2
            draw.text((text_x, ty2), tmpl, font=f_item, fill=rgb(CREAM))
        else:
            # Use smaller font
            f_sm = fnt("ab", 38)
            bb2 = draw.textbbox((0,0), tmpl, font=f_sm)
            ty2 = y + (row_h - (bb2[3]-bb2[1])) // 2
            draw_wrapped_text(draw, tmpl, text_x, ty2, f_sm, CREAM, avail_w, line_spacing=4)

    # Bottom bar
    bottom_y = H - 110
    draw.rectangle([0, bottom_y, W, H], fill=rgb(ACCENT))
    f_bot = fnt("ab", 52)
    cx(draw, "Instant Download  •  Google Docs Compatible", bottom_y+28, f_bot, CREAM)

    img.save(os.path.join(OUT, "02_whats_inside.jpg"), "JPEG", quality=95)
    print("02_whats_inside.jpg done")

# ─────────────────────────────────────────────────────────────────────────────
# 03_content_preview.jpg
# ─────────────────────────────────────────────────────────────────────────────
def make_03():
    img = Image.new("RGB", (W, H), rgb(DARK))
    draw = ImageDraw.Draw(img)

    # Header
    f_hdr = fnt("sb", 96)
    cx(draw, "365 DENTAL CAPTIONS INCLUDED", 40, f_hdr, GOLD)

    # Divider
    draw.rectangle([100, 165, W-100, 171], fill=rgb(ACCENT))

    captions = [
        "Healthy teeth aren't just cosmetic. They're connected to your heart health, your confidence, and your quality of life.",
        "We saw 18 patients today. Every single one got the same level of attention and care. That's the standard we hold ourselves to.",
        "Teeth whitening question we get every week: is it safe? Yes — here's what actually happens to your enamel.",
        "We have 3 new patient slots open this week. If you've been putting off that appointment, now is the time.",
        "5-star review: 'I've never felt so comfortable at a dentist in my life.' This is what we work for every day.",
        "Poll: how often do you actually floss? Daily | Sometimes | Never (no judgment)",
    ]

    # 2x3 grid
    cols = 2
    rows = 3
    pad = 60
    gap_x = 40
    gap_y = 32
    card_w = (W - 2*pad - gap_x) // 2
    card_h = (H - 200 - 2*pad - 2*gap_y) // 3
    f_cap = fnt("ar", 36)
    f_num = fnt("ab", 32)

    for i, cap in enumerate(captions):
        col = i % cols
        row = i // cols
        cx2 = pad + col * (card_w + gap_x)
        cy2 = 200 + row * (card_h + gap_y)

        # Card
        draw.rounded_rectangle([cx2, cy2, cx2+card_w, cy2+card_h], radius=12, fill=rgb(MAIN))
        draw.rounded_rectangle([cx2, cy2, cx2+card_w, cy2+card_h], radius=12, outline=rgb(ACCENT), width=2)

        # Gold top accent strip
        draw.rectangle([cx2, cy2, cx2+card_w, cy2+6], fill=rgb(GOLD))

        # Caption number
        num_lbl = f"#{i+1}"
        draw.text((cx2+18, cy2+16), num_lbl, font=f_num, fill=rgb(GOLD))

        # Caption text
        draw_wrapped_text(draw, cap, cx2+18, cy2+65, f_cap, CREAM, card_w-36, line_spacing=8)

    img.save(os.path.join(OUT, "03_content_preview.jpg"), "JPEG", quality=95)
    print("03_content_preview.jpg done")

# ─────────────────────────────────────────────────────────────────────────────
# 04_system_feature.jpg
# ─────────────────────────────────────────────────────────────────────────────
def make_04():
    img = Image.new("RGB", (W, H), rgb(DARK))
    draw = ImageDraw.Draw(img)

    # Title
    f_title = fnt("sb", 88)
    cx(draw, "COMPLETE PATIENT REACTIVATION SYSTEM", 60, f_title, GOLD)

    # Subtitle
    f_sub = fnt("ar", 52)
    cx(draw, "Bring back lapsed patients with a proven multi-touch follow-up sequence", 185, f_sub, CREAM)

    # Divider
    draw.rectangle([100, 270, W-100, 278], fill=rgb(ACCENT))

    # Flow diagram
    steps = [
        ("IDENTIFY\nLAPSED", "Find patients\nmissed 12+ months"),
        ("FIRST\nOUTREACH", "Warm, personal\nreactivation script"),
        ("FOLLOW-UP", "2nd & 3rd touch\nreminder templates"),
        ("APPOINTMENT", "Confirmation &\npre-visit reminders"),
        ("RETENTION", "Post-visit review\nrequest system"),
    ]

    step_w = 380
    step_h = 360
    arrow_w = 80
    total_w = len(steps)*step_w + (len(steps)-1)*arrow_w
    sx = (W - total_w) // 2
    sy = 320

    f_step_title = fnt("ab", 40)
    f_step_body = fnt("ar", 30)

    for i, (title, body) in enumerate(steps):
        bx = sx + i*(step_w+arrow_w)

        # Step box
        draw.rounded_rectangle([bx, sy, bx+step_w, sy+step_h], radius=16, fill=rgb(MAIN))
        draw.rounded_rectangle([bx, sy, bx+step_w, sy+step_h], radius=16, outline=rgb(ACCENT), width=4)

        # Step number circle
        circ_r = 36
        cx3 = bx + step_w//2
        cy3 = sy + 50
        draw.ellipse([cx3-circ_r, cy3-circ_r, cx3+circ_r, cy3+circ_r], fill=rgb(GOLD))
        num = str(i+1)
        bb = draw.textbbox((0,0), num, font=f_step_title)
        draw.text((cx3-(bb[2]-bb[0])//2, cy3-(bb[3]-bb[1])//2), num, font=f_step_title, fill=rgb(DARK))

        # Title (multi-line)
        title_lines = title.split("\n")
        ty = sy + 110
        for ln in title_lines:
            bb2 = draw.textbbox((0,0), ln, font=f_step_title)
            lx2 = bx + (step_w-(bb2[2]-bb2[0]))//2
            draw.text((lx2, ty), ln, font=f_step_title, fill=rgb(CREAM))
            ty += (bb2[3]-bb2[1]) + 6

        # Body text
        body_lines = body.split("\n")
        by2 = ty + 20
        for ln in body_lines:
            bb3 = draw.textbbox((0,0), ln, font=f_step_body)
            lx3 = bx + (step_w-(bb3[2]-bb3[0]))//2
            draw.text((lx3, by2), ln, font=f_step_body, fill=rgb(LIGHT))
            by2 += (bb3[3]-bb3[1]) + 8

        # Arrow (not after last)
        if i < len(steps)-1:
            ax = bx + step_w + 10
            ay = sy + step_h//2
            # Arrow body
            draw.rectangle([ax, ay-6, ax+arrow_w-20, ay+6], fill=rgb(ACCENT))
            # Arrowhead
            draw.polygon([(ax+arrow_w-20, ay-18), (ax+arrow_w, ay), (ax+arrow_w-20, ay+18)], fill=rgb(ACCENT))

    # 3 Highlights
    highlights = [
        ("Reactivation Scripts", "Word-for-word outreach\nmessages that actually work"),
        ("Reminder Templates", "Email & text sequences\nfor every stage"),
        ("Review System", "Post-appointment review\nrequests built in"),
    ]

    hl_y = sy + step_h + 80
    hl_w = 720
    hl_h = 220
    hl_gap = 60
    total_hl_w = len(highlights)*hl_w + (len(highlights)-1)*hl_gap
    hl_x = (W - total_hl_w) // 2

    f_hl_title = fnt("ab", 46)
    f_hl_body = fnt("ar", 34)

    for i, (title, body) in enumerate(highlights):
        hx = hl_x + i*(hl_w + hl_gap)
        draw.rounded_rectangle([hx, hl_y, hx+hl_w, hl_y+hl_h], radius=12, fill=rgb(ACCENT))
        # Gold top strip
        draw.rectangle([hx, hl_y, hx+hl_w, hl_y+6], fill=rgb(GOLD))
        # Checkmark
        draw.text((hx+20, hl_y+16), "✓", font=f_hl_title, fill=rgb(GOLD))
        # Title
        bb = draw.textbbox((0,0), title, font=f_hl_title)
        tx = hx + (hl_w-(bb[2]-bb[0]))//2
        draw.text((tx, hl_y+16), title, font=f_hl_title, fill=rgb(DARK))
        # Body
        body_lines = body.split("\n")
        by3 = hl_y+80
        for ln in body_lines:
            bb2 = draw.textbbox((0,0), ln, font=f_hl_body)
            lx4 = hx + (hl_w-(bb2[2]-bb2[0]))//2
            draw.text((lx4, by3), ln, font=f_hl_body, fill=rgb(DARK))
            by3 += (bb2[3]-bb2[1]) + 6

    img.save(os.path.join(OUT, "04_system_feature.jpg"), "JPEG", quality=95)
    print("04_system_feature.jpg done")

# ─────────────────────────────────────────────────────────────────────────────
# 05_value_anchor.jpg
# ─────────────────────────────────────────────────────────────────────────────
def make_05():
    img = Image.new("RGB", (W, H), rgb(DARK))
    draw = ImageDraw.Draw(img)

    half = W // 2

    # LEFT panel — WITHOUT
    draw.rectangle([0, 0, half-4, H], fill=rgb(MAIN))
    # LEFT header
    f_panel_hdr = fnt("ab", 72)
    cx_panel = half // 2
    bb = draw.textbbox((0,0), "WITHOUT", font=f_panel_hdr)
    lx5 = cx_panel - (bb[2]-bb[0])//2
    draw.text((lx5, 60), "WITHOUT", font=f_panel_hdr, fill=rgb(LIGHT))

    # X symbol below
    f_x = fnt("ab", 120)
    bb2 = draw.textbbox((0,0), "✗", font=f_x)
    draw.text((cx_panel-(bb2[2]-bb2[0])//2, 150), "✗", font=f_x, fill=rgb("#CC3333"))

    struggles = [
        "No consistent posting schedule",
        "Reactive patient communication",
        "No systematic review strategy",
        "No patient reactivation plan",
        "Wasting hours creating content",
        "Losing patients to competitors",
    ]

    f_item = fnt("ar", 44)
    iy = 320
    for s in struggles:
        # Red X bullet
        draw.text((60, iy), "✗", font=f_item, fill=rgb("#FF4444"))
        draw.text((115, iy), s, font=f_item, fill=rgb(CREAM))
        bb3 = draw.textbbox((0,0), s, font=f_item)
        iy += (bb3[3]-bb3[1]) + 30

    # RIGHT panel — WITH
    draw.rectangle([half+4, 0, W, H], fill=rgb(ACCENT))
    # RIGHT header
    bb4 = draw.textbbox((0,0), "WITH", font=f_panel_hdr)
    rx5 = half + (half-(bb4[2]-bb4[0]))//2
    draw.text((rx5, 60), "WITH", font=f_panel_hdr, fill=rgb(DARK))

    # Check symbol
    bb5 = draw.textbbox((0,0), "✓", font=f_x)
    draw.text((half + half//2 - (bb5[2]-bb5[0])//2, 150), "✓", font=f_x, fill=rgb(GOLD))

    solutions = [
        "365 captions — always ready",
        "Complete patient scripts library",
        "Proven 5-star review system",
        "Ready-made reactivation templates",
        "Content done — just copy & post",
        "Professional marketing presence",
    ]

    iy2 = 320
    for s in solutions:
        draw.text((half+60, iy2), "✓", font=f_item, fill=rgb(GOLD))
        draw.text((half+115, iy2), s, font=f_item, fill=rgb(DARK))
        bb6 = draw.textbbox((0,0), s, font=f_item)
        iy2 += (bb6[3]-bb6[1]) + 30

    # Divider
    draw.rectangle([half-4, 0, half+4, H], fill=rgb(GOLD))

    # Bottom bar
    bot_y = H - 130
    draw.rectangle([0, bot_y, W, H], fill=rgb(DARK))
    draw.rectangle([0, bot_y, W, bot_y+4], fill=rgb(GOLD))
    f_bot = fnt("ab", 72)
    cx(draw, "10 Templates  •  $24  •  Instant Download", bot_y+28, f_bot, GOLD)

    img.save(os.path.join(OUT, "05_value_anchor.jpg"), "JPEG", quality=95)
    print("05_value_anchor.jpg done")

# ─────────────────────────────────────────────────────────────────────────────
# 06_before_after.jpg
# ─────────────────────────────────────────────────────────────────────────────
def make_06():
    img = Image.new("RGB", (W, H), rgb(DARK))
    draw = ImageDraw.Draw(img)

    # Top banner MAIN
    banner_h = 140
    draw.rectangle([0, 0, W, banner_h], fill=rgb(MAIN))
    f_banner = fnt("sb", 80)
    cx(draw, "FROM EMPTY CHAIR TO FULL SCHEDULE", 22, f_banner, GOLD)

    # Two panels
    half = W // 2
    panel_y = banner_h + 30
    panel_h = H - panel_y - 160

    # BEFORE panel
    draw.rounded_rectangle([40, panel_y, half-20, panel_y+panel_h], radius=16, fill=rgb(MAIN))
    draw.rectangle([40, panel_y, half-20, panel_y+70], fill=rgb("#8B0000"))
    f_ph = fnt("ab", 60)
    bb = draw.textbbox((0,0), "BEFORE", font=f_ph)
    draw.text((40 + (half-60-(bb[2]-bb[0]))//2, panel_y+8), "BEFORE", font=f_ph, fill=rgb(CREAM))

    before_items = [
        "Posting whenever you remember",
        "Scrambling for content ideas",
        "No system to follow up with patients",
        "Losing track of who needs reactivation",
        "Hoping for Google reviews",
        "Marketing feels overwhelming",
        "New patient pipeline is unpredictable",
        "Spending hours writing captions",
    ]
    f_bi = fnt("ar", 40)
    by4 = panel_y + 90
    for item in before_items:
        draw.text((70, by4), "✗", font=f_bi, fill=rgb("#FF5555"))
        draw.text((120, by4), item, font=f_bi, fill=rgb(LIGHT))
        bb2 = draw.textbbox((0,0), item, font=f_bi)
        by4 += (bb2[3]-bb2[1]) + 26

    # AFTER panel
    draw.rounded_rectangle([half+20, panel_y, W-40, panel_y+panel_h], radius=16, fill=rgb(ACCENT))
    draw.rectangle([half+20, panel_y, W-40, panel_y+70], fill=rgb(GOLD))
    bb3 = draw.textbbox((0,0), "AFTER", font=f_ph)
    draw.text((half+20 + (half-60-(bb3[2]-bb3[0]))//2, panel_y+8), "AFTER", font=f_ph, fill=rgb(DARK))

    after_items = [
        "365 captions ready to post anytime",
        "Never run out of content ideas again",
        "Automated patient follow-up system",
        "Reactivation scripts ready to send",
        "Review requests built into workflow",
        "Marketing is systematic and easy",
        "Consistent new patient flow",
        "Content done in minutes, not hours",
    ]
    ay = panel_y + 90
    for item in after_items:
        draw.text((half+50, ay), "✓", font=f_bi, fill=rgb(GOLD))
        draw.text((half+105, ay), item, font=f_bi, fill=rgb(DARK))
        bb4 = draw.textbbox((0,0), item, font=f_bi)
        ay += (bb4[3]-bb4[1]) + 26

    # Bottom
    bot_y = H - 130
    draw.rectangle([0, bot_y, W, H], fill=rgb(MAIN))
    draw.rectangle([0, bot_y, W, bot_y+4], fill=rgb(GOLD))
    f_bot = fnt("ab", 52)
    cx(draw, "Get the Dentist Marketing Kit — Instant Download — Start Today", bot_y+36, f_bot, CREAM)

    img.save(os.path.join(OUT, "06_before_after.jpg"), "JPEG", quality=95)
    print("06_before_after.jpg done")

# ─────────────────────────────────────────────────────────────────────────────
# 07_mockup.jpg
# ─────────────────────────────────────────────────────────────────────────────
def make_07():
    img = Image.new("RGB", (W, H), rgb(DARK))
    draw = ImageDraw.Draw(img)

    # Subtle grid background
    for gx in range(0, W, 80):
        draw.line([(gx, 0), (gx, H)], fill=rgb("#061A33"), width=1)
    for gy in range(0, H, 80):
        draw.line([(0, gy), (W, gy)], fill=rgb("#061A33"), width=1)

    # Laptop body
    lw, lh = 1800, 1050
    lx6 = (W - lw) // 2
    ly6 = 60

    # Laptop base
    base_h = 60
    base_y = ly6 + lh
    draw.rounded_rectangle([lx6-80, base_y, lx6+lw+80, base_y+base_h], radius=10, fill=rgb("#1A1A2E"))
    draw.rounded_rectangle([lx6-80, base_y, lx6+lw+80, base_y+base_h], radius=10, outline=rgb(ACCENT), width=3)
    # Hinge notch
    draw.rounded_rectangle([(W-200)//2, base_y-8, (W+200)//2, base_y+12], radius=6, fill=rgb("#0D0D1A"))

    # Laptop shell
    draw.rounded_rectangle([lx6, ly6, lx6+lw, ly6+lh], radius=18, fill=rgb("#0D1117"))
    draw.rounded_rectangle([lx6, ly6, lx6+lw, ly6+lh], radius=18, outline=rgb(ACCENT), width=10)

    # Screen bezel
    bezel = 40
    sx = lx6 + bezel
    sy = ly6 + bezel
    sw = lw - 2*bezel
    sh = lh - 2*bezel

    # Screen background
    draw.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=10, fill=rgb(CREAM))

    # Screen header bar
    draw.rectangle([sx, sy, sx+sw, sy+70], fill=rgb(MAIN))
    # Traffic light dots
    for ci, col in enumerate(["#FF5F56", "#FFBD2E", "#27C93F"]):
        draw.ellipse([sx+20+ci*36, sy+22, sx+20+ci*36+26, sy+48], fill=rgb(col))

    # Document title on screen
    f_doc_title = fnt("sb", 54)
    cx_screen_text = sx + sw//2
    bb = draw.textbbox((0,0), "Patient Reactivation Script", font=f_doc_title)
    draw.text((sx + (sw-(bb[2]-bb[0]))//2, sy+85), "Patient Reactivation Script", font=f_doc_title, fill=rgb(GOLD))

    # Divider under title
    draw.rectangle([sx+40, sy+155, sx+sw-40, sy+160], fill=rgb(ACCENT))

    # Simulated text lines
    f_line = fnt("ar", 30)
    line_texts = [
        "Subject: We Miss You at [Practice Name]!",
        "",
        "Hi [Patient First Name],",
        "",
        "We noticed it's been a while since your last visit and wanted to",
        "reach out personally. Your oral health is important to us, and we'd",
        "love to welcome you back.",
        "",
        "It's been [X months] since your last appointment, and regular",
        "check-ups are essential for catching small issues before they",
        "become bigger (and more costly) problems.",
        "",
        "[CTA Button: Book My Appointment]",
        "",
        "Warmly,",
        "[Dr. Name] & The Team at [Practice Name]",
    ]

    line_y = sy + 180
    for line in line_texts:
        if line:
            # Determine color based on content
            if line.startswith("[CTA"):
                draw.rounded_rectangle([sx+40, line_y-6, sx+sw-40, line_y+46], radius=8, fill=rgb(ACCENT))
                bb2 = draw.textbbox((0,0), line, font=f_line)
                draw.text((sx+40+(sw-80-(bb2[2]-bb2[0]))//2, line_y), line, font=f_line, fill=rgb(CREAM))
            elif line.startswith("Subject:") or line.startswith("Hi ") or line.startswith("Warmly"):
                draw.text((sx+40, line_y), line, font=f_line, fill=rgb(MAIN))
            else:
                draw.text((sx+40, line_y), line, font=f_line, fill=rgb("#333355"))
        line_y += 46

    # Below laptop text
    text_y = base_y + base_h + 50
    f_below = fnt("ar", 54)
    cx(draw, "Opens instantly in Google Docs, Notion, or Word", text_y, f_below, CREAM)

    # Compatibility icons row
    icon_y = text_y + 80
    icons = ["Google Docs", "Notion", "Microsoft Word", "Apple Pages"]
    f_icon = fnt("ab", 38)
    icon_total_w = sum(draw.textbbox((0,0), ic, font=f_icon)[2] for ic in icons) + len(icons)*60
    ix = (W - icon_total_w) // 2
    for ic in icons:
        bb3 = draw.textbbox((0,0), ic, font=f_icon)
        iw = bb3[2]-bb3[0]
        ih = bb3[3]-bb3[1]
        draw.rounded_rectangle([ix-10, icon_y-6, ix+iw+10, icon_y+ih+6], radius=8, fill=rgb(MAIN))
        draw.text((ix, icon_y), ic, font=f_icon, fill=rgb(LIGHT))
        ix += iw + 70

    # Bottom branding
    bot_y = H - 90
    draw.rectangle([0, bot_y, W, H], fill=rgb(MAIN))
    draw.rectangle([0, bot_y, W, bot_y+4], fill=rgb(ACCENT))
    f_brand = fnt("ab", 44)
    cx(draw, "DENTIST MARKETING KIT", bot_y+22, f_brand, ACCENT)

    img.save(os.path.join(OUT, "07_mockup.jpg"), "JPEG", quality=95)
    print("07_mockup.jpg done")

# ─────────────────────────────────────────────────────────────────────────────
# Run all
# ─────────────────────────────────────────────────────────────────────────────
os.makedirs(OUT, exist_ok=True)

make_01()
make_02()
make_03()
make_04()
make_05()
make_06()
make_07()

print("DONE")
