amount = float(input("Enter recharge amount: "))
if amount > 1000 and amount > 0:
    print("Bonus Added: 100 yen")
elif amount <= 1000 or amount <= 0:
    print("No Bonus")