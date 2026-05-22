age = int(input("Enter your age:"));
if age > 0:
	if age >= 18:
		print("Eligible for voting");
	else:
		print("Not eligible for voting");
else:
	print("Invalid age");