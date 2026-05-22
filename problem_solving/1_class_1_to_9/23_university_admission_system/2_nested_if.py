gpa = float(input("Enter GPA: "))
ielts = float(input("Enter IELTS: "))

if gpa >= 3.5:
    if ielts >= 6.5:
        print("Eligible for admission")
    else:
        print("IELTS requirement not met")
else:
    print("GPA requirement not met")