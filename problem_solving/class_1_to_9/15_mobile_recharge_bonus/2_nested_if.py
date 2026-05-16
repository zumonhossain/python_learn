amount = float(input("Enter recharge amount: "))
if amount > 0:
    if amount > 1000:
        print("Bonus Added: 100 yen")
    else:
        print("No Bonus")
else:
    print("Invalid amount")