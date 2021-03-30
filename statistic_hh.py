import statistics
from itertools import count

import requests

from utils import predict_salary


def fetch_vacancies(program_lang):
    moscow_id = 1
    head_hunter_api = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': f'Программист {program_lang}',
              'area': moscow_id,
              'only_with_salary': 'true'}

    salaries = []
    for page in count(0):
        params['pages'] = page
        response = requests.get(head_hunter_api, params=params, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        vacancies_found = response.json()['found']

        if page >= page_data['pages']:
            break

        for vacancy in page_data['items']:
            if vacancy['salary']['currency'] == 'RUR':
                salaries.append(int(predict_salary(vacancy['salary']['from'], vacancy['salary']['to'])))

    return salaries, vacancies_found


def get_statistic_hh(programmer_languages):
    job_statistics = {}

    for program_language in programmer_languages:
        salaries, vacancies_found = fetch_vacancies(program_language)

        job_statistics[program_language] = {'vacancies_found': vacancies_found,
                                            'vacancies_processed': len(salaries),
                                            'average_salary': int(statistics.mean(salaries))}
    return job_statistics
