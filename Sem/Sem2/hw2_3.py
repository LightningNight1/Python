# 3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

seasons_list = ['spring', 'summer', 'autumn', 'winter']
seasons_dict = {1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter'}
month = int(input('Enter month number (1-12): '))
if 2 < month < 6:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif 5 < month < 9:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif 8 < month < 12:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif 0 < month < 3 or month == 12:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print('Invalid value')
