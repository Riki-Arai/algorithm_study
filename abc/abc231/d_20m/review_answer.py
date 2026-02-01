import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

g_dict = defaultdict(int)
dsu = DSU(N)
for _ in range(M):
    A, B = map(int, input().split())
    dsu.merge(A-1, B-1)
    g_dict[A-1] += 1
    g_dict[B-1] += 1

for g in dsu.groups():
    # 1つのグループであればどこにでも接続できるので無視して問題ない
    if len(g) == 1:
        continue
    o_e, t_e = 0, 0
    for gg in g:
        if g_dict[gg] == 1:
            o_e += 1
        elif g_dict[gg] == 2:
            t_e += 1

    # グラフが直線であるかどうかを判定
    if not (o_e == 2 and t_e == len(g)-2):
        print("No")
        exit()

print("Yes")