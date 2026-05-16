signal = input("Enter signal: ").lower()

result = (
    "Go" if signal == "green" else
    "Slow Down" if signal == "yellow" else
    "Stop" if signal == "red" else
    "Invalid Signal"
)

print(result)