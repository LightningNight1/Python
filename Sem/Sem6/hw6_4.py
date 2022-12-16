# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать, вновь выполнить замеры и ОПИСАТЬ
# СЛОВАМИ, что вы сделали и чего удалось добиться
# Нахождение факториала
from memory_profiler import profile
import math


@profile
def find_fact_cycle():
    num = 1000
    fact = 1
    for i in range(2, num+1):
        fact *= i


find_fact_cycle()

#############################


@profile
def fact():
    n = 1000
    print(math.factorial(n))


fact()


'''
Первый вариант задачи сделал через цикл for, по использованию памяти получилось 46.5 MiB.
Второй вариант задачи сделал через встроенный модуль math.factorial, по использованию памяти получилось 46.5 MiB.
Разницы между замерами памяти нет.

find_fact_cycle() - 
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     46.5 MiB     46.5 MiB           1   @profile
     6                                         def find_fact_cycle():
     7     46.5 MiB      0.0 MiB           1       num = 1000
     8     46.5 MiB      0.0 MiB           1       fact = 1
     9     46.5 MiB      0.0 MiB        1000       for i in range(2, num+1):
    10     46.5 MiB      0.0 MiB         999           fact *= i


fact()
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     46.5 MiB     46.5 MiB           1   @profile
    17                                         def fact():
    18     46.5 MiB      0.0 MiB           1       n = 1000
    19     46.5 MiB      0.0 MiB           1       print(math.factorial(n))    
'''
