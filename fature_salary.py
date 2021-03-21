from dotenv import load_dotenv

from terminaltable import get_table_data, create_table
from statistic_hh import statistic_hh
from statistic_sj import statistic_sj


def main():
    load_dotenv()
    print('Выполняется...')

    hh_info = statistic_hh()
    sj_info = statistic_sj()

    hh_table_data = get_table_data(hh_info)
    sj_table_data = get_table_data(sj_info)

    hh_table = create_table(hh_table_data, 'HeadHunter Moscow')
    sj_table = create_table(sj_table_data, 'SuperJob Moscow')

    print(hh_table.table)
    print()
    print(sj_table.table)


if __name__ == '__main__':
    main()
