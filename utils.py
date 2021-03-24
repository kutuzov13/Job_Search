def predict_salary(salary_from, salary_to):
    avg_salary = None

    if salary_from and salary_to:
        avg_salary = (salary_from + salary_to) / 2
    elif salary_from:
        avg_salary = salary_from * 1.2
    elif salary_to:
        avg_salary = salary_to * 0.8

    return avg_salary
