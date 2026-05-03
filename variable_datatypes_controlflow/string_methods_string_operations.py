
# =====================================================
from doctest import Example


print("-----Whitespace Removal Example------")
# =====================================================
text = "   Hello World   "
print("Before:", text)

new_text = text.strip()
print("After:", new_text)



# =====================================================
print("-----Substring Replacement Example------")
# =====================================================

text = "I love cats"
print("Before:", text)
new_text = text.replace("cats", "dogs")
print("After:", new_text)


# =====================================================
print("-----Startswith 1st text hello- true ------")
# =====================================================

text = "Hello World"
print("Does the text start with 'Hello'? ", text.startswith("Hello"))


# =====================================================
print("-----Startswith 2nd text hello- false because case matters - small size ------")   
# =====================================================
text = "Hello World"
print("Does the text start with 'hello'? ", text.startswith("hello"))


# =====================================================
print("-----Endswith 1st text world- true ------")  
# =====================================================
text = "Hello World"
print("Does the text end with 'World'? ", text.endswith("World"))

# =====================================================
print("-----Endswith 2nd text world- false because case matters - small size ------")
# =====================================================
text = "Hello World"
print("Does the text end with 'world'? ", text.endswith("world"))

# =====================================================
print("-----Case Conversion Example------")
# =====================================================
text = "Hello World"
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


# =====================================================
print("-----Splitting and Joining Example------")
# =====================================================
text = "Hello World"
print("Original:", text)
words = text.split()
print("Split:", words)
new_text = " ".join(words)
print("Joined:", new_text)


# =====================================================
print("-----Finding Substring Example------")
# =====================================================
text = "Hello World"
print("Original:", text)
index = text.find("World")
print("Index of 'World':", index)

# =====================================================
print("-----Finding Substring Not Found Example------")
# =====================================================
text = "Hello World"
print("Original:", text)
index = text.find("Python")
print("Index of 'Python':", index)


# =====================================================
print("-----Counting Substring Occurrences Example------")
# =====================================================
text = "Hello World Hello"
print("Original:", text)
count = text.count("Hello")
print("Number of occurrences of 'Hello':", count)


# =====================================================
print("-----Checking for Substring Example------")
# =====================================================
text = "Hello World"
print("Original:", text)
print("Does the text contain 'World'? ", "World" in text)


# =====================================================
print("-----Checking for Substring Not Found Example------")    
# =====================================================
text = "Hello World"
print("Original:", text)
print("Does the text contain 'Python'? ", "Python" in text)


# =====================================================
print("----- F String Formatting Example------")
# =====================================================
name = "Zumon Hossain"
age = 28
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")  # Using string concatenation
print(f"Hello, my name is {name} and I am {age} years old.") # Using f-string for formatting

# =====================================================
print("----- Title Example------")
# =====================================================
text = "hello world"
print("Original:", text)
print("Title:", text.title())


# =====================================================
print("-----Capitalization Example------")
# =====================================================
text = "hello world"
print("Original:", text)
print("Capitalized:", text.capitalize())

# =====================================================
print("-----Centering Example------")
# =====================================================
text = "Hello"
print("Original:", text)
print("Centered:", text.center(10))

# =====================================================
print("-----Zero Padding Example------")
# =====================================================
number = "42"
print("Original:", number)
print("Zero-padded:", number.zfill(5))


# =====================================================
print("-----String Slicing Example------")
# =====================================================
text = "Hello World"
print("Original:", text)
print("Sliced (0:5):", text[0:5])
print("Sliced (6:11):", text[6:11])


# =====================================================
print("-----isalnum() Alphanumeric Example------")
# ===================================================== 
text = "Hello123"
print("Original:", text)
print("Is alphanumeric?", text.isalnum())

# =====================================================
print("-----isalpha() Alphabetic Example------")
# =====================================================
text = "Hello"
print("Original:", text)
print("Is alphabetic?", text.isalpha())


# =====================================================
print("-----isdigit() Numeric Example------")
# =====================================================
text = "12345"
print("Original:", text)
print("Is digit?", text.isdigit())

# =====================================================
print("-----isspace() Whitespace Example------")
# =====================================================
text = "   "
print("Original:", repr(text))
print("Is whitespace?", text.isspace())

# =====================================================
print("-----isspace() Non-Whitespace Example------")
# =====================================================
text = "Hello"
print("Original:", repr(text))
print("Is whitespace?", text.isspace())


# =====================================================
print("-----Length of String Example------")
# =====================================================
text = "Hello World"
print("Original:", text)
print("Length of the string:", len(text))


# =====================================================
print("-----String Concatenation Example------")
# =====================================================
text1 = "Hello"
text2 = "World"
text3 = text1 + " " + text2
print("Original:", text3)


# =====================================================
print("-----String Repetition Example------")
# =====================================================
text = "Hello "
repeated_text = text * 3
print("Original:", repeated_text)


# =====================================================
print("-----String Formatting with format() Example------")
# =====================================================
name = "Zumom Hossain"
age = 30
print("Hello, my name is {} and I am {} years old.".format(name, age))


# =====================================================
print("-----String Formatting with format() and Positional Arguments Example------")
# =====================================================
name = "Zumom Hossain"
age = 28
print("Hello, my name is {0} and I am {1} years old.".format(name, age))

# =====================================================
print("-----String Formatting with format() and Keyword Arguments Example------")
# =====================================================
name = "Zumom Hossain"
age = 28
print("Hello, my name is {name} and I am {age} years old.".format(name=name, age=age))


# =====================================================
print("-----String Formatting with f-strings Example------")
# =====================================================
name = "Zumom Hossain"
age = 28
print(f"Hello, my name is {name} and I am {age} years old.")


# =====================================================
print("-----String Formatting with f-strings and Expressions Example------")
# ===================================================== 
name = "Zumom Hossain"
age = 28
print(f"Hello, my name is {name} and I am {age} years old.")


# =====================================================
print("-----String Formatting with f-strings and Formatting Specifiers Example------")
# =====================================================
name = "Zumom Hossain"
age = 28
print(f"Hello, my name is {name} and I am {age} years old.")


# =====================================================
print("-----String Formatting with f-strings and Alignment Example------")
# =====================================================
name = "Zumom Hossain"
age = 28 
print(f"Hello, my name is {name} and I am {age} years old.")

# =====================================================
print("-----String Formatting with f-strings and Padding Example------")
# =====================================================
name = "Zumom Hossain"
age = 28
print(f"Hello, my name is {name} and I am {age} years old.")

# =====================================================
print("-----String Formatting with f-strings and Padding Example------")
# =====================================================
name = "Zumom Hossain"
age = 28
print(f"Hello, my name is {name:10} and I am {age:5} years old.")


# =====================================================
print("-----String Formatting with f-strings and Padding with Zeros Example------")
# =====================================================
name = "Zumom Hossain"
age = 28
print(f"Hello, my name is {name:010} and I am {age:05} years old.")


# =====================================================
print("-----String Indexing and Slicing Example------")
# =====================================================
text = "Hello World"
print("Original:", text)
print("First character:", text[0])
print("Last character:", text[-1])
print("Character at index 7:", text[7])
print("Last five characters:", text[6:11])
print("First five characters:", text[0:5])

# =====================================================
print("-----String Immutability Example------")
# =====================================================
text = "Hello World"
print("Original:", text)


#====================================================   
print("-----Data Type of text-----")
#====================================================
text = "Hello World"
print("Type of text:", type(text))


#====================================================
print("-----String Length Example------")
#====================================================
text = "Hello World"
print("Length of the string:", len(text))




#====================================================
print("----- multiple methods added together example Example------")
#====================================================

text = "   Hello World   "

text.strip()                            # "Hello World"
text.strip().lower()                    # "hello world"
text.strip().lower().replace("world", "python")  # "hello python"
print("Original:", text)
print("Modified:", text.strip().lower().replace("world", "python"))
