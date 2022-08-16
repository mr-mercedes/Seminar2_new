# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def table():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if x == 0 and y == 0 and z == 0:
                    print('\tX', '\tY', '\tZ', '\t¬(X ∧ Y) ∨ Z')
                print(f'\t{x} \t{y} \t{z} \t{int(not (x or y) and z)}')


table()
