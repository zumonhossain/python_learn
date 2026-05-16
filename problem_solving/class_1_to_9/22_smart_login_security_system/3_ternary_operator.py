username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")

print(
    "Login Approved" if username == "admin" and password == "12345" and otp == "9999"
    else "Invalid Username" if username != "admin"
    else "Wrong Password" if password != "12345"
    else "Invalid OTP"
)