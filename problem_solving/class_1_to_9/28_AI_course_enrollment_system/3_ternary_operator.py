skill = input("Enter skill level (beginner/intermediate/advanced): ").lower()
age = int(input("Enter age: "))

print(
    "Enrollment Approved"
    if (skill == "beginner" and age >= 18)
    or (skill == "intermediate" and age >= 16)
    or (skill == "advanced" and age >= 14)
    else "Invalid Input"
    if skill not in ["beginner", "intermediate", "advanced"]
    else "Enrollment Denied"
)