# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com
# zhou

def solution():
    seconds = int(input())
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60
    print(f"{h}:{m:02d}:{s:02d}")


if __name__ == "__main__":
    solution()
