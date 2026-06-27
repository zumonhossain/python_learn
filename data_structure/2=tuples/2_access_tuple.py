
# Access Tuple Items
print("------------------- Print the second item in the tuple: ---------------------");

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])



# Negative Indexing
print("------------------- Print the last item of the tuple: ---------------------");

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])



# Range of Indexes
print("------------------- Return the third, fourth, and fifth item: ---------------------");

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])



# This example returns the items from the beginning to, but NOT included, "kiwi":
print("------------------- This example returns the items from the beginning to, but NOT included, 'kiwi': ---------------------");

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])



# This example returns the items from "cherry" and to the end:
print("------------------- This example returns the items from 'cherry' and to the end: ---------------------");

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])



# This example returns the items from "cherry" and to the end:
print("------------------- This example returns the items from 'cherry' and to the end: ---------------------");

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])



# Range of Negative Indexes
print("------------------- This example returns the items from index -4 (included) to index -1 (excluded) ---------------------");

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])



# Check if Item Exists
print("------------------- Check if 'apple' is present in the tuple: ---------------------");

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  


# Check if Item Exists
print("------------------- Check if 'apple' is present in the tuple: ---------------------");

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")