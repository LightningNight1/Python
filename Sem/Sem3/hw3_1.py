# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(*args):
    try:
        arg1 = int(input('Enter the integer arg1: '))
        arg2 = int(input('Enter the integer arg2: '))
        res = arg1 / arg2
    except ValueError:
        return 'Invalid value'
    except ZeroDivisionError:
        return '0 can never be a divisor of any number'
    return res


print(my_func())
