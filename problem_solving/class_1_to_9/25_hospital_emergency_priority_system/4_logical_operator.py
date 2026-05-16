age = int(input("Enter age: "))
emergency = int(input("Enter emergency level: "))

is_priority = age >= 60 or emergency >= 7
is_normal = age >= 18 and emergency >= 4

if is_priority:
    print("Priority Treatment")
elif is_normal:
    print("Normal Treatment")
else:
    print("Standard Queue")