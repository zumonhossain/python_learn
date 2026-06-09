nationality = input("Enter nationality: ")
passport = input("Is passport valid? ")

if nationality == "Bangladesh" and passport == "yes":
    print("Ticket Booking Allowed")
else:
    print("Ticket Booking Denied")