
# The break statement is used to exit a loop prematurely when a certain condition is met.

# for i in range(10):
#     if i == 5:
#         break
#     print(i) # Output: 0 1 2 3 4

# ----------------------------------------------------




# The break statement can also be used in while loops.

# count = 0
# while count < 10:
#     if count == 5:
#         break
#     print(count)
#     count += 1 # Output: 0 1 2 3 4



# --------------------------------------------



# Example: A simple login system that allows the user to enter a pin. The user has 3 attempts to enter the correct pin before being locked out.
count = 0

while count < 3:
    user_pin = int(input("Enter pin: "))

    if user_pin == 123456:
        print("Login Successful")
        break

    else:
        count = count + 1

        if count >= 3:
            print("Try again in 24 hours!")

