# How to Customize Your Templates

Your Small Business Toolkit is designed to be fully customizable so it works exactly the way your business works. This guide walks you through everything from adding your logo to adjusting formulas — no technical experience required. Take it step by step, and remember: always keep a backup of the original files before you start editing.

---

## Adding Your Business Information

The quickest way to make these templates feel like yours is to add your business details wherever placeholder text appears.

### What to Update

- **Business name** — Replace any instance of `[Your Business Name]` with your actual business name.
- **Contact details** — Update email address, phone number, and website URL in headers or footers.
- **Logo** — In Google Sheets or Excel, go to **Insert > Image** to place your logo in the header area of any sheet.
- **Address** — Replace placeholder address lines with your business address (important for the invoice template).

### In CSV/Spreadsheet Files

CSV files don't contain styles or images on their own, but once you've opened them in Google Sheets or Excel, you can add a header row above the data and insert your business name, logo, and contact info there. This is especially useful for the tracker and planner files.

### Consistency Across All Files

For a professional look, use the same business name spelling, the same logo version, and the same color scheme across all of your templates. Setting this up once and saving the styled versions means you'll always start from a polished, branded starting point.

---

## Changing Colors and Fonts (Google Sheets)

### Change Cell Background Color

1. Select the cell(s) or row(s) you want to color.
2. Click the **Fill color** button in the toolbar (it looks like a paint bucket).
3. Choose a color from the palette, or click **Custom** to enter a specific hex code (e.g., `#2C3E50` for a dark navy).

### Change Text Color and Font

1. Select the text or cells you want to style.
2. Click the **Text color** button (the letter **A** with a color bar under it) to change the font color.
3. Click the **Font** dropdown in the toolbar to choose a different font.
4. Use the **Bold (Ctrl+B)**, **Italic (Ctrl+I)**, and **Underline (Ctrl+U)** buttons to style text as needed.

### Apply a Consistent Color Scheme

Choose two or three colors that match your brand and use them consistently:
- **Primary color** for header rows and section titles
- **Accent color** for highlights or alternating rows
- **Neutral** (white or light gray) for data cells

### Apply a Theme in Google Sheets

1. Go to **Format > Theme**.
2. A sidebar will open with pre-designed color themes.
3. Click any theme to preview it, then click **Apply** to apply it to your entire spreadsheet.
4. You can customize further by clicking **Customize** and adjusting individual colors.

---

## Changing Colors and Fonts (Microsoft Excel)

### Change Cell Background Color

1. Select the cell(s) you want to color.
2. Click the **Fill Color** dropdown arrow in the **Home** tab (it looks like a paint bucket).
3. Choose a color from the palette, or click **More Colors** to enter a specific value.

### Change Text Color and Font

1. Select the text or cells to style.
2. Click the **Font Color** dropdown arrow (the letter **A** with a color bar) in the **Home** tab.
3. Use the **Font** box in the Home tab ribbon to select a different typeface.
4. Use **Bold**, **Italic**, and **Underline** buttons as needed.

### Apply a Theme in Excel

1. Click the **Page Layout** tab in the ribbon.
2. Click **Themes** to open the theme gallery.
3. Hover over any theme to preview it, then click to apply.
4. Use the **Colors** and **Fonts** dropdowns next to the Themes button to mix and match if needed.

---

## Adding and Removing Columns

### When to Add Columns

You might want to add columns to track additional information specific to your business — for example, a "Referral Source" column in a client tracker, or a "Category" column in an expense tracker.

### How to Insert a Column Without Breaking Data

1. **Right-click** on the column header (the letter at the top) where you want the new column to appear.
2. Select **Insert 1 column left** (or right).
3. A blank column will be inserted, and existing data will shift over automatically.
4. Add your column header in the first row.

> **Important:** If any formulas reference column positions (e.g., `=SUM(D2:D100)`), inserting columns before those columns will update the references automatically in most cases — but always double-check your formulas after making changes.

### How to Delete a Column

1. Click the column header to select the entire column.
2. Right-click and select **Delete column**.
3. Confirm if prompted.

### Adjust Column Widths

- **Auto-fit:** Double-click the right edge of a column header to auto-fit to the widest content.
- **Manual:** Click and drag the right edge of the column header to set a custom width.

---

## Duplicating Tabs / Sheets

Duplicating a tab is a great workflow trick — for example, creating one tab per month in a budget tracker, or one tab per client in a project planner.

### When to Use Duplicate Tabs

- **Monthly trackers:** Duplicate the January tab for February, March, etc.
- **Client projects:** One tab per client keeps data organized without needing separate files.
- **Before/After:** Keep an "Original" tab and work in a duplicate so you always have a clean reference.

### How to Duplicate a Tab in Google Sheets

1. Right-click the tab name at the bottom of the spreadsheet.
2. Select **Duplicate**.
3. A copy of the tab will appear next to the original.
4. Double-click the new tab name to rename it (e.g., "February" or "Client - ABC Co.").

### How to Duplicate a Tab in Microsoft Excel

1. Right-click the sheet tab at the bottom.
2. Select **Move or Copy**.
3. In the dialog, choose where to place the copy and check the **Create a copy** box.
4. Click **OK**.
5. Rename the new tab by double-clicking on its name.

---

## Adjusting Formulas

### Understanding Existing Formulas

Many of the spreadsheet files in your toolkit include pre-built formulas. Formula cells typically appear in totals rows, summary sections, or highlighted cells. You can click on any cell to see its formula in the formula bar at the top of the screen.

Common formulas you'll encounter:
- `=SUM(B2:B30)` — adds up a column of numbers
- `=B2*C2` — multiplies two values (e.g., quantity × price)
- `=IF(D2>0,"Profit","Loss")` — conditional logic

### Extending Formulas to New Rows

When you add new rows of data, formulas in total/summary rows may not automatically include them. To extend a formula:

1. Click the cell with the existing formula.
2. Look at the range in the formula bar (e.g., `B2:B30`).
3. Update the range to include your new rows (e.g., change to `B2:B50`).
4. Press **Enter** to confirm.

Alternatively, select the formula cell and drag the small blue square (fill handle) in the bottom-right corner down to extend the formula to adjacent cells.

### Modifying Calculations

To change what a formula calculates, click the cell containing the formula, edit the formula in the formula bar, and press Enter. For example, to change a tax rate in a calculation, find the cell containing the rate and update the number.

> **Warning:** Be careful when editing formula cells. If you accidentally delete a formula and type a number instead, you'll lose the automatic calculation. Press **Ctrl+Z** immediately to undo if you make a mistake.

---

## Tips for Maintaining Data Integrity

Following these simple habits will protect your data and keep your records reliable:

- **Always save a backup of the original template** before making any edits. Store it in an "Originals" folder and never edit that copy.
- **Use consistent date formats** throughout each file (e.g., always MM/DD/YYYY or DD/MM/YYYY — never mix them).
- **Validate data before reporting** — spot-check totals and cross-reference key figures before sharing reports.
- **Lock formula cells** to prevent accidental edits:
  - In Google Sheets: Right-click the cell > **Protect range**, then restrict editing to yourself.
  - In Excel: Select formula cells > **Format Cells > Protection > Locked**, then go to **Review > Protect Sheet**.

---

## Customizing the Invoice Template (HTML)

Your toolkit includes an HTML invoice template that you can open in any web browser and print or save as a PDF.

### How to Open the HTML File

1. Locate the `.html` file in your extracted toolkit folder.
2. **Double-click** it — it will open in your default web browser (Chrome, Firefox, Safari, etc.).
3. You'll see a professionally formatted invoice ready to fill in.

### Where to Find Text to Change

The HTML file contains clearly labeled placeholder text in brackets like `[Your Business Name]`, `[Client Name]`, `[Invoice Number]`, etc. To edit these:

1. Right-click the HTML file and select **Open With > Notepad** (Windows) or **TextEdit** (Mac).
2. Use **Ctrl+F** (Find) to search for the bracketed placeholders.
3. Replace each placeholder with your actual information.
4. Save the file, then reopen it in your browser to see the updated invoice.

### How to Change Colors in the HTML/CSS

Inside the HTML file, look for lines that start with color values like `color:` or `background-color:`. Replace the existing color codes with your brand colors (use a hex color picker at [htmlcolorcodes.com](https://htmlcolorcodes.com) if needed).

### How to Save as PDF

Once your invoice is filled in and looking perfect:

1. With the invoice open in your browser, press **Ctrl+P** (Windows) or **Cmd+P** (Mac) to open the Print dialog.
2. In the **Destination** or **Printer** dropdown, select **Save as PDF**.
3. Click **Save** and choose where to save the PDF on your computer.

You now have a professional PDF invoice ready to send to clients.

---

Customizing your templates is one of the best ways to get more value from your toolkit. Take your time, experiment, and remember — you can always go back to the original files if you need a fresh start. Happy customizing!
