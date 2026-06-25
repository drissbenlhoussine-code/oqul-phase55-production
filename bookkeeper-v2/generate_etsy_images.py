"""
Etsy Listing Images — Bookkeeper Practice Launch System v3.0
10 premium SaaS-style images. Roboto fonts. Brand palette.
Size: 2700 x 1800 px (3:2 landscape)
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/etsy-images'
os.makedirs(OUT, exist_ok=True)

W, H = 2700, 1800

# ── Brand Palette ──────────────────────────────────────────────────────────────
NAVY    = (15, 23, 42)       # #0F172A
TEAL    = (15, 118, 110)     # #0F766E
TEAL_L  = (204, 251, 241)    # #CCFBF1 — teal 10%
TEAL_M  = (20, 184, 166)     # #14B8A6 — teal 60%
AMBER   = (217, 119, 6)      # #D97706
AMBER_L = (254, 243, 199)    # #FEF3C7
WHITE   = (255, 255, 255)
BG_SOFT = (248, 250, 252)    # #F8FAFC
RULE    = (226, 232, 240)    # #E2E8F0
MUTED   = (100, 116, 139)    # #64748B
NAVY_2  = (30, 41, 59)       # #1E293B
RED     = (239, 68, 68)      # alert red
GREEN   = (34, 197, 94)      # success green
PURPLE  = (139, 92, 246)     # purple accent

# ── Fonts ──────────────────────────────────────────────────────────────────────
_RB  = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Black.ttf'
_RBo = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Bold.ttf'
_RM  = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Medium.ttf'
_RR  = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf'
_RL  = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Light.ttf'
_RCB = '/usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Bold.ttf'

def fnt(path, size): return ImageFont.truetype(path, size)


# ── Drawing Helpers ─────────────────────────────────────────────────────────────

def new_img():
    img = Image.new('RGB', (W, H), WHITE)
    return img, ImageDraw.Draw(img)


def rr(d, xy, r, fill, outline=None, width=1):
    """Rounded rectangle."""
    x0, y0, x1, y1 = xy
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=fill,
                        outline=outline, width=width)


def shadow_card(img, xy, r, fill, shadow_offset=6, shadow_alpha=30):
    """Card with subtle drop shadow using alpha compositing."""
    x0, y0, x1, y1 = xy
    # shadow
    shad = Image.new('RGBA', (W, H), (0,0,0,0))
    sd = ImageDraw.Draw(shad)
    sd.rounded_rectangle([x0+shadow_offset, y0+shadow_offset,
                          x1+shadow_offset, y1+shadow_offset],
                         radius=r, fill=(0,0,0,shadow_alpha))
    img_rgba = img.convert('RGBA')
    img_rgba = Image.alpha_composite(img_rgba, shad)
    img2 = img_rgba.convert('RGB')
    d2 = ImageDraw.Draw(img2)
    rr(d2, xy, r, fill, outline=RULE, width=1)
    return img2, d2


def text_c(d, xy, text, font, fill, anchor='mm'):
    """Centered text at point."""
    d.text(xy, text, font=font, fill=fill, anchor=anchor)


def text_lm(d, xy, text, font, fill):
    """Left-middle aligned text."""
    d.text(xy, text, font=font, fill=fill, anchor='lm')


def bar_chart(d, x, y, w, h, data, color=TEAL, bg=BG_SOFT, label=True):
    """Simple bar chart. data = list of (label, value 0-100)."""
    n = len(data)
    bar_w = (w - 20) // n - 8
    max_h = h - 40
    rr(d, [x, y, x+w, y+h], 8, bg)
    for i, (lbl, val) in enumerate(data):
        bx = x + 10 + i * (bar_w + 8)
        bh = int(max_h * val / 100)
        by = y + h - 35 - bh
        rr(d, [bx, by, bx+bar_w, y+h-35], 4, color)
        if label:
            d.text((bx + bar_w//2, y+h-18), lbl,
                   font=fnt(_RR, 22), fill=MUTED, anchor='mm')


def mini_line_chart(d, x, y, w, h, points, color=TEAL, fill_color=None):
    """Sparkline. points = list of 0-100 values."""
    if len(points) < 2: return
    pw = w / (len(points) - 1)
    coords = [(x + i*pw, y + h - (h * p/100)) for i, p in enumerate(points)]
    if fill_color:
        poly = list(coords) + [(x+w, y+h), (x, y+h)]
        d.polygon(poly, fill=fill_color)
    d.line(coords, fill=color, width=4)
    for cx, cy in coords:
        d.ellipse([cx-5, cy-5, cx+5, cy+5], fill=color)


def status_pill(d, cx, cy, text, color, text_color=WHITE):
    tw = len(text) * 16 + 28
    d.rounded_rectangle([cx - tw//2, cy-16, cx + tw//2, cy+16],
                        radius=12, fill=color)
    d.text((cx, cy), text, font=fnt(_RM, 26), fill=text_color, anchor='mm')


def teal_badge(d, x, y, text, w_=None):
    tw = w_ or (len(text)*18 + 32)
    d.rounded_rectangle([x, y, x+tw, y+46], radius=8, fill=TEAL)
    d.text((x+tw//2, y+23), text, font=fnt(_RCB, 26), fill=WHITE, anchor='mm')
    return tw


def check_badge(d, x, y, text):
    """✔ Check badge in teal-tinted style."""
    d.ellipse([x, y, x+40, y+40], fill=TEAL)
    d.text((x+20, y+20), '✓', font=fnt(_RBo, 26), fill=WHITE, anchor='mm')
    d.text((x+54, y+20), text, font=fnt(_RM, 28), fill=NAVY, anchor='lm')


def section_label(d, x, y, text):
    """Small teal uppercase label."""
    d.text((x, y), text.upper(), font=fnt(_RCB, 26), fill=TEAL, anchor='lt')


def kpi_card(d, img, x, y, w, h, label, value, sub='', color=TEAL):
    """KPI stat card."""
    img, d = shadow_card(img, [x, y, x+w, y+h], 12, WHITE)
    d.rounded_rectangle([x, y, x+w, y+6], radius=0, fill=color)
    d.text((x+24, y+40), label, font=fnt(_RM, 26), fill=MUTED, anchor='lt')
    d.text((x+24, y+78), value, font=fnt(_RB, 64), fill=NAVY, anchor='lt')
    if sub:
        d.text((x+24, y+h-30), sub, font=fnt(_RR, 24), fill=MUTED, anchor='lt')
    return img, d


def laptop_mockup(d, x, y, w):
    """Simplified laptop wireframe drawing."""
    sw = w
    sh = int(w * 0.58)
    # Base
    bh = int(w * 0.04)
    bw = int(w * 1.1)
    bx = x - int(w * 0.05)
    by = y + sh + 4
    # Screen frame
    rr(d, [x, y, x+sw, y+sh], 12, NAVY_2)
    rr(d, [x+8, y+8, x+sw-8, y+sh-8], 8, (20,30,50))
    # Screen (inner white area)
    rr(d, [x+14, y+14, x+sw-14, y+sh-14], 6, (245,248,252))
    # Notch
    d.ellipse([x+sw//2-16, y-8, x+sw//2+16, y+8], fill=NAVY_2)
    # Base / keyboard
    rr(d, [bx, by, bx+bw, by+bh], 4, NAVY_2)
    return x+14, y+14, sw-28, sh-28  # screen coords


def tablet_mockup(d, x, y, w, h=None):
    """Tablet wireframe."""
    if h is None: h = int(w * 1.35)
    rr(d, [x, y, x+w, y+h], 18, NAVY_2)
    rr(d, [x+8, y+8, x+w-8, y+h-8], 14, (20,30,50))
    rr(d, [x+14, y+14, x+w-14, y+h-14], 10, BG_SOFT)
    d.ellipse([x+w//2-10, y+h-18, x+w//2+10, y+h-6], fill=(40,50,70))
    return x+14, y+14, w-28, h-28


def phone_mockup(d, x, y, w, h=None):
    """Phone wireframe."""
    if h is None: h = int(w * 2.1)
    rr(d, [x, y, x+w, y+h], 28, NAVY_2)
    rr(d, [x+5, y+5, x+w-5, y+h-5], 22, (20,30,50))
    rr(d, [x+10, y+10, x+w-10, y+h-10], 18, BG_SOFT)
    d.ellipse([x+w//2-20, y+6, x+w//2+20, y+22], fill=(40,50,70))
    d.ellipse([x+w//2-8, y+8, x+w//2+8, y+20], fill=(60,70,90))
    d.ellipse([x+w//2-30, y+h-26, x+w//2+30, y+h-8], fill=(40,50,70))
    return x+10, y+40, w-20, h-60


def notion_sidebar(d, x, y, w, h, items):
    """Notion-style dark sidebar."""
    rr(d, [x, y, x+w, y+h], 8, (25, 30, 45))
    d.text((x+20, y+24), 'Bookkeeping Practice', font=fnt(_RBo, 26), fill=WHITE, anchor='lt')
    d.line([x+12, y+60, x+w-12, y+60], fill=(50,60,80), width=1)
    icons = ['📊', '👥', '📋', '📁', '💰', '✅', '📅', '🔔']
    for i, item in enumerate(items):
        iy = y + 76 + i * 52
        ic = icons[i % len(icons)]
        is_active = i == 0
        if is_active:
            rr(d, [x+8, iy-4, x+w-8, iy+44], 6, TEAL)
            d.text((x+22, iy+18), f'{ic}  {item}', font=fnt(_RM, 26), fill=WHITE, anchor='lm')
        else:
            d.text((x+22, iy+18), f'   {item}', font=fnt(_RR, 26), fill=(180,190,210), anchor='lm')


def table_rows(d, x, y, w, row_h, headers, rows, col_ws=None):
    """Mini consulting table."""
    n = len(headers)
    if col_ws is None:
        col_ws = [w // n] * n
    # Header
    rr(d, [x, y, x+w, y+row_h], 0, TEAL)
    cx = x
    for i, h_txt in enumerate(headers):
        d.text((cx+12, y+row_h//2), h_txt, font=fnt(_RBo, 24), fill=WHITE, anchor='lm')
        cx += col_ws[i]
    # Data rows
    for ri, row in enumerate(rows):
        ry = y + row_h + ri * row_h
        bg = BG_SOFT if ri % 2 == 0 else WHITE
        d.rectangle([x, ry, x+w, ry+row_h], fill=bg)
        d.line([x, ry, x+w, ry], fill=RULE, width=1)
        cx = x
        for ci, cell in enumerate(row):
            color = MUTED if ci == 0 else NAVY
            f = fnt(_RBo, 24) if ci == 0 else fnt(_RR, 24)
            d.text((cx+12, ry+row_h//2), str(cell), font=f, fill=color, anchor='lm')
            cx += col_ws[ci]
    d.rectangle([x, y, x+w, y+row_h+len(rows)*row_h], outline=RULE, width=1)


def progress_bar(d, x, y, w, h, pct, color=TEAL, bg=RULE):
    rr(d, [x, y, x+w, y+h], h//2, bg)
    pw = int(w * pct)
    if pw > h:
        rr(d, [x, y, x+pw, y+h], h//2, color)


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 01 — HERO
# ══════════════════════════════════════════════════════════════════════════════

def img01_hero():
    img = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # --- Left panel: dark navy brand strip ---
    rr(d, [0, 0, 780, H], 0, NAVY)

    # NovaOps wordmark
    d.text((60, 60), 'NOVAOPS', font=fnt(_RB, 44), fill=TEAL, anchor='lt')
    d.text((60, 114), 'BOOKKEEPER PRACTICE LAUNCH SYSTEM', font=fnt(_RCB, 22), fill=MUTED, anchor='lt')

    # Teal divider rule
    d.line([60, 148, 720, 148], fill=TEAL, width=2)

    # Main headline
    d.text((60, 185), 'Run Your', font=fnt(_RB, 108), fill=WHITE, anchor='lt')
    d.text((60, 297), 'Bookkeeping', font=fnt(_RB, 108), fill=TEAL, anchor='lt')
    d.text((60, 409), 'Business Like', font=fnt(_RB, 108), fill=WHITE, anchor='lt')
    d.text((60, 521), 'a Professional', font=fnt(_RB, 108), fill=WHITE, anchor='lt')

    # Subtitle
    d.text((60, 660), 'The complete business operating', font=fnt(_RL, 42), fill=(160,180,200), anchor='lt')
    d.text((60, 710), 'system for modern bookkeepers.', font=fnt(_RL, 42), fill=(160,180,200), anchor='lt')

    # Divider
    d.line([60, 774, 720, 774], fill=(40,55,80), width=1)

    # Check badges
    checks = [
        '30+ Premium Templates',
        'Excel Practice Dashboard',
        'Notion Workspace (7 DBs)',
        'SOPs + Checklists',
        'Instant Download',
        'Lifetime Access',
    ]
    for i, c in enumerate(checks):
        iy = 800 + i*76
        d.ellipse([60, iy, 102, iy+42], fill=TEAL)
        d.text((81, iy+21), '✓', font=fnt(_RBo, 28), fill=WHITE, anchor='mm')
        d.text((118, iy+21), c, font=fnt(_RM, 32), fill=WHITE, anchor='lm')

    # Version badge
    rr(d, [60, H-130, 400, H-72], 8, AMBER)
    d.text((230, H-101), 'VERSION 3.0  ·  PREMIUM EDITION', font=fnt(_RCB, 28), fill=WHITE, anchor='mm')

    # --- Right panel: laptop + floating elements ---
    # Large laptop mockup (center-right)
    lx, ly, lw, lh_ = laptop_mockup(d, 850, 140, 1300)

    # Dashboard UI inside laptop screen
    d2 = ImageDraw.Draw(img)
    # Dashboard header bar
    d2.rectangle([lx, ly, lx+lw, ly+52], fill=NAVY)
    d2.text((lx+20, ly+26), 'NOVAOPS  ·  Practice Dashboard', font=fnt(_RBo, 26), fill=WHITE, anchor='lm')
    d2.text((lx+lw-20, ly+26), '● Active', font=fnt(_RR, 22), fill=GREEN, anchor='rm')

    # KPI row
    kpi_y = ly+62
    kpis = [('MRR', '€12,400', '+8%'), ('Clients', '18', 'Active'), ('Pipeline', '€6,200', '4 leads'), ('Close Rate', '78%', 'This month')]
    kw = lw // 4 - 6
    for i, (lbl, val, sub) in enumerate(kpis):
        kx = lx + 4 + i*(kw+4)
        rr(d2, [kx, kpi_y, kx+kw, kpi_y+90], 6, BG_SOFT, outline=RULE, width=1)
        d2.rectangle([kx, kpi_y, kx+kw, kpi_y+4], fill=TEAL)
        d2.text((kx+10, kpi_y+18), lbl, font=fnt(_RM, 18), fill=MUTED, anchor='lt')
        d2.text((kx+10, kpi_y+38), val, font=fnt(_RBo, 32), fill=NAVY, anchor='lt')
        c_ = GREEN if '+' in sub else MUTED
        d2.text((kx+10, kpi_y+76), sub, font=fnt(_RR, 18), fill=c_, anchor='lt')

    # Revenue bar chart
    chart_x, chart_y = lx+4, kpi_y+100
    chart_w = int(lw*0.58)
    rr(d2, [chart_x, chart_y, chart_x+chart_w, chart_y+200], 6, BG_SOFT)
    d2.text((chart_x+12, chart_y+12), 'Monthly Revenue', font=fnt(_RBo, 22), fill=NAVY, anchor='lt')
    months = ['Jan','Feb','Mar','Apr','May','Jun']
    vals = [72,65,80,75,88,100]
    bw2 = (chart_w-40) // 6 - 6
    for i, (m, v) in enumerate(zip(months, vals)):
        bx2 = chart_x+20+i*(bw2+6)
        bh2 = int(140*v/100)
        rr(d2, [bx2, chart_y+190-bh2, bx2+bw2, chart_y+190], 3, TEAL if i<5 else AMBER)
        d2.text((bx2+bw2//2, chart_y+196+6), m, font=fnt(_RR,18), fill=MUTED, anchor='mt')

    # Client table right side
    tbl_x = chart_x + chart_w + 8
    tbl_w = lw - chart_w - 16
    rr(d2, [tbl_x, chart_y, tbl_x+tbl_w, chart_y+200], 6, BG_SOFT)
    d2.text((tbl_x+12, chart_y+12), 'Client CRM', font=fnt(_RBo, 22), fill=NAVY, anchor='lt')
    clients = [('Acme Ltd', 'Active', '€900'), ('Brio Co', 'Active', '€1,200'), ('Finova', 'Active', '€750'), ('EasyPay', 'Review', '€650')]
    for i, (n, s, f) in enumerate(clients):
        cy2 = chart_y + 46 + i*36
        bg2 = WHITE if i%2==0 else BG_SOFT
        d2.rectangle([tbl_x+4, cy2, tbl_x+tbl_w-4, cy2+34], fill=bg2)
        d2.text((tbl_x+10, cy2+17), n, font=fnt(_RM, 22), fill=NAVY, anchor='lm')
        c2 = GREEN if s=='Active' else AMBER
        rr(d2, [tbl_x+tbl_w//2, cy2+8, tbl_x+tbl_w//2+80, cy2+26], 8, c2)
        d2.text((tbl_x+tbl_w//2+40, cy2+17), s, font=fnt(_RR,18), fill=WHITE, anchor='mm')
        d2.text((tbl_x+tbl_w-10, cy2+17), f, font=fnt(_RBo,22), fill=TEAL, anchor='rm')

    # Monthly close below
    close_y = chart_y + 210
    rr(d2, [lx+4, close_y, lx+lw-4, close_y+110], 6, BG_SOFT)
    d2.text((lx+16, close_y+12), 'Monthly Close — June 2025', font=fnt(_RBo, 22), fill=NAVY, anchor='lt')
    close_steps = [('Reconciliation', 100), ('Categorisation', 100), ('Review', 80), ('Adjustments', 60), ('Reporting', 30)]
    for i, (step, pct) in enumerate(close_steps):
        sx = lx + 16 + i * ((lw-32)//5)
        sw = (lw-32)//5 - 8
        d2.text((sx, close_y+38), step, font=fnt(_RR,18), fill=MUTED, anchor='lt')
        progress_bar(d2, sx, close_y+62, sw, 14, pct/100,
                     color=GREEN if pct==100 else TEAL if pct>50 else AMBER)
        d2.text((sx+sw//2, close_y+88), f'{pct}%', font=fnt(_RBo,18), fill=NAVY, anchor='mm')

    # --- Floating tablet (top right) ---
    tx, ty, tw_, th_ = tablet_mockup(d, 2220, 60, 300)
    d.text((tx+tw_//2, ty+20), 'Clients', font=fnt(_RBo, 20), fill=NAVY, anchor='mm')
    d.line([tx, ty+36, tx+tw_, ty+36], fill=RULE, width=1)
    cl = [('Acme Ltd','Active'),('Brio Co','Active'),('Finova','Review')]
    for i,(n,s) in enumerate(cl):
        cy3 = ty+50+i*40
        d.text((tx+8,cy3+10), n, font=fnt(_RR,18), fill=NAVY, anchor='lt')
        c3 = GREEN if s=='Active' else AMBER
        rr(d, [tx+tw_-55,cy3+4,tx+tw_-5,cy3+24], 8, c3)
        d.text((tx+tw_-30,cy3+14), s, font=fnt(_RR,14), fill=WHITE, anchor='mm')

    # --- Floating phone (right side) ---
    px, py, pw_, ph_ = phone_mockup(d, 2260, 440, 240)
    d.text((px+pw_//2, py+20), 'Invoice #042', font=fnt(_RBo,20), fill=NAVY, anchor='mm')
    d.line([px, py+38, px+pw_, py+38], fill=RULE, width=1)
    d.text((px+10, py+58), 'Brio Co Ltd', font=fnt(_RM,22), fill=NAVY, anchor='lt')
    d.text((px+pw_//2, py+90), '€1,200.00', font=fnt(_RB,32), fill=TEAL, anchor='mm')
    rr(d, [px+20, py+130, px+pw_-20, py+162], 10, GREEN)
    d.text((px+pw_//2, py+146), 'PAID', font=fnt(_RCB,22), fill=WHITE, anchor='mm')
    d.text((px+10, py+175), 'Due: 15 Jun', font=fnt(_RR,18), fill=MUTED, anchor='lt')
    d.text((px+10, py+200), 'Method: Transfer', font=fnt(_RR,18), fill=MUTED, anchor='lt')

    # Bottom bar
    d.rectangle([0, H-80, W, H], fill=NAVY)
    d.text((40, H-40), 'BOOKKEEPER PRACTICE LAUNCH SYSTEM  ·  v3.0  ·  NOVAOPS', font=fnt(_RCB, 26), fill=TEAL, anchor='lm')
    d.text((W-40, H-40), 'Instant Download  ·  Lifetime Access', font=fnt(_RR, 26), fill=MUTED, anchor='rm')

    img.save(f'{OUT}/01-Hero.jpg', quality=95)
    print('  ✓ 01-Hero.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 02 — EVERYTHING INCLUDED
# ══════════════════════════════════════════════════════════════════════════════

def img02_included():
    img = Image.new('RGB', (W, H), BG_SOFT)
    d = ImageDraw.Draw(img)

    # Header strip
    d.rectangle([0, 0, W, 140], fill=NAVY)
    d.text((W//2, 48), 'EVERYTHING INCLUDED', font=fnt(_RCB, 40), fill=TEAL, anchor='mm')
    d.text((W//2, 96), 'One purchase. Every tool your bookkeeping practice needs — ready to use today.', font=fnt(_RM, 28), fill=(160,180,210), anchor='mm')

    # 6 category cards in 3×2 grid
    categories = [
        ('📊', 'Practice Dashboard', 'EXCEL', [
            '10-sheet Excel workbook',
            'KPI Dashboard',
            'Client CRM tracker',
            'Lead Pipeline',
            'Invoice Tracker',
            'Pricing Calculator',
        ], TEAL),
        ('📋', 'Client Documents', 'DOCX + PPTX', [
            'Service Guide (5 tiers)',
            'Proposal Template',
            'Engagement Agreement',
            'Onboarding Pack',
            '10-slide Proposal Deck',
        ], AMBER),
        ('⚙️', 'Operations Library', 'DOCX', [
            'SOPs & Checklists (4)',
            'Client Scripts (10)',
            'Tax Prep Checklist',
            'Monthly Close SOP',
            'QC Framework',
        ], PURPLE),
        ('🗂️', 'Notion Workspace', '7 DATABASES', [
            'Clients CRM',
            'Lead Pipeline',
            'Monthly Close',
            'Document Requests',
            'Invoice Register',
            'Tasks + Client Portal',
        ], TEAL_M),
        ('📄', 'PDF Guides', '9 DOCUMENTS', [
            'Read Me First',
            'Installation Guide',
            'Asset Manifest',
            'License Agreement',
            'FAQ (16 questions)',
            'Notion Setup Guide',
        ], TEAL),
        ('🚀', 'Support + Extras', 'BONUS', [
            'Version History',
            'Support Guide',
            'QA Report (91/100)',
            'Lifetime Updates',
            'Commercial License',
        ], AMBER),
    ]

    card_w = 820
    card_h = 720
    pad_x = (W - 3*card_w) // 4
    pad_y = 180

    for ci, (icon, title, badge, items, color) in enumerate(categories):
        col = ci % 3
        row = ci // 3
        cx = pad_x + col*(card_w + pad_x)
        cy = pad_y + row*(card_h + 28)

        # Card shadow + base
        img, d = shadow_card(img, [cx, cy, cx+card_w, cy+card_h], 16, WHITE)

        # Top color accent
        d.rounded_rectangle([cx, cy, cx+card_w, cy+8], radius=4, fill=color)

        # Icon area
        rr(d, [cx+24, cy+30, cx+92, cy+98], 16, (*color, 30) if isinstance(color[0], int) else color)
        d.text((cx+58, cy+64), icon, font=fnt(_RR, 44), fill=color, anchor='mm')

        # Badge
        badge_w = len(badge)*14 + 28
        rr(d, [cx+card_w-badge_w-16, cy+24, cx+card_w-16, cy+54], 8, color)
        d.text((cx+card_w-badge_w//2-28, cy+39), badge, font=fnt(_RCB, 22), fill=WHITE, anchor='mm')

        # Title
        d.text((cx+108, cy+44), title, font=fnt(_RBo, 40), fill=NAVY, anchor='lm')
        d.text((cx+108, cy+82), f'{len(items)} assets included', font=fnt(_RR, 26), fill=MUTED, anchor='lm')

        # Divider
        d.line([cx+24, cy+112, cx+card_w-24, cy+112], fill=RULE, width=1)

        # Items
        for ii, item in enumerate(items):
            iy = cy + 132 + ii*86
            d.ellipse([cx+28, iy+8, cx+52, iy+32], fill=TEAL_L)
            d.text((cx+40, iy+20), '✓', font=fnt(_RBo, 20), fill=TEAL, anchor='mm')
            d.text((cx+66, iy+20), item, font=fnt(_RM, 30), fill=NAVY, anchor='lm')

    # Footer bar
    d.rectangle([0, H-80, W, H], fill=NAVY)
    d.text((W//2, H-40), '33 FILES  ·  5 FOLDERS  ·  BOOKKEEPER PRACTICE LAUNCH SYSTEM v3.0  ·  NOVAOPS', font=fnt(_RCB, 26), fill=TEAL, anchor='mm')

    img.save(f'{OUT}/02-Everything-Included.jpg', quality=95)
    print('  ✓ 02-Everything-Included.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 03 — PRACTICE DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════

def img03_dashboard():
    img = Image.new('RGB', (W, H), (240, 244, 248))
    d = ImageDraw.Draw(img)

    # Browser chrome
    rr(d, [40, 20, W-40, H-20], 16, WHITE, outline=RULE, width=1)

    # Browser top bar
    rr(d, [40, 20, W-40, 72], 16, NAVY_2)
    d.ellipse([66, 36, 86, 56], fill=(239,68,68))
    d.ellipse([98, 36, 118, 56], fill=(245,158,11))
    d.ellipse([130, 36, 150, 56], fill=(34,197,94))
    rr(d, [180, 32, W-200, 60], 6, (40,52,70))
    d.text((W//2, 46), 'app.novaops.io/dashboard', font=fnt(_RR, 24), fill=MUTED, anchor='mm')
    d.text((W-90, 46), 'v3.0', font=fnt(_RM, 22), fill=TEAL, anchor='mm')

    # App header
    d.rectangle([40, 72, W-40, 124], fill=NAVY)
    d.text((80, 98), 'NOVAOPS  ·  Practice Dashboard', font=fnt(_RBo, 30), fill=WHITE, anchor='lm')
    d.text((W-80, 98), '● Connected  ·  June 2025', font=fnt(_RR, 26), fill=GREEN, anchor='rm')

    # Left sidebar
    sb_w = 220
    d.rectangle([40, 124, 40+sb_w, H-20], fill=(248,250,254))
    d.line([40+sb_w, 124, 40+sb_w, H-20], fill=RULE, width=1)
    menu = ['Dashboard','Client CRM','Lead Pipeline','Monthly Close','Invoices','Pricing Calc','Capacity','Instructions']
    icons2 = ['⊞','👥','📈','📅','💳','🧮','📊','❓']
    for i,(m,ic) in enumerate(zip(menu,icons2)):
        my = 144 + i*74
        if i == 0:
            rr(d, [48, my-6, 40+sb_w-8, my+54], 8, TEAL)
            d.text((70, my+22), f'{ic}  {m}', font=fnt(_RM, 26), fill=WHITE, anchor='lm')
        else:
            d.text((70, my+22), f'{ic}  {m}', font=fnt(_RR, 26), fill=MUTED, anchor='lm')

    # Main content area
    main_x = 40+sb_w+20
    main_w = W-40-sb_w-60

    # Title
    d.text((main_x, 140), 'Executive Dashboard', font=fnt(_RB, 38), fill=NAVY, anchor='lt')
    d.text((main_x, 188), 'June 2025  ·  Auto-updated', font=fnt(_RR, 26), fill=MUTED, anchor='lt')

    # KPI strip
    kpi_y2 = 224
    kpis2 = [('Monthly Revenue', '€12,400', '+8% vs May', TEAL),
             ('Active Clients', '18', '2 added this month', GREEN),
             ('Pipeline Value', '€6,200', '4 prospects', AMBER),
             ('Invoices Due', '€3,100', 'This month', NAVY)]
    kw2 = (main_w - 60) // 4
    for i,(lbl,val,sub,col) in enumerate(kpis2):
        kx2 = main_x + i*(kw2+18)
        rr(d, [kx2, kpi_y2, kx2+kw2, kpi_y2+120], 10, WHITE, outline=RULE, width=1)
        d.rectangle([kx2, kpi_y2, kx2+kw2, kpi_y2+5], fill=col)
        d.text((kx2+16, kpi_y2+24), lbl, font=fnt(_RM, 22), fill=MUTED, anchor='lt')
        d.text((kx2+16, kpi_y2+50), val, font=fnt(_RB, 46), fill=NAVY, anchor='lt')
        d.text((kx2+16, kpi_y2+102), sub, font=fnt(_RR, 20), fill=MUTED, anchor='lt')

    # Revenue chart
    rc_y = kpi_y2+140
    rc_w = int(main_w*0.55)
    rc_h = 280
    rr(d, [main_x, rc_y, main_x+rc_w, rc_y+rc_h], 10, WHITE, outline=RULE, width=1)
    d.text((main_x+16, rc_y+16), 'Revenue Trend', font=fnt(_RBo, 28), fill=NAVY, anchor='lt')
    d.text((main_x+16, rc_y+48), '12 months rolling', font=fnt(_RR, 22), fill=MUTED, anchor='lt')
    months2 = ['Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun']
    revenue = [58,62,55,70,66,74,68,78,72,82,88,100]
    bw3 = (rc_w-60)/12 - 4
    for i,(m,v) in enumerate(zip(months2,revenue)):
        bx3 = main_x+30+i*(bw3+4)
        bh3 = int(180*v/100)
        col3 = AMBER if i==11 else TEAL
        rr(d, [bx3, rc_y+250-bh3, bx3+bw3, rc_y+250], 3, col3)
        if i%2==0:
            d.text((bx3+bw3//2, rc_y+rc_h-14), m, font=fnt(_RR,18), fill=MUTED, anchor='mm')

    # Client table (right of chart)
    ct_x = main_x+rc_w+20
    ct_w = main_w-rc_w-20
    rr(d, [ct_x, rc_y, ct_x+ct_w, rc_y+rc_h], 10, WHITE, outline=RULE, width=1)
    d.text((ct_x+16, rc_y+16), 'Top Clients', font=fnt(_RBo, 28), fill=NAVY, anchor='lt')
    clients2 = [('Acme Ltd','€1,200','⬆'),('Brio Co','€1,050','⬆'),('Finova','€900','⬆'),
                ('EasyPay','€780','→'),('Novalux','€650','→'),('BlueWave','€600','⬆')]
    for i,(n,f,t) in enumerate(clients2):
        iy2 = rc_y+68+i*34
        bg3 = BG_SOFT if i%2==0 else WHITE
        d.rectangle([ct_x+8, iy2, ct_x+ct_w-8, iy2+32], fill=bg3)
        d.text((ct_x+16, iy2+16), n, font=fnt(_RM, 22), fill=NAVY, anchor='lm')
        tc = GREEN if t=='⬆' else MUTED
        d.text((ct_x+ct_w-50, iy2+16), f, font=fnt(_RBo, 22), fill=TEAL, anchor='rm')
        d.text((ct_x+ct_w-20, iy2+16), t, font=fnt(_RR, 22), fill=tc, anchor='mm')

    # Monthly close tracker
    mc_y = rc_y+rc_h+20
    rr(d, [main_x, mc_y, main_x+main_w, mc_y+190], 10, WHITE, outline=RULE, width=1)
    d.text((main_x+16, mc_y+16), 'Monthly Close — June 2025', font=fnt(_RBo, 28), fill=NAVY, anchor='lt')
    d.text((main_x+main_w-16, mc_y+16), '3 of 5 steps complete', font=fnt(_RR, 24), fill=MUTED, anchor='rm')
    progress_bar(d, main_x+16, mc_y+58, main_w-32, 16, 0.6, color=TEAL)
    steps2 = [('Reconciliation','Complete',GREEN),('Categorisation','Complete',GREEN),
              ('Review','Complete',GREEN),('Adjustments','In Progress',AMBER),('Reporting','Not Started',RULE)]
    sw2 = (main_w-40) // 5
    for i,(s,st,c) in enumerate(steps2):
        sx2 = main_x+20+i*sw2
        rr(d, [sx2, mc_y+90, sx2+sw2-8, mc_y+180], 8, BG_SOFT, outline=c, width=2)
        d.text((sx2+sw2//2, mc_y+128), s, font=fnt(_RM, 22), fill=NAVY, anchor='mm')
        rr(d, [sx2+8, mc_y+148, sx2+sw2-16, mc_y+170], 8, c)
        d.text((sx2+sw2//2, mc_y+159), st, font=fnt(_RCB, 18), fill=WHITE if c!=RULE else MUTED, anchor='mm')

    img.save(f'{OUT}/03-Dashboard.jpg', quality=95)
    print('  ✓ 03-Dashboard.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 04 — NOTION WORKSPACE
# ══════════════════════════════════════════════════════════════════════════════

def img04_notion():
    img = Image.new('RGB', (W, H), (245, 245, 244))  # Notion off-white
    d = ImageDraw.Draw(img)

    # Window chrome
    rr(d, [30, 20, W-30, H-20], 16, WHITE, outline=RULE, width=1)
    rr(d, [30, 20, W-30, 68], 16, (250, 250, 249))
    d.ellipse([54, 36, 72, 54], fill=(239,68,68))
    d.ellipse([82, 36, 100, 54], fill=(245,158,11))
    d.ellipse([110, 36, 128, 54], fill=(34,197,94))
    d.text((W//2, 44), 'notion.so  ·  Bookkeeping Practice Workspace', font=fnt(_RR, 24), fill=MUTED, anchor='mm')

    # Left sidebar — dark Notion style
    sb_w = 280
    d.rectangle([30, 68, 30+sb_w, H-20], fill=(25,25,25))

    # Workspace header
    d.text((50, 100), '🗂  Bookkeeping Practice', font=fnt(_RBo, 26), fill=WHITE, anchor='lt')
    d.line([42, 130, 30+sb_w-12, 130], fill=(50,50,50), width=1)

    pages = [
        ('⊞ Dashboard', True),
        ('👥 Clients CRM', False),
        ('📈 Lead Pipeline', False),
        ('📅 Monthly Close', False),
        ('💳 Invoices', False),
        ('📋 Tasks', False),
        ('📁 Documents', False),
        ('🔗 Client Portal', False),
        ('📊 Reports', False),
    ]
    for i,(page,active) in enumerate(pages):
        py = 148+i*58
        if active:
            rr(d, [38, py-4, 30+sb_w-8, py+46], 6, (55,55,55))
            d.text((58, py+20), page, font=fnt(_RM, 26), fill=WHITE, anchor='lm')
        else:
            d.text((58, py+20), page, font=fnt(_RR, 26), fill=(150,150,150), anchor='lm')

    # Main content
    mx = 30+sb_w+30
    mw = W-60-sb_w-30

    # Page title
    d.text((mx, 90), '👥', font=fnt(_RR, 50), fill=NAVY, anchor='lt')
    d.text((mx+65, 108), 'Clients CRM', font=fnt(_RB, 52), fill=NAVY, anchor='lm')

    # Toolbar row
    ty = 168
    d.text((mx, ty+8), 'Filter', font=fnt(_RM, 26), fill=MUTED, anchor='lm')
    d.text((mx+90, ty+8), 'Sort', font=fnt(_RM, 26), fill=MUTED, anchor='lm')
    d.text((mx+170, ty+8), 'Group', font=fnt(_RM, 26), fill=MUTED, anchor='lm')
    d.text((mx+270, ty+8), 'Properties', font=fnt(_RM, 26), fill=MUTED, anchor='lm')
    rr(d, [mx+mw-150, ty, mx+mw, ty+36], 8, NAVY)
    d.text((mx+mw-75, ty+18), '+ New', font=fnt(_RM, 26), fill=WHITE, anchor='mm')
    d.line([mx, ty+42, mx+mw, ty+42], fill=RULE, width=1)

    # Table
    t_y = ty+50
    headers = ['Name','Status','Software','Monthly Fee','Close Day','Notes']
    col_ws = [int(mw*p) for p in [0.22, 0.12, 0.14, 0.14, 0.12, 0.26]]
    # Header row
    d.rectangle([mx, t_y, mx+mw, t_y+40], fill=(250,250,249))
    d.line([mx, t_y+40, mx+mw, t_y+40], fill=RULE, width=1)
    cx2 = mx
    for i,(h2,cw2) in enumerate(zip(headers,col_ws)):
        d.text((cx2+12, t_y+20), h2, font=fnt(_RM, 22), fill=MUTED, anchor='lm')
        if i < len(col_ws)-1:
            d.line([cx2+cw2, t_y, cx2+cw2, t_y+40], fill=RULE, width=1)
        cx2 += cw2

    clients3 = [
        ('Acme Ltd', 'Active', 'Xero', '€1,200', '15th', 'Auto-import live'),
        ('Brio Co', 'Active', 'QuickBooks', '€1,050', '15th', 'Q2 review needed'),
        ('Finova GmbH', 'Active', 'Xero', '€900', '20th', 'Multi-currency'),
        ('EasyPay Ltd', 'In Review', 'Wave', '€780', '10th', 'New client Mar'),
        ('Novalux Inc', 'Active', 'Xero', '€650', '15th', 'US entity'),
        ('BlueWave', 'Active', 'QBO', '€600', '20th', 'Ecommerce'),
        ('TechFlow', 'Churned', 'QuickBooks', '€0', '—', 'Closed Jan 2025'),
        ('GreenBuild', 'Active', 'Sage', '€850', '15th', 'Construction co.'),
    ]
    for ri, row in enumerate(clients3):
        ry = t_y + 42 + ri*48
        bg4 = WHITE if ri%2==0 else (252,252,251)
        d.rectangle([mx, ry, mx+mw, ry+46], fill=bg4)
        d.line([mx, ry+46, mx+mw, ry+46], fill=RULE, width=1)
        cx3 = mx
        for ci2,(cell,cw3) in enumerate(zip(row,col_ws)):
            if ci2==0:
                d.text((cx3+30, ry+23), cell, font=fnt(_RM, 26), fill=NAVY, anchor='lm')
                d.ellipse([cx3+10, ry+15, cx3+24, ry+31], fill=TEAL)
            elif ci2==1:
                sc = GREEN if cell=='Active' else (AMBER if cell=='In Review' else MUTED)
                rr(d, [cx3+8, ry+10, cx3+8+len(cell)*12+16, ry+36], 10, sc)
                d.text((cx3+8+len(cell)*6+8, ry+23), cell, font=fnt(_RR, 20), fill=WHITE, anchor='mm')
            elif ci2==3:
                d.text((cx3+12, ry+23), cell, font=fnt(_RBo, 26), fill=TEAL, anchor='lm')
            else:
                d.text((cx3+12, ry+23), str(cell), font=fnt(_RR, 24), fill=NAVY, anchor='lm')
            if ci2 < len(col_ws)-1:
                d.line([cx3+cw3, t_y, cx3+cw3, ry+46], fill=RULE, width=1)
            cx3 += cw3

    # Bottom: summary badges
    sum_y = H-120
    d.line([mx, sum_y, mx+mw, sum_y], fill=RULE, width=1)
    d.text((mx, sum_y+20), '8 clients', font=fnt(_RM, 26), fill=MUTED, anchor='lt')
    d.text((mx+140, sum_y+20), '·  MRR: €6,030', font=fnt(_RM, 26), fill=TEAL, anchor='lt')
    d.text((mx+340, sum_y+20), '·  7 databases connected', font=fnt(_RR, 26), fill=MUTED, anchor='lt')
    d.text((mx+mw-20, sum_y+20), 'NOVAOPS Notion Template  ·  v3.0', font=fnt(_RR, 22), fill=MUTED, anchor='rm')

    img.save(f'{OUT}/04-Notion-Workspace.jpg', quality=95)
    print('  ✓ 04-Notion-Workspace.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 05 — FINANCIAL SYSTEM
# ══════════════════════════════════════════════════════════════════════════════

def img05_financial():
    img = Image.new('RGB', (W, H), BG_SOFT)
    d = ImageDraw.Draw(img)

    # Header
    d.rectangle([0, 0, W, 120], fill=NAVY)
    d.text((60, 60), 'EXCEL PRACTICE DASHBOARD', font=fnt(_RB, 40), fill=WHITE, anchor='lm')
    d.text((W-60, 40), '10 SHEETS', font=fnt(_RB, 36), fill=TEAL, anchor='rm')
    d.text((W-60, 84), 'All your numbers in one place', font=fnt(_RR, 26), fill=MUTED, anchor='rm')

    # Tab row
    tabs = ['Dashboard','Client CRM','Lead Pipeline','Monthly Close','Invoices','Pricing Calc','Capacity','Instructions']
    tx2 = 0
    for i,tab in enumerate(tabs):
        tw = len(tab)*18+40
        bg5 = TEAL if i==0 else (WHITE if i<4 else BG_SOFT)
        fc = WHITE if i==0 else (NAVY if i<4 else MUTED)
        d.rectangle([tx2, 120, tx2+tw, 160], fill=bg5)
        d.line([tx2+tw, 120, tx2+tw, 160], fill=RULE, width=1)
        d.text((tx2+tw//2, 140), tab, font=fnt(_RM if i<4 else _RR, 22), fill=fc, anchor='mm')
        tx2 += tw
    d.line([0, 160, W, 160], fill=RULE, width=2)

    # Main dashboard content (simulating spreadsheet)
    # Freeze row header
    d.rectangle([0, 160, W, 200], fill=(240,244,248))
    row_labels = ['A','B','C','D','E','F','G','H']
    col_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
    for i,c in enumerate(col_labels):
        cx4 = 60+i*210
        d.text((cx4+100, 180), c, font=fnt(_RR, 22), fill=MUTED, anchor='mm')
        d.line([cx4, 160, cx4, H], fill=RULE, width=1)

    # Big KPI section
    k_y = 210
    kpis3 = [('MRR', '€12,400', '+8%', TEAL), ('Clients', '18', 'Active', GREEN),
             ('Pipeline', '€6,200', '4 leads', AMBER), ('MRR Target', '€15,000', '82% to target', PURPLE),
             ('Avg Fee', '€689', 'Per client', TEAL), ('Capacity', '78%', '22% available', NAVY)]
    kw3 = 390
    for i,( lbl,val,sub,col) in enumerate(kpis3):
        kx3 = 60+i*(kw3+16)
        rr(d, [kx3, k_y, kx3+kw3, k_y+130], 10, WHITE, outline=RULE, width=1)
        d.rectangle([kx3, k_y, kx3+kw3, k_y+6], fill=col)
        d.text((kx3+16, k_y+28), lbl, font=fnt(_RM, 24), fill=MUTED, anchor='lt')
        d.text((kx3+16, k_y+58), val, font=fnt(_RB, 52), fill=NAVY, anchor='lt')
        d.text((kx3+16, k_y+114), sub, font=fnt(_RR, 22), fill=MUTED, anchor='lt')

    # Revenue chart
    chart2_y = k_y+152
    chart2_w = int(W*0.55)-60
    chart2_h = 320
    rr(d, [60, chart2_y, 60+chart2_w, chart2_y+chart2_h], 10, WHITE, outline=RULE, width=1)
    d.text((80, chart2_y+20), 'Monthly Revenue  (12-month view)', font=fnt(_RBo, 30), fill=NAVY, anchor='lt')
    # Y axis labels
    for i,v in enumerate([0,3000,6000,9000,12000]):
        yl = chart2_y+chart2_h-40-int(240*v/12000)
        d.text((76, yl), f'€{v//1000}k', font=fnt(_RR, 18), fill=MUTED, anchor='rm')
        d.line([86, yl, 60+chart2_w-10, yl], fill=RULE, width=1)
    months3 = ['Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun']
    revenues = [7200,7800,6900,8700,8200,9200,8500,9700,9000,10200,10900,12400]
    pts = []
    bw4 = (chart2_w-100)/12 - 4
    for i,(m,r) in enumerate(zip(months3,revenues)):
        bx4 = 86+i*(bw4+4)
        bh4 = int(240*r/12000)
        rr(d, [bx4, chart2_y+chart2_h-40-bh4, bx4+bw4, chart2_y+chart2_h-40], 3, TEAL if i<11 else AMBER)
        pts.append((bx4+bw4//2, chart2_y+chart2_h-40-bh4))
        if i%2==0:
            d.text((bx4+bw4//2, chart2_y+chart2_h-22), m, font=fnt(_RR,18), fill=MUTED, anchor='mm')

    # Line overlay
    if len(pts)>1:
        d.line(pts, fill=AMBER, width=3)

    # Invoice tracker (right side)
    inv_x = 60+chart2_w+20
    inv_w = W-60-chart2_w-80
    rr(d, [inv_x, chart2_y, inv_x+inv_w, chart2_y+chart2_h], 10, WHITE, outline=RULE, width=1)
    d.text((inv_x+16, chart2_y+20), 'Invoice Tracker', font=fnt(_RBo, 30), fill=NAVY, anchor='lt')
    d.text((inv_x+inv_w-16, chart2_y+20), '€8,340 outstanding', font=fnt(_RBo, 26), fill=AMBER, anchor='rm')
    inv_data = [('#042','Acme Ltd','€1,200','Paid',GREEN),
                ('#041','Brio Co','€1,050','Paid',GREEN),
                ('#040','Finova','€900','Sent',AMBER),
                ('#039','EasyPay','€780','Sent',AMBER),
                ('#038','Novalux','€650','Overdue',RED),
                ('#037','BlueWave','€600','Overdue',RED)]
    iw = [80,160,100,120]
    d.rectangle([inv_x+8, chart2_y+60, inv_x+inv_w-8, chart2_y+90], fill=TEAL)
    for j,h3 in enumerate(['#','Client','Amount','Status']):
        ix3 = inv_x+16+sum(iw[:j])
        d.text((ix3, chart2_y+75), h3, font=fnt(_RBo, 22), fill=WHITE, anchor='lm')
    for ri2, (n1,n2,n3,st3,sc3) in enumerate(inv_data):
        ry2 = chart2_y+96+ri2*36
        bg6 = WHITE if ri2%2==0 else BG_SOFT
        d.rectangle([inv_x+8, ry2, inv_x+inv_w-8, ry2+34], fill=bg6)
        d.text((inv_x+16, ry2+17), n1, font=fnt(_RR,22), fill=MUTED, anchor='lm')
        d.text((inv_x+96, ry2+17), n2, font=fnt(_RM,22), fill=NAVY, anchor='lm')
        d.text((inv_x+256, ry2+17), n3, font=fnt(_RBo,22), fill=TEAL, anchor='lm')
        rr(d, [inv_x+356, ry2+7, inv_x+476, ry2+29], 8, sc3)
        d.text((inv_x+416, ry2+18), st3, font=fnt(_RCB,18), fill=WHITE, anchor='mm')

    # Pricing calculator strip
    pc_y = chart2_y+chart2_h+20
    rr(d, [60, pc_y, W-60, pc_y+130], 10, NAVY)
    d.text((80, pc_y+20), 'Pricing Calculator', font=fnt(_RBo, 30), fill=WHITE, anchor='lt')
    d.text((80, pc_y+58), 'Enter transaction volume →', font=fnt(_RR, 26), fill=MUTED, anchor='lt')
    tiers = [('Starter','≤150 txn','€500/mo'), ('Growth','≤400 txn','€850/mo'), ('Premium','≤800 txn','€1,400/mo')]
    for i,(tier,txn,fee) in enumerate(tiers):
        tx3 = 600+i*500
        rr(d, [tx3, pc_y+12, tx3+440, pc_y+118], 10, NAVY_2)
        rr(d, [tx3, pc_y+12, tx3+440, pc_y+18], 4, TEAL if i==1 else RULE)
        d.text((tx3+16, pc_y+42), tier, font=fnt(_RBo, 28), fill=WHITE, anchor='lt')
        d.text((tx3+16, pc_y+76), txn, font=fnt(_RR, 24), fill=MUTED, anchor='lt')
        d.text((tx3+400, pc_y+66), fee, font=fnt(_RB, 36), fill=TEAL, anchor='rm')

    img.save(f'{OUT}/05-Financial-System.jpg', quality=95)
    print('  ✓ 05-Financial-System.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 06 — CLIENT EXPERIENCE
# ══════════════════════════════════════════════════════════════════════════════

def img06_client():
    img = Image.new('RGB', (W, H), BG_SOFT)
    d = ImageDraw.Draw(img)

    # Header
    d.rectangle([0, 0, W, 110], fill=NAVY)
    d.text((W//2, 55), 'THE COMPLETE CLIENT EXPERIENCE', font=fnt(_RB, 46), fill=WHITE, anchor='mm')

    # Subtitle
    d.text((W//2, 140), 'Every document. Every workflow. From first contact to year-end.', font=fnt(_RM, 32), fill=MUTED, anchor='mm')

    # Six document cards in 3x2
    docs = [
        ('📧', 'Bookkeeping\nService Guide', 'Your 5-tier menu. Clear pricing.\nProfessional. Sends itself.', TEAL, '5 service tiers'),
        ('📝', 'Proposal\nTemplate', 'Scope. Fees. Timeline. 100%\ncustomisable per client.', AMBER, 'Per-client scoped'),
        ('⚖️', 'Engagement\nAgreement', '15 professional clauses.\nLawyer-reviewed structure.', PURPLE, 'Legal-grade contract'),
        ('📋', 'Onboarding\nPack', 'Structured intake. Document\ncollection. Portal setup.', TEAL_M, '5 structured sections'),
        ('🎤', 'Communication\nScripts', '10 email/portal scripts.\nInquiry to year-end.', TEAL, 'Zero blank-page moments'),
        ('📊', 'Proposal Deck', '10 consulting slides.\nCanva-importable.', AMBER, 'Visual-first pitch'),
    ]

    card_w = 790
    card_h = 540
    pad_x2 = (W-3*card_w)//4
    for i,(icon,title,desc,col,tag) in enumerate(docs):
        col2 = i%3
        row2 = i//3
        cx5 = pad_x2+col2*(card_w+pad_x2)
        cy5 = 180+row2*(card_h+24)

        img, d = shadow_card(img, [cx5, cy5, cx5+card_w, cy5+card_h], 14, WHITE)
        d.rounded_rectangle([cx5, cy5, cx5+card_w, cy5+8], radius=4, fill=col)

        # Icon
        rr(d, [cx5+20, cy5+28, cx5+100, cy5+108], 16, TEAL_L)
        d.text((cx5+60, cy5+68), icon, font=fnt(_RR, 52), fill=col, anchor='mm')

        # Tag
        tag_w = len(tag)*14+24
        rr(d, [cx5+card_w-tag_w-14, cy5+24, cx5+card_w-14, cy5+54], 8, col)
        d.text((cx5+card_w-tag_w//2-26, cy5+39), tag, font=fnt(_RCB, 20), fill=WHITE, anchor='mm')

        # Title
        lines = title.split('\n')
        for li,ln in enumerate(lines):
            d.text((cx5+116, cy5+44+li*46), ln, font=fnt(_RBo, 38), fill=NAVY, anchor='lt')

        d.line([cx5+20, cy5+120, cx5+card_w-20, cy5+120], fill=RULE, width=1)

        # Description
        desc_lines = desc.split('\n')
        for li2, ln2 in enumerate(desc_lines):
            d.text((cx5+24, cy5+140+li2*42), ln2, font=fnt(_RM, 28), fill=MUTED, anchor='lt')

        # Format badge
        fmt = {'📧':'DOCX','📝':'DOCX','⚖️':'DOCX','📋':'DOCX','🎤':'DOCX','📊':'PPTX'}.get(icon,'DOCX')
        rr(d, [cx5+20, cy5+card_h-60, cx5+100, cy5+card_h-20], 8, BG_SOFT, outline=RULE, width=1)
        d.text((cx5+60, cy5+card_h-40), fmt, font=fnt(_RCB, 24), fill=TEAL, anchor='mm')

        # Editable badge
        rr(d, [cx5+112, cy5+card_h-60, cx5+232, cy5+card_h-20], 8, TEAL_L)
        d.text((cx5+172, cy5+card_h-40), 'Editable', font=fnt(_RM, 24), fill=TEAL, anchor='mm')

    # Footer
    d.rectangle([0, H-80, W, H], fill=NAVY)
    d.text((W//2, H-40), 'Replace all [BRACKETED PLACEHOLDERS] with Find & Replace  ·  Ready to send in minutes  ·  NOVAOPS v3.0', font=fnt(_RCB, 26), fill=TEAL, anchor='mm')

    img.save(f'{OUT}/06-Client-Documents.jpg', quality=95)
    print('  ✓ 06-Client-Documents.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 07 — BUSINESS WORKFLOW TIMELINE
# ══════════════════════════════════════════════════════════════════════════════

def img07_workflow():
    img = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # Left dark panel
    d.rectangle([0, 0, 580, H], fill=NAVY)
    d.text((290, 80), 'YOUR', font=fnt(_RB, 72), fill=WHITE, anchor='mm')
    d.text((290, 158), 'BUSINESS', font=fnt(_RB, 72), fill=TEAL, anchor='mm')
    d.text((290, 236), 'WORKFLOW', font=fnt(_RB, 72), fill=WHITE, anchor='mm')
    d.line([60, 272, 520, 272], fill=TEAL, width=2)
    d.text((290, 316), 'From first lead to repeat', font=fnt(_RM, 32), fill=MUTED, anchor='mm')
    d.text((290, 356), 'client — every step covered.', font=fnt(_RM, 32), fill=MUTED, anchor='mm')

    d.text((290, H-100), 'NOVAOPS', font=fnt(_RBo, 30), fill=TEAL, anchor='mm')
    d.text((290, H-60), 'Bookkeeper Practice v3.0', font=fnt(_RR, 24), fill=MUTED, anchor='mm')

    # Right: vertical timeline
    steps_flow = [
        ('01', 'Lead Generation', 'Prospect identified via referral,\nnetwork, or Etsy/LinkedIn.', TEAL, '📥'),
        ('02', 'Discovery Call', 'Qualify business type, volume,\nsoftware, and budget.', AMBER, '📞'),
        ('03', 'Proposal', 'Send Service Guide + Proposal.\nPersonalised scope + fee.', TEAL, '📝'),
        ('04', 'Agreement', 'Engagement Agreement signed.\nSetup fee received.', PURPLE, '⚖️'),
        ('05', 'Onboarding', 'Intake Pack sent. Access granted.\nDocuments collected.', TEAL_M, '📋'),
        ('06', 'Monthly Close', 'Reconcile. Categorise. Review.\nAdjust. Report.', TEAL, '📅'),
        ('07', 'Reporting', 'Deliver P&L + Balance Sheet.\nExceptions documented.', GREEN, '📊'),
        ('08', 'Repeat & Grow', 'Retain. Upsell. Refer.\nScale to next tier.', AMBER, '🚀'),
    ]

    step_h = (H-80)//8
    tl_x = 680  # timeline center
    for i,(num,title,desc,col,icon) in enumerate(steps_flow):
        sy = 40 + i*step_h
        cx6 = tl_x

        # Vertical line (between steps)
        if i < len(steps_flow)-1:
            d.line([cx6, sy+56, cx6, sy+step_h], fill=RULE, width=3)

        # Circle
        r_c = 34
        d.ellipse([cx6-r_c, sy+4, cx6+r_c, sy+4+r_c*2], fill=col)
        d.text((cx6, sy+4+r_c), num, font=fnt(_RBo, 30), fill=WHITE, anchor='mm')

        # Content card (right of circle)
        card_x = cx6+r_c+24
        card_w2 = W-card_x-40
        rr(d, [card_x, sy+4, card_x+card_w2, sy+step_h-6], 10, BG_SOFT, outline=RULE, width=1)
        d.rounded_rectangle([card_x, sy+4, card_x+card_w2, sy+10], radius=4, fill=col)

        d.text((card_x+60, sy+28), icon, font=fnt(_RR, 36), fill=col, anchor='mm')
        d.text((card_x+96, sy+24), title, font=fnt(_RBo, 32), fill=NAVY, anchor='lt')

        d.line([card_x+16, sy+58, card_x+card_w2-16, sy+58], fill=RULE, width=1)

        desc_lines = desc.split('\n')
        for li3,ln3 in enumerate(desc_lines):
            d.text((card_x+16, sy+72+li3*34), ln3, font=fnt(_RR, 26), fill=MUTED, anchor='lt')

        # File used tag
        file_tags = ['Service Guide','Discovery Form','Proposal Template','Engagement Agmt',
                     'Intake Pack','SOPs + Excel','Scripts + Portal','CRM + Dashboard']
        rr(d, [card_x+card_w2-220, sy+step_h-46, card_x+card_w2-16, sy+step_h-18], 8, col)
        d.text((card_x+card_w2-118, sy+step_h-32), file_tags[i], font=fnt(_RCB, 18), fill=WHITE, anchor='mm')

    img.save(f'{OUT}/07-Business-Workflow.jpg', quality=95)
    print('  ✓ 07-Business-Workflow.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 08 — PREMIUM ASSETS
# ══════════════════════════════════════════════════════════════════════════════

def img08_assets():
    img = Image.new('RGB', (W, H), BG_SOFT)
    d = ImageDraw.Draw(img)

    # Header
    d.rectangle([0, 0, W, 120], fill=NAVY)
    d.text((60, 60), '33 PREMIUM FILES', font=fnt(_RB, 50), fill=WHITE, anchor='lm')
    d.text((W-60, 40), 'Instant Download', font=fnt(_RBo, 30), fill=TEAL, anchor='rm')
    d.text((W-60, 84), 'All editable  ·  All branded', font=fnt(_RR, 26), fill=MUTED, anchor='rm')

    assets = [
        # (format_color, format_label, filename, description)
        (TEAL, 'PDF', 'Read-Me-First.pdf', 'Complete product orientation'),
        (TEAL, 'PDF', 'Installation-Guide.pdf', '90-minute setup walkthrough'),
        (TEAL, 'PDF', 'Asset-Manifest.pdf', 'Full file inventory'),
        (TEAL, 'PDF', 'License.pdf', 'Commercial use terms'),
        (TEAL, 'PDF', 'FAQ.pdf', '16 setup questions answered'),
        (TEAL, 'PDF', 'Version-History.pdf', 'Changelog + roadmap'),
        (TEAL, 'PDF', 'Support-Guide.pdf', 'Get help fast'),
        (TEAL, 'PDF', 'Notion-Setup-Guide.pdf', 'Import + connect all 7 DBs'),
        (GREEN, 'XLSX', 'Practice-Dashboard-v3.xlsx', '10-sheet Excel workbook, KPIs, charts'),
        ((0x0D, 0x47, 0xA1), 'DOCX', 'Start-Here-v3.docx', 'Quick-reference overview'),
        ((0x0D, 0x47, 0xA1), 'DOCX', 'Service-Guide-v3.docx', '5-tier service menu'),
        ((0x0D, 0x47, 0xA1), 'DOCX', 'Proposal-Template-v3.docx', 'Per-client scoped proposal'),
        ((0x0D, 0x47, 0xA1), 'DOCX', 'Engagement-Agreement-v3.docx', '15-clause legal contract'),
        ((0x0D, 0x47, 0xA1), 'DOCX', 'Intake-Onboarding-Pack-v3.docx', 'Full client onboarding'),
        ((0x0D, 0x47, 0xA1), 'DOCX', 'SOPs-and-Checklists-v3.docx', '4 SOPs + quality control'),
        ((0x0D, 0x47, 0xA1), 'DOCX', 'Communication-Scripts-v3.docx', '10 email + portal scripts'),
        ((0x0D, 0x47, 0xA1), 'DOCX', 'Tax-Prep-Checklist-v3.docx', '4-phase year-end system'),
        (AMBER, 'PPTX', 'Proposal-Deck-v3.pptx', '10 consulting-grade slides'),
        (PURPLE, 'CSV', 'Clients.csv', 'Master CRM — 20 columns'),
        (PURPLE, 'CSV', 'Leads.csv', 'Lead pipeline — 17 columns'),
        (PURPLE, 'CSV', 'Monthly-Close.csv', 'Close tracker — 16 columns'),
        (PURPLE, 'CSV', 'Document-Requests.csv', 'Doc collection — 11 columns'),
        (PURPLE, 'CSV', 'Invoices.csv', 'Invoice register — 13 columns'),
        (PURPLE, 'CSV', 'Tasks.csv', 'Task manager — 11 columns'),
        (PURPLE, 'CSV', 'Client-Portal.csv', 'Client-visible portal items'),
    ]

    # Two-column layout
    left_assets = assets[:13]
    right_assets = assets[13:]

    def draw_asset_list(d, start_x, start_y, items):
        for i,(col6,fmt,fname,fdesc) in enumerate(items):
            ay = start_y + i*58
            # Format tag
            rr(d, [start_x, ay+6, start_x+80, ay+44], 6, col6)
            d.text((start_x+40, ay+25), fmt, font=fnt(_RCB, 22), fill=WHITE, anchor='mm')
            # File name
            d.text((start_x+94, ay+14), fname, font=fnt(_RBo, 26), fill=NAVY, anchor='lt')
            d.text((start_x+94, ay+42), fdesc, font=fnt(_RR, 22), fill=MUTED, anchor='lt')
            d.line([start_x, ay+56, start_x+1280, ay+56], fill=RULE, width=1)

    draw_asset_list(d, 50, 145, left_assets)
    draw_asset_list(d, 1370, 145, right_assets)

    d.line([W//2, 130, W//2, H-90], fill=RULE, width=1)

    # Footer summary
    d.rectangle([0, H-90, W, H], fill=NAVY)
    items_row = [('9', 'PDF Guides'), ('9', 'DOCX Templates'), ('1', 'Excel Dashboard'),
                 ('1', 'PPTX Deck'), ('7', 'Notion CSVs'), ('6', 'Bonus Guides')]
    iw2 = W//len(items_row)
    for i,(n,lbl) in enumerate(items_row):
        ix4 = i*iw2+iw2//2
        d.text((ix4, H-62), n, font=fnt(_RB, 38), fill=TEAL, anchor='mm')
        d.text((ix4, H-26), lbl, font=fnt(_RR, 22), fill=MUTED, anchor='mm')
        if i<len(items_row)-1:
            d.line([ix4+iw2//2, H-82, ix4+iw2//2, H-8], fill=(40,55,80), width=1)

    img.save(f'{OUT}/08-Premium-Assets.jpg', quality=95)
    print('  ✓ 08-Premium-Assets.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 09 — WHO IS THIS FOR
# ══════════════════════════════════════════════════════════════════════════════

def img09_audience():
    img = Image.new('RGB', (W, H), BG_SOFT)
    d = ImageDraw.Draw(img)

    # Header
    d.rectangle([0, 0, W, 130], fill=NAVY)
    d.text((W//2, 50), 'WHO IS THIS FOR?', font=fnt(_RB, 50), fill=WHITE, anchor='mm')
    d.text((W//2, 100), 'Built for the serious bookkeeper ready to build a premium, scalable practice.', font=fnt(_RM, 28), fill=MUTED, anchor='mm')

    audiences = [
        ('🧾', 'Freelance Bookkeepers', 'Launch or professionalise your\nsolo practice with consulting-\ngrade systems.', [
            'Win clients at premium rates',
            'Stop using ad-hoc documents',
            'Deliver Big Four-quality work',
        ], TEAL),
        ('🏢', 'Bookkeeping Agencies', 'Standardise operations across\nyour team with repeatable\nprocesses.', [
            'Onboard new bookkeepers fast',
            'Consistent client experience',
            'Scale without chaos',
        ], AMBER),
        ('📊', 'Fractional CFOs', 'Layer a bookkeeping practice\nonto your CFO service for\ncomplete client control.', [
            'Unified client management',
            'Seamless monthly reporting',
            'Cross-sell bookkeeping + CFO',
        ], PURPLE),
        ('💻', 'Virtual Bookkeepers', 'Run a fully remote practice\nwith structured workflows and\na client portal.', [
            'Notion portal included',
            'Remote-first SOPs',
            'All documents digital-ready',
        ], TEAL_M),
        ('📈', 'Finance Consultants', 'Add bookkeeping as a revenue\nstream with zero groundwork\nalready done.', [
            'Ready on day one',
            'Professional brand impression',
            'Monthly recurring revenue',
        ], TEAL),
        ('🎓', 'New Bookkeepers', 'Skip 3 years of trial and error.\nStart with a professional system\nfrom day one.', [
            '90-minute setup system',
            'Know exactly what to do',
            'Look experienced immediately',
        ], GREEN),
    ]

    card_w2 = 820
    card_h2 = 740
    pad_x3 = (W-3*card_w2)//4

    for i,(icon,title,desc,benefits,col) in enumerate(audiences):
        col3 = i%3
        row3 = i//3
        cx7 = pad_x3+col3*(card_w2+pad_x3)
        cy7 = 160+row3*(card_h2+20)

        img, d = shadow_card(img, [cx7, cy7, cx7+card_w2, cy7+card_h2], 16, WHITE)
        d.rounded_rectangle([cx7, cy7, cx7+card_w2, cy7+8], radius=4, fill=col)

        # Icon
        rr(d, [cx7+20, cy7+26, cx7+104, cy7+110], 20, TEAL_L)
        d.text((cx7+62, cy7+68), icon, font=fnt(_RR, 56), fill=col, anchor='mm')

        d.text((cx7+116, cy7+42), title, font=fnt(_RBo, 36), fill=NAVY, anchor='lt')

        d.line([cx7+20, cy7+118, cx7+card_w2-20, cy7+118], fill=RULE, width=1)

        desc_lines = desc.split('\n')
        for li4,ln4 in enumerate(desc_lines):
            d.text((cx7+24, cy7+134+li4*42), ln4, font=fnt(_RR, 28), fill=MUTED, anchor='lt')

        d.line([cx7+20, cy7+268, cx7+card_w2-20, cy7+268], fill=RULE, width=1)
        d.text((cx7+24, cy7+286), 'KEY BENEFITS', font=fnt(_RCB, 22), fill=TEAL, anchor='lt')

        for bi,ben in enumerate(benefits):
            by2 = cy7+320+bi*100
            d.ellipse([cx7+24, by2, cx7+60, by2+36], fill=col)
            d.text((cx7+42, by2+18), '✓', font=fnt(_RBo, 24), fill=WHITE, anchor='mm')
            d.text((cx7+74, by2+18), ben, font=fnt(_RM, 28), fill=NAVY, anchor='lm')

    # Bottom CTA
    d.rectangle([0, H-80, W, H], fill=NAVY)
    d.text((W//2, H-40), 'If you want to run a professional bookkeeping practice — this is your system.  ·  NOVAOPS v3.0', font=fnt(_RM, 28), fill=WHITE, anchor='mm')

    img.save(f'{OUT}/09-Who-Is-This-For.jpg', quality=95)
    print('  ✓ 09-Who-Is-This-For.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 10 — FINAL CTA
# ══════════════════════════════════════════════════════════════════════════════

def img10_cta():
    img = Image.new('RGB', (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Subtle grid pattern background
    for gx in range(0, W, 80):
        d.line([gx, 0, gx, H], fill=(20, 30, 50), width=1)
    for gy in range(0, H, 80):
        d.line([0, gy, W, gy], fill=(20, 30, 50), width=1)

    # Teal accent glow (simulated)
    rr(d, [-100, -100, 600, 600], 0, (15, 40, 50))

    # Right panel: white card
    rr(d, [1340, 40, W-40, H-40], 24, WHITE)

    # Headline
    d.text((1400, 100), 'Start Using It', font=fnt(_RB, 70), fill=NAVY, anchor='lt')
    d.text((1400, 178), 'Today.', font=fnt(_RB, 70), fill=TEAL, anchor='lt')

    d.line([1400, 264, W-80, 264], fill=RULE, width=2)

    d.text((1400, 292), 'Download once.', font=fnt(_RM, 34), fill=MUTED, anchor='lt')
    d.text((1400, 334), 'Use forever.', font=fnt(_RM, 34), fill=MUTED, anchor='lt')
    d.text((1400, 376), 'Run your bookkeeping business', font=fnt(_RM, 34), fill=NAVY, anchor='lt')
    d.text((1400, 418), 'like a professional.', font=fnt(_RBo, 34), fill=NAVY, anchor='lt')

    d.line([1400, 472, W-80, 472], fill=RULE, width=1)

    # Feature badges (right panel)
    badges = [
        ('✓', 'Instant Download', TEAL),
        ('✓', 'Lifetime Access', GREEN),
        ('✓', '33 Premium Files', TEAL),
        ('✓', 'Fully Editable', AMBER),
        ('✓', 'Commercial License', PURPLE),
        ('✓', 'Professional System', NAVY),
    ]
    for i,(sym,text2,col) in enumerate(badges):
        by3 = 498+i*76
        d.ellipse([1400, by3+8, 1448, by3+56], fill=col)
        d.text((1424, by3+32), sym, font=fnt(_RBo, 30), fill=WHITE, anchor='mm')
        d.text((1464, by3+32), text2, font=fnt(_RM, 30), fill=NAVY, anchor='lm')

    # CTA Button
    rr(d, [1400, H-190, W-80, H-110], 16, TEAL)
    d.text(((1400+W-80)//2, H-150), '⬇  INSTANT DOWNLOAD', font=fnt(_RB, 38), fill=WHITE, anchor='mm')
    d.text(((1400+W-80)//2, H-108), 'Files delivered immediately after purchase', font=fnt(_RR, 24), fill=(200,240,236), anchor='mm')

    # NOVAOPS tag bottom-right
    rr(d, [1400, H-100, W-80, H-58], 8, BG_SOFT)
    d.text(((1400+W-80)//2, H-79), 'NOVAOPS  ·  Bookkeeper Practice Launch System  ·  v3.0', font=fnt(_RCB, 22), fill=NAVY, anchor='mm')

    # Left panel: device composition
    # Large laptop
    lx2, ly2, lw2, lh3 = laptop_mockup(d, 60, 80, 1080)

    # Dashboard inside laptop
    d2 = ImageDraw.Draw(img)
    d2.rectangle([lx2, ly2, lx2+lw2, ly2+44], fill=NAVY)
    d2.text((lx2+16, ly2+22), 'NOVAOPS Practice Dashboard', font=fnt(_RBo, 22), fill=WHITE, anchor='lm')
    d2.text((lx2+lw2-14, ly2+22), '● Live', font=fnt(_RR, 18), fill=GREEN, anchor='rm')

    kpi_y3 = ly2+52
    kpis4 = [('MRR','€12,400'), ('Clients','18'), ('Pipeline','€6,200'), ('Invoices','€3,100')]
    kw4 = lw2//4-4
    for i2,(lbl3,val3) in enumerate(kpis4):
        kx4 = lx2+2+i2*(kw4+2)
        rr(d2, [kx4, kpi_y3, kx4+kw4, kpi_y3+66], 4, (30,45,70))
        d2.rectangle([kx4, kpi_y3, kx4+kw4, kpi_y3+3], fill=TEAL)
        d2.text((kx4+8, kpi_y3+14), lbl3, font=fnt(_RR, 16), fill=MUTED, anchor='lt')
        d2.text((kx4+8, kpi_y3+34), val3, font=fnt(_RBo, 28), fill=WHITE, anchor='lt')

    # Mini bar chart
    bc_y = kpi_y3+74
    months4 = ['Jan','Feb','Mar','Apr','May','Jun']
    vals2 = [72,65,80,75,88,100]
    bw5 = (lw2-20)//6-4
    for i3,(m3,v3) in enumerate(zip(months4,vals2)):
        bx5 = lx2+10+i3*(bw5+4)
        bh5 = int(120*v3/100)
        rr(d2, [bx5, bc_y+130-bh5, bx5+bw5, bc_y+130], 2, TEAL if i3<5 else AMBER)

    # Floating tablet (top right of laptop)
    tx2, ty2, tw2, th2 = tablet_mockup(d, 1000, 60, 260)
    d2.text((tx2+tw2//2, ty2+20), 'Clients', font=fnt(_RBo, 20), fill=NAVY, anchor='mm')
    cl2 = [('Acme Ltd','Active','€1,200'),('Brio Co','Active','€1,050'),('Finova','Active','€900')]
    for i4,(n4,s4,f4) in enumerate(cl2):
        cy8 = ty2+48+i4*42
        bg7 = WHITE if i4%2==0 else BG_SOFT
        d2.rectangle([tx2+4, cy8, tx2+tw2-4, cy8+38], fill=bg7)
        d2.text((tx2+10, cy8+19), n4, font=fnt(_RR, 18), fill=NAVY, anchor='lm')
        d2.text((tx2+tw2-10, cy8+19), f4, font=fnt(_RBo, 18), fill=TEAL, anchor='rm')

    # Floating phone
    px2, py2, pw2, ph2 = phone_mockup(d, 1110, 360, 200)
    d2.text((px2+pw2//2, py2+22), 'Invoice #042', font=fnt(_RBo, 18), fill=NAVY, anchor='mm')
    d2.text((px2+pw2//2, py2+72), '€1,200.00', font=fnt(_RB, 36), fill=TEAL, anchor='mm')
    rr(d2, [px2+16, py2+110, px2+pw2-16, py2+142], 10, GREEN)
    d2.text((px2+pw2//2, py2+126), 'PAID', font=fnt(_RCB, 20), fill=WHITE, anchor='mm')

    # NOVAOPS wordmark on left panel
    d.text((60, H-80), 'NOVAOPS', font=fnt(_RB, 40), fill=TEAL, anchor='lt')
    d.text((60, H-36), 'Bookkeeper Practice Launch System  ·  v3.0', font=fnt(_RR, 24), fill=MUTED, anchor='lt')

    img.save(f'{OUT}/10-Final-CTA.jpg', quality=95)
    print('  ✓ 10-Final-CTA.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# RUN ALL
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print(f'Generating 10 premium Etsy listing images → {OUT}')
    img01_hero()
    img02_included()
    img03_dashboard()
    img04_notion()
    img05_financial()
    img06_client()
    img07_workflow()
    img08_assets()
    img09_audience()
    img10_cta()
    print('All 10 images complete.')
