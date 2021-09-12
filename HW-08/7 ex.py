"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
 и выполнив сложение и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
"""


class Complex:
    a: float
    b: float

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a1 = self.a * other.a
        a2 = self.b * other.b * -1
        #-----
        b1 = self.a * other.b
        b2 = self.b * other.a
        # -----
        a = a1 + a2
        b = b1 + b2
        return Complex(a, b)

    def __str__(self):
        if self.b < 0:
            result = '(' + str(self.a) + str(self.b) + 'i)'
        else:
            result = '(' + str(self.a) + '+' + str(self.b) + 'i)'
        return result


a = Complex(5, 12)
b = Complex(4, -15)

print(a + b)
print(a * b)
