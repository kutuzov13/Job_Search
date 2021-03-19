import os

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_SUPER_JOB = os.getenv('TOKEN_SUPER_JOB')


def predict_rub_salary_for_sj(token, program_language):
    api_super_job = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': token}
    params = {'town': 'Москва',
              'keyword': f'Программист {program_language}'}

    response = requests.get(api_super_job, params=params, headers=headers)
    response.raise_for_status()

    yield from response.json()['objects']


def predict_salary(salary_from, salary_to):
    if salary_from != 0 and salary_to != 0:
        return int(salary_from + salary_to / 2)
    elif salary_from == 0 and salary_to != 0:
        return salary_to
    elif salary_from != 0 and salary_to == 0:
        return salary_from
    else:
        pass


if __name__ == '__main__':
    for i in predict_rub_salary_for_sj(TOKEN_SUPER_JOB, 'Python'):
        print(predict_salary(i['payment_from'], i['payment_to']))
