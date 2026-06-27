fruits = ["elderberry", "apple", "banana", "cherry", "date", "cherry", "cherry"];
result = sorted(fruits);
print(result); # ['apple', 'banana', 'cherry', 'cherry', 'cherry', 'date', 'elderberry']


fruits = ["elderberry", "apple", "banana", "cherry", "date", "cherry", "cherry"];
result = sorted(fruits, reverse=True);
print(result); # ['elderberry', 'date', 'cherry', 'cherry', 'cherry', 'banana', 'apple']    


numbers = [5, 2, 9, 1, 5, 6];
result = sorted(numbers);
print(result); # [1, 2, 5, 5, 6, 9]

numbers = [5, 2, 9, 1, 5, 6];
result = sorted(numbers, reverse=True);
print(result); # [9, 6, 5, 5, 2, 1]

