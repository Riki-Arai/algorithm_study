import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

a, b, d = map(int, input().split())

def rotate_point(x, y, angle):
    theta = math.radians(angle)
    x_new = x * math.cos(theta) - y * math.sin(theta)
    y_new = x * math.sin(theta) + y * math.cos(theta)
    return x_new, y_new

x_new, y_new = rotate_point(a, b, d)
print(x_new, y_new)