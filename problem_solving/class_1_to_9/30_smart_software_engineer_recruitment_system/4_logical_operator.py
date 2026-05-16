python_score = int(input("Enter Python skill score: "))
problem_solving = int(input("Enter problem solving score: "))
communication = input("Enter communication skill (good/bad): ").lower()
experience = int(input("Enter years of experience: "))

is_python_ok = python_score >= 80
is_problem_ok = problem_solving >= 75
is_comm_ok = communication == "good"
is_exp_ok = experience >= 2

if is_python_ok and is_problem_ok and is_comm_ok and is_exp_ok:
    print("Selected for Final HR Round")
else:
    print("Not Selected")