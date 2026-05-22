vehicle = input("Enter vehicle type: ").lower()
hours = int(input("Enter parking hours: "))

if vehicle == "bike":
    fee = 100 * hours
    print("Total fee:", fee, "yen")
else:
    if vehicle == "car":
        fee = 300 * hours
        print("Total fee:", fee, "yen")
    else:
        if vehicle == "truck":
            fee = 500 * hours
            print("Total fee:", fee, "yen")
        else:
            print("Invalid vehicle type")