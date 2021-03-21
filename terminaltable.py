from terminaltables import AsciiTable


# TABLE_DATA = (
#     ('Programmer Language', 'Jobs found', 'Vacancies processed', 'Average Salary'),
#     ('0', '2007-2009', 'The Golf Mk5 Variant was\nintroduced in 2007.', '4')
# )
#
#
#
# def main():
#     """Main function."""
#     title = 'Head Hunter Moscow'
#
#     # AsciiTable.
#     table_instance = AsciiTable(TABLE_DATA, title)
#     table_instance.justify_columns[2] = 'right'
#     print(table_instance.table)
#     print()


def get_table_data(data):
    table_data = []

    for lang, info in data.items():
        row = [lang, info['vacancies_found'], info['vacancies_processed'], info['average_salary']]
        table_data.append(row)

    return table_data


def create_table(table_data, title):
    header = ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']
    table_data.insert(0, header)
    table = AsciiTable(table_data)
    table.title = title

    return table