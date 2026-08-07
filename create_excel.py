from openpyxl import Workbook

# Create workbook
wb = Workbook()

# Select sheet
sheet = wb.active

# Add headers
sheet['A1'] = 'TC_ID'
sheet['B1'] = 'URL'
sheet['C1'] = 'Execute'

# Add test data
sheet.append([
    'TC001',
    'https://www.google.com',
    'Y'
])

sheet.append([
    'TC002',
    'https://www.facebook.com',
    'Y'
])

sheet.append([
    'TC003',
    'https://www.amazon.in',
    'Y'
])

# Save file
wb.save("TestCases.xlsx")

print("Excel file created successfully")