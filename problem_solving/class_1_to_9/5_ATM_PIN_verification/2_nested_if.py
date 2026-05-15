pin_number = int(input("Enter PIN number:"));
if pin_number > 0:
	if pin_number == 1234:
		print("Access Granted");
	else:
		print("Access Denied!");
else:
	print("Invalid PIN");