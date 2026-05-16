age = int(input("Enter age: "))
country = input("Enter country: ").lower()

result = "Access Granted" if age >= 18 or country == "japan" else "Access Denied"

print(result)