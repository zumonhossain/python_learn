age = int(input("Enter age: "))

if age >= 18 and age <= 100:
    print("You can watch the movie")

elif age < 18 or age > 100:
    print("You cannot watch the movie")