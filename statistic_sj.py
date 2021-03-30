import statistics
from itertools import count

import requests

from utils import predict_salary


def fetch_vacancies(token, program_lang):
    super_job_api = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': token}
    params = {'town': 'Москва',
              'keyword': f'Программист {program_lang}'}

    salaries = []
    for page in count(0):
        params['page'] = page

        response = requests.get(super_job_api, params=params, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        vacancies_found = page_data['total']
        next_pages = page_data['more']

        for vacancy in page_data['objects']:
            salaries.append(predict_salary(int(vacancy['payment_from']), int(vacancy['payment_to'])))
        if not next_pages:
            break

    return list(filter(None, salaries)), vacancies_found


def get_statistic_sj(super_job_token, programmer_languages):
    job_statistics = {}

    for program_language in programmer_languages:
        salaries, vacancies_found = fetch_vacancies(super_job_token, program_language)
        job_statistics[program_language] = {'vacancies_found': vacancies_found,
                                            'vacancies_processed': len(salaries),
                                            'average_salary': int(statistics.mean(salaries))}
    return job_statistics
