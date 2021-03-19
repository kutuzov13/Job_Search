import os

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_SUPER_JOB = os.getenv('TOKEN_SUPER_JOB')


def vacancy_name(token):
    api_super_job = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': token}
    params = {'town': 'Москва',
              'keyword': 'Программист'}

    response = requests.get(api_super_job, params=params, headers=headers)
    response.raise_for_status()

    vacancies_programmers = response.json()['objects']
    for data in vacancies_programmers:
        print(f'{data["profession"]}, {data["town"]["title"]}, от: {data["payment_from"]} до {data["payment_to"]}')


def predict_rub_salary_for_sj(token):
    api_super_job = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {'X-Api-App-Id': token}
    params = {'town': 'Москва',
              'keyword': 'Программист'}

    response = requests.get(api_super_job, params=params, headers=headers)
    response.raise_for_status()

    vacancies_programmers = response.json()['objects']
    for data in vacancies_programmers:
        print(f'{data["profession"]}, {data["town"]["title"]}, от: {data["payment_from"]} до {data["payment_to"]}')


predict_rub_salary_for_sj(TOKEN_SUPER_JOB)