from datetime import datetime


# -ex1--------------------------------------------------------
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    dd = int
    mm = int
    yy = int

    def __init__(self, date_str):
        self.dd, self.mm, self.yy = Date.extract(date_str)

    @classmethod
    def extract(cls, date):
        if cls.inp_valid(date):
            return map(int, date.split('-'))
        else:
            print('Error date')
            return None, None, None

    @staticmethod
    def inp_valid(date):
        try:
            check_date = datetime.strptime(date, '%m-%d-%Y')
        except ValueError as err:
            return False
        return True


print('--- ex1 ---')
d = Date('30-02-2021')
print(d.yy)
d = Date('08-02-2021')
print(f'{d.dd}/{d.mm}/{d.yy % 100}')

# -ex2--------------------------------------------------------
"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.txt = text

    def __str__(self):
        return self.txt


def ex2():
    print('--- ex2 ---')
    a = input("Введите числитель:")
    b = input("Введите знаменатель:")
    try:
        a = int(a)
        b = int(b)
        if b == 0:
            raise MyZeroDivisionError(f"Ошибка возникла из-за деления на ноль.")
        c = a / b
    except MyZeroDivisionError as err:
        print(err)
        print('Ошибка успешно поймана')
    else:
        print(c)


# ex2()


# -ex3--------------------------------------------------------
"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
"""


class NonNumericError(Exception):
    def __init__(self, text):
        self.txt = text

    def __str__(self):
        return self.txt


def ex3():
    print('--- ex3 ---')
    print("Введите число, q - выход: ")
    my_list = []
    while True:
        inp = input()
        if inp == 'q':
            break
        try:
            if not inp.isnumeric():
                raise MyZeroDivisionError(f"Введено не число, повторите ввод./n")
        except MyZeroDivisionError as err:
            print(err)
        else:
            my_list.append(inp)
    print(my_list)


ex3()


