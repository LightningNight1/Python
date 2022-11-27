# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Enter the number: ')


def result(num):
    if float(num) < 0:
        num = float(num) * (-1)
    number = 0
    for i in str(num):
        if i != '.':
            number += int(i)
    return number


print(f'Sum of the digits of the given number is {result(num)}')
