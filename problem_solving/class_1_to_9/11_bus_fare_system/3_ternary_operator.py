age = int(input("Enter age: "))

result = (
    "Bus fare: 150 yen" if age <= 12 else
    "Bus fare: 300 yen" if age <= 17 else
    "Bus fare: 500 yen" if age <= 59 else
    "Bus fare: 200 yen"
)

print(result)