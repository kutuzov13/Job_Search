from terminaltable import get_table_data, create_table
from statistic_hh import get_statistic_hh
from statistic_sj import get_statistic_sj

from dotenv import load_dotenv

PROGRAMMING_LANGUAGES = ['JavaScript',
                         'Java',
                         'Python',
                         'Ruby',
                         'PHP',
                         'C++',
                         'C#',
                         'C',
                         'Go',
                         'Swift']


def main():
    load_dotenv()
    print('Wait for the data to be received...')

    hh_info = get_statistic_hh(PROGRAMMING_LANGUAGES)
    sj_info = get_statistic_sj(PROGRAMMING_LANGUAGES)

    hh_table_data = get_table_data(hh_info)
    sj_table_data = get_table_data(sj_info)

    hh_table = create_table(hh_table_data, 'HeadHunter Moscow')
    sj_table = create_table(sj_table_data, 'SuperJob Moscow')

    print(hh_table.table)
    print()
    print(sj_table.table)


if __name__ == '__main__':
    main()
