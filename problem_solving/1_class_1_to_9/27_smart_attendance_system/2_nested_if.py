attendance = float(input("Enter attendance: "))
assignment = input("Assignment submitted? (yes/no): ").lower()

if attendance >= 75:
    if assignment == "yes":
        print("Eligible for final exam")
    else:
        print("Not eligible (missing assignment)")
else:
    print("Not eligible (low attendance)")