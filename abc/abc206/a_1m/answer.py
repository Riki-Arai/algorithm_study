import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

N = int(input())
res = math.floor(N*1.08)
if res < 206:
    print("Yay!")
elif res == 206:
    print("so-so")
else:
    print(":(")