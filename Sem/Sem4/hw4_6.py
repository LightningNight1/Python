# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
from itertools import cycle


def my_count_func(start_num, final_num):
    for el in count(start_num):
        if el > final_num:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    iter1 = cycle(my_list)
    while i < iteration:
        print(next(iter1))
        i += 1


my_count_func(start_num=int(input('Enter the starting number: ')),
              final_num=int(input('Enter the final number: ')))
my_cycle_func(my_list=[3, 2, 1], iteration=int(
    input('Enter the number of iterations: ')))
