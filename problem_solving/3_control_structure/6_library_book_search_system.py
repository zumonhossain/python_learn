books = [
    "Python Crash Course",
    "Clean Code",
    "Data Structures",
    "Machine Learning Basics",
    "The Alchemist"
]

search_count = 0

while True:
    search = input("Enter book title (or 'exit' to quit): ")

    if search.lower() == "exit":
        break

    search_count += 1
    found = False
    i = 0

    while i < len(books):
        if search.lower() == books[i].lower():
            found = True
            break

        i += 1

    if found:
        print("Book found!")
    else:
        print("Book not available.")
print("Total searches made:", search_count)