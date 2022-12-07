# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Enter the number N: '))


def prime_factors(num):
    first_factor = 2
    some_list = []
    while first_factor <= num:
        if num % first_factor == 0:
            some_list.append(first_factor)
            num //= first_factor
            first_factor = 2
        else:
            first_factor += 1
    print(f'Prime factors = {some_list}')


prime_factors(n)
