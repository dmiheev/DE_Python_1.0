"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class OfficeEquipmentWarehouse:
    equipment_warehouse = {}
    equipment_to_unit = {}


class OfficeEquipment:
    def __init__(self, manufacturer, model, date):
        self.manufacturer = manufacturer
        self.model = model
        self.date = date

    @staticmethod
    def to_warehouse(param, quantity):
        try:
            item = f"{param.manufacturer} {param.model} {param.date}"
            wh_quantity = OfficeEquipmentWarehouse.equipment_warehouse[item]["Quantity"]
        except KeyError:
            wh_quantity = 0

        OfficeEquipmentWarehouse.equipment_warehouse[f"{param.manufacturer} {param.model} {param.date}"] = \
            {"Quantity": wh_quantity + quantity}

    @staticmethod
    def to_unit(param, quantity, unit):
        item = f"{param.manufacturer} {param.model} {param.date}"
        try:
            in_wh = OfficeEquipmentWarehouse.equipment_warehouse[item]["Quantity"]
        except KeyError:
            in_wh = 0
        if in_wh < quantity:
            print("На складе недостаточное количество техники")
        else:
            if in_wh - quantity == 0:
                OfficeEquipmentWarehouse.equipment_warehouse.pop(item)
            else:
                OfficeEquipmentWarehouse.equipment_warehouse[item]["Quantity"] = in_wh - quantity
            if unit not in OfficeEquipmentWarehouse.equipment_to_unit:
                OfficeEquipmentWarehouse.equipment_to_unit.update({unit: {item: {"Quantity": quantity}}})
            else:
                if item not in OfficeEquipmentWarehouse.equipment_to_unit[unit]:
                    OfficeEquipmentWarehouse.equipment_to_unit[unit].update({item: {"Quantity": quantity}})
                else:
                    quantity += OfficeEquipmentWarehouse.equipment_to_unit[unit][item]["Quantity"]
                    OfficeEquipmentWarehouse.equipment_to_unit[unit].update({item: {"Quantity": quantity}})


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, date, paper_format):
        super().__init__(manufacturer, model, date)
        self.paper_format = paper_format


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, date, color=True):
        super().__init__(manufacturer, model, date)
        self.color = color


class Xerox(OfficeEquipment):
    def __init__(self, manufacturer, model, date, resolution):
        super().__init__(manufacturer, model, date)
        self.resolution = resolution


def print_warehouse(param):
    print("\nОстатки техники на складе:")
    for i in param:
        print(f"{i} - {param[i]}")


def print_unit(param):
    print("\nОргтехника в подразделениях:")
    for i in param:
        print(f"{i} - {param[i]}")


printer_1 = Printer("HP", "ZT-435", 2017, "A4")
scanner_1 = Scanner("Samsung", "FF-43", 2019, True)
xerox_1 = Xerox("Xerox", "X-34", 2019, 600)

print(printer_1.paper_format)
print(scanner_1.color)
print(xerox_1.resolution)

OfficeEquipment.to_warehouse(printer_1, 3)
OfficeEquipment.to_warehouse(scanner_1, 3)
OfficeEquipment.to_warehouse(xerox_1, 7)
OfficeEquipment.to_warehouse(printer_1, 2)
OfficeEquipment.to_warehouse(scanner_1, 1)

print_warehouse(OfficeEquipmentWarehouse.equipment_warehouse)
OfficeEquipment.to_unit(printer_1, 2, "Sells")
OfficeEquipment.to_unit(printer_1, 1, "Ceo")
OfficeEquipment.to_unit(printer_1, 1, "Ceo")
OfficeEquipment.to_unit(xerox_1, 1, "Ceo")
OfficeEquipment.to_unit(scanner_1, 1, "Ceo")
OfficeEquipment.to_unit(printer_1, 1, "IT")

print_warehouse(OfficeEquipmentWarehouse.equipment_warehouse)
print_unit(OfficeEquipmentWarehouse.equipment_to_unit)
