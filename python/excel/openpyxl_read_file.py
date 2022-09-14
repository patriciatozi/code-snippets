# 2. READ THE FILE

from openpyxl import load_workbook

# Load the file
wb = load_workbook(filename = 'sample.xlsx')

# Point the sheet to be worked on
sheet_pessoal = wb['Pessoal']