# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать, вновь выполнить замеры и ОПИСАТЬ
# СЛОВАМИ, что вы сделали и чего удалось добиться
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
from memory_profiler import profile


@profile
def my_func1():
    n = 100000
    i = fibo_0 = 0
    fibo_1 = fibo_2 = fibo_n2 = 1
    fibo_n1 = -1
    fibo_list = [fibo_n1, fibo_1, fibo_0, fibo_1, fibo_2]
    while i < n - 2:
        fibo_sum = fibo_1 + fibo_2
        negafibo_sum = fibo_n2 - fibo_n1
        fibo_1 = fibo_2
        fibo_2 = fibo_sum
        fibo_n2 = fibo_n1
        fibo_n1 = negafibo_sum
        fibo_list.append(fibo_sum)
        fibo_list.insert(0, negafibo_sum)
        i = i + 1


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


my_func1()
my_func()

'''
Первый вариант задачи сделал через цикл while, по использованию памяти получилось 973.3 MiB.
Второй вариант задачи сделал через цикл for, по использованию памяти получилось 972.1 MiB.
Благодаря решению через цикл for удалось сэкономить ~ 1 MiB

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    20     50.0 MiB     50.0 MiB           1   @profile
    21                                         def my_func1():
    22     50.0 MiB      0.0 MiB           1       n = 100000
    23     50.0 MiB      0.0 MiB           1       i = fibo_0 = 0
    24     50.0 MiB      0.0 MiB           1       fibo_1 = fibo_2 = fibo_n2 = 1
    25     50.0 MiB      0.0 MiB           1       fibo_n1 = -1
    26     50.0 MiB      0.0 MiB           1       fibo_list = [fibo_n1, fibo_1, fibo_0, fibo_1, fibo_2]
    27    973.3 MiB     -2.8 MiB       99999       while i < n - 2:
    28    973.3 MiB    470.4 MiB       99998           fibo_sum = fibo_1 + fibo_2
    29    973.3 MiB    437.3 MiB       99998           negafibo_sum = fibo_n2 - fibo_n1
    30    973.3 MiB     -2.6 MiB       99998           fibo_1 = fibo_2
    31    973.3 MiB     -2.8 MiB       99998           fibo_2 = fibo_sum
    32    973.3 MiB     -2.8 MiB       99998           fibo_n2 = fibo_n1
    33    973.3 MiB     -2.8 MiB       99998           fibo_n1 = negafibo_sum
    34    973.3 MiB     -2.8 MiB       99998           fibo_list.append(fibo_sum)
    35    973.3 MiB      7.2 MiB       99998           fibo_list.insert(0, negafibo_sum)
    36    973.3 MiB     -2.8 MiB       99998           i = i + 1


    Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     46.4 MiB     46.4 MiB           1   @profile
     8                                         def my_func():
     9     46.4 MiB      0.0 MiB           1       k = 100000
    10     46.4 MiB      0.0 MiB           1       fibo = [0, 1]
    11     46.4 MiB      0.0 MiB           1       negafibo = [0, 1]
    12    970.6 MiB     -3.4 MiB      100000       for i in range(2, k + 1):
    13    970.6 MiB    449.8 MiB       99999           fibo.append(fibo[i - 1] + fibo[i - 2])
    14    970.6 MiB    468.0 MiB       99999           negafibo.append(negafibo[i - 2] - negafibo[i - 1])
    15    970.6 MiB      0.0 MiB           1       negafibo.reverse()
    16    970.6 MiB      0.0 MiB           1       negafibo.remove(0)
    17    972.1 MiB      1.5 MiB           1       negafibo.extend(fibo)
    '''
