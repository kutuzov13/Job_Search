import requests


def search_vacancies_programmer(program_lang):
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': f'Программист {program_lang}',
              'area': 1}
    response = requests.get('https://api.hh.ru/vacancies', params=params, headers=headers)
    return response.json()['found']


def search_by_salary():
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': 'Программист Python',
              'area': 1,
              'only_with_salary': 'true'}
    response = requests.get('https://api.hh.ru/vacancies/', params=params, headers=headers)
    for vacancy in response.json()['items']:
        print(vacancy['salary'])


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


search_by_salary()