
#=============================================================
print("----- Shallow copy of a list using the copy() method -----");
#=============================================================
fruits = ['apple', 'banana', 'cherry'];
# Shallow copy
fruits_copy = fruits.copy();
print(fruits_copy); # ['apple', 'banana', 'cherry']


#==============================================================
print("----- Modifying the original list does not affect the copied list -----");
#==============================================================
# Modifying the original list
fruits.append('fig');
print(fruits); # ['apple', 'banana', 'cherry', 'fig']
print(fruits_copy); # ['apple', 'banana', 'cherry']


#=============================================================
print("----- Using the copy() method to create a copy of the list -----");
#=============================================================
# Using the copy() method to create a copy of the list
fruits = ["apple", "banana", "cherry"]
fruits2 = fruits.copy()
print(fruits2) # Output: ['apple', 'banana', 'cherry']


#=============================================================
print("----- Modifying the original list does not affect the copied list -----");
#=============================================================
# Modifying the original list does not affect the copied list
fruits = ["apple", "banana", "cherry"]
fruits2 = fruits.copy()

fruits2.append("mango")

print(fruits) # Output: ['apple', 'banana', 'cherry']
print(fruits2) # Output: ['apple', 'banana', 'cherry', 'mango']