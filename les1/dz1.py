import random
from random import randint
MIN_LENGTH = -10
MAX_LENGTH = 10
MIN_SIZE = 10


def imperative(numbers):
    k = len(numbers)
    for i in range(k):
        for j in range(0, k-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def declarative(number):
    print('declarative', sorted(number, reverse=True))


if __name__ == '__main__':
    random_list = [randint(MIN_LENGTH, MAX_LENGTH) for i in range(MIN_SIZE)]
    print('random_list', random_list)

    lst = imperative(random_list)
    lst1 = lst[::-1]
    print('imperative', lst1)
    declarative(random_list)
