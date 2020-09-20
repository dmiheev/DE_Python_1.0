"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

name, virabotka, stavka, premia = argv
try:
    virabotka = int(virabotka)
    stavka = int(stavka)
    premia = int(premia)
    result = (virabotka * stavka) + premia
    print(f"Выработка:        {virabotka}")
    print(f"Ставка:           {stavka}")
    print(f"Премия:           {premia}")
    print(f"Заработная плата: {result}")
except ValueError:
    print("Ошибка ввода данных")
