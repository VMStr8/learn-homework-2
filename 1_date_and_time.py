"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    day_ago = timedelta(days=1)
    month_ago = timedelta(days=30)

    today = dt_now.strftime('%d.%m.%Y %H:%M')

    yesterday = dt_now - day_ago
    last_month = dt_now - month_ago
    print(today)
    print(yesterday.strftime('%d.%m.%Y %H:%M'))
    print(last_month.strftime('%d.%m.%Y %H:%M'))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_string


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
