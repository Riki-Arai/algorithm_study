import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

from sys import setrecursionlimit
setrecursionlimit(10**7)

N, M = map(int,input().split())

g_dict = defaultdict(list)
for _ in range(M):
    a, b, c = map(int,input().split())
    g_dict[a].append({b:c})
    g_dict[b].append({a:c})