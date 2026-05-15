units = int(input("Enter units: "))

if units > 500 and units >= 0:
    print("High Bill")

elif units <= 500 and units >= 0:
    print("Normal Bill")

else:
    print("Invalid units")