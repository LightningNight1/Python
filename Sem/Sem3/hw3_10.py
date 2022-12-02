# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
res = ''
num = int(input('Enter the decimal to convert to binary: '))
while num != 0:
    res = str(num % 2) + res
    num //= 2
print(res)
