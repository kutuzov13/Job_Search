import os
import statistics
from itertools import count

import requests

from utils import predict_salary


def fetch_records(program_lang):
    super_job_token = os.getenv('TOKEN_SUPER_JOB')
    super_job_api = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': super_job_token}
    salaries = []

    for page in count(0):
        params = {'town': 'Москва',
                  'page': page,
                  'keyword': f'Программист {program_lang}'}

        response = requests.get(super_job_api, params=params, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        total = page_data['total']

        if page >= total:
            break

        for vacancy in page_data['objects']:
            salaries.append(predict_salary(int(vacancy['payment_from']), int(vacancy['payment_to'])))
    return list(filter(None, salaries))


def search_vacancies_programmer(program_lang):
    token_super_job = os.getenv('TOKEN_SUPER_JOB')

    super_job_token = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': token_super_job}
    params = {'town': 'Москва',
              'keyword': f'Программист {program_lang}'}

    response = requests.get(super_job_token, params=params, headers=headers)
    response.raise_for_status()

    return response.json()['total']


def get_statistic_sj(programmer_languages):
    job_statistics = {}

    for program_language in programmer_languages:
        vacancies_found = search_vacancies_programmer(program_language)
        vacancies_processed = len(fetch_records(program_language))
        avg_salary = int(statistics.mean(fetch_records(program_language)))

        job_statistics[program_language] = {'vacancies_found': vacancies_found,
                                                'vacancies_processed': vacancies_processed,
                                                'average_salary': avg_salary}
    return job_statistics
