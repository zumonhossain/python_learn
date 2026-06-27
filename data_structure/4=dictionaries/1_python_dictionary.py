



# Dictionary
print("------------------- Create and print a dictionary: ---------------------");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)




# Dictionary Items
print("------------------- Print the 'brand' value of the dictionary: ---------------------");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])




# Duplicates Not Allowed
print("------------------- Duplicate values will overwrite existing values:  ---------------------");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)




# Dictionary Length
print("------------------- Duplicate values will overwrite existing values:  ---------------------");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))




# Dictionary Items - Data Types
print("------------------- String, int, boolean, and list data types:  ---------------------");

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)





# type()
print("------------------- Print the data type of a dictionary:  ---------------------");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))





# The dict() Constructor
print("------------------- Using the dict() method to make a dictionary:  ---------------------");

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


