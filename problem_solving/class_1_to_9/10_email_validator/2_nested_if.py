email = input("Enter email: ")

if "@" in email:

    if email.endswith(".com"):
        print("Valid Email")

    else:
        print("Invalid Email")

else:
    print("Invalid Email")