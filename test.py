python_score = int(input("Enter Python skill score: "))
problem_solving = int(input("Enter problem solving score: "))
communication = input("Enter communication skill (good/bad): ").lower()
experience = int(input("Enter years of experience: "))

if python_score < 80:
    print("Not Selected")

elif problem_solving < 75:
    print("Not Selected")

elif communication != "good":
    print("Not Selected")

elif experience < 2:
    print("Not Selected")

else:
    print("Selected for Final HR Round")