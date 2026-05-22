membership = input("Are you a member? (yes/no): ").lower()
amount = float(input("Enter amount: "))

is_member = membership == "yes"

if is_member and amount >= 20000:
    discount = 0.03
elif is_member and amount >= 10000:
    discount = 0.02
elif is_member and amount < 10000 and is_member:
    discount = 0.01
else:
    discount = 0

print("Final bill:", amount - (amount * discount))