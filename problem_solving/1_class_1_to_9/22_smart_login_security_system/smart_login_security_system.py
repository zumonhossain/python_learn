user_name = input("Enter username: ");
password = input("Enter password: ");
otp = input("Enter OTP: ");

if user_name != "admin":
    print("Invalid Username");
elif password != "12345":
    print("Wrong Password");
elif otp != "9999":
    print("Invalid OTP");
else:
    print("Login Approved");