import requests


def search_vacancies_programmer():
    headers = {'User-Agent': 'HH-User-Agent'}
    params = {'text': 'NAME:Программист',
              'area': 1}
    response = requests.get('https://api.hh.ru/vacancies', params=params, headers=headers).json()['items']
    return response
