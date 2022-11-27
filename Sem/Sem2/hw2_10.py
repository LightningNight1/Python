# Реализуйте алгоритм перемешивания списка.

import random
from random import randint
list_length = int(input('Enter the number of elements in the list: '))
my_list = []
for i in range(list_length):
    my_list.append(randint(-50, 50))
print(f'Starting List: {my_list}')
random.shuffle(my_list)
print(f'List after shuffle: {my_list}')
