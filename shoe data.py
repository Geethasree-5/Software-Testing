from faker import Faker
from openpyxl import Workbook

fake = Faker()

wb = Workbook()

ws = wb.active

ws.title="Products"

ws.append(["Category","Maximum Price"])

for i in range(5):

    ws.append([
        fake.random_element(["Electronics","Fashion"]),
        fake.random_int(min=2000,max=60000)
    ])

wb.save("products.xlsx")

print("Excel Created Successfully")