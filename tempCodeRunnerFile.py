prices = [];
i = 0;
while i < 5:
    price = float(input(f"Enter price of item {i + 1}: "));
    prices.append(price);
    i +=1;   

i = 0
total = 0

while i < len(prices):
    print(f"Item {i + 1}: RM {prices[i]}")
    total += prices[i]
    i += 1

print(f"Total Bill: RM {total}");
