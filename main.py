import requests


def search_vacancies_programmer(program_lang):
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': f'Программист {program_lang}',
              'area': 1}
    response = requests.get('https://api.hh.ru/vacancies', params=params, headers=headers)
    return response.json()['found']


def predict_rub_salary(name_vacancy):
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': name_vacancy,
              'area': 1,
              'only_with_salary': 'true'}
    response = requests.get(f'https://api.hh.ru/vacancies/', params=params, headers=headers)
    salary_from_to = response.json()['items']
    expected_salary = []
    for vacancy in salary_from_to:
        if vacancy['salary']['from'] and vacancy['salary']['to'] and vacancy['salary']['currency'] == 'RUR':
            expected_salary.append((vacancy['salary']['from'] + vacancy['salary']['to']) / 2)
            if vacancy['salary']['from'] and vacancy['salary']['to'] is None:
                expected_salary.append(vacancy['salary']['from'] * 1.2)
                if vacancy['salary']['to'] and vacancy['salary']['from'] is None:
                    expected_salary.append(vacancy['salary']['to'] * 0.8)
    return expected_salary


programmer_languages = {'JavaScript': search_vacancies_programmer('JavaScript'),
                        'Java': search_vacancies_programmer('Java'),
                        'Python': search_vacancies_programmer('Python'),
                        'Ruby:': search_vacancies_programmer('Ruby'),
                        'PHP': search_vacancies_programmer('PHP'),
                        'C++': search_vacancies_programmer('C++'),
                        'C#': search_vacancies_programmer('C#'),
                        'C': search_vacancies_programmer('C'),
                        'Go': search_vacancies_programmer('Go'),
                        'Shell': search_vacancies_programmer('Shell')}


for i in predict_rub_salary('Программист Python'):
    print(i)
