# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(p_1, p_2, p_3):
    sorted_list = []
    if p_1 > p_2:
        sorted_list.append(p_1)
        sorted_list.append(p_2)
    else:
        sorted_list.append(p_2)
        sorted_list.append(p_1)

    if p_3 > sorted_list[0]:
        sorted_list.insert(0, p_3)
    elif p_3 < sorted_list[1]:
        sorted_list.append(p_3)
    else:
        sorted_list.insert(1, p_3)

    return sorted_list[0] + sorted_list[1]


print(my_func("qqq", "w", "z3"))
print(my_func(14, -10, -1))
print(my_func(1, 2, 5))
