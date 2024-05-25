def evaluate_performance(presentation, communication, productivity, leadership, coding_skills):
    # Weightage for each skill
    presentation_weight = 0.25
    communication_weight = 0.2
    productivity_weight = 0.2
    leadership_weight = 0.2
    coding_skills_weight = 0.15

    # Calculate the overall score
    overall_score = (
        presentation * presentation_weight +
        communication * communication_weight +
        productivity * productivity_weight +
        leadership * leadership_weight +
        coding_skills * coding_skills_weight
    )

    return overall_score

def employee_of_the_year(employees):
    best_employee = None
    best_performance = -1
    for employee, skills in employees.items():
        performance = evaluate_performance(
            skills["presentation"], 
            skills["communication"], 
            skills["productivity"], 
            skills["leadership"], 
            skills["coding_skills"]
        )
        if performance > best_performance:
            best_employee = employee
            best_performance = performance
    return best_employee

def best_employee_by_skill(employees, skill):
    best_employee = None
    best_performance = -1
    for employee, skills in employees.items():
        performance = skills[skill]
        if performance > best_performance:
            best_employee = employee
            best_performance = performance
    return best_employee

# Store skills for 5 employees
employees = {
    "Employee 1": {"presentation": 85, "communication": 90, "productivity": 80, "leadership": 75, "coding_skills": 80},
    "Employee 2": {"presentation": 70, "communication": 80, "productivity": 90, "leadership": 85, "coding_skills": 85},
    "Employee 3": {"presentation": 80, "communication": 75, "productivity": 85, "leadership": 90, "coding_skills": 75},
    "Employee 4": {"presentation": 90, "communication": 85, "productivity": 70, "leadership": 80, "coding_skills": 95},
    "Employee 5": {"presentation": 75, "communication": 70, "productivity": 95, "leadership": 85, "coding_skills": 70}
}

# Calculate performance for each employee
# for employee, skills in employees.items():
#     performance = evaluate_performance(
#         skills["presentation"], 
#         skills["communication"], 
#         skills["productivity"], 
#         skills["leadership"], 
#         skills.get("coding_skills", 0) # Use get method to handle the case when "coding_skills" is not present
#     )
#     employees[employee]["performance"] = performance

# Prompt for action
while True:

    prompt = input("What would you like to know? ")

    # Perform the appropriate action
    if "year" in prompt.lower():
        best_employee_year = employee_of_the_year(employees)
        print("Employee of the Year:", best_employee_year)
    elif any(skill in prompt.lower() for skill in ["presentation", "communication", "productivity", "leadership"]):
        skill = next(skill for skill in ["presentation", "communication", "productivity", "leadership"] if skill in prompt.lower())
        best_employee_skill = best_employee_by_skill(employees, skill)
        print(f"Best Employee for {skill.capitalize()}: {best_employee_skill}")
    elif "coding" in prompt.lower():
        best_employee_coding = best_employee_by_skill(employees, "coding_skills")
        print(f"Best Employee for Coding Skills: {best_employee_coding}")
    else:
        print("Invalid input.")
