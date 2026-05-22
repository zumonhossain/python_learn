membership = input("Are you a member? (yes/no): ").lower()
amount = float(input("Enter amount: "))

discount = (
    0.03 if membership == "yes" and amount >= 20000 else
    0.02 if membership == "yes" and amount >= 10000 else
    0.01 if membership == "yes" else
    0
)

print("Final bill:", amount - (amount * discount))