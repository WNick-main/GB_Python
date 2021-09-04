import time


# -------------------------ex1--------------------------
class TrafficLight:
    """
    1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд,
    второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.

    Задачу можно усложнить, реализовав проверку порядка режимов,
    и при его нарушении выводить соответствующее сообщение и завершать скрипт.
    """
    __color: str

    def running(self):
        __color = 'Красный'
        print(__color)
        time.sleep(7)

        __color = 'Желтый'
        print(__color)
        time.sleep(2)

        __color = 'Зеленый'
        print(__color)
        time.sleep(5)


print('--- ex1 ---')
newTrafficLight = TrafficLight()


# newTrafficLight.running()

# -------------------------ex2--------------------------
class Road:
    """
    2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
    Значения данных атрибутов должны передаваться при создании экземпляра класса.
    Атрибуты сделать защищенными.
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
    Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
    толщиной в 1 см*число см толщины полотна.
    Проверить работу метода.

    Например: 20м*5000м*25кг*5см = 12500 т
    """
    _length: int
    _width: int
    _weight: int = 25

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calculate(self, thickness):
        result = (self._length * self._width * self._weight * thickness) / 1000
        print(f"{result} т")


print('--- ex2 ---')
m3 = Road(5000, 20)
m3.calculate(5)


# -------------------------ex3--------------------------
class Worker:
    """
    3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
    name, surname, position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
    оклад и премия, например, {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
    дохода с учетом премии (get_total_income).
    Проверить работу примера на реальных данных
    (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
    """
    name: str
    surname: str
    position: str  # Должность
    _income: {}  # (доход)

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"ФИО: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход с учетом премии: {sum(self._income.values())}")


print('--- ex3 ---')
John = Position('John', 'Dou', 'master', 25000, 10000)
print(f'{John.name} {John.surname} {John.position}')
John.get_full_name()
John.get_total_income()


# -------------------------ex4--------------------------
class Car:
    """
    4.Реализуйте базовый класс Car.
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать,
    что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

    Создайте экземпляры классов, передайте значения атрибутов.
    Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
    """
    _speed: int
    _color: str
    name: str
    _is_police: bool

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self._color = color
        self._speed = speed
        self._is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self._speed > 60:
            print('Внимание, превышение!')
        print(f'Скорость {self.name}: {self._speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self._speed > 40:
            print('Внимание, превышение!')
        print(f'Скорость {self.name}: {self._speed}')


class PoliceCar(Car):
    pass


print('--- ex4 ---')
prius = TownCar('Prius', 'Red', 80, False)
ferrari = SportCar('Ferrari', 'Yellow', 120, False)
kamaz = WorkCar('Kamaz', 'Blue', 60, False)
kitt = PoliceCar('KITT', 'Black', 200,  True)


prius.go()
ferrari.stop()
kitt.turn('направо')
kamaz.show_speed()
prius.show_speed()


# -------------------------ex5--------------------------
class Stationery:
    """
    5. Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка).
    Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов метод должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
    """
    _title: str

    def draw(self):
        print('Запуск отрисовки.')

    def __init__(self, title):
        self._title = title


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой: {self._title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом: {self._title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером: {self._title}')


print('--- ex5 ---')
red_pen = Pen('Красная ручка')
black_pencil = Pencil('Черный карандаш')
blue_handle = Handle('Синий маркер')

red_pen.draw()
black_pencil.draw()
blue_handle.draw()