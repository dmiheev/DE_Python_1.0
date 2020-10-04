"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


def my_division(x, y):
    class MyException(Exception):
        def __init__(self, txt):
            self.txt = txt

    try:
        x = int(x)
        y = int(y)
        if y == 0:
            raise MyException("На ноль делить нельзя!")
    except ValueError:
        return "Введено не число!"
    except MyException as err:
        return err
    else:
        return x / y


print(my_division(5, 2))
print(my_division(5, 0))
print(my_division("Hello", 2))
