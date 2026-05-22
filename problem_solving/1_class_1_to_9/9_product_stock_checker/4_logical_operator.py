quantity = int(input("Enter quantity: "))

if quantity > 0 and quantity <= 1000:
    print("In Stock")

elif quantity <= 0 or quantity > 1000:
    print("Out of Stock")