import os
import statistics
from itertools import count

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_SUPER_JOB = os.getenv('TOKEN_SUPER_JOB')


def fetch_records(program_lang):
    api_super_job = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': TOKEN_SUPER_JOB}
    for page in count(0):
        params = {'town': 4,
                  'page': page,
                  'keyword': f'Программист {program_lang}'}

        response = requests.get(api_super_job, params=params, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        total = page_data['total']
        pages = total

        if page >= pages:
            break

        yield from page_data['objects']


def search_vacancies_programmer(program_lang):
    api_hh = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': TOKEN_SUPER_JOB}
    params = {'town': 4,
              'keyword': f'Программист {program_lang}'}
    response = requests.get(api_hh, params=params, headers=headers)
    response.raise_for_status()

    return response.json()['total']


def predict_salary(salary_from, salary_to):
    if salary_from != 0 and salary_to != 0:
        return int(salary_from + salary_to / 2)
    elif salary_from == 0 and salary_to != 0:
        return salary_to * 1.2
    elif salary_from != 0 and salary_to == 0:
        return salary_from * 0.8
    else:
        pass


def vacancies_processed(program_lang):
    ls = []
    for vacancy in fetch_records(program_lang):
        avg = predict_salary(vacancy['payment_from'], vacancy['payment_to'])
        ls.append(avg)
    return len([processed for processed in ls if processed is not None])


def get_avg_salary(program_lang):
    ls = []
    for vacancy in fetch_records(program_lang):
        avg = predict_salary(vacancy['payment_from'], vacancy['payment_to'])
        ls.append(avg)
    return int(statistics.mean([avg_salary for avg_salary in ls if avg_salary is not None]))


def get_statistic_sj(programmer_languages):
    statistics_vacancy = {}

    for program_language in programmer_languages:
        statistics_vacancy[program_language] = {'vacancies_found': search_vacancies_programmer(program_language),
                                                'vacancies_processed': vacancies_processed(program_language),
                                                'average_salary': get_avg_salary(program_language)}
    return statistics_vacancy

