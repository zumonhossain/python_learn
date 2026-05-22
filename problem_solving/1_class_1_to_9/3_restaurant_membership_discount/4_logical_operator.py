member = input("Are you a member? yes or no: ").lower()
total_bill = float(input("Enter bill amount: "))

if member == "yes" and total_bill > 0:
    final_bill = total_bill * 0.90
    print("Final bill:", final_bill)

elif member == "no" and total_bill > 0:
    print("Final bill:", total_bill)

else:
    print("Invalid input")