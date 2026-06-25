"""
Consulting-grade PPTX — McKinsey / Deloitte / PwC standard.
White backgrounds, teal accent-only, insight headlines, clean layouts.
Preserves all content from v2; redesigns visual layer only.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/v2-consulting/03-Client-Documents'
os.makedirs(OUT, exist_ok=True)

# ── Consulting Palette ────────────────────────────────────────────────────────
INK       = RGBColor(0x0F, 0x17, 0x2A)   # near-black
TEAL      = RGBColor(0x0F, 0x76, 0x6E)   # accent
TEAL_10   = RGBColor(0xCC, 0xFB, 0xF1)   # teal 10% tint
AMBER     = RGBColor(0xD9, 0x77, 0x06)
AMBER_10  = RGBColor(0xFE, 0xF3, 0xC7)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
BG_SOFT   = RGBColor(0xF8, 0xFA, 0xFC)
RULE      = RGBColor(0xE2, 0xE8, 0xF0)
MUTED     = RGBColor(0x64, 0x74, 0x8B)
DARK_NAVY = RGBColor(0x0F, 0x17, 0x2A)
NAVY_CARD = RGBColor(0x1E, 0x29, 0x3B)
DANGER    = RGBColor(0xEF, 0x44, 0x44)

W = Inches(13.33)
H = Inches(7.5)


def new_prs():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    return prs


def blank_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def bg(slide, color=WHITE):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def rect(slide, left, top, width, height, fill_rgb, line=False, line_rgb=None, line_w=Pt(0.5)):
    shape = slide.shapes.add_shape(1, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_rgb
    if line and line_rgb:
        shape.line.color.rgb = line_rgb
        shape.line.width = line_w
    else:
        shape.line.fill.background()
    return shape


def tb(slide, text, left, top, width, height,
       size=10, bold=False, color=None, align=PP_ALIGN.LEFT,
       italic=False, name='Calibri', wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color
    return txBox


def add_para(tf, text, size=10, bold=False, color=None,
             align=PP_ALIGN.LEFT, name='Calibri', space_before=Pt(4)):
    p = tf.add_paragraph()
    p.alignment = align
    p.space_before = space_before
    run = p.add_run()
    run.text = text
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = color
    return p


# ── Consulting Page Template ───────────────────────────────────────────────────

def page_header(slide, number, title, slide_count=10, note=''):
    """
    White slide with thin teal top rule, section number, insight title.
    """
    bg(slide, WHITE)

    # Thin teal top rule (full width, 6pt tall)
    rect(slide, 0, 0, W, Inches(0.07), TEAL)

    # Section number (01 / 10)
    tb(slide, f'{number:02d} / {slide_count:02d}',
       Inches(0.35), Inches(0.15), Inches(1.2), Inches(0.38),
       size=9, color=TEAL, bold=True)

    # Insight title
    tb(slide, title,
       Inches(0.35), Inches(0.5), W - Inches(0.7), Inches(0.7),
       size=18, bold=True, color=INK)

    # Rule under title
    rect(slide, Inches(0.35), Inches(1.18), W - Inches(0.7), Inches(0.015), RULE)

    if note:
        tb(slide, note,
           Inches(0.35), Inches(1.22), W - Inches(0.7), Inches(0.3),
           size=8.5, color=MUTED, italic=True)


def footer(slide, practice='[PRACTICE NAME]', n='', total=''):
    """Thin bottom footer: rule + practice name + page number."""
    rect(slide, 0, H - Inches(0.35), W, Inches(0.015), RULE)
    tb(slide, practice,
       Inches(0.35), H - Inches(0.34), Inches(6), Inches(0.3),
       size=7.5, color=MUTED)
    if n:
        tb(slide, f'{n} / {total}',
           W - Inches(1.5), H - Inches(0.34), Inches(1.3), Inches(0.3),
           size=7.5, color=MUTED, align=PP_ALIGN.RIGHT)


def callout(slide, left, top, width, height, text, label='KEY POINT', accent=TEAL):
    """Left-border callout: accent left bar, teal-10 fill, label + text."""
    rect(slide, left, top, width, height, TEAL_10 if accent==TEAL else AMBER_10)
    rect(slide, left, top, Inches(0.055), height, accent)
    tb(slide, label,
       left + Inches(0.12), top + Inches(0.1), width - Inches(0.2), Inches(0.28),
       size=7.5, bold=True, color=accent)
    tb(slide, text,
       left + Inches(0.12), top + Inches(0.36), width - Inches(0.2), height - Inches(0.45),
       size=10, color=INK)


def kpi_card(slide, left, top, width, height, label, value, note='', accent=TEAL):
    """
    Clean consulting KPI card: white bg, teal left accent border,
    thin outer rule border.
    """
    rect(slide, left, top, width, height, WHITE,
         line=True, line_rgb=RULE, line_w=Pt(0.5))
    # Left accent
    rect(slide, left, top, Inches(0.055), height, accent)
    # Label
    tb(slide, label,
       left + Inches(0.12), top + Inches(0.12), width - Inches(0.2), Inches(0.3),
       size=8, bold=True, color=MUTED)
    # Value
    tb(slide, value,
       left + Inches(0.12), top + Inches(0.38), width - Inches(0.2), height - Inches(0.7),
       size=22, bold=True, color=INK)
    if note:
        tb(slide, note,
           left + Inches(0.12), top + height - Inches(0.32), width - Inches(0.2), Inches(0.28),
           size=8, color=MUTED, italic=True)
    # Bottom teal rule
    rect(slide, left, top + height - Inches(0.045), width, Inches(0.045), accent)


def table_header(slide, left, top, cols_data, col_widths, height=Inches(0.38)):
    """Teal header row for a consulting table."""
    x = left
    for val, w in zip(cols_data, col_widths):
        rect(slide, x, top, w, height, TEAL)
        tb(slide, val, x + Inches(0.1), top + Inches(0.06),
           w - Inches(0.2), height - Inches(0.12),
           size=8.5, bold=True, color=WHITE)
        x += w


def table_row_c(slide, left, top, cols_data, col_widths, zebra=False, height=Inches(0.42)):
    """Consulting table data row: white / BG_SOFT zebra, thin rule borders."""
    fill = BG_SOFT if zebra else WHITE
    x = left
    for val, w in zip(cols_data, col_widths):
        rect(slide, x, top, w, height, fill,
             line=True, line_rgb=RULE, line_w=Pt(0.3))
        tb(slide, str(val), x + Inches(0.1), top + Inches(0.06),
           w - Inches(0.2), height - Inches(0.12),
           size=9.5, color=INK)
        x += w


# ══════════════════════════════════════════════════════════════════════════════
# Slides
# ══════════════════════════════════════════════════════════════════════════════

def build_slides(prs):

    # ── Slide 1: Cover ────────────────────────────────────────────────────────
    s = blank_slide(prs)
    bg(s, DARK_NAVY)

    # Thin teal left rule
    rect(s, 0, 0, Inches(0.07), H, TEAL)

    # Geometric corner accents (minimal)
    rect(s, W - Inches(2.4), H - Inches(2.4), Inches(2.4), Inches(2.4), NAVY_CARD)
    rect(s, W - Inches(1.2), H - Inches(1.2), Inches(1.2), Inches(1.2), TEAL)
    rect(s, W - Inches(0.5), H - Inches(0.5), Inches(0.5), Inches(0.5), AMBER)

    # Section badge
    rect(s, Inches(0.45), Inches(1.0), Inches(3.8), Inches(0.38), TEAL)
    tb(s, 'BOOKKEEPING SERVICES PROPOSAL',
       Inches(0.6), Inches(1.05), Inches(3.6), Inches(0.28),
       size=7.5, bold=True, color=WHITE)

    # Main title
    tb(s, 'Prepared For',
       Inches(0.45), Inches(1.6), Inches(10), Inches(0.55),
       size=13, color=MUTED)
    tb(s, '[CLIENT COMPANY]',
       Inches(0.45), Inches(2.1), Inches(10), Inches(2.0),
       size=40, bold=True, color=WHITE)

    tb(s, 'A tailored bookkeeping engagement proposal',
       Inches(0.45), Inches(4.2), Inches(9), Inches(0.55),
       size=12, color=MUTED, italic=True)

    # Thin teal rule
    rect(s, Inches(0.45), Inches(4.9), Inches(2.0), Inches(0.04), TEAL)

    # Metadata row
    tb(s, '[PRACTICE NAME]  ·  [DATE]  ·  Valid until [DATE + 14 DAYS]',
       Inches(0.45), Inches(5.1), Inches(9), Inches(0.38),
       size=9.5, color=MUTED)

    # Version line at bottom
    tb(s, 'Bookkeeper Practice Launch System  v2.0  —  Consulting Edition',
       Inches(0.45), H - Inches(0.9), Inches(9), Inches(0.38),
       size=8, color=MUTED, italic=True)

    rect(s, 0, H - Inches(0.07), W, Inches(0.07), TEAL)


    # ── Slide 2: About the Practice ──────────────────────────────────────────
    s = blank_slide(prs)
    page_header(s, 2, '[PRACTICE NAME] — Who We Are',
                note='Providing professional bookkeeping services to growing businesses')
    footer(s, n='2', total='10')

    # Left narrative block
    left_box = Inches(0.35)
    top_box = Inches(1.55)
    box_h = Inches(5.5)
    box_w = Inches(5.8)
    rect(s, left_box, top_box, box_w, box_h, WHITE,
         line=True, line_rgb=RULE, line_w=Pt(0.3))
    rect(s, left_box, top_box, Inches(0.055), box_h, TEAL)

    tb(s, 'OUR PRACTICE',
       left_box + Inches(0.15), top_box + Inches(0.2), box_w - Inches(0.3), Inches(0.35),
       size=9.5, bold=True, color=TEAL)
    tb(s,
       '[PRACTICE NAME] provides professional bookkeeping services to [TARGET CLIENT TYPE] businesses. '
       'We specialise in [SPECIALISATION] and work with clients who need accurate, timely books '
       'and clear financial reporting.\n\n'
       'Our clients receive:\n'
       '→  Clean, accurate books delivered on schedule\n'
       '→  A single point of contact who knows their business\n'
       '→  Secure access to reports and documents at all times\n'
       '→  A system that scales with their growth',
       left_box + Inches(0.15), top_box + Inches(0.65), box_w - Inches(0.3), Inches(4.6),
       size=10.5, color=INK)

    # Right KPI cards — clean consulting style
    kw = Inches(3.3)
    kh = Inches(1.55)
    kpi_card(s, Inches(6.55), Inches(1.55), kw, kh, 'CLIENTS SERVED', '[X]+', 'and growing')
    kpi_card(s, Inches(10.05), Inches(1.55), kw, kh, 'YEARS EXPERIENCE', '[X]+', 'in bookkeeping')
    kpi_card(s, Inches(6.55), Inches(3.25), kw, kh, 'SOFTWARE PLATFORMS', '[X]+', 'supported', accent=AMBER)
    kpi_card(s, Inches(10.05), Inches(3.25), kw, kh, 'AVG CLIENT TENURE', '[X] yrs', 'average')
    kpi_card(s, Inches(6.55), Inches(4.95), kw * 2 + Inches(0.2), kh,
             'TEAM / COVERAGE', '[Describe coverage]', 'e.g., dedicated bookkeeper + backup cover')


    # ── Slide 3: What We Found ────────────────────────────────────────────────
    s = blank_slide(prs)
    page_header(s, 3, 'What We Found in Your Diagnostic Review',
                note='Based on the information you shared and our initial assessment')
    footer(s, n='3', total='10')

    # Top diagnostic summary callout
    callout(s, Inches(0.35), Inches(1.55), W - Inches(0.7), Inches(0.85),
            '[Summarise what you found: current book condition, backlog, reconciliation status, '
            'reporting gaps, software issues, and the client\'s primary goal.]',
            label='DIAGNOSTIC SUMMARY')

    # Three finding columns
    finding_data = [
        ('01 — Current Situation',
         '[Describe the current state of the books, last reconciled period, and any known issues]'),
        ('02 — Primary Challenge',
         '[What is the biggest problem to solve — backlog, messy categorisation, no reporting, etc.]'),
        ('03 — Desired Outcome',
         '[What does the client want — clean books by X date, monthly reporting, tax readiness, etc.]'),
    ]

    col_w = Inches(4.1)
    for i, (title, desc) in enumerate(finding_data):
        x = Inches(0.35) + i * (col_w + Inches(0.16))
        y = Inches(2.6)
        rect(s, x, y, col_w, Inches(4.45), WHITE,
             line=True, line_rgb=RULE, line_w=Pt(0.3))
        rect(s, x, y, Inches(0.055), Inches(4.45), TEAL)
        tb(s, title, x + Inches(0.12), y + Inches(0.18),
           col_w - Inches(0.2), Inches(0.42),
           size=10, bold=True, color=TEAL)
        rect(s, x + Inches(0.12), y + Inches(0.65), col_w - Inches(0.2), Inches(0.015), RULE)
        tb(s, desc, x + Inches(0.12), y + Inches(0.75),
           col_w - Inches(0.2), Inches(3.5),
           size=10, color=INK)


    # ── Slide 4: Recommended Scope ────────────────────────────────────────────
    s = blank_slide(prs)
    page_header(s, 4, 'Recommended Scope — What We Will Do',
                note='Monthly recurring services proposed for your engagement')
    footer(s, n='4', total='10')

    # Scope table
    col_widths = [Inches(3.5), Inches(2.0), Inches(7.5)]
    table_header(s, Inches(0.2), Inches(1.55),
                 ['SERVICE', 'CADENCE', 'WHAT IS INCLUDED'], col_widths)

    scope_data = [
        ('Bookkeeping', 'Monthly',
         'Transaction categorisation, reconciliation, review, and approved adjusting entries'),
        ('Financial Reporting', 'Monthly',
         'Profit & Loss, Balance Sheet, and additional agreed reports'),
        ('Client Questions', 'Monthly',
         'Consolidated exception list and documented follow-up process'),
        ('Review Meeting', '[Cadence]',
         '[Duration] review call — walk through reports, exceptions, and next actions'),
        ('Cleanup Project', 'One-Time',
         '[Months / accounts / issues — complete description of cleanup scope]'),
    ]

    for i, row in enumerate(scope_data):
        table_row_c(s, Inches(0.2), Inches(1.93) + i * Inches(0.52), row,
                    col_widths, zebra=(i % 2 == 0))

    # Exclusion notice
    callout(s, Inches(0.2), Inches(4.85), W - Inches(0.4), Inches(0.65),
            'Tax advice, tax returns, audit/assurance, legal advice, and CFO services are '
            'excluded unless separately contracted and permitted under applicable regulations.',
            label='EXCLUSIONS', accent=AMBER)


    # ── Slide 5: Implementation Plan ─────────────────────────────────────────
    s = blank_slide(prs)
    page_header(s, 5, 'Implementation Plan — From Signature to First Close',
                note='A structured six-step onboarding process')
    footer(s, n='5', total='10')

    steps = [
        ('01', 'Sign & Pay',         'Engagement agreement signed and initial payment received.',    'Day 1'),
        ('02', 'Access & Documents', 'Secure accountant access granted; documents uploaded to portal.', 'Days 1–5'),
        ('03', 'Diagnostic Review',  'Opening balances confirmed and cleanup scope documented.',     'Week 1'),
        ('04', 'Cleanup Work',       'Prior-period cleanup completed (if applicable).',              'Weeks 2–[X]'),
        ('05', 'First Close',        'First monthly close completed — books brought current.',       '[Month/Year]'),
        ('06', 'Deliver & Refine',   'Reports delivered; process refinement call held.',             'After Close'),
    ]

    for i, (num, title, desc, timing) in enumerate(steps):
        col = i % 3
        row_ = i // 3
        x = Inches(0.2) + col * Inches(4.42)
        y = Inches(1.55) + row_ * Inches(2.6)
        card_w = Inches(4.25)
        card_h = Inches(2.4)

        rect(s, x, y, card_w, card_h, WHITE,
             line=True, line_rgb=RULE, line_w=Pt(0.3))

        # Number in teal, large
        tb(s, num, x + Inches(0.15), y + Inches(0.1), Inches(1.2), Inches(0.7),
           size=26, bold=True, color=TEAL)

        rect(s, x + Inches(0.15), y + Inches(0.78), card_w - Inches(0.3), Inches(0.015), RULE)

        tb(s, title,
           x + Inches(0.15), y + Inches(0.88), card_w - Inches(0.3), Inches(0.45),
           size=11, bold=True, color=INK)
        tb(s, desc,
           x + Inches(0.15), y + Inches(1.35), card_w - Inches(0.3), Inches(0.7),
           size=9.5, color=INK)

        # Timing badge bottom-right
        rect(s, x + card_w - Inches(1.6), y + card_h - Inches(0.38), Inches(1.5), Inches(0.32), TEAL_10)
        tb(s, timing,
           x + card_w - Inches(1.58), y + card_h - Inches(0.36), Inches(1.46), Inches(0.28),
           size=8, bold=True, color=TEAL, align=PP_ALIGN.CENTER)


    # ── Slide 6: Investment ───────────────────────────────────────────────────
    s = blank_slide(prs)
    page_header(s, 6, 'Your Investment — Transparent, Fixed Pricing',
                note='No surprises, no scope creep — agreed in writing before we start')
    footer(s, n='6', total='10')

    inv_items = [
        ('Setup / Diagnostic Fee',  '€[ ]',          'Due on acceptance',                     'one-time'),
        ('Cleanup Project',         '€[ ]',           '[50% on start / 50% on delivery]',      'one-time'),
        ('Monthly Bookkeeping',     '€[ ] / month',   'Monthly in advance by bank transfer',   'recurring'),
        ('Additional Work',         '€[ ] / hour',    'With written approval — no surprises',  'as needed'),
    ]

    row_h = Inches(1.2)
    for i, (label, amount, billing, type_) in enumerate(inv_items):
        y = Inches(1.55) + i * (row_h + Inches(0.08))

        # Row bg: alternating BG_SOFT / WHITE with rule
        rect(s, Inches(0.2), y, W - Inches(0.4), row_h, BG_SOFT if i % 2 == 0 else WHITE,
             line=True, line_rgb=RULE, line_w=Pt(0.3))

        # Left teal accent for recurring items
        accent_c = TEAL if type_ == 'recurring' else AMBER if type_ == 'one-time' else MUTED
        rect(s, Inches(0.2), y, Inches(0.055), row_h, accent_c)

        # Label + billing
        tb(s, label, Inches(0.4), y + Inches(0.18), Inches(7), Inches(0.45),
           size=12, bold=True, color=INK)
        tb(s, billing, Inches(0.4), y + Inches(0.65), Inches(7), Inches(0.38),
           size=9.5, color=MUTED, italic=True)

        # Amount box
        rect(s, Inches(9.5), y + Inches(0.12), Inches(3.6), row_h - Inches(0.24),
             TEAL_10 if type_ == 'recurring' else AMBER_10)
        rect(s, Inches(9.5), y + Inches(0.12), Inches(0.055), row_h - Inches(0.24), accent_c)
        tb(s, amount, Inches(9.6), y + Inches(0.25),
           Inches(3.4), row_h - Inches(0.5),
           size=18, bold=True, color=accent_c, align=PP_ALIGN.CENTER)

        # Type tag
        rect(s, W - Inches(1.1), y, Inches(0.9), row_h, accent_c)
        tag_text = type_.upper()
        tb(s, tag_text, W - Inches(1.08), y + Inches(0.42), Inches(0.86), Inches(0.38),
           size=7.5, bold=True, color=WHITE, align=PP_ALIGN.CENTER)


    # ── Slide 7: Why Work With Us ─────────────────────────────────────────────
    s = blank_slide(prs)
    page_header(s, 7, 'Why Choose [PRACTICE NAME] — What Sets Us Apart',
                note='Six commitments to every client we work with')
    footer(s, n='7', total='10')

    reasons = [
        ('Consistent & Reliable',   'Your books are closed on schedule, every month. No chasing, no guessing about where things stand.'),
        ('Clear Communication',      'One consolidated question list. One report delivery. No noise, no surprise requests mid-month.'),
        ('Secure by Design',         'Role-based access only. Secure portal for all documents. No passwords by email — ever.'),
        ('Scales With You',          'Whether you are at €1M or €5M revenue, the system scales without rebuilding your workflow.'),
        ('Finance-First Thinking',   'We flag issues before they become problems. Your books tell a story — we help you read it.'),
        ('One Point of Contact',     'You work directly with your bookkeeper. No call centres, no handoffs, no repeating yourself.'),
    ]

    col_w = Inches(4.1)
    row_h = Inches(2.45)
    for i, (title, desc) in enumerate(reasons):
        col = i % 3
        row_ = i // 3
        x = Inches(0.3) + col * (col_w + Inches(0.17))
        y = Inches(1.55) + row_ * (row_h + Inches(0.1))

        rect(s, x, y, col_w, row_h, WHITE,
             line=True, line_rgb=RULE, line_w=Pt(0.3))
        rect(s, x, y, Inches(0.055), row_h, TEAL)

        tb(s, title, x + Inches(0.12), y + Inches(0.2), col_w - Inches(0.2), Inches(0.45),
           size=11, bold=True, color=INK)
        rect(s, x + Inches(0.12), y + Inches(0.72), col_w - Inches(0.24), Inches(0.015), RULE)
        tb(s, desc, x + Inches(0.12), y + Inches(0.82), col_w - Inches(0.2), Inches(1.5),
           size=10, color=INK)


    # ── Slide 8: How We Work Together ────────────────────────────────────────
    s = blank_slide(prs)
    page_header(s, 8, 'How We Work Together — A Two-Way Commitment',
                note='A successful engagement requires clear responsibilities on both sides')
    footer(s, n='8', total='10')

    # Two columns
    col_w = Inches(6.25)
    col_h = Inches(5.45)

    # Left: client responsibilities
    rect(s, Inches(0.2), Inches(1.55), col_w, col_h, WHITE,
         line=True, line_rgb=RULE, line_w=Pt(0.3))
    rect(s, Inches(0.2), Inches(1.55), Inches(0.055), col_h, MUTED)
    tb(s, 'YOUR RESPONSIBILITIES',
       Inches(0.37), Inches(1.72), col_w - Inches(0.2), Inches(0.38),
       size=9.5, bold=True, color=MUTED)
    rect(s, Inches(0.37), Inches(2.15), col_w - Inches(0.2), Inches(0.015), RULE)

    client_resp = [
        'Provide complete and accurate records by the agreed deadline each month',
        'Grant secure, role-based software access (not passwords by email)',
        'Respond to transaction questions within [X] business days',
        'Review and acknowledge monthly reports',
        'Retain original source documents for the required period',
        'Engage a qualified tax professional for tax advice and filings',
    ]
    for j, resp in enumerate(client_resp):
        tb(s, f'→  {resp}',
           Inches(0.37), Inches(2.25) + j * Inches(0.7),
           col_w - Inches(0.2), Inches(0.62),
           size=9.5, color=INK)

    # Right: our commitments
    rx = Inches(6.7)
    rect(s, rx, Inches(1.55), col_w, col_h, WHITE,
         line=True, line_rgb=RULE, line_w=Pt(0.3))
    rect(s, rx, Inches(1.55), Inches(0.055), col_h, TEAL)
    tb(s, 'OUR COMMITMENTS TO YOU',
       rx + Inches(0.12), Inches(1.72), col_w - Inches(0.2), Inches(0.38),
       size=9.5, bold=True, color=TEAL)
    rect(s, rx + Inches(0.12), Inches(2.15), col_w - Inches(0.2), Inches(0.015), TEAL)

    our_resp = [
        'Close on schedule — or notify you immediately if delayed',
        'Raise questions in one batch, not scattered throughout the month',
        'Document every judgment, exception, and adjusting entry',
        'Never request passwords by ordinary email',
        'Deliver reports to your secure portal, not your inbox',
        'Flag unusual transactions or financial risks proactively',
    ]
    for j, resp in enumerate(our_resp):
        tb(s, f'→  {resp}',
           rx + Inches(0.12), Inches(2.25) + j * Inches(0.7),
           col_w - Inches(0.2), Inches(0.62),
           size=9.5, color=INK)


    # ── Slide 9: Next Steps ───────────────────────────────────────────────────
    s = blank_slide(prs)
    page_header(s, 9, 'Next Steps — How to Move Forward',
                note='Five steps from this proposal to your first monthly close')
    footer(s, n='9', total='10')

    steps_next = [
        ('Review this proposal',  'Take a few minutes to read through the scope, investment, and responsibilities. Note any questions.'),
        ('Ask your questions',    'Reply to this proposal or book a quick call: [LINK]. We want to make sure this is exactly right for you.'),
        ('Approve the scope',     'Reply with "Approved" or confirm your preferred scope option. We will send the engagement agreement.'),
        ('Sign & pay',            'Sign the engagement agreement and pay the setup fee. You will receive your portal invitation within 24 hours.'),
        ('We get started',        'We request access, collect documents, and schedule your kickoff call. First close begins [START DATE].'),
    ]

    for i, (title, desc) in enumerate(steps_next):
        y = Inches(1.6) + i * Inches(1.0)
        row_h = Inches(0.88)

        row_bg = BG_SOFT if i % 2 == 0 else WHITE
        rect(s, Inches(0.2), y, W - Inches(0.4), row_h, row_bg,
             line=True, line_rgb=RULE, line_w=Pt(0.3))

        # Step number
        rect(s, Inches(0.2), y, Inches(0.65), row_h, TEAL)
        tb(s, str(i + 1), Inches(0.2), y + Inches(0.14),
           Inches(0.65), Inches(0.6), size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

        tb(s, title, Inches(1.0), y + Inches(0.08), Inches(4.5), Inches(0.4),
           size=11, bold=True, color=INK)
        tb(s, desc, Inches(1.0), y + Inches(0.5), W - Inches(1.3), Inches(0.35),
           size=9.5, color=MUTED)

    # Validity notice
    callout(s, Inches(0.2), Inches(6.72), W - Inches(0.4), Inches(0.55),
            'This proposal is valid until [DATE + 14 DAYS]. After that date, '
            'please contact us to confirm current availability and pricing.',
            label='PROPOSAL VALIDITY', accent=AMBER)


    # ── Slide 10: Thank You / Contact ─────────────────────────────────────────
    s = blank_slide(prs)
    bg(s, DARK_NAVY)

    rect(s, 0, 0, Inches(0.07), H, TEAL)
    rect(s, W - Inches(2.0), H - Inches(2.0), Inches(2.0), Inches(2.0), NAVY_CARD)
    rect(s, W - Inches(1.0), H - Inches(1.0), Inches(1.0), Inches(1.0), TEAL)
    rect(s, W - Inches(0.4), H - Inches(0.4), Inches(0.4), Inches(0.4), AMBER)

    tb(s, 'Thank you for considering',
       Inches(0.45), Inches(1.0), Inches(11), Inches(0.7),
       size=16, color=MUTED)
    tb(s, '[PRACTICE NAME]',
       Inches(0.45), Inches(1.65), Inches(11), Inches(1.6),
       size=44, bold=True, color=WHITE)

    rect(s, Inches(0.45), Inches(3.5), Inches(2.0), Inches(0.04), TEAL)

    contact_lines = [
        ('[BOOKKEEPER NAME]', True, WHITE),
        ('[EMAIL ADDRESS]',   False, MUTED),
        ('[PHONE NUMBER]',    False, MUTED),
        ('[WEBSITE / PORTAL URL]', False, MUTED),
    ]
    for j, (line, bold_, color_) in enumerate(contact_lines):
        tb(s, line, Inches(0.45), Inches(3.7) + j * Inches(0.5),
           Inches(9), Inches(0.45), size=11, bold=bold_, color=color_)

    # Reminder badge (amber)
    rect(s, Inches(0.45), H - Inches(1.0), Inches(5.5), Inches(0.45), AMBER)
    tb(s, 'Replace all [BRACKETED TEXT] before sharing this deck with a client',
       Inches(0.55), H - Inches(0.98), Inches(5.3), Inches(0.38),
       size=8, bold=True, color=WHITE)

    rect(s, 0, H - Inches(0.07), W, Inches(0.07), TEAL)


if __name__ == '__main__':
    print('Building consulting-grade PPTX...')
    prs = new_prs()
    build_slides(prs)
    out_path = f'{OUT}/Canva-Bookkeeping-Proposal-Deck-v2.pptx'
    prs.save(out_path)
    print(f'  ✓ Canva-Bookkeeping-Proposal-Deck-v2.pptx')
    print('PPTX done.')
