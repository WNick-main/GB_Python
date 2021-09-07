"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
"""

class Cells:
    _cell_count: int

    def __init__(self,cell_count:int):
        self._cell_count = cell_count

    def __add__(self, other):
        """
        - Сложение. Объединение двух клеток.
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        """
        if isinstance(other,Cells):
            return Cells(self._cell_count + other._cell_count)

    def __sub__(self, other):
        """
         - Вычитание. Участвуют две клетки.
        Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
        иначе выводить соответствующее сообщение.
        """
        if isinstance(other, Cells):
            if self._cell_count - other._cell_count > 0:
                return Cells(self._cell_count - other._cell_count)
            else:
                print("Результат разности меньше нуля")

    def __mul__(self, other):
        """
         - Умножение. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
        """
        if isinstance(other,Cells):
            cell_count = self._cell_count * other._cell_count
            return Cells(cell_count)

    def __truediv__(self, other):
        """
         - Деление. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
        """
        if isinstance(other, Cells):
            if self._cell_count // other._cell_count > 0:
                return Cells(self._cell_count // other._cell_count)
            else:
                print("Результат деления меньше единицы")

    def __str__(self):
        return str(self._cell_count)

    def make_order(self, cells_in_row):
        """
        В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
        Данный метод позволяет организовать ячейки по рядам.
        Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
        Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
        Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
        Тогда метод make_order() вернет строку: *****\n*****\n**.
        Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
        Тогда метод make_order() вернет строку: *****\n*****\n*****.
        Подсказка: подробный список операторов для перегрузки доступен по ссылке.
        """
        rows = self._cell_count // cells_in_row
        last_row = self._cell_count % cells_in_row
        result_str = ''
        for row in range(0,rows):
            result_str += '*' * cells_in_row + '\n'
        result_str += '*' * last_row
        return result_str


cell1 = Cells(9)
cell2 = Cells(6)

print(cell1 + cell2)

print(cell1 - cell2)
print(cell2 - cell1)

print(cell1 * cell2)

print(cell1 / cell2)
print(cell2 / cell1)

cell3 = Cells(12)
print(cell3.make_order(5))

print('-------')

cell4 = cell1 + cell2
print(cell4.make_order(5))

