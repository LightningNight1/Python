# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
x1, y1 = float(input("Point A\nx1: ")), float(input("y1: "))
x2, y2 = float(input("Point B\nx2: ")), float(input("y2: "))
s = round(math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)), 2)
print(f'The distance between two points is {s}')
