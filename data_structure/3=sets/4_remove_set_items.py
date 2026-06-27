


# Remove Item
print("------------------- Remove 'banana' by using the remove() method: ---------------------");

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)



# Remove discard() method:
print("------------------- Remove 'banana' by using the discard() method: ---------------------");

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)



# pop()
print("------------------- Remove a random item by using the pop() method: ---------------------");

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



# clear
print("------------------- The clear() method empties the set: ---------------------");

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)



# Delete
print("------------------- The del keyword will delete the set completely: ---------------------");

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
