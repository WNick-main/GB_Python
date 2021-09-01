import json


def ex1():
    """
    1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка.
    :return:
    """
    print('--- Ex 1 ---')
    print("Введите текст. Пуста срока - выход")
    line_list = []
    while True:
        str = input()
        if str == "":
            break
        line_list.append(str + '\n')
    print(line_list)
    with open(r'ex1.txt', 'w') as my_file:
        my_file.writelines(line_list)


ex1()


def ex2():
    """
    2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
    :return:
    """
    print('--- Ex 2 ---')
    with open(r'ex2.txt', 'r') as my_file:
        lines_list = my_file.readlines()
    word_cnt = 0
    lines_cnt = 0
    for i, line in enumerate(lines_list):
        word_cnt += len(line.split())
        lines_cnt = i+1
    print(f'В файле {word_cnt} слов и {lines_cnt} строк.')



ex2()


def ex3():
    """
    3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
    величину их окладов (не менее 10 строк).
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.

    Пример файла:

    Иванов 23543.12
    Петров 13749.32
    :return:
    """
    print('--- Ex 3 ---')
    with open(r'ex3.txt', 'r', encoding='utf-8', errors='ignore') as my_file:
        data = my_file.readlines()
    user_list = []
    sum = 0
    for line in data:
        split_lines = line.split()
        user, salary = split_lines[0].strip(), float(split_lines[1].strip())
        sum += salary
        if salary < 20000:
            user_list.append(user)
    avg = sum/len(data)
    print(user_list)
    print(f'Средняя зарплата: {avg}')


ex3()


def ex4():
    """
    4. Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
    :return:
    """
    print('--- Ex 4 ---')
    num_dict={
        'One': 'Один'
        ,'Two': 'Два'
        ,'Three': 'Три'
        ,'Four': 'Четыре'
    }
    with open(r'ex4_in.txt', 'r', encoding='utf-8', errors='ignore') as inp_file:
        with open(r'ex4_out.txt', 'w') as out_file:
            for line in inp_file:
                for item, val in num_dict.items():
                    if item in line:
                        out_file.writelines(line.replace(item, val))


ex4()

import random
def ex5():
    """
    5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
    :return:
    """
    print('--- Ex 5 ---')
    num_list = list(str(random.randint(1, 20)) for x in range(0, 15))

    with open(r'ex5.txt', 'w', encoding='utf-8', errors='ignore') as my_file:
        my_file.writelines(' '.join(num_list))

    with open(r'ex5.txt', 'r') as in_file:
        num_sum = 0
        for line in in_file.readlines():
            num_sum += sum(int(x) for x in line.split())
    print(f'Результат суммы всех чисел: {num_sum}')


ex5()



def ex6():
    """
    6. Необходимо создать (не программно) текстовый файл,
    где каждая строка описывает учебный предмет и наличие лекционных,
    практических и лабораторных занятий по этому предмету и их количество.
    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести словарь на экран.

    Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —
    Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
    :return:
    """
    print('--- Ex 6 ---')
    plan = {}
    with open(r'ex6.txt', 'r', encoding='utf-8', errors='ignore') as in_file:
        h_sum = 0
        for line in in_file.readlines():
            subject, hours = line.split(':')
            for les_type in ('(л)', '(пр)', '(лаб)', '—'):
                hours = hours.replace(les_type, '').strip()
            h_sum = sum(int(x.strip()) for x in hours.split())
            plan[subject] = h_sum

    print(plan)


ex6()


def ex7():
    """
    7. Создать вручную и заполнить несколькими строками текстовый файл,
    в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.

    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
    Если фирма получила убытки, в расчет средней прибыли ее не включать.
    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.

    Пример json-объекта:

    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
    :return:
    """
    print('--- Ex 7 ---')
    firm_dict = {}
    avg_profit = [0, 0]
    with open(r'ex7.txt', 'r', encoding='utf-8', errors='ignore') as in_file:
        profit_sum = 0
        for line in in_file.readlines():
            name, form, income, cost = line.split()
            profit = float(income) - float(cost)
            if profit > 0:
                avg_profit[0] += 1
                avg_profit[1] += profit
            firm_dict[name] = profit
    result_list = [firm_dict, {'average_profit': avg_profit[1]/avg_profit[0]}]

    print(result_list)

    with open(r'ex7_out.txt', 'w') as my_file:
        json.dump(result_list, my_file)


ex7()