# 2) Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, birth_year, city, email, phone_number):
    return ' '.join([name, surname, birth_year, city, email, phone_number])


print(my_func(name='John', surname='Smith',  birth_year='1999',
              city='Moscow', email='JohnSmith3535@gmail.com', phone_number='8800555'))
