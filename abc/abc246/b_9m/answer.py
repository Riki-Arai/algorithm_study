import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

A, B = map(int, input().split())

rate = 1 / math.sqrt((pow(A, 2) + pow(B, 2)))
print(A*rate, B*rate)