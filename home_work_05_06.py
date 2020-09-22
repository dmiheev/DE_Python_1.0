"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from functools import reduce


def parsing_line(s):
    s = str(s)
    subject = s[:s.find(":")]
    list_num = []
    i_ = ""
    for i in s:
        try:
            i = int(i)
            i_ += str(i)
        except ValueError:
            if i_ != "":
                list_num.append(int(i_))
            i_ = ""
            continue
    hours = reduce(lambda x, y: x + y, list_num)
    return subject, hours


new_dict = {}
try:
    file = open("text_6.txt", "r", encoding="utf-8")
    content = file.readlines()
    for line in content:
        subject_val, hours_val = parsing_line(line)
        # В случае если значения по ключу есть, то будем прибавлять к ним, а не заменять
        if new_dict.get(subject_val) is not None:
            hours_val += new_dict.get(subject_val)
        new_dict.update({subject_val: hours_val})
except IOError:
    print("IOError!!!")
finally:
    file.close()

print(new_dict)
