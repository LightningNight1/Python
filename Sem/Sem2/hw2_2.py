# 2) Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_length = int(input('Enter the number of elements in the list: '))
my_list = []
i = 0
el = 0
while i < list_length:
    my_list.append(input('Enter the list element: '))
    i += 1
for elem in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
