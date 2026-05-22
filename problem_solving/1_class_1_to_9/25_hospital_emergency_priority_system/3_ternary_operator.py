age = int(input("Enter age: "))
emergency = int(input("Enter emergency level: "))

print(
    "Priority Treatment"
    if age >= 60 or emergency >= 7
    else "Normal Treatment"
    if age >= 18 and emergency >= 4
    else "Standard Queue"
)