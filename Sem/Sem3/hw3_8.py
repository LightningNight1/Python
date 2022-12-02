# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и
#  предпоследний и т.д.

my_list = [2, 3, 4, 5, 6]
i = 0
mid_product = 0
product = []
while i < len(my_list)/2:
    mid_product = my_list[i] * my_list[-i-1]
    product.append(mid_product)
    i += 1
print('Product of pairs of numbers in the list:', product)
