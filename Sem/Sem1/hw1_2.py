# 2) Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч: мм: сс.
# Используйте форматирование строк.

time = int(input('Enter time in seconds: '))
hour = time // 3600
minute = (time - hour * 3600) // 60
second = time - (hour * 3600 + minute * 60)
print(f'Time format HH:MM:SS -  {hour} : {minute} : {second}')
