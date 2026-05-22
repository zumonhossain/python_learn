email = input("Enter email: ")

if "@" in email and email.endswith(".com"):
    print("Valid Email")

elif "@" not in email or not email.endswith(".com"):
    print("Invalid Email")