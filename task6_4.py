# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# ----------------------------------------------------------------------
# Решение №1
# num = int(input('Введите число N: '))
# lst = list()
# for i in range(num):
#     lst.append(i+1)
# for i in range(1, num):
#     lst[i] = lst[i-1]*lst[i]

# print(f'Произведение числе от 1 до N = {lst}')
# ----------------------------------------------------------------------

# Решение №2. С помощью использования лямбд, filter, map, zip, enumerate, list comprehension

from math import factorial
num = int(input('Введите число N: '))
print(f'Произведение числе от 1 до N = {list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,num+1))))}')