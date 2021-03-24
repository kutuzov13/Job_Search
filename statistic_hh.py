import statistics
from itertools import count

import requests


def fetch_records(program_lang):
    api_hh = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    for page in count():
        params = {'text': f'Программист {program_lang}',
                  'page': page,
                  'area': 1,
                  'only_with_salary': 'true'}
        page_response = requests.get(api_hh, params=params, headers=headers)
        page_response.raise_for_status()
        page_data = page_response.json()
        if page >= page_data['pages']:
            break
        yield from page_data['items']


def search_vacancies_programmer(program_lang):
    api_hh = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': f'Программист {program_lang}',
              'area': 1}
    response = requests.get(api_hh, params=params, headers=headers)
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


def get_statistic_hh():
    statistics_vacancy = {}
    top_programmer_languages = ['JavaScript',
                                'Java',
                                'Python',
                                'Ruby',
                                'PHP',
                                'C++',
                                'C#',
                                'C',
                                'Go',
                                'Swift']
    for program_language in top_programmer_languages:
        statistics_vacancy[program_language] = {'vacancies_found': search_vacancies_programmer(program_language),
                                                'vacancies_processed': vacancies_processed(program_language),
                                                'average_salary': get_avg_salary(program_language)}
    return statistics_vacancy


if __name__ == '__main__':
    print(get_statistic_hh())
