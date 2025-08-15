import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

A, B, C, D = map(int, input().split()) # 取得例：1 2

def lcm(a: int, b: int) -> int:
    return abs(a*b) // math.gcd(a, b)

E = lcm(C, D)
x = (B//C)-((A-1)//C)
y = (B//D)-((A-1)//D)
z = ((B//E)-((A-1)//E))
print((B-A+1)-(x+y-z))