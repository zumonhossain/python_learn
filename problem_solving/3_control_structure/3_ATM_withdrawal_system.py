account_balance = 50000;
print("Balance:", account_balance)

while True:
    input_amount = int(input("Enter withdrawal amount (0 to exit): "))
    if input_amount <= 0:
        break
    elif input_amount > account_balance:
        print("Insufficient funds.")
    else:
        account_balance = account_balance - input_amount
        print("Withdrawal successful. Remaining balance:", account_balance)
print("Thank you! Final balance:", account_balance)