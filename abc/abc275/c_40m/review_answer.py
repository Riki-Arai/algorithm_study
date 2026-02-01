import itertools

grid = [list(input()) for _ in range(9)]

points = []
for i in range(9):
    for j in range(9):
        if grid[i][j] == "#":
            points.append((i, j))

def is_square(p):
    d = []
    for a, b in itertools.combinations(p, 2):
        dx = (a[0] - b[0])
        dy = (a[1] - b[1])
        d.append(dx * dx + dy * dy)

    d.sort()
    return (
        d[0] > 0 and
        d[0] == d[1] == d[2] == d[3] and
        d[4] == d[5] == 2*d[0]
    )

ans = 0
for comb in itertools.combinations(points, 4):
    if is_square(comb):
        ans += 1

print(ans)



import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

grid_lists = [list(input()) for _ in range(9)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

res_lists = []
for i in range(9):
    for j in range(9):
        if grid_lists[i][j] == "#":
            res_lists.append((i, j))

def orth(p, q, r):
    v1x, v1y = p[0] - q[0], p[1] - q[1]
    v2x, v2y = r[0] - q[0], r[1] - q[1]
    return v1x * v2x + v1y * v2y == 0

res_set = set()
for comb in itertools.combinations(res_lists, 4):
    for p in itertools.permutations(comb):
        a = pow(p[0][0]-p[1][0], 2) + pow(p[0][1]-p[1][1], 2)
        b = pow(p[1][0]-p[2][0], 2) + pow(p[1][1]-p[2][1], 2)
        c = pow(p[2][0]-p[3][0], 2) + pow(p[2][1]-p[3][1], 2)
        d = pow(p[3][0]-p[0][0], 2) + pow(p[3][1]-p[0][1], 2)
        if a == b == c == d and orth(p[0], p[1], p[2]) and orth(p[1], p[2], p[3]) and orth(p[2], p[3], p[0]) and orth(p[3], p[0], p[1]):
            res_set.add(comb)

print(len(res_set))