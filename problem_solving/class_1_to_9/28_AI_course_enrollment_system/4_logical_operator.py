skill = input("Enter skill level (beginner/intermediate/advanced): ").lower()
age = int(input("Enter age: "))

is_valid_skill = skill in ["beginner", "intermediate", "advanced"]

if skill == "beginner" and age >= 18:
    print("Enrollment Approved")
elif skill == "intermediate" and age >= 16:
    print("Enrollment Approved")
elif skill == "advanced" and age >= 14:
    print("Enrollment Approved")
elif is_valid_skill:
    print("Enrollment Denied")
else:
    print("Invalid Input")