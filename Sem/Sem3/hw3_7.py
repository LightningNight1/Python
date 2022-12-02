# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

my_list = [2, 3, 5, 9, 3]
my_sum = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        my_sum += my_list[i]
print(f'The sum of values of odd index positions: {my_sum}')
