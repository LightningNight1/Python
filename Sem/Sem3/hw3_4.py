# 4) Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    return x ** y


print(f'Result: {my_func(5, -2)}')

##################################


def my_func(x, y):
    res = 1
    i = 1
    while i <= abs(y):
        res *= x
        i += 1
    return 1 / res


print(f'Result: {my_func(5, -2)}')
