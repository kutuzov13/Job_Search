import statistics
from itertools import count

import requests


def fetch_records(program_lang):
    url = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    for page in count():
        params = {'text': f'Программист {program_lang}',
                  'page': page,
                  'area': 1,
                  'only_with_salary': 'true'}
        page_response = requests.get(url, params=params, headers=headers)
        page_response.raise_for_status()
        page_data = page_response.json()
        if page >= page_data['pages']:
            break
        yield from page_data['items']


def search_vacancies_programmer(program_lang):
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': f'Программист {program_lang}',
              'area': 1}
    response = requests.get('https://api.hh.ru/vacancies', params=params, headers=headers)
    response.raise_for_status()
    return response.json()['found']


def predict_rub_salary(salary):
    if salary['from'] and salary['to'] and salary['currency'] == 'RUR':
        return salary['from'] + salary['to'] / 2
    if salary['from'] and salary['to'] is None and salary['currency'] == 'RUR':
        return salary['from'] * 1.2
    if salary['to'] and salary['from'] is None and salary['currency'] == 'RUR':
        return salary['to'] * 0.8
    else:
        pass


def vacancies_processed(program_lang):
    number_vacancies = [predict_rub_salary(vacancy['salary']) for vacancy in fetch_records(program_lang)]
    return len([processed for processed in number_vacancies if processed is not None])


def get_avg_salary(program_lang):
    avg_salaries = [predict_rub_salary(salary['salary']) for salary in fetch_records(program_lang)]
    return int(statistics.mean([avg_salary for avg_salary in avg_salaries if avg_salary is not None]))


top_programmer_languages = {'JavaScript': {'vacancies_found': search_vacancies_programmer('JavaScript'),
                                           'vacancies_processed': vacancies_processed('JavaScript'),
                                           'average_salary': get_avg_salary('JavaScript')},
                            'Java': {'vacancies_found': search_vacancies_programmer('Java'),
                                     'vacancies_processed': vacancies_processed('Java'),
                                     'average_salary': get_avg_salary('Java')},
                            'Python': {'vacancies_found': search_vacancies_programmer('Python'),
                                       'vacancies_processed': vacancies_processed('Python'),
                                       'average_salary': get_avg_salary('Python')},
                            'Ruby:': {'vacancies_found': search_vacancies_programmer('Ruby'),
                                      'vacancies_processed': vacancies_processed('Ruby'),
                                      'average_salary': get_avg_salary('Ruby')},
                            'PHP': {'vacancies_found': search_vacancies_programmer('PHP'),
                                    'vacancies_processed': vacancies_processed('PHP'),
                                    'average_salary': get_avg_salary('PHP')},
                            'C++': {'vacancies_found': search_vacancies_programmer('C++'),
                                    'vacancies_processed': vacancies_processed('C++'),
                                    'average_salary': get_avg_salary('C++')},
                            'C#': {'vacancies_found': search_vacancies_programmer('C#'),
                                   'vacancies_processed': vacancies_processed('C#'),
                                   'average_salary': get_avg_salary('C#')},
                            'C': {'vacancies_found': search_vacancies_programmer('C'),
                                  'vacancies_processed': vacancies_processed('C'),
                                  'average_salary': get_avg_salary('C')},
                            'Go': {'vacancies_found': search_vacancies_programmer('Go'),
                                   'vacancies_processed': vacancies_processed('Go'),
                                   'average_salary': get_avg_salary('Go')},
                            'Shell': {'vacancies_found': search_vacancies_programmer('Shell'),
                                      'vacancies_processed': vacancies_processed('Shell'),
                                      'average_salary': get_avg_salary('Shell')}}

if __name__ == '__main__':
    print(top_programmer_languages)
