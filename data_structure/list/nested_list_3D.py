fruits = [
    ["Apple", "Banana", "Cherry", "Strawberry"],
    ["Mango", "Orange", ["Fig", "Date", "Persimmon", "Pomegranate"], "Peach", "Watermelon"],
    ["Grapes", "Pineapple", "Kiwi", "Blueberry"],
    ["Pears", "Plums", "Apricots", ["Lychee", "Dragon Fruit", "Starfruit", "Durian"], "Cantaloupe"],
    ["Raspberry", "Blackberry", "Lemon", "Lime"],
    ["Coconut", "Papaya", "Guava", "Passion Fruit"],
]

print(fruits[1][2][3])  # Output: Pomegranate
print(fruits[3][3][0])  # Output: Lychee
print(fruits[3][3][2])  # Output: Starfruit
print(fruits[0][1])     # Output: Banana
print(fruits[4][2])     # Output: Lemon
print(fruits[5][3])     # Output: Passion Fruit
