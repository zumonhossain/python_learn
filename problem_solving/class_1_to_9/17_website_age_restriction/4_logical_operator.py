age = int(input("Enter age: "))

if age >= 13 and age <= 100:
    print("Account creation allowed")

elif age < 13 or age > 100:
    print("Account creation denied")