records = [
    ["aiko yamamoto", 28, 2000],
    ["kenji mori", 18, 1500],
    ["hana sato", 22, 1800],
    ["riku tanaka", 26, 2500]
]

print("=====================================================")
print("MONTHLY PAYROLL REPORT")
print("=====================================================")

print("Name | Days | Daily Wage | Salary | Status")
print("-------------------------------------------------")

i = 0
total_payroll = 0

while i < len(records):
    name = records[i][0].title()
    days_present = records[i][1]
    daily_wage = records[i][2]
    salary = days_present * daily_wage

    if days_present < 20:
        salary = salary - (salary * 0.10)
        status = "Deducted"
    elif days_present >= 26:
        salary = salary + (salary * 0.05)
        status = "Bonus"
    else:
        status = "Standard"

    total_payroll += salary

    print(name, "|", days_present, "|", daily_wage, "|", int(salary), "|", status)
    i += 1

print("-" * 49)
print("Total Payroll:", int(total_payroll))