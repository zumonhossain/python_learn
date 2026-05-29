product_names = []
product_prices = []

while True:
    name = input("Enter product (or 'done' to finish): ")
    if name.lower() == "done":
        break
    price = float(input("Enter price: "))
    product_names.append(name)
    product_prices.append(price)

print("--- Your Receipt ---")

i = 0

while i < len(product_names):
    print(product_names[i], ":", product_prices[i])
    i += 1
total_items = len(product_names)
total_bill = sum(product_prices)
print("Total items:", total_items)
print("Total bill:", total_bill)