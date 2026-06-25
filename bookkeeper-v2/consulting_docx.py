"""
NOVAOPS — Bookkeeper Practice Launch System v2.0
Consulting-grade DOCX Builder — Premium Edition
Design: McKinsey / Deloitte / PwC + NovaOps brand identity

Visual upgrades over v1:
  • NovaOps branding on every page (header, footer, cover)
  • Full-width two-tone section headers (teal number + dark navy title)
  • Premium three-strip cover (teal top + dark body + amber bottom)
  • At-a-glance stat cards at the start of every document
  • Proper ☐ / ✓ checklist items with teal accent
  • → icon bullets replacing plain list bullets
  • Horizontal process flow diagrams with numbered steps
  • Side-by-side comparison panels
  • Generous white space, improved spacing throughout
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/v2-consulting'

# ── NovaOps Brand Palette ─────────────────────────────────────────────────────
TEAL    = RGBColor(0x0F, 0x76, 0x6E)   # Primary accent
INK     = RGBColor(0x0F, 0x17, 0x2A)   # Near-black body text
AMBER   = RGBColor(0xD9, 0x77, 0x06)   # Warm highlight
MUTED   = RGBColor(0x64, 0x74, 0x8B)   # Secondary text
RULE    = RGBColor(0xCB, 0xD5, 0xE1)   # Thin rule lines
SOFT_BG = RGBColor(0xF8, 0xFA, 0xFC)   # Near-white rows
TEAL_10 = RGBColor(0xF0, 0xFD, 0xFA)   # 10% teal tint
AMB_10  = RGBColor(0xFF, 0xFB, 0xEB)   # 10% amber tint
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
DARK    = RGBColor(0x0F, 0x17, 0x2A)   # Cover background
LIGHT_T = RGBColor(0xCC, 0xFB, 0xF1)   # Teal 30% — on dark bg
SLATE   = RGBColor(0x94, 0xA3, 0xB8)   # Gray — on dark bg


# ══════════════════════════════════════════════════════════════════════════════
# LOW-LEVEL XML HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def hex3(rgb: RGBColor) -> str:
    return f'{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}'


def _set_cell_bg(cell, rgb: RGBColor):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex3(rgb))
    existing = tcPr.find(qn('w:shd'))
    if existing is not None:
        tcPr.remove(existing)
    tcPr.append(shd)


def _set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    """
    Set individual cell borders. Each side is (RGBColor, size_pt) or None.
    None = no border on that side.
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    config = {'top': top, 'bottom': bottom, 'left': left, 'right': right,
              'insideH': None, 'insideV': None}
    for side, val in config.items():
        b = OxmlElement(f'w:{side}')
        if val:
            color, size = val
            b.set(qn('w:val'), 'single')
            b.set(qn('w:sz'), str(int(size * 8)))   # sz in 1/8pt
            b.set(qn('w:color'), hex3(color))
        else:
            b.set(qn('w:val'), 'none')
            b.set(qn('w:sz'), '0')
            b.set(qn('w:color'), 'auto')
        tcBorders.append(b)
    existing = tcPr.find(qn('w:tcBorders'))
    if existing is not None:
        tcPr.remove(existing)
    tcPr.append(tcBorders)


def _border_all(cell, color=RULE, size=0.5):
    _set_cell_borders(cell, top=(color, size), bottom=(color, size),
                      left=(color, size), right=(color, size))


def _remove_borders(table):
    for row in table.rows:
        for cell in row.cells:
            _set_cell_borders(cell)


def _cell_margins(cell, top=60, bottom=60, left=120, right=120):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for side, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        m = OxmlElement(f'w:{side}')
        m.set(qn('w:w'), str(val))
        m.set(qn('w:type'), 'dxa')
        tcMar.append(m)
    ex = tcPr.find(qn('w:tcMar'))
    if ex is not None:
        tcPr.remove(ex)
    tcPr.append(tcMar)


def _cell_valign(cell, align='center'):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    v = OxmlElement('w:vAlign')
    v.set(qn('w:val'), align)
    ex = tcPr.find(qn('w:vAlign'))
    if ex is not None:
        tcPr.remove(ex)
    tcPr.append(v)


def _set_row_height(row, pts, rule='atLeast'):
    """Set minimum (or exact) row height in points."""
    tr = row._tr
    trPr = tr.get_or_add_trPr()
    trH = OxmlElement('w:trHeight')
    trH.set(qn('w:val'), str(int(pts * 20)))   # twips
    trH.set(qn('w:hRule'), rule)
    ex = trPr.find(qn('w:trHeight'))
    if ex is not None:
        trPr.remove(ex)
    trPr.insert(0, trH)


def _para_spacing(para, before=0, after=4):
    pPr = para._p.get_or_add_pPr()
    sp = OxmlElement('w:spacing')
    sp.set(qn('w:before'), str(int(before * 20)))
    sp.set(qn('w:after'), str(int(after * 20)))
    sp.set(qn('w:line'), '276')
    sp.set(qn('w:lineRule'), 'auto')
    ex = pPr.find(qn('w:spacing'))
    if ex is not None:
        pPr.remove(ex)
    pPr.append(sp)


def _para_indent(para, left=0, right=0, hanging=0):
    pPr = para._p.get_or_add_pPr()
    ind = OxmlElement('w:ind')
    if left:   ind.set(qn('w:left'),    str(int(left)))
    if right:  ind.set(qn('w:right'),   str(int(right)))
    if hanging: ind.set(qn('w:hanging'), str(int(hanging)))
    ex = pPr.find(qn('w:ind'))
    if ex is not None:
        pPr.remove(ex)
    pPr.append(ind)


def _para_shading(para, rgb: RGBColor):
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex3(rgb))
    ex = pPr.find(qn('w:shd'))
    if ex is not None:
        pPr.remove(ex)
    pPr.append(shd)


def _para_bottom_rule(para, color=TEAL, size=1.0):
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    b = OxmlElement('w:bottom')
    b.set(qn('w:val'), 'single')
    b.set(qn('w:sz'), str(int(size * 8)))
    b.set(qn('w:space'), '1')
    b.set(qn('w:color'), hex3(color))
    pBdr.append(b)
    ex = pPr.find(qn('w:pBdr'))
    if ex is not None:
        pPr.remove(ex)
    pPr.append(pBdr)


def _font(run, name, size, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    rf = OxmlElement('w:rFonts')
    rf.set(qn('w:ascii'), name)
    rf.set(qn('w:hAnsi'), name)
    rf.set(qn('w:eastAsia'), name)
    ex = rPr.find(qn('w:rFonts'))
    if ex is not None:
        rPr.remove(ex)
    rPr.insert(0, rf)


def _page_number(paragraph):
    run = paragraph.add_run()
    for tag in ['begin', 'instrText', 'separate', 'end']:
        if tag == 'instrText':
            el = OxmlElement('w:instrText')
            el.text = 'PAGE'
        else:
            el = OxmlElement('w:fldChar')
            el.set(qn('w:fldCharType'), tag)
        run._r.append(el)
    _font(run, 'Inter', 7.5, bold=True, color=TEAL)


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT FACTORY
# ══════════════════════════════════════════════════════════════════════════════

def new_doc():
    doc = Document()
    for section in doc.sections:
        section.top_margin    = Cm(2.2)
        section.bottom_margin = Cm(2.2)
        section.left_margin   = Cm(2.4)
        section.right_margin  = Cm(2.4)
    doc.styles['Normal'].font.name = 'Calibri'
    doc.styles['Normal'].font.size = Pt(9.5)
    return doc


def add_header_footer(doc, doc_title=''):
    """
    NovaOps consulting header: teal top rule, brand name left, doc title right.
    Footer: thin rule, confidential notice, page number.
    """
    section = doc.sections[0]
    section.different_first_page_header_footer = True

    # ── HEADER ────────────────────────────────────────────────────────────────
    header = section.header
    header.is_linked_to_previous = False
    for p in header.paragraphs:
        p.clear()

    ht = header.add_table(1, 2, width=Inches(6.3))
    ht.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(ht)

    lc = ht.cell(0, 0)
    _cell_margins(lc, 55, 55, 0, 60)
    lp = lc.paragraphs[0]
    lr1 = lp.add_run('NOVAOPS')
    _font(lr1, 'Poppins', 7, bold=True, color=TEAL)
    lr2 = lp.add_run('  ·  Bookkeeper Practice Launch System  ·  v2.0')
    _font(lr2, 'Inter', 6.5, color=MUTED)
    lp.alignment = WD_ALIGN_PARAGRAPH.LEFT

    rc = ht.cell(0, 1)
    _cell_margins(rc, 55, 55, 60, 0)
    rp = rc.paragraphs[0]
    rr = rp.add_run(doc_title.upper())
    _font(rr, 'Inter', 7, bold=True, color=INK)
    rp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    for cell in [lc, rc]:
        _set_cell_borders(cell, bottom=(TEAL, 1.0))

    # ── FOOTER ────────────────────────────────────────────────────────────────
    footer = section.footer
    footer.is_linked_to_previous = False
    for p in footer.paragraphs:
        p.clear()

    ft = footer.add_table(1, 2, width=Inches(6.3))
    ft.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(ft)

    lfc = ft.cell(0, 0)
    rfc = ft.cell(0, 1)
    for c in [lfc, rfc]:
        _set_cell_borders(c, top=(RULE, 0.5))
        _cell_margins(c, 55, 55, 0, 0)

    lfp = lfc.paragraphs[0]
    lfr = lfp.add_run('© 2025 NovaOps  ·  Commercial Use License  ·  Bookkeeper Practice Launch System')
    _font(lfr, 'Inter', 6.5, color=MUTED)
    lfp.alignment = WD_ALIGN_PARAGRAPH.LEFT

    rfp = rfc.paragraphs[0]
    rfr = rfp.add_run('Page ')
    _font(rfr, 'Inter', 7.5, color=MUTED)
    _page_number(rfp)
    rfp.alignment = WD_ALIGN_PARAGRAPH.RIGHT


# ══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════

def add_cover(doc, title_lines, subtitle, section_code='', meta_pairs=None):
    """
    Premium NovaOps cover — three-strip design:
      Top strip  : teal   — NovaOps wordmark + product version
      Body       : dark navy — title, subtitle, rule, metadata
      Bottom strip: amber  — version badge
    """
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)
    cell = t.cell(0, 0)
    _set_cell_bg(cell, DARK)
    _cell_margins(cell, top=0, bottom=0, left=0, right=0)
    _cell_valign(cell, 'top')

    # ── TOP STRIP: NovaOps brand bar ─────────────────────────────────────────
    p_top = cell.paragraphs[0]
    _para_shading(p_top, TEAL)
    _para_spacing(p_top, 8, 8)
    _para_indent(p_top, left=400)
    r1 = p_top.add_run('NOVAOPS')
    _font(r1, 'Poppins', 9, bold=True, color=WHITE)
    r2 = p_top.add_run('  ·  Bookkeeper Practice Launch System  ·  v2.0')
    _font(r2, 'Inter', 7.5, color=LIGHT_T)

    # ── BODY spacer ──────────────────────────────────────────────────────────
    p_sp1 = cell.add_paragraph()
    _para_spacing(p_sp1, 60, 0)

    # ── Section code badge ───────────────────────────────────────────────────
    if section_code:
        p_code = cell.add_paragraph()
        r_code = p_code.add_run(section_code.upper())
        _font(r_code, 'Inter', 7.5, bold=True, color=TEAL)
        _para_spacing(p_code, 0, 14)
        _para_indent(p_code, left=400)

    # ── NOVAOPS wordmark ─────────────────────────────────────────────────────
    p_wm = cell.add_paragraph()
    r_wm = p_wm.add_run('NOVAOPS')
    _font(r_wm, 'Poppins', 11, bold=True, color=TEAL)
    _para_spacing(p_wm, 0, 50)
    _para_indent(p_wm, left=400)

    # ── Title lines ──────────────────────────────────────────────────────────
    for line in title_lines:
        p_t = cell.add_paragraph()
        r_t = p_t.add_run(line)
        _font(r_t, 'Poppins', 32, bold=True, color=WHITE)
        _para_spacing(p_t, 0, 4)
        _para_indent(p_t, left=400)

    # ── Subtitle ─────────────────────────────────────────────────────────────
    p_sub = cell.add_paragraph()
    r_sub = p_sub.add_run(subtitle)
    _font(r_sub, 'Inter', 12, italic=True, color=SLATE)
    _para_spacing(p_sub, 8, 28)
    _para_indent(p_sub, left=400)

    # ── Teal separator rule ───────────────────────────────────────────────────
    p_rule = cell.add_paragraph()
    _para_bottom_rule(p_rule, TEAL, 1.5)
    _para_spacing(p_rule, 0, 20)
    _para_indent(p_rule, left=400, right=400)

    # ── Metadata pairs ────────────────────────────────────────────────────────
    if meta_pairs:
        for label, value in meta_pairs:
            p_m = cell.add_paragraph()
            r_l = p_m.add_run(f'{label.upper():<14}')
            _font(r_l, 'Inter', 7.5, color=MUTED)
            r_v = p_m.add_run(value)
            _font(r_v, 'Inter', 7.5, bold=True, color=WHITE)
            _para_spacing(p_m, 0, 4)
            _para_indent(p_m, left=400)

    # ── Body bottom spacer ────────────────────────────────────────────────────
    p_sp2 = cell.add_paragraph()
    _para_spacing(p_sp2, 40, 0)

    # ── BOTTOM STRIP: version/edition badge ──────────────────────────────────
    p_bot = cell.add_paragraph()
    _para_shading(p_bot, AMBER)
    _para_spacing(p_bot, 8, 8)
    _para_indent(p_bot, left=400)
    r_v = p_bot.add_run('VERSION 2.0  ·  PREMIUM CONSULTING EDITION  ·  © 2025 NOVAOPS')
    _font(r_v, 'Poppins', 7.5, bold=True, color=WHITE)

    doc.add_page_break()


# ══════════════════════════════════════════════════════════════════════════════
# SECTION HEADERS & TYPOGRAPHY
# ══════════════════════════════════════════════════════════════════════════════

def section_header(doc, number, title):
    """
    Full-width two-tone section header — teal number block + dark navy title.
    Much more visually impactful than a plain inline label.
    """
    # Spacer before
    p_pre = doc.add_paragraph()
    _para_spacing(p_pre, 10, 0)

    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)

    # Number cell (teal background)
    nc = t.cell(0, 0)
    nc.width = Cm(1.6)
    _set_cell_bg(nc, TEAL)
    _cell_margins(nc, 100, 100, 140, 100)
    _cell_valign(nc, 'center')
    _set_row_height(t.rows[0], 24)
    np_ = nc.paragraphs[0]
    nr = np_.add_run(f'{number:02d}')
    _font(nr, 'Poppins', 13, bold=True, color=WHITE)
    np_.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Title cell (dark navy background)
    tc = t.cell(0, 1)
    _set_cell_bg(tc, DARK)
    _cell_margins(tc, 100, 100, 180, 120)
    _cell_valign(tc, 'center')
    tp = tc.paragraphs[0]
    r_dash = tp.add_run('— ')
    _font(r_dash, 'Poppins', 10.5, bold=True, color=TEAL)
    r_title = tp.add_run(title.upper())
    _font(r_title, 'Poppins', 10.5, bold=True, color=WHITE)

    # Spacer after
    p_post = doc.add_paragraph()
    _para_spacing(p_post, 0, 6)
    return t


def h1(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    _font(r, 'Poppins', 16, bold=True, color=INK)
    _para_spacing(p, 12, 4)
    return p


def h2(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    _font(r, 'Poppins', 11.5, bold=True, color=TEAL)
    _para_spacing(p, 10, 2)
    return p


def h3(doc, text, color=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    _font(r, 'Poppins', 10, bold=True, color=color or INK)
    _para_spacing(p, 8, 2)
    return p


def body(doc, text, size=9.5, color=None, italic=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    _font(r, 'Calibri', size, italic=italic, color=color or INK)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _para_spacing(p, 0, 4)
    return p


def icon_bullet(doc, text, icon='→', color=None):
    """Arrow/icon bullet — much cleaner than default list bullets."""
    p = doc.add_paragraph()
    r_icon = p.add_run(f'{icon}  ')
    _font(r_icon, 'Calibri', 9.5, bold=True, color=color or TEAL)
    r_text = p.add_run(text)
    _font(r_text, 'Calibri', 9.5, color=INK)
    _para_spacing(p, 0, 3)
    _para_indent(p, left=200, hanging=200)
    return p


def checklist_item(doc, text, done=False, sub=False):
    """Properly formatted checklist with ☐ / ✓ symbol and teal accent."""
    p = doc.add_paragraph()
    symbol = '✓' if done else '☐'
    r_sym = p.add_run(f'{symbol}  ')
    _font(r_sym, 'Calibri', 10, bold=True, color=TEAL if done else INK)
    r_text = p.add_run(text)
    _font(r_text, 'Calibri', 9.5, color=INK)
    _para_spacing(p, 0, 4)
    _para_indent(p, left=(360 if sub else 180), hanging=180)
    return p


# ══════════════════════════════════════════════════════════════════════════════
# CALLOUT BOXES
# ══════════════════════════════════════════════════════════════════════════════

def key_message_box(doc, text, label='KEY INSIGHT'):
    """Left-border callout — teal 10% tint, teal 2pt left accent."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)
    cell = t.cell(0, 0)
    _set_cell_bg(cell, TEAL_10)
    _cell_margins(cell, top=120, bottom=120, left=180, right=180)
    _set_cell_borders(cell,
                      top=(RULE, 0.5), bottom=(RULE, 0.5),
                      left=(TEAL, 2.5), right=(RULE, 0.5))

    p_l = cell.paragraphs[0]
    r_l = p_l.add_run(label)
    _font(r_l, 'Poppins', 7, bold=True, color=TEAL)
    _para_spacing(p_l, 0, 5)

    p_t = cell.add_paragraph()
    r_t = p_t.add_run(text)
    _font(r_t, 'Calibri', 9.5, bold=True, color=INK)
    _para_spacing(p_t, 0, 0)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 6)
    return t


def notice_box(doc, text, label='NOTICE', amber=False):
    """Left-border notice — amber or muted tint."""
    bg = AMB_10 if amber else RGBColor(0xF1, 0xF5, 0xF9)
    accent = AMBER if amber else MUTED
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)
    cell = t.cell(0, 0)
    _set_cell_bg(cell, bg)
    _cell_margins(cell, top=110, bottom=110, left=170, right=170)
    _set_cell_borders(cell,
                      top=(RULE, 0.5), bottom=(RULE, 0.5),
                      left=(accent, 2.0), right=(RULE, 0.5))

    p_l = cell.paragraphs[0]
    r_l = p_l.add_run(label)
    _font(r_l, 'Poppins', 7, bold=True, color=accent)
    _para_spacing(p_l, 0, 5)

    p_t = cell.add_paragraph()
    r_t = p_t.add_run(text)
    _font(r_t, 'Calibri', 9, color=INK)
    _para_spacing(p_t, 0, 0)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 6)
    return t


def script_box(doc, body_text):
    """Email/script body box — soft background, teal left border."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)
    cell = t.cell(0, 0)
    _set_cell_bg(cell, SOFT_BG)
    _cell_margins(cell, top=150, bottom=150, left=200, right=200)
    _set_cell_borders(cell,
                      top=(RULE, 0.5), bottom=(RULE, 0.5),
                      left=(TEAL, 1.5), right=(RULE, 0.5))

    first = True
    for line in body_text.split('\n'):
        if first:
            p = cell.paragraphs[0]
            first = False
        else:
            p = cell.add_paragraph()
        r = p.add_run(line)
        _font(r, 'Calibri', 8.5, color=INK)
        _para_spacing(p, 0, 2)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 6)
    return t


# ══════════════════════════════════════════════════════════════════════════════
# DATA COMPONENTS
# ══════════════════════════════════════════════════════════════════════════════

def consulting_table(doc, headers, rows, col_widths_cm=None):
    """Consulting-grade table — teal header, zebra rows, thin grid."""
    n = len(headers)
    t = doc.add_table(rows=1 + len(rows), cols=n)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = 'Table Grid'

    if col_widths_cm:
        for i, w in enumerate(col_widths_cm):
            for row in t.rows:
                if i < len(row.cells):
                    row.cells[i].width = Cm(w)

    # Header row
    _set_row_height(t.rows[0], 20)
    for j, h in enumerate(headers):
        cell = t.cell(0, j)
        _set_cell_bg(cell, TEAL)
        _cell_margins(cell, 70, 70, 100, 100)
        _set_cell_borders(cell,
                          top=(TEAL, 0.5), bottom=(TEAL, 1.0),
                          left=(TEAL, 0.5), right=(TEAL, 0.5))
        p = cell.paragraphs[0]
        r = p.add_run(h)
        _font(r, 'Poppins', 8, bold=True, color=WHITE)

    # Data rows
    for i, row_data in enumerate(rows):
        bg = WHITE if i % 2 == 0 else SOFT_BG
        for j, val in enumerate(row_data):
            cell = t.cell(i + 1, j)
            _set_cell_bg(cell, bg)
            _border_all(cell, RULE, 0.4)
            _cell_margins(cell, 60, 60, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(str(val))
            _font(r, 'Calibri', 8.5, color=INK)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 8)
    return t


def step_row(doc, number, title, description):
    """Numbered process step — large teal number + title + description."""
    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)

    nc = t.cell(0, 0)
    nc.width = Cm(1.5)
    _set_cell_bg(nc, TEAL)
    _cell_margins(nc, 90, 90, 120, 100)
    _cell_valign(nc, 'center')
    _set_row_height(t.rows[0], 14)
    np_ = nc.paragraphs[0]
    nr = np_.add_run(number)
    _font(nr, 'Poppins', 15, bold=True, color=WHITE)
    np_.alignment = WD_ALIGN_PARAGRAPH.CENTER

    tc_cell = t.cell(0, 1)
    _cell_margins(tc_cell, 80, 80, 160, 80)
    _set_cell_borders(tc_cell, top=(RULE, 0.5))

    tp = tc_cell.paragraphs[0]
    tr = tp.add_run(title)
    _font(tr, 'Poppins', 10.5, bold=True, color=INK)
    _para_spacing(tp, 0, 3)

    dp = tc_cell.add_paragraph()
    dr = dp.add_run(description)
    _font(dr, 'Calibri', 9, color=MUTED)
    _para_spacing(dp, 0, 6)
    _cell_valign(tc_cell, 'top')

    return t


# ══════════════════════════════════════════════════════════════════════════════
# NEW PREMIUM COMPONENTS
# ══════════════════════════════════════════════════════════════════════════════

def at_a_glance_box(doc, stats):
    """
    Horizontal stat cards — document overview at a glance.
    stats = [(label, value, note), ...]   (max 4)
    """
    n = min(len(stats), 4)
    t = doc.add_table(rows=3, cols=n)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)

    for i, (label, value, note) in enumerate(stats[:n]):
        # Label row (teal)
        lc = t.cell(0, i)
        _set_cell_bg(lc, TEAL)
        _cell_margins(lc, 80, 60, 120, 120)
        _set_row_height(t.rows[0], 13)
        lp = lc.paragraphs[0]
        lr = lp.add_run(label.upper())
        _font(lr, 'Inter', 6.5, bold=True, color=LIGHT_T)
        lp.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Value row (dark navy)
        vc = t.cell(1, i)
        _set_cell_bg(vc, DARK)
        _cell_margins(vc, 60, 60, 120, 120)
        _set_row_height(t.rows[1], 32)
        vp = vc.paragraphs[0]
        vr = vp.add_run(str(value))
        _font(vr, 'Poppins', 22, bold=True, color=WHITE)
        vp.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Note row (soft bg)
        nc = t.cell(2, i)
        _set_cell_bg(nc, SOFT_BG)
        _cell_margins(nc, 55, 70, 120, 120)
        _set_row_height(t.rows[2], 13)
        np_ = nc.paragraphs[0]
        nr = np_.add_run(note)
        _font(nr, 'Calibri', 7.5, italic=True, color=MUTED)
        np_.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 10)
    return t


def process_flow(doc, steps, compact=False):
    """
    Horizontal numbered process flow — [01] → [02] → [03] ...
    steps = [(title, note), ...]   max 5 for horizontal, else use step_row
    """
    n = len(steps)
    cols = n * 2 - 1   # steps + arrows between them
    t = doc.add_table(rows=2, cols=cols)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)

    for i, (title, note) in enumerate(steps):
        col = i * 2

        # Number box (teal)
        nb = t.cell(0, col)
        _set_cell_bg(nb, TEAL)
        _cell_margins(nb, 80, 55, 100, 100)
        _set_row_height(t.rows[0], 24 if not compact else 18)
        np_ = nb.paragraphs[0]
        nr = np_.add_run(f'{i + 1:02d}')
        _font(nr, 'Poppins', 14 if not compact else 11, bold=True, color=WHITE)
        np_.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Title box (soft bg with top teal rule)
        tb = t.cell(1, col)
        _set_cell_bg(tb, SOFT_BG)
        _set_cell_borders(tb, top=(TEAL, 1.0))
        _cell_margins(tb, 80, 80, 80, 80)
        _set_row_height(t.rows[1], 28)
        tp = tb.paragraphs[0]
        tr = tp.add_run(title)
        _font(tr, 'Poppins', 8, bold=True, color=INK)
        tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if note:
            np2 = tb.add_paragraph()
            nr2 = np2.add_run(note)
            _font(nr2, 'Calibri', 7.5, italic=True, color=MUTED)
            np2.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Arrow (except after last step)
        if i < n - 1:
            ac = t.cell(0, col + 1)
            _cell_margins(ac, 80, 55, 30, 30)
            ap = ac.paragraphs[0]
            ar = ap.add_run('→')
            _font(ar, 'Poppins', 14, bold=True, color=TEAL)
            ap.alignment = WD_ALIGN_PARAGRAPH.CENTER

            ab = t.cell(1, col + 1)
            _cell_margins(ab, 80, 80, 30, 30)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 10)
    return t


def two_panel_box(doc, left_title, left_items, right_title, right_items,
                  left_bg=TEAL_10, right_bg=SOFT_BG):
    """
    Side-by-side comparison panel.
    items = [(icon, text), ...]
    """
    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)

    for i, (panel_bg, title, items) in enumerate([
        (left_bg, left_title, left_items),
        (right_bg, right_title, right_items),
    ]):
        cell = t.cell(0, i)
        _set_cell_bg(cell, panel_bg)
        _cell_margins(cell, 140, 140, 180, 180)
        accent = TEAL if i == 0 else MUTED
        _set_cell_borders(cell, left=(accent, 2.0))

        tp = cell.paragraphs[0]
        tr = tp.add_run(title.upper())
        _font(tr, 'Poppins', 8.5, bold=True, color=accent)
        _para_spacing(tp, 0, 8)

        for (icon, text) in items:
            p = cell.add_paragraph()
            r_i = p.add_run(f'{icon}  ')
            _font(r_i, 'Calibri', 9.5, bold=True, color=accent)
            r_t = p.add_run(text)
            _font(r_t, 'Calibri', 9, color=INK)
            _para_spacing(p, 0, 3)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 10)
    return t


def phase_banner(doc, number, title, description=''):
    """Full-width phase/section banner — dark navy fill."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)
    cell = t.cell(0, 0)
    _set_cell_bg(cell, DARK)
    _cell_margins(cell, 110, 110, 200, 200)
    _set_row_height(t.rows[0], 20)

    p = cell.paragraphs[0]
    r_ph = p.add_run(f'PHASE {number}  ')
    _font(r_ph, 'Poppins', 8, bold=True, color=TEAL)
    r_title = p.add_run('—  ' + title.upper())
    _font(r_title, 'Poppins', 9.5, bold=True, color=WHITE)
    if description:
        r_desc = p.add_run(f'   ·   {description}')
        _font(r_desc, 'Calibri', 8.5, italic=True, color=SLATE)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 6)
    return t


def save(doc, path):
    doc.save(path)
    print(f'  ✓ {os.path.basename(path)}')


# ══════════════════════════════════════════════════════════════════════════════
# 1. START HERE
# ══════════════════════════════════════════════════════════════════════════════

def build_start_here():
    doc = new_doc()
    add_cover(doc,
              ['Start Here'],
              'Your complete 90-minute guide to launching your bookkeeping practice system',
              '00  —  START HERE',
              [('Version', '2.0  —  Premium Consulting Edition'),
               ('Audience', 'Product Owner / Practice Manager'),
               ('Setup time', 'Approximately 90 minutes')])
    add_header_footer(doc, 'Start Here')

    key_message_box(doc,
        'Read this file before opening anything else. It tells you what you received, '
        'how to set it up in 90 minutes, and exactly how every file connects to the next.',
        'START HERE — READ FIRST')

    at_a_glance_box(doc, [
        ('Folders',     '5',   'organised sections'),
        ('Files',       '26',  'premium assets'),
        ('Setup Time',  '90m', 'to full operation'),
        ('Licence',     '1yr', 'commercial use'),
    ])

    section_header(doc, 1, 'What Is Included')
    consulting_table(doc,
        ['Folder', 'Contains', 'Purpose'],
        [
            ['00 — START HERE',        'Read Me, Install Guide, Asset Manifest',      'Orientation and setup walkthrough'],
            ['01 — QUICK REFERENCE',   'Licence, FAQ, Version History, Support Guide', 'Legal, support, and product reference'],
            ['02 — PRACTICE DASHBOARD','Excel dashboard (10 sheets)',                  'Your daily operations hub'],
            ['03 — CLIENT DOCUMENTS',  'Service Guide, Proposal, Agreement, Intake, Deck', 'Send-ready client-facing files'],
            ['04 — OPERATIONS LIBRARY','SOPs, Checklists, Communication Scripts',     'Internal practice procedures'],
            ['05 — NOTION WORKSPACE',  '7 CSV databases + Notion Setup Guide',         'Importable workspace for Notion'],
        ],
        col_widths_cm=[4.5, 6, 7]
    )

    section_header(doc, 2, '90-Minute Setup Sequence')
    body(doc, 'Follow these six steps in order. Do not customise files before reading the guides — '
         'the sequence is designed to prevent rework.')
    doc.add_paragraph()

    process_flow(doc, [
        ('Read Guides', '10 min'),
        ('Customise Dashboard', '20 min'),
        ('Update Client Docs', '25 min'),
        ('Build Notion', '15 min'),
        ('Validate', '15 min'),
        ('Review Licence', '5 min'),
    ])

    steps = [
        ('01', 'Read the guides (10 min)',
         'Read this file, then the Installation-Guide in 00-START-HERE. Understand the full system before customising anything.'),
        ('02', 'Customise the Dashboard (20 min)',
         'Open 02-Practice-Dashboard/Bookkeeper-Practice-Dashboard-v2.xlsx. Fill all amber Setup cells with your practice name, services, and pricing.'),
        ('03', 'Update client documents (25 min)',
         'Replace all [BRACKETED TEXT] in the 5 files in 03-Client-Documents. Use Find & Replace (Ctrl+H or Cmd+H) in Word.'),
        ('04', 'Build your Notion workspace (15 min)',
         'Follow Notion-Setup-Guide.pdf in 05-Notion-Workspace. Import all 7 CSV files and connect them with Relations.'),
        ('05', 'Validate and review (15 min)',
         'Add 2–3 sample clients. Confirm KPI cards populate on the Dashboard. Search every DOCX for remaining brackets.'),
        ('06', 'Read the Licence (5 min)',
         'Review 01-Quick-Reference/License.pdf before sending any document to a client.'),
    ]
    for num, title, desc in steps:
        step_row(doc, num, title, desc)

    section_header(doc, 3, 'Core Client Workflow')
    body(doc, 'Every client engagement follows this sequence. The system provides a file or tool for every stage.')
    doc.add_paragraph()
    consulting_table(doc,
        ['Stage', 'What Happens', 'System File'],
        [
            ['01  Lead',       'Qualify entity type, volume, software, complexity, and urgency', 'Dashboard — Lead Pipeline'],
            ['02  Diagnostic', 'Review books, backlog, accounts, and reporting needs',            'Client-Intake-and-Onboarding-Pack-v2'],
            ['03  Proposal',   'Define scope, assumptions, cleanup, and monthly fee',             'Bookkeeping-Proposal-Template-v2'],
            ['04  Engagement', 'Sign contract, collect payment, confirm responsibilities',        'Bookkeeping-Engagement-Agreement-v2'],
            ['05  Onboarding', 'Collect access, COA, documents, deadlines',                      'Client-Intake-and-Onboarding-Pack-v2'],
            ['06  Monthly Close','Reconcile, review, adjust, report, document exceptions',       'Dashboard + SOPs-and-Checklists-v2'],
            ['07  Delivery',   'Deliver reports, explain variances, confirm next actions',        'Client Portal (Notion) + Scripts'],
        ],
        col_widths_cm=[3, 8, 6.5]
    )

    notice_box(doc,
        'This product supports bookkeeping operations only. It does not constitute accounting, '
        'tax, legal, audit, assurance, payroll, or regulatory advice. Adapt all files to your '
        'credentials, jurisdiction, and permitted professional scope before client use.',
        label='PROFESSIONAL SCOPE — READ BEFORE CLIENT USE', amber=True)

    save(doc, f'{OUT}/00-START-HERE/Start-Here-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 2. BOOKKEEPING SERVICE GUIDE
# ══════════════════════════════════════════════════════════════════════════════

def build_service_guide():
    doc = new_doc()
    add_cover(doc,
              ['Bookkeeping', 'Service Guide'],
              'A clear overview of what we do, how we work, and what to expect every month',
              '03  —  CLIENT DOCUMENTS',
              [('Prepared by', '[PRACTICE NAME]'),
               ('Document type', 'Client-Facing Overview'),
               ('Last updated', '2025')])
    add_header_footer(doc, 'Bookkeeping Service Guide')

    notice_box(doc,
        'Replace all [BRACKETED TEXT] with your practice details before sending to any client.',
        label='CUSTOMISATION REQUIRED', amber=True)

    at_a_glance_box(doc, [
        ('Service Packages', '3',        'Essentials · Growth · Advanced'),
        ('Deliverables',    'Monthly',   'P&L, Balance Sheet & more'),
        ('Close Deadline',  'Day [X]',   'of the following month'),
        ('Response SLA',    '[X] days',  'for transaction questions'),
    ])

    section_header(doc, 1, 'What Monthly Bookkeeping Includes')
    body(doc, 'Every monthly engagement with [PRACTICE NAME] includes the following as standard:')
    doc.add_paragraph()
    for item in [
        'Transaction categorisation and ledger review',
        'Bank and credit-card reconciliations for all agreed accounts',
        'Balance-sheet account review and exception documentation',
        'Monthly financial statements — Profit & Loss and Balance Sheet',
        'Consolidated exception log and missing-document requests',
        'Agreed monthly communication cadence and close schedule',
        'Secure report delivery via client portal — never by ordinary email',
    ]:
        icon_bullet(doc, item)

    section_header(doc, 2, 'Service Packages')
    consulting_table(doc,
        ['Package', 'Typical Scope', 'Deliverables', 'Starting Price'],
        [
            ['Essentials', 'Up to [X] accounts, [X] transactions/month',
             'Monthly P&L, Balance Sheet, reconciliations', '€[ ] / month'],
            ['Growth', 'Higher volume, class or location tracking',
             'All Essentials + monthly review call, cash summary', '€[ ] / month'],
            ['Advanced', 'Multi-entity or complex workflows',
             'All Growth + custom reporting, priority support', '€[ ] / month'],
            ['Tax Ready Add-On', 'Year-end package preparation',
             'Tax document checklist + preparer coordination', '€[ ] / year'],
        ],
        col_widths_cm=[3, 5.5, 6.5, 2.5]
    )

    section_header(doc, 3, 'Optional Project Services')
    consulting_table(doc,
        ['Service', 'Description', 'Pricing'],
        [
            ['Catch-up / Cleanup', 'Bring overdue or disorganised books current', 'Quote after diagnostic'],
            ['Historical Reconciliations', 'Reconcile prior months or years', 'Quote after diagnostic'],
            ['Chart-of-Accounts Redesign', 'Rebuild account structure for clarity and reporting', 'Fixed fee: €[ ]'],
            ['Software Migration & Setup', 'Move from one platform to another', 'Quote per project'],
            ['Accounts Payable/Receivable', 'Invoice management and payment tracking support', '€[ ]/month add-on'],
        ],
        col_widths_cm=[4.5, 7.5, 5.5]
    )

    section_header(doc, 4, 'Monthly Close Timeline')
    body(doc, 'Every month follows a structured, predictable process. You will always know where things stand.')
    doc.add_paragraph()

    process_flow(doc, [
        ('Records Ready', 'Days 1–5'),
        ('Bookkeeping', 'Days 5–12'),
        ('Q&A Round', 'Days 12–18'),
        ('Reports Delivered', 'By Day [X]'),
    ])

    consulting_table(doc,
        ['Days', 'Activity', 'Responsible'],
        [
            ['Days 1–5',       'Client provides bank statements, payroll reports, loan records, and missing documents', 'Client'],
            ['Days 5–12',      'Bookkeeper imports transactions, categorises, reconciles, and raises questions',        'Bookkeeper'],
            ['Days 12–18',     'Client answers questions; bookkeeper posts adjustments and finalises',                  'Both'],
            ['By Day [X]',     'Reports and action summary delivered through the secure portal',                        'Bookkeeper'],
        ],
        col_widths_cm=[3, 11, 3.5]
    )

    section_header(doc, 5, 'Service Boundaries')
    notice_box(doc,
        'The following are outside the scope of bookkeeping unless separately contracted and '
        'legally permitted: tax advice and return preparation, audit and assurance services, '
        'payroll processing, legal advice, regulatory compliance, CFO services.',
        label='WHAT IS NOT INCLUDED', amber=True)

    section_header(doc, 6, 'Client Responsibilities')
    two_panel_box(doc,
        'What We Do For You',
        [
            ('✓', 'Clean, accurate books delivered on schedule'),
            ('✓', 'One consolidated question list — no ad-hoc interruptions'),
            ('✓', 'Secure report delivery to your portal'),
            ('✓', 'Proactive exception and variance flagging'),
            ('✓', 'Single point of contact who knows your business'),
        ],
        'What We Need From You',
        [
            ('→', 'Source documents by the agreed monthly deadline'),
            ('→', 'Role-based software access (no email passwords)'),
            ('→', 'Answers to questions within [X] business days'),
            ('→', 'Review and acknowledgement of monthly reports'),
            ('→', 'Engagement of a qualified tax professional for tax matters'),
        ]
    )

    notice_box(doc,
        'We use secure client portals, read-only accountant access, and approved password managers. '
        'We will never ask you to share banking credentials by ordinary email. '
        'All document exchange happens through your secure portal at [PORTAL LINK].',
        label='SECURITY & DATA PROTECTION')

    save(doc, f'{OUT}/03-Client-Documents/Bookkeeping-Service-Guide-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 3. CLIENT INTAKE & ONBOARDING PACK
# ══════════════════════════════════════════════════════════════════════════════

def build_intake_pack():
    doc = new_doc()
    add_cover(doc,
              ['Client Intake &', 'Onboarding Pack'],
              'Everything needed to start a clean, confident bookkeeping engagement',
              '03  —  CLIENT DOCUMENTS',
              [('Prepared by', '[PRACTICE NAME]'),
               ('Client', '[CLIENT COMPANY]'),
               ('Kickoff date', '[DATE]')])
    add_header_footer(doc, 'Client Intake & Onboarding Pack')

    notice_box(doc,
        'Complete Sections 1–5 with the client during or before the kickoff call. '
        'Replace all [BRACKETED TEXT] before sending.',
        label='INSTRUCTIONS', amber=True)

    at_a_glance_box(doc, [
        ('Sections',    '5',    'intake to access'),
        ('Form Fields', '22+',  'business + volume'),
        ('Documents',   '9+',   'to collect upfront'),
        ('Access Items','6',    'to grant before close'),
    ])

    section_header(doc, 1, 'Business Profile')
    consulting_table(doc,
        ['Field', 'Client Response'],
        [
            ['Legal Business Name', ''],
            ['Trading Name (if different)', ''],
            ['Entity Type & Jurisdiction', ''],
            ['Business Address', ''],
            ['Primary Contact & Approver', ''],
            ['Fiscal Year End', ''],
            ['Industry & Business Model', ''],
            ['Number of Entities / Locations', ''],
            ['Current Accounting Basis (Cash / Accrual)', ''],
            ['Current Bookkeeping Software & Subscription', ''],
        ],
        col_widths_cm=[7.5, 10]
    )

    section_header(doc, 2, 'Volume & Complexity Assessment')
    consulting_table(doc,
        ['Assessment Question', 'Response'],
        [
            ['Average monthly bank and card transactions', ''],
            ['Number of bank accounts', ''],
            ['Number of credit cards', ''],
            ['Payroll provider and employee count', ''],
            ['Loans / lines of credit outstanding', ''],
            ['Inventory (Yes/No + brief description)', ''],
            ['Sales channels and payment processors', ''],
            ['Foreign currency or cross-border activity', ''],
            ['Class, project, or location tracking required', ''],
            ['Last fully reconciled month', ''],
            ['Known backlogs, issues, or prior-year adjustments', ''],
        ],
        col_widths_cm=[8.5, 9]
    )

    section_header(doc, 3, 'Documents Required Before Kickoff')
    body(doc, 'Please upload the following to your secure portal at [PORTAL LINK] before the kickoff call:')
    doc.add_paragraph()
    for item in [
        'Prior-year financial statements and trial balance',
        'Bank and credit-card statements from the agreed engagement start date',
        'Loan statements and amortisation schedules',
        'Payroll summaries and payroll tax liability reports',
        'Sales-tax / VAT filings and any outstanding notices',
        'Merchant processor and e-commerce platform reports',
        'Fixed-asset list with purchase dates and costs',
        'Outstanding accounts receivable and payable ageing reports',
        'Tax return or tax-preparer adjusting entries (where appropriate)',
    ]:
        checklist_item(doc, item)

    notice_box(doc,
        'Never share banking passwords by email. Use secure portals, read-only accountant access, '
        'or an approved password manager. We will never request passwords by ordinary email.',
        label='SECURITY NOTICE', amber=True)

    section_header(doc, 4, 'Kickoff Decisions')
    consulting_table(doc,
        ['Decision', 'Agreed Approach'],
        [
            ['Monthly close deadline', ''],
            ['Document cutoff day (when statements are available)', ''],
            ['Primary question and approval contact', ''],
            ['Preferred communication channel', ''],
            ['Report package (P&L, Balance Sheet, Cash, Custom)', ''],
            ['Escalation process for urgent items', ''],
            ['First close period', ''],
            ['Cleanup scope and start date (if applicable)', ''],
        ],
        col_widths_cm=[7.5, 10]
    )

    section_header(doc, 5, 'Access & Integration Checklist')
    consulting_table(doc,
        ['Access Item', 'Status', 'Notes'],
        [
            ['Bookkeeping software — accountant/adviser role', '☐  Granted', ''],
            ['Bank feed connection or read-only bank access', '☐  Granted', ''],
            ['Payroll platform — read-only access', '☐  Granted', ''],
            ['Payment processor / e-commerce reports', '☐  Granted', ''],
            ['Client portal invitation accepted', '☐  Accepted', ''],
            ['Document upload folder shared and accessible', '☐  Confirmed', ''],
        ],
        col_widths_cm=[8, 3.5, 6]
    )

    save(doc, f'{OUT}/03-Client-Documents/Client-Intake-and-Onboarding-Pack-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 4. PROPOSAL TEMPLATE
# ══════════════════════════════════════════════════════════════════════════════

def build_proposal():
    doc = new_doc()
    add_cover(doc,
              ['Bookkeeping Services', 'Proposal'],
              'Prepared exclusively for [CLIENT COMPANY] by [PRACTICE NAME]',
              '03  —  CLIENT DOCUMENTS',
              [('Prepared for', '[CLIENT COMPANY]'),
               ('Prepared by', '[PRACTICE NAME]'),
               ('Proposal date', '[DATE]'),
               ('Valid until', '[DATE + 14 DAYS]')])
    add_header_footer(doc, 'Bookkeeping Services Proposal')

    notice_box(doc,
        'Complete all [BRACKETED] fields for this specific client. '
        'Replace sample figures with real diagnostic findings before sending.',
        label='CUSTOMISATION REQUIRED', amber=True)

    at_a_glance_box(doc, [
        ('Sections',     '7',         'proposal to signature'),
        ('Pricing',      'Fixed',     'transparent, no surprises'),
        ('Valid',        '14 days',   'from proposal date'),
        ('Start',        '[DATE]',    'proposed engagement start'),
    ])

    section_header(doc, 1, 'Proposal Details')
    consulting_table(doc,
        ['Detail', 'Information'],
        [
            ['Prepared For', '[CLIENT COMPANY]'],
            ['Contact Name & Title', '[NAME / TITLE]'],
            ['Prepared By', '[PRACTICE NAME]'],
            ['Proposal Date', '[DATE]'],
            ['Valid Until', '[DATE + 14 DAYS]'],
            ['Proposed Engagement Start', '[DATE]'],
        ],
        col_widths_cm=[5.5, 12]
    )

    section_header(doc, 2, 'Current Situation')
    key_message_box(doc,
        '[Summarise the client\'s current books, backlog, software, reporting gaps, and desired '
        'outcome. Reference findings from your diagnostic. This demonstrates you understand their '
        'situation before presenting a solution.]',
        'DIAGNOSTIC FINDINGS — REPLACE WITH REAL FINDINGS')

    section_header(doc, 3, 'Recommended Scope')
    consulting_table(doc,
        ['Service', 'Cadence', 'What Is Included'],
        [
            ['Bookkeeping',        'Monthly',    'Categorisation, reconciliation, review, and approved adjusting entries'],
            ['Financial Reporting','Monthly',    'Profit & Loss, Balance Sheet, and [additional agreed reports]'],
            ['Client Questions',   'Monthly',    'Consolidated exception list and documented follow-up'],
            ['Review Meeting',     '[Cadence]',  '[Duration] review call with [participants]'],
            ['Cleanup Project',    'One-time',   '[Months / accounts / issues included in cleanup scope]'],
        ],
        col_widths_cm=[3.5, 3, 11]
    )

    section_header(doc, 4, 'Implementation Plan')
    process_flow(doc, [
        ('Sign & Pay', 'Day 1'),
        ('Access & Docs', 'Days 1–5'),
        ('Diagnostic', 'Week 1'),
        ('Cleanup', 'Weeks 2–[X]'),
        ('First Close', '[Month]'),
        ('Deliver', 'After close'),
    ])
    consulting_table(doc,
        ['Phase', 'Activity', 'Timeline'],
        [
            ['1', 'Engagement signed and initial payment received', 'Day 1'],
            ['2', 'Secure access granted and documents uploaded to portal', 'Days 1–5'],
            ['3', 'Diagnostic review and opening-balance confirmation', 'Week 1'],
            ['4', 'Cleanup or conversion work (if applicable)', 'Weeks 2–[X]'],
            ['5', 'First monthly close completed', '[Month / Year]'],
            ['6', 'Report delivery and process refinement call', 'After first close'],
        ],
        col_widths_cm=[1.5, 11.5, 4.5]
    )

    section_header(doc, 5, 'Investment')
    consulting_table(doc,
        ['Item', 'Fee', 'Billing Schedule'],
        [
            ['Setup / Diagnostic Fee', '€[ ]', 'Due on acceptance'],
            ['Cleanup Project', '€[ ]', '[e.g., 50% on start, 50% on delivery]'],
            ['Monthly Bookkeeping', '€[ ] / month', 'Monthly in advance, first day of service month'],
            ['Additional Work', '€[ ] / hour', 'With written approval before commencement'],
        ],
        col_widths_cm=[6, 3, 8.5]
    )
    notice_box(doc,
        'Pricing assumes the transaction volume, account count, software, and book condition '
        'described above. Material changes may require a pricing review with [X] days notice.',
        label='PRICING ASSUMPTIONS')

    section_header(doc, 6, 'Assumptions & Exclusions')
    for item in [
        'Pricing assumes books are in the condition described following the diagnostic review',
        'Tax advice, returns, audit/assurance, legal advice, and CFO services are excluded unless separately contracted',
        'Client provides source documents and answers to questions by agreed monthly deadlines',
        'Material scope or volume changes require a written pricing amendment',
    ]:
        icon_bullet(doc, item)

    section_header(doc, 7, 'Acceptance')
    consulting_table(doc,
        ['Field', 'Response'],
        [
            ['Selected scope', ''],
            ['Engagement start date', ''],
            ['Client name and title', ''],
            ['Client signature and date', ''],
            ['Practice representative', '[PRACTICE NAME]'],
            ['Practice signature and date', ''],
        ],
        col_widths_cm=[5.5, 12]
    )
    notice_box(doc,
        'Questions before accepting? Contact [PRACTICE NAME] at [EMAIL] or [PHONE]. '
        'This proposal expires on [DATE + 14 DAYS].',
        label='QUESTIONS?')

    save(doc, f'{OUT}/03-Client-Documents/Bookkeeping-Proposal-Template-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 5. ENGAGEMENT AGREEMENT
# ══════════════════════════════════════════════════════════════════════════════

def build_engagement_agreement():
    doc = new_doc()
    add_cover(doc,
              ['Bookkeeping', 'Engagement Agreement'],
              'Between [PRACTICE LEGAL NAME] and [CLIENT LEGAL NAME]',
              '03  —  CLIENT DOCUMENTS',
              [('Practice', '[PRACTICE LEGAL NAME]'),
               ('Client', '[CLIENT LEGAL NAME]'),
               ('Agreement date', '[DATE]'),
               ('Governed by', '[JURISDICTION]')])
    add_header_footer(doc, 'Bookkeeping Engagement Agreement')

    notice_box(doc,
        'This is a general template — not legal advice. Engage a qualified lawyer in your '
        'jurisdiction to review it before sending to any client. Do not skip this step.',
        label='LEGAL REVIEW REQUIRED BEFORE USE', amber=True)

    at_a_glance_box(doc, [
        ('Clauses',      '15',   'comprehensive coverage'),
        ('Signatures',   '2',    'both parties required'),
        ('Jurisdiction', 'Custom','adapt to your location'),
        ('Schedules',    'Attach','scope of work included'),
    ])

    section_header(doc, 0, 'Agreement Details')
    consulting_table(doc,
        ['Party / Field', 'Details'],
        [
            ['Practice Legal Name', '[PRACTICE LEGAL NAME]'],
            ['Practice Address', '[PRACTICE ADDRESS]'],
            ['Client Legal Name', '[CLIENT LEGAL NAME]'],
            ['Client Address', '[CLIENT ADDRESS]'],
            ['Agreement Date', '[DATE]'],
            ['Governing Law', '[JURISDICTION]'],
        ],
        col_widths_cm=[5.5, 12]
    )

    clauses = [
        (1,  'Services',
         'The Practice will perform the bookkeeping services described in the attached Scope of Work. '
         'Services not expressly listed are excluded. The Scope of Work may be updated by written '
         'amendment signed by both parties.'),
        (2,  'Client Responsibilities',
         'Client remains responsible for all business decisions, internal controls, source records, '
         'transaction authorisation, legal compliance, and the completeness and accuracy of all '
         'information supplied. The Practice relies on information provided by Client and does not '
         'independently verify source documents.'),
        (3,  'No Assurance, Tax, or Legal Opinion',
         'Unless separately agreed and legally permitted, this engagement does not include audit, '
         'review, assurance, tax advice, tax-return preparation, legal advice, fraud detection, '
         'forensic accounting, or independent verification of source information.'),
        (4,  'Fees and Payment',
         'Fees are [AMOUNT/STRUCTURE] as described in the attached Scope of Work. Invoices are due '
         '[TERMS]. Work may be suspended for overdue balances after [X] days written notice. '
         'Client remains responsible for fees for completed work during any suspension.'),
        (5,  'Access and Security',
         'Both parties will maintain reasonable security controls and use role-based software access. '
         'Client will not transmit passwords through ordinary email. Each party will promptly notify '
         'the other of any suspected unauthorised access to systems or client data.'),
        (6,  'Deadlines and Delays',
         'Delivery dates depend on timely receipt of records, responses, and approvals from Client. '
         'Client delays may shift close and reporting dates by an equivalent period without penalty.'),
        (7,  'Corrections and Prior Periods',
         'The Practice may correct bookkeeping errors identified during the engagement. Material '
         'prior-period or cleanup work outside scope requires written approval and additional fees.'),
        (8,  'Confidentiality and Privacy',
         'Each party will protect the other\'s confidential information using at least reasonable care '
         'and will comply with applicable privacy obligations. Data-processing terms required by law '
         'may be attached as a schedule.'),
        (9,  'Third-Party Systems',
         'The Practice is not responsible for outages, data loss, policy changes, fees, or errors '
         'caused by banks, accounting software, payroll providers, payment processors, or other '
         'third parties used in delivering services.'),
        (10, 'Records and Retention',
         'Client owns and is responsible for retaining original source documents for the legally '
         'required period. The Practice may retain working files in accordance with its retention '
         'policy and applicable professional standards.'),
        (11, 'Termination',
         'Either party may terminate with [NUMBER] days written notice. Client will pay for all '
         'completed work, work in progress, and non-cancellable costs. The Practice will deliver '
         'a final report package on termination.'),
        (12, 'Limitation and Dispute Resolution',
         'Liability limits, governing law, venue, and dispute resolution must be customised for '
         'the applicable jurisdiction and reviewed by a qualified lawyer. [CUSTOMISE FOR YOUR JURISDICTION]'),
        (13, 'Entire Agreement',
         'This Agreement and all attached schedules constitute the entire agreement between the '
         'parties and supersede all prior discussions. Changes require a written amendment signed '
         'by authorised representatives of both parties.'),
    ]

    for num, title, text in clauses:
        section_header(doc, num, title)
        body(doc, text)
        doc.add_paragraph()

    section_header(doc, 14, 'Scope of Work')
    consulting_table(doc,
        ['Field', 'Details'],
        [
            ['Engagement Start Date', ''],
            ['Bookkeeping Software', ''],
            ['Accounts / Volume Assumption', ''],
            ['Recurring Services', ''],
            ['Excluded Services', ''],
            ['Monthly Fee', ''],
            ['Monthly Close Deadline', ''],
            ['Client Primary Contact', ''],
            ['Billing Terms', ''],
        ],
        col_widths_cm=[6, 11.5]
    )

    section_header(doc, 15, 'Signatures')
    consulting_table(doc,
        ['Party', 'Name & Title', 'Signature', 'Date'],
        [
            ['Client', '', '', ''],
            ['Practice', '[PRACTICE NAME]', '', ''],
        ],
        col_widths_cm=[2.5, 6, 5.5, 3.5]
    )

    save(doc, f'{OUT}/03-Client-Documents/Bookkeeping-Engagement-Agreement-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 6. SOPs & CHECKLISTS
# ══════════════════════════════════════════════════════════════════════════════

def build_sops():
    doc = new_doc()
    add_cover(doc,
              ['Bookkeeping SOPs &', 'Checklists'],
              'Internal operating manual — onboarding, monthly close, quality control, and documents',
              '04  —  OPERATIONS LIBRARY',
              [('Document type', 'Internal Procedures'),
               ('Audience', 'Bookkeeper / Practice Owner'),
               ('Last updated', '2025')])
    add_header_footer(doc, 'Bookkeeping SOPs & Checklists')

    notice_box(doc,
        'Internal use only — not for clients. Customise [BRACKETED TEXT] to match your tools, '
        'deadlines, and workflow.',
        label='INTERNAL DOCUMENT')

    at_a_glance_box(doc, [
        ('SOPs',         '4',    'end-to-end procedures'),
        ('Monthly Close','12',   'control checkpoints'),
        ('QC Checks',    '10',   'before delivery'),
        ('Tax Docs',     '7',    'collection categories'),
    ])

    section_header(doc, 1, 'SOP — Client Onboarding')
    body(doc, 'Complete these steps for every new client before the first monthly close. '
         'Sign off each step as you complete it.')
    doc.add_paragraph()

    process_flow(doc, [
        ('Confirm & Record', 'Day 1'),
        ('Set Up Systems', 'Day 2'),
        ('Request Access', 'Day 2'),
        ('Collect Docs', 'Day 2'),
        ('Kickoff Call', 'Week 1'),
        ('First Review', 'Week 1'),
    ], compact=True)

    consulting_table(doc,
        ['#', 'Action', 'Owner', 'Deadline'],
        [
            ['1',  'Confirm signed engagement agreement and initial payment received',          '[OWNER]', 'Before kickoff'],
            ['2',  'Create client folder in [SYSTEM] with standard subfolder structure',        '[OWNER]', 'Day 1'],
            ['3',  'Create client record in Notion with all profile data from intake pack',     '[OWNER]', 'Day 1'],
            ['4',  'Set up recurring tasks in [PROJECT TOOL] for monthly close cadence',        '[OWNER]', 'Day 2'],
            ['5',  'Request secure accountant / user access to bookkeeping software',           '[OWNER]', 'Day 2'],
            ['6',  'Request required source documents via secure portal',                       '[OWNER]', 'Day 2'],
            ['7',  'Capture entity type, fiscal year, basis, integrations, payroll, taxes',     '[OWNER]', 'Kickoff call'],
            ['8',  'Review opening balances and last fully reconciled period',                  '[OWNER]', 'Week 1'],
            ['9',  'Document known issues, cleanup scope, deadlines, responsibilities',         '[OWNER]', 'Week 1'],
            ['10', 'Run kickoff call; send written action summary within 24 hours',             '[OWNER]', 'Week 1'],
        ],
        col_widths_cm=[1.5, 10, 3, 3]
    )

    section_header(doc, 2, 'Monthly Close Checklist')
    body(doc, 'Work through these control points in sequence every month. '
         'Do not proceed past a step if the previous one has unresolved items.')
    doc.add_paragraph()

    for step_text in [
        'Confirm all bank, card, loan, payroll, and processor data is available',
        'Import / sync transactions; investigate duplicates or failed feeds',
        'Categorise all transactions; resolve uncategorised / suspense items',
        'Reconcile every bank and credit-card account to statements',
        'Reconcile loans, payroll liabilities, sales-tax/VAT, and clearing accounts',
        'Review accounts receivable, payable, negative balances, and stale items',
        'Record approved accruals, prepayments, depreciation, and adjustments within scope',
        'Compare current month with prior month and budget; document material variances',
        'Run balance-sheet integrity and reasonableness checks',
        'Prepare consolidated question list and obtain documented client responses',
        'Finalise P&L, balance sheet, cash summary, and all agreed reports',
        'Complete reviewer sign-off, lock/close period, and deliver to client portal',
    ]:
        checklist_item(doc, step_text)

    section_header(doc, 3, 'Tax Document Collection Checklist')
    body(doc, 'Use at year-end or when preparing the annual bookkeeping package for the tax preparer.')
    doc.add_paragraph()
    consulting_table(doc,
        ['Category', 'Documents Required'],
        [
            ['Income',        'Sales summaries, invoices, merchant reports, platform statements, interest income'],
            ['Banking',       'Year-end bank and credit-card statements, final reconciliations for all accounts'],
            ['Payroll',       'Annual payroll summary, W-2/1099 or local equivalent, payroll tax filings'],
            ['Expenses',      'Major receipts, insurance, rent, professional fees, travel, vehicle records'],
            ['Assets & Debt', 'Asset purchases/disposals with dates/amounts, year-end loan statements'],
            ['Tax & Compliance','Prior-year return, estimated payments, notices, sales-tax/VAT filings'],
            ['Owner Activity','All contributions, draws, distributions, shareholder/partner transactions'],
        ],
        col_widths_cm=[4, 13.5]
    )
    notice_box(doc,
        'Document collection is not tax advice. Confirm the final list and filing deadlines '
        'with the client\'s qualified tax professional.',
        label='SCOPE REMINDER', amber=True)

    section_header(doc, 4, 'Quality Control Review')
    body(doc, 'Complete before delivering any report to any client. '
         'Both bookkeeper and reviewer must sign off before period lock.')
    doc.add_paragraph()

    for qc_text in [
        'All statement balances agree to the ledger',
        'No unexplained suspense or uncategorised balances remaining',
        'Opening balances and retained earnings are understood and documented',
        'Negative assets / liabilities and unusual balances investigated and documented',
        'Payroll, loans, sales-tax/VAT, and processor clearing fully reconciled',
        'All material variances have documented explanations',
        'Reports use correct period, basis, entity, and comparison column',
        'All questions, judgments, and client approvals are documented in writing',
        'Period is locked or closed in the software after review sign-off',
        'Reports delivered to client portal — not by ordinary email',
    ]:
        checklist_item(doc, qc_text)

    save(doc, f'{OUT}/04-Operations-Library/Bookkeeping-SOPs-and-Checklists-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 7. CLIENT COMMUNICATION SCRIPTS
# ══════════════════════════════════════════════════════════════════════════════

def build_scripts():
    doc = new_doc()
    add_cover(doc,
              ['Client Communication', 'Scripts'],
              'Ten ready-to-use messages for every critical stage of the client lifecycle',
              '04  —  OPERATIONS LIBRARY',
              [('Document type', 'Internal Reference — Customise Before Sending'),
               ('Scripts included', '10  ·  Full client lifecycle'),
               ('Last updated', '2025')])
    add_header_footer(doc, 'Client Communication Scripts')

    notice_box(doc,
        'Internal reference only — not for direct forwarding. '
        'Customise [BRACKETED TEXT] for every recipient before sending.',
        label='CUSTOMISE BEFORE SENDING', amber=True)

    at_a_glance_box(doc, [
        ('Scripts',    '10',      'full lifecycle'),
        ('Channels',   'Email',   '+ portal messages'),
        ('Tone',       'Professional', 'clear & direct'),
        ('Format',     'Copy-paste', 'ready to use'),
    ])

    scripts = [
        ('01', 'Inquiry Response', 'Email',
         'Subject line: Next step for your bookkeeping inquiry',
         'Hi [NAME],\n\nThank you for reaching out. To understand whether we are a good fit, I have a few quick questions:\n\n→  Entity type and jurisdiction\n→  Current bookkeeping software\n→  Number of bank and credit-card accounts\n→  Average monthly transaction volume\n→  Payroll, sales tax/VAT, or multi-entity requirements\n→  Known backlogs or issues with current books\n→  Reporting needs (P&L, cash flow, custom)\n\nYou can reply here or complete the intake form: [LINK]\n\n[PRACTICE NAME]'),
        ('02', 'Diagnostic Booking', 'Email',
         'Subject line: Bookkeeping diagnostic confirmed — [DATE]',
         'Hi [NAME],\n\nYour diagnostic call is confirmed for [DATE] at [TIME] via [PLATFORM].\n\nWe will review your current system, last reconciled month, volume, known issues, and reporting goals.\n\nPlease securely upload or share before the call: [LIST OF DOCUMENTS]\n\nJoin link: [LINK]\n\n[PRACTICE NAME]'),
        ('03', 'Proposal Follow-Up', 'Email',
         'Subject line: Bookkeeping proposal — [COMPANY]',
         'Hi [NAME],\n\nFollowing up on the proposal sent [DATE] for [COMPANY]. It addresses [PRIMARY ISSUE] with a recommended scope of [SUMMARY] at €[AMOUNT] per month, assuming an engagement start of [DATE].\n\nHappy to answer questions before [DECISION DATE]. Book a call here: [LINK]\n\n[PRACTICE NAME]'),
        ('04', 'Welcome & Onboarding', 'Email',
         'Subject line: Welcome — your bookkeeping onboarding steps',
         'Hi [NAME],\n\nWelcome — we are glad to be working with you. Three steps to get started:\n\n01  Complete the intake form: [LINK]\n02  Grant bookkeeping software access (instructions attached)\n03  Upload requested documents to your portal: [LINK]\n\nPlease complete steps 01 and 02 by [DATE]. Your kickoff call is [DATE/TIME]: [LINK]\n\n[PRACTICE NAME]'),
        ('05', 'Missing Documents', 'Email or Portal',
         'Subject line: Documents needed — [MONTH] close',
         'Hi [NAME],\n\nTo complete the [MONTH] close on schedule, we still need:\n\n[LIST SPECIFIC MISSING ITEMS]\n\nPlease upload to your portal by [DATE]: [LINK]\n\nIf not received by [DATE], report delivery may move from [ORIGINAL DATE] to [REVISED DATE].\n\n[PRACTICE NAME]'),
        ('06', 'Transaction Questions', 'Email or Portal',
         'Subject line: [MONTH] bookkeeping questions',
         'Hi [NAME],\n\nThe [MONTH] question list is ready at [LINK]. Please respond by [DATE] to keep the close on schedule.\n\nWhen answering — if a transaction is personal, reimbursable, or owner-related, note that. If unclear, add context rather than guessing the account.\n\n[PRACTICE NAME]'),
        ('07', 'Close Complete', 'Email or Portal',
         'Subject line: [MONTH] books are closed',
         'Hi [NAME],\n\nThe [MONTH] books are complete. Your reports are at [LINK].\n\nKey items this month:\n→  [FINANCIAL INSIGHT 1]\n→  [FINANCIAL INSIGHT 2]\n→  [ACTION REQUIRED]\n\nPlease confirm there are no material events after month-end that may affect the records.\n\nNext close deadline: [DATE]\n\n[PRACTICE NAME]'),
        ('08', 'Year-End Handoff', 'Email',
         'Subject line: Year-end bookkeeping package — [COMPANY]',
         'Hi [NAME],\n\nThe year-end bookkeeping package for [COMPANY] ([FISCAL YEAR]) is ready in your portal: [LINK]\n\nThe package includes: final P&L, final balance sheet, reconciliation summaries, and [OTHER REPORTS].\n\nOpen items and bookkeeping judgments are documented at [LINK]. Please send proposed adjusting entries through the secure portal — not by email.\n\n[PRACTICE NAME]'),
        ('09', 'Overdue Invoice', 'Email',
         'Subject line: Invoice [NUMBER] — payment reminder',
         'Hi [NAME],\n\nInvoice [NUMBER] for €[AMOUNT] (service period [PERIOD]) was due [DATE] and remains outstanding.\n\nPayment options: [LINK / INSTRUCTIONS]\n\nUnder our engagement agreement, work may be paused if a balance remains overdue beyond [X] days. Please reach out if you have any questions.\n\n[PRACTICE NAME]'),
        ('10', 'Scope Change Approval', 'Email',
         'Subject line: Approval needed — scope change for [COMPANY]',
         'Hi [NAME],\n\nActual volume or complexity for [MONTH] differs from the proposal because: [SPECIFIC REASON].\n\nAdditional work required: [DESCRIPTION]\nRevised fee: €[AMOUNT] — [BILLING TERMS]\n\nThis work will not proceed without your approval. Please reply "Approved" or ask any questions.\n\n[PRACTICE NAME]'),
    ]

    for num, title, channel, subject, body_text in scripts:
        section_header(doc, int(num), title)

        # Channel + subject meta
        meta_t = doc.add_table(rows=1, cols=2)
        meta_t.alignment = WD_TABLE_ALIGNMENT.CENTER
        _remove_borders(meta_t)
        lc = meta_t.cell(0, 0)
        rc = meta_t.cell(0, 1)
        _cell_margins(lc, 30, 30, 0, 60)
        _cell_margins(rc, 30, 30, 60, 0)

        lp = lc.paragraphs[0]
        lr = lp.add_run(f'Channel  ·  {channel}')
        _font(lr, 'Calibri', 8, italic=True, color=MUTED)

        rp = rc.paragraphs[0]
        rr = rp.add_run(subject)
        _font(rr, 'Poppins', 8.5, bold=True, color=INK)

        doc.add_paragraph()
        script_box(doc, body_text)

    save(doc, f'{OUT}/04-Operations-Library/Client-Communication-Scripts-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 8. ANNUAL TAX PREP CHECKLIST
# ══════════════════════════════════════════════════════════════════════════════

def build_tax_prep():
    doc = new_doc()
    add_cover(doc,
              ['Annual Tax Prep', 'Checklist'],
              'A four-phase year-end guide for bookkeepers preparing the tax package',
              '04  —  OPERATIONS LIBRARY',
              [('Document type', 'Operational Checklist — Internal Use'),
               ('Phases', '4  ·  Close · Adjust · Collect · Assemble'),
               ('Last updated', '2025')])
    add_header_footer(doc, 'Annual Tax Prep Checklist')

    notice_box(doc,
        'This checklist supports year-end bookkeeping package preparation only. '
        'It is not tax advice. The tax preparer is responsible for all tax judgments and filings.',
        label='SCOPE NOTICE')

    at_a_glance_box(doc, [
        ('Phases',      '4',    'structured sequence'),
        ('Categories',  '8',    'document collection'),
        ('QC Steps',    '8+',   'before delivery'),
        ('Deliverables','8',    'report package items'),
    ])

    # Phase overview flow
    process_flow(doc, [
        ('Phase 1', 'Final Close'),
        ('Phase 2', 'Adjustments'),
        ('Phase 3', 'Doc Collection'),
        ('Phase 4', 'Package Assembly'),
    ])

    section_header(doc, 0, 'Engagement Details')
    consulting_table(doc,
        ['Field', 'Details'],
        [
            ['Client Name', ''],
            ['Fiscal Year End', ''],
            ['Tax Preparer Name / Firm', ''],
            ['Bookkeeping Software', ''],
            ['Package Delivery Deadline', ''],
            ['Prepared By', ''],
            ['Review / Sign-Off Date', ''],
        ],
        col_widths_cm=[5.5, 12]
    )

    phase_banner(doc, 1, 'Final Month Close',
                 'Complete the standard monthly close for the final month of the fiscal year')
    for item in [
        'Final month close completed per monthly close checklist',
        'All bank and credit-card accounts reconciled to year-end statements',
        'All loan accounts reconciled to year-end statements',
        'Payroll liabilities reconciled to payroll year-end reports',
        'Sales-tax / VAT accounts reconciled to filings',
        'Accounts receivable ageing reviewed and confirmed',
        'Accounts payable ageing reviewed and confirmed',
        'All suspense and clearing accounts at zero or fully documented',
    ]:
        checklist_item(doc, item)

    phase_banner(doc, 2, 'Year-End Adjustments',
                 'Record all entries needed to close the fiscal year correctly')
    for item in [
        'Depreciation / amortisation recorded (within scope)',
        'Prepaid expenses adjusted to correct period',
        'Accrued revenue or expenses recorded (within scope)',
        'Owner draw and contribution accounts reviewed',
        'Loans to / from owners fully documented',
        'Inventory count reconciled to ledger (if applicable)',
        'Prior-year adjusting entries from tax preparer posted',
    ]:
        checklist_item(doc, item)

    phase_banner(doc, 3, 'Document Collection',
                 'Collect and confirm all supporting documents for the tax preparer')
    consulting_table(doc,
        ['Category', 'Documents Required', 'Received', 'Notes'],
        [
            ['Income',        'All sales reports, merchant statements, platform reports, interest income', '☐', ''],
            ['Banking',       'Year-end bank and credit-card statements for all accounts',                 '☐', ''],
            ['Payroll',       'Annual payroll summary, W-2/1099 or equivalent, payroll tax filings',       '☐', ''],
            ['Major Expenses','Rent, insurance, professional fees, travel, vehicle records',               '☐', ''],
            ['Fixed Assets',  'Asset purchases and disposals with dates and amounts',                      '☐', ''],
            ['Loans & Finance','Year-end loan statements, amortisation schedules',                        '☐', ''],
            ['Tax & Compliance','Prior-year return, estimated payments, notices, VAT/sales-tax filings',  '☐', ''],
            ['Owner Activity','Contributions, draws, distributions, shareholder/partner transactions',     '☐', ''],
        ],
        col_widths_cm=[3.5, 8.5, 1.5, 4]
    )

    phase_banner(doc, 4, 'Package Assembly',
                 'Compile and deliver the complete year-end bookkeeping package')
    consulting_table(doc,
        ['Report / Item', 'Format', 'Done', 'Notes'],
        [
            ['Annual Profit & Loss (full year)',         'PDF',            '☐', ''],
            ['Annual Balance Sheet (year-end)',           'PDF',            '☐', ''],
            ['Cash Flow Statement (if applicable)',       'PDF',            '☐', ''],
            ['Monthly P&L comparison (all 12 months)',    'PDF or Excel',   '☐', ''],
            ['Bank reconciliation summaries',             'PDF',            '☐', ''],
            ['Trial balance (year-end)',                  'Excel or PDF',   '☐', ''],
            ['Open items and bookkeeping judgment log',   'PDF or Notes',   '☐', ''],
            ['Chart of accounts (year-end)',              'PDF',            '☐', ''],
        ],
        col_widths_cm=[8.5, 3.5, 1.5, 4]
    )

    notice_box(doc,
        'Upload the completed package to the client\'s secure portal and notify the tax preparer '
        'through the appropriate channel. Do not email sensitive financial reports. '
        'The tax preparer is responsible for all tax judgments and filings.',
        label='DELIVERY AND SCOPE NOTICE', amber=True)

    save(doc, f'{OUT}/04-Operations-Library/Annual-Tax-Prep-Checklist-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('Building NovaOps consulting-grade DOCX files...')
    build_start_here()
    build_service_guide()
    build_intake_pack()
    build_proposal()
    build_engagement_agreement()
    build_sops()
    build_scripts()
    build_tax_prep()
    print('All DOCX files done.')
