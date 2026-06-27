fruits = ["apple", "banana", "cherry", "date", "cherry", "cherry", "elderberry"];
result = fruits.count("cherry");
print(result); # Output: 3, because "cherry" appears three times in the list.

result = fruits.count("mango");
print(result); # Output: 0, because "mango" is not in the list.