# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
# величины дохода сотрудников.

with open('hw5_3.py.txt', 'r') as file:
    salary_list = []
    less_list = []
    my_list = file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            less_list.append(i[0])
        salary_list.append(i[1])
print(f'The salary less than 20k: {less_list}')
print(
    f'The average salary: {round(sum(map(float, salary_list)),3) / len(salary_list)}')
