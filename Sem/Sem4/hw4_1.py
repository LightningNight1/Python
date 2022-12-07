# 1) Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо
# использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо
# запускать скрипт с параметрами.

from sys import argv

file_name, hrs, rate, bonus = argv
try:
    salary = int(hrs) * int(rate) + int(bonus)
    print(f"The employee's salary is {salary}")
except ValueError:
    print('Invalid value')

############################################################
try:
    hrs = int(input('Enter the number of employee hours: '))
    rate = int(input('Enter the hourly rate: '))
    bonus = int(input("Enter the employee's bonus: "))
    salary = hrs * rate + bonus
    print(f"The employee's salary is {salary}")
except ValueError:
    print('Invalid value')
