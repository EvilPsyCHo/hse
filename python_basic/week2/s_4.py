# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com


def solution():
    n = int(input())
    m = int(input())
    i = int(input())
    j = int(input())
    if abs(n-i) == abs(m-j):
        print("YES")
        return
    print("NO")


if __name__ == "__main__":
    solution()
