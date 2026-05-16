cgpa = float(input("Enter CGPA: "))

if cgpa >= 3.80 and cgpa <= 4.00:
    print("Full Scholarship")

elif cgpa >= 3.50 and cgpa < 3.80:
    print("Half Scholarship")

elif cgpa >= 3.00 and cgpa < 3.50:
    print("Quarter Scholarship")

elif cgpa < 3.00:
    print("No Scholarship")

else:
    print("Invalid CGPA")