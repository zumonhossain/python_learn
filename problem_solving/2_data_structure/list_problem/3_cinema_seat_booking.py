given_seats =  [10, 11, 12, 13, 14, 15, 16];
booked_seats = given_seats[2:5];
print("First seat:", given_seats[0], "|", "Last seat:", given_seats[-1]);
print("Booked seats:", booked_seats);
if len(booked_seats) == 3:
	print("Booking confirmed for 3 seats!");