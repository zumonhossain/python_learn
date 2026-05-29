patients = []
priority_count = 0
normal_count = 0
standard_count = 0

while True:
    name = input("Enter patient name (or 'done'): ")

    if name.lower() == "done":
        break

    age = int(input("Enter age: "))
    severity = int(input("Enter severity (1-10): "))

    name = name.title()
    patient = [name, age, severity]
    patients.append(patient)

print("--- Patient Report ---")

i = 0

while i < len(patients):
    name = patients[i][0]
    age = patients[i][1]
    severity = patients[i][2]

    if age >= 60 or severity >= 7:
        status = "Priority Treatment"
        priority_count += 1
    elif age >= 18 and severity >= 4:
        status = "Normal Treatment"
        normal_count += 1
    else:
        status = "Standard Queue"
        standard_count += 1

    print(name,
          "| Age:", age,
          "| Severity:", severity,
          "->", status)
    
    i += 1

print("Priority Treatment :", priority_count)
print("Normal Treatment :", normal_count)
print("Standard Queue :", standard_count)