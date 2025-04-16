import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て

S_list = list(input())
c_dic = Counter(S_list)
for c in c_dic:
    if c_dic[c] == 1:
        print(c)
        exit()

print(-1)