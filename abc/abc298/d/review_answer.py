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

res = 1
add_d = 0
dq = deque()
dq.append(1)
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        _, x = q
        x = int(x)
        dq.append(x)
        add_d += 1
        res = (10*res%998244353 + x%998244353)%998244353
    elif q[0] == "2":
        pop_int = dq.popleft()
        # res = divmod(res, pow(10, d, 998244353))[1]%998244353とするとWAになる（modの世界では特殊な状況以外では商を使えないらしい）
        res = res - (pop_int * pow(10, add_d, 998244353))
        add_d -= 1
    else:
        print(res%998244353)