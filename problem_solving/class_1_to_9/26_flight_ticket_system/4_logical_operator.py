nationality = input("Enter nationality: ")
passport = input("Is passport valid? (yes/no): ").lower()

is_valid = passport == "yes"

if is_valid:
    print("Ticket Booking Allowed")
else:
    print("Ticket Booking Denied")