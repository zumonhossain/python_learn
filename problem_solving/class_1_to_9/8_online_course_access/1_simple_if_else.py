age = int(input("Enter age: "));
country = input("Enter country: ").lower();

if age >= 18 or country == "japan":
    print("Access Granted");
else:
    print("Access Denied");