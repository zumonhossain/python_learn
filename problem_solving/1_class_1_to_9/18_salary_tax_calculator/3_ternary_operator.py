salary = float(input("Enter salary: "))

result = (
    salary * 0.30 if salary > 1000000 else
    salary * 0.10 if salary > 500000 else
    0
)

print("Tax:", result)