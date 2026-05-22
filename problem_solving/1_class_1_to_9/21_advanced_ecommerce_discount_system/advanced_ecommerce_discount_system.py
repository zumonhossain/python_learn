membership = input("Are you a member? (yes or no): ").lower();
total_amount = float(input("Enter amount: "));
discount_amount = 0;

if membership == "yes":
    if total_amount >= 20000:
        discount_amount = 0.03;
    elif total_amount >= 10000:
        discount_amount = 0.02;
    else:
        discount_amount = 0.01;
else:
    discount_amount = 0;

final_bill = total_amount - (total_amount * discount_amount);

print("Final bill:", final_bill);