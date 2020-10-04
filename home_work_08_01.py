"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def to_int(cls, date):
        date_list = date.split("-")
        for i in range(len(date_list)):
            try:
                date_list[i] = int(date_list[i])
            except ValueError:
                print("Ошибка!")
        return date_list

    @staticmethod
    def validate(date):
        class MyException(Exception):
            def __init__(self, txt):
                self.txt = txt

        date_list = date.split("-")
        for i in range(len(date_list)):
            try:
                date_list[i] = int(date_list[i])
                if len(date_list) > 3:
                    raise MyException("Не соответствует формату DD-MM-YYYY")
                if i == 0 and date_list[i] > 31:
                    raise MyException("День введен не правильно")
                if i == 1 and date_list[i] > 12:
                    raise MyException("Месяц введен не правильно")
                if i == 2 and date_list[i] < 1:
                    raise MyException("Год введен не правильно")
            except ValueError:
                print("Вы ввели не число!")
            except MyException as err:
                print(err)
                return False
        return True


d1 = Date("05-10-1979")
print(d1)
print(Date.to_int("05-10-1979"))
print(d1.validate("30-12-1979"))
