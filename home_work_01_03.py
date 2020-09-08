# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print("Задание №3:")
n = int(input("Введите число n: "))
nn = int(str(n) + str(n))
nnn = int(str(nn) + str(n))
result = n + nn + nnn
print("Сумма чисел n + nn + nnn = {0}".format(result))
