"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
from functools import reduce


def generate_num_list(cnt, f, t):
    res = []
    for i in range(1, cnt + 1):
        res.append(random.randint(f, t))
    return res


# Запишем в файл сгенерированные числа
with open("text_5.txt", "w", encoding="utf-8") as data:
    for el in generate_num_list(5, 1, 10):
        print(el, end=" ", file=data)


with open("text_5.txt", "r", encoding="utf-8") as data:
    new_list = list(map(int, data.readline().split()))
    print(new_list)
    print(f"Сумма чисел в файле = {reduce(lambda x,y: x + y, new_list)}")
