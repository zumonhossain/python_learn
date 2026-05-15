pin = int(input("Enter PIN: "))

if pin == 1234 and len(str(pin)) == 4:
    print("Access Granted")

elif pin != 1234 or len(str(pin)) != 4:
    print("Access Denied")