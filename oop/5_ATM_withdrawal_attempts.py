pin = 1234;
attempts = 3;

while attempts > 0:
    guess = int(input("Enter pin: "));

    if guess == pin:
        print("Access granted");
        break

    attempts -= 1

if attempts == 0 and guess != pin:
    print("Card blocked");