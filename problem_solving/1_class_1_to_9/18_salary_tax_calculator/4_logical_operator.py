salary = float(input("Enter salary: "))

if salary > 1000000 and salary > 0:
    tax = salary * 0.30
    print("Tax:", tax)

elif salary > 500000 and salary <= 1000000:
    tax = salary * 0.10
    print("Tax:", tax)

elif salary <= 500000 or salary == 0:
    print("Tax: 0")

else:
    print("Invalid salary")