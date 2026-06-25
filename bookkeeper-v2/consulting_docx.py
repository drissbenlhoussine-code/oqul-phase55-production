"""
CONSULTING-GRADE DOCX builder — Bookkeeper Practice Launch System v2.0
Design standard: McKinsey / Deloitte / PwC
- White pages, maximum white space
- Thin rule lines and left-border callouts (no heavy coloured fills)
- Section numbering: 01 — TITLE format
- Premium consulting cover pages
- Poppins headings / Inter body
- Minimal color — teal as accent, never backgrounds
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/v2-consulting'

# ── Brand Colours ──────────────────────────────────────────────────────────────
TEAL    = RGBColor(0x0F, 0x76, 0x6E)
INK     = RGBColor(0x0F, 0x17, 0x2A)
AMBER   = RGBColor(0xD9, 0x77, 0x06)
MUTED   = RGBColor(0x64, 0x74, 0x8B)
RULE    = RGBColor(0xCB, 0xD5, 0xE1)
SOFT_BG = RGBColor(0xF8, 0xFA, 0xFC)
TEAL_10 = RGBColor(0xF0, 0xFD, 0xFA)
AMB_10  = RGBColor(0xFF, 0xFB, 0xEB)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
DARK    = RGBColor(0x0F, 0x17, 0x2A)


# ══════════════════════════════════════════════════════════════════════════════
# XML / STYLE HELPERS
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


def _set_cell_borders(cell, sides, color=RULE, size=4):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    hx = hex3(color)
    for side in ['top','bottom','left','right','insideH','insideV']:
        b = OxmlElement(f'w:{side}')
        if side in sides:
            b.set(qn('w:val'), 'single')
            b.set(qn('w:sz'), str(size))
            b.set(qn('w:color'), hx)
        else:
            b.set(qn('w:val'), 'none')
            b.set(qn('w:sz'), '0')
            b.set(qn('w:color'), 'auto')
        tcBorders.append(b)
    existing = tcPr.find(qn('w:tcBorders'))
    if existing is not None:
        tcPr.remove(existing)
    tcPr.append(tcBorders)


def _remove_borders(table):
    for row in table.rows:
        for cell in row.cells:
            _set_cell_borders(cell, [], RULE, 0)


def _cell_margins(cell, top=60, bottom=60, left=120, right=120):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for side, val in [('top',top),('bottom',bottom),('left',left),('right',right)]:
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


def _para_spacing(para, before=0, after=4):
    pPr = para._p.get_or_add_pPr()
    sp = OxmlElement('w:spacing')
    sp.set(qn('w:before'), str(before * 20))
    sp.set(qn('w:after'), str(after * 20))
    ex = pPr.find(qn('w:spacing'))
    if ex is not None:
        pPr.remove(ex)
    pPr.append(sp)


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
    for tag, text in [('begin', None), ('instrText', 'PAGE'), ('separate', None), ('end', None)]:
        if tag == 'instrText':
            el = OxmlElement('w:instrText')
            el.text = text
        else:
            el = OxmlElement('w:fldChar')
            el.set(qn('w:fldCharType'), tag)
        run._r.append(el)
    _font(run, 'Inter', 8, bold=True, color=TEAL)


# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT FACTORY
# ══════════════════════════════════════════════════════════════════════════════

def new_doc():
    doc = Document()
    for section in doc.sections:
        section.top_margin    = Cm(2.4)
        section.bottom_margin = Cm(2.4)
        section.left_margin   = Cm(2.5)
        section.right_margin  = Cm(2.5)
    doc.styles['Normal'].font.name = 'Inter'
    doc.styles['Normal'].font.size = Pt(9.5)
    return doc


def add_header_footer(doc, doc_title=''):
    """Consulting header: thin teal rule + small text. Footer: thin rule + page number."""
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

    # Left: brand name
    lc = ht.cell(0, 0)
    _cell_margins(lc, 60, 60, 0, 60)
    lp = lc.paragraphs[0]
    lr = lp.add_run('BOOKKEEPER PRACTICE LAUNCH SYSTEM  ·  v2.0')
    _font(lr, 'Inter', 7, color=MUTED)
    lp.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Right: doc title
    rc = ht.cell(0, 1)
    _cell_margins(rc, 60, 60, 60, 0)
    rp = rc.paragraphs[0]
    rr = rp.add_run(doc_title.upper())
    _font(rr, 'Inter', 7, bold=True, color=INK)
    rp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # Teal rule below header (using table bottom border)
    for cell in [lc, rc]:
        _set_cell_borders(cell, ['bottom'], TEAL, 12)

    # ── FOOTER ────────────────────────────────────────────────────────────────
    footer = section.footer
    footer.is_linked_to_previous = False
    for p in footer.paragraphs:
        p.clear()

    ft = footer.add_table(1, 2, width=Inches(6.3))
    ft.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(ft)

    # Rule above footer
    lfc = ft.cell(0, 0)
    rfc = ft.cell(0, 1)
    for c in [lfc, rfc]:
        _set_cell_borders(c, ['top'], RULE, 4)
        _cell_margins(c, 50, 50, 0, 0)

    lfp = lfc.paragraphs[0]
    lfr = lfp.add_run('Confidential  ·  Commercial Use Licence  ·  © 2025 Bookkeeper Practice Launch System')
    _font(lfr, 'Inter', 7, color=MUTED)
    lfp.alignment = WD_ALIGN_PARAGRAPH.LEFT

    rfp = rfc.paragraphs[0]
    rfr = rfp.add_run('Page ')
    _font(rfr, 'Inter', 8, color=MUTED)
    _page_number(rfp)
    rfp.alignment = WD_ALIGN_PARAGRAPH.RIGHT


def add_cover(doc, title_lines, subtitle, section_code='', meta_pairs=None):
    """Premium consulting cover — dark navy, minimal."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0)
    _set_cell_bg(cell, DARK)
    _cell_margins(cell, top=800, bottom=800, left=700, right=700)
    _cell_valign(cell, 'center')
    _remove_borders(t)

    # Teal accent strip — rendered as a thin paragraph shading
    p_strip = cell.add_paragraph()
    _set_para_shading(p_strip, TEAL)
    _para_spacing(p_strip, 0, 0)
    doc_p = p_strip._p
    doc_p.getparent().remove(doc_p)
    # insert at top of cell
    cell._tc.insert(1, p_strip._p)

    # Section code
    if section_code:
        p_code = cell.add_paragraph()
        r_code = p_code.add_run(section_code.upper())
        _font(r_code, 'Poppins', 8, bold=True, color=TEAL)
        _para_spacing(p_code, 0, 12)

    # Title
    for line in title_lines:
        p_t = cell.add_paragraph()
        r_t = p_t.add_run(line)
        _font(r_t, 'Poppins', 30, bold=True, color=WHITE)
        _para_spacing(p_t, 0, 4)

    # Subtitle
    p_sub = cell.add_paragraph()
    r_sub = p_sub.add_run(subtitle)
    _font(r_sub, 'Inter', 12, color=RGBColor(0x94, 0xA3, 0xB8))
    _para_spacing(p_sub, 6, 20)

    # Teal rule
    p_rule = cell.add_paragraph()
    _para_spacing(p_rule, 0, 16)
    pPr = p_rule._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '12')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), hex3(TEAL))
    pBdr.append(bottom)
    pPr.append(pBdr)

    # Meta pairs
    if meta_pairs:
        for label, value in meta_pairs:
            p_m = cell.add_paragraph()
            r_label = p_m.add_run(f'{label.upper()}  ')
            _font(r_label, 'Inter', 7.5, color=MUTED)
            r_val = p_m.add_run(value)
            _font(r_val, 'Inter', 8, bold=True, color=WHITE)
            _para_spacing(p_m, 0, 3)

    # Version badge
    p_v = cell.add_paragraph()
    r_v = p_v.add_run('VERSION 2.0  ·  PREMIUM EDITION  ·  2025')
    _font(r_v, 'Poppins', 7.5, bold=True, color=AMBER)
    _para_spacing(p_v, 40, 0)

    doc.add_page_break()


def _set_para_shading(para, rgb: RGBColor):
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex3(rgb))
    pPr.append(shd)


# ══════════════════════════════════════════════════════════════════════════════
# PARAGRAPH HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def h1(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    _font(r, 'Poppins', 18, bold=True, color=INK)
    _para_spacing(p, 14, 4)
    return p


def h2(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    _font(r, 'Poppins', 12, bold=True, color=TEAL)
    _para_spacing(p, 10, 3)
    return p


def h3(doc, text, color=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    _font(r, 'Poppins', 10.5, bold=True, color=color or INK)
    _para_spacing(p, 8, 2)
    return p


def body(doc, text, size=9.5, color=None, italic=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    _font(r, 'Inter', size, italic=italic, color=color or INK)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    _para_spacing(p, 0, 4)
    return p


def bullet(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run(text)
    _font(r, 'Inter', 9.5, color=INK)
    _para_spacing(p, 0, 2)
    return p


def section_rule(doc):
    """Thin teal rule line for section breaks."""
    p = doc.add_paragraph()
    _para_spacing(p, 6, 6)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '8')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), hex3(TEAL))
    pBdr.append(bottom)
    pPr.append(pBdr)


def section_num_label(doc, number, title):
    """01 — SECTION TITLE  (number in teal, title in ink)"""
    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)

    # Number cell
    nc = t.cell(0, 0)
    nc.width = Cm(1.5)
    _cell_margins(nc, 0, 0, 0, 60)
    np_ = nc.paragraphs[0]
    nr = np_.add_run(f'{number:02d}')
    _font(nr, 'Poppins', 10, bold=True, color=TEAL)
    _para_spacing(np_, 0, 0)

    # Title cell
    tc = t.cell(0, 1)
    _cell_margins(tc, 0, 0, 0, 0)
    tp = tc.paragraphs[0]
    tr = tp.add_run(f'—  {title.upper()}')
    _font(tr, 'Poppins', 10, bold=True, color=INK)
    _para_spacing(tp, 0, 0)

    # Rule below
    section_rule(doc)
    return t


def key_message_box(doc, text, label='KEY MESSAGE'):
    """McKinsey-style key message — left border, very light tint."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0)
    _set_cell_bg(cell, TEAL_10)
    _cell_margins(cell, top=120, bottom=120, left=180, right=180)
    _set_cell_borders(cell, ['left'], TEAL, 18)
    _set_cell_borders_right_top_bottom(cell)

    p_l = cell.add_paragraph()
    r_l = p_l.add_run(label)
    _font(r_l, 'Poppins', 7, bold=True, color=TEAL)
    _para_spacing(p_l, 0, 4)

    p_t = cell.paragraphs[0]
    r_t = p_t.add_run(text)
    _font(r_t, 'Inter', 9.5, bold=True, color=INK)
    _para_spacing(p_t, 0, 0)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 4)
    return t


def _set_cell_borders_right_top_bottom(cell):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for side in ['top', 'right', 'bottom']:
        b = OxmlElement(f'w:{side}')
        b.set(qn('w:val'), 'single')
        b.set(qn('w:sz'), '4')
        b.set(qn('w:color'), hex3(RULE))
        tcBorders.append(b)
    existing = tcPr.find(qn('w:tcBorders'))
    if existing is not None:
        for side in ['top', 'right', 'bottom']:
            el = existing.find(qn(f'w:{side}'))
            if el is not None:
                existing.remove(el)
            existing.append(tcBorders.find(qn(f'w:{side}')))
    else:
        tcPr.append(tcBorders)


def notice_box(doc, text, label='NOTICE', amber=False):
    bg = AMB_10 if amber else RGBColor(0xF1, 0xF5, 0xF9)
    border_color = AMBER if amber else MUTED
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0)
    _set_cell_bg(cell, bg)
    _cell_margins(cell, top=100, bottom=100, left=160, right=160)
    _set_cell_borders(cell, ['left'], border_color, 14)
    _set_cell_borders_right_top_bottom(cell)

    p_l = cell.add_paragraph()
    r_l = p_l.add_run(label)
    _font(r_l, 'Poppins', 7, bold=True, color=border_color)
    _para_spacing(p_l, 0, 4)

    p_t = cell.paragraphs[0]
    r_t = p_t.add_run(text)
    _font(r_t, 'Inter', 9, color=INK)
    _para_spacing(p_t, 0, 0)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 4)
    return t


def consulting_table(doc, headers, rows, col_widths_cm=None):
    """Consulting-grade table: teal header, zebra rows, thin grid."""
    n = len(headers)
    t = doc.add_table(rows=1 + len(rows), cols=n)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = 'Table Grid'

    if col_widths_cm:
        for i, w in enumerate(col_widths_cm):
            for row in t.rows:
                row.cells[i].width = Cm(w)

    # Header row
    for j, h in enumerate(headers):
        cell = t.cell(0, j)
        _set_cell_bg(cell, TEAL)
        _cell_margins(cell, 70, 70, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        _font(r, 'Poppins', 8, bold=True, color=WHITE)

    # Data rows
    for i, row_data in enumerate(rows):
        bg = WHITE if i % 2 == 0 else SOFT_BG
        for j, val in enumerate(row_data):
            cell = t.cell(i + 1, j)
            _set_cell_bg(cell, bg)
            _set_cell_borders(cell, ['top','bottom','left','right'], RULE, 4)
            _cell_margins(cell, 55, 55, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(str(val))
            _font(r, 'Inter', 8.5, color=INK)

    # Strong bottom border on header
    for j in range(n):
        _set_cell_borders(t.cell(0, j), ['bottom'], TEAL, 8)

    p_sp = doc.add_paragraph()
    _para_spacing(p_sp, 0, 6)
    return t


def step_row(doc, number, title, description):
    """Numbered step row — teal number + title + description."""
    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _remove_borders(t)

    nc = t.cell(0, 0)
    nc.width = Cm(1.4)
    _cell_margins(nc, 80, 80, 0, 80)
    np_ = nc.paragraphs[0]
    nr = np_.add_run(number)
    _font(nr, 'Poppins', 16, bold=True, color=TEAL)
    _para_spacing(np_, 0, 0)
    _cell_valign(nc, 'top')

    tc_cell = t.cell(0, 1)
    _cell_margins(tc_cell, 60, 60, 0, 0)
    # Rule above
    _set_cell_borders(tc_cell, ['top'], RULE, 4)

    tp = tc_cell.paragraphs[0]
    tr = tp.add_run(title)
    _font(tr, 'Poppins', 10.5, bold=True, color=INK)
    _para_spacing(tp, 0, 2)

    dp = tc_cell.add_paragraph()
    dr = dp.add_run(description)
    _font(dr, 'Inter', 9, color=MUTED)
    _para_spacing(dp, 0, 6)
    _cell_valign(tc_cell, 'top')

    return t


def save(doc, path):
    doc.save(path)
    print(f'  ✓ {os.path.basename(path)}')


# ══════════════════════════════════════════════════════════════════════════════
# 1. START HERE
# ══════════════════════════════════════════════════════════════════════════════

def build_start_here():
    doc = new_doc()
    add_cover(doc, ['Start Here'], 'Your 90-minute launch guide to the complete system',
              '00  —  START HERE',
              [('Version', '2.0  —  June 2025'), ('Audience', 'Product Owner')])
    add_header_footer(doc, 'Start Here')

    h1(doc, 'Welcome to Bookkeeper Practice Launch System v2.0')
    body(doc, 'You now have a complete operating system for your bookkeeping practice. '
         'This guide shows you exactly what you received, how to set it up in 90 minutes, '
         'and how every file connects to the next.')

    key_message_box(doc,
        'Read this file before opening anything else. It tells you what to do, in what order, '
        'and why each step matters.',
        'START HERE — READ FIRST')
    doc.add_paragraph()

    section_num_label(doc, 1, 'What Is Included')
    consulting_table(doc,
        ['Folder', 'Purpose'],
        [
            ['00 — START HERE', 'Orientation, setup walkthrough, and file inventory'],
            ['01 — QUICK REFERENCE', 'Licence, FAQ, version history, support guide'],
            ['02 — PRACTICE DASHBOARD', 'Excel dashboard — your daily operations hub'],
            ['03 — CLIENT DOCUMENTS', 'Service guide, proposal, agreement, intake pack, deck'],
            ['04 — OPERATIONS LIBRARY', 'SOPs, checklists, and communication scripts'],
            ['05 — NOTION WORKSPACE', '7 CSV databases and Notion setup guide'],
        ],
        col_widths_cm=[5, 12.5]
    )

    section_num_label(doc, 2, '90-Minute Setup Sequence')
    steps = [
        ('01', 'Read the guides (10 min)', 'Read this file, then Installation-Guide.pdf in 00-START-HERE. Understand the full system before customising anything.'),
        ('02', 'Customise the Dashboard (20 min)', 'Open 02-Practice-Dashboard/Bookkeeper-Practice-Dashboard-v2.xlsx. Fill in all yellow Setup cells with your practice name, services, and pricing.'),
        ('03', 'Customise client documents (25 min)', 'Replace all [BRACKETED TEXT] in the 5 files in 03-Client-Documents. Use Find & Replace in Word (Ctrl+H).'),
        ('04', 'Build Notion workspace (15 min)', 'Follow Notion-Setup-Guide.pdf in 05-Notion-Workspace. Import all 7 CSV files and connect them with Relations.'),
        ('05', 'Validate and review (15 min)', 'Add 2–3 sample clients. Confirm KPI cards populate on the Dashboard sheet. Search every DOCX for remaining brackets.'),
        ('06', 'Read the Licence (5 min)', 'Review 01-Quick-Reference/License.pdf before sending any document to a client.'),
    ]
    for num, title, desc in steps:
        step_row(doc, num, title, desc)

    section_num_label(doc, 3, 'Core Client Workflow')
    consulting_table(doc,
        ['Stage', 'Action', 'File'],
        [
            ['Lead', 'Qualify entity, volume, software, complexity, urgency', 'Lead Pipeline (Dashboard)'],
            ['Diagnostic', 'Review books, backlog, accounts, and reporting needs', 'Client-Intake-and-Onboarding-Pack-v2'],
            ['Proposal', 'Define scope, assumptions, cleanup, and recurring fee', 'Bookkeeping-Proposal-Template-v2'],
            ['Engagement', 'Sign contract, collect payment, confirm responsibilities', 'Bookkeeping-Engagement-Agreement-v2'],
            ['Onboarding', 'Collect access, COA, documents, deadlines', 'Client-Intake-and-Onboarding-Pack-v2'],
            ['Monthly Close', 'Reconcile, review, adjust, report, document exceptions', 'Dashboard + SOPs-and-Checklists-v2'],
            ['Report Delivery', 'Deliver reports, explain variances, confirm next actions', 'Client Portal (Notion) + Scripts'],
        ],
        col_widths_cm=[3.5, 7.5, 6.5]
    )

    notice_box(doc,
        'This product supports bookkeeping operations only. It does not constitute accounting, tax, '
        'legal, audit, assurance, payroll, or regulatory advice. Adapt all files to your credentials, '
        'jurisdiction, and permitted professional scope before use.',
        label='PROFESSIONAL SCOPE — READ BEFORE CLIENT USE', amber=True)

    save(doc, f'{OUT}/00-START-HERE/Start-Here-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 2. BOOKKEEPING SERVICE GUIDE
# ══════════════════════════════════════════════════════════════════════════════

def build_service_guide():
    doc = new_doc()
    add_cover(doc,
              ['Bookkeeping', 'Service Guide'],
              'Your complete guide to our services, packages, and process',
              '03  —  CLIENT DOCUMENTS',
              [('Prepared by', '[PRACTICE NAME]'), ('Document type', 'Client-Facing Guide')])
    add_header_footer(doc, 'Bookkeeping Service Guide')

    notice_box(doc, 'Replace all [BRACKETED TEXT] with your practice details before sending to clients.',
               label='CUSTOMISATION REQUIRED', amber=True)

    section_num_label(doc, 1, 'What Monthly Bookkeeping Includes')
    body(doc, 'Every monthly bookkeeping engagement with [PRACTICE NAME] includes the following services as standard:')
    for item in [
        'Transaction categorisation and ledger review',
        'Bank and credit-card reconciliations for all agreed accounts',
        'Balance-sheet account review and exception documentation',
        'Monthly financial statements — Profit & Loss and Balance Sheet',
        'Consolidated exception log and missing-document requests',
        'Agreed monthly communication cadence and close schedule',
        'Secure report delivery via client portal',
    ]:
        bullet(doc, item)

    section_num_label(doc, 2, 'Service Packages')
    consulting_table(doc,
        ['Package', 'Typical Scope', 'Includes', 'Starting Price'],
        [
            ['Essentials', 'Up to [X] accounts, [X] transactions / month', 'Monthly P&L, Balance Sheet, reconciliations', '€[ ] / month'],
            ['Growth', 'Higher volume, class or location tracking', 'All Essentials + monthly review call, cash summary', '€[ ] / month'],
            ['Advanced', 'Multi-entity or complex workflows', 'All Growth + custom reporting, priority support', '€[ ] / month'],
            ['Tax Ready Add-On', 'Year-end package preparation', 'Tax document checklist + preparer coordination', '€[ ] / year'],
        ],
        col_widths_cm=[3, 5.5, 6.5, 3]
    )

    section_num_label(doc, 3, 'Optional Project Services')
    consulting_table(doc,
        ['Service', 'Description', 'Pricing Basis'],
        [
            ['Catch-up / Cleanup Bookkeeping', 'Bring overdue or disorganised books current', 'Quote after diagnostic'],
            ['Historical Reconciliations', 'Reconcile prior months or years', 'Quote after diagnostic'],
            ['Chart-of-Accounts Redesign', 'Rebuild account structure for clarity and reporting', 'Fixed fee: €[ ]'],
            ['Software Migration & Setup', 'Move from one platform to another', 'Quote per project'],
            ['Accounts Payable / Receivable', 'Invoice management and payment tracking support', '€[ ] / month add-on'],
        ],
        col_widths_cm=[5, 7, 6]
    )

    section_num_label(doc, 4, 'Service Boundaries — What Is Not Included')
    notice_box(doc,
        'The following are outside the scope of bookkeeping unless separately contracted and '
        'legally permitted in your jurisdiction: tax advice and return preparation, audit and assurance '
        'services, payroll processing, legal advice, regulatory compliance, CFO services.',
        label='SERVICE SCOPE EXCLUSIONS', amber=True)

    section_num_label(doc, 5, 'Client Responsibilities')
    body(doc, 'A successful engagement requires active client participation. Clients are responsible for:')
    for item in [
        'Providing complete and accurate records by the agreed deadline each month',
        'Maintaining secure account access and approving role-based software invitations',
        'Answering transaction questions within [X] business days',
        'Retaining original source documents for the legally required period',
        'Reviewing reports and notifying us promptly of errors or material events',
        'Engaging a qualified tax professional for all tax advice and return filings',
    ]:
        bullet(doc, item)

    section_num_label(doc, 6, 'Monthly Timeline')
    consulting_table(doc,
        ['Day of Month', 'Activity', 'Responsible Party'],
        [
            ['Days 1–5', 'Client provides bank statements, payroll reports, loan records, and missing documents', 'Client'],
            ['Days 5–12', 'Bookkeeper imports transactions, categorises, reconciles, and raises questions', 'Bookkeeper'],
            ['Days 12–18', 'Client answers questions; bookkeeper posts adjustments and finalises', 'Both'],
            ['By Day [X]', 'Reports and action summary delivered through the secure portal', 'Bookkeeper'],
        ],
        col_widths_cm=[3, 11, 4]
    )

    notice_box(doc,
        'We use secure client portals, read-only accountant access, and approved password managers. '
        'We will never ask you to share banking credentials by email. '
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
              'Everything needed for a clean, confident engagement start',
              '03  —  CLIENT DOCUMENTS',
              [('Prepared by', '[PRACTICE NAME]'), ('Client', '[CLIENT COMPANY]')])
    add_header_footer(doc, 'Client Intake & Onboarding Pack')

    notice_box(doc, 'Complete Sections 1–4 with the client during or before the kickoff call. Replace all [BRACKETED TEXT] before sending.',
               label='INSTRUCTIONS', amber=True)

    section_num_label(doc, 1, 'Business Profile')
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
        col_widths_cm=[7, 11]
    )

    section_num_label(doc, 2, 'Volume & Complexity Assessment')
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
        col_widths_cm=[8, 10]
    )

    section_num_label(doc, 3, 'Documents Required')
    body(doc, 'Please upload the following documents to your secure portal at [PORTAL LINK] before the kickoff call:')
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
        bullet(doc, item)

    notice_box(doc,
        'Never share banking passwords by email. Use secure portals, read-only accountant access, '
        'or an approved password manager only. We will never request passwords by ordinary email.',
        label='SECURITY NOTICE — READ BEFORE SUBMITTING', amber=True)

    section_num_label(doc, 4, 'Kickoff Decisions')
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
        col_widths_cm=[7, 11]
    )

    section_num_label(doc, 5, 'Access & Integration Checklist')
    consulting_table(doc,
        ['Access Item', 'Status', 'Notes'],
        [
            ['Bookkeeping software (accountant role)', '[ ] Granted', ''],
            ['Bank feed connection or read-only access', '[ ] Granted', ''],
            ['Payroll platform (read-only)', '[ ] Granted', ''],
            ['Payment processor / e-commerce reports', '[ ] Granted', ''],
            ['Client portal invitation accepted', '[ ] Accepted', ''],
            ['Document upload folder shared', '[ ] Shared', ''],
        ],
        col_widths_cm=[7.5, 3, 7.5]
    )

    save(doc, f'{OUT}/03-Client-Documents/Client-Intake-and-Onboarding-Pack-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 4. PROPOSAL TEMPLATE
# ══════════════════════════════════════════════════════════════════════════════

def build_proposal():
    doc = new_doc()
    add_cover(doc,
              ['Bookkeeping Services', 'Proposal'],
              'Prepared for [CLIENT COMPANY] by [PRACTICE NAME]',
              '03  —  CLIENT DOCUMENTS',
              [('Prepared for', '[CLIENT COMPANY]'), ('Prepared by', '[PRACTICE NAME]'),
               ('Date', '[DATE]'), ('Valid until', '[DATE + 14 days]')])
    add_header_footer(doc, 'Bookkeeping Services Proposal')

    notice_box(doc, 'Complete all [BRACKETED] fields for this specific client. Replace sample figures with real diagnostic findings.',
               label='CUSTOMISATION REQUIRED', amber=True)

    section_num_label(doc, 1, 'Proposal Details')
    consulting_table(doc,
        ['Detail', 'Information'],
        [
            ['Prepared For', '[CLIENT COMPANY]'],
            ['Contact Name & Title', '[NAME / TITLE]'],
            ['Prepared By', '[PRACTICE NAME]'],
            ['Proposal Date', '[DATE]'],
            ['Valid Until', '[DATE + 14 days]'],
            ['Proposed Engagement Start', '[DATE]'],
        ],
        col_widths_cm=[5, 13]
    )

    section_num_label(doc, 2, 'Current Situation')
    body(doc, '[Summarise the client\'s current books, backlog, software, reporting gaps, and the outcome they want to achieve. Be specific — reference findings from your diagnostic. This section demonstrates that you understand their situation before presenting a solution.]')

    section_num_label(doc, 3, 'Recommended Scope')
    consulting_table(doc,
        ['Service', 'Cadence', 'What Is Included'],
        [
            ['Bookkeeping', 'Monthly', 'Categorisation, reconciliation, review, and approved adjusting entries'],
            ['Financial Reporting', 'Monthly', 'Profit & Loss, Balance Sheet, and [additional agreed reports]'],
            ['Client Questions', 'Monthly', 'Consolidated exception list and documented follow-up'],
            ['Review Meeting', '[Cadence]', '[Duration] review call with [participants]'],
            ['Cleanup Project', 'One-time', '[Months / accounts / issues included in cleanup scope]'],
        ],
        col_widths_cm=[3.5, 3, 11.5]
    )

    section_num_label(doc, 4, 'Implementation Plan')
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
        col_widths_cm=[1.5, 11, 5.5]
    )

    section_num_label(doc, 5, 'Investment')
    consulting_table(doc,
        ['Item', 'Fee', 'Billing'],
        [
            ['Setup / Diagnostic Fee', '€[ ]', 'Due on acceptance'],
            ['Cleanup Project', '€[ ]', '[e.g., 50% on start, 50% on delivery]'],
            ['Monthly Bookkeeping', '€[ ] / month', 'Monthly in advance, first day of service month'],
            ['Additional Work', '€[ ] / hour', 'With written approval before commencement'],
        ],
        col_widths_cm=[6.5, 3, 8.5]
    )
    notice_box(doc,
        'Pricing assumes the transaction volume, account count, software, and book condition described '
        'above. Material changes after engagement start may require a pricing review with [X] days written notice.',
        label='PRICING ASSUMPTIONS')

    section_num_label(doc, 6, 'Assumptions & Exclusions')
    for item in [
        'Pricing assumes books are in the condition described following the diagnostic review.',
        'Tax advice, returns, audit/assurance, legal advice, and CFO services are excluded unless separately contracted.',
        'Client provides source documents and answers to questions by agreed monthly deadlines.',
        'Material scope or volume changes require a written pricing amendment.',
    ]:
        bullet(doc, item)

    section_num_label(doc, 7, 'Acceptance')
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
        col_widths_cm=[5.5, 12.5]
    )
    notice_box(doc, 'Questions before accepting? Contact [PRACTICE NAME] at [EMAIL] or [PHONE]. This proposal expires on [DATE + 14 days].',
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
              [('Practice', '[PRACTICE LEGAL NAME]'), ('Client', '[CLIENT LEGAL NAME]'),
               ('Agreement date', '[DATE]'), ('Governed by', '[JURISDICTION]')])
    add_header_footer(doc, 'Bookkeeping Engagement Agreement')

    notice_box(doc,
        'This is a general template — not legal advice. Engage a qualified lawyer in your jurisdiction '
        'to review it before sending to any client. Do not skip this step.',
        label='LEGAL REVIEW REQUIRED BEFORE USE', amber=True)

    section_num_label(doc, 0, 'Agreement Details')
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
        col_widths_cm=[5, 13]
    )

    clauses = [
        (1, 'Services',
         'The Practice will perform the bookkeeping services described in the attached Scope of Work. '
         'Services not expressly listed are excluded. The Scope of Work may be updated by written '
         'amendment signed by both parties.'),
        (2, 'Client Responsibilities',
         'Client remains responsible for all business decisions, internal controls, source records, '
         'transaction authorisation, legal compliance, and the completeness and accuracy of all '
         'information supplied. The Practice relies on information provided by Client and does not '
         'independently verify source documents.'),
        (3, 'No Assurance, Tax, or Legal Opinion',
         'Unless separately agreed and legally permitted, this engagement does not include audit, '
         'review, assurance, tax advice, tax-return preparation, legal advice, fraud detection, '
         'forensic accounting, or independent verification of source information.'),
        (4, 'Fees and Payment',
         'Fees are [AMOUNT/STRUCTURE] as described in the attached Scope of Work. Invoices are due '
         '[TERMS]. Work may be suspended for overdue balances after [X] days written notice. '
         'Client remains responsible for fees for completed work during any suspension.'),
        (5, 'Access and Security',
         'Both parties will maintain reasonable security controls and use role-based software access. '
         'Client will not transmit passwords through ordinary email. Each party will promptly notify '
         'the other of any suspected unauthorised access to systems or client data.'),
        (6, 'Deadlines and Delays',
         'Delivery dates depend on timely receipt of records, responses, and approvals from Client. '
         'Client delays may shift close and reporting dates by an equivalent period without penalty to the Practice.'),
        (7, 'Corrections and Prior Periods',
         'The Practice may correct bookkeeping errors identified during the engagement. Material '
         'prior-period or cleanup work outside scope requires written approval and additional fees.'),
        (8, 'Confidentiality and Privacy',
         'Each party will protect the other\'s confidential information using at least reasonable care '
         'and will comply with applicable privacy obligations. Data-processing terms required by law '
         'may be attached as a schedule.'),
        (9, 'Third-Party Systems',
         'The Practice is not responsible for outages, data loss, policy changes, fees, or errors '
         'caused by banks, accounting software, payroll providers, payment processors, or other '
         'third parties used in delivering services.'),
        (10, 'Records and Retention',
         'Client owns and is responsible for retaining original source documents for the legally '
         'required period. The Practice may retain working files in accordance with its retention '
         'policy and applicable professional standards.'),
        (11, 'Termination',
         'Either party may terminate with [NUMBER] days written notice. Client will pay for all '
         'completed work, work in progress, and non-cancellable costs before the effective date. '
         'The Practice will deliver a final report package on termination.'),
        (12, 'Limitation and Dispute Resolution',
         'Liability limits, governing law, venue, and dispute resolution must be customised for '
         'the applicable jurisdiction and reviewed by a qualified lawyer before use. [CUSTOMISE FOR YOUR JURISDICTION]'),
        (13, 'Entire Agreement',
         'This Agreement and all attached schedules constitute the entire agreement between the '
         'parties and supersede all prior discussions. Changes require a written amendment signed '
         'by authorised representatives of both parties.'),
    ]

    for num, title, text in clauses:
        section_num_label(doc, num, title)
        body(doc, text)
        doc.add_paragraph()

    section_num_label(doc, 14, 'Scope of Work')
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
        col_widths_cm=[5.5, 12.5]
    )

    section_num_label(doc, 15, 'Signatures')
    consulting_table(doc,
        ['Party', 'Name & Title', 'Signature', 'Date'],
        [
            ['Client', '', '', ''],
            ['Practice', '[PRACTICE NAME]', '', ''],
        ],
        col_widths_cm=[2.5, 6, 5.5, 4]
    )

    save(doc, f'{OUT}/03-Client-Documents/Bookkeeping-Engagement-Agreement-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 6. SOPs & CHECKLISTS
# ══════════════════════════════════════════════════════════════════════════════

def build_sops():
    doc = new_doc()
    add_cover(doc,
              ['Bookkeeping SOPs &', 'Checklists'],
              'Internal operating manual — onboarding, monthly close, QC, and documents',
              '04  —  OPERATIONS LIBRARY',
              [('Document type', 'Internal Procedures'), ('Audience', 'Bookkeeper / Practice Owner')])
    add_header_footer(doc, 'Bookkeeping SOPs & Checklists')

    notice_box(doc, 'Internal use only — not for clients. Customise [BRACKETED TEXT] to match your tools and workflow.',
               label='INTERNAL DOCUMENT')

    section_num_label(doc, 1, 'SOP — Client Onboarding')
    body(doc, 'Complete these steps for every new client before the first monthly close. Sign off each step.')
    consulting_table(doc,
        ['#', 'Action', 'Owner', 'Deadline'],
        [
            ['1', 'Confirm signed engagement agreement and initial payment received', '[OWNER]', 'Before kickoff'],
            ['2', 'Create client folder in [SYSTEM] with standard subfolder structure', '[OWNER]', 'Day 1'],
            ['3', 'Create client record in Notion with all profile data from intake pack', '[OWNER]', 'Day 1'],
            ['4', 'Set up recurring tasks in [PROJECT TOOL] for monthly close cadence', '[OWNER]', 'Day 2'],
            ['5', 'Request secure accountant / user access to bookkeeping software', '[OWNER]', 'Day 2'],
            ['6', 'Request required source documents via secure portal', '[OWNER]', 'Day 2'],
            ['7', 'Capture entity type, fiscal year, accounting basis, integrations, payroll, taxes', '[OWNER]', 'Kickoff call'],
            ['8', 'Review opening balances and last fully reconciled period', '[OWNER]', 'Week 1'],
            ['9', 'Document known issues, cleanup scope, deadlines, and responsibilities in writing', '[OWNER]', 'Week 1'],
            ['10', 'Run kickoff call and send written action summary within 24 hours', '[OWNER]', 'Week 1'],
        ],
        col_widths_cm=[1.5, 9, 3, 4]
    )

    section_num_label(doc, 2, 'Monthly Close Checklist')
    consulting_table(doc,
        ['Step', 'Control Point', 'Done'],
        [
            ['1', 'Confirm all bank, card, loan, payroll, and processor data is available', '[ ]'],
            ['2', 'Import / sync transactions; investigate duplicates or failed feeds', '[ ]'],
            ['3', 'Categorise all transactions; resolve uncategorised / suspense items', '[ ]'],
            ['4', 'Reconcile every bank and credit-card account to statements', '[ ]'],
            ['5', 'Reconcile loans, payroll liabilities, sales-tax/VAT, and clearing accounts', '[ ]'],
            ['6', 'Review accounts receivable, payable, negative balances, and stale items', '[ ]'],
            ['7', 'Record approved accruals, prepayments, depreciation, and adjustments within scope', '[ ]'],
            ['8', 'Compare current month with prior month and budget; document material variances', '[ ]'],
            ['9', 'Run balance-sheet integrity and reasonableness checks', '[ ]'],
            ['10', 'Prepare consolidated question list and obtain documented responses from client', '[ ]'],
            ['11', 'Finalise P&L, balance sheet, cash summary, and all agreed reports', '[ ]'],
            ['12', 'Complete reviewer sign-off, lock or close period, and deliver to client portal', '[ ]'],
        ],
        col_widths_cm=[1.5, 14, 2]
    )

    section_num_label(doc, 3, 'Tax Document Collection Checklist')
    body(doc, 'Use at year-end or when preparing the annual bookkeeping package for the tax preparer.')
    consulting_table(doc,
        ['Category', 'Documents Required'],
        [
            ['Income', 'Sales summaries, invoices, merchant reports, platform statements, interest income'],
            ['Banking', 'Year-end bank and credit-card statements, final reconciliations for all accounts'],
            ['Payroll', 'Annual payroll summary, W-2 / 1099 or local equivalent, payroll tax filings'],
            ['Expenses', 'Major receipts, insurance, rent, professional fees, travel, vehicle records'],
            ['Assets & Debt', 'Asset purchases/disposals with dates/amounts, year-end loan statements'],
            ['Tax & Compliance', 'Prior-year return, estimated payments, notices, sales-tax/VAT filings'],
            ['Owner Activity', 'All contributions, draws, distributions, shareholder/partner transactions'],
        ],
        col_widths_cm=[3.5, 14.5]
    )
    notice_box(doc, 'Document collection is not tax advice. Confirm the final list and filing deadlines with the client\'s qualified tax professional.',
               label='SCOPE REMINDER', amber=True)

    section_num_label(doc, 4, 'Quality Control Review')
    body(doc, 'Complete before delivering any reports to any client. Both bookkeeper and reviewer must sign off.')
    consulting_table(doc,
        ['QC Check', 'Verified By', 'Done'],
        [
            ['All statement balances agree to the ledger', '', '[ ]'],
            ['No unexplained suspense or uncategorised balances remaining', '', '[ ]'],
            ['Opening balances and retained earnings are understood and documented', '', '[ ]'],
            ['Negative assets / liabilities and unusual balances investigated and documented', '', '[ ]'],
            ['Payroll, loans, sales-tax/VAT, and processor clearing fully reconciled', '', '[ ]'],
            ['All material variances have documented explanations', '', '[ ]'],
            ['Reports use correct period, basis, entity, and comparison column', '', '[ ]'],
            ['All questions, judgments, and client approvals are documented in writing', '', '[ ]'],
            ['Period is locked or closed in the software after review sign-off', '', '[ ]'],
            ['Reports delivered to client portal — not by ordinary email', '', '[ ]'],
        ],
        col_widths_cm=[11.5, 4, 2]
    )

    save(doc, f'{OUT}/04-Operations-Library/Bookkeeping-SOPs-and-Checklists-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 7. CLIENT COMMUNICATION SCRIPTS
# ══════════════════════════════════════════════════════════════════════════════

def build_scripts():
    doc = new_doc()
    add_cover(doc,
              ['Client Communication', 'Scripts'],
              'Ready-to-use messages for every stage of the client lifecycle',
              '04  —  OPERATIONS LIBRARY',
              [('Document type', 'Internal Reference'), ('Scripts included', '10')])
    add_header_footer(doc, 'Client Communication Scripts')

    notice_box(doc, 'Internal reference — not for direct forwarding. Customise [BRACKETED TEXT] before sending each message.',
               label='CUSTOMISE BEFORE SENDING', amber=True)

    scripts = [
        ('01', 'Inquiry Response', 'Email', 'Next step for your bookkeeping inquiry',
         'Hi [NAME],\n\nThank you for reaching out. To understand whether we are a good fit, I have a few quick questions:\n\n→  Entity type and jurisdiction\n→  Current bookkeeping software\n→  Number of bank and credit-card accounts\n→  Average monthly transaction volume\n→  Payroll, sales tax/VAT, or multi-entity requirements\n→  Known backlogs or issues with current books\n→  Reporting needs (P&L, cash flow, custom)\n\nYou can reply here or complete the intake form: [LINK]\n\n[PRACTICE NAME]'),
        ('02', 'Diagnostic Booking', 'Email', 'Bookkeeping diagnostic confirmed — [DATE]',
         'Hi [NAME],\n\nYour diagnostic call is confirmed for [DATE] at [TIME] via [PLATFORM].\n\nWe will review your current system, last reconciled month, volume, known issues, and reporting goals.\n\nPlease securely upload or share before the call: [LIST OF DOCUMENTS]\n\nJoin link: [LINK]\n\n[PRACTICE NAME]'),
        ('03', 'Proposal Follow-Up', 'Email', 'Bookkeeping proposal — [COMPANY]',
         'Hi [NAME],\n\nFollowing up on the proposal sent [DATE] for [COMPANY]. It addresses [PRIMARY ISSUE] with a recommended scope of [SUMMARY] at €[AMOUNT] per month, assuming an engagement start of [DATE].\n\nHappy to answer questions before [DECISION DATE]. Book a call here: [LINK]\n\n[PRACTICE NAME]'),
        ('04', 'Welcome & Onboarding', 'Email', 'Welcome — your bookkeeping onboarding steps',
         'Hi [NAME],\n\nWelcome — we are glad to be working with you. Three steps to get started:\n\n01  Complete the intake form: [LINK]\n02  Grant bookkeeping software access (instructions attached)\n03  Upload requested documents to your portal: [LINK]\n\nPlease complete steps 01 and 02 by [DATE]. Your kickoff call is [DATE/TIME]: [LINK]\n\n[PRACTICE NAME]'),
        ('05', 'Missing Documents', 'Email or Portal', 'Documents needed — [MONTH] close',
         'Hi [NAME],\n\nTo complete the [MONTH] close on schedule, we still need:\n\n[LIST SPECIFIC MISSING ITEMS]\n\nPlease upload to your portal by [DATE]: [LINK]\n\nIf not received by [DATE], report delivery may move from [ORIGINAL DATE] to [REVISED DATE].\n\n[PRACTICE NAME]'),
        ('06', 'Transaction Questions', 'Email or Portal', '[MONTH] bookkeeping questions',
         'Hi [NAME],\n\nThe [MONTH] question list is ready at [LINK]. Please respond by [DATE] to keep the close on schedule.\n\nWhen answering — if a transaction is personal, reimbursable, or owner-related, note that. If unclear, add context rather than guessing the account.\n\n[PRACTICE NAME]'),
        ('07', 'Close Complete', 'Email or Portal', '[MONTH] books are closed',
         'Hi [NAME],\n\nThe [MONTH] books are complete. Your reports are at [LINK].\n\nKey items this month:\n→  [FINANCIAL INSIGHT 1]\n→  [FINANCIAL INSIGHT 2]\n→  [ACTION REQUIRED]\n\nPlease confirm there are no material events after month-end that may affect the records.\n\nNext close deadline: [DATE]\n\n[PRACTICE NAME]'),
        ('08', 'Year-End Handoff', 'Email', 'Year-end bookkeeping package — [COMPANY]',
         'Hi [NAME],\n\nThe year-end bookkeeping package for [COMPANY] ([FISCAL YEAR]) is ready in your portal: [LINK]\n\nThe package includes: final P&L, final balance sheet, reconciliation summaries, and [OTHER REPORTS].\n\nOpen items and bookkeeping judgments are documented at [LINK]. Please send proposed adjusting entries through the secure portal — not by email.\n\n[PRACTICE NAME]'),
        ('09', 'Overdue Invoice', 'Email', 'Invoice [NUMBER] — payment reminder',
         'Hi [NAME],\n\nInvoice [NUMBER] for €[AMOUNT] (service period [PERIOD]) was due [DATE] and remains outstanding.\n\nPayment options: [LINK / INSTRUCTIONS]\n\nUnder our engagement agreement, work may be paused if a balance remains overdue beyond [X] days. Please reach out if you have any questions.\n\n[PRACTICE NAME]'),
        ('10', 'Scope Change Approval', 'Email', 'Approval needed — scope change for [COMPANY]',
         'Hi [NAME],\n\nActual volume or complexity for [MONTH] differs from the proposal because: [SPECIFIC REASON].\n\nAdditional work required: [DESCRIPTION]\nRevised fee: €[AMOUNT] — [BILLING TERMS]\n\nThis work will not proceed without your approval. Please reply "Approved" or ask any questions before we continue.\n\n[PRACTICE NAME]'),
    ]

    for num, title, channel, subject, body_text in scripts:
        section_num_label(doc, int(num), title)

        # Meta row
        meta_t = doc.add_table(rows=1, cols=2)
        meta_t.alignment = WD_TABLE_ALIGNMENT.CENTER
        _remove_borders(meta_t)
        lc = meta_t.cell(0, 0)
        rc = meta_t.cell(0, 1)
        lc.width = Cm(9)
        _cell_margins(lc, 40, 40, 0, 60)
        lp = lc.paragraphs[0]
        lr = lp.add_run(f'Channel: {channel}')
        _font(lr, 'Inter', 8.5, color=MUTED)

        _cell_margins(rc, 40, 40, 60, 0)
        rp = rc.paragraphs[0]
        rr = rp.add_run(f'Subject line: {subject}')
        _font(rr, 'Inter', 8.5, bold=True, color=INK)
        rp.alignment = WD_ALIGN_PARAGRAPH.LEFT

        doc.add_paragraph()

        # Script body as notice box
        bt = doc.add_table(rows=1, cols=1)
        bt.alignment = WD_TABLE_ALIGNMENT.CENTER
        bc = bt.cell(0, 0)
        _set_cell_bg(bc, SOFT_BG)
        _cell_margins(bc, top=140, bottom=140, left=180, right=180)
        _set_cell_borders(bc, ['left'], TEAL, 14)
        _set_cell_borders_right_top_bottom(bc)

        first = True
        for line in body_text.split('\n'):
            if first:
                bp = bc.paragraphs[0]
                first = False
            else:
                bp = bc.add_paragraph()
            br = bp.add_run(line)
            _font(br, 'Inter', 8.5, color=INK)
            _para_spacing(bp, 0, 2)

        doc.add_paragraph()

    save(doc, f'{OUT}/04-Operations-Library/Client-Communication-Scripts-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 8. ANNUAL TAX PREP CHECKLIST
# ══════════════════════════════════════════════════════════════════════════════

def build_tax_prep():
    doc = new_doc()
    add_cover(doc,
              ['Annual Tax Prep', 'Checklist'],
              'Year-end document preparation — 4-phase guide for bookkeepers',
              '04  —  OPERATIONS LIBRARY',
              [('Document type', 'Operational Checklist'), ('Phases', '4')])
    add_header_footer(doc, 'Annual Tax Prep Checklist')

    notice_box(doc, 'This checklist supports year-end bookkeeping package preparation only. It is not tax advice.',
               label='SCOPE NOTICE')

    section_num_label(doc, 0, 'Engagement Details')
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
        col_widths_cm=[5.5, 12.5]
    )

    section_num_label(doc, 1, 'Phase 1 — Final Month Close')
    body(doc, 'Complete the standard monthly close for the final month of the fiscal year before beginning the tax package.')
    consulting_table(doc,
        ['Task', 'Done', 'Notes'],
        [
            ['Final month close completed per monthly close checklist', '[ ]', ''],
            ['All bank and credit-card accounts reconciled to year-end statements', '[ ]', ''],
            ['All loan accounts reconciled to year-end statements', '[ ]', ''],
            ['Payroll liabilities reconciled to payroll year-end reports', '[ ]', ''],
            ['Sales-tax / VAT accounts reconciled to filings', '[ ]', ''],
            ['Accounts receivable ageing reviewed and confirmed', '[ ]', ''],
            ['Accounts payable ageing reviewed and confirmed', '[ ]', ''],
            ['All suspense and clearing accounts at zero or fully documented', '[ ]', ''],
        ],
        col_widths_cm=[11, 1.5, 5.5]
    )

    section_num_label(doc, 2, 'Phase 2 — Year-End Adjustments')
    consulting_table(doc,
        ['Adjustment Type', 'Done', 'Notes'],
        [
            ['Depreciation / amortisation recorded (within scope)', '[ ]', ''],
            ['Prepaid expenses adjusted to correct period', '[ ]', ''],
            ['Accrued revenue or expenses recorded (within scope)', '[ ]', ''],
            ['Owner draw and contribution accounts reviewed', '[ ]', ''],
            ['Loans to / from owners fully documented', '[ ]', ''],
            ['Inventory count reconciled to ledger (if applicable)', '[ ]', ''],
            ['Prior-year adjusting entries from tax preparer posted', '[ ]', ''],
        ],
        col_widths_cm=[11, 1.5, 5.5]
    )

    section_num_label(doc, 3, 'Phase 3 — Document Collection')
    consulting_table(doc,
        ['Category', 'Documents Required', 'Received', 'Notes'],
        [
            ['Income', 'All sales reports, merchant statements, platform reports, interest income', '[ ]', ''],
            ['Banking', 'Year-end bank and credit-card statements for all accounts', '[ ]', ''],
            ['Payroll', 'Annual payroll summary, W-2/1099 or equivalent, payroll tax filings', '[ ]', ''],
            ['Major Expenses', 'Rent, insurance, professional fees, travel, vehicle records', '[ ]', ''],
            ['Fixed Assets', 'Asset purchases and disposals with dates and amounts', '[ ]', ''],
            ['Loans & Financing', 'Year-end loan statements, amortisation schedules', '[ ]', ''],
            ['Tax & Compliance', 'Prior-year return, estimated payments, notices, VAT/sales-tax filings', '[ ]', ''],
            ['Owner Activity', 'Contributions, draws, distributions, shareholder/partner transactions', '[ ]', ''],
        ],
        col_widths_cm=[3.5, 7.5, 1.5, 5.5]
    )

    section_num_label(doc, 4, 'Phase 4 — Package Assembly')
    consulting_table(doc,
        ['Report / Item', 'Format', 'Done', 'Notes'],
        [
            ['Annual Profit & Loss (full year)', 'PDF', '[ ]', ''],
            ['Annual Balance Sheet (year-end)', 'PDF', '[ ]', ''],
            ['Cash Flow Statement (if applicable)', 'PDF', '[ ]', ''],
            ['Monthly P&L comparison (all 12 months)', 'PDF or Excel', '[ ]', ''],
            ['Bank reconciliation summaries', 'PDF', '[ ]', ''],
            ['Trial balance (year-end)', 'Excel or PDF', '[ ]', ''],
            ['Open items and bookkeeping judgment log', 'PDF or Notes', '[ ]', ''],
            ['Chart of accounts (year-end)', 'PDF', '[ ]', ''],
        ],
        col_widths_cm=[8, 3.5, 1.5, 5]
    )

    notice_box(doc,
        'Upload the completed package to the client\'s secure portal and notify the tax preparer '
        'through the appropriate channel. Do not email sensitive financial reports. '
        'The tax preparer is responsible for all tax judgments and filings.',
        label='DELIVERY AND SCOPE NOTICE', amber=True)

    save(doc, f'{OUT}/04-Operations-Library/Annual-Tax-Prep-Checklist-v2.docx')


if __name__ == '__main__':
    print('Building consulting-grade DOCX files...')
    build_start_here()
    build_service_guide()
    build_intake_pack()
    build_proposal()
    build_engagement_agreement()
    build_sops()
    build_scripts()
    build_tax_prep()
    print('All DOCX files done.')
