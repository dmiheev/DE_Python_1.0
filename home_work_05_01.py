"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import datetime
import getpass
# Формируем красивое имя файла, пришлось погуглить :)
file_name = f"{getpass.getuser()}-{datetime.datetime.today().strftime('%Y-%m-%d')}.txt"
try:
    out_f = open(file_name, "a", encoding="utf-8")
    while True:
        new_string = input("Введите строку: ")
        if len(new_string) == 0:
            print(f"Файл {file_name} дозаписан...")
            break
        else:
            out_f.write(new_string + "\n")
except IOError:
    print("IOError!!!")
finally:
    print(f"Закроем файл {file_name}...")
    out_f.close()
