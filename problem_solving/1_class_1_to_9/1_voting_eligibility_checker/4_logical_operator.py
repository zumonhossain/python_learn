

# age = int(input("enter your age:"));
# if age >= 18 and age <= 100:
# 	print("Eligible for voting");
# else:
# 	print("Not eligible for voting");
 



age = int(input("Enter your age:"));
if age > 0 and age <= 100:
	if age >= 18:
		print("Eligible for voting");
	else:
		print("Not eligible for voting");
else:
	print("Invalid age");