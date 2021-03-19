import statistics

import requests


def search_vacancies_programmer(program_lang):
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': f'Программист {program_lang}',
              'area': 1}
    response = requests.get('https://api.hh.ru/vacancies', params=params, headers=headers)
    return response.json()['found']


def predict_rub_salary(program_lang):
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': f'Программист {program_lang}',
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


programmer_languages = {'JavaScript': {'vacancies_found': search_vacancies_programmer('JavaScript'),
                                       'vacancies_processed': len(predict_rub_salary('JavaScript')),
                                       'average_salary': int(statistics.mean(predict_rub_salary('JavaScript')))},
                        'Java': {'vacancies_found': search_vacancies_programmer('Java'),
                                 'vacancies_processed': len(predict_rub_salary('Java')),
                                 'average_salary': int(statistics.mean(predict_rub_salary('Java')))},
                        'Python': {'vacancies_found': search_vacancies_programmer('Python'),
                                   'vacancies_processed': len(predict_rub_salary('Python')),
                                   'average_salary': int(statistics.mean(predict_rub_salary('Python')))},
                        'Ruby:': {'vacancies_found': search_vacancies_programmer('Ruby'),
                                  'vacancies_processed': len(predict_rub_salary('Ruby')),
                                  'average_salary': int(statistics.mean(predict_rub_salary('Ruby')))},
                        'PHP': {'vacancies_found': search_vacancies_programmer('PHP'),
                                'vacancies_processed': len(predict_rub_salary('PHP')),
                                'average_salary': int(statistics.mean(predict_rub_salary('PHP')))},
                        'C++': {'vacancies_found': search_vacancies_programmer('C++'),
                                'vacancies_processed': len(predict_rub_salary('C++')),
                                'average_salary': int(statistics.mean(predict_rub_salary('C++')))},
                        'C#': {'vacancies_found': search_vacancies_programmer('C#'),
                               'vacancies_processed': len(predict_rub_salary('C#')),
                               'average_salary': int(statistics.mean(predict_rub_salary('C#')))},
                        'C': {'vacancies_found': search_vacancies_programmer('C'),
                              'vacancies_processed': len(predict_rub_salary('C')),
                              'average_salary': int(statistics.mean(predict_rub_salary('C')))},
                        'Go': {'vacancies_found': search_vacancies_programmer('Go'),
                               'vacancies_processed': len(predict_rub_salary('Go')),
                               'average_salary': int(statistics.mean(predict_rub_salary('Go')))},
                        'Shell': {'vacancies_found': search_vacancies_programmer('Shell'),
                                  'vacancies_processed': len(predict_rub_salary('Shell')),
                                  'average_salary': int(statistics.mean(predict_rub_salary('Shell')))}}


if __name__ == '__main__':
    print(programmer_languages)
