email = input("Enter email: ")

result = "Valid Email" if "@" in email and email.endswith(".com") else "Invalid Email"

print(result)