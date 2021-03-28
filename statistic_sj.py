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
        next_pages = page_data['more']

        for vacancy in page_data['objects']:
            salaries.append(predict_salary(int(vacancy['payment_from']), int(vacancy['payment_to'])))
        if not next_pages:
            break
    return list(filter(None, salaries))


def search_vacancies_programmer(token, program_lang):

    super_job_token = 'https://api.superjob.ru/2.0/vacancies/'

    headers = {'X-Api-App-Id': token}

    params = {'town': 'Москва',
              'keyword': f'Программист {program_lang}'}

    response = requests.get(super_job_token, params=params, headers=headers)
    response.raise_for_status()

    return response.json()['total']


def get_statistic_sj(programmer_languages):
    super_job_token = os.getenv('TOKEN_SUPER_JOB')

    job_statistics = {}

    for program_language in programmer_languages:
        vacancies_found = search_vacancies_programmer(super_job_token, program_language)
        vacancies_processed = len(fetch_vacancies(super_job_token, program_language))
        avg_salary = int(statistics.mean(fetch_vacancies(super_job_token, program_language)))

        job_statistics[program_language] = {'vacancies_found': vacancies_found,
                                            'vacancies_processed': vacancies_processed,
                                            'average_salary': avg_salary}
    return job_statistics
