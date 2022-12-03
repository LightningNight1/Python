# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(arg1, arg2):
    try:
        res = arg1/arg2
        return res
    except ZeroDivisionError:
        return '0 can never be a divisor of any number'


print(my_func(int(input('Enter the integer arg1: ')),
              int(input('Enter the integer arg2: '))))
