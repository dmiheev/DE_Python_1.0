"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} тронулась...")

    def stop(self):
        print(f"Машина {self.name} остановилась...")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} = {self.speed}")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Городской автомобиль {self.name} превышает скорость!!!")
        else:
            print(f"Текущая скорость автомобиля {self.name} = {self.speed}")


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Рабочий автомобиль {self.name} превышает скорость!!!")
        else:
            print(f"Текущая скорость автомобиля {self.name} = {self.speed}")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


police = PoliceCar(120, "Черный", "Форд")
bugatti = SportCar(250, "желтый", "Бугатти")
vaz = TownCar(80, "красный", "Лада")
pochta = WorkCar(20, "синий", "Почтовый Фургон")

police.go()
police.turn("налево")
police.show_speed()

bugatti.go()
bugatti.show_speed()

vaz.go()
vaz.show_speed()
vaz.stop()

pochta.go()
pochta.turn("направо")
