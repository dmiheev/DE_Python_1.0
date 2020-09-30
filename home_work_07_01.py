"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода__add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        if self.size == other.size:
            result = []
            numbers = []
            for row in range(self.size[0]):
                for i in range(self.size[1]):
                    sums = self.matrix[row][i] + other.matrix[row][i]
                    numbers.append(sums)
                result.append(numbers)
                numbers = []
            return Matrix(result)
        else:
            return "Складывать можно матрицы одной размерности"

    @property
    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)

        return rows, cols


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])

print(f"matrix1 = \n{matrix1}")
print(f"Размерность матрицы: {matrix1.size}\n")
print(f"matrix2 = \n{matrix2}")
print(f"Размерность матрицы: {matrix2.size}\n")
print(f"matrix1 + matrix2 =\n{matrix1 + matrix2}")
