# 1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать, вновь выполнить замеры и
# ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
from timeit import timeit


def my_func():
    seasons_dict = {1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter'}
    month = 6
    if 2 < month < 6:
        (seasons_dict.get(1))
    elif 5 < month < 9:
        (seasons_dict.get(2))
    elif 8 < month < 12:
        (seasons_dict.get(3))
    elif 0 < month < 3 or month == 12:
        (seasons_dict.get(4))


def my_func1():
    seasons_list = ['spring', 'summer', 'autumn', 'winter']
    month = 6
    if 2 < month < 6:
        (seasons_list[0])
    elif 5 < month < 9:
        (seasons_list[1])
    elif 8 < month < 12:
        (seasons_list[2])
    elif 0 < month < 3 or month == 12:
        (seasons_list[3])


print(timeit("my_func()", "from __main__ import my_func", number=1000000))
print(timeit("my_func1()", "from __main__ import my_func1", number=1000000))

'''
Первый вариант задачи сделал через словарь, по времени получилось 0.5778304999985266
Второй вариант задачи сделал через список, по времени получилось 0.35221440000168514
Благодаря решению через список удалось ускориться на ~ 60%
'''
