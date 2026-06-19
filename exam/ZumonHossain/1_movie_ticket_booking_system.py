ticket_booking = [];

while True:
    tickets_number = int(input("Enter number of tickets (0 to stop): "));
    if tickets_number == 0:
        break;
    ticket_amount = tickets_number * 150;
    ticket_booking.append(ticket_amount);
# print(ticket_booking);

total_revenue = 0;
height_booking = 0;
i = 0;

while i < len(ticket_booking):
    total_revenue = total_revenue + ticket_booking[i];

    if ticket_booking[i] > height_booking:
        height_booking = ticket_booking[i];
    i = i + 1;
print("Total revenue:",total_revenue);
print("Highest booking amount:", height_booking);