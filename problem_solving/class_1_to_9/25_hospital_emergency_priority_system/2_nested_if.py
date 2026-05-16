age = int(input("Enter age: "))
emergency = int(input("Enter emergency level: "))

if age >= 60 or emergency >= 7:
    print("Priority Treatment")
else:
    if age >= 18 and emergency >= 4:
        print("Normal Treatment")
    else:
        print("Standard Queue")