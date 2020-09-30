# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com


def solution():
    N = int(input())
    i = 1
    store = []
    while True:
        square = i ** 2
        if square <= N:
            store.append(str(square))
            i += 1
        else:
            break
    print(" ".join(store))


if __name__ == "__main__":
    solution()
