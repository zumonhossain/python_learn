gpa_score = float(input("Enter GPA: "));
ielts_score = float(input("Enter IELTS: "));

if gpa_score >= 3.5 and ielts_score >= 6.5:
    print("Eligible for admission");
elif gpa_score < 3.5:
    print("GPA requirement not met");
else:
    print("IELTS requirement not met");