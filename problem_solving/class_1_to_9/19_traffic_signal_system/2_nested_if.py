signal = input("Enter signal: ").lower()

if signal == "green":

    print("Go")

else:

    if signal == "yellow":
        print("Slow Down")

    elif signal == "red":
        print("Stop")

    else:
        print("Invalid Signal")