# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать, вновь выполнить замеры и ОПИСАТЬ
# СЛОВАМИ, что вы сделали и чего удалось добиться
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
from memory_profiler import profile


@profile
def my_func():
    k = 100000
    fibo = [0, 1]
    negafibo = [0, 1]
    for i in range(2, k + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])
        negafibo.append(negafibo[i - 2] - negafibo[i - 1])
    negafibo.reverse()
    negafibo.remove(0)
    negafibo.extend(fibo)


@profile
def my_func1():
    k = 100000
    if k == 0:
        fib_list = [0]
    else:
        fib_list = [1, 0, 1]
    for el in range(1, k):
        fib_list.insert(0, fib_list[1] - fib_list[0])
        fib_list.append(fib_list[-1] + fib_list[-2])


my_func()
my_func1()

'''
Разница между замерами памяти составила ~ 5 MiB (970.2 MiB / 975.6 MiB)

my_func
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     46.2 MiB     46.2 MiB           1   @profile
     5                                         def my_func():
     6     46.2 MiB      0.0 MiB           1       k = 100000
     7     46.2 MiB      0.0 MiB           1       if k == 0:
     8                                                 fib_list = [0]
     9                                             else:
    10     46.2 MiB      0.0 MiB           1           fib_list = [1, 0, 1]
    11    970.2 MiB     -1.6 MiB      100000       for el in range(1, k):
    12    970.2 MiB    456.1 MiB       99999           fib_list.insert(0, fib_list[1] - fib_list[0])
    13    970.2 MiB    464.6 MiB       99999           fib_list.append(fib_list[-1] + fib_list[-2])



my_func1
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     50.3 MiB     50.3 MiB           1   @profile
    17                                         def my_func1():
    18     50.3 MiB      0.0 MiB           1       k = 100000
    19     50.3 MiB      0.0 MiB           1       fibo = [0, 1]
    20     50.3 MiB      0.0 MiB           1       negafibo = [0, 1]
    21    974.1 MiB     -3.4 MiB      100000       for i in range(2, k + 1):
    22    974.1 MiB    441.1 MiB       99999           fibo.append(fibo[i - 1] + fibo[i - 2])
    23    974.1 MiB    475.0 MiB       99999           negafibo.append(negafibo[i - 2] - negafibo[i - 1])
    24    974.1 MiB      0.0 MiB           1       negafibo.reverse()
    25    974.1 MiB      0.0 MiB           1       negafibo.remove(0)
    26    975.6 MiB      1.5 MiB           1       negafibo.extend(fibo)
    '''
