# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

sum_res = 0
ex = False
while ex == False:
    num = input(
        'Enter numbers separated by a space or "q" to quit: ').split()
    res = 0
    for el in range(len(num)):
        if num[el] == 'q' or num[el] == 'Q':
            ex = True
            break
        else:
            res = res + int(num[el])
    sum_res = sum_res + res
    print(f'Result: {sum_res}')
