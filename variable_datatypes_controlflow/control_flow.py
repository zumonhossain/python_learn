
# if Condition
age = 18
if age >= 18:
    print("You are an adult.")

# if-else Condition
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if-elif-else Condition
age = 70
if age < 18:
    print("You are a minor.")
elif age < 70:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Logical Operators and
name = "Rasel"
age = 20
has_nid = True

if age >= 18 and has_nid == True:
    print(name, "can vote! Age OK and NID OK.")
else:
    print(name, "cannot vote!")

# Logical Operators or
name = "Rasel"
age = 20
has_permission = False

if age >= 18 or has_permission == True:
    print(name, "can vote!")
else:
    print(name, "cannot vote!")


# Logical Operators not
name = "Rasel"
age = 20
is_underage = False

if not is_underage:
    print(name, "can vote!")
else:
    print(name, "cannot vote!")


# Ternary Operator

name = "Rasel"
age = 20

result = "can vote!" if age >= 18 else "cannot vote!"
print(name, result)



#========================
print("for loop")
#==========================
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#========================
print("while loop")
#==========================

count = 1
while count <= 5:
    print("Count:", count)
    count = count + 1


#========================
print("break statement")
#==========================

for i in range(1, 10):
    if i == 5:
        break
    print(i)
print("Loop ended!")


#========================
print("continue statement") 
#==========================

for i in range(1, 10):
    if i == 5:
        continue
    print(i)
print("Loop ended!")