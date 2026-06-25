"""
Excel builder for Bookkeeper Practice Launch System v2.0
Creates a premium dashboard with KPI cards, charts, formulas,
conditional formatting, dropdowns, and 10 professional sheets.
"""
import openpyxl
from openpyxl.styles import (
    Font, PatternFill, Alignment, Border, Side,
    numbers as num_formats
)
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.series import DataPoint
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import (
    ColorScaleRule, DataBarRule, CellIsRule, FormulaRule
)
from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1
from openpyxl.drawing.image import Image as XLImage
import os

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/v2/02-Practice-Dashboard'

# ── Brand Colors (ARGB) ───────────────────────────────────────────────────────
PRI      = 'FF0F766E'
PRI_L    = 'FFCCFBF1'
SEC      = 'FF0F172A'
ACCENT   = 'FFD97706'
ACC_L    = 'FFFEF3C7'
BG       = 'FFF8FAFC'
CARD     = 'FFFFFFFF'
BORDER   = 'FFE2E8F0'
MUTED    = 'FF64748B'
WHITE    = 'FFFFFFFF'
SUCCESS  = 'FF10B981'
DANGER   = 'FFEF4444'
WARN     = 'FFF59E0B'
DARK     = 'FF1E293B'
LIGHT    = 'FFF1F5F9'


# ── Style Helpers ─────────────────────────────────────────────────────────────

def F(bold=False, size=10, color='FF0F172A', name='Inter'):
    return Font(name=name, bold=bold, size=size, color=color)


def Fill(color):
    return PatternFill('solid', fgColor=color)


def Align(h='left', v='center', wrap=False):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)


def border_thin(color=BORDER):
    s = Side(style='thin', color=color)
    return Border(left=s, right=s, top=s, bottom=s)


def border_medium(color=PRI):
    s = Side(style='medium', color=color)
    n = Side(style='thin', color=BORDER)
    return Border(left=s, right=n, top=n, bottom=n)


def border_bottom(color=BORDER):
    s = Side(style='thin', color=color)
    n = Side(style=None)
    return Border(bottom=s)


def style_cell(ws, row, col, value=None, font=None, fill=None,
               align=None, border=None, number_format=None,
               col_width=None, row_height=None):
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
    if number_format:
        cell.number_format = number_format
    if col_width:
        ws.column_dimensions[get_column_letter(col)].width = col_width
    if row_height:
        ws.row_dimensions[row].height = row_height
    return cell


def merge_style(ws, start_row, start_col, end_row, end_col,
                value='', font=None, fill=None, align=None, border=None):
    ws.merge_cells(start_row=start_row, start_column=start_col,
                   end_row=end_row, end_column=end_col)
    cell = ws.cell(row=start_row, column=start_col)
    cell.value = value
    if font:
        cell.font = font
    if fill:
        cell.fill = fill
    if align:
        cell.alignment = align
    if border:
        cell.border = border
    return cell


def sheet_header_bar(ws, title, subtitle='', row=1):
    """Dark header bar spanning columns A-P."""
    ws.row_dimensions[row].height = 36
    ws.row_dimensions[row + 1].height = 20
    # Merge A:P
    merge_style(ws, row, 1, row, 16, value=title,
                font=F(bold=True, size=14, color=WHITE, name='Poppins'),
                fill=Fill(SEC),
                align=Align('left', 'center'))
    if subtitle:
        merge_style(ws, row + 1, 1, row + 1, 16, value=subtitle,
                    font=F(size=8.5, color='FF94A3B8'),
                    fill=Fill(DARK),
                    align=Align('left', 'center'))
    # Fill remaining cells in header rows
    for col in range(1, 17):
        for r in [row, row + 1]:
            c = ws.cell(row=r, column=col)
            if not c.fill or c.fill.fgColor.rgb in ('00000000', 'FFFFFFFF', None):
                c.fill = Fill(SEC if r == row else DARK)
    return row + (2 if subtitle else 1)


def col_header(ws, row, col, label, width=14):
    c = style_cell(ws, row, col, value=label,
                   font=F(bold=True, size=8.5, color=WHITE, name='Poppins'),
                   fill=Fill(PRI),
                   align=Align('center', 'center'),
                   border=border_thin(PRI),
                   col_width=width)
    ws.row_dimensions[row].height = 22
    return c


def kpi_card(ws, start_row, start_col, title, formula_or_value, subtitle='',
             bg=PRI, text_color=WHITE, width=20, height=36):
    """Paint a KPI card as a merged cell block."""
    # Title bar
    merge_style(ws, start_row, start_col, start_row, start_col + 1,
                value=title,
                font=F(bold=True, size=7.5, color='FFCCFBF1', name='Poppins'),
                fill=Fill(bg),
                align=Align('left', 'bottom'))
    ws.row_dimensions[start_row].height = 14

    # Value
    merge_style(ws, start_row + 1, start_col, start_row + 1, start_col + 1,
                value=formula_or_value,
                font=F(bold=True, size=20, color=text_color, name='Poppins'),
                fill=Fill(bg),
                align=Align('left', 'center'))
    ws.row_dimensions[start_row + 1].height = height

    # Subtitle
    merge_style(ws, start_row + 2, start_col, start_row + 2, start_col + 1,
                value=subtitle,
                font=F(size=7.5, color='FF94A3B8' if bg == SEC else 'FFCCFBF1'),
                fill=Fill(bg),
                align=Align('left', 'top'))
    ws.row_dimensions[start_row + 2].height = 14

    # Border bottom accent
    for c in range(start_col, start_col + 2):
        ws.cell(row=start_row + 3, column=c).fill = Fill(ACCENT)
    ws.row_dimensions[start_row + 3].height = 3


# ── Sheet Builders ────────────────────────────────────────────────────────────

def build_setup(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'SETUP', 'Fill in the yellow cells — do not edit white formula cells', 1)
    r += 1

    ws.row_dimensions[r].height = 14
    r += 1

    # Practice info section
    merge_style(ws, r, 2, r, 9, value='PRACTICE INFORMATION',
                font=F(bold=True, size=9, color=WHITE, name='Poppins'),
                fill=Fill(PRI), align=Align('left', 'center'))
    ws.row_dimensions[r].height = 22
    r += 1

    setup_fields = [
        ('Practice Name', '[Your Practice Name]', True),
        ('Tagline / Descriptor', '[e.g., Bookkeeping for service businesses]', True),
        ('Owner / Bookkeeper Name', '[Your Name]', True),
        ('Email Address', '[your@email.com]', True),
        ('Phone Number', '[Your Phone]', True),
        ('Website / Portal URL', '[https://yoursite.com]', True),
        ('Bookkeeping Software Used', '[QuickBooks Online / Xero / Wave / Other]', True),
        ('Currency Symbol', '€', True),
        ('Monthly Close Day (of following month)', '15', True),
        ('Fiscal Year End Month', 'December', True),
    ]

    for label, default, editable in setup_fields:
        ws.row_dimensions[r].height = 22
        style_cell(ws, r, 2, value=label,
                   font=F(size=9, color=SEC), fill=Fill(LIGHT),
                   align=Align('left', 'center'), border=border_thin())
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=5)
        c = style_cell(ws, r, 6, value=default,
                       font=F(size=9, color=SEC, bold=editable),
                       fill=Fill(ACC_L if editable else CARD),
                       align=Align('left', 'center'), border=border_thin())
        ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=9)
        r += 1

    r += 1
    merge_style(ws, r, 2, r, 9, value='SERVICE TIERS',
                font=F(bold=True, size=9, color=WHITE, name='Poppins'),
                fill=Fill(PRI), align=Align('left', 'center'))
    ws.row_dimensions[r].height = 22
    r += 1

    # Headers
    for col, label, w in [(2,'Tier Name',18),(3,'Monthly Transactions',18),(4,'Monthly Accounts',14),(5,'Monthly Fee (€)',14),(6,'Hourly Rate (€)',14)]:
        col_header(ws, r, col, label, w)
    r += 1

    tier_data = [
        ('Essentials', 100, 3, 650, 75),
        ('Growth', 300, 6, 1200, 85),
        ('Advanced', 600, 12, 2200, 100),
    ]
    for name, txn, accts, fee, rate in tier_data:
        ws.row_dimensions[r].height = 20
        for col, val in [(2,name),(3,txn),(4,accts),(5,fee),(6,rate)]:
            style_cell(ws, r, col, value=val,
                       font=F(size=9, color=SEC),
                       fill=Fill(ACC_L), align=Align('center', 'center'),
                       border=border_thin())
        r += 1


def build_client_crm(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'CLIENT CRM', 'Master record for all active and former clients', 1)
    r += 1

    headers = [
        ('B', 'Client Name', 24), ('C', 'Status', 14), ('D', 'Entity Type', 14),
        ('E', 'Software', 14), ('F', 'Monthly Fee (€)', 15), ('G', 'Close Day', 10),
        ('H', 'Primary Contact', 18), ('I', 'Email', 22), ('J', 'Tax Preparer', 18),
        ('K', 'Start Date', 12), ('L', 'Service Package', 16), ('M', 'Notes', 24),
    ]
    for col_letter, label, width in headers:
        col = column_index_from_string(col_letter)
        col_header(ws, r, col, label, width)
    header_row = r
    r += 1

    # Sample data
    data = [
        ['Harbor Design LLC', 'Active', 'LLC', 'QuickBooks Online', 850, 15, 'Alex Morgan', 'alex@example.com', '[Tax Preparer Name]', '2025-01-01', 'Growth', ''],
        ['Oak & Pine Co.', 'Active', 'S-Corp', 'Xero', 1200, 15, 'Jamie Chen', 'jamie@example.com', '[Tax Preparer Name]', '2025-03-01', 'Advanced', ''],
        ['[Client Name]', 'Active', '[Entity]', '[Software]', 0, 15, '[Contact]', '[Email]', '[Tax Preparer]', '', 'Essentials', ''],
    ]

    for row_data in data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            fill = Fill(LIGHT) if r % 2 == 0 else Fill(CARD)
            style_cell(ws, r, col, value=val,
                       font=F(size=8.5, color=SEC), fill=fill,
                       align=Align('left', 'center'), border=border_thin())
        r += 1

    # Status dropdown
    dv = DataValidation(type='list', formula1='"Active,On Hold,Churned,Prospect"', allow_blank=True)
    dv.sqref = f'C{header_row+1}:C200'
    ws.add_data_validation(dv)

    # Package dropdown
    dv2 = DataValidation(type='list', formula1='"Essentials,Growth,Advanced"', allow_blank=True)
    dv2.sqref = f'L{header_row+1}:L200'
    ws.add_data_validation(dv2)

    # Conditional formatting for Status
    from openpyxl.formatting.rule import CellIsRule
    ws.conditional_formatting.add(
        f'C{header_row+1}:C200',
        CellIsRule(operator='equal', formula=['"Active"'],
                   fill=PatternFill('solid', fgColor=PRI_L[2:]),
                   font=Font(color=PRI[2:], bold=True, name='Inter', size=8.5))
    )
    ws.conditional_formatting.add(
        f'C{header_row+1}:C200',
        CellIsRule(operator='equal', formula=['"Churned"'],
                   fill=PatternFill('solid', fgColor='FFFEE2E2'),
                   font=Font(color=DANGER[2:], bold=True, name='Inter', size=8.5))
    )

    # Monthly revenue total
    r += 1
    merge_style(ws, r, 1, r, 4, value='TOTAL MONTHLY RECURRING REVENUE',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(PRI),
                align=Align('right', 'center'))
    style_cell(ws, r, 5,
               value=f'=SUMIF(C{header_row+1}:C200,"Active",F{header_row+1}:F200)',
               font=F(bold=True, size=11, color=WHITE, name='Poppins'),
               fill=Fill(PRI), align=Align('center', 'center'),
               number_format='€#,##0', border=border_thin(WHITE))


def build_lead_pipeline(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'LEAD PIPELINE', 'Track every prospect from first contact to closed deal', 1)
    r += 1

    headers = [
        ('B','Lead / Contact Name',22), ('C','Company',20), ('D','Stage',16),
        ('E','Source',14), ('F','Est. Monthly Fee (€)',16), ('G','Cleanup Est. (€)',14),
        ('H','Next Action',22), ('I','Next Action Date',14), ('J','Email',22), ('K','Notes',24),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r
    r += 1

    data = [
        ['Jamie Chen', 'Oak & Pine Co.', 'Diagnostic Scheduled', 'Referral', 1200, 2400, 'Run diagnostic', '2026-07-03', 'jamie@example.com', ''],
        ['[Lead Name]', '[Company]', 'New Inquiry', '[Source]', 0, 0, '[Action]', '', '[Email]', ''],
    ]

    stages = '"New Inquiry,Intake Sent,Diagnostic Scheduled,Proposal Sent,Negotiating,Closed Won,Closed Lost"'
    sources = '"Referral,Website,LinkedIn,Etsy,Cold Outreach,Other"'

    dv_stage = DataValidation(type='list', formula1=stages, allow_blank=True)
    dv_source = DataValidation(type='list', formula1=sources, allow_blank=True)
    dv_stage.sqref = f'D{header_row+1}:D200'
    dv_source.sqref = f'E{header_row+1}:E200'
    ws.add_data_validation(dv_stage)
    ws.add_data_validation(dv_source)

    for row_data in data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            fill = Fill(LIGHT) if r % 2 == 0 else Fill(CARD)
            style_cell(ws, r, col, value=val,
                       font=F(size=8.5, color=SEC), fill=fill,
                       align=Align('left', 'center'), border=border_thin())
        r += 1

    # Conditional formatting for Stage
    ws.conditional_formatting.add(
        f'D{header_row+1}:D200',
        CellIsRule(operator='equal', formula=['"Closed Won"'],
                   fill=PatternFill('solid', fgColor=PRI_L[2:]),
                   font=Font(color=PRI[2:], bold=True, name='Inter', size=8.5))
    )
    ws.conditional_formatting.add(
        f'D{header_row+1}:D200',
        CellIsRule(operator='equal', formula=['"Closed Lost"'],
                   fill=PatternFill('solid', fgColor='FFFEE2E2'),
                   font=Font(color=DANGER[2:], name='Inter', size=8.5))
    )

    # Pipeline totals
    r += 1
    for label, formula, col in [
        ('TOTAL PIPELINE VALUE (Monthly)', f'=SUMIF(D{header_row+1}:D200,"<>Closed Lost",F{header_row+1}:F200)', 5),
        ('PIPELINE COUNT', f'=COUNTIF(D{header_row+1}:D200,"<>Closed Lost")', 3),
    ]:
        merge_style(ws, r, 1, r, col - 1, value=label,
                    font=F(bold=True, size=8.5, color=WHITE), fill=Fill(ACCENT),
                    align=Align('right', 'center'))
        style_cell(ws, r, col, value=formula,
                   font=F(bold=True, size=10, color=WHITE, name='Poppins'),
                   fill=Fill(ACCENT), align=Align('center', 'center'),
                   number_format='€#,##0' if col == 5 else '0',
                   border=border_thin(WHITE))
        r += 1


def build_pricing_calc(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'PRICING CALCULATOR', 'Calculate client fees based on scope — fill yellow cells', 1)
    r += 1
    ws.row_dimensions[r].height = 10
    r += 1

    merge_style(ws, r, 2, r, 10, value='CLIENT INPUTS',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(PRI),
                align=Align('left', 'center'))
    ws.row_dimensions[r].height = 20
    r += 1

    inputs = [
        ('Monthly Bank Transactions', 150, 'txn'),
        ('Number of Bank Accounts', 3, 'accts'),
        ('Number of Credit Cards', 2, 'cards'),
        ('Has Payroll?  (1=Yes / 0=No)', 0, 'yn'),
        ('Has Sales Tax / VAT?  (1=Yes / 0=No)', 0, 'yn'),
        ('Has Multi-Entity / Class Tracking?  (1=Yes / 0=No)', 0, 'yn'),
        ('Has Foreign Currency?  (1=Yes / 0=No)', 0, 'yn'),
        ('Cleanup Months Needed', 0, 'mo'),
    ]

    input_cells = {}
    for label, default, key in inputs:
        ws.row_dimensions[r].height = 22
        style_cell(ws, r, 2, value=label,
                   font=F(size=9, color=SEC), fill=Fill(LIGHT),
                   align=Align('left', 'center'), border=border_thin())
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
        c = style_cell(ws, r, 8, value=default,
                       font=F(bold=True, size=10, color=SEC, name='Poppins'),
                       fill=Fill(ACC_L), align=Align('center', 'center'),
                       border=border_thin(ACCENT))
        ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)
        input_cells[key] = f'H{r}'
        r += 1

    r += 1
    merge_style(ws, r, 2, r, 10, value='CALCULATED FEES',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(PRI),
                align=Align('left', 'center'))
    ws.row_dimensions[r].height = 20
    r += 1

    # Base fee lookup (simplified formula)
    txn_cell = input_cells.get('txn', 'H5')
    payroll_cell = input_cells.get('yn', 'H8')

    fee_rows = [
        ('Base Monthly Fee', f'=IF({txn_cell}<=100,650,IF({txn_cell}<=300,1200,2200))'),
        ('Payroll Add-On', f'=IF({input_cells.get("yn","H8")}=1,150,0)'),
        ('Sales Tax / VAT Add-On', f'=IF({input_cells.get("yn","H9") if "H9" in (v for v in input_cells.values()) else "H9"}=1,100,0)'),
        ('Multi-Entity Add-On', f'=IF(H12=1,300,0)'),
        ('Foreign Currency Add-On', f'=IF(H13=1,200,0)'),
        ('Cleanup Project Estimate', f'=H14*400'),
    ]

    running_total_row = r
    for label, formula in fee_rows:
        ws.row_dimensions[r].height = 22
        style_cell(ws, r, 2, value=label,
                   font=F(size=9, color=SEC), fill=Fill(LIGHT),
                   align=Align('left', 'center'), border=border_thin())
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=7)
        style_cell(ws, r, 8, value=formula,
                   font=F(size=10, color=SEC, name='Poppins'),
                   fill=Fill(PRI_L), align=Align('center', 'center'),
                   border=border_thin(PRIMARY_BORDER := PRI),
                   number_format='€#,##0')
        ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)
        r += 1

    # Totals
    ws.row_dimensions[r].height = 30
    merge_style(ws, r, 2, r, 7, value='RECOMMENDED MONTHLY FEE',
                font=F(bold=True, size=11, color=WHITE, name='Poppins'), fill=Fill(PRI),
                align=Align('right', 'center'))
    style_cell(ws, r, 8,
               value=f'=SUM(H{running_total_row}:H{r-1})-H{r-1}',
               font=F(bold=True, size=16, color=WHITE, name='Poppins'),
               fill=Fill(PRI), align=Align('center', 'center'),
               number_format='€#,##0', border=border_thin(WHITE))
    ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)
    r += 1

    merge_style(ws, r, 2, r, 7, value='CLEANUP PROJECT ESTIMATE (one-time)',
                font=F(bold=True, size=10, color=WHITE), fill=Fill(ACCENT),
                align=Align('right', 'center'))
    style_cell(ws, r, 8, value=f'=H{r-1}',
               font=F(bold=True, size=14, color=WHITE, name='Poppins'),
               fill=Fill(ACCENT), align=Align('center', 'center'),
               number_format='€#,##0', border=border_thin(WHITE))
    ws.merge_cells(start_row=r, start_column=8, end_row=r, end_column=10)


def build_monthly_close(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'MONTHLY CLOSE TRACKER', 'Track close status for every client each period', 1)
    r += 1

    headers = [
        ('B','Period',12),('C','Client',22),('D','Status',16),('E','Owner',14),
        ('F','Bank Rec.',10),('G','Card Rec.',10),('H','Questions Sent',12),
        ('I','Questions Answered',16),('J','Reports Delivered',14),('K','Due Date',12),('L','Review Notes',28),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r
    r += 1

    data = [
        ['2026-07', 'Harbor Design LLC', 'In Progress', '[OWNER]', 'Yes', 'No', 'No', 'No', 'No', '2026-08-15', ''],
        ['2026-07', 'Oak & Pine Co.', 'Not Started', '[OWNER]', 'No', 'No', 'No', 'No', 'No', '2026-08-15', ''],
        ['2026-07', '[Client Name]', 'Not Started', '[OWNER]', 'No', 'No', 'No', 'No', 'No', '', ''],
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
            fill = Fill(LIGHT) if r % 2 == 0 else Fill(CARD)
            style_cell(ws, r, col, value=val,
                       font=F(size=8.5, color=SEC), fill=fill,
                       align=Align('center' if col > 3 else 'left', 'center'),
                       border=border_thin())
        r += 1

    # Conditional formatting
    ws.conditional_formatting.add(
        f'D{header_row+1}:D500',
        CellIsRule(operator='equal', formula=['"Delivered"'],
                   fill=PatternFill('solid', fgColor=PRI_L[2:]),
                   font=Font(color=PRI[2:], bold=True, name='Inter', size=8.5))
    )
    ws.conditional_formatting.add(
        f'D{header_row+1}:D500',
        CellIsRule(operator='equal', formula=['"Not Started"'],
                   fill=PatternFill('solid', fgColor='FFF1F5F9'),
                   font=Font(color=MUTED[2:], name='Inter', size=8.5))
    )
    ws.conditional_formatting.add(
        f'F{header_row+1}:J500',
        CellIsRule(operator='equal', formula=['"Yes"'],
                   fill=PatternFill('solid', fgColor=PRI_L[2:]),
                   font=Font(color=PRI[2:], bold=True, name='Inter', size=8.5))
    )
    ws.conditional_formatting.add(
        f'F{header_row+1}:J500',
        CellIsRule(operator='equal', formula=['"No"'],
                   fill=PatternFill('solid', fgColor='FFFEE2E2'),
                   font=Font(color=DANGER[2:], name='Inter', size=8.5))
    )


def build_invoice_tracker(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'INVOICE TRACKER', 'Track all invoices, payment status, and outstanding balances', 1)
    r += 1

    headers = [
        ('B','Invoice #',12),('C','Client',22),('D','Issue Date',12),('E','Due Date',12),
        ('F','Amount (€)',12),('G','Status',14),('H','Paid Date',12),
        ('I','Service Period',12),('J','Method',12),('K','Notes',24),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r
    r += 1

    data = [
        ['INV-001', 'Harbor Design LLC', '2026-07-01', '2026-07-08', 850, 'Paid', '2026-07-05', '2026-07', 'Bank Transfer', ''],
        ['INV-002', 'Oak & Pine Co.', '2026-07-01', '2026-07-08', 1200, 'Paid', '2026-07-03', '2026-07', 'Bank Transfer', ''],
        ['INV-003', '[Client Name]', '2026-08-01', '2026-08-08', 0, 'Draft', '', '2026-08', '', ''],
    ]

    status_dv = DataValidation(type='list', formula1='"Draft,Sent,Paid,Overdue,Void"', allow_blank=True)
    status_dv.sqref = f'G{header_row+1}:G500'
    ws.add_data_validation(status_dv)

    for row_data in data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            fill = Fill(LIGHT) if r % 2 == 0 else Fill(CARD)
            nf = '€#,##0' if col == 6 else None
            style_cell(ws, r, col, value=val,
                       font=F(size=8.5, color=SEC), fill=fill,
                       align=Align('center' if col > 4 else 'left', 'center'),
                       border=border_thin(), number_format=nf)
        r += 1

    # Totals
    r += 1
    ws.row_dimensions[r].height = 25
    for label, formula, col, fg in [
        ('TOTAL INVOICED', f'=SUMIF(G{header_row+1}:G500,"<>Void",F{header_row+1}:F500)', 5, PRI),
        ('TOTAL PAID', f'=SUMIF(G{header_row+1}:G500,"Paid",F{header_row+1}:F500)', 6, SUCCESS),
        ('TOTAL OUTSTANDING', f'=SUMIF(G{header_row+1}:G500,"Sent",F{header_row+1}:F500)+SUMIF(G{header_row+1}:G500,"Overdue",F{header_row+1}:F500)', 7, DANGER),
    ]:
        merge_style(ws, r, 2, r, col - 1, value=label,
                    font=F(bold=True, size=8.5, color=WHITE), fill=Fill(fg),
                    align=Align('right', 'center'))
        style_cell(ws, r, col,
                   value=formula,
                   font=F(bold=True, size=11, color=WHITE, name='Poppins'),
                   fill=Fill(fg), align=Align('center', 'center'),
                   number_format='€#,##0', border=border_thin(WHITE))
        r += 1

    ws.conditional_formatting.add(
        f'G{header_row+1}:G500',
        CellIsRule(operator='equal', formula=['"Paid"'],
                   fill=PatternFill('solid', fgColor=PRI_L[2:]),
                   font=Font(color=PRI[2:], bold=True, name='Inter', size=8.5))
    )
    ws.conditional_formatting.add(
        f'G{header_row+1}:G500',
        CellIsRule(operator='equal', formula=['"Overdue"'],
                   fill=PatternFill('solid', fgColor='FFFEE2E2'),
                   font=Font(color=DANGER[2:], bold=True, name='Inter', size=8.5))
    )


def build_tax_docs(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'TAX DOCUMENTS', 'Track year-end document collection status per client', 1)
    r += 1

    headers = [
        ('B','Client',22), ('C','Fiscal Year',10), ('D','Income Docs',12),
        ('E','Bank Stmts',10), ('F','Payroll',10), ('G','Expenses',10),
        ('H','Assets/Debt',12), ('I','Tax/Compliance',14), ('J','Owner Activity',14),
        ('K','Package Delivered',16), ('L','Tax Preparer',18), ('M','Notes',20),
    ]
    for col_letter, label, width in headers:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row = r
    r += 1

    data = [
        ['Harbor Design LLC', '2025', 'Received', 'Received', 'N/A', 'Received', 'Received', 'Pending', 'N/A', 'No', '[Tax Preparer]', ''],
        ['Oak & Pine Co.', '2025', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'No', '[Tax Preparer]', ''],
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
            fill = Fill(LIGHT) if r % 2 == 0 else Fill(CARD)
            style_cell(ws, r, col, value=val,
                       font=F(size=8.5, color=SEC), fill=fill,
                       align=Align('center' if col > 2 else 'left', 'center'),
                       border=border_thin())
        r += 1

    ws.conditional_formatting.add(
        f'D{header_row+1}:J500',
        CellIsRule(operator='equal', formula=['"Received"'],
                   fill=PatternFill('solid', fgColor=PRI_L[2:]),
                   font=Font(color=PRI[2:], bold=True, name='Inter', size=8.5))
    )


def build_capacity(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'CAPACITY PLANNER', 'Plan your available hours vs. committed client time', 1)
    r += 1
    ws.row_dimensions[r].height = 10
    r += 1

    merge_style(ws, r, 2, r, 12, value='WEEKLY CAPACITY INPUTS',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(PRI),
                align=Align('left', 'center'))
    ws.row_dimensions[r].height = 20
    r += 1

    cap_inputs = [
        ('Total available hours per week', 40),
        ('Admin / sales hours per week', 8),
        ('Buffer / training hours per week', 2),
        ('Billable hours available per week', '=C'+str(r)+'-C'+str(r+1)+'-C'+str(r+2)),
    ]

    input_refs = []
    for label, val in cap_inputs:
        ws.row_dimensions[r].height = 22
        style_cell(ws, r, 2, value=label,
                   font=F(size=9, color=SEC), fill=Fill(LIGHT),
                   align=Align('left', 'center'), border=border_thin())
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
        is_formula = isinstance(val, str)
        font_color = SEC if not is_formula else PRI
        c = style_cell(ws, r, 7, value=val,
                       font=F(bold=True, size=10, color=font_color),
                       fill=Fill(ACC_L if not is_formula else PRI_L),
                       align=Align('center', 'center'), border=border_thin())
        ws.merge_cells(start_row=r, start_column=7, end_row=r, end_column=9)
        input_refs.append(f'G{r}')
        r += 1

    r += 1
    merge_style(ws, r, 2, r, 12, value='CLIENT TIME COMMITMENTS',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(PRI),
                align=Align('left', 'center'))
    ws.row_dimensions[r].height = 20
    r += 1

    headers_cap = [
        ('B','Client',22),('C','Package',14),('D','Avg Hours/Month',16),
        ('E','Hours/Week',12),('F','Notes',28),
    ]
    for col_letter, label, width in headers_cap:
        col_header(ws, r, column_index_from_string(col_letter), label, width)
    header_row_cap = r
    r += 1

    cap_data = [
        ['Harbor Design LLC', 'Growth', 8, '=D'+str(r)+'/4', ''],
        ['Oak & Pine Co.', 'Advanced', 12, '=D'+str(r+1)+'/4', ''],
        ['[Client Name]', 'Essentials', 5, '=D'+str(r+2)+'/4', ''],
    ]

    for row_data in cap_data:
        ws.row_dimensions[r].height = 20
        for i, (col_letter, _, _) in enumerate(headers_cap):
            col = column_index_from_string(col_letter)
            val = row_data[i] if i < len(row_data) else ''
            if isinstance(val, str) and val.startswith('='):
                val = val.replace('row_number', str(r))
            fill = Fill(LIGHT) if r % 2 == 0 else Fill(CARD)
            style_cell(ws, r, col, value=val,
                       font=F(size=8.5, color=SEC), fill=fill,
                       align=Align('left' if col < 4 else 'center', 'center'),
                       border=border_thin(),
                       number_format='0.0' if col in [4, 5] else None)
        r += 1

    r += 1
    merge_style(ws, r, 2, r, 4, value='TOTAL COMMITTED HOURS/WEEK',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(SEC),
                align=Align('right', 'center'))
    style_cell(ws, r, 5,
               value=f'=SUM(E{header_row_cap+1}:E{r-1})',
               font=F(bold=True, size=12, color=WHITE, name='Poppins'),
               fill=Fill(SEC), align=Align('center', 'center'),
               number_format='0.0', border=border_thin(WHITE))


def build_dashboard(ws):
    ws.sheet_view.showGridLines = False

    # Full-width header
    r = 1
    ws.row_dimensions[r].height = 50
    merge_style(ws, r, 1, r, 20, value='BOOKKEEPER PRACTICE DASHBOARD',
                font=F(bold=True, size=22, color=WHITE, name='Poppins'),
                fill=Fill(SEC), align=Align('left', 'center'))
    ws.cell(row=r, column=1).alignment = Alignment(horizontal='left', vertical='center',
                                                    indent=2)
    r += 1
    ws.row_dimensions[r].height = 18
    merge_style(ws, r, 1, r, 20, value='v2.0  ·  Your complete practice operations overview',
                font=F(size=9, color='FF94A3B8'),
                fill=Fill(DARK), align=Align('left', 'center'))
    r += 1

    # Spacer
    ws.row_dimensions[r].height = 12
    r += 1

    # ── KPI Row 1 ─────────────────────────────────────────────────────────────
    # KPI Card 1: Active Clients
    kpi_card(ws, r, 1, 'ACTIVE CLIENTS',
             "=COUNTIF('Client CRM'!C:C,\"Active\")",
             'from Client CRM', bg=PRI)

    # KPI Card 2: MRR
    kpi_card(ws, r, 4, 'MONTHLY RECURRING REVENUE',
             "=SUMIF('Client CRM'!C:C,\"Active\",'Client CRM'!F:F)",
             'total active client fees', bg=PRI)
    ws.cell(row=r+1, column=4).number_format = '€#,##0'

    # KPI Card 3: Open Pipeline
    kpi_card(ws, r, 7, 'OPEN PIPELINE VALUE',
             "=SUMIF('Lead Pipeline'!D:D,\"<>Closed Lost\",'Lead Pipeline'!F:F)",
             'est. monthly from leads', bg=SEC, text_color=WHITE)
    ws.cell(row=r+1, column=7).number_format = '€#,##0'

    # KPI Card 4: Leads
    kpi_card(ws, r, 10, 'ACTIVE LEADS',
             "=COUNTIF('Lead Pipeline'!D:D,\"<>Closed Lost\")-COUNTIF('Lead Pipeline'!D:D,\"Closed Won\")",
             'in pipeline', bg=SEC, text_color=WHITE)

    # KPI Card 5: Invoiced This Year
    kpi_card(ws, r, 13, 'TOTAL INVOICED (YTD)',
             "=SUMIF('Invoice Tracker'!G:G,\"<>Void\",'Invoice Tracker'!F:F)",
             'all non-void invoices', bg=ACCENT, text_color=WHITE)
    ws.cell(row=r+1, column=13).number_format = '€#,##0'

    # KPI Card 6: Closes In Progress
    kpi_card(ws, r, 16, 'CLOSES IN PROGRESS',
             "=COUNTIF('Monthly Close'!D:D,\"In Progress\")",
             'this month', bg=ACCENT, text_color=WHITE)

    r += 5  # KPI cards take 4 rows + 1 spacer

    # ── Section: Active Clients Summary ───────────────────────────────────────
    ws.row_dimensions[r].height = 10
    r += 1

    merge_style(ws, r, 1, r, 12, value='ACTIVE CLIENT SNAPSHOT',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(PRI),
                align=Align('left', 'center'))
    ws.row_dimensions[r].height = 20
    r += 1

    for col, label, width in [(1,'Client',22),(3,'Package',14),(5,'Monthly Fee',12),(7,'Close Day',10),(9,'Contact',16),(11,'Software',14)]:
        col_header(ws, r, col, label, width)
    ws.row_dimensions[r].height = 20
    r += 1

    for formula_row in range(1, 4):
        ws.row_dimensions[r].height = 18
        for col, formula in [
            (1, f"=IFERROR(INDEX('Client CRM'!B:B,MATCH(\"Active\",'Client CRM'!C:C,0)+{formula_row-1}),\"\")"),
            (3, f"=IFERROR(INDEX('Client CRM'!L:L,MATCH(\"Active\",'Client CRM'!C:C,0)+{formula_row-1}),\"\")"),
            (5, f"=IFERROR(INDEX('Client CRM'!F:F,MATCH(\"Active\",'Client CRM'!C:C,0)+{formula_row-1}),\"\")"),
            (7, f"=IFERROR(INDEX('Client CRM'!G:G,MATCH(\"Active\",'Client CRM'!C:C,0)+{formula_row-1}),\"\")"),
            (9, f"=IFERROR(INDEX('Client CRM'!H:H,MATCH(\"Active\",'Client CRM'!C:C,0)+{formula_row-1}),\"\")"),
            (11, f"=IFERROR(INDEX('Client CRM'!E:E,MATCH(\"Active\",'Client CRM'!C:C,0)+{formula_row-1}),\"\")"),
        ]:
            fill = Fill(LIGHT) if r % 2 == 0 else Fill(CARD)
            style_cell(ws, r, col, value=formula, font=F(size=8.5, color=SEC),
                       fill=fill, align=Align('left', 'center'), border=border_thin())
            ws.merge_cells(start_row=r, start_column=col, end_row=r, end_column=col+1)
        r += 1

    # ── Section: Close Status This Month ──────────────────────────────────────
    ws.row_dimensions[r].height = 10
    r += 1

    merge_style(ws, r, 1, r, 12, value='MONTHLY CLOSE STATUS — CURRENT PERIOD',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(SEC),
                align=Align('left', 'center'))
    ws.row_dimensions[r].height = 20
    r += 1

    for col, label in [(1,'Client'),(3,'Status'),(5,'Bank Rec'),(7,'Reports Delivered'),(9,'Due Date'),(11,'Owner')]:
        col_header(ws, r, col, label, 14)
    ws.row_dimensions[r].height = 20
    r += 1

    for formula_row in range(1, 4):
        ws.row_dimensions[r].height = 18
        cr = r
        for col, formula in [
            (1, f"=IFERROR(INDEX('Monthly Close'!C:C,{formula_row}+1),\"\")"),
            (3, f"=IFERROR(INDEX('Monthly Close'!D:D,{formula_row}+1),\"\")"),
            (5, f"=IFERROR(INDEX('Monthly Close'!F:F,{formula_row}+1),\"\")"),
            (7, f"=IFERROR(INDEX('Monthly Close'!J:J,{formula_row}+1),\"\")"),
            (9, f"=IFERROR(INDEX('Monthly Close'!K:K,{formula_row}+1),\"\")"),
            (11, f"=IFERROR(INDEX('Monthly Close'!E:E,{formula_row}+1),\"\")"),
        ]:
            fill = Fill(LIGHT) if r % 2 == 0 else Fill(CARD)
            style_cell(ws, r, col, value=formula, font=F(size=8.5, color=SEC),
                       fill=fill, align=Align('left', 'center'), border=border_thin())
            ws.merge_cells(start_row=r, start_column=col, end_row=r, end_column=col+1)
        r += 1

    # ── Upcoming Deadlines ────────────────────────────────────────────────────
    ws.row_dimensions[r].height = 10
    r += 1

    merge_style(ws, r, 13, r, 20, value='OUTSTANDING INVOICES',
                font=F(bold=True, size=9, color=WHITE), fill=Fill(DANGER),
                align=Align('left', 'center'))
    ws.row_dimensions[r].height = 20
    r_inv = r + 1

    for col, label in [(13,'Invoice #'),(15,'Client'),(17,'Amount'),(19,'Due Date')]:
        col_header(ws, r_inv, col, label, 12)
    ws.row_dimensions[r_inv].height = 20

    # Set column widths for dashboard
    for col in range(1, 21):
        ws.column_dimensions[get_column_letter(col)].width = 11


def build_instructions(ws):
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 2

    r = sheet_header_bar(ws, 'INSTRUCTIONS', 'How to use every sheet in this dashboard', 1)
    r += 1

    from openpyxl.styles import Font as F2, PatternFill as PF2, Alignment as AL2

    instructions = [
        ('SETUP', 'Fill in the yellow cells only. White cells contain formulas that reference Setup data — do not edit them. Changes to Practice Name and pricing cascade to the Pricing Calculator.'),
        ('CLIENT CRM', 'Add one row per client. The Status column (Active/Churned/On Hold) drives the Dashboard KPIs. Use the Package dropdown to match your service tiers. The MRR formula at the bottom sums only Active clients.'),
        ('LEAD PIPELINE', 'Add a row for each prospect. The Pipeline Value at the bottom sums all leads not marked Closed Lost. Move Stage through the dropdown — from New Inquiry to Closed Won.'),
        ('PRICING CALCULATOR', 'Enter the prospect\'s details in the yellow cells. The calculator produces a recommended monthly fee and cleanup estimate using your tier pricing from Setup. Use it during diagnostic calls.'),
        ('MONTHLY CLOSE', 'Add one row per client per period (e.g., "2026-07"). Use the Status and checkbox dropdowns (Yes/No) to track progress. Conditional formatting turns cells green when complete.'),
        ('INVOICE TRACKER', 'Add one row per invoice. Status drives the Outstanding balance formula at the bottom. Mark Paid invoices with the payment date. Overdue rows turn red automatically.'),
        ('TAX DOCUMENTS', 'Use this sheet at year-end. One row per client per fiscal year. Track document collection across all categories. Mark items N/A if they do not apply to that client.'),
        ('CAPACITY PLANNER', 'Enter your weekly available hours and admin time. Add one row per client with their average monthly hours. The sheet shows whether you are over or under capacity.'),
        ('DASHBOARD', 'This sheet auto-populates from all other sheets. Do not enter data here directly. KPI cards show active clients, MRR, pipeline value, and close status in real time.'),
        ('INSTRUCTIONS', 'This sheet. Reference it anytime you are unsure about a feature.'),
    ]

    for sheet_name, desc in instructions:
        merge_style(ws, r, 2, r, 5, value=sheet_name,
                    font=F(bold=True, size=9, color=WHITE), fill=Fill(PRI),
                    align=Align('left', 'center'))
        merge_style(ws, r, 6, r, 16, value=desc,
                    font=F(size=9, color=SEC), fill=Fill(LIGHT),
                    align=Align('left', 'center', wrap=True))
        ws.row_dimensions[r].height = 36
        r += 1
        ws.row_dimensions[r].height = 4  # spacer
        r += 1

    r += 1
    merge_style(ws, r, 2, r, 16,
                value='TIP: Only edit cells with yellow background (ACC_L) or white background. Never edit cells with teal (PRI) or dark (SEC) backgrounds — those contain formulas.',
                font=F(bold=True, size=9, color=SEC), fill=Fill(ACC_L),
                align=Align('left', 'center', wrap=True))
    ws.row_dimensions[r].height = 30


# ══════════════════════════════════════════════════════════════════════════════
# Main build
# ══════════════════════════════════════════════════════════════════════════════

def build_dashboard_xlsx():
    wb = openpyxl.Workbook()

    sheet_defs = [
        ('Setup', build_setup),
        ('Client CRM', build_client_crm),
        ('Lead Pipeline', build_lead_pipeline),
        ('Pricing Calculator', build_pricing_calc),
        ('Monthly Close', build_monthly_close),
        ('Invoice Tracker', build_invoice_tracker),
        ('Tax Documents', build_tax_docs),
        ('Capacity Planner', build_capacity),
        ('Dashboard', build_dashboard),
        ('Instructions', build_instructions),
    ]

    # Rename default sheet and create all
    wb.active.title = sheet_defs[0][0]
    for name, _ in sheet_defs[1:]:
        wb.create_sheet(name)

    # Apply tab colors
    tab_colors = [PRI, PRI, PRI, ACCENT, SEC, SEC, SEC, MUTED, DARK, '00000000']
    for i, (ws, tc) in enumerate(zip(wb.worksheets, tab_colors)):
        if tc and tc != '00000000':
            ws.sheet_properties.tabColor = tc[2:]  # strip FF prefix

    # Build each sheet
    for ws, (name, builder) in zip(wb.worksheets, sheet_defs):
        builder(ws)
        ws.sheet_view.showGridLines = False
        ws.sheet_view.zoomScale = 90

    # Set Dashboard as active
    wb.active = wb['Dashboard']

    path = f'{OUT}/Bookkeeper-Practice-Dashboard-v2.xlsx'
    wb.save(path)
    print(f'  ✓ Bookkeeper-Practice-Dashboard-v2.xlsx')


if __name__ == '__main__':
    print('Building XLSX...')
    build_dashboard_xlsx()
    print('XLSX done.')
