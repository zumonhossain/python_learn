def supermarket_bill(customer_name, *items, discount=0, **extras):
    print(f"Customer : {customer_name}");
    print("----- Items ----")
    
    subtotal = 0;
    
    # Items list
    for name, price in items:
        print(f"{name} ¥{price}");
        subtotal += price;
    
    print(f"Subtotal : ¥{subtotal}");
    
    discount_amount = subtotal * discount / 100;
    print(f"Discount ({discount}%): -¥{int(discount_amount)}");
    
    loyalty = extras.get("loyalty_points", 0);
    print(f"Loyalty pts {loyalty}: -¥{loyalty}");
    
    gift = 50 if extras.get("gift_wrap") else 0;
    if gift:
        print(f"Gift wrap : +¥{gift}");
    
    print("--------------------");
    
    total = subtotal - discount_amount - loyalty + gift;
    return int(total);

total = supermarket_bill(
    "Meena",
    ("Milk 1L", 65),
    ("Bread", 45),
    ("Eggs 12pk", 90),
    discount=10,
    loyalty_points=20,
    gift_wrap=True
);
print(f"You pay: ¥{total}");