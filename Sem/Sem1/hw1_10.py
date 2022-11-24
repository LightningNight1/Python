# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x_num = int(input("Enter quarter number (1-4): "))
if x_num == 1:
    print('(x > 0 and y > 0)')
elif x_num == 2:
    print('x < 0 and y > 0')
elif x_num == 3:
    print('x < 0 and y < 0')
elif x_num == 4:
    print('x > 0 and y < 0')
else:
    print('Invalid value')
