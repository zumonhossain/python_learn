age = int(input("Enter age: "))

if age > 0:

    if age >= 13:
        print("Account creation allowed")

    else:
        print("Account creation denied")

else:
    print("Invalid age")