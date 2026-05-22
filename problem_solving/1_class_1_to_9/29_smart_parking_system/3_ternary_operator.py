vehicle = input("Enter vehicle type: ").lower()
hours = int(input("Enter parking hours: "))

fee = (
    100 * hours if vehicle == "bike" else
    300 * hours if vehicle == "car" else
    500 * hours if vehicle == "truck" else
    None
)

print("Invalid vehicle type" if fee is None else f"Total fee: {fee} yen")