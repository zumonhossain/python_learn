inventory = []

while True:
    name = input("Enter product name (or 'done'): ")

    if name.lower() == 'done':
        break

    category = input("Enter category: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    name = name.title()
    category = category.upper()

    inventory.append([name, category, qty, price])

print("=============================================================")
print("WAREHOUSE INVENTORY REPORT")
print("=============================================================")
print("Product | Category | Qty | Unit Price | Total Value | Stock")
print("-------------------------------------------------------------")

i = 0
highest_value = 0
highest_product = ""

while i < len(inventory):
    name = inventory[i][0]
    category = inventory[i][1]
    qty = inventory[i][2]
    price = inventory[i][3]

    total_value = qty * price

    if qty >= 100:
        stock = "High"
    elif qty >= 50:
        stock = "Medium"
    else:
        stock = "Low"

    print(f"{name} | {category} | {qty} | {price} | {total_value} | {stock}")

    if total_value > highest_value:
        highest_value = total_value
        highest_product = name

    i += 1

print("-------------------------------------------------------------")
print(f"Highest value product: {highest_product} ({highest_value} yen)")