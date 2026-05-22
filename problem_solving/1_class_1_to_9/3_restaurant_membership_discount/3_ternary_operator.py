# member = input("Are you a member? yes or no: ").lower();
# total_bill = float(input("Enter bill amount: "));

# final_bill = "Final bill:" + str(total_bill * 0.90) if member == "yes" else "Total bill:" + str(total_bill);
# print(final_bill); 


member = input("Are you a member? yes or no: ").lower();
total_bill = float(input("Enter bill amount: "));

final_bill = total_bill * 0.90 if member == "yes" else total_bill;
print("Final bill:", final_bill);