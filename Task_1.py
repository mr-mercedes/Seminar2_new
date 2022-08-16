# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(number):
    if number == 1:
        return 1
    else:
        return factorial(number-1) * number


def function(number):
    factorial_list = []
    for i in range(1, number + 1):
        factorial_list.append(factorial(i))

    return factorial_list


user_number = int(input('Введите число: '))
print(function(user_number))
