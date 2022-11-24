# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки(соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Enter the company's revenue: "))
costs = int(input("Enter the company's costs: "))
if revenue > costs:
    profit = revenue-costs
    profitability = profit/revenue
    print(f'Profit / Profitability = {profit} / {profitability} ')
    employees = int(input('Enter the number of employees: '))
    print(f'Profit per employee is {profit/employees} ')
elif revenue == costs:
    print('The revenue is equal to the cost')
else:
    print('The company is operating at a loss')
