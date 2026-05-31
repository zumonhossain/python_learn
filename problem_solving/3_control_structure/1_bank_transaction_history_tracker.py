balance = 100000

transaction_types = []
transaction_amounts = []

deposit_count = 0
withdraw_count = 0

print("Opening Balance:", balance)

while True:

    t_type = input("Enter transaction type (deposit/withdraw or 'done'): ")

    if t_type.lower() == "done":
        break

    amount = int(input("Enter amount: "))

    t_type = t_type.upper()

    if t_type == "DEPOSIT":
        balance += amount

        transaction_types.append(t_type)
        transaction_amounts.append(amount)

        deposit_count += 1

    elif t_type == "WITHDRAW":

        if amount > balance:
            print("Rejected: Insufficient balance")

        else:
            balance -= amount

            transaction_types.append(t_type)
            transaction_amounts.append(amount)

            withdraw_count += 1

    else:
        print("Invalid transaction type")

print("=========================================================")
print("TRANSACTION HISTORY")
print("=========================================================")

print("No. | Type | Amount | Balance")
print("------------------------------------------------")

i = 0
running_balance = 100000

while i < len(transaction_types):

    t_type = transaction_types[i]
    amount = transaction_amounts[i]

    if t_type == "DEPOSIT":
        running_balance += amount
        sign = "+"

    else:
        running_balance -= amount
        sign = "-"

    print(i + 1, "|", t_type, "|", sign + str(amount), "|", running_balance)

    i += 1

print("------------------------------------------------")

print("Total Deposits :", deposit_count)
print("Total Withdrawals:", withdraw_count)
print("Closing Balance :", balance)