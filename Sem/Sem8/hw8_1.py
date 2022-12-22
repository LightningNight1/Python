# Задание 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы. [[], [], []] Следующий шаг — реализовать перегрузку метода
# str() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода add() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    matrix_count = 0

    def __init__(self, param):
        self.param = param
        Matrix.matrix_count += 1

    def __str__(self):
        print(f'Matrix {Matrix.matrix_count}')
        for el in self.param:
            print(el)
        return ''

    def __add__(self, other):
        result = []
        for i in range(len(self.param)):
            matr = []
            for j in range(len(self.param[i])):
                matr.append(self.param[i][j] + other.param[i][j])
            result.append(matr)
        return Matrix(result)


list1 = [i for i in range(1, 4)]
list2 = [i for i in range(4, 7)]
list3 = [i for i in range(7, 10)]

my_matrix = [list1, list2, list3]

matrix1 = Matrix(my_matrix)
print(matrix1)
matrix2 = Matrix(my_matrix)
print(matrix2)
print('The sum of the matrices is: ')
matrix3 = matrix1 + matrix2
print(matrix3)
