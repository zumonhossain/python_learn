age = int(input("Enter age: "))
country = input("Enter country: ").lower()

if age >= 18:

    print("Access Granted")

else:

    if country == "japan":
        print("Access Granted")

    else:
        print("Access Denied")