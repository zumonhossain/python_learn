password = input("Enter password: ")
result = "Strong Password" if len(password) >= 8 and any(char.isdigit() for char in password) else "Weak Password"
print(result)