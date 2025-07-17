import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_dict = defaultdict(set)
for A_list in A_lists:
    x, y = A_list
    res_dict[x].add(y)
    res_dict[y].add(x)

res = 0
for a in range(N+1):
    for b in range(a, N+1):
        for c in range(a, N+1):
            if b in res_dict[a] and c in res_dict[b] and a in res_dict[c]:
                res += 1

print(res//2)