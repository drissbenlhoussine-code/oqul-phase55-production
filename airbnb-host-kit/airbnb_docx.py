"""
NOVAOPS — Airbnb Host Starter Kit
Professional Host Operating System — DOCX Builder
8 consulting-grade documents for Airbnb hosts
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

BASE = '/home/user/oqul-phase55-production/airbnb-host-kit/output/Airbnb-Host-Starter-Kit'

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
LIGHT_T = RGBColor(0xCC, 0xFB, 0xF1)
SLATE   = RGBColor(0x94, 0xA3, 0xB8)
GREEN   = RGBColor(0x16, 0xA3, 0x4A)
GREEN_L = RGBColor(0xDC, 0xFC, 0xE7)
RED_L   = RGBColor(0xFE, 0xE2, 0xE2)


def hex3(rgb):
    return f'{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}'

def _set_cell_bg(cell, rgb):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex3(rgb))
    ex = tcPr.find(qn('w:shd'))
    if ex is not None: tcPr.remove(ex)
    tcPr.append(shd)

def _set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for side, val in [('top',top),('bottom',bottom),('left',left),('right',right),('insideH',None),('insideV',None)]:
        b = OxmlElement(f'w:{side}')
        if val:
            color, size = val
            b.set(qn('w:val'), 'single')
            b.set(qn('w:sz'), str(int(size*8)))
            b.set(qn('w:color'), hex3(color))
        else:
            b.set(qn('w:val'), 'none')
            b.set(qn('w:sz'), '0')
            b.set(qn('w:color'), 'auto')
        tcBorders.append(b)
    ex = tcPr.find(qn('w:tcBorders'))
    if ex is not None: tcPr.remove(ex)
    tcPr.append(tcBorders)

def _border_all(cell, color=RULE, size=0.5):
    _set_cell_borders(cell, top=(color,size), bottom=(color,size), left=(color,size), right=(color,size))

def _remove_borders(table):
    for row in table.rows:
        for cell in row.cells:
            _set_cell_borders(cell)

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
    if ex is not None: tcPr.remove(ex)
    tcPr.append(tcMar)

def _cell_valign(cell, align='center'):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    vAlign = OxmlElement('w:vAlign')
    vAlign.set(qn('w:val'), align)
    ex = tcPr.find(qn('w:vAlign'))
    if ex is not None: tcPr.remove(ex)
    tcPr.append(vAlign)

def _col_widths(table, widths_cm):
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            if i < len(widths_cm):
                tc = cell._tc
                tcPr = tc.get_or_add_tcPr()
                tcW = OxmlElement('w:tcW')
                tcW.set(qn('w:w'), str(int(widths_cm[i]*567)))
                tcW.set(qn('w:type'), 'dxa')
                ex = tcPr.find(qn('w:tcW'))
                if ex is not None: tcPr.remove(ex)
                tcPr.append(tcW)

def _no_space_before(para):
    pPr = para._p.get_or_add_pPr()
    sb = OxmlElement('w:spacing')
    sb.set(qn('w:before'), '0')
    ex = pPr.find(qn('w:spacing'))
    if ex is not None: pPr.remove(ex)
    pPr.append(sb)

def new_doc():
    doc = Document()
    for sec in doc.sections:
        sec.top_margin    = Cm(1.8)
        sec.bottom_margin = Cm(1.8)
        sec.left_margin   = Cm(2.0)
        sec.right_margin  = Cm(2.0)
    doc.styles['Normal'].font.name = 'Calibri'
    doc.styles['Normal'].font.size = Pt(10)
    doc.styles['Normal'].font.color.rgb = INK
    return doc

def page_break(doc):
    p = doc.add_paragraph()
    run = p.add_run()
    br = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    run._r.append(br)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(0)

def add_header_footer(doc, title):
    for section in doc.sections:
        header = section.header
        header.is_linked_to_previous = False
        hp = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        hp.clear()
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r1 = hp.add_run('NOVAOPS')
        r1.bold = True; r1.font.size = Pt(7); r1.font.color.rgb = TEAL
        r2 = hp.add_run(f'  ·  Airbnb Host Starter Kit  ·  {title}')
        r2.font.size = Pt(7); r2.font.color.rgb = MUTED

        footer = section.footer
        footer.is_linked_to_previous = False
        fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        fp.clear()
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        rf = fp.add_run('© 2025 NovaOps  ·  Airbnb Host Starter Kit  ·  Commercial Use License')
        rf.font.size = Pt(7); rf.font.color.rgb = MUTED

# ── Cover page ────────────────────────────────────────────────────────────────

def three_strip_cover(doc, title, subtitle, tagline, doc_label=''):
    # Teal top strip
    t1 = doc.add_table(rows=1, cols=1)
    t1.alignment = WD_TABLE_ALIGNMENT.LEFT
    c1 = t1.rows[0].cells[0]
    _set_cell_bg(c1, TEAL)
    _remove_borders(t1)
    _cell_margins(c1, top=200, bottom=200, left=300, right=300)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r1 = p1.add_run('NOVAOPS  ·  AIRBNB HOST STARTER KIT')
    r1.font.size = Pt(8); r1.font.color.rgb = LIGHT_T; r1.bold = True

    # Dark body
    t2 = doc.add_table(rows=1, cols=1)
    t2.alignment = WD_TABLE_ALIGNMENT.LEFT
    c2 = t2.rows[0].cells[0]
    _set_cell_bg(c2, DARK)
    _remove_borders(t2)
    _cell_margins(c2, top=500, bottom=500, left=300, right=300)
    # doc label
    if doc_label:
        pl = c2.add_paragraph()
        pl.alignment = WD_ALIGN_PARAGRAPH.LEFT
        rl = pl.add_run(doc_label)
        rl.font.size = Pt(9); rl.font.color.rgb = SLATE; rl.bold = True
        pl.paragraph_format.space_before = Pt(0)
        pl.paragraph_format.space_after  = Pt(4)
    # title
    for line in title.split('\n'):
        pt = c2.add_paragraph()
        pt.alignment = WD_ALIGN_PARAGRAPH.LEFT
        rt = pt.add_run(line)
        rt.font.size = Pt(28); rt.font.color.rgb = WHITE; rt.bold = True
        pt.paragraph_format.space_before = Pt(0)
        pt.paragraph_format.space_after  = Pt(2)
    # subtitle
    ps = c2.add_paragraph()
    ps.alignment = WD_ALIGN_PARAGRAPH.LEFT
    rs = ps.add_run(subtitle)
    rs.font.size = Pt(13); rs.font.color.rgb = LIGHT_T
    ps.paragraph_format.space_before = Pt(8)
    ps.paragraph_format.space_after  = Pt(4)
    # tagline
    pg = c2.add_paragraph()
    pg.alignment = WD_ALIGN_PARAGRAPH.LEFT
    rg = pg.add_run(tagline)
    rg.font.size = Pt(10); rg.font.color.rgb = SLATE
    pg.paragraph_format.space_before = Pt(0)

    # Amber bottom strip
    t3 = doc.add_table(rows=1, cols=1)
    t3.alignment = WD_TABLE_ALIGNMENT.LEFT
    c3 = t3.rows[0].cells[0]
    _set_cell_bg(c3, AMBER)
    _remove_borders(t3)
    _cell_margins(c3, top=200, bottom=200, left=300, right=300)
    p3 = c3.paragraphs[0]
    p3.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r3 = p3.add_run('PROFESSIONAL HOST OPERATING SYSTEM  ·  v1.0  ·  INSTANT DOWNLOAD')
    r3.font.size = Pt(8); r3.font.color.rgb = WHITE; r3.bold = True

    page_break(doc)

def section_header(doc, num, title, color=TEAL):
    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    _remove_borders(t)
    cn = t.rows[0].cells[0]
    ct = t.rows[0].cells[1]
    _set_cell_bg(cn, color)
    _set_cell_bg(ct, DARK)
    _cell_margins(cn, top=120, bottom=120, left=160, right=160)
    _cell_margins(ct, top=120, bottom=120, left=200, right=200)
    _cell_valign(cn, 'center'); _cell_valign(ct, 'center')
    pn = cn.paragraphs[0]
    pn.alignment = WD_ALIGN_PARAGRAPH.CENTER
    rn = pn.add_run(str(num).zfill(2))
    rn.font.size = Pt(16); rn.font.color.rgb = WHITE; rn.bold = True
    pt = ct.paragraphs[0]
    pt.alignment = WD_ALIGN_PARAGRAPH.LEFT
    rt = pt.add_run(title.upper())
    rt.font.size = Pt(12); rt.font.color.rgb = WHITE; rt.bold = True
    tc_num = cn._tc
    tcPr_n = tc_num.get_or_add_tcPr()
    tcW_n = OxmlElement('w:tcW')
    tcW_n.set(qn('w:w'), str(int(1.0*567)))
    tcW_n.set(qn('w:type'), 'dxa')
    ex = tcPr_n.find(qn('w:tcW'))
    if ex is not None: tcPr_n.remove(ex)
    tcPr_n.append(tcW_n)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def heading2(doc, text, color=TEAL):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(12); r.font.color.rgb = color
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after  = Pt(4)
    return p

def heading3(doc, text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = INK
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after  = Pt(3)
    return p

def body(doc, text, indent=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(4)
    if indent:
        p.paragraph_format.left_indent = Cm(0.6)
    r = p.add_run(text)
    r.font.size = Pt(10); r.font.color.rgb = INK
    return p

def bullet(doc, text, check=False, indent_cm=0.6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after  = Pt(1)
    p.paragraph_format.left_indent  = Cm(indent_cm)
    icon = '☐ ' if check else '→ '
    r1 = p.add_run(icon)
    r1.font.color.rgb = TEAL; r1.font.size = Pt(10)
    r2 = p.add_run(text)
    r2.font.size = Pt(10); r2.font.color.rgb = INK
    return p

def check_item(doc, text, done=False, indent_cm=0.6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after  = Pt(1)
    p.paragraph_format.left_indent  = Cm(indent_cm)
    icon = '☐ ' if not done else '✓ '
    r1 = p.add_run(icon)
    r1.font.color.rgb = TEAL; r1.font.size = Pt(10)
    r2 = p.add_run(text)
    r2.font.size = Pt(10); r2.font.color.rgb = INK
    return p

def stat_cards(doc, cards):
    """cards = list of (label, value, note)"""
    n = len(cards)
    t = doc.add_table(rows=1, cols=n)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    _remove_borders(t)
    for i, (label, value, note) in enumerate(cards):
        cell = t.rows[0].cells[i]
        _set_cell_bg(cell, TEAL_10)
        _set_cell_borders(cell, top=(TEAL,2), bottom=(RULE,0.5), left=(RULE,0.5), right=(RULE,0.5))
        _cell_margins(cell, top=120, bottom=100, left=150, right=150)
        p_lbl = cell.add_paragraph()
        _no_space_before(p_lbl)
        r_lbl = p_lbl.add_run(label.upper())
        r_lbl.font.size = Pt(7); r_lbl.font.color.rgb = MUTED; r_lbl.bold = True
        p_val = cell.add_paragraph()
        _no_space_before(p_val)
        r_val = p_val.add_run(value)
        r_val.font.size = Pt(18); r_val.font.color.rgb = TEAL; r_val.bold = True
        p_note = cell.add_paragraph()
        _no_space_before(p_note)
        r_note = p_note.add_run(note)
        r_note.font.size = Pt(8); r_note.font.color.rgb = MUTED
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

def info_box(doc, text, color=TEAL_10, border_color=TEAL):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    _remove_borders(t)
    c = t.rows[0].cells[0]
    _set_cell_bg(c, color)
    _set_cell_borders(c, left=(border_color, 3))
    _cell_margins(c, top=120, bottom=120, left=200, right=200)
    p = c.paragraphs[0]
    r = p.add_run(text)
    r.font.size = Pt(10); r.font.color.rgb = INK
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def amber_box(doc, text):
    info_box(doc, text, color=AMB_10, border_color=AMBER)

def process_steps(doc, steps):
    """steps = list of (number, title, description)"""
    n = len(steps)
    t = doc.add_table(rows=1, cols=n)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    _remove_borders(t)
    for i, (num, title, desc) in enumerate(steps):
        cell = t.rows[0].cells[i]
        _set_cell_bg(cell, TEAL_10 if i % 2 == 0 else SOFT_BG)
        _border_all(cell, RULE, 0.5)
        _cell_margins(cell, top=140, bottom=140, left=140, right=140)
        _cell_valign(cell, 'top')
        p_num = cell.add_paragraph()
        _no_space_before(p_num)
        r_num = p_num.add_run(str(num).zfill(2))
        r_num.font.size = Pt(20); r_num.font.color.rgb = TEAL; r_num.bold = True
        p_t = cell.add_paragraph()
        _no_space_before(p_t)
        r_t = p_t.add_run(title)
        r_t.font.size = Pt(10); r_t.font.color.rgb = INK; r_t.bold = True
        p_d = cell.add_paragraph()
        _no_space_before(p_d)
        r_d = p_d.add_run(desc)
        r_d.font.size = Pt(9); r_d.font.color.rgb = MUTED
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

def two_col_table(doc, headers, rows, col_widths_cm=None):
    n_cols = len(headers)
    t = doc.add_table(rows=1+len(rows), cols=n_cols)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    _remove_borders(t)
    # Header row
    for i, h in enumerate(headers):
        cell = t.rows[0].cells[i]
        _set_cell_bg(cell, DARK)
        _border_all(cell, DARK, 0.5)
        _cell_margins(cell, top=100, bottom=100, left=140, right=140)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h.upper())
        r.font.size = Pt(8); r.font.color.rgb = WHITE; r.bold = True
    # Data rows
    for ri, row in enumerate(rows):
        bg = SOFT_BG if ri % 2 == 0 else WHITE
        for ci, val in enumerate(row):
            cell = t.rows[ri+1].cells[ci]
            _set_cell_bg(cell, bg)
            _set_cell_borders(cell, bottom=(RULE,0.5))
            _cell_margins(cell, top=80, bottom=80, left=140, right=140)
            p = cell.paragraphs[0]
            r = p.add_run(str(val))
            r.font.size = Pt(9.5); r.font.color.rgb = INK
    if col_widths_cm:
        _col_widths(t, col_widths_cm)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def message_template_box(doc, label, subject, body_text):
    """Styled box for a message template"""
    # Label
    p_lbl = doc.add_paragraph()
    r_lbl = p_lbl.add_run(f'  {label}  ')
    r_lbl.bold = True; r_lbl.font.size = Pt(9); r_lbl.font.color.rgb = WHITE
    # Simulate colored label by using a table
    t_lbl = doc.add_table(rows=1, cols=2)
    t_lbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    _remove_borders(t_lbl)
    c_lbl = t_lbl.rows[0].cells[0]
    c_rest = t_lbl.rows[0].cells[1]
    _set_cell_bg(c_lbl, TEAL)
    _cell_margins(c_lbl, top=80, bottom=80, left=140, right=140)
    p_ll = c_lbl.paragraphs[0]
    r_ll = p_ll.add_run(label.upper())
    r_ll.bold = True; r_ll.font.size = Pt(8); r_ll.font.color.rgb = WHITE
    _set_cell_bg(c_rest, SOFT_BG)
    _cell_margins(c_rest, top=80, bottom=80, left=140, right=140)
    p_rl = c_rest.paragraphs[0]
    r_rl = p_rl.add_run(subject)
    r_rl.bold = True; r_rl.font.size = Pt(9.5); r_rl.font.color.rgb = INK
    tc_lbl = c_lbl._tc; tcPr = tc_lbl.get_or_add_tcPr()
    tcW = OxmlElement('w:tcW'); tcW.set(qn('w:w'), str(int(3.5*567))); tcW.set(qn('w:type'), 'dxa')
    ex = tcPr.find(qn('w:tcW'))
    if ex is not None: tcPr.remove(ex)
    tcPr.append(tcW)

    # Body box
    t_body = doc.add_table(rows=1, cols=1)
    t_body.alignment = WD_TABLE_ALIGNMENT.LEFT
    _remove_borders(t_body)
    c_body = t_body.rows[0].cells[0]
    _set_cell_bg(c_body, WHITE)
    _set_cell_borders(c_body, top=(RULE,0.5), bottom=(RULE,0.5), left=(RULE,0.5), right=(RULE,0.5))
    _cell_margins(c_body, top=140, bottom=140, left=200, right=200)
    for line in body_text.strip().split('\n'):
        pb = c_body.add_paragraph()
        pb.paragraph_format.space_before = Pt(0)
        pb.paragraph_format.space_after  = Pt(3)
        rb = pb.add_run(line)
        rb.font.size = Pt(9.5); rb.font.color.rgb = INK
    doc.add_paragraph().paragraph_format.space_after = Pt(10)


# ==============================================================================
# DOCUMENT 1 — QUICK START GUIDE
# ==============================================================================

def build_quick_start():
    doc = new_doc()
    add_header_footer(doc, 'Quick Start Guide')
    three_strip_cover(doc,
        'Quick Start\nGuide',
        'Your Professional Host Operating System',
        'Read this first. Complete setup in under 7 days.',
        'DOCUMENT 01 OF 08')

    stat_cards(doc, [
        ('Documents Included', '8', 'Guides, templates & SOPs'),
        ('Excel Sheets', '8', 'Operations dashboard'),
        ('Time to Set Up', '7 Days', 'Phased launch plan'),
        ('Target Rating', '4.9 ★', 'With this system'),
    ])

    section_header(doc, 1, 'Welcome to Your Host Operating System')
    body(doc, 'This kit gives you the operational infrastructure of a professional short-term rental manager. Every document connects to another. Every workflow leads naturally to the next. You do not need to create anything from scratch — every asset is production-ready and immediately usable.')
    body(doc, 'The system is designed around three realities of professional hosting: guest experience must be consistent, operations must be systematised, and financial performance must be measurable. This kit delivers all three.')

    info_box(doc, 'How to use this kit: Read this guide first. Follow the 3-Phase Roadmap below. Customise [BRACKETED] fields with your property details. Your first guest can check in using this system within one week.')

    section_header(doc, 2, '3-Phase Launch Roadmap')

    heading2(doc, 'Phase 1 — Foundations  (Days 1–7)')
    body(doc, 'Build your operational base before your first booking arrives. This phase is non-negotiable — skipping it means dealing with every situation reactively instead of systematically.')

    steps1 = [
        ('1', 'Listing Setup', 'Apply the Listing Optimization Guide. Rewrite your title and description using the frameworks provided.'),
        ('2', 'Communication', 'Load the 15 message templates into your Airbnb saved messages. Customise [BRACKETS] for your property.'),
        ('3', 'Guest Experience', 'Customise the House Manual template. Print or share digitally with every guest at check-in.'),
        ('4', 'House Rules', 'Customise and publish the House Rules template on your Airbnb listing.'),
        ('5', 'Operations', 'Open the Host Operations Dashboard. Fill in your property details on the Dashboard sheet.'),
    ]
    process_steps(doc, steps1)

    check_item(doc, 'Listing title and description rewritten')
    check_item(doc, 'All 15 message templates loaded into Airbnb saved messages')
    check_item(doc, 'House Manual customised with your property details')
    check_item(doc, 'House Rules published on listing')
    check_item(doc, 'Operations Dashboard set up with property info')
    check_item(doc, 'Cleaning SOP shared with your cleaner')
    check_item(doc, 'Check-In SOP reviewed and ready')

    heading2(doc, 'Phase 2 — Optimise  (Days 8–30)')
    body(doc, 'With the foundation in place, shift focus to performance. Review your pricing, track your first bookings, and start collecting your first reviews systematically.')

    steps2 = [
        ('1', 'Pricing Review', 'Apply the Pricing Strategy Guide to set seasonal and dynamic pricing for the next 90 days.'),
        ('2', 'First Bookings', 'Log every booking in the Booking Tracker. Record revenue, cleaning costs and expenses.'),
        ('3', 'Review Strategy', 'After each checkout, apply the Review Strategy Guide. Request reviews using the provided template.'),
        ('4', 'Expense Tracking', 'Log all property expenses in the Expense Tracker. Set up your monthly categories.'),
        ('5', 'Feedback Loop', 'After 3–5 checkouts, review guest feedback. Adjust your House Manual if questions repeat.'),
    ]
    process_steps(doc, steps2)

    heading2(doc, 'Phase 3 — Automate  (Month 2+)')
    body(doc, 'Once operations run smoothly, focus on removing yourself from repetitive tasks. Automated messaging, streamlined cleaning handoffs, and regular financial reviews become your standard rhythm.')

    steps3 = [
        ('1', 'Automate Messages', 'Set up automated scheduled messages in Airbnb using your saved templates.'),
        ('2', 'Cleaner System', 'Brief your cleaner on the full Cleaning SOP. Create a shared checklist they sign off on each turn.'),
        ('3', 'Monthly Review', 'On the 1st of each month, complete the Monthly Host Review checklist (included in this guide).'),
        ('4', 'Pricing Rhythm', 'Every 4 weeks, review occupancy rate and adjust pricing for the next 30 days.'),
        ('5', 'Scale Planning', 'If occupancy exceeds 80%, consider adding a second property using the Growth Scaling section.'),
    ]
    process_steps(doc, steps3)

    section_header(doc, 3, 'Product Navigation — What Is in Each Folder')
    body(doc, 'Every folder in this kit has a specific purpose. Nothing is duplicated. Everything connects.')

    two_col_table(doc,
        ['Folder', 'Contents', 'When to Use'],
        [
            ['00-START-HERE', 'This Quick Start Guide', 'First. Before anything else.'],
            ['01-Listing-Optimization', 'Listing Guide + Pricing Strategy', 'Day 1–2. Improve your listing immediately.'],
            ['02-Guest-Communication', 'Message Templates + House Rules', 'Day 1–3. Load into Airbnb saved messages.'],
            ['03-Operations-Hub', 'Excel Dashboard + All Trackers', 'Day 1 onwards. Your operational command centre.'],
            ['04-Guest-Experience', 'House Manual Template', 'Before first guest. Customise once, reuse forever.'],
            ['05-SOP-Library', 'Check-In, Cleaning, Review SOPs', 'Train your team. Run every operation consistently.'],
            ['06-Growth-Scaling', 'Co-Host Agreement', 'When you are ready to add team members or properties.'],
        ],
        col_widths_cm=[4.5, 6.5, 6.5]
    )

    section_header(doc, 4, 'Key Performance Metrics')
    body(doc, 'Track these six metrics monthly using the Operations Dashboard. They tell you everything about listing health and income performance.')

    two_col_table(doc,
        ['Metric', 'How to Calculate', 'Target Benchmark'],
        [
            ['Occupancy Rate', 'Nights Booked ÷ Nights Available × 100', '65–80%'],
            ['Average Nightly Rate (ANR)', 'Total Revenue ÷ Nights Booked', 'Market + 10–15%'],
            ['RevPAR', 'ANR × Occupancy Rate ÷ 100', 'Improves monthly'],
            ['Net Profit Margin', '(Revenue – Expenses) ÷ Revenue × 100', '>40%'],
            ['Guest Rating', 'Average of all Airbnb reviews', '4.8 or above'],
            ['Review Conversion Rate', 'Reviews Received ÷ Checkouts × 100', '>75%'],
        ],
        col_widths_cm=[5.0, 6.5, 5.5]
    )

    section_header(doc, 5, 'Monthly Host Review Checklist')
    body(doc, 'Complete this review on the first working day of each month. It takes 20 minutes and keeps your operation running at full performance.')

    heading3(doc, 'Financial Review')
    check_item(doc, 'Total revenue for the month logged in Booking Tracker')
    check_item(doc, 'All expenses logged and categorised in Expense Tracker')
    check_item(doc, 'Net profit margin calculated and recorded')
    check_item(doc, 'Occupancy rate for the month calculated')
    check_item(doc, 'Average nightly rate compared to previous month')

    heading3(doc, 'Operations Review')
    check_item(doc, 'Review Tracker updated with all guest ratings')
    check_item(doc, 'Maintenance Log reviewed — all open issues assigned')
    check_item(doc, 'Cleaning performance reviewed — any issues flagged with cleaner')
    check_item(doc, 'Guest feedback reviewed — recurring complaints addressed')
    check_item(doc, 'Consumables stock checked and restocked if needed')

    heading3(doc, 'Listing & Pricing Review')
    check_item(doc, 'Pricing reviewed for next 30 days — seasonal adjustments made')
    check_item(doc, 'Competitor listings checked — ensure you remain competitive')
    check_item(doc, 'Listing photos reviewed — any outdated images updated')
    check_item(doc, 'Listing description reviewed — accuracy confirmed')

    amber_box(doc, 'Pro Tip: Set a recurring calendar reminder on the 1st of each month for your Host Review. Hosts who do monthly reviews consistently outperform those who only check in when problems arise.')

    path = f'{BASE}/00-START-HERE/00-Quick-Start-Guide.docx'
    doc.save(path)
    print(f'  ✓ 00-Quick-Start-Guide.docx')


# ==============================================================================
# DOCUMENT 2 — LISTING OPTIMIZATION GUIDE
# ==============================================================================

def build_listing_guide():
    doc = new_doc()
    add_header_footer(doc, 'Listing Optimization Guide')
    three_strip_cover(doc,
        'Listing\nOptimization\nGuide',
        'Title · Description · Photos · Amenities · Search Strategy',
        'Rank higher. Convert more. Earn more.',
        'DOCUMENT 02 OF 08')

    stat_cards(doc, [
        ('Title Length', '64 chars', 'Airbnb maximum'),
        ('Photo Minimum', '20 shots', 'For top search rank'),
        ('Description', '500 words', 'Optimal length'),
        ('First Impression', '3 seconds', 'Visitor decision window'),
    ])

    section_header(doc, 1, 'Title Formula — 64 Characters That Convert')
    body(doc, 'Your title is the first thing a potential guest reads. Airbnb allows 64 characters. The algorithm rewards titles that include location, property type, standout amenities, and guest-experience language.')

    info_box(doc, 'Title Formula:  [Property Type + Unique Selling Point] + [Location] + [Top Amenity 1] + [Top Amenity 2]')

    heading2(doc, 'Title Examples by Property Type')
    two_col_table(doc,
        ['Property Type', 'Example Title (High-Converting)'],
        [
            ['City Apartment', 'Modern Studio | City Centre | Fast WiFi + Netflix'],
            ['Beach Property', 'Beachfront Cottage | Sea Views | Private Garden + Parking'],
            ['Country House', 'Countryside Retreat | 3 Beds | Hot Tub + Wood Burner'],
            ['City Flat 2BR', 'Stylish 2BR | 5 Min Walk to Station | Workspace + Gym'],
            ['Luxury Villa', 'Luxury Villa | Pool + Chef\'s Kitchen | Sleeps 8'],
            ['Cosy Studio', 'Cosy Studio | Quiet Street | Superhost · Fast Check-In'],
        ],
        col_widths_cm=[5.0, 12.5]
    )

    heading2(doc, 'Title Optimisation Rules')
    bullet(doc, 'Lead with the property type (Studio, Flat, Cottage, Villa) — guests filter by type first')
    bullet(doc, 'Include the micro-location (City Centre, Seafront, Near Station) — not just the city name')
    bullet(doc, 'Use the pipe character | to separate feature groups — it reads cleanly on mobile')
    bullet(doc, 'Mention your top 2 amenities that command price premium (Pool, Hot Tub, Parking, Workspace)')
    bullet(doc, 'Avoid generic words: "Nice," "Great," "Lovely," "Beautiful" — guests cannot search for these')
    bullet(doc, 'Do not repeat the word "Airbnb" — the platform adds this automatically')
    bullet(doc, 'Update your title for peak seasons: add "Ski Season," "Summer," "Festive" for relevant months')

    section_header(doc, 2, 'Description Framework — The FEAT Method')
    body(doc, 'Your description should follow the FEAT structure: Feel → Experience → Amenities → Tips. Guests decide emotionally first. Lead with how the property feels, not with a list of rooms.')

    two_col_table(doc,
        ['Section', 'Purpose', 'Length', 'Example Opening'],
        [
            ['Feel', 'Emotional hook — why this place is special', '2–3 sentences', '"Step through the door and leave the city behind..."'],
            ['Experience', 'The guest journey — what they will actually do here', '3–4 sentences', '"Wake up to sea views, walk to the village in 5 minutes..."'],
            ['Amenities', 'Practical specifics — the things guests search for', '5–8 bullet points', '"→ Super-fast 200Mbps WiFi, ideal for remote work"'],
            ['Tips', 'Local knowledge that adds genuine value', '2–3 sentences', '"For the best local coffee, walk two minutes to The Arch..."'],
        ],
        col_widths_cm=[2.5, 5.0, 2.5, 7.5]
    )

    heading2(doc, 'High-Converting Amenity Language')
    body(doc, 'Use specific, searchable language when describing amenities. Vague descriptions reduce search visibility.')

    two_col_table(doc,
        ['Instead of This', 'Write This'],
        [
            ['Good WiFi', '200 Mbps fibre WiFi — tested and reliable for video calls'],
            ['Parking available', 'Private off-street parking for one vehicle — included'],
            ['Nice kitchen', 'Fully equipped kitchen: espresso machine, dishwasher, oven, microwave'],
            ['Smart TV', '65" Smart TV with Netflix, Prime Video and Disney+ (accounts included)'],
            ['Outdoor area', 'South-facing private garden with table, chairs and BBQ'],
            ['Near transport', '4-minute walk to Central Station — direct to airport in 20 min'],
            ['Baby-friendly', 'Travel cot, high chair and stair gate available on request'],
        ],
        col_widths_cm=[5.5, 12.0]
    )

    section_header(doc, 3, 'Photo Strategy — 20-Shot Blueprint')
    body(doc, 'Airbnb\'s algorithm boosts listings with 20+ professional photos. The cover photo determines click-through rate. Interior shots determine booking conversion. Follow this exact sequence.')

    two_col_table(doc,
        ['Shot #', 'Subject', 'Time of Day', 'Why It Matters'],
        [
            ['01', 'Cover — Living room or best room, wide angle', 'Natural daylight', 'Primary decision driver — must be magazine quality'],
            ['02', 'Living room — alternative angle', 'Daylight', 'Confirms space and comfort'],
            ['03', 'Kitchen — full view showing appliances', 'Daylight', 'Guests highly value kitchen quality'],
            ['04', 'Kitchen detail — coffee machine / appliances', 'Any', 'Signals quality of amenities'],
            ['05', 'Bedroom 1 — wide angle from doorway', 'Daylight', 'Sleep quality is top concern for most guests'],
            ['06', 'Bedroom 1 — headboard detail', 'Any', 'Reinforces quality of bedding'],
            ['07', 'Bedroom 2 (if applicable)', 'Daylight', 'Shows full sleeping capacity clearly'],
            ['08', 'Bathroom 1 — full width shot', 'Artificial light', 'Cleanliness and quality perception'],
            ['09', 'Bathroom detail — toiletries / towels staged', 'Any', 'Signals premium guest experience'],
            ['10', 'Dining area', 'Daylight', 'Group dynamics — important for 3+ guests'],
            ['11', 'Workspace / desk setup', 'Daylight', 'Critical for business and remote-work guests'],
            ['12', 'Outdoor space — wide angle', 'Golden hour', 'Aspirational — drives premium bookings'],
            ['13', 'Outdoor dining / BBQ area', 'Any', 'Increases perceived value significantly'],
            ['14', 'View from window or balcony', 'Golden hour', 'Location advantage visualised'],
            ['15', 'Hallway / entrance', 'Any', 'Sets arrival expectations'],
            ['16', 'Welcome setup: door mat, key, flowers', 'Any', 'Signals host care and attention to detail'],
            ['17', 'Smart TV / entertainment setup', 'Evening', 'Leisure appeal — evenings in'],
            ['18', 'Local area — café, beach, park within 5 min', 'Daylight', 'Contextualises location for guests'],
            ['19', 'Unique feature (fireplace, hot tub, view)', 'Best light', 'The thing guests remember and mention in reviews'],
            ['20', 'Property exterior / building frontage', 'Golden hour', 'Arrival experience and neighbourhood feel'],
        ],
        col_widths_cm=[1.5, 5.0, 3.0, 8.0]
    )

    section_header(doc, 4, 'Amenity Optimisation — Priority Matrix')
    body(doc, 'Add these amenities in priority order. Each tier adds measurable booking conversion impact. Tier 1 amenities are non-negotiable for consistent 4.9-star ratings.')

    two_col_table(doc,
        ['Tier', 'Amenity', 'Impact', 'Guest Expectation'],
        [
            ['TIER 1 — ESSENTIAL', 'Fast WiFi (100Mbps+)', 'Critical', 'Guests filter for this — no WiFi = no booking'],
            ['TIER 1 — ESSENTIAL', 'Dedicated workspace + monitor', 'High', 'Remote worker segment growing 40% annually'],
            ['TIER 1 — ESSENTIAL', 'Self check-in (lockbox/smart lock)', 'High', 'Flexibility is now a base expectation'],
            ['TIER 1 — ESSENTIAL', 'Full kitchen (espresso machine included)', 'High', 'Espresso machine specifically mentioned in reviews'],
            ['TIER 1 — ESSENTIAL', 'Fresh towels + toiletries (shampoo, conditioner, soap)', 'High', 'Hotel-standard = 5-star review trigger'],
            ['TIER 2 — HIGH VALUE', 'Smart TV with streaming accounts', 'Medium-High', 'Differentiator vs. bare-bones listings'],
            ['TIER 2 — HIGH VALUE', 'Blackout curtains in bedrooms', 'Medium-High', 'Sleep quality — mentioned frequently in reviews'],
            ['TIER 2 — HIGH VALUE', 'Free private parking', 'High (location dependent)', 'Commands 15–25% price premium in cities'],
            ['TIER 2 — HIGH VALUE', 'Iron + ironing board', 'Medium', 'Business travellers specifically check for this'],
            ['TIER 2 — HIGH VALUE', 'Hair dryer', 'Medium', 'Absence triggers 4-star ratings from some guests'],
            ['TIER 3 — PREMIUM', 'Hot tub / outdoor pool', 'Very High', 'Commands 30–50% price premium'],
            ['TIER 3 — PREMIUM', 'EV charging point', 'Growing', 'Differentiator now, essential in 3 years'],
            ['TIER 3 — PREMIUM', 'Baby/toddler equipment', 'Segment-specific', 'Opens family segment; families book longer stays'],
            ['TIER 3 — PREMIUM', 'Local welcome pack (coffee, wine, snacks)', 'High review impact', 'Single highest-mentioned item in 5-star reviews'],
        ],
        col_widths_cm=[3.5, 4.5, 2.5, 7.0]
    )

    section_header(doc, 5, 'Listing Audit Checklist')
    body(doc, 'Run this audit on your current listing before your next price adjustment. Check every item.')

    heading3(doc, 'Title & Search Visibility')
    check_item(doc, 'Title is exactly 64 characters (use all available space)')
    check_item(doc, 'Title includes property type, micro-location, and top 2 amenities')
    check_item(doc, 'No generic filler words: "Nice," "Lovely," "Great," "Beautiful"')
    check_item(doc, 'Title updated for current season if applicable')

    heading3(doc, 'Description Quality')
    check_item(doc, 'Opening paragraph creates emotional connection (not a list of rooms)')
    check_item(doc, 'FEAT structure followed: Feel → Experience → Amenities → Tips')
    check_item(doc, 'Amenities use specific, searchable language (not "good WiFi" but "200Mbps")')
    check_item(doc, 'Local tips section included with 2–3 genuine recommendations')
    check_item(doc, 'Description is 400–600 words (optimal for Airbnb algorithm)')

    heading3(doc, 'Photos')
    check_item(doc, 'Minimum 20 photos published')
    check_item(doc, 'Cover photo is the single best room in natural daylight')
    check_item(doc, 'All 20-shot blueprint positions covered')
    check_item(doc, 'No dark, blurry or cluttered photos in listing')
    check_item(doc, 'Photos show property at its best (staged, clean, good lighting)')

    heading3(doc, 'Pricing & Availability')
    check_item(doc, 'Pricing calendar updated for next 90 days')
    check_item(doc, 'Weekend premium applied (Friday–Saturday nights)')
    check_item(doc, 'Seasonal pricing set for upcoming high and low seasons')
    check_item(doc, 'Minimum stay rules reviewed and appropriate for your market')
    check_item(doc, 'Cleaning fee is competitive with comparable local listings')

    path = f'{BASE}/01-Listing-Optimization/01-Listing-Optimization-Guide.docx'
    doc.save(path)
    print(f'  ✓ 01-Listing-Optimization-Guide.docx')


# ==============================================================================
# DOCUMENT 3 — GUEST MESSAGE TEMPLATES
# ==============================================================================

def build_message_templates():
    doc = new_doc()
    add_header_footer(doc, 'Guest Message Templates')
    three_strip_cover(doc,
        'Guest Message\nTemplates Library',
        '15 Production-Ready Templates · Every Guest Situation Covered',
        'Copy. Personalise [BRACKETS]. Send.',
        'DOCUMENT 03 OF 08')

    stat_cards(doc, [
        ('Templates Included', '15', 'Every guest scenario'),
        ('Response Rate Target', '<1 hour', 'Airbnb algorithm boost'),
        ('Variables Format', '[BRACKETS]', 'Find & Replace to customise'),
        ('Sequences', '5', 'Pre/during/post + special'),
    ])

    info_box(doc, 'How to use: Replace every [BRACKETED ITEM] with your property-specific information. Load templates into Airbnb\'s Saved Messages feature for one-click sending. Customise tone to match your hosting style — these are frameworks, not scripts.')

    section_header(doc, 1, 'Sequence 1 — Pre-Booking')

    message_template_box(doc,
        'TEMPLATE 01',
        'Booking Inquiry Response',
        """Hi [GUEST FIRST NAME],

Thank you for your interest in [PROPERTY NAME] — it's a great choice for [their stated trip purpose or "your stay"].

To confirm everything lines up for you: the property sleeps [NUMBER] comfortably and is located [LOCATION DESCRIPTION — e.g., "a 5-minute walk from the city centre"].

[PROPERTY NAME] has everything you need for a comfortable stay: [TOP 3 AMENITIES — e.g., "fast WiFi, a fully equipped kitchen, and private parking"].

I'd be delighted to host you. Please feel free to ask any questions before booking — I always respond within a few hours.

Looking forward to welcoming you,
[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 02',
        'Booking Confirmation',
        """Hi [GUEST FIRST NAME],

Your booking is confirmed — welcome to [PROPERTY NAME]! I'm really looking forward to hosting you on [CHECK-IN DATE].

A few things to know now:
→ Check-in is from [CHECK-IN TIME] onwards
→ Check-out is by [CHECK-OUT TIME]
→ I'll send your full arrival instructions and access details 48 hours before you arrive

In the meantime, feel free to message me with any questions. I typically respond within 1–2 hours.

See you soon,
[YOUR NAME]"""
    )

    section_header(doc, 2, 'Sequence 2 — Pre-Arrival')

    message_template_box(doc,
        'TEMPLATE 03',
        '7 Days Before Arrival',
        """Hi [GUEST FIRST NAME],

Just a friendly note — your stay at [PROPERTY NAME] is one week away! Really looking forward to having you.

A couple of useful things ahead of arrival:

→ Check-in is from [CHECK-IN TIME]. If you're arriving later than [LATE TIME], no problem at all — the access is self-serve and works at any hour.
→ Parking: [PARKING INSTRUCTIONS — e.g., "Private space directly outside the property. The space is clearly marked."]
→ Nearest supermarket: [SUPERMARKET NAME + DISTANCE]

I'll send your full check-in instructions and door code 48 hours before you arrive.

Any questions at all, just message me — I'm always happy to help.

See you soon,
[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 04',
        '48 Hours Before Arrival — Access Instructions',
        """Hi [GUEST FIRST NAME],

Your arrival at [PROPERTY NAME] is in two days — here's everything you need for a smooth check-in.

ACCESS
→ Address: [FULL ADDRESS INCLUDING POSTCODE]
→ Entry: [LOCKBOX / SMART LOCK / KEY COLLECTION INSTRUCTIONS]
→ Door code: [CODE] (active from [CHECK-IN TIME] on [CHECK-IN DATE])
→ [ADDITIONAL ACCESS NOTES — e.g., "The main entrance code is separate from the flat code"]

PARKING
→ [DETAILED PARKING INSTRUCTIONS]

WIFI
→ Network: [WIFI NETWORK NAME]
→ Password: [WIFI PASSWORD]

A full House Manual with appliance guides, local recommendations and check-out instructions is inside the property.

Message me if anything is unclear. Safe travels!
[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 05',
        'Day of Arrival (Morning Message)',
        """Hi [GUEST FIRST NAME],

Today's the day! Just a quick check-in before you arrive at [PROPERTY NAME].

Everything is ready and waiting for you. The property was cleaned this morning and [WELCOME TOUCH — e.g., "there's fresh coffee, tea and a small welcome treat on the kitchen counter"].

A reminder of your access details:
→ Address: [ADDRESS]
→ Entry code: [CODE]
→ Check-in available from: [CHECK-IN TIME]

I'll be reachable on Airbnb messaging all day if you need anything. Enjoy your stay!

[YOUR NAME]"""
    )

    section_header(doc, 3, 'Sequence 3 — During Stay')

    message_template_box(doc,
        'TEMPLATE 06',
        'Mid-Stay Check-In',
        """Hi [GUEST FIRST NAME],

Hope you're having a wonderful stay at [PROPERTY NAME]!

Just a quick note to check everything is going well. If there's anything you need — extra towels, a question about the appliances, a local recommendation — please don't hesitate to message me.

Enjoy the rest of your stay,
[YOUR NAME]"""
    )

    section_header(doc, 4, 'Sequence 4 — Departure')

    message_template_box(doc,
        'TEMPLATE 07',
        'Check-Out Reminder (Evening Before)',
        """Hi [GUEST FIRST NAME],

Hope you've had a brilliant stay! Just a quick reminder that check-out is by [CHECK-OUT TIME] tomorrow.

For check-out, please:
→ Leave the key [KEY RETURN INSTRUCTIONS — e.g., "in the lockbox using code 1234"]
→ [ADDITIONAL CHECK-OUT STEP — e.g., "Leave used towels in the bathroom"]
→ [ADDITIONAL CHECK-OUT STEP — e.g., "Ensure all windows and doors are locked"]

No need to do any cleaning — that's handled.

Safe travels home, and I hope to welcome you back to [LOCATION] again soon.

[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 08',
        'Post Check-Out Thank You + Review Request',
        """Hi [GUEST FIRST NAME],

Thank you so much for staying at [PROPERTY NAME] — it was a pleasure having you.

If you have a moment, I'd really appreciate a review. Reviews are incredibly important for small independent hosts like myself, and honest feedback from guests like you makes a real difference.

I'll be leaving you a 5-star review in return — you were a wonderful guest.

I hope our paths cross again. Safe travels,
[YOUR NAME]

P.S. If anything could have been better during your stay, please message me directly before leaving a review. I take all feedback seriously and am always looking to improve."""
    )

    section_header(doc, 5, 'Special Situations')

    message_template_box(doc,
        'TEMPLATE 09',
        'Late Check-Out Request (Approve)',
        """Hi [GUEST FIRST NAME],

Of course — no problem at all! You're welcome to check out by [APPROVED LATE TIME] instead.

Just let me know if you need anything in the meantime, and I'll make sure your extra time is confirmed with the cleaning team.

Enjoy your morning,
[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 10',
        'Late Check-Out Request (Decline — Back-to-Back)',
        """Hi [GUEST FIRST NAME],

I appreciate you asking, and I'm sorry I can't accommodate this on this occasion — I have guests arriving in the early afternoon so the cleaning team needs to turn the property around.

I hope you understand. I'd love to welcome you back for a full stay another time — with more flexibility built in.

Have a wonderful journey home,
[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 11',
        'Early Check-In Request (Approve)',
        """Hi [GUEST FIRST NAME],

Great news — the property is ready early so I can confirm early check-in from [APPROVED EARLY TIME].

Your access code will be active from that time. Everything else remains the same as in your original check-in instructions.

See you soon,
[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 12',
        'Noise Complaint — Polite First Contact',
        """Hi [GUEST FIRST NAME],

I hope you're having a great stay. I've received a note from a neighbour about noise levels this evening — I'm sure this is just a minor misunderstanding.

As a reminder, the property's quiet hours are [QUIET HOURS — e.g., "10pm–8am"], which is also a condition of the booking.

I'm confident this is easily sorted, and I know you'll be a considerate neighbour for the rest of your stay. Thank you for understanding.

Best,
[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 13',
        'Property Damage — Professional Response',
        """Hi [GUEST FIRST NAME],

Thank you for your stay. During the post-checkout inspection, [CLEANER / I] noticed damage to [DESCRIBE ITEM SPECIFICALLY — e.g., "the kitchen table — a chip on the corner that was not present on the pre-arrival inspection"].

I always document the property before and after each stay. I'd like to resolve this straightforwardly. The replacement cost for [ITEM] is approximately [AMOUNT].

Could you confirm whether this occurred during your stay so we can agree next steps? I want to handle this professionally and fairly for both of us.

Kind regards,
[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 14',
        'Response to a 5-Star Review (Public)',
        """Thank you so much, [GUEST FIRST NAME] — what a lovely review! It was a genuine pleasure having you stay at [PROPERTY NAME]. Guests like you are exactly why I love hosting.

I hope to welcome you back to [LOCATION] again soon. Safe travels until then!

[YOUR NAME]"""
    )

    message_template_box(doc,
        'TEMPLATE 15',
        'Response to a Negative Review (Public — Professional)',
        """Thank you for taking the time to share your feedback, [GUEST FIRST NAME]. I'm sorry to hear that [SPECIFIC ISSUE MENTIONED] didn't meet your expectations during your stay.

[BRIEF FACTUAL RESPONSE TO THE SPECIFIC POINT — e.g., "The WiFi outage was caused by a provider-side issue that affected the whole street that evening — something entirely outside my control, though I completely understand the frustration."]

I take all feedback seriously and am always working to improve the experience at [PROPERTY NAME]. I hope you'll give [LOCATION] another visit in the future.

[YOUR NAME]"""
    )

    path = f'{BASE}/02-Guest-Communication/03-Guest-Message-Templates.docx'
    doc.save(path)
    print(f'  ✓ 03-Guest-Message-Templates.docx')


# ==============================================================================
# DOCUMENT 4 — HOUSE RULES TEMPLATE
# ==============================================================================

def build_house_rules():
    doc = new_doc()
    add_header_footer(doc, 'House Rules')
    three_strip_cover(doc,
        'House Rules\nTemplate',
        'Customise once. Publish on Airbnb. Share with every guest.',
        'Professional rules that protect you without alienating guests.',
        'DOCUMENT 04 OF 08')

    info_box(doc, 'How to use: Replace [BRACKETED ITEMS] with your property details. Publish the core rules on your Airbnb listing. Include the full version in your House Manual for guests to reference during their stay.')

    section_header(doc, 1, 'Check-In & Check-Out')
    check_item(doc, 'Check-in: from [CHECK-IN TIME] | Check-out: by [CHECK-OUT TIME]')
    check_item(doc, 'Early check-in and late check-out are subject to availability and must be requested in advance')
    check_item(doc, 'Access instructions are provided 48 hours before arrival via Airbnb messaging')
    check_item(doc, 'Please do not share the door/lockbox code with anyone not registered on the booking')

    section_header(doc, 2, 'Guests & Occupancy')
    check_item(doc, 'Maximum occupancy: [NUMBER] guests. This is a strict limit enforced by the building/property')
    check_item(doc, 'Only guests registered on the Airbnb booking may stay overnight')
    check_item(doc, 'Day visitors are welcome but must not exceed [VISITOR LIMIT] at any one time')
    check_item(doc, 'All guests must be 18 years or older unless accompanied by an adult responsible for them')

    section_header(doc, 3, 'Noise & Neighbours')
    check_item(doc, 'Quiet hours: [QUIET START TIME] to [QUIET END TIME]. Please respect neighbours during these hours')
    check_item(doc, 'Music, TV and conversation must be kept to a reasonable volume at all times')
    check_item(doc, 'No loud gatherings, parties or events — this property is a private residence, not an event venue')
    check_item(doc, 'If a neighbour raises a concern, please address it immediately and contact me via Airbnb message')

    section_header(doc, 4, 'Smoking & Substances')
    check_item(doc, 'This is a strictly non-smoking property — indoors and on all balconies/patios')
    check_item(doc, '[SMOKING AREA NOTE — e.g., "Smoking is permitted in the rear garden only, with full disposal of all cigarette waste"]')
    check_item(doc, 'Evidence of smoking indoors will result in a deep-cleaning fee of [AMOUNT] charged via the Resolution Centre')
    check_item(doc, 'Illegal substances are strictly prohibited on the premises')

    section_header(doc, 5, 'Pets')
    if True:  # Template for both versions
        check_item(doc, '[PETS ALLOWED]: Well-behaved pets are welcome with prior written agreement. Please declare your pet at time of booking.')
        check_item(doc, '[PETS NOT ALLOWED]: I\'m sorry — this property is not suitable for pets. If a pet is brought without agreement, a cleaning fee may apply.')
        check_item(doc, 'Pet owners are responsible for any damage caused by their animals and for all pet hair removal')
        check_item(doc, 'Pets are not permitted on furniture or bedding at any time')
    amber_box(doc, 'Choose one of the pet options above and remove the other based on your policy. Add your specific pet fee if applicable.')

    section_header(doc, 6, 'Property Care')
    check_item(doc, 'Please treat the property as you would your own home')
    check_item(doc, 'Report any accidental damage or breakages immediately via Airbnb — this avoids complications at checkout')
    check_item(doc, 'Do not move furniture between rooms or rearrange the layout of the property')
    check_item(doc, 'No candles or naked flames indoors. Battery-powered candles are provided if ambience is desired')
    check_item(doc, 'Please do not put non-flushable items down toilets or sinks (wet wipes, sanitary products)')

    section_header(doc, 7, 'Parking')
    check_item(doc, '[PARKING AVAILABLE]: [NUMBER] parking space(s) available at [LOCATION/DESCRIPTION]. For your registered vehicle only.')
    check_item(doc, 'Do not park in spaces marked for other residents')
    check_item(doc, 'Electric vehicle charging: [AVAILABLE / NOT AVAILABLE — include details if available]')

    section_header(doc, 8, 'Security & Departure')
    check_item(doc, 'On departure, please ensure all windows and external doors are locked')
    check_item(doc, 'Leave all keys / return key to lockbox using code [CODE] on departure')
    check_item(doc, 'Switch off all lights, appliances and heating before leaving (check-out only)')
    check_item(doc, 'Leave used towels in the [LOCATION — e.g., "bathroom floor / laundry basket"] before departure')

    section_header(doc, 9, 'Photography & Social Media')
    check_item(doc, 'You are welcome to share photos of your stay on social media — tag us at [HANDLE] if you\'d like!')
    check_item(doc, 'Please do not photograph or share images of neighbouring properties or their occupants')
    check_item(doc, 'Commercial photography or filming on the premises requires prior written consent')

    section_header(doc, 10, 'Violations & Consequences')
    body(doc, 'Serious rule violations may result in:')
    bullet(doc, 'Early termination of the booking without refund')
    bullet(doc, 'Security deposit claim via Airbnb\'s Resolution Centre')
    bullet(doc, 'Reporting to Airbnb Trust & Safety for pattern violations')
    bullet(doc, 'Local authority involvement in the case of illegal activity')
    amber_box(doc, 'By completing a booking, guests confirm they have read and agreed to these House Rules. These rules form part of the rental agreement.')

    path = f'{BASE}/02-Guest-Communication/04-House-Rules-Template.docx'
    doc.save(path)
    print(f'  ✓ 04-House-Rules-Template.docx')


# ==============================================================================
# DOCUMENT 5 — HOUSE MANUAL TEMPLATE
# ==============================================================================

def build_house_manual():
    doc = new_doc()
    add_header_footer(doc, 'House Manual')
    three_strip_cover(doc,
        'House Manual\nTemplate',
        'Customise this document and leave a printed copy at your property',
        'Your guests\' complete reference guide during their stay.',
        'DOCUMENT 05 OF 08')

    info_box(doc, 'This is a guest-facing document. Replace every [BRACKETED ITEM] with your specific details. Print and laminate the key pages, or share as a PDF via Airbnb messaging before arrival. A well-prepared House Manual reduces guest messages by 60–70%.')

    section_header(doc, 1, 'Welcome')
    body(doc, 'Dear [GUEST FIRST NAME],')
    body(doc, 'Welcome to [PROPERTY NAME]! We\'re so pleased you\'re here.')
    body(doc, '[PERSONALISED WELCOME — e.g., "This flat has been our home for three years and we\'ve tried to make it everything we\'d want in a place to stay — comfortable, well-equipped and stocked with everything you need."]')
    body(doc, 'This guide covers everything you need to know about the property. Please read the Check-Out section before your last morning — it makes the handover quick and smooth for everyone.')
    body(doc, 'If anything is unclear or you need help, message us through Airbnb at any time. We typically respond within one hour.')
    body(doc, 'Enjoy your stay,')
    body(doc, '[YOUR NAME(S)]')

    section_header(doc, 2, 'Access & Entry')
    heading3(doc, 'Property Address')
    body(doc, '[FULL ADDRESS INCLUDING POSTCODE / ZIP CODE]', indent=True)

    heading3(doc, 'Main Entry')
    body(doc, '[ENTRY INSTRUCTIONS — e.g., "Enter through the main street-level door using the keypad code: 4821. Take the lift or stairs to Floor 3. Your flat door is number 14 — same code applies."]', indent=True)

    heading3(doc, 'Parking')
    body(doc, '[PARKING INSTRUCTIONS — e.g., "Your dedicated parking space is in the underground car park — access via the ramp on [STREET NAME]. Enter code 5539 at the barrier. Your space is marked with our flat number: 14."]', indent=True)

    heading3(doc, 'Key Return on Departure')
    body(doc, '[KEY RETURN INSTRUCTIONS — e.g., "On check-out, please return the key fob to the lockbox by the front door. Leave it inside and press any button to close and lock it."]', indent=True)

    section_header(doc, 3, 'WiFi & Technology')

    two_col_table(doc,
        ['Connection', 'Details'],
        [
            ['WiFi Network Name', '[SSID / NETWORK NAME]'],
            ['WiFi Password', '[PASSWORD]'],
            ['Smart TV', '[e.g., "65" Samsung — use your own Netflix/Apple TV login or use the guest account: login: guest@email.com / pw: guest123"]'],
            ['TV Channels', '[e.g., "All Freeview channels available. Press Home on the remote for Smart TV features."]'],
            ['Sound System', '[e.g., "Sonos speaker in living room — connect via Bluetooth or use AirPlay. Name: Living Room Sonos"]'],
            ['Laptop Stand / Monitor', '[e.g., "Dell 24" monitor on the desk with HDMI and USB-C cables. Printer available — WiFi name: HP-Office-7823, no password needed"]'],
        ],
        col_widths_cm=[4.5, 13.0]
    )

    section_header(doc, 4, 'Kitchen Guide')
    body(doc, 'The kitchen is fully equipped for home cooking. Everything below is available for your use.')

    two_col_table(doc,
        ['Appliance', 'Location', 'Notes'],
        [
            ['Espresso Machine', 'Left of sink', '[e.g., "Nespresso Vertuo — pods in the drawer below. Press the button once to brew. Capsules are in the top drawer — help yourself."]'],
            ['Oven', 'Under hob', '[e.g., "Fan oven — preheat for 10 minutes. Trays and dishes in the lower drawer."]'],
            ['Dishwasher', 'Under counter, right of sink', '[e.g., "Tablets under the sink. Full instructions on the inside of the door. Short cycle: 40 mins."]'],
            ['Washing Machine', '[LOCATION]', '[e.g., "In the bathroom. Standard wash: 40°C, 1h20m. Detergent and softener under the sink."]'],
            ['Microwave', 'On counter beside fridge', '[e.g., "Standard microwave. Defrost setting = power level 3."]'],
            ['Fridge / Freezer', 'Left of door', '[e.g., "Please keep the freezer compartment clear — it\'s for your use during your stay."]'],
            ['Hob', 'Built in — centre of kitchen', '[e.g., "Induction hob — compatible pans are in the cupboard to the right. Turn the knob to ignite, then adjust heat."]'],
            ['Toaster / Kettle', 'Counter, right side', '[e.g., "Both ready to use. Tea, coffee and sugar are in the first drawer."]'],
        ],
        col_widths_cm=[4.0, 3.5, 10.0]
    )

    heading3(doc, 'Kitchen Supplies Provided')
    bullet(doc, 'Tea, coffee (ground and pods), sugar, salt and pepper')
    bullet(doc, 'Washing-up liquid, dishwasher tablets, washing machine detergent')
    bullet(doc, 'Basic cooking oils: vegetable oil and olive oil')
    bullet(doc, 'Tin foil, cling film, food bags, paper towels')
    bullet(doc, '[ADD YOUR OWN: e.g., "Local honey, fresh eggs from the farm next door"]')

    section_header(doc, 5, 'Bedrooms & Bathrooms')

    heading3(doc, 'Sleeping Arrangements')
    two_col_table(doc,
        ['Room', 'Bed Type', 'Extras'],
        [
            ['Bedroom 1', '[e.g., King-size, memory foam mattress]', '[e.g., Blackout curtains, bedside USB chargers, reading lamps]'],
            ['Bedroom 2', '[e.g., Two single beds (can be joined as a super-king)]', '[e.g., Built-in wardrobe, desk, USB sockets]'],
            ['[Sofa Bed]', '[e.g., Double sofa bed in living room]', '[e.g., Bedding stored in the ottoman at the foot of the sofa]'],
        ],
        col_widths_cm=[4.0, 5.0, 8.5]
    )

    heading3(doc, 'Bathrooms & Toiletries')
    body(doc, 'The following toiletries are provided as a welcome supply. For longer stays, we recommend bringing your preferred products.', indent=True)
    bullet(doc, 'Shampoo, conditioner and body wash (mounted dispensers in shower)')
    bullet(doc, 'Hand soap at each sink')
    bullet(doc, 'Shower gel and a bar of soap as backup')
    bullet(doc, 'Toilet paper (extra rolls under the sink in each bathroom)')
    bullet(doc, 'Bath towels × [NUMBER] and hand towels × [NUMBER] per bathroom')
    bullet(doc, 'Hair dryer: [LOCATION — e.g., "under the sink in the main bathroom"]')

    section_header(doc, 6, 'Heating & Cooling')
    body(doc, '[HEATING SYSTEM DESCRIPTION — e.g., "The property has underfloor heating throughout. The thermostat is on the wall in the hallway. We recommend setting it between 19–22°C for a comfortable temperature. It takes approximately 30 minutes to reach your chosen temperature."]')
    body(doc, '[COOLING SYSTEM — e.g., "Air conditioning units are in both bedrooms and the living room. Use the remote on the bedside table. We recommend Cooling mode at 21°C. Please turn off when leaving the property."]')
    amber_box(doc, 'To save energy (and the planet!), please turn off heating/cooling when leaving the property for more than an hour. Thank you.')

    section_header(doc, 7, 'Check-Out Instructions')
    body(doc, 'Check-out is by [CHECK-OUT TIME]. Following these simple steps ensures a smooth handover and helps us prepare for the next guests.')

    check_item(doc, 'Return key/fob to: [KEY RETURN LOCATION AND INSTRUCTIONS]')
    check_item(doc, 'Leave used towels [LOCATION — e.g., "in the bathroom on the floor / in the laundry basket"]')
    check_item(doc, 'Leave used bedding as it is — the cleaning team will strip and wash it')
    check_item(doc, 'Wash up or load used dishes into the dishwasher and start a cycle')
    check_item(doc, 'Put all rubbish in [RUBBISH BIN LOCATION + COLLECTION NOTES]')
    check_item(doc, 'Close and lock all windows')
    check_item(doc, 'Ensure all doors are closed and the front door is locked behind you')
    check_item(doc, 'Turn off all lights, appliances and heating/cooling')
    body(doc, 'Please do not do any additional cleaning — that is handled by our professional cleaning team.')

    section_header(doc, 8, 'Emergency Contacts')
    two_col_table(doc,
        ['Situation', 'Who to Contact', 'Number / Method'],
        [
            ['General questions during stay', '[YOUR NAME]', 'Airbnb messaging (fastest) / [PHONE NUMBER IF APPLICABLE]'],
            ['Property emergency (water, power, lock)', '[YOUR NAME]', '[PHONE NUMBER — available 24/7 for true emergencies]'],
            ['Medical emergency', 'Emergency services', '[LOCAL EMERGENCY NUMBER — e.g., "999 (UK) / 112 (EU) / 911 (US)"]'],
            ['Gas leak', 'Gas Emergency Line', '[GAS EMERGENCY NUMBER — e.g., "0800 111 999 (UK)"]'],
            ['Building management (if applicable)', '[BUILDING MANAGER NAME]', '[PHONE / EMAIL]'],
            ['[LOCAL TAXI / RIDE SERVICE]', '[NAME]', '[NUMBER / APP]'],
        ],
        col_widths_cm=[4.5, 4.5, 8.5]
    )

    section_header(doc, 9, 'Local Area Guide')
    body(doc, 'Our personal recommendations — tried, tested and genuinely good.')

    heading3(doc, 'Coffee & Breakfast')
    bullet(doc, '[CAFÉ NAME] — [DESCRIPTION, e.g., "Best flat white in the neighbourhood. 3-minute walk. Always busy on weekends — arrive before 9am."]')
    bullet(doc, '[CAFÉ NAME 2] — [e.g., "Great for working — quiet, good WiFi, power sockets at every table."]')

    heading3(doc, 'Lunch & Dinner')
    bullet(doc, '[RESTAURANT NAME] — [e.g., "Outstanding Italian. Book in advance on weekends. 5-minute walk."]')
    bullet(doc, '[RESTAURANT NAME 2] — [e.g., "Casual but brilliant — the best burgers locally. No booking needed."]')
    bullet(doc, '[RESTAURANT NAME 3] — [e.g., "If you want something special, this is the one. Tasting menu is worth every penny."]')

    heading3(doc, 'Supermarkets & Shops')
    bullet(doc, '[SUPERMARKET NAME] — [e.g., "Largest local option. 7 minutes walk. Open Mon–Sat 7am–9pm, Sun 10am–4pm."]')
    bullet(doc, '[CONVENIENCE STORE] — [e.g., "Open 24/7. 2 minutes walk. Good for essentials at any hour."]')

    heading3(doc, 'Transport')
    bullet(doc, '[NEAREST STATION / BUS STOP] — [e.g., "Central Station: 5-minute walk. Direct to airport: Line 3, 22 minutes."]')
    bullet(doc, '[TAXI / RIDE APP] — [e.g., "Uber works well here. Alternatively, [LOCAL TAXI COMPANY] on [NUMBER] is reliable."]')
    bullet(doc, '[BIKE / SCOOTER] — [e.g., "City bikes available at the stand on [STREET NAME] — download the [APP NAME] app."]')

    heading3(doc, 'Things to Do Nearby')
    bullet(doc, '[ATTRACTION 1] — [e.g., "The old town is a 10-minute walk — beautiful architecture, weekend market every Saturday."]')
    bullet(doc, '[ATTRACTION 2] — [e.g., "The coastal path starts from the end of our road — a 6km walk to the lighthouse with stunning views."]')
    bullet(doc, '[ATTRACTION 3] — [e.g., "The city museum is free entry and genuinely world-class — 2 hours well spent."]')

    path = f'{BASE}/04-Guest-Experience/05-House-Manual-Template.docx'
    doc.save(path)
    print(f'  ✓ 05-House-Manual-Template.docx')


# ==============================================================================
# DOCUMENT 6 — CHECK-IN SOP
# ==============================================================================

def build_checkin_sop():
    doc = new_doc()
    add_header_footer(doc, 'Check-In SOP')
    three_strip_cover(doc,
        'Check-In\nStandard Operating\nProcedure',
        'Every step. Every time. Every guest.',
        'A consistent check-in experience drives 5-star reviews.',
        'DOCUMENT 06 OF 08')

    stat_cards(doc, [
        ('Preparation Window', '24 Hours', 'Before each arrival'),
        ('Response Time Target', '<1 Hour', 'For arrival day queries'),
        ('Welcome Setup', '45 Min', 'For property staging'),
        ('Guest Satisfaction', '5 Stars', 'Consistent execution'),
    ])

    section_header(doc, 1, '48 Hours Before Arrival')
    body(doc, 'Complete this checklist 48 hours before every check-in. Assign to host or co-host as appropriate.')

    heading3(doc, 'Booking Confirmation Review')
    check_item(doc, 'Confirm guest name, check-in date, check-out date and number of guests')
    check_item(doc, 'Confirm that guest has sent the 48-hour pre-arrival message (or send manually if not scheduled)')
    check_item(doc, 'Verify access code is active and functioning (test the lockbox or smart lock)')
    check_item(doc, 'Check that no maintenance issues are outstanding from previous guest')

    heading3(doc, 'Property Readiness')
    check_item(doc, 'Confirm cleaning is booked and scheduled after previous guest\'s check-out')
    check_item(doc, 'Confirm all consumables are stocked: coffee pods, tea, toilet paper, toiletries, bin bags')
    check_item(doc, 'Check that welcome supplies are ready if you provide a welcome pack')
    check_item(doc, 'Confirm all appliances are operational (no issues flagged by previous guest)')

    section_header(doc, 2, 'Day of Arrival — Property Preparation')
    body(doc, 'This checklist is for the person doing the final pre-arrival check. Typically completed after the cleaner has finished.')

    heading3(doc, 'Exterior')
    check_item(doc, 'Pathway, front garden or entrance area is clean and tidy')
    check_item(doc, 'Doormat in position and clean')
    check_item(doc, 'Building / property exterior is presentable')
    check_item(doc, 'Parking space is clear and accessible (if applicable)')
    check_item(doc, 'Lockbox/smart lock is functional — test the code before leaving')

    heading3(doc, 'Interior — Living Areas')
    check_item(doc, 'Property is clean, fresh-smelling and at a comfortable temperature (18–20°C recommended)')
    check_item(doc, 'All lights functioning — replace any blown bulbs')
    check_item(doc, 'TV remote has working batteries and is in a visible location')
    check_item(doc, 'WiFi is working — test from the property with a phone')
    check_item(doc, 'No personal items, previous-guest belongings or cleaning equipment visible')
    check_item(doc, 'Cushions arranged, throw blankets folded neatly')

    heading3(doc, 'Interior — Kitchen')
    check_item(doc, 'All dishes, glasses and cutlery clean and stored correctly')
    check_item(doc, 'Dishwasher empty and clean')
    check_item(doc, 'Coffee machine cleaned and stocked with pods/beans')
    check_item(doc, 'Fridge clean and empty of previous guest\'s food — door closed')
    check_item(doc, 'Bin is empty with a fresh bin bag')
    check_item(doc, 'Hob, oven and counters clean')
    check_item(doc, 'Tea, coffee, sugar in clearly visible containers')
    check_item(doc, 'Welcome supplies staged as per your welcome setup (see Section 3)')

    heading3(doc, 'Interior — Bedrooms')
    check_item(doc, 'Fresh bedding on all beds — fitted sheet, duvet, pillowcases all changed')
    check_item(doc, 'Beds made with hotel-style presentation (top sheet folded, pillows plumped)')
    check_item(doc, 'Wardrobes and drawers empty and clean for guest use')
    check_item(doc, 'Curtains or blinds in working order')
    check_item(doc, 'Bedside lamps functional and positioned correctly')
    check_item(doc, 'Extra blanket and spare pillows visible or accessible')

    heading3(doc, 'Interior — Bathrooms')
    check_item(doc, 'Toilet, sink and shower/bath fully clean and streak-free')
    check_item(doc, 'Fresh towels folded and staged hotel-style')
    check_item(doc, 'Toiletries: shampoo, conditioner, body wash, hand soap restocked')
    check_item(doc, 'Toilet roll visible on holder — one spare roll placed under sink')
    check_item(doc, 'Mirror clean and streak-free')
    check_item(doc, 'Bath mat clean and positioned correctly')
    check_item(doc, 'Bin empty with fresh bin bag')
    check_item(doc, 'Hair dryer in position and functional')

    section_header(doc, 3, 'Welcome Staging Setup')
    body(doc, 'The welcome setup is the single highest-impact action for generating 5-star reviews. It takes 10–15 minutes and requires minimal cost. Guests who receive a welcome pack mention it in reviews more than any other single item.')

    two_col_table(doc,
        ['Welcome Element', 'Details', 'Cost', 'Review Impact'],
        [
            ['Welcome note', 'Printed or handwritten. Guest name, wifi, check-out time', '£0', 'High — personal touch'],
            ['Tea & coffee selection', '4–6 pods/bags, sugar, local biscuit or chocolate', '£2–4', 'Very High — mentioned constantly in reviews'],
            ['Small local treat', 'Local chocolates, honey, mini wine bottle or juice', '£3–8', 'Very High — guests always comment on this'],
            ['Fresh flowers', 'Simple supermarket bunch, in a vase on dining table', '£5–8', 'High — aspirational, photo-worthy'],
            ['Toiletry top-up', 'Fresh shampoo bottle visible, not nearly empty', '£2–5', 'High — cleanliness indicator'],
            ['Local guide booklet', 'Your House Manual — printed and laminated or in a stand', '£5 (once)', 'High — professional presentation'],
        ],
        col_widths_cm=[4.0, 6.0, 2.0, 5.5]
    )

    info_box(doc, 'Minimum recommended welcome setup: Welcome note + tea/coffee selection + one local treat. Total cost: £4–8 per booking. Return: measurable uplift in review scores and review rate.')

    section_header(doc, 4, 'Communication Timeline')
    process_steps(doc, [
        ('1', 'Booking Confirmed', 'Send Template 02 (Booking Confirmation) within 1 hour of booking.'),
        ('2', '7 Days Before', 'Send Template 03 (Pre-Arrival — Week Before) on Day 7.'),
        ('3', '48 Hours Before', 'Send Template 04 (Access Instructions) exactly 48h before check-in.'),
        ('4', 'Morning of Arrival', 'Send Template 05 (Day of Arrival) by 10am on the check-in date.'),
        ('5', 'Day 2 of Stay', 'Send Template 06 (Mid-Stay Check-In) if stay is 3+ nights.'),
        ('6', 'Evening Before Checkout', 'Send Template 07 (Check-Out Reminder) by 6pm the evening before.'),
    ])

    section_header(doc, 5, 'Handling Arrival Problems')
    body(doc, 'Even with perfect preparation, issues occur. This section gives you a response framework for the most common scenarios.')

    two_col_table(doc,
        ['Problem', 'Immediate Action', 'Resolution'],
        [
            ['Guest cannot access property', 'Respond within 5 minutes. Walk through access steps via message.', 'If still locked out: call locksmith. Log incident.'],
            ['Guest arrives before check-in time', 'Apologise — "Property is being prepared until [TIME]." Offer luggage storage if available.', 'Offer early check-in only if property is genuinely ready.'],
            ['Property not clean on arrival', 'Apologise immediately. Offer to send cleaner urgently or discount.', 'Contact cleaner immediately. Document issue. Review cleaner performance.'],
            ['WiFi not working', 'Send router reset instructions. Router is at [LOCATION]. Unplug 30s, replug.', 'If still failing: contact ISP. Offer mobile hotspot as temporary solution.'],
            ['Heating/AC not working', 'Walk guest through thermostat via message.', 'Send engineer if not resolved in 2 hours. Partial refund if overnight issue.'],
            ['Something is damaged/broken', 'Acknowledge immediately. Apologise. Offer resolution.', 'Log in Maintenance Tracker. Arrange repair for next available window.'],
        ],
        col_widths_cm=[3.5, 5.5, 8.5]
    )

    path = f'{BASE}/05-SOP-Library/06-Check-In-SOP.docx'
    doc.save(path)
    print(f'  ✓ 06-Check-In-SOP.docx')


# ==============================================================================
# DOCUMENT 7 — CLEANING SOP
# ==============================================================================

def build_cleaning_sop():
    doc = new_doc()
    add_header_footer(doc, 'Cleaning SOP')
    three_strip_cover(doc,
        'Cleaning\nStandard Operating\nProcedure',
        'Room-by-room protocol · Linen standards · Quality inspection',
        'The same 5-star result every single turnover.',
        'DOCUMENT 07 OF 08')

    stat_cards(doc, [
        ('Studio Clean', '1.5 Hours', 'Standard allocation'),
        ('2BR Clean', '2.5–3 Hours', 'Standard allocation'),
        ('3BR Clean', '3.5–4 Hours', 'Standard allocation'),
        ('Quality Score', '100%', 'Every item checked'),
    ])

    info_box(doc, 'This SOP is designed to be shared directly with your cleaning team. Print this document and brief your cleaner on your first working session together. Expect the first 2–3 cleans to take longer as your cleaner learns the property. Time allowances above assume an experienced cleaner familiar with the property.')

    section_header(doc, 1, 'Cleaning Standards — Non-Negotiables')
    body(doc, 'The following standards apply to every single turnover, regardless of how long the previous guest stayed or what condition they left the property in.')

    bullet(doc, 'Every surface the guest touched must be cleaned and wiped — no exceptions')
    bullet(doc, 'All beds must have fresh linen every turnover — no "it looks clean" exceptions')
    bullet(doc, 'All towels must be fresh every turnover — even if barely used')
    bullet(doc, 'The property must smell clean and neutral — never of cleaning products or previous guests')
    bullet(doc, 'Every bin must be empty before departure')
    bullet(doc, 'Nothing from a previous guest should be left in the property')
    bullet(doc, 'Appliances must be cleaned and reset to default settings')
    bullet(doc, 'If in doubt — clean it again')

    heading2(doc, 'Cleaning Order — Most Efficient Sequence')
    process_steps(doc, [
        ('1', 'Strip Linen', 'Start immediately — strip all beds and collect towels before anything else. Start washing machine.'),
        ('2', 'Rubbish', 'Empty all bins. Take to external bins. Replace bin bags in all bins.'),
        ('3', 'Surfaces', 'Clear and wipe all surfaces in every room — kitchen, bathrooms, bedrooms, living room.'),
        ('4', 'Bathrooms', 'Full bathroom deep clean — toilet, sink, shower, mirrors, floors. Restock toiletries.'),
        ('5', 'Kitchen', 'Full kitchen clean — hob, oven, fridge, surfaces, sink. Restock supplies.'),
        ('6', 'Bedrooms', 'Make beds (fresh linen). Stage towels. Clean surfaces, mirrors, vacuums.'),
        ('7', 'Living Room', 'Vacuum, dust, plump cushions, wipe remote, reset TV/appliances.'),
        ('8', 'Floors', 'Vacuum throughout. Mop hard floors. Polish bathroom floors.'),
        ('9', 'Final Inspect', 'Walk through every room using Final Inspection Checklist. Stage welcome items.'),
    ])

    section_header(doc, 2, 'Kitchen — Full Checklist')
    check_item(doc, 'All dishes washed, dried and stored in correct cupboards')
    check_item(doc, 'Dishwasher emptied, cleaned (door seal wiped), and left open to air')
    check_item(doc, 'Hob wiped clean — no grease residue on burners or surrounding surfaces')
    check_item(doc, 'Oven interior wiped — pay attention to door glass and bottom tray')
    check_item(doc, 'Microwave interior clean — check ceiling and turntable')
    check_item(doc, 'Fridge emptied of all previous guest food — shelves wiped clean')
    check_item(doc, 'Coffee machine: empty water tank and drip tray, wipe exterior, reload capsules')
    check_item(doc, 'Kettle: empty, rinse, wipe exterior')
    check_item(doc, 'All countertops disinfected and dried streak-free')
    check_item(doc, 'Sink and taps cleaned and polished — no limescale visible')
    check_item(doc, 'Splashbacks wiped down')
    check_item(doc, 'Bin empty with fresh bag — pedal clean and odour-free')
    check_item(doc, 'Consumables restocked: coffee pods, tea bags, sugar, kitchen roll, washing-up liquid')
    check_item(doc, 'All appliances returned to default position')
    check_item(doc, 'Floor swept and mopped')

    section_header(doc, 3, 'Bathroom(s) — Full Checklist')
    heading3(doc, 'Each Bathroom')
    check_item(doc, 'Toilet: clean under rim, seat (top and bottom), bowl, exterior, base, flush handle')
    check_item(doc, 'Shower/bath: scrub all walls and floor, remove any hair, clean door/curtain, clean plughole')
    check_item(doc, 'Sink: clean basin, taps (no limescale), overflow, drain — polish taps dry')
    check_item(doc, 'Mirror: clean and streak-free — check in different light angles')
    check_item(doc, 'Vanity surfaces: cleared, cleaned and dried')
    check_item(doc, 'Shower shelf or caddy: wipe clean, no product residue')
    check_item(doc, 'Dispenser bottles: refill if below 1/3 (shampoo, conditioner, body wash)')
    check_item(doc, 'Fresh hand soap at sink')
    check_item(doc, 'Toilet roll: on holder — full or near-full. Spare under sink.')
    check_item(doc, 'Fresh towels — hotel fold or rolled, staged on towel rail or bed')
    check_item(doc, 'Bath mat clean and correctly positioned')
    check_item(doc, 'Hair dryer in designated location — cord neatly wrapped')
    check_item(doc, 'Bin: emptied, cleaned, fresh bag')
    check_item(doc, 'Floor: scrubbed and dried — no hair visible')

    section_header(doc, 4, 'Bedrooms — Full Checklist')
    heading3(doc, 'Each Bedroom')
    check_item(doc, 'Strip all used linen — sheets, pillowcases, duvet cover. Place in laundry bag.')
    check_item(doc, 'Check under beds and pillows for forgotten guest items')
    check_item(doc, 'Mattress inspected for stains — report any damage immediately')
    check_item(doc, 'Fresh fitted sheet: smooth, no wrinkles')
    check_item(doc, 'Duvet cover and pillowcases: fresh, tight, hotel presentation')
    check_item(doc, 'Spare pillow: placed on shelf or in wardrobe — not on bed')
    check_item(doc, 'Duvet and pillows plumped and symmetrical')
    check_item(doc, 'Bedside tables wiped — no dust, no ring marks from drinks')
    check_item(doc, 'Lamps functioning — check bulbs')
    check_item(doc, 'Wardrobe/drawers empty and wiped inside')
    check_item(doc, 'Curtains/blinds fully open (or drawn if daylight creates issue)')
    check_item(doc, 'Mirrors wiped clean and streak-free')
    check_item(doc, 'Floor vacuumed including corners and under furniture')

    section_header(doc, 5, 'Living Room & Entrance')
    check_item(doc, 'Sofa: remove all crumbs, fluff cushions, fold throws neatly')
    check_item(doc, 'Coffee table: wiped clean, no ring marks, coasters in position')
    check_item(doc, 'Remote controls: cleaned with antibacterial wipe — placed visibly on table')
    check_item(doc, 'Smart TV: screen wiped, set to home screen (not previous guest\'s account)')
    check_item(doc, 'Windows: inside glass clean, no smears or fingerprints')
    check_item(doc, 'Windowsills: dusted')
    check_item(doc, 'All surfaces dusted including skirting boards and lamp shades')
    check_item(doc, 'Plants watered if applicable')
    check_item(doc, 'Floor vacuumed throughout including under furniture')

    heading3(doc, 'Entrance / Hallway')
    check_item(doc, 'Entrance mat clean or replaced')
    check_item(doc, 'Coat hooks clear of previous guest items')
    check_item(doc, 'Key/key fob in designated handoff location')
    check_item(doc, 'Welcome supplies staged as per host instructions')

    section_header(doc, 6, 'Linen & Laundry Protocol')
    body(doc, 'Linen quality is one of the most-mentioned factors in guest reviews. Establish a linen system from day one.')

    two_col_table(doc,
        ['Item', 'Wash Temperature', 'Tumble Dry', 'Iron Required', 'Replace Every'],
        [
            ['Fitted sheets', '60°C', 'Yes — medium heat', 'No (fitted)', '12 months or when worn'],
            ['Duvet covers', '60°C', 'Yes — low heat', 'Yes (visible surface)', '12 months'],
            ['Pillowcases', '60°C', 'Yes', 'Yes', '12 months'],
            ['Bath towels', '60°C', 'Yes — high heat', 'No', '18 months or when thin'],
            ['Hand towels', '60°C', 'Yes', 'No', '18 months'],
            ['Bath mat', '40°C', 'Yes', 'No', '12 months'],
        ],
        col_widths_cm=[3.5, 3.0, 3.0, 3.0, 4.5]
    )

    info_box(doc, 'Linen par level recommendation: 3 full sets per bed. Set 1 = on the bed. Set 2 = in the wash. Set 3 = clean and ready for emergencies or same-day turnovers.')

    section_header(doc, 7, 'Consumables Restocking List')
    body(doc, 'Check and restock these items at every turnover. Keep a supply box at the property or deliver with each clean.')

    two_col_table(doc,
        ['Item', 'Minimum Level', 'Full Restock Amount', 'Location in Property'],
        [
            ['Toilet paper', '1 on holder + 1 spare', '1 on holder + 2 spare per bathroom', 'Under sink each bathroom'],
            ['Shampoo', '50% dispenser min', 'Full dispenser', 'Shower dispenser'],
            ['Conditioner', '50% dispenser min', 'Full dispenser', 'Shower dispenser'],
            ['Body wash', '50% dispenser min', 'Full dispenser', 'Shower dispenser'],
            ['Hand soap', '50% pump min', 'Full pump per sink', 'Each bathroom sink'],
            ['Coffee pods', '3 pods minimum', '8 pods', 'Coffee machine drawer'],
            ['Tea bags', '4 bags minimum', '8 bags', 'Kitchen counter/canister'],
            ['Sugar', '8 sachets minimum', '12 sachets', 'Kitchen counter'],
            ['Washing-up liquid', '30% remaining', 'Full bottle', 'Under kitchen sink'],
            ['Kitchen roll', '1 sheet remaining', '1 full roll', 'Kitchen counter'],
            ['Bin bags (kitchen)', '1 in bin', '3 spares under sink', 'Under kitchen sink'],
            ['Dishwasher tablets', '2 minimum', '5 tablets', 'Under kitchen sink'],
        ],
        col_widths_cm=[4.0, 3.0, 3.5, 7.0]
    )

    section_header(doc, 8, 'Final Inspection Checklist')
    body(doc, 'Walk through every room with this checklist before marking the clean as complete. This is your quality gate.')

    check_item(doc, 'Kitchen: all appliances clean and reset, consumables restocked, floor mopped')
    check_item(doc, 'Bathroom(s): gleaming — toilet, sink, shower, mirror. Towels staged. Consumables full.')
    check_item(doc, 'Bedrooms: fresh beds made hotel-style, floors vacuumed, nothing from previous guest')
    check_item(doc, 'Living room: reset, clean, cushions and throws staged')
    check_item(doc, 'Entrance: key in place, welcome setup complete, mat clean')
    check_item(doc, 'All lights: tested and working')
    check_item(doc, 'WiFi: test connection on phone')
    check_item(doc, 'All bins: emptied with fresh bags')
    check_item(doc, 'All windows and external doors: closed and locked')
    check_item(doc, 'Any damage or maintenance issue: photographed and reported to host immediately')

    amber_box(doc, 'Damage Reporting: If you discover any damage during a clean, photograph it immediately and send to the host via WhatsApp or Airbnb message with the photo and a brief description. Include: what is damaged, where it is, and whether it was damage or normal wear.')

    path = f'{BASE}/05-SOP-Library/07-Cleaning-SOP.docx'
    doc.save(path)
    print(f'  ✓ 07-Cleaning-SOP.docx')


# ==============================================================================
# DOCUMENT 8 — REVIEW STRATEGY GUIDE
# ==============================================================================

def build_review_guide():
    doc = new_doc()
    add_header_footer(doc, 'Review Strategy Guide')
    three_strip_cover(doc,
        'Review Strategy\nGuide',
        'Get 5-Star Reviews · Respond Professionally · Protect Your Reputation',
        'Reviews are your listing\'s most powerful commercial asset.',
        'DOCUMENT 08 OF 08')

    stat_cards(doc, [
        ('Target Rating', '4.8+', 'For Superhost status'),
        ('Superhost Threshold', '4.8 ★', 'Airbnb requirement'),
        ('Review Conversion', '>75%', 'Reviews per checkout'),
        ('Response Target', '100%', 'Reply to all reviews'),
    ])

    section_header(doc, 1, 'Why Reviews Are Your Most Valuable Asset')
    body(doc, 'Airbnb\'s search algorithm weights reviews more heavily than any other single factor. A listing with a 4.9 rating and 50 reviews will appear above a listing with 4.5 and 200 reviews in most search scenarios. Reviews are not just social proof — they are your primary ranking signal.')
    body(doc, 'Beyond search ranking, reviews drive two key commercial outcomes: higher booking conversion (guests are 3× more likely to book a 4.9-star listing over a 4.5-star listing at the same price) and pricing power (a 4.9-star listing can command a 15–25% premium over a 4.5-star equivalent in the same market).')

    info_box(doc, 'Superhost status requires: 4.8+ average rating, 10+ stays per year, 90%+ response rate, and <1% cancellation rate. Superhost badges increase booking rates by approximately 20–30% on average.')

    section_header(doc, 2, 'The 6 Rating Categories — What Guests Evaluate')
    body(doc, 'Airbnb asks guests to rate 6 specific categories. Understanding what each category truly measures allows you to address each systematically.')

    two_col_table(doc,
        ['Category', 'What Guests Actually Assess', 'Key Drivers'],
        [
            ['Overall Experience', 'Holistic impression — did the stay match expectations?', 'Accuracy of listing, no negative surprises, welcome experience'],
            ['Cleanliness', 'Hygiene, freshness and presentation standards', 'Cleaning SOP execution, linen quality, bathroom condition'],
            ['Accuracy', 'Did the listing accurately represent the property?', 'No misleading photos, honest descriptions, no hidden fees'],
            ['Check-In', 'Ease, clarity and warmth of arrival process', 'Clear instructions, functional lockbox, working code, welcome'],
            ['Communication', 'Response speed, helpfulness and professionalism', 'Response time, tone, anticipating questions before they\'re asked'],
            ['Location', 'Transport, proximity to amenities, area feel', 'Primarily fixed — but can be managed with accurate description'],
            ['Value', 'Did they feel the price was fair for what they received?', 'Pricing relative to competitors, quality of welcome pack, amenities'],
        ],
        col_widths_cm=[3.0, 5.5, 9.0]
    )

    section_header(doc, 3, 'The Top 10 Drivers of 5-Star Reviews')
    body(doc, 'Based on analysis of Airbnb review text across thousands of listings, these are the factors guests mention most frequently in positive reviews. Execute these consistently and 5-star reviews become the default result.')

    two_col_table(doc,
        ['Rank', 'Driver', 'How to Deliver It'],
        [
            ['1', 'Cleanliness (immaculate standard)', 'Execute the Cleaning SOP — no shortcuts, every item checked'],
            ['2', 'Host communication (fast & warm)', 'Sub-1-hour responses. Friendly tone. Anticipate questions proactively.'],
            ['3', 'Welcome surprise (local treat or note)', 'Budget £4–8 per booking. Return on investment in reviews is enormous.'],
            ['4', 'Quality of bedding (hotel-standard)', 'Invest in 200+ thread count sheets and quality duvets. Replace annually.'],
            ['5', 'Accurate listing (no surprises)', 'Review your listing quarterly. Update anything that has changed.'],
            ['6', 'Fast WiFi (test regularly)', 'Run speed test monthly. Call provider immediately if speed drops below 50Mbps.'],
            ['7', 'Smooth self check-in', 'Test your lockbox code monthly. Always confirm code works day before arrival.'],
            ['8', 'Good local recommendations', 'Keep your House Manual recommendations genuinely current and personal.'],
            ['9', 'Well-stocked kitchen', 'Espresso machine with pods is mentioned in reviews more than any other appliance.'],
            ['10', 'Comfortable temperature', 'Ensure heating/cooling is working before every check-in. Pre-set to 19°C.'],
        ],
        col_widths_cm=[1.0, 4.5, 12.0]
    )

    section_header(doc, 4, 'Review Request Strategy')
    body(doc, 'The timing and phrasing of your review request directly impacts how many reviews you receive. Follow this approach for maximum conversion.')

    heading2(doc, 'Timing')
    bullet(doc, 'Send the post-checkout message (Template 08) within 1 hour of check-out time — not immediately when they leave, but around the scheduled check-out time')
    bullet(doc, 'Do not wait 24+ hours — the guest\'s positive feelings are strongest in the first few hours after checkout')
    bullet(doc, 'Airbnb sends its own review reminder — your message supplements this and makes it personal')
    bullet(doc, 'If the guest does not review within 5 days, a gentle one-time follow-up is acceptable')

    heading2(doc, 'Framing Your Request')
    body(doc, 'The most effective review requests have three elements: genuine thanks, an honest acknowledgment of the value reviews provide to small independent hosts, and a reciprocal commitment to leave them a positive review.')
    info_box(doc, 'What NOT to do: Do not ask guests to leave "5 stars" or "a positive review." This violates Airbnb\'s policies and, if detected, can result in review removal. Ask for an honest review only.')

    section_header(doc, 5, 'Responding to Reviews — Framework & Templates')

    heading2(doc, 'The 3-Part Response Formula')
    process_steps(doc, [
        ('1', 'Acknowledge', 'Thank the guest by name. Reference something specific about their stay.'),
        ('2', 'Respond', 'If any criticism was mentioned: brief factual response. No defensiveness. No over-explaining.'),
        ('3', 'Close', 'Invite them back. Wish them well. Sign with your name.'),
    ])

    heading3(doc, 'Responding to 5-Star Reviews')
    body(doc, 'Keep responses warm but brief. Long responses to positive reviews look performative. 2–4 sentences is ideal.')
    message_template_box(doc,
        'RESPONSE TEMPLATE',
        '5-Star Review Response',
        """Thank you so much, [NAME] — what a wonderful review! It was a genuine pleasure having you stay at [PROPERTY NAME] and I'm thrilled everything was to your liking.

I hope to welcome you back to [LOCATION] again soon. Safe travels!

[YOUR NAME]"""
    )

    heading3(doc, 'Responding to 4-Star Reviews (Minor Issue Mentioned)')
    message_template_box(doc,
        'RESPONSE TEMPLATE',
        '4-Star Review — Minor Issue',
        """Thank you for your kind review, [NAME], and for taking the time to share your feedback. I'm really glad you enjoyed your stay overall.

I appreciate your note about [SPECIFIC ISSUE]. [BRIEF RESPONSE — e.g., "I've already arranged for the [item] to be replaced/repaired before the next guests arrive."] I'm always looking to improve and feedback like this is exactly what helps.

It would be lovely to welcome you back again. All the best,
[YOUR NAME]"""
    )

    heading3(doc, 'Responding to Negative Reviews (3 Stars or Below)')
    body(doc, 'Negative review responses are read by future guests as much as the review itself. A calm, professional response to a negative review often converts more future guests than a listing full of 5-stars with no responses.')
    message_template_box(doc,
        'RESPONSE TEMPLATE',
        'Negative Review — Professional Response',
        """Thank you for sharing your feedback, [NAME]. I\'m sorry to hear that [PROPERTY NAME] didn\'t fully meet your expectations on this occasion.

[BRIEF FACTUAL RESPONSE TO THE SPECIFIC POINT — be factual, not defensive. If the complaint was valid: "You are absolutely right and I have since [action taken]." If the complaint was inaccurate or unfair: "To give future guests full context, [factual clarification in one sentence]."]

I genuinely value all feedback as it helps me continue improving. I wish you well in your future travels.

[YOUR NAME]"""
    )

    section_header(doc, 6, 'Handling Unfair or False Reviews')
    body(doc, 'Airbnb allows hosts to request review removal only in very specific circumstances. Understanding these circumstances prevents wasted time on unwinnable disputes.')

    two_col_table(doc,
        ['Situation', 'Airbnb Policy', 'Recommended Action'],
        [
            ['Review contains factually incorrect information', 'May be eligible for removal if provably false', 'Submit removal request with evidence. Respond publicly in the meantime.'],
            ['Guest left 1-star review after a dispute you won', 'Not automatically removable due to disagreement', 'Respond calmly and factually in public response.'],
            ['Review violates content policy (personal attacks, hate speech)', 'Eligible for removal — flag immediately', 'Report via Resolution Centre. Screenshot for your records.'],
            ['Guest did not actually stay (booking cancelled before)', 'May be removable', 'Contact Airbnb support with booking reference.'],
            ['Review was left in retaliation for a legitimate damage claim', 'Difficult to remove but document everything', 'Respond professionally. Evidence of damage claim provides context.'],
        ],
        col_widths_cm=[4.0, 4.5, 9.0]
    )

    amber_box(doc, 'The 14-day window: Both hosts and guests have 14 days to leave a review. Guests cannot see your review of them until they submit their own (or until the 14-day window closes). Leave thoughtful reviews of every guest — even difficult ones. Accurate, fair feedback protects the Airbnb community.')

    section_header(doc, 7, 'Building Review Velocity as a New Host')
    body(doc, 'New listings start with zero reviews. Airbnb\'s algorithm deprioritises zero-review listings. The first 5 reviews are disproportionately important — they establish your baseline and unlock the algorithm.')

    heading2(doc, 'New Host Acceleration Strategy')
    bullet(doc, 'Price 15–20% below market for the first 5 bookings — prioritise reviews over revenue in your first month')
    bullet(doc, 'Start with shorter minimum stays (2–3 nights) to accumulate more bookings and reviews faster')
    bullet(doc, 'Personally review every guest immediately after checkout — guests who receive a review are 40% more likely to leave one')
    bullet(doc, 'Enable Instant Book — it increases booking volume significantly for new listings')
    bullet(doc, 'Maximise your response rate to 100% in the first 90 days — this signals reliability to the algorithm')
    bullet(doc, 'Invest extra in the welcome pack for early guests — these are your review-building bookings')

    info_box(doc, 'Target milestone: 10 reviews with a 4.8+ average unlocks Superhost eligibility and dramatically increases your search visibility. Most hosts can achieve this in 60–90 days from launch with the right strategy.')

    path = f'{BASE}/05-SOP-Library/08-Review-Strategy-Guide.docx'
    doc.save(path)
    print(f'  ✓ 08-Review-Strategy-Guide.docx')


# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == '__main__':
    print('Building Airbnb Host Starter Kit — DOCX Documents...')
    print()
    build_quick_start()
    build_listing_guide()
    build_message_templates()
    build_house_rules()
    build_house_manual()
    build_checkin_sop()
    build_cleaning_sop()
    build_review_guide()
    print()
    print('All 8 DOCX documents complete.')
