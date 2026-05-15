username = input("Enter username: ")

if username.isalpha() and len(username) >= 5:
    print("Valid username")

elif not username.isalpha() or len(username) < 5:
    print("Invalid username")