username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login Successful")

elif username != "admin" or password != "12345":

    if username != "admin":
        print("Invalid Username")

    else:
        print("Wrong Password")