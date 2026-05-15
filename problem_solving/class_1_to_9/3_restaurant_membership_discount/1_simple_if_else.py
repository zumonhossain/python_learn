

# member = input("Are you a member? yes or no:").lower();
# total_bill = float(input("Enter bill amount"));

# if member == "yes":
# 	discount_amount = (total_bill * 10) / 100;
# 	final_bill = total_bill - discount_amount;
	
# 	print("Total Discount:", discount_amount);
# 	print("Final Bill:", final_bill);

# else:
# 	print("Discount Amount: 0");
# 	print("Final bill:", total_bill);
    


member = input("Are you a member? yes or no: ").lower();
total_bill = float(input("Enter bill amount: "));

if member == "yes": # comparison operator
    final_bill = total_bill * 0.90
    print("Final bill:", final_bill)
else:
    print("Final bill:", total_bill)
    


