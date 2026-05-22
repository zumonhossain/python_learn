signal = input("Enter signal: ").lower()

if signal == "green":
    print("Go")

elif signal == "yellow":
    print("Slow Down")

elif signal == "red":
    print("Stop")

elif signal != "green" and signal != "yellow" and signal != "red":
    print("Invalid Signal")