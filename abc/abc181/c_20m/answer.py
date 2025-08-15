import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input()) # 取得例：1
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

x_list, y_list = [], []
for x, y in A_lists:
    x_list.append(x)
    y_list.append(y)

for v in Counter(x_list).values():
    if v >= 3:
        print("Yes")
        exit()

for v in Counter(y_list).values():
    if v >= 3:
        print("Yes")
        exit()

def is_linear(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

for i in range(N):
    x, y = A_lists[i]
    for j in range(i+1, N):
        xx, yy = A_lists[j]
        for k in range(j+1, N):
            xxx, yyy = A_lists[k]
            if is_linear(x, y, xx, yy, xxx, yyy):
                print("Yes")
                exit()

print("No")