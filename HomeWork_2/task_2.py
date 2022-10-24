""" Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z. """

def truth_table():
    counter  = 0
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                counter += 1
                print(f"{counter}. {x} | {y} | {z} | {bool(not x or y or z)}")

print("   x | y | z | ¬(X ∧ Y) ∨ Z")
truth_table()