python_score = int(input("Enter Python skill score: "))
problem_solving = int(input("Enter problem solving score: "))
communication = input("Enter communication skill (good/bad): ").lower()
experience = int(input("Enter years of experience: "))

if python_score >= 80:
    if problem_solving >= 75:
        if communication == "good":
            if experience >= 2:
                print("Selected for Final HR Round")
            else:
                print("Not Selected")
        else:
            print("Not Selected")
    else:
        print("Not Selected")
else:
    print("Not Selected")