# Finding the maximum value manually
numbers = [4, 8, 15, 16, 23, 42]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest:", largest)