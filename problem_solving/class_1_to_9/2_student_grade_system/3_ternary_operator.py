marks = int(input("Enter your marks: "))

result = (
	"A+" if marks >= 90 else
	"A" if marks >= 80 else
	"B" if marks >= 70 else
	"C" if marks >= 60 else
	"F"
)
print(result)