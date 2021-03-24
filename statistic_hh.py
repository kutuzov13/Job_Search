import statistics
from itertools import count

import requests

from utils import predict_salary


def fetch_records(program_lang):
    api_hh = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    id_moscow = 1
    salaries = []

    for page in count():
        params = {'text': f'Программист {program_lang}',
                  'page': page,
                  'area': id_moscow,
                  'only_with_salary': 'true'}
        page_response = requests.get(api_hh, params=params, headers=headers)
        page_response.raise_for_status()
        page_data = page_response.json()

        if page >= page_data['pages']:
            break

        for vacancy in page_data['items']:
            if vacancy['salary']['currency'] == 'RUR':

                salaries.append(int(predict_salary(vacancy['salary']['from'], vacancy['salary']['to'])))
    return salaries


def search_vacancies_programmer(program_lang):
    api_hh = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': f'Программист {program_lang}',
              'area': 1}
    response = requests.get(api_hh, params=params, headers=headers)
    response.raise_for_status()
    return response.json()['found']


def get_statistic_hh(programmer_languages):
    statistics_vacancy = {}

    for program_language in programmer_languages:
        statistics_vacancy[program_language] = {'vacancies_found': search_vacancies_programmer(program_language),
                                                'vacancies_processed': len(fetch_records(program_language)),
                                                'average_salary': int(statistics.mean(fetch_records(program_language)))}
    return statistics_vacancy
