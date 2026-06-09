membership_status = input("Are you a member? yes/no: ").lower();
cart_amount = float(input("Enter amount: "));

if membership_status == "yes" and cart_amount >= 20000: 
	discount_amount = (cart_amount * 3) / 100;
	final_amount = cart_amount - discount_amount;
	print("Final bill", final_amount);
elif membership_status == "yes" and cart_amount >= 10000: 
	discount_amount = (cart_amount * 2) / 100;
	final_amount = cart_amount - discount_amount;
	print("Final bill", final_amount);
elif membership_status == "yes" and cart_amount <= 10000: 
	discount_amount = (cart_amount * 1) / 100;
	final_amount = cart_amount - discount_amount;
	print("Final bill", final_amount);
else:
	print("Final bill", cart_amount);