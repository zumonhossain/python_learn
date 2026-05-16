email = input("Enter email: ")

if email.find("@") != -1 and email.find(".com") != -1:
    print("Valid Email")
else:
    print("Invalid Email")