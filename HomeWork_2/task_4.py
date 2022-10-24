"""Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
3 -> [2, 3, -3, -2, -1, 0, 1]"""


# функция ввода числа
def input_numder():
    num = int(input("Введите число: "))
    return num

# функция получения и сдвига элементов массива на 2 вправо
def shift_array(n):
    shift_array = [] 
    for i in range(-n, n+1):
        shift_array.append(i)
    shift_array = shift_array[-2:] + shift_array[:-2]
    return shift_array


print(shift_array(input_numder()))