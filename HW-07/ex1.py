"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    _matrix: []

    def __init__(self, m_list: []):
        self._matrix = m_list

    def __str__(self):
        return '\n'.join((str(list(row)) for row in self._matrix))

    def __getitem__(self, item):
        pass

    def __add__(self, other):
        if isinstance(other, Matrix):
            new_list=[]
            for i, row in enumerate(self._matrix):
                new_row = []
                for j, item in enumerate(row):
                    if i <= len(other._matrix)-1 and j <= len(other._matrix[i])-1:
                        new_row.append(item + other._matrix[i][j])
                    else:
                        new_row.append(item)
                new_list.append(new_row)
            return Matrix(new_list)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m3 = m1 + m2
print(m3)

m21 = Matrix([[10, 10], [10, 10]])
m31 = m1 + m21
print(m31)
