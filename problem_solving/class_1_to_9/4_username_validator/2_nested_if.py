user_name = input("Enter username:");
if user_name.isalpha():
	if len(user_name) >= 5:
		print("Valid username");
	else:
		print("Invalid username");
else:
	print("Invalid username");