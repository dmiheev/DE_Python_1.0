# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func(x):
    for el in str(x):
        if ord(el) < 97 or ord(el) > 122:
            print("Строка содержит неверные символы")
            return None
    return str(x).title()


def int_func_2(z):
    res = ""
    try:
        for i in str(z).split():
            if res == "":
                res = int_func(i)
            else:
                res += " " + int_func(i)
        return res
    except TypeError:
        print("Строка содержит чтото не то")


print(int_func("hello"))
print(int_func_2("hello my name"))
