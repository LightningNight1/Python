# 5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

num = int(input('Enter the number: '))
my_list = [7, 5, 3, 3, 2]
c = my_list.count(num)
for element in my_list:
    if c > 0:
        i = my_list.index(num)
        my_list.insert(i+c, num)
        break
    else:
        if num > element:
            j = my_list.index(element)
            my_list.insert(j, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)
