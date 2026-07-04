def gym_attendance(*members):
    print("Today's Attendance:", len(members));
    print("Members:", ", ".join(members));

    if len(members) >= 10:
        print("Status: Full");
    else:
        print("Status: Available");

    print("--------------------------");

gym_attendance("Riya", "Arjun", "Priya", "Karan");
gym_attendance("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K");