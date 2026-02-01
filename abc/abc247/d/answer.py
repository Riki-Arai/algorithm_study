import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

Q = int(input())

dq = deque()
for _ in range(Q):
    input_ = input().split()
    if input_[0] == "1":
        _, x, c = input_
        dq.append([int(x), int(c)])
    else:
        _, c = input_
        c = int(c)
        res = 0
        while c:
            x, cc = dq.popleft()
            if cc > c:
                res += x*c
                dq.appendleft([x, cc-c])
                c -= c
            else:
                res += x*cc
                c -= cc
        print(res)