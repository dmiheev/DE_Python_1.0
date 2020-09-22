"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
numbers = {1: {"en": "One", "ru": "Один"},
           2: {"en": "Two", "ru": "Два"},
           3: {"en": "Three", "ru": "Три"},
           4: {"en": "Four", "ru": "Четыре"}}
new_list = []
try:
    file1 = open("text_4.txt", "r", encoding="utf-8")
    file2 = open("text_4_rus.txt", "w", encoding="utf-8")

    content = file1.readlines()

    for el in content:
        new_list.append([el.split()[0], int(el.split()[2])])

    for el in new_list:
        print(f"{numbers.get(el[1]).get('ru')} - {el[1]}", file=file2)

except IOError:
    print("IOError!!!")
finally:
    file1.close()
    file2.close()
