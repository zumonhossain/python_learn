rooms = [
    ["Standard", 5000, 1],
    ["Deluxe", 8000, 1],
    ["Suite", 15000, 1],
    ["Family", 10000, 1],
    ["Executive", 20000, 1]
]

print("========================================")
print("HOTEL ROOM AVAILABILITY")
print("========================================")
print("No. | Type | Price/Night | Status")
print("----------------------------------------")

i = 0
while i < len(rooms):
    status = "Available" if rooms[i][2] == 1 else "Booked"
    print(f"{i+1} | {rooms[i][0]} | {rooms[i][1]} | {status}")
    i += 1

total_booked = 0
total_revenue = 0

while True:
    choice = int(input("Enter room number to book (0 to exit): "))

    if choice == 0:
        break

    if choice < 1 or choice > 5:
        print("Invalid room number!")
        continue

    index = choice - 1

    if rooms[index][2] == 0:
        print("Room not available.")
    else:
        rooms[index][2] = 0

        room_type = rooms[index][0]
        price = rooms[index][1]

        total_cost = price * 3

        print(f"Booking confirmed! {room_type} room for 3 nights.")
        print(f"Total cost: {total_cost} yen")

        total_booked += 1
        total_revenue += total_cost

print(f"Total rooms booked : {total_booked}")
print(f"Total revenue : {total_revenue} yen")