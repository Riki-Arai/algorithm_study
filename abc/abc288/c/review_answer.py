import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU

N, M = map(int, input().split())

res = 0
dsu = DSU(N)
for _ in range(M):
    a, b = list(map(int, input().split()))
    # 別の頂点を経由して連結済みである場合はmergeすることでサイクルができてしまうので、ここでは+1をする処理をする
    if dsu.same(a-1, b-1):
        res += 1
    else:
        dsu.merge(a-1, b-1)

print(res)