# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
dict_months = {1: "зима",
               2: "зима",
               3: "весна",
               4: "весна",
               5: "весна",
               6: "лето",
               7: "лето",
               8: "весна",
               9: "осень",
               10: "осень",
               11: "осень",
               12: "зима"}
list_months = ["", "зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
while True:
    month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
    if 1 <= month <= 12:
        break
print(f"{month}-ый месяц относится к времени года {dict_months.get(month)}")
print(f"{month}-ый месяц относится к времени года {list_months[month]}")
