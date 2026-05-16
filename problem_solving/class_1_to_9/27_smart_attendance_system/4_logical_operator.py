attendance = float(input("Enter attendance: "))
assignment = input("Assignment submitted? (yes/no): ").lower()

has_attendance = attendance >= 75
has_assignment = assignment == "yes"

if has_attendance and has_assignment:
    print("Eligible for final exam")
elif not has_attendance:
    print("Not eligible (low attendance)")
else:
    print("Not eligible (missing assignment)")