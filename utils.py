def predict_salary(salary_from, salary_to):
    if salary_from != 0 and salary_to != 0:
        return int(salary_from + salary_to / 2)
    elif salary_from == 0 and salary_to != 0:
        return salary_to * 1.2
    elif salary_from != 0 and salary_to == 0:
        return salary_from * 0.8
