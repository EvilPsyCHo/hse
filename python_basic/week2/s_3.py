# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com


def solution():
    year = int(input())
    if (year % 4) == 0:
        if (year % 100) == 0 and (year % 400) != 0:
            print("NO")
            return
        print("YES")
        return
    print("NO")


if __name__ == "__main__":
    solution()
