

is_member = input("You are a member (yes/no): ").lower();
total_amount = int(input("total amount: "));
total_discount_amount = 0;

if is_member == "yes":
    if total_amount >= 15000 and total_amount <= 20000:
        total_discount_amount = 500
    elif total_amount >= 20000 and total_amount <= 50000:
        total_discount_amount = total_amount * 3/100
    elif total_amount > 50000:
        total_discount_amount = total_amount * 6/100

subtotal_amount = total_amount - total_discount_amount;
print("Total Amount: ", subtotal_amount);