import statistics
from itertools import count

import requests

from utils import predict_salary


def fetch_records(program_lang):
    head_hunter_api = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    moscow_id = 1
    salaries = []

    for page in count(0):
        params = {'text': f'Программист {program_lang}',
                  'page': page,
                  'area': moscow_id,
                  'only_with_salary': 'true'}

        page_response = requests.get(head_hunter_api, params=params, headers=headers)
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
    id_moscow = 1

    params = {'text': f'Программист {program_lang}',
              'area': id_moscow}

    response = requests.get(api_hh, params=params, headers=headers)
    response.raise_for_status()

    return response.json()['found']


def get_statistic_hh(programmer_languages):
    job_statistics = {}

    for program_language in programmer_languages:
        vacancies_found = search_vacancies_programmer(program_language)
        vacancies_processed = len(fetch_records(program_language))
        avg_salary = int(statistics.mean(fetch_records(program_language)))

        job_statistics[program_language] = {'vacancies_found': vacancies_found,
                                                'vacancies_processed': vacancies_processed,
                                                'average_salary': avg_salary}
    return job_statistics
