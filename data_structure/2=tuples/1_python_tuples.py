
# Create a Tuple
print("------------------- Create a Tuple ---------------------");

mytuple = ("apple", "banana", "cherry");
print(mytuple);


# Allow Duplicates
print("------------------- Allow Duplicates ---------------------");

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# Tuple Length
print("------------------- Tuple Length ---------------------");

thistuple = ("apple", "banana", "cherry")
print(len(thistuple));



# Create Tuple With One Item
print("------------------- Create Tuple With One Item ---------------------");

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))



# String, int and boolean data types:
print("------------------- String, int and boolean data types: ---------------------");

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1);
print(tuple2);
print(tuple3);



# A tuple with strings, integers and boolean values:
print("------------------- A tuple with strings, integers and boolean values: ---------------------");

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1);



# What is the data type of a tuple?
print("------------------- What is the data type of a tuple? ---------------------");

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))



# Using the tuple() method to make a tuple:
print("------------------- Using the tuple() method to make a tuple: ---------------------");

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)