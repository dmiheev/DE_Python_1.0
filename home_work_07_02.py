"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate(self):
        pass


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def calculate(self):
        return 2 * self.H + 0.3


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def calculate(self):
        return self.V / 6.5 + 0.5


suit = Suit(1.76)
print(f"Ткани для пошива костюма необходимо {suit.calculate} м.кв.")

coat = Coat(52)
print(f"Ткани для пошива пальто необходимо {coat.calculate} м.кв.")
