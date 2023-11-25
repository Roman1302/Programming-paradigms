import math
from random import randint

MIN_LENGTH = 0
MAX_LENGTH = 10
MIN_SIZE = 10

def meaning(array):
    return sum(array) / float(len(array))


def correlation(x, y):
    x_m = meaning(x)
    y_m = meaning(y)
    numerator = sum((xi - x_m) * (yi - y_m) for xi, yi in zip(x, y))
    denominator = math.sqrt(sum((xi - x_m) ** 2 for xi in x) * sum((yi - y_m) ** 2 for yi in y))

    return round(numerator / denominator, 2)


def interpret(index):
    if index > 0.9:
        a_i = 'весьма высокая'
    elif 0.9 >= index > 0.7:
        a_i = 'высокая'
    elif 0.7 >= index > 0.5:
        a_i = 'заметная'
    elif 0.5 >= index > 0.3:
        a_i = 'умеренная'
    else:
        a_i = 'слабая'

    return a_i


x = [randint(MIN_LENGTH, MAX_LENGTH) for i in range(MIN_SIZE)]
y = [randint(MIN_LENGTH, MAX_LENGTH) for i in range(MIN_SIZE)]
# x = [1, 2, 3, 4, 4]
# y = [1, 2, 3, 4, 3]

# проверим
print('x = ', x)
print('y = ', y)
print(f"Корреляция X & Y по Пирсону: {correlation(x, y), interpret(correlation(x, y))}")
