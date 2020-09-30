# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com

def solution():
    N = int(input())
    f0 = 0
    f1 = 1

    step = 0
    while f0 < N:
        f0, f1 = f1, f0 + f1
        step += 1

    if f0 == N: print(step)
    else: print(-1)


if __name__ == "__main__":
    solution()


