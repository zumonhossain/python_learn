amount = float(input("Enter amount: "))
if amount > 0:
    if amount > 5000:
        print("Free Delivery")
    else:
        print("Delivery Charge: 500 yen")
else:
    print("Invalid amount")