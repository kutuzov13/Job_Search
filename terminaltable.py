from typing import List

from terminaltables import AsciiTable


def get_table_data(data_vacancies: dict) -> List:
    table_data = []

    for lang, statistics in data_vacancies.items():
        row = [lang, statistics['vacancies_found'], statistics['vacancies_processed'], statistics['average_salary']]
        table_data.append(row)

    return table_data


def create_table(table_data: list, title):
    header = ['Programmer Languages', 'Jobs found', 'Vacancies processed', 'Average Salary']
    table_data.insert(0, header)
    table = AsciiTable(table_data)
    table.title = title

    return table
