vending_machine = {
    "cola": 150,
    "water": 120,
    "coffee": 130
}

item = input("Enter item name: ");

if item in vending_machine:
    print(f"Price: {vending_machine[item]} yen");
else:
    print("Item not available");