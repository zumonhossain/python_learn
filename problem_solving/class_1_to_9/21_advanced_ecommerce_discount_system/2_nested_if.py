membership = input("Are you a member? (yes/no): ").lower()
amount = float(input("Enter amount: "))

if membership == "yes":
    if amount >= 20000:
        discount = 0.03
    else:
        if amount >= 10000:
            discount = 0.02
        else:
            discount = 0.01
else:
    discount = 0

print("Final bill:", amount - (amount * discount))