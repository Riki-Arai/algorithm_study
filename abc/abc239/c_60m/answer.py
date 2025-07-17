import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

x1, y1, x2, y2 = map(int, input().split())

x_lists = []
for x, y in zip([1, 1, -1, -1, 2, 2, -2, -2], [2, -2, 2, -2, 1, -1, 1, -1]):
    x_lists.append((x1+x, y1+y))

for xx, yy in x_lists:
    if pow(x2-xx, 2) + pow(y2-yy, 2) == 5:
        print("Yes")
        exit()

print("No")