# Задание 3. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input('Enter dividend: ')
divisor = input('Enter divisor: ')

try:
    dividend = int(dividend)
    divisor = int(divisor)

    if divisor == 0:
        raise DivisionByZero('0 can never be a divisor of any number')
    result = dividend / divisor
except ValueError:
    print('Invalid value')
except DivisionByZero as err:
    print(err)
else:
    print(f'{divisor} / {dividend} = {result}')
