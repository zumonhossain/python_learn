attendance = float(input("Enter attendance: "));
assignment = input("Assignment submitted? (yes/no): ").lower();

if attendance >= 75 and assignment == "yes":
    print("Eligible for final exam");
elif attendance < 75:
    print("Not eligible (low attendance)");
else:
    print("Not eligible (missing assignment)");