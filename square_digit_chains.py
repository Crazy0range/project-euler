"""
https://projecteuler.net/problem=92
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has
been seen before.

For example,
44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import cProfile


def sum_of_square(number):
    """
    Get sum of square of digits in a number
    :param number: The integer number
    :return: The new number
    """
    assert type(number) == int, 'Can\'t deal with none int value.'
    s = str(number)
    result = 0
    for c in s:
        d = int(c)
        result += d * d
    return result


def sum_of_square2(number):
    """
    Get sum of square of digits in a number - the faster version
    :param number: The integer number
    :return: The new number
    """
    assert type(number) == int, 'Can\'t deal with none int value.'
    r = 0
    n = number
    while n:
        s = n % 10
        r, n = r + s * s, n // 10
    return r


ten_million = 10000000


# Solution 1, brutal force, actually solvable in practical time
def solution1():
    result = 0
    for x in range(1, ten_million):
        s = x
        while s != 1 and s != 89:
            s = sum_of_square2(s)
        if s == 89:
            result += 1
    return result


# Solution 2, cache in dict

numbers_89 = {89: 0}
numbers_1 = {1: 0}


def solution2():
    result = 0
    for x in range(1, ten_million):
        s = x
        chain = []
        while s not in numbers_1 and s not in numbers_89:
            chain.append(s)
            s = sum_of_square2(s)
        if s in numbers_1:
            for e in chain:
                numbers_1[e] = 0
        else:
            for e in chain:
                numbers_89[e] = 0
            result += 1

    return result


# print solution2()

# my answer is 8581146
cProfile.run('solution2()', sort='cumtime')
