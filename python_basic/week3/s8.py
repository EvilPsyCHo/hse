# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com
import math

x = input()

l1 = math.ceil(len(x) / 2)
x1 = x[:l1]
x2 = x[l1:]
y = x2 + x1

print(y)
