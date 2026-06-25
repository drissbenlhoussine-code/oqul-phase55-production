"""
Etsy Listing Images v2 — Bookkeeper Practice Launch System v3.0
11 premium world-class images. Stripe / Notion / Linear quality.
2700 x 1800 px. Roboto. Proper shadows, glass effects, depth.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, random

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/etsy-images-v2'
os.makedirs(OUT, exist_ok=True)

W, H = 2700, 1800

# ── Brand Palette ──────────────────────────────────────────────────────────────
NAVY      = (15,  23,  42)
NAVY_2    = (30,  41,  59)
NAVY_3    = (51,  65,  85)
TEAL      = (15, 118, 110)
TEAL_D    = (13,  94,  88)
TEAL_L    = (204,251,241)
TEAL_M    = (20, 184, 166)
TEAL_XL   = (240,253,250)
AMBER     = (217,119,  6)
AMBER_L   = (254,243,199)
AMBER_M   = (245,158, 11)
WHITE     = (255,255,255)
OFF_WHITE = (252,253,255)
BG_SOFT   = (248,250,252)
BG_COOL   = (241,245,249)
RULE      = (226,232,240)
RULE_D    = (203,213,225)
MUTED     = (100,116,139)
MUTED_L   = (148,163,184)
GREEN     = ( 34,197, 94)
GREEN_D   = ( 22,163, 74)
GREEN_L   = (220,252,231)
RED       = (239, 68, 68)
RED_L     = (254,226,226)
PURPLE    = (139, 92,246)
PURPLE_L  = (237,233,254)
BLUE      = ( 59,130,246)
BLUE_L    = (219,234,254)

# ── Font paths ─────────────────────────────────────────────────────────────────
F_BK = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Black.ttf'
F_BO = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Bold.ttf'
F_MD = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Medium.ttf'
F_RG = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf'
F_LT = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Light.ttf'
F_CB = '/usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Bold.ttf'

def f(path, size): return ImageFont.truetype(path, size)


# ══════════════════════════════════════════════════════════════════════════════
# COMPOSITING HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def new_canvas():
    img = Image.new('RGB', (W, H), WHITE)
    return img, ImageDraw.Draw(img)


def drop_shadow(base_img, xy, w, h, radius=20, blur=18, alpha=55, color=(0,0,0)):
    """Render a soft drop shadow under a rectangle, return composited image."""
    sx0, sy0 = xy[0]+10, xy[1]+12
    shadow_layer = Image.new('RGBA', (W, H), (0,0,0,0))
    sd = ImageDraw.Draw(shadow_layer)
    sd.rounded_rectangle([sx0, sy0, sx0+w, sy0+h], radius=radius,
                         fill=(*color, alpha))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(blur))
    base_rgba = base_img.convert('RGBA')
    base_rgba = Image.alpha_composite(base_rgba, shadow_layer)
    img2 = base_rgba.convert('RGB')
    return img2, ImageDraw.Draw(img2)


def glass_card(img, x, y, w, h, r=16, fill=(255,255,255), border_alpha=80,
               shadow=True, shadow_blur=18, shadow_alpha=50):
    """Draw a premium card with soft shadow + subtle border."""
    if shadow:
        img, d = drop_shadow(img, (x,y), w, h, radius=r,
                             blur=shadow_blur, alpha=shadow_alpha)
    else:
        d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x+w, y+h], radius=r, fill=fill,
                        outline=RULE, width=1)
    return img, d


def gradient_rect(d, x, y, w, h, c1, c2, vertical=True):
    """Linear gradient fill."""
    for i in range(h if vertical else w):
        t = i/(h-1) if vertical else i/(w-1)
        cr = int(c1[0]+(c2[0]-c1[0])*t)
        cg = int(c1[1]+(c2[1]-c1[1])*t)
        cb = int(c1[2]+(c2[2]-c1[2])*t)
        if vertical:
            d.line([x, y+i, x+w, y+i], fill=(cr,cg,cb))
        else:
            d.line([x+i, y, x+i, y+h], fill=(cr,cg,cb))


def tint_overlay(img, x, y, w, h, color, alpha=15):
    """Soft color tint over a region."""
    overlay = Image.new('RGBA', (W, H), (0,0,0,0))
    od = ImageDraw.Draw(overlay)
    od.rectangle([x, y, x+w, y+h], fill=(*color, alpha))
    base_rgba = img.convert('RGBA')
    base_rgba = Image.alpha_composite(base_rgba, overlay)
    img2 = base_rgba.convert('RGB')
    return img2, ImageDraw.Draw(img2)


def pill(d, cx, cy, text, bg, fg=WHITE, size=24, pad_x=22, pad_y=10):
    """Rounded pill badge."""
    tw = len(text)*size//2 + pad_x*2
    th = size + pad_y*2
    d.rounded_rectangle([cx-tw//2, cy-th//2, cx+tw//2, cy+th//2],
                        radius=th//2, fill=bg)
    d.text((cx, cy), text, font=f(F_CB, size), fill=fg, anchor='mm')


def dot_label(d, x, y, text, color=TEAL, size=28):
    d.ellipse([x-8, y-8, x+8, y+8], fill=color)
    d.text((x+20, y), text, font=f(F_RG, size), fill=MUTED, anchor='lm')


def check_row(d, x, y, text, color=TEAL, size=30):
    r = size//2 - 2
    d.ellipse([x, y-r, x+r*2, y+r], fill=color)
    d.text((x+r, y), '✓', font=f(F_BO, size-6), fill=WHITE, anchor='mm')
    d.text((x+r*2+14, y), text, font=f(F_MD, size), fill=NAVY, anchor='lm')


def tag(d, x, y, text, bg=TEAL, fg=WHITE, size=22):
    tw = len(text)*size//2 + 20
    d.rounded_rectangle([x, y-14, x+tw, y+18], radius=8, fill=bg)
    d.text((x+tw//2, y+2), text, font=f(F_CB, size), fill=fg, anchor='mm')
    return tw


def sparkline(d, x, y, w, h, pts, color=TEAL, fill=None, width=3):
    if len(pts) < 2: return
    pw = w/(len(pts)-1)
    coords = [(x+i*pw, y+h-h*p/100) for i,p in enumerate(pts)]
    if fill:
        poly = list(coords)+[(x+w,y+h),(x,y+h)]
        d.polygon(poly, fill=fill)
    d.line(coords, fill=color, width=width)


def mini_bar(d, x, y, w, h, pct, color=TEAL, bg=RULE, r=4):
    d.rounded_rectangle([x,y,x+w,y+h], radius=r, fill=bg)
    if pct > 0:
        pw = max(int(w*pct), h)
        d.rounded_rectangle([x,y,x+pw,y+h], radius=r, fill=color)


# ══════════════════════════════════════════════════════════════════════════════
# DEVICE MOCKUPS (premium quality)
# ══════════════════════════════════════════════════════════════════════════════

def laptop(img, x, y, screen_w, content_fn=None):
    """Premium laptop mockup. Returns screen coords."""
    d = ImageDraw.Draw(img)
    sw = screen_w
    sh = int(sw*0.62)
    bezel = 18
    # Shadow
    img, d = drop_shadow(img, (x,y), sw+60, sh+60, radius=20, blur=30, alpha=60)
    # Lid body
    d.rounded_rectangle([x, y, x+sw, y+sh], radius=14, fill=NAVY_2)
    # Screen area
    d.rounded_rectangle([x+bezel, y+bezel, x+sw-bezel, y+sh-bezel],
                        radius=6, fill=(18,22,36))
    # Camera dot
    d.ellipse([x+sw//2-7, y+6, x+sw//2+7, y+20], fill=(40,50,70))
    # Base/hinge
    bw = int(sw*1.08)
    bx = x - int(sw*0.04)
    bh = 28
    d.rounded_rectangle([bx, y+sh, bx+bw, y+sh+bh], radius=6, fill=NAVY_3)
    # Trackpad groove
    tpw, tph = int(sw*0.22), 18
    tpx = bx + (bw-tpw)//2
    tpy = y+sh+5
    d.rounded_rectangle([tpx, tpy, tpx+tpw, tpy+tph], radius=4,
                        fill=(40,52,70), outline=(55,65,85), width=1)
    # Screen content area (inside bezel)
    sc_x = x+bezel+2
    sc_y = y+bezel+2
    sc_w = sw-bezel*2-4
    sc_h = sh-bezel*2-4
    if content_fn:
        content_fn(img, d, sc_x, sc_y, sc_w, sc_h)
    return sc_x, sc_y, sc_w, sc_h


def ipad(img, x, y, w, content_fn=None):
    """iPad mockup."""
    h_dev = int(w*1.35)
    bezel = 14
    img, d = drop_shadow(img, (x,y), w, h_dev, radius=24, blur=20, alpha=50)
    d.rounded_rectangle([x, y, x+w, y+h_dev], radius=24, fill=NAVY_2)
    d.rounded_rectangle([x+bezel, y+bezel, x+w-bezel, y+h_dev-bezel],
                        radius=12, fill=(16,20,34))
    # Home indicator
    d.rounded_rectangle([x+w//2-30, y+h_dev-16, x+w//2+30, y+h_dev-6],
                        radius=4, fill=(50,60,80))
    # Camera
    d.ellipse([x+w//2-6, y+6, x+w//2+6, y+18], fill=(40,52,70))
    sc_x = x+bezel+1
    sc_y = y+bezel+24
    sc_w = w-bezel*2-2
    sc_h = h_dev-bezel*2-36
    if content_fn:
        content_fn(img, d, sc_x, sc_y, sc_w, sc_h)
    return sc_x, sc_y, sc_w, sc_h, h_dev


def iphone(img, x, y, w, content_fn=None):
    """iPhone mockup."""
    h_dev = int(w*2.16)
    bezel = 12
    img, d = drop_shadow(img, (x,y), w, h_dev, radius=36, blur=20, alpha=45)
    d.rounded_rectangle([x, y, x+w, y+h_dev], radius=36, fill=NAVY_2)
    d.rounded_rectangle([x+bezel, y+bezel, x+w-bezel, y+h_dev-bezel],
                        radius=28, fill=(16,20,34))
    # Dynamic island
    di_w, di_h = int(w*0.38), 22
    d.rounded_rectangle([x+(w-di_w)//2, y+14, x+(w+di_w)//2, y+14+di_h],
                        radius=12, fill=(8,10,18))
    # Side button
    d.rounded_rectangle([x+w, y+200, x+w+6, y+290], radius=3, fill=NAVY_3)
    # Home indicator
    d.rounded_rectangle([x+w//2-40, y+h_dev-20, x+w//2+40, y+h_dev-8],
                        radius=4, fill=(50,62,80))
    sc_x = x+bezel+1
    sc_y = y+bezel+40
    sc_w = w-bezel*2-2
    sc_h = h_dev-bezel*2-56
    if content_fn:
        content_fn(img, d, sc_x, sc_y, sc_w, sc_h)
    return sc_x, sc_y, sc_w, sc_h, h_dev


# ══════════════════════════════════════════════════════════════════════════════
# REUSABLE UI COMPONENTS
# ══════════════════════════════════════════════════════════════════════════════

def app_chrome(d, x, y, w, h, title='', url='', dark=False):
    """Browser / app window chrome bar."""
    bg = NAVY_2 if dark else (250,250,249)
    d.rounded_rectangle([x, y, x+w, y+h], radius=12, fill=bg)
    # Traffic lights
    for i, c in enumerate([(239,68,68),(245,158,11),(34,197,94)]):
        d.ellipse([x+16+i*26, y+h//2-8, x+32+i*26, y+h//2+8], fill=c)
    if url:
        uw = int(w*0.5)
        ux = x+(w-uw)//2
        d.rounded_rectangle([ux, y+8, ux+uw, y+h-8], radius=8,
                            fill=(40,52,70) if dark else RULE)
        d.text((x+w//2, y+h//2), url, font=f(F_RG, 22), fill=MUTED, anchor='mm')
    if title:
        d.text((x+w-20, y+h//2), title, font=f(F_MD, 22),
               fill=TEAL if dark else NAVY, anchor='rm')


def sidebar_item(d, x, y, w, icon_char, label, active=False, color=TEAL):
    h_item = 52
    if active:
        d.rounded_rectangle([x+6, y, x+w-6, y+h_item], radius=8, fill=color)
        d.text((x+22, y+h_item//2), f'{icon_char}  {label}',
               font=f(F_MD, 26), fill=WHITE, anchor='lm')
    else:
        d.text((x+22, y+h_item//2), f'{icon_char}  {label}',
               font=f(F_RG, 26), fill=MUTED_L, anchor='lm')


def kpi_tile(img, x, y, w, h, label, value, delta='', delta_up=True,
             color=TEAL, micro_chart=None):
    """KPI card with optional sparkline."""
    img, d = glass_card(img, x, y, w, h, r=12, fill=WHITE,
                        shadow_blur=16, shadow_alpha=40)
    # Top accent bar
    d.rounded_rectangle([x, y, x+w, y+5], radius=2, fill=color)
    d.text((x+18, y+26), label, font=f(F_MD, 24), fill=MUTED, anchor='lt')
    d.text((x+18, y+58), value, font=f(F_BK, 58), fill=NAVY, anchor='lt')
    if delta:
        dc = GREEN if delta_up else RED
        arrow = '↑' if delta_up else '↓'
        d.text((x+18, y+h-28), f'{arrow} {delta}', font=f(F_MD, 24),
               fill=dc, anchor='lt')
    if micro_chart:
        sparkline(d, x+w-120, y+h-60, 100, 40, micro_chart,
                  color=color, fill=(*color, 20) if isinstance(color,tuple) and len(color)==3
                  else TEAL_L, width=2)
    return img, d


def notion_db_row(d, x, y, w, cells, col_widths, bg=WHITE, is_header=False):
    d.rectangle([x, y, x+w, y+42], fill=bg)
    d.line([x, y+42, x+w, y+42], fill=RULE, width=1)
    cx = x
    for cell, cw in zip(cells, col_widths):
        fnt_ = f(F_MD, 22) if is_header else f(F_RG, 22)
        fc = MUTED if is_header else NAVY
        d.text((cx+12, y+21), str(cell)[:28], font=fnt_, fill=fc, anchor='lm')
        d.line([cx+cw, y, cx+cw, y+42], fill=RULE, width=1)
        cx += cw


def notion_status(d, cx, cy, text, color):
    tw = len(text)*12+20
    d.rounded_rectangle([cx-tw//2, cy-14, cx+tw//2, cy+14], radius=8, fill=color)
    d.text((cx, cy), text, font=f(F_CB, 20), fill=WHITE, anchor='mm')


def section_header_bar(d, x, y, w, number, title, color=TEAL):
    """Full-width two-tone section divider."""
    num_w = 80
    d.rounded_rectangle([x, y, x+num_w, y+48], radius=0, fill=color)
    d.text((x+num_w//2, y+24), f'{number:02d}', font=f(F_BO, 30),
           fill=WHITE, anchor='mm')
    d.rounded_rectangle([x+num_w, y, x+w, y+48], radius=0, fill=NAVY)
    d.text((x+num_w+20, y+24), f'— {title.upper()}',
           font=f(F_MD, 26), fill=WHITE, anchor='lm')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 01 — HERO (dramatically upgraded)
# ══════════════════════════════════════════════════════════════════════════════

def dashboard_screen(img, d, sx, sy, sw, sh):
    """Render live dashboard inside laptop screen."""
    d.rectangle([sx, sy, sx+sw, sy+sh], fill=(15,20,35))
    # Top nav
    d.rectangle([sx, sy, sx+sw, sy+44], fill=(20,28,48))
    d.text((sx+18, sy+22), '⊞  Practice Dashboard', fill=TEAL, font=f(F_MD,22), anchor='lm')
    d.text((sx+sw-80, sy+22), '● Live', fill=GREEN, font=f(F_RG,20), anchor='rm')
    # KPI row
    ky = sy+54
    kpis = [('MRR','€12,400',GREEN),('Clients','18',TEAL),('Pipeline','€6.2k',AMBER),('Close','78%',PURPLE)]
    kw = (sw-20)//4
    for i,(lb,vl,co) in enumerate(kpis):
        kx = sx+10+i*(kw-1)
        d.rounded_rectangle([kx,ky,kx+kw-6,ky+72], radius=6, fill=(25,34,55))
        d.rectangle([kx,ky,kx+kw-6,ky+3], fill=co)
        d.text((kx+10,ky+16), lb, fill=MUTED_L, font=f(F_RG,16), anchor='lt')
        d.text((kx+10,ky+34), vl, fill=WHITE, font=f(F_BO,30), anchor='lt')
    # Revenue bars
    by = ky+84
    bh = sh - by - sy - 48
    months = ['J','F','M','A','M','J']
    vals = [68,74,62,81,88,100]
    bw = (sw-20)//6-4
    for i,(m,v) in enumerate(zip(months,vals)):
        bx = sx+10+i*(bw+4)
        barh = int((bh-30)*v/100)
        col = AMBER if i==5 else TEAL
        d.rounded_rectangle([bx, by+bh-30-barh, bx+bw, by+bh-30], radius=3, fill=col)
        d.text((bx+bw//2, by+bh-14), m, fill=MUTED_L, font=f(F_RG,16), anchor='mm')
    # Sparkline overlay
    pts = [68,74,62,81,88,100]
    sparkline(d, sx+10, by, sw-20, bh-30, pts, TEAL_M,
              fill=(20,184,166,25), width=2)


def img01_hero():
    img, d = new_canvas()

    # --- Dark left panel ---
    gradient_rect(d, 0, 0, 760, H, NAVY_2, NAVY)
    # Fine grid dots on dark panel
    for gx in range(0, 760, 44):
        for gy in range(0, H, 44):
            d.ellipse([gx-1,gy-1,gx+1,gy+1], fill=(30,42,62))

    # NovaOps wordmark
    d.text((56, 62), 'NOVAOPS', fill=TEAL, font=f(F_BK, 48), anchor='lt')
    d.line([56, 122, 700, 122], fill=TEAL, width=2)

    # Headline
    for i, (line, color) in enumerate([
        ('Run Your',    WHITE),
        ('Bookkeeping', TEAL),
        ('Business',    WHITE),
        ('Like a Pro.', WHITE),
    ]):
        d.text((56, 148+i*108), line, fill=color, font=f(F_BK, 102), anchor='lt')

    d.text((56, 592), 'The complete operating system for', fill=MUTED_L, font=f(F_LT, 36), anchor='lt')
    d.text((56, 636), 'professional bookkeepers.', fill=MUTED_L, font=f(F_LT, 36), anchor='lt')

    d.line([56, 700, 700, 700], fill=(40,55,78), width=1)

    # Premium feature badges
    checks = ['33 Premium Files','Excel Dashboard (10 sheets)',
              'Notion Workspace (7 DBs)','SOPs + Checklists',
              'Client Templates + Scripts','Instant Download · Lifetime Access']
    for i,c in enumerate(checks):
        check_row(d, 56, 728+i*78, c, TEAL, 30)

    # Version badge
    img, d = glass_card(img, 56, H-140, 640, 68, r=10,
                        fill=AMBER, shadow=False)
    d.text((56+320, H-106), 'VERSION 3.0  ·  PREMIUM CONSULTING EDITION',
           fill=WHITE, font=f(F_CB, 26), anchor='mm')

    # --- Central laptop (large) ---
    def dash_fn(i2, d2, sx, sy, sw, sh):
        dashboard_screen(i2, d2, sx, sy, sw, sh)

    sc_x, sc_y, sc_w, sc_h = laptop(img, 780, 60, 1360, dashboard_screen)
    d = ImageDraw.Draw(img)

    # --- Floating iPad (top-right) ---
    ipad_x = 2230
    ipad_fn_called = False
    def ipad_content(im, dd, sx, sy, sw, sh):
        dd.rectangle([sx,sy,sx+sw,sy+sh], fill=BG_COOL)
        dd.text((sx+sw//2,sy+22), 'Clients CRM', fill=NAVY, font=f(F_BO,22), anchor='mm')
        dd.line([sx,sy+40,sx+sw,sy+40], fill=RULE, width=1)
        rows=[('Acme Ltd','Active','€1,200'),('Brio Co','Active','€1,050'),
              ('Finova','Review','€900'),('EasyPay','Active','€780'),
              ('Novalux','Active','€650')]
        for ri,(n,s,fee) in enumerate(rows):
            ry = sy+46+ri*44
            bg=BG_SOFT if ri%2==0 else WHITE
            dd.rectangle([sx,ry,sx+sw,ry+42], fill=bg)
            dd.text((sx+10,ry+21), n, fill=NAVY, font=f(F_MD,20), anchor='lm')
            sc=GREEN if s=='Active' else AMBER
            dd.rounded_rectangle([sx+sw-92,ry+8,sx+sw-4,ry+34], radius=8, fill=sc)
            dd.text((sx+sw-48,ry+21), s, fill=WHITE, font=f(F_RG,16), anchor='mm')

    sc2_x,sc2_y,sc2_w,sc2_h,ipad_h = ipad(img, ipad_x, 80, 330, ipad_content)
    d = ImageDraw.Draw(img)

    # --- iPhone (bottom-right) ---
    def iphone_content(im, dd, sx, sy, sw, sh):
        dd.rectangle([sx,sy,sx+sw,sy+sh], fill=BG_SOFT)
        dd.text((sx+sw//2,sy+20), 'Invoice #042', fill=NAVY, font=f(F_BO,18), anchor='mm')
        dd.line([sx,sy+38,sx+sw,sy+38], fill=RULE, width=1)
        dd.text((sx+sw//2,sy+70), 'Brio Co Ltd', fill=MUTED, font=f(F_MD,20), anchor='mm')
        dd.text((sx+sw//2,sy+108), '€1,200', fill=NAVY, font=f(F_BK,42), anchor='mm')
        dd.rounded_rectangle([sx+16,sy+158,sx+sw-16,sy+192], radius=10, fill=GREEN)
        dd.text((sx+sw//2,sy+175), '✓  PAID', fill=WHITE, font=f(F_CB,22), anchor='mm')
        dd.text((sx+sw//2,sy+214), 'June 15, 2025', fill=MUTED, font=f(F_RG,16), anchor='mm')
        mini_bar(dd, sx+16, sy+246, sw-32, 10, 1.0, GREEN)

    sc3_x,sc3_y,sc3_w,sc3_h,iphone_h = iphone(img, 2280, 820, 230, iphone_content)
    d = ImageDraw.Draw(img)

    # --- Floating document card (PDF preview) ---
    img, d = glass_card(img, 1980, 780, 280, 360, r=12, fill=WHITE,
                        shadow_blur=20, shadow_alpha=45)
    d.rounded_rectangle([1980,780,2260,828], radius=0, fill=TEAL)
    d.text((2120, 804), 'SERVICE GUIDE', fill=WHITE, font=f(F_CB,22), anchor='mm')
    d.text((1998, 848), 'Bookkeeping Services', fill=NAVY, font=f(F_BO,22), anchor='lt')
    d.text((1998, 876), 'v3.0  ·  NOVAOPS', fill=MUTED, font=f(F_RG,20), anchor='lt')
    d.line([1998,904,2244,904], fill=RULE, width=1)
    for i,line in enumerate(['5 service tiers','Clear pricing table','Scope boundaries','FAQ section']):
        d.text((2004,920+i*36), f'→  {line}', fill=MUTED, font=f(F_RG,20), anchor='lt')
    tag(d, 1998, 1096, 'DOCX', TEAL)

    # Bottom bar
    d.rectangle([0, H-72, W, H], fill=NAVY)
    d.text((50, H-36), 'BOOKKEEPER PRACTICE LAUNCH SYSTEM  ·  v3.0  ·  NOVAOPS',
           fill=TEAL, font=f(F_CB,28), anchor='lm')
    d.text((W-50, H-36), 'Instant Download  ·  Lifetime Access',
           fill=MUTED_L, font=f(F_RG,28), anchor='rm')

    img.save(f'{OUT}/01-Hero.jpg', quality=96)
    print('  ✓ 01-Hero.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 02 — EVERYTHING INCLUDED
# ══════════════════════════════════════════════════════════════════════════════

def img02_included():
    img, d = new_canvas()

    # Subtle top gradient
    gradient_rect(d, 0, 0, W, 140, NAVY, NAVY_2)
    d.text((W//2, 52), 'EVERYTHING INCLUDED', fill=WHITE, font=f(F_BK,46), anchor='mm')
    d.text((W//2, 100), 'One purchase. Every tool your bookkeeping practice needs — forever.',
           fill=MUTED_L, font=f(F_MD,30), anchor='mm')

    categories = [
        ('📊', 'PRACTICE DASHBOARD', TEAL, 'Excel · 10 Sheets', [
            ('KPI Dashboard', 'Auto-calculates MRR, pipeline, capacity'),
            ('Client CRM', '20-column client database'),
            ('Lead Pipeline', 'Conversion tracking + value'),
            ('Invoice Tracker', 'Status + payment method'),
            ('Pricing Calculator', '3-tier fee automation'),
        ]),
        ('🗂️', 'NOTION WORKSPACE', PURPLE, 'Notion · 7 Databases', [
            ('Clients CRM', 'Master hub — links all databases'),
            ('Monthly Close', 'Period tracker per client'),
            ('Lead Pipeline', 'Board + table views'),
            ('Invoice Register', 'With VAT + payment'),
            ('Client Portal', 'Shared with clients'),
        ]),
        ('📋', 'CLIENT DOCUMENTS', AMBER, 'DOCX + PPTX · 5 Files', [
            ('Service Guide', '5 tiers, scope, pricing'),
            ('Proposal Template', 'Per-client, fully scoped'),
            ('Engagement Agreement', '15 professional clauses'),
            ('Onboarding Pack', '5 structured sections'),
            ('Proposal Deck', '10 consulting slides'),
        ]),
        ('⚙️', 'OPERATIONS LIBRARY', BLUE, 'DOCX · 3 Files', [
            ('SOPs & Checklists', '4 SOPs with QC framework'),
            ('Client Scripts', '10 email + portal scripts'),
            ('Tax Prep Checklist', '4-phase year-end system'),
        ]),
        ('📄', 'PDF GUIDES', GREEN, 'PDF · 9 Documents', [
            ('Read Me First', 'Complete orientation guide'),
            ('Installation Guide', '90-minute setup walkthrough'),
            ('FAQ', '16 answered questions'),
            ('Notion Setup Guide', 'Import + connect all 7 DBs'),
            ('Asset Manifest', 'Full inventory with descriptions'),
        ]),
        ('🚀', 'BONUS & SUPPORT', TEAL_M, 'Included Free', [
            ('Commercial License', 'Use with your direct clients'),
            ('Version History', 'Roadmap + changelog'),
            ('QA Report', 'Scored 91/100'),
            ('Support Guide', '1–3 day response time'),
            ('Lifetime Updates', 'Minor updates always free'),
        ]),
    ]

    cw, ch = 830, 670
    cols, rows = 3, 2
    px = (W - cols*cw) // (cols+1)
    py_start = 160

    for i, (icon, title, color, badge_text, items) in enumerate(categories):
        col = i % cols
        row = i // cols
        cx = px + col*(cw+px)
        cy = py_start + row*(ch+20)

        img, d = glass_card(img, cx, cy, cw, ch, r=14, fill=WHITE,
                            shadow_blur=18, shadow_alpha=38)
        # Top color band
        d.rounded_rectangle([cx, cy, cx+cw, cy+6], radius=2, fill=color)

        # Icon circle
        d.ellipse([cx+22, cy+24, cx+90, cy+92], fill=(*color[:3], 30) if len(color)==3 else TEAL_L)
        d.text((cx+56, cy+58), icon, fill=color, font=f(F_RG,48), anchor='mm')

        # Title + badge
        d.text((cx+106, cy+36), title, fill=NAVY, font=f(F_BO,30), anchor='lt')
        d.text((cx+106, cy+72), badge_text, fill=MUTED, font=f(F_RG,24), anchor='lt')
        tag(d, cx+cw-len(badge_text)*14-40, cy+22, badge_text, color)

        d.line([cx+18, cy+104, cx+cw-18, cy+104], fill=RULE, width=1)

        # Items
        for j, (item_title, item_desc) in enumerate(items):
            iy = cy+116+j*96
            # Check circle
            r = 14
            d.ellipse([cx+22, iy+r-2, cx+22+r*2, iy+r*2+r-2], fill=TEAL_L)
            d.text((cx+22+r, iy+r*2-2), '✓', fill=TEAL, font=f(F_BO,18), anchor='mm')
            d.text((cx+60, iy+14), item_title, fill=NAVY, font=f(F_MD,28), anchor='lt')
            d.text((cx+60, iy+46), item_desc, fill=MUTED, font=f(F_RG,22), anchor='lt')

    # Footer
    d.rectangle([0, H-72, W, H], fill=NAVY)
    d.text((W//2, H-36), '33 FILES  ·  5 FORMATS  ·  5 FOLDERS  ·  NOVAOPS BOOKKEEPER PRACTICE LAUNCH SYSTEM v3.0',
           fill=TEAL, font=f(F_CB,26), anchor='mm')

    img.save(f'{OUT}/02-Everything-Included.jpg', quality=96)
    print('  ✓ 02-Everything-Included.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 03 — DASHBOARD (full SaaS app)
# ══════════════════════════════════════════════════════════════════════════════

def img03_dashboard():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, H, (235,240,248), BG_COOL)

    # Browser window
    img, d = glass_card(img, 30, 20, W-60, H-40, r=16, fill=WHITE,
                        shadow_blur=24, shadow_alpha=35)
    # Chrome bar
    d.rounded_rectangle([30, 20, W-30, 70], radius=16, fill=(250,250,249))
    d.line([30, 70, W-30, 70], fill=RULE, width=1)
    for i,c in enumerate([(239,68,68),(245,158,11),(34,197,94)]):
        d.ellipse([54+i*26, 37, 70+i*26, 53], fill=c)
    url_w = 680
    d.rounded_rectangle([(W-url_w)//2, 32, (W+url_w)//2, 60], radius=6, fill=RULE)
    d.text((W//2, 46), 'app.novaops.io/dashboard', fill=MUTED, font=f(F_RG,22), anchor='mm')

    # App top bar
    d.rectangle([30, 70, W-30, 120], fill=NAVY)
    d.text((70, 95), '⊞  NOVAOPS · Practice Dashboard', fill=WHITE, font=f(F_BO,30), anchor='lm')
    d.text((W-80, 95), '● Live  ·  June 2025', fill=GREEN, font=f(F_RG,26), anchor='rm')

    # Left sidebar
    sb_w = 230
    d.rectangle([30, 120, 30+sb_w, H-40], fill=(248,250,254))
    d.line([30+sb_w, 120, 30+sb_w, H-40], fill=RULE, width=1)
    nav = [('⊞','Dashboard',True),('👥','Client CRM',False),('📈','Lead Pipeline',False),
           ('📅','Monthly Close',False),('💳','Invoices',False),('🧮','Pricing Calc',False),
           ('📊','Capacity',False),('❓','Instructions',False)]
    for i,(ic,lbl,active) in enumerate(nav):
        sidebar_item(d, 30, 136+i*72, sb_w, ic, lbl, active)

    # Main content
    mx, mw = 30+sb_w+24, W-60-sb_w-48

    # Page title
    d.text((mx, 136), 'Executive Dashboard', fill=NAVY, font=f(F_BK,42), anchor='lt')
    d.text((mx, 186), 'Auto-updated  ·  June 2025  ·  All metrics live', fill=MUTED, font=f(F_RG,26), anchor='lt')

    # 4 KPI tiles
    kpi_y = 228
    kpi_w = (mw-60)//4
    kpi_h = 130
    kpi_data = [
        ('Monthly Revenue','€12,400','+8% vs May',True,TEAL,[65,70,62,78,82,100]),
        ('Active Clients','18','+2 this month',True,GREEN,[14,15,15,16,16,18]),
        ('Pipeline Value','€6,200','4 prospects',True,AMBER,[42,38,51,44,58,62]),
        ('Invoices Due','€3,100','This month',False,PURPLE,[22,28,19,31,26,31]),
    ]
    for i,(lbl,val,sub,up,col,pts) in enumerate(kpi_data):
        kx = mx+i*(kpi_w+18)
        img, d = kpi_tile(img, kx, kpi_y, kpi_w, kpi_h, lbl, val, sub, up,
                          col, pts)

    # Revenue chart
    chart_y = kpi_y+kpi_h+20
    chart_w = int(mw*0.56)
    chart_h = 310
    img, d = glass_card(img, mx, chart_y, chart_w, chart_h, r=12, fill=WHITE,
                        shadow_blur=14, shadow_alpha=30)
    d.text((mx+18, chart_y+18), 'Revenue Trend', fill=NAVY, font=f(F_BO,30), anchor='lt')
    d.text((mx+18, chart_y+52), '12-month rolling', fill=MUTED, font=f(F_RG,22), anchor='lt')
    # Y-axis
    for i,yv in enumerate([0,4,8,12]):
        yl = chart_y+chart_h-40-int((chart_h-80)*yv/12)
        d.text((mx+14, yl), f'€{yv}k', fill=MUTED_L, font=f(F_RG,18), anchor='rm')
        d.line([mx+20, yl, mx+chart_w-10, yl], fill=RULE, width=1)
    months_12 = ['Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun']
    rev_12 = [72,78,69,87,82,92,85,97,90,102,109,124]
    bw = (chart_w-40)//12 - 3
    pts_line = []
    for i,(m,r) in enumerate(zip(months_12,rev_12)):
        bx = mx+24+i*(bw+3)
        bh2 = int((chart_h-80)*r/124)
        col2 = AMBER if i==11 else TEAL
        d.rounded_rectangle([bx, chart_y+chart_h-40-bh2, bx+bw, chart_y+chart_h-40],
                            radius=3, fill=col2)
        pts_line.append((bx+bw//2, chart_y+chart_h-40-bh2))
        if i%2==0:
            d.text((bx+bw//2, chart_y+chart_h-22), m, fill=MUTED, font=f(F_RG,18), anchor='mm')
    if len(pts_line)>1:
        d.line(pts_line, fill=(*AMBER_M,200), width=2)

    # Client table (right of chart)
    ct_x = mx+chart_w+18
    ct_w = mw-chart_w-18
    img, d = glass_card(img, ct_x, chart_y, ct_w, chart_h, r=12, fill=WHITE,
                        shadow_blur=14, shadow_alpha=30)
    d.text((ct_x+16, chart_y+18), 'Top Clients', fill=NAVY, font=f(F_BO,30), anchor='lt')
    d.text((ct_x+ct_w-16, chart_y+18), 'MRR: €6,030', fill=TEAL, font=f(F_BO,26), anchor='rm')
    d.line([ct_x+10, chart_y+56, ct_x+ct_w-10, chart_y+56], fill=RULE, width=1)
    clients_t = [('Acme Ltd','€1,200',GREEN),('Brio Co','€1,050',GREEN),
                 ('Finova GmbH','€900',GREEN),('EasyPay Ltd','€780',AMBER),
                 ('Novalux Inc','€650',GREEN),('BlueWave','€600',GREEN)]
    for ri,(n,fee,st) in enumerate(clients_t):
        ry = chart_y+64+ri*38
        d.rectangle([ct_x+8, ry, ct_x+ct_w-8, ry+36], fill=BG_SOFT if ri%2==0 else WHITE)
        d.ellipse([ct_x+16, ry+8, ct_x+32, ry+24], fill=TEAL_L)
        d.text((ct_x+24, ry+16), '●', fill=TEAL, font=f(F_RG,16), anchor='mm')
        d.text((ct_x+42, ry+18), n, fill=NAVY, font=f(F_MD,22), anchor='lm')
        d.text((ct_x+ct_w-18, ry+18), fee, fill=TEAL, font=f(F_BO,22), anchor='rm')

    # Monthly close strip
    mc_y = chart_y+chart_h+18
    img, d = glass_card(img, mx, mc_y, mw, 196, r=12, fill=WHITE,
                        shadow_blur=14, shadow_alpha=30)
    d.text((mx+18, mc_y+18), 'Monthly Close — June 2025', fill=NAVY, font=f(F_BO,30), anchor='lt')
    mini_bar(d, mx+18, mc_y+58, int(mw*0.6), 12, 0.62, TEAL)
    d.text((mx+int(mw*0.6)+30, mc_y+64), '62% complete', fill=MUTED, font=f(F_MD,24), anchor='lm')
    steps = [('Reconciliation','Done',GREEN),('Categorisation','Done',GREEN),
             ('Review','Done',GREEN),('Adjustments','Active',AMBER),('Reporting','Pending',RULE_D)]
    sw2 = (mw-40)//5
    for i,(s,st,sc) in enumerate(steps):
        sx2 = mx+20+i*sw2
        img, d = glass_card(img, sx2, mc_y+84, sw2-8, 94, r=8,
                            fill=BG_SOFT, shadow=False)
        d.rounded_rectangle([sx2, mc_y+84, sx2+sw2-8, mc_y+90], radius=4, fill=sc)
        d.text((sx2+(sw2-8)//2, mc_y+120), s, fill=NAVY, font=f(F_MD,22), anchor='mm')
        d.rounded_rectangle([sx2+12, mc_y+152, sx2+sw2-20, mc_y+172], radius=8, fill=sc)
        d.text((sx2+(sw2-8)//2, mc_y+162), st, fill=WHITE if sc!=RULE_D else MUTED, font=f(F_CB,18), anchor='mm')

    img.save(f'{OUT}/03-Dashboard.jpg', quality=96)
    print('  ✓ 03-Dashboard.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 04 — NOTION WORKSPACE
# ══════════════════════════════════════════════════════════════════════════════

def img04_notion():
    img, d = new_canvas()
    d.rectangle([0, 0, W, H], fill=(245,245,244))

    # Window
    img, d = glass_card(img, 28, 18, W-56, H-36, r=14, fill=WHITE,
                        shadow_blur=22, shadow_alpha=30)
    app_chrome(d, 28, 18, W-56, 52,
               url='notion.so  ·  Bookkeeping Practice Workspace', dark=False)
    d.line([28, 70, W-28, 70], fill=RULE, width=1)

    # Notion sidebar (dark)
    sb_w = 260
    d.rounded_rectangle([28, 70, 28+sb_w, H-36], radius=0, fill=(25,25,25))
    d.text((46, 100), '📁  Bookkeeping Practice', fill=WHITE, font=f(F_BO,24), anchor='lt')
    d.line([38, 130, 28+sb_w-10, 130], fill=(45,45,45), width=1)
    pages = [('⊞','Dashboard',True),('👥','Clients',False),('📈','Leads',False),
             ('📅','Monthly Close',False),('💳','Invoices',False),('✅','Tasks',False),
             ('📁','Documents',False),('🔗','Client Portal',False),('📊','Reports',False)]
    for i,(ic,pg,active) in enumerate(pages):
        py = 142+i*58
        if active:
            d.rounded_rectangle([36,py,28+sb_w-10,py+46], radius=6, fill=(55,55,55))
            d.text((54,py+23), f'{ic}  {pg}', fill=WHITE, font=f(F_MD,24), anchor='lm')
        else:
            d.text((54,py+23), f'{ic}  {pg}', fill=(150,150,150), font=f(F_RG,24), anchor='lm')

    # Main area
    mx, mw = 28+sb_w+28, W-56-sb_w-56

    # Page header
    d.text((mx, 86), '👥', fill=NAVY, font=f(F_RG,52), anchor='lt')
    d.text((mx+68, 104), 'Clients', fill=NAVY, font=f(F_BK,56), anchor='lm')
    d.text((mx+68, 158), '8 records  ·  Filtered: Active', fill=MUTED, font=f(F_RG,26), anchor='lm')

    # Toolbar
    tool_y = 188
    for i,btn in enumerate(['Filter','Sort','Group by','Properties']):
        bx = mx + i*140
        d.text((bx, tool_y+10), btn, fill=MUTED, font=f(F_MD,26), anchor='lt')
    d.rounded_rectangle([mx+mw-140, tool_y, mx+mw, tool_y+38], radius=8, fill=NAVY)
    d.text((mx+mw-70, tool_y+19), '+ New', fill=WHITE, font=f(F_MD,26), anchor='mm')
    d.line([mx, tool_y+44, mx+mw, tool_y+44], fill=RULE, width=1)

    # Table
    t_y = tool_y+52
    headers = ['Name','Status','Software','Monthly Fee','Close Day','Entity','Contact']
    col_ws_pct = [0.20,0.11,0.12,0.12,0.11,0.12,0.22]
    col_ws = [int(mw*p) for p in col_ws_pct]

    # Header row
    d.rectangle([mx, t_y, mx+mw, t_y+40], fill=(250,250,249))
    cx2 = mx
    for hdr,cw2 in zip(headers,col_ws):
        d.text((cx2+12, t_y+20), hdr, fill=MUTED, font=f(F_MD,22), anchor='lm')
        d.line([cx2+cw2, t_y, cx2+cw2, t_y+40], fill=RULE, width=1)
        cx2 += cw2
    d.line([mx, t_y+40, mx+mw, t_y+40], fill=RULE_D, width=1)

    rows_data = [
        ('Acme Ltd','Active','Xero','€1,200','15th','Ltd','J. Moore'),
        ('Brio Co','Active','QuickBooks','€1,050','15th','Ltd','S. Chen'),
        ('Finova GmbH','Active','Xero','€900','20th','GmbH','M. Braun'),
        ('EasyPay Ltd','In Review','Wave','€780','10th','Ltd','K. Singh'),
        ('Novalux Inc','Active','Xero','€650','15th','Inc','T. Davis'),
        ('BlueWave','Active','QBO','€600','20th','LLC','P. White'),
        ('TechFlow','Churned','QuickBooks','€0','—','Ltd','—'),
        ('GreenBuild','Active','Sage','€850','15th','Ltd','C. Park'),
    ]
    status_colors = {'Active':GREEN,'In Review':AMBER,'Churned':RED}

    for ri,row in enumerate(rows_data):
        ry = t_y+42+ri*48
        d.rectangle([mx, ry, mx+mw, ry+46],
                    fill=WHITE if ri%2==0 else (252,252,251))
        d.line([mx, ry+46, mx+mw, ry+46], fill=RULE, width=1)
        cx3 = mx
        for ci2,(cell,cw3) in enumerate(zip(row,col_ws)):
            if ci2==0:
                d.ellipse([cx3+10,ry+13,cx3+30,ry+33], fill=TEAL_L)
                d.text((cx3+20,ry+23), cell[0], fill=TEAL, font=f(F_BO,18), anchor='mm')
                d.text((cx3+38,ry+23), cell, fill=NAVY, font=f(F_MD,24), anchor='lm')
            elif ci2==1:
                sc = status_colors.get(cell, MUTED)
                notion_status(d, cx3+cw3//2, ry+23, cell, sc)
            elif ci2==3:
                d.text((cx3+12,ry+23), cell, fill=TEAL, font=f(F_BO,24), anchor='lm')
            else:
                d.text((cx3+12,ry+23), str(cell)[:20], fill=NAVY, font=f(F_RG,22), anchor='lm')
            d.line([cx3+cw3, t_y, cx3+cw3, ry+46], fill=RULE, width=1)
            cx3 += cw3

    # Summary bar
    sum_y = t_y+42+len(rows_data)*48+8
    d.text((mx, sum_y+8), '8 records', fill=MUTED, font=f(F_MD,26), anchor='lt')
    d.text((mx+150, sum_y+8), '·  MRR: €6,030', fill=TEAL, font=f(F_MD,26), anchor='lt')
    d.text((mx+390, sum_y+8), '·  7 databases linked', fill=MUTED, font=f(F_RG,26), anchor='lt')
    d.text((mx+mw, sum_y+8), 'NOVAOPS Notion Template v3.0', fill=MUTED, font=f(F_RG,22), anchor='rm')

    img.save(f'{OUT}/04-Notion-Workspace.jpg', quality=96)
    print('  ✓ 04-Notion-Workspace.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 05 — FINANCIAL SYSTEM
# ══════════════════════════════════════════════════════════════════════════════

def img05_financial():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, H, (238,244,252), BG_COOL)

    # Header
    gradient_rect(d, 0, 0, W, 110, NAVY, NAVY_2)
    d.text((60, 55), 'EXCEL PRACTICE DASHBOARD', fill=WHITE, font=f(F_BK,44), anchor='lm')
    d.text((W-60, 35), '10 SHEETS', fill=TEAL, font=f(F_BK,38), anchor='rm')
    d.text((W-60, 82), 'All your numbers. One workbook.', fill=MUTED_L, font=f(F_RG,28), anchor='rm')

    # Sheet tabs
    tabs_data = [('Dashboard',True,TEAL),('Client CRM',False,None),
                 ('Lead Pipeline',False,None),('Monthly Close',False,None),
                 ('Invoices',False,None),('Pricing Calc',False,None),
                 ('Capacity',False,None),('Instructions',False,None)]
    tx = 0
    for tab,active,col in tabs_data:
        tw = len(tab)*17+44
        bg = col if active else (WHITE if not active else BG_SOFT)
        fc = WHITE if active else (NAVY if tw > 100 else MUTED)
        d.rectangle([tx, 110, tx+tw, 154], fill=bg if active else WHITE)
        d.line([tx+tw, 110, tx+tw, 154], fill=RULE, width=1)
        d.text((tx+tw//2, 132), tab, fill=fc if active else NAVY,
               font=f(F_MD if active else F_RG, 24), anchor='mm')
        tx += tw
    d.line([0, 154, W, 154], fill=RULE_D, width=2)

    # KPI row (6 tiles)
    kpi_data2 = [
        ('Monthly Revenue','€12,400','+8%',TEAL),('Active Clients','18','+2 this mo',GREEN),
        ('Pipeline Value','€6,200','4 leads',AMBER),('Avg Fee / Client','€689','Tier: Growth',PURPLE),
        ('MRR Target','€15,000','82% to goal',BLUE),('Capacity Used','78%','22% free',NAVY),
    ]
    kw3 = (W-100)//6-10
    for i,(lbl,val,sub,col) in enumerate(kpi_data2):
        kx3 = 50+i*(kw3+10)
        img, d = glass_card(img, kx3, 170, kw3, 118, r=10, fill=WHITE,
                            shadow_blur=12, shadow_alpha=28)
        d.rounded_rectangle([kx3,170,kx3+kw3,174], radius=2, fill=col)
        d.text((kx3+14,186), lbl, fill=MUTED, font=f(F_RG,22), anchor='lt')
        d.text((kx3+14,212), val, fill=NAVY, font=f(F_BK,48), anchor='lt')
        d.text((kx3+14,270), sub, fill=MUTED, font=f(F_RG,20), anchor='lt')

    # Revenue chart (left)
    c1_y = 308
    c1_w = int(W*0.56)-40
    c1_h = 340
    img, d = glass_card(img, 40, c1_y, c1_w, c1_h, r=12, fill=WHITE,
                        shadow_blur=16, shadow_alpha=32)
    d.text((60, c1_y+18), 'Revenue  (12-month)', fill=NAVY, font=f(F_BO,32), anchor='lt')
    d.text((60, c1_y+54), 'Monthly recurring + one-time', fill=MUTED, font=f(F_RG,24), anchor='lt')
    months12 = ['Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun']
    rev12 = [72,78,69,87,82,92,85,97,90,102,109,124]
    for i,yv in enumerate([0,4,8,12]):
        yl = c1_y+c1_h-40-int((c1_h-100)*yv/12)
        d.text((56, yl), f'€{yv}k', fill=MUTED_L, font=f(F_RG,18), anchor='rm')
        d.line([62, yl, 40+c1_w-12, yl], fill=RULE, width=1)
    bw4 = (c1_w-60)//12-3
    pts2 = []
    for i,(m,r) in enumerate(zip(months12,rev12)):
        bx4 = 60+i*(bw4+3)
        bh4 = int((c1_h-100)*r/124)
        d.rounded_rectangle([bx4,c1_y+c1_h-40-bh4,bx4+bw4,c1_y+c1_h-40],
                            radius=3, fill=AMBER if i==11 else TEAL)
        pts2.append((bx4+bw4//2, c1_y+c1_h-40-bh4))
        if i%2==0:
            d.text((bx4+bw4//2, c1_y+c1_h-22), m, fill=MUTED, font=f(F_RG,18), anchor='mm')
    if len(pts2)>1: d.line(pts2, fill=AMBER_M, width=2)

    # Invoice tracker (right)
    c2_x = 40+c1_w+20
    c2_w = W-c2_x-40
    img, d = glass_card(img, c2_x, c1_y, c2_w, c1_h, r=12, fill=WHITE,
                        shadow_blur=16, shadow_alpha=32)
    d.text((c2_x+16, c1_y+18), 'Invoice Tracker', fill=NAVY, font=f(F_BO,32), anchor='lt')
    d.text((c2_x+c2_w-16, c1_y+18), '€8,340 outstanding', fill=AMBER, font=f(F_BO,26), anchor='rm')
    # Table header
    d.rounded_rectangle([c2_x+8,c1_y+60,c2_x+c2_w-8,c1_y+92], radius=4, fill=TEAL)
    for j,(hdr,xoff) in enumerate([('#',0),('Client',76),('Amount',276),('Status',406)]):
        d.text((c2_x+16+xoff,c1_y+76), hdr, fill=WHITE, font=f(F_BO,22), anchor='lm')
    inv = [('#042','Acme Ltd','€1,200','Paid',GREEN),('#041','Brio Co','€1,050','Paid',GREEN),
           ('#040','Finova','€900','Sent',AMBER),('#039','EasyPay','€780','Sent',AMBER),
           ('#038','Novalux','€650','Overdue',RED),('#037','BlueWave','€600','Overdue',RED),
           ('#036','TechFlow','€400','Paid',GREEN),('#035','GreenBuild','€850','Paid',GREEN)]
    for ri2,(n0,n1,n2,st2,sc2) in enumerate(inv):
        ry2 = c1_y+98+ri2*30
        d.rectangle([c2_x+8,ry2,c2_x+c2_w-8,ry2+28],fill=BG_SOFT if ri2%2==0 else WHITE)
        d.text((c2_x+16,ry2+14), n0, fill=MUTED, font=f(F_RG,20), anchor='lm')
        d.text((c2_x+92,ry2+14), n1, fill=NAVY, font=f(F_MD,20), anchor='lm')
        d.text((c2_x+292,ry2+14), n2, fill=TEAL, font=f(F_BO,20), anchor='lm')
        d.rounded_rectangle([c2_x+418,ry2+5,c2_x+548,ry2+25], radius=8, fill=sc2)
        d.text((c2_x+483,ry2+15), st2, fill=WHITE, font=f(F_CB,18), anchor='mm')

    # Pricing calculator bar
    pc_y = c1_y+c1_h+18
    img, d = glass_card(img, 40, pc_y, W-80, 144, r=12, fill=NAVY,
                        shadow_blur=14, shadow_alpha=25)
    d.text((60, pc_y+18), 'Pricing Calculator', fill=WHITE, font=f(F_BO,32), anchor='lt')
    d.text((60, pc_y+56), 'Auto-calculates monthly fee from transaction volume →', fill=MUTED_L, font=f(F_RG,26), anchor='lt')
    tiers_data = [('Starter','≤ 150 txn/mo','€500/mo',False),
                  ('Growth','≤ 400 txn/mo','€850/mo',True),
                  ('Premium','≤ 800 txn/mo','€1,400/mo',False)]
    for i,(tier,txn,fee,hl) in enumerate(tiers_data):
        tx2 = 620+i*510
        d.rounded_rectangle([tx2,pc_y+12,tx2+480,pc_y+132], radius=10,
                            fill=NAVY_2 if not hl else TEAL_D)
        if hl:
            tag(d, tx2+290, pc_y+18, 'POPULAR', AMBER)
        d.text((tx2+18,pc_y+36), tier, fill=WHITE, font=f(F_BO,30), anchor='lt')
        d.text((tx2+18,pc_y+70), txn, fill=MUTED_L, font=f(F_RG,24), anchor='lt')
        d.text((tx2+460,pc_y+80), fee, fill=TEAL_M if not hl else WHITE, font=f(F_BK,38), anchor='rm')

    img.save(f'{OUT}/05-Financial-System.jpg', quality=96)
    print('  ✓ 05-Financial-System.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 06 — CLIENT EXPERIENCE (journey + document cards)
# ══════════════════════════════════════════════════════════════════════════════

def img06_client():
    img, d = new_canvas()

    gradient_rect(d, 0, 0, W, H, BG_SOFT, OFF_WHITE)
    gradient_rect(d, 0, 0, W, 112, NAVY, NAVY_2)
    d.text((W//2, 56), 'THE COMPLETE CLIENT EXPERIENCE', fill=WHITE, font=f(F_BK,48), anchor='mm')

    d.text((W//2, 140), 'Every document. Every conversation. Every workflow — done.',
           fill=MUTED, font=f(F_MD,32), anchor='mm')

    # Journey timeline (top horizontal)
    journey = [('Lead','📥',TEAL),('Proposal','📝',AMBER),('Agreement','⚖️',PURPLE),
               ('Onboarding','📋',BLUE),('Monthly Close','📅',TEAL_M),
               ('Reports','📊',GREEN),('Renewal','🔄',AMBER)]
    jw = W-100
    jx0 = 50
    jy = 186
    step_w = jw//len(journey)
    for i,(label,icon,col) in enumerate(journey):
        cx8 = jx0+i*step_w+step_w//2
        # Connector line
        if i < len(journey)-1:
            d.line([cx8+30, jy+30, cx8+step_w-30, jy+30], fill=RULE_D, width=3)
            d.text((cx8+step_w//2, jy+24), '→', fill=col, font=f(F_BO,28), anchor='mm')
        # Circle
        d.ellipse([cx8-30, jy, cx8+30, jy+60], fill=col)
        d.text((cx8, jy+30), icon, fill=WHITE, font=f(F_RG,32), anchor='mm')
        d.text((cx8, jy+74), label, fill=NAVY, font=f(F_MD,24), anchor='mm')

    # 6 document cards (2 rows x 3)
    docs = [
        ('📧','Bookkeeping\nService Guide','DOCX','5-tier service menu\nClear scope + pricing','Send to every\nprospect','Every prospect',TEAL),
        ('📝','Proposal\nTemplate','DOCX','Per-client scoped\nFees + timeline','Customise per\nopportunity','Per opportunity',AMBER),
        ('⚖️','Engagement\nAgreement','DOCX','15-clause contract\nLegal-grade structure','Sign before\nstarting','Before kick-off',PURPLE),
        ('📋','Client Intake\nOnboarding Pack','DOCX','5 structured sections\nDocument checklist','Send on\nsignature','Day 1',BLUE),
        ('🎤','Communication\nScripts','DOCX','10 email templates\nInquiry to year-end','Use every\nmonth','Ongoing',TEAL_M),
        ('📊','Proposal\nDeck','PPTX','10 consulting slides\nCanva-importable','Send with\nproposal','Visual pitch',TEAL),
    ]

    card_w2 = 820
    card_h2 = 500
    gx = (W-3*card_w2)//4
    gy_start = 284

    for i,(icon,title,fmt,desc,usage,timing,col) in enumerate(docs):
        col2 = i%3
        row2 = i//3
        cx9 = gx + col2*(card_w2+gx)
        cy9 = gy_start + row2*(card_h2+20)

        img, d = glass_card(img, cx9, cy9, card_w2, card_h2, r=14, fill=WHITE,
                            shadow_blur=18, shadow_alpha=36)
        d.rounded_rectangle([cx9,cy9,cx9+card_w2,cy9+6], radius=3, fill=col)

        # Icon
        d.ellipse([cx9+20,cy9+22,cx9+96,cy9+98], fill=TEAL_XL)
        d.text((cx9+58,cy9+60), icon, fill=col, font=f(F_RG,52), anchor='mm')

        # Format + timing tags
        tag(d, cx9+card_w2-84, cy9+22, fmt, col)
        tag(d, cx9+card_w2-90-len(timing)*16-20, cy9+22, timing, BG_COOL, MUTED)

        # Title
        title_lines = title.split('\n')
        for li,ln in enumerate(title_lines):
            d.text((cx9+110, cy9+32+li*44), ln, fill=NAVY, font=f(F_BO,36), anchor='lt')
        d.line([cx9+18,cy9+108,cx9+card_w2-18,cy9+108], fill=RULE, width=1)

        # Description
        desc_lines = desc.split('\n')
        for li,ln in enumerate(desc_lines):
            d.text((cx9+22,cy9+120+li*40), ln, fill=MUTED, font=f(F_MD,28), anchor='lt')

        d.line([cx9+18,cy9+212,cx9+card_w2-18,cy9+212], fill=RULE, width=1)
        d.text((cx9+22,cy9+226), 'WHEN TO USE', fill=TEAL, font=f(F_CB,22), anchor='lt')
        usage_lines = usage.split('\n')
        for li,ln in enumerate(usage_lines):
            d.text((cx9+22,cy9+256+li*38), f'→  {ln}', fill=NAVY, font=f(F_RG,28), anchor='lt')

    d.rectangle([0, H-70, W, H], fill=NAVY)
    d.text((W//2, H-35), 'Replace [BRACKETS] with Find & Replace  ·  Done in minutes  ·  NOVAOPS v3.0',
           fill=TEAL, font=f(F_CB,26), anchor='mm')

    img.save(f'{OUT}/06-Client-Experience.jpg', quality=96)
    print('  ✓ 06-Client-Experience.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 07 — WORKFLOW ROADMAP
# ══════════════════════════════════════════════════════════════════════════════

def img07_workflow():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, H, BG_SOFT, OFF_WHITE)

    # Left brand column
    d.rounded_rectangle([0, 0, 520, H], radius=0, fill=NAVY)
    # Subtle dot matrix
    for gx2 in range(20, 520, 40):
        for gy2 in range(20, H, 40):
            d.ellipse([gx2-1,gy2-1,gx2+1,gy2+1], fill=(28,38,58))

    d.text((260, 70), 'NOVAOPS', fill=TEAL, font=f(F_BK,42), anchor='mm')
    d.text((260, 124), 'Bookkeeper', fill=WHITE, font=f(F_BK,64), anchor='mm')
    d.text((260, 190), 'Practice', fill=WHITE, font=f(F_BK,64), anchor='mm')
    d.text((260, 256), 'Workflow', fill=TEAL, font=f(F_BK,64), anchor='mm')
    d.line([60, 290, 460, 290], fill=TEAL, width=2)
    d.text((260, 322), 'From first lead to', fill=MUTED_L, font=f(F_LT,32), anchor='mm')
    d.text((260, 360), 'repeat client —', fill=MUTED_L, font=f(F_LT,32), anchor='mm')
    d.text((260, 398), 'every step covered.', fill=MUTED_L, font=f(F_LT,32), anchor='mm')

    d.text((260, H-90), 'v3.0  ·  PREMIUM EDITION', fill=MUTED_L, font=f(F_CB,26), anchor='mm')
    d.text((260, H-52), '33 files  ·  90-min setup', fill=MUTED, font=f(F_RG,24), anchor='mm')

    # Workflow steps
    steps = [
        ('01','Lead Generation','Prospect identified via referral, LinkedIn, or network.',
         'Qualification criteria defined','Lead Pipeline (Excel + Notion)', TEAL),
        ('02','Discovery Call','Qualify entity type, volume, software, complexity, budget.',
         'Discovery questions documented','Intake Pack → Section 1', AMBER),
        ('03','Proposal Sent','Service Guide + scoped Proposal delivered within 24 hours.',
         'Pricing Calculator used','Service Guide + Proposal Template', TEAL),
        ('04','Agreement Signed','Engagement Agreement executed. Setup fee received.',
         'Legal review completed','Engagement Agreement', PURPLE),
        ('05','Onboarding','Intake Pack sent. Portal access granted. Documents collected.',
         'Access secured, books assessed','Intake Pack + SOPs', BLUE),
        ('06','Monthly Close','Reconcile → Categorise → Review → Adjust → Report.',
         'Every step documented','Dashboard + SOPs + Scripts', TEAL_M),
        ('07','Report Delivery','P&L + Balance Sheet delivered via Notion client portal.',
         'Exceptions documented','Client Portal + Scripts', GREEN),
        ('08','Renewal & Growth','Retain, upsell to next tier, request referral.',
         'Client relationship deepened','CRM + Proposal Template', AMBER),
        ('09','Repeat','Monthly cycle restarts. System scales automatically.',
         'Practice grows without chaos','All files, every month', TEAL),
    ]

    step_h = (H - 60)//len(steps)
    tl_x = 590

    for i,(num,title,desc,outcome,files,col) in enumerate(steps):
        sy = 30 + i*step_h
        mid_y = sy+step_h//2

        # Vertical connector
        if i < len(steps)-1:
            d.line([tl_x, mid_y+30, tl_x, mid_y+step_h], fill=RULE_D, width=3)

        # Step node
        r2 = 26
        img, d = glass_card(img, tl_x-r2, mid_y-r2, r2*2, r2*2,
                            r=r2, fill=col, shadow_blur=12, shadow_alpha=40)
        d.text((tl_x, mid_y), num, fill=WHITE, font=f(F_BO,26), anchor='mm')

        # Card
        card_x = tl_x+42
        card_w3 = W-card_x-30
        img, d = glass_card(img, card_x, sy+6, card_w3, step_h-14,
                            r=10, fill=WHITE, shadow_blur=10, shadow_alpha=25)
        d.rounded_rectangle([card_x, sy+6, card_x+card_w3, sy+12], radius=4, fill=col)

        d.text((card_x+16, sy+24), title, fill=NAVY, font=f(F_BO,28), anchor='lt')
        d.text((card_x+16, sy+56), desc, fill=MUTED, font=f(F_RG,22), anchor='lt')

        # Right tags
        tag(d, card_x+card_w3-340, sy+14, f'→  {outcome}', BG_SOFT, MUTED, 20)

    img.save(f'{OUT}/07-Business-Workflow.jpg', quality=96)
    print('  ✓ 07-Business-Workflow.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 08 — PREMIUM ASSETS LIST
# ══════════════════════════════════════════════════════════════════════════════

def img08_assets():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, H, (236,241,250), BG_COOL)

    gradient_rect(d, 0, 0, W, 110, NAVY, NAVY_2)
    d.text((60, 55), '33 PREMIUM FILES', fill=WHITE, font=f(F_BK,52), anchor='lm')
    d.text((W-60, 36), 'Instant Download', fill=TEAL, font=f(F_BO,30), anchor='rm')
    d.text((W-60, 80), 'All editable  ·  All branded  ·  All connected', fill=MUTED_L, font=f(F_RG,26), anchor='rm')

    format_colors = {'PDF':TEAL,'XLSX':GREEN,'DOCX':BLUE,'PPTX':AMBER,'CSV':PURPLE,'BONUS':NAVY}
    assets = [
        ('PDF','Read-Me-First.pdf','Complete product orientation — read before anything else'),
        ('PDF','Installation-Guide.pdf','Step-by-step 90-minute setup walkthrough'),
        ('PDF','Asset-Manifest.pdf','Full file inventory with descriptions'),
        ('PDF','License.pdf','Commercial use licence terms'),
        ('PDF','FAQ.pdf','16 questions — setup, Excel, Notion, licensing'),
        ('PDF','Version-History.pdf','Changelog + product roadmap'),
        ('PDF','Support-Guide.pdf','How to get help — response times + what to include'),
        ('PDF','QA-Report.pdf','Scored 91/100 — transparent quality assessment'),
        ('PDF','Notion-Setup-Guide.pdf','Import all 7 CSVs + connect Relations step by step'),
        ('XLSX','Practice-Dashboard-v3.xlsx','10 sheets: KPI Dashboard, CRM, Pipeline, Close, Invoices, Pricing…'),
        ('DOCX','Start-Here-v3.docx','Quick-reference overview and 90-minute checklist'),
        ('DOCX','Service-Guide-v3.docx','5-tier service menu with scope, pricing, and boundaries'),
        ('DOCX','Proposal-Template-v3.docx','Per-client scoped proposal — investment table + acceptance block'),
        ('DOCX','Engagement-Agreement-v3.docx','15-clause legal contract — requires lawyer review before use'),
        ('DOCX','Intake-Onboarding-Pack-v3.docx','Full client onboarding — 5 structured sections + checklists'),
        ('DOCX','SOPs-and-Checklists-v3.docx','4 SOPs: Onboarding, Monthly Close, Tax Prep, QC Framework'),
        ('DOCX','Communication-Scripts-v3.docx','10 email + portal scripts — inquiry to year-end handoff'),
        ('DOCX','Tax-Prep-Checklist-v3.docx','4-phase year-end document preparation system'),
        ('PPTX','Proposal-Deck-v3.pptx','10 consulting-grade slides — Canva-importable, fully editable'),
        ('CSV','Clients.csv','Master CRM database — 20 columns'),
        ('CSV','Leads.csv','Lead pipeline — 17 columns with source, stage, estimates'),
        ('CSV','Monthly-Close.csv','Close tracker — 16 columns with per-step status'),
        ('CSV','Document-Requests.csv','Document collection — 11 columns with reminder flag'),
        ('CSV','Invoices.csv','Invoice register — 13 columns including VAT + method'),
        ('CSV','Tasks.csv','Task management — 11 columns with recurring flag'),
        ('CSV','Client-Portal.csv','Client-visible portal items — 11 columns'),
    ]

    col1 = assets[:13]
    col2 = assets[13:]
    row_h = 56

    def draw_list(start_x, start_y, items):
        for i,(fmt,fname,fdesc) in enumerate(items):
            ay = start_y + i*row_h
            fc = format_colors.get(fmt, NAVY)
            d.rounded_rectangle([start_x, ay+8, start_x+82, ay+46], radius=6, fill=fc)
            d.text((start_x+41, ay+27), fmt, fill=WHITE, font=f(F_CB,22), anchor='mm')
            d.text((start_x+96, ay+18), fname, fill=NAVY, font=f(F_BO,24), anchor='lt')
            d.text((start_x+96, ay+44), fdesc[:68], fill=MUTED, font=f(F_RG,20), anchor='lt')
            d.line([start_x, ay+row_h-2, start_x+1290, ay+row_h-2], fill=RULE, width=1)

    draw_list(50, 134, col1)
    draw_list(1390, 134, col2)
    d.line([W//2, 118, W//2, H-90], fill=RULE_D, width=1)

    # Summary footer
    d.rectangle([0, H-90, W, H], fill=NAVY)
    summary = [('9','PDF Guides'),('9','DOCX Templates'),('1','Excel Dashboard'),
               ('1','PPTX Deck'),('7','Notion CSVs'),('6','PDF References')]
    sw3 = W//len(summary)
    for i,(n,lbl) in enumerate(summary):
        ix5 = i*sw3+sw3//2
        d.text((ix5, H-62), n, fill=TEAL, font=f(F_BK,40), anchor='mm')
        d.text((ix5, H-25), lbl, fill=MUTED_L, font=f(F_RG,22), anchor='mm')
        if i<len(summary)-1:
            d.line([ix5+sw3//2,H-84,ix5+sw3//2,H-8], fill=(38,50,72), width=1)

    img.save(f'{OUT}/08-Premium-Assets.jpg', quality=96)
    print('  ✓ 08-Premium-Assets.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 09 — WHO IS THIS FOR
# ══════════════════════════════════════════════════════════════════════════════

def img09_audience():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, H, BG_SOFT, OFF_WHITE)

    gradient_rect(d, 0, 0, W, 120, NAVY, NAVY_2)
    d.text((W//2, 50), 'WHO IS THIS FOR?', fill=WHITE, font=f(F_BK,50), anchor='mm')
    d.text((W//2, 96), 'Built for serious bookkeepers ready to run a premium, scalable practice.',
           fill=MUTED_L, font=f(F_MD,30), anchor='mm')

    audiences = [
        ('🧾','Freelance\nBookkeepers','Launch or upgrade your\npractice to premium.',
         TEAL,['Win clients at €500–€1,400/month','Stop ad-hoc documents forever','Look Big Four from day one']),
        ('🏢','Bookkeeping\nAgencies','Standardise operations\nacross your whole team.',
         AMBER,['Onboard new bookkeepers fast','Consistent client experience','Scale without chaos']),
        ('📊','Fractional\nCFOs','Add bookkeeping as a\nrevenue stream.',
         PURPLE,['Unified client management','Cross-sell bookkeeping + CFO','Seamless monthly reporting']),
        ('💻','Virtual\nBookkeepers','Run a fully remote\npractice with structure.',
         BLUE,['Notion portal included','Remote-first SOP system','All documents digital-ready']),
        ('📈','Finance\nConsultants','Enter bookkeeping with\nzero groundwork needed.',
         TEAL_M,['Ready to use on day one','Professional brand impression','Monthly recurring revenue']),
        ('🎓','New\nBookkeepers','Skip 3 years of\ntrial and error.',
         GREEN,['90-minute setup sequence','Know exactly what to do','Look experienced immediately']),
    ]

    card_w3 = 830
    card_h3 = 700
    gx2 = (W-3*card_w3)//4
    gy2 = 148

    for i,(icon,title,desc,col,benefits) in enumerate(audiences):
        col2 = i%3
        row2 = i//3
        cx10 = gx2+col2*(card_w3+gx2)
        cy10 = gy2+row2*(card_h3+20)

        img, d = glass_card(img, cx10, cy10, card_w3, card_h3, r=14,
                            fill=WHITE, shadow_blur=18, shadow_alpha=36)
        d.rounded_rectangle([cx10,cy10,cx10+card_w3,cy10+6], radius=3, fill=col)

        # Icon with color bg
        d.ellipse([cx10+20,cy10+22,cx10+108,cy10+110], fill=TEAL_XL)
        d.text((cx10+64,cy10+66), icon, fill=col, font=f(F_RG,60), anchor='mm')

        title_lines = title.split('\n')
        for li,ln in enumerate(title_lines):
            d.text((cx10+122,cy10+28+li*50), ln, fill=NAVY, font=f(F_BK,40), anchor='lt')

        d.line([cx10+18,cy10+118,cx10+card_w3-18,cy10+118], fill=RULE, width=1)

        desc_lines = desc.split('\n')
        for li,ln in enumerate(desc_lines):
            d.text((cx10+22,cy10+132+li*42), ln, fill=MUTED, font=f(F_RG,30), anchor='lt')

        d.line([cx10+18,cy10+232,cx10+card_w3-18,cy10+232], fill=RULE, width=1)
        d.text((cx10+22,cy10+250), 'WHAT YOU GET', fill=TEAL, font=f(F_CB,22), anchor='lt')

        for bi,ben in enumerate(benefits):
            by3 = cy10+288+bi*116
            img, d = glass_card(img, cx10+18, by3, card_w3-36, 98, r=8,
                                fill=BG_SOFT, shadow=False)
            d.rounded_rectangle([cx10+18,by3,cx10+28,by3+98], radius=4, fill=col)
            d.text((cx10+46, by3+49), ben, fill=NAVY, font=f(F_MD,28), anchor='lm')

    d.rectangle([0,H-72,W,H], fill=NAVY)
    d.text((W//2,H-36),
           'If you want to run a professional bookkeeping practice — this is your system.  ·  NOVAOPS v3.0',
           fill=WHITE, font=f(F_MD,28), anchor='mm')

    img.save(f'{OUT}/09-Who-Is-This-For.jpg', quality=96)
    print('  ✓ 09-Who-Is-This-For.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 10 — FINAL CTA (dark premium composition)
# ══════════════════════════════════════════════════════════════════════════════

def img10_cta():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, H, NAVY, NAVY_2)

    # Subtle grid
    for gx3 in range(0, W, 60):
        d.line([gx3,0,gx3,H], fill=(22,32,52), width=1)
    for gy3 in range(0, H, 60):
        d.line([0,gy3,W,gy3], fill=(22,32,52), width=1)

    # Glowing teal circle (bottom-left ambient)
    for r3 in range(300, 0, -10):
        alpha = int(6*(1-r3/300))
        tint = Image.new('RGBA',(W,H),(0,0,0,0))
        td = ImageDraw.Draw(tint)
        td.ellipse([-50,H-350-r3,r3*2-50,H+r3-350], fill=(*TEAL,alpha))
        img = Image.alpha_composite(img.convert('RGBA'), tint).convert('RGB')

    d = ImageDraw.Draw(img)

    # Left: device composition
    def laptop_dash(im, dd, sx, sy, sw, sh):
        dd.rectangle([sx,sy,sx+sw,sy+sh], fill=(14,20,36))
        dd.rectangle([sx,sy,sx+sw,sy+40], fill=(20,28,48))
        dd.text((sx+14,sy+20), '⊞  Practice Dashboard', fill=TEAL, font=f(F_MD,20), anchor='lm')
        dd.text((sx+sw-12,sy+20), '● Live', fill=GREEN, font=f(F_RG,18), anchor='rm')
        kw5 = (sw-16)//4
        ky5 = sy+48
        for i2,(lb2,vl2,co2) in enumerate([('MRR','€12.4k',GREEN),('Clients','18',TEAL),
                                            ('Pipeline','€6.2k',AMBER),('Close','78%',PURPLE)]):
            kx5=sx+8+i2*(kw5-1)
            dd.rounded_rectangle([kx5,ky5,kx5+kw5-5,ky5+60], radius=5, fill=(24,34,54))
            dd.rectangle([kx5,ky5,kx5+kw5-5,ky5+3], fill=co2)
            dd.text((kx5+8,ky5+12), lb2, fill=MUTED_L, font=f(F_RG,14), anchor='lt')
            dd.text((kx5+8,ky5+28), vl2, fill=WHITE, font=f(F_BO,26), anchor='lt')
        by4=ky5+72
        bh6=sh-by4+sy-12
        for i3,v4 in enumerate([68,74,62,81,88,100]):
            bx6=sx+8+i3*((sw-16)//6-2)
            bh7=int((bh6-16)*v4/100)
            col3=AMBER if i3==5 else TEAL
            dd.rounded_rectangle([bx6,by4+bh6-16-bh7,bx6+(sw-16)//6-5,by4+bh6-16],
                                 radius=2, fill=col3)

    sc4_x,sc4_y,sc4_w,sc4_h = laptop(img, 50, 100, 1080, laptop_dash)
    d = ImageDraw.Draw(img)

    # Floating iPad
    def ipad_fn(im,dd,sx,sy,sw,sh):
        dd.rectangle([sx,sy,sx+sw,sy+sh], fill=BG_SOFT)
        dd.text((sx+sw//2,sy+18), 'Clients', fill=NAVY, font=f(F_BO,20), anchor='mm')
        dd.line([sx,sy+36,sx+sw,sy+36], fill=RULE, width=1)
        for ri3,(n5,s5,f5) in enumerate([('Acme Ltd','Active','€1,200'),
                                         ('Brio Co','Active','€1,050'),
                                         ('Finova','Active','€900'),
                                         ('EasyPay','Review','€780')]):
            ry3=sy+44+ri3*38
            dd.rectangle([sx,ry3,sx+sw,ry3+36], fill=BG_SOFT if ri3%2==0 else WHITE)
            dd.text((sx+10,ry3+18), n5, fill=NAVY, font=f(F_MD,18), anchor='lm')
            dd.text((sx+sw-10,ry3+18), f5, fill=TEAL, font=f(F_BO,18), anchor='rm')
    ipad(img, 1010, 80, 290, ipad_fn)
    d = ImageDraw.Draw(img)

    # iPhone
    def iphone_fn(im,dd,sx,sy,sw,sh):
        dd.rectangle([sx,sy,sx+sw,sy+sh], fill=BG_SOFT)
        dd.text((sx+sw//2,sy+18), 'Invoice', fill=NAVY, font=f(F_BO,16), anchor='mm')
        dd.text((sx+sw//2,sy+60), '€1,200', fill=NAVY, font=f(F_BK,36), anchor='mm')
        dd.rounded_rectangle([sx+14,sy+96,sx+sw-14,sy+126], radius=8, fill=GREEN)
        dd.text((sx+sw//2,sy+111), 'PAID', fill=WHITE, font=f(F_CB,20), anchor='mm')
    iphone(img, 1070, 430, 200, iphone_fn)
    d = ImageDraw.Draw(img)

    # Right: CTA panel (white card)
    img, d = glass_card(img, 1310, 50, W-1360, H-100, r=20, fill=WHITE,
                        shadow_blur=30, shadow_alpha=30)

    d.text((1360, 100), 'Start Using It', fill=NAVY, font=f(F_BK,76), anchor='lt')
    d.text((1360, 182), 'Today.', fill=TEAL, font=f(F_BK,76), anchor='lt')
    d.line([1360, 276, W-80, 276], fill=RULE, width=2)

    d.text((1360, 300), 'Download once. Use forever.', fill=MUTED, font=f(F_MD,36), anchor='lt')
    d.text((1360, 346), 'Run your bookkeeping business', fill=NAVY, font=f(F_BO,36), anchor='lt')
    d.text((1360, 392), 'like a professional.', fill=NAVY, font=f(F_BO,36), anchor='lt')
    d.line([1360, 448, W-80, 448], fill=RULE, width=1)

    badges = [('✓','Instant Download',TEAL),('✓','33 Premium Files',GREEN),
              ('✓','Lifetime Access',TEAL),('✓','Fully Editable',AMBER),
              ('✓','Commercial License',PURPLE),('✓','Notion + Excel Included',NAVY)]
    for i,(sym,txt,col) in enumerate(badges):
        by5 = 472+i*76
        d.ellipse([1360,by5+6,1400,by5+46], fill=col)
        d.text((1380,by5+26), sym, fill=WHITE, font=f(F_BO,28), anchor='mm')
        d.text((1416,by5+26), txt, fill=NAVY, font=f(F_MD,32), anchor='lm')

    # CTA button
    d.rounded_rectangle([1360, H-216, W-80, H-136], radius=14, fill=TEAL)
    d.text(((1360+W-80)//2, H-176), '⬇   INSTANT DOWNLOAD', fill=WHITE, font=f(F_BK,38), anchor='mm')
    d.text(((1360+W-80)//2, H-138), 'Files delivered immediately after purchase',
           fill=TEAL_L, font=f(F_RG,24), anchor='mm')

    d.rounded_rectangle([1360, H-118, W-80, H-72], radius=10, fill=BG_SOFT)
    d.text(((1360+W-80)//2, H-95),
           'NOVAOPS  ·  Bookkeeper Practice Launch System  ·  v3.0',
           fill=NAVY, font=f(F_CB,22), anchor='mm')

    img.save(f'{OUT}/10-Final-CTA.jpg', quality=96)
    print('  ✓ 10-Final-CTA.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 11 — INSIDE THE DOWNLOAD (new)
# ══════════════════════════════════════════════════════════════════════════════

def img11_inside():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, H, (236,242,252), BG_COOL)

    # Header
    gradient_rect(d, 0, 0, W, 108, NAVY, NAVY_2)
    d.text((60, 54), 'INSIDE THE DOWNLOAD', fill=WHITE, font=f(F_BK,48), anchor='lm')
    d.text((W-60, 36), '33 Files', fill=TEAL, font=f(F_BK,36), anchor='rm')
    d.text((W-60, 78), 'Organised  ·  Named  ·  Ready to use', fill=MUTED_L, font=f(F_RG,26), anchor='rm')

    # Root folder
    root_y = 126
    img, d = glass_card(img, 40, root_y, W-80, 68, r=10, fill=NAVY,
                        shadow_blur=14, shadow_alpha=30)
    d.text((72, root_y+34), '📦', fill=WHITE, font=f(F_RG,36), anchor='mm')
    d.text((114, root_y+34), 'Bookkeeper-Practice-Launch-System-v3.0/', fill=WHITE, font=f(F_BK,32), anchor='lm')
    tag(d, W-280, root_y+14, '33 FILES', TEAL)

    folders = [
        ('00-START-HERE/', TEAL, '📂', [
            ('PDF','Read-Me-First.pdf'),('PDF','Installation-Guide.pdf'),
            ('PDF','Asset-Manifest.pdf'),('DOCX','Start-Here-v3.docx'),
        ]),
        ('01-Quick-Reference/', MUTED, '📂', [
            ('PDF','License.pdf'),('PDF','FAQ.pdf'),
            ('PDF','Version-History.pdf'),('PDF','Support-Guide.pdf'),
        ]),
        ('02-Practice-Dashboard/', GREEN, '📂', [
            ('XLSX','Bookkeeper-Practice-Dashboard-v3.xlsx'),
        ]),
        ('03-Client-Documents/', AMBER, '📂', [
            ('DOCX','Bookkeeping-Service-Guide-v3.docx'),
            ('DOCX','Bookkeeping-Proposal-Template-v3.docx'),
            ('DOCX','Bookkeeping-Engagement-Agreement-v3.docx'),
            ('DOCX','Client-Intake-and-Onboarding-Pack-v3.docx'),
            ('PPTX','Canva-Bookkeeping-Proposal-Deck-v3.pptx'),
        ]),
        ('04-Operations-Library/', PURPLE, '📂', [
            ('DOCX','Bookkeeping-SOPs-and-Checklists-v3.docx'),
            ('DOCX','Client-Communication-Scripts-v3.docx'),
            ('DOCX','Annual-Tax-Prep-Checklist-v3.docx'),
        ]),
        ('05-Notion-Workspace/', BLUE, '📂', [
            ('CSV','Clients.csv'),('CSV','Leads.csv'),('CSV','Monthly-Close.csv'),
            ('CSV','Document-Requests.csv'),('CSV','Invoices.csv'),
            ('CSV','Tasks.csv'),('CSV','Client-Portal.csv'),
            ('PDF','Notion-Setup-Guide.pdf'),
        ]),
    ]

    format_colors = {'PDF':TEAL,'XLSX':GREEN,'DOCX':BLUE,'PPTX':AMBER,'CSV':PURPLE}

    # Two-column layout
    col_w = (W-120)//2
    left_folders = folders[:3]
    right_folders = folders[3:]

    def draw_folder_block(f_list, start_x, start_y):
        cy = start_y
        for folder_name, col, icon, files in f_list:
            # Folder header
            img2, d2 = glass_card(img, start_x, cy, col_w, 56, r=8,
                                  fill=(*col[:3],), shadow_blur=10, shadow_alpha=25)
            d2.text((start_x+18, cy+28), f'{icon}  {folder_name}',
                    fill=WHITE, font=f(F_BO,28), anchor='lm')
            fc_count = f'{len(files)} file{"s" if len(files)>1 else ""}'
            tag(d2, start_x+col_w-len(fc_count)*14-40, cy+10, fc_count, (0,0,0,40), WHITE, 20)

            cy += 60
            for fi,(fmt,fname) in enumerate(files):
                f_y = cy + fi*50
                bg = WHITE if fi%2==0 else BG_SOFT
                img2, d2 = glass_card(img, start_x+20, f_y, col_w-20, 46,
                                      r=6, fill=bg, shadow=False)
                fc2 = format_colors.get(fmt, NAVY)
                d2.rounded_rectangle([start_x+28,f_y+8,start_x+86,f_y+38],
                                     radius=5, fill=fc2)
                d2.text((start_x+57,f_y+23), fmt, fill=WHITE, font=f(F_CB,20), anchor='mm')
                d2.text((start_x+96,f_y+23), fname, fill=NAVY, font=f(F_MD,22), anchor='lm')
                # Tree line
                d2.line([start_x+30,f_y-4,start_x+30,f_y+23], fill=RULE_D, width=2)
                d2.line([start_x+30,f_y+23,start_x+40,f_y+23], fill=RULE_D, width=2)

            cy += len(files)*50 + 18
        return cy

    draw_folder_block(left_folders, 50, 218)
    draw_folder_block(right_folders, 60+col_w, 218)

    # Footer
    d.rectangle([0,H-72,W,H], fill=NAVY)
    d.text((W//2,H-36),
           'Every file named, organised, and documented  ·  Open the ZIP and know exactly where everything is  ·  NOVAOPS v3.0',
           fill=TEAL, font=f(F_CB,26), anchor='mm')

    img.save(f'{OUT}/11-Inside-The-Download.jpg', quality=96)
    print('  ✓ 11-Inside-The-Download.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# RUN ALL
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print(f'Generating 11 premium world-class Etsy images → {OUT}\n')
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
    img11_inside()
    print(f'\nAll 11 images complete.')
