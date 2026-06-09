username = input("Enter username: ");
password = input("Enter password: ");
otp = input("Enter OTP: ");

if username == "admin" and password == "12345" and otp == "9999":
	print("Login Approved");
elif username != "admin":
	print("Invalid Username");
elif password != "12345":
	print("Wrong Password");
else: 
	print("Invalid OTP");