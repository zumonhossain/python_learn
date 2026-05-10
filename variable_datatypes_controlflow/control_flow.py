
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

#========================
print("if-elif-else Condition")
#========================

age = 70
if age < 18:
    print("You are a minor.")
elif age < 70:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# =========================
print("Nested if-else Condition")
#========================
marks = int(input("Enter marks: "))

if marks > 100:
    print("Invalid marks!")
elif marks >= 80 and marks <= 100:
    print("Grade: A+")
elif marks >= 70 and marks < 80:
    print("Grade: A")
elif marks >= 60 and marks < 70:
    print("Grade: B")
elif marks >= 50 and marks < 60:
    print("Grade: C")
else:
    print("Grade: F")



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


#========================
print("Nested loops")
#==========================
age = int(input("Enter age: "))
has_nid = input("Have NID? (yes/no): ")

if age >= 18:
    print("Age OK!")
    if has_nid == "yes":
        print("You can vote!")
    else:
        print("No NID!")
else:
    print("Too young!")







'''
- user input → member or not, total amount

- if
-- member and total amount between 15000 and 20000 
   → Discount 500 yen

-- member and total amount between 20001 and 500000 
   → Discount 3% of total amount

-- member and total amount above 500000 
   → Discount 6% of total amount

- calculate the final bill

'''

is_member = input("You are a member (yes/no): ").lower();
total_amount = int(input("total amount: "));
total_discount_amount = 0;

if is_member == "yes":
    if total_amount >= 15000 and total_amount <= 20000:
        total_discount_amount = 500
    elif total_amount >= 20000 and total_amount <= 50000:
        total_discount_amount = total_amount * 3/100
    elif total_amount > 50000:
        total_discount_amount = total_amount * 6/100

subtotal_amount = total_amount - total_discount_amount;
print("Total Amount: ", subtotal_amount);


# =========================
print("Ternary Operator")
#==========================

age = 20

result = "Adult" if age >= 18 else "Not Adult"
print(result)









