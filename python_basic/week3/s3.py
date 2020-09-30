# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com
import math

p = int(input())
x = int(input())
y = int(input())
k = int(input())


def one_year(x, y):
    s = (x + y / 100) * (p + 100) / 100
    new_x = math.floor(s)
    new_y = (math.floor(s * 100) / 100 - new_x) * 100
    return new_x, new_y


for i in range(k):
    x, y = one_year(x, y)

print(x, int(y))
