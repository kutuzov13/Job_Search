"""Get statistics of programmer vacancies from the HeadHunter website."""

import statistics
from itertools import count
from typing import Dict, Tuple

import requests
from utils import predict_salary

MOSCOW_ID = 1


def fetch_vacancies(program_lang: str) -> Tuple:
    """Get an average salary depending on the programming language and the number of jobs."""
    head_hunter_api = 'https://api.hh.ru/vacancies'
    headers = {'User-Agent': 'HH-User-Agent'}
    payload = {
        'text': f'Программист {program_lang}',
        'area': MOSCOW_ID,
        'only_with_salary': 'true',
    }

    salaries = []
    for page in count(0):
        payload['pages'] = page
        response = requests.get(head_hunter_api, params=payload, headers=headers)
        response.raise_for_status()
        page_data = response.json()
        vacancies_found = page_data['found']

        if page >= page_data['pages']:
            break

        for vacancy in page_data['items']:
            if vacancy['salary']['currency'] == 'RUR':
                salaries.append(int(predict_salary(vacancy['salary']['from'], vacancy['salary']['to'])))

    return salaries, vacancies_found


def get_statistic_hh(programmer_languages: list) -> Dict:
    """Get job statistics for a programming language."""
    job_statistics = {}

    for program_language in programmer_languages:
        salaries, vacancies_found = fetch_vacancies(program_language)

        job_statistics[program_language] = {
            'vacancies_found': vacancies_found,
            'vacancies_processed': len(salaries),
            'average_salary': int(statistics.mean(salaries)),
        }
    return job_statistics
