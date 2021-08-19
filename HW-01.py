# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.
var1 = 123
var2 = 'test'
var1 = 'other str'
print(var1)
user_var = input('Введите число: ')
user_var2 = input('Введите строку: ')

# print(f'Вами были введены число: {user_var} и строка {user_var2}')

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
var_time = int(input('Введите время в секундах: '))
var_h = var_time // 3600
var_m = (var_time % 3600) // 60
var_s = var_time % 60
print(f'{var_h}:{var_m}:{var_s}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
inp_num = input('Введите число: ')
result_sum = int(inp_num) + int(inp_num*2) + int(inp_num*3)
print(f'Результат суммы вида n + nn + nnn = {result_sum}')

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
inp_num = int(input('Введите число: '))
max_num = 0
while True:
    temp_num = inp_num % 10
    if max_num < temp_num:
        max_num = temp_num
    if inp_num // 10 == 0:
        break
    inp_num //= 10

print(f'Самая большая цифра в числе: {max_num}')

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
inp_income = int(input('Введите сумму выручки: '))
inp_costs = int(input('Введите сумму издержек: '))
profit = inp_income - inp_costs
if profit > 0:
    print('Ваше предприятие прибыльно')
    profitability = round((profit / inp_income) * 100)
    print(f'Рентабельность предприятия: {profitability}%')
    inp_headcount = int(input('Введите численность сотрудников: '))
    NIPE = profit / inp_headcount
    print(f'Прибыль фирмы в расчете на одного сотрудника: {NIPE}')
else:
    print('Ваше предприятие убыточно')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
#
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
inp_a = int(input('Введите результат пробежки в первый день: '))
inp_b = int(input('Введите цель для спортсмена: '))
counter = 1
distance = inp_a
while distance < inp_b:
    print(f'{counter}-й день: {distance}')
    distance += round(0.1 * distance, 2)
    counter += 1
print(f'Ответ: на {counter}-й день спортсмен достиг результата — не менее {inp_b} км.')