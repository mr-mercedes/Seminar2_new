# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def create_list(number):
    new_list = []
    for i in range(-number, number + 1):
        new_list.append(i)

    return new_list


def hyper_push_list(some_list, number_of_push):
    push_number = number_of_push
    new_list = []
    for i in range(-push_number, len(some_list) - push_number):
        new_list.append(some_list[i])

    return new_list


user_number = int(input('Введите число: '))
user_push = int(input('Введите размер сдвига: '))
my_list = create_list(user_number)

print(f'Начальный список -> {my_list} <-')
print(f'Новый список -> {hyper_push_list(my_list, user_push)} <- сдвинутый на {user_push} элемент{"ов" if user_push > 4 else "а"}')

