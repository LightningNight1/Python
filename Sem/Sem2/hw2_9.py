# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

num = int(input('Enter the number: '))
sequence_list = {}
result = 0
for i in range(1, num + 1):
    sequence_list[i] = round(((1+1/i)**i), 2)
    result += sequence_list[i]
print(f'{sequence_list} \nsum = {round(result,2)}')
