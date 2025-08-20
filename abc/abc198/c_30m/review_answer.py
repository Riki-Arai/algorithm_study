import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

R, X, Y = map(int, input().split())

g_dis = math.sqrt(pow(X, 2) + pow(Y, 2))
r_dis = math.sqrt(R*R)
if g_dis % r_dis == 0:
    print(int(g_dis//r_dis))
elif g_dis-2*r_dis < 0:
    print(2)
else:
    print(int(2 + ((g_dis-2*r_dis)//r_dis) + 1))