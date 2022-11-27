# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Enter the number: '))
product = 1
for i in range(num):
    i = i + 1
    product = i * product
    print(product, end=' ')
