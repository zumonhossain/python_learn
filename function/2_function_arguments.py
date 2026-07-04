
print("-------- one argument ---------")
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")



print("-------- 2 arguments, and gets 2 arguments ---------")
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


print("-------- Default Parameter Values ---------")
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")



print("-------- Keyword Arguments ---------")
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")



print("-------- Positional Arguments ---------")
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")


print("-------- Mixing Positional and Keyword Arguments ---------")
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)



print("-------- Passing Different Data Types ---------")
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


print("-------- Return Values ---------")
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


print("-------- Returning Different Data Types ---------")
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


print("-------- Positional-Only Arguments ---------")
def my_function(name, /):
  print("Hello", name)

my_function("Emil")


print("-------- Keyword-Only Arguments ---------")
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")


print("-------- Combining Positional-Only and Keyword-Only ---------")
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


