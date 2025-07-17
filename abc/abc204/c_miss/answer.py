import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

g_dict = defaultdict(set)
for a, b in A_lists:
    g_dict[a].add(b)

def dfs(i, j):
    if j in seen_set:
        return

    res_set.add(((i, j)))
    seen_set.add(j)
    for k in g_dict[j]:
        dfs(i, k)

res = 0
for i in range(1, N+1):
    res_set = set()
    seen_set = set()
    dfs(i, i)
    res += len(res_set)

print(res)