# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = 8
fibo = [0, 1]
negafibo = [0, 1]
for i in range(2, k + 1):
    fibo.append(fibo[i - 1] + fibo[i - 2])
    negafibo.append(negafibo[i - 2] - negafibo[i - 1])
negafibo.reverse()
negafibo.remove(0)
negafibo.extend(fibo)
print('K-Fibonacci series for K =', k, ' \n', negafibo)
