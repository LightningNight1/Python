# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

with open('file_for_hw2_11.py.txt', 'r') as f:
    a = f.read().split('\n')
print(a)
my_list = []
num = int(input('Enter the number: '))
for i in range(-num, num+1):
    my_list.append((i))
print(my_list)
res = 1
for item in a:
    res *= my_list[int(item)]
print(f'The product of the elements at the specified positions is {res}')
