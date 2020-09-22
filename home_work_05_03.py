"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
try:
    my_file = open("text_3.txt", "r", encoding="utf-8")
    content = my_file.readlines()
    ss = 0  # Сумма окладов
    employee_cnt = len(content)  # Количество сотрудников
    emp_list = []  # Список для сотрудников

    # Соберем список сотрудников emp_list и заодно просуммируем оклады
    for el in content:
        emp_list.append([el.split()[0], float(el.split()[1])])
        ss += float(el.split()[1])

    # С помощью генератора соберем список сотрудников с низкими окладами
    low_list = [el for el in emp_list if el[1] < 20000.0]

    print("Список сотрудников с низкими окладами:")
    for _ in low_list:
        print(_[0])

    print(f"Средний доход всех сотрудников = {ss / employee_cnt}")

except IOError:
    print("IOError!!!")
finally:
    my_file.close()
