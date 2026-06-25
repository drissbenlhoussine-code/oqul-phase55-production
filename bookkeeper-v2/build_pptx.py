"""
PPTX builder for Bookkeeper Practice Launch System v2.0
Creates a premium 10-slide Canva-ready proposal deck.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
import os

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/v2/03-Client-Documents'

# Colors
PRI    = RGBColor(0x0F, 0x76, 0x6E)
SEC    = RGBColor(0x0F, 0x17, 0x2A)
ACCENT = RGBColor(0xD9, 0x77, 0x06)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
BG     = RGBColor(0xF8, 0xFA, 0xFC)
MUTED  = RGBColor(0x64, 0x74, 0x8B)
BORDER = RGBColor(0xE2, 0xE8, 0xF0)
LIGHT  = RGBColor(0xCC, 0xFB, 0xF1)

W = Inches(13.33)
H = Inches(7.5)


def new_prs():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    return prs


def blank_slide(prs):
    layout = prs.slide_layouts[6]  # blank
    return prs.slides.add_slide(layout)


def rgb_to_hex(rgb: RGBColor):
    return f'{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}'


def add_rect(slide, left, top, width, height, fill_rgb, line_rgb=None, line_width=Pt(0)):
    from pptx.util import Emu
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_rgb
    if line_rgb:
        shape.line.color.rgb = line_rgb
        shape.line.width = line_width
    else:
        shape.line.fill.background()
    return shape


def add_text_box(slide, text, left, top, width, height,
                 font_name='Poppins', font_size=12, bold=False,
                 color=None, align=PP_ALIGN.LEFT, italic=False,
                 word_wrap=True):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = word_wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color
    return txBox


def add_para_run(tf, text, font_name='Inter', font_size=11,
                 bold=False, color=None, align=PP_ALIGN.LEFT,
                 space_before=Pt(0)):
    p = tf.add_paragraph()
    p.alignment = align
    p.space_before = space_before
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = color
    return p


def slide_bg(slide, color=BG):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def dark_header_bar(slide, title, subtitle='', height=Inches(1.4)):
    # Dark bar top
    add_rect(slide, 0, 0, W, height, SEC)
    # Primary accent left strip
    add_rect(slide, 0, 0, Inches(0.15), height, PRI)

    add_text_box(slide, title,
                 Inches(0.35), Inches(0.18), W - Inches(0.7), Inches(0.65),
                 font_name='Poppins', font_size=22, bold=True, color=WHITE)
    if subtitle:
        add_text_box(slide, subtitle,
                     Inches(0.35), Inches(0.82), W - Inches(0.7), Inches(0.45),
                     font_name='Inter', font_size=11, color=RGBColor(0x94, 0xA3, 0xB8))


def footer_bar(slide):
    add_rect(slide, 0, H - Inches(0.5), W, Inches(0.5), SEC)
    add_text_box(slide, 'Bookkeeper Practice Launch System v2.0  ·  [PRACTICE NAME]  ·  Confidential',
                 Inches(0.5), H - Inches(0.45), W - Inches(1), Inches(0.38),
                 font_name='Inter', font_size=8.5, color=RGBColor(0x64, 0x74, 0x8B),
                 align=PP_ALIGN.CENTER)


def kpi_box(slide, left, top, label, value, subtitle='', bg=PRI, width=Inches(2.8), height=Inches(1.6)):
    add_rect(slide, left, top, width, height, bg)
    # Label
    add_text_box(slide, label, left + Inches(0.15), top + Inches(0.12),
                 width - Inches(0.3), Inches(0.35),
                 font_name='Poppins', font_size=8, bold=True,
                 color=RGBColor(0xCC, 0xFB, 0xF1))
    # Value
    add_text_box(slide, value, left + Inches(0.15), top + Inches(0.42),
                 width - Inches(0.3), Inches(0.75),
                 font_name='Poppins', font_size=26, bold=True, color=WHITE)
    if subtitle:
        add_text_box(slide, subtitle, left + Inches(0.15), top + Inches(1.2),
                     width - Inches(0.3), Inches(0.3),
                     font_name='Inter', font_size=8, color=RGBColor(0x94, 0xA3, 0xB8))
    # Accent bottom
    add_rect(slide, left, top + height - Inches(0.05), width, Inches(0.05), ACCENT)


def table_row(slide, left, top, cols_data, col_widths,
              bg=BG, font_size=9.5, bold=False, height=Inches(0.38)):
    x = left
    for val, w in zip(cols_data, col_widths):
        add_rect(slide, x, top, w, height, bg)
        add_text_box(slide, str(val), x + Inches(0.1), top + Inches(0.05),
                     w - Inches(0.2), height - Inches(0.1),
                     font_name='Poppins' if bold else 'Inter',
                     font_size=font_size, bold=bold,
                     color=WHITE if bold and bg == PRI else SEC)
        x += w


def build_slides(prs):

    # ── Slide 1: Cover ────────────────────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, SEC)

    # Left accent
    add_rect(s, 0, 0, Inches(0.2), H, PRI)

    # Geometric decorations bottom-right
    add_rect(s, W - Inches(3.5), H - Inches(3.5), Inches(3.5), Inches(3.5), RGBColor(0x1E, 0x29, 0x3B))
    add_rect(s, W - Inches(2.2), H - Inches(2.2), Inches(2.2), Inches(2.2), PRI)
    add_rect(s, W - Inches(1), H - Inches(1), Inches(1), Inches(1), ACCENT)

    # Label badge
    add_rect(s, Inches(0.5), Inches(1.0), Inches(3.2), Inches(0.45), PRI)
    add_text_box(s, 'BOOKKEEPING SERVICES PROPOSAL',
                 Inches(0.65), Inches(1.05), Inches(3), Inches(0.35),
                 font_name='Poppins', font_size=7.5, bold=True, color=WHITE)

    # Main title
    add_text_box(s, 'Prepared For\n[CLIENT COMPANY]',
                 Inches(0.5), Inches(1.8), Inches(9), Inches(2.5),
                 font_name='Poppins', font_size=38, bold=True, color=WHITE)

    add_text_box(s, 'A tailored bookkeeping engagement proposal',
                 Inches(0.5), Inches(4.4), Inches(8), Inches(0.6),
                 font_name='Inter', font_size=14, color=RGBColor(0x94, 0xA3, 0xB8))

    # Line accent
    add_rect(s, Inches(0.5), Inches(5.1), Inches(2.5), Inches(0.06), PRI)

    # Meta
    add_text_box(s, '[PRACTICE NAME]  ·  [DATE]  ·  Valid until [DATE + 14 days]',
                 Inches(0.5), Inches(5.4), Inches(9), Inches(0.4),
                 font_name='Inter', font_size=10, color=RGBColor(0x64, 0x74, 0x8B))

    # Version badge
    add_rect(s, Inches(0.5), Inches(6.5), Inches(2.4), Inches(0.5), ACCENT)
    add_text_box(s, 'BOOKKEEPER PRACTICE LAUNCH SYSTEM v2.0',
                 Inches(0.6), Inches(6.55), Inches(2.2), Inches(0.38),
                 font_name='Poppins', font_size=7, bold=True, color=WHITE)


    # ── Slide 2: About the Practice ──────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, BG)
    dark_header_bar(s, 'About [PRACTICE NAME]', 'Your trusted bookkeeping partner')
    footer_bar(s)

    # Left content
    add_rect(s, Inches(0.5), Inches(1.6), Inches(5.8), Inches(5.2), WHITE)
    add_text_box(s, 'WHO WE ARE',
                 Inches(0.7), Inches(1.75), Inches(5.4), Inches(0.4),
                 font_name='Poppins', font_size=11, bold=True, color=PRI)
    add_text_box(s,
                 '[PRACTICE NAME] provides professional bookkeeping services to [TARGET CLIENT TYPE] '
                 'businesses. We specialize in [SPECIALIZATION] and work with clients who need '
                 'accurate, timely books and clear financial reporting.\n\n'
                 'Our clients get:\n'
                 '• Clean, accurate books delivered on schedule\n'
                 '• A single point of contact who knows their business\n'
                 '• Secure access to reports and documents anytime\n'
                 '• A system that scales with their growth',
                 Inches(0.7), Inches(2.2), Inches(5.4), Inches(3.5),
                 font_name='Inter', font_size=10.5, color=SEC)

    # Right stats
    kpi_box(s, Inches(6.8), Inches(1.6), 'CLIENTS SERVED', '[X]+', 'and growing', bg=PRI, width=Inches(2.9))
    kpi_box(s, Inches(10.0), Inches(1.6), 'YEARS EXPERIENCE', '[X]+', 'in bookkeeping', bg=SEC, width=Inches(2.9))
    kpi_box(s, Inches(6.8), Inches(3.5), 'SOFTWARE PLATFORMS', '[X]+', 'supported', bg=ACCENT, width=Inches(2.9))
    kpi_box(s, Inches(10.0), Inches(3.5), 'AVG CLIENT TENURE', '[X] yrs', 'average', bg=PRI, width=Inches(2.9))


    # ── Slide 3: What We Found ────────────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, BG)
    dark_header_bar(s, 'What We Found', 'Summary of your diagnostic review')
    footer_bar(s)

    # Main callout box
    add_rect(s, Inches(0.5), Inches(1.6), W - Inches(1), Inches(1.1), LIGHT)
    add_rect(s, Inches(0.5), Inches(1.6), Inches(0.12), Inches(1.1), PRI)
    add_text_box(s, 'DIAGNOSTIC SUMMARY',
                 Inches(0.75), Inches(1.68), W - Inches(1.5), Inches(0.35),
                 font_name='Poppins', font_size=9, bold=True, color=PRI)
    add_text_box(s,
                 '[Summarize what you found during the diagnostic: current book condition, backlog, '
                 'reconciliation status, reporting gaps, software issues, and the client\'s primary goal.]',
                 Inches(0.75), Inches(2.0), W - Inches(1.5), Inches(0.55),
                 font_name='Inter', font_size=10, color=SEC)

    # Three finding boxes
    finding_data = [
        ('Current Situation', '[Describe the current state of the books, last reconciled period, and any known issues]'),
        ('Primary Challenge', '[What is the biggest problem to solve — backlog, messy categorization, no reporting, etc.]'),
        ('Desired Outcome', '[What does the client want to achieve — clean books by X date, monthly reporting, tax readiness, etc.]'),
    ]

    for i, (title, desc) in enumerate(finding_data):
        x = Inches(0.5) + i * Inches(4.28)
        add_rect(s, x, Inches(2.95), Inches(4.0), Inches(3.7), WHITE)
        add_rect(s, x, Inches(2.95), Inches(4.0), Inches(0.12), PRI)
        add_text_box(s, title, x + Inches(0.15), Inches(3.12),
                     Inches(3.7), Inches(0.45),
                     font_name='Poppins', font_size=11, bold=True, color=PRI)
        add_text_box(s, desc, x + Inches(0.15), Inches(3.6),
                     Inches(3.7), Inches(2.8),
                     font_name='Inter', font_size=10, color=SEC)


    # ── Slide 4: Recommended Scope ────────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, BG)
    dark_header_bar(s, 'Recommended Scope', 'What we will do for you, every month')
    footer_bar(s)

    # Table
    col_widths = [Inches(3.5), Inches(2.0), Inches(7.3)]
    table_row(s, Inches(0.25), Inches(1.55), ['SERVICE', 'CADENCE', 'WHAT IS INCLUDED'],
              col_widths, bg=PRI, bold=True, font_size=9, height=Inches(0.42))

    scope_data = [
        ('Bookkeeping', 'Monthly', 'Transaction categorization, reconciliation, review, and approved adjusting entries'),
        ('Financial Reporting', 'Monthly', 'Profit & Loss, Balance Sheet, and additional agreed reports'),
        ('Client Questions', 'Monthly', 'Consolidated exception list and documented follow-up process'),
        ('Review Meeting', '[Cadence]', '[Duration] review call — walk through reports, exceptions, and next actions'),
        ('Cleanup Project', 'One-Time', '[Months / accounts / issues — complete description of cleanup scope]'),
    ]

    for i, row in enumerate(scope_data):
        bg = WHITE if i % 2 == 0 else BG
        table_row(s, Inches(0.25), Inches(1.97) + i * Inches(0.53), row,
                  col_widths, bg=bg, height=Inches(0.53))

    # Note
    add_rect(s, Inches(0.25), Inches(5.0), W - Inches(0.5), Inches(0.55), RGBColor(0xFE, 0xF3, 0xC7))
    add_rect(s, Inches(0.25), Inches(5.0), Inches(0.1), Inches(0.55), ACCENT)
    add_text_box(s,
                 'Tax advice, tax returns, audit/assurance, legal advice, and CFO services are excluded unless separately contracted and permitted.',
                 Inches(0.45), Inches(5.05), W - Inches(0.7), Inches(0.42),
                 font_name='Inter', font_size=9.5, color=SEC)


    # ── Slide 5: Implementation Plan ─────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, BG)
    dark_header_bar(s, 'Implementation Plan', 'How we get started — from signature to first close')
    footer_bar(s)

    steps = [
        ('1', 'Sign & Pay', 'Engagement agreement signed and initial payment received.', 'Day 1'),
        ('2', 'Access & Docs', 'Secure accountant access granted and documents uploaded to portal.', 'Days 1–5'),
        ('3', 'Diagnostic Review', 'Opening balances confirmed and cleanup scope documented.', 'Week 1'),
        ('4', 'Cleanup Work', 'Prior-period cleanup completed (if applicable).', 'Weeks 2–[X]'),
        ('5', 'First Close', 'First monthly close completed — books brought current.', '[Month/Year]'),
        ('6', 'Deliver & Refine', 'Reports delivered; process refinement call held.', 'After Close'),
    ]

    for i, (num, title, desc, timing) in enumerate(steps):
        row_y = Inches(1.55) + i * Inches(0.93)
        # Number circle (fake with square)
        add_rect(s, Inches(0.25), row_y, Inches(0.65), Inches(0.72), PRI)
        add_text_box(s, num, Inches(0.25), row_y + Inches(0.1), Inches(0.65), Inches(0.5),
                     font_name='Poppins', font_size=18, bold=True, color=WHITE,
                     align=PP_ALIGN.CENTER)

        add_rect(s, Inches(1.0), row_y, Inches(9.5), Inches(0.72), WHITE if i % 2 == 0 else BG)
        add_text_box(s, title, Inches(1.15), row_y + Inches(0.04),
                     Inches(4), Inches(0.35), font_name='Poppins', font_size=10,
                     bold=True, color=PRI)
        add_text_box(s, desc, Inches(1.15), row_y + Inches(0.38),
                     Inches(7), Inches(0.3), font_name='Inter', font_size=9, color=SEC)

        add_rect(s, Inches(10.6), row_y, Inches(2.5), Inches(0.72), BG if i % 2 == 0 else WHITE)
        add_text_box(s, timing, Inches(10.7), row_y + Inches(0.18),
                     Inches(2.3), Inches(0.35), font_name='Poppins', font_size=9.5,
                     bold=True, color=ACCENT)


    # ── Slide 6: Investment ───────────────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, SEC)

    # Full dark background — investment is premium
    add_rect(s, 0, 0, Inches(0.2), H, PRI)

    add_text_box(s, 'YOUR INVESTMENT',
                 Inches(0.5), Inches(0.3), W - Inches(1), Inches(0.55),
                 font_name='Poppins', font_size=11, bold=True, color=PRI)
    add_text_box(s, 'Transparent, fixed pricing — no surprises',
                 Inches(0.5), Inches(0.82), W - Inches(1), Inches(0.45),
                 font_name='Inter', font_size=12, color=RGBColor(0x94, 0xA3, 0xB8))

    # Investment items
    inv_items = [
        ('Setup / Diagnostic Fee', '€[ ]', 'Due on acceptance', 'One-time'),
        ('Cleanup Project', '€[ ]', '[Schedule — 50% start / 50% delivery]', 'One-time'),
        ('Monthly Bookkeeping', '€[ ] / month', 'Monthly in advance', 'Recurring'),
        ('Additional Work', '€[ ] / hour', 'With written approval', 'As needed'),
    ]

    for i, (label, amount, billing, type_) in enumerate(inv_items):
        y = Inches(1.5) + i * Inches(1.18)
        add_rect(s, Inches(0.5), y, W - Inches(1), Inches(1.1), RGBColor(0x1E, 0x29, 0x3B))
        add_text_box(s, label, Inches(0.7), y + Inches(0.12),
                     Inches(5), Inches(0.38), font_name='Poppins', font_size=12,
                     bold=True, color=WHITE)
        add_text_box(s, billing, Inches(0.7), y + Inches(0.52),
                     Inches(6), Inches(0.4), font_name='Inter', font_size=9.5,
                     color=RGBColor(0x64, 0x74, 0x8B))

        add_rect(s, Inches(9.5), y, Inches(3.6), Inches(1.1), PRI)
        add_text_box(s, amount, Inches(9.65), y + Inches(0.18),
                     Inches(3.3), Inches(0.72), font_name='Poppins', font_size=20,
                     bold=True, color=WHITE, align=PP_ALIGN.CENTER)

        add_rect(s, W - Inches(0.75), y, Inches(0.25), Inches(1.1), ACCENT if type_ == 'Recurring' else RGBColor(0x1E, 0x29, 0x3B))

    footer_bar(s)


    # ── Slide 7: Why Work With Us ─────────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, BG)
    dark_header_bar(s, 'Why Work With [PRACTICE NAME]', 'What makes us different')
    footer_bar(s)

    reasons = [
        ('Consistent & Reliable', 'Your books are closed on schedule, every month. No chasing, no guessing about where things stand.'),
        ('Clear Communication', 'One consolidated question list. One report delivery. No noise, no surprise requests mid-month.'),
        ('Secure by Design', 'Role-based access only. Secure portal for all documents. No passwords by email — ever.'),
        ('Scales With You', 'Whether you are at €1M or €5M revenue, the system scales without rebuilding your workflow.'),
        ('Finance-First Thinking', 'We flag issues before they become problems. Your books tell a story — we help you read it.'),
        ('One Point of Contact', 'You work directly with your bookkeeper. No call centres, no handoffs, no repeating yourself.'),
    ]

    for i, (title, desc) in enumerate(reasons):
        col = i % 3
        row_ = i // 3
        x = Inches(0.25) + col * Inches(4.38)
        y = Inches(1.6) + row_ * Inches(2.5)

        add_rect(s, x, y, Inches(4.2), Inches(2.3), WHITE)
        add_rect(s, x, y, Inches(0.12), Inches(2.3), PRI)
        add_rect(s, x, y + Inches(2.24), Inches(4.2), Inches(0.06), PRI)

        add_text_box(s, title, x + Inches(0.22), y + Inches(0.15),
                     Inches(3.8), Inches(0.45), font_name='Poppins', font_size=11,
                     bold=True, color=PRI)
        add_text_box(s, desc, x + Inches(0.22), y + Inches(0.65),
                     Inches(3.8), Inches(1.5), font_name='Inter', font_size=10, color=SEC)


    # ── Slide 8: Client Responsibilities ─────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, BG)
    dark_header_bar(s, 'How We Work Together', 'A successful engagement is a two-way commitment')
    footer_bar(s)

    add_rect(s, Inches(0.25), Inches(1.6), Inches(6.4), Inches(5.2), WHITE)
    add_text_box(s, 'YOUR RESPONSIBILITIES',
                 Inches(0.45), Inches(1.75), Inches(6), Inches(0.4),
                 font_name='Poppins', font_size=11, bold=True, color=PRI)

    client_resp = [
        'Provide complete and accurate records by the agreed deadline each month',
        'Grant secure, role-based software access (not passwords by email)',
        'Respond to transaction questions within [X] business days',
        'Review and acknowledge monthly reports',
        'Retain original source documents',
        'Engage a qualified tax professional for tax advice and filings',
    ]
    for resp in client_resp:
        add_text_box(s, f'→  {resp}',
                     Inches(0.45), Inches(2.25) + client_resp.index(resp) * Inches(0.6),
                     Inches(5.9), Inches(0.55), font_name='Inter', font_size=10, color=SEC)

    add_rect(s, Inches(6.9), Inches(1.6), Inches(6.2), Inches(5.2), RGBColor(0x1E, 0x29, 0x3B))
    add_text_box(s, 'OUR COMMITMENTS TO YOU',
                 Inches(7.1), Inches(1.75), Inches(5.8), Inches(0.4),
                 font_name='Poppins', font_size=11, bold=True, color=RGBColor(0xCC, 0xFB, 0xF1))

    our_resp = [
        'Close on schedule — or notify you immediately if delayed',
        'Raise questions in one batch, not scattered throughout the month',
        'Document every judgment, exception, and adjustment',
        'Never request passwords by ordinary email',
        'Deliver reports to your secure portal, not your inbox',
        'Flag unusual transactions or financial risks proactively',
    ]
    for resp in our_resp:
        add_text_box(s, f'→  {resp}',
                     Inches(7.1), Inches(2.25) + our_resp.index(resp) * Inches(0.6),
                     Inches(5.8), Inches(0.55), font_name='Inter', font_size=10,
                     color=WHITE)


    # ── Slide 9: Next Steps ───────────────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, BG)
    dark_header_bar(s, 'Next Steps', 'How to move forward')
    footer_bar(s)

    steps_next = [
        ('Review this proposal', 'Take a few minutes to read through the scope, investment, and responsibilities. Note any questions.'),
        ('Ask your questions', 'Reply to this proposal or book a quick call: [LINK]. We want to make sure this is exactly right for you.'),
        ('Approve the scope', 'Reply with "Approved" or select your preferred scope option. We\'ll send the engagement agreement.'),
        ('Sign & pay', 'Sign the engagement agreement and pay the setup fee. You\'ll receive your secure portal invitation within 24 hours.'),
        ('We get started', 'We request access, collect documents, and schedule your kickoff call. First close begins [DATE].'),
    ]

    for i, (title, desc) in enumerate(steps_next):
        y = Inches(1.65) + i * Inches(1.05)
        add_rect(s, Inches(0.25), y, Inches(0.65), Inches(0.88), PRI if i % 2 == 0 else ACCENT)
        add_text_box(s, str(i + 1), Inches(0.25), y + Inches(0.1),
                     Inches(0.65), Inches(0.65), font_name='Poppins', font_size=20,
                     bold=True, color=WHITE, align=PP_ALIGN.CENTER)

        add_rect(s, Inches(1.0), y, W - Inches(1.25), Inches(0.88),
                 WHITE if i % 2 == 0 else BG)
        add_text_box(s, title, Inches(1.2), y + Inches(0.06),
                     Inches(4), Inches(0.38), font_name='Poppins', font_size=11,
                     bold=True, color=PRI)
        add_text_box(s, desc, Inches(1.2), y + Inches(0.45),
                     W - Inches(1.5), Inches(0.38), font_name='Inter', font_size=9.5,
                     color=SEC)

    # Expiry notice
    add_rect(s, Inches(0.25), Inches(7.0), W - Inches(0.5), Inches(0.38), RGBColor(0xFE, 0xF3, 0xC7))
    add_text_box(s, '⚠  This proposal is valid until [DATE + 14 DAYS]. After that date, please contact us to confirm current availability.',
                 Inches(0.4), Inches(7.02), W - Inches(0.8), Inches(0.32),
                 font_name='Inter', font_size=9, color=SEC)


    # ── Slide 10: Thank You ───────────────────────────────────────────────────
    s = blank_slide(prs)
    slide_bg(s, SEC)

    add_rect(s, 0, 0, Inches(0.2), H, PRI)

    # Geometric
    add_rect(s, W - Inches(3), H - Inches(3), Inches(3), Inches(3), RGBColor(0x1E, 0x29, 0x3B))
    add_rect(s, W - Inches(1.8), H - Inches(1.8), Inches(1.8), Inches(1.8), PRI)
    add_rect(s, W - Inches(0.8), H - Inches(0.8), Inches(0.8), Inches(0.8), ACCENT)

    add_text_box(s, 'Thank you for\nconsidering\n[PRACTICE NAME]',
                 Inches(0.5), Inches(1.0), Inches(10), Inches(3.5),
                 font_name='Poppins', font_size=40, bold=True, color=WHITE)

    add_rect(s, Inches(0.5), Inches(4.7), Inches(2.5), Inches(0.08), PRI)

    contact_info = [
        '[PRACTICE NAME]',
        '[BOOKKEEPER NAME]',
        '[EMAIL ADDRESS]',
        '[PHONE NUMBER]',
        '[WEBSITE / PORTAL URL]',
    ]
    for i, line in enumerate(contact_info):
        add_text_box(s, line, Inches(0.5), Inches(5.0) + i * Inches(0.4),
                     Inches(8), Inches(0.38), font_name='Inter', font_size=11,
                     color=WHITE if i == 0 else RGBColor(0x94, 0xA3, 0xB8),
                     bold=(i == 0))

    add_rect(s, Inches(0.5), Inches(7.1), Inches(3.5), Inches(0.38), ACCENT)
    add_text_box(s, 'Replace all [BRACKETED TEXT] before sharing with a client',
                 Inches(0.55), Inches(7.13), Inches(3.4), Inches(0.32),
                 font_name='Poppins', font_size=7.5, bold=True, color=WHITE)

    footer_bar(s)


if __name__ == '__main__':
    print('Building PPTX...')
    prs = new_prs()
    build_slides(prs)
    out_path = f'{OUT}/Canva-Bookkeeping-Proposal-Deck-v2.pptx'
    prs.save(out_path)
    print(f'  ✓ Canva-Bookkeeping-Proposal-Deck-v2.pptx')
    print('PPTX done.')
