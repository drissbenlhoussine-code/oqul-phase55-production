# How to Open CSV Files

Your Small Business Toolkit includes several `.csv` files. This guide explains what CSV files are and how to open them in the most popular spreadsheet applications — including free options. Follow the section that matches the software you have available.

---

## What is a CSV File?

**CSV** stands for **Comma Separated Values**. It is a simple, universal file format used to store structured data — like a table — in plain text. Each row in the file represents one record (such as a transaction or a client entry), and each value in that row is separated by a comma.

CSV files are widely used because they are compatible with virtually every spreadsheet application, including Microsoft Excel, Google Sheets, Apple Numbers, and LibreOffice Calc. Think of a CSV as a spreadsheet stripped down to its most basic form — no colors, no formulas, just clean, portable data.

When you open a CSV file in a spreadsheet application, the commas are used to separate the data into individual columns, giving you the familiar table view you're used to.

---

## Opening in Microsoft Excel

Microsoft Excel is one of the most common ways to open CSV files.

1. Locate your `.csv` file in File Explorer (Windows) or Finder (Mac).
2. **Right-click** on the file.
3. Select **Open With** from the context menu.
4. Choose **Microsoft Excel** from the list.
5. Excel will open the file and automatically separate the data into columns.

### If Columns Don't Separate Correctly (Text Import Wizard)

Occasionally, all of your data may appear in a single column instead of being spread across multiple columns. This happens when Excel doesn't automatically detect the comma separator. Here's how to fix it using the Text Import Wizard:

1. Open Excel and go to **File > Open**.
2. Browse to your CSV file and click **Open**.
3. The **Text Import Wizard** will launch. On Step 1, select **Delimited** and click **Next**.
4. On Step 2, check the box next to **Comma** as the delimiter and uncheck any others. Click **Next**.
5. On Step 3, you can set the data format for each column if needed. Click **Finish**.
6. Your data will now appear correctly in separate columns.

> **Save as Excel Format:** Once your file is open and looking correct, go to **File > Save As** and choose **Excel Workbook (.xlsx)** to save it in Excel's native format so you can add formulas and formatting.

---

## Opening in Google Sheets

Google Sheets is a free, browser-based option that works on any device with internet access.

1. Go to [sheets.google.com](https://sheets.google.com) and sign in with your Google account.
2. Click the **blank spreadsheet** icon to create a new spreadsheet (or use the menu at the top).
3. Go to **File > Import**.
4. Click the **Upload** tab and drag your CSV file into the upload area, or click **Browse** to locate it.
5. In the import settings dialog, set **Separator type** to **Comma**.
6. Choose whether to replace the current sheet or create a new one.
7. Click **Import Data**.

Your CSV data will now appear in Google Sheets, neatly organized in rows and columns.

---

## Opening in Apple Numbers (Mac)

Apple Numbers is the built-in spreadsheet app on Mac, iPad, and iPhone.

1. Locate your `.csv` file in Finder.
2. **Double-click** the file — if Numbers is your default app for CSV files, it will open automatically.
3. If it doesn't open in Numbers automatically, **right-click** the file, select **Open With**, and choose **Numbers**.
4. Numbers will import the CSV and display the data in a table.
5. You can now format, edit, and save the file in Numbers format (`.numbers`) for future use.

---

## Opening in LibreOffice Calc (Free)

LibreOffice Calc is a free, open-source alternative to Microsoft Excel. It handles CSV files extremely well.

1. Download and install LibreOffice from [libreoffice.org](https://www.libreoffice.org) if you haven't already (it's completely free).
2. Locate your CSV file and **right-click** on it.
3. Select **Open With > LibreOffice Calc**.
4. An **Import Wizard** will appear. Make sure **Comma** is checked as the separator.
5. A preview will show how your data will be arranged. When it looks correct, click **OK**.
6. Your data will open in Calc, properly separated into columns.

---

## Troubleshooting Common Issues

### All Data Appearing in One Column

This is one of the most common issues and is easy to fix using the **Text to Columns** feature in Excel:

1. Click on the column header (Column A) to select the entire column.
2. Go to the **Data** tab in the ribbon.
3. Click **Text to Columns**.
4. Choose **Delimited** and click **Next**.
5. Check **Comma** as the delimiter and click **Finish**.

Your data will now be separated across multiple columns correctly.

---

### Special Characters Showing Incorrectly

If you see strange symbols like `â€™` instead of apostrophes or `Ã©` instead of accented letters, there is an encoding mismatch. Your file uses **UTF-8 encoding** and your software needs to be told this.

**In Excel:**
1. Use **File > Open** (not double-click).
2. Change the file type filter to **All Files**.
3. Select your CSV and click **Open**.
4. In the Text Import Wizard, look for **File Origin** and set it to **65001: Unicode (UTF-8)**.
5. Complete the wizard and the characters will display correctly.

**In Google Sheets:** UTF-8 is handled automatically — just re-import the file using the steps above.

---

### File Opens in Notepad Instead of Excel

1. **Right-click** on the CSV file.
2. Select **Open With > Choose Another App**.
3. Select **Microsoft Excel** from the list.
4. Check the box that says **Always use this app to open .csv files** if you want Excel to be the default going forward.
5. Click **OK**.

---

### Numbers Showing as Dates

Excel sometimes auto-formats entries like "1-5" or "3/4" as dates. To fix this:

1. Select the affected column(s).
2. Right-click and choose **Format Cells**.
3. Under the **Number** tab, select **Text** or the appropriate number format.
4. Re-enter or re-paste the values — the formatting applies to new entries.

To prevent this on import, use the Text Import Wizard and set those columns to **Text** format during Step 3.

---

### Formulas Not Calculating

If formula cells are showing the formula text instead of a result:

1. Go to **File > Options > Formulas** (Excel) or **Tools > Options > LibreOffice Calc > Formula** (LibreOffice).
2. Make sure **Automatic** calculation is selected.
3. Alternatively, press **Ctrl + Alt + F9** (Excel) to force a full recalculation.

In Google Sheets, formulas calculate automatically — if a formula shows as text, check that the cell is not formatted as **Plain text**. Select the cell, go to **Format > Number > Automatic**, then re-enter the formula.

---

If you're still having trouble after working through these steps, don't hesitate to reach out to us through Etsy Messages. We're here to help!
