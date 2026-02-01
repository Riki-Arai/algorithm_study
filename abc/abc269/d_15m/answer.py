import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())

g_dict = defaultdict(int)
dsu = DSU(N)
for i in range(N):
    X, Y = map(int, input().split())
    g_dict[(X, Y)] = i

for k, v in g_dict.items():
    x, y = k
    for i, j in [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]:
        if (x+i, y+j) in g_dict:
            dsu.merge(v, g_dict[(x+i, y+j)])

print(len(dsu.groups()))