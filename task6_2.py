# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# ----------------------------------------------------------------------
# Решение №1
# xa = int(input('Введите координату X точки A: '))
# ya = int(input('Введите координату Y точки A: '))
# xb = int(input('Введите координату X точки B: '))
# yb = int(input('Введите координату Y точки B: '))

# distance = ((xb-xa)**2+(yb-ya)**2)**0.5

# print(f'расстояние между точками A и B', distance)
# ----------------------------------------------------------------------

# Решение №2. С помощью использования лямбд, filter, map, zip, enumerate, list comprehension

from functools import reduce
point_1 = list(
    map(int, input('введите координаты X и Y для точки A, через пробел: ').split()))
point_2 = list(
    map(int, input('введите координаты X и Y для точки B, через пробел: ').split()))


def distance(point_1, point_2):
    rng = reduce(lambda x, y: (x + y)**(1/2),
                 (map(lambda point: (point[1] - point[0])**2, zip(point_1, point_2))))
    return round(rng, 2)


print(f'расстояние между точками A и B = {distance(point_1, point_2)}')
