"""
Consulting-grade Excel dashboard — McKinsey / Deloitte / PwC standard.
White backgrounds, teal accent-only, thin rule lines, executive layout.
Preserves all content and formulas from v2; redesigns visual layer only.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
import os

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/v2-consulting/02-Practice-Dashboard'
os.makedirs(OUT, exist_ok=True)

# ── Consulting Color Palette (ARGB) ──────────────────────────────────────────
INK        = 'FF0F172A'   # near-black body text
TEAL       = 'FF0F766E'   # accent only
TEAL_10    = 'FFCCFBF1'   # teal 10% tint
AMBER      = 'FFD97706'   # warm accent
AMBER_10   = 'FFFEF3C7'   # amber 10%
WHITE      = 'FFFFFFFF'
BG_SOFT    = 'FFF8FAFC'   # near-white page fill
RULE       = 'FFE2E8F0'   # thin rule line
MUTED      = 'FF64748B'   # secondary text
DARK_NAVY  = 'FF0F172A'   # cover / header bg
SUCCESS_G  = 'FF10B981'
DANGER_R   = 'FFEF4444'
WARN_Y     = 'FFF59E0B'


# ── Style Helpers ─────────────────────────────────────────────────────────────

def F(bold=False, size=9, color=INK, name='Calibri', italic=False):
    return Font(name=name, bold=bold, size=size, color=color, italic=italic)


def Fill(color):
    return PatternFill('solid', fgColor=color)


def Align(h='left', v='center', wrap=False, indent=0):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap, indent=indent)


def thin_side(color=RULE):
    return Side(style='thin', color=color)


def no_side():
    return Side(style=None)


def border_all(color=RULE):
    s = thin_side(color)
    return Border(left=s, right=s, top=s, bottom=s)


def border_bottom_only(color=RULE):
    return Border(bottom=thin_side(color))


def border_left_accent(color=TEAL, width='medium'):
    return Border(left=Side(style=width, color=color),
                  right=no_side(), top=no_side(), bottom=no_side())


def sc(ws, row, col, value=None, font=None, fill=None, align=None,
       border=None, nf=None, w=None, h=None):
    """Style a single cell."""
    cell = ws.cell(row=row, column=col)
    if value is not None:
        cell.value = value
    if font:
        cell.font = font
    if fill:
        cell.fill = fill
    if align:
        cell.alignment = align
    if border:
        cell.border = border
    if nf:
        cell.number_format = nf
    if w:
        ws.column_dimensions[get_column_letter(col)].width = w
    if h:
        ws.row_dimensions[row].height = h
    return cell


def mc(ws, r1, c1, r2, c2, value='', font=None, fill=None, align=None, border=None, nf=None):
    """Merge and style cells."""
    ws.merge_cells(start_row=r1, start_column=c1, end_row=r2, end_column=c2)
    cell = ws.cell(row=r1, column=c1)
    cell.value = value
    if font:
        cell.font = font
    if fill:
        cell.fill = fill
    if align:
        cell.alignment = align
    if border:
        cell.border = border
    if nf:
        cell.number_format = nf
    return cell


# ── Consulting Page Header (white bg, teal rule, section numbering) ───────────

def page_header(ws, number, title, subtitle='', row=1):
    """
    Consulting-style page header: white bg, teal 2pt bottom rule,
    section number (01 — TITLE) pattern.
    """
    ws.row_dimensions[row].height = 10   # top margin
    row += 1

    # Teal left accent bar (2 cells wide, merged, teal fill)
    mc(ws, row, 1, row + 1, 1, value='',
       fill=Fill(TEAL))

    # Section number
    num_str = f'{number:02d}'
    sc(ws, row, 2, value=num_str,
       font=F(bold=True, size=18, color=TEAL, name='Calibri'),
       align=Align('left', 'bottom'),
       h=22)

    # Em-dash + title
    sc(ws, row, 3, value=f'— {title.upper()}',
       font=F(bold=True, size=13, color=INK, name='Calibri'),
       align=Align('left', 'bottom'))
    ws.merge_cells(start_row=row, start_column=3, end_row=row, end_column=16)

    if subtitle:
        sc(ws, row + 1, 2, value=subtitle,
           font=F(size=8, color=MUTED, italic=True),
           align=Align('left', 'top'),
           h=16)
        ws.merge_cells(start_row=row + 1, start_column=2, end_row=row + 1, end_column=16)
        end_row = row + 2
    else:
        ws.row_dimensions[row + 1].height = 12
        end_row = row + 2

    # Teal rule line below header
    rule_row = end_row
    ws.row_dimensions[rule_row].height = 3
    mc(ws, rule_row, 1, rule_row, 18, fill=Fill(TEAL))
    ws.row_dimensions[rule_row + 1].height = 8  # space after rule

    return rule_row + 2   # first content row


def section_label(ws, row, number, title):
    """Inline section divider: numbered, teal accent."""
    ws.row_dimensions[row].height = 4
    row += 1
    sc(ws, row, 2, value=f'{number:02d}  —  {title.upper()}',
       font=F(bold=True, size=8.5, color=TEAL),
       align=Align('left', 'center'),
       h=18)
    ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=16)
    # Thin teal underline on that row
    for col in range(2, 17):
        ws.cell(row=row, column=col).border = border_bottom_only(TEAL)
    ws.row_dimensions[row + 1].height = 6
    return row + 2


def col_header(ws, row, col, label, width=14):
    ws.column_dimensions[get_column_letter(col)].width = width
    ws.row_dimensions[row].height = 20
    c = sc(ws, row, col, value=label,
           font=F(bold=True, size=8, color=WHITE),
           fill=Fill(TEAL),
           align=Align('center', 'center'),
           border=border_all(TEAL))
    return c


def data_row(ws, row, col, value, center=False, nf=None, bold=False):
    fill = Fill(BG_SOFT) if row % 2 == 0 else Fill(WHITE)
    sc(ws, row, col, value=value,
       font=F(size=8.5, bold=bold, color=INK),
       fill=fill,
       align=Align('center' if center else 'left', 'center'),
       border=border_all(RULE),
       nf=nf)


# ── Consulting KPI Card (clean, minimal) ─────────────────────────────────────

def kpi_card(ws, row, col, label, value, note='', accent=TEAL):
    """
    Consulting KPI: white card, teal left border accent, clean typography.
    Takes 4 rows (label, value, note, thin rule).
    """
    # Card background rows
    for r in range(row, row + 4):
        for c in range(col, col + 3):
            sc(ws, r, c, fill=Fill(WHITE), border=border_all(RULE))

    ws.row_dimensions[row].height = 13
    ws.row_dimensions[row + 1].height = 30
    ws.row_dimensions[row + 2].height = 13
    ws.row_dimensions[row + 3].height = 4

    # Label
    mc(ws, row, col, row, col + 2, value=label,
       font=F(size=7.5, bold=True, color=MUTED),
       fill=Fill(WHITE),
       align=Align('left', 'bottom', indent=1))

    # Value
    mc(ws, row + 1, col, row + 1, col + 2, value=value,
       font=F(size=18, bold=True, color=INK, name='Calibri'),
       fill=Fill(WHITE),
       align=Align('left', 'center', indent=1))

    # Note
    mc(ws, row + 2, col, row + 2, col + 2, value=note,
       font=F(size=7.5, color=MUTED, italic=True),
       fill=Fill(WHITE),
       align=Align('left', 'top', indent=1))

    # Teal bottom rule on card
    for c in range(col, col + 3):
        ws.cell(row=row + 3, column=c).fill = Fill(accent)

    # Left accent border on the card value row
    ws.cell(row=row + 1, column=col).border = Border(
        left=Side(style='medium', color=accent),
        right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)
    )


# ── Print Settings Helper ─────────────────────────────────────────────────────

def apply_print_settings(ws, header_end_row=7):
    """Apply landscape print settings with header row repeat."""
    ws.print_title_rows = f'1:{header_end_row}'
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0


# ══════════════════════════════════════════════════════════════════════════════
# Sheet Builders
# ══════════════════════════════════════════════════════════════════════════════

def build_navigation(ws):
    """Branded landing / navigation sheet — first sheet in workbook."""
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2
    ws.column_dimensions['B'].width = 28
    ws.column_dimensions['C'].width = 60
    ws.column_dimensions['D'].width = 2

    # ── Dark navy full-width header ───────────────────────────────────────────
    ws.row_dimensions[1].height = 6    # top margin
    ws.row_dimensions[2].height = 46
    mc(ws, 2, 1, 2, 20,
       value='NOVAOPS  ·  Bookkeeper Practice Dashboard  ·  v2.0',
       font=F(bold=True, size=22, color=WHITE, name='Calibri'),
       fill=Fill(DARK_NAVY),
       align=Align('center', 'center'))

    ws.row_dimensions[3].height = 20
    mc(ws, 3, 1, 3, 20,
       value='Your complete practice operations system',
       font=F(size=10, color=MUTED, italic=True),
       fill=Fill(DARK_NAVY),
       align=Align('center', 'center'))

    ws.row_dimensions[4].height = 3
    mc(ws, 4, 1, 4, 20, fill=Fill(TEAL))   # teal rule

    ws.row_dimensions[5].height = 14       # spacer

    # ── Navigation table header ───────────────────────────────────────────────
    ws.row_dimensions[6].height = 20
    sc(ws, 6, 2, value='Sheet Name',
       font=F(bold=True, size=9, color=WHITE),
       fill=Fill(TEAL),
       align=Align('center', 'center'),
       border=border_all(TEAL))
    sc(ws, 6, 3, value='Description',
       font=F(bold=True, size=9, color=WHITE),
       fill=Fill(TEAL),
       align=Align('center', 'center'),
       border=border_all(TEAL))

    # ── Sheet list ────────────────────────────────────────────────────────────
    nav_items = [
        ('Navigation',         'This landing page — start here'),
        ('Setup',              'Enter your practice name, pricing tiers, and settings'),
        ('Client CRM',         'Master record for all active and former clients'),
        ('Lead Pipeline',      'Track every prospect from first contact to closed deal'),
        ('Pricing Calculator', 'Calculate client fees and cleanup estimates instantly'),
        ('Monthly Close',      'Track monthly close status and checklist for every client'),
        ('Invoice Tracker',    'Log invoices, payment status, and outstanding balances'),
        ('Tax Documents',      'Year-end document collection tracker per client'),
        ('Capacity Planner',   'Plan available hours vs. committed client time'),
        ('Dashboard',          'Live KPI overview — auto-populates from all sheets'),
        ('Instructions',       'Full usage guide for every sheet in this system'),
    ]

    r = 7
    for i, (sheet_name, desc) in enumerate(nav_items):
        ws.row_dimensions[r].height = 20
        fill_color = BG_SOFT if i % 2 == 0 else WHITE
        sc(ws, r, 2, value=sheet_name,
           font=F(bold=True, size=9, color=TEAL if sheet_name != 'Navigation' else INK),
           fill=Fill(fill_color),
           align=Align('left', 'center', indent=1),
           border=border_all(RULE))
        sc(ws, r, 3, value=desc,
           font=F(size=9, color=INK),
           fill=Fill(fill_color),
           align=Align('left', 'center', indent=1),
           border=border_all(RULE))
        r += 1

    ws.row_dimensions[r].height = 16   # spacer
    r += 1

    # ── HOW TO START callout box ──────────────────────────────────────────────
    ws.row_dimensions[r].height = 18
    mc(ws, r, 2, r, 3,
       value='HOW TO START',
       font=F(bold=True, size=10, color=AMBER),
       fill=Fill(AMBER_10),
       align=Align('left', 'center', indent=1),
       border=Border(left=Side(style='medium', color=AMBER),
                     right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)))
    r += 1

    ws.row_dimensions[r].height = 54
    mc(ws, r, 2, r, 3,
       value=(
           'Step 1: Go to Setup sheet and fill all amber cells.\n'
           'Step 2: Add your clients in Client CRM.\n'
           'Step 3: Use Dashboard to track everything at a glance.'
       ),
       font=F(size=9, color=INK),
       fill=Fill(AMBER_10),
       align=Align('left', 'center', wrap=True, indent=1),
       border=Border(left=Side(style='medium', color=AMBER),
                     right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)))
    r += 1

    ws.row_dimensions[r].height = 14   # spacer before footer
    r += 1

    # ── NovaOps brand footer ──────────────────────────────────────────────────
    ws.row_dimensions[r].height = 22
    mc(ws, r, 1, r, 20,
       value='© 2025 NovaOps  ·  Bookkeeper Practice Launch System  ·  Commercial Use License',
       font=F(size=8, color=MUTED, italic=True),
       fill=Fill(DARK_NAVY),
       align=Align('center', 'center'))


def build_setup(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 1, 'Setup',
                    'Fill in the amber cells — do not edit white formula cells')

    # Freeze panes below the page header (row 7 is first content row, freeze at col B)
    ws.freeze_panes = ws.cell(row=7, column=2)

    r = section_label(ws, r, 1, 'Practice Information')

    setup_fields = [
        ('Practice Name', '[Your Practice Name]'),
        ('Tagline / Descriptor', '[e.g., Bookkeeping for service businesses]'),
        ('Owner / Bookkeeper Name', '[Your Name]'),
        ('Email Address', '[your@email.com]'),
        ('Phone Number', '[Your Phone]'),
        ('Website / Portal URL', '[https://yoursite.com]'),
        ('Bookkeeping Software Used', '[QuickBooks Online / Xero / Wave / Other]'),
        ('Currency Symbol', '€'),
        ('Monthly Close Day (of following month)', '15'),
        ('Fiscal Year End Month', 'December'),
    ]

    input_cells = []
    for label, default in setup_fields:
        ws.row_dimensions[r].height = 20
        sc(ws, r, 2, value=label,
           font=F(size=9, color=INK),
           fill=Fill(BG_SOFT),
           align=Align('left', 'center', indent=1),
           border=border_all(RULE))
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
        input_cell = sc(ws, r, 6, value=default,
           font=F(size=9, bold=True, color=INK),
           fill=Fill(AMBER_10),
           align=Align('left', 'center', indent=1),
           border=Border(left=Side(style='medium', color=AMBER),
                         right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)))
        ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=9)
        input_cells.append(f'F{r}')
        r += 1

    # Data validation with error messages on amber input cells
    for cell_ref in input_cells:
        dv = DataValidation(type='textLength', operator='greaterThan', formula1='0',
                            allow_blank=False)
        dv.error = 'Please enter a value'
        dv.errorTitle = 'Required Field'
        dv.showErrorMessage = True
        dv.sqref = cell_ref
        ws.add_data_validation(dv)

    r = section_label(ws, r, 2, 'Service Tiers')

    for col, label, width in [(2,'Tier Name',18),(3,'Monthly Transactions',18),
                               (4,'Accounts',12),(5,'Monthly Fee (€)',14),(6,'Hourly Rate (€)',14)]:
        col_header(ws, r, col, label, width)
    r += 1

    for name, txn, accts, fee, rate in [('Essentials',100,3,650,75),('Growth',300,6,1200,85),('Advanced',600,12,2200,100)]:
        ws.row_dimensions[r].height = 20
        for col, val in [(2,name),(3,txn),(4,accts),(5,fee),(6,rate)]:
            data_row(ws, r, col, val, center=(col>2), nf='€#,##0' if col in [5,6] else None)
        r += 1

    apply_print_settings(ws, header_end_row=7)


def build_client_crm(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 2, 'Client CRM', 'Master record for all active and former clients')

    headers = [
        ('B','Client Name',24),('C','Status',16),('D','Entity Type',14),
        ('E','Software',14),('F','Monthly Fee (€)',16),('G','Close Day',10),
        ('H','Primary Contact',18),('I','Email',22),('J','Tax Preparer',18),
        ('K','Start Date',14),('L','Service Package',16),('M','Notes',30),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r

    # Freeze panes so column headers stay visible
    ws.freeze_panes = ws.cell(row=r + 1, column=2)

    r += 1

    data = [
        ['Harbor Design LLC','Active','LLC','QuickBooks Online',850,15,'Alex Morgan','alex@example.com','[Tax Preparer]','2025-01-01','Growth',''],
        ['Oak & Pine Co.','Active','S-Corp','Xero',1200,15,'Jamie Chen','jamie@example.com','[Tax Preparer]','2025-03-01','Advanced',''],
        ['[Client Name]','Active','[Entity]','[Software]',0,15,'[Contact]','[Email]','[Tax Preparer]','','Essentials',''],
    ]

    for row_data in data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            nf = '€#,##0' if col == 6 else None
            data_row(ws, r, col, val, center=(col > 4), nf=nf)
        r += 1

    # Dropdowns
    dv = DataValidation(type='list', formula1='"Active,On Hold,Churned,Prospect"', allow_blank=True)
    dv.sqref = f'C{header_row+1}:C200'
    ws.add_data_validation(dv)
    dv2 = DataValidation(type='list', formula1='"Essentials,Growth,Advanced"', allow_blank=True)
    dv2.sqref = f'L{header_row+1}:L200'
    ws.add_data_validation(dv2)

    # Conditional formatting
    ws.conditional_formatting.add(f'C{header_row+1}:C200',
        CellIsRule(operator='equal', formula=['"Active"'],
                   fill=PatternFill('solid', fgColor=TEAL_10[2:]),
                   font=Font(color=TEAL[2:], bold=True, name='Calibri', size=8.5)))
    ws.conditional_formatting.add(f'C{header_row+1}:C200',
        CellIsRule(operator='equal', formula=['"Churned"'],
                   fill=PatternFill('solid', fgColor='FFFEE2E2'),
                   font=Font(color=DANGER_R[2:], bold=True, name='Calibri', size=8.5)))

    # MRR total
    r += 1
    ws.row_dimensions[r].height = 24
    mc(ws, r, 2, r, 5, value='TOTAL MONTHLY RECURRING REVENUE',
       font=F(bold=True, size=9, color=TEAL),
       fill=Fill(TEAL_10),
       align=Align('right', 'center'),
       border=border_all(TEAL))
    sc(ws, r, 6,
       value=f'=SUMIF(C{header_row+1}:C200,"Active",F{header_row+1}:F200)',
       font=F(bold=True, size=11, color=TEAL),
       fill=Fill(TEAL_10),
       align=Align('center', 'center'),
       border=Border(left=Side(style='medium', color=TEAL),
                     right=thin_side(TEAL), top=thin_side(TEAL), bottom=thin_side(TEAL)),
       nf='€#,##0')

    apply_print_settings(ws, header_end_row=header_row)


def build_lead_pipeline(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 3, 'Lead Pipeline', 'Track every prospect from first contact to closed deal')

    headers = [
        ('B','Lead / Contact Name',22),('C','Company',20),('D','Stage',16),
        ('E','Source',14),('F','Est. Monthly Fee (€)',16),('G','Cleanup Est. (€)',14),
        ('H','Next Action',22),('I','Next Action Date',14),('J','Email',22),('K','Notes',30),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r

    # Freeze panes below column headers
    ws.freeze_panes = ws.cell(row=r + 1, column=2)

    r += 1

    data = [
        ['Jamie Chen','Oak & Pine Co.','Diagnostic Scheduled','Referral',1200,2400,'Run diagnostic','2026-07-03','jamie@example.com',''],
        ['[Lead Name]','[Company]','New Inquiry','[Source]',0,0,'[Action]','','[Email]',''],
    ]

    dv_stage = DataValidation(type='list',
        formula1='"New Inquiry,Intake Sent,Diagnostic Scheduled,Proposal Sent,Negotiating,Closed Won,Closed Lost"',
        allow_blank=True)
    dv_stage.sqref = f'D{header_row+1}:D200'
    ws.add_data_validation(dv_stage)
    dv_source = DataValidation(type='list',
        formula1='"Referral,Website,LinkedIn,Etsy,Cold Outreach,Other"', allow_blank=True)
    dv_source.sqref = f'E{header_row+1}:E200'
    ws.add_data_validation(dv_source)

    for row_data in data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            nf = '€#,##0' if col in [6,7] else None
            data_row(ws, r, col, val, center=(col>4), nf=nf)
        r += 1

    ws.conditional_formatting.add(f'D{header_row+1}:D200',
        CellIsRule(operator='equal', formula=['"Closed Won"'],
                   fill=PatternFill('solid', fgColor=TEAL_10[2:]),
                   font=Font(color=TEAL[2:], bold=True, name='Calibri', size=8.5)))
    ws.conditional_formatting.add(f'D{header_row+1}:D200',
        CellIsRule(operator='equal', formula=['"Closed Lost"'],
                   fill=PatternFill('solid', fgColor='FFFEE2E2'),
                   font=Font(color=DANGER_R[2:], name='Calibri', size=8.5)))

    r += 1
    for label, formula, end_col, accent in [
        ('TOTAL PIPELINE VALUE (MONTHLY)', f'=SUMIF(D{header_row+1}:D200,"<>Closed Lost",F{header_row+1}:F200)', 5, TEAL),
        ('OPEN LEAD COUNT', f'=COUNTIF(D{header_row+1}:D200,"<>Closed Lost")-COUNTIF(D{header_row+1}:D200,"Closed Won")', 4, AMBER),
    ]:
        ws.row_dimensions[r].height = 22
        mc(ws, r, 2, r, end_col - 1, value=label,
           font=F(bold=True, size=8.5, color=accent),
           fill=Fill(TEAL_10 if accent==TEAL else AMBER_10),
           align=Align('right', 'center'),
           border=border_all(RULE))
        sc(ws, r, end_col, value=formula,
           font=F(bold=True, size=11, color=accent),
           fill=Fill(TEAL_10 if accent==TEAL else AMBER_10),
           align=Align('center', 'center'),
           border=Border(left=Side(style='medium', color=accent),
                         right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)),
           nf='€#,##0' if end_col==5 else '0')
        r += 1

    apply_print_settings(ws, header_end_row=header_row)


def build_pricing_calc(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 4, 'Pricing Calculator', 'Calculate client fees based on scope — fill amber cells')

    # Freeze below the page header
    ws.freeze_panes = ws.cell(row=7, column=2)

    r = section_label(ws, r, 1, 'Client Inputs')

    inputs = [
        ('Monthly Bank Transactions', 150),
        ('Number of Bank Accounts', 3),
        ('Number of Credit Cards', 2),
        ('Has Payroll?  (1=Yes / 0=No)', 0),
        ('Has Sales Tax / VAT?  (1=Yes / 0=No)', 0),
        ('Has Multi-Entity / Class Tracking?  (1=Yes / 0=No)', 0),
        ('Has Foreign Currency?  (1=Yes / 0=No)', 0),
        ('Cleanup Months Needed', 0),
    ]

    input_refs = {}
    for i, (label, default) in enumerate(inputs):
        ws.row_dimensions[r].height = 22
        sc(ws, r, 2, value=label,
           font=F(size=9, color=INK),
           fill=Fill(BG_SOFT),
           align=Align('left', 'center', indent=1),
           border=border_all(RULE))
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
        sc(ws, r, 8, value=default,
           font=F(bold=True, size=10, color=INK),
           fill=Fill(AMBER_10),
           align=Align('center', 'center'),
           border=Border(left=Side(style='medium', color=AMBER),
                         right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)))
        ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)
        input_refs[i] = f'H{r}'
        r += 1

    r = section_label(ws, r, 2, 'Calculated Fees')

    fee_rows = [
        ('Base Monthly Fee', f'=IF({input_refs[0]}<=100,650,IF({input_refs[0]}<=300,1200,2200))'),
        ('Payroll Add-On', f'=IF({input_refs[3]}=1,150,0)'),
        ('Sales Tax / VAT Add-On', f'=IF({input_refs[4]}=1,100,0)'),
        ('Multi-Entity Add-On', f'=IF({input_refs[5]}=1,300,0)'),
        ('Foreign Currency Add-On', f'=IF({input_refs[6]}=1,200,0)'),
        ('Cleanup Project Estimate', f'={input_refs[7]}*400'),
    ]

    first_fee_row = r
    for label, formula in fee_rows:
        ws.row_dimensions[r].height = 22
        sc(ws, r, 2, value=label,
           font=F(size=9, color=INK),
           fill=Fill(BG_SOFT),
           align=Align('left', 'center', indent=1),
           border=border_all(RULE))
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
        sc(ws, r, 8, value=formula,
           font=F(size=10, color=TEAL),
           fill=Fill(TEAL_10),
           align=Align('center', 'center'),
           border=border_all(RULE),
           nf='€#,##0')
        ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)
        r += 1

    # Total recommended fee
    ws.row_dimensions[r].height = 28
    mc(ws, r, 2, r, 7, value='RECOMMENDED MONTHLY FEE',
       font=F(bold=True, size=10, color=WHITE),
       fill=Fill(TEAL),
       align=Align('right', 'center'),
       border=border_all(TEAL))
    sc(ws, r, 8,
       value=f'=SUM(H{first_fee_row}:H{r-1})-H{r-1}',
       font=F(bold=True, size=14, color=WHITE),
       fill=Fill(TEAL),
       align=Align('center', 'center'),
       border=border_all(TEAL),
       nf='€#,##0')
    ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)
    r += 1

    ws.row_dimensions[r].height = 24
    mc(ws, r, 2, r, 7, value='CLEANUP PROJECT ESTIMATE (one-time)',
       font=F(bold=True, size=9, color=WHITE),
       fill=Fill(AMBER),
       align=Align('right', 'center'),
       border=border_all(AMBER))
    sc(ws, r, 8, value=f'=H{r-1}',
       font=F(bold=True, size=12, color=WHITE),
       fill=Fill(AMBER),
       align=Align('center', 'center'),
       border=border_all(AMBER),
       nf='€#,##0')
    ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)

    apply_print_settings(ws, header_end_row=7)


def build_monthly_close(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 5, 'Monthly Close Tracker', 'Track close status for every client each period')

    headers = [
        ('B','Period',12),('C','Client',22),('D','Status',16),('E','Owner',14),
        ('F','Bank Rec.',10),('G','Card Rec.',10),('H','Questions Sent',14),
        ('I','Questions Answered',16),('J','Reports Delivered',14),
        ('K','Due Date',14),('L','Review Notes',30),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r

    # Freeze panes below column headers
    ws.freeze_panes = ws.cell(row=r + 1, column=2)

    r += 1
    data_start = r

    data = [
        ['2026-07','Harbor Design LLC','In Progress','[OWNER]','Yes','No','No','No','No','2026-08-15',''],
        ['2026-07','Oak & Pine Co.','Not Started','[OWNER]','No','No','No','No','No','2026-08-15',''],
        ['2026-07','[Client Name]','Not Started','[OWNER]','No','No','No','No','No','',''],
    ]

    status_dv = DataValidation(type='list',
        formula1='"Not Started,In Progress,Questions Pending,Under Review,Delivered,On Hold"',
        allow_blank=True)
    status_dv.sqref = f'D{header_row+1}:D500'
    ws.add_data_validation(status_dv)
    yn_dv = DataValidation(type='list', formula1='"Yes,No,N/A"', allow_blank=True)
    yn_dv.sqref = f'F{header_row+1}:J500'
    ws.add_data_validation(yn_dv)

    for row_data in data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            data_row(ws, r, col, val, center=(col > 4))
        r += 1

    data_end = r - 1

    ws.conditional_formatting.add(f'D{header_row+1}:D500',
        CellIsRule(operator='equal', formula=['"Delivered"'],
                   fill=PatternFill('solid', fgColor=TEAL_10[2:]),
                   font=Font(color=TEAL[2:], bold=True, name='Calibri', size=8.5)))
    ws.conditional_formatting.add(f'D{header_row+1}:D500',
        CellIsRule(operator='equal', formula=['"Not Started"'],
                   fill=PatternFill('solid', fgColor=BG_SOFT[2:]),
                   font=Font(color=MUTED[2:], name='Calibri', size=8.5)))
    ws.conditional_formatting.add(f'F{header_row+1}:J500',
        CellIsRule(operator='equal', formula=['"Yes"'],
                   fill=PatternFill('solid', fgColor=TEAL_10[2:]),
                   font=Font(color=TEAL[2:], bold=True, name='Calibri', size=8.5)))
    ws.conditional_formatting.add(f'F{header_row+1}:J500',
        CellIsRule(operator='equal', formula=['"No"'],
                   fill=PatternFill('solid', fgColor='FFFEE2E2'),
                   font=Font(color=DANGER_R[2:], name='Calibri', size=8.5)))

    # ── Progress Bar Row ──────────────────────────────────────────────────────
    r += 1
    ws.row_dimensions[r].height = 24
    progress_formula = (
        f'=IFERROR(COUNTIF(D{data_start}:D{data_end},"Delivered")'
        f'/COUNTA(C{data_start}:C{data_end}),0)'
    )
    mc(ws, r, 2, r, 3, value='CLOSE PROGRESS',
       font=F(bold=True, size=9, color=WHITE),
       fill=Fill(TEAL),
       align=Align('right', 'center'),
       border=border_all(TEAL))
    progress_cell = sc(ws, r, 4, value=progress_formula,
       font=F(bold=True, size=11, color=WHITE),
       fill=Fill(TEAL),
       align=Align('center', 'center'),
       border=Border(left=Side(style='medium', color=TEAL),
                     right=thin_side(TEAL), top=thin_side(TEAL), bottom=thin_side(TEAL)),
       nf='0%')

    # Conditional formatting on progress cell: green >80%, amber >50%, red <50%
    prog_ref = f'D{r}'
    ws.conditional_formatting.add(prog_ref,
        CellIsRule(operator='greaterThan', formula=['0.8'],
                   fill=PatternFill('solid', fgColor=SUCCESS_G[2:])))
    ws.conditional_formatting.add(prog_ref,
        CellIsRule(operator='between', formula=['0.5', '0.8'],
                   fill=PatternFill('solid', fgColor=WARN_Y[2:])))
    ws.conditional_formatting.add(prog_ref,
        CellIsRule(operator='lessThan', formula=['0.5'],
                   fill=PatternFill('solid', fgColor=DANGER_R[2:])))

    apply_print_settings(ws, header_end_row=header_row)


def build_invoice_tracker(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 6, 'Invoice Tracker', 'Track all invoices, payment status, and outstanding balances')

    headers = [
        ('B','Invoice #',12),('C','Client',22),('D','Issue Date',14),('E','Due Date',14),
        ('F','Amount (€)',14),('G','Status',16),('H','Paid Date',14),
        ('I','Service Period',14),('J','Method',14),('K','Notes',30),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r

    # Freeze panes below column headers
    ws.freeze_panes = ws.cell(row=r + 1, column=2)

    r += 1

    data = [
        ['INV-001','Harbor Design LLC','2026-07-01','2026-07-08',850,'Paid','2026-07-05','2026-07','Bank Transfer',''],
        ['INV-002','Oak & Pine Co.','2026-07-01','2026-07-08',1200,'Paid','2026-07-03','2026-07','Bank Transfer',''],
        ['INV-003','[Client Name]','2026-08-01','2026-08-08',0,'Draft','','2026-08','',''],
    ]

    status_dv = DataValidation(type='list', formula1='"Draft,Sent,Paid,Overdue,Void"', allow_blank=True)
    status_dv.sqref = f'G{header_row+1}:G500'
    ws.add_data_validation(status_dv)

    for row_data in data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            nf = '€#,##0' if col == 6 else None
            data_row(ws, r, col, val, center=(col > 4), nf=nf)
        r += 1

    r += 1
    ws.row_dimensions[r].height = 24
    for label, formula, end_col, accent in [
        ('TOTAL INVOICED', f'=SUMIF(G{header_row+1}:G500,"<>Void",F{header_row+1}:F500)', 4, TEAL),
        ('TOTAL PAID', f'=SUMIF(G{header_row+1}:G500,"Paid",F{header_row+1}:F500)', 5, TEAL),
        ('TOTAL OUTSTANDING', f'=SUMIF(G{header_row+1}:G500,"Sent",F{header_row+1}:F500)+SUMIF(G{header_row+1}:G500,"Overdue",F{header_row+1}:F500)', 6, AMBER),
    ]:
        mc(ws, r, 2, r, end_col - 1, value=label,
           font=F(bold=True, size=8.5, color=accent),
           fill=Fill(TEAL_10 if accent==TEAL else AMBER_10),
           align=Align('right', 'center'),
           border=border_all(RULE))
        sc(ws, r, end_col, value=formula,
           font=F(bold=True, size=11, color=accent),
           fill=Fill(TEAL_10 if accent==TEAL else AMBER_10),
           align=Align('center', 'center'),
           border=Border(left=Side(style='medium', color=accent),
                         right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)),
           nf='€#,##0')
        r += 1

    ws.conditional_formatting.add(f'G{header_row+1}:G500',
        CellIsRule(operator='equal', formula=['"Paid"'],
                   fill=PatternFill('solid', fgColor=TEAL_10[2:]),
                   font=Font(color=TEAL[2:], bold=True, name='Calibri', size=8.5)))
    ws.conditional_formatting.add(f'G{header_row+1}:G500',
        CellIsRule(operator='equal', formula=['"Overdue"'],
                   fill=PatternFill('solid', fgColor='FFFEE2E2'),
                   font=Font(color=DANGER_R[2:], bold=True, name='Calibri', size=8.5)))

    apply_print_settings(ws, header_end_row=header_row)


def build_tax_docs(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 7, 'Tax Documents', 'Track year-end document collection status per client')

    headers = [
        ('B','Client',22),('C','Fiscal Year',10),('D','Income Docs',14),
        ('E','Bank Stmts',14),('F','Payroll',14),('G','Expenses',14),
        ('H','Assets/Debt',14),('I','Tax/Compliance',14),('J','Owner Activity',14),
        ('K','Package Delivered',16),('L','Tax Preparer',18),('M','Notes',30),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r

    # Freeze panes below column headers
    ws.freeze_panes = ws.cell(row=r + 1, column=2)

    r += 1

    data = [
        ['Harbor Design LLC','2025','Received','Received','N/A','Received','Received','Pending','N/A','No','[Tax Preparer]',''],
        ['Oak & Pine Co.','2025','Pending','Pending','Pending','Pending','Pending','Pending','Pending','No','[Tax Preparer]',''],
    ]

    status_dv = DataValidation(type='list', formula1='"Pending,Requested,Received,N/A"', allow_blank=True)
    status_dv.sqref = f'D{header_row+1}:J500'
    ws.add_data_validation(status_dv)
    yn_dv = DataValidation(type='list', formula1='"Yes,No"', allow_blank=True)
    yn_dv.sqref = f'K{header_row+1}:K500'
    ws.add_data_validation(yn_dv)

    for row_data in data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            data_row(ws, r, col, val, center=(col > 2))
        r += 1

    ws.conditional_formatting.add(f'D{header_row+1}:J500',
        CellIsRule(operator='equal', formula=['"Received"'],
                   fill=PatternFill('solid', fgColor=TEAL_10[2:]),
                   font=Font(color=TEAL[2:], bold=True, name='Calibri', size=8.5)))

    apply_print_settings(ws, header_end_row=header_row)


def build_capacity(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 8, 'Capacity Planner', 'Plan your available hours vs. committed client time')

    # Freeze below page header
    ws.freeze_panes = ws.cell(row=7, column=2)

    r = section_label(ws, r, 1, 'Weekly Capacity Inputs')

    cap_inputs = [
        ('Total available hours per week', 40),
        ('Admin / sales hours per week', 8),
        ('Buffer / training hours per week', 2),
        ('Billable hours available per week', None),
    ]

    refs = []
    for i, (label, val) in enumerate(cap_inputs):
        ws.row_dimensions[r].height = 22
        sc(ws, r, 2, value=label,
           font=F(size=9, color=INK),
           fill=Fill(BG_SOFT),
           align=Align('left', 'center', indent=1),
           border=border_all(RULE))
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
        refs.append(f'G{r}')
        if val is None:
            formula = f'={refs[0]}-{refs[1]}-{refs[2]}'
            sc(ws, r, 7, value=formula,
               font=F(bold=True, size=10, color=TEAL),
               fill=Fill(TEAL_10),
               align=Align('center', 'center'),
               border=Border(left=Side(style='medium', color=TEAL),
                             right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)),
               nf='0.0')
        else:
            sc(ws, r, 7, value=val,
               font=F(bold=True, size=10, color=INK),
               fill=Fill(AMBER_10),
               align=Align('center', 'center'),
               border=Border(left=Side(style='medium', color=AMBER),
                             right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)))
        ws.merge_cells(start_row=r, start_column=7, end_row=r, end_column=9)
        r += 1

    r = section_label(ws, r, 2, 'Client Time Commitments')

    headers_cap = [
        ('B','Client',22),('C','Package',16),('D','Avg Hours/Month',16),
        ('E','Hours/Week',14),('F','Notes',30),
    ]
    for col_letter, label, width in headers_cap:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row_cap = r
    r += 1

    cap_data = [
        ['Harbor Design LLC','Growth',8,f'=D{r}/4',''],
        ['Oak & Pine Co.','Advanced',12,f'=D{r+1}/4',''],
        ['[Client Name]','Essentials',5,f'=D{r+2}/4',''],
    ]

    for row_data in cap_data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers_cap):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            data_row(ws, r, col, val, center=(col >= 4),
                     nf='0.0' if col in [4, 5] else None)
        r += 1

    r += 1
    ws.row_dimensions[r].height = 22
    mc(ws, r, 2, r, 4, value='TOTAL COMMITTED HOURS / WEEK',
       font=F(bold=True, size=8.5, color=TEAL),
       fill=Fill(TEAL_10),
       align=Align('right', 'center'),
       border=border_all(RULE))
    sc(ws, r, 5,
       value=f'=SUM(E{header_row_cap+1}:E{r-1})',
       font=F(bold=True, size=11, color=TEAL),
       fill=Fill(TEAL_10),
       align=Align('center', 'center'),
       border=Border(left=Side(style='medium', color=TEAL),
                     right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)),
       nf='0.0')

    apply_print_settings(ws, header_end_row=7)


def build_dashboard(ws):
    ws.sheet_view.showGridLines = False

    # Cover header: dark navy with NovaOps branding
    ws.row_dimensions[1].height = 14   # top margin
    ws.row_dimensions[2].height = 44
    mc(ws, 2, 1, 2, 20, value='NOVAOPS  ·  BOOKKEEPER PRACTICE DASHBOARD',
       font=F(bold=True, size=20, color=WHITE, name='Calibri'),
       fill=Fill(DARK_NAVY),
       align=Align('left', 'center', indent=2))
    ws.row_dimensions[3].height = 16
    mc(ws, 3, 1, 3, 20, value='v2.0   ·   Consulting Edition   ·   Live data from all sheets',
       font=F(size=8.5, color=MUTED, italic=True),
       fill=Fill(DARK_NAVY),
       align=Align('left', 'center', indent=2))
    ws.row_dimensions[4].height = 4
    mc(ws, 4, 1, 4, 20, fill=Fill(TEAL))   # teal rule under header
    ws.row_dimensions[5].height = 12        # space

    # ── KPI Row ───────────────────────────────────────────────────────────────
    r = 6

    # Set column widths
    for col in range(1, 21):
        ws.column_dimensions[get_column_letter(col)].width = 10

    kpi_card(ws, r, 1, 'ACTIVE CLIENTS',
             "=COUNTIF('Client CRM'!C:C,\"Active\")",
             'from Client CRM', accent=TEAL)
    kpi_card(ws, r, 4, 'MONTHLY RECURRING REVENUE',
             "=SUMIF('Client CRM'!C:C,\"Active\",'Client CRM'!F:F)",
             'total active fees', accent=TEAL)
    ws.cell(row=r+1, column=4).number_format = '€#,##0'

    kpi_card(ws, r, 7, 'OPEN PIPELINE VALUE',
             "=SUMIF('Lead Pipeline'!D:D,\"<>Closed Lost\",'Lead Pipeline'!F:F)",
             'est. monthly from leads', accent=AMBER)
    ws.cell(row=r+1, column=7).number_format = '€#,##0'

    kpi_card(ws, r, 10, 'ACTIVE LEADS',
             "=COUNTIF('Lead Pipeline'!D:D,\"<>Closed Lost\")-COUNTIF('Lead Pipeline'!D:D,\"Closed Won\")",
             'in pipeline', accent=AMBER)

    kpi_card(ws, r, 13, 'TOTAL INVOICED (YTD)',
             "=SUMIF('Invoice Tracker'!G:G,\"<>Void\",'Invoice Tracker'!F:F)",
             'all non-void invoices', accent=TEAL)
    ws.cell(row=r+1, column=13).number_format = '€#,##0'

    kpi_card(ws, r, 16, 'CLOSES IN PROGRESS',
             "=COUNTIF('Monthly Close'!D:D,\"In Progress\")",
             'this month', accent=TEAL)

    r += 6   # 4 card rows + 1 rule + 1 space

    # ── Active Clients Snapshot ───────────────────────────────────────────────
    ws.row_dimensions[r].height = 8
    r += 1
    mc(ws, r, 1, r, 12, value='01 — ACTIVE CLIENT SNAPSHOT',
       font=F(bold=True, size=9, color=TEAL),
       fill=Fill(TEAL_10),
       align=Align('left', 'center', indent=1),
       border=border_all(TEAL))
    ws.row_dimensions[r].height = 18
    r += 1

    for col, label in [(1,'Client'),(3,'Package'),(5,'Fee (€)'),(7,'Close Day'),(9,'Contact'),(11,'Software')]:
        col_header(ws, r, col, label, 10)
    ws.row_dimensions[r].height = 18
    r += 1

    for i in range(1, 4):
        ws.row_dimensions[r].height = 16
        for col, formula in [
            (1, f"=IFERROR(INDEX('Client CRM'!B:B,MATCH(\"Active\",'Client CRM'!C:C,0)+{i-1}),\"\")"),
            (3, f"=IFERROR(INDEX('Client CRM'!L:L,MATCH(\"Active\",'Client CRM'!C:C,0)+{i-1}),\"\")"),
            (5, f"=IFERROR(INDEX('Client CRM'!F:F,MATCH(\"Active\",'Client CRM'!C:C,0)+{i-1}),\"\")"),
            (7, f"=IFERROR(INDEX('Client CRM'!G:G,MATCH(\"Active\",'Client CRM'!C:C,0)+{i-1}),\"\")"),
            (9, f"=IFERROR(INDEX('Client CRM'!H:H,MATCH(\"Active\",'Client CRM'!C:C,0)+{i-1}),\"\")"),
            (11, f"=IFERROR(INDEX('Client CRM'!E:E,MATCH(\"Active\",'Client CRM'!C:C,0)+{i-1}),\"\")"),
        ]:
            fill = Fill(BG_SOFT) if r % 2 == 0 else Fill(WHITE)
            sc(ws, r, col, value=formula,
               font=F(size=8.5, color=INK),
               fill=fill,
               align=Align('left', 'center'),
               border=border_all(RULE))
            ws.merge_cells(start_row=r, start_column=col, end_row=r, end_column=col+1)
        r += 1

    # ── Monthly Close Status ───────────────────────────────────────────────────
    ws.row_dimensions[r].height = 8
    r += 1
    mc(ws, r, 1, r, 12, value='02 — MONTHLY CLOSE STATUS — CURRENT PERIOD',
       font=F(bold=True, size=9, color=TEAL),
       fill=Fill(TEAL_10),
       align=Align('left', 'center', indent=1),
       border=border_all(TEAL))
    ws.row_dimensions[r].height = 18
    r += 1

    for col, label in [(1,'Client'),(3,'Status'),(5,'Bank Rec'),(7,'Reports Delivered'),(9,'Due Date'),(11,'Owner')]:
        col_header(ws, r, col, label, 10)
    ws.row_dimensions[r].height = 18
    r += 1

    for i in range(1, 4):
        ws.row_dimensions[r].height = 16
        for col, formula in [
            (1, f"=IFERROR(INDEX('Monthly Close'!C:C,{i}+1),\"\")"),
            (3, f"=IFERROR(INDEX('Monthly Close'!D:D,{i}+1),\"\")"),
            (5, f"=IFERROR(INDEX('Monthly Close'!F:F,{i}+1),\"\")"),
            (7, f"=IFERROR(INDEX('Monthly Close'!J:J,{i}+1),\"\")"),
            (9, f"=IFERROR(INDEX('Monthly Close'!K:K,{i}+1),\"\")"),
            (11, f"=IFERROR(INDEX('Monthly Close'!E:E,{i}+1),\"\")"),
        ]:
            fill = Fill(BG_SOFT) if r % 2 == 0 else Fill(WHITE)
            sc(ws, r, col, value=formula,
               font=F(size=8.5, color=INK),
               fill=fill,
               align=Align('left', 'center'),
               border=border_all(RULE))
            ws.merge_cells(start_row=r, start_column=col, end_row=r, end_column=col+1)
        r += 1

    # ── LAST UPDATED status bar ───────────────────────────────────────────────
    ws.row_dimensions[r].height = 8   # spacer
    r += 1
    ws.row_dimensions[r].height = 20
    mc(ws, r, 1, r, 8,
       value='Dashboard auto-updates when you open this file',
       font=F(size=8, color=MUTED, italic=True),
       fill=Fill(BG_SOFT),
       align=Align('left', 'center', indent=1),
       border=border_all(RULE))
    sc(ws, r, 9, value='LAST UPDATED',
       font=F(bold=True, size=8, color=MUTED),
       fill=Fill(BG_SOFT),
       align=Align('right', 'center'),
       border=border_all(RULE))
    ws.merge_cells(start_row=r, start_column=9, end_row=r, end_column=11)
    sc(ws, r, 12, value='=TEXT(NOW(),"MMMM D, YYYY")',
       font=F(bold=True, size=8.5, color=TEAL),
       fill=Fill(TEAL_10),
       align=Align('center', 'center'),
       border=Border(left=Side(style='medium', color=TEAL),
                     right=thin_side(TEAL), top=thin_side(TEAL), bottom=thin_side(TEAL)))
    ws.merge_cells(start_row=r, start_column=12, end_row=r, end_column=16)

    apply_print_settings(ws, header_end_row=5)


def build_instructions(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 1.5

    r = page_header(ws, 9, 'Instructions', 'How to use every sheet in this dashboard')

    # Freeze below the page header
    ws.freeze_panes = ws.cell(row=7, column=2)

    instructions = [
        ('00 — NAVIGATION', 'Branded landing page. Overview of all sheets and quick-start guide.'),
        ('01 — SETUP', 'Fill in the amber cells only. White cells contain formulas that reference Setup data — do not edit them. Changes to Practice Name and pricing cascade to the Pricing Calculator.'),
        ('02 — CLIENT CRM', 'Add one row per client. The Status column (Active/Churned/On Hold) drives the Dashboard KPIs. Use the Package dropdown to match your service tiers. The MRR formula at the bottom sums only Active clients.'),
        ('03 — LEAD PIPELINE', 'Add a row for each prospect. The Pipeline Value at the bottom sums all leads not marked Closed Lost. Move Stage through the dropdown — from New Inquiry to Closed Won.'),
        ('04 — PRICING CALCULATOR', 'Enter the prospect\'s details in the amber cells. The calculator produces a recommended monthly fee and cleanup estimate. Use it during diagnostic calls.'),
        ('05 — MONTHLY CLOSE', 'Add one row per client per period (e.g., "2026-07"). Use the Status and checkbox dropdowns (Yes/No) to track progress. The Close Progress row at the bottom shows your completion percentage.'),
        ('06 — INVOICE TRACKER', 'Add one row per invoice. Status drives the Outstanding balance formula at the bottom. Mark Paid invoices with the payment date. Overdue rows turn red automatically.'),
        ('07 — TAX DOCUMENTS', 'Use this sheet at year-end. One row per client per fiscal year. Track document collection across all categories. Mark items N/A if they do not apply to that client.'),
        ('08 — CAPACITY PLANNER', 'Enter your weekly available hours and admin time. Add one row per client with their average monthly hours. The sheet shows whether you are over or under capacity.'),
        ('09 — DASHBOARD', 'This sheet auto-populates from all other sheets. Do not enter data here directly. KPI cards show active clients, MRR, pipeline value, and close status in real time. Last Updated shows today\'s date.'),
        ('10 — INSTRUCTIONS', 'This sheet. Reference it anytime you are unsure about a feature.'),
    ]

    for sheet_name, desc in instructions:
        ws.row_dimensions[r].height = 36
        sc(ws, r, 2, value=sheet_name,
           font=F(bold=True, size=9, color=WHITE),
           fill=Fill(TEAL),
           align=Align('left', 'center', indent=1),
           border=border_all(TEAL))
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
        sc(ws, r, 5, value=desc,
           font=F(size=9, color=INK),
           fill=Fill(BG_SOFT),
           align=Align('left', 'center', wrap=True),
           border=border_all(RULE))
        ws.merge_cells(start_row=r, start_column=5, end_row=r, end_column=16)
        r += 1
        ws.row_dimensions[r].height = 4
        r += 1

    r += 1
    ws.row_dimensions[r].height = 30
    mc(ws, r, 2, r, 16,
       value='TIP: Only edit cells with amber background. Never edit cells with teal or dark backgrounds — those contain formulas or are read-only display areas.',
       font=F(size=9, color=INK),
       fill=Fill(AMBER_10),
       align=Align('left', 'center', wrap=True),
       border=Border(left=Side(style='medium', color=AMBER),
                     right=thin_side(RULE), top=thin_side(RULE), bottom=thin_side(RULE)))

    apply_print_settings(ws, header_end_row=7)


# ══════════════════════════════════════════════════════════════════════════════
# Main build
# ══════════════════════════════════════════════════════════════════════════════

def build():
    wb = openpyxl.Workbook()

    sheet_defs = [
        ('Navigation',        build_navigation),
        ('Setup',             build_setup),
        ('Client CRM',        build_client_crm),
        ('Lead Pipeline',     build_lead_pipeline),
        ('Pricing Calculator',build_pricing_calc),
        ('Monthly Close',     build_monthly_close),
        ('Invoice Tracker',   build_invoice_tracker),
        ('Tax Documents',     build_tax_docs),
        ('Capacity Planner',  build_capacity),
        ('Dashboard',         build_dashboard),
        ('Instructions',      build_instructions),
    ]

    wb.active.title = sheet_defs[0][0]
    for name, _ in sheet_defs[1:]:
        wb.create_sheet(name)

    # Tab colors — Navigation gets teal; rest follow original scheme
    tab_colors = [TEAL, TEAL, TEAL, TEAL, AMBER, TEAL, TEAL, TEAL, MUTED, DARK_NAVY, '00000000']
    for ws, tc in zip(wb.worksheets, tab_colors):
        if tc and tc != '00000000':
            ws.sheet_properties.tabColor = tc[2:]

    for ws, (name, builder) in zip(wb.worksheets, sheet_defs):
        print(f'  Building sheet: {name}')
        builder(ws)
        ws.sheet_view.showGridLines = False
        ws.sheet_view.zoomScale = 95

    wb.active = wb['Dashboard']

    path = f'{OUT}/Bookkeeper-Practice-Dashboard-v2.xlsx'
    wb.save(path)
    print(f'  ✓ Bookkeeper-Practice-Dashboard-v2.xlsx saved')


if __name__ == '__main__':
    print('Building consulting-grade XLSX...')
    build()
    print('XLSX done.')
