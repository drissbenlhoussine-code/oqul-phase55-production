"""
Build premium CSV files and package the final ZIP.
"""
import csv, os, shutil, zipfile
from datetime import datetime

OUT = '/home/user/oqul-phase55-production/bookkeeper-v2/v2'
SRC = '/home/user/oqul-phase55-production/bookkeeper-v2/original/Bookkeeper-Practice-Launch-System/05-Notion-Import'
DEST = f'{OUT}/05-Notion-Workspace'


def write_csv(filename, headers, rows):
    path = os.path.join(DEST, filename)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(headers)
        w.writerows(rows)
    print(f'  ✓ {filename}')


def build_csvs():
    # Clients.csv — expanded
    write_csv('Clients.csv',
        ['Client', 'Status', 'Entity Type', 'Jurisdiction', 'Software', 'Monthly Fee',
         'Close Day', 'Primary Contact', 'Email', 'Phone', 'Tax Preparer', 'Tax Preparer Email',
         'Start Date', 'Service Package', 'Accounts Count', 'Avg Monthly Transactions',
         'Has Payroll', 'Has Sales Tax/VAT', 'Portal Link', 'Notes'],
        [
            ['Harbor Design LLC', 'Active', 'LLC', 'Ireland', 'QuickBooks Online', 850, 15,
             'Alex Morgan', 'alex@example.com', '+353-1-555-0001', 'Smith & Co. Accountants',
             'tax@smithco.ie', '2025-01-15', 'Growth', 3, 120, 'No', 'No',
             'https://portal.example.com/harbor', 'Sample row — replace with real client data'],
            ['Oak & Pine Co.', 'Active', 'S-Corp', 'Ireland', 'Xero', 1200, 15,
             'Jamie Chen', 'jamie@example.com', '+353-1-555-0002', 'Jones & Partners',
             'tax@jonespartners.ie', '2025-03-01', 'Advanced', 6, 280, 'Yes', 'Yes',
             'https://portal.example.com/oak', 'Multi-class tracking; payroll via Thrive'],
            ['[Client Name]', 'Active', '[Entity Type]', '[Jurisdiction]', '[Software]', 0, 15,
             '[Contact Name]', '[email@example.com]', '[Phone]', '[Tax Preparer]', '[Tax Email]',
             '', 'Essentials', 0, 0, 'No', 'No', '[Portal URL]', ''],
        ]
    )

    # Leads.csv — expanded
    write_csv('Leads.csv',
        ['Lead', 'Company', 'Stage', 'Source', 'Estimated Monthly Fee', 'Cleanup Estimate',
         'Next Action', 'Next Action Date', 'Email', 'Phone', 'Industry', 'Software',
         'Avg Transactions', 'Has Payroll', 'Referred By', 'Proposal Sent Date', 'Notes'],
        [
            ['Jamie Chen', 'Oak & Pine Co.', 'Diagnostic Scheduled', 'Referral', 1200, 2400,
             'Run diagnostic call', '2026-07-03', 'jamie@example.com', '+353-1-555-0002',
             'Retail', 'Xero', 280, 'Yes', 'Alex Morgan', '', 'Sample — already converted to client'],
            ['Sarah Li', 'Bright Coast Events', 'Intake Sent', 'LinkedIn', 800, 0,
             'Follow up on intake form', '2026-07-10', 'sarah@example.com', '',
             'Events / Hospitality', 'QuickBooks Online', 90, 'No', '', '', 'Reached out via DM'],
            ['[Lead Name]', '[Company]', 'New Inquiry', '[Source]', 0, 0,
             '[Next Action]', '', '[Email]', '', '[Industry]', '[Software]', 0, 'No', '', '', ''],
        ]
    )

    # Monthly-Close.csv — expanded
    write_csv('Monthly-Close.csv',
        ['Period', 'Client', 'Status', 'Owner', 'Bank Reconciled', 'Cards Reconciled',
         'Loans Reconciled', 'Payroll Reconciled', 'Questions Sent', 'Questions Answered',
         'Adjustments Posted', 'Reports Delivered', 'Due Date', 'Delivered Date',
         'Report Package', 'Review Notes'],
        [
            ['2026-07', 'Harbor Design LLC', 'In Progress', '[OWNER]', 'Yes', 'No', 'N/A', 'N/A',
             'No', 'No', 'No', 'No', '2026-08-15', '', 'P&L, Balance Sheet', ''],
            ['2026-07', 'Oak & Pine Co.', 'Not Started', '[OWNER]', 'No', 'No', 'No', 'No',
             'No', 'No', 'No', 'No', '2026-08-15', '', 'P&L, Balance Sheet, Class Report', ''],
            ['2026-06', 'Harbor Design LLC', 'Delivered', '[OWNER]', 'Yes', 'Yes', 'N/A', 'N/A',
             'Yes', 'Yes', 'Yes', 'Yes', '2026-07-15', '2026-07-13', 'P&L, Balance Sheet', 'Delivered early — clean month'],
        ]
    )

    # Document-Requests.csv — expanded
    write_csv('Document-Requests.csv',
        ['Document', 'Client', 'Period', 'Category', 'Status', 'Requested Date',
         'Due Date', 'Received Date', 'Secure Link', 'Reminder Sent', 'Notes'],
        [
            ['July bank statement — operating account', 'Harbor Design LLC', '2026-07',
             'Banking', 'Requested', '2026-08-01', '2026-08-05', '', '[LINK]', 'No', ''],
            ['July Stripe merchant report', 'Harbor Design LLC', '2026-07',
             'Income', 'Received', '2026-08-01', '2026-08-05', '2026-08-03', '[LINK]', 'No', ''],
            ['July payroll summary', 'Oak & Pine Co.', '2026-07',
             'Payroll', 'Requested', '2026-08-01', '2026-08-04', '', '[LINK]', 'Yes', 'Second reminder sent 08-03'],
            ['[Document Name]', '[Client Name]', '[Period]', '[Category]', 'Requested',
             '', '', '', '[LINK]', 'No', ''],
        ]
    )

    # Invoices.csv — expanded
    write_csv('Invoices.csv',
        ['Invoice', 'Client', 'Issue Date', 'Due Date', 'Amount', 'VAT Amount', 'Total Amount',
         'Status', 'Paid Date', 'Payment Method', 'Service Period', 'Invoice Type', 'Notes'],
        [
            ['INV-001', 'Harbor Design LLC', '2026-07-01', '2026-07-08', 850, 0, 850,
             'Paid', '2026-07-05', 'Bank Transfer', '2026-07', 'Monthly', ''],
            ['INV-002', 'Oak & Pine Co.', '2026-07-01', '2026-07-08', 1200, 0, 1200,
             'Paid', '2026-07-03', 'Bank Transfer', '2026-07', 'Monthly', ''],
            ['INV-003', 'Harbor Design LLC', '2026-08-01', '2026-08-08', 850, 0, 850,
             'Sent', '', '', '2026-08', 'Monthly', ''],
            ['INV-004', '[Client Name]', '', '', 0, 0, 0,
             'Draft', '', '', '', 'Monthly', ''],
        ]
    )

    # Tasks.csv — expanded
    write_csv('Tasks.csv',
        ['Task', 'Client', 'Period', 'Owner', 'Status', 'Priority', 'Due Date',
         'Recurring', 'Category', 'Completed Date', 'Notes'],
        [
            ['Reconcile operating account', 'Harbor Design LLC', '2026-07', '[OWNER]',
             'In Progress', 'High', '2026-08-08', 'Monthly', 'Monthly Close', '', ''],
            ['Categorize uncategorized transactions', 'Harbor Design LLC', '2026-07', '[OWNER]',
             'Not Started', 'High', '2026-08-06', 'Monthly', 'Monthly Close', '', '3 transactions flagged'],
            ['Send question list to client', 'Harbor Design LLC', '2026-07', '[OWNER]',
             'Not Started', 'Medium', '2026-08-10', 'Monthly', 'Client Communication', '', ''],
            ['Request July payroll summary', 'Oak & Pine Co.', '2026-07', '[OWNER]',
             'Done', 'High', '2026-08-05', 'Monthly', 'Document Collection', '2026-08-01', ''],
            ['[Task Name]', '[Client Name]', '[Period]', '[OWNER]', 'Not Started',
             'Medium', '', 'Monthly', '[Category]', '', ''],
        ]
    )

    # Client-Portal.csv — expanded
    write_csv('Client-Portal.csv',
        ['Item', 'Client', 'Section', 'Status', 'Owner', 'Due Date', 'Link',
         'Client Visible', 'Item Type', 'Period', 'Notes'],
        [
            ['June 2026 P&L Report', 'Harbor Design LLC', 'Reports', 'Ready',
             '[OWNER]', '2026-07-13', '[LINK]', 'Yes', 'Report', '2026-06', 'Delivered early'],
            ['June 2026 Balance Sheet', 'Harbor Design LLC', 'Reports', 'Ready',
             '[OWNER]', '2026-07-13', '[LINK]', 'Yes', 'Report', '2026-06', ''],
            ['July bank statement request', 'Harbor Design LLC', 'Document Requests', 'Pending',
             '[OWNER]', '2026-08-05', '', 'Yes', 'Document Request', '2026-07', ''],
            ['July 2026 P&L Report', 'Harbor Design LLC', 'Reports', 'Not Ready',
             '[OWNER]', '2026-08-15', '', 'Yes', 'Report', '2026-07', ''],
            ['[Item Name]', '[Client Name]', '[Section]', 'Not Ready', '[OWNER]',
             '', '', 'Yes', '[Type]', '[Period]', ''],
        ]
    )


def build_zip():
    zip_name = '/home/user/oqul-phase55-production/bookkeeper-v2/Bookkeeper-Practice-Launch-System-v2.0.zip'
    root_folder = 'Bookkeeper-Practice-Launch-System-v2.0'

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(OUT):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                arcname = os.path.join(root_folder, os.path.relpath(file_path, OUT))
                zf.write(file_path, arcname)

    size = os.path.getsize(zip_name) / (1024 * 1024)
    print(f'\n  ✓ ZIP created: {os.path.basename(zip_name)} ({size:.1f} MB)')

    # List contents
    with zipfile.ZipFile(zip_name) as zf:
        files = sorted(zf.namelist())
        print(f'\n  Total files in ZIP: {len(files)}')
        for f in files:
            info = zf.getinfo(f)
            size_kb = info.file_size / 1024
            print(f'    {f}  ({size_kb:.0f} KB)')

    return zip_name


if __name__ == '__main__':
    print('Building CSV files...')
    build_csvs()

    print('\nBuilding final ZIP...')
    build_zip()

    print('\n✓ COMPLETE — Bookkeeper Practice Launch System v2.0 is ready.')
