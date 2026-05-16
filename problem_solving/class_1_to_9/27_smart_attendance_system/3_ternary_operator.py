attendance = float(input("Enter attendance: "))
assignment = input("Assignment submitted? (yes/no): ").lower()

print(
    "Eligible for final exam"
    if attendance >= 75 and assignment == "yes"
    else "Not eligible (low attendance)"
    if attendance < 75
    else "Not eligible (missing assignment)"
)