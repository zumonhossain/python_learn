nationality = input("Enter nationality: ")
passport = input("Is passport valid? (yes/no): ").lower()

if passport == "yes":
    print("Ticket Booking Allowed")
else:
    print("Ticket Booking Denied")