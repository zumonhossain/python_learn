


# Accessing Items
print("------------------- Get the value of the 'model' key:  ---------------------");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)




# get
print("------------------- Get the value of the 'model' key:  ---------------------");

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)




# Get Keys
print("------------------- Get a list of the keys:  ---------------------");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)




# Add a new item to the original dictionary, and see that the keys list gets updated as well:
print("--- Add a new item to the original dictionary, and see that the keys list gets updated as well:  ---");

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change




# Get Values
print("--- Get a list of the values:  ---");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)




# Make a change in the original dictionary, and see that the values list gets updated as well:
print("--- Make a change in the original dictionary, and see that the values list gets updated as well:  ---");

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change




# Add a new item to the original dictionary, and see that the values list gets updated as well:
print("--- Add a new item to the original dictionary, and see that the values list gets updated as well: ---");

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change




# Get Items
print("--- Get a list of the key:value pairs ---");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)




# Make a change in the original dictionary, and see that the items list gets updated as well:
print("--- Make a change in the original dictionary, and see that the items list gets updated as well: ---");

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change





# Check if Key Exists
print("--- Check if 'model' is present in the dictionary: ---");

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")