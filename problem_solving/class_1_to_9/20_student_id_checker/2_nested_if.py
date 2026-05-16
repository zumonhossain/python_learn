student_id = input("Enter student ID: ")

if student_id:
    if student_id.startswith("260"):
        print("Valid Student")
    else:
        print("Invalid Student")
else:
    print("No ID entered")