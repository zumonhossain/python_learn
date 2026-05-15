user_name = input("Enter username");
result = "Valid username" if user_name.isalpha() and len(user_name) >= 5 else "Invalid username";
print(result);