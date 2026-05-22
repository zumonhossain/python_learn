age = int(input("Enter age: "))
country = input("Enter country: ").lower()

if age >= 18 or country == "japan":
    print("Access Granted")

elif age < 18 and country != "japan":
    print("Access Denied")