from abc import ABC, abstractmethod

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
 - для пальто (V/6.5 + 0.5),
 - для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
 - реализовать абстрактные классы для основных классов проекта,
 - проверить на практике работу декоратора @property.
"""


class AbstractClothes(ABC):
    @abstractmethod
    def calculate(self):
        pass


class Coat(AbstractClothes):
    _V: int

    def __init__(self, V: int):
        self._V = V

    @property
    def calculate(self):
        return self._V / 6.5 + 0.5


class Suit(AbstractClothes):
    _H: int

    def __init__(self, H: int):
        self._H = H

    @property
    def calculate(self):
        return 2 * self._H + 0.3


black_suit = Suit(10)
print(black_suit.calculate)

brown_coat = Coat(13)
print(brown_coat.calculate)