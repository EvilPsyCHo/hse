# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com
import math

x = float(input())
y = float(input())
z = float(input())
p = (x + y + z) / 2
s = math.sqrt(p*(p-x)*(p-y)*(p-z))
print(round(s, 5))
