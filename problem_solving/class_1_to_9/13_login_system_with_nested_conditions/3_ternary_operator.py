username = input("Enter username: ")
password = input("Enter password: ")

result = (
    "Login Successful"
    if username == "admin" and password == "12345"
    else "Invalid Username"
    if username != "admin"
    else "Wrong Password"
)

print(result)