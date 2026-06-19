fine_list = [];

while True:
    days_input = int(input("Enter overdue days (-1 to stop): "));

    if days_input == -1:
        break;

    if days_input <= 0:
        fine = 0
    else:
        fine = days_input * 5

    fine_list.append(fine)

total_fines = 0;
no_fine_books = 0;
i = 0;

while i < len(fine_list):
    total_fines = total_fines + fine_list[i];

    if fine_list[i] == 0:
        no_fine_books = no_fine_books + 1

    i = i + 1

print("Total fines collected: ¥" + str(total_fines));
print("Books with no fine:", no_fine_books);