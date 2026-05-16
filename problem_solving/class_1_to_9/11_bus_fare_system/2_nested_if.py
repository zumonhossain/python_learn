age = int(input("Enter age: "))

if age >= 0:

    if age <= 12:
        print("Bus fare: 150 yen")

    elif age <= 17:
        print("Bus fare: 300 yen")

    elif age <= 59:
        print("Bus fare: 500 yen")

    else:
        print("Bus fare: 200 yen")

else:
    print("Invalid age")