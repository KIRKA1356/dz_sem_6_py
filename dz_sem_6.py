# Задача 1

# from os import system
# system("cls")

# import function as fun

# # lines = ['abc', '45', 'bfgt', '10']
# lines = [input('Введите элемент массива:') for _ in range (fun.get_number('Введите размер списка: '))]
# num = fun.get_number('Введите число: ')
# result = list(filter(lambda x: x == str(num), lines))
# if result == []:
#     print(f'Число {num} в списке отсутствует.')
# else:
#     print(f'Число {num} есть в списке.')

# Задача 2

# from os import system
# system("cls")
# import function as fun

# number = abs(fun.get_number('Введите размер списка, это должно быть целое число: '))
# list_1 = fun.get_list(number)
# # list_1 = [2, 3, 5, 9, 3]
# result = sum([v for i, v in enumerate(list_1) if i % 2])
# print('Список элементов:\n', list_1)
# print('Сумма элементов стоящих на нечетных позициях =', result)

# Задача 3 


# from os import system
# system("cls")

# def get_point(input_string:str)->list:
#     '''
#     Получение координат точки
#     в виде списка 
#     '''
#     while True:
#         try:
#             a = input(input_string)
#             lst = list(map(int, a.split(' ')))
#             return lst
#         except ValueError:
#             print('Это не то ...')

# # a = '3 6'
# # b = '2 1'
# # a, b = list(map(int, a.split(' '))), list(map(int, b.split(' ')))

# point_a = get_point('Введите координаты точки (числа вводятся через пробел):')
# point_b = get_point('Введите координаты точки (числа вводятся через пробел):')
# result = round(sum([(j - i) ** 2 for i, j in zip(point_a, point_b)]) ** 0.5, 2)
# print('Расстояние между точками =', result)

# Задача 4

# from os import system
# system("cls")

# import function as fun


# # lines = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# # elem = 'qwe'
# lines = [input('Введите элемент массива:') for _ in range (fun.get_number('Введите размер списка: '))]
# elem = input('Введите элемент для поиска: ')
# res = [y for x, y in zip(lines, list(range(len(lines)))) if  x == elem]
# if len(res) > 1:
#     print(res[1])
# else:
#     print('Нет второго вхождения')

# Задача 5


# from os import system
# system("cls")
# import function as fun


# # list_number = [2, 3, 4, 5, 6]

# number = abs(fun.get_number('Введите размер списка, это должно быть целое число: '))
# list_number = fun.get_list(number)
# print('Исходный список:\n', list_number)
# len_num = len(list_number) // 2 + len(list_number) % 2
# l_1, l_2 = list_number[:len_num], list_number[-1:len_num-2:-1]
# list_result = list(x*y for x, y in zip(l_1, l_2))
# print('Список произведений пар чисел:\n', list_result)

# Задача 6
# from os import system
# system("cls")
# import function as fun

# # num = 5
# num = abs(fun.get_number('Введите число для создания последовательности: '))
# list_num = list((-3) ** x for x in range(num))
# print(list_num)