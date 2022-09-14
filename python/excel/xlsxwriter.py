import xlsxwriter

# Create the workbook with the filename
workbook = xlsxwriter.Workbook('hello.xlsx')

# Name the current sheet
worksheet = workbook.add_worksheet('Page 1')

# Include rows by their position
worksheet.write('A1', 'Hello world')

# Close the book after making all changes
workbook.close()