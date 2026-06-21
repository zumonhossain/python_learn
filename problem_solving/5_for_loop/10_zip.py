products = ["mango", "apple", "banana"];
prices = [100, 200, 300];

for product, price in zip(products, prices):
    print(f"{product}: {price}");