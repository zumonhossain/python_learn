username = input("Enter username: ");
password = input("Enter password: ");

if username == "admin" and password == "12345":
    print("Login Successful");
elif username != "admin":
    print("Invalid Username");
else:
    print("Wrong Password");