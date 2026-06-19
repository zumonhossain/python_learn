words = []

while True:
    word = input("Enter a word (or 'done'): ")

    if word == "done":
        break

    words.append(word)

search_word = input("Enter a word to search: ")

count = 0
i = 0

while i < len(words):
    if words[i] == search_word:
        count = count + 1

    i = i + 1

print(search_word, count, "times")