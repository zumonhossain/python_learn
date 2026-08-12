age = int(input("Enter your age: "));

if age < 12:
    print("Child");
elif age <= 22:
    print("Student");
elif age <= 64:
    print("Adult")
else:
    print("Senior");