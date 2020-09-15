# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def print_string(**kwargs):
    return f"имя: {kwargs.get('first_name')}, " \
           f"фамилия: {kwargs.get('second_name')}, " \
           f"год рождения: {kwargs.get('date_of_birth')}, " \
           f"город: {kwargs.get('city')}, " \
           f"email: {kwargs.get('email')}, " \
           f"телефон: {kwargs.get('phone')}"


print(print_string(first_name="Дмитрий",
                   second_name="Михеев",
                   date_of_birth=1900,
                   city="Москва",
                   email="xxx@mail.ru",
                   phone="+79091111111"))
