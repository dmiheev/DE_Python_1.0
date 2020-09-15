# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def func_division(p_1=(input("A: ")), p_2=(input("B: "))):
    try:
        a = float(p_1)
        b = float(p_2)
        res = a / b
        print(f"A / B = {res}")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except ValueError:
        print("Введено не число")


func_division()
