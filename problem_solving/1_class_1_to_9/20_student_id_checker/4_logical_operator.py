student_id = input("Enter student ID: ")

is_valid = (student_id[:3] == "260") and True

if is_valid:
    print("Valid Student")
else:
    print("Invalid Student")