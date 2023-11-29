'''Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.'''
import random

MAX_LENGTH = 100
MIN_SIZE = 10


def binary_search(arr, num):
    less = 0
    more = len(arr) - 1
    while less <= more:
        mid = (less + more) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            less = mid + 1
        else:
            more = mid - 1
    return -1


def output(arr, num):
    result = binary_search(arr, num)
    print(f"Индекс элемента ({num}): {result}")


if __name__ == "__main__":
    integer_array = sorted(random.sample(range(MAX_LENGTH), MIN_SIZE))
    print(f"Исходный массив: {integer_array}")
    number = int(input("Введите число: "))
    output(integer_array, number)
