import json

print("========================================")
print("API RESPONSE VALIDATION WITH UI")
print("========================================")

# -----------------------------
# Simulated API Response
# -----------------------------
api_response = '''
[
    {
        "id": 101,
        "name": "Anita"
    },
    {
        "id": 102,
        "name": "Rahul"
    },
    {
        "id": 103,
        "name": "Deepa"
    },
    {
        "id": 104,
        "name": "Kiran"
    },
    {
        "id": 105,
        "name": "Bhavya"
    }
]
'''

# Parse JSON
api_data = json.loads(api_response)

# Extract API names
api_names = []

for student in api_data:
    api_names.append(student["name"])

# -----------------------------
# Simulated UI Data
# -----------------------------
ui_names = [
    "Anita",
    "Rahul",
    "Deepa",
    "Kiran",
    "Bhavya"
]

# Display data
print("\nStudent Names from UI")
print("----------------------")
for name in ui_names:
    print(name)

print("\nStudent Names from API")
print("-----------------------")
for name in api_names:
    print(name)

# -----------------------------
# Validation
# -----------------------------
print("\nValidating records...")

assert len(ui_names) == len(api_names), "Record count mismatch!"

assert sorted(ui_names) == sorted(api_names), "Student names do not match!"

print("\nNumber of UI Records :", len(ui_names))
print("Number of API Records:", len(api_names))

print("\nNo Missing Records")
print("No Extra Records")
print("All Student Records Match")

print("\n========================================")
print("TEST CASE PASSED")
print("========================================")