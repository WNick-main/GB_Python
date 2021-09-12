import random
# -ex4--------------------------------------------------------
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class NotNumericException(Exception):
    def __init__(self, text):
        self.txt = text

    def __str__(self):
        return self.txt


class Office_equipment:
    model: str
    location: str
    resource: float

    def check_resource(self, ):
        """Проверка остаточного ресурса оборудования"""
        if self.resource == 0:
            for i, item in enumerate(Warehouse.in_stock):
                if type(self) == type(item):
                    Warehouse.send_to_department(item, self.location)
                    break
                elif i == len(Warehouse.in_stock) - 1:
                    print('Замены нет.')
            self.write_off()

    def write_off(self):
        """Спасание оборудования после исчерпания ресурса"""
        print(f'Старое оборудование {self.model} списано.')
        del self


class Warehouse:
    empty_place_left: int = 0
    in_stock: list = []
    in_departments: dict = {}

    def __init__(self, name, capacity):
        self.name = name
        self.empty_place_left = capacity
        print(f'Основан склад {self.name}')

    def purchase_equipments(self, count: int):
        """Закупка случайного оборудования"""
        try:
            if type(count) != int:
                raise NotNumericException("Количество закупаемого оборудования не может характеризоваться строкой")
        except NotNumericException as err:
            print(err)
            exit()
        buy_list = []
        for i in range(count):
            if self.empty_place_left > 0:
                new_item = random.choice([Office_printer('HP LaserJet', 10),
                                          Office_scanner('Epson Perfection', 5),
                                          Office_xerox('Kyocera ECOSYS', 8)])
                buy_list.append(new_item)
                self.empty_place_left -= 1
                print(f'Приобретен {new_item.model}')
            else:
                print(f'Нехватка места. Приобретено {i} из {count}')
                break
        self.in_stock.extend(buy_list)

    def purchase_one_equipment(self, item: Office_equipment):
        """Закупка единичного оборудования"""
        if self.empty_place_left > 0:
            self.empty_place_left -= 1
            self.in_stock.append(item)
            print(f'Приобретен {item.model}')
        else:
            print(f'Нехватка места.')

    @classmethod
    def send_to_department(cls, item: Office_equipment, department_name):
        """Отправка оборудования в подразделение"""
        item.location = department_name
        cls.empty_place_left += 1
        cls.in_stock.remove(item)
        if not cls.in_departments.get(department_name):
            cls.in_departments[department_name] = []
        cls.in_departments[department_name].append(item)
        print(f'{item.model} отправлен в {department_name}')

    def report(self):
        print(f'На складе {len(self.in_stock)} единиц оборудования:  {", ".join(item.model for item in self.in_stock)}')


class Office_printer(Office_equipment):
    print_limit: int
    print_cur: int

    def __init__(self, model, print_limit):
        self.model = model
        self.print_limit = print_limit
        self.print_cur = 0

    def print_doc(self, count):
        for i in range(count):
            if self.print_cur < self.print_limit:
                self.print_cur += 1
                self.resource = 1 - self.print_cur / self.print_limit
                print(f'Print doc {i + 1} - done')
            else:
                print('Ресурс истощен, требуется обслуживание.')
                break
        self.check_resource()


class Office_scanner(Office_equipment):
    scan_limit: int
    scan_cur: int

    def __init__(self, model, scan_limit):
        self.model = model
        self.scan_limit = scan_limit
        self.scan_cur = 0

    def scan_doc(self, count):
        for i in range(count):
            if self.scan_cur < self.scan_limit:
                self.scan_cur += 1
                self.resource = 1 - self.scan_cur / self.scan_limit
                print(f'Scan doc {i + 1} - done')
            else:
                print('Ресурс истощен, требуется обслуживание.')
                break
        self.check_resource()


class Office_xerox(Office_equipment):
    copy_limit: int
    copy_cur: int

    def __init__(self, model, copy_limit):
        self.model = model
        self.copy_limit = copy_limit
        self.copy_cur = 0

    def copy_doc(self, count):
        for i in range(count):
            if self.copy_cur < self.copy_limit:
                self.copy_cur += 1
                self.resource = 1 - self.copy_cur / self.copy_limit
                print(f'Copy doc {i + 1} - done')
            else:
                print('Ресурс истощен, требуется обслуживание.')
                break
        self.check_resource()


print('--- ex4-6 ---')
Stock = Warehouse('Main', 5)
Stock.purchase_one_equipment(Office_printer('HP LaserJet', 4))
Stock.purchase_one_equipment(Office_scanner('Epson Perfection', 5))
Stock.purchase_one_equipment(Office_xerox('Kyocera ECOSYS', 2))
Stock.report()

Stock.send_to_department(Stock.in_stock[0], 'ДРП')
Stock.send_to_department(Stock.in_stock[0], 'ФК')
Stock.send_to_department(Stock.in_stock[0], 'MIS')
Stock.purchase_equipments(2)
Stock.report()

Stock.in_departments['ДРП'][0].print_doc(10)
print('--- ---')
Stock.in_departments['ФК'][0].scan_doc(10)
print('--- ---')
Stock.in_departments['MIS'][0].copy_doc(10)
print('--- ---')

Stock.purchase_equipments('t')
