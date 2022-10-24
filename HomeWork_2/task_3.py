"""Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
«one» «onetwonine» - o – 2, n – 3, e – 2"""


# функция ввода первой строки
def input_first_string():
    first_string = input("Введите первую строку: ")
    return first_string

# функция ввода второй строки
def input_second_string():
    second_string = input("Введите вторую строку: ")
    return second_string

# функция подсчета вхождений
def include_char(first_string, second_string):

    first_array = list(first_string)
    second_array = list(second_string)

    if len(first_array) < len(second_array):
        for elem in first_array:
            print(f"{elem} - {second_array.count(elem)}")
    else:
        for elem in second_array:
            print(f"{elem} - {first_array.count(elem)}")        

# вызов метода подсчета вхождений
include_char(input_first_string(), input_second_string())