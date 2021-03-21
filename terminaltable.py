from terminaltables import AsciiTable


def get_table_data(data):
    table_data = []

    for lang, info in data.items():
        row = [lang, info['vacancies_found'], info['vacancies_processed'], info['average_salary']]
        table_data.append(row)

    return table_data


def create_table(table_data, title):
    header = ['Programmer Languages', 'Jobs found', 'Vacancies processed', 'Average Salary']
    table_data.insert(0, header)
    table = AsciiTable(table_data)
    table.title = title

    return table