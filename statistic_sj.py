import os
import statistics
from itertools import count

import requests

from utils import predict_salary


def fetch_vacancies(token, program_lang):

    super_job_api = 'https://api.superjob.ru/2.0/vacancies/'

    headers = {'X-Api-App-Id': token}

    salaries = []

    for page in count(0):
        params = {'town': 'Москва',
                  'page': page,
                  'keyword': f'Программист {program_lang}'}

        response = requests.get(super_job_api, params=params, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        total_vacancy = response.json()['total']
        next_pages = page_data['more']

        for vacancy in page_data['objects']:
            salaries.append(predict_salary(int(vacancy['payment_from']), int(vacancy['payment_to'])))
        if not next_pages:
            break

    return list(filter(None, salaries)), total_vacancy


def get_statistic_sj(programmer_languages):
    super_job_token = os.getenv('TOKEN_SUPER_JOB')

    job_statistics = {}

    for program_language in programmer_languages:
        data_vacancy = fetch_vacancies(super_job_token, program_language)
        job_statistics[program_language] = {'vacancies_found': data_vacancy[1],
                                            'vacancies_processed': len(data_vacancy[0]),
                                            'average_salary': int(statistics.mean(data_vacancy[0]))}
    return job_statistics
