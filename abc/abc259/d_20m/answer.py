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
sx, sy, tx, ty = map(int, input().split())

cir_lists = []
s_list, t_list = [], []
for i in range(N):
    x, y, r = map(int, input().split())
    cir_lists.append([x, y, r])
    if pow(x-sx, 2)+pow(y-sy, 2) == pow(r, 2):
        s_list.append((i))
    if pow(x-tx, 2)+pow(y-ty, 2) == pow(r, 2):
        t_list.append((i))

dsu = DSU(N)
for i in range(N):
    for j in range(N):
        if i != j:
            x, y, r = cir_lists[i]
            xx, yy, rr = cir_lists[j]
            if pow(r-rr, 2) <= pow(x-xx, 2)+pow(y-yy, 2) <= pow(r+rr, 2):
                dsu.merge(i, j)

for s in s_list:
    for t in t_list:
        if s == t or dsu.same(s, t):
            print("Yes")
            exit()

print("No")