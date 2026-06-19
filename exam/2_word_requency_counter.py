word_list = [];

while True:
    word_input = input("Enter a word (or 'done'): ");

    if word_input == "done":
        break;
    word_list.append(word_input);

search_word = input("search word:");
count_item = 0;
i = 0;

while i < len(word_list):
    if word_list[i] == search_word:
        count_item = count_item + 1;
    i = i + 1;
print(search_word, "count_item", "times");
