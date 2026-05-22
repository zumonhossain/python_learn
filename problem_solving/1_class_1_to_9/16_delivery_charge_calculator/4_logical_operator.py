amount = float(input("Enter amount: "))
if amount > 5000 and amount > 0:
    print("Free Delivery")
elif amount <= 5000 or amount <= 0:
    print("Delivery Charge: 500 yen")
