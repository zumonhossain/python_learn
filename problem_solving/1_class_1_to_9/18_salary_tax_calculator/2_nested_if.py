salary = float(input("Enter salary: "))

if salary > 0:

    if salary > 1000000:
        tax = salary * 0.30
        print("Tax:", tax)

    elif salary > 500000:
        tax = salary * 0.10
        print("Tax:", tax)

    else:
        print("Tax: 0")

else:
    print("Invalid salary")