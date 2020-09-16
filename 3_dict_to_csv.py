"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

list_of_dicts = [{'name': 'Иван', 'age': 25, 'job': 'электрик'},
                 {'name': 'Галя', 'age': 44, 'job': 'бухгалтер'},
                 {'name': 'Валерий', 'age': 54, 'job': 'летчик-испытатель'},
                 {'name': 'Кирилл', 'age': 29, 'job': 'безработный'}]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('vot_eti_rebyata.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for row in list_of_dicts:
            writer.writerow(row)


if __name__ == "__main__":
    main()
