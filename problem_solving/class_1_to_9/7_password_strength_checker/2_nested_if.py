password = input("Enter password: ")
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")