nationality = input("Enter nationality: ")
passport = input("Is passport valid? (yes/no): ").lower()

print("Ticket Booking Allowed" if passport == "yes" else "Ticket Booking Denied")