# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
# слов в каждой строке.

with open('hw5_1.py.txt') as file:

    line = 0
    for i in file:
        line += 1
        flag = 0
        word = 0
        for j in i:
            if j != ' ' and flag == 0:
                word += 1
                flag = 1
            elif j == ' ':
                flag = 0

        print(i, len(i.strip('\n')), 'chars,', word, 'words')
    print(f'{line} lines')
