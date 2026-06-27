


# Removing Items
print("--- The pop() method removes the item with the specified key name: ---");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)




# popitem()
print("--- The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead): ---");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)





# delete
print("--- The del keyword removes the item with the specified key name: ---");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)





# delete
print("--- The del keyword can also delete the dictionary completely: ---");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.





# clear()
print("--- The clear() method empties the dictionary: ---");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
