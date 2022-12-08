# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
# подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open('hw5_5.py.txt', 'w+') as file:
        set_nums = input('Enter numbers separated by a space: ')
        file.writelines(set_nums)
        nums = set_nums.split()
        print(f'The sum of the numbers is {sum(map(int, nums))}')
except ValueError:
    print('Invalid value')
