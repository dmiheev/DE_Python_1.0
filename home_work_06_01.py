"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора
в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""
from itertools import cycle
from time import sleep


class TrafficLight:
    __color_list = [("RED", 7), ("YELLOW", 2), ("GREEN", 10), ("YELLOW", 2)]  # Настройки смены цветов

    def __init__(self, color=None):
        self.__color = color
        print("Светофор создан...")

    def running(self):
        def out_red(text):
            print("\033[31m{}".format(text))

        def out_yellow(text):
            print("\033[33m{}".format(text))

        def out_green(text):
            print("\033[32m{}".format(text))

        color_list = self.__color_list
        print("Светофор запущен...")
        for el in cycle(color_list):
            color = el[0]
            pause = el[1]
            if color == "RED":
                out_red(f"{color} на {pause} секунд...")
            elif color == "YELLOW":
                out_yellow(f"{color} на {pause} секунд...")
            else:
                out_green(f"{color} на {pause} секунд...")
            sleep(pause)


tl = TrafficLight()
tl.running()
