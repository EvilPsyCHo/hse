# encoding: utf-8
# Author: 周知瑞
# Mail: evilpsycho42@gmail.com
from math import log


x = float(input())

if x > 0:
    print(round(log(x), 5))
else:
    print("Undefined")
