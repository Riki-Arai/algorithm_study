import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

grid_lists = [list(input().strip()) for _ in range(9)]

p_lists = []
for i in range(9):
    for j in range(9):
        if grid_lists[i][j] == "#":
            p_lists.append((i, j))

def is_square(c):
    res_list = []
    for cc in it.combinations(c, 2):
        r, c = cc[0]
        rr, cc= cc[1]
        res_list.append(pow(abs(r-rr), 2) + pow(abs(c-cc), 2))
    res_list.sort()
    return res_list[0] >= 0 and res_list[0] == res_list[1] == res_list[2] == res_list[3] and 2*res_list[0] == res_list[-2] and 2*res_list[0] == res_list[-1]

res = 0
for c in it.combinations(p_lists, 4):
    if is_square(c):
        res += 1

print(res)