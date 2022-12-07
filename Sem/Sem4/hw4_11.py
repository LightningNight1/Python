# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.

import random

k = int(input('Enter the natural power of the equation: '))
ratio = []
for i in range(k + 1):
    ratio.append(random.randint(0, 100))


def create_polynomial(lst):
    res = ''
    if len(lst) < 1:
        res = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                res += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    res += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                res += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    res += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                res += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                res += ' = 0'
    return res


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


write_file('file.txt', create_polynomial(ratio))
print('The equation was written to the file')
