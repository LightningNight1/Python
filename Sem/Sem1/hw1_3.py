# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333=369.

num = input('Enter the number: ')
num2 = int(num + num)
num3 = int(num+num+num)
sum = int(num) + num2 + num3
print(f'{num} + {num2} + {num3} = {sum}')
