"""
NOVAOPS — Airbnb Host Starter Kit
Host Operations Dashboard — Excel Builder (8 sheets)
"""

from openpyxl import Workbook
from openpyxl.styles import (Font, PatternFill, Alignment, Border, Side,
                              GradientFill)
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import ColorScaleRule, DataBarRule, CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation
import os

OUT = '/home/user/oqul-phase55-production/airbnb-host-kit/output/Airbnb-Host-Starter-Kit/03-Operations-Hub'

# ── Palette ───────────────────────────────────────────────────────────────────
NAVY    = '0F172A'
TEAL    = '0F766E'
TEAL_L  = 'CCFBF1'
TEAL_M  = '14B8A6'
AMBER   = 'D97706'
AMBER_L = 'FEF3C7'
WHITE   = 'FFFFFF'
SOFT    = 'F8FAFC'
RULE    = 'CBD5E1'
MUTED   = '64748B'
INK     = '1E293B'
GREEN   = '16A34A'
GREEN_L = 'DCFCE7'
RED     = 'DC2626'
RED_L   = 'FEE2E2'
YELLOW  = 'CA8A04'
YELLOW_L= 'FEF9C3'
BLUE    = '1D4ED8'
BLUE_L  = 'DBEAFE'
PURPLE_L= 'EDE9FE'

def fill(hex_): return PatternFill('solid', fgColor=hex_)
def font(bold=False, size=10, color=INK, name='Calibri', italic=False):
    return Font(bold=bold, size=size, color=color, name=name, italic=italic)
def align(h='left', v='center', wrap=False):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)
def border(color=RULE, thick=False):
    s = 'medium' if thick else 'thin'
    side = Side(style=s, color=color)
    return Border(left=side, right=side, top=side, bottom=side)
def bottom_border(color=RULE):
    return Border(bottom=Side(style='thin', color=color))
def col_w(ws, col_letter, width): ws.column_dimensions[col_letter].width = width
def row_h(ws, row_num, height): ws.row_dimensions[row_num].height = height

def header_row(ws, row, cols, bg=NAVY, fg=WHITE, sz=9, bold=True, height=22):
    row_h(ws, row, height)
    for col, (letter, val, width) in enumerate(cols, 1):
        c = ws.cell(row=row, column=col, value=val)
        c.fill = fill(bg); c.font = font(bold=bold, size=sz, color=fg)
        c.alignment = align('center', 'center')
        c.border = border(NAVY)
        ws.column_dimensions[get_column_letter(col)].width = width

def data_row(ws, row, values, bg=WHITE, sz=10, bold=False, number_fmt=None, height=18):
    row_h(ws, row, height)
    for col, val in enumerate(values, 1):
        c = ws.cell(row=row, column=col, value=val)
        c.fill = fill(bg); c.font = font(bold=bold, size=sz)
        c.alignment = align('left', 'center')
        c.border = bottom_border()
        if number_fmt and isinstance(val, (int, float)):
            c.number_format = number_fmt

def section_title(ws, row, text, col_span=10, bg=NAVY, sz=11):
    row_h(ws, row, 26)
    c = ws.cell(row=row, column=1, value=text)
    c.fill = fill(bg); c.font = font(bold=True, size=sz, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=col_span)

def kpi_block(ws, row, col, label, value, note='', label_bg=TEAL, value_bg=TEAL_L):
    row_h(ws, row, 18)
    row_h(ws, row+1, 28)
    row_h(ws, row+2, 16)
    lc = ws.cell(row=row, column=col, value=label.upper())
    lc.fill = fill(label_bg); lc.font = font(bold=True, size=7, color=WHITE)
    lc.alignment = align('left', 'center')
    vc = ws.cell(row=row+1, column=col, value=value)
    vc.fill = fill(value_bg); vc.font = font(bold=True, size=22, color=TEAL)
    vc.alignment = align('left', 'center')
    nc = ws.cell(row=row+2, column=col, value=note)
    nc.fill = fill(value_bg); nc.font = font(size=8, color=MUTED)
    nc.alignment = align('left', 'center')


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 1 — DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════

def build_dashboard(wb):
    ws = wb.active
    ws.title = '📊 Dashboard'
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = 'A6'

    # Title bar
    row_h(ws, 1, 36)
    c = ws.cell(row=1, column=1, value='AIRBNB HOST OPERATIONS DASHBOARD')
    c.fill = fill(NAVY); c.font = font(bold=True, size=16, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells('A1:M1')
    c2 = ws.cell(row=1, column=14, value='NOVAOPS  ·  v1.0')
    c2.fill = fill(NAVY); c2.font = font(bold=True, size=9, color=TEAL_M)
    c2.alignment = align('right', 'center')
    ws.merge_cells('N1:P1')

    # Property details row
    row_h(ws, 2, 20)
    ws.cell(row=2, column=1, value='Property Name:').font = font(bold=True, size=9)
    ws.cell(row=2, column=1).fill = fill(SOFT)
    ws.merge_cells('A2:B2')
    ws.cell(row=2, column=3, value='[YOUR PROPERTY NAME]').font = font(size=9, italic=True, color=MUTED)
    ws.merge_cells('C2:F2')
    ws.cell(row=2, column=7, value='Listing URL:').font = font(bold=True, size=9)
    ws.cell(row=2, column=7).fill = fill(SOFT)
    ws.merge_cells('G2:H2')
    ws.cell(row=2, column=9, value='[PASTE AIRBNB URL]').font = font(size=9, italic=True, color=MUTED)
    ws.merge_cells('I2:L2')
    ws.cell(row=2, column=13, value='Year:').font = font(bold=True, size=9)
    ws.cell(row=2, column=13).fill = fill(SOFT)
    ws.cell(row=2, column=14, value=2025).font = font(bold=True, size=9, color=TEAL)

    # Spacer
    row_h(ws, 3, 8)

    # Section: KPI tiles
    row_h(ws, 4, 20)
    c = ws.cell(row=4, column=1, value='THIS MONTH AT A GLANCE')
    c.font = font(bold=True, size=9, color=TEAL)
    c.fill = fill(SOFT)
    ws.merge_cells('A4:P4')

    # KPI tiles row (row 5-7)
    kpi_data = [
        ('Total Revenue', '=\'📅 Booking Tracker\'!K2', 'Gross bookings (this month)', 1),
        ('Net Profit', '=\'📅 Booking Tracker\'!N2', 'Revenue minus all expenses', 5),
        ('Bookings', '=\'📅 Booking Tracker\'!O2', 'Completed stays this month', 9),
        ('Avg Rating', '=\'⭐ Review Tracker\'!H2', 'Current average star rating', 13),
    ]
    for label, formula, note, col in kpi_data:
        kpi_block(ws, 5, col, label, formula, note)
        ws.merge_cells(start_row=5, start_column=col, end_row=5, end_column=col+3)
        ws.merge_cells(start_row=6, start_column=col, end_row=6, end_column=col+3)
        ws.merge_cells(start_row=7, start_column=col, end_row=7, end_column=col+3)

    row_h(ws, 8, 8)

    # Section: Year-to-date summary
    section_title(ws, 9, '  YEAR-TO-DATE PERFORMANCE', col_span=16)

    headers_ytd = [
        ('A', 'Month', 12), ('B', 'Revenue (€)', 13), ('C', 'Expenses (€)', 13),
        ('D', 'Net Profit (€)', 13), ('E', 'Bookings', 10), ('F', 'Nights Booked', 12),
        ('G', 'Occupancy %', 12), ('H', 'Avg Nightly Rate', 14), ('I', 'Avg Rating', 10),
    ]
    header_row(ws, 10, headers_ytd, bg=TEAL)

    months = ['January','February','March','April','May','June',
              'July','August','September','October','November','December']
    for i, month in enumerate(months):
        r = 11 + i
        bg = SOFT if i % 2 == 0 else WHITE
        row_h(ws, r, 18)
        ws.cell(row=r, column=1, value=month).fill = fill(bg)
        for col in range(2, 10):
            c = ws.cell(row=r, column=col, value=0)
            c.fill = fill(bg)
            c.font = font(size=10)
            c.alignment = align('center', 'center')
            c.border = bottom_border()
            if col in (2, 3, 4, 8):
                c.number_format = '#,##0.00'
            elif col == 7:
                c.number_format = '0.0"%"'
            elif col == 9:
                c.number_format = '0.0'

    # Totals row
    r_total = 23
    row_h(ws, r_total, 22)
    ws.cell(row=r_total, column=1, value='FULL YEAR TOTAL').fill = fill(NAVY)
    ws.cell(row=r_total, column=1).font = font(bold=True, size=10, color=WHITE)
    for col in range(2, 10):
        letter = get_column_letter(col)
        formula = f'=SUM({letter}11:{letter}22)'
        if col in (7, 9):
            formula = f'=AVERAGE({letter}11:{letter}22)'
        c = ws.cell(row=r_total, column=col, value=formula)
        c.fill = fill(TEAL)
        c.font = font(bold=True, size=10, color=WHITE)
        c.alignment = align('center', 'center')
        c.border = border(TEAL, thick=True)
        if col in (2, 3, 4, 8):
            c.number_format = '#,##0.00'

    row_h(ws, 24, 8)
    section_title(ws, 25, '  MAINTENANCE ALERTS — OPEN ITEMS', col_span=16)

    header_row(ws, 26,
        [('A','Issue',25),('B','Location',16),('C','Priority',12),
         ('D','Status',14),('E','Assigned To',18),('F','Est. Cost (€)',14)],
        bg=AMBER
    )
    alert_data = [
        ['Check boiler service date', 'Utility room', 'Medium', 'Scheduled', '[PLUMBER NAME]', ''],
        ['Replace kitchen tap washer', 'Kitchen', 'Low', 'Open', 'Self', '15'],
        ['[ADD ISSUE]', '', '', '', '', ''],
    ]
    for i, row_data in enumerate(alert_data):
        r = 27 + i
        bg = AMBER_L if i == 0 else (SOFT if i % 2 == 0 else WHITE)
        row_h(ws, r, 18)
        for col, val in enumerate(row_data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('left', 'center')
            c.border = bottom_border()

    # Column widths for dashboard
    for letter, width in [('A',14),('B',13),('C',13),('D',13),('E',10),
                           ('F',12),('G',12),('H',14),('I',10),
                           ('J',10),('K',10),('L',10),('M',10),('N',10)]:
        col_w(ws, letter, width)

    print('  ✓ Sheet: Dashboard')


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 2 — BOOKING TRACKER
# ══════════════════════════════════════════════════════════════════════════════

def build_booking_tracker(wb):
    ws = wb.create_sheet('📅 Booking Tracker')
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = 'A3'

    row_h(ws, 1, 30)
    c = ws.cell(row=1, column=1, value='BOOKING TRACKER  —  Log every booking here')
    c.fill = fill(NAVY); c.font = font(bold=True, size=13, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells('A1:P1')

    # Summary formulas row
    row_h(ws, 2, 22)
    summaries = [
        (1, 'TOTAL REVENUE:', 3, '=SUMIF(K4:K1000,"<>",K4:K1000)', '#,##0.00'),
        (5, 'NET PROFIT:', 3, '=SUMIF(N4:N1000,"<>",N4:N1000)', '#,##0.00'),
        (9, 'BOOKINGS:', 3, '=COUNTA(A4:A1000)', '0'),
        (13, 'AVG RATING:', 3, '=IFERROR(AVERAGE(O4:O1000),"—")', '0.0'),
    ]
    for col, label, span, formula, fmt in summaries:
        lc = ws.cell(row=2, column=col, value=label)
        lc.fill = fill(TEAL); lc.font = font(bold=True, size=8, color=WHITE)
        lc.alignment = align('right', 'center')
        ws.merge_cells(start_row=2, start_column=col, end_row=2, end_column=col+1)
        vc = ws.cell(row=2, column=col+2, value=formula)
        vc.fill = fill(TEAL_L); vc.font = font(bold=True, size=12, color=TEAL)
        vc.alignment = align('center', 'center')
        vc.number_format = fmt
        ws.merge_cells(start_row=2, start_column=col+2, end_row=2, end_column=col+span)

    cols = [
        ('A','Booking Ref',12),('B','Guest Name',16),('C','Check-In',12),
        ('D','Check-Out',12),('E','Nights',7),('F','Guests',7),
        ('G','Gross Rate (€)',13),('H','Cleaning Fee (€)',14),('I','Platform Fee (€)',14),
        ('J','Tax (€)',10),('K','Host Payout (€)',14),('L','Expenses (€)',12),
        ('M','Cleaning Cost (€)',15),('N','Net Profit (€)',13),('O','Rating ★',9),
        ('P','Review Left',10),('Q','Notes',25),
    ]
    header_row(ws, 3, cols, bg=NAVY)

    sample_rows = [
        ['BK-001','Sarah J.','2025-06-10','2025-06-14',4,2,480,60,72,0,408,0,80,328,5,'Yes','Lovely guests — left spotless'],
        ['BK-002','Marcus T.','2025-06-18','2025-06-21',3,3,360,60,54,0,306,0,80,226,5,'Yes','Asked about early check-in — accommodated'],
        ['BK-003','[GUEST NAME]','','','','','','','','','','','','','','',''],
    ]
    for i, row_data in enumerate(sample_rows):
        r = 4 + i
        bg = SOFT if i % 2 == 0 else WHITE
        row_h(ws, r, 18)
        for col, val in enumerate(row_data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('left', 'center')
            c.border = bottom_border()
            if col in (7,8,9,10,11,12,13,14):
                c.number_format = '#,##0.00'
            if col == 15:
                c.font = font(bold=True, size=10, color=TEAL)
                c.alignment = align('center', 'center')

    # Add empty rows for data entry
    for i in range(3, 30):
        r = 4 + len(sample_rows) + i - 3
        row_h(ws, r, 18)
        for col in range(1, 18):
            c = ws.cell(row=r, column=col, value='')
            c.fill = fill(WHITE if (r % 2 == 0) else SOFT)
            c.border = bottom_border()

    # Data validation for Review Left
    dv = DataValidation(type='list', formula1='"Yes,No,Pending"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add('P4:P1003')

    # Column widths
    for item in cols:
        col_w(ws, item[0], item[2])

    print('  ✓ Sheet: Booking Tracker')


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 3 — EXPENSE TRACKER
# ══════════════════════════════════════════════════════════════════════════════

def build_expense_tracker(wb):
    ws = wb.create_sheet('💰 Expense Tracker')
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = 'A4'

    row_h(ws, 1, 30)
    c = ws.cell(row=1, column=1, value='EXPENSE TRACKER  —  Log all property expenses for tax reporting')
    c.fill = fill(NAVY); c.font = font(bold=True, size=13, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells('A1:J1')

    # Category summary
    row_h(ws, 2, 18)
    ws.cell(row=2, column=1, value='YTD TOTAL:').fill = fill(TEAL)
    ws.cell(row=2, column=1).font = font(bold=True, size=9, color=WHITE)
    ws.cell(row=2, column=2, value='=SUMIF(E5:E1000,"<>",E5:E1000)').fill = fill(TEAL_L)
    ws.cell(row=2, column=2).font = font(bold=True, size=14, color=TEAL)
    ws.cell(row=2, column=2).number_format = '#,##0.00'
    ws.merge_cells('B2:D2')

    cols = [
        ('A','Date',12),('B','Category',20),('C','Sub-Category',22),
        ('D','Description',35),('E','Amount (€)',13),('F','Receipt',10),
        ('G','Tax Deductible',14),('H','Notes',30),
    ]
    row_h(ws, 3, 8)
    header_row(ws, 4, cols, bg=NAVY)

    categories = [
        ('2025-06-01','Cleaning','Turnover Clean','June 10 turnover — 2BR clean',80,'Yes','Yes','BK-001'),
        ('2025-06-01','Cleaning','Turnover Clean','June 18 turnover — 2BR clean',80,'Yes','Yes','BK-002'),
        ('2025-06-05','Supplies','Consumables','Coffee pods, tea, toiletries restock',28,'Yes','Yes','Receipt #47'),
        ('2025-06-08','Maintenance','Minor Repair','Kitchen tap washer replacement',22,'Yes','Yes','Self-fix'),
        ('2025-06-15','Platform Fees','Airbnb Host Fee','June platform fees (auto-deducted)',126,'No','Yes','Auto from payout'),
        ('2025-06-20','Utilities','Internet','Monthly broadband — June',45,'Yes','Yes','ISP invoice'),
        ('2025-06-20','Utilities','Electricity','June electricity bill',90,'Yes','Yes','Utility invoice'),
        ('2025-06-20','Insurance','STR Insurance','Monthly short-term rental insurance premium',55,'Yes','Yes','Policy #XYZ'),
        ('2025-06-01','Mortgage/Rent','Monthly Payment','June mortgage payment (property portion)',850,'Yes','Yes','See accountant for % calc'),
        ('2025-06-22','Supplies','Welcome Pack','Wine, coffee, local treats for 2 guests',16,'Yes','Yes','BK-001, BK-002'),
        ('[DATE]','[CATEGORY]','','[DESCRIPTION]','','','',''),
    ]

    cat_options = '"Cleaning,Supplies,Maintenance,Platform Fees,Utilities,Insurance,Mortgage/Rent,Furnishings,Marketing,Professional Services,Other"'
    dv = DataValidation(type='list', formula1=cat_options, allow_blank=True)
    ws.add_data_validation(dv)
    dv.add('B5:B1004')

    dv2 = DataValidation(type='list', formula1='"Yes,No"', allow_blank=True)
    ws.add_data_validation(dv2)
    dv2.add('F5:F1004')
    dv2.add('G5:G1004')

    for i, row_data in enumerate(categories):
        r = 5 + i
        bg = SOFT if i % 2 == 0 else WHITE
        row_h(ws, r, 18)
        for col, val in enumerate(row_data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('left', 'center')
            c.border = bottom_border()
            if col == 5 and isinstance(val, (int, float)):
                c.number_format = '#,##0.00'

    for item in cols:
        col_w(ws, item[0], item[2])

    print('  ✓ Sheet: Expense Tracker')


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 4 — PRICING CALCULATOR
# ══════════════════════════════════════════════════════════════════════════════

def build_pricing_calculator(wb):
    ws = wb.create_sheet('🧮 Pricing Calculator')
    ws.sheet_view.showGridLines = False

    row_h(ws, 1, 30)
    c = ws.cell(row=1, column=1, value='PRICING CALCULATOR  —  Find Your Optimal Nightly Rate')
    c.fill = fill(NAVY); c.font = font(bold=True, size=13, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells('A1:F1')

    # Left: inputs
    row_h(ws, 2, 12)
    section_title(ws, 3, '  STEP 1 — MONTHLY COST INPUTS', col_span=3)

    inputs = [
        ('Mortgage / Rent (monthly €)', 850),
        ('Utilities — Electricity (monthly €)', 90),
        ('Utilities — Gas / Heating (monthly €)', 50),
        ('Utilities — Internet (monthly €)', 45),
        ('Insurance — STR policy (monthly €)', 55),
        ('Cleaning cost per turnover (€)', 80),
        ('Consumables per turnover (€)', 30),
        ('Welcome pack per booking (€)', 12),
        ('Platform fee % (Airbnb host fee)', 3),
        ('Tax rate on income (%)', 20),
    ]

    for i, (label, val) in enumerate(inputs):
        r = 4 + i
        row_h(ws, r, 20)
        lc = ws.cell(row=r, column=1, value=label)
        lc.fill = fill(SOFT if i % 2 == 0 else WHITE)
        lc.font = font(size=10)
        lc.alignment = align('left', 'center')
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        vc = ws.cell(row=r, column=3, value=val)
        vc.fill = fill(TEAL_L)
        vc.font = font(bold=True, size=11, color=TEAL)
        vc.alignment = align('center', 'center')
        vc.border = border(TEAL)
        if label.endswith('%)') or label.endswith('(%)'):
            vc.number_format = '0"%"'
        else:
            vc.number_format = '#,##0.00'

    row_h(ws, 14, 12)
    section_title(ws, 15, '  STEP 2 — OCCUPANCY TARGETS', col_span=3)
    occ_inputs = [
        ('Target bookings per month', 6),
        ('Average nights per booking', 3),
        ('Total nights booked per month', '=C16*C17'),
        ('Nights available per month', 28),
        ('Target occupancy rate', '=C18/C19'),
    ]
    for i, (label, val) in enumerate(occ_inputs):
        r = 16 + i
        row_h(ws, r, 20)
        lc = ws.cell(row=r, column=1, value=label)
        lc.fill = fill(SOFT if i % 2 == 0 else WHITE)
        lc.font = font(size=10)
        lc.alignment = align('left', 'center')
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        vc = ws.cell(row=r, column=3, value=val)
        vc.fill = fill(TEAL_L)
        vc.font = font(bold=True, size=11, color=TEAL)
        vc.alignment = align('center', 'center')
        vc.border = border(TEAL)
        if label.startswith('Target occupancy') or label.startswith('Nights available'):
            pass
        if label == 'Target occupancy rate':
            vc.number_format = '0.0"%"'

    # Right: results
    row_h(ws, 3, 26)
    results_start_col = 5

    section_title_r = ws.cell(row=3, column=results_start_col,
        value='  CALCULATED RATES')
    section_title_r.fill = fill(TEAL)
    section_title_r.font = font(bold=True, size=11, color=WHITE)
    ws.merge_cells(start_row=3, start_column=5, end_row=3, end_column=6)

    results = [
        ('Total fixed monthly costs', '=(C4+C5+C6+C7+C8)', '#,##0.00'),
        ('Variable cost per turnover', '=(C9+C10+C11)', '#,##0.00'),
        ('Total variable costs (monthly)', '=F5*C16', '#,##0.00'),
        ('Total monthly costs', '=F4+F6', '#,##0.00'),
        ('Break-even nightly rate', '=F7/C18', '#,##0.00'),
        ('Min viable rate (10% margin)', '=F8*1.10', '#,##0.00'),
        ('Recommended base rate', '=F8*1.25', '#,##0.00'),
        ('Weekend premium rate (+25%)', '=F10*1.25', '#,##0.00'),
        ('Peak season rate (+50%)', '=F10*1.50', '#,##0.00'),
        ('Monthly revenue at base rate', '=F10*C18', '#,##0.00'),
        ('Monthly revenue at occupancy target', '=F10*C18*0.75', '#,##0.00'),
        ('Estimated monthly net profit', '=F14-F7', '#,##0.00'),
    ]

    labels = [r[0] for r in results]
    formulas = [r[1] for r in results]
    fmts = [r[2] for r in results]

    for i, (lbl, frm, fmt) in enumerate(results):
        r = 4 + i
        row_h(ws, r, 20)
        lc = ws.cell(row=r, column=results_start_col, value=lbl)
        bg = AMBER_L if lbl.startswith('Recommended') else (GREEN_L if lbl.startswith('Estimated') else (SOFT if i % 2 == 0 else WHITE))
        lc.fill = fill(bg); lc.font = font(bold=(lbl.startswith(('Recommended','Estimated'))), size=10)
        lc.alignment = align('left', 'center')
        vc = ws.cell(row=r, column=results_start_col+1, value=frm)
        vc.fill = fill(bg)
        vc.font = font(bold=True, size=11, color=TEAL if not lbl.startswith('Estimated') else GREEN)
        vc.alignment = align('center', 'center')
        vc.border = border(RULE)
        vc.number_format = fmt

    # Seasonal pricing table
    row_h(ws, 22, 12)
    section_title(ws, 23, '  SEASONAL PRICING GUIDE', col_span=6)
    header_row(ws, 24,
        [('A','Season',18),('B','Period',22),('C','Multiplier',12),
         ('D','Rate Formula',18),('E','Example Rate',14),('F','Notes',28)],
        bg=AMBER
    )
    seasonal = [
        ('Low Season', 'Jan–Feb, Nov', '0.85×', '=F10*0.85', '—', 'Minimise vacancies, attract longer stays'),
        ('Shoulder Season', 'Mar–May, Sep–Oct', '1.00×', '=F10', '—', 'Base rate — standard period'),
        ('High Season', 'Jun–Aug, Dec', '1.35×', '=F10*1.35', '—', 'Increase minimum stay to 3–5 nights'),
        ('Peak / Events', 'Bank holidays, local events', '1.75×', '=F10*1.75', '—', 'Monitor local event calendars monthly'),
        ('Last Minute (<3 days)', 'Any gap in calendar', '0.90×', '=F10*0.90', '—', 'Fill gaps — revenue beats vacancy'),
        ('Long Stay (7+ nights)', 'Any season', '0.92×', '=F10*0.92', '—', 'Offer weekly discount to fill calendar'),
    ]
    for i, row_data in enumerate(seasonal):
        r = 25 + i
        bg = SOFT if i % 2 == 0 else WHITE
        row_h(ws, r, 18)
        for col, val in enumerate(row_data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('left', 'center')
            c.border = bottom_border()

    for letter, width in [('A',26),('B',22),('C',12),('D',16),('E',14),('F',28)]:
        col_w(ws, letter, width)

    print('  ✓ Sheet: Pricing Calculator')


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 5 — CLEANING SCHEDULE
# ══════════════════════════════════════════════════════════════════════════════

def build_cleaning_schedule(wb):
    ws = wb.create_sheet('🧹 Cleaning Schedule')
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = 'A3'

    row_h(ws, 1, 30)
    c = ws.cell(row=1, column=1, value='CLEANING SCHEDULE  —  Track every turnover clean')
    c.fill = fill(NAVY); c.font = font(bold=True, size=13, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells('A1:J1')

    cols = [
        ('A','Check-Out Date',14),('B','Check-In Date',14),('C','Booking Ref',12),
        ('D','Cleaner',16),('E','Scheduled Time',14),('F','Duration (hrs)',13),
        ('G','Rate / Hour (€)',13),('H','Total Cost (€)',13),('I','Status',14),
        ('J','Quality Score',13),('K','Issues Found',30),
    ]
    header_row(ws, 2, cols, bg=NAVY)

    sample = [
        ['2025-06-14','2025-06-18','BK-001','[CLEANER NAME]','10:00 AM',2.5,32,80,'Complete',5,'None'],
        ['2025-06-21','2025-06-25','BK-002','[CLEANER NAME]','10:00 AM',2.5,32,80,'Complete',4,'Oven needed extra attention'],
        ['[DATE]','[DATE]','','','','','','','Scheduled','',''],
    ]
    for i, row_data in enumerate(sample):
        r = 3 + i
        bg = SOFT if i % 2 == 0 else WHITE
        row_h(ws, r, 18)
        for col, val in enumerate(row_data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('center' if col in (1,2,3,5,6,7,8,9,10) else 'left', 'center')
            c.border = bottom_border()
            if col == 8:
                c.number_format = '#,##0.00'
            if col == 9 and val == 'Complete':
                c.font = font(bold=True, size=10, color=GREEN)
            if col == 10 and isinstance(val, int):
                c.font = font(bold=True, size=10, color=TEAL)

    dv = DataValidation(type='list',
        formula1='"Scheduled,In Progress,Complete,Issue,Cancelled"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add('I3:I1002')

    for item in cols:
        col_w(ws, item[0], item[2])
    col_w(ws, 'K', 30)

    print('  ✓ Sheet: Cleaning Schedule')


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 6 — MAINTENANCE LOG
# ══════════════════════════════════════════════════════════════════════════════

def build_maintenance_log(wb):
    ws = wb.create_sheet('🔧 Maintenance Log')
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = 'A3'

    row_h(ws, 1, 30)
    c = ws.cell(row=1, column=1, value='MAINTENANCE LOG  —  Track all property issues, repairs and replacements')
    c.fill = fill(NAVY); c.font = font(bold=True, size=13, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells('A1:K1')

    cols = [
        ('A','Date Reported',14),('B','Issue',28),('C','Location',16),
        ('D','Priority',10),('E','Status',14),('F','Assigned To',16),
        ('G','Est. Cost (€)',13),('H','Actual Cost (€)',13),('I','Completion Date',14),
        ('J','Reported By',16),('K','Notes',28),
    ]
    header_row(ws, 2, cols, bg=NAVY)

    sample = [
        ['2025-06-05','Kitchen tap dripping','Kitchen','Low','Complete','Self',15,12,'2025-06-06','Host','Replaced washer — fixed'],
        ['2025-06-18','Boiler annual service due','Utility Room','Medium','Scheduled','[Boiler Co]',120,'','2025-07-15','Host','Annual legal requirement'],
        ['2025-06-22','Shower screen seal deteriorating','Bathroom 1','Low','Open','[Handyman]',45,'','','Cleaner','Noticed during turnover'],
        ['[DATE]','[ISSUE DESCRIPTION]','','High','Open','','','','','',''],
    ]
    prio_colors = {'High': RED_L, 'Medium': AMBER_L, 'Low': GREEN_L}
    status_colors = {'Complete': GREEN_L, 'Open': RED_L, 'Scheduled': YELLOW_L}

    for i, row_data in enumerate(sample):
        r = 3 + i
        row_h(ws, r, 18)
        for col, val in enumerate(row_data, 1):
            bg = WHITE
            if col == 4:
                bg = prio_colors.get(str(val), WHITE)
            elif col == 5:
                bg = status_colors.get(str(val), WHITE)
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('center' if col in (4,5,7,8,9) else 'left', 'center')
            c.border = bottom_border()
            if col in (7,8) and isinstance(val, (int, float)):
                c.number_format = '#,##0.00'
            if col in (4, 5):
                c.font = font(bold=True, size=10)

    dv1 = DataValidation(type='list', formula1='"High,Medium,Low"', allow_blank=True)
    dv2 = DataValidation(type='list',
        formula1='"Open,In Progress,Scheduled,Complete,Deferred"', allow_blank=True)
    ws.add_data_validation(dv1); dv1.add('D3:D1002')
    ws.add_data_validation(dv2); dv2.add('E3:E1002')

    for item in cols:
        col_w(ws, item[0], item[2])

    print('  ✓ Sheet: Maintenance Log')


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 7 — REVIEW TRACKER
# ══════════════════════════════════════════════════════════════════════════════

def build_review_tracker(wb):
    ws = wb.create_sheet('⭐ Review Tracker')
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = 'A4'

    row_h(ws, 1, 30)
    c = ws.cell(row=1, column=1, value='REVIEW TRACKER  —  Monitor ratings, trends and response performance')
    c.fill = fill(NAVY); c.font = font(bold=True, size=13, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells('A1:N1')

    # Summary
    row_h(ws, 2, 22)
    summaries = [
        (1, 'TOTAL REVIEWS:', '=COUNTA(A5:A1000)', '0'),
        (4, 'AVERAGE RATING:', '=IFERROR(AVERAGE(E5:E1000),"—")', '0.00'),
        (7, '5-STAR COUNT:', '=COUNTIF(E5:E1000,5)', '0'),
        (10, 'RESPONSE RATE:', '=IFERROR(COUNTIF(L5:L1000,"Yes")/COUNTA(A5:A1000),"—")', '0%'),
    ]
    for col, label, formula, fmt in summaries:
        lc = ws.cell(row=2, column=col, value=label)
        lc.fill = fill(TEAL); lc.font = font(bold=True, size=8, color=WHITE)
        lc.alignment = align('right', 'center')
        ws.merge_cells(start_row=2, start_column=col, end_row=2, end_column=col+1)
        vc = ws.cell(row=2, column=col+2, value=formula)
        vc.fill = fill(TEAL_L); vc.font = font(bold=True, size=12, color=TEAL)
        vc.alignment = align('center', 'center')
        vc.number_format = fmt
        ws.merge_cells(start_row=2, start_column=col+2, end_row=2, end_column=col+2)

    row_h(ws, 3, 8)
    cols = [
        ('A','Date',12),('B','Booking Ref',12),('C','Guest Name',16),
        ('D','Overall ★',10),('E','Cleanliness ★',12),('F','Accuracy ★',10),
        ('G','Communication ★',15),('H','Check-In ★',10),('I','Value ★',10),
        ('J','Location ★',10),('K','Review Snippet',35),('L','Response Sent',13),
        ('M','Response Date',13),('N','Action Required',20),
    ]
    header_row(ws, 4, cols, bg=NAVY)

    # Re-map H2 formula to correct column reference after header
    ws.cell(row=2, column=6, value='=IFERROR(AVERAGE(D5:D1000),"—")').number_format = '0.00'

    sample = [
        ['2025-06-14','BK-001','Sarah J.',5,5,5,5,5,5,5,'"Absolutely perfect — spotless, beautifully decorated..."','Yes','2025-06-14','None'],
        ['2025-06-21','BK-002','Marcus T.',5,5,5,5,5,4,5,'"Great place, well-equipped. Kitchen slightly small for 3."','Yes','2025-06-21','None'],
        ['[DATE]','','','','','','','','','','','No','','Review request pending'],
    ]
    for i, row_data in enumerate(sample):
        r = 5 + i
        bg = SOFT if i % 2 == 0 else WHITE
        row_h(ws, r, 22)
        for col, val in enumerate(row_data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('center' if col in range(4,12) else 'left', 'center')
            c.border = bottom_border()
            if col in range(4, 11) and isinstance(val, int) and val == 5:
                c.font = font(bold=True, size=10, color=GREEN)
            elif col in range(4, 11) and isinstance(val, int) and val <= 3:
                c.font = font(bold=True, size=10, color=RED)

    dv = DataValidation(type='list', formula1='"Yes,No,Pending"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add('L5:L1004')

    ws.column_dimensions['K'].width = 35
    ws.column_dimensions['N'].width = 20
    for item in cols:
        col_w(ws, item[0], item[2])

    print('  ✓ Sheet: Review Tracker')


# ══════════════════════════════════════════════════════════════════════════════
# SHEET 8 — ANNUAL SUMMARY
# ══════════════════════════════════════════════════════════════════════════════

def build_annual_summary(wb):
    ws = wb.create_sheet('📈 Annual Summary')
    ws.sheet_view.showGridLines = False

    row_h(ws, 1, 30)
    c = ws.cell(row=1, column=1, value='ANNUAL PERFORMANCE SUMMARY  —  Full year at a glance')
    c.fill = fill(NAVY); c.font = font(bold=True, size=13, color=WHITE)
    c.alignment = align('left', 'center')
    ws.merge_cells('A1:J1')

    cols = [
        ('A','Month',14),('B','Gross Revenue (€)',16),('C','Total Expenses (€)',16),
        ('D','Net Profit (€)',15),('E','Profit Margin',13),('F','Bookings',10),
        ('G','Nights Booked',13),('H','Occupancy %',12),('I','Avg Nightly Rate',14),
        ('J','Avg Rating ★',11),
    ]
    header_row(ws, 2, cols, bg=NAVY)

    months = ['January','February','March','April','May','June',
              'July','August','September','October','November','December']
    annual_data = [
        (850, 420, 430, '50.6%', 4, 12, '43%', 70.8, 4.9),
        (720, 390, 330, '45.8%', 3, 10, '36%', 72.0, 5.0),
        (980, 445, 535, '54.6%', 5, 16, '57%', 61.3, 4.8),
        (1100, 460, 640, '58.2%', 6, 18, '64%', 61.1, 5.0),
        (1350, 510, 840, '62.2%', 7, 21, '75%', 64.3, 4.9),
        (1680, 540, 1140, '67.9%', 8, 25, '89%', 67.2, 5.0),
        (1820, 560, 1260, '69.2%', 9, 27, '96%', 67.4, 4.8),
        (1750, 545, 1205, '68.9%', 8, 26, '93%', 67.3, 4.9),
        (1200, 490, 710, '59.2%', 6, 19, '68%', 63.2, 5.0),
        (980, 445, 535, '54.6%', 5, 15, '54%', 65.3, 4.8),
        (760, 400, 360, '47.4%', 4, 12, '43%', 63.3, 5.0),
        (1420, 520, 900, '63.4%', 7, 22, '79%', 64.5, 4.9),
    ]
    for i, (month, *row_nums) in enumerate(zip(months, annual_data)):
        r = 3 + i
        nums = annual_data[i]
        row_data = [month] + list(nums)
        bg = SOFT if i % 2 == 0 else WHITE
        row_h(ws, r, 18)
        for col, val in enumerate(row_data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('center' if col > 1 else 'left', 'center')
            c.border = bottom_border()
            if col in (2, 3, 4, 9):
                c.number_format = '#,##0.00'
            elif col == 10:
                c.font = font(bold=True, size=10, color=GREEN if val == 5.0 else TEAL)

    # Totals
    r_total = 15
    row_h(ws, r_total, 24)
    ws.cell(row=r_total, column=1, value='FULL YEAR TOTAL / AVG').fill = fill(TEAL)
    ws.cell(row=r_total, column=1).font = font(bold=True, size=10, color=WHITE)
    ws.cell(row=r_total, column=1).alignment = align('left', 'center')
    for col in range(2, 11):
        letter = get_column_letter(col)
        if col in (5, 8, 9, 10):
            formula = f'=AVERAGE({letter}3:{letter}14)'
        else:
            formula = f'=SUM({letter}3:{letter}14)'
        c = ws.cell(row=r_total, column=col, value=formula)
        c.fill = fill(TEAL)
        c.font = font(bold=True, size=10, color=WHITE)
        c.alignment = align('center', 'center')
        c.border = border(TEAL, thick=True)
        if col in (2, 3, 4):
            c.number_format = '#,##0.00'

    # Goals section
    row_h(ws, 16, 12)
    section_title(ws, 17, '  ANNUAL GOALS — TRACK YOUR TARGETS', col_span=5)
    header_row(ws, 18,
        [('A','Goal',30),('B','Target',14),('C','Actual',14),('D','Status',14),('E','Notes',30)],
        bg=AMBER
    )
    goals = [
        ['Annual gross revenue target', '€15,000', '=SUM(B3:B14)', '=IF(C19>=B19,"On Track","Below Target")', 'Update B19 with your target'],
        ['Average rating target', '4.9 ★', '=AVERAGE(J3:J14)', '=IF(C20>=4.9,"On Track","Below Target")', 'Review after each 5 bookings'],
        ['Annual occupancy target', '70%', '=AVERAGE(H3:H14)', '=IF(C21>="70%","On Track","Below Target")', 'Review pricing if below 65%'],
        ['Total bookings target', '60', '=SUM(F3:F14)', '=IF(C22>=B22,"On Track","Below Target")', 'Based on ~5 per month'],
        ['Superhost status', 'Maintain', 'Check App', 'Review Quarterly', 'Requires 4.8★, 90% response rate'],
    ]
    for i, row_data in enumerate(goals):
        r = 19 + i
        bg = SOFT if i % 2 == 0 else WHITE
        row_h(ws, r, 18)
        for col, val in enumerate(row_data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.fill = fill(bg); c.font = font(size=10)
            c.alignment = align('center' if col in (2,3,4) else 'left', 'center')
            c.border = bottom_border()

    for item in cols:
        col_w(ws, item[0], item[2])

    print('  ✓ Sheet: Annual Summary')


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('Building Airbnb Host Operations Dashboard...')
    print()
    wb = Workbook()
    build_dashboard(wb)
    build_booking_tracker(wb)
    build_expense_tracker(wb)
    build_pricing_calculator(wb)
    build_cleaning_schedule(wb)
    build_maintenance_log(wb)
    build_review_tracker(wb)
    build_annual_summary(wb)

    path = f'{OUT}/Host-Operations-Dashboard.xlsx'
    wb.save(path)
    print()
    print(f'  → Saved: Host-Operations-Dashboard.xlsx')
    print('Excel dashboard complete.')
