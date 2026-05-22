username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")

if username == "admin":
    if password == "12345":
        if otp == "9999":
            print("Login Approved")
        else:
            print("Invalid OTP")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")