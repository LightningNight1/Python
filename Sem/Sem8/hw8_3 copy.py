# Задание 3. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class DivisionByZero:
    def __init__(self, dividend, divisor):
        self.divisor = dividend
        self.denominator = divisor

    @staticmethod
    def divide_by_zero(dividend, divisor):
        try:
            return (dividend / divisor)
        except:
            return '0 can never be a divisor of any number'


print(DivisionByZero.divide_by_zero(int(input('Enter dividend: ')),
                                    int(input('Enter divisor: '))))
