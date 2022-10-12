import time

"""Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели."""


week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

day_number = int(input("Для получения дня недели введите его номер (от до 7): "))

print(f"Это - {week_days[day_number - 1]}!", end=' ')
if day_number > 6: print("Ура! Выходной!")
print('\n')

#####################################################################################################################################

time.sleep(1)

"""Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве."""

import math

a = [int(elem) for elem in input("Введите через пробел координаты X и Y точки A: ").split()]
b = [int(elem) for elem in input("Введите через пробел координаты X и Y точки B: ").split()]

# AB = √(xb - xa)2 + (yb - ya)2
distance = round(math.sqrt((math.pow(b[0] - a[0], 2) + math.pow(b[1] - a[1], 2))), 2)

print(f"Расстояние между точками в 2D пространстве: {distance}")
print()

#####################################################################################################################################

time.sleep(1)

"""Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)."""

time.sleep(1)

quarter =  int(input("Введите номер четверти плоскости: "))

coordinates = {1 : "x > 0, y > 0", 2 : "x < 0, y > 0", 3 : "x < 0, y < 0", 4 : "x > 0, y < 0"}

print(f"Четверти принадлежат координаты: {coordinates[quarter]}")
print()

#####################################################################################################################################

time.sleep(1)

"""Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N."""


n = int(input("Введите максимальное число больше 0: "))

counter = 0

while counter <= n:
    if counter % 2 == 0:
        print(counter, end=', ')
    counter += 1