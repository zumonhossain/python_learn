vehicle = input("Enter vehicle type: ").lower()
hours = int(input("Enter parking hours: "))

is_bike = vehicle == "bike"
is_car = vehicle == "car"
is_truck = vehicle == "truck"

if is_bike:
    print("Total fee:", 100 * hours, "yen")
elif is_car:
    print("Total fee:", 300 * hours, "yen")
elif is_truck:
    print("Total fee:", 500 * hours, "yen")
else:
    print("Invalid vehicle type")