age = int(input("Enter age: "));

if age <= 12:
    print("Child Bus Fare: 150 Yen");
elif age <= 17:
    print("Teen Bus Fare: 300 Yen");
elif age <= 59:
    print("Adult Bus Fare: 500 Yen");
else:
    print("Senior Bus Fare: 200 Yen");