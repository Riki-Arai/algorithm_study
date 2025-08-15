import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, K = map(int, input().split()) # 取得例：1 2
T_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
n_list = [i for i in range(N)]
for c in itertools.permutations(n_list, N):
    if c[0] != 0:
        break
    c_list = list(c)
    c_list.append(0)
    s = c_list[0]
    time = 0
    for n in c_list[1:]:
        time += T_lists[s][n]
        s = n

    if time == K:
        res += 1

print(res)