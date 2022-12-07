# Вычислить число c заданной точностью d

from math import pi

d = float(input('Enter the number between 0.1 and 0.0000000001: '))


def fractional_part_len(number_to_count):
    count = 0
    while number_to_count % 1 != 0:
        number_to_count *= 10
        count += 1
    return count


if pow(10, -1) >= d >= pow(10, -10):
    new_d = fractional_part_len(d)
    print(f'At d = {d}, π = {round(pi, new_d)}')
else:
    print('Invalid value')
