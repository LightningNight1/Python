# 1) Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода
# данных свидетельствует пустая строка.

my_list = []
while True:
    line = input('Enter text: ')
    if not line:
        break
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open('hw5_1.py.txt', 'w') as file:
        file.writelines(my_list)
