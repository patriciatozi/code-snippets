from pyxlsb import open_workbook

# Open the binary file
with open_workbook('sample.xlsb') as wb:
    
    # Choose the sheet
    sheet = wb.get_sheet('Pessoal')
    
    # Print each row with the following output format: 
    # Cell(r=<row>, c=<column>, v=<value)
    for row in sheet.rows():
        print(row)