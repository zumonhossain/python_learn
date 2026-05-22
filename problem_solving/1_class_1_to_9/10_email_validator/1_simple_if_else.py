email = input("Enter Your Email:")

if email.count("@") == 1 and email.endswith(".com"):
    print("Valid Email")
else:
    print("Invalid Email")