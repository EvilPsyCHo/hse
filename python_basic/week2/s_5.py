# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com


def solution():
    k = int(input())
    m = int(input())
    n = int(input())
    nl = n % k
    if nl != 0:
        print(((n // k) + 1) * m * 2)
    else:
        print((n // k) * m * 2)


if __name__ == "__main__":
    solution()
