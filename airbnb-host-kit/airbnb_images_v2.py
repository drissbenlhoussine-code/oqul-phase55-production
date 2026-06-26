"""
Airbnb Host Starter Kit — Premium Etsy Listing Images v2
Quality standard: Apple / Stripe / Linear
Dark mode. Device mockups. Real UI. Premium depth.
2700 × 1800 px, JPEG quality=96
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = '/home/user/oqul-phase55-production/airbnb-host-kit/output/etsy-images-v2'
os.makedirs(OUT, exist_ok=True)
W, H = 2700, 1800

# ── Palette ────────────────────────────────────────────────────────────────
BG      = (6,   8,  18)
BG_2    = (10,  14, 30)
BG_3    = (15,  22, 48)
PNL     = (18,  27, 58)
PNL_2   = (25,  36, 76)
PNL_3   = (34,  48, 96)
LINE    = (32,  46, 88)

TEAL    = ( 0, 200, 182)
TEAL_D  = ( 0, 130, 116)
TEAL_GL = ( 0, 200, 182)
CYAN    = (14, 165, 233)
BLUE    = (99, 102, 241)
AMBER   = (251, 191, 36)
AMBER_D = (180, 130, 18)
GREEN   = ( 34, 197, 94)
GREEN_D = ( 22, 140, 60)
RED     = (239,  68, 68)
PURPLE  = (139,  92, 246)

WHITE   = (255, 255, 255)
SL      = (148, 163, 184)
SL_D    = (100, 116, 139)
SL_DD   = ( 64,  80, 110)

MAC_LID  = (44, 46, 52)
MAC_BZL  = (16, 18, 22)
MAC_BASE = (38, 40, 46)
MAC_KB   = (28, 30, 34)
IPAD_FRM = (42, 44, 50)
PHONE_FRM= (34, 36, 42)

FD = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/'
F_BK = FD + 'Roboto-Black.ttf'
F_BO = FD + 'Roboto-Bold.ttf'
F_MD = FD + 'Roboto-Medium.ttf'
F_RG = FD + 'Roboto-Regular.ttf'
F_LT = FD + 'Roboto-Light.ttf'
F_CN = FD + 'RobotoCondensed-Bold.ttf'

def f(path, size): return ImageFont.truetype(path, size)

def save(img, name):
    img.save(f'{OUT}/{name}', quality=96)
    print(f'  ✓ {name}')

# ── Core helpers ────────────────────────────────────────────────────────────

def grad_bg(img, top=BG, bot=BG_3):
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(top[i] + t * (bot[i] - top[i])) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)

def dot_grid(img, gap=80, alpha=10):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d  = ImageDraw.Draw(ov)
    for x in range(0, W, gap):
        for y in range(0, H, gap):
            d.ellipse([x-1, y-1, x+1, y+1], fill=(255, 255, 255, alpha))
    return Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')

def glow(img, cx, cy, r, col, s=55):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d  = ImageDraw.Draw(ov)
    for i in range(12, 0, -1):
        rr = r * i // 12
        a  = int(s * (1 - i / 12) ** 1.4)
        d.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], fill=col[:3] + (a,))
    ov = ov.filter(ImageFilter.GaussianBlur(r // 6))
    return Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')

def drop_sh(img, x1, y1, x2, y2, blur=55, a=170, dy=18):
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d  = ImageDraw.Draw(sh)
    d.rounded_rectangle([x1+6, y1+dy, x2-6, y2+dy+10], radius=18, fill=(0, 0, 0, a))
    sh = sh.filter(ImageFilter.GaussianBlur(blur // 3))
    return Image.alpha_composite(img.convert('RGBA'), sh).convert('RGB')

def glass_card(img, x1, y1, x2, y2, r=18, fa=20, oa=55):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d  = ImageDraw.Draw(ov)
    d.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=(255, 255, 255, fa))
    d.rounded_rectangle([x1, y1, x2, y2], radius=r, outline=(255, 255, 255, oa), width=1)
    return Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')

def dark_card(img, x1, y1, x2, y2, r=18, fill=PNL, accent=None, outline_a=28):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    d  = ImageDraw.Draw(ov)
    d.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=fill + (255,))
    d.rounded_rectangle([x1, y1, x2, y2], radius=r, outline=(255, 255, 255, outline_a), width=1)
    if accent:
        d.rectangle([x1+1, y1+1, x1+4, y2-1], fill=accent + (255,))
    return Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')

def pill(img, x, y, text, bg=TEAL, fg=BG, sz=24):
    d  = ImageDraw.Draw(img)
    fn = f(F_BO, sz)
    bb = d.textbbox((0, 0), text, font=fn)
    tw, th = bb[2]-bb[0], bb[3]-bb[1]
    px, py = 20, 9
    x2, y2 = x + tw + px*2, y + th + py*2
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    dd = ImageDraw.Draw(ov)
    dd.rounded_rectangle([x, y, x2, y2], radius=(y2-y)//2, fill=bg + (255,))
    img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
    ImageDraw.Draw(img).text((x + px, y + py - 1), text, fill=fg, font=fn)
    return img, x2

def check_row(d, x, y, text, done=True, sz=30):
    col = GREEN if done else SL_D
    bx, by = x, y + 4
    if done:
        d.rounded_rectangle([bx, by, bx+22, by+22], radius=4, fill=GREEN)
        d.text((bx+11, by+11), '✓', fill=BG, font=f(F_BO, 14), anchor='mm')
    else:
        d.rounded_rectangle([bx, by, bx+22, by+22], radius=4,
                             outline=SL_D, width=2, fill=PNL_2)
    d.text((x+34, y+1), text, fill=WHITE if done else SL, font=f(F_RG, sz))

def tl(d, x, y, text, col=TEAL, sz=28):
    d.text((x, y), text, fill=col, font=f(F_MD, sz))

# ── MacBook Pro mockup ──────────────────────────────────────────────────────

def macbook(img, cx, cy, sw=1400, sh=880):
    """Draw premium frontal MacBook Pro. Returns (img, sx, sy, sw, sh)."""
    BT, BS, BB = 14, 11, 20
    BASE_H, NOTCH_W, NOTCH_H = 82, 92, 12

    lid_w = sw + BS * 2
    lid_h = sh + BT + BB
    lx    = cx - lid_w // 2
    ly    = cy - (lid_h + BASE_H) // 2

    img = drop_sh(img, lx-30, ly-10, lx+lid_w+30, ly+lid_h+BASE_H+10, blur=110, a=200, dy=30)
    d   = ImageDraw.Draw(img)

    # Lid
    d.rounded_rectangle([lx, ly, lx+lid_w, ly+lid_h], radius=13, fill=MAC_LID)
    # Bezel
    d.rounded_rectangle([lx+2, ly+2, lx+lid_w-2, ly+lid_h-2], radius=11, fill=MAC_BZL)
    # Screen area (placeholder — will be filled by UI)
    sx, sy_s = lx+BS, ly+BT
    d.rectangle([sx, sy_s, sx+sw, sy_s+sh], fill=BG)

    # Notch
    nx = cx - NOTCH_W // 2
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    dd = ImageDraw.Draw(ov)
    dd.rounded_rectangle([nx, ly-1, nx+NOTCH_W, ly+NOTCH_H+2],
                          radius=6, fill=MAC_LID + (255,))
    img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
    d   = ImageDraw.Draw(img)

    # Camera dot
    d.ellipse([cx-4, ly+BT//2-4, cx+4, ly+BT//2+4], fill=(14, 16, 20))

    # Hinge
    d.rectangle([lx, ly+lid_h, lx+lid_w, ly+lid_h+3], fill=(20, 22, 26))

    # Base
    bx1, by1 = lx+22, ly+lid_h+3
    bx2, by2 = lx+lid_w-22, by1+BASE_H
    d.rounded_rectangle([bx1, by1, bx2, by2], radius=10, fill=MAC_BASE)

    # Keyboard rows
    kb_l, kb_r = bx1+38, bx2-38
    kb_t, kb_b = by1+7,  by2-28
    rows, keys = 4, 16
    rh_k = (kb_b - kb_t) // rows
    kw_t = kb_r - kb_l
    for row in range(rows):
        ky = kb_t + row * rh_k + 2
        kw = kw_t // keys - 4
        for k in range(keys):
            kx = kb_l + k * (kw_t // keys) + 2
            d.rounded_rectangle([kx, ky, kx+kw, ky+rh_k-6], radius=2, fill=MAC_KB)

    # Trackpad
    tpw, tph = 256, 36
    tpx, tpy = cx - tpw//2, by2 - tph - 8
    d.rounded_rectangle([tpx, tpy, tpx+tpw, tpy+tph], radius=6,
                         outline=(26, 28, 32), width=1, fill=MAC_BASE)

    # Screen edge glow
    img = glow(img, cx, sy_s+sh//2, sh//2+60, CYAN, s=28)
    d   = ImageDraw.Draw(img)
    d.rectangle([sx, sy_s, sx+sw, sy_s+sh], fill=BG)

    return img, sx, sy_s, sw, sh


def ipad(img, cx, cy, sw=1600, sh=1100):
    """Draw iPad Pro landscape. Returns (img, sx, sy, sw, sh)."""
    BZL_H, BZL_V = 28, 22
    lid_w = sw + BZL_H * 2
    lid_h = sh + BZL_V * 2
    lx    = cx - lid_w // 2
    ly    = cy - lid_h // 2

    img = drop_sh(img, lx-20, ly-8, lx+lid_w+20, ly+lid_h+8, blur=80, a=180, dy=20)
    d   = ImageDraw.Draw(img)
    d.rounded_rectangle([lx, ly, lx+lid_w, ly+lid_h], radius=20, fill=IPAD_FRM)
    d.rounded_rectangle([lx+2, ly+2, lx+lid_w-2, ly+lid_h-2], radius=18, fill=MAC_BZL)
    sx, sy_s = lx+BZL_H, ly+BZL_V
    d.rectangle([sx, sy_s, sx+sw, sy_s+sh], fill=BG)

    # Camera (landscape right side)
    d.ellipse([lx+lid_w-BZL_H//2-4, ly+lid_h//2-4,
               lx+lid_w-BZL_H//2+4, ly+lid_h//2+4], fill=(14, 16, 20))
    # Home bar bottom center
    hb_w = 100
    d.rounded_rectangle([cx-hb_w//2, ly+lid_h-8, cx+hb_w//2, ly+lid_h-4],
                         radius=3, fill=(52, 54, 60))

    img = glow(img, cx, sy_s+sh//2, sh//3, CYAN, s=20)
    d   = ImageDraw.Draw(img)
    d.rectangle([sx, sy_s, sx+sw, sy_s+sh], fill=BG)

    return img, sx, sy_s, sw, sh


def iphone(img, cx, cy, sw=420, sh=900):
    """Draw iPhone vertical. Returns (img, sx, sy, sw, sh)."""
    BZL = 20
    DI_W, DI_H = 120, 30
    lid_w = sw + BZL * 2
    lid_h = sh + BZL * 2
    lx    = cx - lid_w // 2
    ly    = cy - lid_h // 2

    img = drop_sh(img, lx-14, ly-6, lx+lid_w+14, ly+lid_h+6, blur=50, a=150, dy=14)
    d   = ImageDraw.Draw(img)
    d.rounded_rectangle([lx, ly, lx+lid_w, ly+lid_h], radius=52, fill=PHONE_FRM)
    d.rounded_rectangle([lx+2, ly+2, lx+lid_w-2, ly+lid_h-2], radius=50, fill=MAC_BZL)
    sx, sy_s = lx+BZL, ly+BZL
    d.rounded_rectangle([sx, sy_s, sx+sw, sy_s+sh], radius=34, fill=BG)

    # Dynamic island
    dix = cx - DI_W//2
    diy = sy_s + 10
    d.rounded_rectangle([dix, diy, dix+DI_W, diy+DI_H], radius=DI_H//2, fill=MAC_BZL)

    # Side buttons
    d.rounded_rectangle([lx-4, ly+220, lx, ly+340], radius=3, fill=(34, 36, 42))  # power
    d.rounded_rectangle([lx+lid_w, ly+200, lx+lid_w+4, ly+290], radius=3, fill=(34, 36, 42))

    # Home indicator
    hi_w = 100
    d.rounded_rectangle([cx-hi_w//2, sy_s+sh-16, cx+hi_w//2, sy_s+sh-8],
                         radius=3, fill=(52, 54, 60))

    img = glow(img, cx, sy_s+sh//2, sh//3, CYAN, s=22)
    d   = ImageDraw.Draw(img)
    d.rounded_rectangle([sx, sy_s, sx+sw, sy_s+sh], radius=34, fill=BG)

    return img, sx, sy_s, sw, sh


# ── UI renderers ────────────────────────────────────────────────────────────

def ui_dashboard(img, sx, sy, sw, sh):
    d = ImageDraw.Draw(img)
    SB = sw // 7
    TB = sh // 9

    d.rectangle([sx, sy, sx+sw, sy+sh], fill=BG)
    d.rectangle([sx, sy, sx+SB, sy+sh], fill=(9, 12, 26))
    d.line([(sx+SB, sy), (sx+SB, sy+sh)], fill=LINE, width=1)

    # Logo
    d.rounded_rectangle([sx+10, sy+10, sx+SB-10, sy+52], radius=8, fill=TEAL)
    d.text((sx+SB//2, sy+31), 'AH', fill=BG, font=f(F_BO, 20), anchor='mm')

    # Nav
    nav = [('⌂', True), ('📅', False), ('✉', False), ('📊', False), ('⚙', False)]
    for i, (ic, act) in enumerate(nav):
        ny = sy + 68 + i * 66
        if act:
            d.rounded_rectangle([sx+7, ny-3, sx+SB-7, ny+42], radius=7, fill=TEAL_D + (70,))
            d.rectangle([sx+2, ny+6, sx+5, ny+36], fill=TEAL)
        d.text((sx+SB//2, ny+20), ic, fill=TEAL if act else SL_D,
               font=f(F_MD, int(TB * 0.48)), anchor='mm')

    # Top bar
    d.rectangle([sx+SB, sy, sx+sw, sy+TB], fill=(8, 10, 22))
    d.line([(sx+SB, sy+TB), (sx+sw, sy+TB)], fill=LINE, width=1)
    d.text((sx+SB+16, sy+TB//2), 'Host Dashboard', fill=WHITE,
           font=f(F_BO, int(TB * 0.38)), anchor='lm')
    d.text((sx+SB+200, sy+TB//2), '/ Villa Serena', fill=TEAL,
           font=f(F_RG, int(TB * 0.3)), anchor='lm')
    avx = sx + sw - 22
    avy = sy + TB // 2
    d.ellipse([avx-16, avy-16, avx+16, avy+16], fill=TEAL)
    d.text((avx, avy), 'S', fill=BG, font=f(F_BO, int(TB * 0.38)), anchor='mm')

    # KPI row
    KY  = sy + TB + 12
    KH  = sh // 5
    CW  = sw - SB
    KW  = CW // 4
    kpis = [
        ('$3,240', 'Monthly Revenue', TEAL,  '+12% ▲'),
        ('92%',    'Occupancy',       AMBER, 'peak season'),
        ('4.9 ★',  'Host Rating',     GREEN, 'top 1%'),
        ('18',     'Bookings YTD',    BLUE,  '+3 this month'),
    ]
    for i, (val, lbl, col, note) in enumerate(kpis):
        kx = sx + SB + i * KW + 6
        d.rounded_rectangle([kx, KY, kx+KW-12, KY+KH-12], radius=8, fill=PNL)
        d.rectangle([kx+1, KY+1, kx+KW-13, KY+3], fill=col)
        d.text((kx+13, KY+KH*2//5), val,  fill=WHITE, font=f(F_BO, int(KH * 0.34)), anchor='lm')
        d.text((kx+13, KY+KH*3//5), lbl,  fill=SL,    font=f(F_RG, int(KH * 0.18)), anchor='lm')
        d.text((kx+13, KY+KH*4//5), note, fill=col,   font=f(F_RG, int(KH * 0.14)), anchor='lm')

    # Chart + panel
    CHY  = KY + KH + 8
    CHH  = sh - (CHY - sy) - 12
    CHX  = sx + SB + 8
    CHW  = CW * 11 // 16
    RPX  = CHX + CHW + 8
    RPW  = CW - CHW - 20

    d.rounded_rectangle([CHX, CHY, CHX+CHW, CHY+CHH], radius=8, fill=PNL)
    d.text((CHX+14, CHY+12), 'Revenue Overview', fill=WHITE,
           font=f(F_BO, int(CHH * 0.1)))

    vals   = [1800, 2400, 1950, 2700, 2100, 3240]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    bax1, bax2 = CHX+14, CHX+CHW-14
    bay1, bay2 = CHY+int(CHH*0.28), CHY+CHH-28
    bw_s = (bax2 - bax1) // len(vals)
    mxv  = max(vals)

    for gi in range(4):
        gy = bay1 + gi * (bay2-bay1)//3
        d.line([(bax1, gy), (bax2, gy)], fill=LINE, width=1)
        d.text((bax1-6, gy), f'${int(mxv*(1-gi/3))//1000}k', fill=SL_D,
               font=f(F_RG, int(CHH*0.08)), anchor='rm')

    for i, (v, mo) in enumerate(zip(vals, months)):
        bx  = bax1 + i * bw_s + 8
        bh_ = int((v/mxv)*(bay2-bay1-8))
        by  = bay2 - bh_
        is_last = (i == len(vals)-1)
        d.rounded_rectangle([bx, by, bx+bw_s-16, bay2], radius=4,
                             fill=TEAL if is_last else TEAL_D)
        if is_last:
            d.text((bx+(bw_s-16)//2, by-9), f'${v:,}', fill=AMBER,
                   font=f(F_BO, int(CHH*0.1)), anchor='mb')
        d.text((bx+(bw_s-16)//2, bay2+7), mo, fill=SL,
               font=f(F_RG, int(CHH*0.08)), anchor='mt')

    # Right panel
    d.rounded_rectangle([RPX, CHY, RPX+RPW, CHY+CHH], radius=8, fill=PNL)
    d.text((RPX+12, CHY+12), 'Upcoming Stays', fill=WHITE,
           font=f(F_BO, int(CHH*0.1)))
    guests = [('Sarah M.', 'Jun 28 – Jul 1',  3, GREEN),
              ('James T.', 'Jul 4 – Jul 11',  7, AMBER),
              ('Emma K.', 'Jul 12 – Jul 14',  2, CYAN)]
    gh_s = (CHH - 48) // 3
    for j, (g, dates, n, col) in enumerate(guests):
        gy = CHY + 44 + j * gh_s
        d.rounded_rectangle([RPX+8, gy, RPX+RPW-8, gy+gh_s-8], radius=6, fill=PNL_2)
        d.ellipse([RPX+18, gy+10, RPX+34, gy+26], fill=col)
        d.text((RPX+44, gy+6),  g,     fill=WHITE, font=f(F_MD, int(gh_s*0.25)))
        d.text((RPX+44, gy+30), dates, fill=SL,    font=f(F_RG, int(gh_s*0.2)))
        d.text((RPX+RPW-14, gy+gh_s//2), f'{n}n',
               fill=col, font=f(F_BO, int(gh_s*0.22)), anchor='rm')
    return img


def ui_templates(img, sx, sy, sw, sh):
    d = ImageDraw.Draw(img)
    SB = sw // 4
    d.rectangle([sx, sy, sx+sw, sy+sh], fill=BG)
    d.rectangle([sx, sy, sx+SB, sy+sh], fill=(9, 12, 26))
    d.line([(sx+SB, sy), (sx+SB, sy+sh)], fill=LINE, width=1)

    d.text((sx+14, sy+14), 'Templates', fill=WHITE, font=f(F_BO, int(sh*0.06)))
    d.line([(sx, sy+52), (sx+SB, sy+52)], fill=LINE, width=1)

    tmpls = ['Booking Confirmation', 'Pre-Arrival Guide', 'Welcome Message',
             'Check-in Reminder', 'Day-Before Checkout', '5-Star Review Request',
             'Noise Complaint Response', 'Returning Guest Offer']
    th_s = (sh - 60) // len(tmpls)
    for i, t in enumerate(tmpls):
        ty = sy + 58 + i * th_s
        active = (i == 0)
        if active:
            d.rounded_rectangle([sx+5, ty+2, sx+SB-5, ty+th_s-4], radius=6,
                                 fill=TEAL_D + (80,))
            d.rectangle([sx+2, ty+8, sx+5, ty+th_s-10], fill=TEAL)
        d.text((sx+18, ty+th_s//2), t, fill=WHITE if active else SL,
               font=f(F_MD if active else F_RG, int(th_s*0.38)), anchor='lm')

    # Template preview
    mx, my = sx+SB+18, sy+14
    mw = sw - SB - 28
    d.text((mx, my), '📧  Booking Confirmation', fill=WHITE,
           font=f(F_BO, int(sh*0.062)))
    d.line([(mx, my+50), (sx+sw-10, my+50)], fill=LINE, width=1)

    d.text((mx,    my+68), 'Subject:', fill=SL_D, font=f(F_RG, int(sh*0.04)))
    d.text((mx+130, my+68), 'Your Booking is Confirmed! 🏡', fill=WHITE,
           font=f(F_MD, int(sh*0.04)))

    d.rounded_rectangle([mx, my+108, sx+sw-12, sy+sh-12], radius=10, fill=PNL)
    body = [
        'Hi [GUEST_NAME],',
        '',
        'Great news — your reservation is confirmed! 🎉',
        '',
        '📍  Address:      [YOUR_FULL_ADDRESS]',
        '📅  Check-in:     [DATE] after [TIME]',
        '📅  Check-out:    [DATE] by [TIME]',
        '🔑  Entry code:   [LOCKBOX_CODE]',
        '',
        '🅿️   Parking:      [PARKING_INSTRUCTIONS]',
        '📶  WiFi name:    [NETWORK_NAME]',
        '🔐  WiFi pass:    [PASSWORD]',
        '',
        'Message me anytime — happy to help!',
        '[YOUR_NAME]',
    ]
    lh = int(sh * 0.044)
    for i, line in enumerate(body[:14]):
        lx = mx + 18
        ly = my + 126 + i * lh
        is_var = '[' in line
        is_icon = line.startswith(('📍', '📅', '🔑', '🅿', '📶', '🔐'))
        col = TEAL if is_var else (SL if is_icon else WHITE)
        if not line:
            continue
        d.text((lx, ly), line, fill=col, font=f(F_RG, int(sh*0.038)))
    return img


def ui_pricing(img, sx, sy, sw, sh):
    d = ImageDraw.Draw(img)
    d.rectangle([sx, sy, sx+sw, sy+sh], fill=BG)

    TB = sh // 9
    d.rectangle([sx, sy, sx+sw, sy+TB], fill=(8, 10, 22))
    d.line([(sx, sy+TB), (sx+sw, sy+TB)], fill=LINE, width=1)
    d.text((sx+16, sy+TB//2), 'Pricing Calculator', fill=WHITE,
           font=f(F_BO, int(TB*0.42)), anchor='lm')
    d.text((sx+sw-16, sy+TB//2), '📈  Revenue Optimizer', fill=TEAL,
           font=f(F_RG, int(TB*0.3)), anchor='rm')

    # Sheet tabs
    tabs = ['📊 Dashboard', '📅 Bookings', '💰 Expenses',
            '🧮 Pricing', '🧹 Cleaning', '⭐ Reviews']
    TH = 30
    TY = sy + TB
    tw = sw // len(tabs)
    for i, tab in enumerate(tabs):
        tx = sx + i * tw
        act = (i == 3)
        d.rectangle([tx, TY, tx+tw, TY+TH], fill=TEAL_D if act else PNL_2)
        d.text((tx+tw//2, TY+TH//2), tab, fill=WHITE if act else SL_D,
               font=f(F_BO if act else F_RG, 17), anchor='mm')
        if i < len(tabs)-1:
            d.line([(tx+tw, TY), (tx+tw, TY+TH)], fill=LINE, width=1)
    d.line([(sx, TY+TH), (sx+sw, TY+TH)], fill=LINE, width=1)

    CY = sy + TB + TH + 16
    CW = sw - 40
    col_w = CW // 2

    d.text((sx+20, CY), 'Monthly Cost Inputs', fill=WHITE, font=f(F_BO, int(sh*0.055)))

    inputs_data = [
        ('Mortgage / Rent',      '$2,400'),
        ('Utilities',            '$320'),
        ('Cleaning (per stay)',  '$85'),
        ('Platform Fees (3%)',   'auto'),
        ('Insurance',            '$180'),
        ('Supplies / Month',     '$60'),
        ('HOA / Misc',           '$150'),
    ]
    RH = int(sh * 0.09)
    for i, (label, val) in enumerate(inputs_data):
        ry = CY + 56 + i * RH
        d.rounded_rectangle([sx+20, ry, sx+col_w-10, ry+RH-8], radius=6, fill=PNL)
        d.text((sx+34, ry+RH//2), label, fill=SL,
               font=f(F_RG, int(RH*0.35)), anchor='lm')
        is_auto = val == 'auto'
        d.text((sx+col_w-24, ry+RH//2), val,
               fill=TEAL if is_auto else AMBER,
               font=f(F_BO, int(RH*0.35)), anchor='rm')

    # Results
    rx = sx + col_w + 20
    d.text((rx, CY), 'Recommended Rates', fill=WHITE, font=f(F_BO, int(sh*0.055)))

    results = [
        ('Break-Even Rate',  '$142/night', SL,    'covers all monthly costs'),
        ('Recommended Rate', '$185/night', TEAL,  '30% above break-even'),
        ('Peak Season',      '$240/night', AMBER, 'holidays & long weekends'),
        ('Off-Season',       '$155/night', BLUE,  'maintain occupancy'),
        ('Monthly Target',   '$3,800',     GREEN, 'at 85% occupancy rate'),
    ]
    for i, (label, val, col, note) in enumerate(results):
        ry = CY + 56 + i * int(RH * 1.12)
        d.rounded_rectangle([rx, ry, sx+sw-20, ry+RH], radius=6, fill=PNL)
        d.rectangle([rx+1, ry+1, rx+4, ry+RH-1], fill=col)
        d.text((rx+16, ry+RH//3), label, fill=SL, font=f(F_RG, int(RH*0.32)), anchor='lm')
        d.text((rx+16, ry+RH*2//3), note, fill=SL_D, font=f(F_RG, int(RH*0.24)), anchor='lm')
        d.text((sx+sw-24, ry+RH//2), val, fill=col,
               font=f(F_BO, int(RH*0.38)), anchor='rm')
    return img


def ui_house_manual(img, sx, sy, sw, sh):
    d = ImageDraw.Draw(img)
    d.rectangle([sx, sy, sx+sw, sy+sh], fill=BG)

    TB = sh // 8
    d.rectangle([sx, sy, sx+sw, sy+TB], fill=TEAL_D)
    d.text((sx+20, sy+TB//2), '🏡  Villa Serena — Guest Manual', fill=WHITE,
           font=f(F_BO, int(TB*0.45)), anchor='lm')
    d.text((sx+sw-20, sy+TB//2), 'Your home away from home', fill=(200, 255, 248),
           font=f(F_LT, int(TB*0.32)), anchor='rm')

    cols = [
        [('🔑 Check-In', [
            'Self check-in · no key needed',
            'Lockbox code: [4-DIGIT CODE]',
            'Located: front door, right side',
            'Reset to 0000 after entering',
         ]),
         ('📶 WiFi & Entertainment', [
            'Network:  VillaNest_Guest',
            'Password: [WIFI_PASSWORD]',
            'Smart TV: use guest profile',
            'Netflix included for your stay',
         ])],
        [('🚗 Parking & Access', [
            'Private driveway: up to 2 cars',
            'Street parking: free after 6pm',
            'EV charger available — ask us',
         ]),
         ('⚠️ House Rules', [
            'No smoking indoors',
            'No pets (allergies)',
            'Quiet hours: 10pm – 8am',
            'Maximum 6 guests at all times',
         ])]
    ]
    col_w = sw // 2 - 10

    def draw_sec(sections, start_x, start_y):
        y = start_y
        for title, items in sections:
            d.text((start_x+12, y), title, fill=TEAL, font=f(F_BO, int(sh*0.052)))
            y += int(sh*0.062)
            for item in items:
                d.text((start_x+26, y), '·  ' + item, fill=SL,
                       font=f(F_RG, int(sh*0.04)))
                y += int(sh*0.048)
            y += 14

    draw_sec(cols[0], sx+4,          sy+TB+14)
    draw_sec(cols[1], sx+col_w+16,   sy+TB+14)

    rec_y = sy + sh - int(sh*0.26)
    d.line([(sx, rec_y-6), (sx+sw, rec_y-6)], fill=LINE, width=1)
    d.text((sx+14, rec_y), '📍 Local Recommendations', fill=AMBER,
           font=f(F_BO, int(sh*0.052)))
    recs = [('Café Miel', 'Best coffee, 3 min walk'),
            ('Trattoria da Luca', 'Italian, 5 min drive'),
            ('City Sunrise Park', 'Morning walks, highly rated')]
    for i, (name, note) in enumerate(recs):
        rx = sx + 14 + i * (sw // 3)
        ry = rec_y + int(sh*0.065)
        d.text((rx, ry),             name, fill=WHITE, font=f(F_MD, int(sh*0.04)))
        d.text((rx, ry+int(sh*0.045)), note, fill=SL_D,  font=f(F_RG, int(sh*0.033)))
    return img


def ui_sop(img, sx, sy, sw, sh):
    d = ImageDraw.Draw(img)
    d.rectangle([sx, sy, sx+sw, sy+sh], fill=BG)

    d.rectangle([sx, sy, sx+sw, sy+sh//9], fill=(9, 12, 26))
    d.text((sx+14, sy+sh//18), '✓  Cleaning SOP — Full Turnover Protocol',
           fill=WHITE, font=f(F_BO, int(sh*0.062)), anchor='lm')
    d.line([(sx, sy+sh//9), (sx+sw, sy+sh//9)], fill=LINE, width=1)

    rooms_l = [
        ('Living Room', [
            ('Vacuum sofas and cushions', True),
            ('Wipe coffee table and surfaces', True),
            ('Check under cushions for items', True),
            ('Replace throw pillow arrangement', False),
            ('Spot-clean walls and baseboards', False),
        ]),
        ('Kitchen', [
            ('Clean stovetop — all burners', True),
            ('Empty and wipe refrigerator', True),
            ('Run dishwasher, empty and put away', True),
            ('Restock coffee pods and sugar', False),
            ('Wipe inside microwave', False),
        ]),
    ]
    rooms_r = [
        ('Master Bedroom', [
            ('Change all bedding and pillowcases', True),
            ('Vacuum under and around bed', True),
            ('Check drawers for personal items', False),
            ('Set thermostat to 70°F', False),
        ]),
        ('Bathroom', [
            ('Deep clean toilet inside and out', True),
            ('Clean shower glass — no streaks', True),
            ('Replace towels: 2 sets per guest', True),
            ('Restock toiletries kit', False),
            ('Polish mirror and chrome fixtures', False),
        ]),
    ]

    def draw_cl(rooms_data, ox):
        y = sy + sh//9 + 14
        RH_C = int(sh * 0.076)
        for room, items in rooms_data:
            d.text((ox+12, y), room, fill=AMBER, font=f(F_BO, int(sh*0.052)))
            y += int(sh*0.062)
            for text, done in items:
                bx, by = ox+12, y+4
                if done:
                    d.rounded_rectangle([bx, by, bx+20, by+20], radius=4, fill=GREEN)
                    d.text((bx+10, by+10), '✓', fill=BG, font=f(F_BO, 13), anchor='mm')
                else:
                    d.rounded_rectangle([bx, by, bx+20, by+20], radius=4,
                                         outline=SL_D, width=2, fill=PNL_2)
                d.text((ox+42, y+1), text, fill=WHITE if done else SL,
                       font=f(F_RG if done else F_LT, int(sh*0.04)))
                y += RH_C
            y += 10

    draw_cl(rooms_l, sx+8)
    draw_cl(rooms_r, sx+sw//2+6)

    # Progress bar at bottom
    py = sy + sh - 38
    d.rounded_rectangle([sx+14, py, sx+sw-14, py+22], radius=11, fill=PNL_2)
    prog_w = int((sw-28) * 0.6)
    d.rounded_rectangle([sx+14, py, sx+14+prog_w, py+22], radius=11, fill=TEAL)
    d.text((sx+sw//2, py+11), '60% complete — 3 rooms remaining',
           fill=WHITE, font=f(F_BO, 17), anchor='mm')
    return img


def ui_messages_phone(img, sx, sy, sw, sh):
    """iMessage-style message thread."""
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([sx, sy, sx+sw, sy+sh], radius=32, fill=BG)

    # Top bar
    d.text((sx+sw//2, sy+50), 'James T.', fill=WHITE,
           font=f(F_BO, int(sw*0.08)), anchor='mt')
    d.text((sx+sw//2, sy+90), '🟢 Active now', fill=GREEN,
           font=f(F_RG, int(sw*0.05)), anchor='mt')
    d.line([(sx+20, sy+110), (sx+sw-20, sy+110)], fill=LINE, width=1)

    msgs = [
        ('James',  'Hi! Just confirmed my booking for July 4–11. So excited!', False),
        ('You',    'Hi James! Welcome 🎉 Your booking is confirmed. Check-in is after 3pm.', True),
        ('You',    'I\'ll send full details 48hrs before arrival.', True),
        ('James',  'Perfect — do you have parking?', False),
        ('You',    'Yes! Private driveway for 2 cars. EV charger available too 🚗', True),
        ('James',  'Amazing. Can\'t wait!', False),
    ]
    y = sy + 130
    MH = int(sh * 0.12)
    for sender, text, is_me in msgs:
        bub_w = int(sw * 0.82)
        bg_col = TEAL_D if is_me else PNL_2
        align = 'right' if is_me else 'left'
        bx1 = (sx + sw - bub_w - 14) if is_me else (sx + 14)
        bx2 = bx1 + bub_w
        # Wrap text (very rough, 2 lines max)
        lines = [text[:50], text[50:]] if len(text) > 50 else [text]
        lines = [l for l in lines if l]
        bh = 20 + len(lines) * int(sw * 0.054)
        d.rounded_rectangle([bx1, y, bx2, y+bh], radius=16, fill=bg_col)
        for j, line in enumerate(lines):
            d.text((bx1+14, y+10+j*int(sw*0.054)), line, fill=WHITE,
                   font=f(F_RG, int(sw*0.048)))
        y += bh + 12
    return img


# ── Bar chart helper ─────────────────────────────────────────────────────────

def area_chart(img, x1, y1, x2, y2, vals, col=TEAL, fill_col=None):
    """Draw a line + area chart."""
    d   = ImageDraw.Draw(img)
    n   = len(vals)
    mx  = max(vals)
    mn  = min(vals) * 0.8
    pts = []
    for i, v in enumerate(vals):
        px = x1 + i * (x2-x1) // (n-1)
        py = y2 - int((v-mn)/(mx-mn) * (y2-y1) * 0.92)
        pts.append((px, py))

    # Fill area under line
    fill_pts = [(x1, y2)] + pts + [(x2, y2)]
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    dd = ImageDraw.Draw(ov)
    dd.polygon(fill_pts, fill=(col[0], col[1], col[2], 35))
    img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
    d   = ImageDraw.Draw(img)

    # Line
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill=col, width=4)

    # Dots
    for px, py in pts:
        d.ellipse([px-5, py-5, px+5, py+5], fill=col)

    return img, pts


# ── Image generators ─────────────────────────────────────────────────────────

def img01_hero():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W//2-200, H//2+80, 750, TEAL, s=42)
    img = glow(img, W//2+500, H//3, 500, CYAN, s=26)

    img, sx, sy, sw_m, sh_m = macbook(img, cx=W//2-120, cy=H//2+50, sw=1380, sh=860)
    img = ui_dashboard(img, sx, sy, sw_m, sh_m)
    img = glow(img, sx+sw_m//2, sy+sh_m//2, sh_m//2+80, CYAN, s=22)
    d = ImageDraw.Draw(img)
    d.rectangle([sx, sy, sx+sw_m, sy+sh_m], fill=None)  # let glow show

    img, _ = pill(img, 82, 66, '  AIRBNB HOST STARTER KIT  ', bg=TEAL, fg=BG, sz=26)
    d = ImageDraw.Draw(img)

    hx = W - 80
    d.text((hx, 168), 'The Complete', fill=SL,    font=f(F_MD, 52), anchor='rt')
    d.text((hx, 240), 'Airbnb Host', fill=WHITE,  font=f(F_BK, 108), anchor='rt')
    d.text((hx, 372), 'System.',     fill=TEAL,   font=f(F_BK, 108), anchor='rt')
    d.text((hx, 484), 'Run your property like a business.', fill=SL,
           font=f(F_RG, 38), anchor='rt')

    stat_cards = [
        ('$3,240/mo', 'Average monthly revenue', TEAL),
        ('4.9 ★',     'Host satisfaction rating', AMBER),
        ('92%',       'Peak season occupancy',    GREEN),
    ]
    for i, (val, lbl, col) in enumerate(stat_cards):
        cx1 = W - 80 - 440
        cy1 = 574 + i * 162
        img = drop_sh(img, cx1, cy1, cx1+440, cy1+130, blur=40, a=130, dy=10)
        img = dark_card(img, cx1, cy1, cx1+440, cy1+130, r=14, fill=PNL, accent=col)
        d = ImageDraw.Draw(img)
        d.text((cx1+20, cy1+36), val, fill=WHITE, font=f(F_BO, 48))
        d.text((cx1+20, cy1+94), lbl, fill=SL,    font=f(F_RG, 26))

    d = ImageDraw.Draw(img)
    d.rectangle([0, H-64, W, H], fill=PNL)
    d.line([(0, H-64), (W, H-64)], fill=LINE, width=1)
    items = ['9 Professional Tools', '100+ Ready Templates',
             '8-Sheet Dashboard', '⚡ Instant Download']
    for i, item in enumerate(items):
        ix = 200 + i * (W-400)//3
        d.text((ix, H-32), item, fill=SL, font=f(F_MD, 28), anchor='mm')
    save(img, '01-Hero.jpg')


def img02_problem_solved():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W*3//4+100, H//2, 650, TEAL, s=38)

    d = ImageDraw.Draw(img)
    d.text((W//2, 110), 'Stop Guessing.', fill=WHITE, font=f(F_BK, 112), anchor='mt')
    d.text((W//2, 248), 'Start Hosting.', fill=TEAL,  font=f(F_BK, 112), anchor='mt')
    d.text((W//2, 375),
           'One system that covers every corner of your short-term rental business.',
           fill=SL, font=f(F_RG, 40), anchor='mt')

    LY, LH = 460, H - 500

    # Left card: Without
    WL, WR = 60, W//2 - 55
    img = drop_sh(img, WL, LY, WR, LY+LH, blur=50, a=140, dy=14)
    img = dark_card(img, WL, LY, WR, LY+LH, r=18, fill=(16, 14, 28))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([WL, LY, WR, LY+52], radius=18, fill=(80,20,20))
    d.text((WL+(WR-WL)//2, LY+26), 'WITHOUT THIS KIT', fill=(255,100,100),
           font=f(F_CN, 32), anchor='mm')

    probs = ['Inconsistent guest communication',
             'No standard cleaning checklist',
             'Guessing at the right nightly rate',
             'Scrambling to reply to every guest',
             'No strategy for earning 5-star reviews',
             'Reinventing the wheel every booking',
             'Missing maintenance before it escalates',
             'Zero systems — just constant firefighting']
    ph = (LH - 66) // len(probs)
    for i, p in enumerate(probs):
        d.text((WL+22, LY+62+i*ph), '✗  ' + p, fill=(210,80,80), font=f(F_RG, 30))

    # Right card: With
    RL, RR = W//2 + 55, W - 60
    img = drop_sh(img, RL, LY, RR, LY+LH, blur=50, a=140, dy=14)
    img = dark_card(img, RL, LY, RR, LY+LH, r=18, fill=PNL)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([RL, LY, RR, LY+52], radius=18, fill=TEAL_D)
    d.text((RL+(RR-RL)//2, LY+26), 'WITH THIS KIT', fill=WHITE,
           font=f(F_CN, 32), anchor='mm')

    sols = ['15 proven templates — ready to copy & send',
            'Step-by-step room-by-room cleaning SOP',
            'Pricing calculator that finds your sweet spot',
            'Guest communication system that earns Superhost',
            'Review strategy that consistently gets 5 stars',
            'House Manual guests actually read and love',
            'Maintenance log before issues cost you money',
            'One organized system for everything']
    for i, s in enumerate(sols):
        d.text((RL+22, LY+62+i*ph), '✓  ' + s, fill=WHITE, font=f(F_MD, 30))

    save(img, '02-Problem-Solved.jpg')


def img03_whats_included():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W//2, H//2+100, 700, TEAL, s=30)

    d = ImageDraw.Draw(img)
    d.text((W//2, 56), 'Everything Included.', fill=WHITE, font=f(F_BK, 100), anchor='mt')
    d.text((W//2, 178), '9 premium tools. One complete short-term rental system.',
           fill=SL, font=f(F_RG, 40), anchor='mt')

    cards_data = [
        ('⚡', '00  Quick Start Guide',        '5-minute setup checklist',       TEAL),
        ('📋', '01  Listing Optimization',     'Title, photos, SEO secrets',     BLUE),
        ('✉',  '02  15 Message Templates',     'Copy-paste guest communication', PURPLE),
        ('📜', '03  House Rules Template',     'Professional guest boundaries',  AMBER),
        ('🏡', '04  House Manual',             'Digital welcome guide for guests',GREEN),
        ('🔑', '05  Check-In SOP',             '12-step arrival procedure',      CYAN),
        ('🧹', '06  Cleaning SOP',             'Room-by-room turnover protocol', RED),
        ('⭐', '07  Review Strategy Guide',   '5-star review system',           AMBER),
        ('📊', '08  Operations Dashboard',     '8-sheet Excel command center',   TEAL),
    ]

    COLS = 3
    ROWS = 3
    PAD  = 28
    card_w = (W - PAD * (COLS + 1)) // COLS
    card_h = (H - 280 - PAD * (ROWS + 1)) // ROWS
    start_y = 256

    for i, (ic, title, desc, col) in enumerate(cards_data):
        row, col_i = divmod(i, COLS)
        cx_ = PAD + col_i * (card_w + PAD)
        cy_ = start_y + row * (card_h + PAD)

        img = drop_sh(img, cx_, cy_, cx_+card_w, cy_+card_h, blur=30, a=120, dy=8)
        img = dark_card(img, cx_, cy_, cx_+card_w, cy_+card_h, r=16, fill=PNL, accent=col)
        d = ImageDraw.Draw(img)

        d.text((cx_+20, cy_+card_h//2 - 28), ic, fill=col,  font=f(F_MD, 44), anchor='lm')
        d.text((cx_+76, cy_+card_h//2 - 30), title, fill=WHITE,
               font=f(F_BO, 28), anchor='lm')
        d.text((cx_+76, cy_+card_h//2 + 10), desc,  fill=SL,
               font=f(F_RG, 24), anchor='lm')

    save(img, '03-Whats-Included.jpg')


def img04_dashboard():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W//2, H//2, 800, CYAN, s=25)

    img, sx, sy, sw_m, sh_m = macbook(img, cx=W//2, cy=H//2+60, sw=1700, sh=1062)
    img = ui_pricing(img, sx, sy, sw_m, sh_m)
    img = glow(img, sx+sw_m//2, sy+sh_m//2, sh_m//2, CYAN, s=18)
    d = ImageDraw.Draw(img)
    # Redraw screen edges clean
    d.rectangle([sx, sy, sx+1, sy+sh_m], fill=BG)
    d.rectangle([sx+sw_m-1, sy, sx+sw_m, sy+sh_m], fill=BG)

    img, _ = pill(img, 82, 62, '  OPERATIONS DASHBOARD  ', bg=TEAL, fg=BG, sz=26)
    d = ImageDraw.Draw(img)
    d.text((82, 132), 'Your entire operation,', fill=WHITE, font=f(F_BK, 80))
    d.text((82, 234), 'on one dashboard.',      fill=TEAL,  font=f(F_BK, 80))
    d.text((82, 330), '8 professional sheets. Built for serious hosts.', fill=SL,
           font=f(F_RG, 36))

    # Badge: 8 sheets
    img = drop_sh(img, W-380, H-160, W-60, H-60, blur=25, a=110, dy=8)
    img = dark_card(img, W-380, H-160, W-60, H-60, r=14, fill=PNL, accent=AMBER)
    d = ImageDraw.Draw(img)
    d.text((W-220, H-130), '8 Sheets', fill=WHITE, font=f(F_BO, 34), anchor='mm')
    d.text((W-220, H-88),  '100% formula-driven', fill=SL, font=f(F_RG, 24), anchor='mm')

    save(img, '04-Dashboard.jpg')


def img05_workflow():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W//2, H//2, 750, PURPLE, s=32)
    img = glow(img, W//2-300, H//2+100, 400, TEAL, s=28)

    # iPhone center
    img, sx, sy, sw_p, sh_p = iphone(img, cx=W//2, cy=H//2+60, sw=440, sh=930)
    img = ui_messages_phone(img, sx, sy, sw_p, sh_p)

    d = ImageDraw.Draw(img)

    img, _ = pill(img, 82, 62, '  GUEST COMMUNICATION  ', bg=PURPLE, fg=WHITE, sz=26)
    d = ImageDraw.Draw(img)

    d.text((82,  138), 'Reply faster.', fill=WHITE, font=f(F_BK, 96))
    d.text((82,  258), 'Earn 5 stars.', fill=TEAL,  font=f(F_BK, 96))
    d.text((82,  368), '15 done-for-you message templates.', fill=SL, font=f(F_RG, 38))
    d.text((82,  420), 'Every situation. Every guest type.', fill=SL, font=f(F_RG, 38))

    # Right: stats
    stats = [
        ('15',  'Message templates ready', TEAL),
        ('4.8★', 'Avg communication rating', AMBER),
        ('<30s', 'Average response time',   GREEN),
    ]
    for i, (val, lbl, col) in enumerate(stats):
        cx1 = W - 520
        cy1 = 500 + i * 160
        img = drop_sh(img, cx1, cy1, cx1+440, cy1+130, blur=35, a=120, dy=10)
        img = dark_card(img, cx1, cy1, cx1+440, cy1+130, r=14, fill=PNL, accent=col)
        d = ImageDraw.Draw(img)
        d.text((cx1+20, cy1+36), val, fill=WHITE, font=f(F_BO, 48))
        d.text((cx1+20, cy1+93), lbl, fill=SL,    font=f(F_RG, 26))

    save(img, '05-Workflow.jpg')


def img06_templates():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W//2-200, H//2, 700, BLUE, s=30)

    img, sx, sy, sw_m, sh_m = macbook(img, cx=W//2-100, cy=H//2+50, sw=1380, sh=860)
    img = ui_templates(img, sx, sy, sw_m, sh_m)
    img = glow(img, sx+sw_m//2, sy+sh_m//2, sh_m//2+60, BLUE, s=16)

    d = ImageDraw.Draw(img)
    img, _ = pill(img, W-620, 66, '  15 TEMPLATES  ', bg=BLUE, fg=WHITE, sz=26)
    d = ImageDraw.Draw(img)

    d.text((W-82, 152), '15 Professional',  fill=SL,   font=f(F_MD,  52), anchor='rt')
    d.text((W-82, 224), 'Message',           fill=WHITE, font=f(F_BK, 100), anchor='rt')
    d.text((W-82, 350), 'Templates.',        fill=TEAL,  font=f(F_BK, 100), anchor='rt')
    d.text((W-82, 464), 'Copy. Paste. Personalize. Done.', fill=SL,
           font=f(F_RG, 38), anchor='rt')

    # List of template names
    tmpls = ['Booking Confirmation', 'Pre-Arrival Instructions',
             'Welcome Message', 'Check-in Reminder',
             'Day-Before Checkout', '5-Star Review Request',
             'Early Check-out Request', 'Noise Complaint Response',
             'Lost Item Response', 'Returning Guest Offer']
    tx = W - 82
    for i, t in enumerate(tmpls):
        d.text((tx, 540 + i * 108), '✓  ' + t,
               fill=TEAL if i < 6 else SL,
               font=f(F_MD if i < 6 else F_RG, 30),
               anchor='rt')
    save(img, '06-Templates.jpg')


def img07_guest_experience():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W//2+100, H//2, 700, AMBER, s=25)
    img = glow(img, W//2-400, H//2, 500, TEAL, s=22)

    img, sx, sy, sw_m, sh_m = ipad(img, cx=W//2+80, cy=H//2+80, sw=1600, sh=1100)
    img = ui_house_manual(img, sx, sy, sw_m, sh_m)
    img = glow(img, sx+sw_m//2, sy+sh_m//2, sh_m//2, AMBER, s=16)

    d = ImageDraw.Draw(img)

    img, _ = pill(img, 82, 62, '  GUEST EXPERIENCE  ', bg=AMBER, fg=BG, sz=26)
    d = ImageDraw.Draw(img)
    d.text((82, 138), 'Impress guests', fill=WHITE, font=f(F_BK, 84))
    d.text((82, 244), 'from the moment', fill=WHITE, font=f(F_BK, 84))
    d.text((82, 350), 'they arrive.',   fill=TEAL,  font=f(F_BK, 84))
    d.text((82, 448),
           'A digital House Manual that\nguests actually read and love.',
           fill=SL, font=f(F_RG, 36))

    # Floating review card
    rc_x, rc_y, rc_w, rc_h = 60, H-290, 580, 210
    img = drop_sh(img, rc_x, rc_y, rc_x+rc_w, rc_y+rc_h, blur=35, a=120, dy=10)
    img = glass_card(img, rc_x, rc_y, rc_x+rc_w, rc_y+rc_h, r=18, fa=28, oa=60)
    d = ImageDraw.Draw(img)
    d.text((rc_x+22, rc_y+22), '⭐⭐⭐⭐⭐', fill=AMBER, font=f(F_MD, 34))
    d.text((rc_x+22, rc_y+72),
           '"The house manual was perfect.\nWe knew everything before we arrived!"',
           fill=WHITE, font=f(F_RG, 26))
    d.text((rc_x+22, rc_y+168), '— Sarah M., Verified Guest', fill=SL, font=f(F_RG, 24))

    save(img, '07-Guest-Experience.jpg')


def img08_results():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W//3, H//2+100, 700, GREEN, s=32)
    img = glow(img, W*2//3+100, H//2, 500, TEAL, s=26)

    d = ImageDraw.Draw(img)

    img, _ = pill(img, 82, 62, '  THE RESULTS  ', bg=GREEN, fg=BG, sz=26)
    d = ImageDraw.Draw(img)
    d.text((82, 136), "The numbers",  fill=WHITE, font=f(F_BK, 100))
    d.text((82, 262), "don't lie.",   fill=TEAL,  font=f(F_BK, 100))

    # Area chart
    cx1, cy1, cx2, cy2 = 82, 400, W*3//5, H-120
    img = dark_card(img, cx1-10, cy1-10, cx2+10, cy2+10, r=18, fill=PNL)
    d = ImageDraw.Draw(img)
    d.text((cx1+10, cy1+14), 'Host Revenue Growth', fill=WHITE,
           font=f(F_BO, int((cy2-cy1)*0.1)))

    revenue = [1200, 1450, 1800, 1600, 2200, 2800, 2600, 3240]
    months  = ['Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    ax1, ay1 = cx1+20, cy1+60
    ax2, ay2 = cx2-20, cy2-36
    img, pts = area_chart(img, ax1, ay1, ax2, ay2, revenue, col=TEAL)
    d = ImageDraw.Draw(img)
    for i, (label, (px, py)) in enumerate(zip(months, pts)):
        d.text((px, ay2+8), label, fill=SL, font=f(F_RG, 22), anchor='mt')
    # Mark last point
    d.text((pts[-1][0], pts[-1][1]-18), '$3,240', fill=AMBER,
           font=f(F_BO, 28), anchor='mb')

    # Stat cards right
    stats = [
        ('4.9 ★',  'Host rating',          AMBER),
        ('+170%',  'Revenue increase',      TEAL),
        ('92%',    'Peak occupancy rate',   GREEN),
        ('94%',    '5-star reviews',        PURPLE),
    ]
    sx_r = W*3//5 + 50
    for i, (val, lbl, col) in enumerate(stats):
        cy_s = 360 + i * 175
        img = drop_sh(img, sx_r, cy_s, sx_r+540, cy_s+145, blur=35, a=120, dy=10)
        img = dark_card(img, sx_r, cy_s, sx_r+540, cy_s+145, r=16, fill=PNL, accent=col)
        d = ImageDraw.Draw(img)
        d.text((sx_r+20, cy_s+42), val, fill=WHITE, font=f(F_BO, 56))
        d.text((sx_r+20, cy_s+106), lbl, fill=SL,   font=f(F_RG, 28))

    save(img, '08-Results.jpg')


def img09_who_its_for():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img)
    img = dot_grid(img)
    img = glow(img, W//2, H//2+100, 800, BLUE, s=30)

    d = ImageDraw.Draw(img)

    img, _ = pill(img, 82, 62, '  WHO IS THIS FOR?  ', bg=BLUE, fg=WHITE, sz=26)
    d = ImageDraw.Draw(img)
    d.text((W//2, 136), 'Built for ambitious hosts.',  fill=WHITE, font=f(F_BK, 100), anchor='mt')
    d.text((W//2, 258), "Whether you have 1 property or 10, this system works.",
           fill=SL, font=f(F_RG, 38), anchor='mt')

    profiles = [
        ('🏠', 'New Host',
         'Just listed your first property',
         ['Get set up the right way', 'Avoid beginner mistakes',
          'Build 5-star habits early', 'Professional from day one'],
         TEAL),
        ('🔑', 'Scaling Host',
         'Managing 2–5 properties',
         ['Systemize before you scale', 'Delegate with SOPs',
          'Protect your Superhost status', 'Maximize revenue per unit'],
         AMBER),
        ('📊', 'Professional Host',
         'Running a hosting business',
         ['Plug gaps in your system', 'Coach your team',
          'Refine pricing strategy', 'Analyze and optimize'],
         PURPLE),
    ]

    PAD  = 60
    CW   = (W - PAD * 4) // 3
    CH   = H - 400
    CY   = 340

    for i, (ic, title, sub, bullets, col) in enumerate(profiles):
        cx_c = PAD + i * (CW + PAD)
        img = drop_sh(img, cx_c, CY, cx_c+CW, CY+CH, blur=45, a=140, dy=16)
        img = dark_card(img, cx_c, CY, cx_c+CW, CY+CH, r=20, fill=PNL)
        d = ImageDraw.Draw(img)

        # Top accent strip
        d.rounded_rectangle([cx_c, CY, cx_c+CW, CY+60], radius=20, fill=col)

        # Icon
        d.text((cx_c+CW//2, CY+30), ic, fill=WHITE, font=f(F_MD, 40), anchor='mm')

        # Title
        d.text((cx_c+CW//2, CY+100), title, fill=WHITE,
               font=f(F_BK, 48), anchor='mt')
        d.text((cx_c+CW//2, CY+160), sub, fill=SL,
               font=f(F_RG, 28), anchor='mt')

        # Divider
        d.line([(cx_c+30, CY+204), (cx_c+CW-30, CY+204)], fill=LINE, width=1)

        # Bullets
        for j, bullet in enumerate(bullets):
            by = CY + 224 + j * 94
            d.ellipse([cx_c+30, by+8, cx_c+50, by+28], fill=col)
            d.text((cx_c+64, by+4), bullet, fill=WHITE, font=f(F_RG, 28))

    save(img, '09-Who-Its-For.jpg')


def img10_cta():
    img = Image.new('RGB', (W, H), BG)
    grad_bg(img, top=BG, bot=(10, 16, 40))
    img = dot_grid(img)
    img = glow(img, W//2, H//2, 900, TEAL, s=35)
    img = glow(img, W//2, H//2, 500, AMBER, s=18)

    d = ImageDraw.Draw(img)

    img, _ = pill(img, 82, 62, '  COMPLETE STARTER KIT  ', bg=TEAL, fg=BG, sz=26)
    d = ImageDraw.Draw(img)

    d.text((82, 136), 'Get the complete',  fill=SL,   font=f(F_MD, 60))
    d.text((82, 218), 'Airbnb Host',       fill=WHITE, font=f(F_BK, 108))
    d.text((82, 352), 'Starter Kit.',      fill=TEAL,  font=f(F_BK, 108))
    d.text((82, 472), 'Everything you need. Instant download.', fill=SL, font=f(F_RG, 38))

    # Value stack (left panel)
    vs_x, vs_y, vs_w = 82, 556, 760
    items_val = [
        ('Quick Start Guide',       '$19'),
        ('Listing Optimization',    '$29'),
        ('15 Message Templates',    '$39'),
        ('House Rules Template',    '$19'),
        ('House Manual Template',   '$29'),
        ('Check-In SOP',            '$19'),
        ('Cleaning SOP',            '$19'),
        ('Review Strategy Guide',   '$29'),
        ('8-Sheet Operations Hub',  '$49'),
    ]
    VIH = 52
    img = dark_card(img, vs_x-10, vs_y-14, vs_x+vs_w+10, vs_y+VIH*len(items_val)+80,
                    r=16, fill=PNL)
    d = ImageDraw.Draw(img)
    d.text((vs_x+12, vs_y-2), 'What you get:', fill=SL, font=f(F_BO, 28))
    for i, (name, price) in enumerate(items_val):
        vy = vs_y + 42 + i * VIH
        d.text((vs_x+12, vy), '·  ' + name, fill=WHITE, font=f(F_RG, 26))
        d.text((vs_x+vs_w-8, vy+2), price, fill=SL_D, font=f(F_RG, 26), anchor='rt')
    sep_y = vs_y + 42 + len(items_val)*VIH + 2
    d.line([(vs_x+12, sep_y), (vs_x+vs_w-12, sep_y)], fill=LINE, width=1)
    d.text((vs_x+12, sep_y+10), 'Total retail value:', fill=SL, font=f(F_RG, 26))
    d.text((vs_x+vs_w-8, sep_y+12), '$250', fill=SL_D, font=f(F_BO, 26), anchor='rt')

    # Right: Price + CTA block
    px_r = vs_x + vs_w + 80
    pw_r = W - px_r - 80

    # Main price card
    mc_y = 556
    mc_h = 360
    img = drop_sh(img, px_r, mc_y, px_r+pw_r, mc_y+mc_h, blur=50, a=160, dy=18)
    img = dark_card(img, px_r, mc_y, px_r+pw_r, mc_y+mc_h, r=20, fill=PNL_2)
    d = ImageDraw.Draw(img)
    d.text((px_r+pw_r//2, mc_y+40), 'TODAY ONLY', fill=AMBER,
           font=f(F_CN, 32), anchor='mt')
    d.text((px_r+pw_r//2, mc_y+96), '$27', fill=WHITE,
           font=f(F_BK, 130), anchor='mt')
    d.text((px_r+pw_r//2, mc_y+244), 'One-time payment', fill=SL,
           font=f(F_RG, 30), anchor='mt')
    d.text((px_r+pw_r//2, mc_y+288), 'Lifetime access · Instant download', fill=SL_D,
           font=f(F_RG, 26), anchor='mt')

    # CTA button
    btn_x, btn_y = px_r+40, mc_y+mc_h+28
    btn_w, btn_h = pw_r-80, 88
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0))
    dd = ImageDraw.Draw(ov)
    dd.rounded_rectangle([btn_x, btn_y, btn_x+btn_w, btn_y+btn_h],
                          radius=btn_h//2, fill=TEAL+(255,))
    img = Image.alpha_composite(img.convert('RGBA'), ov).convert('RGB')
    d = ImageDraw.Draw(img)
    d.text((btn_x+btn_w//2, btn_y+btn_h//2), 'Get Instant Access  →',
           fill=BG, font=f(F_BK, 36), anchor='mm')

    # Trust badges
    badges = ['⚡  Instant Download', '🔄  Lifetime Updates',
              '❤️  10,000+ Hosts',    '✓  No subscription']
    bw_b = (pw_r-20) // 2
    for i, badge in enumerate(badges):
        bx = px_r + (i % 2) * bw_b + 10
        by = mc_y + mc_h + btn_h + 50 + (i // 2) * 72
        img = dark_card(img, bx, by, bx+bw_b-20, by+58, r=10, fill=PNL)
        d = ImageDraw.Draw(img)
        d.text((bx+bw_b//2-10, by+29), badge, fill=SL, font=f(F_RG, 24), anchor='mm')

    save(img, '10-CTA.jpg')


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print(f'\nGenerating 10 premium Etsy images → {OUT}\n')
    img01_hero()
    img02_problem_solved()
    img03_whats_included()
    img04_dashboard()
    img05_workflow()
    img06_templates()
    img07_guest_experience()
    img08_results()
    img09_who_its_for()
    img10_cta()
    print('\nAll 10 images complete.\n')
