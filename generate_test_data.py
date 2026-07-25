from faker import Faker
from openpyxl import Workbook

fake = Faker()

wb = Workbook()
ws = wb.active
ws.title = "LoginData"

ws.append(["Email","Password"])

# Generate 5 invalid email/password combinations
for i in range(5):
    ws.append([
        fake.email(),
        fake.password(length=8)
    ])

# Add one valid login
ws.append([
    "admin@gmail.com",
    "admin123"
])

wb.save("testdata.xlsx")

print("Test data created successfully.")