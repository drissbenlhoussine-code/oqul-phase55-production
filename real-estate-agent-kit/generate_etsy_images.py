#!/usr/bin/env python3
"""
Generate 7 Etsy listing images for Real Estate Agent Kit.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ── Constants ────────────────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/liberation"
OUT_DIR  = "/home/user/oqul-phase55-production/real-estate-agent-kit/4_ETSY_IMAGES"
W, H     = 2700, 2025
Q        = 95  # JPEG quality

# Palette
DARK   = "#0A1A0F"
MAIN   = "#1A3C34"
ACCENT = "#2E7D52"
LIGHT  = "#A9DFBF"
CREAM  = "#F0FFF4"
GOLD   = "#D4AC0D"

# ── Helpers ──────────────────────────────────────────────────────────────────
def fnt(n, s):
    f = {
        "sb": "LiberationSerif-Bold.ttf",
        "sr": "LiberationSerif-Regular.ttf",
        "ab": "LiberationSans-Bold.ttf",
        "ar": "LiberationSans-Regular.ttf",
    }
    return ImageFont.truetype(os.path.join(FONT_DIR, f[n]), s)

def rgb(h):
    if isinstance(h, tuple):
        return h
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def cx(draw, text, y, f, col, w=W):
    """Center text horizontally."""
    c  = rgb(col)
    bb = draw.textbbox((0, 0), text, font=f)
    x  = (w - (bb[2] - bb[0])) // 2
    draw.text((x, y), text, font=f, fill=c)

def lx(draw, text, x, y, f, col):
    draw.text((x, y), text, font=f, fill=rgb(col))

def text_h(draw, text, f):
    """Return rendered text height."""
    bb = draw.textbbox((0, 0), text, font=f)
    return bb[3] - bb[1]

def text_w(draw, text, f):
    bb = draw.textbbox((0, 0), text, font=f)
    return bb[2] - bb[0]

def wrap_text(draw, text, f, max_w):
    """Wrap text to fit within max_w pixels. Returns list of lines."""
    words  = text.split()
    lines  = []
    line   = ""
    for w in words:
        test = (line + " " + w).strip()
        if text_w(draw, test, f) <= max_w:
            line = test
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines

def draw_wrapped(draw, text, x, y, f, col, max_w, line_gap=8, center=False, canvas_w=W):
    """Draw wrapped text, return bottom y."""
    lines = wrap_text(draw, text, f, max_w)
    for ln in lines:
        if center:
            cx(draw, ln, y, f, col, canvas_w)
        else:
            lx(draw, ln, x, y, f, col)
        y += text_h(draw, ln, f) + line_gap
    return y

def hline(draw, y, col, thickness=4, margin=0):
    draw.rectangle([(margin, y), (W - margin, y + thickness)], fill=rgb(col))

def save(img, name):
    path = os.path.join(OUT_DIR, name)
    img.save(path, "JPEG", quality=Q)
    print(f"  Saved {name}")

def new_img(bg):
    img  = Image.new("RGB", (W, H), rgb(bg))
    draw = ImageDraw.Draw(img)
    return img, draw

def gold_border(draw, t=12):
    """4-side gold border."""
    c = rgb(GOLD)
    draw.rectangle([(0, 0), (W, t)],     fill=c)
    draw.rectangle([(0, H-t), (W, H)],   fill=c)
    draw.rectangle([(0, 0), (t, H)],     fill=c)
    draw.rectangle([(W-t, 0), (W, H)],   fill=c)

# ── 01 HERO ──────────────────────────────────────────────────────────────────
def make_01():
    img, draw = new_img(DARK)
    gold_border(draw, 12)

    # Decorative top strip
    draw.rectangle([(12, 12), (W-12, 80)], fill=rgb(MAIN))

    # Main title
    f_title = fnt("sb", 120)
    cx(draw, "REAL ESTATE AGENT KIT", 130, f_title, GOLD)

    # Subtitle
    f_sub = fnt("sr", 68)
    cx(draw, "The Complete Agent Business System", 278, f_sub, CREAM)

    # Divider
    hline(draw, 380, GOLD, 4, 200)

    # Tagline
    f_tag = fnt("ar", 52)
    cx(draw, "10 Professional Templates  •  Instant Digital Download", 410, f_tag, LIGHT)

    # Section label
    f_lbl = fnt("ab", 40)
    cx(draw, "EVERYTHING INCLUDED IN YOUR KIT:", 520, f_lbl, LIGHT)

    # Six preview boxes
    boxes = ["365 Captions", "Listing Scripts", "Lead Nurture",
             "Client Scripts", "Ad Copy", "Agent Guide"]
    n     = len(boxes)
    bw    = 360
    bh    = 260
    gap   = 36
    total = n * bw + (n-1) * gap
    sx    = (W - total) // 2
    by    = 640

    f_box  = fnt("ab", 38)
    f_box2 = fnt("ar", 32)

    icons = ["📋", "🎤", "📧", "💬", "📢", "📖"]
    # Map box label to two lines
    two_lines = {
        "365 Captions":   ("365", "Captions"),
        "Listing Scripts":("Listing", "Scripts"),
        "Lead Nurture":   ("Lead", "Nurture"),
        "Client Scripts": ("Client", "Scripts"),
        "Ad Copy":        ("Ad", "Copy"),
        "Agent Guide":    ("Agent", "Guide"),
    }

    for i, label in enumerate(boxes):
        x0 = sx + i * (bw + gap)
        y0 = by
        x1 = x0 + bw
        y1 = y0 + bh
        # Box background
        draw.rectangle([(x0, y0), (x1, y1)], fill=rgb(MAIN))
        # Gold top accent bar
        draw.rectangle([(x0, y0), (x1, y0+8)], fill=rgb(GOLD))
        # Number badge
        f_num = fnt("ab", 44)
        num_str = str(i+1)
        draw.ellipse([(x0+14, y0+18), (x0+64, y0+68)], fill=rgb(GOLD))
        nb = draw.textbbox((0,0), num_str, font=fnt("ab", 30))
        nx = x0+14 + (50-(nb[2]-nb[0]))//2
        ny = y0+18 + (50-(nb[3]-nb[1]))//2
        draw.text((nx, ny), num_str, font=fnt("ab", 30), fill=rgb(DARK))
        # Lines
        l1, l2 = two_lines[label]
        tw1 = text_w(draw, l1, f_box)
        tx1 = x0 + (bw - tw1) // 2
        draw.text((tx1, y0 + 80), l1, font=f_box, fill=rgb(CREAM))
        tw2 = text_w(draw, l2, f_box2)
        tx2 = x0 + (bw - tw2) // 2
        draw.text((tx2, y0 + 148), l2, font=f_box2, fill=rgb(LIGHT))
        # Bottom accent
        draw.rectangle([(x0, y1-8), (x1, y1)], fill=rgb(ACCENT))

    # Bottom decorative bar
    draw.rectangle([(0, H-110), (W, H-12)], fill=rgb(MAIN))
    f_bot = fnt("ar", 42)
    cx(draw, "Instant Digital Download  •  Google Docs & Notion Compatible", H-90, f_bot, GOLD)

    save(img, "01_hero.jpg")

# ── 02 WHAT'S INSIDE ─────────────────────────────────────────────────────────
def make_02():
    img, draw = new_img(DARK)

    # Header bar
    draw.rectangle([(0, 0), (W, 180)], fill=rgb(MAIN))
    draw.rectangle([(0, 0), (W, 8)],   fill=rgb(GOLD))
    f_hdr = fnt("ab", 90)
    cx(draw, "WHAT'S INSIDE", 44, f_hdr, GOLD)

    # Sub-header
    f_sub = fnt("ar", 46)
    cx(draw, "10 Professional Templates — Complete Agent Business System", 198, f_sub, LIGHT)
    hline(draw, 252, GOLD, 3, 100)

    # Template list — 2 columns
    templates = [
        "365 Real Estate Captions",
        "Listing Presentation Scripts",
        "Buyer & Seller Consultation Scripts",
        "Lead Nurture Email Sequences",
        "Open House Templates & Scripts",
        "Client Onboarding System",
        "Social Media Ad Copy (10 ads)",
        "Hashtag Bank (200 hashtags)",
        "30-Day Content Calendar",
        "Real Estate Business Systems Guide",
    ]

    f_num  = fnt("ab", 46)
    f_item = fnt("sb", 50)
    f_desc = fnt("ar", 36)

    col_w  = W // 2 - 100
    starts = [80, W // 2 + 40]
    row_h  = 148
    start_y = 280

    # Column headers
    draw.rectangle([(60, 268), (W//2 - 40, 288)], fill=rgb(ACCENT))
    draw.rectangle([(W//2+20, 268), (W-60, 288)], fill=rgb(ACCENT))

    for idx, tpl in enumerate(templates):
        col   = idx % 2
        row   = idx // 2
        x0    = starts[col]
        y0    = start_y + row * row_h + 20

        # Number badge
        badge_r = 34
        bx = x0
        by = y0 + 10
        draw.ellipse([(bx, by), (bx + badge_r*2, by + badge_r*2)], fill=rgb(GOLD))
        num_str = str(idx + 1)
        nb = draw.textbbox((0,0), num_str, font=fnt("ab", 34))
        nx = bx + (badge_r*2 - (nb[2]-nb[0])) // 2
        ny = by + (badge_r*2 - (nb[3]-nb[1])) // 2
        draw.text((nx, ny), num_str, font=fnt("ab", 34), fill=rgb(DARK))

        # Card background
        card_x0 = x0 + badge_r*2 + 16
        card_y0 = y0
        card_x1 = x0 + col_w
        card_y1 = y0 + row_h - 12
        draw.rectangle([(card_x0, card_y0), (card_x1, card_y1)],
                       fill=rgb(MAIN), outline=rgb(ACCENT), width=2)
        # Left accent bar
        draw.rectangle([(card_x0, card_y0), (card_x0+6, card_y1)], fill=rgb(GOLD))

        # Wrap template name
        avail_w = card_x1 - card_x0 - 30
        lines = wrap_text(draw, tpl, f_item, avail_w)
        ty = card_y0 + 14
        for ln in lines:
            lx(draw, ln, card_x0 + 20, ty, f_item, CREAM)
            ty += text_h(draw, ln, f_item) + 4

    # Bottom gold bar
    draw.rectangle([(0, H-100), (W, H)], fill=rgb(GOLD))
    f_bot = fnt("ab", 52)
    cx(draw, "Instant Download  •  Google Docs Compatible  •  Start Today", H-82, f_bot, DARK)

    save(img, "02_whats_inside.jpg")

# ── 03 CAPTION PREVIEW ───────────────────────────────────────────────────────
def make_03():
    img, draw = new_img(DARK)

    # Header
    draw.rectangle([(0, 0), (W, 8)], fill=rgb(GOLD))
    f_hdr = fnt("sb", 110)
    cx(draw, "365 REAL ESTATE CAPTIONS", 30, f_hdr, GOLD)

    f_sub = fnt("ar", 48)
    cx(draw, "Ready-to-post captions for every market condition", 162, f_sub, LIGHT)
    hline(draw, 228, GOLD, 4, 120)

    # 6 caption cards — 2 columns x 3 rows
    captions = [
        "Just listed: 4 bed, 3 bath in [Neighborhood]. Open Sunday 1–4pm. Comment below for the full details.",
        "The first offer came in 6 hours after listing. This is what happens when the price is right and the photos are done properly.",
        "Buyers: the market has shifted. Here's what that actually means for your offer strategy right now.",
        "Behind the listing: the staging consultation, the photographer walkthrough, the pricing conversation. What you see online took weeks.",
        "Thinking about selling in the next 6 months? Let's talk before you're ready — the prep work starts now.",
        "Poll: what's your biggest fear about buying a home right now? Money Prices | Rates | Inventory",
    ]

    labels = ["JUST LISTED", "MARKET INSIGHT", "BUYER TIP",
              "BEHIND THE SCENES", "SELLER LEAD", "ENGAGEMENT POLL"]

    n_cols = 2
    n_rows = 3
    margin = 70
    gap    = 40
    cw     = (W - 2*margin - gap) // 2
    ch     = (H - 260 - 2*margin - 2*gap) // 3
    start_y = 260

    f_label = fnt("ab", 32)
    f_cap   = fnt("ar", 36)
    f_num   = fnt("ab", 28)

    for i, (cap, label) in enumerate(zip(captions, labels)):
        col = i % n_cols
        row = i // n_cols
        x0  = margin + col * (cw + gap)
        y0  = start_y + row * (ch + gap)
        x1  = x0 + cw
        y1  = y0 + ch

        # Card
        draw.rectangle([(x0, y0), (x1, y1)], fill=rgb(MAIN))
        # Top bar with label
        draw.rectangle([(x0, y0), (x1, y0+52)], fill=rgb(ACCENT))
        # Label
        lbl_w = text_w(draw, label, f_label)
        draw.text((x0 + 16, y0 + 10), label, font=f_label, fill=rgb(GOLD))
        # Number
        num_str = f"#{i+1}"
        draw.text((x1 - text_w(draw, num_str, f_num) - 14, y0 + 14),
                  num_str, font=f_num, fill=rgb(LIGHT))
        # Gold left bar
        draw.rectangle([(x0, y0+52), (x0+5, y1)], fill=rgb(GOLD))

        # Caption text
        avail_w = cw - 30
        ty = y0 + 72
        lines = wrap_text(draw, cap, f_cap, avail_w)
        for ln in lines:
            if ty + text_h(draw, ln, f_cap) > y1 - 10:
                # Truncate
                draw.text((x0+18, ty), "…", font=f_cap, fill=rgb(LIGHT))
                break
            lx(draw, ln, x0 + 18, ty, f_cap, CREAM)
            ty += text_h(draw, ln, f_cap) + 8

    # Bottom bar
    draw.rectangle([(0, H-80), (W, H)], fill=rgb(MAIN))
    draw.rectangle([(0, H-80), (W, H-74)], fill=rgb(GOLD))
    f_bot = fnt("ar", 42)
    cx(draw, "All 365 captions included  •  Every market  •  Every season", H-68, f_bot, LIGHT)

    save(img, "03_content_preview.jpg")

# ── 04 LEAD NURTURE SYSTEM ───────────────────────────────────────────────────
def make_04():
    img, draw = new_img(DARK)

    # Top border
    draw.rectangle([(0, 0), (W, 10)], fill=rgb(GOLD))

    # Title block
    draw.rectangle([(0, 10), (W, 200)], fill=rgb(MAIN))
    f_title = fnt("ab", 100)
    cx(draw, "COMPLETE LEAD NURTURE SYSTEM", 46, f_title, GOLD)

    f_sub = fnt("ar", 50)
    cx(draw, "Turn cold leads into closed deals with proven scripts & sequences", 164, f_sub, LIGHT)

    hline(draw, 210, GOLD, 4, 80)

    # Flow diagram — 5 steps
    steps = [
        ("LEAD", "CAPTURED", "01"),
        ("FIRST", "CONTACT", "02"),
        ("FOLLOW-UP", "SEQUENCE", "03"),
        ("CONSULTATION", "BOOKED", "04"),
        ("DEAL", "CLOSED", "05"),
    ]

    n      = len(steps)
    bw     = 380
    bh     = 300
    gap    = 40
    total  = n * bw + (n-1) * gap
    sx     = (W - total) // 2
    sy     = 270

    f_sn   = fnt("ab", 36)
    f_sl1  = fnt("ab", 44)
    f_sl2  = fnt("ar", 38)
    f_step = fnt("ab", 28)

    for i, (l1, l2, num) in enumerate(steps):
        x0 = sx + i * (bw + gap)
        y0 = sy
        x1 = x0 + bw
        y1 = y0 + bh

        # Box
        fill_c = rgb(GOLD) if i == 4 else rgb(MAIN)
        text_c = DARK if i == 4 else CREAM
        draw.rectangle([(x0, y0), (x1, y1)], fill=fill_c)

        # Step number badge
        draw.ellipse([(x0 + bw//2 - 36, y0 + 20), (x0 + bw//2 + 36, y0 + 92)],
                     fill=rgb(DARK) if i == 4 else rgb(GOLD))
        nb = draw.textbbox((0,0), num, font=fnt("ab", 40))
        nx = x0 + bw//2 - (nb[2]-nb[0])//2
        ny = y0 + 20 + (72 - (nb[3]-nb[1]))//2
        num_col = GOLD if i == 4 else DARK
        draw.text((nx, ny), num, font=fnt("ab", 40), fill=rgb(num_col))

        # Lines
        tw1 = text_w(draw, l1, f_sl1)
        draw.text((x0 + (bw-tw1)//2, y0 + 108), l1,
                  font=f_sl1, fill=rgb(text_c))
        tw2 = text_w(draw, l2, f_sl2)
        draw.text((x0 + (bw-tw2)//2, y0 + 168), l2,
                  font=f_sl2, fill=rgb(text_c if i < 4 else MAIN))

        # Arrow between boxes
        if i < n-1:
            ax = x1 + gap // 2
            ay = y0 + bh // 2
            draw.polygon([(ax-16, ay-18), (ax+16, ay), (ax-16, ay+18)],
                         fill=rgb(GOLD))

    # Bottom description
    hline(draw, 608, ACCENT, 2, 80)

    desc_items = [
        ("What's Included:", "ab", 52, GOLD),
        ("", "ar", 10, DARK),
    ]

    f_desc_hdr = fnt("ab", 52)
    cx(draw, "What's Included in the Nurture System:", 638, f_desc_hdr, GOLD)

    # Three highlight boxes
    highlights = [
        ("BUYER\nSCRIPTS", "Scripts for every buyer stage\nfrom first call to closing"),
        ("SELLER\nSCRIPTS", "Listing presentation to\noffer negotiation scripts"),
        ("EMAIL\nSEQUENCES", "Multi-touch follow-up\nfor warm & cold leads"),
    ]

    hw     = 720
    hh     = 340
    hgap   = 60
    htotal = 3 * hw + 2 * hgap
    hsx    = (W - htotal) // 2
    hsy    = 720

    f_hl1  = fnt("ab", 54)
    f_hl2  = fnt("ar", 38)

    for i, (title, desc) in enumerate(highlights):
        x0 = hsx + i * (hw + hgap)
        y0 = hsy
        x1 = x0 + hw
        y1 = y0 + hh

        draw.rectangle([(x0, y0), (x1, y1)], fill=rgb(MAIN))
        draw.rectangle([(x0, y0), (x1, y0+8)], fill=rgb(GOLD))
        draw.rectangle([(x0, y1-8), (x1, y1)], fill=rgb(ACCENT))

        # Title
        for j, tl in enumerate(title.split("\n")):
            tw = text_w(draw, tl, f_hl1)
            draw.text((x0 + (hw-tw)//2, y0 + 28 + j*68), tl,
                      font=f_hl1, fill=rgb(GOLD))
        # Desc
        for j, dl in enumerate(desc.split("\n")):
            dw = text_w(draw, dl, f_hl2)
            draw.text((x0 + (hw-dw)//2, y0 + 190 + j*52), dl,
                      font=f_hl2, fill=rgb(CREAM))

    # Bottom bar
    draw.rectangle([(0, H-90), (W, H)], fill=rgb(MAIN))
    draw.rectangle([(0, H-90), (W, H-84)], fill=rgb(GOLD))
    f_bot = fnt("ab", 46)
    cx(draw, "Proven scripts used by top-producing agents nationwide", H-76, f_bot, LIGHT)

    save(img, "04_system_feature.jpg")

# ── 05 VALUE ANCHOR ──────────────────────────────────────────────────────────
def make_05():
    img, draw = new_img(DARK)

    # Split line
    draw.rectangle([(W//2 - 3, 0), (W//2 + 3, H-110)], fill=rgb(GOLD))

    # Left panel — WITHOUT
    draw.rectangle([(0, 0), (W//2-3, H-110)], fill=rgb(MAIN))

    # Left header
    draw.rectangle([(0, 0), (W//2-3, 160)], fill=rgb("#1a1a1a"))
    f_side = fnt("ab", 80)
    lw = text_w(draw, "WITHOUT", f_side)
    draw.text(((W//2-3-lw)//2, 44), "WITHOUT", font=f_side, fill=rgb("#CC3333"))

    # Left struggles
    struggles = [
        "Inconsistent follow-up with leads",
        "No proven listing script",
        "Generic, forgettable content",
        "Starting from scratch every time",
        "Losing deals to more prepared agents",
        "Hours writing captions that don't convert",
    ]
    f_item = fnt("ar", 44)
    ty = 200
    for s in struggles:
        # X mark
        draw.ellipse([(80, ty+2), (126, ty+48)], fill=rgb("#CC3333"))
        xf = fnt("ab", 32)
        draw.text((93, ty+6), "✗", font=xf, fill=rgb(CREAM))
        lines = wrap_text(draw, s, f_item, W//2 - 170)
        for ln in lines:
            lx(draw, ln, 148, ty, f_item, CREAM)
            ty += text_h(draw, ln, f_item) + 6
        ty += 30

    # Right panel — WITH
    draw.rectangle([(W//2+3, 0), (W, H-110)], fill=rgb(DARK))

    # Right header
    draw.rectangle([(W//2+3, 0), (W, 160)], fill=rgb(MAIN))
    rw = text_w(draw, "WITH THIS KIT", f_side)
    draw.text((W//2+3 + (W//2-3-rw)//2, 44), "WITH THIS KIT",
              font=f_side, fill=rgb(GOLD))

    # Right solutions
    solutions = [
        "Proven lead nurture that converts",
        "Professional listing scripts ready to use",
        "365 days of ready-to-post content",
        "Complete system from day one",
        "Show up prepared and close more deals",
        "Captions that attract and engage buyers",
    ]
    ty = 200
    for s in solutions:
        # Check mark
        draw.ellipse([(W//2 + 80, ty+2), (W//2 + 126, ty+48)], fill=rgb(ACCENT))
        draw.text((W//2 + 88, ty+6), "✓", font=fnt("ab", 32), fill=rgb(CREAM))
        lines = wrap_text(draw, s, f_item, W//2 - 170)
        for ln in lines:
            lx(draw, ln, W//2 + 148, ty, f_item, CREAM)
            ty += text_h(draw, ln, f_item) + 6
        ty += 30

    # Center VS badge
    draw.ellipse([(W//2-60, H//2-80), (W//2+60, H//2+40)],
                 fill=rgb(GOLD))
    f_vs = fnt("ab", 64)
    vsw  = text_w(draw, "VS", f_vs)
    draw.text((W//2 - vsw//2, H//2 - 58), "VS", font=f_vs, fill=rgb(DARK))

    # Bottom bar
    draw.rectangle([(0, H-110), (W, H)], fill=rgb(GOLD))
    f_bot = fnt("ab", 80)
    cx(draw, "10 Templates  •  $27  •  Instant Download", H-98, f_bot, DARK)

    save(img, "05_value_anchor.jpg")

# ── 06 BEFORE / AFTER ────────────────────────────────────────────────────────
def make_06():
    img, draw = new_img(DARK)

    # Top banner
    draw.rectangle([(0, 0), (W, 180)], fill=rgb(MAIN))
    draw.rectangle([(0, 0), (W, 10)], fill=rgb(GOLD))
    f_top = fnt("ab", 80)
    cx(draw, "FROM CHASING LEADS TO CLOSING DEALS", 54, f_top, GOLD)

    hline(draw, 188, GOLD, 4, 0)

    # Two panels
    pw = W // 2 - 60
    ph = H - 360

    # BEFORE panel
    bx0, by0 = 40, 220
    bx1, by1 = bx0 + pw, by0 + ph
    draw.rectangle([(bx0, by0), (bx1, by1)], fill=rgb(MAIN))
    draw.rectangle([(bx0, by0), (bx1, by0+10)], fill=rgb("#CC3333"))

    f_ph = fnt("ab", 68)
    cx(draw, "BEFORE", by0 + 30, f_ph, "#CC3333", pw)
    # adjust cx for left panel
    tw = text_w(draw, "BEFORE", f_ph)
    draw.text((bx0 + (pw - tw)//2, by0 + 30), "BEFORE", font=f_ph, fill=rgb("#CC3333"))

    befores = [
        "Winging every listing appointment",
        "Copy-pasting generic social posts",
        "Chasing leads with no system",
        "No consistent follow-up process",
        "Content that blends in with everyone else",
        "Starting each week without a plan",
    ]
    f_li = fnt("ar", 44)
    ty = by0 + 130
    for b in befores:
        draw.text((bx0+30, ty), "–", font=f_li, fill=rgb("#CC3333"))
        lines = wrap_text(draw, b, f_li, pw - 90)
        for ln in lines:
            draw.text((bx0+68, ty), ln, font=f_li, fill=rgb(CREAM))
            ty += text_h(draw, ln, f_li) + 8
        ty += 18

    # AFTER panel
    ax0 = W // 2 + 20
    ay0, ax1, ay1 = 220, ax0 + pw, by1
    draw.rectangle([(ax0, ay0), (ax1, ay1)], fill=rgb(MAIN))
    draw.rectangle([(ax0, ay0), (ax1, ay0+10)], fill=rgb(GOLD))

    tw2 = text_w(draw, "AFTER", f_ph)
    draw.text((ax0 + (pw - tw2)//2, ay0 + 30), "AFTER", font=f_ph, fill=rgb(GOLD))

    afters = [
        "Confident listing presentations every time",
        "365 days of professional captions ready",
        "Systematic lead nurture that converts",
        "Consistent multi-touch follow-up process",
        "Content that positions you as the expert",
        "Structured 30-day plan from day one",
    ]
    ty = ay0 + 130
    for a in afters:
        draw.text((ax0+30, ty), "✓", font=f_li, fill=rgb(GOLD))
        lines = wrap_text(draw, a, f_li, pw - 90)
        for ln in lines:
            draw.text((ax0+68, ty), ln, font=f_li, fill=rgb(CREAM))
            ty += text_h(draw, ln, f_li) + 8
        ty += 18

    # Divider
    draw.rectangle([(W//2-3, 220), (W//2+3, by1)], fill=rgb(GOLD))

    # Bottom bar
    draw.rectangle([(0, H-130), (W, H)], fill=rgb(MAIN))
    draw.rectangle([(0, H-130), (W, H-124)], fill=rgb(GOLD))
    f_bot1 = fnt("ab", 56)
    cx(draw, "The Real Estate Agent Kit gives you the system, scripts & content", H-118, f_bot1, LIGHT)
    f_bot2 = fnt("ab", 48)
    cx(draw, "to run a professional real estate business from day one.", H-58, f_bot2, CREAM)

    save(img, "06_before_after.jpg")

# ── 07 LAPTOP MOCKUP ─────────────────────────────────────────────────────────
def make_07():
    img, draw = new_img(DARK)

    # Background texture — subtle grid lines
    for y in range(0, H, 80):
        draw.rectangle([(0, y), (W, y+1)], fill=rgb("#0E2418"))
    for x in range(0, W, 80):
        draw.rectangle([(x, 0), (x+1, H)], fill=rgb("#0E2418"))

    # Title at top
    draw.rectangle([(0, 0), (W, 12)], fill=rgb(GOLD))
    f_title = fnt("ab", 72)
    cx(draw, "INSTANT DIGITAL DOWNLOAD", 28, f_title, GOLD)
    f_sub = fnt("ar", 48)
    cx(draw, "Open in Google Docs, Notion, or Microsoft Word", 116, f_sub, LIGHT)
    hline(draw, 178, GOLD, 3, 200)

    # ── Laptop body ──
    lw = 1800
    lh = 1100
    lx0 = (W - lw) // 2
    ly0 = 200
    lx1 = lx0 + lw
    ly1 = ly0 + lh

    # Outer laptop body (lid)
    draw.rounded_rectangle([(lx0, ly0), (lx1, ly1)], radius=40,
                            fill=rgb("#222222"), outline=rgb("#444444"), width=6)
    # GOLD screen bezel
    bezel = 28
    sx0, sy0 = lx0+bezel, ly0+bezel
    sx1, sy1 = lx1-bezel, ly1-60
    draw.rounded_rectangle([(sx0, sy0), (sx1, sy1)], radius=20,
                            fill=rgb(DARK), outline=rgb(GOLD), width=6)

    # Screen content area
    scx0, scy0 = sx0+12, sy0+12
    scx1, scy1 = sx1-12, sy1-12
    draw.rectangle([(scx0, scy0), (scx1, scy1)], fill=rgb(DARK))

    # Screen — document header bar
    doc_bar_h = 80
    draw.rectangle([(scx0, scy0), (scx1, scy0+doc_bar_h)], fill=rgb(MAIN))
    draw.rectangle([(scx0, scy0), (scx1, scy0+6)], fill=rgb(GOLD))

    f_doc_title = fnt("sb", 56)
    doc_t = "Listing Presentation Script"
    dtw = text_w(draw, doc_t, f_doc_title)
    draw.text(((scx0+scx1-dtw)//2, scy0 + 18), doc_t,
              font=f_doc_title, fill=rgb(GOLD))

    # Simulated document text lines
    f_sim = fnt("ar", 32)
    f_sim_b = fnt("ab", 32)

    doc_lines = [
        ("SECTION 1: THE INTRODUCTION", True),
        ("Open with a warm handshake and introduce yourself.", False),
        ("\"Hi, I'm [Your Name] with [Brokerage]. Thank you for having me today.\"", False),
        ("", False),
        ("SECTION 2: THE PRICE DISCUSSION", True),
        ("Review comparable properties in the neighborhood.", False),
        ("\"Based on recent sales data, the optimal pricing range is...\"", False),
        ("", False),
        ("SECTION 3: YOUR MARKETING PLAN", True),
        ("Present your professional photography and listing strategy.", False),
        ("\"Here's how I'll position your home to attract the right buyers...\"", False),
        ("", False),
        ("SECTION 4: HANDLING OBJECTIONS", True),
        ("\"I understand your concern about pricing. Let me show you the data.\"", False),
    ]

    ty = scy0 + doc_bar_h + 20
    line_h = 46
    for text, bold in doc_lines:
        if not text:
            ty += 14
            continue
        if ty + line_h > scy1 - 10:
            break
        f_use  = f_sim_b if bold else f_sim
        col_use = GOLD if bold else CREAM
        tw     = text_w(draw, text, f_use)
        # Truncate if too wide
        if tw > (scx1 - scx0 - 40):
            # wrap to one line, clip
            lines = wrap_text(draw, text, f_use, scx1 - scx0 - 40)
            text  = lines[0] + ("…" if len(lines) > 1 else "")
        draw.text((scx0 + 20, ty), text, font=f_use, fill=rgb(col_use))
        ty += line_h

    # Laptop base/hinge
    base_h = 50
    draw.rounded_rectangle([(lx0-30, ly1), (lx1+30, ly1+base_h)],
                            radius=8, fill=rgb("#1A1A1A"), outline=rgb("#333333"), width=4)
    # Trackpad
    tp_w, tp_h = 360, 26
    draw.rounded_rectangle([(W//2 - tp_w//2, ly1 + 10), (W//2 + tp_w//2, ly1+10+tp_h)],
                            radius=6, fill=rgb("#2A2A2A"), outline=rgb("#444444"), width=2)

    # Below laptop text
    by_start = ly1 + base_h + 44
    f_open = fnt("ar", 54)
    cx(draw, "Opens instantly in Google Docs, Notion, or Word", by_start, f_open, CREAM)

    f_kit = fnt("ab", 44)
    cx(draw, "REAL ESTATE AGENT KIT  •  10 TEMPLATES  •  $27  •  INSTANT DOWNLOAD",
       by_start + 80, f_kit, GOLD)

    # Bottom bar
    draw.rectangle([(0, H-8), (W, H)], fill=rgb(GOLD))

    save(img, "07_mockup.jpg")

# ── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Generating Etsy listing images …")
    make_01()
    make_02()
    make_03()
    make_04()
    make_05()
    make_06()
    make_07()
    print("\nAll 7 images generated successfully.")

if __name__ == "__main__":
    main()
