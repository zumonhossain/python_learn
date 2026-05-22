salary = float(input("Enter salary: "))
experience = float(input("Enter experience: "))

print(
    "Loan Approved"
    if salary >= 300000 and experience >= 2
    else "Salary requirement not met"
    if salary < 300000
    else "Experience requirement not met"
)