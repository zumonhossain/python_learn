marks = int(input("Enter your marks:"));
if marks > 60:
	if marks >= 90:
		print("A+");
	elif marks >= 80:
		print("A");
	elif marks >= 70:
		print("B");
	else:
		print("C");
else:
	print("F");