username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")

is_user = username == "admin"
is_pass = password == "12345"
is_otp = otp == "9999"

if is_user and is_pass and is_otp:
    print("Login Approved")
elif not is_user:
    print("Invalid Username")
elif not is_pass:
    print("Wrong Password")
else:
    print("Invalid OTP")