salary = float(input("Enter salary: "))
experience = float(input("Enter experience: "))

has_salary = salary >= 300000
has_exp = experience >= 2

if has_salary and has_exp:
    print("Loan Approved")
elif not has_salary:
    print("Salary requirement not met")
else:
    print("Experience requirement not met")