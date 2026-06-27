


# Loop Through a Dictionary
print("--- Print all key names in the dictionary, one by one: ---");

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)




# Print all values in the dictionary, one by one:
print("--- Print all values in the dictionary, one by one: ---");

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
  



# values()
print("--- You can also use the values() method to return values of a dictionary: ---");

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
  



# keys()
print("--- You can use the keys() method to return the keys of a dictionary: ---");

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
    



# items()
print("--- Loop through both keys and values, by using the items() method: ---");

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)