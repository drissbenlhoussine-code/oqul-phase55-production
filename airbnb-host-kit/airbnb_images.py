"""
NOVAOPS — Airbnb Host Starter Kit
10 Premium Etsy Listing Images — 2700×1800px
Stripe / Notion / Linear quality. Roboto. Glass cards. Device mockups.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

OUT = '/home/user/oqul-phase55-production/airbnb-host-kit/output/etsy-images'
os.makedirs(OUT, exist_ok=True)

W, H = 2700, 1800

NAVY    = (15, 23, 42)
NAVY_2  = (30, 41, 59)
NAVY_3  = (51, 65, 85)
TEAL    = (15, 118, 110)
TEAL_D  = (13, 94, 88)
TEAL_L  = (204, 251, 241)
TEAL_M  = (20, 184, 166)
TEAL_XL = (240, 253, 250)
AMBER   = (217, 119, 6)
AMBER_L = (254, 243, 199)
AMBER_M = (245, 158, 11)
WHITE   = (255, 255, 255)
OFF_W   = (252, 253, 255)
BG_SOFT = (248, 250, 252)
BG_COOL = (241, 245, 249)
RULE    = (226, 232, 240)
RULE_D  = (203, 213, 225)
MUTED   = (100, 116, 139)
MUTED_L = (148, 163, 184)
GREEN   = (34, 197, 94)
GREEN_D = (22, 163, 74)
GREEN_L = (220, 252, 231)
RED     = (239, 68, 68)
RED_L   = (254, 226, 226)
PURPLE  = (139, 92, 246)
PURPLE_L= (237, 233, 254)
BLUE    = (59, 130, 246)
BLUE_L  = (219, 234, 254)

F_BK = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Black.ttf'
F_BO = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Bold.ttf'
F_MD = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Medium.ttf'
F_RG = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf'
F_LT = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Light.ttf'
F_CB = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/RobotoCondensed-Bold.ttf'

def f(path, size): return ImageFont.truetype(path, size)

def new_canvas():
    img = Image.new('RGB', (W, H), BG_SOFT)
    return img, ImageDraw.Draw(img)

def drop_shadow(img, xy, w, h, radius=20, blur=18, alpha=50, color=(0,0,0)):
    sx, sy = xy[0]+10, xy[1]+12
    sl = Image.new('RGBA', (W, H), (0,0,0,0))
    sd = ImageDraw.Draw(sl)
    sd.rounded_rectangle([sx, sy, sx+w, sy+h], radius=radius, fill=(*color, alpha))
    sl = sl.filter(ImageFilter.GaussianBlur(blur))
    base = img.convert('RGBA')
    base = Image.alpha_composite(base, sl)
    img2 = base.convert('RGB')
    return img2, ImageDraw.Draw(img2)

def glass_card(img, x, y, w, h, r=16, fill_color=WHITE, shadow=True,
               shadow_blur=18, shadow_alpha=45, border_color=RULE):
    if shadow:
        img, d = drop_shadow(img, (x,y), w, h, radius=r, blur=shadow_blur, alpha=shadow_alpha)
    else:
        d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x+w, y+h], radius=r, fill=fill_color, outline=border_color, width=1)
    return img, d

def gradient_rect(d, x, y, w, h, c1, c2, vertical=True):
    n = h if vertical else w
    for i in range(n):
        t = i / max(n-1, 1)
        cr = int(c1[0]+(c2[0]-c1[0])*t)
        cg = int(c1[1]+(c2[1]-c1[1])*t)
        cb = int(c1[2]+(c2[2]-c1[2])*t)
        if vertical:
            d.line([x, y+i, x+w, y+i], fill=(cr,cg,cb))
        else:
            d.line([x+i, y, x+i, y+h], fill=(cr,cg,cb))

def laptop(img, cx, cy, sw=900):
    """Draw laptop mockup centered at cx, cy. Returns screen rect."""
    lid_h = int(sw * 0.63)
    base_h = int(sw * 0.06)
    total_h = lid_h + base_h
    lx = cx - sw//2
    ly = cy - total_h//2
    # Lid (screen bezel)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([lx, ly, lx+sw, ly+lid_h], radius=14, fill=NAVY_2)
    # Screen area (inner)
    pad = int(sw * 0.04)
    sc_x = lx + pad
    sc_y = ly + pad
    sc_w = sw - 2*pad
    sc_h = lid_h - 2*pad - int(sw*0.01)
    d.rectangle([sc_x, sc_y, sc_x+sc_w, sc_y+sc_h], fill=(8,15,30))
    # Camera dot
    cam_x = lx + sw//2
    cam_y = ly + int(pad*0.5)
    d.ellipse([cam_x-5, cam_y-5, cam_x+5, cam_y+5], fill=(40,55,75))
    # Base/keyboard
    bx = lx - int(sw*0.06)
    by = ly + lid_h
    bw = sw + int(sw*0.12)
    d.rounded_rectangle([bx, by, bx+bw, by+base_h], radius=4, fill=NAVY_3)
    # Trackpad groove
    tp_w = int(sw*0.25)
    tp_h = int(base_h*0.55)
    tp_x = bx + bw//2 - tp_w//2
    tp_y = by + (base_h-tp_h)//2
    d.rounded_rectangle([tp_x, tp_y, tp_x+tp_w, tp_y+tp_h], radius=3,
                         fill=NAVY_2, outline=NAVY_3, width=1)
    return sc_x, sc_y, sc_w, sc_h

def tag(d, x, y, text, bg, fg=WHITE, size=22, r=8, pad=16):
    fnt = f(F_CB, size)
    bbox = fnt.getbbox(text)
    tw = bbox[2] - bbox[0]
    w = tw + pad*2
    h = (bbox[3] - bbox[1]) + pad
    d.rounded_rectangle([x, y, x+w, y+h], radius=r, fill=bg)
    d.text((x+pad, y+pad//2), text, fill=fg, font=fnt, anchor='lt')
    return w

def pill(d, x, y, text, bg, fg=WHITE, size=20):
    fnt = f(F_MD, size)
    bb = fnt.getbbox(text)
    tw = bb[2]-bb[0]
    w = tw+28; h=34
    d.rounded_rectangle([x, y, x+w, y+h], radius=17, fill=bg)
    d.text((x+w//2, y+h//2), text, fill=fg, font=fnt, anchor='mm')
    return w

def bottom_bar(img, d, text='AIRBNB HOST STARTER KIT  ·  v1.0  ·  NOVAOPS  ·  PROFESSIONAL HOST OPERATING SYSTEM'):
    d.rectangle([0, H-72, W, H], fill=NAVY)
    d.text((W//2, H-36), text, fill=TEAL_M, font=f(F_CB, 24), anchor='mm')

def check_row(d, x, y, text, dot_color=TEAL, size=32, dot_r=14):
    d.ellipse([x, y-dot_r, x+dot_r*2, y+dot_r], fill=dot_color)
    d.text((x+dot_r, y), '✓', fill=WHITE, font=f(F_BO, size-8), anchor='mm')
    d.text((x+dot_r*2+18, y), text, fill=NAVY, font=f(F_MD, size), anchor='lm')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 01 — HERO
# ══════════════════════════════════════════════════════════════════════════════

def img01_hero():
    img, d = new_canvas()
    # Left panel — dark navy
    gradient_rect(d, 0, 0, 780, H, NAVY, NAVY_2, vertical=False)
    # NOVAOPS wordmark
    d.text((56, 62), 'NOVAOPS', fill=TEAL, font=f(F_BK, 48), anchor='lt')
    # Main headline
    for i, (line, color) in enumerate([
        ('Airbnb Host', WHITE),
        ('Starter Kit', TEAL),
    ]):
        d.text((56, 148+i*118), line, fill=color, font=f(F_BK, 108), anchor='lt')
    d.text((56, 390), 'Professional Host', fill=MUTED_L, font=f(F_LT, 38), anchor='lt')
    d.text((56, 434), 'Operating System', fill=MUTED_L, font=f(F_LT, 38), anchor='lt')
    d.line([56, 498, 720, 498], fill=(40,55,78), width=1)
    checks = [
        '8 Professional Documents',
        '15 Guest Message Templates',
        'Excel Operations Dashboard',
        '5-Star Review System',
        'Cleaning + Check-In SOPs',
        'Pricing & Revenue Calculator',
    ]
    for i, c in enumerate(checks):
        check_row(d, 56, 548+i*76, c, TEAL, 30, 13)
    # Version badge
    img, d = glass_card(img, 56, H-146, 640, 68, r=10, fill_color=AMBER, shadow=False)
    d.text((56+320, H-112), 'INSTANT DOWNLOAD  ·  COMMERCIAL USE  ·  v1.0',
           fill=WHITE, font=f(F_CB, 25), anchor='mm')

    # Laptop on right with dashboard screen
    sc_x, sc_y, sc_w, sc_h = laptop(img, 1720, 820, 960)
    d = ImageDraw.Draw(img)
    # Dashboard content on screen
    d.rectangle([sc_x, sc_y, sc_x+sc_w, sc_y+sc_h], fill=(10,18,32))
    # Top browser bar
    d.rectangle([sc_x, sc_y, sc_x+sc_w, sc_y+38], fill=NAVY_2)
    d.ellipse([sc_x+10,sc_y+12,sc_x+22,sc_y+26], fill=(239,68,68))
    d.ellipse([sc_x+28,sc_y+12,sc_x+40,sc_y+26], fill=AMBER_M)
    d.ellipse([sc_x+46,sc_y+12,sc_x+58,sc_y+26], fill=GREEN_D)
    d.text((sc_x+sc_w//2, sc_y+19), 'Host Operations Dashboard', fill=MUTED_L, font=f(F_RG,16), anchor='mm')
    # Sidebar
    sb_w = int(sc_w*0.22)
    d.rectangle([sc_x, sc_y+38, sc_x+sb_w, sc_y+sc_h], fill=NAVY)
    d.text((sc_x+sb_w//2, sc_y+60), 'NOVAOPS', fill=TEAL_M, font=f(F_BK,14), anchor='mm')
    nav_items = ['📊 Dashboard','📅 Bookings','💰 Expenses','🧹 Cleaning','🔧 Maintenance','⭐ Reviews','📈 Analytics']
    for i, item in enumerate(nav_items):
        ny = sc_y+80+i*46
        if i == 0:
            d.rounded_rectangle([sc_x+6,ny-6,sc_x+sb_w-6,ny+30], radius=6, fill=TEAL)
            d.text((sc_x+16,ny+12), item, fill=WHITE, font=f(F_MD,15), anchor='lm')
        else:
            d.text((sc_x+16,ny+12), item, fill=MUTED_L, font=f(F_RG,14), anchor='lm')
    # KPI tiles
    mx = sc_x + sb_w + 12
    mw = sc_w - sb_w - 24
    d.text((mx, sc_y+52), 'June 2025  ·  Live', fill=MUTED_L, font=f(F_RG,14), anchor='lt')
    d.text((mx, sc_y+72), 'Host Dashboard', fill=WHITE, font=f(F_BK,26), anchor='lt')
    kpis = [('Revenue','€4,080','↑ 18%',TEAL),('Bookings','8','This month',BLUE),
            ('Occupancy','89%','Peak season',GREEN_D),('Rating','4.9 ★','Superhost',AMBER_M)]
    kw = (mw-36)//4
    for ki, (lbl,val,sub,col) in enumerate(kpis):
        kx = mx + ki*(kw+12)
        ky = sc_y+108
        d.rounded_rectangle([kx,ky,kx+kw,ky+70], radius=6, fill=NAVY_2)
        d.rectangle([kx,ky,kx+kw,ky+3], fill=col)
        d.text((kx+8,ky+12), lbl, fill=MUTED_L, font=f(F_RG,11), anchor='lt')
        d.text((kx+8,ky+28), val, fill=WHITE, font=f(F_BO,18), anchor='lt')
        d.text((kx+8,ky+54), sub, fill=col, font=f(F_RG,11), anchor='lt')

    bottom_bar(img, d)
    img.save(f'{OUT}/01-Hero.jpg', quality=96)
    print('  ✓ 01-Hero.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 02 — WHAT'S INCLUDED
# ══════════════════════════════════════════════════════════════════════════════

def img02_included():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, 128, NAVY, NAVY_2)
    d.text((W//2, 50), 'EVERYTHING INCLUDED', fill=WHITE, font=f(F_BK, 48), anchor='mm')
    d.text((W//2, 98), 'One purchase. Every system a professional Airbnb host needs.',
           fill=MUTED_L, font=f(F_MD, 30), anchor='mm')

    categories = [
        ('📋', 'QUICK START GUIDE', TEAL, 'Setup · Navigation',
         [('3-Phase Launch Roadmap',''),('System Navigation Map',''),
          ('Monthly Host Review Checklist',''),('KPI Tracking Framework','')]),
        ('🏠', 'LISTING OPTIMIZATION', BLUE, 'Title · Photos · SEO',
         [('64-Character Title Formula',''),('FEAT Description Method',''),
          ('20-Shot Photo Blueprint',''),('Amenity Priority Matrix','')]),
        ('💬', 'GUEST COMMUNICATION', PURPLE, '15 Message Templates',
         [('Pre-Booking + Confirmation',''),('Pre-Arrival × 3 Sequences',''),
          ('Mid-Stay + Post-Checkout',''),('Damage, Complaints, Reviews','')]),
        ('📊', 'OPERATIONS DASHBOARD', GREEN_D, '8-Sheet Excel System',
         [('Booking Revenue Tracker',''),('Expense + Tax Tracker',''),
          ('Pricing Calculator',''),('Cleaning + Maintenance Logs','')]),
        ('📖', 'GUEST EXPERIENCE', AMBER, 'Manual · Rules',
         [('House Manual Template',''),('House Rules Template',''),
          ('Local Area Guide Format',''),('Emergency Contacts Page','')]),
        ('⚙️', 'SOP LIBRARY', (120, 60, 200), 'Check-In · Cleaning · Reviews',
         [('Check-In Standard Operating Procedure',''),('Room-by-Room Cleaning Protocol',''),
          ('Review Strategy + Templates',''),('Damage Reporting Procedure','')]),
    ]

    cw = (W-100)//3
    ch = (H-170)//2
    for idx, (icon, title, color, badge, items) in enumerate(categories):
        col = idx % 3
        row = idx // 3
        cx = 50 + col*(cw+25)
        cy = 138 + row*(ch+25)
        img, d = glass_card(img, cx, cy, cw, ch, r=14, fill_color=WHITE, shadow_alpha=38)
        d.rounded_rectangle([cx, cy, cx+cw, cy+5], radius=3, fill=color)
        # Icon circle
        ir = 36
        d.ellipse([cx+24, cy+22, cx+24+ir*2, cy+22+ir*2], fill=(*color[:3],30) if len(color)==3 else color)
        d.text((cx+24+ir, cy+22+ir), icon, fill=color, font=f(F_RG, 38), anchor='mm')
        d.text((cx+24+ir*2+16, cy+32), title, fill=NAVY, font=f(F_BO, 24), anchor='lt')
        tag(d, cx+24+ir*2+16, cy+62, badge, color, WHITE, 18)
        # Items
        for i, (item, _) in enumerate(items):
            iy = cy + 108 + i*54
            d.ellipse([cx+24, iy+10, cx+24+22, iy+32], fill=TEAL_L)
            d.text((cx+24+11, iy+21), '✓', fill=TEAL, font=f(F_BO, 14), anchor='mm')
            d.text((cx+56, iy+20), item, fill=NAVY, font=f(F_MD, 24), anchor='lm')

    bottom_bar(img, d, '8 DOCUMENTS  ·  8 EXCEL SHEETS  ·  15 MESSAGE TEMPLATES  ·  NOVAOPS AIRBNB HOST STARTER KIT')
    img.save(f'{OUT}/02-Whats-Included.jpg', quality=96)
    print('  ✓ 02-Whats-Included.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 03 — OPERATIONS DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════

def img03_dashboard():
    img, d = new_canvas()
    # Top bar: browser chrome
    d.rectangle([0, 0, W, 64], fill=NAVY_2)
    for i, col in enumerate([(239,68,68), AMBER_M, GREEN_D]):
        d.ellipse([16+i*28, 22, 36+i*28, 42], fill=col)
    d.rounded_rectangle([180, 18, W-300, 46], radius=10, fill=NAVY_3)
    d.text((W//2-60, 32), 'app.novaops.io/airbnb-dashboard', fill=MUTED_L, font=f(F_RG, 20), anchor='mm')

    # App header
    d.rectangle([0, 64, W, 130], fill=NAVY)
    d.text((60, 97), '⊞  NOVAOPS · Airbnb Host Dashboard', fill=WHITE, font=f(F_BO, 28), anchor='lm')
    d.text((W-60, 97), '● Live  ·  June 2025', fill=GREEN, font=f(F_RG, 24), anchor='rm')

    # Sidebar
    sb_w = 220
    d.rectangle([0, 130, sb_w, H-72], fill=NAVY)
    d.text((sb_w//2, 162), 'NOVAOPS', fill=TEAL_M, font=f(F_BK, 20), anchor='mm')
    nav = [('📊','Dashboard',True),('📅','Bookings',False),('💰','Expenses',False),
           ('🧹','Cleaning',False),('🔧','Maintenance',False),('⭐','Reviews',False),('📈','Analytics',False)]
    for i,(icon,label,active) in enumerate(nav):
        ny = 190+i*66
        if active:
            d.rounded_rectangle([10,ny-4,sb_w-10,ny+46], radius=8, fill=TEAL)
            d.text((28,ny+20), f'{icon}  {label}', fill=WHITE, font=f(F_MD,22), anchor='lm')
        else:
            d.text((28,ny+20), f'{icon}  {label}', fill=MUTED_L, font=f(F_RG,20), anchor='lm')

    # Main content
    mx = sb_w + 30
    mw = W - mx - 30
    d.text((mx, 152), 'June 2025 — Host Performance Overview', fill=NAVY, font=f(F_BK, 36), anchor='lt')
    d.text((mx, 194), 'Superhost Active  ·  8 Bookings  ·  All metrics updated in real time',
           fill=MUTED, font=f(F_RG, 22), anchor='lt')

    # KPI tiles
    kpis = [
        ('GROSS REVENUE','€4,080','+18% vs. May',TEAL),
        ('NET PROFIT','€2,640','+€420 vs. May',GREEN_D),
        ('OCCUPANCY RATE','89%','Peak season',BLUE),
        ('AVG RATING','4.9 ★','Superhost: ✓',AMBER_M),
    ]
    kw = (mw-45)//4
    ky = 228
    kh = 110
    for ki, (lbl, val, sub, col) in enumerate(kpis):
        kx = mx + ki*(kw+15)
        img, d = glass_card(img, kx, ky, kw, kh, r=10, fill_color=WHITE, shadow_alpha=35)
        d.rectangle([kx, ky, kx+kw, ky+4], fill=col)
        d.text((kx+16, ky+18), lbl, fill=MUTED, font=f(F_RG, 18), anchor='lt')
        d.text((kx+16, ky+46), val, fill=NAVY, font=f(F_BK, 42), anchor='lt')
        arrow = '↑' if '+' in sub else ''
        sub_col = GREEN_D if '+' in sub else MUTED
        d.text((kx+16, ky+96), f'{arrow} {sub}', fill=sub_col, font=f(F_MD, 18), anchor='lm')

    # Revenue bar chart
    chart_y = 360
    chart_h = 280
    chart_w = int(mw*0.62)
    img, d = glass_card(img, mx, chart_y, chart_w, chart_h+60, r=10, fill_color=WHITE, shadow_alpha=30)
    d.text((mx+18, chart_y+16), 'Monthly Revenue — 2025', fill=NAVY, font=f(F_BO, 26), anchor='lt')
    d.text((mx+18, chart_y+46), '12-month rolling', fill=MUTED, font=f(F_RG, 18), anchor='lt')
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    vals = [850,720,980,1100,1350,1680,1820,1750,1200,980,760,1420]
    max_v = max(vals)
    bw = (chart_w-60)//(len(months)+1)
    for mi, (m, v) in enumerate(zip(months, vals)):
        bx = mx+30+mi*(bw+8)
        bh = int((v/max_v)*chart_h*0.82)
        by = chart_y+chart_h+30-bh
        col = TEAL if mi == 5 else ((*TEAL_L,) if mi < 5 else RULE_D)
        d.rounded_rectangle([bx, by, bx+bw, chart_y+chart_h+30], radius=4, fill=col)
        if mi == 5:
            d.text((bx+bw//2, by-12), f'€{v//1000:.1f}k', fill=TEAL, font=f(F_BO,16), anchor='mm')
        d.text((bx+bw//2, chart_y+chart_h+46), m, fill=MUTED, font=f(F_RG,16), anchor='mm')

    # Recent bookings table
    ct_x = mx + chart_w + 20
    ct_w = mw - chart_w - 20
    img, d = glass_card(img, ct_x, chart_y, ct_w, chart_h+60, r=10, fill_color=WHITE, shadow_alpha=30)
    d.text((ct_x+16, chart_y+16), 'Recent Bookings', fill=NAVY, font=f(F_BO,26), anchor='lt')
    d.text((ct_x+ct_w-16, chart_y+16), 'MRR: €4,080', fill=TEAL, font=f(F_BO,22), anchor='rm')
    headers = ['Guest','Nights','Payout','Rating']
    hw = ct_w//len(headers)
    d.rectangle([ct_x, chart_y+52, ct_x+ct_w, chart_y+74], fill=NAVY)
    for hi, h in enumerate(headers):
        d.text((ct_x+hi*hw+hw//2, chart_y+63), h, fill=WHITE, font=f(F_CB,18), anchor='mm')
    rows = [('Sarah J.','4','€408','5 ★'),('Marcus T.','3','€306','5 ★'),
            ('Priya K.','5','€510','5 ★'),('Tom B.','2','€204','4 ★'),
            ('Chloe M.','6','€612','5 ★')]
    for ri, (g,n,p,r) in enumerate(rows):
        ry = chart_y+80+ri*50
        bg = BG_SOFT if ri%2==0 else WHITE
        d.rectangle([ct_x, ry, ct_x+ct_w, ry+46], fill=bg)
        vals_r = [g,n,p,r]
        for ci, v in enumerate(vals_r):
            col = GREEN_D if v.endswith('★') and v[0]=='5' else NAVY
            fnt = f(F_MD,20) if ci<2 else f(F_BO,20)
            d.text((ct_x+ci*hw+hw//2, ry+23), v, fill=col, font=fnt, anchor='mm')

    # Bottom monthly close strip
    strip_y = chart_y + chart_h + 76
    d.rectangle([mx, strip_y, mx+mw, strip_y+50], fill=NAVY)
    closes = [('Bookings','8',WHITE),('Nights Sold','26',TEAL_M),('Occupancy','89%',GREEN),
              ('Avg Rate','€157',AMBER_M),('Revenue','€4,080',TEAL_M),('Expenses','€1,440',MUTED_L),
              ('Net Profit','€2,640',GREEN),('Rating','4.9 ★',AMBER_M)]
    cw2 = mw//len(closes)
    for ci,(lbl,val,col) in enumerate(closes):
        cx2 = mx+ci*cw2+cw2//2
        d.text((cx2, strip_y+14), lbl, fill=MUTED_L, font=f(F_RG,14), anchor='mm')
        d.text((cx2, strip_y+36), val, fill=col, font=f(F_BO,18), anchor='mm')

    bottom_bar(img, d)
    img.save(f'{OUT}/03-Operations-Dashboard.jpg', quality=96)
    print('  ✓ 03-Operations-Dashboard.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 04 — MESSAGE TEMPLATES
# ══════════════════════════════════════════════════════════════════════════════

def img04_messages():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, 120, NAVY, NAVY_2)
    d.text((W//2, 50), 'GUEST COMMUNICATION SYSTEM', fill=WHITE, font=f(F_BK, 50), anchor='mm')
    d.text((W//2, 96), '15 production-ready templates · Every scenario covered · Copy, personalise, send.',
           fill=MUTED_L, font=f(F_MD, 28), anchor='mm')

    templates = [
        ('SEQUENCE 1 — PRE-BOOKING', TEAL, [
            ('01', 'Inquiry Response', 'Thank you for your interest in [PROPERTY NAME]! To confirm everything lines up...'),
            ('02', 'Booking Confirmation', 'Your booking is confirmed — welcome to [PROPERTY NAME]! I\'m really looking forward...'),
        ]),
        ('SEQUENCE 2 — PRE-ARRIVAL', BLUE, [
            ('03', '7 Days Before', 'Just a friendly note — your stay at [PROPERTY NAME] is one week away!...'),
            ('04', '48h Access Instructions', 'Your arrival is in two days — here\'s everything: Address: [ADDRESS], Code: [CODE]...'),
            ('05', 'Day of Arrival', 'Today\'s the day! Everything is ready. Fresh coffee and a small welcome treat awaits...'),
        ]),
        ('SEQUENCE 3 — DURING & AFTER', GREEN_D, [
            ('06', 'Mid-Stay Check-In', 'Hope you\'re having a wonderful stay at [PROPERTY NAME]! Just a quick note to check...'),
            ('07', 'Check-Out Reminder', 'Hope you\'ve had a brilliant stay! Check-out is by [TIME] tomorrow. Please leave key...'),
            ('08', 'Post-Stay + Review Request', 'Thank you so much for staying — it was a pleasure having you. If you have a moment...'),
        ]),
        ('SPECIAL SITUATIONS', PURPLE, [
            ('09', 'Late Check-Out (Approve)', 'Of course — no problem at all! You\'re welcome to check out by [APPROVED TIME]...'),
            ('10', 'Late Check-Out (Decline)', 'I appreciate you asking — I\'m sorry I can\'t accommodate this today...'),
            ('11', 'Early Check-In (Approve)', 'Great news — the property is ready early. Check-in confirmed from [TIME]!...'),
            ('12', 'Noise Complaint', 'I hope you\'re having a great stay. I\'ve received a note from a neighbour...'),
            ('13', 'Property Damage', 'Thank you for your stay. During the inspection, I noticed [DAMAGE DESCRIPTION]...'),
            ('14', '5-Star Review Response', 'Thank you so much, [NAME] — what a wonderful review! It was a genuine pleasure...'),
            ('15', 'Negative Review Response', 'Thank you for sharing your feedback. I\'m sorry to hear [ISSUE] didn\'t meet expectations...'),
        ]),
    ]

    cw = (W-100)//2
    left_col = [templates[0], templates[2]]
    right_col = [templates[1], templates[3]]

    y_offset = 136
    for col_idx, col_templates in enumerate([left_col, right_col]):
        cx = 50 + col_idx*(cw+20)
        cy = y_offset
        for seq_title, color, tmpl_list in col_templates:
            # Section header
            img, d = glass_card(img, cx, cy, cw, 42, r=6, fill_color=color, shadow=False)
            d.text((cx+16, cy+21), seq_title, fill=WHITE, font=f(F_CB, 22), anchor='lm')
            cy += 48
            for num, title, preview in tmpl_list:
                h_tmpl = 96
                img, d = glass_card(img, cx, cy, cw, h_tmpl, r=8, fill_color=WHITE, shadow_alpha=28)
                # Number badge
                d.rounded_rectangle([cx+12, cy+14, cx+52, cy+50], radius=6, fill=color)
                d.text((cx+32, cy+32), num, fill=WHITE, font=f(F_BO, 20), anchor='mm')
                d.text((cx+62, cy+26), title, fill=NAVY, font=f(F_BO, 24), anchor='lt')
                # Preview text (truncated)
                preview_short = preview[:65] + ('...' if len(preview) > 65 else '')
                d.text((cx+62, cy+56), f'"{preview_short}"',
                       fill=MUTED, font=f(F_RG, 18), anchor='lt')
                # Tag
                tag(d, cx+cw-100, cy+14, 'READY', GREEN_D, WHITE, 16)
                cy += h_tmpl + 10
            cy += 14

    bottom_bar(img, d, '15 MESSAGE TEMPLATES  ·  EVERY GUEST SCENARIO  ·  COPY · PERSONALISE [BRACKETS] · SEND  ·  NOVAOPS')
    img.save(f'{OUT}/04-Message-Templates.jpg', quality=96)
    print('  ✓ 04-Message-Templates.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 05 — GUEST EXPERIENCE
# ══════════════════════════════════════════════════════════════════════════════

def img05_experience():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, 120, NAVY, NAVY_2)
    d.text((W//2, 50), 'GUEST EXPERIENCE SYSTEM', fill=WHITE, font=f(F_BK, 50), anchor='mm')
    d.text((W//2, 96), 'House Manual · House Rules · Local Guide · Pricing Strategy',
           fill=MUTED_L, font=f(F_MD, 28), anchor='mm')

    # Left: House Manual preview
    cw = (W-120)//2
    img, d = glass_card(img, 50, 140, cw, H-240, r=14, fill_color=WHITE, shadow_alpha=40)

    d.rectangle([50, 140, 50+cw, 196], fill=TEAL)
    d.text((50+cw//2, 168), '📖  HOUSE MANUAL TEMPLATE', fill=WHITE, font=f(F_CB, 26), anchor='mm')
    d.text((50+20, 212), 'Guest-facing guide. Customise once.', fill=NAVY, font=f(F_BO, 24), anchor='lt')
    d.text((50+20, 242), 'Reduces guest messages by 60–70%', fill=MUTED, font=f(F_RG, 22), anchor='lt')

    sections = [
        ('🔑', 'Access & Entry', 'Door code, parking, key return instructions'),
        ('📶', 'WiFi & Technology', 'Network, password, Smart TV, streaming accounts'),
        ('🍳', 'Kitchen Guide', '8 appliances documented. Coffee machine, oven, dishwasher.'),
        ('🛏', 'Bedrooms & Bathrooms', 'Bed types, towels, toiletries, hair dryer location'),
        ('🌡', 'Heating & Cooling', 'Thermostat guide, AC remotes, energy saving note'),
        ('✅', 'Check-Out Instructions', '8-step check-out guide — no confusion, smooth handover'),
        ('🆘', 'Emergency Contacts', 'Host, building manager, gas, medical — all in one place'),
        ('🗺', 'Local Area Guide', 'Coffee, restaurants, transport, attractions — personal picks'),
    ]
    for i, (icon, title, desc) in enumerate(sections):
        sy = 286 + i * 118
        bg = TEAL_XL if i % 2 == 0 else WHITE
        d.rectangle([50+12, sy, 50+cw-12, sy+108], fill=bg)
        d.text((50+28, sy+24), icon, fill=TEAL, font=f(F_RG, 32), anchor='lt')
        d.text((50+78, sy+18), title, fill=NAVY, font=f(F_BO, 26), anchor='lt')
        d.text((50+78, sy+52), desc, fill=MUTED, font=f(F_RG, 20), anchor='lt')
        d.line([50+28, sy+88, 50+cw-28, sy+88], fill=RULE, width=1)

    # Right: House Rules + Pricing
    rx = 50 + cw + 20
    rw = W - rx - 50

    # House Rules
    img, d = glass_card(img, rx, 140, rw, 740, r=14, fill_color=WHITE, shadow_alpha=40)
    d.rectangle([rx, 140, rx+rw, 196], fill=AMBER)
    d.text((rx+rw//2, 168), '📋  HOUSE RULES TEMPLATE', fill=WHITE, font=f(F_CB, 26), anchor='mm')
    rules_sections = [
        ('CHECK-IN & CHECK-OUT', 'Arrival/departure times, access, code sharing'),
        ('GUESTS & OCCUPANCY', 'Max occupancy, overnight guests, visitors'),
        ('NOISE & NEIGHBOURS', 'Quiet hours, gatherings policy, enforcement'),
        ('SMOKING & SUBSTANCES', 'Indoor ban, designated area, penalties'),
        ('PETS POLICY', 'Both allowed/not-allowed versions included'),
        ('PROPERTY CARE', 'Damage reporting, furniture, candles, toilets'),
        ('PARKING', 'Spaces, restrictions, EV charging note'),
        ('SECURITY & DEPARTURE', 'Lock-up checklist, key return, utilities'),
    ]
    for i, (title, desc) in enumerate(rules_sections):
        sy = 206 + i * 76
        bg = AMBER_L if i % 2 == 0 else WHITE
        d.rectangle([rx+12, sy, rx+rw-12, sy+68], fill=bg)
        d.ellipse([rx+22, sy+18, rx+44, sy+40], fill=AMBER)
        d.text((rx+33, sy+29), '✓', fill=WHITE, font=f(F_BO, 14), anchor='mm')
        d.text((rx+52, sy+14), title, fill=NAVY, font=f(F_BO, 20), anchor='lt')
        d.text((rx+52, sy+40), desc, fill=MUTED, font=f(F_RG, 18), anchor='lt')

    # Pricing Strategy card
    img, d = glass_card(img, rx, 904, rw, H-240-904+140, r=14, fill_color=WHITE, shadow_alpha=40)
    d.rectangle([rx, 904, rx+rw, 960], fill=NAVY)
    d.text((rx+rw//2, 932), '🧮  PRICING STRATEGY GUIDE', fill=TEAL_M, font=f(F_CB, 26), anchor='mm')
    pricing = [
        ('Base Rate Formula', 'Cost-plus method — know your minimum viable rate'),
        ('Seasonal Tiers', 'Low 0.85× · Shoulder 1.00× · High 1.35× · Peak 1.75×'),
        ('Dynamic Pricing', 'Last-minute fills, weekend premium, long-stay discount'),
        ('Calculator Included', 'Enter your costs → Excel outputs your optimal rate'),
    ]
    for i, (title, desc) in enumerate(pricing):
        sy = 970 + i*92
        img, d = glass_card(img, rx+12, sy, rw-24, 80, r=8, fill_color=BG_SOFT, shadow=False)
        d.text((rx+28, sy+16), title, fill=NAVY, font=f(F_BO, 22), anchor='lt')
        d.text((rx+28, sy+46), desc, fill=MUTED, font=f(F_RG, 19), anchor='lt')

    bottom_bar(img, d)
    img.save(f'{OUT}/05-Guest-Experience.jpg', quality=96)
    print('  ✓ 05-Guest-Experience.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 06 — SOP LIBRARY
# ══════════════════════════════════════════════════════════════════════════════

def img06_sops():
    img, d = new_canvas()
    # Dark left panel
    gradient_rect(d, 0, 0, 680, H, NAVY, NAVY_2, vertical=False)
    d.text((54, 62), 'SOP LIBRARY', fill=TEAL, font=f(F_BK, 48), anchor='lt')
    d.text((54, 126), 'Standard Operating', fill=WHITE, font=f(F_BK, 52), anchor='lt')
    d.text((54, 186), 'Procedures', fill=WHITE, font=f(F_BK, 52), anchor='lt')
    d.text((54, 262), 'The same 5-star result.', fill=MUTED_L, font=f(F_LT, 30), anchor='lt')
    d.text((54, 302), 'Every single time.', fill=MUTED_L, font=f(F_LT, 30), anchor='lt')
    d.line([54, 350, 626, 350], fill=(40,55,78), width=1)

    sop_overview = [
        ('Check-In SOP', '22 steps', TEAL),
        ('Cleaning SOP', '68+ items', GREEN_D),
        ('Review Strategy', '7 sections', AMBER_M),
    ]
    for i, (name, count, col) in enumerate(sop_overview):
        sy = 378+i*106
        d.rounded_rectangle([54, sy, 626, sy+90], radius=10, fill=NAVY_3)
        d.text((80, sy+45), name, fill=WHITE, font=f(F_BO, 28), anchor='lm')
        tag(d, 400, sy+22, count, col, WHITE, 20)
    d.text((54, H-106), '3 SOPs  ·  100+ action items', fill=MUTED_L, font=f(F_MD, 26), anchor='lt')
    d.text((54, H-72), 'Ready to share with your team', fill=MUTED_L, font=f(F_RG, 22), anchor='lt')

    # Right: Cleaning SOP detail
    sop_x = 708
    sop_w = W - sop_x - 40

    d.text((sop_x, 40), 'CLEANING SOP — Room-by-Room Protocol', fill=NAVY, font=f(F_BK, 38), anchor='lt')
    d.text((sop_x, 88), 'Studio: 1.5h · 2BR: 2.5–3h · 3BR: 3.5–4h · Same standard every turnover',
           fill=MUTED, font=f(F_RG, 22), anchor='lt')

    rooms = [
        ('🍳 KITCHEN', TEAL, [
            'All dishes washed and stored in correct cupboards',
            'Hob, oven and countertops disinfected and dried streak-free',
            'Coffee machine cleaned and stocked with fresh pods',
            'Fridge emptied of previous guest food — shelves wiped',
            'Consumables restocked: coffee, tea, sugar, kitchen roll',
            'Bin empty with fresh bag · Floor swept and mopped',
        ]),
        ('🛁 BATHROOM(S)', BLUE, [
            'Toilet cleaned: rim, seat, bowl, exterior, base, handle',
            'Shower/bath scrubbed: walls, floor, door, plughole',
            'Mirror: clean and streak-free (check in different light)',
            'Toiletry dispensers refilled if below one-third',
            'Fresh towels staged hotel-style on rail',
            'Toilet roll on holder · Spare under sink',
        ]),
        ('🛏 BEDROOM(S)', PURPLE, [
            'All linen stripped and placed in laundry bag',
            'Mattress inspected — any damage reported immediately',
            'Fresh fitted sheet, duvet cover, pillowcases: hotel standard',
            'Wardrobe and drawers empty and wiped inside',
            'Bedside lamps and USB chargers tested and working',
            'Floor vacuumed including corners and under furniture',
        ]),
        ('🛋 LIVING ROOM', AMBER_M, [
            'Sofa: crumbs removed, cushions fluffed, throws folded',
            'Remote controls wiped with antibacterial wipe',
            'Smart TV set to home screen — not previous guest\'s account',
            'All surfaces dusted including skirting and lamp shades',
            'Windows: inside glass clean, no smears or fingerprints',
            'Floor vacuumed throughout including under furniture',
        ]),
    ]

    row_h2 = (H-170)//2
    for idx, (room, color, items) in enumerate(rooms):
        col = idx % 2
        row = idx // 2
        rx = sop_x + col*((sop_w-20)//2+10)
        ry = 128 + row*(row_h2+20)
        rw2 = (sop_w-20)//2
        img, d = glass_card(img, rx, ry, rw2, row_h2, r=12, fill_color=WHITE, shadow_alpha=32)
        d.rounded_rectangle([rx, ry, rx+rw2, ry+46], radius=8, fill=color)
        d.text((rx+16, ry+23), room, fill=WHITE, font=f(F_CB, 24), anchor='lm')
        tag(d, rx+rw2-100, ry+10, '6 steps', WHITE, color, 18)
        for ii, item in enumerate(items):
            iy = ry+58+ii*102
            d.ellipse([rx+16, iy+6, rx+38, iy+28], fill=(*color[:3],25))
            d.text((rx+27, iy+17), '✓', fill=color, font=f(F_BO,14), anchor='mm')
            d.text((rx+48, iy+16), item, fill=NAVY, font=f(F_MD, 20), anchor='lt')

    bottom_bar(img, d)
    img.save(f'{OUT}/06-SOP-Library.jpg', quality=96)
    print('  ✓ 06-SOP-Library.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 07 — REVIEW STRATEGY
# ══════════════════════════════════════════════════════════════════════════════

def img07_reviews():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, 120, NAVY, NAVY_2)
    d.text((W//2, 50), 'REVIEW STRATEGY SYSTEM', fill=WHITE, font=f(F_BK, 50), anchor='mm')
    d.text((W//2, 96), 'Get 5-star reviews consistently · Respond professionally · Protect Superhost status',
           fill=MUTED_L, font=f(F_MD, 28), anchor='mm')

    cw3 = (W-120)//3
    panels = [
        ('🌟', '4.8+', 'Superhost threshold', TEAL,
         'Rating Strategy',
         ['Top 10 5-star drivers identified','Welcome pack boosts reviews by 40%',
          'WiFi speed is most-mentioned factor','Bedding quality drives cleanliness score',
          'Host communication speed matters most','Accurate listing = no surprises = 5 stars']),
        ('✉️', '75%+', 'Target review rate', AMBER,
         'Request System',
         ['Optimal timing: within 1h of checkout','Personal tone outperforms generic asks',
          'Reciprocal commitment: "I\'ll review you too"','No "5-star" language — Airbnb policy',
          'One polite follow-up after 5 days','Leave guest review first to encourage theirs']),
        ('🛡', '100%', 'Response rate target', BLUE,
         'Response Templates',
         ['5-star response (2–4 sentences)','4-star + minor issue response',
          '3-star professional response','Negative review: factual not defensive',
          'Unfair review: dispute framework','Retaliation response strategy']),
    ]

    for idx, (icon, stat, stat_sub, color, title, items) in enumerate(panels):
        px = 50 + idx*(cw3+20)
        py = 140
        ph = H-240
        img, d = glass_card(img, px, py, cw3, ph, r=14, fill_color=WHITE, shadow_alpha=35)
        # Top accent
        d.rounded_rectangle([px, py, px+cw3, py+6], radius=3, fill=color)
        # Icon + stat
        ir = 44
        d.ellipse([px+24, py+22, px+24+ir*2, py+22+ir*2], fill=(*color[:3], 20) if True else color)
        # use lighter version
        light = TEAL_L if color==TEAL else (AMBER_L if color==AMBER else BLUE_L)
        d.ellipse([px+24, py+22, px+24+ir*2, py+22+ir*2], fill=light)
        d.text((px+24+ir, py+22+ir), icon, fill=color, font=f(F_RG, 44), anchor='mm')
        d.text((px+24+ir*2+16, py+28), stat, fill=NAVY, font=f(F_BK, 42), anchor='lt')
        d.text((px+24+ir*2+16, py+76), stat_sub, fill=MUTED, font=f(F_RG, 20), anchor='lt')
        # Title bar
        d.rounded_rectangle([px+12, py+108, px+cw3-12, py+150], radius=6, fill=color)
        d.text((px+cw3//2, py+129), title, fill=WHITE, font=f(F_CB, 24), anchor='mm')
        # Items
        for ii, item in enumerate(items):
            iy = py+164+ii*108
            d.ellipse([px+22, iy+8, px+46, iy+32], fill=light)
            d.text((px+34, iy+20), '→', fill=color, font=f(F_BO, 16), anchor='mm')
            d.text((px+56, iy+8), item, fill=NAVY, font=f(F_MD, 22), anchor='lt')

    bottom_bar(img, d, 'REVIEW STRATEGY GUIDE  ·  RESPONSE TEMPLATES INCLUDED  ·  SUPERHOST ACCELERATION PLAN  ·  NOVAOPS')
    img.save(f'{OUT}/07-Review-Strategy.jpg', quality=96)
    print('  ✓ 07-Review-Strategy.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 08 — PRICING & REVENUE
# ══════════════════════════════════════════════════════════════════════════════

def img08_pricing():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, 120, NAVY, NAVY_2)
    d.text((W//2, 50), 'PRICING & REVENUE SYSTEM', fill=WHITE, font=f(F_BK, 50), anchor='mm')
    d.text((W//2, 96), 'Know your break-even rate · Dynamic seasonal pricing · Maximise RevPAR',
           fill=MUTED_L, font=f(F_MD, 28), anchor='mm')

    # Left: Calculator inputs
    lw = (W-120)//2
    img, d = glass_card(img, 50, 140, lw, H-240, r=14, fill_color=WHITE, shadow_alpha=40)
    d.rectangle([50, 140, 50+lw, 196], fill=TEAL)
    d.text((50+lw//2, 168), '🧮  PRICING CALCULATOR — LIVE FORMULA', fill=WHITE, font=f(F_CB, 26), anchor='mm')

    d.text((80, 220), 'Enter your costs. Get your optimal rate.', fill=NAVY, font=f(F_BO, 26), anchor='lt')
    d.text((80, 256), 'No guesswork. No undercharging. No leaving money on the table.',
           fill=MUTED, font=f(F_RG, 22), anchor='lt')

    inputs = [
        ('Monthly mortgage / rent', '€850', TEAL_L),
        ('Utilities (electricity + gas + internet)', '€185', TEAL_L),
        ('STR insurance (monthly)', '€55', TEAL_L),
        ('Cleaning cost per turnover', '€80', TEAL_L),
        ('Consumables per turnover', '€30', TEAL_L),
        ('Platform fee % (Airbnb)', '3%', TEAL_L),
        ('Target bookings per month', '6 stays', TEAL_L),
    ]
    for i, (label, val, bg) in enumerate(inputs):
        iy = 302 + i*88
        d.rectangle([66, iy, 66+lw-32, iy+72], fill=BG_SOFT if i%2==0 else WHITE)
        d.text((82, iy+20), label, fill=MUTED, font=f(F_MD, 20), anchor='lt')
        d.text((82, iy+46), val, fill=NAVY, font=f(F_BK, 28), anchor='lt')
        # Value box
        vbox_x = 66+lw-32-120
        d.rounded_rectangle([vbox_x, iy+14, vbox_x+110, iy+52], radius=6, fill=TEAL_L)
        d.text((vbox_x+55, iy+33), val, fill=TEAL, font=f(F_BO, 24), anchor='mm')

    d.rectangle([66, 920, 66+lw-32, 922], fill=RULE, )

    # Results
    results = [
        ('Break-Even Nightly Rate', '€63', MUTED),
        ('Min Viable Rate (+10% margin)', '€69', MUTED),
        ('→  RECOMMENDED BASE RATE', '€79', TEAL),
        ('Weekend Premium (+25%)', '€99', AMBER_M),
        ('Peak Season Rate (+50%)', '€119', AMBER),
    ]
    for i, (label, val, col) in enumerate(results):
        ry = 936 + i*92
        is_rec = '→' in label
        bg = AMBER_L if is_rec else (BG_SOFT if i%2==0 else WHITE)
        d.rectangle([66, ry, 66+lw-32, ry+76], fill=bg)
        if is_rec:
            d.rectangle([66, ry, 70, ry+76], fill=AMBER)
        d.text((92, ry+18), label, fill=NAVY if is_rec else MUTED,
               font=f(F_BO if is_rec else F_MD, 20), anchor='lt')
        d.text((92, ry+46), val, fill=col, font=f(F_BK, 36), anchor='lt')

    # Right: Seasonal pricing + annual projections
    rx = 50 + lw + 20
    rw = W - rx - 50

    img, d = glass_card(img, rx, 140, rw, 420, r=14, fill_color=WHITE, shadow_alpha=40)
    d.rectangle([rx, 140, rx+rw, 196], fill=AMBER)
    d.text((rx+rw//2, 168), '📅  SEASONAL PRICING GUIDE', fill=WHITE, font=f(F_CB, 26), anchor='mm')

    seasons = [
        ('Low Season', 'Jan–Feb, Nov', '0.85×', '€67',  GREEN_L,  GREEN_D),
        ('Shoulder',   'Mar–May, Sep–Oct','1.00×','€79', BG_SOFT,  NAVY),
        ('High Season','Jun–Aug, Dec',  '1.35×', '€107', TEAL_XL,  TEAL),
        ('Peak Events','Bank hols, events','1.75×','€138', AMBER_L,  AMBER),
        ('Last Minute','Gaps < 3 days', '0.90×', '€71',  PURPLE_L, PURPLE),
        ('Long Stay',  '7+ nights',     '0.92×', '€73',  BLUE_L,   BLUE),
    ]
    sh = (420-70)//len(seasons)
    for i, (name, period, mult, rate, bg, col) in enumerate(seasons):
        sy = 206 + i*sh
        d.rectangle([rx+12, sy, rx+rw-12, sy+sh-4], fill=bg)
        d.text((rx+24, sy+sh//2-12), name, fill=NAVY, font=f(F_BO, 22), anchor='lt')
        d.text((rx+24, sy+sh//2+12), period, fill=MUTED, font=f(F_RG, 18), anchor='lt')
        d.text((rx+rw//2, sy+sh//2), mult, fill=col, font=f(F_BK, 28), anchor='mm')
        d.text((rx+rw-100, sy+sh//2), rate, fill=col, font=f(F_BK, 28), anchor='mm')
        if i < len(seasons)-1:
            d.line([rx+12, sy+sh-4, rx+rw-12, sy+sh-4], fill=RULE, width=1)

    # Annual revenue projection
    img, d = glass_card(img, rx, 580, rw, 400, r=14, fill_color=WHITE, shadow_alpha=40)
    d.rectangle([rx, 580, rx+rw, 636], fill=NAVY)
    d.text((rx+rw//2, 608), '📈  ANNUAL REVENUE PROJECTION', fill=WHITE, font=f(F_CB, 26), anchor='mm')

    proj = [
        ('Conservative (65% occupancy)', '€14,200 / year', MUTED),
        ('Moderate (75% occupancy)', '€18,600 / year', TEAL),
        ('Optimised (85% occupancy + seasonal)', '€24,800 / year', GREEN_D),
    ]
    for i, (scenario, rev, col) in enumerate(proj):
        py = 652 + i*106
        d.rectangle([rx+12, py, rx+rw-12, py+90], fill=BG_SOFT if i%2==0 else WHITE)
        d.text((rx+24, py+20), scenario, fill=MUTED, font=f(F_MD, 20), anchor='lt')
        d.text((rx+24, py+54), rev, fill=col, font=f(F_BK, 38), anchor='lt')

    # Metric cards
    metrics = [
        ('RevPAR', '€138', 'At peak season'),
        ('ROI', '62%', 'Net margin target'),
        ('Break-Even', '€63/night', 'Minimum viable rate'),
    ]
    mw2 = rw//len(metrics)
    for i, (label, val, note) in enumerate(metrics):
        mx2 = rx + i*mw2
        img, d = glass_card(img, mx2+8, 1000, mw2-16, 100, r=10, fill_color=BG_SOFT, shadow=False)
        d.text((mx2+mw2//2, 1022), label, fill=MUTED, font=f(F_MD, 20), anchor='mm')
        d.text((mx2+mw2//2, 1055), val, fill=TEAL, font=f(F_BK, 34), anchor='mm')
        d.text((mx2+mw2//2, 1086), note, fill=MUTED, font=f(F_RG, 17), anchor='mm')

    bottom_bar(img, d)
    img.save(f'{OUT}/08-Pricing-Revenue.jpg', quality=96)
    print('  ✓ 08-Pricing-Revenue.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 09 — WHO IS THIS FOR
# ══════════════════════════════════════════════════════════════════════════════

def img09_audience():
    img, d = new_canvas()
    gradient_rect(d, 0, 0, W, 120, NAVY, NAVY_2)
    d.text((W//2, 50), 'WHO IS THIS KIT FOR?', fill=WHITE, font=f(F_BK, 50), anchor='mm')
    d.text((W//2, 96), 'Built for serious hosts ready to operate a professional, scalable Airbnb business.',
           fill=MUTED_L, font=f(F_MD, 28), anchor='mm')

    audiences = [
        ('🏠','New Airbnb Hosts','Just listed or about to go live.', TEAL,
         ['Launch with professional systems from day 1','Avoid the most common new-host mistakes',
          'Set up automated guest communication','Get your first 10 reviews faster']),
        ('📈','Hosts Wanting 5 Stars','Currently getting 4.5 — want consistent 4.9.', AMBER,
         ['Identify the exact gaps lowering your score','Implement hotel-standard cleaning protocols',
          'Use the review strategy to boost response rate','Fix your listing title and description']),
        ('🔄','Hosts Who Are Overwhelmed','Spending hours on messages and logistics.', BLUE,
         ['15 templates eliminate repetitive messaging','Automate your communication sequence',
          'Brief your cleaner with a professional SOP','Spend 3h/week instead of 15h/week']),
        ('💼','Multi-Property Managers','Running 2+ properties or managing for others.', GREEN_D,
         ['Standardise operations across all properties','Use one dashboard for all bookings',
          'Co-host agreement template included','Track revenue and expenses per property']),
        ('💡','Side-Income Optimisers','Want to maximise yield without full-time effort.', PURPLE,
         ['Pricing calculator shows exact optimal rate','Seasonal pricing strategy maximises revenue',
          'Operations run smoothly with minimal input','Financial tracker ready for tax reporting']),
        ('🎯','Aspiring Superhosts','Want the Superhost badge within 90 days.', (217, 70, 50),
         ['4.8+ rating strategy with specific actions','Review acceleration plan for new hosts',
          '90%+ response rate with saved message system','Complete Superhost criteria checklist']),
    ]

    cw = (W-100)//3
    ch = (H-190)//2
    for idx, (icon, title, sub, color, benefits) in enumerate(audiences):
        col = idx % 3
        row = idx // 3
        cx = 50 + col*(cw+25)
        cy = 140 + row*(ch+20)
        img, d = glass_card(img, cx, cy, cw, ch, r=14, fill_color=WHITE, shadow_alpha=35)
        d.rounded_rectangle([cx, cy, cx+cw, cy+5], radius=3, fill=color)
        ir = 38
        light_map = {TEAL:TEAL_L, AMBER:AMBER_L, BLUE:BLUE_L, GREEN_D:GREEN_L,
                     PURPLE:PURPLE_L, (217,70,50):RED_L}
        light = light_map.get(color, BG_SOFT)
        d.ellipse([cx+22, cy+18, cx+22+ir*2, cy+18+ir*2], fill=light)
        d.text((cx+22+ir, cy+18+ir), icon, fill=color, font=f(F_RG, 38), anchor='mm')
        d.text((cx+22+ir*2+14, cy+26), title, fill=NAVY, font=f(F_BO, 26), anchor='lt')
        d.text((cx+22+ir*2+14, cy+58), sub, fill=MUTED, font=f(F_RG, 20), anchor='lt')
        d.line([cx+16, cy+92, cx+cw-16, cy+92], fill=RULE, width=1)
        for bi, benefit in enumerate(benefits):
            by = cy+106+bi*92
            d.ellipse([cx+20, by+8, cx+44, by+32], fill=light)
            d.text((cx+32, by+20), '✓', fill=color, font=f(F_BO,14), anchor='mm')
            d.text((cx+52, by+20), benefit, fill=NAVY, font=f(F_MD, 22), anchor='lm')

    bottom_bar(img, d, 'AIRBNB HOST STARTER KIT  ·  FOR EVERY HOST AT EVERY STAGE  ·  NOVAOPS PROFESSIONAL HOST OPERATING SYSTEM')
    img.save(f'{OUT}/09-Who-Is-This-For.jpg', quality=96)
    print('  ✓ 09-Who-Is-This-For.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# IMAGE 10 — FINAL CTA
# ══════════════════════════════════════════════════════════════════════════════

def img10_cta():
    img, d = new_canvas()
    # Full dark background
    gradient_rect(d, 0, 0, W, H, NAVY, NAVY_2)
    # Ambient teal glow
    glow = Image.new('RGBA', (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    for r in range(600, 0, -10):
        alpha = int(18 * (1 - r/600))
        gd.ellipse([W//2-r-300, H//2-r, W//2+r-300, H//2+r], fill=(*TEAL, alpha))
    img = Image.alpha_composite(img.convert('RGBA'), glow).convert('RGB')
    d = ImageDraw.Draw(img)

    # Left device composition — laptop
    sc_x, sc_y, sc_w, sc_h = laptop(img, 820, 850, 800)
    d = ImageDraw.Draw(img)
    # Screen content: dashboard
    d.rectangle([sc_x, sc_y, sc_x+sc_w, sc_y+sc_h], fill=(10,18,32))
    d.rectangle([sc_x, sc_y, sc_x+sc_w, sc_y+32], fill=NAVY_2)
    d.text((sc_x+sc_w//2, sc_y+16), 'Airbnb Host Dashboard  ·  NOVAOPS', fill=MUTED_L, font=f(F_RG,14), anchor='mm')
    kk = [('Revenue','€4,080',TEAL_M),('Occupancy','89%',GREEN),('Rating','4.9 ★',AMBER_M)]
    kw = sc_w//3
    for ki,(lbl,val,col) in enumerate(kk):
        kx = sc_x+ki*kw+10
        d.rounded_rectangle([kx,sc_y+40,kx+kw-20,sc_y+100], radius=5, fill=NAVY_3)
        d.text((kx+kw//2-10, sc_y+56), lbl, fill=MUTED_L, font=f(F_RG,12), anchor='mm')
        d.text((kx+kw//2-10, sc_y+82), val, fill=col, font=f(F_BO,18), anchor='mm')

    # Right: CTA card
    card_x = W - 1100
    card_w = 1040
    img, d = glass_card(img, card_x, 120, card_w, H-280, r=20,
                         fill_color=WHITE, shadow_blur=30, shadow_alpha=60)
    d.text((card_x+card_w//2, 200), 'NOVAOPS', fill=TEAL, font=f(F_BK, 44), anchor='mm')
    d.text((card_x+card_w//2, 272), 'Airbnb Host', fill=NAVY, font=f(F_BK, 62), anchor='mm')
    d.text((card_x+card_w//2, 340), 'Starter Kit', fill=NAVY, font=f(F_BK, 62), anchor='mm')

    d.line([card_x+60, 378, card_x+card_w-60, 378], fill=RULE, width=1)

    items = [
        '8 Professional Documents',
        '15 Guest Message Templates',
        'Excel Operations Dashboard (8 sheets)',
        'Check-In + Cleaning SOPs',
        'Review Strategy System',
        'Pricing Calculator + Strategy Guide',
        'Instant Download · Lifetime Access',
    ]
    for i, item in enumerate(items):
        iy = 402+i*80
        d.ellipse([card_x+56, iy+2, card_x+82, iy+28], fill=TEAL_L)
        d.text((card_x+69, iy+15), '✓', fill=TEAL, font=f(F_BO,14), anchor='mm')
        d.text((card_x+94, iy+15), item, fill=NAVY, font=f(F_MD, 26), anchor='lm')

    # Download button
    btn_y = H-240
    d.rounded_rectangle([card_x+60, btn_y, card_x+card_w-60, btn_y+88], radius=14, fill=TEAL)
    d.text((card_x+card_w//2, btn_y+44), '⬇   INSTANT DOWNLOAD', fill=WHITE, font=f(F_BK, 36), anchor='mm')
    d.text((card_x+card_w//2, btn_y+88+20), 'Files delivered immediately after purchase',
           fill=MUTED, font=f(F_RG, 22), anchor='mm')
    d.rounded_rectangle([card_x+60, btn_y+120, card_x+card_w-60, btn_y+160], radius=10, fill=BG_SOFT)
    d.text((card_x+card_w//2, btn_y+140),
           'NOVAOPS  ·  Airbnb Host Starter Kit  ·  v1.0',
           fill=NAVY, font=f(F_CB, 20), anchor='mm')

    img.save(f'{OUT}/10-Final-CTA.jpg', quality=96)
    print('  ✓ 10-Final-CTA.jpg')


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print(f'Generating 10 premium Etsy images → {OUT}')
    print()
    img01_hero()
    img02_included()
    img03_dashboard()
    img04_messages()
    img05_experience()
    img06_sops()
    img07_reviews()
    img08_pricing()
    img09_audience()
    img10_cta()
    print()
    print('All 10 images complete.')
