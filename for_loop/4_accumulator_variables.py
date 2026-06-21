#=======================================================
print("------------------ Sum of a list ----------------------")
#=======================================================

# Sum of a list
numbers = [4, 8, 15, 16, 23, 42]
total = 0
for n in numbers:
    total += n
print("Total:", total) # Output: Total: 108

#=======================================================
print("------------------ Finding the maximum value manually ----------------------")
#=======================================================

# Finding the maximum value manually
numbers = [4, 8, 15, 16, 23, 42]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest:", largest)


#=======================================================
print("------------------ Counting items that meet a condition ----------------------")
#=======================================================

# Counting items that meet a condition
words = ["cat", "elephant", "dog", "butterfly", "ant"]
count = 0
for word in words:
    if len(word) > 3:
        count += 1
print("Words longer than 3 letters:", count)


