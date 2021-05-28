#! python3
# new_CSV_from_each_excel_sheet.py - Removes the header from all CSV files in the current
# working directory.
# TODO https://www.nasdaq.com/market-activity/stocks/goog/historical pull data to check stocks i want to use
# TODO backtesting module from youtube stocks course.


import csv, os


for excelFile in os.listdir('..'):
    # Skip non-xlsx files, load the workbook object.
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
    sheet = wb.get_sheet_by_name(sheetName)

    # Create the CSV filename from the Excel filename and sheet title.
    # Create teh csv.writer object for this CSV file.

    # Loop through ever row in the sheet.
    for rowNum in range(1, sheet.get_highest_row() +1):
        rowData = []  # append each cell to this list
        # Loop through each cell in the row.
        for colNum in range(1, sheet.get_highest_column() +1):
            # Append each cell to this list

    csvFile.close()