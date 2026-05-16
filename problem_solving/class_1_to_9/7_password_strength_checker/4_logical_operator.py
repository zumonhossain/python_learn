password = input("Enter password: ")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Strong Password")
elif len(password) < 8 or not any(char.isdigit() for char in password):
    print("Weak Password")