# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def count_symbols(first_str, second_str):
    count = 0
    letter_dict = {}
    for i in range(len(first_str)):
        for j in range(len(second_str)):
            if j == len(second_str) - 1 and first_str[i] != second_str[j]:
                letter_dict[first_str[i]] = count
                count = 0
            elif j == len(second_str) - 1 and first_str[i] == second_str[j]:
                count += 1
                letter_dict[first_str[i]] = count
                count = 0
            elif first_str[i] == second_str[j]:
                count += 1

    return letter_dict


user_str1 = input('Введите первую строку: ')
user_str2 = input('Введите вторую строку: ')
print(count_symbols(user_str1, user_str2))
