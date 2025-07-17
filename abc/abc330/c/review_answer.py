import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

D = int(input())

limit = int(math.isqrt(D))
res = float("INF")
for x in range(limit+1):
    y = math.isqrt(abs(D-x**2))
    for yy in [y-1, y, y+1]:
        res = min(abs(D-x**2-yy**2), res)

print(res)