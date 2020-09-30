# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com


def solution():
    N = int(input())
    i = 0
    store = []
    while True:
        s = 2 ** i
        if s <= N:
            store.append(str(s))
            i += 1
        else:
            break
    print(" ".join(store))


if __name__ == "__main__":
    solution()
