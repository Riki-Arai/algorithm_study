import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

R, C = map(int, input().split()) # 取得例：1 2
sy, sx = map(int, input().split()) # 取得例：1 2
gy, gx = map(int, input().split()) # 取得例：1 2

A_list = []
for i in sys.stdin:
    A_list.append(list(i.strip()))

move_dict = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}
sy -= 1
sx -= 1
gy -= 1
gx -= 1
dq = deque()
dq.append((sy, sx))
A_list[sy][sx] = 0
while len(dq):
    y, x = dq.popleft()
    for mx, my in move_dict.values():
        if 0 <= x+mx < C and 0 <= y+my < R and A_list[y+my][x+mx] == ".":
            A_list[y+my][x+mx] = A_list[y][x] + 1
            dq.append((y+my, x+mx))

print(A_list[gy][gx])