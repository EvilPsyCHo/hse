# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com


def solution():
    n = int(input())

    # def recursion(x):
    #     if x == 0: return 0
    #     elif x == 1: return 1
    #     else:
    #         return recursion(x-1) + recursion(x-2)

    def recurrence(x):
        x1 = 0
        x2 = 1
        for i in range(x):
            x1, x2 = x2, x1+x2
        return x1

    print(recurrence(n))


if __name__ == "__main__":
    solution()
