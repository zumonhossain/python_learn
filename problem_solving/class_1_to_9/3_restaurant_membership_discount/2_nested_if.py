member = input("Are you a member? yes or no: ").lower();
total_bill = float(input("Enter bill amount: "));

if total_bill > 0:
	if member == "yes":
		final_bill = total_bill * 0.90;
		print("Final bill:", final_bill);
	else:
		print("Final bill:", total_bill);
else:
	print("Invalid amount");