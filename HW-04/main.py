"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys
import ex1_lib

try:
    file, hours, rate, bonus = sys.argv
except ValueError:
    print("Invalid args")
    exit()

print('--- Ex 1 ---')
print(ex1_lib.calculate2(int(hours), int(rate), int(bonus)))

assert ex1_lib.calculate(10) == 8.7, "ex1_lib.calculate(10)"
assert ex1_lib.calculate2(8, 1000, 2000) == 10000, "ex1_lib.calculate2(8,1000,2000)"

# --------------------------------------------------------------------------
"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
import random

print('--- Ex 2 ---')

f_list = list(random.randint(1, 300) for x in range(0, 15))
ed_list = [x for c, x in enumerate(f_list) if c > 0 and x > f_list[c - 1]]

print(f_list)
print(ed_list)

# --------------------------------------------------------------------------
"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
print('--- Ex 3 ---')

f_list = list(x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0)

print(f_list)

# --------------------------------------------------------------------------
"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
print('--- Ex 4 ---')

f_list = list(random.randint(1, 20) for x in range(0, 15))
ed_list = [x for x in f_list if f_list.count(x) == 1]

print(f_list)
print(ed_list)

# --------------------------------------------------------------------------
"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
"""
from functools import reduce

print('--- Ex 5 ---')

f_list = list(x for x in range(100, 1001) if x % 2 == 0)
total_amount = reduce(lambda total, amount: total * amount, f_list)

print(f_list)
print(total_amount)

# --------------------------------------------------------------------------
"""
6. Реализовать два небольших скрипта:

а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from itertools import count, cycle

print('--- Ex 6 ---')


def f_gen(start):
    for num in count(start, 1):
        yield num


for i, num in enumerate(f_gen(5)):
    print(num)
    if i > 3:
        break

print('---  ---')
# --------------------------------------------------------------------------


def s_gen(list):
    for item in cycle(list):
        yield item


my_list = ['1st', '2nd', '3rd']
for i, item in enumerate(s_gen(my_list)):
    print(item)
    if i > 3:
        break



# --------------------------------------------------------------------------
"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
print('--- Ex 7 ---')


def fact(end):
    for item in range(1, end+1):
        yield reduce(lambda total, amount: total * amount, range(1, item+1))

n = 4
for el in fact(n):
    print(el)
