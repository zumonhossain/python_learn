marks = int(input("Enter marks: "))

if not (marks >= 0 and marks <= 100):
    print("Invalid marks!")
elif not marks < 80 and marks <= 100:
    print("Grade: A+")
elif not marks < 70 and marks < 80:
    print("Grade: A")
elif not marks < 60 and marks < 70:
    print("Grade: B")
elif not marks < 50 and marks < 60:
    print("Grade: C")
else:
    print("Grade: F")