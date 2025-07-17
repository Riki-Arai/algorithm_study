import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())

res_dict = defaultdict(set)
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        res_dict[A].add(B)
    elif T == 2:
        res_dict[A].discard(B)
    else:
        if B in res_dict[A] and A in res_dict[B]:
            print("Yes")
        else:
            print("No")