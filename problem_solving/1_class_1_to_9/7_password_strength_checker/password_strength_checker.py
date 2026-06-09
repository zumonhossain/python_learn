password = input("Enter password: ");

if not password.isalpha() and not password.isdigit() and len(password) >= 8:
	print("Strong Password");
else:
	print("Weak Password");