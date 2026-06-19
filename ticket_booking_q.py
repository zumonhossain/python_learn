queue = []

# Step 1: Take input
while True:
    name = input("Enter name (or type 'start' to begin): ")
    
    if name.lower() == "start":
        break
    
    queue.append(name)

# Step 2: Serve people
while len(queue) > 0:
    current = queue.pop(0)   # remove from front
    remaining = len(queue)
    
    print(f"Serving: {current}. Remaining: {remaining}")

# Step 3: End
print("Queue is empty. All customers served.")