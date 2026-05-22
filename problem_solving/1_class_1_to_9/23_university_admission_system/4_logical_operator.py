gpa = float(input("Enter GPA: "))
ielts = float(input("Enter IELTS: "))

has_gpa = gpa >= 3.5
has_ielts = ielts >= 6.5

if has_gpa and has_ielts:
    print("Eligible for admission")
elif not has_gpa:
    print("GPA requirement not met")
else:
    print("IELTS requirement not met")