import xlrd

# Load the workbook
workbook = xlrd.open_workbook('sample.xls') 

# Choose the sheet by its index number
worksheet = workbook.sheet_by_index(0) 

# Show each row from that sheet
for i in range(worksheet.nrows): 
    print(worksheet.row(i))