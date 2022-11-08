"""Выведите число π с заданной точностью. Точность
вводится пользователем в виде натурального числа.
"""


def enter():
    n = int(input("Введите натуральное число: "))
    return n

def round_pi():
    k = 1
    x = 0
    for k in range(1, 1000000):
        x = x + 4 * ((-1) ** (k + 1)) / (2 * k - 1)
    return x

def show_digit(x,n):
    print(round(x, n))

show_digit(round_pi(), enter())