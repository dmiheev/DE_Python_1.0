# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
print("Задание №2:")
seconds = int(input("Введите время в секундах: "))
hh = seconds // 3600
mm = (seconds % 3600) // 60
ss = seconds % 60
print("{0}:{1}:{2}".format("%02d" % hh, "%02d" % mm, "%02d" % ss))
