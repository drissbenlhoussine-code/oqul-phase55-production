"""
DOCX builder for Bookkeeper Practice Launch System v2.0
Uses python-docx to create premium Word documents with cover pages,
headers/footers, tables, callout boxes, and consistent brand styling.
"""
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy, os

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/v2'

# ── Brand Colors ──────────────────────────────────────────────────────────────
PRIMARY    = RGBColor(0x0F, 0x76, 0x6E)
SECONDARY  = RGBColor(0x0F, 0x17, 0x2A)
ACCENT     = RGBColor(0xD9, 0x77, 0x06)
BG         = RGBColor(0xF8, 0xFA, 0xFC)
CARD       = RGBColor(0xFF, 0xFF, 0xFF)
BORDER     = RGBColor(0xE2, 0xE8, 0xF0)
MUTED      = RGBColor(0x64, 0x74, 0x8B)
SUCCESS    = RGBColor(0x10, 0xB9, 0x81)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_PRI  = RGBColor(0xCC, 0xFB, 0xF1)
LIGHT_ACC  = RGBColor(0xFE, 0xF3, 0xC7)
LIGHT_BLUE = RGBColor(0xEF, 0xF6, 0xFF)


# ── XML Helpers ───────────────────────────────────────────────────────────────

def set_cell_bg(cell, rgb: RGBColor):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), f'{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}')
    tcPr.append(shd)


def set_cell_borders(cell, color=BORDER, size=4, sides=('top','bottom','left','right')):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    hex_color = f'{color[0]:02X}{color[1]:02X}{color[2]:02X}'
    for side in sides:
        border = OxmlElement(f'w:{side}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), str(size))
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), hex_color)
        tcBorders.append(border)
    tcPr.append(tcBorders)


def set_table_borders(table, color=BORDER, size=4):
    for row in table.rows:
        for cell in row.cells:
            set_cell_borders(cell, color, size)


def remove_table_borders(table):
    for row in table.rows:
        for cell in row.cells:
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcBorders = OxmlElement('w:tcBorders')
            for side in ('top','bottom','left','right','insideH','insideV'):
                b = OxmlElement(f'w:{side}')
                b.set(qn('w:val'), 'none')
                b.set(qn('w:sz'), '0')
                b.set(qn('w:space'), '0')
                b.set(qn('w:color'), 'auto')
                tcBorders.append(b)
            tcPr.append(tcBorders)


def set_run_font(run, name, size_pt, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color
    # Also set eastAsia and ascii
    rPr = run._r.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), name)
    rFonts.set(qn('w:hAnsi'), name)
    rFonts.set(qn('w:eastAsia'), name)
    existing = rPr.find(qn('w:rFonts'))
    if existing is not None:
        rPr.remove(existing)
    rPr.insert(0, rFonts)


def para_spacing(para, before=0, after=6):
    pPr = para._p.get_or_add_pPr()
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:before'), str(before * 20))
    spacing.set(qn('w:after'), str(after * 20))
    existing = pPr.find(qn('w:spacing'))
    if existing is not None:
        pPr.remove(existing)
    pPr.append(spacing)


def set_para_bg(para, rgb: RGBColor):
    pPr = para._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), f'{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}')
    existing = pPr.find(qn('w:shd'))
    if existing is not None:
        pPr.remove(existing)
    pPr.append(shd)


def set_cell_margins(cell, top=60, bottom=60, left=120, right=120):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for side, val in (('top', top), ('bottom', bottom), ('left', left), ('right', right)):
        m = OxmlElement(f'w:{side}')
        m.set(qn('w:w'), str(val))
        m.set(qn('w:type'), 'dxa')
        tcMar.append(m)
    existing = tcPr.find(qn('w:tcMar'))
    if existing is not None:
        tcPr.remove(existing)
    tcPr.append(tcMar)


def set_cell_valign(cell, align='center'):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    vAlign = OxmlElement('w:vAlign')
    vAlign.set(qn('w:val'), align)
    existing = tcPr.find(qn('w:vAlign'))
    if existing is not None:
        tcPr.remove(existing)
    tcPr.append(vAlign)


def add_page_number(paragraph):
    """Add auto page number field to a paragraph."""
    run = paragraph.add_run()
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.text = 'PAGE'
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)
    set_run_font(run, 'Inter', 8, color=MUTED)


# ── Document Factory ──────────────────────────────────────────────────────────

def new_doc():
    doc = Document()
    # Page margins
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)
    # Remove default paragraph spacing
    doc.styles['Normal'].font.name = 'Inter'
    doc.styles['Normal'].font.size = Pt(9.5)
    return doc


def add_header(doc, product_name='BOOKKEEPER PRACTICE LAUNCH SYSTEM', doc_title=''):
    """Add header with brand bar."""
    section = doc.sections[0]
    section.different_first_page_header_footer = True

    # Regular pages header
    header = section.header
    header.is_linked_to_previous = False
    for para in header.paragraphs:
        para.clear()

    # Header table: left = brand name, right = doc title
    htable = header.add_table(1, 2, width=Inches(6.5))
    htable.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Left cell - brand
    left_cell = htable.cell(0, 0)
    set_cell_bg(left_cell, SECONDARY)
    set_cell_margins(left_cell, top=80, bottom=80, left=150, right=80)
    lp = left_cell.paragraphs[0]
    lr = lp.add_run(product_name)
    set_run_font(lr, 'Poppins', 8.5, bold=True, color=WHITE)
    lp.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Right cell - doc title
    right_cell = htable.cell(0, 1)
    set_cell_bg(right_cell, PRIMARY)
    set_cell_margins(right_cell, top=80, bottom=80, left=80, right=150)
    rp = right_cell.paragraphs[0]
    rr = rp.add_run(doc_title)
    set_run_font(rr, 'Poppins', 8.5, bold=True, color=WHITE)
    rp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    remove_table_borders(htable)

    # Remove default header paragraph (it's already inside htable container)
    # Footer
    footer = section.footer
    footer.is_linked_to_previous = False
    for para in footer.paragraphs:
        para.clear()

    ftable = footer.add_table(1, 2, width=Inches(6.5))
    ftable.alignment = WD_TABLE_ALIGNMENT.CENTER

    left_fc = ftable.cell(0, 0)
    set_cell_margins(left_fc, top=60, bottom=60, left=0, right=60)
    lfp = left_fc.paragraphs[0]
    lfr = lfp.add_run('© 2025 Bookkeeper Practice Launch System v2.0  ·  Commercial Use License')
    set_run_font(lfr, 'Inter', 7.5, color=MUTED)
    lfp.alignment = WD_ALIGN_PARAGRAPH.LEFT

    right_fc = ftable.cell(0, 1)
    set_cell_margins(right_fc, top=60, bottom=60, left=60, right=0)
    rfp = right_fc.paragraphs[0]
    rfr = rfp.add_run('Page ')
    set_run_font(rfr, 'Inter', 7.5, bold=True, color=PRIMARY)
    add_page_number(rfp)
    rfp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    remove_table_borders(ftable)


def add_cover_page(doc, title, subtitle, section_label='', version='v2.0'):
    """Add a dark full-page cover using a table."""
    # Cover table (full page visual)
    cover_table = doc.add_table(rows=1, cols=1)
    cover_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = cover_table.cell(0, 0)
    set_cell_bg(cell, SECONDARY)
    set_cell_margins(cell, top=600, bottom=600, left=600, right=600)
    set_cell_valign(cell, 'center')

    # Section label
    if section_label:
        p_label = cell.add_paragraph()
        r_label = p_label.add_run(section_label.upper())
        set_run_font(r_label, 'Poppins', 8, bold=True, color=RGBColor(0x0F, 0x76, 0x6E))
        p_label.alignment = WD_ALIGN_PARAGRAPH.LEFT
        para_spacing(p_label, before=0, after=18)

    # Title
    p_title = cell.add_paragraph()
    r_title = p_title.add_run(title)
    set_run_font(r_title, 'Poppins', 28, bold=True, color=WHITE)
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    para_spacing(p_title, before=0, after=12)

    # Subtitle
    p_sub = cell.add_paragraph()
    r_sub = p_sub.add_run(subtitle)
    set_run_font(r_sub, 'Inter', 12, color=RGBColor(0x94, 0xA3, 0xB8))
    p_sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    para_spacing(p_sub, before=0, after=36)

    # Divider bar (using a small table inside)
    div_table = cell.add_table(rows=1, cols=1)
    div_cell = div_table.cell(0, 0)
    set_cell_bg(div_cell, PRIMARY)
    set_cell_margins(div_cell, top=20, bottom=20, left=0, right=0)
    dp = div_cell.paragraphs[0]
    dp.add_run(' ')
    remove_table_borders(div_table)

    # Version
    p_ver = cell.add_paragraph()
    para_spacing(p_ver, before=24, after=0)
    r_ver = p_ver.add_run(f'VERSION {version}  ·  2025  ·  PREMIUM EDITION')
    set_run_font(r_ver, 'Poppins', 8, bold=True, color=ACCENT)
    p_ver.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Copyright
    p_copy = cell.add_paragraph()
    para_spacing(p_copy, before=60, after=0)
    r_copy = p_copy.add_run('Bookkeeper Practice Launch System  ·  Single-Practice Commercial Use License')
    set_run_font(r_copy, 'Inter', 7.5, color=RGBColor(0x47, 0x55, 0x69))
    p_copy.alignment = WD_ALIGN_PARAGRAPH.LEFT

    remove_table_borders(cover_table)
    doc.add_page_break()


# ── Paragraph Helpers ─────────────────────────────────────────────────────────

def h1(doc, text, color=SECONDARY):
    p = doc.add_paragraph()
    r = p.add_run(text)
    set_run_font(r, 'Poppins', 18, bold=True, color=color)
    para_spacing(p, before=12, after=6)
    return p


def h2(doc, text, color=PRIMARY):
    p = doc.add_paragraph()
    r = p.add_run(text)
    set_run_font(r, 'Poppins', 13, bold=True, color=color)
    para_spacing(p, before=10, after=4)
    return p


def h3(doc, text, color=SECONDARY):
    p = doc.add_paragraph()
    r = p.add_run(text)
    set_run_font(r, 'Poppins', 11, bold=True, color=color)
    para_spacing(p, before=8, after=3)
    return p


def body(doc, text, color=SECONDARY, size=9.5, italic=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    set_run_font(r, 'Inter', size, italic=italic, color=color)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    para_spacing(p, before=0, after=4)
    return p


def bullet(doc, text, color=SECONDARY):
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run(text)
    set_run_font(r, 'Inter', 9.5, color=color)
    para_spacing(p, before=0, after=2)
    return p


def section_bar(doc, text, bg=PRIMARY):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0)
    set_cell_bg(cell, bg)
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    p = cell.paragraphs[0]
    r = p.add_run(text.upper())
    set_run_font(r, 'Poppins', 10, bold=True, color=WHITE)
    remove_table_borders(t)
    sp = doc.add_paragraph()
    para_spacing(sp, before=0, after=4)
    return t


def callout(doc, text, heading='', style='info'):
    bg_map = {'info': LIGHT_PRI, 'warning': LIGHT_ACC, 'tip': LIGHT_BLUE,
              'important': RGBColor(0xFE, 0xF2, 0xF2)}
    border_map = {'info': PRIMARY, 'warning': ACCENT,
                  'tip': RGBColor(0x3B, 0x82, 0xF6), 'important': RGBColor(0xEF, 0x44, 0x44)}
    bg = bg_map.get(style, LIGHT_PRI)
    bd = border_map.get(style, PRIMARY)

    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = t.cell(0, 0)
    set_cell_bg(cell, bg)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    set_cell_borders(cell, bd, 12, ('left',))
    set_cell_borders(cell, RGBColor(0xE2, 0xE8, 0xF0), 4, ('top', 'bottom', 'right'))

    if heading:
        ph = cell.add_paragraph()
        rh = ph.add_run(heading)
        set_run_font(rh, 'Poppins', 9.5, bold=True, color=bd)
        para_spacing(ph, before=0, after=4)

    pb = cell.paragraphs[0] if not heading else cell.add_paragraph()
    rb = pb.add_run(text)
    set_run_font(rb, 'Inter', 9, color=SECONDARY)
    para_spacing(pb, before=0, after=0)

    sp = doc.add_paragraph()
    para_spacing(sp, before=0, after=6)
    return t


def premium_table(doc, headers, rows, col_widths_cm=None):
    """Create a premium styled table."""
    n_cols = len(headers)
    t = doc.add_table(rows=1 + len(rows), cols=n_cols)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = 'Table Grid'

    if col_widths_cm:
        for i, w in enumerate(col_widths_cm):
            for row in t.rows:
                row.cells[i].width = Cm(w)

    # Header row
    for j, h in enumerate(headers):
        cell = t.cell(0, j)
        set_cell_bg(cell, PRIMARY)
        set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        set_run_font(r, 'Poppins', 8.5, bold=True, color=WHITE)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Data rows
    for i, row_data in enumerate(rows):
        bg = CARD if i % 2 == 0 else BG
        for j, val in enumerate(row_data):
            cell = t.cell(i + 1, j)
            set_cell_bg(cell, bg)
            set_cell_borders(cell, BORDER, 4)
            set_cell_margins(cell, top=60, bottom=60, left=120, right=120)
            p = cell.paragraphs[0]
            r = p.add_run(str(val))
            set_run_font(r, 'Inter', 8.5, color=SECONDARY)

    sp = doc.add_paragraph()
    para_spacing(sp, before=0, after=6)
    return t


def save(doc, path):
    doc.save(path)
    print(f'  ✓ {os.path.basename(path)}')


# ══════════════════════════════════════════════════════════════════════════════
# 1. START HERE v2 (DOCX)
# ══════════════════════════════════════════════════════════════════════════════

def build_start_here():
    doc = new_doc()
    add_cover_page(doc, 'Start Here', 'Your 90-minute launch guide to the complete system', '00 — START HERE')
    add_header(doc, doc_title='Start Here')

    h1(doc, 'Welcome to Bookkeeper Practice Launch System v2.0')
    body(doc, 'You now have a complete operating system for your bookkeeping practice. '
         'This guide shows you exactly how to set it up in 90 minutes.')
    callout(doc, 'Read this file before opening anything else. It tells you what to do, in what order, and why.', style='info', heading='Start Here')
    doc.add_paragraph()

    section_bar(doc, 'What Is Included')
    doc.add_paragraph()
    premium_table(doc,
        ['Folder', 'Purpose'],
        [
            ['00-START-HERE', 'Orientation, setup guides, and file inventory'],
            ['01-Quick-Reference', 'License, FAQ, version history, support guide'],
            ['02-Practice-Dashboard', 'Excel dashboard — your daily operations hub'],
            ['03-Client-Documents', 'Service guide, proposal, agreement, intake, deck'],
            ['04-Operations-Library', 'SOPs, checklists, and communication scripts'],
            ['05-Notion-Workspace', '7 CSV databases and Notion setup guide'],
        ],
        col_widths_cm=[5.5, 13]
    )

    section_bar(doc, '90-Minute Setup Sequence')
    doc.add_paragraph()
    steps = [
        ('Step 1 — Read the guides (10 min)', 'Read this file, then Installation-Guide.pdf in 00-START-HERE.'),
        ('Step 2 — Customize the Dashboard (20 min)', 'Open 02-Practice-Dashboard/Bookkeeper-Practice-Dashboard-v2.xlsx. Fill in the yellow Setup cells with your practice name, services, and pricing.'),
        ('Step 3 — Customize Client Documents (25 min)', 'Replace all [BRACKETED TEXT] in the 5 files in 03-Client-Documents. Use Find & Replace in Word (Ctrl+H).'),
        ('Step 4 — Build your Notion Workspace (15 min)', 'Follow the Notion-Setup-Guide.pdf in 05-Notion-Workspace. Import all 7 CSV files and connect them.'),
        ('Step 5 — Add test data and review (15 min)', 'Add 2-3 sample clients. Confirm KPIs populate on the Dashboard sheet.'),
        ('Step 6 — Read License & FAQ (5 min)', 'Review 01-Quick-Reference/License.pdf before sending anything to clients.'),
    ]
    for title, desc in steps:
        h3(doc, title)
        body(doc, desc)
        doc.add_paragraph()

    section_bar(doc, 'Core Client Workflow')
    doc.add_paragraph()
    premium_table(doc,
        ['Stage', 'Action', 'File'],
        [
            ['Lead', 'Qualify entity, volume, software, and urgency', 'Lead Pipeline (Dashboard)'],
            ['Diagnostic', 'Review books, backlog, accounts, and reporting needs', 'Client-Intake-and-Onboarding-Pack-v2.docx'],
            ['Proposal', 'Define scope, assumptions, cleanup, and fee', 'Bookkeeping-Proposal-Template-v2.docx'],
            ['Engagement', 'Sign terms, collect payment, confirm responsibilities', 'Bookkeeping-Engagement-Agreement-v2.docx'],
            ['Onboarding', 'Collect access, chart of accounts, documents', 'Client-Intake-and-Onboarding-Pack-v2.docx'],
            ['Monthly Close', 'Reconcile, review, adjust, report, document', 'Dashboard + SOPs-and-Checklists-v2.docx'],
            ['Client Review', 'Deliver reports, explain exceptions, confirm next steps', 'Client-Portal (Notion) + Scripts'],
        ],
        col_widths_cm=[4, 7.5, 7]
    )

    callout(doc,
        'This product supports bookkeeping operations only. It is not accounting, tax, legal, '
        'audit, assurance, payroll, or regulatory advice. Adapt all files to your credentials, '
        'jurisdiction, and permitted professional scope.',
        style='important', heading='Professional Notice')

    save(doc, f'{OUT}/00-START-HERE/Start-Here-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 2. Bookkeeping Service Guide v2
# ══════════════════════════════════════════════════════════════════════════════

def build_service_guide():
    doc = new_doc()
    add_cover_page(doc, 'Bookkeeping Service Guide',
                   'Your complete guide to our services, packages, and process',
                   '03 — CLIENT DOCUMENTS')
    add_header(doc, doc_title='Bookkeeping Service Guide')

    callout(doc, 'Replace all [BRACKETED TEXT] with your practice details before sending to clients. '
            'This is a client-facing document.', style='warning', heading='Customization Required')
    doc.add_paragraph()

    h1(doc, 'What Monthly Bookkeeping Includes')
    body(doc, 'Every monthly bookkeeping engagement with [PRACTICE NAME] includes the following core services:')
    for item in [
        'Transaction categorization and ledger review',
        'Bank and credit-card reconciliations for all accounts',
        'Balance-sheet account review and cleanup',
        'Monthly financial statements (Profit & Loss and Balance Sheet)',
        'Exception log and missing-document requests',
        'Agreed monthly communication and close cadence',
        'Secure document delivery via client portal',
    ]:
        bullet(doc, item)
    doc.add_paragraph()

    section_bar(doc, 'Service Packages')
    doc.add_paragraph()
    premium_table(doc,
        ['Package', 'Typical Scope', 'Includes', 'Starting Price'],
        [
            ['Essentials', 'Up to [X] accounts and [X] monthly transactions', 'Monthly P&L, Balance Sheet, and bank reconciliations', '€[ ] / month'],
            ['Growth', 'Higher volume, class or location tracking', 'All Essentials + monthly review call and cash summary', '€[ ] / month'],
            ['Advanced', 'Multi-entity or complex workflows', 'All Growth + custom reporting and priority support', '€[ ] / month'],
            ['Tax Ready Add-On', 'Year-end package preparation', 'Tax document checklist + preparer coordination', '€[ ] / year'],
        ],
        col_widths_cm=[3.5, 5.5, 6.5, 3]
    )

    section_bar(doc, 'Optional Project Services')
    doc.add_paragraph()
    premium_table(doc,
        ['Service', 'Description', 'Pricing'],
        [
            ['Catch-up / Cleanup Bookkeeping', 'Bring overdue or disorganized books current', 'Quote after diagnostic'],
            ['Historical Reconciliations', 'Reconcile prior months or years', 'Quote after diagnostic'],
            ['Chart-of-Accounts Redesign', 'Rebuild your account structure for clarity and reporting', 'Fixed fee: €[ ]'],
            ['Software Migration & Setup', 'Move from one platform to another (e.g., Wave to QBO)', 'Quote per project'],
            ['Accounts Payable / Receivable Support', 'Invoice management and payment tracking assistance', '€[ ] / month add-on'],
        ],
        col_widths_cm=[5, 7.5, 6]
    )

    section_bar(doc, 'What Is Not Included')
    doc.add_paragraph()
    callout(doc,
        'The following services are outside the scope of bookkeeping unless separately '
        'contracted and legally permitted in your jurisdiction: tax advice and returns, '
        'audit and assurance services, payroll processing, legal advice, regulatory '
        'compliance guidance, CFO or controller services.',
        style='important', heading='Service Boundaries')
    doc.add_paragraph()

    section_bar(doc, 'Client Responsibilities')
    doc.add_paragraph()
    body(doc, 'A successful engagement depends on your active participation. Clients are responsible for:')
    for item in [
        'Providing complete and accurate records by the agreed deadline each month',
        'Maintaining secure account access and approving role-based software invitations',
        'Answering transaction questions promptly (within [X] business days)',
        'Retaining original source documents for the required period',
        'Reviewing reports and notifying us of errors or material events',
        'Working with a qualified tax professional for tax advice and filings',
    ]:
        bullet(doc, item)
    doc.add_paragraph()

    section_bar(doc, 'Monthly Timeline')
    doc.add_paragraph()
    premium_table(doc,
        ['Day of Month', 'Activity', 'Who'],
        [
            ['Days 1–5', 'Client provides bank statements, payroll reports, loan records, and missing documents', 'Client'],
            ['Days 5–12', 'Bookkeeper imports transactions, categorizes, reconciles, and raises questions', 'Bookkeeper'],
            ['Days 12–18', 'Client answers questions; bookkeeper completes review and adjusting entries', 'Both'],
            ['By Day [X]', 'Reports and action summary delivered through the secure portal', 'Bookkeeper'],
        ],
        col_widths_cm=[3.5, 11, 4]
    )

    section_bar(doc, 'Security & Access')
    doc.add_paragraph()
    callout(doc,
        'We use secure client portals, read-only accountant access, and approved password '
        'managers. We will never ask you to share banking passwords by email. All document '
        'exchange happens through your secure portal at [PORTAL LINK].',
        style='info', heading='Your Data Is Secure')

    save(doc, f'{OUT}/03-Client-Documents/Bookkeeping-Service-Guide-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 3. Client Intake & Onboarding Pack v2
# ══════════════════════════════════════════════════════════════════════════════

def build_intake_pack():
    doc = new_doc()
    add_cover_page(doc, 'Client Intake &\nOnboarding Pack',
                   'Collect everything needed for a clean, confident start',
                   '03 — CLIENT DOCUMENTS')
    add_header(doc, doc_title='Client Intake & Onboarding Pack')

    callout(doc, 'Replace all [BRACKETED TEXT] before sending. Complete Sections 1-4 with the client during or before the kickoff call.', style='warning', heading='Customization Required')
    doc.add_paragraph()

    h1(doc, 'Section 1 — Business Profile')
    premium_table(doc,
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
        col_widths_cm=[7, 11.5]
    )

    h1(doc, 'Section 2 — Volume & Complexity')
    premium_table(doc,
        ['Question', 'Response'],
        [
            ['Avg. monthly bank & card transactions', ''],
            ['Number of bank accounts', ''],
            ['Number of credit cards', ''],
            ['Payroll provider & employee count', ''],
            ['Loans / lines of credit', ''],
            ['Inventory (YES/NO + details)', ''],
            ['Sales channels & payment processors', ''],
            ['Foreign currency or cross-border activity', ''],
            ['Class, project, or location tracking', ''],
            ['Last fully reconciled month', ''],
            ['Known backlogs or issues', ''],
        ],
        col_widths_cm=[8, 10.5]
    )

    h1(doc, 'Section 3 — Documents Requested')
    body(doc, 'Please upload the following documents to your secure portal at [PORTAL LINK] '
         'before the kickoff call:')
    for item in [
        'Prior-year financial statements and trial balance',
        'Bank and credit-card statements from the agreed start date',
        'Loan statements and amortization schedules',
        'Payroll summaries and payroll tax liability reports',
        'Sales-tax / VAT filings and notices',
        'Merchant processor and e-commerce reports',
        'Fixed-asset list with purchase dates and costs',
        'Outstanding accounts receivable and payable aging reports',
        'Tax return or tax-preparer adjusting entries (where appropriate)',
    ]:
        bullet(doc, item)
    doc.add_paragraph()

    callout(doc,
        'Never email banking passwords. Use secure portals, read-only accountant access, '
        'or an approved password manager only.',
        style='important', heading='Security Notice')
    doc.add_paragraph()

    h1(doc, 'Section 4 — Kickoff Decisions')
    premium_table(doc,
        ['Decision', 'Agreed Approach'],
        [
            ['Monthly close deadline', ''],
            ['Document cutoff day (day statements are available)', ''],
            ['Primary question / approval contact', ''],
            ['Preferred communication channel', ''],
            ['Report package (P&L, Balance Sheet, Cash, Custom)', ''],
            ['Escalation process for urgent items', ''],
            ['First close period', ''],
            ['Cleanup scope and start date (if applicable)', ''],
        ],
        col_widths_cm=[7, 11.5]
    )

    h1(doc, 'Section 5 — Access & Integration Checklist')
    premium_table(doc,
        ['Access Item', 'Status', 'Notes'],
        [
            ['Bookkeeping software (accountant role)', '[ ] Granted', ''],
            ['Bank feed connection or read-only access', '[ ] Granted', ''],
            ['Payroll platform (read-only)', '[ ] Granted', ''],
            ['Payment processor / e-commerce reports', '[ ] Granted', ''],
            ['Client portal invitation accepted', '[ ] Accepted', ''],
            ['Document upload folder shared', '[ ] Shared', ''],
        ],
        col_widths_cm=[7.5, 3, 8]
    )

    callout(doc,
        'Send this completed pack to [PRACTICE NAME] at [EMAIL] or upload to your '
        'secure portal before the kickoff call. A written summary will be sent after '
        'the call confirming all decisions.',
        style='info', heading='Submission Instructions')

    save(doc, f'{OUT}/03-Client-Documents/Client-Intake-and-Onboarding-Pack-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 4. Bookkeeping Proposal Template v2
# ══════════════════════════════════════════════════════════════════════════════

def build_proposal():
    doc = new_doc()
    add_cover_page(doc, 'Bookkeeping Services\nProposal',
                   'Prepared for [CLIENT COMPANY] by [PRACTICE NAME]',
                   '03 — CLIENT DOCUMENTS')
    add_header(doc, doc_title='Bookkeeping Services Proposal')

    callout(doc, 'Complete the [BRACKETED] fields for each client. Replace sample figures with real ones from your diagnostic.', style='warning', heading='Customization Required')
    doc.add_paragraph()

    # Proposal meta
    premium_table(doc,
        ['Proposal Detail', 'Information'],
        [
            ['Prepared For', '[CLIENT COMPANY]'],
            ['Contact Name', '[NAME / TITLE]'],
            ['Prepared By', '[PRACTICE NAME]'],
            ['Proposal Date', '[DATE]'],
            ['Valid Until', '[DATE + 14 days]'],
            ['Engagement Start', '[PROPOSED START DATE]'],
        ],
        col_widths_cm=[5, 13.5]
    )

    h1(doc, '1. Current Situation')
    body(doc, '[Summarize the client\'s current books, backlog, risks, software, reporting needs, '
         'and the outcome they are trying to achieve. Be specific — reference what you found '
         'in the diagnostic call. This section shows the client you understand their situation.]')
    doc.add_paragraph()

    h1(doc, '2. Recommended Scope')
    premium_table(doc,
        ['Service', 'Cadence', 'What Is Included'],
        [
            ['Bookkeeping', 'Monthly', 'Transaction categorization, reconciliation, review, and agreed adjusting entries'],
            ['Financial Reporting', 'Monthly', 'Profit & Loss, Balance Sheet, and [additional reports agreed]'],
            ['Client Questions', 'Monthly', 'Consolidated exception list and documented follow-up'],
            ['Review Meeting', '[Cadence]', '[Duration] review call with [participants]'],
            ['Cleanup Project', 'One-time', '[Months / accounts / issues included in cleanup scope]'],
        ],
        col_widths_cm=[4, 3, 11.5]
    )

    h1(doc, '3. Implementation Plan')
    premium_table(doc,
        ['Phase', 'Activity', 'Timeline'],
        [
            ['1', 'Engagement signed and initial payment received', 'Day 1'],
            ['2', 'Secure access granted and documents uploaded', 'Days 1–5'],
            ['3', 'Diagnostic review and opening-balance confirmation', 'Week 1'],
            ['4', 'Cleanup or conversion work (if applicable)', 'Weeks 2–[X]'],
            ['5', 'First monthly close completed', '[Month / Year]'],
            ['6', 'Report delivery and process refinement call', 'After first close'],
        ],
        col_widths_cm=[1.5, 11, 6]
    )

    h1(doc, '4. Investment')
    premium_table(doc,
        ['Item', 'Fee', 'Billing'],
        [
            ['Setup / Diagnostic Fee', '€[ ]', 'Due on acceptance'],
            ['Cleanup Project', '€[ ]', '[Schedule — e.g., 50% on start, 50% on delivery]'],
            ['Monthly Bookkeeping', '€[ ] / month', 'Monthly in advance, first day of service month'],
            ['Additional Work', '€[ ] / hour', 'With written approval before commencement'],
        ],
        col_widths_cm=[7, 3.5, 8]
    )

    callout(doc,
        'Pricing assumes the transaction volume, account count, software, and book condition '
        'described above. Material changes in scope or volume after engagement start may '
        'require a pricing review with [X] days written notice.',
        style='info', heading='Pricing Assumptions')
    doc.add_paragraph()

    h1(doc, '5. Assumptions & Exclusions')
    for item in [
        'Pricing assumes books are in the condition described after diagnostic review.',
        'Tax advice, tax returns, audit and assurance, legal advice, and CFO services are excluded unless separately contracted and legally permitted.',
        'Client provides source documents and answers to questions by agreed monthly deadlines.',
        'Material scope or volume changes require a repricing discussion and written amendment.',
    ]:
        bullet(doc, item)
    doc.add_paragraph()

    h1(doc, '6. Acceptance')
    premium_table(doc,
        ['Field', 'Response'],
        [
            ['Selected scope', ''],
            ['Engagement start date', ''],
            ['Client name and title', ''],
            ['Client signature and date', ''],
            ['Practice representative', '[PRACTICE NAME]'],
            ['Practice signature and date', ''],
        ],
        col_widths_cm=[5.5, 13]
    )

    callout(doc,
        'Questions before accepting? Contact [PRACTICE NAME] at [EMAIL] or [PHONE]. '
        'This proposal expires on [DATE + 14 days].',
        style='tip', heading='Questions?')

    save(doc, f'{OUT}/03-Client-Documents/Bookkeeping-Proposal-Template-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 5. Engagement Agreement v2
# ══════════════════════════════════════════════════════════════════════════════

def build_engagement_agreement():
    doc = new_doc()
    add_cover_page(doc, 'Bookkeeping\nEngagement Agreement',
                   'Between [PRACTICE LEGAL NAME] and [CLIENT LEGAL NAME]',
                   '03 — CLIENT DOCUMENTS')
    add_header(doc, doc_title='Bookkeeping Engagement Agreement')

    callout(doc,
        'This is a general template — not legal advice. Have a qualified lawyer review '
        'it for your jurisdiction, credentials, privacy duties, and permitted services '
        'before sending to any client.',
        style='important', heading='Legal Review Required Before Use')
    doc.add_paragraph()

    h1(doc, 'Agreement Details')
    premium_table(doc,
        ['Party', 'Details'],
        [
            ['Practice Legal Name', '[PRACTICE LEGAL NAME]'],
            ['Practice Address', '[PRACTICE ADDRESS]'],
            ['Client Legal Name', '[CLIENT LEGAL NAME]'],
            ['Client Address', '[CLIENT ADDRESS]'],
            ['Agreement Date', '[DATE]'],
            ['Governed by the law of', '[JURISDICTION]'],
        ],
        col_widths_cm=[5, 13.5]
    )

    for i, (title, content) in enumerate([
        ('Services', 'The Practice will perform the bookkeeping services described in the attached Scope of Work. Services not expressly listed are excluded. The Scope of Work may be updated by written amendment signed by both parties.'),
        ('Client Responsibilities', 'Client remains responsible for all business decisions, internal controls, source records, transaction authorization, legal compliance, and the completeness and accuracy of all information supplied. The Practice relies on information provided by Client and does not independently verify source documents.'),
        ('No Assurance, Tax, or Legal Opinion', 'Unless separately agreed and legally permitted, this engagement does not include audit, review, assurance, tax advice, tax-return preparation, legal advice, fraud detection, forensic accounting, or independent verification of source information. Client should engage qualified tax and legal professionals for those services.'),
        ('Fees and Payment', 'Fees are [AMOUNT/STRUCTURE] as described in the attached Scope of Work. Invoices are due [TERMS]. Work may be suspended for overdue balances after [X] days written notice. Client remains responsible for fees for completed work during any suspension period.'),
        ('Access and Security', 'Both parties will maintain reasonable security controls and use role-based software access. Client will not transmit passwords through ordinary email. Each party will promptly notify the other of any suspected unauthorized access to systems or data.'),
        ('Deadlines and Delays', 'Delivery dates for reports and close schedules depend on timely receipt of records, responses, and approvals from Client. Client delays may shift the close and reporting dates by an equivalent period without penalty to the Practice.'),
        ('Corrections and Prior Periods', 'The Practice may correct bookkeeping errors identified during the engagement at no additional charge. Material prior-period work, cleanup, or adjustments outside the original scope require written approval and additional fees per the Scope of Work.'),
        ('Confidentiality and Privacy', 'Each party will protect the other\'s confidential information using at least reasonable care and will comply with applicable privacy obligations. Data-processing terms required by applicable law may be attached as a schedule to this Agreement.'),
        ('Third-Party Systems', 'The Practice is not responsible for outages, data loss, policy changes, fees, or errors caused by banks, accounting software platforms, payroll providers, payment processors, or any other third parties used in delivering services.'),
        ('Records and Retention', 'Client owns and is responsible for retaining original source documents for the legally required period. The Practice may retain working files and reports in accordance with its retention policy and applicable professional standards.'),
        ('Termination', 'Either party may terminate this Agreement with [NUMBER] days written notice. Client will pay for all completed work, work in progress, and non-cancellable costs incurred before the termination effective date. The Practice will deliver a final report package on termination.'),
        ('Limitation and Dispute Resolution', 'Liability limits, governing law, venue, and dispute resolution procedures must be customized for the applicable jurisdiction and reviewed by a qualified lawyer before use. [CUSTOMIZE FOR YOUR JURISDICTION]'),
        ('Entire Agreement', 'This Agreement and all attached schedules constitute the entire agreement between the parties regarding the subject matter herein and supersede all prior discussions. Changes require a written amendment signed by authorized representatives of both parties.'),
    ], 1):
        h2(doc, f'{i}. {title}')
        body(doc, content)
        doc.add_paragraph()

    section_bar(doc, 'Scope of Work')
    doc.add_paragraph()
    premium_table(doc,
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
        col_widths_cm=[5.5, 13]
    )

    section_bar(doc, 'Signatures')
    doc.add_paragraph()
    premium_table(doc,
        ['Party', 'Name & Title', 'Signature', 'Date'],
        [
            ['Client', '', '', ''],
            ['Practice', '[PRACTICE NAME]', '', ''],
        ],
        col_widths_cm=[2.5, 6, 5.5, 4.5]
    )

    save(doc, f'{OUT}/03-Client-Documents/Bookkeeping-Engagement-Agreement-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 6. SOPs & Checklists v2
# ══════════════════════════════════════════════════════════════════════════════

def build_sops():
    doc = new_doc()
    add_cover_page(doc, 'Bookkeeping SOPs\n& Checklists',
                   'Internal operating manual for onboarding, close, QC, and document collection',
                   '04 — OPERATIONS LIBRARY')
    add_header(doc, doc_title='Bookkeeping SOPs & Checklists')

    callout(doc, 'These are internal documents — not for clients. Customize the [BRACKETED TEXT] and adapt procedures to your tools and workflow.', style='warning', heading='Internal Use Only')
    doc.add_paragraph()

    h1(doc, 'SOP 1 — Client Onboarding')
    body(doc, 'Complete these steps for every new client before the first monthly close.')
    premium_table(doc,
        ['#', 'Action', 'Owner', 'Deadline'],
        [
            ['1', 'Confirm signed engagement agreement and initial payment received', '[OWNER]', 'Before kickoff'],
            ['2', 'Create client folder in [SYSTEM] with standard subfolder structure', '[OWNER]', 'Day 1'],
            ['3', 'Create client record in Notion (or CRM) with all profile data', '[OWNER]', 'Day 1'],
            ['4', 'Set up recurring tasks in [PROJECT TOOL] for monthly close cadence', '[OWNER]', 'Day 2'],
            ['5', 'Request secure accountant / user access to bookkeeping software', '[OWNER]', 'Day 2'],
            ['6', 'Request required source documents via secure portal', '[OWNER]', 'Day 2'],
            ['7', 'Capture entity type, fiscal year, accounting basis, accounts, integrations', '[OWNER]', 'Kickoff call'],
            ['8', 'Review opening balances and last fully reconciled period', '[OWNER]', 'Week 1'],
            ['9', 'Document known issues, cleanup scope, deadlines, and responsibilities', '[OWNER]', 'Week 1'],
            ['10', 'Run kickoff call and send written action summary within 24 hours', '[OWNER]', 'Week 1'],
        ],
        col_widths_cm=[1.5, 9, 3, 4]
    )

    h1(doc, 'SOP 2 — Monthly Close Checklist')
    premium_table(doc,
        ['Step', 'Control Point', 'Done'],
        [
            ['1', 'Confirm all bank, card, loan, payroll, and processor data is available', '[ ]'],
            ['2', 'Import / sync transactions and investigate duplicates or failed feeds', '[ ]'],
            ['3', 'Categorize all transactions; resolve uncategorized / suspense items', '[ ]'],
            ['4', 'Reconcile every bank and credit-card account to statements', '[ ]'],
            ['5', 'Reconcile loans, payroll liabilities, sales-tax/VAT liabilities, and clearing accounts', '[ ]'],
            ['6', 'Review accounts receivable, accounts payable, negative balances, and stale items', '[ ]'],
            ['7', 'Record approved accruals, prepayments, depreciation, or adjustments within scope', '[ ]'],
            ['8', 'Compare current month with prior month and budget; document material variances', '[ ]'],
            ['9', 'Run balance-sheet integrity and reasonableness checks', '[ ]'],
            ['10', 'Prepare consolidated client question list and obtain documented responses', '[ ]'],
            ['11', 'Finalize P&L, balance sheet, cash summary, and all agreed reports', '[ ]'],
            ['12', 'Complete reviewer sign-off, lock or close period, and deliver to client', '[ ]'],
        ],
        col_widths_cm=[1.5, 14, 2]
    )

    h1(doc, 'SOP 3 — Tax Document Checklist')
    body(doc, 'Use this checklist at year-end or when preparing the annual tax package.')
    premium_table(doc,
        ['Category', 'Typical Documents Required'],
        [
            ['Income', 'Sales summaries, invoices, merchant reports, platform statements, interest income'],
            ['Banking', 'Year-end bank and credit-card statements, final reconciliations'],
            ['Payroll', 'Annual payroll summaries, W-2/1099 or equivalent, payroll tax filings'],
            ['Expenses', 'Major receipts, insurance, rent, professional fees, travel, vehicle records'],
            ['Assets & Debt', 'Asset purchases/disposals, loan statements, financing agreements'],
            ['Tax & Compliance', 'Prior-year return, estimated payments, notices, sales-tax/VAT filings'],
            ['Owner Activity', 'Contributions, draws/distributions, shareholder/partner transactions'],
        ],
        col_widths_cm=[4, 14.5]
    )
    callout(doc, 'Document collection is not tax advice. Confirm the final list and filing deadlines with the client\'s qualified tax professional.', style='important', heading='Scope Reminder')
    doc.add_paragraph()

    h1(doc, 'SOP 4 — Quality Control Review')
    body(doc, 'Complete this review before delivering reports to any client.')
    premium_table(doc,
        ['QC Check', 'Verified By', 'Done'],
        [
            ['All statement balances agree to the ledger', '', '[ ]'],
            ['No unexplained suspense or uncategorized balances', '', '[ ]'],
            ['Opening balances and retained earnings are understood', '', '[ ]'],
            ['Negative assets/liabilities and unusual balances are investigated and documented', '', '[ ]'],
            ['Payroll, loans, sales tax/VAT, and processor clearing accounts are fully reconciled', '', '[ ]'],
            ['Material variances have documented explanations', '', '[ ]'],
            ['Reports use correct period, basis, entity, and comparison column', '', '[ ]'],
            ['All questions, judgments, and client approvals are documented', '', '[ ]'],
            ['Period is locked or closed in the software after review', '', '[ ]'],
            ['Reports delivered to client portal — not by ordinary email', '', '[ ]'],
        ],
        col_widths_cm=[11.5, 4, 2]
    )

    save(doc, f'{OUT}/04-Operations-Library/Bookkeeping-SOPs-and-Checklists-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 7. Client Communication Scripts v2
# ══════════════════════════════════════════════════════════════════════════════

def build_scripts():
    doc = new_doc()
    add_cover_page(doc, 'Client Communication\nScripts',
                   'Ready-to-customize messages for every stage of the client lifecycle',
                   '04 — OPERATIONS LIBRARY')
    add_header(doc, doc_title='Client Communication Scripts')

    callout(doc, 'These are internal templates — not for direct forwarding. Replace [BRACKETED TEXT] with real details before sending each message.', style='warning', heading='Customize Before Sending')
    doc.add_paragraph()

    scripts = [
        ('1. Inquiry Response', 'Email', 'Next step for your bookkeeping inquiry',
         'Hi [NAME],\n\nThank you for reaching out about bookkeeping support. To understand whether we are a good fit and to provide an accurate scope, I have a few quick questions:\n\n• What entity type and jurisdiction is the business?\n• What bookkeeping software are you currently using?\n• Approximately how many bank and credit-card accounts do you have?\n• What is your average monthly transaction volume?\n• Do you have payroll, sales tax/VAT, or multi-entity requirements?\n• Are there any known backlogs, cleanups, or issues with the current books?\n• What reporting do you need (P&L, cash flow, custom)?\n\nYou can reply here or complete the intake form at: [LINK]\n\nLooking forward to learning more about your business.\n\n[PRACTICE NAME]'),

        ('2. Diagnostic Booking Confirmation', 'Email', 'Bookkeeping diagnostic confirmed — [DATE]',
         'Hi [NAME],\n\nYour diagnostic call is confirmed for [DATE] at [TIME] via [PLATFORM].\n\nDuring the call we will review:\n• Your current bookkeeping system and software\n• The last fully reconciled month\n• Transaction volume and account structure\n• Any known issues or backlog\n• Your reporting and advisory goals\n\nTo make the most of the call, please securely upload or share: [LIST OF DOCUMENTS]\n\nJoin link: [LINK]\n\nSee you then,\n[PRACTICE NAME]'),

        ('3. Proposal Follow-Up', 'Email', 'Bookkeeping proposal — [COMPANY]',
         'Hi [NAME],\n\nI wanted to follow up on the proposal sent on [DATE] for [COMPANY].\n\nThe proposal addresses [PRIMARY ISSUE] with the recommended scope of [SUMMARY]. The monthly investment of €[AMOUNT] assumes [VOLUME/ACCOUNTS] and an engagement start of [DATE].\n\nHappy to answer any questions before [DECISION DATE]. A quick call works well — use this link to book time: [LINK]\n\nBest,\n[PRACTICE NAME]'),

        ('4. Welcome & Onboarding', 'Email', 'Welcome — your bookkeeping onboarding steps',
         'Hi [NAME],\n\nWelcome — we are glad to be working with you.\n\nHere are your first three steps to get started:\n\n1. Complete the intake form: [LINK]\n2. Grant bookkeeping software access (instructions attached)\n3. Upload the requested documents to your secure portal: [LINK]\n\nPlease complete steps 1 and 2 by [DATE] so we can begin the diagnostic review on schedule.\n\nYour kickoff call is [DATE/TIME] — join here: [LINK]\n\nAny questions before then, just reply here.\n\n[PRACTICE NAME]'),

        ('5. Missing Documents Request', 'Email or Portal', 'Documents needed — [MONTH] close',
         'Hi [NAME],\n\nTo complete the [MONTH] close on schedule, we still need the following:\n\n[LIST SPECIFIC MISSING ITEMS]\n\nPlease upload these to your secure portal by [DATE]: [LINK]\n\nIf these documents are not available by [DATE], the report delivery may shift from [ORIGINAL DATE] to approximately [REVISED DATE].\n\nIf any item on this list does not apply to [COMPANY], please let us know so we can update your document checklist.\n\n[PRACTICE NAME]'),

        ('6. Transaction Questions', 'Email or Portal', '[MONTH] bookkeeping questions',
         'Hi [NAME],\n\nThe consolidated question list for [MONTH] is ready for your review here: [LINK]\n\nPlease respond by [DATE] to keep the close on schedule.\n\nWhen answering:\n• If a transaction is personal, reimbursable, or owner-related — note that\n• If a transaction is unclear — add context rather than guessing an account\n• If a transaction repeats each month — we will set it up to categorize automatically going forward\n\nThank you,\n[PRACTICE NAME]'),

        ('7. Close Complete & Report Delivery', 'Email or Portal', '[MONTH] books are closed',
         'Hi [NAME],\n\nThe [MONTH] books are complete. Your reports are available in your secure portal: [LINK]\n\nKey items for this month:\n• [FINANCIAL INSIGHT 1 — e.g., Revenue was X% above prior month]\n• [FINANCIAL INSIGHT 2 — e.g., One large expense in [CATEGORY] worth reviewing]\n• [ACTION — e.g., Invoice [#] from [DATE] is still outstanding]\n\nPlease review and confirm there are no material events after month-end that might affect the records.\n\nNext close deadline: [DATE]\n\n[PRACTICE NAME]'),

        ('8. Tax Preparer Year-End Handoff', 'Email', 'Year-end bookkeeping package — [COMPANY]',
         'Hi [NAME],\n\nThe year-end bookkeeping package for [COMPANY] for [FISCAL YEAR] is ready.\n\nThe package includes:\n• Final profit & loss statement\n• Final balance sheet\n• Bank reconciliation summaries\n• [OTHER REPORTS]\n\nAll documents are in your secure portal: [LINK]\n\nOpen items and bookkeeping judgments are documented in the notes at: [LINK]\n\nPlease send any proposed adjusting entries through the secure portal. Do not send them by ordinary email.\n\n[PRACTICE NAME]'),

        ('9. Overdue Invoice Notice', 'Email', 'Invoice [NUMBER] — payment reminder',
         'Hi [NAME],\n\nThis is a friendly reminder that Invoice [NUMBER] for €[AMOUNT], covering [SERVICE PERIOD], was due on [DATE] and remains outstanding.\n\nPayment options: [PAYMENT LINK / INSTRUCTIONS]\n\nIf payment has already been made, please disregard this message and accept our thanks.\n\nUnder our engagement agreement, bookkeeping work may be paused if a balance remains overdue beyond [X] days of the due date. We want to avoid that, so please reach out if you have any questions about this invoice.\n\n[PRACTICE NAME]'),

        ('10. Scope Change Approval Request', 'Email', 'Approval needed — scope change for [COMPANY]',
         'Hi [NAME],\n\nDuring [MONTH] work, we identified that the actual volume or complexity differs from what was estimated at proposal because: [SPECIFIC REASON]\n\nThe additional work required is: [DESCRIPTION]\n\nThe revised fee for this work is: €[AMOUNT] — [BILLING TERMS]\n\nThis work will not proceed until you confirm approval. Please reply with "Approved" or let us know if you have questions before we proceed.\n\nThank you,\n[PRACTICE NAME]'),
    ]

    for title, channel, subject, body_text in scripts:
        section_bar(doc, title, bg=SECONDARY)
        doc.add_paragraph()

        meta_table = doc.add_table(rows=1, cols=2)
        meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        lc = meta_table.cell(0, 0)
        lc.width = Cm(9)
        set_cell_bg(lc, BG)
        set_cell_margins(lc, top=60, bottom=60, left=120, right=60)
        lp = lc.paragraphs[0]
        lr = lp.add_run(f'Channel: {channel}')
        set_run_font(lr, 'Inter', 8.5, color=MUTED)

        rc = meta_table.cell(0, 1)
        rc.width = Cm(9.5)
        set_cell_bg(rc, BG)
        set_cell_margins(rc, top=60, bottom=60, left=60, right=120)
        rp = rc.paragraphs[0]
        rr = rp.add_run(f'Subject: {subject}')
        set_run_font(rr, 'Inter', 8.5, bold=True, color=SECONDARY)
        rp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        remove_table_borders(meta_table)

        doc.add_paragraph()

        # Body as callout
        body_table = doc.add_table(rows=1, cols=1)
        body_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        bc = body_table.cell(0, 0)
        set_cell_bg(bc, LIGHT_PRI)
        set_cell_margins(bc, top=150, bottom=150, left=200, right=200)
        set_cell_borders(bc, PRIMARY, 12, ('left',))
        set_cell_borders(bc, BORDER, 4, ('top', 'bottom', 'right'))

        for line in body_text.split('\n'):
            bp = bc.add_paragraph()
            br = bp.add_run(line)
            set_run_font(br, 'Inter', 8.5, color=SECONDARY)
            para_spacing(bp, before=0, after=2)

        doc.add_paragraph()

    save(doc, f'{OUT}/04-Operations-Library/Client-Communication-Scripts-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# 8. Annual Tax Prep Checklist v2 (NEW)
# ══════════════════════════════════════════════════════════════════════════════

def build_tax_prep():
    doc = new_doc()
    add_cover_page(doc, 'Annual Tax Prep\nChecklist',
                   'Year-end document preparation guide for bookkeepers and clients',
                   '04 — OPERATIONS LIBRARY')
    add_header(doc, doc_title='Annual Tax Prep Checklist')

    callout(doc, 'This checklist helps you prepare the year-end bookkeeping package for the client\'s tax preparer. It does not replace tax advice.', style='info', heading='Purpose')
    doc.add_paragraph()

    h1(doc, 'Client & Engagement Details')
    premium_table(doc,
        ['Field', 'Details'],
        [
            ['Client Name', ''],
            ['Fiscal Year End', ''],
            ['Tax Preparer Name / Firm', ''],
            ['Bookkeeping Software', ''],
            ['Package Delivery Deadline', ''],
            ['Prepared By', ''],
            ['Review Date', ''],
        ],
        col_widths_cm=[5.5, 13]
    )

    h1(doc, 'Phase 1 — Final Month Close')
    body(doc, 'Complete the standard monthly close for the final month of the fiscal year before starting the tax package.')
    premium_table(doc,
        ['Task', 'Done', 'Notes'],
        [
            ['Final month close completed per monthly checklist', '[ ]', ''],
            ['All bank and credit-card accounts reconciled to year-end statements', '[ ]', ''],
            ['All loans reconciled to year-end statements', '[ ]', ''],
            ['Payroll liabilities reconciled to payroll provider year-end reports', '[ ]', ''],
            ['Sales-tax / VAT accounts reconciled to filings', '[ ]', ''],
            ['Accounts receivable aging reviewed and confirmed', '[ ]', ''],
            ['Accounts payable aging reviewed and confirmed', '[ ]', ''],
            ['All suspense and clearing accounts at zero or documented', '[ ]', ''],
        ],
        col_widths_cm=[11, 1.5, 6]
    )

    h1(doc, 'Phase 2 — Year-End Adjustments')
    premium_table(doc,
        ['Adjustment Type', 'Done', 'Notes'],
        [
            ['Depreciation / amortization recorded (within scope)', '[ ]', ''],
            ['Prepaid expenses adjusted to correct period', '[ ]', ''],
            ['Accrued revenue or expenses recorded (within scope)', '[ ]', ''],
            ['Owner draw and contribution accounts reviewed', '[ ]', ''],
            ['Loans to / from owners documented', '[ ]', ''],
            ['Inventory count reconciled to ledger (if applicable)', '[ ]', ''],
            ['Prior-year adjusting entries from tax preparer posted', '[ ]', ''],
        ],
        col_widths_cm=[11, 1.5, 6]
    )

    h1(doc, 'Phase 3 — Document Collection Checklist')
    premium_table(doc,
        ['Category', 'Documents Required', 'Received', 'Notes'],
        [
            ['Income', 'All sales reports, merchant statements, platform reports, interest income', '[ ]', ''],
            ['Banking', 'Year-end bank statements, credit-card statements for all accounts', '[ ]', ''],
            ['Payroll', 'Annual payroll summary, W-2 / 1099 or local equivalent, payroll tax filings', '[ ]', ''],
            ['Major Expenses', 'Rent, insurance, professional fees, travel, vehicle, significant receipts', '[ ]', ''],
            ['Fixed Assets', 'Asset purchases and disposals with dates and amounts', '[ ]', ''],
            ['Loans & Financing', 'Year-end loan statements, amortization schedules', '[ ]', ''],
            ['Tax & Compliance', 'Prior-year tax return, estimated tax payments, sales-tax/VAT filings, notices', '[ ]', ''],
            ['Owner Activity', 'All owner contributions, draws, distributions, shareholder loan activity', '[ ]', ''],
        ],
        col_widths_cm=[3.5, 7, 1.5, 6.5]
    )

    h1(doc, 'Phase 4 — Package Assembly')
    premium_table(doc,
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
        col_widths_cm=[8, 3, 1.5, 6]
    )

    callout(doc,
        'Upload the completed package to the client\'s secure portal and notify the tax preparer '
        'through the appropriate channel. Do not email sensitive financial reports.',
        style='info', heading='Delivery Instructions')
    doc.add_paragraph()

    callout(doc,
        'This checklist does not replace professional tax advice. The tax preparer is responsible '
        'for determining what documents are required and for all tax-related judgments and filings.',
        style='important', heading='Professional Notice')

    save(doc, f'{OUT}/04-Operations-Library/Annual-Tax-Prep-Checklist-v2.docx')


# ══════════════════════════════════════════════════════════════════════════════
# Run all
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('Building DOCX files...')
    build_start_here()
    build_service_guide()
    build_intake_pack()
    build_proposal()
    build_engagement_agreement()
    build_sops()
    build_scripts()
    build_tax_prep()
    print('All DOCX files done.')
