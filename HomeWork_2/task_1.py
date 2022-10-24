
"""Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N."""

# функция ввода числа
def input_numder():
    num = int(input("Введите число: "))
    return num

# функция расчета факториалов
def factorials(num):

    factorial = 1
    for i in range(1, num+1):
        factorial *= i
        print(factorial, end=',')
    print()    

factorials(input_numder())


