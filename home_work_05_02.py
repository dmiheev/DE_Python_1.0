"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from functools import reduce

try:
    my_file = open("text_2.txt", "r", encoding="utf-8")
    cnt = 0
    words_cnt = []
    content = my_file.readlines()
    print(f"Количество строк в файле: {len(content)}")
    for el in content:
        words_cnt.append(len(el.split()))
    print(f"Слов по строкам: {words_cnt}")
    print(f"Всего слов: {reduce(lambda x, y: x + y, words_cnt)}")
except IOError:
    print("IOError!!!")
finally:
    my_file.close()
