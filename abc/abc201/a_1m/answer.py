import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
for p in list(itertools.permutations(A_list, 3)):
    if p[2] - p[1] == p[1] - p[0]:
        print("Yes")
        exit()

print("No")