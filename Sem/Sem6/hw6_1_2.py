from timeit import timeit

print(timeit("my_func()", setup="from hw6_1 import my_func"))
print(timeit("my_func1()", setup="from hw6_1 import my_func"))
