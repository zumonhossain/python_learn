python_score = int(input("Enter Python skill score: "))
problem_solving = int(input("Enter problem solving score: "))
communication = input("Enter communication skill (good/bad): ").lower()
experience = int(input("Enter years of experience: "))

print(
    "Selected for Final HR Round"
    if python_score >= 80
    and problem_solving >= 75
    and communication == "good"
    and experience >= 2
    else "Not Selected"
)