"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json

result_list = []
firms_dict = {}
profit_dict = {}
profit_sum = 0
cnt = 0
try:
    file = open("text_7.txt", "r", encoding="utf-8")
    content = file.readlines()
    for ln in content:
        ln = ln.split()
        name = ln[0]
        profit = int(ln[2]) - int(ln[3])
        if profit > 0:
            profit_sum += profit
            cnt += 1
        firms_dict.update({name: profit})
    profit_dict.update({'average_profit': (profit_sum / cnt)})
    result_list.append(firms_dict)
    result_list.append(profit_dict)
except IOError:
    print("IOError!!!")
finally:
    file.close()

with open("text_7.json", "w", encoding="utf-8") as write_f:
    json.dump(result_list, write_f, indent=4, ensure_ascii=False)
