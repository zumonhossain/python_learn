cgpa = float(input("Enter CGPA: "))

result = (
    "Full Scholarship" if cgpa >= 3.80 else
    "Half Scholarship" if cgpa >= 3.50 else
    "Quarter Scholarship" if cgpa >= 3.00 else
    "No Scholarship"
)

print(result)