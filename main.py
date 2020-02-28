#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Ybrayym Abamov"


# import sys


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    counter = 0
    if y < 0:
        for _ in range(abs(y)):
            counter = add(-x, counter)
    for _ in range(y):
        counter = add(x, counter)
    return counter


def power(x, n):
    """Raise x to power n, where n >= 0"""
    counter = 1
    for _ in range(n):
        counter = multiply(counter, x)
    return counter


def factorial(x):
    """Compute factorial of x, where x > 0"""
    if x <= 1:
        return 1
    else:
        for num in range(1, x):
            x = multiply(x, num)
    return x


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, add(a, b)
    return b


# def main():
#     option = sys.argv[1]
#     if option == 'add':
#         print(add(2, 4))
#     elif option == 'multiply':
#         print(multiply(6, -8))
#     elif option == 'power':
#         print(power(2, 8))
#     elif option == 'factorial':
#         print(factorial(4))


# if __name__ == '__main__':
#     main()
