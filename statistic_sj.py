import os
import statistics
from itertools import count

import requests

from utils import predict_salary


def fetch_records(program_lang):
    super_job_token = os.getenv('TOKEN_SUPER_JOB')
    api_super_job = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': super_job_token}
    salaries = []

    for page in count(0):
        params = {'town': 'Москва',
                  'page': page,
                  'keyword': f'Программист {program_lang}'}

        response = requests.get(api_super_job, params=params, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        total = page_data['total']

        if page >= total:
            break

        for vacancy in page_data['objects']:
            salaries.append(predict_salary(int(vacancy['payment_from']), int(vacancy['payment_to'])))
    return [avg_salary for avg_salary in salaries if avg_salary is not None]


def search_vacancies_programmer(program_lang):
    token_super_job = os.getenv('TOKEN_SUPER_JOB')

    api_super_job = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': token_super_job}
    params = {'town': 'Москва',
              'keyword': f'Программист {program_lang}'}

    response = requests.get(api_super_job, params=params, headers=headers)
    response.raise_for_status()

    return response.json()['total']


def get_statistic_sj(programmer_languages):
    statistics_vacancy = {}

    for program_language in programmer_languages:
        statistics_vacancy[program_language] = {'vacancies_found': search_vacancies_programmer(program_language),
                                                'vacancies_processed': len(fetch_records(program_language)),
                                                'average_salary': int(statistics.mean(fetch_records(program_language)))}
    return statistics_vacancy
