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


def predict_rub_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return salary_from + salary_to / 2
    if salary_from and salary_to is None:
        return salary_from * 1.2
    if salary_to and salary_from is None:
        return salary_to * 0.8


def vacancies_processed(program_lang):
    number_vacancies = [predict_rub_salary(salary['salary']['from'], salary['salary']['to']) for salary in fetch_records(program_lang)]
    return len([processed for processed in number_vacancies if processed is not None])


def get_avg_salary(program_lang):
    avg_salaries = [predict_rub_salary(salary['salary']['from'], salary['salary']['to']) for salary in fetch_records(program_lang)]
    return int(statistics.mean([avg_salary for avg_salary in avg_salaries if avg_salary is not None]))


def get_statistic_hh(programmer_languages):
    statistics_vacancy = {}

    for program_language in programmer_languages:
        statistics_vacancy[program_language] = {'vacancies_found': search_vacancies_programmer(program_language),
                                                'vacancies_processed': vacancies_processed(program_language),
                                                'average_salary': get_avg_salary(program_language)}
    return statistics_vacancy

