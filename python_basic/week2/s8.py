# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com
import re

#
# def solution():
#     x = float(input())
#     p = float(input()) / 100
#     y = float(input())
#
#     def one_year(m, n):
#         interest = round((m * n), 2)
#         print("interest", interest)
#         return m + interest
#
#     year = 0
#
#     while x < y:
#         x = one_year(x, p)
#         print(x)
#         year += 1
#     print(year)


def solution():
    x = float(input())
    p = float(input()) / 100
    y = float(input())

    def one_year(m, n):
        interest = float(int(m * n * 100)) / 100
        # print("interest", interest)
        return m + interest
    year = 0
    while x < y:
        x = one_year(x, p)
        # print(x)
        year += 1
    print(year)


if __name__ == "__main__":
    solution()

