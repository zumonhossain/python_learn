gpa = float(input("Enter GPA: "))
ielts = float(input("Enter IELTS: "))

print(
    "Eligible for admission"
    if gpa >= 3.5 and ielts >= 6.5
    else "GPA requirement not met"
    if gpa < 3.5
    else "IELTS requirement not met"
)