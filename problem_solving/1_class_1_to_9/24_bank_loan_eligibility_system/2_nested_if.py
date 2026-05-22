salary = float(input("Enter salary: "))
experience = float(input("Enter experience: "))

if salary >= 300000:
    if experience >= 2:
        print("Loan Approved")
    else:
        print("Experience requirement not met")
else:
    print("Salary requirement not met")