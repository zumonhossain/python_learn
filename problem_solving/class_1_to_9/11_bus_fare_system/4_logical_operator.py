age = int(input("Enter age: "))

if age >= 0 and age <= 12:
    print("Bus fare: 150 yen")

elif age >= 13 and age <= 17:
    print("Bus fare: 300 yen")

elif age >= 18 and age <= 59:
    print("Bus fare: 500 yen")

elif age >= 60:
    print("Bus fare: 200 yen")

else:
    print("Invalid age")