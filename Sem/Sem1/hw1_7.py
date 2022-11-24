# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

day = int(input("Enter a number of a week's day (1 - Mon, 2 - Tue, 3 - Wed, 4 - Thu, 5 - Fri, 6 - Sat, 7 - Sun): "))
if (0 < day < 6):
    print("It's not a day off yet")
elif (5 < day < 8):
    print('Day off!')
else:
    print('Invalid value')
